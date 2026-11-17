"""Independently check the explicit fourteen-variable certificate, without SNF."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json

root = Path(__file__).resolve().parents[1]
cp = root / 'records/root_coarse_corrections29.json'
hp = root / 'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
c, h = json.loads(cp.read_text()), json.loads(hp.read_text())
assert hashlib.sha256(cp.read_bytes()).hexdigest() == '97f7c8b246182f75a21c81bcae49c02c0a019e4b2381e9cfdda242e18b18064a'
assert hashlib.sha256(hp.read_bytes()).hexdigest() == 'f1f12e21935c05d0c4aa6846624c16a480be55752c5781832c49cb5f2afe1e5e'
rows = {(r['operator'], r['retained_generator']): r for r in c['rows'] if r['section'] == 'old_c_section'}
heads = {('m', 1): [-1,2,1], ('m', 2): [1], ('m', 3): [3,-2,1],
         ('v', 1): [3,2,-3], ('v', 3): [3,-2,1]}
classes = {('m',1): {}, ('m',2): {}, ('m',3): {},
           ('v',1): {():1,(3,-2,-3):-1},
           ('v',3): {(3,-2):1,(3,-2,1):-1}}
for key, head in heads.items():
    row = rows[key]
    assert row['coarse_head_T'] == head
    got = {tuple(t['retained_word_T']): t['coefficient'] for t in row['module_coefficients'] if t['family_index_F11'] == 2}
    assert got == classes[key], key
for source, head in [('m',[-1,2]),('v',[3,-2,-3])]:
    data=h['all_four_signed_source_operators'][source]['family_images']['2']
    assert data['signed_core']==2 and data['retained_head']==head

eq = [
    ({'F0':1,'G0':-1},0),
    ({'F2':1,'F3':1,'F0':-1,'G1':-1,'G0':1},0),
    ({'F3':1,'G3':-1},0),
    ({'G2':1,'G3':1,'G0':-1,'F1':-1,'M':-1},0),
    ({'X2':1,'X3':1,'X0':-1,'X1':-1,'G1':1,'F1':-1,'M':-1},0),
    ({'X1':1,'X3':-1,'X0':1,'X2':-1,'G2':1,'F2':-1,'F0':1,'G0':-1,'M':1},0),
    ({'F1':1,'F3':-1,'F0':-1,'G2':-1,'X0':1,'V':-1},-1),
    ({'X2':1,'X3':1,'X1':-1,'G1':1,'F1':-1,'V':-1},1),
]
coefficients=[-1,-2,1,1,-3,-2,-1,1]
total=Counter(); rhs=0
for scale,(left,right) in zip(coefficients,eq):
    for variable,value in left.items(): total[variable]+=scale*value
    rhs+=scale*right
assert len(total)==14 and all(v==0 for v in total.values())
assert rhs==2 and rhs%3==2
out={'status':'PASS_EXACT_UNRESTRICTED_SECTION_CERTIFICATE',
     'utc':datetime.now(timezone.utc).isoformat(),
     'inputs':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (cp,hp)},
     'equations':[{'left':left,'right':right} for left,right in eq],
     'combination':coefficients,'combined_coefficients':dict(sorted(total.items())),
     'combined_right_side':rhs,'combined_right_side_mod3':rhs%3,
     'scope':'Complete selected actual color/heads checked. Eight manually derived equations cancel on fourteen unrestricted variables. No delta, paired-color, inverse-source, Smith-normal-form, or bounded-search assumption.'}
dest=root/'records/root_arbitrary_section_certificate29.json'
assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print('PASS: actual source heads and entire selected B-color defects.')
print('PASS: eight equations cancel all14 unrestricted variables; right side2, also nonzero modulo3.')
