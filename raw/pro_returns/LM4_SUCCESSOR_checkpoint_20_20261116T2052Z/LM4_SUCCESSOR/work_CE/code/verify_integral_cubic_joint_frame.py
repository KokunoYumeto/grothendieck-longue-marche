"""Original-law check of the compatible mod4,20-chief,128-scalar frame.

No solver is used here. The correction is read from the independently
constructed integral-frame certificate and tested in both actual laws.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
cert=json.loads((HERE.parent/'full_scalar_integral_frame_gate.json').read_text())
def tup(x):return tuple(tup(v)for v in x)if isinstance(x,list)else x
src=ROOT/'work_A/check_A66_W0_twenty_sframe.py'
code=src.read_text().split("out=dict(scope=")[0]
assert 'write_text' not in code
G={'__file__':str(src),'__name__':'_CE_twenty_direct'}
with redirect_stdout(StringIO()):exec(compile(code,str(src),'exec'),G)
O=G['O'];P=G['P'];z=tup(cert['scalar_ordinary_correction']);t=tup(cert['UT4_lower_T_correction'])
old=(O['AA0'],tup(cert['old_complete_center_correction']),O['HN0'])
K=((old,t),(G['zero'],)*4+z)
B20=G['em'](G['BFRAME'],K)
assert G['ein'](B20,G['SS'])==G['ph'](G['SS'])
assert G['em'](G['ei'](B20),G['na'](G['ei'](B20)))==G['ONE']
print('Actual complete20 law after old-center and lowerT/ordinaryZ correction: PASS')

src2=ROOT/'code/check_diagonal_scalar_frame_lift.py'
code2=src2.read_text().split('norm_columns=[]')[0]
# The source has an optional write branch, disabled by the literal argv.
H={'__file__':str(src2),'__name__':'_CE_scalar_direct'}
argv=sys.argv;sys.argv=[str(src2),'--full-cubic']
try:
 with redirect_stdout(StringIO()):exec(compile(code2,str(src2),'exec'),H)
finally:sys.argv=argv
KC=(H['A0'],tup(cert['initial_half_center']),z,H['U0'],H['H0'])
B128=H['gm'](H['B'],KC)
assert H['gin'](B128,H['S'])==H['S']
assert H['gm'](H['gi'](B128),H['ca'](H['gi'](B128)))==H['ONE']
print('Actual full128 law: corrected s-conjugacy and scalar normalizer norm1: PASS')
ap,mp,hp=H['old_project'](B20[0][0])
assert (ap,mp,hp)==(B128[0],B128[1],B128[4])
assert B20[1][4:]==B128[2]
print('The20 and128 frames have literally identical common projections: PASS')
B4=cert['corrected_mod4_free_frame']
def red(x):return(x&1)|(((x>>2)&1)<<1)|(((x>>4)&1)<<2)
mpairs=list(__import__('itertools').combinations_with_replacement(range(4),2))
a4=tuple(tuple(red(x)for x in row)for row in B4[0])
m4=tuple(red(x)if i!=j else x for x,(i,j)in zip(B4[1],mpairs))
assert a4==B128[0]and m4==B128[1]and tup(B4[2])==B128[4]
print('The integralmod4 frame has that same literal binary free-center projection: PASS')
out=dict(scope='Actual joint finite witness, compatible with the independently checked mod4 integral frame; higher-level proof separate',
 corrected_twenty_frame=B20,corrected_scalar_frame=B128,
 corrected_mod4_free_frame=B4,all_original_laws='PASS',common_projections='PASS',
 source_correction='work_CE/full_scalar_integral_frame_gate.json')
(HERE.parent/'integral_cubic_joint_frame_verified.json').write_text(json.dumps(out,indent=2)+'\n')
