#!/usr/bin/env python3
"""Integral obstruction map for the finite CM shadow's homology refinements."""
from pathlib import Path
from collections import deque
from contextlib import redirect_stdout
import io,json,runpy
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from sympy.polys.domains import ZZ
import numpy as np
ROOT=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):D=runpy.run_path(str(ROOT/'d_cm_shadow.py'))
Q,ix,one,qs,qr=D['Q'],D['ix'],D['one'],D['qs'],D['qr']
qm,adj,root,v2,v3=D['qm'],D['adj'],D['root'],D['v2'],D['v3']
E=len(Q);z=ix[one]
perms={q:np.array(D['all_left'][ix[q]],dtype=int) for q in Q}
def action(vec,q):
 ans=np.zeros(E,dtype=np.int64);ans[perms[q]]=vec;return ans
paths={root:np.zeros(E,dtype=np.int64)};queue=deque([root]);tree=set()
while queue:
 v=queue.popleft()
 for w,e in adj[v]:
  if w not in paths:
   p=paths[v].copy();p[e]+=1 if v[0]=='s' else -1
   paths[w]=p;tree.add(e);queue.append(w)
chords=[i for i in range(E) if i not in tree];C=[]
for i in chords:
 q=Q[i];c=paths[v2[q]]-paths[v3[q]];c[i]+=1;C.append(c)
assert np.array_equal(np.stack(C)[:,chords],np.eye(97,dtype=int))
columns=[c-action(c,qs) for c in C]+[action(c-action(c,qr),qs) for c in C]
L=sp.Matrix(np.stack(columns).T[chords,:].tolist())
S=smith_normal_form(L,domain=ZZ)
diag=[abs(int(S[i,i])) for i in range(97)]
Pr=np.zeros(E,dtype=np.int64);Pr[z]=1;Pr[ix[qr]]=-1
qt=qm(qs,qr);Pt=action(Pr,qs);ct=np.zeros(E,dtype=np.int64);gt=one
for j in range(12):ct+=action(Pt,gt);gt=qm(gt,qt)
assert gt==one
aug=L.row_join(sp.Matrix((-ct[chords]).tolist()))
SA=smith_normal_form(aug,domain=ZZ)
diaga=[abs(int(SA[i,i])) for i in range(97)]
assert diag==[1]*96+[2] and diaga==[1]*97
assert hermite_normal_form(aug)==sp.eye(97)
# Integral paths are chosen by exactly the same BFS as d_cm_shadow.py.
P={one:np.zeros(E,dtype=np.int64)};queue=deque([one])
while queue:
 q=queue.popleft()
 for g,Pg in ((qs,np.zeros(E,dtype=np.int64)),(qr,Pr)):
  qg=qm(q,g)
  if qg not in P:P[qg]=P[q]+action(Pg,q);queue.append(qg)
CI=np.stack(C).T
LI=np.array(L.tolist(),dtype=np.int64)
AI=np.array(aug.tolist(),dtype=np.int64)
def modular_solver(matrix,p):
 basis={}
 for j,col in enumerate(matrix.T):
  v=col.copy()%p;w=np.zeros(matrix.shape[1],dtype=np.int64);w[j]=1
  while np.any(v):
   pos=int(np.flatnonzero(v)[-1]);a=int(v[pos])
   if pos not in basis:
    ai=pow(a,-1,p);basis[pos]=(v*ai%p,w*ai%p);break
   bv,bw=basis[pos];v=(v-a*bv)%p;w=(w-a*bw)%p
 def solve(rhs):
  v=np.array(rhs,dtype=np.int64)%p;w=np.zeros(matrix.shape[1],dtype=np.int64)
  for pos in sorted(basis,reverse=True):
   a=int(v[pos]);bv,bw=basis[pos];v=(v-a*bv)%p;w=(w+a*bw)%p
  assert not np.any(v)
  assert np.array_equal(matrix@w%p,np.array(rhs)%p)
  return w
 return solve,len(basis)
solvers={p:modular_solver(AI,p)[0] for p in (2,3)}
def group_check(a,b,pa,pb,h,j):
 def mm(g,hg):return qm(g[0],hg[0]),(g[1]+action(hg[1],g[0]))%j
 def ii(g):
  qi=D['canon'](D['inv'](g[0]));return qi,(-action(g[1],qi))%j
 def pw(g,k):
  if k<0:return pw(ii(g),-k)
  ans=(one,np.zeros(E,dtype=np.int64))
  while k:
   if k&1:ans=mm(ans,g)
   g=mm(g,g);k//=2
  return ans
 def cc(g,hg):return mm(mm(g,hg),ii(g))
 def eq(g,hg):return g[0]==hg[0] and np.array_equal(g[1]%j,hg[1]%j)
 s=(qs,np.zeros(E,dtype=np.int64));r=(qr,Pr%j);t=mm(s,r)
 u=ii(t);v=mm(mm(s,u),s);x=pw(u,2);y=pw(v,2)
 ss=cc((b,pb%j),s);rr=cc((a,pa%j),r)
 lam=1+12*h;m=6*h;f=mm(s,ss)
 assert eq(mm(ss,rr),pw(t,lam))
 assert eq(mm(mm(mm(pw(u,lam),ii(f)),pw(v,lam)),f),mm(mm(ii(f),r),pw(x,-m)))
 assert eq(mm(mm(mm(ii(f),pw(v,lam)),f),pw(u,lam)),mm(mm(mm(v,u),pw(y,-m)),f))
 return True
refinements=[]
for row in D['records']:
 if not(row.get('finite_automorphism') and row.get('mod3_automorphism')):continue
 a=D['canon'](tuple(row['A']));b=D['canon'](tuple(row['beta']))
 error=P[b]-action(P[b],qs)+action(P[a]-action(P[a],qr)+action(Pr,a)-Pr,qs)
 assert np.array_equal(CI@error[chords],error)
 certificates={}
 for p in (2,3):
  w=np.array([row['mod6_beta_cycles'].get(str(i),0) for i in range(97)]+
             [row['mod6_A_cycles'].get(str(i),0) for i in range(97)],dtype=np.int64)%p
  h=0;mod=p;steps=[]
  for k in range(1,5):
   defect=error[chords]+LI@w-h*ct[chords]
   assert not np.any(defect%mod)
   pa=P[a]+CI@w[97:];pb=P[b]+CI@w[:97]
   group_check(a,b,pa,pb,h,mod)
   steps.append({'kernel_exponent':mod,'h_mod_exponent':int(h%mod),
                 'lambda_mod_cusp_order':int((1+12*h)%(12*mod)),
                 'cusp_order':12*mod,'hexagons_checked':True})
   if k<4:
    delta=solvers[p]((-defect//mod)%p)
    w+=mod*delta[:194];h+=mod*int(delta[194]);mod*=p
  assert h%p==0
  certificates[str(p)]={'steps':steps,'h':int(h),
    'beta_cycles':{str(i):int(w[i]) for i in range(97) if w[i]},
    'A_cycles':{str(i):int(w[97+i]) for i in range(97) if w[97+i]}}
 refinements.append({'A':row['A'],'beta':row['beta'],'missing_coset':row['missing_coset'],
                     'certificates':certificates})
assert len(refinements)==24
out={'cusp_map_shape':list(L.shape),'cusp_map_smith':diag,
     'cusp_map_cokernel_order':int(sp.prod(diag)),
     'with_multiplier_shape':list(aug.shape),'with_multiplier_smith':diaga,
     'with_multiplier_cokernel_order':int(sp.prod(diaga)),
     'cusp_cycle_coordinates':ct[chords].tolist(),
     'hermite_augmented_is_identity':True,
     'certified_pairs':len(refinements),
     'certified_nonarithmetical_pairs':sum(r['missing_coset'] for r in refinements),
     'finite_refinement_moduli':[2,4,8,16,3,9,27,81],
     'generic_hexagon_checks':len(refinements)*8*2,
     'initial_multiplier_preserved':'h is 0 mod2 and mod3, so lambda=1+12h is 1 mod72 and m=6h is 0 mod36.',
     'interpretation':'Columns are (1-s)C and s(1-r)C; extra column is the change from t to t^(1+12h).',
     'refinement_certificates':refinements}
(ROOT/'d_cm_refine.json').write_text(json.dumps(out,indent=2)+'\n')
summary={k:v for k,v in out.items() if k not in ['cusp_map_smith','with_multiplier_smith','cusp_cycle_coordinates','refinement_certificates']}
summary['smith_multiplicities']={'cusp':{'1':96,'2':1},'with_multiplier':{'1':97}}
print(json.dumps(summary,indent=2))
print('Exact Smith diagonals, cusp coordinates, all 24 paired lifts, and their coefficients are in d_cm_refine.json.')
