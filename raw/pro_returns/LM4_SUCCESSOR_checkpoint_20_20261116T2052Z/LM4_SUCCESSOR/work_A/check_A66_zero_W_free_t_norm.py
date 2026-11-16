"""Old A56 central norm on root's exact zero-cusp-frame affine subfamily.
The original witness is read-only. A successful new tuple is verified by
the original operations and saved under a separate name.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,subprocess
import numpy as np
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):G=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
globals().update({k:v for k,v in G.items()if not k.startswith('__')})
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
old=json.loads((HERE/'Q6_actual_central_solution.json').read_text())
root=json.loads((HERE.parent/'records/A66_zero_cusp_action_free_frame_feasibility.json').read_text())
WE=tup(old['WE']);BFRAME=tup(old['BFRAME']);PSHIFT=tup(old['PSHIFT'])
phi0.__globals__['WE']=WE;ph.__globals__['PSHIFT']=PSHIFT
def apply_pair(tc,sc):
 global WE,BFRAME,PSHIFT
 WE=em((tc,ZA,HN0),WE);BFRAME=em(em((tc,ZA,HN0),BFRAME),(sc,ZA,HN0))
 phi0.__globals__['WE']=WE
 td=em(phi0(TT),ei(TT));assert td[0]==AA0 and td[2]==HN0
 PSHIFT=td[1];ph.__globals__['PSHIFT']=PSHIFT
 assert ph(TT)==TT and ph(SS)==ein(BFRAME,SS)
 assert na(na(SS))==SS and na(na(RR))==RR
def pair_from_mask(mask):
 tc=AA0;sc=AA0
 for j,(kind,i,a)in enumerate(LABELS):
  if mask>>j&1:
   vv=tuple(fsm(a,row)for row in(TBASE if kind=='tau'else SBASE)[i])
   if kind=='tau':tc=av(tc,vv)
   else:sc=av(sc,vv)
 return tc,sc
apply_pair(*pair_from_mask(root['solution_mask']))
ad=json.loads((HERE.parent/'work_CE/Q6_integral_affine_data.json').read_text())
E=tup(ad['new_basis_columns_in_old_EB']);ag=tup(ad['cochain_coboundary_in_V8'])
def cusp_frame():
 pa=av(av(mix(E,BFRAME[0]),ag),betaa(ag))
 vc=av(av(ag,mix(E,WC)),tuple(flin(CV,v)for v in ag))
 qq=av(mix(E,WE[0]),vc)
 return av(pa,qq)[:4]
assert not any(any(row)for row in mix(E,WE[0])[:4])
print('Root zero-W/free-t affine solution substituted into original group laws and normalized cusp coordinates: PASS')

def bkernel(cols):
 piv={};ker=[]
 for j,v in enumerate(cols):
  aux=1<<j
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i][0];aux^=piv[i][1]
   else:piv[i]=(v,aux);break
  if not v:ker.append(aux)
 return ker
def reducer(cols):
 piv={}
 for v in cols:
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 def red(v):
  for i in sorted(piv,reverse=True):
   if v>>i&1:v^=piv[i]
  return v
 return red,len(piv)
KH=bkernel(root['columns']);assert len(KH)==258
HOM=[pair_from_mask(v)for v in KH]
NR,nrank=reducer([packed(fsm(a,v))for v in ZNORM for a in(1,2,4)])
bs=em(ei(BFRAME),na(ei(BFRAME)));assert bs[0]==AA0 and bs[2]==HN0
target=NR(packed(bs[1]))
def qnorm(pair):
 t,u=pair;pt=(t,ZA,HN0);pu=(u,ZA,HN0)
 nt=em(pt,na(pt));nu=em(pu,ein(ei(BFRAME),na(pu)))
 assert nt[0]==nu[0]==AA0 and nt[2]==nu[2]==HN0
 return NR(packed(fva(nt[1],nu[1])))
FM=np.array([[fm(i,j)for j in range(8)]for i in range(8)],dtype=np.uint8)
LEFT=np.array([i for i,j in vpairs]);RIGHT=np.array([j for i,j in vpairs])
NH=[tuple(np.array(v,dtype=np.uint8)for v in pair)for pair in HOM]
def polar(a,b):
 total=np.zeros((8,8),dtype=np.uint8)
 for aa,bb in zip(a,b):
  total^=np.bitwise_xor.reduce(FM[aa[:,LEFT,None],bb.T[RIGHT][None,:,:]],axis=1)
  total^=np.bitwise_xor.reduce(FM[aa[:,RIGHT,None],bb.T[LEFT][None,:,:]],axis=1)
 return NR(packed(tuple(int(total[i,j]^(total[j,i]if i!=j else 0))for i,j in zpairs)))
Q=[qnorm(v)for v in HOM];P=[[0]*258 for _ in HOM]
for i in range(258):
 for j in range(i):P[i][j]=P[j][i]=polar(NH[i],NH[j])
for i,j in((0,1),(32,85),(100,257)):
 assert qnorm(tuple(av(a,b)for a,b in zip(HOM[i],HOM[j])))==Q[i]^Q[j]^P[i][j]
def qval(mask):
 ids=[i for i in range(258)if mask>>i&1];out=0
 for k,i in enumerate(ids):
  out^=Q[i]
  for j in ids[:k]:out^=P[i][j]
 return out
RC=[sum(P[i][j]<<(108*j)for j in range(258))for i in range(258)]
RAD=bkernel(RC);RV=[qval(v)for v in RAD];RRAD,rrank=reducer(RV)
span={}
def ins(v):
 while v:
  i=v.bit_length()-1
  if i in span:v^=span[i]
  else:span[i]=v;return True
 return False
for v in RAD:assert ins(v)
COMP=[]
for i in range(258):
 if ins(1<<i):COMP.append(1<<i)
n=len(COMP);CQ=[RRAD(qval(v))for v in COMP]
CP=[[0]*n for _ in range(n)]
for i in range(n):
 for j in range(i):CP[i][j]=CP[j][i]=RRAD(qval(COMP[i]^COMP[j])^qval(COMP[i])^qval(COMP[j]))
ct=RRAD(target)
print('Zero-W/free-t central norm: variables258; polar radical',len(RAD),'; radical image',rrank,'; core',n)
core=dict(n=n,q=CQ,polar=CP,target=ct,complement=COMP,radical=RAD,radical_values=RV,
 homogeneous_kernel=KH,full_target=target,affine_solution=root['solution_mask'])
(HERE/'A66_zero_W_free_t_quadratic_core.json').write_text(json.dumps(core,indent=2)+'\n')
assert n<=31,'Core requires a different exact solver; no obstruction inferred.'
words=[n]
for v in CQ+[v for row in CP for v in row]+[ct]:words.extend((v&((1<<64)-1),v>>64))
inp='\n'.join(map(str,words))+'\n';(HERE/'A66_zero_W_free_t_quadratic_core.in').write_text(inp)
search=subprocess.run([str(HERE/'check_Q6_quadratic_core')],input=inp,text=True,capture_output=True,timeout=60)
(HERE/'A66_zero_W_free_t_quadratic_search.out').write_text(search.stdout+search.stderr)
print(search.stdout.strip())
if search.returncode!=0:
 print('No successful old-group witness produced; no larger-family impossibility inferred.')
 raise SystemExit(search.returncode)
cmask=int(search.stdout.split()[1]);orig=0
for i,v in enumerate(COMP):
 if cmask>>i&1:orig^=v
rc,rank=bit_solve(RV,qval(orig)^target);assert rc is not None
ans=orig
for i,v in enumerate(RAD):
 if rc>>i&1:ans^=v
assert qval(ans)==target
tc=AA0;sc=AA0
for i,(a,b)in enumerate(HOM):
 if ans>>i&1:tc=av(tc,a);sc=av(sc,b)
apply_pair(tc,sc)
assert not any(any(row)for row in mix(E,WE[0])[:4])
bs=em(ei(BFRAME),na(ei(BFRAME)))
bz=fsolve(ZNORM,bs[1]);assert bz is not None
BFRAME=(BFRAME[0],fva(BFRAME[1],bz),BFRAME[2])
assert em(ei(BFRAME),na(ei(BFRAME)))==ONE
q=av(WE[0],la(WC));assert av(q,ba(q))==AA0
JFRAME=(q,ZA,HS);assert na(RR)==ein(JFRAME,ei(RR))
js=em(ei(JFRAME),na(ei(JFRAME)));jz=fsolve(ZNORM,js[1])
if jz is None:
 out=dict(scope='Partial W0/free-t datum: old action/cusp/s-frame solved; displayed r-frame has not been norm-corrected',
  WE=WE,PSHIFT=PSHIFT,BFRAME=BFRAME,JFRAME=JFRAME,
  core_assignment=cmask,homogeneous_assignment=ans,radical_assignment=rc,
  s_frame_checks='PASS',r_frame_conjugacy='PASS',r_frame_norm_solved=False,r_initial_norm=js[1],
  normalized_cusp_frame_vectors=cusp_frame(),free_positive_cusp_inner=mix(E,WE[0])[:4])
 (HERE/'A66_zero_W_free_t_partial.json').write_text(json.dumps(out,indent=2)+'\n')
 print('Partial tuple saved: old negative action, cusp and s-normalizer PASS; the convenient r-frame requires a broader affine correction.')
 raise SystemExit(0)
JFRAME=(JFRAME[0],fva(JFRAME[1],jz),JFRAME[2])
assert em(ei(JFRAME),na(ei(JFRAME)))==ONE
out=dict(scope='New actual A56 tuple in the zero-cusp-frame subfamily; original witness unchanged',
 WE=WE,PSHIFT=PSHIFT,BFRAME=BFRAME,JFRAME=JFRAME,
 core_assignment=cmask,homogeneous_assignment=ans,radical_assignment=rc,
 all_direct_frame_checks='PASS',normalized_cusp_frame_vectors=cusp_frame(),free_positive_cusp_inner=mix(E,WE[0])[:4])
(HERE/'A66_zero_W_free_t_A56_solution.json').write_text(json.dumps(out,indent=2)+'\n')
print('New zero-W/free-t A56 tuple: literal cusp, action square, both frame conjugacies/norms and zero t PASS.')
