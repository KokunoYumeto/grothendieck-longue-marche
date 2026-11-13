"""Exact supplementary certificates for D.17, D.18 and D.23.

The symbolic identities are checked in the stated finite degree range.
They supplement the general written proofs; they are not an exhaustive
classification of rings or group schemes.
"""
from pathlib import Path
import itertools
import json
import sympy as sp

OUT = Path(__file__).with_suffix('.json')
T, U, n0, c, x, y, u, v, s = sp.symbols('T U n0 c x y u v s')

monic = []
for d in range(1, 9):
    aa = sp.symbols(f'a0:{d}')
    rel = c**d + sum(aa[i] * c**i for i in range(d))
    Q = (U-1)**d + sum(aa[i]*(T-n0)**(d-i)*(U-1)**i for i in range(d))
    assert sp.expand(Q.subs(U, 1+(T-n0)*c) - (T-n0)**d*rel) == 0
    D = sp.expand(Q.subs(U, 0))
    assert sp.expand(D.subs(T, n0)) == (-1)**d
    quotient, remainder = sp.div(sp.Poly(Q-D, U), sp.Poly(U, U))
    assert remainder.is_zero
    assert sp.expand(U*quotient.as_expr()+D-Q) == 0
    monic.append({'monic_degree': d, 'substitution_identity': True,
                  'D_at_n0': (-1)**d, 'division_by_U_identity': True})

# An actual nonnormal domain example: R=Q[s^2,s^3] localized at its cusp.
F = s**2 / (1+s*T)
N, D = s**2-s**3*T, 1-s**2*T**2
assert sp.cancel(F-N/D) == 0
assert D.subs(T, 0) == 1
cusp = {
    'ring': 'Q[s^2,s^3]_(s^2,s^3)',
    'F': str(F), 'numerator_in_R': str(N), 'denominator_in_R': str(D),
    'identity_verified': True, 'D_at_0': 1,
    'coefficient_exponents': sorted({term[0][0] for P in (N,D)
                                    for term in sp.Poly(P, s,T).terms()}),
    'reason_all_integer_values_are_integral': 'D(n)=1-n^2*s^2 is a unit in the displayed local ring for every integer n.'
}

# A primary ring with nonsaturated naive nilradical powers:
# A=Q[x,e,f]/(e^2-x*f,e*f,f^2), localized at (x,e,f).
# It is free on 1,e,f over Q[x]; the total quotient ring is
# Q(x)[e]/e^3, with f=e^2/x. Thus I2=(f) but p^2=(x*f).
def mul(a, b):
    return tuple(map(sp.expand, (a[0]*b[0], a[0]*b[1]+a[1]*b[0],
                               a[0]*b[2]+a[2]*b[0]+x*a[1]*b[1])))

basis = [(1,0,0),(0,1,0),(0,0,1)]
for a,b,cvec in itertools.product(basis, repeat=3):
    assert mul(mul(a,b),cvec) == mul(a,mul(b,cvec))
assert mul(basis[1],basis[1]) == (0,0,x)
assert mul(basis[1],basis[2]) == (0,0,0)
assert mul(basis[2],basis[2]) == (0,0,0)
primary = {
    'ring': 'Q[x,e,f]/(e^2-x*f,e*f,f^2), localized at (x,e,f)',
    'basis_over_Qx': ['1','e','f'],
    'all_basis_associativity_triples_checked': 27,
    'p_squared': '(x*f)', 'saturated_I2': '(f)',
    'generic_relation': 'f=e^2/x in Q(x)[e]/e^3',
    'finite_certificate_only': True
}

# The required computable counterexample check for D.23.
# Scaling the additive coordinate gives a group homomorphism, but
# the generic-identification-preserving scale 2 collapses over F_2.
scale = sp.symbols('scale')
assert sp.expand(scale*(x+u*y) - (scale*x+u*scale*y)) == 0
finite_scalings = []
for p in (2,3,5,7):
    pts = [(a,b) for a in range(p) for b in range(1,p)]
    def law(a,b): return ((a[0]+a[1]*b[0])%p, a[1]*b[1]%p)
    for q in (1,2,3,6):
        def phi(a): return (q*a[0]%p, a[1])
        for a,b in itertools.product(pts,repeat=2):
            assert phi(law(a,b)) == law(phi(a),phi(b))
        image = {phi(a) for a in pts}
        kernel = [a for a in pts if phi(a)==(0,1)]
        finite_scalings.append({'p':p,'scale':q,'group_order':len(pts),
                                'image_order':len(image),'kernel_order':len(kernel),
                                'all_group_law_pairs_checked':len(pts)**2})
assert next(row for row in finite_scalings if row['p']==2 and row['scale']==2)['kernel_order']==2

result = {'status':'PASS',
          'scope':'Exact finite symbolic and finite-field certificates; all general theorems are proved in sections/D_surface.tex.',
          'monic_denominator_identities_degrees_1_to_8':monic,
          'nonnormal_cusp_example':cusp,
          'saturated_primary_filtration_example':primary,
          'D23_group_scaling_checks':finite_scalings,
          'D23_F2_nonisomorphism_witness':{'input':[1,1],'image_under_scale_2':[0,1],
                                        'nonidentity_input':True,'identity_image':True}}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: monic denominator identities in degrees 1–8; exact cusp denominator; 27 primary-ring basis triples; 16 finite scaling maps with all multiplication pairs checked.')
print('D.23 witness: over F2, (1,1) is nonidentity and maps to (0,1) under the generic-identity model map (z,u)↦(2z,u).')
print('These finite certificates supplement the written infinite proofs; no ring classification is claimed.')
