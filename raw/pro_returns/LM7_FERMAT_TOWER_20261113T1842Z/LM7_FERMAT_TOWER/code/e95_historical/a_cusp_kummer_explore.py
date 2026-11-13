#!/usr/bin/env python3
"""Exact framed-cusp Kummer calculations for the E95 continuation."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import importlib.util
import json
import sympy as s

BASE=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER/code'
spec=importlib.util.spec_from_file_location('e95_cubic',BASE/'e_cubic_abelian.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
K=mod.K;zeta=K(0,1);lam=1-zeta
labels=['A0','A1','A2','B0','B1','B2','C1','C2']
alllabels=['C0']+labels
coords={'C0':(0,0),'A0':(1,0),'A1':(2,2),'A2':(0,1),'B0':(2,0),
        'B1':(1,1),'B2':(0,2),'C1':(2,1),'C2':(1,2)}
inverse={v:k for k,v in coords.items()}
points={**{'A'+str(i):(K(0),-zeta**i,K(1))for i in range(3)},
        **{'B'+str(i):(-zeta**i,K(0),K(1))for i in range(3)},
        **{'C'+str(i):(K(1),-zeta**i,K(0))for i in range(3)}}
data=json.loads((BASE/'e_wild_layers.json').read_text())['layers']
T=s.Matrix(data['1']['input_tau']);J=s.Matrix(data['1']['input_c'])
U=s.Matrix([[v,-u]for d in labels for u,v in [coords[d]]])
j=s.Matrix.vstack(3*s.eye(2),U);pi=s.eye(10)[:2,:]
assert T*j==j*T[:2,:2] and J*j==j*J[:2,:2]

def integral3(M):return all(int(s.Rational(x).q)%3 for x in M)
def equivalent(a,b):return integral3((T-s.eye(10)).inv()*(a-b))
def groupadd(a,b):return inverse[tuple((x+y)%3 for x,y in zip(coords[a],coords[b]))]
def neg(a):return inverse[tuple(-x%3 for x in coords[a])]

def leading(line,at):
    a,b,c=line;i=int(at[1]);zz=zeta**i
    terms={'A':[(0,c-b*zz),(1,a),(3,-b*zz/3)],
           'B':[(0,c-a*zz),(1,b),(3,-a*zz/3)],
           'C':[(0,a-b*zz),(1,c),(3,-b*zz/3)]}[at[0]]
    return next((n,x)for n,x in terms if x!=0)

def tangent(at):
    i=int(at[1])
    return {'A':(K(0),K(1),zeta**i),'B':(K(1),K(0),zeta**i),
            'C':(K(1),zeta**(2*i),K(0))}[at[0]]

def chord(a,b):
    if a==b:return tangent(a)
    x,y=points[a],points[b]
    out=(x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
    assert any(z!=0 for z in out)
    assert sum((out[i]*points[a][i]for i in range(3)),K(0))==0
    assert sum((out[i]*points[b][i]for i in range(3)),K(0))==0
    return out

def unitform(x):
    for n in range(-20,21):
        for e in range(3):
            for sign in (1,-1):
                if x==sign*zeta**e*lam**n:return sign,e,n
    raise AssertionError(('not S unit',x.data()))

def kval(x,prime=False):
    sign,e,n=unitform(x)
    return 2*e+s.Rational(n,2)*(1 if prime else 3)

def ratioframes(num,den):
    records={}
    oN,loN=leading(num,'C0');oD,loD=leading(den,'C0');lo=loN/loD
    for d in alllabels:
        a,x=leading(num,d);b,y=leading(den,d)
        records[d]={'order':a-b,'value':x/y/lo}
    assert sum(x['order']for x in records.values())==0
    return records

def additionframes(a,b):
    assert a!='C0' and b!='C0'
    d=groupadd(a,b)
    num=chord(a,b)
    den=tangent('C0') if d=='C0' else chord(d,neg(d))
    records=ratioframes(num,den)
    expected={z:0 for z in alllabels}
    expected[a]+=1;expected[b]+=1;expected[d]-=1;expected['C0']-=1
    assert {z:r['order']for z,r in records.items()}==expected
    return records

def toruskum(records,prime=False):
    return s.Matrix([0,0]+[kval(records[d]['value'],prime)for d in labels])

def toruscoeff(records):
    ex=[unitform(records[d]['value'])for d in labels]
    return (s.Matrix([0,0]+[s.Rational(n,2)for sign,e,n in ex]),
            s.Matrix([0,0]+[e+s.Rational(n,2)for sign,e,n in ex]))

# All three point-torsion possibilities, after the exact elliptic carry.
base=s.Matrix([0,1,-1,-s.Rational(3,2),s.Rational(1,2),-1,
               -s.Rational(3,2),s.Rational(1,2),-3,1])
tors=s.zeros(10,3)
for col,(a,b)in enumerate([(3,4),(6,7),(8,9)]):tors[a,col]=2;tors[b,col]=-2
crosslines=[(K(1),zeta**2,K(1)),(zeta**2,K(1),K(1))]
unit_constraints=[]
for line in crosslines:
    frames=ratioframes(line,tangent('C0'))
    div=s.Matrix([[frames[d]['order']for d in labels]])
    row=(-div*U/3).row_join(div)
    assert integral3(row) and row*j==s.zeros(1,2)
    value=frames['A0']['value']
    unit_constraints.append((row,kval(value),kval(value,True),value))
survivors=[]
for eps in product(range(3),repeat=3):
    v=base+tors*s.Matrix(eps)
    ok=True
    for row,a,b,value in unit_constraints:
        d1=(row*v)[0]-a;d2=(row*J*v)[0]-b
        ok&=d1==d2 and integral3(s.Matrix([d1/6]))
    if ok:survivors.append(eps)
assert survivors==[(0,1,2),(1,0,1),(2,2,0)],survivors
assert all((e1,e2,e3)==((1-e2)%3,e2,(1+e2)%3)for e1,e2,e3 in survivors)
kp=base+tors*s.Matrix([1,0,1])

# The actual CM automorphism z -> zeta*z and its frame transport.
R=s.Matrix([[0,-1],[1,-1]])
cm={d:inverse[tuple(int(x)%3 for x in R*s.Matrix(coords[d]))]for d in alllabels}
S=s.zeros(8)
for col,d in enumerate(labels):S[labels.index(cm[d]),col]=1
Sigma=R.row_join(s.zeros(2,8)).col_join(((U*R-S*U)/3).row_join(S))
assert integral3(Sigma) and Sigma**3==s.eye(10) and Sigma*T==T*Sigma
assert Sigma*j==j*R
delta=s.Matrix([0,0]+[0 if d=='A2' else 2 for d in labels])
kq=Sigma*kp-delta

def buildpaths(prime=False):
    pp=J*kp if prime else kp
    paths={'C0':s.zeros(10,1),'A0':pp,'A2':Sigma*pp-delta}
    for a,b in [('A0','A0'),('A2','A2'),('A0','A2'),('A0','B1'),('A0','B2'),('B0','A2'),('B0','B2')]:
        d=groupadd(a,b)
        assert a in paths and b in paths
        value=paths[a]+paths[b]-toruskum(additionframes(a,b),prime)
        if d not in paths:paths[d]=value
    assert set(paths)==set(alllabels),set(paths)
    return paths
paths=buildpaths();pathsprime=buildpaths(True)
Tp=J*T*J
for d in labels:
    conjugated=inverse[(coords[d][0]-coords[d][1])%3,-coords[d][1]%3]
    assert integral3((Tp-s.eye(10)).inv()*(pathsprime[conjugated]-J*paths[d])),d
for a,b in product(labels,repeat=2):
    d=groupadd(a,b)
    defect=paths[a]+paths[b]-paths[d]-toruskum(additionframes(a,b))
    defectp=pathsprime[a]+pathsprime[b]-pathsprime[d]-toruskum(additionframes(a,b),True)
    h=(T-s.eye(10)).inv()*defect
    assert integral3(h) and (Tp-s.eye(10))*h==defectp,(a,b,d,h)

# Every displayed third multiple and every proper elliptic Kummer image.
triplechecks=[]
for d in labels:
    fr=ratioframes(tangent(d),tangent('C0'))
    assert equivalent(3*paths[d],toruskum(fr)),d
    target=(T[:2,:2]-s.eye(2))*s.Matrix(coords[d])/3
    assert integral3((T[:2,:2]-s.eye(2)).inv()*(paths[d][:2,:]-target)),d
    triplechecks.append(d)

# The phase is removed by an actual scalar Tate-basis change.
for t in range(3):
    Pu=s.eye(10)+t*j*pi
    assert Pu*T==T*Pu and Pu*J==J*Pu and integral3(Pu.inv())
    old=base+tors*s.Matrix([(1-t)%3,t,(1+t)%3])
    assert equivalent(Pu.inv()*old,kp),t
    h=(T-s.eye(10)).inv()*(Pu.inv()*old-kp)
    assert integral3(h) and J*h==h,(t,h)

# A full actual P-cocycle formula, retaining ordinary Kummer(3).
hplus=(s.eye(10)+J)*s.eye(10)[:,0]/2
qc=s.Matrix([0,0,0,0,0,0,s.Rational(1,4),-s.Rational(1,4),s.Rational(1,4),-s.Rational(1,4)])
hstar=hplus-qc
ct3=s.Matrix([0,0,1,1,1,2,s.Rational(1,2),s.Rational(1,2),s.Rational(3,2),s.Rational(3,2)])
ctz=s.Matrix([0,0,0,1,-1,0,s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2),-s.Rational(1,2)])
assert ct3+2*ctz+(T-s.eye(10))*hstar==3*s.eye(10)[:,1]
assert -ct3+2*ctz+(Tp-s.eye(10))*hstar==3*J*s.eye(10)[:,1]
br=s.Matrix([0,0,-1,-s.Rational(1,2),-s.Rational(1,2),-1,-s.Rational(1,2),-s.Rational(1,2),-1,-1])
bs=s.Matrix([0,0,0,s.Rational(1,2),-s.Rational(1,2),0,-s.Rational(1,2),s.Rational(1,2),0,0])
cp=(hstar/3,ct3/3+br,ctz/3+bs)
cq=(Sigma*cp[0],Sigma*cp[1],Sigma*cp[2]-delta/2)
coeff={'C0':(s.zeros(10,1),)*3,'A0':cp,'A2':cq}
for a,b in [('A0','A0'),('A2','A2'),('A0','A2'),('A0','B1'),('A0','B2'),('B0','B2')]:
    d=groupadd(a,b);rr,ss=toruscoeff(additionframes(a,b))
    coeff[d]=(coeff[a][0]+coeff[b][0],coeff[a][1]+coeff[b][1]-rr,coeff[a][2]+coeff[b][2]-ss)
assert set(coeff)==set(alllabels)
for d in labels:
    bb,rr,ss=coeff[d]
    assert (T-s.eye(10))*bb+rr+2*ss==paths[d]
    assert (Tp-s.eye(10))*bb-rr+2*ss==pathsprime[d]
    assert rr[:2,:]==ss[:2,:]==s.zeros(2,1)
symcoeff={}
sympaths={}
for d in labels:
    cd=inverse[((coords[d][0]-coords[d][1])%3,(-coords[d][1])%3)]
    bb=(coeff[d][0]+J*coeff[cd][0])/2
    rr=(coeff[d][1]-J*coeff[cd][1])/2
    ss=(coeff[d][2]+J*coeff[cd][2])/2
    symcoeff[d]=(bb,rr,ss)
    sympaths[d]=(T-s.eye(10))*bb+rr+2*ss
    assert integral3(sympaths[d]) and equivalent(sympaths[d],paths[d])
for d in labels:
    cd=inverse[((coords[d][0]-coords[d][1])%3,(-coords[d][1])%3)]
    assert symcoeff[cd][0]==J*symcoeff[d][0]
    assert symcoeff[cd][1]==-J*symcoeff[d][1]
    assert symcoeff[cd][2]==J*symcoeff[d][2]
assert sympaths['A0']==kp

print('PASS two exact framed-unit equations; the remaining phase is j(P).')
print('PASS actual CM/frame transport, all64 additions and all8 third multiples.')
print('PASS all proper Kummer projections and the three exact Tate-basis changes.')
print('PASS full P-cocycle formulas and the exact c-equivariant path representatives.')
for d in labels:print(d,[str(x)for x in sympaths[d]])
out={'status':'PASS','phase_solutions':survivors,
     'P_Kummer':[str(x)for x in kp],'CM_matrix':[[str(x)for x in row]for row in Sigma.tolist()],
     'CM_frame_correction':[str(x)for x in delta],
     'cusp_tau_Kummer':{d:[str(x)for x in paths[d]]for d in labels},
     'c_equivariant_cusp_tau_Kummer':{d:[str(x)for x in sympaths[d]]for d in labels},
     'global_cusp_coefficients':{d:{k:[str(x)for x in col]for k,col in zip(['rational_coboundary','Kummer3','Kummer_zeta'],symcoeff[d])}for d in labels},
     'unit_values':[x[3].data()for x in unit_constraints],
     'unit_equations':[[str(a)for a in x[0]]for x in unit_constraints]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
