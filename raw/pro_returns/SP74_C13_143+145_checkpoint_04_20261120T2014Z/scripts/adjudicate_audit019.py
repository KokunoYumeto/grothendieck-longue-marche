"""Main's four audit019 decisions, all checked on the existing image crops."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1];key='143_scan019'
a=json.loads((R/'reviews'/f'{key}_auditB.json').read_text());r=json.loads((R/'reviews'/f'{key}_accepted.json').read_text())
p=dict(key=key,reader='B',findings=[],change_operations=[],remaining_doubts_remove=['Beta input tuple, final component','Lower groupoid tuple, final component'],notes_remove=[key+'-N5'],notes_add=[],hand_log_add=a['hand_log'][:4],check_events_add=[],inventory_remove=[],inventory_add=[])
reasons=[
 'Main independently inspected both local graphs and the explicit action a on 017. Their rising shoulder and compressed return are the same handwritten a; no separately diagnostic relation sign is established.',
 'Main confirms the same reduced a, distinct from the long descending g forms. This revises the provisional sim-first preference, not only its certainty.',
 'Main saw two dark points and two separate lighter elongated strokes, aligned in a gently rising sequence. Their shared alignment and stroke shapes support the literal four-mark continuation at medium confidence.',
 'Main confirms the long converging/retraced segments and the final open two-tine return. Draw these shapes without assigning a direction to the fork; first two links remain bare and the isolated tap is not a label.'
]
for i,(f,reason) in enumerate(zip(a['findings'],reasons),1):
 p['findings'].append(dict(index=i,decision='accept',reason=reason))
 if i in (1,2,4):
  old=next(x for x in r['changes'] if x['place']==f['existing_difference_row']);new=dict(old)
  new.update(final=f['after'],ink=f['reason']+' '+reason,confidence=f['confidence'],against_C=f['against_C'],against_H=f['against_H'])
  # The row still includes the consequential bare-versus-headed differences in the first two links.
  if i==4:new['consequential']=old['consequential']
  p['change_operations'].append(dict(operation='replace',place=old['place'],row=new))
 else:
  row={k:f[k] for k in ('place','C','H','against_C','against_H','kind','confidence','crop','box','marked_in_H','consequential')};row.update(final=f['after'],ink=f['reason'])
  p['change_operations'].append(dict(operation='append',row=row))
old=next(x for x in r['changes'] if x['place']=='Action on the object set: group and set alphabets');new=dict(old)
new.update(C=r'$\mathcal E$ sur $Z$',H=r'$\Sigma$ sur $\mathfrak{Z}$',final=r'$\unsure{\mathcal E|\Sigma}$ sur $\mathfrak Z$',ink='The action-group glyph is the same rounded two-lobed form; the following set letter has the same long curled tail. The four physical continuation marks are logged separately, rather than included in this alphabet comparison.')
p['change_operations'].append(dict(operation='replace',place=old['place'],row=new))
n=dict(next(x for x in r['notes'] if x['id']==key+'-N5'))
n['text']='The two final tuple components are compressed a graphs with a low shoulder and flattened return. Main compared both with the explicitly named action map on017 and with018; the preferred reading is now a. The round set label remains tau/calligraphic T, and the rounded group glyph retains its shared E/Sigma alternative. These alphabet identifications do not assert different mathematical objects.'
p['notes_add']=[n]+a['notes']
for e in a['check_events']:
 e=dict(e);e.update(date='2026-11-20',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; second reader B');p['check_events_add'].append(e)
for eid,desc in [('E02','beta(Pi, tilde Pi, p, G, a) = (rounded group glyph, G, pi, ornate Z), ainsi :'),('E07','Ornate Z = Ob tilde Pi, avec opération évidente de rounded group glyph sur ornate Z, then the four-mark E22 continuation'),('E11','1 — pi — rounded group glyph; long converging/retraced strokes to G; shaft and open two-tine return before 1'),('E13','Double-headed correspondence and (Pi, tilde Pi, p, G, a)')]:
 old=next(x for x in r['inventory'] if x['element']==eid);new=dict(old);new['first_words_or_objects']=desc;p['inventory_remove'].append(eid);p['inventory_add'].append(new)
v=dict(a['inventory_additions'][0]);v.update(hand='his hand',transcribed='yes');p['inventory_add'].append(v)
p['main_summary']='All four findings accepted after main image comparison. Both action data resolve from sim-first to a; existing witness flags reverse appropriately. Literal four-mark continuation and nonstandard connector shapes are drawn. M0698 unchanged; five remaining doubts. No new caret or insertion guide is inferred.'
(R/'reviews'/f'{key}_main_audit_plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
