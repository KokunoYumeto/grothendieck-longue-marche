from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'reviews/143_scan019_readerC.json'; d=json.loads(p.read_text())
tp=r/'reviews/143_scan019_readerC.tex'; t=tp.read_text()
old=r'\unsure{$(\simeq\widehat{\mathbf Z}^{*}\;\text{canon.}?)$}'
new=r'\unsure{$(\simeq\widehat{\mathbf Z}^{*}\unsure{)|?}\;\text{canon.}?)$}'
assert old in t
t=t.replace(old,new)
for i in [1,15]:d['changes'][i].update(confidence='low',consequential=False)
for i in [3,5,20,27]:d['changes'][i].update(confidence='low',consequential=False)
mapping={0:('heading',[270,65,1250,185]),3:('pair_group',[315,370,1000,480]),5:('projection',[340,570,1550,735]),7:('object_action',[315,865,1570,1175]),8:('object_action',[315,865,1570,1175]),9:('circle8',[280,1350,440,1470]),13:('recap_set',[1010,1485,1640,1620]),14:('recap_set',[1010,1485,1640,1620]),20:('ens_description',[350,2070,845,2180]),21:('ens_description',[350,2070,845,2180]),27:('last_line',[360,2230,1590,2340]),28:('number18',[20,2290,95,2355])}
for i,(name,box) in mapping.items():d['changes'][i].update(crop=f'crops/143_scan019_main_{name}.png',box=box)
c=d['changes'][24]
c.update(final=new,against_C=True,against_H=True,confidence='low',consequential=False,kind='misread symbol or index')
c['ink']='The hat, raised star and canon. are readable. A distinct tall curved stroke immediately after Z-star is present and must not disappear: a closing parenthesis is first, with a question-like sign as alternative. Both the intermediate sign and the overall grouping remain unsure; the source is not regularized to a canonical-isomorphism claim.'
d['decisions'][0].update(reading=new,confidence='low',ink=c['ink'])
for x in d['remaining_doubts']:
 if x['place'] in ['Beta input tuple, final component','Lower groupoid tuple, final component']:x['confidence']='low'
 if x['place'].startswith('Rounded extension'):
  x['confidence']='low';x['reason']='The main pair-definition crop and upper-extension crop show two open bowls resembling a cursive E. The shared notation remains provisional pending comparison with the other pages; the uncertainty concerns alphabet encoding, not a different mathematical object.'
 if x['place'].startswith('M0698:'):
  x.update(reading=new,confidence='low',reason=c['ink'])
d['notes'][2]['text']='The source asks whether T is isomorphic to the hatted integer group, with an explicit question mark. It adds chi : G to Aut(T), and a crowded comparison involving hatted Z-star and canon.?. The tall curved stroke after Z-star is now explicitly represented as an unsure closing-parenthesis/question-like sign; the whole parenthesis remains unsure. No canonical identification is asserted by this review.'
d['notes'][4]['text']='The two final tuple components are low waves, explicitly sim/compressed-a. The round set label remains tau/calligraphic T. The pair-definition and upper-extension capitals favour cursive E through two open bowls, but the shared E/Sigma convention remains provisional pending cross-page comparison. All unresolved alphabet-only choices are non-consequential.'
for ev,n in zip(d['check_events'],[1,2,3]):ev['statement_id']=f'143_scan019-N{n}'
d['main_adjudication']={'summary':'Original and all ten reader-C crops inspected, followed by nine main crops for every remaining page-only change. Accepted with explicit preservation of the extra curved sign after Z-star. The chi-map endpoint was checked against the same crop: a small raised angular head is present, so the shared arrow reading is retained. No bare-connector change is made there.','new_main_crops':[f'crops/143_scan019_main_{name}.png' for name in ['heading','pair_group','projection','object_action','circle8','recap_set','ens_description','last_line','number18']]}
tp.write_text(t);p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(r/'reviews/143_scan019_main.md').write_text('''# Main adjudication — 143_scan019

The original and all ten reader-C crops were visually inspected. Nine further crops (heading, pair_group, projection, object_action, circle8, recap_set, ens_description, last_line, number18) cover the remaining changes previously referenced only to the page; their boxes are recorded in the accepted JSON and main crop manifest.

Accepted: no stop after the heading; avec after the ordered pair; upper links bare/head/bare/head, lower links bare/bare/head/bare; ornate Z; circled 8; cancelled du/de; section sign; ens without a stop; the small chi inside the tuple and a separate chi-colon interlinear above où; no supposed cancelled word after T; no extra illegible word after groupe; no comma before et; footer 18 in an unnamed pencil hand. The object-set and action-group alphabets are checked at every local occurrence.

The dense inserted comparison contains a tall curved stroke immediately after Z-star. The candidate omitted its explicit representation; it is now preserved as an unsure closing-parenthesis/question-like mark inside the already unsure grouping. M0698 remains undecided. The word canon. itself is readable.

The chi-map shaft has a small raised angular thickening at its right end. Comparison with the existing map crop supports retaining the shared arrow; the larger Phi-map arrow is unambiguous. No new bare-link reading is counted. The two wave-shaped action components, the tau/calligraphic-T alphabet, and the cancelled preposition remain explicit doubts. E/Sigma remains provisional for global comparison despite strong local E-shaped open bowls.

No new mathematical proof or computation was performed on this page. Source constructions and questions are distinguished from verified assertions in CHECK_EVENTS.
''')
