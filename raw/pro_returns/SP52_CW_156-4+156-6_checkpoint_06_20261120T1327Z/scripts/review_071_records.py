from pathlib import Path
import json,datetime,hashlib
O=Path(__file__).resolve().parents[1];p=O/'decisions/156-4_071.json';d=json.loads(p.read_text())
assert d['final_text_sha256']==hashlib.sha256((O/'pages'/d['filename']).read_bytes()).hexdigest()
d['c_doubts'][22]['crop']='readers/156-4_071/R1/crops/01_top_folio.jpg; readers/156-4_071/R1/crops/02_donnons.jpg'
d['c_doubts'][22]['scan_shows']='Each opening repetition mark consists of two unequal parallel bars: the first is fully visible in R1/01, the second in R1/02. Both occurrences are retained literally.'
for x in d['inventory']:
 if x['element'] in ['left marginal fragments','right marginal fragments']:x['hand']='uncertain hand'
old=d['inventory'];lower={x['element']:x for x in old[18:]}
seq=['continuous draft boundary','thirteen long cancellation strokes','broad cancellation of draft text','draft final paragraph','detached low points','detached high point','first internal cancelled group','second internal cancelled group','draft assertion paragraph','draft opening paragraph','possible older layer beneath Phi','inverted folio','overwritten second folio digit']
assert set(seq)==set(lower)
d['inventory']=old[:18]+[lower[k] for k in seq]
for x in d['inventory'][18:]:x['position']='In original scan orientation: '+x['position']
d['inventory'][21]['position']='Upper edge of inverted draft in original scan orientation; final line in its own reading order, G5'
for i in range(51,56):d['differences'][i]['confidence']='medium'
d['differences'][52]['scan_shows']='Donc starts a new physical line beneath the corollary. The final preserves its separate block; this row concerns only H joining that start to the preceding paragraph.'
d['differences'][53]['scan_shows']='En d’autres termes begins the next physical block below the Donc line. The final retains that start in G4; this row concerns paragraph joining only.'
d['differences'][54]['scan_shows']='In the inverted block, Alors starts its own line with a capital initial. G5 keeps that block start at its observed position; this row concerns paragraph joining only.'
d['differences'][55]['scan_shows']='Dém starts the last inverted line with a greater left indent than the preceding lines. G5 retains that separate start; this row does not recount its lettering or stop.'
d['notes']={
 'summary':'The upright text says that F and F prime have the same cosupport, equivalently the same support, and reformulates the disjointness implication. Its corollary says that an object’s cosupport in the family is closed for both the straight order and the bowed order, hence is a sous-contrée; the assertion is then extended to a part Phi of the family. The restatement calls an F-support, or F-saturated part in terms of the straight order, automatically a sous-contrée. The inverted cancelled draft begins mid-sentence with a family Phi of parts of M subject to a preceding condition. It asserts that inclusion satisfies C1, that the irreducibles are the A_x, and that the capped assignment from x to A_x gives a bijection from M to those objects. Its last line starts Dém with A_x equal to a union of A_i and breaks off. These are statements transcribed from the page, not results established in this run.',
 'math_reading_decisions':[
  'The corollary’s two orders prompted direct comparison of the strokes. The first is straight; the second is bowed. C’s alternative is resolved, while H’s preccurlyeq is treated as equivalent encoding of the same observed bowed glyph.',
  'The inverted application/bijection wording might suggest mapsto, but its short horizontal has two upright terminal caps and no clear arrowhead. The capped sign is retained without assigning it a new logical meaning or repairing it from the expected function notation.',
  'The repeated x, dotted i and barred I were read by their size, strokes and placement. Plain M and the looped live family F are local alphabet readings; the small raised F and possible old layer beneath Phi retain their own uncertainties.',
  'The apparent grammatical preference at the cosupport insertion did not settle whether de was cancelled by the crossing arm. One word position and both states remain in the text.',
  'No claim was proved, computed, used as a checked result or refuted. Reading the manuscript statements and detecting an unusual sign generated no mathematical check event.'
 ],
 'author_checks':[
  'Dém introduces an unfinished argument within the cancelled draft. No completed proof or verification is supplied on this page.',
  'The live restatement has an opening quotation pair without a visible closing pair before the comma, and another closing parenthesis follows 67. These are retained, together with the uncertain right-edge punctuation, rather than regularized.',
  'The lower draft is broadly cancelled. The upper ends of the long strokes lie below its folio, so the folio’s overprint is kept without an invented broad cancellation across the number.'
 ],
 'title_dates_pagination':'No title or date. Running folio remains 70/79 over 69/79, read locally without adjacent-page inference. The inverted folio is 55 in two positions, the second over an uncertain 4/3. The page also carries two marginal columns, the insertion arm, a high mark over itou, a continuous draft boundary, thirteen long cancellation strokes and three detached points.'
}
d['review_status']='approved by root after crop adjudication and text-record review'
d['root_review_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['root_record_review_script']='scripts/review_071_records.py'
d['workflow_note']+=' Root reviewed the draft records, expanded the page-specific mathematical summary without validating its assertions, gave both opening equals crops in their joint disposition, left marginal authorship uncertain, and ordered the lower inventory by the original scan orientation. Paragraph-start rows have medium confidence and narrowly scoped evidence.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print({'approved':d['key'],'changes_C':sum(x['change_c'] for x in d['differences']),'changes_H':sum(x['change_h'] for x in d['differences'])})
