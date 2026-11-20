"""Final sole-reader synthesis; run only after the last rebuild and enrichment.

No page transcription or recorded decision is changed by this script.
"""
from pathlib import Path
import csv,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def block(text,start,end,body):
    body=re.sub(r'\b(on|in|by|all|these|the|including)(?=\d)',r'\1 ',body.strip())
    addition=start+'\n'+body+'\n'+end
    if start in text:return text[:text.index(start)]+addition+text[text.index(end)+len(end):]
    return text.rstrip()+'\n\n'+addition+'\n'
def front(path,start,end,body):
 s=path.read_text()
 if start in s:s=s[:s.index(start)]+s[s.index(end)+len(end):]
 title,rest=s.split('\n',1)
 path.write_text(title+'\n\n'+start+'\n'+re.sub(r'\b(on|in|by|all|these|the|including)(?=\d)',r'\1 ',body.strip())+'\n'+end+'\n'+rest.lstrip('\n'))
def cell(s):return str(s).replace('|',r'\|').replace('\n',' ')
notation=r'''
## Cross-page notation review

The table below records the final comparison made after both readings. Its scope is the written occurrences on these25 leaves. A shared mathematical role resolves ambiguous letterforms only where the ink admits that reading; a clear contrary index, alphabet or unfinished expression is retained. Detailed entries and individual doubts follow.

| family | scans compared | final reading and scope | limits and witness errors |
| --- | --- | --- | --- |
| Divided powers, total stars and iteration |330,332–335|Crossed total-degree stars are distinguished from looped alpha; the superscript order and every parenthesized power remain as written.|The330 beta target reads pq despite the expected p+q. Clear alpha in330 is retained; the first source exponent remains * or p. Both witnesses sometimes supplied the expected degree.|
| Lowercase and uppercase coefficients |330,334,335,337,346|The four coefficient c forms on335 are lowercase, as are the rank coefficients on337; clear C on other leaves stays capital.|This is a local distinction, not a rule that every combinatorial coefficient must be c. H regularized several335 occurrences.|
| Plain and doubled C |337–340,343,346,355|Plain C in the337 exterior-power column is confirmed by338’s repeated notation; explicit inner strokes mark doubled C in340’s K-map sources and nearby unfinished fragment, and in343’s target.|The temporary337 second-reading doubling was withdrawn after this comparison. Clear local alphabet variation, including340’s earlier plain C, is preserved.|
| Stars, degree dots and bracket shapes |338–340,342,345,346,350,352,355,357|A crossed star, round degree dot, prime and square-bracket evaluation index are kept distinct at each position.|The chain inclusion on338 actually changes star to dot in its argument. Extra stars such as345’s m* are retained; these are not made uniform by type.|
| Upright equality pairs |332–335,339,340,343,357–359,361|Two straight upright strokes between aligned formulas are vertical equalities; TeX uses Vert or the visually equivalent parallel glyph.|C’s apostrophe pairs on332,333 and335 were corrected. H sometimes omitted the marks or repeated unwritten objects. Prose quotation marks remain separate.|
| Wavy/bent vertical relations |337,343,355,363|Wavy and straight comparison strokes are distinguished from straight equality pairs.355 has a vertical equivalence sign;363’s definition has two wavy strokes.|The oblique337 signs and363’s overtraced underbrace relation remain doubtful. A single conventional wr is not substituted for two drawn strokes.|
| Flattened K |358,359,361–363|The short upper arm and separate lower fork recur in every classifying/Moore-space K occurrence, including363’s deletion; each is read as K at medium confidence.|The displayed normalization and the recurring notation settle K versus kappa where the isolated form is ambiguous.342’s much more overwritten K/P trial is not resolved by this later habit.|
| Phi, Psi, phi, beta and related loops |330,332–335,337–340,342,346,350,352,355,357,362|Loop-and-stem Phi, forked Psi, descending phi and two-loop beta are compared locally.362’s inserted exterior factor has Phi.|The pale final factor on346 and the raised label on355 retain alternatives. Clear beta in342 is not replaced by alpha.357’s first phi/psi directions remain as drawn despite reversed composite domains.|
| Hom decorations |338,339,355,359,360|Hom! and its raised exclamation, Mon, Hom with a single prime, and unmarked Hom are different written forms.|H’s Mon/Hom confusion on339 is corrected. All three prime-bearing Hom signs on360 remain prime-bearing; no grading dot is imposed.|
| Arrowheads, hooks and parallel shafts |330,332,334,342,343,345,355,357–363|Every written head, missing head, hooked tail, double stem and separate parallel shaft is retained in its diagram.|A headless shaft is not completed from the mathematical direction.355 has a hook without the opposite head;357’s k map has two rightward arrows.|
| Dashes within products |333,337,346|Long and short dashes are retained where written between first and last product factors or before a terminal plus.|The mathematical discussion identifies product continuation where appropriate; the transcription does not replace it by ellipses. H often normalized these runs.|
| n, p, i, j, r and ell |345,350,357,359,361–363|Distinct visible indices are retained; hooked dotted j in362’s deleted trials differs from straight dotted i, and the repeated shoulder-shaped r in the box is read consistently.|The first cancelled362 exponent remains j/i. The359/361 n–p switches,357’s n+1 versus n,362’s unexpected Lambda^i and363’s ell are not regularized.|
| Accents, hats, tildes and primes |330,337–340,355,357,359,360|Check on A, double dual signs, normalization tildes, hats and detached primes retain their written scope.|357 introduces a prime only in the later iterated last-face formula;359 changes tilde to hat locally;360’s tildes attach to Z.|
| Abbreviations and literal blanks |all handwritten leaves;351 typescript|Short forms, unusual spellings, unfinished arguments and actual blank spaces are preserved. Expansions occur only in the abbreviations table.|The equals sign in332’s de = pr is a verbal abbreviation. No closing delimiter, missing sign exponent or typescript symbol is supplied from expectation.|
'''
front(ROOT/'SP67_C13_136_doubts.md','<!-- FINAL_NOTATION_START -->','<!-- FINAL_NOTATION_END -->',notation)
hand=r'''
## Scope of the learned forms

The cross-page review in the doubts file is the consolidated notation table. The entries below preserve the observations made page by page, including which witness was misleading. The following restrictions are part of the hand log:

- The flattened K reading holds at every inspected occurrence on358,359,361,362 and363, including the deleted occurrence on363. It does not decide the differently overwritten342 K/P trial.
- Vertical equality pairs recur on332,333,334,335,339,340,343,357,358,359 and361. The straight pairs are not prose quotation marks. The wavy relations on337,343,355 and363 were compared separately; unresolved overtracing stays doubtful.
- C versus doubled C is not an invariant alphabet rule for the whole dossier. The337 ambiguity was settled from the adjacent repeated exterior-power notation, while340’s visible inner strokes and its clear plain-C exception were retained. Every later occurrence was checked rather than copied from this rule.
- A star can resemble alpha, but a closed alpha-shaped loop is not automatically a star. The total Gamma notation on332/335 and the clear loop in330’s comparison label have different outcomes. The unresolved330 source exponent is still marked.
- Lowercase c is consistent in the four335 coefficients and the337 rank calculation. Clear uppercase C elsewhere remains uppercase. Similarly, the small shoulder-shaped r on362/363 is not made n or2 solely from its silhouette.
- Printed music staves are not handwriting. This affected underlines and apparent equality strokes on340,345,355 and357. The typed351 sheet has different provenance: its underlined matrix y and its spelling are recorded without using them as evidence about Grothendieck’s hand.
- Cancellation scope and insertion attachment must be decided separately from the letters. The cancelled lower draft on330, source-only cancellation on348, erased/circled node on355, full X-crossing on358 and qualification pour X variable on360 illustrate different cases. No universal rule about nearby strokes was applied.

Ambiguous forms not settled by a repeated notation remain local doubts: pale prose on348/350/352; the330 h/k map label;337 oblique signs;355 raised and lower Hom labels;359’s class letter and product sign; and several densely cancelled trials. A hand habit is not a license to repair a clear mathematical slip.
'''
front(ROOT/'SP67_C13_136_hand_log.md','<!-- FINAL_SCOPE_START -->','<!-- FINAL_SCOPE_END -->',hand)
legibility='''## Legibility and witnesses

All25 scans were read in the specified order and then read a second time against their images. Most dark blue formulas and large diagrams are legible, but certainty is not uniform. The pale leaves348,350 and352 are the least secure: interrupted strokes, small interlinear phrases and large crossed paragraphs often permit only a provisional reading. The bottom cancelled prose on348 contains four physically unreadable spans; these remain marked with their approximate word counts. Other weak places include crowded small indices, overwritten Hom labels on355 and densely cancelled trials on337,346,357,360 and363. A plausible mathematical completion has not been used to hide these gaps.

Witness C supplied the fuller diplomatic layout and many useful uncertain readings, but its unmarked indices, parenthesis completions, arrowheads and treatment of vertical ticks still required correction. H sometimes supplied a better letter or word, and sometimes normalized spelling, omitted trials and diagrams, or replaced an unfinished expression with a plausible one. Its omissions on the extensive346 sheet were substantial. Agreement between the witnesses was never treated as independent evidence. The351 typescript has no H witness; it was transcribed in full, including its spelling, blank and annotations, with its hand/provenance distinguished in the inventory.

Confidence labels describe a reading of the supplied scan, not a guarantee of the underlying mathematical assertion. Medium confidence often means a repeated notation resolves an otherwise ambiguous isolated form; low confidence keeps the uncertainty visible in the transcription. The remaining-doubt table and the struck-text ledger below retain the alternatives and unrecoverable places. No OCR, external text, cited publication or TeX compilation was used.
'''
p=ROOT/'SP67_C13_136_doubts.md';s=p.read_text();k=s.index('## Legibility and witnesses');s=s[:k]+re.sub(r'\b(on|in|by|all|these|the|including)(?=\d)',r'\1 ',legibility)
rows=list(csv.DictReader((ROOT/'deleted_mark_review.tsv').open(),delimiter='\t'))
assert all(r['reader_disposition']!='REVIEW REQUIRED' and r['reader_note'] for r in rows)
lines=['## Struck-text doubt decisions','', 'This explicit ledger supplements the 388 indexed live-text marks. It records the 132 original uncertainty tokens inside C’s deletions and 13 final tokens without an identical original-token counterpart. Some final rows are the revised form of an earlier source row, so 145 rows do not mean 145 distinct manuscript places. The dispositions record the first reading and its second-reading confirmation; exact-token matching alone did not decide them.','', '| review id | scan / source | original or final token | disposition | final reading, confidence and evidence |','| --- | --- | --- | --- | --- |']
for r in rows:lines.append('| '+' | '.join(cell(r[x]) for x in ['review_id'])+' | '+cell(r['scan']+' / '+r['origin'])+' | '+cell(r['token'])+' | '+cell(r['reader_disposition'])+' | '+cell(r['reader_note'])+' |')
p.write_text(s.rstrip()+'\n\n'+'\n'.join(lines)+'\n')
feedback='''## Recurring distinctions to add to the error sheet

These are refinements of recurring error mechanisms, not additional places to add to the counts above.

| recurring issue | places in this run | practical consequence |
| --- | --- | --- |
| Printed ruling mistaken for manuscript emphasis or a relation |340 second-row dot;345 vertical staves;355 Hom underlines;357 MacLane/Homology citation|Compare stroke color, continuity and regular spacing before adding an underline or equals sign.|
| An unfinished delimiter or empty sign slot completed as standard notation |330 lower Hom and Sym trials;332 nested expressions;345 last closing cluster;355 Hom trials;357 cochain target and cup sign;358 two missing closes;360 two theorem rows;361 first H factor and sign exponent|Distinguish actual missing ink from an unreadable written character. Empty does not mean illegible.|
| A repeated mathematical role overriding a clear local alphabet or index change |330 pq target;334 iteration order;338 star/dot argument;340 plain/doubled C variation;357 composite domains and cup indices;359/361 n–p switches;362 Lambda^i|Use mathematics to detect the place, then preserve the clear written form and discuss the mismatch in the notes.|
| Counting shafts without checking the relation they form |342 double-stem arrow versus two parallel maps;355 hook without opposite head;357 two k arrows;359 two top arrows|Count heads, tails and separate shafts independently. A double stem, a pair of maps and a vertical equals sign are different objects.|
| An irregular border or callout reduced to a typographic box/label |334 degré p callout;343 enclosure;348 three-sided pale outline;355 B0 callout and F(X*) enclosure;360 two-line parenthesis;362 box and partial underline|Reproduce the drawing’s scope and openings, not merely its textual label.|
| Whole-region versus local cancellation confused |330 lower draft;338 et iso can.;346 lower index conditions;348 source versus target and two whole paragraphs;357 naturels and cap;358 parenthesized diagram|Determine the cancelled region first, then transcribe surviving live material and earlier trials separately.|
| Editorial structure of H mistaken for source content |H section headings after352,355 and363; continuation note after361|These editorial headings are excluded from the transcription and the substantive collation count. Manuscript EZ labels and author/archive numbers are still included.|

Certainty-only resolutions are listed in the doubts file, including the struck-text ledger; they are not added to substantive change counts merely because an uncertainty wrapper disappeared. Explicit descriptions in H are credited for the manuscript content they convey; the raised C*(U) insertion on350, enclosing oval on355, whole-block cross on358, cancelled trial on359 and deleted index on362 are not counted against H merely because they occur in prose notes. Counts above measure logged places, sometimes one repeated phenomenon over several occurrences, rather than individual glyphs or a total error rate for either witness. The changes log identifies separately which witness differs at each place.
'''
p=ROOT/'SP67_C13_136_sheet_feedback.md';p.write_text(block(p.read_text(),'<!-- FINAL_FEEDBACK_START -->','<!-- FINAL_FEEDBACK_END -->',feedback))
methods='''## Reading and mathematical-check scope

The page notes describe what these leaves state, calculate or ask. A manuscript assertion or citation is not by itself a verified theorem. CHECK_EVENTS.tsv records the limited proof checks, direct algebraic computations and explicitly retained background assumptions actually used in this run. For example, composition domains, degree counts and a displayed sign can be checked without proving the surrounding Eilenberg–Zilber, free-resolution, operation, décalage or stability claims. Qualifications and possible slips are kept in these notes; they do not alter the ink in the transcription.

The only textual sources used were the supplied scans and witnesses C and H. References named on the leaves were transcribed without consulting those works. One reader made all ink and mathematical decisions; a separate helper performed only schema, token, macro, count and package checks. The archive contains the reading records and scripts for traceability. No scan, half, crop or other image is included; the changes file records the 233 inspection boxes in original-image coordinates.
'''
p=ROOT/'SP67_C13_136_notes.md';p.write_text(block(p.read_text(),'<!-- FINAL_METHOD_START -->','<!-- FINAL_METHOD_END -->',methods))
log=ROOT/'progress.log';s=log.read_text()
marker='cross-page notation review completed'
if marker not in s:
 with log.open('a') as f:f.write(f'{marker} {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}; paired relations, C alphabets, flattened K, stars/dots, coefficient case, indices, primes, accents, arrow forms and unfinished expressions compared;145 struck-token ledger rows explicitly disposed by sole reader; final report synthesis written\n')
print('Final report synthesis complete;145 deleted-review rows included.')
