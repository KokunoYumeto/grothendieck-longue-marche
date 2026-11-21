from pathlib import Path
import json
R=Path('edition');d=json.loads((R/'reports/147_scan127_report.json').read_text())
for i in (4,7):d['rows'][i]['against_C']=True
d['rows'][4]['scan_shows']=d['rows'][4]['scan_shows'].replace('H’s form omits the visible o; C’s i remains admitted, so a new certainty-only error is not assigned to C.','H’s form omits the visible o. C’s i remains admitted as an alternative, but the leading y changes the primary reading and is counted against C.')
d['rows'][7]['scan_shows']+=' The primary reading changes from C’s je to p, and the period of C’s p. alternative is absent; this is counted against C.'
for i,e in enumerate(d['check_events'],1):e['statement_id']+=f'; N127-{i:02d}'
assert len(d['second_boxes'])==27 and d['second_boxes'][-1]['reading']==r'\deleted{canoniques de groupoïdes}'
(R/'review/147_scan127_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'notation.md').open('a') as f:f.write('\n- Scan127: the middle letter of déployement/déploiement remains y/i uncertain after retracing. The short p-like form before me has no period; je remains an alternative. Delta in the canceled image-inverse note is angular, while the live inserted Theta is round. The boxed groupoid map uses capital Pi; its target low1 is crossed and uncertain. Four short dashes are separate strokes, and hom de générisation is only partly double-underlined.\n')
