"""Exact symbolic transport certificate for A.71.

The three rank-zero rows printed at the end are selected from the existing
rigorous A.38 census.  This script does not replace its analytic certificates.
"""
import csv
from pathlib import Path
import sympy as s

a,b,c,z,X,Y,x,y = s.symbols("a b c z X Y x y")
cyc = z*z+z+1
gd = (6*a*z*z*X-Y-36*a**3)/(6*a*X-Y-36*a**3)
h = (z*z*c-1)/(c-1)

def numerator(expr):
    return s.fraction(s.cancel(expr))[0]

# The chosen points are flexes, and the indicated lines are their tangents.
for i in range(3):
    yi = 6*a*z**(2*i)*X-36*a**3
    residual = yi**2-X**3+432*a**6+(X-12*a*a*z**i)**3
    assert s.rem(s.expand(residual),cyc,z) == 0

# The universal coefficient-two value is independent of the cubic twist.
assert s.rem((6*c*a*a)**3-432*a**6,c**3-2,c) == 0
assert s.cancel(gd.subs({X:6*c*a*a,Y:0})-h) == 0

# The cubic scaling transports E_d and its normalized flex unit to E_9.
t = b*b/a
g9 = (6*b*b*z*z*X-Y-324)/(6*b*b*X-Y-324)
transport = g9.subs({X:t*t*X,Y:t**3*Y}, simultaneous=True)
assert s.rem(numerator(transport-gd),b**3-3,b) == 0
curve_transport = -432*a**6*t**6+432*9**2
assert s.rem(s.expand(curve_transport),b**3-3,b) == 0

# The known minimal model E_9:y²+y=x³−1 has X=36x,Y=216y+108.
g0 = (b*b*z*z*x-y-2)/(b*b*x-y-2)
assert s.cancel(g9.subs({X:36*x,Y:216*y+108},simultaneous=True)-g0) == 0
assert s.expand((216*y+108)**2-(36*x)**3+432*9**2) == 46656*(y*y+y-x**3+1)

print("All three tangent-line identities passed: intersection divisor3(d_i).")
print("S2=(6*c*a^2,0), c^3=2, lies on E_d.")
print("g_d(S2)=(z^2*c-1)/(c-1), independent ofd.")
print("t=b^2/a transports E_d to E_9 and preserves the normalized flex ratio.")
print("X=36x,Y=216y+108 transports g_9 to the exact A.69 unitg0.")

path = Path(__file__).with_name("a_main_cubic_census.csv")
rows = {row["d"]:row for row in csv.DictReader(path.open())}
print("Previously certified A.38 rank-zero exceptional rows:")
for d in ("1","2","4"):
    row=rows[d]
    assert row["analytic_rank"] == "0" and row["central_status"] == "nonzero"
    print("d=",d,"conductor=",row["conductor"],"Linterval=",row["arb_interval"])
print("All exact symbolic assertions passed.")
