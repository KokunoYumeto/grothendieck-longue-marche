"""Small exact checks added while drafting the notes; no OCR or source edits."""
import sympy as S
from datetime import datetime, timezone

t, e = S.symbols("t epsilon")
lam = 2/t - 2*e/t**2
residual = S.expand(2*S.diff(lam, t) + lam**2)
mod_e2 = S.rem(S.Poly(residual, e), S.Poly(e**2, e)).as_expr()
assert mod_e2 == 0
print("UTC", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"))
print("SymPy", S.__version__)
print("A14_MOVING_POLE_DUAL_NUMBERS\tPASS\tresidual mod epsilon^2 =", mod_e2)
print("Unreduced residual:", residual)
print("Scope: Q[epsilon]/epsilon^2 with t inverted; actual pole divisor t+epsilon.")
s = S.log(t)
g = -2*S.diff(s, t, 3)/S.diff(s, t) + 3*(S.diff(s, t, 2)/S.diff(s, t))**2
assert S.simplify(g + 1/t**2) == 0
print("E10_MULTIPLICATIVE_UNIFORMIZATION\tPASS\tG_t(log t) =", S.simplify(g))
mu = -(t**2-t+1)/(t**2*(t-1)**2)
at_zero = S.limit(t**2*mu, t, 0)
at_one = S.limit((t-1)**2*mu, t, 1)
u = S.symbols("u")
at_infty = S.limit(u**2*mu.subs(t, 1/u)/u**4, u, 0)
assert (at_zero, at_one, at_infty) == (-1, -1, -1)
print("B18_THREE_PUNCTURES\tPASS\tleading coefficients at 0,1,infinity =", (at_zero, at_one, at_infty))
