#!/usr/bin/env python3
"""Exhaust the lower N-centralizer freedom in the rank4 degree6 test.

N/(N intersect D6(K)) has order2^303 and is class2 exponent4.
Its Frattini subgroup is central elementary abelian. Fixed
subgroup generators are computed through its Frattini quotient,
with every connecting defect evaluated as an actual group word.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
mp=R['mulpoly'];Nwords=R['Nwords'];collapse=R['collapse'];poly=R['poly'];bp=R['bitpoly']
zero=(0,0,0,0,0)
def gx(a,b):return tuple(x^y for x,y in zip(a,b))
def product(a,b):
 c=list(gx(a,b))
 for i in range(3):
  for j in range(3-i):c[i+j+2]^=mp(a[i],b[j],j+2)
 return tuple(c)
def inverse(a):
 aa=product(a,a);aaa=mp(mp(a[0],a[0],2),a[0],2)
 c=list(gx(a,aa));c[4]^=aaa;return tuple(c)
def square(a):return product(a,a)
def comm(a,b):return product(product(product(a,b),inverse(a)),inverse(b))
def low(a):return a[0]^(a[1]<<16)^(a[2]<<80)^(a[3]<<336)
def lead(v):return (v&-v).bit_length()-1
def fromword(w):
 q,ww=collapse(w);assert q==R['e'];P=poly(ww)
 assert not P[1].any();return tuple(bp(P[n]) for n in range(2,7))
G=[fromword(w) for w in Nwords];SG=[fromword([0]+w+[0]) for w in Nwords]
for a in G:assert product(a,inverse(a))==zero

# The central Frattini subgroup W in the class2 exponent4 quotient.
W={};sources=[]
for i in range(97):
 sources.append(('square',i,i))
 candidates=[(square(G[i]),square(SG[i]),len(sources)-1)]
 for j in range(i):
  sources.append(('comm',i,j));candidates.append((comm(G[i],G[j]),comm(SG[i],SG[j]),len(sources)-1))
 for a,sa,num in candidates:
  coeff=1<<num;v=low(a)
  while v:
   k=lead(v)
   if k not in W:W[k]=(a,sa,coeff);break
   a=gx(a,W[k][0]);sa=gx(sa,W[k][1]);coeff^=W[k][2];v=low(a)
Wkeys=sorted(W);WB=[W[k] for k in Wkeys];wd=len(WB)
assert all(not a[0] and not a[1] for a,sa,coeff in WB)
def w_reduce(a,sa=None):
 coeff=0
 for j,k in enumerate(Wkeys):
  if (low(a)>>k)&1:
   a=product(a,WB[j][0]);coeff^=1<<j
   if sa is not None:sa=product(sa,WB[j][1])
 return a,sa,coeff
def w_coords(a):
 v=low(a);ans=0
 for j,k in enumerate(Wkeys):
  if (v>>k)&1:v^=low(WB[j][0]);ans^=1<<j
 assert not v
 return ans
def w_element(mask):
 a=zero;sa=zero
 for j,(g,sg,_) in enumerate(WB):
  if (mask>>j)&1:a=gx(a,g);sa=gx(sa,sg)
 return a,sa

# Basis of N/Frattini(N image), with full degree6 lifts retained.
V={}
for i,(a,sa) in enumerate(zip(G,SG)):
 a,sa,wc=w_reduce(a,sa);recipe=[('N',i),('W',wc)]
 for k in sorted(V):
  if (low(a)>>k)&1:
   a=product(a,inverse(V[k][0]));sa=product(sa,inverse(V[k][1]));recipe.append(('Vinv',k))
   a,sa,wc=w_reduce(a,sa);recipe.append(('W',wc))
 if low(a):
  k=lead(low(a));assert k not in V;V[k]=(a,sa,recipe)
Vkeys=sorted(V);VB=[V[k] for k in Vkeys];vd=len(VB)
assert vd+wd==303
def v_coords(a):
 a,_,_=w_reduce(a);v=0
 for j,k in enumerate(Vkeys):
  if (low(a)>>k)&1:
   a=product(a,inverse(VB[j][0]));a,_,_=w_reduce(a);v^=1<<j
 assert not low(a);return v
def v_element(mask):
 a=zero;sa=zero
 for j,(g,sg,_) in enumerate(VB):
  if (mask>>j)&1:a=product(a,g);sa=product(sa,sg)
 return a,sa
SW=[w_coords(sa) for a,sa,_ in WB]
SV=[v_coords(sa) for a,sa,_ in VB]
def columns_null(cols):
 bas={};null=[]
 for j,col in enumerate(cols):
  v=col;w=1<<j
  while v:
   k=v.bit_length()-1
   if k not in bas:bas[k]=(v,w);break
   v^=bas[k][0];w^=bas[k][1]
  if not v:null.append(w)
 return bas,null
def solve(v,bas):
 w=0
 while v:
  k=v.bit_length()-1
  if k not in bas:return False,w,v
  v^=bas[k][0];w^=bas[k][1]
 return True,w,0
def remainder(v,bas):
 for k in sorted(bas,reverse=True):
  if (v>>k)&1:v^=bas[k][0]
 return v
WC,WF=columns_null([(1<<j)^s for j,s in enumerate(SW)])
_,VF=columns_null([(1<<j)^s for j,s in enumerate(SV)])
VG=[v_element(v) for v in VF]
connecting=[]
for a,sa in VG:
 delta=product(a,inverse(sa));wc=w_coords(delta)
 connecting.append(remainder(wc,WC))
CB,UF=columns_null(connecting)
extras=[];certs=[]
for v in WF:
 a,sa=w_element(v);delta=product(a,inverse(sa));assert not low(delta)
 extras.append(delta[4]);certs.append({'kind':'fixed_Frattini','W_coefficients':hex(v)})
for v in UF:
 a=zero;sa=zero
 for j,(g,sg) in enumerate(VG):
  if (v>>j)&1:a=product(a,g);sa=product(sa,sg)
 delta=product(a,inverse(sa));wc=w_coords(delta)
 good,wfix,rem=solve(wc,WC);assert good and not rem
 w,sw=w_element(wfix);a=product(w,a);sa=product(sw,sa)
 delta=product(a,inverse(sa));assert not low(delta)
 extras.append(delta[4]);certs.append({'kind':'lifted_fixed_Frattini_quotient',
  'V_fixed_basis_combination':hex(v),'W_correction':hex(wfix)})
assert len(extras)==len(WF)+len(UF)

def augmented_test(basis,target=None):
 S=[R['action'](w,R['MS']) for w in basis]
 SR=[R['action'](w,R['MSR']) for w in basis]
 cols=[w^s for w,s in zip(basis,S)]+[s^r for s,r in zip(S,SR)]+extras
 target=R['target'] if target is None else target
 bas=R['echelon'](cols);good,sol,rem=R['solve'](target,bas)
 result={'rank':len(bas),'solvable':good,'solution':hex(sol),'obstruction':hex(rem)}
 if not good:
  functional=1<<(rem.bit_length()-1)
  for k in sorted(bas):
   if (functional&bas[k][0]).bit_count()%2:functional^=1<<k
  assert all((functional&c).bit_count()%2==0 for c in cols)
  assert (functional&target).bit_count()%2==1
  result['separating_functional']=hex(functional)
 return result
small=augmented_test(R['W']);large=augmented_test(R['Z'])
q,w27=collapse(R['wb27']+[0]+R['inverse'](R['wb27'])+R['wa27']+[1]+R['inverse'](R['wa27'])+[2,0])
assert q==R['e'];p27=poly(w27);assert all(not p27[n].any() for n in range(1,6))
original27=augmented_test(R['Z'],bp(p27[6]))
summary={'N_image_order':'2^303','Frattini_dimension':wd,'Frattini_quotient_dimension':vd,
 'fixed_Frattini_dimension':len(WF),'fixed_quotient_before_connecting':len(VF),
 'connecting_obstruction_rank':len(CB),'fixed_quotient_lifting_dimension':len(UF),
 'complete_s_centralizer_generators':len(extras),
 'gamma3N_correction_rank_with_centralizers':small['rank'],
 'gamma3N_corrections_and_lower_centralizer_solve':small['solvable'],
 'full_degree6_rank_with_centralizers':large['rank'],
 'full_degree6_and_lower_centralizer_solve':large['solvable'],
 'D27_original_H2_action_solve':original27['solvable'],
 'scope':'Complete lower N-centralizer freedom preserving the selected K/D6 action and fixed Q-conjugator coordinates; no exclusion of other homology actions with the same CM pair.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank4_centralizer.json').write_text(json.dumps({'summary':summary,
 'gamma3N_augmented':small,'full_augmented':large,
 'D27_original_H2_augmented':original27,
 'centralizer_generator_certificates':certs,
 'Frattini_basis_source_masks':[hex(c) for a,sa,c in WB],
 'Frattini_quotient_basis_recipes':[rec for a,sa,rec in VB],
 'fixed_quotient_basis':[hex(v) for v in VF],
 'centralizer_degree6_defects':[hex(v) for v in extras]},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
