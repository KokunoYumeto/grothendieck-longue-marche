"""Direct full20 check of the integral-compatible scalar-frame correction.

Reads CE's actual GR(4,3) free-frame lift, applies its old-center/Z/T
corrections in the original full20 law, and emits the same correction
format accepted by the independent root scalar-cover verifier.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
model=HERE/'check_A66_W0_twenty_sframe.py'
src=model.read_text().split('out=dict(scope=')[0]
D={'__file__':str(model),'__name__':'__A69_model__'}
with redirect_stdout(StringIO()):exec(compile(src,str(model),'exec'),D)
O=D['O'];P=D['P']
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
ce=json.loads((ROOT/'work_CE/full_scalar_integral_frame_gate.json').read_text())
raw=json.loads((ROOT/'records/full_cubic_scalar_frame_lift.json').read_text())
assert ce['mod4_free_norm']=='PASS'and ce['scalar_equation_after_integral_half']and ce['UT4_equation']
mc=tup(ce['old_complete_center_correction']);tc=tup(ce['UT4_lower_T_correction']);zc=tup(ce['scalar_ordinary_correction'])
uc=(D['zero'],)*4
q=(((O['AA0'],mc,O['HN0']),tc),uc+zc)
assert D['ein'](q,D['SS'])==D['SS']
bf=D['em'](D['BFRAME'],q)
assert D['ph'](D['SS'])==D['ein'](bf,D['SS'])
assert D['em'](D['ei'](bf),D['na'](D['ei'](bf)))==D['ONE']
assert D['ph'](D['TT'])==D['TT']
assert D['na'](D['na'](D['SS']))==D['SS']and D['na'](D['na'](D['RR']))==D['RR']
projected=O['flin'](tup(raw['old_center_projection_columns']),mc)
assert projected==tup(ce['initial_half_center'])
assert O['fva'](tup(raw['full20_frame_projection'][1]),projected)==tup(ce['corrected_mod2_free_center'])
print('Original full20 law: integral-compatible old-center/Z/T correction retains s-conjugacy and norm1: PASS')
print('Actual free-center projection agrees with the corrected GR(4,3) frame modulo2: PASS')
print('Literal cusp and quotient negative-square checks: PASS')
out=dict(scope='Integral-compatible full20/scalar128 frame correction; GR(4,3) free-frame proof in CE certificate and scalar-cover law independently verified by root',
 old_center_correction=mc,T_correction=tc,U_correction=uc,ordinary_correction=zc,
 corrected_full20_BFRAME=bf,corrected_mod4_free_frame=ce['corrected_mod4_free_frame'],
 free_mod2_center=ce['corrected_mod2_free_center'],forced_free_half=ce['initial_half_center'],
 free_center_projection='PASS',full20_direct_checks='PASS',
 integral_source='work_CE/full_scalar_integral_frame_gate.json',
 scalar_status='Exact scalar equations verified; independent original128-cover verifier is the final check')
(HERE/'A69_integral_scalar_frame_solution.json').write_text(json.dumps(out,indent=2)+'\n')
