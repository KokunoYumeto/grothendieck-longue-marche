"""Finite quotient and integral cocycle for S=SL_2(Z)/[Pi_0,Pi_0]."""
from collections import deque
from itertools import product, permutations
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.eye(2)
rho=s.Matrix([[0,1],[-1,1]])
sigma=s.Matrix([[0,-1],[1,0]])
l0=-sigma*rho*sigma*rho
l1=-rho*sigma*rho*sigma
assert rho*l0*rho.inv()==l1
assert rho*l1*rho.inv()==(l1*l0).inv()
assert sigma*l0*sigma.inv()==l1
assert sigma*l1*sigma.inv()==l0

def mod(M,n=4):return tuple(int(x)%n for x in M)
def mat(t):return s.Matrix(2,2,t)
def mul(a,b):return mod(mat(a)*mat(b))
def inv(a):
    x,y,z,w=a
    k=pow((x*w-y*z)%4,-1,4)
    return ((k*w)%4,(-k*y)%4,(-k*z)%4,(k*x)%4)
E=mod(I);rr=mod(rho);ss=mod(sigma)
def closure(gens):
    seen={E};todo=[E]
    for a in todo:
        for b in gens:
            c=mul(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
G4=closure([rr,ss]);V=closure([mod(l0),mod(l1)])
assert len(G4)==48 and len(V)==4
assert all(mul(mul(g,v),inv(g)) in V for g in G4 for v in V)
tauprime=s.Matrix([[0,1],[1,0]])
GL4=closure([rr,ss,mod(tauprime)])
assert len(GL4)==96
assert all(mul(mul(g,v),inv(g)) in V for g in GL4 for v in V)
assert tauprime*l0*tauprime==l1.inv()
assert tauprime*l1*tauprime==l0.inv()
def cos(g):return min(mul(v,g) for v in V)

R=s.Matrix([[0,-1],[1,-1]])
S=s.Matrix([[0,1],[1,0]])
zero=s.zeros(2,1);bb=s.Matrix([s.Rational(1,3),-s.Rational(1,3)])
gens=[('r',rr,R,zero),('s',ss,S,bb)]
reps={cos(E):{'matrix':E,'word':'','action':I,'translation':zero}}
todo=list(reps)
for h in todo:
    a=reps[h]
    for name,g,B,t in gens:
        m=mul(a['matrix'],g);k=cos(m)
        if k not in reps:
            reps[k]={'matrix':m,'word':a['word']+name,
                     'action':a['action']*B,
                     'translation':a['translation']+a['action']*t}
            todo.append(k)
assert len(reps)==12
keys=list(reps);index={h:i for i,h in enumerate(keys)}
unit=index[cos(E)]
mult=[];coc=[]
for h in keys:
    row=[];crow=[]
    for k in keys:
        a,b=reps[h],reps[k];hk=cos(mul(a['matrix'],b['matrix']))
        z=a['translation']+a['action']*b['translation']-reps[hk]['translation']
        assert all(x.q==1 for x in z)
        assert a['action']*b['action']==reps[hk]['action']
        row.append(index[hk]);crow.append(tuple(int(x) for x in z))
    mult.append(row);coc.append(crow)
for h,k,l in product(range(12),repeat=3):
    lhs=s.Matrix(coc[h][k])+s.Matrix(coc[mult[h][k]][l])
    rhs=reps[keys[h]]['action']*s.Matrix(coc[k][l])+s.Matrix(coc[h][mult[k][l]])
    assert lhs==rhs

def groupmul(x,y,n):
    h,a,b=x;k,c,d=y
    v=s.Matrix([a,b])+reps[keys[h]]['action']*s.Matrix([c,d])+s.Matrix(coc[h][k])
    return (mult[h][k],int(v[0])%n,int(v[1])%n)

ri=index[cos(rr)];si=index[cos(ss)]
finite=[]
for n in [1,2,3,4,8,9]:
    ident=(unit,0,0);seen={ident};todo=[ident]
    for a in todo:
        for b in [(ri,0,0),(si,0,0)]:
            c=groupmul(a,b,n)
            if c not in seen:seen.add(c);todo.append(c)
    assert len(seen)==12*n*n
    finite.append({'n':n,'size_H_n':len(seen),'expected':12*n*n})

# A rational representation not admitted by the quasi-unipotent envelope.
# Induce chi: M -> Q^*, chi(lambda0)=2, chi(lambda1)=1, from index-12 M.
def induced(g):
    T=s.zeros(12)
    for h in range(12):T[h,mult[h][g]]=s.Integer(2)**coc[h][g][0]
    return T
ir,isg=induced(ri),induced(si)
assert ir**6==s.eye(12) and isg**4==s.eye(12) and ir**3==isg**2
il0=ir**3*isg*ir*isg*ir
il1=ir**3*ir*isg*ir*isg
assert il0*il1==il1*il0
assert all(il0[i,j]==0 for i,j in product(range(12),repeat=2) if i!=j)
eigen=[str(il0[i,i]) for i in range(12)]
assert '2' in eigen

# Three-letter covering from the BISITE lead. Composition is rightmost first.
def pmul(a,b):return tuple(a[b[i]] for i in range(3))
def pinv(a):return tuple(a.index(i) for i in range(3))
a=(1,0,2);b=(2,1,0)
comm=pmul(pmul(pmul(a,b),pinv(a)),pinv(b))
after=pmul(b,comm)
assert after==a
def orbits(gens):
    todo=set(range(3));out=[]
    while todo:
        q=[min(todo)];seen=set(q)
        for x in q:
            for g in gens:
                if g[x] not in seen:seen.add(g[x]);q.append(g[x])
        todo-=seen;out.append(sorted(x+1 for x in seen))
    return out
assert orbits([a,b])==[[1,2,3]]
assert orbits([a,after])==[[1,2],[3]]

data={
 'SL2_Z4_size':len(G4),'V4_size':len(V),'V4':[list(x) for x in sorted(V)],
 'GL2_Z4_size':len(GL4),'orientation_quotient_size':len(GL4)//len(V),
 'H_size':12,'representatives':[{'id':i,'word':reps[h]['word'] or '1',
             'matrix_mod4':list(reps[h]['matrix']),
             'action':[int(x) for x in reps[h]['action']],
             'translation':[str(x) for x in reps[h]['translation']]} for i,h in enumerate(keys)],
 'multiplication':mult,'cocycle':coc,'cocycle_triples_checked':12**3,
 'finite_quotients':finite,
 'finite_stage_Fp_counts':[{'p':p,'size':12*p*p} for p in (2,3,5,7,11,13)],
 'induced_representation':{'rho':[[str(x) for x in ir.row(i)] for i in range(12)],
                         'sigma':[[str(x) for x in isg.row(i)] for i in range(12)],
                         'lambda0_eigenvalues':eigen},
 'BISITE_cover':{'before_orbits':orbits([a,b]),'after_orbits':orbits([a,after]),
                'commutator':comm,'new_y':after}}
(OUT/'E_envelope.json').write_text(json.dumps(data,indent=2)+'\n')
print('SL2(Z/4):',len(G4),'; normal V4:',len(V),'; quotient H:',len(keys))
print('GL2(Z/4):',len(GL4),'; orientation quotient:',len(GL4)//len(V),'; tauprime action = -S')
print('Integral extension cocycle:',12**3,'associativity triples PASS')
print('id word A_h flattened translation t_h')
for r in data['representatives']: print(r['id'],r['word'],r['action'],r['translation'])
print('Quotients S/nM:',finite)
print('Finite-stage model counts:',data['finite_stage_Fp_counts'])
print('Induced rational representation: defining relations PASS; lambda0 eigenvalues:',eigen)
print('BISITE covering orbits:',orbits([a,b]),'->',orbits([a,after]))
