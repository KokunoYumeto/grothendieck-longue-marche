"""Exact genus-two word checks for the six multicurve stabilizers.
The sphere outer action detects the quotient by the hyperelliptic C2;
the symplectic action distinguishes its two lifts, since W acts as -I.
"""
from pathlib import Path
import json
import sympy as S
P=Path(__file__).parent
H={};exec((P/'b_genus_zero.py').read_text().split('\ndata={}')[0],H)
red,inv,action,subst,conjugator=[H[k] for k in ('red','inv','action','subst','conjugator')]
def cat(*ws):return red(x for w in ws for x in w)
def conj(x,y):return cat(x,y,inv(x))
def outer_identity(w):
 imgs=action(6,w)
 elim=tuple((i,) for i in range(1,6))+(inv((1,2,3,4,5)),)
 imgs=tuple(subst(x,elim) for x in imgs[:5])
 try:
  c=conjugator(imgs[0],1)
  v=cat(inv(c),imgs[1],c);d=conjugator(v,2)
  if any(abs(x)!=1 for x in d):return False,None
  cc=cat(c,d)
  ok=all(imgs[i-1]==cat(cc,(i,),inv(cc)) for i in range(1,6))
  return ok,cc
 except AssertionError:return False,None
a=(1,);b=(3,);cc=(5,)
W=(1,2,3,4,5,5,4,3,2,1)
delta=(1,2,3,4,5)
t=(1,2,3,1,2,1)
rr=cat(cc,inv(b),(3,4)*3)
ee=cat(inv(a),rr)
q=delta*3
hL=(1,2)*3;hR=(4,5)*3
J=S.diag(S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,1],[-1,0]]))
chain=[(1,0,0,0),(0,1,0,0),(1,0,1,0),(0,0,0,1),(0,0,1,0)]
transvections=[S.eye(4)+S.Matrix(v)*(S.Matrix(v).T*J) for v in chain]
def symplectic(w):
 out=S.eye(4)
 for x in w:out=out*(transvections[x-1] if x>0 else transvections[-x-1].inv())
 return out
assert symplectic(W)==-S.eye(4)
u=cat(t,inv(cc))
v=cat((3,4,5,3,4,3),inv(a))
swap_dumbbell=cat(inv((1,2)),(4,5),q)
checks=[
 ('global W square',cat(W,W)),
 ('global full twist',delta*6),
 ('N chain',cat((3,4,5)*4,inv(a+a))),
 ('S hyperelliptic word',cat(W,inv(cat(hL,inv(hR))))),
 ('S q swaps first generator',cat(conj(q,a),(-4,))),
 ('S q swaps second generator',cat(conj(q,(2,)),(-5,))),
 ('B exchange square',cat(t,t,inv(cc+cc))),
 ('B exchange e',cat(conj(t,ee),inv(cat(W,cc,ee,inv(cc))))),
 ('B e square',cat(ee,ee)),
 ('B t exchanges a',cat(conj(t,a),inv(b))),
 ('B t exchanges b',cat(conj(t,b),inv(a))),
 ('B t fixes c',cat(conj(t,cc),inv(cc))),
 ('theta u square',cat(u,u)),
 ('theta v square',cat(v,v)),
 ('theta Coxeter cube',cat(*(u+v,)*3)),
 ('theta u swaps a,b',cat(conj(u,a),inv(b))),
 ('theta v swaps b,c',cat(conj(v,b),inv(cc))),
 ('dumbbell swap square',cat(swap_dumbbell,swap_dumbbell)),
 ('dumbbell swap a,c',cat(conj(swap_dumbbell,a),inv(cc))),
 ('dumbbell swap c,a',cat(conj(swap_dumbbell,cc),inv(a))),
 ('dumbbell swap h',cat(conj(swap_dumbbell,hL),inv(cat(W,hL)))),
]
data=[]
for name,w in checks:
 ok,c=outer_identity(w)
 matrix=symplectic(w);lift=matrix==S.eye(4)
 print(name,'sphere',ok,'symplectic',lift,'inner conjugator length',None if c is None else len(c))
 assert ok and lift,(name,matrix)
 data.append(dict(name=name,word=w,sphere_outer_identity=ok,symplectic_identity=lift,inner_conjugator=c))
print('All',len(checks),'genus-two identities verified, including the central lift.')
(P/'b_genus2_checks.json').write_text(json.dumps(data,indent=2)+'\n')
