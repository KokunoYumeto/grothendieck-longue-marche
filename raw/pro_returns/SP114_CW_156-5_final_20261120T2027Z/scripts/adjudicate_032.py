from pathlib import Path
import argparse, json

p=argparse.ArgumentParser();p.add_argument('--utc',required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'review/scan032_findings.json').read_text())
x['scan']=32
manifest=json.loads((root/'review/scan032_crop_manifest.json').read_text())
# Derived upright views retain the original source ROI and the recorded post-rotation crop.
for z in manifest:
    z['crop']=z.get('crop',z.get('path',''))
    if any(s in z.get('crop','') for s in ('note_main','note_tail','note_end')):
        z['derived_view_estimated_bounding_box']=z.get('box')
        z['box']=[18,1270,991,2120]
        z['coordinate_note']='Original source ROI before rotation; post-rotation cropping is recorded separately. White rotation padding is not a source pixel.'
(root/'review/scan032_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
text=(root/'review/scan032_draft.tex').read_text()
(root/'pages/J156-5-04_156-5_scan032.tex').write_text(text)
for c in x['changes']:
    c['crop']=c.get('crop','').removeprefix('deliverable/')
    c['main_decision']='Accepted after main-reader inspection of the saved crop; unclear letters and stroke function remain expressly doubtful.'
    if any(s in c['crop'] for s in ('note_main','note_tail','note_end')):
        c['derived_view_estimated_bounding_box']=c['box'];c['box']=[18,1270,991,2120]
        c['evidence']+=' The stated source box is the original ROI before rotation; the manifest records the subsequent upright subcrop.'
    i=int(c['id'].split('-')[1])
    if i in (12,24,29,33,34,37,40,52,56,58):
        c['certainty_only']=False
    if i==4:
        c['against_H']=True;c['certainty_only']=False
        c['main_decision']='Keep à as the preferred but unresolved reading, with colon explicitly admitted. This is not a resolved punctuation decision.'
    if i in (14,46,50,61):
        c['against_C']=False;c['against_H']=False;c['certainty_only']=False;c['review_only']=True
        c['main_decision']+=' The same physical locus is counted with '+{14:'032-13',46:'032-45',50:'032-49',61:'032-36'}[i]+', not counted twice.'
    if i==13:
        c['evidence']+=' The raised insertion belongs to chacune; des stays on the baseline. Both the omitted word and its attachment are covered in this one locus.'
    if i==15:
        c['against_H']=False;c['macro_only']=True
        c['main_decision']='The same heading is represented in H with bold markup. This typographic macro difference alone is excluded from the collation.'
    if i==17:
        c['against_H']=False;c['review_only']=True
        c['main_decision']='H explicitly describes the large cancellation in its editorial note. The same state is therefore recognized by both witnesses despite different encoding; no substantive H departure is counted.'
    if i==32:
        c['main_decision']='The long caractéris- stem is supported; the ending remains crossed and doubtful. H’s conditions is not supported at this position.'
    if i==34:
        c['final']=r'Mais \unsure{ces trois|c) très}'
    if i==45:
        c['evidence']+=' The final sont remains doubtful because two cancellation strokes obscure its middle; this is included in the same old-line locus.'
    if i==49:
        c['main_decision']='The large initial loop belongs to the single live On. The horizontal stroke above it underlines Dém; no independently cancelled second On exists.'
    if c['kind'].startswith('readable ink left'):
        c['kind']='readable ink left as `\\ill{}`'
for z in x['inventory']:
    z['kind']={'number':'text','text block':'text','display and deletion':'deletion','marginal note':'margin note','text block and deletion':'deletion','insertion and later deletion':'insertion','unresolved linking or cancellation stroke':'drawing','deletion by overwriting':'deletion'}.get(z['kind'],z['kind'])
    z['hand']='his hand'
for group in ('unresolved','C_state_audit','C_doubt_audit'):
    for c in x.get(group,[]):
        c['crop']=c.get('crop','').removeprefix('deliverable/')
        if 'box' in c and any(s in c['crop'] for s in ('note_main','note_tail','note_end')):
            c['derived_view_estimated_bounding_box']=c['box'];c['box']=[18,1270,991,2120]
x['notes']=[
    'The handwritten page number is 31. The opening continues the stratum argument for the proposed subdivision. A corollary then states four purportedly equivalent characterizations; condition a) is crossed out and the margin says “Ultra faux”. The proof announces d)⇒b)⇒c)⇒a)⇒d), then begins d)⇒b). The page ends at the equality F\\setminus G=F′\\setminus G′. There is no title or date.',
    'Two clearly written primes remain in “Si A∉G′” and “A∈F\\setminus G′⊂F′”. The next case instead says “Si A∈G”. The construction on scan030 directly includes F\\setminus G in F′, whereas it does not directly assert inclusion of F\\setminus G′. Replacing the two G′ by G would give complementary cases and the inclusion supplied by the construction, but the ink is not changed. This is a local consistency comparison, not a proof of the corollary.',
    'The cancelled union has B≤F in its lower limit. The letter has two crossbars and is not changed to a conjectural A. The corollary begins Le although raffinement is cancelled and replaced by subdivision; the grammatical disagreement is retained. Chacune is a raised insertion before baseline des.',
    'The slanted note reads b), c), d) as equivalent and “impliquées par a)”; later words favor “loin d’impliquer a)”, with intervening words still doubtful. This registers the author’s own objection to the announced cycle, but no implication in the cycle is independently proved here. The note’s broad curved stroke has a terminal turn and is reproduced without an inferred arrowhead. Whether it cancels or links/groups the note is unresolved; the note remains live with that state doubt recorded.',
    'At the proof heading the crop shows one live On; C’s additional cancelled On is absent. At the foot, inclusion is written over a doubtful older identité, with cancelled (trivial) replaced above by can. and the hooked map F\\setminus G↪F. The restriction is therefore called the canonical inclusion in the live layer, not the identity as in H. The remaining set equality is asserted as a task to prove, not as an established result on this page.',
    'The NB says “c’est tjrs surj. donc c’est l’injectivité qu’il faut prouver ici”. The statement about surjectivity is transcribed but was not independently checked. Literal equals signs in the starred margin stand for même; can., tjrs and ens retain their written short forms. The densely intersecting oblique note and overwritten words are the least secure areas.'
]
x['check_events']=[{'statement_id':'032-consistency-01','type':'used and rechecked in this run','outcome':'Compared the written construction F′=G′∪(F\\setminus G) on scan030 with the two primed G′ in scan032 and its following unprimed-G case. The construction directly supplies inclusion of F\\setminus G, not the displayed F\\setminus G′. This is a local formula/case consistency check only; it does not establish a counterexample within the unspecified figure axioms or prove the corollary.'}]
x['adjudicator']='GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc']=a.utc
(root/'review/scan032_adjudicated.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
with (root/'review/main_image_reviews.tsv').open('a') as f:
    f.write('032\twhole source scan\tmain reader\tinspected once for layout before first adjudication\n')
    for z in manifest:f.write('032\t'+z['crop'].removeprefix('deliverable/')+'\tmain reader\tinspected before first adjudication\n')
rows=sum(bool(c.get('certainty_only') or c.get('against_C') or c.get('against_H')) for c in x['changes'])
with (root/'progress.log').open('a') as f:f.write(f"scan 032 done {a.utc}: {x['line_count']} lines read, {len(manifest)} places cropped, {rows} rows\n")
print('Saved032',rows,'rows')
