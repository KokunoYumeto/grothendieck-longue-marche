from pathlib import Path
import json,datetime
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'review/scan026_findings.json').read_text())
t=(root/'review/scan026_draft.tex').read_text()
t=t.replace(r'\unsure{G|F}\unsure{\}|,}',r'\unsure{G|F|K}\unsure{\}|,}')
(root/'pages/J156-5-04_156-5_scan026.tex').write_text(t)
kindmap={'case':'other','certainty':'other','lexical':'misread word','lexical/punctuation':'misread word','punctuation':'other','state':'deletion state (struck given live or live given struck)','state/lexical':'deletion state (struck given live or live given struck)','state/omission':'omission','symbol':'misread symbol or index','symbol/certainty':'misread symbol or index','symbol/omission':'misread symbol or index','omission/drawing':'drawing or diagram'}
for c in x['changes']:
 c['kind']=kindmap.get(c['kind'],c['kind'])
 if c.get('crop'): c['crop']=c['crop'].removeprefix('deliverable/')
 c['main_decision']='Accepted after main-reader inspection of the referenced crop (whole-page image for the manuscript number); explicit uncertainty is retained where the strokes do not decide.'
 if c['id'] in ['026-04','026-13','026-15','026-19','026-25','026-31','026-35','026-37']: c['kind']='abbreviation expanded or spelling modernised'
 if c['id']=='026-14': c['kind']=r'readable ink left as \ill{}'
 if c['id']=='026-10':
  c.update(against_H=True,certainty_only=False,kind='misread symbol or index')
  c['main_decision']='The preferred diplomatic reading still includes a possible composition circle; it therefore differs from H, but the loop cannot be separated securely from the entry of p. The formula remains explicitly doubtful.'
 if c['id']=='026-46':
  c['final']=c['final'].replace(r'\unsure{G|F}',r'\unsure{G|F|K}')
  c['main_decision']='The folded right-edge cluster also admits a K-like outline. Add K among the explicit alternatives; retain the doubtful set-difference stroke and terminal brace/comma. No enclosure bar is supplied.'
for u in x['unresolved']:
 if u['place']=='bottom first-line final capital':
  u['alternatives']=['F','K'];u['reason']+=' A stem with two diverging arms also gives a K-like appearance.'
x['notes']=[
 'The page continues a discussion of subdivisions, gives the surjection diagram S→I→J, and states that a refinement F≪G factors through a subdivision G′, with F≤G′≼G. Its marginal warning distinguishes a bijective order map from an order isomorphism. Item b) and a separate unfinished “Ainsi, … F” are cancelled. The handwritten page number is 25; no title or date is written on this leaf.',
 'In a), the ink reads “G′ de F”, whereas the adjacent displayed G′≼G names G as the figure subdivided. The F has a straight stem and middle bar, so it remains F in the transcription. This is a local consistency observation, not a proof of the proposition (026-check-02).',
 'The final lower index clearly reads x∈|F|\\|G|. Under the intended support-extension construction, adjoining these singleton sets cannot enlarge the support beyond |F|; with |F|⊆|G| this index set is empty. To extend to |G| by singleton strata, the missing points would instead be |G|\\|F|. H and S SA21-K5-02 give this mathematical repair; the transcription keeps the visible reverse order. The precise claim checked is the elementary support calculation, not admissibility of the resulting figure (026-check-01).',
 'The cramped first-line formula ending and several overwritten or abbreviated groups remain doubtful. No word “tel” is visible after the cancelled “comme”, and no additional amalgamation sign is visible between F and the indexed coproduct. There is no explicit authorial “à vérifier” or question mark on this leaf.']
x['check_events']=[
 {'statement_id':'026-check-01','type':'targeted proof check','outcome':'For support |F|=union(F), adjoining singletons indexed by |F|\\|G| leaves the support |F| unchanged; if |F|⊆|G|, the index is empty. The intended support extension to |G| requires the missing-point set |G|\\|F|. This is a support calculation only; no claim about all figure axioms is certified.'},
 {'statement_id':'026-check-02','type':'used and rechecked in this run','outcome':'The page identifies ≼ as subdivision; its display F≤G′≼G therefore makes G′ a subdivision of G. The prose visibly says de F. Local notation and consistency checked; theorem not proved.'}
]
x['S_decisions']=[{'id':'SA21-K5-02','decision':'Overturned as a transcription instruction; confirmed only as the intended mathematical repair.','evidence':'The source CORRECTIONS row itself says “not decided on the scan”. In scan026_bottom_formula.png, the lower index has a straight-stem F before the set difference and the rounded G after it. Thus the ink is |F|\\|G|; |G|\\|F| belongs only in these notes.','crop':'crops/scan026_bottom_formula.png','box':[520,2178,1688,2364]}]
x['adjudicator']='GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc']='2026-11-20 18:33:39 UTC'
(root/'review/scan026_adjudicated.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
# Record images actually inspected by root, including the continuation after initial manifest entries.
p=root/'review/main_image_reviews.tsv'
with p.open('a') as f:
 for n in ['en_posant','deleted_b_tail','formula_edge','formula_g','grouping_rule','margin_deletion','margin_relation','part_a_overwrite','proof_evid','proof_invers']:
  f.write(f'026\tcrops/scan026_{n}.png\tmain reader\tinspected before first adjudication\n')
 for n in ['display_gloss','nb_display','donc_ramene_cancel','proof_signifie','proof_par_c5','top_cancel','deleted_proof_note','cancel_heading','question_axiomes','c5','foot','si_on_avait','number']:
  f.write(f'027\tcrops/scan027_{n}.png\tmain reader\tinspected before first adjudication\n')
print('Saved adjudicated scan026 and final page.')
