"""Exact rank-five pure homology lattice and affine torsion centralizers.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_five_point_lattice.py
"""
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

E=[S.eye(5)[:,i] for i in range(5)]
pairs={}
for i in range(5):
    pairs[tuple(sorted((i,(i+1)%5)))]=E[i]
    pairs[tuple(sorted((i,(i+2)%5)))]=-E[i]-E[(i+1)%5]+E[(i+3)%5]
for i in range(5):assert sum((pairs[tuple(sorted((i,j)))] for j in range(5) if j!=i),S.zeros(5,1))==S.zeros(5,1)
def action(p):return S.Matrix.hstack(*(pairs[tuple(sorted((p[i],p[(i+1)%5])))] for i in range(5)))
perms={'a':(1,2,3,4,0),'b':(1,2,3,0,4),'d':(0,2,3,1,4)}
vectors={'a':S.ones(5,1),'b':S.Matrix([-1,-2,-1,1,1]),'d':S.Matrix([0,0,0,0,1])}
q=S.Matrix([[1,0,1,0,0],[0,1,0,0,0]])
zeta=S.Matrix([[0,0,0,1,1]])
data={}
for t,p in perms.items():
    A=action(p);v=vectors[t]
    assert A*v==v and (A-S.eye(5)).rank()==4
    sn=smith_normal_form(A-S.eye(5),domain=S.ZZ)
    data[t]={'matrix':A.tolist(),'primitive_fixed_vector':list(v),'Smith_diagonal':[int(sn[i,i])for i in range(5)],
             'forgetful_abelian_image':list(q*v),'zeta_on_fixed_vector_mod2':int((zeta*v)[0])%2}
assert list(q*vectors['b'])==[-2,-2]
assert list(q*vectors['d'])==[0,0]

# Verify that the abelianized b/d relation imposes no condition on the two
# independent invariant coefficients.
T1=action((1,0,2,3,4));B=action(perms['b']);D=action(perms['d'])
assert T1*B==D
for kb in range(-2,3):
    for kd in range(-2,3):
        beta=kb*vectors['b'];alpha=kd*vectors['d'];h=alpha-beta
        assert B*h==-beta+T1*(beta+h)

P=3
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j]for k in range(3))%P for j in range(3))for i in range(3))
I=((1,0,0),(0,1,0),(0,0,1))
A=((1,1,0),(0,1,0),(0,0,1));B3=((1,0,0),(2,1,0),(0,0,1));C=((1,1,1),(0,1,0),(0,0,1))
quartic=mul(mul(A,B3),C)
cubic=mul(A,quartic)
seen={I};todo=[I]
while todo:
    g=todo.pop()
    for h in (A,B3,C):
        k=mul(g,h)
        if k not in seen:seen.add(k);todo.append(k)
assert len(seen)==216
def block(g):return tuple(tuple(g[i][j] for j in range(2))for i in range(2))
centralizers={}
for label,t in [('quartic',quartic),('cubic',cubic)]:
    cent=[g for g in seen if mul(g,t)==mul(t,g)]
    proj={block(g)for g in cent}
    centralizers[label]={'matrix':t,'centralizer_order':len(cent),'linear_projection_order':len(proj),'linear_projection':sorted(proj)}
assert centralizers['quartic']['linear_projection_order']==4
assert centralizers['cubic']['linear_projection_order']==3
assert ((2,0),(0,2)) not in centralizers['cubic']['linear_projection']

def convert(x):
    if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [convert(v)for v in x]
    if isinstance(x,S.Integer):return int(x)
    return x
print(json.dumps(convert({'fixed_lattices':data,'abelianized_b_d_relation_all_independent_test_coefficients':True,
 'affine_image_order':len(seen),'affine_torsion_centralizers':centralizers,
 'interpretation':'The cubic frame has a canonical additive coefficient kappa_d; its parity equals epsilon_3(T) after including zeta, the central sign of the signed forgotten-point lift. No relation to epsilon_2(W) follows from the rank-five lattice alone.'}),indent=2))
