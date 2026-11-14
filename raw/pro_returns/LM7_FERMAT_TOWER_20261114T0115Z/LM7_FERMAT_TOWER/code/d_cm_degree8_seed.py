#!/usr/bin/env python3
"""Evaluate the exact recorded D31 conjugators one Zassenhaus degree farther.

This intentionally performs the full actual word calculation. It changes no
recorded lower coordinate and does not linearize the degree-eight equation.
All imported dependencies and all output are in this separate experiment tree.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np

OUT=Path(__file__).resolve().parent
started=time.time()
with redirect_stdout(io.StringIO()):
    R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
inv=R['inverse'];comm=R['comm'];central=R['central']
J30=json.loads((OUT/'d_cm_rank4_joint.json').read_text())['witness']
J31all=json.loads((OUT/'d_cm_rank4_degree7.json').read_text())
J31=J31all['witness']
Uwords=list(R['Wwords'])
for i,j,k in J31all['degree7_basis_indices']:
    Uwords.append(comm(R['relwords'][i],comm(R['relwords'][j],R['lieword'](R['L3'][k]))))
assert len(Uwords)==1860

def select_words(mask,words):
    ans=[]
    while mask:
        bit=mask&-mask
        ans+=words[bit.bit_length()-1]
        mask^=bit
    return ans

wa=central(int(J30['upper_A_correction'],16),2)+central(int(J30['previous_Z4_A_central_change'],16))+R['wa']
wb=central(int(J30['upper_beta_correction'],16),2)+central(int(J30['previous_Z4_beta_central_change'],16))+R['wb']
wa=select_words(int(J30['gamma3N_A_correction'],16),R['Wwords'])+wa
wb=select_words(int(J30['gamma3N_beta_correction'],16),R['Wwords'])+wb
assert J30['lambda_mod288']==1
wa=central(int(J31['upper_A_correction'],16),2)+central(int(J31['lower_A_change'],16))+wa
wb=central(int(J31['upper_beta_correction'],16),2)+central(int(J31['lower_beta_change'],16))+wb
wa=select_words(int(J31['gamma3N_A_correction'],16),Uwords)+wa
wb=select_words(int(J31['gamma3N_beta_correction'],16),Uwords)+wb
lam=J31['lambda_mod288'];assert lam==1
cusp=wb+[0]+inv(wb)+wa+[1]+inv(wa)+[2,0]*lam
assert len(cusp)==J31['corrected_B_word_length']
print('Exact recorded cusp word:',len(cusp),'B letters',flush=True)
q,w=R['collapse'](cusp);assert q==R['e']
print('Collapsed K word:',len(w),'letters',flush=True)
P=R['poly'](w,8)
assert all(not p.any() for p in P[1:8])
target=R['bitpoly'](P[8])
print('Degree-eight target nonzero:',bool(target),'support:',target.bit_count(),flush=True)

# Multiplier changes preserving the complete T2 action are multiples of48.
# Unlike the previous transition, t^48 is now a nonzero degree-eight column.
q,ct=R['collapse']([0,1]*48);assert q==R['e']
CP=R['poly'](ct,8);assert all(not x.any() for x in CP[1:8])
multiplier=R['bitpoly'](CP[8]);assert multiplier
summary={
    'recorded_D31_seed_retained_exactly':True,
    'B_cusp_word_length':len(cusp),'K_cusp_word_length':len(w),
    'lower_degrees_one_through_seven_zero':True,
    'degree8_target_nonzero':bool(target),'degree8_target_support':target.bit_count(),
    'degree8_target':hex(target),
    't48_degree8_nonzero':True,'t48_degree8_support':multiplier.bit_count(),
    't48_degree8_column':hex(multiplier),
    'scope':'Only evaluation of the exact recorded representative; no lift or nonlift assertion yet.',
    'elapsed_seconds':round(time.time()-started,3)
}
(OUT/'d_cm_degree8_seed.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['degree8_target','t48_degree8_column']},indent=2),flush=True)
