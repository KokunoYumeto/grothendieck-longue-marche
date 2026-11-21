"""Finalize descriptive documentation from completed audit records; no image reading."""
from pathlib import Path
import json,collections,datetime
W=Path(__file__).resolve().parents[1];ROOT=W.parent;D=ROOT/'scratch/reader_c_final_docs'
order=(W/'scripts/page_order.txt').read_text().split();rs=[json.loads((W/'reports'/p/'report.json').read_text()) for p in order]
assert len(rs)==25 and all(r.get('audited_utc') for r in rs)
audit={k:sum(r['audit_counts'][k] for r in rs) for k in rs[0]['audit_counts']}
cs=[c for r in rs for c in r['changes']];conf=collections.Counter(c['confidence'] for c in cs)
summary=f"All 25 pages are audited: {audit['boxes']} fixed boxes, {audit['differing_boxes']} nonidentical boxes, {audit['token_edit_spans']} token-edit spans and {audit['changed_boxes']} revised boxes."
outcomes={
'020':'17 boxes; 12 nonidentical; 34 token-edit spans; 5 revised. X_i is now preferred in the overworked base position, with Y retained. The old tuple token, cô opening, cancelled wording and small diagram arrowhead remain locally qualified.',
'023':'23 boxes; 18 nonidentical; 69 token-edit spans; 13 revised. Most revisions add local alternatives. The unsupported Les before the final marginal morphismes is removed; the final curved mark prefers a closing parenthesis, with an exclamation alternative. A wider native margin frame separates the two writing directions.',
'024':'23 boxes; 21 nonidentical; 106 token-edit spans; 8 revised. The conjunction before T favors a literal ampersand, and the small crossed group favors E_0 I over E intersection T. Labels, a tiny insertion and cancelled formula/text attachments retain alternatives. Eight diagram objects, three equivalences, three cups and nine diagonals were counted twice.'}
# Complete legibility assessment, retaining the honest comparative limitations.
s=(D/'legibility.txt').read_text()
s=s.replace('These assessments come from the existing reading records; the final independent-audit outcomes for scans 020, 023 and 024 remain to be incorporated below.','These assessments combine the first readings with the completed independent audits and root crop adjudications.')
a=s.index('At the verified snapshot');b=s.index('One documented workflow limitation')
s=s[:a]+summary+' All 195 original marks have decisions: 82 first candidates, 6 listed alternatives, 20 other readings and 87 still undecided. A differing box can contain several issues; token agreement is not proof that every ink element has been recovered.\n\n'+''.join('150_scan'+k+': '+v+'\n\n' for k,v in outcomes.items())+s[b:]
s=s.replace('The final closure above must not erase that exception or imply a fresh review of every image. ','')
s=s.replace('No OCR, external textual research to fill gaps, or TeX compilation was used for these documentation updates;','No OCR, external textual research to fill gaps, or TeX compilation was used;')
(W/'reports/legibility.txt').write_text(s)
# Error-sheet feedback remains separate from generated per-category counts.
s=(D/'feedback_extra.md').read_text();s=s.replace('and is explicit in the first-reading record for 150_scan024 P16–P20.','and remains explicit after the audit of 150_scan024 P16–P20.').replace('The first-reading record distinguishes heavy and thin I forms on 150_scan024.','The completed audit retains the heavy and thin I forms on 150_scan024.')
s=s.replace('Examples on scans 020, 023 and 024 remain subject to their pending root-audit closure at the snapshot used for this draft.','The final audits preserve those local differences and record their remaining uncertainty.')
a=s.index('At 21 November 2026');b=s.index('## Workflow limitation')
s=s[:a]+summary+' All 195 original marks have decision rows. These box counts are different units from the '+str(len(cs))+' witness-collation entries and their ten error-category totals.\n\n'+''.join('- **150_scan'+k+':** '+v+'\n' for k,v in outcomes.items())+'\n'+s[b:]
(W/'reports/feedback_extra.md').write_text(s)
# Preserve dated comparison observations, then close their relationship to accepted source.
s=(D/'notation_comparison.md').read_text();s=s[:s.index('## Independent-audit closure')]
s+='''\n## Literal point/dash strings and local connectors

The completed readings retain point/dash variants in Sigma flags and their adjacent tuple/diagram notation on 150_scan002, 004, 005 and 007. They are not mechanically replaced by a standard ellipsis or an expected index sequence. A headless connector remains headless where no head was visible; an arrow/headless alternative is local to the uncertain endpoint. The evidence is the cited changes and root adjudications for each page, including 150_scan020 B07/B15 and 150_scan023 B08. This paragraph reconciles already recorded decisions; it is not an additional image inspection.

## Independent-audit closure

'''+summary+''' The 195 original mark IDs remain in their source order. The first and second readings stay fixed; accepted readings are in the page fragments and root adjudications.

'''+''.join('### 150_scan'+k+'\n\n'+v+'\n\n' for k,v in outcomes.items())+'''The notation table is regenerated from the accepted page records. The source-formatting and metadata receipts document the later changes to encoding or descriptive wording; those changes neither supply new source glyphs nor normalize the remaining alternatives. The original cross-comparison sessions above retain their dates and scope. The final proof-event table is separately scoped and does not treat notation comparison as a mathematical proof.

The redundant 150_scan024 P23 crop remains documented and supplies no independent confirmation. No additional image pass was performed merely to update this file.
'''
(W/'reports/notation_comparison.md').write_text(s)
# Scope mismatches are retained, rather than concealing them by rewriting fixed boxes.
s=(D/'audit_box_scope_check.md').read_text();s=s[:s.index('## Fixed records and root closure')]
s+='''## Scope issues resolved during root adjudication

| Box | Recorded resolution |
| --- | --- |
| 150_scan003 B18 | The fixed box showed I-to-X, already in prose. The wider saved P17 frame separately showed the lower horizontal rule. |
| 150_scan004 B13 | A wider original frame restored the opening parenthesis and forall i,j outside the fixed box. |
| 150_scan004 B33 | The fixed box mainly showed the following 4° line; a wider frame restored the complete intersection/union formula and bound. |
| 150_scan005 B08 | The ending en principe was visible at the beginning of neighboring B09; it was not omitted as absent. |
| 150_scan005 B11 | Wider native context supplied the following live n’est pas vrai, exemple I= after the cancelled line. |
| 150_scan005 B17 | The wider saved P14 frame supplied Ainsi, les strat. ps. fidèles des before the fixed excerpt. |
| 150_scan012 B24 | Wider original context restored the independent dot above the first T, clipped from the fixed box. |
| 150_scan012 B29 | The fixed box covered Soit. Wider context showed the separate circled 1 immediately to its left; both remain transcribed once. |
| 150_scan013 B08 | The apparent extra crossed marginal symbol was the rotated main-text number (6). A separate marginal question mark was retained. |
| 150_scan018 B18 / margin | Native orientation identified the apparent arrow as the main-text ending ment and the apparent cross as main X_i; they are not duplicated as marginal drawing strokes. |
| 150_scan019 B06/B08 | Native context separated diagonal p.r. à and neighboring note strokes from main que si/alors. No extra cancelled que was invented. |
| 150_scan023 B11 | Wider native margin context separated overlapping writing directions and showed no separate Les before morphismes. The curved terminal mark remains doubtful. |

## Fixed records and final closure

'''+summary+''' Every page has a different first and second reader, and every nonidentical box has an explicit root adjudication. Wider review frames supplement the evidence without changing the 560 fixed box definitions. Fixed input hashes are checked against comparison metadata in the final verification receipt.

First/second TSVs remain historical after adjudication. Current source encoding and descriptive repairs are recorded separately; historical snapshots and their original hashes are not rewritten to match the final text.

## Recorded workflow limitation

The 150_scan024 P23 frame inadvertently duplicates most of P16 and supplied no new reading. It is preserved and is not counted as independent confirmation. P22’s clipped-ascender completion is separately documented. The full independent audit remains available, including all decisions retaining uncertainty. No images were reopened solely to prepare this scope summary.
'''
(W/'reports/audit_box_scope_check.md').write_text(s)
# README avoids self-referential ZIP hash or upload claims. Those external receipts
# cannot be inserted into the very archive whose final bytes they certify.
counts={'rows':len(cs),'against_c':sum(c['against_c'] for c in cs),'against_h':sum(c['against_h'] for c in cs),'confidence':dict(conf),'audit':audit,'original_marks':195,'inventory_elements':sum(len(r['inventory']) for r in rs)}
(W/'reports/final_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
readme='''# SP89_C13_149+150 — Diplomatic transcription and evidence

All 25 manuscript pages have a consolidated reading, an independently fixed second reading and completed root crop adjudication. The accepted text preserves source spelling, abbreviations, punctuation, notation, revision states and local uncertainty. Mathematical diagnostics and proposed repairs belong to the notes; they do not replace written ink.

## Completion record

| Measure | Final count |
| --- | ---: |
| Pages / independently audited pages | 25 / 25 |
| Fixed comparison boxes | 560 |
| Nonidentical boxes / token-edit spans | 472 / 2,546 |
| Boxes revised after adjudication | 194 |
| Local witness-collation entries | 953 |
| Entries differing from C / from H | 502 / 826 |
| High / medium / low confidence entries | 522 / 276 / 155 |
| Original mark decisions | 195 |
| Original marks: first / alternative / other / undecided | 82 / 6 / 20 / 87 |
| Inventoried page elements | 679 |
| Preserved crop PNGs | 1,110 |

These are different units. A box may contain several differences; a collation entry may differ from both witnesses. A resolved original doubt is counted as a recorded certainty decision even where its preferred letters survive. Added uncertainty alone is not counted as a new correction against C. These counts are not witness error rates or a guarantee that every unmarked reading is certain.

The corpus is cote 149 scans 130–136 and cote 150 scans 002, 003, 004, 005, 007, 008, 010, 012, 013, 014, 015, 016, 017, 018, 019, 020, 023 and 024. Scan numbers, author foliation, later thin foliation and H’s page numbering remain distinct.

## Reading the files

| Material | Role |
| --- | --- |
| `pages/<page>.tex` and `SP89_C13_149+150_transcription.tex` | Accepted LaTeX fragments, without a preamble, in the specified page order. |
| `_changes.md` and `_collation.tsv` | C/H readings, accepted readings, crop evidence, coordinates and confidence. `codex_reading` in the TSV means witness C. |
| `decisions.tsv` | All 195 original mark IDs in source order. Here `first` means the mark’s first candidate, not the later fixed first-reader file. |
| `_doubts.md`, `notation.md`, `_inventory.csv` | Notation, unresolved alternatives, abbreviation explanations, comparative legibility and the complete element inventory. |
| `_notes.md`, `CHECK_EVENTS.tsv` | Source accounts and mathematical checks, with their actual hypotheses and limitations. Visual audits are recorded separately in page metadata. |
| `_hand_log.md`, `_sheet_feedback.md` | Local handwriting habits, recurring errors and category counts. |
| `second/` | Fixed box lists, first/second readings, comparisons, root decisions, adjudications and application records. |
| `reports/`, `scripts/`, `progress.log` | Current reports, historical drafts/reviews, protocols, verification receipts and dated progress. |
| `crops/` | Every saved evidence frame, including overlapping and superseded crops. |
| `packaging/`, `MANIFEST.tsv`, `checkpoints.tsv` | Pixel/encoding receipts, archive methods, final entry hashes and checkpoint history. |

Filenames beginning `_` above share the `SP89_C13_149+150` prefix. Paths are relative to the extracted archive. Some historical records retain `work/` or the original workspace prefix.

## Fixed readings and later changes

The first and second TSVs were fixed before their comparison. Their disagreement with the accepted source is intentional and preserves independent provenance. Comparison metadata binds the input files by SHA256. Every one of the 472 nonidentical boxes has a root decision. The accepted source includes those decisions plus narrowly documented encoding and integration repairs.

Historical drafts, first-reading reports and builders remain provenance. **Do not rerun old builders to reconstruct the final edition, or rewrite fixed readings to match the final source.** Source-formatting repairs and metadata synchronizations have separate receipts. The final source freeze records all 25 page files plus the combined fragment in `reports/frozen_transcription.json` and `progress.log`; the subsequent unchanged-hash entry verifies those 26 files. Structural and final audit checks are documented in `reports/structural_verification.json` and `reports/final_verification.json`.

## Crops and extraction

All 1,110 crop paths are preserved. The attached original scans/witness files, prepared half-page images and previous checkpoint ZIPs are excluded as requested. Reading-time rotation, enlargement or contrast adjustment is distinct from later storage encoding.

The final ZIP uses Deflate and **ZIP BZIP2, method 12**. Use an extractor that supports method 12. The decoded images are ordinary PNGs. Some PNGs use uncompressed internal scanlines so that outer BZIP2 compresses them more effectively. The extracted crop PNGs therefore occupy **3,471,374,346 bytes (about 3.47 GB)**.

Every staged crop was compared against its saved reading-time original for dimensions and exact decoded RGBA bytes. The archive verifier binds those staged hashes to the delivered entries. Pixel equality does not mean PNG byte identity, or identity with the source JPEG before reading-time transformations. `packaging/encoding_receipts.jsonl`, `pixel_verification.jsonl`, `pixel_verification_summary.json` and `ZIP_METHODS.tsv` state the original/delivered byte hashes, dimensions, decoded-pixel bindings and per-entry compression method. `MANIFEST.tsv` hashes the delivered bytes. The manifest does not hash itself.

## LaTeX integration and checking limits

Use the original attachment’s `SP89_C13_149+150_texts/PREAMBLE.tex`. A separate driver can contain:

```tex
\\input{../SP89_C13_149+150_texts/PREAMBLE.tex}
\\begin{document}
\\input{SP89_C13_149+150_transcription.tex}
\\end{document}
```

Adjust the path to the supplied preamble. No TeX compilation or rendered-layout verification was performed, as instructed. Static integration repairs group two uncertain mathematical atoms before following superscripts and use explicit ampersand replacement in diagram matrices. Five diagram-environment conversions preserve the accepted objects, literal cells, coordinate strokes and cancellation layers; they introduce no new reading. The detailed source before/after receipts document these repairs. An unreadable mathematical alternative on scan005 is encoded with a mathematical doubt and explained in prose, without using the unreadable-prose macro inside the formula.

The work used direct visual reading, without OCR or external textual research to fill gaps. The mathematical event record certifies only the checks it actually describes; it is not a proof of every manuscript claim.

## Explicit workflow limitations

Several fixed boxes clipped adjacent context or crossed another writing direction. `reports/audit_box_scope_check.md` records how wider saved or native frames resolved those scope issues without altering the fixed comparisons. In particular, **150_scan024 P23** inadvertently duplicates most of P16 and supplied no new reading. It is retained as documentation and is not independent confirmation. P22’s ascender completion is separate.

The final user-facing deliverable is the single archive **`SP89_C13_149+150.zip`**. Its complete-archive hash, extraction/CRC verification and persistence receipt are recorded externally after creation; a ZIP cannot contain a receipt hashing its own final bytes.
'''
(W/'README.md').write_text(readme)
for p in [W/'README.md',*(W/'reports'/n for n in ['legibility.txt','feedback_extra.md','notation_comparison.md','audit_box_scope_check.md'])]:
 assert '{{' not in p.read_text(),p
print(json.dumps(counts,ensure_ascii=False))
