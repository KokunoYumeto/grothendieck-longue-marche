# Administrative record audit — 156-4 scan 071

Text-only audit of C.tex, H.tex, all 25 scan-071 C_context rows, brief v07, and the three final reader reports/transcriptions. No images were opened; no ink, mathematical, OCR, or compilation decisions were made here. Root decisions control the draft records.

## Coverage and schema

- All five H unreadable placeholders are covered: Donnons/nous (R1-D04, R2-04, R3-D04); the adjacent pair before une sous- (R1-D12, R2-13, R3-D13); the inverted parenthesis (R1-D33, R2-32, R3-D33); and the single internal-deletion placeholder covering two crossed groups (R1-D45, R2-36, R3-D39). The adjacent pair and the single deleted placeholder must each retain their correct scope.
- Every one of C's 22 unsure occurrences has a disposition, including both margin groups, both folio layers, the nested lower-folio doubt, and both internal deleted groups. All 25 explicit context rows are covered, including plain equals signs, the first straight order, family/Phi/inclusion, final i/I and possible stop, struck toute, and muni.
- The final reports have required fields, valid enums and JSON booleans; IDs are unique, all referenced crop paths exist, and all three finished_utc fields are populated. Required reading/check data are present. check_events is empty in all three.
- Remaining-doubt readings match each reader's text, allowing explicit figure references. R2's named punctuation reference is descriptive rather than a literal excerpt, but points to its actual doubtful TikZ group.

## Normalizations for consolidated records

1. H's folio notes are editorial excerpts. Use marked_in_h=yes for the folio qualifications; do not count their prose as omitted manuscript text. R1/R3 used no, whereas R2 used yes.
2. Root explicitly confirms that preccurlyeq and preceq are equivalent encodings here. Retain change_h=false for that sign; explain the equivalence outside counted differences.
3. R2-28 joins two noncontiguous source snippets with a synthetic semicolon. Retain R1's separate first-ens and later-l'ens rows. R2-08 and R3-D39 reconstruct prose distributed across nodes; use exact node excerpts or clearly named figure references.
4. Rows whose neighbouring labels differ need explicit narrow scopes: state of de versus inserted-F alphabet; quotation strokes versus F alphabet/accent; Dém lettering versus its stop; insertion arm/high itou stroke versus nearby words. Do not count graphic labels again as text.
5. R3 records paragraph boundaries that R1/R2 did not separately collate. Layout rows must compare paragraphing only. The root's temporary suspicion about the Donnons paragraph was withdrawn: C literally has a blank line, all readers preserve it, and root restored it.

## Reader disagreements requiring the supplied root decisions

| Locus | R1 | R2 | R3 |
| --- | --- | --- | --- |
| de under addition | Deleted | Deleted | Live/deleted uncertainty |
| Inserted F | F/calligraphic F doubt | Certain calligraphic F | Calligraphic F/F doubt |
| seult | seult/seulemt doubt | Same | seult resolved |
| itou | Uncertain itou | itou/itout plus drawn high mark | Uncertain itou |
| saturée accent | saturee/saturée | Same | saturée |
| Edge punctuation | Character alternatives | Doubtful drawing | Drawing with identities open |
| Reference word | page/pge | page | page |
| Worked Phi | Possible older F or mere retracing | Same, Phi first | Earlier F layer asserted |
| un after Phi | Resolved | Retained doubt | Resolved |
| inclusion comma | Doubt; crop limitation disclosed | Doubt | Resolved |
| Application terminal | Capped/mapsto doubt | Capped resolved | Capped resolved |
| Second inner deletion | p/par | p/par | par/p |
| Dém | Uncertain Dém | Dém/Dire | Dém resolved |
| Draft geometry | Boundary and 13 drawn cancellations | Drawn rotated block | Separator and ordinary deletion macros |
| Three detached points | Not separately represented | Not separately represented | One high and two low points drawn |

All readers broadly cancel the lower folio and serialize the underlying digit beside its successor. Root specifically supersedes both choices: two positions, an overprinted second digit, no broad folio cancellation. Root also requires the worked Phi's candidate layers to occupy one position.

## Evidence coverage

The audit caught a real gap at the later family F after objet G: its original-image bbox [385,730,450,810] was outside every then-viewed root crop. Root created and viewed a03_de_family_F.jpg and confirmed calligraphic F. The final allowed evidence set is 23 existing reader crops plus three new root crops. No unrelated crop is to be attached to that occurrence.

## Draft record assembly

The root-authorized builder is scripts/decide_071_records.py; its output is decisions/156-4_071.json. These remain draft records for root review. The builder preserves the final page and original reader files, uses only root-viewed crops for counted differences, retains independent reading disputes, and leaves check_events empty.

The written draft contains 56 difference loci (20 against C and 53 against H), 29 C dispositions covering all 22 unsure occurrences and 25 context rows, 18 reader/root disputes, 18 remaining doubts, and 31 inventory elements. It also maps each of H's five placeholders explicitly to its single appropriate difference row. Required enums, boolean types, exact C/H/final excerpts or final figure-reference comments, final doubt excerpts, and the evidence allowlist pass the builder's text-only consistency checks.
