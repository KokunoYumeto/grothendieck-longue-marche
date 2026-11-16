"""Independent direct verification, with no search and no A-directory writes."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,sys
HERE=Path(__file__).resolve().parent
AD=HERE.parents[1]/'work_A'
p=AD/'check_A63_cross_cup.py'
D={'__file__':str(p),'__name__':'_independent_frame_reselection_'}
argv=sys.argv
try:
 sys.argv=[str(p)]
 with redirect_stdout(StringIO()):
  exec(compile(p.read_text().split('out=dict(scope=')[0],str(p),'exec'),D)
finally:sys.argv=argv
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
old=json.loads((AD/'Q6_actual_central_solution.json').read_text())
saved=json.loads((AD/'A76_fixed_action_frame_reselection.json').read_text())
f=saved['found'];assert f is not None
assert f['WE']==old['WE'] and f['PSHIFT']==old['PSHIFT']
O=D['O'];bf=tup(f['BFRAME']);new=tup(f['six_cup_BFRAME'])
assert new[0]==bf
assert bf[2]==tup(old['BFRAME'])[2]
assert O['ein'](bf,O['SS'])==O['ph'](O['SS'])
assert O['em'](O['ei'](bf),O['na'](O['ei'](bf)))==O['ONE']
assert D['ep'](D['SS'],2)==D['ep'](D['RR'],3)==D['ONE']
assert D['ph'](D['TT'])==D['TT']
assert D['na'](D['na'](D['SS']))==D['SS']
assert D['na'](D['na'](D['RR']))==D['RR']
assert D['ein'](new,D['SS'])==D['ph'](D['SS'])
assert D['em'](D['ei'](new),D['na'](D['ei'](new)))==D['ONE']
print('Original WE and PSHIFT literally unchanged; old head retained: PASS')
print('Original old-group s conjugacy and normalizer norm: PASS')
print('Actual six-cup source, literal cusp, negative action square: PASS')
print('Reselected actual six-cup s conjugacy and normalizer norm: PASS')
print('Conclusion: the fixed-frame obstruction does not extend to all residual frames with the original action fixed.')
(HERE.parent/'original_A56_frame_reselection_independent.json').write_text(json.dumps(dict(
 scope='Direct finite source/action/frame witness; no scalar/full involution conclusion',
 original_action_unchanged=True,head_unchanged=True,old_norm=True,
 six_cup_source=True,six_cup_action_square=True,six_cup_s_frame=True,
 all_checks='PASS'),indent=2)+'\n')
