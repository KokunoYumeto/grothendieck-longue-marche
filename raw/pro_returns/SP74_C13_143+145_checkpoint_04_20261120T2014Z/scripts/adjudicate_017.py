from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'reviews/143_scan017_readerC.json';d=json.loads(p.read_text())
for i in [0,2,9]:d['changes'][i].update(confidence='low',consequential=False)
d['changes'][8].update(kind='insertion or placement',confidence='high',consequential=False)
for i in [0,1,2,3]:d['changes'][i].update(crop='crops/143_scan017_main_upper_groups.png',box=[290,375,1635,575])
for i,name,box in [(10,'category_C',[375,1220,1375,1320]),(14,'action_group',[1210,1520,1620,1655]),(17,'number16',[30,2288,110,2355])]:d['changes'][i].update(crop=f'crops/143_scan017_main_{name}.png',box=box)
d['remaining_doubts'][0]['confidence']='low'
d['inventory'][-1]['hand']='unnamed hand (pencil pagination)'
d['main_adjudication']={'summary':'Original page and all eight reader crops plus four main crops inspected. Candidate retained, with evidence mapping and confidence corrected. The tuple g and later low a are both preserved; M0690 and crossed word remain uncertain.','crops':[f'crops/143_scan017_main_{n}.png' for n in ['upper_groups','category_C','action_group','number16']]}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(r/'reviews/143_scan017_main.md').write_text('''# Main-reader adjudication: 143_scan017

The original page was viewed once for context. All eight existing reader-C crops were inspected: formula-numbers, quotient, extension, action-set, tuple, groupoid-insertion, deleted-word, action-map. Four additional single-locus crops inspected: upper_groups [290,375,1635,575], category_C [375,1220,1375,1320], action_group [1210,1520,1620,1655], number16 [30,2288,110,2355]. A previous oversized tool output was truncated; the eight reader images were therefore explicitly displayed successfully before adjudication. No second crop was made.

The references are (7) and (8). The two covered-set symbols have the crossed curled X, tilde, prime and J; both prime marks on the acting group are visible. The short separate ens is present before quotient, and four dark points close the paragraph. All four extension connectors are bare shafts. The set symbol has a 3-like outline with a lower loop; mathfrak Z is the provisional alphabet encoding. The inserted nonempty condition and the baseline comma remain; there is no point after ens. No terminal point follows the first category C.

The tuple's final letter descends in a hook and is g, while the subsequent action label is a low a-like stroke, retained with medium confidence. The group letters have the common round descending G form. The small addition before connexe is not readable enough to choose its supplied verbal or symbolic alternatives; M0690 remains undecided. The crossed word still admits sur/de. The later map arrow has a real triangular head, and the bottom alpha/beta arrows run in opposite directions as transcribed. Pencil footer 16 is present; its hand is unnamed.

No new mathematical proposition was proved. The announced equivalence and the request to explain (7), (8) are recorded as claims/requests of the source. The tuple/map discrepancy is not silently repaired. E/Sigma-only rows are low confidence and not treated as consequential corrections while unresolved.
''')
n=r/'notation.md';s=n.read_text()
if '\\mathfrak Z' not in s:s+='\n| `\\mathfrak Z` (provisional alphabet encoding) | The action set on 143_scan017–018: diagonal upper stroke, 3-like outline and looped lower return. Reconfirm each later glyph; this does not predetermine differently formed set symbols. |\n'
n.write_text(s)
