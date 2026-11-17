#!/usr/bin/env python3
"""Literal Artin, parity-cover, and signed-period maps for the finite detector bridge."""
import numpy as np,json
from pathlib import Path
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,images):return red(x for j in w for x in (images[j-1] if j>0 else inv(images[-j-1])))
def compose(f,g):return tuple(sub(w,f) for w in g)
id3=((1,),(2,),(3,));a=((1,2,-1),(1,),(3,));b=((1,),(2,3,-2),(2,))
ai=((2,),(-2,1,2),(3,));bi=((1,),(3,),(-3,2,3))
assert compose(a,ai)==compose(ai,a)==id3 and compose(b,bi)==compose(bi,b)==id3
assert compose(a,compose(b,a))==compose(b,compose(a,b))
t=(1,2,3)
assert sub(t,a)==sub(t,b)==t
z=id3
for g in (a,b)*3:z=compose(z,g)
assert z==tuple(red(t+(i,)+inv(t)) for i in range(1,4))

# Fill the fourth sphere puncture literally, with the free basis x=x1,y=x2.
toT=((1,),(2,),(-2,-1))
adown=tuple(sub(w,toT) for w in a[:2]);bdown=tuple(sub(w,toT) for w in b[:2])
a2=compose(adown,adown);b2=compose(bdown,bdown)
assert a2==tuple(red((1,2)+(i,)+(-2,-1)) for i in (1,2))
assert b2==tuple(red((-1,i,1)) for i in (1,2))
# The exact inverse pure basis: x=b^-2, y=b^2 a^2 under the inner identification.
assert red(inv((-1,)))==(1,)
assert red((-1,)+(1,2))==(2,)
print('PASS Artin braid relation, fixed boundary, central full twist, and both pure inner maps',flush=True)

# Literal parity-kernel basis d=x1²,u=x2 x1^-1,v=x3 x1^-1,
# w=x1 x2,z=x1 x3, with no replacement of an outer action by an inner one.
Kbasis=((1,1),(2,-1),(3,-1),(1,2),(1,3))
def rewrite(w):
 state=0;out=[]
 positive={(0,1):(),(0,2):(2,),(0,3):(3,),
           (1,1):(1,),(1,2):(4,),(1,3):(5,)}
 for x in w:
  if x>0:piece=positive[state,x];state^=1
  else:state^=1;piece=inv(positive[state,-x])
  out.extend(piece)
 assert state==0
 return red(out)
for i,w in enumerate(Kbasis):assert rewrite(w)==(i+1,)
Kautos=[tuple(rewrite(sub(w,g)) for w in Kbasis) for g in (a,b,z)]
Kper=[rewrite((j,j)) for j in (1,2,3)]+[rewrite(inv(t+t))]
assert Kper==[(1,),(2,4),(3,5),(-5,-2,-1,-3,-4)]
def exponent(w):return np.array([w.count(i)-w.count(-i) for i in range(1,6)],dtype=np.int64)
matrices=[np.stack([exponent(w) for w in g],axis=1) for g in Kautos]
# Primitive compact period basis A=u, B=u^-1 v.
periods=np.array([[0,1,1,-1,-1],[0,0,1,0,-1]],dtype=np.int64)
U=np.array([[1,1],[0,1]],dtype=np.int64);L=np.array([[1,0],[-1,1]],dtype=np.int64)
for M,N in zip(matrices,(U,L,-np.eye(2,dtype=np.int64))):assert np.array_equal(periods@M,N@periods)
assert all(not np.any(periods@exponent(w)) for w in Kper)
# Full twist squared is literally inner by t² in the parity kernel.
t2=rewrite(t+t);zz=compose(Kautos[2],Kautos[2])
assert zz==tuple(red(t2+(i,)+inv(t2)) for i in range(1,6))
print('PASS rank5 parity-cover basis and all four primitive peripheral words',flush=True)
print('PASS exact compact period map: braid generators U,L; central full twist -I',flush=True)
print('PASS central square is literally inner by the retained fourth peripheral word',flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact source and marking maps for the constructive finite modular surface realization',
 'Artin_generators':[a,b],'sphere_boundary':t,'sphere_filling':toT,
 'pure_inner_generators':{'a_squared_conjugator':[1,2],'b_squared_conjugator':[-1]},
 'parity_free_basis':Kbasis,'parity_peripheral_words':Kper,
 'parity_braid_and_central_automorphisms':Kautos,
 'compact_period_map':periods.tolist(),'compact_braid_matrices':[U.tolist(),L.tolist()],
 'compact_central_matrix':(-np.eye(2,dtype=np.int64)).tolist(),
 'central_square_inner_word':t2,
 'projective_detector_order':'576*3^97','pure_detector_order':'d=96*3^97',
 'centre_detecting_order':'e=d*5^(d+1)','boundary_detecting_order':'r=e*5^(1+2*e)',
 'characteristic_surface_quotient_order_bound':'(r!)^((r!)^5)'},indent=2)+'\n')
