#!/usr/bin/env python3
"""Exact twisted graph over the actual A_* semidirect Q quotient.

This is the order46656 quotient from D56, not a substitute finite base.
The four representative nonzero character-pair blocks are computed over F4.
No arithmetic boundary is asserted to vanish by this module calculation.
"""
from pathlib import Path
from itertools import product
from collections import deque
import hashlib,json,time
import numpy as np

OUT=Path(__file__).resolve().parent
start=time.time()
paths=[OUT/'d_arithmetic_correction_graph.json',OUT/'d_arithmetic_affine_base.json']
D=json.loads(paths[0].read_text());A=json.loads(paths[1].read_text())
states=[tuple(x) for x in D['Q_states']];qi={v:i for i,v in enumerate(states)}
def normq(a):return min(tuple(a),tuple(-x%12 for x in a))
def mulq(a,b):
 x,y,z,w=a;p,q,r,s=b
 return normq(((x*p+y*r)%12,(x*q+y*s)%12,(z*p+w*r)%12,(z*q+w*s)%12))
tab=np.array([[qi[mulq(a,b)] for b in states] for a in states],dtype=np.int16)
S=qi[normq((0,1,11,0))];R=qi[normq((0,11,1,11))]
assert qi[normq((1,0,0,1))]==0
assert tab[:,S].tolist()==D['right_s'] and tab[:,R].tolist()==D['right_r']
inv=[next(j for j in range(576) if tab[i,j]==0) for i in range(576)]
qstar=[np.array(x,dtype=np.int16).T for x in A['Q_linear_image_matrices']]
to_star=np.array(A['Q_to_linear_image'],dtype=np.int16)
Qlin=np.array([qstar[j] for j in to_star],dtype=np.int16)
kr=[i for i,j in enumerate(to_star) if j==0]
assert len(kr)==12 and kr==A['Q_linear_kernel_states']
vr=np.array(A['affine_r_translation'],dtype=np.int16)
assert len(vr)==4
for g in range(576):
 for h in [S,R]:assert np.array_equal(Qlin[g]@Qlin[h]%3,Qlin[tab[g,h]])

qstar_index={tuple(M.ravel()):i for i,M in enumerate(qstar)}
star_tab=np.array([[qstar_index[tuple((a@b%3).ravel())] for b in qstar] for a in qstar],dtype=np.int16)
SS=int(to_star[S]);RR=int(to_star[R])
small_inv=[next(j for j in range(48) if star_tab[i,j]==0) for i in range(48)]

# F4=F2[z]/(z^2+z+1), encoded0,1,z,z+1.
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
INV=np.array([0,1,3,2],dtype=np.uint8)
FROB=np.array([0,1,3,2],dtype=np.uint8)
ZPOW=np.array([1,2,3],dtype=np.uint8)

def mm(a,b):
 a=np.asarray(a,dtype=np.uint8);b=np.asarray(b,dtype=np.uint8)
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out

def echelon(a):
 a=np.array(a,dtype=np.uint8,copy=True);piv=[];row=0
 for col in range(a.shape[1]):
  ids=np.flatnonzero(a[row:,col])
  if not len(ids):continue
  k=row+int(ids[0]);a[[row,k]]=a[[k,row]]
  a[row]=MUL[INV[a[row,col]],a[row]]
  fac=a[:,col].copy();fac[row]=0
  a^=MUL[fac[:,None],a[row,None,:]]
  piv.append(col);row+=1
  if row==a.shape[0]:break
 return a,piv

def rank(a):return len(echelon(a)[1])

def inverse(a):
 n=len(a);r,p=echelon(np.column_stack([a,np.eye(n,dtype=np.uint8)]))
 assert p[:n]==list(range(n)) and np.array_equal(r[:,:n],np.eye(n,dtype=np.uint8))
 return r[:,n:]

def line(v):
 v=tuple(int(x)%3 for x in v);a=next(x for x in v if x)
 return tuple(x*pow(a,-1,3)%3 for x in v)

lines=sorted({line(v) for v in product(range(3),repeat=4) if any(v)})
def act_line(g,ell):return line(np.array(ell,dtype=np.int16)@Qlin[inv[g]]%3)
orbits=[];seen=set()
for ell in lines:
 if ell in seen:continue
 orb=sorted({act_line(g,ell) for g in range(576)})
 seen.update(orb);orbits.append((ell,orb))
assert sorted(len(x[1]) for x in orbits)==[8,8,12,12]

def graph(ell,T,s,r,Lin):
 n=len(T);v2=[min(g,int(T[g,s])) for g in range(n)]
 v3=[min(g,int(T[g,r]),int(T[T[g,r],r])) for g in range(n)]
 re2=sorted(set(v2));re3=sorted(set(v3));ix2={v:i for i,v in enumerate(re2)};ix3={v:len(re2)+i for i,v in enumerate(re3)}
 phase=np.zeros(n,dtype=np.uint8)
 for root in re3:
  at=root;value=1
  for _ in range(3):
   phase[at]=value
   k=int(np.array(ell)@(Lin[at]@vr%3)%3)
   value=int(MUL[value,INV[ZPOW[k]]])
   at=int(T[at,r])
  assert at==root and value==1
 B=np.zeros((len(re2)+len(re3),n),dtype=np.uint8)
 for e in range(n):B[ix2[v2[e]],e]=1;B[ix3[v3[e]],e]=phase[e]
 rr,piv=echelon(B);assert len(piv)==len(B)
 free=[i for i in range(n) if i not in piv]
 basis=np.zeros((n,len(free)),dtype=np.uint8)
 basis[free,np.arange(len(free))]=1
 basis[np.array(piv),:]=rr[:,free]
 assert not np.any(mm(B,basis))
 return B,basis,free

def power(T,g,n):
 out=0
 for _ in range(n):out=int(T[out,g])
 return out

def cusp(ell,T,s,r,Lin):
 chain=np.zeros(len(T),dtype=np.uint8);at=0;v=np.zeros(4,dtype=np.int16)
 for _ in range(12):
  at=int(T[at,s])
  chain[at]^=ZPOW[int(np.array(ell)@v%3)]
  v=(v+Lin[at]@vr)%3
  at=int(T[at,r])
  chain[at]^=ZPOW[int(np.array(ell)@v%3)]
 assert at==0 and not np.any(v)
 return chain

records=[]
rng=np.random.default_rng(0xD60)
for ell,orb in orbits:
 B,U,free=graph(ell,tab,S,R,Qlin)
 b,u,f=graph(ell,star_tab,SS,RR,np.array(qstar))
 assert U.shape==(576,96) and u.shape==(48,8)
 projection=np.zeros((48,96),dtype=np.uint8)
 for i in range(576):projection[to_star[i]]^=U[i]
 theta=projection[f]
 assert rank(theta)==8 and np.array_equal(mm(u,theta),projection)
 a4=[]
 for g in kr:
  dest=np.zeros_like(U);dest[tab[g]]=U
  mat=dest[free]
  assert np.array_equal(mm(U,mat),dest)
  assert np.array_equal(mm(theta,mat),theta)
  a4.append(mat)
 # Exhibit eight exact regular A4 generators, not only a dimension match.
 trials=0
 while True:
  trials+=1;seeds=rng.integers(0,4,size=(96,8),dtype=np.uint8)
  regular=np.column_stack([mm(M,seeds[:,j:j+1]) for j in range(8) for M in a4])
  if rank(regular)==96:break
  assert trials<1000
 regular_inverse=inverse(regular)
 assert np.array_equal(mm(regular_inverse,regular),np.eye(96,dtype=np.uint8))
 theta_regular=mm(theta,regular)
 for j in range(8):assert all(np.array_equal(theta_regular[:,12*j],theta_regular[:,12*j+k]) for k in range(12))
 assert rank(theta_regular[:,::12])==8
 a4_perms=[]
 for g in kr:
  perm=[12*j+kr.index(int(tab[g,h])) for j in range(8) for h in kr]
  M=a4[kr.index(g)]
  assert np.array_equal(mm(M,regular),regular[:,perm])
  a4_perms.append(perm)
 # The actual cusp radical is retained as a submodule, rather than inferred
 # solely from Euler characteristics.
 c=cusp(ell,tab,S,R,Qlin);cc=cusp(ell,star_tab,SS,RR,np.array(qstar))
 assert not np.any(mm(B,c[:,None])) and not np.any(mm(b,cc[:,None]))
 t=int(tab[S,R]);tt=int(star_tab[SS,RR]);tp=[power(tab,t,n) for n in range(12)];ttp=[power(star_tab,tt,n) for n in range(12)]
 cr=sorted({min(int(tab[g,h]) for h in tp) for g in range(576)})
 ccr=sorted({min(int(star_tab[g,h]) for h in ttp) for g in range(48)})
 C=[];smallC=[]
 # The scalar factor from a pure Q lift is1.  These character components
 # need not individually be cycles unless the character is transported;
 # use the literal cusp conjugate word, whose phase is directly known.
 for g in cr:
  oldell=np.array(ell)@Qlin[g]%3
  c0=cusp(tuple(oldell),tab,S,R,Qlin)
  dest=np.zeros(576,dtype=np.uint8);dest[tab[g]]=c0
  assert not np.any(mm(B,dest[:,None]))
  C.append(dest[free])
 for g in ccr:
  oldell=np.array(ell)@qstar[g]%3
  c0=cusp(tuple(oldell),star_tab,SS,RR,np.array(qstar))
  dest=np.zeros(48,dtype=np.uint8);dest[star_tab[g]]=c0
  assert not np.any(mm(b,dest[:,None]))
  smallC.append(dest[f])
 C=np.array(C,dtype=np.uint8).T;smallC=np.array(smallC,dtype=np.uint8).T
 assert C.shape==(96,48) and rank(C)==48
 assert smallC.shape==(8,4) and rank(smallC)==4
 assert rank(mm(theta,C))==4
 # All actual pair-stabilizer actions, in the same A4-free basis.
 stabilizer=[g for g in range(576) if act_line(g,ell)==ell]
 actions=[]
 for g in stabilizer:
  image=np.array(ell)@Qlin[inv[g]]%3
  flip=tuple(image)!=ell
  assert tuple(image) in (ell,tuple(-x%3 for x in ell))
  dest=np.zeros_like(U);dest[tab[g]]=U
  if flip:dest=FROB[dest]
  mat=dest[free]
  assert np.array_equal(mm(U,mat),dest)
  mr=mm(mm(regular_inverse,mat),FROB[regular] if flip else regular)
  actions.append({'q_state':g,'flip':flip,'columns':mr.T.tolist()})
 assert len(stabilizer)*len(orb)==576
 records.append({'character':ell,'orbit':orb,'stabilizer_order':len(stabilizer),
                 'source_basis_columns':U.T.tolist(),'source_free_edges':free,
                 'target_basis_columns':u.T.tolist(),'target_free_edges':f,
                 'homology_projection_columns':theta.T.tolist(),
                 'regular_A4_basis_columns':regular.T.tolist(),'regular_A4_inverse_rows':regular_inverse.tolist(),
                 'A4_left_permutations':a4_perms,'regular_A4_trials':trials,
                 'regular_projection_columns':theta_regular.T.tolist(),
                 'cusp_columns':C.T.tolist(),'target_cusp_columns':smallC.T.tolist(),
                 'all_stabilizer_actions':actions})
 print(json.dumps({'character':ell,'orbit_size':len(orb),'stabilizer_order':len(stabilizer),
                   'homology_dimensions':[96,8],'projection_rank':8,'cusp_ranks':[48,4],
                   'A4_free_rank':8,'regular_basis_trials':trials}),flush=True)

result={'summary':{'status':'PASS','actual_source_base_order':46656,'target_base_order':3888,
                   'source_free_rank':7777,'target_free_rank':649,'base_kernel':'A4',
                   'odd_source_kernel_dimension':93,'pair_orbit_sizes':[len(x[1]) for x in orbits],
                   'residual_dimension':40*(96*96-8*8),'all_four_actual_character_modules_checked':True,
                   'arithmetic_boundary_solved':False,'elapsed_seconds':time.time()-start},
        'Q_states':states,'Q_multiplication':tab.tolist(),'A4_states':kr,
        'character_blocks':records,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_arithmetic_A4_twisted.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
