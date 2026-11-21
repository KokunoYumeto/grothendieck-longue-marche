from pathlib import Path
import json
R=Path('edition'); d=json.loads((R/'reports/147_scan128_report.json').read_text())
# The complete formula box must also include its left-hand written number.
for b in d['second_boxes']:
    if b['box']=='B17': b['coords'][0]=205
for i,e in enumerate(d['check_events'],2): e['statement_id']+=f'; N128-{i:02d}'
d['check_events'].append({'statement_id':'N128-01; N128-07; N128-08; N128-09; N128-10','type':'used and rechecked in this run','outcome':'Root visually checked all21 first crops, including the final Theta, shortened revêt, terminal hyphen, literal annotation hook and three doubled N forms. These are palaeographic and inventory checks, not proofs of analytic claims.'})
for r in d['rows']:
    if r['place']=='Delta subscript in final paragraph':
        r['math_consequential']=False
        r['scan_shows']+=' The continuous dash is retained as the author’s graphic index shorthand; no new mathematical operation is asserted by this rendering.'
(R/'review/147_scan128_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'notation.md').open('a') as f:f.write('\n- Scan128: I_r occurs twice with a straight stem and transverse bars, distinct from angular Delta; both stay as written. All three N forms are doubled on the left. The first range has a retraced2-like index, retained as d_2/d_1. Formula205 has a true bang and the broad group S below the wedge; the angular flag symbol is P. The terminal annotation curve is literal geometry, and the boundary ending is simple-.\n')
with (R/'review/root_visual_readings.md').open('a') as f:f.write('\n### Scan128 final return review\nAccepted all21 crop findings and four resolved original marks. The fixed second box for205 was widened leftward to x205 before commitment so it also covers the handwritten formula number; no extra first crop was made. The single dash in the Delta subscript is graphic shorthand rather than a demonstrated mathematical correction. All10 notes are linked to honest check events.\n')
