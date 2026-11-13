#!/usr/bin/env python3
"""Exact, dependency-free checks for the Part B counterexamples and type (0,3).
Run from any directory. Outputs are written beside this script.
The geometric completeness proof for type (0,3) is in statement B.20.
"""
from itertools import permutations, product
from fractions import Fraction
from pathlib import Path
import csv, json
OUT=Path(__file__).resolve().parent
P=list(permutations(range(3)))
idp=(0,1,2)
G=[(p,e) for p in P for e in range(2)]
I=(idp,0)
def mul(x,y): return (tuple(x[0][y[0][i]] for i in range(3)),x[1]^y[1])
def inv(x): return next(y for y in G if mul(x,y)==I)
def power(x,n):
 z=I
 for _ in range(n): z=mul(z,x)
 return z
def order(x): return next(n for n in range(1,13) if power(x,n)==I)
def conj(g,h): return mul(mul(g,h),inv(g))
def closure(gens):
 H={I}; todo=list(gens)
 while todo:
  x=todo.pop()
  if x in H: continue
  H.add(x);old=list(H)
  todo.extend(mul(x,y) for y in old);todo.extend(mul(y,x) for y in old)
 return frozenset(H)
def sign(p): return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1
r=((1,2,0),0); a=((0,2,1),0); tau=(idp,1)
subgroups={frozenset({I})}
while True:
 more={closure(set(H)|{x}) for H in subgroups for x in G}
 if more<=subgroups: break
 subgroups|=more
classes=[];left=set(subgroups)
while left:
 H=min(left,key=lambda h:(len(h),sorted(h)))
 orbit={frozenset(conj(g,x) for x in H) for g in G}
 classes.append(orbit);left-=orbit
assert len(subgroups)==16 and len(classes)==10
named=[('1',[]),('C2_rotation',[a]),('C2_horizontal',[tau]),
 ('C2_vertical',[mul(a,tau)]),('C3',[r]),('V4',[a,tau]),
 ('C6',[r,tau]),('S3_positive',[r,a]),
 ('S3_mixed',[r,mul(a,tau)]),('S3_x_C2',[r,a,tau])]
Hs={name:closure(gens) for name,gens in named}
assert all(any(H in C for C in classes) for H in Hs.values())
assert len({next(i for i,C in enumerate(classes) if H in C) for H in Hs.values()})==10

def fixed(H):
 """Connected fixed components on S2 minus the three positive equatorial axes.
 Punctures are P_i; surviving opposite axes Q_i; N,S poles.
 A_i is the horizontal mirror interval containing Q_i.
 B_i is the vertical mirror minus its unique puncture P_i.
 """
 if len(H)==1:return ('U',)
 positive=[x for x in H if x[1]==0]
 if len(positive)==1:
  t=next(x for x in H if x!=I)
  if t==tau:return ('A0','A1','A2')
  assert order(t)==2 and sign(t[0])==-1
  return ('B'+str(next(i for i in range(3) if t[0][i]==i)),)
 if len(positive)==2:
  t=next(x for x in positive if x!=I)
  idx=next(i for i in range(3) if t[0][i]==i)
  return ('Q'+str(idx),) if all(x[0][idx]==idx for x in H) else ()
 if len(positive)==3:
  return ('N','S') if all(sign(x[0])*(-1)**x[1]==1 for x in H) else ()
 return ()

def inc(c,d):
 H,x=c;J,y=d
 if not H<J:return False
 if x.startswith('A'):return y=='Q'+x[1:]
 if x.startswith('B'):return y in ('N','S','Q'+x[1:])
 return x==y

def act(g,c):
 H,x=c;J=frozenset(conj(g,h) for h in H)
 if x in ('N','S'):
  y= x if sign(g[0])*(-1)**g[1]==1 else ('S' if x=='N' else 'N')
 elif x[0] in 'QAB': y=x[0]+str(g[0][int(x[1:])])
 else:y=x
 return (J,y)
rows=[];partials=[]
for name,K in Hs.items():
 cs=[(H,x) for H in subgroups if len(H)>1 and H<=K for x in fixed(H)]
 maximal=[c for c in cs if not any(inc(c,d) for d in cs)]
 remaining=set(maximal);orbits=[]
 while remaining:
  c=next(iter(remaining));orb={act(g,c) for g in K}
  assert orb<=set(maximal)
  orbits.append(orb);remaining-=orb
 maxdesc='; '.join(sorted(f'{x}: order {len(H)}' for H,x in maximal))
 row={'type':'(0,3)','subgroup':name,'order':len(K),
 'positive_order':sum(x[1]==0 for x in K),
 'full_splitting_classes':len(fixed(K)),
 'nontrivial_partial_splitting_classes':len(cs),
 'maximal_partial_classes_Phi':len(maximal),
 'Gamma_orbits_on_Phi':len(orbits),'maximal_stabilizers':maxdesc}
 rows.append(row)
 for H,x in sorted(cs,key=lambda c:(len(c[0]),c[1],sorted(c[0]))):
  mu=[]
  for h in H:
   if h==I: value='0'
   elif h[1] or order(h)==2:value='1/2'
   else:
    # r is counterclockwise at N and clockwise at S.
    k=1 if h==r else 2
    value=str(Fraction(k if x=='N' else -k,3)%1)
   mu.append((G.index(h),value))
  partials.append({'ambient':name,'image_order':len(H),'component':x,
   'maximal':(H,x) in maximal,'image_elements':[G.index(h) for h in sorted(H)],
   'mu_by_element':sorted(mu)})
with (OUT/'type_0_3_finite_subgroups.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(OUT/'type_0_3_partial_sections.json').write_text(json.dumps({'elements':G,'partial_sections':partials},indent=2)+'\n')
# Exact finite quotient of the NEC triangle counterexample.
s0=tau;s1=mul(a,tau);s2=mul(mul(r,a),tau)
assert all(order(s)==2 for s in [s0,s1,s2])
assert order(mul(s0,s1))==2 and order(mul(s1,s2))==3
A=closure([s0,s1]);B=closure([s1,s2]);C=closure([s0,s2])
assert (len(A),len(B),len(A&B),len(C),len(closure([s0,s1,s2])))==(4,6,2,4,12)
chiE=Fraction(1,4)+Fraction(1,6)-Fraction(1,2)
chip=12*chiE;cusps=12//len(C);genus=(2-cusps-chip)/2
assert (chip,cusps,genus)==(-1,3,0)
# The displayed presentation (52) at g=2.
e0=((2,1,0),0);e1=I;t=I;tp=((1,0,2),0);rr=mul(e0,e1)
rels=[power(e0,2),power(e1,2),power(t,2),power(tp,2),
 power(mul(t,e0),2),power(mul(t,e1),2),power(mul(tp,e1),2),
 power(rr,4),power(mul(tp,power(rr,2)),2)]
assert all(z==I for z in rels)
rho0=mul(tp,t);rho1=conj(rr,rho0)
assert mul(rho0,rho1)!=mul(rho1,rho0)
# Exact 2x2 integral matrix example in the pointed punctured torus.
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mp(A,n):
 ans=[[1,0],[0,1]]
 for _ in range(n):ans=mm(ans,A)
 return ans
def mi(A):return [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
S=[[0,-1],[1,0]];T=[[2,1],[-1,0]];V=mm(mm(T,S),mi(T));SV=mm(S,V)
assert mp(S,2)==mp(V,2)==[[-1,0],[0,-1]]
assert mp(S,4)==mp(V,4)==[[1,0],[0,1]]
assert SV[0][0]+SV[1][1]==-6
# Counts of unlabelled real punctured-surface types, by quotient data.
def partitions(n,b):
 if b==0:return int(n==0)
 dp=[0]*(n+1);dp[0]=1
 for k in range(1,b+1):
  for j in range(k,n+1):dp[j]+=dp[j-k]
 return dp[n]
def real_count(g,nu):
 bs=list(range(g+1))+list(range(1,g+2,2) if (g+1)%2 else range(2,g+2,2))
 return sum(partitions(nu-2*r,b) for b in bs for r in range(nu//2+1))
realrows=[{'g':g,'nu':nu,'topological_real_types':real_count(g,nu)}
 for g in range(4) for nu in range(7-2*g)]
for g in range(21):assert real_count(g,0)==(3*g+4)//2
with (OUT/'real_type_counts.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(realrows[0]));w.writeheader();w.writerows(realrows)
monodromy=[]
for second in (1,-1):
 cusp_image=(1+second)%3
 ncusp=3 if cusp_image==0 else 1
 monodromy.append({'q_u':1,'q_v':second,'cusp_image':cusp_image,'cusps':ncusp,'genus':(3-ncusp)//2,'chi':-1})
assert [(z['cusps'],z['genus']) for z in monodromy]==[(1,1),(3,0)]
summary={'C3_free_product_monodromies':monodromy,'torus_reflection_extension_parities':{'0':2,'1':0},'finite_group_order':12,'all_subgroups':len(subgroups),'subgroup_conjugacy_classes':len(classes),
 'NEC_vertex_orders':[len(A),len(B)],'NEC_intersection_order':len(A&B),
 'NEC_kernel_Euler_characteristic':str(chip),'NEC_cusps':cusps,'NEC_genus':str(genus),
 'presentation_52_relators_checked':len(rels),'rho0_rho1_commute':False,
 'S':S,'T':T,'TST_inverse':V,'product':SV,'product_trace':-6,
 'real_closed_counts_g0_to_8':[real_count(g,0) for g in range(9)],
 'table':rows}
(OUT/'check_part_b_output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
