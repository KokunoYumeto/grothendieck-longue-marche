"""Consolidate the reader's reports and tabular counts after the second reading.

This script does not examine images or make transcription decisions. Its prose
records the completed manual image readings; its tables derive from the saved
canonical records. Run once before freezing the transcription.
"""
import csv
from collections import Counter
from reading_support import ROOT, PREFIX, read_table, build_changes, assemble, log, md, utc
from audit_second_read import replace_in, write_table

if (ROOT/(PREFIX+'_sheet_feedback.md')).exists():
    raise RuntimeError('Final reports already exist; do not duplicate finalization.')

replace_in(PREFIX+'_notes.md',
    'The repeated category role and matching curves justify reading the three as `\\mathcal C`; the alphabet choice is medium confidence.',
    'The repeated category role and matching curves identify the letter as C. The second reading qualifies the first pass: ordinary versus calligraphic alphabet is not secure, so the first occurrence is `\\unsure{C|\\mathcal C}` and the later two are plain C under that same doubt.')
replace_in(PREFIX+'_notes.md',
    'It will be reconciled with scan 017 during the second reading.',
    'The second reading applies this same alphabet doubt to scan 017; the recurrent letter is consistent without claiming a securely distinguishable calligraphic style.')
replace_in(PREFIX+'_notes.md',
    'The top word completes scan 023: “contour.” The manuscript itself has no following stop. Underlined “Exos (DEA)” asks:',
    'The top word “contour” completes scan 023, without a following stop. Underlined “Exos”, followed by “(DEA)”, asks:')
replace_in(PREFIX+'_hand_log.md',
    'This qualifies the firmer script interpretation on scan 017 and must be resolved consistently at audit.',
    'The second reading has qualified the earlier script interpretation on scan 017 accordingly: the first occurrence carries the alphabet doubt, and subsequent occurrences are plain C.')
replace_in(PREFIX+'_hand_log.md',
    'Later pages must decide whether there is a distinct notation.',
    'The later pages do not settle all attached caps; scan 017 has one securely detached bar. The remaining broad-cap forms keep their explicit doubt.')
replace_in(PREFIX+'_doubts.md',
    'The category alphabet is now explicitly open (`C|\\mathcal C`), pending comparison with scan 017.',
    'The second reading consistently retains the category alphabet doubt (`C|\\mathcal C`) on scans 017–019 and 022, without forcing a calligraphic style.')

# Preserve the already written certainty decisions as a separate section.
old_doubts=(ROOT/(PREFIX+'_doubts.md')).read_text()
certainty=old_doubts[old_doubts.index('### Scan 016'):]
rows=read_table('remaining_doubts.tsv')
for r in rows:
    if r['scan']=='16' and r['line']=='first product and recurring torsor letter':
        r['reason']='The broad horizontal cap may belong to P; the visible lower loop excludes T. Cross-page comparison finds one detached bar on scan 017 but does not settle every attached cap. The ambiguity remains local and explicit.'
    if r['scan']=='16' and r['line']=='foot addition, two deletions':
        r['reading']=r"\deleted{\unsure{ens|d'un}} \deleted{\unsure{$(G,E)$-st}}"
    if r['scan']=='21' and r['line']=='corrected Y in second proposition':
        r['reading']=r'\deleted{\unsure{X}}Y in two positions'
rows=sorted(rows,key=lambda r:int(r['scan']))
write_table('remaining_doubts.tsv',rows)

notation=r'''# SP61_CW_75 — Notation, doubts, and abbreviations

## Notation table

This table records the comparison across all ten pages after the second image reading. A common letter form is read consistently; a clear local difference is retained. An uncertainty at the first occurrence of a recurring form governs the later occurrences specified here. This does not assert that every category called C on different pages is the same mathematical category.

| Sign / notation | Reading and visible form | Scope and exceptions |
| --- | --- | --- |
| P and a possible bar | Standalone P often has a broad cap above a short lower loop; small raised P has an ordinary loop. | Scans 016–017: initial `P` / barred-P doubt retained. Scan 017's first Isom result has a detached bar and is explicitly barred. T is not substituted for the looped P. |
| T and T′ | A long top bar and upright, usually without P's loop. A separate short raised mark is read as a possible prime. | Torsor notation on 019–025. The first twist on 019 remains `T′` / `T`; the later unprimed occurrences are not changed to match it. |
| Twists and extensions | Left superscripts in the earlier twists; live right superscripts in extension notation. | Left P/T on 016–020 and left ω on 024. The live `E^{G′}` on 020 and `T^{G′}`, `F^T` on 021 remain on the right. Cancelled earlier exponents stay separate. |
| Contracted product | A crossing × with a low group label; distinct from the open ∧ used later. | Products on 016–021 and 025. Wedges on 021–024 are retained where drawn, including low `{±1}` on 022. No replacement by a mathematically preferred product glyph. |
| Category C | Open C curves alternate with an inward upper curl resembling e. The curve does not establish a calligraphic alphabet. | First relevant occurrence on 017, 018, 019 and 022 explicitly offers C / calligraphic C; later letters in that family use plain C. The subscripts and primes remain as written. |
| Script E | A curved upper body, inward middle turn and lower lobe distinguish it from nearby open C. | Scan 019's action-category labels and Aut superscript. Retained even where the prose or another node still says C. |
| G versus C | Small G can be open, with a short descending stroke at the lower right. | The raised group identity on 018 prefers G with C alternative. No universal rule turns every open capital into G. |
| E versus F | E's third arm can be extremely short. | The second orientation subscript on 025 is E. The object labels E and F elsewhere are individually retained. |
| B | Plain B may be overwritten by E or remain a separate abbreviation. | Old B in the product on 016; live B in the stabilizer paragraph is not expanded to Bij. The paired set on 022 is B. |
| u versus x | u has a shallow trough; x may have a rounded first stroke but a crossing remains. | Scan 016 really alternates live u with x in a membership parenthesis. Scan 017 evaluation x is clear; the last source letter remains u/x. |
| ζ, τ, σ | ζ has a long curling body; τ has a horizontal top with short stem; σ has an open loop. | Scan 018's live labels are distinguished; cancelled versions remain doubtful. The exponent on σ on 022 is 2/prime, not silently regularized. |
| Φ, ω, Γ | Capital Φ has a central upright; ω has low joined humps; Γ is angular. | Φ in 019; ω orientation/twist notation in 023–025; Γ in 024. Low indices, including the doubtful E₀ on 019, are individually retained. |
| Numeral 1 and unit | The torsor unit has two stems and a base. | Scan 021 uses `\mathbb{1}`; the second is written over an old G-like designation and is separately underlined. Ordinary numerals 1 elsewhere are not doubled automatically. |
| Field and number alphabets | Visible duplicate stems/diagonals are represented by blackboard letters. | Double C on 018, N on 022, Z_n on 023, and most real-number R forms on 020/025. The abstract Z on 024 and the R in the first orientation quotient on 025 remain plain. |
| Equivalence marks | Wavy signs, approximation signs and arrows are kept distinct. | Scan 022 has a vertical wavy decoration beside a downward arrow. Scan 023's first identification is a left arrow with a wavy sign; its lower relation remains unresolved. |
| Arrows, source bars and blunt lines | A transverse source bar is different from a pointed head. Some connectors are genuinely headless. | Blunt/bar-ended forms on 016–021 remain blunt. The solid rising diagonal on 019 has a source bar; the opposite diagonal is dashed. No blanket conversion to mapsto or two-headed arrows. |
| à versus punctuation | An accent and very short lower body can resemble two dots. | The reduced word recurs on 016, 018–021 and 025. Scan 024 prefers à with colon as an alternative after cross-page comparison. The clear colon in `G:Aut_C(E)` on 019 remains a colon. |
| Added versus struck text | Long curved strokes often attach an interlinear word; an actual cancellation crosses older letter bodies. | Particularly 016, 018, 020–022 and 025. The live words `sur les` on 021 are not cancelled by the insertion guide above them. Old readable terms are kept with deletion macros. |
| Quotation and section marks | Two short opening/closing quotation strokes; circled Arabic item numbers. | Quotations on 016 and 020 use the required paired backticks/apostrophes. Circled items follow the local source sequence, including a fresh 1–2 on 023. |
| Accents and spelling | Accents are not supplied from conventional spelling; singular/plural endings are not repaired. | `polygône`, `cotés`, `homothetie`, `homotheties`, `role`, the singular `muni`, and the module-adjective doubts retain their local spellings. |

## Remaining doubts

The table groups adjacent inseparable uncertainties at a single locus; its row count is not the number of `\unsure` macros. The first candidate is the current visual preference. “Low” is a real limit on the reading, not an assertion that a correction has been established. Two wholly obscured cancelled words use `\illegible{1}`; uncertain mathematical symbols do not use that macro.

| Scan | Line / place | Current reading | Alternatives | Confidence | Why unresolved |
| --- | --- | --- | --- | --- | --- |
'''
table='\n'.join('| '+' | '.join(md(r[k]) for k in ['scan','line','reading','alternatives','confidence','reason'])+' |' for r in rows)
abbreviations=r'''

## Abbreviations encountered

These proposed expansions are explanatory only and are never inserted into the transcription. A stop, superscript or ending is included below only in forms actually encountered; the same short form can appear with and without a stop on different lines.

| Written form | Likely expansion / meaning | Scans / qualification |
| --- | --- | --- |
| tt; ttes | tout / tous; toutes | 018, 020, 022; agreement depends on the phrase. |
| ens; ens. | ensemble / ensembles | Throughout; no automatic terminal period. |
| pts; pt | points; point | 016; 022. |
| p.r. | par rapport | 016. |
| fidᵗ; fid | fidèlement | Small foot addition on 016; cancelled wording on 018. |
| st; str | structure | Cancelled `(G,E)-st` on 016; inserted str on 017. Some cancelled stan/st on 018 belongs instead to an abandoned start of standard. |
| applicᵗⁿ | application | 016 foot addition; both the terminal letters and their raised form remain uncertain. |
| Ex; Ex.; Exos | exemple, exemple(s), or exercices according to context | 017, 021; Exos on 024 denotes exercises. No full word is substituted in the fragment. |
| p.ex. | par exemple | 017. |
| NB | nota bene | 016, cancelled on 017, 019, 020. |
| i.e. | id est / c'est-à-dire | 016–018, 020. |
| top. | topologique | 017. |
| Méth. / Mét. | probably méthode | Cancelled heading on 017; uncertain letters, so expansion is tentative. |
| isom; isom.; iso | isomorphe / isomorphisme(s) | 016–023; adjective and noun uses are distinguished by context, not expanded. |
| cat; cat.; catégor. | catégorie | 019, 022. |
| ss/cat. / s/cat. | sous-catégorie | 019; the doubled prefix remains doubtful. |
| ds | dans | 019. |
| can. | canonique | 019, 021, 023. |
| cf | confer / comparer | 019 margin; underlined, without a supplied stop. |
| comb. | combinatoire | 020, 023. |
| rg | rang | 020. |
| Changᵐᵗ | changement | Cancelled heading on 020. |
| g; g. | gauche | 020–021; direction words can conflict with the formulas and are not repaired. |
| dr; dr.; drᵗᵉ | droite | 020, 025; raised te on 020 remains uncertain. |
| Op. | opération(s) | 021. |
| Prop | proposition | 021; no terminal stop supplied. |
| él; élémts | élément; éléments | 021, 023; full versus compressed spelling is doubtful at some loci. |
| rel.; équiv. | relation; équivalence / équivaut | 021–022; équiv. is only an alternative in the small foot text on 016. |
| card.; card | cardinal | 022. |
| syst. | système | 022. |
| inversmt / inversemt | inversement | 023; contracted/full spelling remains unresolved. |
| 1/2 direct | semi-direct | 024; the numerical shorthand and absence of a hyphen are preserved. |
| DEA | probably diplôme d'études approfondies | Course/exercise designation on 019 and 024; no external identification was researched. |
| dim | dimension | 025. |
| hom | homomorphisme | 025. |
| comm. | commutatif / commutatif (diagramme) | 025, ring and diagram contexts. |
| quadr; quadr. | quadratique | 025; the deleted old word remains doubtful. |
| tors | torseur | Cancelled on 023; live on 025. |
| orthon. | orthonormale(s) | 025. |
| ext. | extension | 025. |
| incl | inclusion | Bottom diagram on 025. |
| Aut, Bij, Hom, Isom, Ob, Tors, Env | automorphismes, bijections, morphismes/foncteurs, isomorphismes, objets, torseurs, enveloppe | Mathematical operator names; capitals and underlines follow the ink. |
| det, sgn, id, Gl, O, SO | déterminant; signe; identité; general linear, orthogonal, special orthogonal group | Mathematical labels; these explanations do not alter the source's notation or its general-ring claim. |

## Certainty-only decisions and audit qualifications

'''
trust=r'''
## Legibility and comparison of the witnesses

The main live text and most displayed formulas are reasonably legible in the supplied enhanced halves. The least trustworthy passages are the crowded foot addition and corollary on scan 016; overwritten capitals and cancelled short words on 017–021; the clipped right edge and lower relation on 023; and the smudged determinant-label area on 025. The small possible deleted `sgn` on 025 is particularly insecure: both its reading and its status as text rather than smear are uncertain. A legible neighboring formula does not cure that uncertainty.

Witness C was closer to a diplomatic record in this run: it usually preserved short forms, insertion layers and cancellations, and it explicitly exposed many difficult loci. It still required changes at both doubtful and undoubted places, including the u/x stabilizers, category forms, connectors, the noun involution and opère. H sometimes gave the clearer live word, notably involution and opère, but it also expanded abbreviations, supplied punctuation, regularized word endings, or omitted earlier layers. Its separate notes were consulted as part of the witness; editorial prose was not transcribed as source text. Its conventional formatting alone was not counted as a reading difference.

Agreement between the witnesses was not treated as visual evidence. The root reader made both sequential image readings; a separate helper performed only mechanical checks of files and tables, without images or witnesses. This is an AI consolidation with explicit unresolved readings, not a human-verified edition. No OCR, outside research, image-based recognition software or TeX compilation was used. The counts in the changes report measure recorded difference loci, including tentative ones; they are not error rates or a claim of exhaustive certainty.
'''
(ROOT/(PREFIX+'_doubts.md')).write_text(notation+table+abbreviations+certainty+trust)

# The pencilled archive numbers already survive as comments in each fragment.
# Make their separate visual inventory status explicit without attributing the
# pencilled hand to the author.
p=ROOT/(PREFIX+'_inventory.csv')
with p.open(newline='') as f:
    reader=csv.DictReader(f)
    fields=reader.fieldnames
    inv=list(reader)
for scan in range(16,26):
    entries=[r for r in inv if r['scan']==str(scan)]
    if any('archive numeral' in r['position'] for r in entries):
        raise RuntimeError('Archive numeral already inventoried')
    number=max(int(r['element'].split('-E')[1]) for r in entries)+1
    inv.append(dict(zip(fields,[scan,'text','unnamed hand (pencil numbering; attribution uncertain)',f'S{scan:03}-E{number:02}','text','foot, pencil archive numeral',str(scan-1)+'; retained as archive sheet number comment','yes'])))
inv=sorted(inv,key=lambda r:(int(r['scan']),int(r['element'].split('-E')[1])))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fields)
    w.writeheader();w.writerows(inv)

decisions=read_table('reading_decisions.tsv')
names={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left as illegible',6:'Insertion placement',7:'Struck text and overwritten layers',8:'Abbreviations and spelling',9:'Text not on the page',10:'Other'}
feedback=['# SP61_CW_75 — Feedback on the error sheet','',
 'Counts are of recorded difference loci, with one primary error-sheet category per row. They include unresolved and low-confidence readings, so they must not be read as counts of proven witness errors. A locus can differ from both witnesses; the C and H columns overlap. Confidence concerns the recorded decision, not every letter inside a long row. Pure macro differences and certainty-only decisions are excluded.','',
 '| Error-sheet kind | All loci | Against C | Against H | High | Medium | Low |',
 '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
for n in range(1,11):
    rs=[r for r in decisions if int(r['error_sheet'])==n]
    values=[len(rs),sum(r['against_C']=='yes' for r in rs),sum(r['against_H']=='yes' for r in rs)]+[sum(r['confidence']==c for r in rs) for c in ['high','medium','low']]
    feedback.append('| '+str(n)+'. '+names[n]+' | '+' | '.join(map(str,values))+' |')
values=[len(decisions),sum(r['against_C']=='yes' for r in decisions),sum(r['against_H']=='yes' for r in decisions)]+[sum(r['confidence']==c for r in decisions) for c in ['high','medium','low']]
feedback.append('| **Total** | '+' | '.join(map(str,values))+' |')
feedback += ['', '## Places by primary category', '', 'The IDs below refer to the final changes table; that table supplies both witness readings and the image evidence.']
for n in range(1,11):
    feedback += ['',f'### {n}. {names[n]}','',', '.join(r['id'] for r in decisions if int(r['error_sheet'])==n)+'.']
feedback += ['','## Additional recurring patterns worth naming','',
 'All observed patterns fit the sheet’s ten broad categories. The following more specific patterns deserve explicit prompts in later runs; they are not additional counts.','',
 '| Pattern | Places | What to check next time |',
 '| --- | --- | --- |',
 '| Stops added to short forms | ens on 017, 018, 020, 022, 023, 025; dim, hom, tors and quadr on 025 | A conventional abbreviation does not authorize a terminal dot. Inspect each word ending separately. |',
 '| Letter identity confused with typographic alphabet | Category C on 017–019/022; script E on 019; doubled Z on 023 versus plain Z on 024; real-number R on 025 | Establish the letter first, then ask whether the ink truly distinguishes its alphabet. State an alphabet doubt instead of forcing a font choice. |',
 '| Headless connectors promoted to ordinary maps | 016 NB; 017 evaluation; 018 sigma row; 019 margin; 020 group-change stroke; 021 inverse formula | Read head, source bar and shaft independently. Mathematical function does not supply a missing point. |',
 '| Old terms lost inside overwriting | 016 B→E; 017 Applications; 020 direction and exponents; 021 X→Y and G→unit; 024 factor names; 025 scalar and old quadratic text | Separate the live letter from each recoverable old layer; a note that merely says surcharge does not necessarily give the earlier reading. |',
 '| Insertion guides mistaken for cancellation or literal parentheses | 017 str; 020 direction; 021 de produit and new example; 022 card. 2n; 025 quadratique | Determine which line the guide touches before deciding the status or attachment of the words. |',
 '| Grammatically expected words or endings supplied | 017 muni; 018 singular structure; 022 munis/muni; 023 absent ens after deleted tors; 025 Module/libre | Preserve agreement failures and missing nouns. A mathematical or grammatical repair belongs only in the notes. |',
 '| Small à mistaken for a colon | 016 direction; 019 uniqueness phrase; 024 celle de, compared with 018 and 025 | Compare the same reduced accent-plus-body form across the run. Do not replace the genuine mathematical colon after G on 019. |',
 '', '## What remained unresolved', '',
 f'There are {len(rows)} grouped doubt loci in the final doubts table. Dense cancellations, clipped edges and smudges are not made legible by a plausible argument. The scan-023 lower relation and possible old scan-025 label are explicit low-confidence examples. Two wholly obscured cancelled words remain illegible. No second crop of a decided locus was made; the existing crops at those two difficult formula loci were reviewed during the second reading.',
 '', '## Audit changes and counting discipline', '',
 'The second reading qualified the three category subscripts on scan 017 and preferred the recurring reduced à on scan 024. The latter now agrees with both witnesses’ preferred word, so its first-pass difference row was removed. The italic/underlined compatibility heading on scan 025 was also removed as a rendering-convention-only difference. Historical first-pass records remain documented in the audit and checkpoint; the current tables and totals use the final decisions.',
 '', 'The inventory includes the ten pencilled archive numerals as separately attributed elements; the fragments preserve them in comments rather than misidentifying them as authorial manuscript page numbers. No page in this supplied run is a typescript, reused typed sheet, cover, letter or list.']
(ROOT/(PREFIX+'_sheet_feedback.md')).write_text('\n'.join(feedback)+'\n')

readme=f'''# SP61_CW_75 — Consolidated diplomatic transcription

## Scope

Montpellier cote 75, archive scans 16–25. The ten supplied sheets were read in order by the root reader against witnesses C and H, then read against their images a second time in the same order. H’s page numbers are one less than the scan numbers. The pencilled archive numerals 15–24 are retained in fragment comments and separately inventoried; no authorial date or page count was found on these sheets.

## Files

- `pages/`: one LaTeX fragment per scan, named as in C.
- `{PREFIX}_transcription.tex`: the ordered combined fragment, with no preamble.
- `{PREFIX}_changes.md`: differences from either witness, counts, consequences, unresolved places and every crop box.
- `{PREFIX}_collation.tsv`: only the differences from H, in the requested schema.
- `{PREFIX}_doubts.md`: notation table, remaining doubts, abbreviations, certainty decisions and trust limits.
- `{PREFIX}_inventory.csv`: all recorded page elements, including the pencilled numerals.
- `{PREFIX}_notes.md` and `CHECK_EVENTS.tsv`: page notes and the actual mathematical checks performed.
- `{PREFIX}_hand_log.md` and `{PREFIX}_sheet_feedback.md`: observed handwriting habits and error-sheet feedback.
- `{PREFIX}_audit.md`, `progress.log`, `checkpoint_history.md`: the two-reading and checkpoint record.
- `reading_decisions.tsv`, `remaining_doubts.tsv`, `crop_register.tsv`: canonical supporting tables.
- `scripts/`: the actual recording, report-building, validation and packaging code. Per-page recording scripts document the first pass and must not be rerun over the finalized tables.
- `transcription_hashes.sha256`: the frozen page/combined hashes; the completion log records their final verification.
- `package_file_list.txt`: every file included in this archive.

## Editorial limits

Uncertain readings remain marked in place; spelling, abbreviations, contradictory direction words, incomplete sentences and possible mathematical slips are not silently corrected. Mathematical comments do not alter the transcription. Low-confidence differences are not presented as established errors. The final reports supersede first-pass choices where the audit records a revision.

The fragments use the supplied C macro vocabulary with standard LaTeX, TikZ and tikz-cd. No new preamble is supplied and no TeX compilation was performed. Mechanical checks verify file structure and internal records, not fidelity to the handwriting or rendered layout. The mechanical helper did not read images or witnesses. No OCR or outside research was used. This remains an AI reading with disclosed uncertainties.

No source scans, crops, witness files, input archives, earlier checkpoint ZIPs or generated caches are included.

Reports consolidated {utc()}.
'''
(ROOT/'README.md').write_text(readme)

with (ROOT/(PREFIX+'_hand_log.md')).open('a') as f:
    f.write('## Cross-page audit conclusion\n\nThe second reading retained local distinctions in P caps, twists, product glyphs, alphabets and arrow decorations. It qualified the original calligraphic-C choice and used the recurring reduced à form to reorder the scan-024 doubt. No general handwriting rule was used to erase a clear local letter, prime, punctuation mark or cancellation. The notation table in the doubts file gives the final scope and exceptions.\n\nThe small pencilled numerals 15–24 are visually distinct from the body hand. Their attribution is left uncertain; they are treated as archive numbering, not as the author’s own page count.\n')
with (ROOT/(PREFIX+'_audit.md')).open('a') as f:
    f.write('## Cross-page comparison and report reconciliation\n\nAll ten second image readings were completed in scan order. Recurring C, script E, P/T caps, u/x, Greek labels, doubled number letters, unit signs, twist positions, blunt/source-barred connectors, abbreviation stops and reduced à forms were compared across the run. Remaining local differences are documented in the notation and hand tables rather than normalized. The final inventory separately records the pencilled archive numerals already preserved in comments. Stale first-pass alphabet statements were updated, and certainty-only or pure rendering-convention differences were excluded from counts.\n\nNo further source-text change was made during this report reconciliation.\n')
assemble();build_changes()
log('reports consolidated after all ten second readings; archive numeral inventory completed')
print('Reports consolidated:',len(decisions),'difference loci;',len(rows),'grouped doubt loci;',len(inv),'inventory elements.')
