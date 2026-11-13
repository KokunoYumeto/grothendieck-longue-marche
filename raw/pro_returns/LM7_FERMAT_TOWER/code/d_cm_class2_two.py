#!/usr/bin/env python3
"""Characteristic class-two 2-quotient refinement of the exact D.25 witnesses.

N/(Gamma3(N) [N,N]^2 N^4) has order2^4850. Its central kernel over
Nab/2 is the4753-dimensional space of symmetric97-square matrices.
Truncated noncommutative Magnus expansion overF2 is exact here.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;start=time.time()
with redirect_stdout(io.StringIO()):D3=runpy.run_path(str(OUT/'d_cm_class2.py'))
D=D3['D'];Q,ix,one,qs,qr=D3['Q'],D3['ix'],D3['one'],D3['qs'],D3['qr']
qm,qr2,C,chords,chord=D3['qm'],D3['qr2'],D3['C'],D3['chords'],D3['chord']
Nwords,reps,invert=D3['Nwords'],D3['reps'],D3['invert'];d=97
pairs=[(i,j) for i in range(d) for j in range(i,d)]
pos={ij:k for k,ij in enumerate(pairs)};cdim=len(pairs);assert cdim==4753
M={}
for q in Q:
 tmp=np.zeros_like(C);tmp[np.array(D['all_left'][ix[q]],dtype=int)]=C
 M[q]=tmp[chords]%2
def supports(v):return list(map(int,np.flatnonzero(v)))
def square_bits(v):
 ids=[]
 while v:
  b=v&-v;ids.append(b.bit_length()-1);v^=b
 ans=0
 for k,i in enumerate(ids):
  for j in ids[k:]:ans^=1<<pos[(i,j)]
 return ans
def action_columns(q):
 supp=[supports(M[q][:,i]) for i in range(d)];ans=[]
 for i,j in pairs:
  z=0
  if i==j:
   for k,a in enumerate(supp[i]):
    for b in supp[i][k:]:z^=1<<pos[(a,b)]
  else:
   for a in supp[i]:
    for b in supp[j]:
     if a!=b:z^=1<<pos[tuple(sorted((a,b)))]
  ans.append(z)
 return ans
S=action_columns(qs);SR=action_columns(qm(qs,qr))
columns=[(1<<i)^S[i] for i in range(cdim)]+[S[i]^SR[i] for i in range(cdim)]
def evaluate(word):
 q=one;v=0;w=[0]*d
 def append(e,sgn):
  nonlocal v,w
  i=chord.get(e)
  if i is None:return
  b=1<<i;vv=v
  while vv:
   a=vv&-vv;w[a.bit_length()-1]^=b;vv^=a
  if sgn<0:w[i]^=b
  v^=b
 for letter in word:
  if letter==0:q=qm(q,qs)
  else:
   qq=qm(q,qr if letter==1 else qr2)
   append(ix[q],1);append(ix[qq],-1);q=qq
 return q,v,w
def central(w):
 for i in range(d):
  for j in range(i+1,d):assert ((w[i]>>j)&1)==((w[j]>>i)&1)
 z=0
 for k,(i,j) in enumerate(pairs):
  if (w[i]>>j)&1:z^=1<<k
 return z
for i,word in enumerate(Nwords):
 q,v,w=evaluate(word);assert q==one and v==1<<i and not any(w)
 q,v,w=evaluate(word+word);assert q==one and v==0 and central(w)==1<<pos[(i,i)]
q,vc,wc=evaluate([0,1]*12);assert q==one
c2=square_bits(vc);q,v,w=evaluate([0,1]*24);assert q==one and v==0 and central(w)==c2

# Eliminate exact bit columns; witnesses retain all central corrections.
bas={}
def add(col,j):
 v=col;w=1<<j
 while v:
  p=v.bit_length()-1
  if p not in bas:bas[p]=(v,w);return True
  bv,bw=bas[p];v^=bv;w^=bw
 return False
for j,col in enumerate(columns):add(col,j)
rank=len(bas);added=add(c2,len(columns));rank_aug=len(bas)
print('Central dimension',cdim,'rank',rank,'with multiplier rank',rank_aug,
      'elapsed',round(time.time()-start,2),flush=True)
def solve(v,basis=None):
 basis=bas if basis is None else basis
 w=0
 while v:
  p=v.bit_length()-1
  if p not in basis:return False,w,v
  bv,bw=basis[p];v^=bv;w^=bw
 return True,w,0
def verify_solution(w,target):
 val=0;ww=w
 while ww:
  bit=ww&-ww;k=bit.bit_length()-1
  val^=columns[k] if k<len(columns) else c2;ww^=bit
 assert val==target

# Exhaust the changes beta -> beta c preserving its conjugation of s in G2,
# with q(c)=1. The order3 r-centralizer lifts through2-kernels automatically.
rows=[]
mat=(np.eye(d,dtype=np.int16)+M[qs])%2
for row in mat:rows.append(sum((1<<i) for i in np.flatnonzero(row)))
rb={}
for row in rows:
 while row:
  k=row.bit_length()-1
  if k not in rb:rb[k]=row;break
  row^=rb[k]
fixed_s=[]
for j in range(d):
 if j in rb:continue
 v=1<<j
 for k in sorted(rb):
  if (rb[k]&v).bit_count()%2:v^=1<<k
 assert all((r&v).bit_count()%2==0 for r in rows)
 fixed_s.append(v)
s_defects=[]
for v in fixed_s:
 cw=[]
 for i,nw in enumerate(Nwords):
  if (v>>i)&1:cw+=nw
 q,vv,w=evaluate(cw+[0]+invert(cw)+[0]);assert q==one and vv==0
 s_defects.append(central(w))
actcache={qs:S,qm(qs,qr):SR}
def actbits(q,z):
 if q not in actcache:actcache[q]=action_columns(q)
 cols=actcache[q];ans=0
 while z:
  bit=z&-z;ans^=cols[bit.bit_length()-1];z^=bit
 return ans
augcache={}
def augmented(q):
 if q in augcache:return augcache[q]
 extra=[actbits(q,z) for z in s_defects];bb=bas.copy()
 for i,col in enumerate(extra):
  v=col;w=1<<(len(columns)+1+i)
  while v:
   k=v.bit_length()-1
   if k not in bb:bb[k]=(v,w);break
   bv,bw=bb[k];v^=bv;w^=bw
 augcache[q]=(bb,extra);return bb,extra
print('s-fixed vectors:',len(fixed_s),'for all lower-conjugator freedoms at2',flush=True)

records=[]
for row in D['records']:
 if not(row.get('finite_automorphism') and row.get('mod3_automorphism')):continue
 a=D['canon'](tuple(row['A']));b=D['canon'](tuple(row['beta']))
 aa=int(row['A_cycle_coefficients'],16);bb=int(row['beta_cycle_coefficients'],16)
 wa=[];wb=[]
 for i,word in enumerate(Nwords):
  if (aa>>i)&1:wa+=word
  if (bb>>i)&1:wb+=word
 wa+=reps[a];wb+=reps[b]
 cusp=wb+[0]+invert(wb)+wa+[1]+invert(wa)+[2,0]
 q,v,w=evaluate(cusp);assert q==one and v==0
 target=central(w);good,sol,rem=solve(target)
 rec={'A':row['A'],'beta':row['beta'],'missing_coset':row['missing_coset'],
      'fixed_conjugators_lift':good,'cusp_central_defect':hex(target),
      'obstruction':hex(rem),'base_word_length':len(cusp)}
 if good:
  verify_solution(sol,target)
  eta=(sol>>(2*cdim))&1
  rec.update({'beta_central_coefficients':hex(sol&((1<<cdim)-1)),
              'A_central_coefficients':hex((sol>>cdim)&((1<<cdim)-1)),
              'multiplier_bit':eta,'lambda_mod144':1+72*eta,
              'full_4753_coordinate_equation_checked':True})
 ab,extra=augmented(b)
 action_good,asol,arem=solve(target,ab)
 rec.update({'same_G2_action_lifts':action_good,
             'rank_including_conjugator_freedom':len(ab),
             'action_obstruction':hex(arem)})
 if action_good:
  val=0;ww=asol
  while ww:
   bit=ww&-ww;k=bit.bit_length()-1
   val^=columns[k] if k<len(columns) else c2 if k==len(columns) else extra[k-len(columns)-1]
   ww^=bit
  assert val==target
  rec['action_lift_certificate']={
     'beta_central_coefficients':hex(asol&((1<<cdim)-1)),
     'A_central_coefficients':hex((asol>>cdim)&((1<<cdim)-1)),
     'multiplier_bit':(asol>>(2*cdim))&1,
     'beta_right_s_centralizer_coefficients':hex(asol>>(2*cdim+1)),
     'full_4753_coordinate_equation_checked':True}
 records.append(rec)
 print('pair',len(records),'extra' if row['missing_coset'] else 'compatible',
       'LIFT' if good else 'FIXED-CONJUGATORS OBSTRUCTED',
       'same-action lift' if action_good else 'same-action obstructed',flush=True)
summary={'prime':2,'Q_order':576,'N_rank':97,'kernel_order':'2^4850',
 'central_dimension':cdim,'central_correction_rank':rank,
 'rank_with_multiplier':rank_aug,'central_cokernel_dimension':cdim-rank_aug,
 'tested_pairs':len(records),
 'fixed_compatible_lifts':sum(r['fixed_conjugators_lift'] and not r['missing_coset'] for r in records),
 'fixed_extra_CM_lifts':sum(r['fixed_conjugators_lift'] and r['missing_coset'] for r in records),
 's_centralizer_fixed_dimension':len(fixed_s),
 'rank_with_conjugator_freedom':sorted(set(r['rank_including_conjugator_freedom'] for r in records)),
 'same_action_compatible_lifts':sum(r['same_G2_action_lifts'] and not r['missing_coset'] for r in records),
 'same_action_extra_lifts':sum(r['same_G2_action_lifts'] and r['missing_coset'] for r in records),
 'kernel_definition':'Gamma3(N) [N,N]^2 N^4',
 'combined_with_G3_order':'576 * 2^4850 * 3^97',
 'multiplier_normalization':'lambda=1+72 eta, m=36 eta, so the G6 multiplier m=0 mod36 is preserved',
 'scope':'Tests the given D25 conjugators; failed fixed-lift attempts alone are not called fake shadows.',
 'elapsed_seconds':round(time.time()-start,3)}
(OUT/'d_cm_class2_two.json').write_text(json.dumps({'summary':summary,
 's_centralizer_basis':[hex(v) for v in fixed_s],'pairs':records},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
