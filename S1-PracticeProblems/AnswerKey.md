# S1 Answer Key

Step-by-step solutions to all 30 problems.

---

## Algebra

---

### Problem 1

Solve for $x$: $\dfrac{2x-3}{x+1} = \dfrac{x+5}{x-2}$

**Cross-multiply:**

$$
(2x-3)(x-2) = (x+5)(x+1)
$$

**Expand both sides:**

$$
2x^2 - 4x - 3x + 6 = x^2 + x + 5x + 5
$$

$$
2x^2 - 7x + 6 = x^2 + 6x + 5
$$

**Collect terms:**

$$
x^2 - 13x + 1 = 0
$$

**Apply the quadratic formula:**

$$
x = \frac{13 \pm \sqrt{169 - 4}}{2} = \frac{13 \pm \sqrt{165}}{2}
$$

**Check that neither solution makes a denominator zero** ($x \neq -1$, $x \neq 2$). Both solutions are approximately $x \approx 12.92$ and $x \approx 0.077$ — neither is $-1$ or $2$.

$$\boxed{x = \frac{13 \pm \sqrt{165}}{2}}$$

---

### Problem 2

Find all real solutions: $x^4 - 5x^2 + 4 = 0$

**Substitute** $u = x^2$:

$$
u^2 - 5u + 4 = 0
$$

**Factor:**

$$
(u - 1)(u - 4) = 0 \implies u = 1 \text{ or } u = 4
$$

**Back-substitute:**

- $x^2 = 1 \implies x = \pm 1$
- $x^2 = 4 \implies x = \pm 2$

$$\boxed{x = -2,\; -1,\; 1,\; 2}$$

---

### Problem 3

Solve: $\log_2(x+3) + \log_2(x-1) = 5$

**Combine using the product rule for logarithms:**

$$
\log_2\bigl[(x+3)(x-1)\bigr] = 5
$$

**Rewrite in exponential form:**

$$
(x+3)(x-1) = 2^5 = 32
$$

**Expand and solve:**

$$
x^2 + 2x - 3 = 32 \implies x^2 + 2x - 35 = 0
$$

$$
(x + 7)(x - 5) = 0 \implies x = -7 \text{ or } x = 5
$$

**Check domain** — $\log_2$ requires both arguments positive:
- $x = -7$: $x + 3 = -4 < 0$ — **rejected**
- $x = 5$: $x + 3 = 8 > 0$, $x - 1 = 4 > 0$ — **valid**

$$\boxed{x = 5}$$

---

### Problem 4

Partial fraction decomposition of $\dfrac{5x-1}{(x-1)(x+2)}$

**Set up the form:**

$$
\frac{5x-1}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}
$$

**Multiply both sides by $(x-1)(x+2)$:**

$$
5x - 1 = A(x+2) + B(x-1)
$$

**Solve for $A$ — let $x = 1$:**

$$
5(1) - 1 = A(3) \implies 4 = 3A \implies A = \frac{4}{3}
$$

**Solve for $B$ — let $x = -2$:**

$$
5(-2) - 1 = B(-3) \implies -11 = -3B \implies B = \frac{11}{3}
$$

$$\boxed{\frac{5x-1}{(x-1)(x+2)} = \frac{4/3}{x-1} + \frac{11/3}{x+2}}$$

---

## Limits

---

### Problem 5

Evaluate $\displaystyle\lim_{x \to 0} \frac{\sin(3x)}{x}$

**Rewrite to apply the standard limit** $\displaystyle\lim_{\theta \to 0}\frac{\sin\theta}{\theta} = 1$:

$$
\lim_{x \to 0} \frac{\sin(3x)}{x} = \lim_{x \to 0} 3 \cdot \frac{\sin(3x)}{3x} = 3 \cdot 1
$$

$$\boxed{3}$$

---

### Problem 6

Evaluate $\displaystyle\lim_{x \to \infty} \frac{4x^3 - 2x + 1}{7x^3 + 5x^2}$

**Divide numerator and denominator by $x^3$** (highest power):

$$
\lim_{x \to \infty} \frac{4 - \frac{2}{x^2} + \frac{1}{x^3}}{7 + \frac{5}{x}} = \frac{4 - 0 + 0}{7 + 0}
$$

$$\boxed{\dfrac{4}{7}}$$

---

### Problem 7

Evaluate $\displaystyle\lim_{x \to 0} \frac{e^{2x} - 1 - 2x}{x^2}$

This is $\frac{0}{0}$ — apply **L'Hôpital's Rule** twice.

**First application:**

$$
\lim_{x \to 0} \frac{2e^{2x} - 2}{2x} \quad \left(\frac{0}{0}\right)
$$

**Second application:**

$$
\lim_{x \to 0} \frac{4e^{2x}}{2} = \frac{4 \cdot 1}{2}
$$

$$\boxed{2}$$

---

## Basic Derivatives

---

### Problem 8

Differentiate $f(x) = 4x^5 - \dfrac{3}{x^2} + \sqrt{x} - 7$

**Rewrite with exponents:**

$$
f(x) = 4x^5 - 3x^{-2} + x^{1/2} - 7
$$

**Apply the power rule to each term:**

$$
f'(x) = 20x^4 - 3(-2)x^{-3} + \tfrac{1}{2}x^{-1/2} - 0
$$

$$\boxed{f'(x) = 20x^4 + \frac{6}{x^3} + \frac{1}{2\sqrt{x}}}$$

---

### Problem 9

Differentiate $f(x) = 3\sin(x) - 5\cos(x) + 2\tan(x)$

**Apply standard trig derivative rules:**

$$\boxed{f'(x) = 3\cos(x) + 5\sin(x) + 2\sec^2(x)}$$

---

### Problem 10

Differentiate $f(x) = e^{3x} - \ln(x^2 + 1)$

**First term** — chain rule: $\dfrac{d}{dx}e^{3x} = 3e^{3x}$

**Second term** — chain rule: $\dfrac{d}{dx}\ln(x^2+1) = \dfrac{2x}{x^2+1}$

$$\boxed{f'(x) = 3e^{3x} - \frac{2x}{x^2+1}}$$

---

## Chain, Product, and Quotient Rules

---

### Problem 11

Find $\dfrac{dy}{dx}$ for $y = x^3\ln(x) - e^{2x}\sin(x)$

**First term** — product rule:

$$
\frac{d}{dx}\bigl[x^3\ln(x)\bigr] = 3x^2\ln(x) + x^3 \cdot \frac{1}{x} = 3x^2\ln(x) + x^2
$$

**Second term** — product rule with chain rule on $e^{2x}$:

$$
\frac{d}{dx}\bigl[e^{2x}\sin(x)\bigr] = 2e^{2x}\sin(x) + e^{2x}\cos(x)
$$

**Combine:**

$$\boxed{\frac{dy}{dx} = 3x^2\ln(x) + x^2 - e^{2x}\bigl(2\sin(x) + \cos(x)\bigr)}$$

---

### Problem 12

Find $\dfrac{dy}{dx}$ for $y = \dfrac{x^2 - 1}{\sin(x)}$

**Apply the quotient rule** $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$:

$$
\frac{dy}{dx} = \frac{2x \cdot \sin(x) - (x^2-1)\cos(x)}{\sin^2(x)}
$$

$$\boxed{\frac{dy}{dx} = \frac{2x\sin(x) - (x^2-1)\cos(x)}{\sin^2(x)}}$$

---

### Problem 13

Find $\dfrac{dy}{dx}$ for $y = \cos^3(4x^2+1)$

**Three nested functions** — apply the chain rule twice.

Let $u = \cos(4x^2+1)$, so $y = u^3$:

$$
\frac{dy}{dx} = 3u^2 \cdot \frac{du}{dx}
$$

Now $\dfrac{du}{dx} = -\sin(4x^2+1) \cdot 8x$:

$$
\frac{dy}{dx} = 3\cos^2(4x^2+1) \cdot \bigl(-\sin(4x^2+1)\bigr) \cdot 8x
$$

$$\boxed{\frac{dy}{dx} = -24x\cos^2(4x^2+1)\sin(4x^2+1)}$$

---

## Implicit Differentiation

---

### Problem 14

Find $\dfrac{dy}{dx}$ for $x^2y + y^3 = 6$

**Differentiate both sides with respect to $x$:**

$$
2xy + x^2\frac{dy}{dx} + 3y^2\frac{dy}{dx} = 0
$$

**Collect $\dfrac{dy}{dx}$ terms:**

$$
\frac{dy}{dx}\bigl(x^2 + 3y^2\bigr) = -2xy
$$

$$\boxed{\frac{dy}{dx} = \frac{-2xy}{x^2 + 3y^2}}$$

---

### Problem 15

For $x^3 + y^3 = 3xy$, find $\dfrac{dy}{dx}$ and the tangent line at $\left(\dfrac{3}{2},\,\dfrac{3}{2}\right)$.

*(Note: verify the point lies on the curve: $\frac{27}{8} + \frac{27}{8} = \frac{27}{4}$ and $3\cdot\frac{3}{2}\cdot\frac{3}{2} = \frac{27}{4}$ ✓)*

**Differentiate both sides:**

$$
3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx}
$$

**Isolate $\dfrac{dy}{dx}$:**

$$
3y^2\frac{dy}{dx} - 3x\frac{dy}{dx} = 3y - 3x^2
$$

$$
\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}
$$

**Evaluate at $\left(\frac{3}{2},\frac{3}{2}\right)$:**

$$
\frac{dy}{dx} = \frac{\frac{3}{2} - \frac{9}{4}}{\frac{9}{4} - \frac{3}{2}} = \frac{-\frac{3}{4}}{\frac{3}{4}} = -1
$$

**Tangent line:**

$$
y - \frac{3}{2} = -1\!\left(x - \frac{3}{2}\right) \implies y = -x + 3
$$

$$\boxed{\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}, \qquad \text{tangent line: } y = -x + 3}$$

---

## Applied Optimization

---

### Problem 16

Find the absolute max and min of $f(x) = x^3 - 3x^2 - 9x + 5$ on $[-2,\,4]$.

**Find critical points** — set $f'(x) = 0$:

$$
f'(x) = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x-3)(x+1)
$$

Critical points: $x = 3$ and $x = -1$ — both in $[-2,\,4]$.

**Evaluate $f$ at the critical points and endpoints:**

$$
f(-2) = -8 - 12 + 18 + 5 = 3
$$

$$
f(-1) = -1 - 3 + 9 + 5 = 10
$$

$$
f(3) = 27 - 27 - 27 + 5 = -22
$$

$$
f(4) = 64 - 48 - 36 + 5 = -15
$$

$$\boxed{\text{Absolute maximum: } f(-1) = 10 \qquad \text{Absolute minimum: } f(3) = -22}$$

---

### Problem 17

$s(t) = t^3 - 6t^2 + 9t$, $\;t \geq 0$. Find when at rest, when moving in the positive direction, and total distance on $[0,4]$.

**Velocity:**

$$
v(t) = s'(t) = 3t^2 - 12t + 9 = 3(t-1)(t-3)
$$

**At rest:** $v(t) = 0 \implies$ $\boxed{t = 1 \text{ and } t = 3}$

**Moving in positive direction:** $v(t) > 0$ when $t \in [0,1)$ or $t \in (3, \infty)$

**Total distance on $[0,4]$** — evaluate $s$ at each rest time and endpoint:

$$
s(0) = 0, \quad s(1) = 1 - 6 + 9 = 4, \quad s(3) = 27 - 54 + 27 = 0, \quad s(4) = 64 - 96 + 36 = 4
$$

$$
d = |s(1) - s(0)| + |s(3) - s(1)| + |s(4) - s(3)| = 4 + 4 + 4
$$

$$\boxed{\text{Total distance} = 12 \text{ units}}$$

---

## Basic Integrals

---

### Problem 18

Evaluate $\displaystyle\int \left(6x^2 - \frac{4}{x} + 3e^x\right)dx$

**Integrate term by term:**

$$
\int 6x^2\,dx = 2x^3, \qquad \int \frac{4}{x}\,dx = 4\ln|x|, \qquad \int 3e^x\,dx = 3e^x
$$

$$\boxed{2x^3 - 4\ln|x| + 3e^x + C}$$

---

### Problem 19

Evaluate $\displaystyle\int_0^{\pi} \sin(x)\,dx$

$$
\int_0^{\pi} \sin(x)\,dx = \Bigl[-\cos(x)\Bigr]_0^{\pi} = -\cos(\pi) + \cos(0) = 1 + 1
$$

$$\boxed{2}$$

---

### Problem 20

Find $F'(x)$ where $F(x) = \displaystyle\int_1^{x^2} \frac{t}{t^2+1}\,dt$

**Apply the Fundamental Theorem of Calculus with the chain rule.** Let $g(x) = x^2$:

$$
F'(x) = \frac{g(x)}{[g(x)]^2 + 1} \cdot g'(x) = \frac{x^2}{x^4 + 1} \cdot 2x
$$

$$\boxed{F'(x) = \frac{2x^3}{x^4 + 1}}$$

---

## U-Substitution

---

### Problem 21

Evaluate $\displaystyle\int \frac{3x^2 + 2}{x^3 + 2x + 1}\,dx$

**Let** $u = x^3 + 2x + 1$, then $du = (3x^2 + 2)\,dx$:

$$
\int \frac{du}{u} = \ln|u| + C
$$

$$\boxed{\ln\left|x^3 + 2x + 1\right| + C}$$

---

### Problem 22

Evaluate $\displaystyle\int_0^1 x\,e^{x^2}\,dx$

**Let** $u = x^2$, then $du = 2x\,dx$, so $x\,dx = \dfrac{du}{2}$.

**Change limits:** $x=0 \to u=0$; $x=1 \to u=1$

$$
\int_0^1 x\,e^{x^2}\,dx = \frac{1}{2}\int_0^1 e^u\,du = \frac{1}{2}\Bigl[e^u\Bigr]_0^1 = \frac{1}{2}(e - 1)
$$

$$\boxed{\dfrac{e-1}{2}}$$

---

### Problem 23

Evaluate $\displaystyle\int \sin^4(x)\cos(x)\,dx$

**Let** $u = \sin(x)$, then $du = \cos(x)\,dx$:

$$
\int u^4\,du = \frac{u^5}{5} + C
$$

$$\boxed{\frac{\sin^5(x)}{5} + C}$$

---

## Integration by Parts

---

### Problem 24

Evaluate $\displaystyle\int_0^{\pi/2} x\cos(x)\,dx$

**Let** $u = x$, $dv = \cos(x)\,dx$ $\;\Rightarrow\;$ $du = dx$, $v = \sin(x)$

$$
\int_0^{\pi/2} x\cos(x)\,dx = \Bigl[x\sin(x)\Bigr]_0^{\pi/2} - \int_0^{\pi/2}\sin(x)\,dx
$$

$$
= \frac{\pi}{2}\cdot 1 - 0 - \Bigl[-\cos(x)\Bigr]_0^{\pi/2}
$$

$$
= \frac{\pi}{2} - \bigl(-\cos(\tfrac{\pi}{2}) + \cos(0)\bigr) = \frac{\pi}{2} - (0 + 1)
$$

$$\boxed{\dfrac{\pi}{2} - 1}$$

---

### Problem 25

Evaluate $\displaystyle\int x^2 e^x\,dx$

**First pass** — let $u = x^2$, $dv = e^x\,dx$:

$$
\int x^2 e^x\,dx = x^2 e^x - \int 2x\,e^x\,dx
$$

**Second pass** on $\displaystyle\int 2x\,e^x\,dx$ — let $u = 2x$, $dv = e^x\,dx$:

$$
\int 2x\,e^x\,dx = 2x\,e^x - \int 2e^x\,dx = 2x\,e^x - 2e^x
$$

**Combine:**

$$
\int x^2 e^x\,dx = x^2 e^x - 2x\,e^x + 2e^x + C = e^x(x^2 - 2x + 2) + C
$$

$$\boxed{e^x(x^2 - 2x + 2) + C}$$

---

## Differential Equations

---

### Problem 26

Solve $\dfrac{dy}{dx} = \dfrac{x^2}{y}$, $\;y(0) = 3$

**Separate variables:**

$$
y\,dy = x^2\,dx
$$

**Integrate both sides:**

$$
\frac{y^2}{2} = \frac{x^3}{3} + C
$$

**Apply initial condition** $y(0) = 3$:

$$
\frac{9}{2} = 0 + C \implies C = \frac{9}{2}
$$

**Solve for $y$:**

$$
y^2 = \frac{2x^3}{3} + 9 \implies y = \sqrt{\frac{2x^3}{3} + 9} \quad (y > 0)
$$

$$\boxed{y = \sqrt{\dfrac{2x^3}{3} + 9}}$$

---

### Problem 27

Solve $\dfrac{dy}{dx} + 2y = 4e^{-x}$

**Identify integrating factor** $\mu = e^{\int 2\,dx} = e^{2x}$

**Multiply both sides by $\mu$:**

$$
\frac{d}{dx}\bigl[e^{2x}y\bigr] = 4e^{-x} \cdot e^{2x} = 4e^{x}
$$

**Integrate both sides:**

$$
e^{2x}y = 4e^{x} + C
$$

**Divide by $e^{2x}$:**

$$\boxed{y = 4e^{-x} + Ce^{-2x}}$$

---

### Problem 28

Find the general solution of $y'' - 5y' + 6y = 0$

**Write the characteristic equation:**

$$
r^2 - 5r + 6 = 0 \implies (r-2)(r-3) = 0
$$

**Distinct real roots:** $r_1 = 2$, $r_2 = 3$

$$\boxed{y = C_1 e^{2x} + C_2 e^{3x}}$$

---

### Problem 29

Solve $y'' + 4y' + 4y = 0$, $\;y(0) = 1$, $\;y'(0) = -1$

**Characteristic equation:**

$$
r^2 + 4r + 4 = 0 \implies (r+2)^2 = 0
$$

**Repeated root** $r = -2$, so the general solution is:

$$
y = (C_1 + C_2 x)e^{-2x}
$$

**Apply $y(0) = 1$:**

$$
C_1 = 1
$$

**Differentiate:**

$$
y' = C_2 e^{-2x} - 2(C_1 + C_2 x)e^{-2x}
$$

**Apply $y'(0) = -1$:**

$$
C_2 - 2C_1 = -1 \implies C_2 - 2 = -1 \implies C_2 = 1
$$

$$\boxed{y = (1 + x)e^{-2x}}$$

---

### Problem 30

Salt tank mixing problem: $Q(0) = 10$ kg, volume = 100 L, flow in/out = 5 L/min (pure water in).

**Set up the IVP.** The rate of salt leaving is:

$$
\text{rate out} = 5\,\frac{\text{L}}{\text{min}} \cdot \frac{Q}{100}\,\frac{\text{kg}}{\text{L}} = \frac{Q}{20}\,\frac{\text{kg}}{\text{min}}
$$

$$
\frac{dQ}{dt} = -\frac{Q}{20}, \qquad Q(0) = 10
$$

**Separate and integrate:**

$$
\frac{dQ}{Q} = -\frac{dt}{20} \implies \ln|Q| = -\frac{t}{20} + C
$$

**General solution:**

$$
Q(t) = Ae^{-t/20}
$$

**Apply $Q(0) = 10$:** $A = 10$

$$
Q(t) = 10e^{-t/20}
$$

**Find $t$ when $Q = 1$ kg:**

$$
1 = 10e^{-t/20} \implies e^{-t/20} = \frac{1}{10} \implies -\frac{t}{20} = -\ln(10) \implies t = 20\ln(10)
$$

$$\boxed{Q(t) = 10e^{-t/20}\text{ kg}, \qquad t = 20\ln(10) \approx 46.1 \text{ minutes}}$$
