"""Reconstruct one locally compatible W0 tuple in the original old group law."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):G=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
globals().update({k:v for k,v in G.items()if not k.startswith('__')})
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
w=json.loads((HERE/'A66_zero_W_free_t_partial.json').read_text())
c=next(x for x in json.loads((HERE/'A66_W0_radical_local_gate.json').read_text())['solutions'] if x['local_indices']==[6,3])
WE=tup(w['WE']);BFRAME=tup(w['BFRAME']);PSHIFT=tup(w['PSHIFT'])
phi0.__globals__['WE']=WE;ph.__globals__['PSHIFT']=PSHIFT
tc,sc=AA0,AA0
for j,(kind,i,a)in enumerate(LABELS):
 if c['full360_mask']>>j&1:
  v=tuple(fsm(a,row)for row in(TBASE if kind=='tau'else SBASE)[i])
  if kind=='tau':tc=av(tc,v)
  else:sc=av(sc,v)
WE=em((tc,ZA,HN0),WE);BFRAME=em(em((tc,ZA,HN0),BFRAME),(sc,ZA,HN0))
phi0.__globals__['WE']=WE
dif=em(phi0(TT),ei(TT));assert dif[0]==AA0 and dif[2]==HN0
PSHIFT=dif[1];ph.__globals__['PSHIFT']=PSHIFT
assert ph(TT)==TT and ph(SS)==ein(BFRAME,SS)
assert na(na(SS))==SS and na(na(RR))==RR
bn=em(ei(BFRAME),na(ei(BFRAME)));assert bn[0]==AA0 and bn[2]==HN0
z=fsolve(ZNORM,bn[1]);assert z is not None
BFRAME=(BFRAME[0],fva(BFRAME[1],z),BFRAME[2])
assert em(ei(BFRAME),na(ei(BFRAME)))==ONE
ad=json.loads((HERE.parent/'work_CE/Q6_integral_affine_data.json').read_text())
E=tup(ad['new_basis_columns_in_old_EB']);ag=tup(ad['cochain_coboundary_in_V8'])
pa=av(av(mix(E,BFRAME[0]),ag),betaa(ag))
vc=av(av(ag,mix(E,WC)),tuple(flin(CV,v)for v in ag))
pw=mix(E,WE[0]);t=av(pa,av(pw,vc))[:4]
assert not any(any(row)for row in pw[:4])
local=sum(t[i][a]<<(3*(4*j+i))for j,a in enumerate((8,11,20,23))for i in range(4))
assert local==c['target_local']
q=av(WE[0],la(WC));JFRAME=(q,ZA,HS)
assert na(RR)==ein(JFRAME,ei(RR))
jn=em(ei(JFRAME),na(ei(JFRAME)));jz=fsolve(ZNORM,jn[1])
if jz is not None:JFRAME=(JFRAME[0],fva(JFRAME[1],jz),JFRAME[2])
out=dict(scope='Actual W0 old s-frame with joint local lower-six/ordinary-sixteen conditions; r status explicit',
 WE=WE,PSHIFT=PSHIFT,BFRAME=BFRAME,JFRAME=JFRAME,
 r_frame_norm_solved=jz is not None,r_initial_norm=jn[1],s_frame_checks='PASS',
 normalized_cusp_frame_vectors=t,free_positive_cusp_inner=pw[:4],
 local_indices=c['local_indices'],local_target=local,full360_correction=c['full360_mask'])
(HERE/'A66_W0_rank4_partial.json').write_text(json.dumps(out,indent=2)+'\n')
print('Original group-law negative square, literal cusp, s conjugacy/norm, W0 and selected local coordinates: PASS')
print('Convenient r-frame centrally correctable:',jz is not None,'; broader r-frame existence is a separate argument.')
