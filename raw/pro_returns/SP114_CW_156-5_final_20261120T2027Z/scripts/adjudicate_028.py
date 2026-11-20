from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'review/scan028_findings.json').read_text())
t=(root/'review/scan028_draft.tex').read_text()
t=t.replace(r'\deleted{\unsure{Cons|Con}} \deleted{Soit \deleted{$\unsure{K|H}$}}',r'\deleted{\deleted{\unsure{Cons|Con}} Soit \deleted{$\unsure{K|H}$}}')
(root/'pages/J156-5-04_156-5_scan028.tex').write_text(t)
km={'state/scope':'deletion state (struck given live or live given struck)','certainty':'other','lexical':'misread word','lexical/abbreviation':'abbreviation expanded or spelling modernised','symbol/glyph':'misread symbol or index','lexical/state':'misread word','symbol':'misread symbol or index','omission/certainty':'omission','lexical/punctuation/state':'insertion or placement','deletion/insertion/omission':'insertion or placement','alphabet':'misread symbol or index','omission/deletion':'omission','diagram/sign':'drawing or diagram','omission/state':'omission','alphabet/certainty':'misread symbol or index','diagram/arrow':'drawing or diagram','omission/certainty/diagram':'drawing or diagram','symbol/certainty':'misread symbol or index','omission/overwrite':'omission','symbol/overwrite':'misread symbol or index'}
for c in x['changes']:
 c['kind']=km.get(c['kind'],c['kind'])
 if c.get('crop'):c['crop']=c['crop'].removeprefix('deliverable/')
 c['main_decision']='Accepted after main-reader inspection of the cited crop. Remaining uncertainty records obscured ink or indeterminate overwriting chronology; expected formulae do not replace the source.'
 i=int(c['id'].split('-')[1])
 if i in [12,21,23,26,29,34,37]:c['certainty_only']=False
 if i==2:
  c['main_decision']='Keep the opening sentence live and the local Proposition strike. The short Cons fragment also has its own horizontal strike inside the broader cancelled attempt; the final text preserves both layers there.'
  c['consequential']=True
 if i in [9,11,14,15,20,25,26,29,31,34,36,37]:c['consequential']=True
for z in x['inventory']:
 z['kind']={'page_number':'text','text_block':'text','heading':'text','margin':'margin note'}.get(z['kind'],z['kind'])
x['notes']=[
 'The handwritten sheet number is 27. An opening sentence naming two set-theoretic figures remains live after the locally cancelled heading “Proposition”. Four long oblique strokes cancel the subsequent attempted construction, including its displays and smaller local revisions. Two diagrams and the lower construction remain live. No title, date, explicit question mark, or verbal authorial doubt is written on this sheet.',
 'The abandoned passage forms nonempty intersections of open pieces and calls their equivalence relation a “borne sup”. Conditionally, intersections of two partitions are the classes of the intersection of their equivalence relations. Under inclusion of relations this is a meet; under the reverse order it is a join. The page does not establish the ordering convention, so no correction of “borne sup” is justified (028-check-02).',
 'In the lower diagram φ has target I and φ′ has target I′. Their paired restriction therefore has target I×I′, while the image formula visibly writes I×J. This local codomain mismatch is retained (028-check-01). The nearby pair is (i,j′), followed by j=(i,i′); the first definition writes A_i′ although the boxed formula uses A_i, and the second definition has a j subscript and j cutoff. H regularizes several of these tokens. The ink determines the preserved primes and descending j strokes; the A/B overwriting remains doubtful.',
 'The first diagram uses two isolated oblique inclusion signs; the second uses hooked arrows and a headless ψ-labelled vertical segment. The lower-left J was overwritten by K and is not a drawn box. Both occurrences of the empty sign have the phi-shaped oval and long stem. The small interlinear abbreviation ends in v; the final point after that inserted occurrence is not separately visible.']
x['check_events']=[
 {'statement_id':'028-check-01','type':'targeted proof check','outcome':'Read φ:S→I and φ′:T→I′ from the diagram. The ordered pair of their restrictions to S∩T necessarily takes values in I×I′. The displayed I×J is a local codomain mismatch; no assertion about the existence or properties of the resulting figure is proved.'},
 {'statement_id':'028-check-02','type':'targeted proof check','outcome':'Conditional partition calculation: on a common support, x and y lie in the same intersection of two equivalence classes iff x R_F y and x R_G y. Hence those intersections are classes of R_F∩R_G, a meet for relation inclusion and a join for reverse inclusion. The manuscript order convention is not established by this page; borne sup is retained without declaring the claim false.'}
]
x['adjudicator']='GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc']='2026-11-20 18:42:56 UTC'
(root/'review/scan028_adjudicated.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
manifest=json.loads((root/'review/scan028_crop_manifest.json').read_text())
with (root/'review/main_image_reviews.tsv').open('a') as f:
 for name,c in manifest.items():f.write(f'028\tcrops/scan028_{name}.png\tmain reader\tinspected before first adjudication\n')
rows=sum(c.get('certainty_only',False) or c.get('against_C') or c.get('against_H') for c in x['changes'])
with (root/'progress.log').open('a') as f:f.write(f"scan 028 done 2026-11-20 18:42:56 UTC: {x['line_count']} lines read, 26 places cropped, {rows} rows\n")
print('Saved scan028, rows',rows)
