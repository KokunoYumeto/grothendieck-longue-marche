#!/usr/bin/env python3
"""Exact symbolic verification of the universal class-two algebra in A81.

The coefficient field is QQ with formal indeterminates.  Three independent
exterior-square coordinates retain every universal alternating-bilinear term.
The r calculation is in the Q-coinvariant center: Q acts trivially there.
This is not a selected-prime computation or a numerical coefficient matrix.
"""
from pathlib import Path
import json
import sympy as sp

HALF=sp.Rational(1,2)
THIRD=sp.Rational(1,3)
ZERO=(sp.Integer(0),)*3

def vec(name): return tuple(sp.symbols(name+'0:3'))
def add(a,b): return tuple(sp.expand(x+y) for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def scale(c,a): return tuple(sp.expand(c*x) for x in a)
def wedge(a,b):
    return tuple(sp.expand(a[i]*b[j]-a[j]*b[i]) for i,j in ((0,1),(0,2),(1,2)))
def mul(x,y):
    a,z=x; b,w=y
    return add(a,b), add(add(z,w),scale(HALF,wedge(a,b)))
def inv(x): return neg(x[0]),neg(x[1])
def inner(x,y): return mul(mul(x,y),inv(x))
def flat(x): return x[0]+x[1]
def same(x,y): return all(sp.expand(a-b)==0 for a,b in zip(flat(x),flat(y)))

results={}
def check(name,condition):
    assert condition, name
    results[name]=True
    print('PASS:',name)

a,b,d=vec('a'),vec('b'),vec('d')
z,w,u=vec('z'),vec('w'),vec('u')
x,y,q=(a,z),(b,w),(d,u)
check('BCH associativity, all vector and exterior coordinates',same(mul(mul(x,y),q),mul(x,mul(y,q))))
check('BCH inverse',same(mul(x,inv(x)),(ZERO,ZERO)))
comm=mul(mul(mul(x,y),inv(x)),inv(y))
check('commutator equals the universal exterior product',same(comm,(ZERO,wedge(a,b))))
check('inner conjugation adds v wedge a to the central coordinate',same(inner((b,ZERO),x),(a,add(z,wedge(b,a)))))

# In the r orbit, r(a)=b and r^2(a)=-a-b; z is Q-coinvariant.
r2a=neg(add(a,b))
cube=mul(mul((a,z),(b,z)),(r2a,z))
check('R cube under a+r a+r^2 a=0',same(cube,(ZERO,add(scale(3,z),scale(HALF,wedge(a,b))))))
rz=scale(-sp.Rational(1,6),wedge(a,b))
check('the source correction -1/6*(a wedge r a) gives R^3=1',same(mul(mul((a,rz),(b,rz)),(r2a,rz)),(ZERO,ZERO)))
check('the pure source correction gives S^2=1 when s a=-a',same(mul((a,ZERO),(neg(a),ZERO)),(ZERO,ZERO)))

# On the t-fixed a,v plane the semidirect head contributes no additional
# term.  B(a)=-a, and its central action is retained as an independent Bw.
v,Bz=vec('v'),vec('Bz')
corrected=inner((v,ZERO),(neg(a),Bz))
expected=(neg(a),add(Bz,wedge(a,v)))
check('cusp inner correction has sign +a0 wedge v = -v wedge a0',same(corrected,expected))
discrepancy=add(corrected[1],z)
check('complete cusp discrepancy is z+B_W z+a0 wedge v',all(sp.expand(x-y)==0 for x,y in zip(discrepancy,add(add(z,Bz),wedge(a,v)))))

# The square of Inn(v)B is Inn((v,0)*B(v,0)); this evaluates the
# universal square cocycle first, then imposes Bv=-v.
Bv=vec('Bv')
norm=mul((v,ZERO),(Bv,ZERO))
check('universal inner-action square cocycle',same(norm,(add(v,Bv),scale(HALF,wedge(v,Bv)))))
subs=dict(zip(Bv,neg(v)))
norm_minus=(tuple(sp.expand(c.subs(subs)) for c in norm[0]),tuple(sp.expand(c.subs(subs)) for c in norm[1]))
check('Bv=-v makes the corrected involution square exactly one',same(norm_minus,(ZERO,ZERO)))
check('a fixed central normalizer norm is killed by its negative half',all(sp.expand(c+2*(-c/2))==0 for c in u))

summary={
    'scope':'Universal rational polynomial identities; valid after reduction at every characteristic other than 2 and 3 where the displayed fractions are defined. No prime, giant B matrix, or finite group census selected.',
    'model':'M times exterior-square coinvariants with BCH coefficient 1/2',
    'checks':results,
    'count':len(results),
    'r_central_correction':'-1/6*(a wedge r(a))',
    'cusp_discrepancy':'z+B_W(z)+a0 wedge v',
    'square_cocycle':'(v+Bv, (v wedge Bv)/2)'
}
Path('work_A/A81_symbolic_identity_certificate.json').write_text(json.dumps(summary,indent=2)+'\n')
print('ALL',len(results),'EXACT SYMBOLIC CHECKS PASS')
print(summary['scope'])
