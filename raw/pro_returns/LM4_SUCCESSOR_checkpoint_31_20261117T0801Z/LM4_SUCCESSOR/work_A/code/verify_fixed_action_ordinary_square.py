"""Action-only recheck of the stored A64 ordinary-cup obstruction.

No witness search or witness mutation. The imported legacy group builder
performs its existing exploratory algebra, but has no artifact writes.
The exhaustive unframed inference is proved in the accompanying note.
"""
from pathlib import Path
import hashlib,json,sys

HERE=Path(__file__).resolve().parent
A=HERE.parent
source=A/'check_A66_ordinary_cubic.py'
prefix=source.read_text().split("out=dict(scope='Ordinary16-cup quotient;")[0]
assert 'write_text' not in prefix
oldargv=sys.argv
sys.argv=[str(source)]
G={'__file__':str(source),'__name__':'_action_only_review'}
try:
    exec(compile(prefix,str(source),'exec'),G)
finally:
    sys.argv=oldargv

O=G['O'];INNER=G['INNER'];na=G['na'];zero=G['zero']
assert INNER[0][0]==1
assert G['sd']!=G['SS'] or G['rd']!=G['RR']
assert G['ac'](O['SS'])==G['AZ']
assert G['SS'][1]==G['TZ']
assert O['frank'](G['cc'])==44
assert O['frank'](G['pc'])==40
assert O['frank'](G['cob'])==36

checked=0
for i in range(16):
    for v0 in O['TF']:
        for scalar in (1,2,4):
            v=G['fsm'](scalar,G['j3'](v0))
            z=tuple(v if j==i else zero for j in range(16))
            element=(O['ONE'],z)
            assert na(element)==element
            assert G['em'](element,element)==G['ONE']
            checked+=1

assert checked==192
print('Actual source S^2=R^3=1 and canonical-c action/square: PASS')
print('Actual literal-cusp positive ordinary action: PASS')
print('Complete source cocycle rank44; joint condition rank40; coboundary rank36: PASS')
print('Source free cusp coordinate at S is literally zero: PASS')
print('All192 binary cusp-inner directions are fixed by the negative action and have zero norm: PASS')
print('Stored negative square is Inner(t), ordinary00 weight0=1: PASS')
print('The square moves at least one actual source generator: PASS')
print('Unframed centralizer surjectivity is the general zero-cup proof in the accompanying research note.')

names=['A63_zero_t_A56_solution.json','A66_ordinary_cubic_result.json','check_A66_ordinary_cubic.py']
out=dict(scope='Fixed finite action; no prescribed-frame hypothesis in the accompanying proof; literal tau required',
         hashes={n:hashlib.sha256((A/n).read_bytes()).hexdigest() for n in names},
         cocycle_rank=44,joint_rank=40,coboundary_rank=36,
         source_s_free_cusp_zero=True,cusp_inner_binary_directions=checked,
         nonzero_coordinate=dict(slot='ordinary00',weight=0,value=1),
         moves_s=G['sd']!=G['SS'],moves_r=G['rd']!=G['RR'],
         inner_square=INNER,checks='PASS')
(A/'fixed_action_ordinary_square_verified.json').write_text(json.dumps(out,indent=2)+'\n')
