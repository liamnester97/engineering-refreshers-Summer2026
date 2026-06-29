# M3 — L-Bracket Hand Calculation
# Treats the horizontal leg as a cantilever beam with a point load at the tip.
# All units: mm, N, MPa (N/mm²)

# ── Inputs ────────────────────────────────────────────────────────────────────
F = 500         # Applied load (N)
L = 80          # Horizontal leg length (mm)
b = 50          # Section depth (mm)
h = 5           # Wall thickness — bending dimension (mm)
sigma_yield = 250  # Yield strength of structural steel (MPa)
FOS_required = 2.0

# ── Bending Moment ─────────────────────────────────────────────────────────────
M = F * L       # N·mm — moment at the fixed end (interior corner)

# ── Section Properties ─────────────────────────────────────────────────────────
I = (b * h**3) / 12     # Second moment of area (mm⁴)
c = h / 2               # Distance from neutral axis to outer fiber (mm)

# ── Bending Stress ─────────────────────────────────────────────────────────────
sigma = (M * c) / I     # MPa — peak bending stress at fixed end

# ── Factor of Safety ───────────────────────────────────────────────────────────
FOS = sigma_yield / sigma

# ── Results ────────────────────────────────────────────────────────────────────
print("=" * 45)
print("  M3 L-Bracket — Cantilever Hand Calculation")
print("=" * 45)
print(f"  Bending Moment      M  = {M:>10,.1f} N·mm")
print(f"  Moment of Inertia   I  = {I:>10.2f} mm⁴")
print(f"  Neutral Axis Dist.  c  = {c:>10.2f} mm")
print(f"  Bending Stress      σ  = {sigma:>10.2f} MPa")
print(f"  Yield Strength      σy = {sigma_yield:>10.1f} MPa")
print(f"  Factor of Safety    FOS = {FOS:>9.3f}")
print("-" * 45)
if FOS >= FOS_required:
    print(f"  ✅ PASS — FOS {FOS:.3f} ≥ {FOS_required}")
else:
    print(f"  ❌ FAIL — FOS {FOS:.3f} < {FOS_required} (hand calc is conservative)")
print("=" * 45)
