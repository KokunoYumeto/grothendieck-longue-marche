"""Exact finite identities for the dyadic Prym Kummer comparison.

The proof covers every possible x-valuation.  This program checks the
residue cases, duplication identity, and complete torsion-bound counts.
It does not infer a rank or a global Selmer-group size.
"""
from pathlib import Path
import json, math
import sympy as s

base=Path(__file__).resolve().parent
M=7*13*23*139*1119169
assert M==325596479663 and M%2==1 and 573%8==5

def mul(z,w):
    return ((z[0]*w[0]+2*z[1]*w[1])%8,
            (z[0]*w[1]+z[1]*w[0])%4)
units=[(a,c) for a in range(1,8,2) for c in range(4)]
squares=sorted({mul(z,z) for z in units})
assert squares==[(1,0),(3,2)]
def v2(n):
    return 1000 if not n else (abs(n)&-abs(n)).bit_length()-1
def vp(z):
    return min(2*v2(z[0]),2*v2(z[1])+1)
residue_rows=[]
for z2 in squares:
    plus=((z2[0]+573)%8,z2[1])
    minus=((z2[0]-573)%8,z2[1])
    plus_v,minus_v=vp(plus),vp(minus)
    assert plus_v<5 and minus_v<5
    rhs_v=3+plus_v
    doubled_x_v=2*minus_v-plus_v-3
    residue_rows.append(dict(unit_square=z2,plus=plus,minus=minus,
                             plus_v=plus_v,minus_v=minus_v,
                             curve_rhs_v=rhs_v,doubled_x_v=doubled_x_v))
assert residue_rows[0]['curve_rhs_v']==5
assert residue_rows[1]['curve_rhs_v']==6
assert residue_rows[1]['doubled_x_v']==-2

x,y,b=s.symbols('x y b',nonzero=True)
slope=(3*x*x+b)/(2*y)
x2=slope*slope-2*x
formula=(x*x-b)**2/(4*x*(x*x+b))
assert s.factor((x2-formula).subs(y*y,x**3+b*x))==0

# The other valuation cases are exact linear identities, not sampling
# of field points.  Positive r>1 has 2r>v(b)=2; negative r has 2r<2.
r=s.symbols('r',integer=True)
assert s.expand(4*r-(4+3*r))==r-4
assert s.expand(4-(4+r+2))==-r-2
assert 0-(4+0+0)==-4

reductions=[]
for p,expected in [(17,10),(41,52)]:
    roots=[t for t in range(p) if t*t%p==2]
    assert len(roots)==2
    for t in roots:
        bp=1146*(1+t)**2*M*M%p
        assert bp and (-64*bp**3)%p
        affine=[(xx,yy) for xx in range(p) for yy in range(p)
                if (yy*yy-xx**3-bp*xx)%p==0]
        count=1+len(affine)
        assert count==expected
        reductions.append(dict(p=p,sqrt2=t,b=bp,count=count,affine_points=affine))
assert math.gcd(10,52)==2 and 52%17 and 10%41

data=dict(unit_squares_mod_pi5=squares,valuation_one_rows=residue_rows,
          good_reductions=reductions,
          exact_bound='v_pi(x([2^n]P)) <= 2-4n for every nonzero double image, n>=1',
          scope='Local Kummer injectivity and global torsion; no rank or full Selmer conclusion.')
(base/'harmonic_prym_dyadic_injection_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: all16 unit residues modulo pi^5 give exactly the two displayed square residues.')
for row in residue_rows:print('Valuation-one case:',row)
print('PASS: literal duplication formula and all remaining valuation-case identities.')
for row in reductions:print('Complete good reduction:',{k:v for k,v in row.items() if k!='affine_points'})
print('PASS: torsion bound gcd(10,52)=2, with residue characteristics17,41 handled explicitly.')
print('The proof supplies the arbitrary-depth bound and the actual Kummer and boundary maps.')
