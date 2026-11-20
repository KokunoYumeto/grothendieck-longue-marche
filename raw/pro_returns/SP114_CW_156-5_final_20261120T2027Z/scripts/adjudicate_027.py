from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'review/scan027_findings.json').read_text())
t=(root/'review/scan027_draft.tex').read_text()
(root/'pages/J156-5-04_156-5_scan027.tex').write_text(t)
km={'certainty':'other','word':'misread word','abbreviation':'abbreviation expanded or spelling modernised','punctuation':'other','state':'insertion or placement','symbol':'misread symbol or index'}
for c in x['changes']:
 c['kind']=km.get(c['kind'],c['kind'])
 if c.get('crop'):c['crop']=c['crop'].removeprefix('deliverable/')
 c['main_decision']='Accepted after main-reader inspection of the cited image evidence; remaining crossed or clipped letterforms stay explicitly doubtful.'
 i=int(c['id'].split('-')[1])
 # Count preferred lexical/sign readings, excluding uncertainty-wrapper changes.
 if i in [2,24,32,34,39,40]:c.update(against_C=False,against_H=False,certainty_only=True)
 if i in [8,14,29]:c.update(against_C=False,against_H=True,certainty_only=False,kind='misread word')
 if i in [9,38]:c['against_C']=False
 if i==44:c['against_H']=False
 if i in [7,26,27,28,42,43]:c['kind']=r'readable ink left as \ill{}'
 if i==10:c['kind']='deletion state (struck given live or live given struck)'
 if i in [18,19,25,36]:
  c['main_decision']='Confirmed as the author’s phi-shaped empty sign: an oval on a stem extending beyond it. Encode ϕ consistently as \\phi rather than normalizing it to a slashed-circle empty-set glyph.'
  c['consequential']=True
 if i==21:c['consequential']=True
 if i==23:c['consequential']=True
 if i==44:
  c['main_decision']='The possible to/polo- sequence, later descending loop and dotted short stroke favour topologique; the compressed ending remains unresolved. H’s preferred word matches the first candidate, so added uncertainty alone is not counted against H.'
 if i==45:c['consequential']=True
for z in x['inventory']:
 z['kind']={'page_number':'text','text_block':'text','heading':'text','margin':'margin note'}.get(z['kind'],z['kind'])
x['notes']=[
 'The sheet, numbered 26, asks whether the subfigure order ≤ can be expressed using refinement ≪ and subdivision ≼, and places “??” in the margin. It asserts F≤G and F≼G ⇒ F=G, then proposes a reduction using a nonempty figure H disjoint from F. These statements are reported, not certified from definitions absent here. No title or date is written on the sheet.',
 'The local reduction is propositionally consistent: assuming the asserted existence of nonempty H for strict F≤G, C5 transfers disjointness from F to G under F≼G; the displayed lemma would then give H=ϕ, a contradiction. Only this conditional structure was checked, not the existence assertion, C5, or the displayed lemma (027-check-01). The gloss reads “comp. à G”, and the inserted proof reference reads “par C5” after G′. Those crops determine the readings; expected mathematics does not supply them.',
 'C5 is justified on the page by equality of supports and the empty-intersection criterion. C6 says “on la verra tantôt”; C7 says “on le vérifiera” followed by a doubtful topologique/topologiquement-like ending. These are promises of verification. The final label retains a doubtful 8/ϕ-shaped main glyph and a distinct low 0.',
 'Retain the unexpected “de, F” and the literal = shorthand in the opening question. The small gloss opens a parenthesis without a visible close. The conclusion’s subscript in ϕ_F is present although the later proof writes plain ϕ. The upper figure/fig. addition, cancelled proof note and several struck letters remain unresolved.']
x['check_events']=[{'statement_id':'027-check-01','type':'targeted proof check','outcome':'Checked only the propositional reduction: strict F≤G supplies nonempty H with H≪G and H disjoint from F; if F≼G and C5 transfers disjointness, the displayed H≪G plus disjointness-from-G lemma implies H=ϕ, contradicting nonemptiness. The existence claim, C5, and lemma were assumptions for this check, not independently established.'}]
x['adjudicator']='GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc']='2026-11-20 18:38:54 UTC'
(root/'review/scan027_adjudicated.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
with (root/'review/main_image_reviews.tsv').open('a') as f:
 for n in ['c7_terminal','last_label','c6_initial','c5_avec','deleted_proof_note_rot','proof_par_c5_rot']:
  f.write(f'027\tcrops/scan027_{n}.png\tmain reader\tinspected before first adjudication\n')
with (root/'progress.log').open('a') as f:f.write('scan 027 done 2026-11-20 18:38:54 UTC: 34 lines read, 24 places cropped, 45 rows\n')
print('Saved scan027.')
