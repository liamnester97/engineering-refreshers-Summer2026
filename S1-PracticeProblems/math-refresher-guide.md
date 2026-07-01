# Comprehensive Math Refresher & Reference Guide

**Audience:** Experienced engineer. BS+ background in math through differential equations and linear algebra.  
**Purpose:** Dense reference for solving any standard problem in Algebra, Calculus 1–3, Differential Equations, and Linear Algebra.  
**Format:** Every formula defined. Every technique includes a worked numerical example. Every section includes a Common Mistakes callout.

---

# QUICK LOOKUP: TECHNIQUE SELECTOR

## Which Integration Technique?

| What you see | Technique | Section |
|---|---|---|
| $f(g(x))\cdot g'(x)$ — composite with its derivative present | u-substitution | 3.2 |
| Product of unrelated functions (poly × trig, poly × exp, ln, arctan) | Integration by parts (LIATE) | 3.2 |
| $\sin^m x\cos^n x$, $\tan^m x\sec^n x$ | Trig integrals | 3.2 |
| $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$ | Trig substitution | 3.2 |
| Rational function (poly/poly), denominator factorable | Partial fractions (long divide first if deg↑ ≥ deg↓) | 1.1, 3.2 |
| $e^{ax}\sin(bx)$ or similar cycling product | IBP twice (cycling) | 3.2 |
| $\int\ln x$ or $\int\arctan x$ alone | IBP with $dv = dx$ | 3.2 |

## Which ODE Method?

| ODE form | Method | Section |
|---|---|---|
| $\frac{dy}{dx} = g(x)h(y)$ | Separable | 5.1 |
| $y' + P(x)y = Q(x)$ | Integrating factor | 5.1 |
| $M\,dx + N\,dy = 0$ with $M_y = N_x$ | Exact | 5.1 |
| $y' + P(x)y = Q(x)y^n$ | Bernoulli substitution $v = y^{1-n}$ | 5.1 |
| $ay'' + by' + cy = 0$ | Characteristic equation | 5.2 |
| $ay'' + by' + cy = g(x)$, $g$ is poly/exp/trig | Undetermined coefficients | 5.2 |
| $ay'' + by' + cy = g(x)$, general $g$ | Variation of parameters | 5.2 |
| IVP, need exact solution from initial conditions | Laplace transform | 5.3 |
| System $\mathbf{x}' = A\mathbf{x}$ | Eigenvalue method | 5.4 |

## Which Coordinate System (Calc 3)?

| Region shape | Best coordinates | Section |
|---|---|---|
| Rectangular box or general region | Cartesian | 4.5 |
| Cylinder, cone, disk in $xy$-plane | Cylindrical $(r,\theta,z)$ | 4.5 |
| Sphere, cone from origin | Spherical $(\rho,\phi,\theta)$ | 4.5 |

## Which Vector Calculus Theorem?

| Situation | Theorem | Section |
|---|---|---|
| 2D closed curve, want to convert to area integral | Green's | 4.6 |
| 3D closed curve or want to swap surfaces | Stokes' | 4.6 |
| Closed surface, want outward flux | Divergence | 4.6 |
| Path-independent field, need work | FT for Line Integrals | 4.6 |

---

# TABLE OF CONTENTS

0. [Quick Lookup: Technique Selector](#quick-lookup-technique-selector)
1. [Algebra](#subject-1-algebra)
2. [Calculus 1 — Limits & Derivatives](#subject-2-calculus-1)
3. [Calculus 2 — Integration & Series](#subject-3-calculus-2)
   - 3.4b Hyperbolic Functions
   - 3.4c Numerical Integration (Trapezoidal, Simpson's)
4. [Calculus 3 — Multivariable](#subject-4-calculus-3)
   - 4.5b Surface Integrals
5. [Differential Equations](#subject-5-differential-equations)
6. [Linear Algebra](#subject-6-linear-algebra)

---

# SUBJECT 1: ALGEBRA

---

## 1.1 Factoring and Algebraic Manipulation

### Difference of Squares
$$a^2 - b^2 = (a+b)(a-b)$$

**Example:** $x^2 - 9 = (x+3)(x-3)$

### Perfect Square Trinomial
$$a^2 \pm 2ab + b^2 = (a \pm b)^2$$

**Example:** $x^2 + 6x + 9 = (x+3)^2$

### Sum/Difference of Cubes
$$a^3 + b^3 = (a+b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$$

**Example:** $8x^3 - 27 = (2x-3)(4x^2 + 6x + 9)$

### General Trinomial Factoring
For $ax^2 + bx + c$: find two numbers that multiply to $ac$ and add to $b$. Split the middle term and factor by grouping.

**Example:** $6x^2 + 7x - 3$. Need two numbers multiplying to $6 \cdot (-3) = -18$, adding to $7$: that's $9$ and $-2$.
$$6x^2 + 9x - 2x - 3 = 3x(2x+3) - 1(2x+3) = (3x-1)(2x+3)$$

### Factoring by Grouping
**Example:** $x^3 + 2x^2 - 3x - 6 = x^2(x+2) - 3(x+2) = (x^2-3)(x+2)$

### Completing the Square
To convert $ax^2 + bx + c$:
1. Factor out $a$ from the $x$ terms: $a\left(x^2 + \frac{b}{a}x\right) + c$
2. Add and subtract $\left(\frac{b}{2a}\right)^2$ inside: $a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$

**Example:** $2x^2 - 8x + 5$
$$= 2(x^2 - 4x) + 5 = 2(x^2 - 4x + 4 - 4) + 5 = 2(x-2)^2 - 8 + 5 = 2(x-2)^2 - 3$$

**Use cases:** vertex form of parabola, trig substitution setup, integrating $\int \frac{dx}{x^2+bx+c}$.

### Polynomial Long Division
Divide $2x^3 - 3x^2 + x - 5$ by $x - 2$:

```
2x² + x + 3
         ___________
x - 2 | 2x³ - 3x² + x - 5
        2x³ - 4x²
        ---------
              x² + x
              x² - 2x
              -------
                  3x - 5
                  3x - 6
                  ------
                       1
```
Result: $2x^2 + x + 3 + \frac{1}{x-2}$

### Synthetic Division
Only for dividing by $(x - c)$. For $2x^3 - 3x^2 + x - 5$ ÷ $(x-2)$, use $c = 2$:
```
2 | 2  -3   1  -5
  |    4    2   6
  |-----------
    2   1   3   1
```
Same result: $2x^2 + x + 3$ remainder $1$.

### Partial Fraction Decomposition

**Step 1:** If deg(numerator) ≥ deg(denominator), do polynomial long division first.  
**Step 2:** Factor denominator completely over the reals.  
**Step 3:** Set up the decomposition:

| Factor in denominator | Contribution to decomposition |
|---|---|
| $(ax + b)$ | $\dfrac{A}{ax+b}$ |
| $(ax + b)^2$ | $\dfrac{A}{ax+b} + \dfrac{B}{(ax+b)^2}$ |
| $(ax + b)^n$ | $\dfrac{A_1}{ax+b} + \dfrac{A_2}{(ax+b)^2} + \cdots + \dfrac{A_n}{(ax+b)^n}$ |
| $ax^2 + bx + c$ (irreducible) | $\dfrac{Ax+B}{ax^2+bx+c}$ |

**Example (distinct linear):** $\dfrac{3x+1}{(x-1)(x+2)}$

$$\frac{3x+1}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}$$

Multiply through: $3x+1 = A(x+2) + B(x-1)$

Set $x = 1$: $4 = 3A \Rightarrow A = \frac{4}{3}$  
Set $x = -2$: $-5 = -3B \Rightarrow B = \frac{5}{3}$

**Example (irreducible quadratic):** $\dfrac{x^2+2x+3}{(x+1)(x^2+4)}$

$$= \frac{A}{x+1} + \frac{Bx+C}{x^2+4}$$

Multiply through: $x^2+2x+3 = A(x^2+4) + (Bx+C)(x+1)$  
Set $x=-1$: $1-2+3 = A(5) \Rightarrow A = \frac{2}{5}$  
Expand and match coefficients for $B$ and $C$.

> **Common Mistakes:**
> - Forgetting to do long division when deg(num) ≥ deg(denom)
> - Setting up $\frac{Ax+B}{(ax+b)^2}$ for a repeated linear factor instead of two separate terms
> - Skipping the irreducible quadratic check — $x^2 + 4$ does NOT factor over the reals

---

## 1.2 Exponent and Logarithm Laws

### Exponent Laws
| Law | Formula |
|---|---|
| Product | $a^m \cdot a^n = a^{m+n}$ |
| Quotient | $a^m / a^n = a^{m-n}$ |
| Power | $(a^m)^n = a^{mn}$ |
| Product base | $(ab)^n = a^n b^n$ |
| Negative | $a^{-n} = 1/a^n$ |
| Zero | $a^0 = 1$ ($a \neq 0$) |
| Fractional | $a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$ |

### Logarithm Laws
$$\log_b(xy) = \log_b x + \log_b y$$
$$\log_b\!\left(\frac{x}{y}\right) = \log_b x - \log_b y$$
$$\log_b(x^r) = r\log_b x$$
$$\log_b x = \frac{\ln x}{\ln b} \quad \text{(change of base)}$$
$$\ln(e^x) = x, \quad e^{\ln x} = x$$
$$\log_b(b^x) = x, \quad b^{\log_b x} = x$$

> **Common Mistakes:**
> - $\ln(x+y) \neq \ln x + \ln y$ (no product rule for sums)
> - $(\ln x)^2 \neq 2\ln x$ (the power rule requires the argument to be raised, not the log itself)

---

## 1.3 Solving Equations

### Quadratic: All Methods
Given $ax^2 + bx + c = 0$:

**Quadratic Formula:**
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Discriminant $\Delta = b^2 - 4ac$: if $\Delta > 0$, two real roots; $\Delta = 0$, one repeated real root; $\Delta < 0$, two complex roots.

**Example:** $3x^2 - 5x - 2 = 0$  
$x = \frac{5 \pm \sqrt{25 + 24}}{6} = \frac{5 \pm 7}{6}$  
$x = 2$ or $x = -\frac{1}{3}$

### Rational Equations
Multiply through by LCD. Check for extraneous solutions (values making the original denominator zero).

**Example:** $\frac{1}{x-2} + \frac{3}{x+1} = \frac{4}{x^2-x-2}$  
Note $x^2-x-2 = (x-2)(x+1)$. Multiply by $(x-2)(x+1)$:  
$(x+1) + 3(x-2) = 4$  
$x + 1 + 3x - 6 = 4 \Rightarrow 4x = 9 \Rightarrow x = 9/4$  
Check: $x=9/4$ doesn't make any denominator zero. ✓

### Radical Equations
Isolate the radical, square both sides, check for extraneous solutions.

**Example:** $\sqrt{2x+3} = x - 1$  
Square: $2x + 3 = x^2 - 2x + 1 \Rightarrow x^2 - 4x - 2 = 0$  
$x = \frac{4 \pm \sqrt{16+8}}{2} = 2 \pm \sqrt{6}$  
Check both in original: $x = 2 + \sqrt{6}$ works; $x = 2 - \sqrt{6} \approx -0.449$ gives $\sqrt{} \approx 1.55$ but $x-1 \approx -1.449$ — extraneous.

### Absolute Value Equations
$|f(x)| = c$: if $c > 0$, solve $f(x) = c$ and $f(x) = -c$.  
$|f(x)| = |g(x)|$: solve $f(x) = g(x)$ and $f(x) = -g(x)$.

### Exponential Equations
Isolate the exponential, apply $\ln$ to both sides.

**Example:** $3^{2x-1} = 5$  
$(2x-1)\ln 3 = \ln 5$  
$x = \frac{\ln 5 / \ln 3 + 1}{2} = \frac{\log_3 5 + 1}{2}$

### Logarithmic Equations
Isolate the log, exponentiate. Check domain (argument must be positive).

**Example:** $\ln(x+2) + \ln(x-1) = \ln(4x)$  
$\ln[(x+2)(x-1)] = \ln(4x)$  
$(x+2)(x-1) = 4x$  
$x^2 + x - 2 = 4x \Rightarrow x^2 - 3x - 2 = 0$  
$x = \frac{3 \pm \sqrt{17}}{2}$  
Discard negative root (check domain).

---

## 1.4 Inequalities

### Linear Inequalities
Solve like equations; flip the inequality when multiplying/dividing by a negative number.

### Quadratic Inequalities
Solve $ax^2 + bx + c > 0$: find roots, test intervals.

**Example:** $x^2 - 5x + 6 > 0 \Rightarrow (x-2)(x-3) > 0$  
Roots: $x = 2, 3$. Test intervals $(-\infty,2)$, $(2,3)$, $(3,\infty)$:  
- $x=0$: $(−2)(−3) = 6 > 0$ ✓  
- $x=2.5$: $(0.5)(−0.5) < 0$ ✗  
- $x=4$: $(2)(1) = 2 > 0$ ✓  
Solution: $(-\infty, 2) \cup (3, \infty)$

### Rational Inequalities
Find critical values (zeros of numerator and denominator), test intervals, exclude denominator zeros from solution.

### Absolute Value Inequalities
- $|f(x)| < c$: $-c < f(x) < c$
- $|f(x)| > c$: $f(x) < -c$ or $f(x) > c$

> **Common Mistakes:**
> - Not flipping the inequality when multiplying by a negative
> - Including denominator zeros in the solution set of a rational inequality

---

## 1.5 Functions

### Domain Determination
- Rational: exclude where denominator = 0
- Square roots (even): radicand ≥ 0
- Logarithms: argument > 0
- Compositions: apply restrictions sequentially

**Example:** Domain of $f(x) = \sqrt{\ln(x-1)}$  
Need $x - 1 > 0$ (for ln), so $x > 1$. Then need $\ln(x-1) \geq 0$, so $x - 1 \geq 1$, so $x \geq 2$.  
Domain: $[2, \infty)$

### Inverse Functions
1. Verify $f$ is one-to-one (horizontal line test, or confirm strictly monotone)
2. Write $y = f(x)$, swap $x$ and $y$, solve for $y$
3. The result is $f^{-1}(x)$

**Example:** $f(x) = \frac{2x-3}{x+1}$. Swap: $x = \frac{2y-3}{y+1}$  
$x(y+1) = 2y-3 \Rightarrow xy + x = 2y - 3 \Rightarrow y(x-2) = -3-x$  
$f^{-1}(x) = \frac{-x-3}{x-2}$

### Transformations
Starting from $y = f(x)$:
| Transformation | Effect |
|---|---|
| $y = f(x) + k$ | Shift up $k$ |
| $y = f(x-h)$ | Shift right $h$ |
| $y = -f(x)$ | Reflect over $x$-axis |
| $y = f(-x)$ | Reflect over $y$-axis |
| $y = af(x)$, $a>1$ | Vertical stretch by $a$ |
| $y = f(bx)$, $b>1$ | Horizontal compress by $b$ |

---

## 1.6 Trigonometry — Complete Reference

### Unit Circle (Key Values)

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---|---|---|
| $0$ | $0$ | $1$ | $0$ |
| $\pi/6$ | $1/2$ | $\sqrt{3}/2$ | $1/\sqrt{3}$ |
| $\pi/4$ | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| $\pi/3$ | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |
| $\pi/2$ | $1$ | $0$ | undefined |
| $\pi$ | $0$ | $-1$ | $0$ |
| $3\pi/2$ | $-1$ | $0$ | undefined |
| $2\pi$ | $0$ | $1$ | $0$ |

Reciprocal functions: $\csc = 1/\sin$, $\sec = 1/\cos$, $\cot = 1/\tan$

### Pythagorean Identities
$$\sin^2\theta + \cos^2\theta = 1$$
$$1 + \tan^2\theta = \sec^2\theta$$
$$1 + \cot^2\theta = \csc^2\theta$$

### Angle Addition / Subtraction
$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$
$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$
$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$

### Double Angle Formulas
$$\sin(2\theta) = 2\sin\theta\cos\theta$$
$$\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$$
$$\tan(2\theta) = \frac{2\tan\theta}{1-\tan^2\theta}$$

### Power Reduction (used constantly in integration)
$$\sin^2\theta = \frac{1 - \cos(2\theta)}{2}, \qquad \cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$

### Half Angle Formulas
$$\sin\frac{\theta}{2} = \pm\sqrt{\frac{1-\cos\theta}{2}}, \qquad \cos\frac{\theta}{2} = \pm\sqrt{\frac{1+\cos\theta}{2}}$$

Sign depends on the quadrant of $\theta/2$.

### Product-to-Sum
$$\sin A \cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$$
$$\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$$
$$\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$$

### Inverse Trig Functions

| Function | Domain | Range |
|---|---|---|
| $\arcsin x$ | $[-1,1]$ | $[-\pi/2, \pi/2]$ |
| $\arccos x$ | $[-1,1]$ | $[0, \pi]$ |
| $\arctan x$ | $(-\infty,\infty)$ | $(-\pi/2, \pi/2)$ |
| $\text{arcsec}\, x$ | $|x| \geq 1$ | $[0,\pi/2) \cup (\pi/2, \pi]$ |

**Composition identities:**
$$\sin(\arctan x) = \frac{x}{\sqrt{1+x^2}}, \qquad \cos(\arctan x) = \frac{1}{\sqrt{1+x^2}}$$
$$\tan(\arcsin x) = \frac{x}{\sqrt{1-x^2}}$$

Draw a reference triangle to derive these.

### Solving Trig Equations
Find all solutions in $[0, 2\pi)$, then add $2\pi k$ for general solution.

**Example:** $2\sin^2 x - \sin x - 1 = 0$  
Factor: $(2\sin x + 1)(\sin x - 1) = 0$  
$\sin x = -1/2 \Rightarrow x = 7\pi/6, 11\pi/6$  
$\sin x = 1 \Rightarrow x = \pi/2$

> **Common Mistakes:**
> - Dividing by $\sin x$ or $\cos x$ (you lose solutions where they equal zero — factor instead)
> - Forgetting that $\arcsin$ only returns values in $[-\pi/2, \pi/2]$; there's a second solution in $[\pi/2, 3\pi/2]$

---

## 1.7 Complex Numbers

### Rectangular Form: $z = a + bi$, where $i = \sqrt{-1}$, $i^2 = -1$

- **Addition:** $(a+bi) + (c+di) = (a+c) + (b+d)i$
- **Multiplication:** $(a+bi)(c+di) = (ac-bd) + (ad+bc)i$
- **Division:** $\frac{a+bi}{c+di} = \frac{(a+bi)(c-di)}{c^2+d^2}$
- **Conjugate:** $\bar{z} = a - bi$; note $z\bar{z} = a^2 + b^2 = |z|^2$

### Polar Form
$$z = r(\cos\theta + i\sin\theta) = re^{i\theta}$$
where $r = |z| = \sqrt{a^2+b^2}$ (modulus) and $\theta = \arg(z) = \arctan(b/a)$ (argument, careful with quadrant).

**Euler's formula:** $e^{i\theta} = \cos\theta + i\sin\theta$

### De Moivre's Theorem
$$(re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos(n\theta) + i\sin(n\theta))$$

**Example:** $(1+i)^8$. Write $1+i = \sqrt{2}e^{i\pi/4}$.  
$(1+i)^8 = (\sqrt{2})^8 e^{i \cdot 8\pi/4} = 16 e^{2\pi i} = 16$

### nth Roots
The $n$ nth roots of $re^{i\theta}$ are:
$$z_k = r^{1/n} e^{i(\theta + 2\pi k)/n}, \quad k = 0, 1, \ldots, n-1$$

---

# SUBJECT 2: CALCULUS 1

---

## 2.1 Limits

### Limit Laws
If $\lim_{x\to a} f(x) = L$ and $\lim_{x\to a} g(x) = M$, then:
- $\lim[f \pm g] = L \pm M$
- $\lim[f \cdot g] = L \cdot M$
- $\lim[f/g] = L/M$ (provided $M \neq 0$)
- $\lim[f^n] = L^n$
- $\lim[\sqrt[n]{f}] = \sqrt[n]{L}$ (provided $L > 0$ for even $n$)

### Formal Definition (ε-δ)
$\lim_{x \to a} f(x) = L$ means: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$.

**Proof example:** $\lim_{x\to 3}(2x-1) = 5$.  
$|f(x) - 5| = |2x-1-5| = 2|x-3|$. Set $2|x-3| < \varepsilon$, so $\delta = \varepsilon/2$.

### Techniques for Evaluating Limits

**Direct substitution:** try $f(a)$ first. If defined and continuous, you're done.

**Factoring/canceling (0/0):**
$$\lim_{x\to 2} \frac{x^2-4}{x-2} = \lim_{x\to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x\to 2}(x+2) = 4$$

**Rationalization:**
$$\lim_{x\to 0} \frac{\sqrt{x+4}-2}{x} \cdot \frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \lim_{x\to 0} \frac{x}{x(\sqrt{x+4}+2)} = \frac{1}{4}$$

**Squeeze Theorem:** If $g(x) \leq f(x) \leq h(x)$ near $a$ and $\lim g = \lim h = L$, then $\lim f = L$.

**Example:** $\lim_{x\to 0} x^2 \sin(1/x)$. Since $-1 \leq \sin(1/x) \leq 1$: $-x^2 \leq x^2\sin(1/x) \leq x^2$. Both squeeze limits = 0, so the limit = 0.

### Limits at Infinity
- $\lim_{x\to\infty} x^n = \infty$ for $n > 0$; $\lim_{x\to\infty} x^{-n} = 0$
- For rational functions: divide numerator and denominator by the highest power of $x$ in the denominator.

**Example:** $\lim_{x\to\infty} \frac{3x^2 - 2x}{5x^2 + 1} = \lim_{x\to\infty}\frac{3 - 2/x}{5 + 1/x^2} = \frac{3}{5}$

### Indeterminate Forms and Resolutions

| Form | Resolution |
|---|---|
| $0/0$ | Factor, rationalize, or L'Hôpital |
| $\infty/\infty$ | Divide by dominant term or L'Hôpital |
| $0 \cdot \infty$ | Rewrite as $0/(1/\infty)$ or $\infty/(1/0)$, then L'Hôpital |
| $\infty - \infty$ | Combine fractions, rationalize |
| $0^0, 1^\infty, \infty^0$ | Take $\ln$, convert to $0/0$ or $\infty/\infty$, then L'Hôpital |

**L'Hôpital's Rule:** If $\lim f/g$ is $0/0$ or $\pm\infty/\infty$, then $\lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}$ (provided the latter exists).

**Example:** $\lim_{x\to 0} \frac{e^x - 1}{x} = \lim_{x\to 0} \frac{e^x}{1} = 1$

**Example ($1^\infty$):** $\lim_{x\to 0^+} x^x$. Let $L = \lim x^x$. Then $\ln L = \lim x\ln x = \lim \frac{\ln x}{1/x} \overset{H}{=} \lim \frac{1/x}{-1/x^2} = \lim(-x) = 0$. So $L = e^0 = 1$.

### Continuity
$f$ is continuous at $a$ iff:
1. $f(a)$ is defined
2. $\lim_{x\to a} f(x)$ exists
3. $\lim_{x\to a} f(x) = f(a)$

**Types of discontinuity:**
- **Removable:** limit exists but $\neq f(a)$ (or $f(a)$ undefined)
- **Jump:** one-sided limits exist but are unequal
- **Infinite:** limit is $\pm\infty$

**Intermediate Value Theorem:** If $f$ is continuous on $[a,b]$ and $f(a) < k < f(b)$, then $\exists c \in (a,b)$ with $f(c) = k$.

> **Common Mistakes:**
> - Applying L'Hôpital when the form is NOT $0/0$ or $\infty/\infty$
> - Forgetting to check that the post-L'Hôpital limit actually exists before concluding
> - Assuming continuity at a point just because the function is "nice-looking" there

---

## 2.2 Derivatives — All Rules and Techniques

### Limit Definition
$$f'(x) = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h}$$

**Example:** Find $f'(x)$ for $f(x) = x^2 + 3x$.  
$\frac{(x+h)^2 + 3(x+h) - x^2 - 3x}{h} = \frac{2xh + h^2 + 3h}{h} = 2x + h + 3 \to 2x + 3$

### Differentiation Rules

| Rule | Formula | Example |
|---|---|---|
| Power | $\frac{d}{dx}[x^n] = nx^{n-1}$ | $\frac{d}{dx}[x^5] = 5x^4$ |
| Constant multiple | $\frac{d}{dx}[cf] = cf'$ | $\frac{d}{dx}[3x^4] = 12x^3$ |
| Sum/Difference | $(f \pm g)' = f' \pm g'$ | |
| Product | $(fg)' = f'g + fg'$ | $(x^2 \sin x)' = 2x\sin x + x^2\cos x$ |
| Quotient | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ | |
| Chain | $\frac{d}{dx}[f(g(x))] = f'(g(x))\cdot g'(x)$ | $\frac{d}{dx}[\sin(x^2)] = \cos(x^2)\cdot 2x$ |

**Triple chain rule example:** $\frac{d}{dx}[e^{\sin(x^2)}] = e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x$

### Derivatives of Standard Functions

| Function | Derivative |
|---|---|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $1/x$ |
| $\log_a x$ | $1/(x\ln a)$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |
| $\arcsin x$ | $1/\sqrt{1-x^2}$ |
| $\arccos x$ | $-1/\sqrt{1-x^2}$ |
| $\arctan x$ | $1/(1+x^2)$ |
| $\text{arcsec}\, x$ | $1/(|x|\sqrt{x^2-1})$ |

### Implicit Differentiation
Differentiate both sides with respect to $x$; whenever you differentiate a $y$ term, multiply by $dy/dx$.

**Example:** Find $dy/dx$ for $x^3 + y^3 = 6xy$.  
$3x^2 + 3y^2 \frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$  
$\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$  
$\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x} = \frac{2y - x^2}{y^2 - 2x}$

### Logarithmic Differentiation
Useful when: the function is a product/quotient of many terms, or has variable exponents.

**Example:** $y = \frac{x^3 \sqrt{x+1}}{(2x-1)^4}$

Take $\ln$: $\ln y = 3\ln x + \frac{1}{2}\ln(x+1) - 4\ln(2x-1)$

Differentiate: $\frac{y'}{y} = \frac{3}{x} + \frac{1}{2(x+1)} - \frac{8}{2x-1}$

Multiply both sides by $y$.

**Example (variable exponent):** $y = x^x$  
$\ln y = x\ln x \Rightarrow \frac{y'}{y} = \ln x + 1 \Rightarrow y' = x^x(\ln x + 1)$

### Higher-Order Derivatives
$f'', f''', f^{(n)}$ or $\frac{d^2y}{dx^2}$, etc. — differentiate repeatedly.

### Linear Approximation
$$L(x) = f(a) + f'(a)(x-a)$$

**Example:** Approximate $\sqrt{4.02}$. Let $f(x) = \sqrt{x}$, $a = 4$:  
$f'(x) = 1/(2\sqrt{x})$, $f'(4) = 1/4$  
$L(4.02) = 2 + \frac{1}{4}(0.02) = 2.005$

> **Common Mistakes:**
> - Product rule: writing $(fg)' = f'g'$ instead of $f'g + fg'$
> - Chain rule: forgetting to multiply by the derivative of the inner function
> - Implicit differentiation: not applying chain rule to $y$ terms (missing the $dy/dx$ factor)

---

## 2.3 Applications of Derivatives

### Increasing/Decreasing and First Derivative Test
- $f' > 0$ on $(a,b)$ → $f$ is increasing on $(a,b)$
- $f' < 0$ on $(a,b)$ → $f$ is decreasing on $(a,b)$
- At a critical point $c$ where $f'(c) = 0$ or $f'(c)$ DNE:
  - $f'$ changes $+ \to -$: local maximum
  - $f'$ changes $- \to +$: local minimum
  - No sign change: neither

### Concavity and Second Derivative Test
- $f'' > 0$: concave up
- $f'' < 0$: concave down
- $f''(c) = 0$ and sign changes: inflection point
- At a critical point $c$: $f''(c) > 0$ → local min; $f''(c) < 0$ → local max; $f''(c) = 0$ → inconclusive (use FDT)

### Absolute Extrema on $[a,b]$ — Closed Interval Method
1. Find all critical points in $(a,b)$
2. Evaluate $f$ at each critical point AND at $a$ and $b$
3. Largest value = absolute max; smallest = absolute min

**Example:** $f(x) = x^3 - 3x^2 + 1$ on $[-1/2, 4]$  
$f'(x) = 3x^2 - 6x = 3x(x-2)$; critical points $x=0, 2$  
$f(-1/2) = -1/8 - 3/4 + 1 = 1/8$  
$f(0) = 1$, $f(2) = 8-12+1 = -3$, $f(4) = 64-48+1 = 17$  
Absolute max: $17$ at $x=4$. Absolute min: $-3$ at $x=2$.

### Applied Optimization — Setup Procedure
1. Assign variables, draw a diagram
2. Write the objective function (what you're maximizing/minimizing)
3. Write the constraint equation; use it to eliminate one variable
4. Differentiate, set $= 0$, solve
5. Verify it's a max/min (FDT, SDT, or endpoints)
6. Answer the original question (include units)

**Example:** A box with square base and open top, volume = 32 m³. Minimize surface area.  
Let base side = $x$, height = $h$.  
Surface area: $A = x^2 + 4xh$. Constraint: $x^2 h = 32 \Rightarrow h = 32/x^2$.  
$A(x) = x^2 + 4x \cdot \frac{32}{x^2} = x^2 + \frac{128}{x}$  
$A'(x) = 2x - \frac{128}{x^2} = 0 \Rightarrow x^3 = 64 \Rightarrow x = 4$  
$h = 32/16 = 2$. Dimensions: $4 \times 4 \times 2$ m.

### Related Rates — Setup Procedure
1. Draw and label all quantities (with values and rates given)
2. Write an equation relating the quantities
3. Differentiate both sides with respect to $t$
4. Substitute known values and solve for the unknown rate

**Example:** Ladder: 10 m ladder, foot sliding away at 2 m/s. How fast is the top sliding down when foot is 6 m from wall?  
$x^2 + y^2 = 100$. Differentiate: $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$.  
At $x=6$: $y = 8$. Given $dx/dt = 2$.  
$2(6)(2) + 2(8)\frac{dy}{dt} = 0 \Rightarrow \frac{dy}{dt} = -\frac{3}{2}$ m/s (negative = sliding down).

### Mean Value Theorem
If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $\exists c \in (a,b)$ such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

**Rolle's Theorem:** Special case where $f(a) = f(b)$, guaranteeing $f'(c) = 0$.

> **Common Mistakes:**
> - Optimization: not checking whether the critical point is a max or min (just assuming)
> - Related rates: substituting numerical values BEFORE differentiating (rates must come from the differentiated equation)
> - Closed interval method: forgetting to evaluate at endpoints

---

# SUBJECT 3: CALCULUS 2

---

## 3.1 Integration — Foundations

### Antiderivatives and Indefinite Integrals
$\int f(x)\,dx = F(x) + C$ where $F'(x) = f(x)$

### Fundamental Theorem of Calculus
**Part 1:** $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$

With chain rule: $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x))\cdot g'(x)$

**Part 2:** $\int_a^b f(x)\,dx = F(b) - F(a)$

### Standard Integral Table

| $f(x)$ | $\int f(x)\,dx$ |
|---|---|
| $x^n$ ($n \neq -1$) | $\frac{x^{n+1}}{n+1} + C$ |
| $1/x$ | $\ln\|x\| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\tan x$ | $\ln\|\sec x\| + C$ |
| $\cot x$ | $\ln\|\sin x\| + C$ |
| $\sec x$ | $\ln\|\sec x + \tan x\| + C$ |
| $\csc x$ | $-\ln\|\csc x + \cot x\| + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\sec x\tan x$ | $\sec x + C$ |
| $\csc x\cot x$ | $-\csc x + C$ |
| $1/\sqrt{1-x^2}$ | $\arcsin x + C$ |
| $1/(1+x^2)$ | $\arctan x + C$ |
| $1/(x\sqrt{x^2-1})$ | $\text{arcsec}\,x + C$ |

---

## 3.2 Integration Techniques

### u-Substitution
**When to use:** Composite function where $u = g(x)$ simplifies to a known form. Spot the pattern $f(g(x))\cdot g'(x)$.

**Procedure:**
1. Choose $u = g(x)$
2. Compute $du = g'(x)\,dx$, solve for $dx$
3. Substitute everything — the result should be entirely in terms of $u$
4. Integrate in $u$
5. Back-substitute to $x$

**Definite integrals:** change limits: new limits are $g(a)$ and $g(b)$.

**Example:** $\int_0^1 2x e^{x^2}\,dx$  
$u = x^2$, $du = 2x\,dx$; limits: $u(0) = 0$, $u(1) = 1$  
$\int_0^1 e^u\,du = e^1 - e^0 = e - 1$

**Example (tricky):** $\int \frac{x}{x^2+1}\,dx$  
$u = x^2+1$, $du = 2x\,dx$  
$\int \frac{1}{2u}\,du = \frac{1}{2}\ln|u| + C = \frac{1}{2}\ln(x^2+1) + C$

> **Common Mistakes:**
> - Forgetting to change the limits for definite integrals
> - Not fully substituting: leaving an $x$ in the integrand
> - Choosing $u$ for the outer function instead of the inner

### Integration by Parts
$$\int u\,dv = uv - \int v\,du$$

**LIATE priority for $u$:** Logarithm, Inverse trig, Algebraic, Trigonometric, Exponential

**Example:** $\int x e^x\,dx$  
$u = x$, $dv = e^x\,dx$ → $du = dx$, $v = e^x$  
$= xe^x - \int e^x\,dx = xe^x - e^x + C = e^x(x-1) + C$

**Example (repeated IBP):** $\int x^2\sin x\,dx$  
Apply twice; tabular method:

| Sign | $u$ (differentiate) | $dv$ (integrate) |
|---|---|---|
| $+$ | $x^2$ | $\sin x$ |
| $-$ | $2x$ | $-\cos x$ |
| $+$ | $2$ | $-\sin x$ |
| $-$ | $0$ | $\cos x$ |

Result: $-x^2\cos x + 2x\sin x + 2\cos x + C$

**Cycling IBP:** $\int e^x\sin x\,dx$  
$u = e^x$, $dv = \sin x$: $= -e^x\cos x + \int e^x\cos x\,dx$  
Apply again: $= -e^x\cos x + e^x\sin x - \int e^x\sin x\,dx$  
Let $I = \int e^x\sin x\,dx$: $I = -e^x\cos x + e^x\sin x - I$  
$2I = e^x(\sin x - \cos x) \Rightarrow I = \frac{e^x(\sin x - \cos x)}{2} + C$

**$\int\ln x\,dx$:** $u = \ln x$, $dv = dx$: $= x\ln x - x + C$

### Trigonometric Integrals

**$\int \sin^m x \cos^n x\,dx$:**

- If $m$ (power of sin) is odd: save one $\sin x$, convert rest using $\sin^2 x = 1 - \cos^2 x$, let $u = \cos x$
- If $n$ (power of cos) is odd: save one $\cos x$, convert rest using $\cos^2 x = 1 - \sin^2 x$, let $u = \sin x$
- If both even: use power reduction identities $\sin^2 = (1-\cos 2x)/2$, $\cos^2 = (1+\cos 2x)/2$

**Example:** $\int \sin^3 x \cos^2 x\,dx$  
$= \int \sin^2 x \cos^2 x \sin x\,dx = \int(1-\cos^2 x)\cos^2 x\sin x\,dx$  
$u = \cos x$, $du = -\sin x\,dx$:  
$= -\int(1-u^2)u^2\,du = -\int(u^2 - u^4)\,du = -\frac{u^3}{3} + \frac{u^5}{5} + C = -\frac{\cos^3 x}{3} + \frac{\cos^5 x}{5} + C$

**$\int \tan^m x \sec^n x\,dx$:**
- $n$ even: save $\sec^2 x$, convert rest using $\sec^2 = 1 + \tan^2$, let $u = \tan x$
- $m$ odd: save $\sec x\tan x$, convert rest using $\tan^2 = \sec^2 - 1$, let $u = \sec x$
- $m$ even, $n$ odd: use $\tan^2 = \sec^2 - 1$ to reduce to powers of $\sec x$ alone; integrate via reduction formula or IBP
- $\int\tan^m x\,dx$ alone ($n=0$): peel off $\tan^2 x = \sec^2 x - 1$ repeatedly. E.g., $\int\tan^3 x\,dx = \int\tan x(\sec^2 x-1)\,dx = \frac{\tan^2 x}{2} - \ln|\sec x| + C$

### Trigonometric Substitution

| Integrand form | Substitution | Identity used |
|---|---|---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

**Procedure:** Substitute, simplify the radical (take positive square root), integrate in $\theta$, back-substitute using a reference triangle.

**Example:** $\int \frac{\sqrt{9-x^2}}{x^2}\,dx$  
$x = 3\sin\theta$, $dx = 3\cos\theta\,d\theta$, $\sqrt{9-x^2} = 3\cos\theta$  
$= \int \frac{3\cos\theta}{9\sin^2\theta} \cdot 3\cos\theta\,d\theta = \int \frac{\cos^2\theta}{\sin^2\theta}\,d\theta = \int\cot^2\theta\,d\theta = \int(\csc^2\theta - 1)\,d\theta$  
$= -\cot\theta - \theta + C$  
Back-sub: $\sin\theta = x/3$, so $\cos\theta = \sqrt{9-x^2}/3$, $\cot\theta = \sqrt{9-x^2}/x$, $\theta = \arcsin(x/3)$  
$= -\frac{\sqrt{9-x^2}}{x} - \arcsin\frac{x}{3} + C$

**Completing the square first:** $\int \frac{dx}{\sqrt{x^2 + 4x + 5}} = \int \frac{dx}{\sqrt{(x+2)^2 + 1}}$, then $u = x+2$, trig sub $u = \tan\theta$.

*Alternative for $\sqrt{x^2\pm a^2}$: hyperbolic substitution $x = a\sinh u$ often gives a cleaner result — see §3.4b.*

> **Common Mistakes:**
> - Forgetting $dx$ in terms of $d\theta$ after substitution
> - Taking the wrong sign of the square root ($\sqrt{a^2\cos^2\theta} = a|\cos\theta|$, assume $\cos\theta > 0$ for $\theta \in (-\pi/2, \pi/2)$)
> - Forgetting to back-substitute at the end

---

## 3.3 Improper Integrals

**Type I (infinite limits):**
$$\int_a^\infty f(x)\,dx = \lim_{t\to\infty}\int_a^t f(x)\,dx$$

**Type II (discontinuous integrand at $c \in [a,b]$):**
$$\int_a^b f(x)\,dx = \lim_{t\to c^-}\int_a^t f(x)\,dx + \lim_{t\to c^+}\int_t^b f(x)\,dx$$

**p-integral results:**
$$\int_1^\infty \frac{1}{x^p}\,dx \text{ converges iff } p > 1, \text{ value} = \frac{1}{p-1}$$
$$\int_0^1 \frac{1}{x^p}\,dx \text{ converges iff } p < 1$$

**Example:** $\int_1^\infty \frac{1}{x^2}\,dx = \lim_{t\to\infty}\left[-\frac{1}{x}\right]_1^t = \lim_{t\to\infty}\left(-\frac{1}{t}+1\right) = 1$

**Comparison Test:** If $0 \leq f(x) \leq g(x)$ for $x \geq a$:
- $\int g$ converges $\Rightarrow$ $\int f$ converges
- $\int f$ diverges $\Rightarrow$ $\int g$ diverges

> **Common Mistakes:**
> - Evaluating $\int_{-1}^{1} \frac{1}{x}\,dx$ directly without splitting at $x=0$ (the integrand is discontinuous there — the integral diverges)

---

## 3.4 Applications of Integration

### Area Between Curves
$$A = \int_a^b [f(x) - g(x)]\,dx \quad \text{where } f(x) \geq g(x) \text{ on } [a,b]$$

If curves cross: split at intersection points.

### Volumes — Disk/Washer Method (rotation about horizontal axis)
$$V = \pi\int_a^b [R(x)]^2\,dx \quad \text{(disk)}$$
$$V = \pi\int_a^b \left([R(x)]^2 - [r(x)]^2\right)dx \quad \text{(washer, outer radius } R \text{, inner radius } r\text{)}$$

### Volumes — Shell Method (rotation about vertical axis)
$$V = 2\pi\int_a^b x \cdot f(x)\,dx$$

**When to use:** Shell is often easier when washers would require solving for $x$ in terms of $y$.

### Arc Length
$$L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$$

### Surface Area of Revolution (about $x$-axis)
$$S = 2\pi\int_a^b f(x)\sqrt{1 + [f'(x)]^2}\,dx$$

### Work
$$W = \int_a^b F(x)\,dx \quad \text{(force varying with position)}$$

> **Common Mistakes:**
> - Washer method: squaring $(R-r)$ instead of $R^2 - r^2$
> - Shell method: forgetting the factor of $2\pi$ and the $x$ factor

---

## 3.4b Hyperbolic Functions

*These appear in Laplace tables, trig substitution alternatives, and solutions to $y'' - k^2y = 0$. Cross-reference: Laplace pairs in §5.3.*

### Definitions
$$\sinh x = \frac{e^x - e^{-x}}{2}, \qquad \cosh x = \frac{e^x + e^{-x}}{2}, \qquad \tanh x = \frac{\sinh x}{\cosh x}$$

### Key Identities
$$\cosh^2 x - \sinh^2 x = 1$$
$$1 - \tanh^2 x = \text{sech}^2 x$$
$$\sinh(2x) = 2\sinh x\cosh x, \qquad \cosh(2x) = \cosh^2 x + \sinh^2 x$$

### Derivatives and Integrals

| $f(x)$ | $f'(x)$ | $\int f(x)\,dx$ |
|---|---|---|
| $\sinh x$ | $\cosh x$ | $\cosh x + C$ |
| $\cosh x$ | $\sinh x$ | $\sinh x + C$ |
| $\tanh x$ | $\text{sech}^2 x$ | $\ln(\cosh x) + C$ |
| $\text{sech}\,x$ | $-\text{sech}\,x\tanh x$ | $\arctan(\sinh x) + C$ |

### Inverse Hyperbolic (useful integral forms)
$$\int \frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\!\left(\frac{x}{a}\right) + C = \ln\!\left(x + \sqrt{x^2+a^2}\right) + C$$
$$\int \frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\!\left(\frac{x}{a}\right) + C = \ln\!\left(x + \sqrt{x^2-a^2}\right) + C \quad (x > a)$$

> **Connection to trig sub:** $\int\frac{dx}{\sqrt{x^2+a^2}}$ can be done via $x = a\tan\theta$ (giving $\ln|\sec\theta+\tan\theta|$) or via $x = a\sinh u$ — both yield the same result in different form.

---

## 3.4c Numerical Integration

*Used when an antiderivative doesn't exist in closed form (e.g., $\int e^{-x^2}dx$) or when $f$ is given as data.*

### Trapezoidal Rule
Divide $[a,b]$ into $n$ equal subintervals of width $h = (b-a)/n$, with nodes $x_0, x_1, \ldots, x_n$:
$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right]$$

**Error bound:** $|E_T| \leq \frac{(b-a)^3}{12n^2}\max_{[a,b]}|f''(x)|$. Error is $O(h^2)$.

### Simpson's Rule (requires $n$ even)
$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 4f(x_{n-1}) + f(x_n)\right]$$

Pattern of coefficients: $1,\;4,\;2,\;4,\;2,\;\ldots,\;4,\;1$

**Error bound:** $|E_S| \leq \frac{(b-a)^5}{180n^4}\max_{[a,b]}|f^{(4)}(x)|$. Error is $O(h^4)$ — much better than Trapezoidal.

**Example:** Approximate $\int_0^1 e^{x^2}\,dx$ with $n = 4$ (Simpson's):  
$h = 0.25$, nodes: $x_0=0, x_1=0.25, x_2=0.5, x_3=0.75, x_4=1$  
$f$ values: $1,\; e^{0.0625},\; e^{0.25},\; e^{0.5625},\; e$  
$\approx \frac{0.25}{3}[1 + 4(1.0645) + 2(1.2840) + 4(1.7551) + 2.7183] \approx 1.4637$

> **Common Mistakes:**
> - Simpson's: using odd $n$ (requires even number of subintervals)
> - Trapezoidal: doubling the endpoints (they get coefficient 1, not 2)
> - Confusing $n$ (number of subintervals) with number of nodes ($n+1$)

---

## 3.5 Sequences and Series

### Sequences
A sequence $\{a_n\}$ converges if $\lim_{n\to\infty} a_n = L$ (finite). Otherwise it diverges.  
Apply L'Hôpital by treating $n$ as continuous: $\lim_{n\to\infty}\frac{\ln n}{n} = 0$.

### Geometric Series
$$\sum_{n=0}^\infty ar^n = \frac{a}{1-r} \quad \text{iff } |r| < 1$$

Diverges if $|r| \geq 1$.

### Convergence Tests

| Test | Statement | Best For |
|---|---|---|
| **Divergence Test** | If $\lim a_n \neq 0$, diverges | Quick check; cannot confirm convergence |
| **Integral Test** | $\sum a_n$ and $\int f(x)\,dx$ both converge or both diverge ($f$ positive, decreasing, $a_n = f(n)$) | $a_n = 1/n^p$, etc. |
| **p-Series** | $\sum 1/n^p$ converges iff $p > 1$ | |
| **Direct Comparison** | $0 \leq a_n \leq b_n$: if $\sum b_n$ converges, so does $\sum a_n$ | Known comparison series |
| **Limit Comparison** | If $\lim a_n/b_n = c > 0$, both series behave the same | Rational-like terms |
| **Alternating Series Test** | $\sum (-1)^n b_n$ converges if $b_n \geq 0$, decreasing, $b_n \to 0$ | Alternating series |
| **Ratio Test** | $L = \lim|a_{n+1}/a_n|$: $L<1$ converges, $L>1$ diverges, $L=1$ inconclusive | Factorials, exponentials |
| **Root Test** | $L = \lim|a_n|^{1/n}$: same conclusions as ratio test | $n$th powers |

**Absolute vs. conditional convergence:**
- Absolutely convergent: $\sum |a_n|$ converges (implies convergence)
- Conditionally convergent: $\sum a_n$ converges but $\sum |a_n|$ diverges (e.g., alternating harmonic series)

### Power Series
$$\sum_{n=0}^\infty c_n(x-a)^n$$

**Radius of convergence** via ratio test: $\frac{1}{R} = \lim\left|\frac{c_{n+1}}{c_n}\right|$

After finding $R$: check each endpoint $x = a \pm R$ separately (ratio test is inconclusive there).

### Taylor and Maclaurin Series

$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n$$

**Maclaurin series to memorize:**

| Function | Series | Converges for |
|---|---|---|
| $e^x$ | $\sum_{n=0}^\infty \frac{x^n}{n!}$ | all $x$ |
| $\sin x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | all $x$ |
| $\cos x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ | all $x$ |
| $\ln(1+x)$ | $\sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n}$ | $-1 < x \leq 1$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^\infty x^n$ | $|x| < 1$ |
| $\arctan x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1}$ | $|x| \leq 1$ |

**Operations:** differentiate or integrate term by term within the radius of convergence. Substitute directly (e.g., $e^{-x^2}$ from $e^x$).

---

## 3.6 Parametric and Polar

### Parametric Curves
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}, \qquad \frac{d^2y}{dx^2} = \frac{d(dy/dx)/dt}{dx/dt}$$

Arc length: $L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$

### Polar Coordinates
$x = r\cos\theta$, $y = r\sin\theta$, $r^2 = x^2+y^2$, $\tan\theta = y/x$

**Common curves:**
- Circle: $r = a$ (radius $a$) or $r = 2a\cos\theta$ (center on $x$-axis)
- Cardioid: $r = a(1 + \cos\theta)$
- Rose: $r = a\cos(n\theta)$ — $n$ petals if $n$ odd, $2n$ if $n$ even
- Lemniscate: $r^2 = a^2\cos(2\theta)$

**Area in polar:**
$$A = \frac{1}{2}\int_\alpha^\beta r^2\,d\theta$$

For area between curves: $A = \frac{1}{2}\int_\alpha^\beta (r_{\text{outer}}^2 - r_{\text{inner}}^2)\,d\theta$

**Arc length in polar:**
$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$

> **Common Mistakes:**
> - Series: applying the ratio test to get $L = 1$ and concluding convergence (inconclusive!)
> - Polar area: using $\int r\,d\theta$ instead of $\frac{1}{2}\int r^2\,d\theta$

---

# SUBJECT 4: CALCULUS 3

---

## 4.1 Vectors and 3D Geometry

### Vector Operations
For $\mathbf{a} = \langle a_1, a_2, a_3\rangle$, $\mathbf{b} = \langle b_1, b_2, b_3\rangle$:

**Dot product:** $\mathbf{a}\cdot\mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 = |\mathbf{a}||\mathbf{b}|\cos\theta$

**Projection of $\mathbf{b}$ onto $\mathbf{a}$:**
$$\text{comp}_\mathbf{a}\mathbf{b} = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}|}, \qquad \text{proj}_\mathbf{a}\mathbf{b} = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}|^2}\mathbf{a}$$

**Cross product:**
$$\mathbf{a}\times\mathbf{b} = \begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3\end{vmatrix} = \langle a_2b_3 - a_3b_2,\; a_3b_1 - a_1b_3,\; a_1b_2 - a_2b_1\rangle$$

- $|\mathbf{a}\times\mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta$ = area of parallelogram
- $\mathbf{a}\times\mathbf{b}$ is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$ (right-hand rule)
- $\mathbf{a}\times\mathbf{b} = -\mathbf{b}\times\mathbf{a}$ (anti-commutative)

### Lines in 3D
Through point $P_0 = (x_0,y_0,z_0)$ with direction $\mathbf{d} = \langle a,b,c\rangle$:

**Parametric:** $x = x_0 + at$, $y = y_0 + bt$, $z = z_0 + ct$

**Symmetric:** $\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}$

### Planes
Through $P_0$ with normal $\mathbf{n} = \langle a,b,c\rangle$:
$$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$

**Distance from point $(x_1,y_1,z_1)$ to plane $ax+by+cz = d$:**
$$D = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2+b^2+c^2}}$$

### Quadric Surfaces (Standard Forms)

| Surface | Equation |
|---|---|
| Ellipsoid | $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$ |
| Elliptic paraboloid | $z = \frac{x^2}{a^2}+\frac{y^2}{b^2}$ |
| Hyperbolic paraboloid (saddle) | $z = \frac{x^2}{a^2}-\frac{y^2}{b^2}$ |
| Cone | $z^2 = \frac{x^2}{a^2}+\frac{y^2}{b^2}$ |
| Hyperboloid of one sheet | $\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1$ |

> **Common Mistakes:**
> - Cross product: computing $\mathbf{a}\times\mathbf{b}$ when you need $\mathbf{b}\times\mathbf{a}$ (sign error in normal direction)
> - Dot product: getting the angle wrong because $\cos^{-1}$ gives $[0,\pi]$ only

---

## 4.2 Vector-Valued Functions

$$\mathbf{r}(t) = \langle f(t), g(t), h(t)\rangle$$

$$\mathbf{r}'(t) = \langle f'(t), g'(t), h'(t)\rangle, \qquad \int \mathbf{r}(t)\,dt = \left\langle \int f\,dt, \int g\,dt, \int h\,dt\right\rangle + \mathbf{C}$$

**Arc length:** $L = \int_a^b |\mathbf{r}'(t)|\,dt$

**Unit tangent:** $\mathbf{T} = \frac{\mathbf{r}'}{|\mathbf{r}'|}$

**Curvature:** $\kappa = \frac{|\mathbf{T}'|}{|\mathbf{r}'|} = \frac{|\mathbf{r}'\times\mathbf{r}''|}{|\mathbf{r}'|^3}$

**Principal normal:** $\mathbf{N} = \frac{\mathbf{T}'}{|\mathbf{T}'|}$, **Binormal:** $\mathbf{B} = \mathbf{T}\times\mathbf{N}$

**Acceleration components:**
$$a_T = \frac{d|\mathbf{v}|}{dt} = \frac{\mathbf{r}'\cdot\mathbf{r}''}{|\mathbf{r}'|}, \qquad a_N = \kappa|\mathbf{v}|^2 = \frac{|\mathbf{r}'\times\mathbf{r}''|}{|\mathbf{r}'|}$$

---

## 4.3 Partial Derivatives

$$f_x = \frac{\partial f}{\partial x}: \text{ differentiate w.r.t. } x, \text{ treating } y \text{ as constant}$$

**Clairaut's theorem:** If $f_{xy}$ and $f_{yx}$ are both continuous, then $f_{xy} = f_{yx}$.

### Chain Rule (Multivariable)

If $z = f(x,y)$ and $x = g(t)$, $y = h(t)$:
$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

If $z = f(x,y)$ and $x = g(s,t)$, $y = h(s,t)$:
$$\frac{\partial z}{\partial s} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial s}$$

**Implicit differentiation:** For $F(x,y) = 0$:
$$\frac{dy}{dx} = -\frac{F_x}{F_y}$$

For $F(x,y,z) = 0$: $\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}$

### Gradient
$$\nabla f = \langle f_x, f_y, f_z\rangle$$

- Points in direction of steepest increase; magnitude = rate of steepest ascent
- Perpendicular to level curves (2D) and level surfaces (3D)

**Directional derivative:** $D_\mathbf{u}f = \nabla f \cdot \mathbf{u}$ ($\mathbf{u}$ must be a unit vector)

**Tangent plane** to $z = f(x,y)$ at $(x_0, y_0, z_0)$:
$$z - z_0 = f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$$

---

## 4.4 Multivariable Optimization

**Critical points:** Solve $\nabla f = \mathbf{0}$, i.e., $f_x = 0$ and $f_y = 0$ simultaneously.

**Second derivative test:** Compute $D = f_{xx}f_{yy} - (f_{xy})^2$ at each critical point.

| $D$ | $f_{xx}$ | Conclusion |
|---|---|---|
| $D > 0$ | $> 0$ | Local minimum |
| $D > 0$ | $< 0$ | Local maximum |
| $D < 0$ | — | Saddle point |
| $D = 0$ | — | Inconclusive |

### Lagrange Multipliers
Optimize $f(x,y,z)$ subject to $g(x,y,z) = k$:
$$\nabla f = \lambda \nabla g, \quad g = k$$

This gives a system of equations; solve for $x, y, z, \lambda$.

**Two constraints:** $\nabla f = \lambda\nabla g + \mu\nabla h$

**Example:** Maximize $f(x,y) = xy$ subject to $x + y = 10$.  
$\nabla f = \langle y, x\rangle = \lambda\langle 1, 1\rangle = \lambda\nabla(x+y)$  
$y = \lambda$, $x = \lambda$, so $x = y$. Combined with $x+y=10$: $x=y=5$. Max $= 25$.

> **Common Mistakes:**
> - Forgetting to check the boundary when finding absolute extrema on a closed region
> - SDT: computing $D = f_{xx}f_{yy} - f_{xy}$ instead of $f_{xx}f_{yy} - (f_{xy})^2$

---

## 4.5 Multiple Integrals

### Double Integrals — Setup
$$\iint_R f(x,y)\,dA = \int_a^b\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx$$

**Switching order:** Sketch the region $R$, re-describe its bounds with the other variable as the outer integral.

**Polar:** $\iint_R f(x,y)\,dA = \int_\alpha^\beta\int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\cdot r\,dr\,d\theta$

Note: $dA = r\,dr\,d\theta$ (don't forget the Jacobian $r$!)

### Triple Integrals

**Cylindrical coordinates:** $x = r\cos\theta$, $y = r\sin\theta$, $z = z$; $dV = r\,dr\,d\theta\,dz$

**Spherical coordinates:** $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$; $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$

- $\rho$: distance from origin
- $\phi$: angle from positive $z$-axis (polar angle), $\phi \in [0,\pi]$
- $\theta$: azimuthal angle from $x$-axis, $\theta \in [0, 2\pi]$

**When to use:** Cylindrical for cylinders/cones; spherical for spheres and cones from origin.

### Change of Variables (Jacobian)
$$\iint_R f(x,y)\,dA = \iint_S f(x(u,v), y(u,v))\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$$

$$\frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix}x_u & x_v \\ y_u & y_v\end{vmatrix}$$

---

## 4.5b Surface Integrals

*Required setup knowledge for Stokes' and Divergence theorems (§4.6).*

### Scalar Surface Integral
For surface $S$ parametrized by $\mathbf{r}(u,v)$ over region $D$:
$$\iint_S f\,dS = \iint_D f(\mathbf{r}(u,v))\,|\mathbf{r}_u \times \mathbf{r}_v|\,dA$$

The cross product $\mathbf{r}_u \times \mathbf{r}_v$ gives the normal vector; its magnitude is the area element.

### Vector Surface Integral (Flux)
$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \iint_D \mathbf{F}(\mathbf{r}(u,v))\cdot(\mathbf{r}_u\times\mathbf{r}_v)\,dA$$

Choose orientation: $\mathbf{r}_u\times\mathbf{r}_v$ points outward (or upward) — flip sign if needed.

### Surface $z = g(x,y)$ (most common case)
$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \iint_D \mathbf{F}\cdot\langle -g_x, -g_y, 1\rangle\,dA \quad \text{(upward normal)}$$

The area element: $dS = \sqrt{1 + g_x^2 + g_y^2}\,dA$

**Example (flux):** Find the upward flux of $\mathbf{F} = \langle x, y, z\rangle$ through $z = 4 - x^2 - y^2$ over $z \geq 0$.

$g_x = -2x$, $g_y = -2y$. Normal vector (upward): $\langle 2x, 2y, 1\rangle$

$\mathbf{F}\cdot\langle 2x, 2y, 1\rangle = 2x^2 + 2y^2 + z = 2x^2 + 2y^2 + (4-x^2-y^2) = x^2 + y^2 + 4$

Convert to polar ($z \geq 0 \Rightarrow r \leq 2$):
$$\int_0^{2\pi}\int_0^2 (r^2+4)r\,dr\,d\theta = 2\pi\left[\frac{r^4}{4}+2r^2\right]_0^2 = 2\pi(4+8) = 24\pi$$

### Common Parametrizations

| Surface | Parametrization | Normal magnitude |
|---|---|---|
| Sphere $\rho = a$ | $\mathbf{r} = a\langle\sin\phi\cos\theta,\sin\phi\sin\theta,\cos\phi\rangle$ | $a^2\sin\phi$ |
| Cylinder $r = a$, $0\leq z\leq h$ | $\mathbf{r} = \langle a\cos\theta, a\sin\theta, z\rangle$ | $a$ |
| $z = g(x,y)$ | $\mathbf{r} = \langle x, y, g(x,y)\rangle$ | $\sqrt{1+g_x^2+g_y^2}$ |

> **Common Mistakes:**
> - Wrong orientation: check that your normal points in the required direction before integrating
> - Forgetting to include $|\mathbf{r}_u\times\mathbf{r}_v|$ in scalar surface integrals
> - On $z = g(x,y)$: the downward normal is $\langle g_x, g_y, -1\rangle$ (signs flip)

---

## 4.6 Vector Calculus

### Line Integrals
**Scalar:** $\int_C f\,ds = \int_a^b f(\mathbf{r}(t))|\mathbf{r}'(t)|\,dt$

**Vector (work):** $\int_C \mathbf{F}\cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)\,dt$

### Conservative Fields and Potential Functions
$\mathbf{F} = \langle P, Q, R\rangle$ is conservative on a simply connected domain iff $\nabla\times\mathbf{F} = \mathbf{0}$ (i.e., $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$, etc.)

**Fundamental Theorem for Line Integrals:**
$$\int_C \nabla f\cdot d\mathbf{r} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$$

**Finding potential $f$:** Integrate $P$ w.r.t. $x$, then differentiate w.r.t. $y$ and match $Q$.

### Curl and Divergence
$$\nabla\times\mathbf{F} = \text{curl}\,\mathbf{F} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\\partial_x&\partial_y&\partial_z\\P&Q&R\end{vmatrix}$$

$$\nabla\cdot\mathbf{F} = \text{div}\,\mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

### The Four Big Theorems

**Green's Theorem** (2D, relates line integral around closed curve $C$ to double integral over enclosed region $D$):
$$\oint_C P\,dx + Q\,dy = \iint_D\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA$$

**Stokes' Theorem** (generalizes Green's to 3D surface $S$ with boundary $C$; for setting up $d\mathbf{S}$, see §4.5b):
$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{S}$$

**Divergence Theorem** (relates flux through closed surface $S$ to volume integral over enclosed $E$):
$$\oiint_S \mathbf{F}\cdot d\mathbf{S} = \iiint_E (\nabla\cdot\mathbf{F})\,dV$$

**When to use each:**
- Green's: 2D closed curve, hard to integrate directly
- Stokes': 3D closed curve, or simplify a surface integral to a different surface
- Divergence: closed surface, outward flux, often easier than direct surface integration

> **Common Mistakes:**
> - Spherical: mixing up $\phi$ (from $z$-axis) and $\theta$ (azimuthal), and forgetting $\sin\phi$ in $dV$
> - Green's: wrong sign ($Q_x - P_y$ not $P_x - Q_y$)
> - Divergence theorem: applying to non-closed surfaces

---

# SUBJECT 5: DIFFERENTIAL EQUATIONS

---

## 5.1 First-Order ODEs

### Separable Equations
Form: $\frac{dy}{dx} = g(x)h(y)$

**Procedure:** $\frac{dy}{h(y)} = g(x)\,dx$, then integrate both sides.

**Example:** $\frac{dy}{dx} = xy$, $y(0) = 2$  
$\frac{dy}{y} = x\,dx \Rightarrow \ln|y| = \frac{x^2}{2} + C_1 \Rightarrow y = Ce^{x^2/2}$  
$y(0) = 2 \Rightarrow C = 2 \Rightarrow y = 2e^{x^2/2}$

### Linear First-Order: $\frac{dy}{dx} + P(x)y = Q(x)$

**Integrating factor:** $\mu(x) = e^{\int P(x)\,dx}$

**General solution:** $y = \frac{1}{\mu(x)}\int\mu(x)Q(x)\,dx + \frac{C}{\mu(x)}$

Equivalently: multiply both sides by $\mu$; left side becomes $\frac{d}{dx}[\mu y]$; integrate.

**Example:** $y' + \frac{2}{x}y = 4x$, $y(1) = 2$  
$\mu = e^{\int 2/x\,dx} = e^{2\ln x} = x^2$  
$\frac{d}{dx}[x^2 y] = 4x \cdot x^2 = 4x^3$  
$x^2 y = x^4 + C \Rightarrow y = x^2 + Cx^{-2}$  
$y(1) = 1 + C = 2 \Rightarrow C = 1 \Rightarrow y = x^2 + x^{-2}$

### Exact Equations
Form: $M(x,y)\,dx + N(x,y)\,dy = 0$

**Test for exactness:** $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$

**Procedure:** Find $F(x,y)$ such that $F_x = M$ and $F_y = N$:
1. $F = \int M\,dx + g(y)$
2. Differentiate w.r.t. $y$: $F_y = (\int M\,dx)_y + g'(y) = N$
3. Solve for $g'(y)$, integrate for $g(y)$
4. Solution: $F(x,y) = C$

**Example:** $(2xy - y^2)\,dx + (x^2 - 2xy)\,dy = 0$  
$M_y = 2x - 2y = N_x$ ✓  
$F = \int(2xy - y^2)\,dx = x^2y - xy^2 + g(y)$  
$F_y = x^2 - 2xy + g'(y) = x^2 - 2xy \Rightarrow g'(y) = 0 \Rightarrow g = C_1$  
Solution: $x^2y - xy^2 = C$

### Bernoulli Equations
Form: $y' + P(x)y = Q(x)y^n$ (nonlinear when $n \neq 0, 1$)

**Substitution:** $v = y^{1-n}$ transforms to linear ODE:
$$v' + (1-n)P(x)v = (1-n)Q(x)$$

### Homogeneous Equations (Type: $dy/dx = f(y/x)$)
**Substitution:** $v = y/x$ (so $y = vx$, $y' = v + xv'$) → separable in $v$ and $x$.

### Existence and Uniqueness
For $y' = f(x,y)$, $y(x_0) = y_0$: if $f$ and $\partial f/\partial y$ are continuous near $(x_0, y_0)$, a unique solution exists in some interval around $x_0$.

> **Common Mistakes:**
> - Linear ODE: computing $\mu$ incorrectly from $P(x)$ (make sure equation is in standard form first)
> - Exact: computing $g'(y)$ and finding $x$ terms remain (not exact, or computational error)

---

## 5.2 Second-Order Linear ODEs with Constant Coefficients

### Homogeneous: $ay'' + by' + cy = 0$

**Characteristic equation:** $ar^2 + br + c = 0$, $r = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$

| $\Delta = b^2 - 4ac$ | Roots | General solution $y_h$ |
|---|---|---|
| $\Delta > 0$ | Two distinct real $r_1, r_2$ | $C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| $\Delta = 0$ | Repeated real root $r$ | $(C_1 + C_2 x)e^{rx}$ |
| $\Delta < 0$ | Complex $\alpha \pm \beta i$ | $e^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)$ |

**Example:** $y'' - 5y' + 6y = 0$  
$r^2 - 5r + 6 = 0 \Rightarrow (r-2)(r-3) = 0 \Rightarrow r = 2, 3$  
$y = C_1 e^{2x} + C_2 e^{3x}$

**Example (complex):** $y'' + 4y = 0$  
$r^2 + 4 = 0 \Rightarrow r = \pm 2i$ ($\alpha = 0, \beta = 2$)  
$y = C_1\cos 2x + C_2\sin 2x$

### Non-Homogeneous: $ay'' + by' + cy = g(x)$

General solution: $y = y_h + y_p$

#### Method of Undetermined Coefficients (guess table for $y_p$):

| $g(x)$ form | Guess for $y_p$ |
|---|---|
| $P_n(x)$ (degree $n$ poly) | $x^s(A_n x^n + \cdots + A_0)$ |
| $e^{\alpha x}$ | $x^s A e^{\alpha x}$ |
| $\cos(\beta x)$ or $\sin(\beta x)$ | $x^s(A\cos\beta x + B\sin\beta x)$ |
| $e^{\alpha x}\cos(\beta x)$ or $e^{\alpha x}\sin(\beta x)$ | $x^s e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |
| $P_n(x)e^{\alpha x}$ | $x^s e^{\alpha x}(A_n x^n + \cdots + A_0)$ |

**Modification rule:** $s$ = smallest non-negative integer such that no term in $y_p$ duplicates $y_h$. Usually $s = 0$; use $s = 1$ if the exponential matches a root, $s = 2$ if it's a repeated root.

**Example:** $y'' - 3y' + 2y = 4e^{2x}$  
$y_h$: $r^2 - 3r + 2 = 0$, $(r-1)(r-2) = 0$, $y_h = C_1 e^x + C_2 e^{2x}$  
Since $e^{2x}$ appears in $y_h$: guess $y_p = Axe^{2x}$ (use $s=1$)  
$y_p' = Ae^{2x}(1+2x)$, $y_p'' = Ae^{2x}(4+4x)$  
Substitute: $A e^{2x}(4+4x) - 3Ae^{2x}(1+2x) + 2Axe^{2x} = 4e^{2x}$  
$Ae^{2x}(4+4x-3-6x+2x) = Ae^{2x} = 4e^{2x} \Rightarrow A = 4$  
$y_p = 4xe^{2x}$

#### Variation of Parameters (general — works for any $g(x)$)
Given $y_h = C_1 y_1 + C_2 y_2$:

**Wronskian:** $W = \begin{vmatrix}y_1 & y_2 \\ y_1' & y_2'\end{vmatrix} = y_1 y_2' - y_2 y_1'$

$$u_1' = \frac{-y_2 g}{aW}, \qquad u_2' = \frac{y_1 g}{aW}$$

Integrate to get $u_1, u_2$. Then $y_p = u_1 y_1 + u_2 y_2$.

### Reduction of Order
If $y_1$ is a known solution, let $y_2 = v(x)y_1$, substitute into the ODE, and solve the resulting first-order ODE in $v'$.

> **Common Mistakes:**
> - UDC: not checking if $y_p$ guess duplicates $y_h$ before differentiating
> - Variation of parameters: using $g(x)$ directly without putting the ODE in standard form first (divide by $a$ so coefficient of $y''$ is 1)

---

## 5.3 Laplace Transforms

### Definition
$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st}f(t)\,dt$$

### Complete Transform Table

| $f(t)$ | $F(s) = \mathcal{L}\{f\}$ | Notes |
|---|---|---|
| $1$ | $1/s$ | $s > 0$ |
| $t^n$ | $n!/s^{n+1}$ | $s > 0$ |
| $e^{at}$ | $1/(s-a)$ | $s > a$ |
| $t^n e^{at}$ | $n!/(s-a)^{n+1}$ | |
| $\sin(bt)$ | $b/(s^2+b^2)$ | |
| $\cos(bt)$ | $s/(s^2+b^2)$ | |
| $e^{at}\sin(bt)$ | $b/((s-a)^2+b^2)$ | |
| $e^{at}\cos(bt)$ | $(s-a)/((s-a)^2+b^2)$ | |
| $\sinh(bt)$ | $b/(s^2-b^2)$ | |
| $\cosh(bt)$ | $s/(s^2-b^2)$ | |
| $u(t-a)$ | $e^{-as}/s$ | unit step |
| $\delta(t-a)$ | $e^{-as}$ | Dirac delta |
| $f(t-a)u(t-a)$ | $e^{-as}F(s)$ | 2nd shift theorem |
| $e^{at}f(t)$ | $F(s-a)$ | 1st shift theorem |
| $f'(t)$ | $sF(s) - f(0)$ | |
| $f''(t)$ | $s^2F(s) - sf(0) - f'(0)$ | |
| $f^{(n)}(t)$ | $s^n F(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0)$ | |
| $(f * g)(t) = \int_0^t f(\tau)g(t-\tau)d\tau$ | $F(s)G(s)$ | convolution |

### Solving IVPs with Laplace

**Procedure:**
1. Take $\mathcal{L}$ of both sides
2. Apply derivative property to express $\mathcal{L}\{y'\}$ and $\mathcal{L}\{y''\}$ in terms of $Y(s) = \mathcal{L}\{y\}$ and ICs
3. Solve algebraically for $Y(s)$
4. Apply partial fractions and inverse Laplace to find $y(t)$

**Example:** $y'' + 3y' + 2y = e^{-t}$, $y(0) = 0$, $y'(0) = 1$

Take Laplace: $[s^2 Y - s\cdot 0 - 1] + 3[sY - 0] + 2Y = \frac{1}{s+1}$

$(s^2 + 3s + 2)Y = 1 + \frac{1}{s+1} = \frac{s+2}{s+1}$

$(s+1)(s+2)Y = \frac{s+2}{s+1}$, so $Y = \frac{1}{(s+1)^2}$

$\mathcal{L}^{-1}\left\{\frac{1}{(s+1)^2}\right\} = te^{-t}$

### Inverse Laplace — Key Techniques
1. **Partial fractions:** decompose $Y(s)$ into recognizable forms from the table
2. **Complete the square:** for complex poles, get $(s-a)^2 + b^2$ in denominator
3. **First shift theorem:** $\mathcal{L}^{-1}\{F(s-a)\} = e^{at}f(t)$

### Unit Step and Discontinuous Forcing
$$u(t-a) = \begin{cases} 0 & t < a \\ 1 & t \geq a\end{cases}$$

$\mathcal{L}\{u(t-a)g(t)\} = e^{-as}\mathcal{L}\{g(t+a)\}$

> **Common Mistakes:**
> - Applying the 1st shift theorem backwards: $F(s-a)$ in $s$-domain corresponds to $e^{at}$ (positive exponent) in time domain
> - Forgetting initial condition terms in $\mathcal{L}\{y''\}$

---

## 5.4 Systems of First-Order Linear ODEs

### Matrix Form
Convert to $\mathbf{x}' = A\mathbf{x}$ where $\mathbf{x} = \begin{pmatrix}x_1\\x_2\end{pmatrix}$

**Converting a 2nd-order ODE:** For $y'' + py' + qy = 0$, let $x_1 = y$, $x_2 = y'$:
$$\begin{pmatrix}x_1'\\x_2'\end{pmatrix} = \begin{pmatrix}0&1\\-q&-p\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}$$

### Solution via Eigenvalues

*Eigenvalue/eigenvector procedure: see §6.5. The three cases below (distinct real, repeated, complex) mirror the three cases for 2nd-order ODEs in §5.2.*

Find eigenvalues from $\det(A - \lambda I) = 0$.

**Case 1 — Distinct real eigenvalues $\lambda_1, \lambda_2$ with eigenvectors $\mathbf{v}_1, \mathbf{v}_2$:**
$$\mathbf{x} = C_1\mathbf{v}_1 e^{\lambda_1 t} + C_2\mathbf{v}_2 e^{\lambda_2 t}$$

**Case 2 — Repeated eigenvalue $\lambda$ (algebraic multiplicity 2):**  
If only one eigenvector $\mathbf{v}_1$ exists, find generalized eigenvector $\mathbf{v}_2$: $(A-\lambda I)\mathbf{v}_2 = \mathbf{v}_1$
$$\mathbf{x} = C_1\mathbf{v}_1 e^{\lambda t} + C_2(\mathbf{v}_1 t + \mathbf{v}_2)e^{\lambda t}$$

**Case 3 — Complex eigenvalues $\alpha \pm \beta i$ with eigenvector $\mathbf{v} = \mathbf{a} + i\mathbf{b}$:**
$$\mathbf{x} = C_1 e^{\alpha t}(\mathbf{a}\cos\beta t - \mathbf{b}\sin\beta t) + C_2 e^{\alpha t}(\mathbf{a}\sin\beta t + \mathbf{b}\cos\beta t)$$

**Example:** $\mathbf{x}' = \begin{pmatrix}1&2\\3&2\end{pmatrix}\mathbf{x}$

$\det(A-\lambda I) = (1-\lambda)(2-\lambda) - 6 = \lambda^2 - 3\lambda - 4 = (\lambda-4)(\lambda+1) = 0$

$\lambda_1 = 4$: $(A-4I)\mathbf{v} = 0 \Rightarrow \mathbf{v}_1 = \langle 2, 3\rangle^T$  
$\lambda_2 = -1$: $(A+I)\mathbf{v} = 0 \Rightarrow \mathbf{v}_2 = \langle -1, 1\rangle^T$

$\mathbf{x} = C_1\begin{pmatrix}2\\3\end{pmatrix}e^{4t} + C_2\begin{pmatrix}-1\\1\end{pmatrix}e^{-t}$

---

## 5.5 Numerical Methods for ODEs

### Euler's Method
$$y_{n+1} = y_n + h\cdot f(x_n, y_n)$$
$h$ = step size. Global error $\sim O(h)$.

### Improved Euler / Heun's Method
$$k_1 = f(x_n, y_n), \quad k_2 = f(x_n + h, y_n + hk_1)$$
$$y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$$
Global error $\sim O(h^2)$.

### Runge-Kutta 4th Order (RK4)
$$k_1 = f(x_n, y_n)$$
$$k_2 = f(x_n + h/2,\; y_n + hk_1/2)$$
$$k_3 = f(x_n + h/2,\; y_n + hk_2/2)$$
$$k_4 = f(x_n + h,\; y_n + hk_3)$$
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

Global error $\sim O(h^4)$. Standard choice for most problems.

---

## 5.6 Qualitative Analysis

### Autonomous Equations: $\frac{dy}{dt} = f(y)$

**Equilibrium solutions:** values $y^*$ where $f(y^*) = 0$

**Stability:**
- **Stable (attractor):** $f'(y^*) < 0$ — nearby solutions converge
- **Unstable (repeller):** $f'(y^*) > 0$ — nearby solutions diverge
- **Semi-stable:** $f$ doesn't change sign at $y^*$

**Phase line:** plot $f(y)$ vs. $y$; where $f > 0$, solutions increase; where $f < 0$, solutions decrease.

**Example:** $dy/dt = y(1-y)(2-y)$  
Equilibria: $y = 0, 1, 2$. Check signs of $f$ in each interval:

| Interval | $y$ | $1-y$ | $2-y$ | $f$ | Direction |
|---|---|---|---|---|---|
| $y < 0$ | $-$ | $+$ | $+$ | $-$ | decreasing |
| $0 < y < 1$ | $+$ | $+$ | $+$ | $+$ | increasing |
| $1 < y < 2$ | $+$ | $-$ | $+$ | $-$ | decreasing |
| $y > 2$ | $+$ | $-$ | $-$ | $+$ | increasing |

Result: $y=0$ unstable, $y=1$ stable, $y=2$ unstable.

---

# SUBJECT 6: LINEAR ALGEBRA

---

## 6.1 Vectors and Vector Spaces

### Vector Space Axioms
A set $V$ with operations $+$ and scalar multiplication satisfies all 10 axioms (closure, commutativity, associativity, identity, inverse, distributivity, etc.). Key examples: $\mathbb{R}^n$, $P_n$ (polynomials of degree $\leq n$), $M_{m\times n}$ (matrices).

### Subspace Test
$H \subseteq V$ is a subspace iff:
1. $\mathbf{0} \in H$
2. Closed under addition: $\mathbf{u}, \mathbf{v} \in H \Rightarrow \mathbf{u}+\mathbf{v} \in H$
3. Closed under scalar multiplication: $\mathbf{u} \in H, c \in \mathbb{R} \Rightarrow c\mathbf{u} \in H$

### Linear Independence
$\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is linearly independent iff $c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p = \mathbf{0}$ implies $c_1 = \cdots = c_p = 0$.

**Test:** set up the matrix $[\mathbf{v}_1 \cdots \mathbf{v}_p]$ and row reduce. Independent iff no free variables.

### Basis and Dimension
A **basis** for $H$ is a linearly independent set that spans $H$. The **dimension** is the number of vectors in any basis.

### Rank-Nullity Theorem
For $m \times n$ matrix $A$:
$$\text{rank}(A) + \text{nullity}(A) = n$$
where rank = dim(col space) = number of pivot columns, nullity = dim(null space) = number of free variables.

---

## 6.2 Matrices and Operations

### Matrix Multiplication
$(AB)_{ij} = \sum_k A_{ik}B_{kj}$ (row of $A$ dotted with column of $B$)

$AB$ is defined only if columns of $A$ = rows of $B$. $AB \neq BA$ in general.

**Properties:**
- $(AB)C = A(BC)$ (associative)
- $A(B+C) = AB+AC$ (distributive)
- $(AB)^T = B^T A^T$
- $(AB)^{-1} = B^{-1}A^{-1}$

### Matrix Inverse
$A^{-1}$ exists iff $\det(A) \neq 0$ iff $A$ has $n$ pivot positions.

**2×2 formula:** $A = \begin{pmatrix}a&b\\c&d\end{pmatrix} \Rightarrow A^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

**General method:** Row reduce $[A | I]$ → $[I | A^{-1}]$

---

## 6.3 Systems of Linear Equations

### Gaussian Elimination to REF
**Row operations (preserve solution set):**
1. Swap two rows
2. Multiply a row by a nonzero scalar
3. Add a multiple of one row to another

**REF:** each leading entry is to the right of all leading entries above it.  
**RREF:** each leading entry is 1, and it's the only nonzero entry in its column.

**Solution structure:** number of solutions determined by consistency and free variables.
- Inconsistent (row $[0\;\cdots\;0\;|\;b]$, $b\neq 0$): no solution
- Consistent, no free variables: exactly one solution
- Consistent, $k$ free variables: infinitely many solutions (parametric form, $k$-dimensional solution set)

**Example:** Solve $\begin{cases}x + 2y + z = 4 \\ 2x + 5y + 3z = 9 \\ x + 3y + 2z = 5\end{cases}$

Augmented matrix row reduction:
$$\begin{pmatrix}1&2&1&4\\2&5&3&9\\1&3&2&5\end{pmatrix} \xrightarrow{R_2-2R_1,R_3-R_1} \begin{pmatrix}1&2&1&4\\0&1&1&1\\0&1&1&1\end{pmatrix} \xrightarrow{R_3-R_2} \begin{pmatrix}1&2&1&4\\0&1&1&1\\0&0&0&0\end{pmatrix}$$

Free variable: $z = t$. Back-substitute: $y = 1 - t$, $x = 4 - 2(1-t) - t = 2 + t$.  
Solution: $(x,y,z) = (2,1,0) + t(1,-1,1)$.

---

## 6.4 Determinants

### Cofactor Expansion (along row $i$)
$$\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} M_{ij}$$

where $M_{ij}$ is the minor (det of the $(n-1)\times(n-1)$ submatrix with row $i$ and column $j$ removed).

**Sign pattern:** $\begin{pmatrix}+&-&+\\-&+&-\\+&-&+\end{pmatrix}$

**Example:** $\det\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}$, expand along row 1:  
$= 1\det\begin{pmatrix}5&6\\8&9\end{pmatrix} - 2\det\begin{pmatrix}4&6\\7&9\end{pmatrix} + 3\det\begin{pmatrix}4&5\\7&8\end{pmatrix}$  
$= 1(45-48) - 2(36-42) + 3(32-35) = -3 + 12 - 9 = 0$ (rows are linearly dependent)

### Properties
- $\det(AB) = \det(A)\det(B)$
- $\det(A^T) = \det(A)$
- $\det(A^{-1}) = 1/\det(A)$
- Swapping two rows multiplies det by $-1$
- Multiplying a row by $k$ multiplies det by $k$
- Adding a multiple of one row to another: det unchanged
- $\det(A) = 0 \Leftrightarrow A$ is singular (not invertible)

### Cramer's Rule
For $n\times n$ system $A\mathbf{x} = \mathbf{b}$ with $\det(A) \neq 0$:
$$x_i = \frac{\det(A_i)}{\det(A)}$$
where $A_i$ is $A$ with column $i$ replaced by $\mathbf{b}$.

> **Common Mistakes:**
> - Getting the sign pattern wrong in cofactor expansion
> - $\det(kA) = k^n \det(A)$ (not $k\det(A)$)

---

## 6.5 Eigenvalues and Eigenvectors

### Definition and Procedure
$\lambda$ is an eigenvalue of $A$ and $\mathbf{v} \neq \mathbf{0}$ is the corresponding eigenvector iff $A\mathbf{v} = \lambda\mathbf{v}$, equivalently $(A-\lambda I)\mathbf{v} = \mathbf{0}$.

**Step 1:** Solve $\det(A - \lambda I) = 0$ (characteristic equation) for $\lambda$.  
**Step 2:** For each $\lambda$, solve $(A-\lambda I)\mathbf{v} = \mathbf{0}$ by row reduction. Each free variable gives one eigenvector.

**Example:** $A = \begin{pmatrix}3&1\\1&3\end{pmatrix}$

$\det(A-\lambda I) = (3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = (\lambda-4)(\lambda-2)$

$\lambda_1 = 4$: $(A-4I) = \begin{pmatrix}-1&1\\1&-1\end{pmatrix} \to \mathbf{v}_1 = \begin{pmatrix}1\\1\end{pmatrix}$

$\lambda_2 = 2$: $(A-2I) = \begin{pmatrix}1&1\\1&1\end{pmatrix} \to \mathbf{v}_2 = \begin{pmatrix}1\\-1\end{pmatrix}$

*Eigenvalues drive the solution to systems of ODEs — see §5.4 for the direct connection.*

### Algebraic vs. Geometric Multiplicity
- **Algebraic multiplicity:** multiplicity of $\lambda$ as a root of the characteristic polynomial
- **Geometric multiplicity:** $\dim(\text{null}(A-\lambda I))$ = number of linearly independent eigenvectors for $\lambda$
- Always: geometric $\leq$ algebraic

### Diagonalization
$A = PDP^{-1}$ where $D$ is diagonal (eigenvalues on diagonal) and $P$ has eigenvectors as columns.

**Condition:** $A$ is diagonalizable iff it has $n$ linearly independent eigenvectors (equivalently, geometric multiplicity = algebraic multiplicity for each eigenvalue).

**Powers:** $A^k = PD^kP^{-1}$ where $D^k$ has $\lambda_i^k$ on the diagonal.

**Symmetric matrices:** always diagonalizable; eigenvectors for distinct eigenvalues are orthogonal; can diagonalize as $A = QDQ^T$ where $Q$ is orthogonal ($Q^{-1} = Q^T$).

> **Common Mistakes:**
> - Putting eigenvectors in the wrong order in $P$ — they must match the order of eigenvalues in $D$
> - A repeated eigenvalue does not automatically mean the matrix is not diagonalizable — check geometric multiplicity

---

## 6.6 Orthogonality

### Orthogonal and Orthonormal Sets
$\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$ is orthogonal if $\mathbf{u}_i \cdot \mathbf{u}_j = 0$ for $i \neq j$.  
Orthonormal: additionally $|\mathbf{u}_i| = 1$ for all $i$.

An orthogonal set of nonzero vectors is automatically linearly independent.

### Gram-Schmidt Process
Given basis $\{\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3\}$, produce orthonormal basis $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$:

$$\mathbf{v}_1 = \mathbf{x}_1$$
$$\mathbf{v}_2 = \mathbf{x}_2 - \frac{\mathbf{x}_2\cdot\mathbf{v}_1}{|\mathbf{v}_1|^2}\mathbf{v}_1$$
$$\mathbf{v}_3 = \mathbf{x}_3 - \frac{\mathbf{x}_3\cdot\mathbf{v}_1}{|\mathbf{v}_1|^2}\mathbf{v}_1 - \frac{\mathbf{x}_3\cdot\mathbf{v}_2}{|\mathbf{v}_2|^2}\mathbf{v}_2$$

Then normalize: $\mathbf{u}_i = \mathbf{v}_i/|\mathbf{v}_i|$

### QR Decomposition
$A = QR$ where $Q$ has orthonormal columns (from Gram-Schmidt on columns of $A$) and $R$ is upper triangular.

$R = Q^T A$ (since $Q^TQ = I$)

### Orthogonal Projection
Projection of $\mathbf{y}$ onto subspace $W$ with orthonormal basis $\{\mathbf{u}_1,\ldots,\mathbf{u}_p\}$:
$$\hat{\mathbf{y}} = (\mathbf{y}\cdot\mathbf{u}_1)\mathbf{u}_1 + \cdots + (\mathbf{y}\cdot\mathbf{u}_p)\mathbf{u}_p$$

**Projection matrix:** $P = QQ^T$ where $Q = [\mathbf{u}_1 \cdots \mathbf{u}_p]$. Then $\hat{\mathbf{y}} = P\mathbf{y}$.

### Least Squares
For overdetermined $A\mathbf{x} = \mathbf{b}$ (no solution), minimize $|\mathbf{b} - A\mathbf{x}|$:

**Normal equations:** $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$

If $A$ has linearly independent columns: $\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$

**Example:** Fit a line $y = \beta_0 + \beta_1 x$ to points $(0,1), (1,3), (2,4), (3,5)$.

$A = \begin{pmatrix}1&0\\1&1\\1&2\\1&3\end{pmatrix}$, $\mathbf{b} = \begin{pmatrix}1\\3\\4\\5\end{pmatrix}$

$A^TA = \begin{pmatrix}4&6\\6&14\end{pmatrix}$, $A^T\mathbf{b} = \begin{pmatrix}13\\26\end{pmatrix}$

Solve: $\hat{\beta}_0 = 1.5$, $\hat{\beta}_1 = 4/3 \approx 1.33$

---

## 6.7 Linear Transformations

### Definition
$T: V \to W$ is linear iff:
1. $T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. $T(c\mathbf{u}) = cT(\mathbf{u})$

Equivalently: $T(c\mathbf{u}+d\mathbf{v}) = cT(\mathbf{u})+dT(\mathbf{v})$ and $T(\mathbf{0}) = \mathbf{0}$.

### Matrix Representation
Every linear $T: \mathbb{R}^n \to \mathbb{R}^m$ has $T(\mathbf{x}) = A\mathbf{x}$ where $A = [T(\mathbf{e}_1)\;\cdots\;T(\mathbf{e}_n)]$ ($m\times n$).

**Standard transformations in $\mathbb{R}^2$:**
- Rotation by $\theta$: $\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$
- Reflection over $x$-axis: $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$
- Projection onto $x$-axis: $\begin{pmatrix}1&0\\0&0\end{pmatrix}$

### Kernel and Image
$$\ker(T) = \{\mathbf{x} : T(\mathbf{x}) = \mathbf{0}\} = \text{null}(A)$$
$$\text{im}(T) = \{T(\mathbf{x}) : \mathbf{x} \in V\} = \text{col}(A)$$

- $T$ is **one-to-one** (injective) iff $\ker(T) = \{\mathbf{0}\}$
- $T$ is **onto** (surjective) iff $\text{im}(T) = W$

### Change of Basis
If $B = \{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ and $B' = \{\mathbf{b}'_1,\ldots,\mathbf{b}'_n\}$ are bases, the change-of-basis matrix from $B$ to the standard basis is $P_B = [\mathbf{b}_1\;\cdots\;\mathbf{b}_n]$.

$[T]_{B'} = P^{-1}[T]P$ where $P$ is the change-of-basis matrix.

---

## 6.8 Matrix Decompositions

### LU Decomposition
$A = LU$ where $L$ is lower triangular (1's on diagonal) and $U$ is upper triangular.

Obtained by tracking the row operations in Gaussian elimination. Used to solve $A\mathbf{x} = \mathbf{b}$ efficiently: forward solve $L\mathbf{y} = \mathbf{b}$, then back-substitute $U\mathbf{x} = \mathbf{y}$.

### Singular Value Decomposition (SVD)
For any $m\times n$ matrix $A$:
$$A = U\Sigma V^T$$

- $U$: $m\times m$ orthogonal matrix (columns = left singular vectors — orthonormal basis for $\mathbb{R}^m$)
- $\Sigma$: $m\times n$ diagonal matrix with singular values $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$ on diagonal
- $V$: $n\times n$ orthogonal matrix (columns = right singular vectors — orthonormal basis for $\mathbb{R}^n$)

**Computing SVD:**
- Singular values $\sigma_i = \sqrt{\lambda_i(A^TA)}$
- $V$ = eigenvectors of $A^TA$
- $U$ = eigenvectors of $AA^T$

**Applications:**
- Rank of $A$ = number of nonzero singular values
- Pseudoinverse: $A^+ = V\Sigma^+ U^T$ where $\Sigma^+$ replaces each nonzero $\sigma_i$ with $1/\sigma_i$
- Least squares: $\hat{\mathbf{x}} = A^+\mathbf{b}$
- Data compression / low-rank approximation: retain top $k$ singular values

> **Common Mistakes:**
> - Gram-Schmidt: not re-orthogonalizing against ALL previous vectors in each step
> - SVD: mixing up left and right singular vectors ($U$ vs. $V$)
> - Least squares: applying normal equations when $A^TA$ is singular (use SVD instead)

---

*End of Guide — Algebra · Calculus 1–3 · Differential Equations · Linear Algebra*
