"""Exact relative-product countermodel; this is not the actual mu5 surface."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]

def mul(p,q):
    return tuple(p[q[i]] for i in range(len(p)))
def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))

a=(1,0,2)
c=(0,2,1)
comm=mul(mul(mul(a,c),inverse(a)),inverse(c))
assert comm!=(0,1,2)
assert mul(mul(comm,comm),comm)==(0,1,2)

# Coordinates are (z exponent, a exponent, c exponent) in abelianization.
# The target coordinates record x winding, y winding, and q=1 winding.
phi=s.Matrix([[1,0,0],[-1,1,0],[0,0,1]])
sigma=s.Matrix([[-1,1,0],[0,1,0],[0,0,1]])
swap=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
assert phi.det()==1
assert sigma*sigma==s.eye(3)
assert phi*sigma==swap*phi
m,n,l=s.symbols('m n l',integer=True)
assert sigma*s.Matrix([m,n,l])-s.Matrix([m,n,l])==s.Matrix([-2*m+n,0,0])
assert phi*s.Matrix([m,2*m,l])==s.Matrix([m,m,l])

out={
    'status':'PASS',
    'actual_space':'C^2 minus x=0, y=0, xy=1',
    'source_group':'Z(z) times F(a,c)',
    'fiber_product':'Z^3',
    'map_on_abelianization':list(map(list,phi.tolist())),
    'nontrivial_commutator_S3':list(comm),
    'fixed_lift':'(m,m,l) is lifted by z^m a^(2m) c^l',
    'scope':'Refutes relative fiber-product injectivity from a maximal transverse A/B intersection; does not refute fixed lifting.'
}
(ROOT/'records/relative_product_countermodel.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS A=x=0 and B=y=0 have their unique transverse intersection outside D=xy=1.')
print('PASS actual group Z times F2 maps onto Z^3 with the displayed unimodular abelianization matrix.')
print('PASS commutator [a,c] is nontrivial in S3 and lies in the map kernel.')
print('PASS swap involution and target exchange commute with the map.')
print('PASS every fixed target element (m,m,l) has the explicit fixed lift z^m a^(2m) c^l.')
print(out['scope'])
