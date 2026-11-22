"""Register only the tuple computations actually executed in this run."""
from pathlib import Path
import json
W = Path(__file__).resolve().parents[1]
report = json.loads((W/'records/151_coordinate_computation.json').read_text())
p = W/'records/root_mathematical_checks.json'
events = json.loads(p.read_text())
events = [e for e in events if not e['statement_id'].startswith('151-coordinate-')]
for i, row in enumerate(report['rows'], 1):
    sid = f'151-coordinate-{i:02d}'
    page = '151_scan005' if row['claim'].startswith('005') else '151_scan003'
    typ = 'computation or formal certificate'
    if i == 18:
        typ = 'refuted, with refined statement 151-coordinate-19 and 151-coordinate-20'
    elif i == 23:
        typ = 'refuted, with refined statement 151-coordinate-24'
    elif i == 27:
        typ = 'computation or formal certificate'
    detail = '; '.join(f'{e} -> {tuple(v)}' for e,v in zip(row['expressions'], row['values']))
    events.append({'page': page, 'statement_id': sid, 'date': report['time_utc'],
                   'who': 'root; GPT-6 Astra Pro; effort not exposed; run SP92',
                   'type': typ, 'outcome': row['claim'] + ': ' + detail + '. '
                   + ('All displayed values agree.' if row['equal'] else 'The displayed values differ for distinct coordinate symbols.')
                   + ' Scope: the stated coordinate model only; see scripts/check_151_coordinates.py and records/151_coordinate_computation.json. No abstract presentation theorem is inferred.'})
p.write_text(json.dumps(events, ensure_ascii=False, indent=2)+'\n')
q = W/'records/root_pending_notes.json'
notes = json.loads(q.read_text())
notes['151_scan003'] = r'''### Root check of the coordinate model

The computations in `scripts/check_151_coordinates.py` were actually executed, and their symbolic tuple outputs are retained in `records/151_coordinate_computation.json`. Composition is read right to left. For this check, p0 and p1 are the first and second projections, delta0 duplicates a coordinate, sigma swaps two coordinates, rho sends (x,y,z) to (y,z,x), and sigma_i swaps the two coordinates other than i. The three deltas and three cyclic pair projections are the explicit formulas read in this scan. This checks their coordinate realization; it does not prove the proposed abstract sufficiency of the relation list.

The cyclic p identities, three sigma-projection identities, cyclic delta identities, p0 delta0=id, sigma delta0=delta0, the delta0 p0 chain, and all three values in the large box agree under substitution. The bottom diagonal identity also holds, since delta1 delta0 sends x to (x,x,x). These checked statements have separate event IDs `151-coordinate-01` through `17` and `21`.

The upper right box visibly writes **sigma3 delta1=delta1**. Its sigma subscript has two open right lobes, and both delta subscripts are single uprights. Substitution gives sigma3 delta1(x,y)=(x,y,x)=delta2(x,y), whereas delta1(x,y)=(y,x,x). The equality therefore fails for x different from y in the coordinate model. The corrected stabilizer identity there would be sigma1 delta1=delta1. Events `151-coordinate-18` to `20` record the failure and both precise refinements. The clear written 3 is preserved. The next mathematical leaf,151_scan005, separately writes a clear 1 in its corresponding stabilizer box.

At the last formula, the inner underbrace p12 rho^2=p31 is valid. The outer overbrace visibly labels p12 rho^2 sigma2 as p12, but that product sends (x,y,z) to (x,z), while p12 sends it to (x,y). Thus that brace label fails in this model; the product instead equals sigma p31, the first-and-third projection. Composing with p0 makes the full displayed equality true, since both sides then return x. Events `151-coordinate-22` to `25` distinguish those assertions. The ink's p12 annotation is retained, as is the locally uncertain lower left p index2|1; no expected label is supplied.

The cancelled inequality retains its two question marks above the not-equal sign. Its right index remains22|12|23 on stroke evidence, and no mathematical conclusion is asserted for that unresolved cancelled expression. Likewise, no proof is claimed for the cancelled trial chains or the abstract axiomatization. The recurring group glyph is read as calligraphic G from its open outer bowl, curled top and inward horizontal return; identifying the intended group as a permutation group does not turn this written glyph into S.
'''
notes['151_scan005'] = r'''### Root check and resolution of the final sigma index

The whole last formula and its enlarged detail show a short upright with a small lower/right swelling, without the two separately visible lobes used for clear 3 elsewhere on this leaf. This favors sigma1. The coordinate check `151-coordinate-26` gives p0 p12 sigma1(x,y,z)=x=p0 p12(x,y,z), whereas the competing3 gives y (`151-coordinate-27`). The ink is compatible with1 and its own notation supports that reading, so M0750 is resolved to1 at medium confidence. This is not a silent correction of a clearly written3. The underlabel remains q1|p1 because both opposing bowls are visible in the overtraced letter and their sequence cannot be separated confidently.

The sigma involution and delta0 p0 idempotent captions were checked by substitution (`151-coordinate-28` and `29`). The central three-value box, the E0 identities, and the sigma1 stabilizer identity repeat the coordinate relations already computed for151_scan003; no independent general presentation theorem is claimed. The clear sigma1 delta1=delta1 on this leaf is consistent with that model, unlike the explicit sigma3 in the corresponding box on151_scan003. All of these leaf-specific indices are transcribed as read.
'''
q.write_text(json.dumps(notes, ensure_ascii=False, indent=2)+'\n')
print(f'Registered {len(report["rows"])} actual computation events and two root note additions.')
