#!/usr/bin/env python3
"""Independent six-action audit, including exact based F compatibility."""
from pathlib import Path
import json,time
H=Path(__file__).resolve().parent;ROOT=H.parent.parent
B=json.loads((ROOT/'work_CE/next_symmetric_nodes/symmetric_old_base_words.json').read_text())
D=json.loads((ROOT/'work_CE/next_symmetric_nodes/symmetric_old_discriminant_orders.json').read_text())
Fdata=json.loads((H/'symmetric_source_bridge_review.json').read_text())
# Fresh exact cyclotomic arithmetic; no producer or SymPy field helpers.
Z=(0,0,0,0);O=(1,0,0,0);z=(0,1,0,0)
def add(a,b):return tuple(a[i]+b[i] for i in range(4))
def neg(a):return tuple(-x for x in a)
def sc(n,a):return tuple(n*x for x in a)
def subf(a,b):return add(a,neg(b))
def mul(a,b):
 c=[0]*7
 for i in range(4):
  for j in range(4):c[i+j]+=a[i]*b[j]
 for k in range(6,3,-1):
  for j in range(4):c[k-4+j]-=c[k]
 return tuple(c[:4])
U=[O]
for i in range(4):U.append(mul(U[-1],z))
assert mul(U[-1],z)==O

def trim(p):
 p=list(p)
 while p and p[-1]==Z:p.pop()
 return p

def pa(a,b):
 c=[Z]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]=add(c[i],x)
 for i,x in enumerate(b):c[i]=add(c[i],x)
 return trim(c)
def pn(p):return [neg(x) for x in p]
def pm(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
 return trim(c)
def pe(p,a):
 v=Z
 for x in reversed(p):v=add(mul(v,a),x)
 return v

def valuation(p,a):
 p=trim(p);assert p
 n=0
 while pe(p,a)==Z:
  assert len(p)>1
  quotient=[Z]*(len(p)-1);carry=p[-1];quotient[-1]=carry
  for i in range(len(p)-2,0,-1):carry=add(p[i],mul(a,carry));quotient[i-1]=carry
  assert add(p[0],mul(a,carry))==Z
  p=trim(quotient);n+=1
 return n
rat=[([Z],[O]),([O],[O]),([Z,O],[O])]
rat += [([u],[O]) for u in U[1:]]
rat += [([Z,O],[u]) for u in U[1:]]
rat += [([u,neg(O)],[subf(u,O)]) for u in U[1:]]
rat += [([Z,subf(O,u)],[neg(u),O]) for u in U[1:]]
assert len(rat)==19
rootpoints=[Z]+U
valrows=[]
for alpha in rootpoints:
 pairs=[];against=[];total=0
 for i,(a,b) in enumerate(rat):
  for j in range(i+1,19):
   c,d=rat[j];P=pa(pm(a,d),pn(pm(c,b)))
   v=valuation(P,alpha)-valuation(b,alpha)-valuation(d,alpha)
   pairs.append({'labels':[i,j],'difference_order':v});total+=2*v
  P=pa(pm(a,a),pn([Z]+pm(b,b)))
  v=valuation(P,alpha)-2*valuation(b,alpha);against.append(v);total+=2*v
 rootorder=int(alpha==Z);total+=rootorder
 valrows.append({'discriminant_order':total,'rational_pair_orders':pairs,'rational_against_two_roots_orders':against,'square_root_pair_discriminant_order':rootorder})
for ours,theirs in zip(valrows,D['rows']):
 for key in ours:assert ours[key]==theirs[key],('valuation mismatch',key)
print('PASS: fresh exact cyclotomic valuation arithmetic verifies all six discriminants and all pair/root orders.',flush=True)

def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(int(x))
 return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
def art(w,n=21):
 A={i:(i,) for i in range(1,n+1)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(red(a+b+inv(a)),a) if x>0 else (b,red(inv(b)+a+b))
 return A

def peel(w,expected):
 c=[];w=list(w)
 while len(w)>1 and w[0]==-w[-1]:c.append(w.pop(0));w.pop()
 assert w==[expected],('not inner peripheral',expected,w)
 return tuple(c)
def inner_word(J):
 c1=peel(J[1],1);c2=peel(J[2],2);d=red(inv(c1)+c2)
 k=0;m=0
 while k<len(d) and abs(d[k])==1:m+=d[k];k+=1
 assert all(abs(x)==2 for x in d[k:]),('inner conjugators incompatible',d)
 power=(1,)*m if m>=0 else (-1,)*(-m)
 c=red(c1+power)
 assert all(J[j]==red(c+(j,)+inv(c)) for j in range(1,22))
 return c
Fauto={int(k):tuple(v) for k,v in Fdata['conjugated_involution_at_nodal_base'].items()}
initial=B['initial_order'];oldpos=[j for j,p in enumerate(initial,1) if p in (0,1,2,19,20)]
outputs=[]
for i,row in enumerate(B['loops']):
 w=row['word'];A=art(w);Ai=art(inv(w))
 assert A=={int(k):tuple(v) for k,v in row['images'].items()}
 assert Ai=={int(k):tuple(v) for k,v in row['inverse_images'].items()}
 for j in range(1,22):assert sub(A[j],Ai)==(j,) and sub(Ai[j],A)==(j,)
 assert sub(tuple(range(1,22)),A)==tuple(range(1,22))
 # Independently recompute every labeled crossing sum.
 perm=list(initial);link={}
 for g in w:
  j=abs(g)-1;k=tuple(sorted(perm[j:j+2]));link[k]=link.get(k,0)+(1 if g>0 else -1);perm[j],perm[j+1]=perm[j+1],perm[j]
 expect=list(initial)
 if i==0:expect=[20 if p==19 else 19 if p==20 else p for p in initial]
 assert perm==expect
 vals=valrows[i]
 for a in vals['rational_pair_orders']:assert link.get(tuple(a['labels']),0)==2*a['difference_order']
 for j,v in enumerate(vals['rational_against_two_roots_orders']):assert link.get((j,19),0)+link.get((j,20),0)==2*v
 assert link.get((19,20),0)==vals['square_root_pair_discriminant_order']
 # Every one-sided and both-sided filling is an actual preserved kernel.
 restrictions=[]
 for killed in (set(range(3,11)),set(range(11,19)),set(range(3,19))):
  keep=[j for j,p in enumerate(initial,1) if p not in killed];fill={j:((keep.index(j)+1,) if j in keep else ()) for j in range(1,22)}
  for j,p in enumerate(initial,1):
   if p in killed:assert not sub(A[j],fill) and not sub(Ai[j],fill)
  C={k+1:sub(A[j],fill) for k,j in enumerate(keep)};Ci={k+1:sub(Ai[j],fill) for k,j in enumerate(keep)}
  for j in C:assert sub(C[j],Ci)==(j,) and sub(Ci[j],C)==(j,)
  restrictions.append({'retained_rank':len(keep),'images':{str(j):list(v) for j,v in C.items()},'inverse_images':{str(j):list(v) for j,v in Ci.items()}})
 # Exact source-based total-space compatibility.
 J={j:sub(sub(sub(Ai[j],Fauto),A),Fauto) for j in range(1,22)}
 k=inner_word(J);assert not red(sub(k,Fauto)+k),('F cocycle',i)
 outputs.append({'index':i,'name':row['name'],'discriminant_order':vals['discriminant_order'],'F_commutator_inner_word':list(k),'filling_restrictions':restrictions})
 print('PASS old action',i,row['name'],'F-commutator inner length',len(k),'and F(k)*k=1.',flush=True)
(H/'symmetric_old_actions_review.json').write_text(json.dumps({'scope':'actual six retained actions with all fillings and based F compatibility','loops':outputs,'inverse_checks_full':252,'full_F_inner_checks':126,'equation':'F alpha_i F alpha_i^-1=Inn(k_i), F(k_i) k_i=1'},indent=2)+'\n')
print('PASS: all six actual old-base actions, all3 filling restrictions each, and complete F-equivariant compatibility.',flush=True)
