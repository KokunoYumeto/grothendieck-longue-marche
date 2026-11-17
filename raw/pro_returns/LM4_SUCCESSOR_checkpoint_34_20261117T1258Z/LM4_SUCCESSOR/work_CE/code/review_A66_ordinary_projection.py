"""Independent source-law projection of the current A66 square obstruction.
The specified old affine tuple is held fixed. No global obstruction claimed.
"""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
p=HERE.parents[1]/'work_A/check_A66_cubic_twenty.py'
s=p.read_text().split("out=dict(scope='Specified zero-t A64 affine datum;")[0]
assert 'write_text'not in s
G={'__file__':str(p),'__name__':'_CE_A66_projection_review'}
exec(compile(s,str(p),'exec'),G)
INNER=G['INNER'];zero=G['zero'];TF=G['TF3'];bact=G['bact']
ordinary=[i for i in range(4,20)if any(INNER[i])]
assert ordinary==[4,5,6,8,9,10,12,13,14,19]
assert all(G['cv3'](v)==v for v in TF)
for i in range(20):
 for v in TF:
  z=tuple(v if j==i else zero for j in range(20))
  assert bact(z)[4:]==z[4:]
print('All80 cusp-inner basis directions have zero ordinary norm component: PASS')
print('Nonzero ordinary square slots:',ordinary)
print('The ordinary projection forgets all six T coordinates; old T-inner action changes are invisible there.')
assert INNER[4][0]==1
print('Explicit fixed-affine obstruction: ordinary slot00, weight0 has value1.')
out=dict(scope='Actual ordinary16-cup projection; fixed A56 affine action/frame only',
         nonzero_ordinary_slots=ordinary,annihilator=dict(slot=4,weight=0,value=1),
         all_80_cusp_inner_norm_columns_have_zero_ordinary_projection=True,
         old_degree_two_inner_changes_project_to_identity=True,
         ordinary_inner_rows=INNER[4:],checks='PASS')
(HERE.parent/'A66_ordinary_projection_independent.json').write_text(json.dumps(out,indent=2)+'\n')
