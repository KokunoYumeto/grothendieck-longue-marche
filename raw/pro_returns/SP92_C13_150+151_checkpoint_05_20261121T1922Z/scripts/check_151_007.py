"""Symbolic coordinate checks prompted by the ink of 151_scan007.

These check the stated coordinate realization, not an abstract presentation.
The separate pointed-set argument is recorded with its hypotheses below.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

W = Path(__file__).resolve().parents[1]
maps = {
    'p0': lambda t: (t[0],), 'p12': lambda t: (t[0], t[1]),
    'p13': lambda t: (t[0], t[2]), 'p11': lambda t: (t[0], t[0]),
    'rho2': lambda t: (t[2], t[0], t[1]),
    's': lambda t: (t[1], t[0]),
    's1': lambda t: (t[0], t[2], t[1]),
    's2': lambda t: (t[2], t[1], t[0]),
    's3': lambda t: (t[1], t[0], t[2]),
    'd1': lambda t: (t[1], t[0], t[0]),
    'd2': lambda t: (t[0], t[1], t[0]),
}
def ev(expr, args):
    out = tuple(args)
    for f in reversed(expr.split()):
        out = maps[f](out)
    return out

specs = [
    ('cancelled top projection equality', 'xyz', ['p0 p12', 'p0 p13', 'p0 p12 rho2 s2'], True),
    ('cancelled top permutation equality', 'xyz', ['rho2 s2', 's3 rho2'], True),
    ('cancelled p0 p12 sigma1 equality', 'xyz', ['p0 p12 s1', 'p0 p12'], True),
    ('cancelled delta1 sigma coordinates', 'xy', ['d1 s'], ('x','y','y')),
    ('cancelled intermediate rho-sigma output', 'xyz', ['rho2 s2'], ('x','z','y')),
    ('live stabilizer of delta2', 'xy', ['s2 d2', 'd2'], True),
    ('literal live p11 relation versus its expected p12', 'xyz', ['p12 s3', 's p11'], False),
    ('refined p12 relation', 'xyz', ['p12 s3', 's p12'], True),
]
rows=[]
for claim, args, expressions, expected in specs:
    values=[ev(e,args) for e in expressions]
    if isinstance(expected, bool):
        result=len(set(values))==1
        assert result==expected
    else:
        assert values[0]==expected
        result=True
    rows.append(dict(claim=claim,arguments=list(args),expressions=expressions,values=values,result=result))
stamp=datetime.now(timezone.utc).isoformat()
(W/'records/151_007_computation.json').write_text(json.dumps({'time_utc':stamp,'rows':rows},ensure_ascii=False,indent=2)+'\n')
p=W/'records/root_mathematical_checks.json'
events=json.loads(p.read_text())
assert not any(e['statement_id'].startswith('151-007-') for e in events), 'Do not overwrite prior registered checks.'
for i,row in enumerate(rows,1):
    outcome='; '.join(f'{e} -> {tuple(v)}' for e,v in zip(row['expressions'],row['values']))
    typ='computation or formal certificate'
    if i==7:typ='refuted, with refined statement 151-007-coordinate-08'
    if i==5:
        outcome+='; the cancelled source continuation instead reads (y,x,z), which differs. The source trial is preserved as cancelled.'
    events.append(dict(page='151_scan007',statement_id=f'151-007-coordinate-{i:02d}',date=stamp,
        who='root; GPT-6 Astra Pro; effort not exposed; run SP92',type=typ,
        outcome=row['claim']+': '+outcome+'. Coordinate realization only; scripts/check_151_007.py.'))

proof='If E0 is a singleton, e1=delta0(*) and e2=delta1(e1), delta0 p0 is constant e1. The previously displayed sigma delta0=delta0 makes e1 fixed. The displayed rho delta1 delta0=sigma1 delta1 delta0=delta1 delta0 fixes e2 under rho and sigma1; if these generate G3, all of G3 fixes e2. The relation p12 delta1=sigma then gives p12(e2)=e1, and delta1 is pointed by definition. Substituting delta2=rho^2 delta1 and rho^3=id into the three value relations gives p12 delta2=id, p12 rho delta2=sigma, and p12 rho^2 delta2=constant e1. This is a conditional algebraic check of these consequences, not a proof of completeness of the proposed relation list.'
events.append(dict(page='151_scan007',statement_id='151-007-pointed-consequences',date=stamp,
    who='root; GPT-6 Astra Pro; effort not exposed; run SP92',type='targeted proof check',outcome=proof))
p.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
q=W/'records/root_pending_notes.json';notes=json.loads(q.read_text())
notes['151_scan007']=r'''### Root checks prompted by the last leaf

Symbolic substitution, saved in `records/151_007_computation.json`, checks the cancelled top projection equality, rho-sigma equality, the repeated p0 p12 sigma1 equality, and delta1 sigma(x,y)=(x,y,y). The cancelled intermediate composition rho^2 sigma2 should return (x,z,y) in this coordinate model, whereas the written continuation reads (y,x,z); the cancelled source trial is retained literally. These are checks of that example only. The point of preserving the cancellation is independent of whether an individual trial is correct.

The right-hand live underlined equality visibly ends **sigma p11**. Its two final index strokes are short uprights, unlike the separate hook-and-foot2 in the same line's p12. With p11 interpreted as repeated-coordinate projection, sigma p11(x,y,z)=(x,x), while p12 sigma3(x,y,z)=(y,x). The literal equality fails for distinct x,y; p12 in place of p11 would give the valid relation repeated elsewhere on the page. The clear11 is retained at medium confidence, not silently replaced. Events `151-007-coordinate-07` and `08` record that distinction. The live sigma2 delta2=delta2 identity checks correctly in the coordinate example.

For the pointed specialization, let e1=delta0(*) and e2=delta1(e1). The prior relations make e1 fixed by sigma and e2 fixed by rho and sigma1. Under the stated permutation-generator interpretation, they are the group-fixed marked points. Also p12(e2)=sigma(e1)=e1, while delta1(e1)=e2 by definition. The three values in the lower-right box follow from delta2=rho^2 delta1 and rho^3=id applied to the three values in the large box. The precise conditional argument is recorded as `151-007-pointed-consequences`; no general sufficiency or completeness theorem for the relations has been proved here.
'''
q.write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('Eight symbolic checks and one conditional pointed-set argument registered.')
