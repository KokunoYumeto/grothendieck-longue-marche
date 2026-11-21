# Scan020 — one targeted source-only audit

## Result

Completed the single frozen-source audit with **four bounded current-record editorial findings** below. The selected TeX, exact source mapping, raw provenance, counts, source identities, inventory ownership, and source attachments have no detected integrity error. Root assigns repairs and final approval. This auditor changed only this report and its JSON companion.

## Initial frozen files

| File | SHA-256 |
| --- | --- |
| `out/checks/scan020_final_draft.tex` | `a89fc91245448bbb60370a9a75cc43b28c330f1fbf3563807468c8f528ee4abb` |
| `out/checks/scan020_final_source_map.json` | `2c46fb1e4622952de0a5f1c30abdf1e723d40b41f540b1ba439d9fa628ec0961` |
| `out/checks/scan020_record_draft.json` | `3419e9069dfffc94f6006419ba41457aed92985328bdb262da883b68170ef5ed` |
| `out/checks/scan020_root_graphics.tex` | `96adf87c927e356989b13670dd27a8fecca782c8072c4e460fa133980b1f53e6` |
| `out/checks/scan020_main_decisions.md` | `0929eb98a2fb9945157a0d8ab27b6e7a068eb0e37199d43932c514ec7779c86d` |
| `out/checks/scan020_root_note_selection.md` | `69e0f616d638d77b594fa8af9f7f97995ecd188f6a917c25adc511800bb492fb` |

The separate assembler audit remains unchanged: `out/checks/scan020_assembly_audit.json`, SHA-256 `c297e294357b8882b44344b47d50c50a69e0cd7ec6b6870b7fc60f17d88dc709`.

## Bounded findings requiring root-assigned repair

### QA020-F01 — completed source groups described in future tense

The current public `decisions[].evidence` fields for **L020-07, L020-08, L020-09 and L020-23**, and their four matching `doubts[].reason` fields, retain historical statements that the group or path “will” be supplied or recorded. The frozen draft already contains **R020-G01, R020-G02, R020-G03 and R020-G05**.

Change only these eight current public evidence/reason strings to describe the supplied groups in their current completed state. Keep the root journal and its verbatim source excerpts unchanged. Primary readings, states, alternatives, confidence, counts and selected paths remain unchanged.

### QA020-F02 — L020-31 witness description

The current evidence sentence is:

> Both current witnesses replace the stroke geometry with a formal brace or apparatus description.

Root supplies this precise replacement:

> C supplies a formal overbrace; H describes the upper hatted label and supplies no brace drawing.

The public H field already gives the correct source description. This is one current evidence-string repair; exact historical journal/witness provenance remains unchanged. L020-32 retains root's separate H annotation-placement count.

### QA020-F03 — resolved I described as possible in inventory position

Inventory **020.I22** has `position = "Possible old I beneath union-index K"`. L020-30 and actual C row C020-R08 are resolved, and the selected inventory description already states that resolution.

Root supplies `position = "I predecessor beneath union-index K"`. Change only that current position field; preserve original inventory source descriptions.

### QA020-F04 — root-directed shortening of public notes

The frozen public `notes` string contains 5,603 characters: the root's three substantive paragraphs followed by detailed source bookkeeping. Root requests the three already selected substantive paragraphs as the public notes.

Use the existing `root_selected_content_note.selected_prose` exactly, retain the complete current long notes as record provenance, and retain all structured CONTENT020 entries and exact source attachments. This presentation revision changes no attribution, ink reading, count or selected-source span.

## Verified selected-source coverage

The draft/map portion checked the frozen bytes, 31 contiguous source segments, and all 12 literal replacements. The replacement chain reconstructs the exact draft. All 665 mapped span references resolve, including 483 final-source attachments and 182 raw-source spans.

The 11 complete selected groups match their selected source pieces. All six root groups match the frozen root-graphics file. A020-G02 and A020-G04 retain their point-only boundaries. B_G03 retains its complete union/body/brace/label group with only the authorized resolved old-I/K node replacement. C's complete second figure retains `partie`, the inserted/cancelled `non vide`, `de I` and its comma, with `et` outside. C's complete `rotatebox{23}` margin block is retained. No extra adjoining word or selected drawing-command occurrence was found.

All 36 literal draw/fill commands have exactly one selected inventory owner. This is a source-command ownership result, with no metric, geometry or rendering claim.

The record portion checked 5,019 source-span references, including 755 final attachments and 1,869 JSON-pointer references. All 941 stored raw-value/source pairs checked against their original objects match. All 121 original inventory identities—100 reader rows and 21 actual C rows—map exactly once into the selected inventory's source provenance.

## Counts, physical parents and uncertainty identities

| Item | Frozen result |
| --- | --- |
| Current C changes | 17: high 3, medium 8, low 6 |
| Current H changes | 29: high 13, medium 10, low 6 |
| Public decisions | 42 |
| Selected inventory entries | 32 |
| Remaining local doubts | 19 |
| Actual C doubt rows / parts | 11 / 13 |
| Resolved actual C rows | C020-R08 and C020-R10 |
| Retained actual C rows / parts | 9 / 11 |
| Mathematical check events | 0 |
| Root local successful inspections | 18, from the recorded root audit |

The remaining local doubts preserve eleven actual C parts, four local short-head-role doubts, two detached-point-role doubts, par/p, and the lower E/predecessor-state doubt. R01 retains its three separately identified ring parts. Original pending source decision statuses remain stored separately from selected root outcomes.

The complete positive-Sigma/index H cluster is counted at L020-06; L020-07 has no duplicate H count. The cancelled-Sigma cluster is counted at L020-09; L020-10 retains zero duplicate C/H count. The three H ill placeholders belong to L020-09, L020-23 and L020-35. The existing closure bars at L020-16 and L020-20 each retain C0/H0. The retained-source constraints preserve the distinct union, index, brace, annotation placement, cancelled phrase and guide loci.

All 42 public decisions have complete A/B/C mappings. Raw report mappings remain separate, and report-silent choices have exact complete TeX spans and source references. Public C/H fields match their witness-provenance readings. Every public `marked_in_H` is Boolean and matches the exact H local source or shared-placeholder basis. The allowed collation kinds and required doubt, abbreviation and inventory fields are present.

## Source-only choices, notes and pending approval

L020-01–39 retain ink-choice flags. L020-40–42 retain source-audit flags. L020-16 and L020-20 carry S identity SA01-K81-06 and their actual local ink confirmations; L020-41 carries the separate source-only S coverage record. Its broad source range supplies no additional local selection.

The root note supplement and unchanged CONTENT020 entries retain attributed manuscript statements and exact selected spans, including adjoining prose. No theorem, proof, implication or equivalence was checked by this auditor.

The map's `draft_sha256_utf8` equals the exact draft hash. Final record attachment paths use `checks/scan020_final_draft.tex` relative to `out/`, with the exact corresponding workspace path `out/checks/scan020_final_draft.tex`. The binding convention was checked against approval-script source.

All 175 inspected current selection approval flags remain false, the top draft flags remain false, and the root-approved decision count is zero. Root decision/confidence pending lists are empty because those choices have been supplied. Root separately reports a gate update for current selected nested approval metadata; this auditor neither executed approval nor altered the gate.

## Preservation and audit limits

All 16 released-reader fingerprint files and all 26 supplied source-fingerprint entries matched. The original reader files, C/H/S packets, root journals, selected draft/map/record and assembler audit remain unchanged by this auditor.

The pass used text and JSON sources only. It performed source-offset, hash, identity, literal-component and record-bookkeeping checks. It performed no image operation, OCR, crop, rendering, compilation, research, installation, delegation, coordinate calculation or mathematical check.

Any repair closure should retain these initial hashes and this original audit, identify only the changed current fields, and inspect the narrow repair scope.


## Bounded closure — QA020-F01–F04

**All four findings are closed within the authorized repair scope.** This closure inspected the twelve recorded patches and the specified approval-gate additions; it did not repeat the full source audit.

Initial audit hashes retained as history:

- Markdown: `84cf2b74b6568a49ee36f3b6ad22e15d82838794e37a33792a929c6d0b16d1ec`.
- JSON: `04d4b9fc5563586a47f5f8dafe870eb9afbddd804f74b208dea3045bf3e24c04`.

Initial record SHA-256: `3419e9069dfffc94f6006419ba41457aed92985328bdb262da883b68170ef5ed`.

Repaired record SHA-256: `de18476259203909b279133feba1a5ccb35d6a267c99e2a82be43fd8ec096d9a`.

Exact patch manifest: `out/checks/scan020_bounded_public_repair.json`, SHA-256 `b61161a43655e8528ce96267bc55794abd2b870e5b79818d5fdcd259fcdad2b4`.

### Repair checks

The twelve patches affect eleven current public fields and add one historical-notes object. Their paths exactly match the authorized scope: five decision evidence fields, four matching doubt reasons, I22's position, public notes, and `notes_before_public_concision`.

Reversing the patches **in memory** reconstructs the complete initial record with SHA-256 `3419e9069dfffc94f6006419ba41457aed92985328bdb262da883b68170ef5ed`. This establishes that the record's remainder is unchanged.

The four repaired doubt reasons exactly match their corresponding evidence fields. The completed groups are identified as R020-G01, R020-G02, R020-G03 and R020-G05. L020-31 and inventory 020.I22 contain root's exact replacement wording. Public notes equal the existing 1,653-character `root_selected_content_note.selected_prose`; the full 5,603-character old notes and initial record hash are preserved in the new historical object.

The source hashes remain unchanged:

| File | SHA-256 |
| --- | --- |
| Root graphics | `96adf87c927e356989b13670dd27a8fecca782c8072c4e460fa133980b1f53e6` |
| Selected draft | `a89fc91245448bbb60370a9a75cc43b28c330f1fbf3563807468c8f528ee4abb` |
| Selected map | `2c46fb1e4622952de0a5f1c30abdf1e723d40b41f540b1ba439d9fa628ec0961` |

### Approval-gate source inspection

The inspected `out/scripts/approve_page.py` has SHA-256 `ef0bd10e424bfb55abceeacd4891310af1c8a78fc01cbd3bc72c13a5ae2046b9`. Its bounded additions set the top-level `main_approved` flag and the current selected graphical-group, source-locus-coverage, abbreviation and two attributed/selected-note object flags at approval. These additions target the named current objects; they do not recursively rewrite raw historical approval flags. The existing core approval and attachment-binding logic remains in place. This auditor did not execute the gate.

There is no remaining finding or identified source-integrity risk within this bounded closure. Root approval and the structural commit gate remain root's actions. No manuscript assertion received a mathematical check, and no image, rendering, compilation, OCR or geometry operation was performed. The initial audit content above and its JSON fields remain preserved as history; this closure records the current disposition.
