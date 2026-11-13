#!/usr/bin/env python3
"""Actual order3888 local class-two transgression, with all marked maps.

The central quotient is the actual 74-dimensional (W wedge V)_G from
d_arithmetic_invariant_module.json.  No finite substitute base is used.
All 600 same-homology peripheral parameters are lifted integrally modulo4.
"""
from pathlib import Path
from itertools import product
import json,time,random
import numpy as np

OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
H=json.loads((OUT/'d_arithmetic_affine_homology.json').read_text())
I=json.loads((OUT/'d_arithmetic_invariant_module.json').read_text())
rho=649;size=3888;cd=74
M=[tuple(map(tuple,x)) for x in D['Q_linear_image_matrices']]
mi={a:i for i,a in enumerate(M)}
S4=tuple(map(tuple,D['quotient_s_columns']));R4=tuple(map(tuple,D['quotient_r_columns']))
vectors=list(product(range(3),repeat=4));vi={v:i for i,v in enumerate(vectors)}
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(mv(A,c) for c in B)
mt=[[mi[mm(a,b)] for b in M] for a in M]
ma=[[vi[mv(a,b)] for b in vectors] for a in M]
va=[[vi[tuple((x+y)%3 for x,y in zip(a,b))] for b in vectors] for a in vectors]
def gm(a,b):
 aq,av=divmod(a,81);bq,bv=divmod(b,81)
 return 81*mt[aq][bq]+va[av][ma[aq][bv]]
s=81*mi[S4]+vi[tuple(D['affine_s_translation'])]
r=81*mi[R4]+vi[tuple(D['affine_r_translation'])]
t=gm(s,r);rs=D['right_s_3888'];rr=D['right_r_3888']
ch=H['cycle_chords'];ci={e:j for j,e in enumerate(ch)}
BW=H['all649_free_generator_words']
def invword(w):return [0 if a==0 else 3-a for a in reversed(w)]
def combine(cols,v):
 out=0
 while v:
  b=v&-v;out^=cols[b.bit_length()-1];v^=b
 return out
def solver(cols):
 bas={};null=[];ind=[]
 for j,col in enumerate(cols):
  v=col;w=1<<j
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=(v,w);ind.append(j);break
   a,b=bas[p];v^=a;w^=b
  if not v:null.append(w)
 def solve(v):
  out=0
  for p in sorted(bas,reverse=True):
   if v>>p&1:a,b=bas[p];v^=a;out^=b
  assert not v
  return out
 return solve,len(bas),null,ind
def rank(cols):return solver(cols)[1]
off=[j*(2*rho-j-1)//2 for j in range(rho)]
def evaluate(word):
 q=0;ab=[0]*rho;odd=0;central=0
 def append(e,sign):
  nonlocal odd,central
  if e in ci:
   j=ci[e];central^=(odd>>(j+1))<<off[j]
   ab[j]=(ab[j]+sign)%4;odd^=1<<j
 for tok in word:
  if tok==0:q=rs[q]
  else:
   h=rr[q] if tok==1 else rr[rr[q]]
   append(q,1);append(h,-1);q=h
 return q,ab,central
IC=[]
for j,w in enumerate(BW):
 q=0;c={}
 for tok in w:
  if tok==0:q=rs[q]
  else:
   h=rr[q] if tok==1 else rr[rr[q]]
   c[q]=c.get(q,0)+1;c[h]=c.get(h,0)-1;q=h
 assert q==0 and [c.get(e,0) for e in ch]==[int(k==j) for k in range(rho)]
 IC.append({e:a for e,a in c.items() if a})

# Pull each exact central coinvariant functional back to the entire free
# exterior module.  The other A-isotypic and mixed summands are killed.
n=16;loff=[i*(2*n-i-1)//2 for i in range(n)]
pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
IB=[int(v,16) for v in I['universal64_invariant_exterior_basis']]
isco,ir,_,_=solver(IB);assert ir==64
JC=[]
for i in range(8):JC.extend([1<<(2*i+1),(1<<(2*i))^(1<<(2*i+1))])
def lwedge(a,b):
 out=0
 for i in range(n):
  row=(b if a>>i&1 else 0)^(a if b>>i&1 else 0)
  out|=(row>>(i+1))<<loff[i]
 return out
def lwa(v,cols):
 out=0
 while v:
  b=v&-v;i,j=pairs[b.bit_length()-1]
  out^=lwedge(cols[i],cols[j]);v^=b
 return out
Ncols=[]
for i,j in pairs:
 v=lwedge(1<<i,1<<j);w=lwa(v,JC)
 Ncols.append(isco(v^w^lwa(w,JC)))
qc=[int(x,16) for x in I['coinvariant_columns']]
Frows=[[0]*rho for _ in range(cd)]
for bi,P in enumerate(I['all40_projector_coordinate_columns']):
 rows=[sum(1<<j for j,v in enumerate(P) if v>>i&1) for i in range(16)]
 local=[[0]*16 for _ in range(cd)]
 for k,(i,j) in enumerate(pairs):
  value=combine(qc[64*bi:64*bi+64],Ncols[k])
  while value:
   bit=value&-value;d=bit.bit_length()-1
   local[d][i]^=1<<j;local[d][j]^=1<<i;value^=bit
 for d in range(cd):
  trans=[combine(rows,col) for col in local[d]]
  if not any(trans):continue
  for j,p in enumerate(P):Frows[d][j]^=combine(trans,p)
assert all(not(row>>j&1) for rows in Frows for j,row in enumerate(rows))
assert all(((rows[i]>>j)&1)==((rows[j]>>i)&1)
           for rows in Frows for i in range(rho) for j in range(i))
Fupper=[[row&~((1<<(j+1))-1) for j,row in enumerate(rows)] for rows in Frows]
duals=[sum((row>>(j+1))<<off[j] for j,row in enumerate(rows)) for rows in Fupper]
def obs(c):return sum(1<<d for d,v in enumerate(duals) if (v&c).bit_count()%2)
def cross(a,b):
 inds=[]
 while b:
  bit=b&-b;inds.append(bit.bit_length()-1);b^=bit
 return sum(1<<d for d,rows in enumerate(Fupper)
            if sum((a&rows[j]).bit_count() for j in inds)%2)
def bitmask(a,bit=0):return sum(1<<i for i,v in enumerate(a) if (int(v)>>bit)&1)
def fullcross(a,b):
 out=0
 while b:
  bit=b&-b;j=bit.bit_length()-1;out^=(a>>(j+1))<<off[j];b^=bit
 return out
rng=random.Random(20261113)
for trial in range(30):
 a=rng.getrandbits(rho);b=rng.getrandbits(rho)
 assert cross(a,b)==obs(fullcross(a,b))
print('actual central functionals',len(duals),'verified',flush=True)

# The integral moving projection uses all81 actual translations on edges.
EA=np.zeros((rho,rho),dtype=np.int16)
for j,c in enumerate(IC):
 for a in range(81):
  for e,v in c.items():
   h=gm(a,e)
   if h in ci:EA[ci[h],j]+=v
EA%=4 # 81^{-1}=1 modulo4.
W=[int(v,16) for v in H['moving_basis']]
assert all(bitmask(EA[:,j])==int(H['A_norm_columns'][j],16) for j in range(rho))
assert not np.any((EA@EA-EA)%4)
I4=np.eye(rho,dtype=np.int16)
WM=np.array([[(w>>i)&1 for i in range(rho)] for w in W],dtype=np.int16).T
def moving(v):return (v-EA@v)%4

# Actual action on the class-two quotient, retained as linear, square,
# and quadratic maps.  Conjugating words are literal s and sr.
actions={}
for name,gword in [('s',[0]),('t',[0,1])]:
 cols=[];lin=[]
 for j,w in enumerate(BW):
  q,a,c=evaluate(gword+w+invword(gword));assert q==0
  cols.append(a);lin.append(obs(c))
 mat=np.array(cols,dtype=np.int16).T
 MC=[bitmask(col) for col in cols]
 assert MC==[int(v,16) for v in H['homology_'+name+'_columns']]
 # F'_j=A^t F_j A; lower-index entries give ordered-product terms.
 lows=[];diag=[0]*rho
 for d,rows in enumerate(Fupper):
  transformed=[]
  for v in MC:
   w=combine(rows,v)
   transformed.append(sum(1<<i for i,c in enumerate(MC) if (c&w).bit_count()%2))
  lows.append([v&((1<<j)-1) for j,v in enumerate(transformed)])
  for j,v in enumerate(transformed):
   if v>>j&1:diag[j]^=1<<d
 actions[name]=(mat,MC,lin,lows,diag)
def action(name,a,c=0):
 mat,MC,lin,lows,diag=actions[name]
 odd=bitmask(a);hi=bitmask(a,1);indices=[];v=odd
 while v:
  b=v&-v;indices.append(b.bit_length()-1);v^=b
 q=combine(lin,odd)^combine(diag,hi)
 for d,rows in enumerate(lows):
  if sum((odd&rows[j]).bit_count() for j in indices)%2:q^=1<<d
 return mat@a%4,c^q
def collected(a):
 w=[]
 for v,b in zip(a,BW):
  v=int(v)%4
  if v==3:w.extend(invword(b))
  elif v:w.extend(b*v)
 return w
for trial in range(12):
 a=np.zeros(rho,dtype=np.int16)
 for j in rng.sample(range(rho),8):a[j]=rng.randrange(4)
 for name,gword in [('s',[0]),('t',[0,1])]:
  aq,cq=action(name,a)
  q,aa,cc=evaluate(gword+collected(a)+invword(gword))
  assert q==0 and aa==aq.tolist() and obs(cc)==cq
print('exact s/t class-two maps verified',flush=True)

HS=[int(v,16) for v in H['homology_s_columns']]
HR=[int(v,16) for v in H['homology_r_columns']]
CS=[w^combine(HS,w) for w in W]
CR=[combine(HS,w^combine(HR,w)) for w in W]
csolve,lr,pk,_=solver(CS+CR);assert lr==640
SM=actions['s'][0];TM=actions['t'][0]
def integral_pair(bm,am):
 b=moving(np.array([(bm>>i)&1 for i in range(rho)],dtype=np.int16))
 a=moving(np.array([(am>>i)&1 for i in range(rho)],dtype=np.int16))
 err=(b+SM@(a-b)-TM@a)%4;assert not any(err%2)
 co=csolve(bitmask(err,1));db=combine(W,co&((1<<640)-1));da=combine(W,co>>640)
 b=(b+2*np.array([(db>>i)&1 for i in range(rho)],dtype=np.int16))%4
 a=(a+2*np.array([(da>>i)&1 for i in range(rho)],dtype=np.int16))%4
 assert not any((b+SM@(a-b)-TM@a)%4)
 assert not any(EA@a%4) and not any(EA@b%4)
 return b,a
def obstruction(b,a):
 sb,sc=action('s',(a-b)%4)
 ta,tc=action('t',(-a)%4)
 bm=bitmask(b);am=bitmask(a);sm=bitmask(sb);tm=bitmask(ta)
 assert not any((b+sb+ta)%4)
 return sc^tc^cross(bm,bm)^cross(bm,am)^cross(bm,sm)^cross(am,am)^cross(bm^sm,tm)
records=[];params=[];local=[]
for name in ('s','r','t'):
 for vhex in H['moving_fixed_bases'][name]:
  v=combine(W,int(vhex,16))
  bm=v if name in ('s','t') else 0
  am=v if name in ('r','t') else 0
  b,a=integral_pair(bm,am);value=obstruction(b,a)
  params.append((b,a));local.append(value)
  records.append({'type':name,'moving_coordinate':vhex,'obstruction':hex(value),
                  'beta_mod4':b.tolist(),'r_mod4':a.tolist()})
assert len(local)==600
cn=[int(v,16) for v in I['compact_norm_representative_images']]
assert all(combine(cn,v)==0 for v in local)
locsolve,loc_rank,locnull,locind=solver(local)
print('actual local image rank',loc_rank,'compact norm kernel',74-I['summary']['compact_group_norm_rank'],flush=True)

# Direct closed B words verify the complete model, including signs and
# the integral correction.  Also test the local linearity on combinations.
checks=[]
for trial in range(15):
 inds=rng.sample(range(600),1 if trial<6 else 3)
 b=sum((params[i][0] for i in inds),np.zeros(rho,dtype=np.int16))%4
 a=sum((params[i][1] for i in inds),np.zeros(rho,dtype=np.int16))%4
 value=obstruction(b,a);assert value==combine(local,sum(1<<i for i in inds))
 aw=collected(a);bw=collected(b)
 word=bw+[0]+invword(bw)+aw+[1]+invword(aw)+[2,0]
 q,ab,c=evaluate(word)
 assert q==0 and ab==[0]*rho and obs(c)==value
 checks.append({'parameters':inds,'B_word_length':len(word),'value':hex(value)})
summary={'scope':'Actual arithmetic order3888 local class-two transgression.',
 'base_order':size,'homology_rank':rho,'central_coinvariant_dimension':cd,
 'complete_same_homology_parameter_dimension':len(local),
 'local_transgression_rank':loc_rank,
 'compact_norm_rank':I['summary']['compact_group_norm_rank'],
 'compact_norm_kernel_dimension':74-I['summary']['compact_group_norm_rank'],
 'local_image_equals_compact_norm_kernel':loc_rank==74-I['summary']['compact_group_norm_rank'],
 'all600_exact_mod4_cusp_and_moving_checks':True,
 'all600_local_images_annihilated_by_compact_norm':True,
 'literal_word_checks':len(checks),'s_t_class2_map_word_checks':24,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'all600_local_parameters':records,
 'local_image_basis_indices':locind,'local_image_kernel_masks':[hex(v) for v in locnull],
 'all74_global_exterior_functionals':[hex(v) for v in duals],
 'literal_word_checks':checks}
(OUT/'d_arithmetic_local_transgression.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
