# P4 — Projectile Motion Simulation with Drag: Complete Study Guide

**Source:** Notion → Engineering Refreshers — Summer 2026 → Physics → P4
**Objective:** Refresh Newtonian mechanics and numerical ODE methods by implementing a projectile motion simulation with aerodynamic drag and comparing it against the analytic ideal case.

This guide has three parts:
- **Part I — Classical Mechanics & Physics Fundamentals**
- **Part II — ODE Formulation, solve_ivp Mechanics, and Numerical Accuracy**
- **Part III — Python Implementation, Plotting, and Deliverable Structure**

Read Part I first if physics is rusty, Part II if numerical methods are rusty, Part III when ready to write code.

---

# PART I — CLASSICAL MECHANICS & PHYSICS FUNDAMENTALS


**Audience:** Engineer/scientist with prior exposure to Newtonian mechanics, refreshing rusty first-principles knowledge before implementation.
**Purpose:** Rebuild the physics foundation (kinematics, forces, dimensional reasoning) needed to correctly formulate the drag-augmented projectile ODE system. Numerical integration methods and Python/plotting are covered in companion documents.
**Format:** Dense reference — derivations, worked numbers, and "why" explanations, not a tutorial.

---

## Quick Lookup

| You're trying to... | Go to |
|---|---|
| Recall the no-drag range/height/time formulas | §1 |
| Prove why 45° is optimal only in the ideal case | §1.4 |
| Get the drag force formula and its direction | §2 |
| Decide if you need Stokes (linear) or quadratic drag | §2.2–2.3 |
| Write the coupled ODEs for vx, vy with drag | §3 |
| Explain (to yourself or a reviewer) why optimal angle < 45° with drag | §4 |
| Check if terminal velocity is relevant here | §5 |
| Sanity-check units in your code | §6 |
| Get realistic numbers for a baseball-scale test case | §7 |

---

## Table of Contents

1. Ideal (No-Drag) Projectile Motion
2. Drag Force Physics
3. Newton's Second Law with Drag — Component ODEs
4. Physical Intuition: Why Drag Reduces Range and Shifts Optimal Angle
5. Terminal Velocity — Relevance and Non-Relevance
6. Dimensional Analysis Checklist
7. Sanity-Check Numbers (Baseball-Scale Example)

---

## 1. Ideal (No-Drag) Projectile Motion

### 1.1 Setup

Launch from origin (x0=y0=0) at speed `v0`, angle `theta` above horizontal, uniform gravitational field `g` pointing in `-y`. No air resistance means the only force is gravity: `F = (0, -mg)`.

Initial velocity components:
$$
v_{x0} = v_0 \cos\theta, \qquad v_{y0} = v_0 \sin\theta
$$

### 1.2 Equations of Motion (analytic)

Acceleration is constant: $a_x = 0$, $a_y = -g$. Integrate twice:

$$
v_x(t) = v_0\cos\theta \quad \text{(constant — no horizontal force)}, \qquad v_y(t) = v_0\sin\theta - gt
$$
$$
x(t) = v_0\cos\theta \cdot t, \qquad y(t) = v_0\sin\theta \cdot t - \tfrac{1}{2}gt^2
$$

This is the textbook decoupling: horizontal motion is uniform velocity, vertical motion is uniform acceleration. The two axes are **independent** in the ideal case — this independence is exactly what drag destroys (see §3), because drag couples $v_x$ and $v_y$ through the speed term $v = \sqrt{v_x^2+v_y^2}$.

### 1.3 Time of Flight, Range, Max Height

**Time of flight** (return to $y=0$, flat ground, same launch/landing height): solve $y(t)=0$ for nonzero $t$:
$$
0 = v_0\sin\theta \cdot t - \tfrac{1}{2}gt^2 \quad\Longrightarrow\quad t_{\text{flight}} = \frac{2v_0\sin\theta}{g}
$$

**Range** (x at $t_{\text{flight}}$):
$$
R = v_{x0}\, t_{\text{flight}} = v_0\cos\theta \cdot \frac{2v_0\sin\theta}{g} = \frac{v_0^2}{g}\bigl(2\sin\theta\cos\theta\bigr) = \frac{v_0^2}{g}\sin(2\theta)
$$
(double-angle identity: $2\sin\theta\cos\theta = \sin 2\theta$)

**Max height** (at $t = t_{\text{flight}}/2$, where $v_y = 0$):
$$
t_{\text{apex}} = \frac{v_0\sin\theta}{g}, \qquad
H_{\max} = v_0\sin\theta \cdot t_{\text{apex}} - \tfrac{1}{2}g\,t_{\text{apex}}^2 = \frac{v_0^2\sin^2\theta}{2g}
$$

### 1.4 Proof: Range Maximized at Exactly 45°

$R(\theta) = \dfrac{v_0^2}{g}\sin(2\theta)$. Since $v_0^2/g$ is a fixed positive constant for a given launch speed, maximizing $R$ is equivalent to maximizing $\sin(2\theta)$ over $\theta \in [0°, 90°]$.

$$
\frac{dR}{d\theta} = \frac{v_0^2}{g}\cdot 2\cos(2\theta) = 0 \quad\Longrightarrow\quad \cos(2\theta) = 0 \quad\Longrightarrow\quad 2\theta = 90° \quad\Longrightarrow\quad \theta = 45°
$$

Second derivative:
$$
\frac{d^2R}{d\theta^2} = -4\frac{v_0^2}{g}\sin(2\theta)
$$
which at $\theta=45°$ gives $\sin(90°)=1>0$, so $\dfrac{d^2R}{d\theta^2}<0$ — confirms a **maximum** (not minimum/inflection).

Equivalent symmetry argument (no calculus): $\sin(2\theta) = \sin(180° - 2\theta)$, so $R(\theta) = R(90°-\theta)$ — e.g., 30° and 60° give identical ranges. The function is symmetric about 45°, and since $\sin$ peaks at argument 90° (i.e., $2\theta = 90°$), 45° is the unique interior maximum. **This symmetry is destroyed by drag** — with drag, $R(\theta) \neq R(90°-\theta)$, which is why the optimal angle shifts (§4).

### 1.5 Trajectory Shape

Eliminating $t$ from $x(t), y(t)$ gives the parabola:
$$
y(x) = x\tan\theta - \frac{g x^2}{2v_0^2\cos^2\theta}
$$
Useful for a quick "does my numerical trajectory look parabolic when I zero out drag" sanity check — with drag, the trajectory becomes asymmetric (steeper descent than ascent), not a true parabola.

---

## 2. Drag Force Physics

### 2.1 The Drag Equation

$$
F_{\text{drag}} = \tfrac{1}{2}\rho C_d A v^2
$$
where:
- $\rho$ = fluid (air) density, kg/m³ (1.225 at sea level, 15°C)
- $C_d$ = drag coefficient, dimensionless, shape/orientation-dependent (0.47 for a smooth sphere in the subcritical regime)
- $A$ = reference cross-sectional area, m² (for a sphere, $A = \pi r^2$)
- $v$ = speed (magnitude of velocity vector), m/s

**Direction:** drag always opposes the *velocity vector*, not any fixed axis. As a vector:
$$
\vec{F}_{\text{drag}} = -\tfrac{1}{2}\rho C_d A\, v\, \vec{v}
$$
Note $\vec{v}$ (not unit vector alone) times $v$ reproduces the $v^2$ magnitude while preserving direction — i.e. $\vec{F}_{\text{drag}} = -\tfrac{1}{2}\rho C_d A\,|\vec{v}|\,\vec{v}$. Written via the unit vector $\hat{v} = \vec{v}/|\vec{v}|$:
$$
\vec{F}_{\text{drag}} = -\tfrac{1}{2}\rho C_d A v^2 \,\hat{v}
$$
Both forms are algebraically identical; the second is what you'll decompose into components in §3.

### 2.2 Quadratic vs Linear (Stokes) Drag

Two idealized drag regimes exist depending on Reynolds number $Re = \dfrac{\rho v D}{\mu}$ ($D$ = characteristic length/diameter, $\mu$ = dynamic viscosity of air $\approx 1.81\times10^{-5}$ Pa·s):

- **Linear (Stokes) drag**, $F = -bv$ ($b$ constant): valid at **low Re** ($Re \ll 1$), where viscous forces dominate over inertial forces — e.g., dust particles, micro-organisms, droplets settling slowly. Derived from Stokes' law for a sphere: $b = 6\pi\mu r$.
- **Quadratic drag**, $F = -\tfrac{1}{2}\rho C_d A v^2$ (this problem): valid at **high Re** ($Re \sim 10^3$–$10^5$, "subcritical" regime), where inertial forces dominate and the flow sheds turbulent eddies (a von Kármán vortex street) — momentum transfer scales with $v^2$ because both the mass flux of displaced air *and* the velocity imparted to it scale with $v$.

### 2.3 Why Quadratic Drag Applies Here

For a projectile like a baseball or similar sphere at typical launch speeds (10–50 m/s), diameter ~0.07 m:
$$
Re = \frac{\rho v D}{\mu} \approx \frac{1.225 \times 30 \times 0.07}{1.81\times10^{-5}} \approx 1.4\times10^{5}
$$
This lands solidly in the **quadratic drag regime** (Re >> 1000), justifying `C_d ≈ 0.47` (the standard subcritical smooth-sphere value; note C_d actually *drops* sharply near Re ~ 3×10^5, the "drag crisis," due to boundary layer transition — not relevant unless modeling very high speeds/large objects, but worth knowing C_d isn't truly constant in reality). For this problem, treat `C_d` as a given constant per the problem statement — that's the standard simplifying assumption.

**Common Mistake:** Assuming linear (Stokes) drag applies to "small" projectiles by analogy with fluids problems from intro courses (e.g., ball bearings in oil). The regime depends on Reynolds number, not just object size — a small fast sphere in air is still quadratic-regime; a small slow sphere in a viscous fluid is Stokes-regime. Don't default to linear drag just because the object is small.

---

## 3. Newton's Second Law with Drag — Component ODEs

### 3.1 Force Balance

Two forces act: gravity (constant, downward) and drag (opposing velocity, magnitude $\propto v^2$):
$$
m\frac{d\vec{v}}{dt} = (0, -mg) + \vec{F}_{\text{drag}}
$$

### 3.2 Decomposing Drag into Components

Let $v_x, v_y$ be velocity components, $v = \sqrt{v_x^2+v_y^2}$ the speed. The unit vector opposing velocity is $(-v_x/v, -v_y/v)$. Substituting into $\vec{F}_{\text{drag}} = -\tfrac{1}{2}\rho C_d A v^2\,\hat{v}$:

$$
F_{\text{drag},x} = -\tfrac{1}{2}\rho C_d A v^2 \left(\frac{v_x}{v}\right) = -\tfrac{1}{2}\rho C_d A\, v\, v_x
$$
$$
F_{\text{drag},y} = -\tfrac{1}{2}\rho C_d A v^2 \left(\frac{v_y}{v}\right) = -\tfrac{1}{2}\rho C_d A\, v\, v_y
$$
(the $v^2\cdot(v_x/v) = v\,v_x$ simplification is the key algebraic step — each component drag force scales with $v$ times *that* component, not $v$ alone or the component squared)

### 3.3 Full Coupled ODE System

Define the drag coefficient lump $k = \dfrac{\rho C_d A}{2m}$ (units $1/\text{m}$, see §6) for brevity:

$$
\frac{dx}{dt} = v_x, \qquad \frac{dy}{dt} = v_y
$$
$$
\frac{dv_x}{dt} = -k\,v\,v_x, \qquad \frac{dv_y}{dt} = -g - k\,v\,v_y, \qquad v = \sqrt{v_x^2+v_y^2}
$$

**This is the system you hand to your numerical ODE solver.** Key structural points to carry into the numerical-methods work:
- It's a first-order system in 4 state variables $(x, y, v_x, v_y)$ — reduce the 2nd-order Newton's law to first-order form exactly as done here before integrating.
- $v$ couples $v_x$ and $v_y$ nonlinearly (no closed-form solution exists in general — this is *why* numerical integration is needed at all; contrast with the ideal case's clean analytic solution in §1).
- Initial conditions: $x(0)=y(0)=0$, $v_x(0)=v_0\cos\theta$, $v_y(0)=v_0\sin\theta$ — identical to the ideal case; only the dynamics differ.

**Common Mistake:** Writing $\dfrac{dv_x}{dt} = -k v_x^2$ (dropping the $v$ factor and squaring only $v_x$). This is wrong — it decouples the axes again and silently reduces to two independent 1-D quadratic-drag problems, which is *not* physically what quadratic drag does in 2D. The coupling through $v = \sqrt{v_x^2+v_y^2}$ is the entire physical point of vector drag.

**Common Mistake:** Forgetting the sign — both drag components are always *negative* relative to their own velocity component's sign (opposing motion), so if `vy` goes negative during descent, `-k*v*vy` becomes *positive* (drag now decelerates the downward fall, i.e., points upward). Don't hardcode drag as "always downward" or "always subtracted" — it's always opposite to the *current* velocity vector, which changes direction over the flight.

---

## 4. Physical Intuition: Why Drag Reduces Range and Shifts Optimal Angle Below 45°

### 4.1 Why Range Decreases

Drag removes kinetic energy throughout flight (it does negative work along the entire path, `W = ∫F_drag · ds < 0` always, since drag opposes velocity by construction). Two effects compound:
1. **Horizontal velocity continuously decays** (unlike the ideal case where `vx` is constant) — so the projectile covers less horizontal distance per unit time as flight progresses.
2. **Time of flight itself changes** — drag on the vertical component means the ascent is "braked" by drag (reducing peak height and thus shortening hang time) while descent is also braked (drag opposes falling too, so terminal-velocity-like effects can partially offset shortened hang time) — net effect is almost always shorter or equal flight time and always less horizontal distance covered per second, so range drops substantially, often by 20-50%+ for typical sports projectiles at high speed.

### 4.2 Why Optimal Angle < 45° with Drag

This is the qualitative result students most often mis-remember (sometimes guessing it goes *up*). Reasoning:

- **Higher angle → more time aloft → more cumulative horizontal drag exposure.** A steep launch spends more time in the air, during which horizontal velocity is continuously being eroded by drag (since `dvx/dt = -k*v*vx`, always acting whenever vx>0). Longer flight time compounds this loss.
- **Lower angle → higher initial vx, less time for drag to act on it, but less time-of-flight altogether limits range too.** There's a genuine tradeoff between "high angle = long hang time but decaying vx" versus "low angle = fast but brief flight."
- The **ideal-case optimum (45°) was a balance point between height/hang-time and horizontal speed** assuming vx never decays. Once vx decays over time, the marginal benefit of extra hang time (from a higher angle) is worth less than it was in vacuum, because that extra time is spent carrying a *decaying* horizontal velocity rather than a constant one. The optimizer therefore shifts toward **lower angles that front-load horizontal distance while it's least degraded**, trading off some height/hang-time.
- Quantitatively, for typical sports-ball drag magnitudes, optimal angle is often in the **30-40° range** rather than 45°, and the effect becomes more pronounced as the drag parameter `k*v0` grows (i.e., higher speed or larger `C_d*A/m` — lighter, draggier objects at higher speed shift the optimum lower).

**When to use this reasoning:** when validating your simulation output — if your drag-augmented range-vs-angle sweep peaks at 45° or above, that's a red flag your drag terms aren't actually being applied (check §3's common mistakes first).

---

## 5. Terminal Velocity — Relevance and Non-Relevance

**Definition:** terminal velocity $v_{\text{term}}$ is the speed at which drag force equals gravitational force in magnitude, for an object falling straight down with no other forces — i.e., $dv/dt = 0$ in pure vertical free-fall:
$$
mg = \tfrac{1}{2}\rho C_d A\, v_{\text{term}}^2 \quad\Longrightarrow\quad v_{\text{term}} = \sqrt{\frac{2mg}{\rho C_d A}}
$$

**Relevance to P4:** Terminal velocity is a useful **sanity-check bound and intuition anchor**, not a quantity you solve for directly in the 2D trajectory ODE. Two uses:
1. **Order-of-magnitude check:** if your simulated `vy` during descent asymptotically approaches a value close to `-v_term` for a sufficiently long/high trajectory, that's a good numerical sanity check that your drag ODE is behaving correctly (the ODE should naturally reproduce this limiting behavior — you don't need to hardcode it).
2. **Regime awareness:** if `v0` is much less than `v_term`, drag effects on the trajectory will be comparatively minor (near-ideal case); if `v0` approaches or exceeds `v_term`, drag dominates strongly and you should expect large deviations from the analytic solution.

**Why it's *not* directly usable here:** terminal velocity as classically defined assumes **pure vertical motion** (vx=0). In the 2D trajectory, `vx` is never exactly zero during flight (except possibly momentarily near apex if there were no horizontal component at all), so the coupled speed `v = sqrt(vx^2+vy^2)` appearing in the actual ODEs is not simply `vy` — you cannot substitute the 1D terminal velocity formula into the 2D equations. Only use it as an external check value, computed once, and compare against your simulated `vy` trend qualitatively.

**Common Mistake:** Trying to non-dimensionalize the whole trajectory using `v_term` as if the projectile actually reaches strict vertical free-fall — valid only in the limit of a very high, very long drop with negligible horizontal velocity remaining, not during the bulk of a projectile's flight.

---

## 6. Dimensional Analysis Checklist

Verify every equation resolves to consistent SI units before trusting your implementation.

| Quantity | Symbol | SI Units |
|---|---|---|
| Position | $x, y$ | m |
| Velocity | $v_x, v_y, v_0, v$ | m/s |
| Acceleration | $g$ | m/s² |
| Mass | $m$ | kg |
| Density | $\rho$ | kg/m³ |
| Area | $A$ | m² |
| Drag coefficient | $C_d$ | dimensionless |
| Force | $F$ | N = kg·m/s² |
| Time | $t$ | s |
| Angle | $\theta$ | degrees (convert to radians before any trig call in code) |

**Check $F_{\text{drag}}$:**
$$
[\rho][C_d][A][v^2] = \left(\frac{\text{kg}}{\text{m}^3}\right)(1)(\text{m}^2)\left(\frac{\text{m}^2}{\text{s}^2}\right) = \frac{\text{kg}\cdot\text{m}}{\text{s}^2} = \text{N} \quad\checkmark \text{ matches force}
$$

**Check $k = \dfrac{\rho C_d A}{2m}$:**
$$
[k] = \frac{\text{kg}/\text{m}^3 \cdot \text{m}^2}{\text{kg}} = \frac{1}{\text{m}}
$$
So $k\,v\,v_x$ has units $\dfrac{1}{\text{m}}\cdot\dfrac{\text{m}}{\text{s}}\cdot\dfrac{\text{m}}{\text{s}} = \dfrac{\text{m}}{\text{s}^2}$ — correctly an acceleration, matching $dv_x/dt$. ✓ This is a good quick check to run mentally any time you touch the ODE right-hand side.

**Check range formula:** $R = v_0^2\sin(2\theta)/g \rightarrow (\text{m/s})^2/(\text{m/s}^2) = \text{m}$ ✓
**Check time of flight:** $t = 2v_0\sin\theta/g \rightarrow (\text{m/s})/(\text{m/s}^2) = \text{s}$ ✓
**Check max height:** $H = v_0^2\sin^2\theta/(2g) \rightarrow (\text{m/s})^2/(\text{m/s}^2) = \text{m}$ ✓
**Check terminal velocity:** $v_{\text{term}} = \sqrt{2mg/(\rho C_d A)} \rightarrow \sqrt{\text{kg}\cdot\text{m/s}^2 / (\text{kg}/\text{m}^3\cdot\text{m}^2)} = \sqrt{\text{m}^2/\text{s}^2} = \text{m/s}$ ✓

**Common Mistake:** Passing `theta` in degrees directly into `sin()`/`cos()` in code (most languages' math libraries expect radians) — always convert (`theta_rad = theta_deg * pi/180`) once at the top and use `theta_rad` everywhere downstream, including inside the ODE if angle-dependent terms appear (they typically only appear in initial conditions, not in the ODE right-hand side itself, since the ODE is expressed in vx, vy directly).

---

## 7. Sanity-Check Numbers (Baseball-Scale Example)

Use these representative values to eyeball whether your simulation output is "in the right ballpark" (pun intended) before trusting more exotic parameter sweeps.

**Regulation baseball parameters:**
$$
m = 0.145\text{ kg}, \quad D = 0.074\text{ m (diameter)} \Rightarrow r = 0.037\text{ m}
$$
$$
A = \pi r^2 = \pi(0.037)^2 \approx 0.0043\text{ m}^2 \quad \text{(problem statement uses ~0.0042, consistent)}
$$
$$
C_d = 0.47, \qquad \rho = 1.225\text{ kg/m}^3, \qquad g = 9.81\text{ m/s}^2
$$

**Example launch:** $v_0 = 40$ m/s (~90 mph, a hard-hit ball), $\theta = 45°$.

**Ideal (no drag) case:**
$$
t_{\text{flight}} = \frac{2(40)\sin 45°}{9.81} \approx 5.77\text{ s}, \qquad
R = \frac{40^2\sin 90°}{9.81} \approx 163.1\text{ m}, \qquad
H_{\max} = \frac{40^2\sin^2 45°}{2(9.81)} \approx 40.8\text{ m}
$$

**Drag parameter check:**
$$
k = \frac{1}{2}\cdot\frac{1.225\cdot0.47\cdot0.0043}{0.145} \approx 0.0086\text{ m}^{-1}
$$
At $v_0=40$ m/s, the drag deceleration scale is $k v_0^2 \approx 0.0086\cdot1600 \approx 13.7\text{ m/s}^2$ — comparable to $g$ itself (9.81 m/s²), confirming drag is **not negligible** at this speed; expect significant deviation from the ideal trajectory (this matches real-world baseball physics, where actual home-run distances are dramatically less than the ideal-vacuum prediction of ~163 m — real fly balls at this speed travel roughly 90-120 m depending on angle/spin, which is the kind of order-of-magnitude reduction, ~30-45%, you should see once your ODE is running correctly).

**Terminal velocity check (bound, not a target):**
$$
v_{\text{term}} = \sqrt{\frac{2(0.145)(9.81)}{1.225\cdot0.47\cdot0.0043}} \approx \sqrt{\frac{2.848}{0.00248}} \approx \sqrt{1149} \approx 33.9\text{ m/s}
$$
Since $v_0 = 40$ m/s $> v_{\text{term}} \approx 34$ m/s, this projectile is launched *faster* than its own terminal velocity — expect substantial early-flight deceleration from drag (v decays quickly from 40 toward the 30s range before the trajectory dynamics settle), reinforcing that drag effects will be visually obvious in this example, not a subtle correction.

**Expected qualitative simulation result for this example:** drag-augmented range noticeably less than 163 m (likely ~90-115 m range depending on exact numeric integration), optimal angle for this ball/speed combo shifting to roughly 35-40° instead of 45° (per §4.2), and a visibly asymmetric trajectory (steeper, faster descent than ascent) when plotted against the ideal parabola.

**Common Mistake:** Using SI-consistent but unrealistic toy numbers (e.g., A=1 m^2 with m=0.1 kg) "just to test the code," which can produce absurd results (near-instant deceleration to near-zero velocity) that are hard to sanity-check against intuition. Prefer physically realistic parameter sets like the baseball example above for initial debugging, then generalize.


---

# PART II — ODE FORMULATION, SOLVE_IVP MECHANICS, AND NUMERICAL ACCURACY

## Projectile Motion with Drag: ODE Formulation, solve_ivp, and Convergence

**Audience:** Engineer refreshing rusty numerical methods / computational physics knowledge before implementing.
**Purpose:** Cover the ODE-system formulation, `scipy.integrate.solve_ivp` mechanics, quadratic drag vector derivation, and numerical-vs-analytic accuracy considerations needed for P4. Mechanics fundamentals and Python/plotting are covered in companion documents.
**Format:** Dense reference — concept, worked example, common mistakes, cross-references.

---

## Quick Lookup

| Situation | What to use / do |
|---|---|
| Need to solve a 2nd-order Newtonian ODE numerically | Convert to first-order system with state vector `[x, y, vx, vy]` (Section 1) |
| Choosing an integrator in `solve_ivp` | `RK45` (default, adaptive, good general-purpose explicit method) unless stiff — drag projectile is non-stiff, RK45 is correct choice |
| Need to stop integration when `y` hits ground | Use `events=` with a terminal event function, not a manual loop (Section 2.3) |
| Drag force direction | Always opposes velocity vector — decompose using `|v|` times component, not component squared (Section 3) |
| Comparing numeric vs analytic trajectories | Check `rtol`/`atol`, check event-detected landing time precision, don't just eyeball the plot (Section 4) |
| Sweeping over launch angle for range-optimization | Loop over theta, re-run `solve_ivp` per angle, extract `t_events`/`y_events` x-coordinate (Section 2.3, 4) |

---

## Table of Contents

1. First-Order ODE System Formulation
2. `scipy.integrate.solve_ivp` Mechanics
   - 2.1 Signature and required structure
   - 2.2 RK45 method
   - 2.3 Event handling (terminal, direction)
   - 2.4 Tolerances (`rtol`, `atol`) and step control
3. Quadratic Drag Physics Derivation
4. Numerical vs Analytic Accuracy and Convergence

---

## 1. First-Order ODE System Formulation

**Principle.** Any n-th order ODE (or system of them) can be rewritten as a first-order system by introducing auxiliary variables for every derivative below the highest order. `solve_ivp` (like virtually all general-purpose ODE solvers) only accepts first-order systems of the form:

$$
\frac{dY}{dt} = f(t, Y), \qquad Y(t_0) = Y_0
$$

where $Y$ is a state vector, not a single scalar function.

**Derivation for projectile motion.** Newton's second law gives two coupled 2nd-order ODEs:

$$
m\frac{d^2x}{dt^2} = F_x\!\left(x, y, \frac{dx}{dt}, \frac{dy}{dt}\right), \qquad
m\frac{d^2y}{dt^2} = F_y\!\left(x, y, \frac{dx}{dt}, \frac{dy}{dt}\right) - mg
$$

Each 2nd-order equation splits into two 1st-order equations by defining velocity as a new state variable:

$$
Y = \begin{bmatrix} x \\ y \\ v_x \\ v_y \end{bmatrix}, \qquad
\frac{dY}{dt} = \begin{bmatrix} v_x \\ v_y \\ -\frac{k}{m} v_x |v| \\ -g - \frac{k}{m} v_y |v| \end{bmatrix}
$$

where $k = \tfrac{1}{2}\rho C_d A$, $\;|v| = \sqrt{v_x^2+v_y^2}$

This is the exact system named in the problem statement. Note the ordering convention: position components first, then velocity components — this is arbitrary but must be **consistent** between your `deriv(t, Y)` function, your initial condition array, and how you unpack the solution afterward (`sol.y[0]` = x, `sol.y[1]` = y, etc., if you keep this order).

**Why this works generally.** The trick is always: for every derivative you need but don't have an explicit equation for (here, `dx/dt` and `dy/dt` themselves), you promote it to a state variable and supply its trivial defining equation (`dx/dt = vx`). The "physics" only enters in the equations for the *highest-order* derivatives (here, the acceleration equations).

**Worked example — building `deriv`.**
```python
def deriv(t, Y, k, m, g):
    x, y, vx, vy = Y
    v = np.hypot(vx, vy)          # |v| = sqrt(vx^2 + vy^2)
    ax = -(k/m) * vx * v
    ay = -g - (k/m) * vy * v
    return [vx, vy, ax, ay]
```

**Common Mistakes**
- Forgetting that `deriv` must return `d(state)/dt` in the *same order* as the state vector — a transposed or misordered return breaks the integration silently (no error, just wrong physics).
- Writing `ax = -(k/m) * vx**2` instead of `-(k/m) * vx * v` — this drops the vector nature of drag (see Section 3); it's the single most common conceptual bug in this exact problem.
- Treating `g` as a signed vs unsigned quantity inconsistently — decide once that `g = 9.81` (positive scalar) and always write `-g` in the `dvy/dt` equation, don't fold the sign into `g` itself elsewhere in the code.
- Not extracting extra parameters (`k, m, g`) via `args=` in `solve_ivp` and instead hardcoding them as globals inside `deriv` — works but breaks reusability for the angle-sweep in step 5.

**Cross-reference:** The `k/m` factor and `|v|` term are derived from the drag force law in Section 3. The ideal (no-drag) analytic case is the same system with `k = 0`, which decouples `vx` (constant) from `vy` (linear in `t`) — this is the closed-form check used in Section 4.

---

## 2. `scipy.integrate.solve_ivp` Mechanics

### 2.1 Signature and required structure

```python
scipy.integrate.solve_ivp(
    fun,                # callable: fun(t, y, *args) -> dy/dt, shape matches y
    t_span,             # (t0, tf): integration interval (tf can be a generous upper bound)
    y0,                 # initial state vector, array-like
    method='RK45',      # integrator
    t_eval=None,        # optional array of times at which to store solution (for smooth plotting)
    events=None,        # callable(s) for root-finding during integration
    args=None,          # extra positional args passed to fun and events
    dense_output=False, # if True, returns a continuous interpolant (sol.sol(t))
    rtol=1e-3, atol=1e-6  # default tolerances — often too loose for this problem, see 2.4
)
```

Returns a `OdeResult` (`Bunch`) object: `sol.t` (times), `sol.y` (state array, shape `(n_states, n_times)`), `sol.t_events`, `sol.y_events`, `sol.status`, `sol.success`.

**Key structural point:** `y0` must be a flat 1D array-like matching the order used inside `fun`. For this problem: `y0 = [0, 0, v0*cos(theta), v0*sin(theta)]`.

### 2.2 RK45 method

RK45 = explicit Runge-Kutta of order 5(4) — specifically the Dormand-Prince pair. Mechanics:
- At each step, computes **two** Runge-Kutta estimates of different order (4th and 5th) using the same function evaluations (an "embedded" pair).
- The **difference** between the 4th- and 5th-order estimates is used as a local error estimate, without extra derivative evaluations beyond what's needed for the 5th-order solution.
- Step size is **adaptive**: if the error estimate exceeds tolerance, the step is rejected and retried with a smaller `h`; if error is comfortably within tolerance, the next step size is increased.
- This is why you don't manually choose a fixed `dt` — RK45 self-tunes step size to hit the requested tolerance, taking large steps where the trajectory is smooth (e.g., near apex) and small steps where it changes rapidly (e.g., steep dives near impact with strong drag).

**When to use this vs alternatives:**
- `RK45`: default choice for smooth, non-stiff ODEs — correct for this problem (drag projectile ODEs are smooth and non-stiff over normal parameter ranges).
- `RK23`: lower order, use only if you need speed over accuracy and the problem is very smooth.
- `Radau`, `BDF`, `LSODA`: implicit / stiff solvers — needed only if the system has widely separated timescales causing explicit methods to require absurdly tiny steps for stability (not the case here; only relevant if e.g. you added extremely strong restoring forces or very small mass with very large drag coefficient — worth knowing as a distinguishing signal for stiffness elsewhere in your career, but not applicable to P4 as scoped).

### 2.3 Event handling (terminal, direction)

To stop "when `y` returns to 0," you do **not** manually poll `sol.y[1]` in a loop and truncate. `solve_ivp` has built-in root-finding for this via `events`.

**Event function contract:**
```python
def hit_ground(t, Y, k, m, g):
    return Y[1]          # y-position; the solver finds t where this crosses zero
hit_ground.terminal = True    # stop integration when this event fires
hit_ground.direction = -1     # only trigger on downward crossing (y decreasing through 0)
```

Pass via `events=hit_ground` (or a list of event functions) to `solve_ivp`. Internally, the solver:
1. Detects a sign change in the event function's value between consecutive accepted steps.
2. Uses dense output / interpolation plus a root-finder (Brent's method, effectively) to locate the precise time `t_event` within the step where the function crosses zero — this is *far* more accurate than just taking whatever step happened to land near `y=0`.
3. If `terminal=True`, integration halts right after that event, and `sol.t_events[0][0]` / `sol.y_events[0][0]` give the precise impact time and full state at impact (giving you exact landing `x`, and impact velocity components for free — useful for range calculations and "range reduction" annotations in Plot 1).

**`direction` attribute:** without setting `direction = -1`, the event would also fire at `t=0` (launch, where `y=0` too, if launching from ground level) potentially causing an immediate false stop, depending on solver internals and initial value handling. Setting `direction = -1` restricts triggering to *downward* zero-crossings only, which is the physically meaningful "landing" event. (Some implementations are robust to the `t=0` edge case regardless because the event is checked only at t > t0, but explicitly setting `direction` is the defensive, correct habit.)

**Worked example — full stopping-at-landing pattern:**
```python
def hit_ground(t, Y, k, m, g):
    return Y[1]
hit_ground.terminal = True
hit_ground.direction = -1

sol = solve_ivp(deriv, (0, 100), y0, method='RK45',
                 args=(k, m, g), events=hit_ground,
                 dense_output=True, rtol=1e-8, atol=1e-10)

t_land = sol.t_events[0][0]
x_land, y_land, vx_land, vy_land = sol.y_events[0][0]
```
Note `t_span=(0, 100)` here is a deliberately generous upper bound — the event will terminate integration long before `t=100` for realistic projectile parameters; it exists only as a safety cap in case parameters are pathological (e.g., launching straight up with such extreme drag it never seems to come down within a reasonable numerical window).

**Common Mistakes**
- Forgetting `hit_ground.terminal = True` — the solver will detect and record the event but keep integrating (and may detect it again spuriously, or run to `t_span[1]` uselessly).
- Omitting `direction = -1` when launching from `y=0` — can cause immediate spurious termination at `t≈0` in some edge cases, or double-counts events if the trajectory has any upward jitter near y=0 numerically.
- Using `t_eval` and `events` together and then reading `sol.y[:, -1]` as "the landing state" — `t_eval` does **not** automatically include the exact event time unless it happens to coincide; always use `sol.y_events` / `sol.t_events` for the precise landing state, not the last column of `sol.y`.
- For the angle-sweep (step 5), forgetting to re-instantiate/reset the event function's mutable attributes if reusing the same function object across many `solve_ivp` calls in unusual ways — generally safe if you don't reassign `.terminal`/`.direction` mid-loop, but be aware these are function attributes, not fresh per call.

### 2.4 Tolerances (`rtol`, `atol`) and step control

- `rtol` (relative tolerance) and `atol` (absolute tolerance) jointly define the acceptable local error per component: roughly `error <= atol + rtol * |y|`.
- Defaults (`rtol=1e-3, atol=1e-6`) are tuned for generic robustness, not precision — for this problem, where you want a **clean, visually smooth trajectory and an accurate range comparison against an analytic ideal**, tighten to something like `rtol=1e-8, atol=1e-10`. The cost is more function evaluations (smaller adaptive steps), which is irrelevant for a 2-body-free-fall-scale ODE (runs in milliseconds regardless).
- Loose tolerances manifest as: visibly polygonal/kinked trajectory plots, event-detected landing point that doesn't match the visually-obvious x-intercept, or angle-sweep range curves with visible noise/jitter instead of a smooth curve — a *diagnostic tell* that tolerances are too loose, distinct from an actual modeling error.
- `max_step` parameter can also be capped explicitly (e.g., `max_step=0.01`) as a blunter alternative to tightening `rtol`/`atol`, but this defeats the point of adaptive stepping (uniformly small steps everywhere, even where unnecessary) — prefer tolerance tightening.

**When to use this:** Always err toward tighter tolerances than default when the output feeds a *quantitative comparison* (range difference, optimal angle) rather than just a qualitative plot. Loose defaults are fine for quick-look diagnostic plots only.

---

## 3. Quadratic Drag Physics Derivation

**Why drag scales as v² (not v or v³).** For a bluff body moving through a fluid at moderate-to-high Reynolds number (turbulent regime, which describes typical human-scale projectiles: baseballs, cannonballs, sports projectiles at normal speeds), the dominant resistance mechanism is *inertial* (form) drag: the body must continuously accelerate a volume of fluid out of its path. The momentum imparted to displaced fluid per unit time scales as:

$$
\text{(fluid density)} \times \text{(area swept per unit time)} \times \text{(velocity imparted to fluid)} \;\sim\; \rho (Av) v = \rho A v^2
$$

This is a dimensional/scaling argument (not a full Navier-Stokes derivation) — full derivation requires solving for the pressure distribution over the body, which depends on body shape and boundary-layer separation. That shape-and-separation-dependent proportionality constant is exactly what $C_d$ (drag coefficient) captures. The standard form:

$$
F_{\text{drag}} = \tfrac{1}{2}\rho C_d A v^2
$$

The factor of $\tfrac{1}{2}$ is a historical/dynamic-pressure convention (dynamic pressure $q = \tfrac{1}{2}\rho v^2$ is the natural pressure scale from Bernoulli's equation), folded into the definition of $C_d$ so that $C_d$ comes out as a clean $O(1)$ dimensionless number for common shapes (sphere ≈ 0.47, as given).

**Vector decomposition — why $|v|$ multiplies each component, not $v_x^2$ / $v_y^2$ directly.**

Drag is defined as a scalar magnitude formula, $F_{\text{drag}} = \tfrac{1}{2}\rho C_d A v^2$ where $v = |\vec v|$ is speed (always positive, direction-less). But drag is physically a **vector** that always points exactly opposite to the velocity vector (it's a resistive force, by definition anti-parallel to motion). To turn the scalar magnitude into a vector force, multiply by the unit vector opposing velocity:

$$
\vec F_{\text{drag}} = -F_{\text{drag}}\left(\frac{\vec v}{|\vec v|}\right) = -\tfrac{1}{2}\rho C_d A |\vec v|^2 \left(\frac{\vec v}{|\vec v|}\right) = -\tfrac{1}{2}\rho C_d A\,|\vec v|\,\vec v
$$

Note the $|\vec v|^2$ and the $1/|\vec v|$ from the unit vector combine to leave a single factor of $|\vec v|$, multiplying the full vector $\vec v = (v_x, v_y)$. Component-wise:

$$
F_{\text{drag},x} = -\tfrac{1}{2}\rho C_d A\,|v|\,v_x, \qquad F_{\text{drag},y} = -\tfrac{1}{2}\rho C_d A\,|v|\,v_y
$$

This is **why** the ODE has $v_x|v|$ and $v_y|v|$ rather than $v_x^2$ and $v_y^2$:
- $v_x^2$ is always positive regardless of the sign of $v_x$ — it would produce a drag force that doesn't correctly reverse direction as $v_x$ changes sign (e.g., on the descending/backward-blown part of an unusual trajectory), and would have the wrong units of directionality entirely (it discards the sign information that tells you which way drag should push).
- $v_x|v|$ correctly carries the sign of $v_x$ (drag on the x-component acts opposite to whatever direction $v_x$ currently points) while $|v|$ supplies the correct $v^2$ magnitude scaling using the *total* speed (both components contribute to the "how fast is this body plowing through air" magnitude, even though we're resolving the force separately per axis).

This is a classic subtlety: drag magnitude depends on total speed `|v|`, but drag direction depends on each component's own sign — you cannot decompose "F ∝ v²" component-wise as `F_x ∝ v_x²` because that discards direction; you must decompose the *vector* equation `F_vec = -k|v|v_vec`, which is component-wise linear in each `v_i` but modulated by the *scalar* total speed `|v|`.

**Common Mistakes**
- Writing `ax = -(k/m) * vx * abs(vx)` (using `|vx|` instead of `|v|`) — this decouples the axes incorrectly; drag magnitude must depend on total speed, not each axis independently. This gives numerically different (wrong) trajectories especially for high launch angles where `vy >> vx` or vice versa.
- Confusing `Cd` values by shape — 0.47 is specifically for a sphere at typical Reynolds numbers; don't assume it's a universal constant if generalizing the exercise to other body shapes later.
- Sign errors: since `k/m * vx * |v|` is already negative when combined with the leading minus sign in the derivative equation and `vx`/`vy` can each be positive or negative, double check the *net* sign behaves as "opposes current motion" for all four quadrants of `(vx, vy)`, not just the launch quadrant (vx>0, vy>0).

**Cross-reference:** This vector form is exactly the acceleration term appearing in the state-derivative equations in Section 1; `k = (1/2) rho Cd A` is defined once and reused there and in Section 2's `deriv` function.

---

## 4. Numerical vs Analytic Accuracy and Convergence

**Analytic (no-drag) baseline.** With $k=0$, the ODE system decouples and integrates in closed form:
$$
x(t) = v_0\cos\theta \cdot t, \qquad y(t) = v_0\sin\theta \cdot t - \tfrac{1}{2}gt^2
$$
Time of flight: $T = 2v_0\sin\theta/g$. Range: $R = v_0^2\sin(2\theta)/g$, maximized at $\theta=45°$ (classic result, independent of $v_0$, $m$, in vacuum).

**Why this matters as a convergence check:** the analytic solution is not just "the other case to plot" — it's your **ground truth for validating the numerical machinery itself**. Before trusting the drag-case numbers, verify that running your same `solve_ivp` setup with `k` forced to 0 reproduces the closed-form `R`, `T`, and trajectory shape to many decimal places. If it doesn't, the bug is in your integration setup (event handling, state ordering, tolerance), not in the drag physics — isolate these independently.

**Convergence considerations specific to this problem:**
1. **Event-time precision dominates range error more than step-size precision.** Because range is read off at the event-detected landing point, the accuracy of `x_land` depends on how precisely `solve_ivp`'s internal root-finder locates `t` where `y=0`, which in turn depends on the tolerance of the dense-output interpolant used for root-finding — tightening `rtol`/`atol` improves this directly.
2. **Angle-sweep smoothness as a convergence diagnostic.** When sweeping theta from 1-89 degrees (step 5) to find max range, plot the resulting `R(theta)` curve — with adequately tight tolerances, this should be smooth and allow clean identification of the maximum (via `argmax` on a fine grid, or a subsequent local optimization / parabola-fit refinement around the coarse maximum). Visible jaggedness in this curve is a tolerance artifact, not real physics — real physics (drag) produces a *smooth* shift of the optimum below 45°, not noise.
3. **Why optimal angle drops below 45° with drag.** Physical intuition to sanity-check your numeric result against: drag penalizes high speed and long flight time; steeper angles (closer to 90°) spend more time at high speed fighting gravity and more total path length exposed to drag, while flatter trajectories reduce time-of-flight. The drag-optimal angle is typically in the 30-40° range depending on the drag-to-weight ratio (`k*v0 / (m*g)`-type dimensionless grouping) — if your numeric sweep gives something wildly outside this range (e.g., still 45°, or below 20°), suspect a bug (likely the `|v|` vs squared-component bug from Section 3, or units mismatch between `theta` in degrees vs radians in `cos`/`sin` calls).
4. **Degrees vs radians is the single most common silent numerical bug in this exact exercise** — `theta` is specified as an input in degrees (per Instruction 1) but `np.cos`/`np.sin` require radians; forgetting `np.radians(theta)` conversion produces a full trajectory that runs and plots without error but is physically nonsensical (and won't match the analytic 45°-max sanity check), which is precisely why doing the analytic-case cross-check first is valuable — it will immediately expose this class of bug.
5. **Global vs local error accumulation.** RK45's adaptive stepping controls *local* per-step error to within tolerance, but *global* error (accumulated over the whole trajectory) can still grow, especially over long integration times or near-singular dynamics. For this problem (finite flight time, smooth non-stiff dynamics, terminal event well before any long-time drift could accumulate) this is a second-order concern — tight `rtol`/`atol` as in Section 2.4 is sufficient — but it's worth knowing the distinction (local per-step control ≠ guaranteed global accuracy) for other problems where integration time is unbounded or dynamics are chaotic.

**When to use dense_output vs t_eval for plotting:** `dense_output=True` gives a continuous interpolant `sol.sol(t)` you can evaluate at an arbitrary fine grid *after* solving — better for smooth plots regardless of what adaptive step points were actually used internally. `t_eval=np.linspace(0, t_guess, N)` forces the solver to also report values at specified times but does not change the internal adaptive stepping; use `dense_output` if you don't know landing time in advance (typical here, since it depends on the event) and want a smooth curve after the fact.

**Common Mistakes**
- Comparing numeric-with-drag range against analytic-no-drag range and calling the entire difference "numerical error" — it's overwhelmingly a *physical* difference (drag reduces range), not solver error; only the sub-component you'd validate against the k=0 analytic check (Section 4, item 2 above) isolates true numerical error.
- Using default tolerances for the main run but tight tolerances only for the validation check — always match tolerance settings between the validation run and the production run, or you haven't actually validated anything.
- Reporting "range reduction" (Instruction 4) using `sol.y[:, -1]` instead of `sol.y_events` — introduces spurious error from whatever the last integration step happened to be, not the true event-refined landing point.

**Cross-reference:** The `k=0` degenerate case validation strategy directly reuses the ODE system and `deriv`/event-handling code from Sections 1 and 2 — no separate code path should be needed, just parameterize `k` and confirm both regimes run through identical machinery.

---

*End of ODE/numerical-methods section. See companion documents for (a) mechanics/physics fundamentals (Newton's laws, kinematics, force diagrams) and (b) Python/matplotlib implementation and plotting conventions.*


---

# PART III — PYTHON IMPLEMENTATION, PLOTTING, AND DELIVERABLE STRUCTURE


**Audience**: Engineer refreshing scipy/matplotlib fluency after time away from daily numerical Python work. Newtonian mechanics and ODE theory are assumed/covered elsewhere — this section is purely about *how to write the code*.

**Purpose**: Bridge from "I know what `solve_ivp` does conceptually" to "I can write the exact call, event function, extraction, and plotting code for P4 without re-deriving API details from docs."

**Format**: Reference sections with runnable code fragments, a Quick Lookup table for API decisions, and Common Mistakes callouts calibrated to errors an experienced-but-rusty programmer actually makes (not syntax typos).

---

## Quick Lookup

| You're trying to... | Use | See section |
|---|---|---|
| Stop integration when projectile lands | `events=` param + terminal event function | §1.3 |
| Get x(t), y(t), vx(t), vy(t) arrays out of the solver | `sol.y[0], sol.y[1], sol.y[2], sol.y[3]` | §2 |
| Get the exact landing time/state (not just last step) | `sol.t_events[0]`, `sol.y_events[0]` | §2.2 |
| Get smooth interpolated curve for plotting | `dense_output=True` + `sol.sol(t_fine)` | §2.3 |
| Plot two trajectories with landing markers + annotation | `ax.plot` x2, `ax.scatter`, `ax.annotate` | §3 |
| Sweep launch angle 1-89° for range curve | Python loop calling `solve_ivp` per angle (not vectorized) | §4 |
| Find optimal drag angle | `np.argmax` on the range array (sufficient; `scipy.optimize` is overkill for 1° resolution) | §4.2 |
| Avoid infinite/runaway integration | Set generous but finite `t_span` upper bound + rely on terminal event | §1.4, §6 |

---

## Table of Contents

1. Structuring the `solve_ivp` call
2. Extracting results from `OdeResult`
3. Matplotlib patterns for the trajectory plot
4. Building the angle-sweep loop
5. Script organization / deliverable structure
6. Common Pitfalls (consolidated)

---

## 1. Structuring the `solve_ivp` Call

### 1.1 The state vector and derivative function

`solve_ivp` integrates a first-order ODE system `dy/dt = f(t, y)`. For P4 the state vector is 4-dimensional:

```python
y = [x, y_pos, vx, vy]
```

The derivative function must have signature `f(t, y) -> array-like of same length`, even though `t` doesn't explicitly appear in the drag equations (it's still a required positional argument — `solve_ivp` always calls `fun(t, y)`).

```python
def projectile_ode(t, state, m, Cd, A, rho, g=9.81):
    """
    Derivative function for drag-affected projectile motion.
    state = [x, y, vx, vy]
    Returns [dx/dt, dy/dt, dvx/dt, dvy/dt].
    """
    x, y_pos, vx, vy = state
    v = np.hypot(vx, vy)                    # |v| = sqrt(vx^2+vy^2)
    k = 0.5 * rho * Cd * A / m               # drag coefficient lumped constant
    dxdt = vx
    dydt = vy
    dvxdt = -k * v * vx
    dvydt = -g - k * v * vy
    return [dxdt, dydt, dvxdt, dvydt]
```

Note the lumped constant `k = rho*Cd*A/(2m)` — computing it once per call (or once outside and passing in) avoids recomputing `rho*Cd*A` repeatedly; harmless at this scale but a good habit for larger sweeps (§4).

Extra parameters (`m, Cd, A, rho, g`) are passed via `solve_ivp(..., args=(m, Cd, A, rho, g))` — **not** via global variables, so the function is reusable inside the angle-sweep loop with different `theta`/`v0` without shadowing bugs.

### 1.2 Initial state vector

```python
theta_rad = np.deg2rad(theta_deg)
vx0 = v0 * np.cos(theta_rad)
vy0 = v0 * np.sin(theta_rad)
y0 = [0.0, 0.0, vx0, vy0]     # launch from origin at ground level
```

`y0` here is the *ODE initial condition* array, unrelated to the state variable also often called `y` for vertical position — naming collision risk, see §6.

### 1.3 Writing the terminal event function

Event functions detect zero-crossings of a scalar function of `(t, y)`. To stop when the projectile returns to `y_pos = 0`:

```python
def hit_ground(t, state, *args):
    """Event: triggers when vertical position crosses zero."""
    return state[1]          # y position component of the state vector

hit_ground.terminal = True   # stop integration when this event fires
hit_ground.direction = -1    # only trigger on downward crossing (positive -> negative)
```

**Why `direction = -1` matters**: at `t=0`, `y=0` too (launch point). Without a direction filter, `solve_ivp` could register a spurious event right at the start since the function value is exactly zero there. `direction=-1` restricts triggering to crossings going from positive to negative (i.e., the *descent* through zero), which is what "hits the ground" means. `direction=+1` would instead fire on an *upward* crossing (irrelevant here); `direction=0` (default) fires on any crossing and risks catching t=0 or numerical noise near it.

The event function must accept the same arguments as `fun` (including any `args=` extras), even if unused — hence the `*args` catch-all above, or explicitly list them to match `projectile_ode`'s signature.

### 1.4 Assembling the call

```python
from scipy.integrate import solve_ivp

sol = solve_ivp(
    fun=projectile_ode,
    t_span=(0, 100),              # generous upper bound; event will stop it early
    y0=y0,
    method='RK45',                 # explicit, matches problem spec
    args=(m, Cd, A, rho, g),
    events=hit_ground,
    dense_output=True,             # enables sol.sol(t) continuous interpolation
    max_step=0.05                  # optional: caps step size for smoother output
)
```

- `t_span=(0,100)` is a *safety ceiling*, not the expected flight time — the terminal event ends integration long before 100s for realistic v0. Pick something clearly larger than any plausible flight time (compute a rough estimate: ideal flight time = `2*v0*sin(theta)/g`, then pad generously, e.g. ×5–10).
- `dense_output=True` costs little and buys you smooth plotting without manually restricting `t_eval` resolution.
- `max_step` is optional insurance for very curvy trajectories at high drag; not strictly required at RK45 default adaptivity but worth knowing as a knob.

### When to use `events` vs. manual post-processing

Use the `events` mechanism (not "integrate a fixed time then truncate the array where y<0") because:
- It gives you the *exact* landing time and state via linear-ish root-finding internal to `solve_ivp`, rather than a stairstep artifact from the last time step's y being slightly negative.
- It's the officially expected/idiomatic pattern the problem statement literally specifies.

---

## 2. Extracting Results from `OdeResult`

`solve_ivp` returns a `Bunch`-like `OdeResult` object. Key attributes:

| Attribute | Shape/type | Meaning |
|---|---|---|
| `sol.t` | `(n,)` array | time points actually taken by the adaptive stepper (non-uniform spacing) |
| `sol.y` | `(4, n)` array | state at each `sol.t` — **rows are variables, columns are time steps** |
| `sol.t_events` | list of arrays, one per event function | times at which each event triggered |
| `sol.y_events` | list of arrays | state vectors at each event trigger |
| `sol.sol` | callable (if `dense_output=True`) | `sol.sol(t)` returns interpolated state at arbitrary `t` |
| `sol.status` | int | 0=success/reached tend, 1=terminal event fired, -1=failure |

### 2.1 Basic array extraction

```python
x_traj  = sol.y[0]
y_traj  = sol.y[1]
vx_traj = sol.y[2]
vy_traj = sol.y[3]
t_traj  = sol.t
```

Remember: `sol.y` indexing is `[state_variable_index, time_index]` — the *opposite* orientation from a typical pandas DataFrame row-per-observation layout. This trips people up coming from pandas/tabular habits.

### 2.2 Getting the exact landing point

```python
t_land = sol.t_events[0][0]        # first (only) trigger of the first (only) event
land_state = sol.y_events[0][0]    # [x, y, vx, vy] at landing
x_land = land_state[0]             # this is your "range" for the drag case
```

Both `t_events` and `y_events` are lists indexed by *which event function* (here there's only one, index `[0]`), and within that, an array of trigger occurrences — index `[0]` again for "the first time it happened" (also the only time, since `terminal=True` stops integration at the first occurrence).

### 2.3 Dense output for smooth plotting

Because `sol.t` only contains adaptive-stepper time points (can be sparse for gentle trajectories), for a visually smooth curve interpolate:

```python
t_fine = np.linspace(0, t_land, 300)
state_fine = sol.sol(t_fine)        # shape (4, 300)
x_fine, y_fine = state_fine[0], state_fine[1]
```

This is purely cosmetic for plotting — do not use `sol.sol` beyond `t_land`; the ODE is only valid/meaningful up to ground impact (drag model doesn't know about the ground).

**Cross-reference**: the ideal analytic case (§3) does not need `solve_ivp` at all — compute it with closed-form kinematics and its own `t_fine` sharing the same style of array for consistent plotting.

---

## 3. Matplotlib Patterns for the Trajectory Plot

### 3.1 Ideal (no-drag) closed form, for comparison

```python
def ideal_trajectory(v0, theta_rad, g=9.81, n=300):
    """Closed-form projectile motion (no drag). Returns x, y arrays and range."""
    t_flight = 2 * v0 * np.sin(theta_rad) / g
    t = np.linspace(0, t_flight, n)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    range_ideal = v0**2 * np.sin(2 * theta_rad) / g
    return x, y, range_ideal, t_flight
```

Keeping this as a standalone function (no scipy dependency) makes the angle sweep (§4) cheap for the ideal case — you don't need to numerically integrate the no-drag case at all.

### 3.2 The dual-curve trajectory plot

```python
fig, ax = plt.subplots(figsize=(8, 5))

# Drag-affected trajectory (numerical)
ax.plot(x_fine, y_fine, color='crimson', label='With drag (numerical)', lw=2)

# Ideal trajectory (analytic)
ax.plot(x_ideal, y_ideal, color='steelblue', linestyle='--', label='Ideal (no drag)', lw=2)

# Landing points
ax.scatter([x_land], [0], color='crimson', zorder=5, s=60, marker='o')
ax.scatter([range_ideal], [0], color='steelblue', zorder=5, s=60, marker='o')

# Ground reference line
ax.axhline(0, color='gray', linewidth=0.8)

# Range-reduction annotation (arrow between the two landing points)
ax.annotate(
    '', xy=(x_land, 0), xytext=(range_ideal, 0),
    arrowprops=dict(arrowstyle='<->', color='black', lw=1)
)
reduction_pct = 100 * (range_ideal - x_land) / range_ideal
ax.text(
    (x_land + range_ideal) / 2, max(y_fine) * 0.05,
    f'Range reduced {reduction_pct:.1f}%',
    ha='center', fontsize=9
)

ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title(f'Projectile Trajectory: v0={v0} m/s, θ={theta_deg}°')
ax.legend()
ax.set_aspect('equal', adjustable='datalim')   # true-to-scale flight path shape
plt.tight_layout()
plt.savefig('trajectory.png', dpi=150)
plt.show()
```

Key API notes:
- `zorder=5` ensures scatter markers draw on top of the line curves (default line zorder is lower).
- `ax.annotate('', xy=..., xytext=..., arrowprops=...)` with empty text is the idiomatic way to draw a bidirectional arrow between two points without a label attached to the arrow itself — the label goes in via a separate `ax.text()` call as done above, which gives independent control over its position (e.g., nudged above the ground line so it doesn't overlap the arrow).
- `set_aspect('equal')` is optional but recommended for a physically intuitive trajectory shape (a 45° launch should visually look like ~45°); omit if the y-range is tiny compared to x-range and equal aspect would flatten the plot unreadably — use judgment based on your actual v0/theta.

### When to use `annotate` vs. `text`
- `annotate` when you need an arrow/connector pointing at a specific data coordinate (landing points, peak height).
- `text` when you just need a floating label with no connector (the percentage callout).

---

## 4. Building the Angle-Sweep Loop

### 4.1 Structure

```python
angles_deg = np.arange(1, 90, 1)          # 1 to 89 inclusive
ranges_drag = np.zeros_like(angles_deg, dtype=float)
ranges_ideal = np.zeros_like(angles_deg, dtype=float)

for i, ang in enumerate(angles_deg):
    ang_rad = np.deg2rad(ang)
    vx0 = v0 * np.cos(ang_rad)
    vy0 = v0 * np.sin(ang_rad)
    y0 = [0.0, 0.0, vx0, vy0]

    # rough flight-time estimate to size t_span safely (no-drag time is an upper bound
    # since drag only shortens flight time)
    t_est = 2 * v0 * np.sin(ang_rad) / g
    t_span = (0, max(t_est * 3, 1.0))

    sol = solve_ivp(
        projectile_ode, t_span, y0,
        args=(m, Cd, A, rho, g),
        events=hit_ground,
        method='RK45'
    )
    ranges_drag[i] = sol.y_events[0][0][0]     # x at landing
    ranges_ideal[i] = v0**2 * np.sin(2 * ang_rad) / g
```

### 4.2 Finding the optimal drag angle

```python
best_idx = np.argmax(ranges_drag)
best_angle_drag = angles_deg[best_idx]
best_range_drag = ranges_drag[best_idx]

best_idx_ideal = np.argmax(ranges_ideal)
best_angle_ideal = angles_deg[best_idx_ideal]   # should be 45 (or 44/46 — see pitfall below)
```

`np.argmax` on a 1-degree-resolution array is entirely sufficient for this deliverable — it gives an answer accurate to the sweep's resolution (±0.5°), which is the resolution the problem explicitly asks for. `scipy.optimize.minimize_scalar(lambda a: -range_at_angle(a), bounds=(1,89), method='bounded')` is a legitimate *upgrade* if you want sub-degree precision, but requires refactoring the per-angle solve into a standalone function `range_at_angle(angle_deg) -> float` first. Mention both; implement the simple one unless finer precision is explicitly wanted.

### 4.3 Vectorization considerations

**This loop cannot be vectorized across angles in the usual numpy sense.** Each angle requires an independent adaptive-step ODE integration with its own event-triggered stop time — `solve_ivp` operates on one initial condition at a time (it is not batched like `vmap` in JAX). 89 iterations of a fast, short-duration ODE integration is computationally trivial (well under a second total), so there is no real performance need to seek vectorization — resist the urge to over-engineer this into `scipy.integrate.odeint` with a batched trick or a custom RK4. Loop simplicity here is the *correct* engineering choice, not a shortcut.

If you did want speed on a much finer sweep (e.g., 10,000 angles), the right move would be `multiprocessing.Pool.map` over angles (embarrassingly parallel), not vectorizing the ODE math itself.

### 4.4 Plot 2 — Range vs Angle

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(angles_deg, ranges_ideal, '--', color='steelblue', label='Ideal')
ax.plot(angles_deg, ranges_drag, color='crimson', label='With drag')

ax.axvline(45, color='steelblue', linestyle=':', alpha=0.6)
ax.axvline(best_angle_drag, color='crimson', linestyle=':', alpha=0.6)

ax.scatter([45], [ranges_ideal[np.where(angles_deg==45)[0][0]]], color='steelblue', zorder=5)
ax.scatter([best_angle_drag], [best_range_drag], color='crimson', zorder=5)

ax.annotate(f'Optimal (drag): {best_angle_drag}°', xy=(best_angle_drag, best_range_drag),
            xytext=(best_angle_drag+5, best_range_drag-10),
            arrowprops=dict(arrowstyle='->'))

ax.set_xlabel('Launch angle (degrees)')
ax.set_ylabel('Range (m)')
ax.set_title('Range vs Launch Angle')
ax.legend()
plt.tight_layout()
plt.savefig('range_vs_angle.png', dpi=150)
plt.show()
```

**Cross-reference**: same annotation idioms as §3.2 (`axvline` here is the sweep-plot analog of `axhline` in the trajectory plot — a reference line, not a data curve).

---

## 5. Script Organization / Deliverable Structure

Recommended file layout for a single self-contained `.py` (or notebook with equivalent cell breaks):

```python
"""
P4 - Projectile Motion Simulation with Drag
Compares numerical (drag) vs analytic (ideal) projectile motion.
"""

# ---- 1. IMPORTS ----
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---- 2. PARAMETER BLOCK (all inputs as named variables, per spec) ----
v0 = 40.0        # initial speed, m/s
theta_deg = 45.0 # launch angle, degrees
m = 0.145        # mass, kg (e.g., baseball)
Cd = 0.47        # drag coefficient, sphere
A = 0.0042       # cross-sectional area, m^2
rho = 1.225      # air density, kg/m^3
g = 9.81         # gravitational acceleration, m/s^2

# ---- 3. FUNCTION DEFINITIONS ----
# 3a. drag ODE derivative function        (see §1.1)
# 3b. terminal ground-impact event func   (see §1.3)
# 3c. ideal closed-form trajectory func   (see §3.1)
# 3d. (optional) range_at_angle(angle) helper, reused by both the sweep
#     loop and any scipy.optimize refinement

# ---- 4. MAIN EXECUTION: single-trajectory case ----
#   - build y0, run solve_ivp, extract landing state (§1.4, §2)
#   - compute ideal case for same v0/theta

# ---- 5. PLOT 1: trajectory comparison (§3.2) ----

# ---- 6. MAIN EXECUTION: angle sweep ----
#   - loop 1-89 degrees, store ranges_drag / ranges_ideal (§4.1)
#   - compute best angles (§4.2)

# ---- 7. PLOT 2: range vs angle (§4.4) ----

# ---- 8. PRINTED SUMMARY (optional but good practice) ----
print(f"Ideal range: {range_ideal:.2f} m at {best_angle_ideal}°")
print(f"Drag range:  {best_range_drag:.2f} m at {best_angle_drag}°")
```

This ordering matches how the problem statement enumerates deliverables 1→6, which is convenient both for grading/review and for a reader following top-to-bottom. Every code block gets a `#` comment header per requirement 6 — the section markers above (`# ---- N. ... ----`) double as both organizational scaffolding and the required comments if expanded into full sentences in the actual file.

**GitHub deliverable**: a single `.py` file is preferable to a notebook for this size of deliverable (easier to diff/review, no cell-execution-order ambiguity) unless the guide/rubric explicitly wants inline rendered plots alongside prose — in that case a notebook with markdown cells between the numbered sections above works equally well. Either way, commit the two saved PNGs or ensure `plt.show()` inline output is preserved in notebook cell outputs before pushing, so a reviewer doesn't have to re-run the code to see the plots.

---

## 6. Common Pitfalls (Consolidated)

- **Degree/radian conversion forgotten or double-applied.** `theta` is specified in degrees per the problem; every trig call (`np.sin`, `np.cos`) needs radians. Convert once near the top of each place `theta` is used (`np.deg2rad`), and never pass a degree value directly into `np.sin`/`np.cos`. This is the single most common silent bug — code runs without error but produces a trajectory subtly (or wildly) wrong.
- **Event `direction` sign error.** Using `direction=+1` (or leaving default 0) can cause the event to fire at launch (t≈0, y≈0, ascending... actually descending would be -1; ascending false-trigger risk is more about default 0 catching noise near t=0) or never fire in edge cases. Always use `direction=-1` for "crossing zero while descending," and sanity check `sol.t_events[0]` is non-empty and `> 0`.
- **Forgetting `terminal = True`.** Without it, the event is merely *recorded* (you get `t_events`) but integration continues to `t_span[1]` regardless — wasting compute and potentially producing nonphysical post-impact "trajectory" in `sol.y` if you naively plot the full array instead of truncating at `t_land`.
- **Unbounded/mismatched `t_span`.** Setting `t_span` too small truncates the integration before landing (event never fires, `sol.t_events[0]` is empty, and indexing it throws `IndexError`). Setting it enormously large (e.g., `(0, 1e6)`) wastes adaptive-stepper effort before the terminal event can end things (usually harmless since it *does* stop at the event, but this is a code smell that suggests you didn't reason about expected flight time). Estimate flight time from the no-drag case and pad by 3-5x.
- **Indexing confusion between `sol.y` (rows=variables) and a pandas-style rows=observations mental model.** `sol.y[1]` is *all* y-position values over time, not "the second time step."
- **Treating `C_d`/`A` as free-form tunable constants without checking they're physically paired.** `C_d=0.47` is for a *sphere*; `A` must be the sphere's cross-sectional area `π r²` for a consistent physical scenario, not an arbitrary shape's frontal area. Mixing a sphere `C_d` with a non-spherical `A` (or vice versa) produces a "working" simulation with a physically meaningless drag force. Pick one consistent projectile (e.g., baseball: r≈0.037m → A≈0.0043 m², m≈0.145 kg) and state the assumption in a comment.
- **Re-solving the ideal case numerically when a closed form exists.** It's tempting to reuse `solve_ivp` with drag terms zeroed for the "ideal" comparison for code symmetry — this works but is unnecessary overhead in the 89-angle sweep loop (halves your total integration calls unnecessarily) and diverges from the "analytic ideal case" language in the spec. Use the closed-form formulas (§3.1) for the ideal case; reserve `solve_ivp` for the drag case only.
- **`np.argmax` on an array that still has stale/zero placeholder values** if the sweep loop errors out partway (e.g., one angle's event never fires due to a `t_span` bug) — an unhandled exception mid-loop silently leaves trailing zeros in `ranges_drag` if you swallow errors with a bare `try/except: pass`. Prefer letting it crash during development, or explicitly log/flag failed angles rather than defaulting to zero.
- **Mutable default / shared-state bugs across loop iterations** are unlikely here since `y0` and `t_span` are freshly built each iteration — but double check you're not accidentally reusing a `sol` object or list across iterations by appending instead of index-assigning into a preallocated array.

---

*End of Python implementation section. Companion sections (separately generated) cover Newtonian mechanics fundamentals and ODE/numerical-methods theory for this same problem.*
