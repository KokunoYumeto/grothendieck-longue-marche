# Scan024 source coverage QA

Scope: clerical coverage and canonical identities, before assembled draft release. Images opened: 0. Ink and mathematics decisions: none.

## Results

- Exact text references replayed: 3253 (source_union: 1782, candidate_crosswalk: 207, inventory_crosswalk: 132, typed_skeleton: 1132).
- Mechanical reference/identity errors: 0.
- Root journal: 30 sections, with 30 once-viewed crop references consistent with the crop audit.
- Source loci: 64; 61 carry root section references. All 161 raw reader differences and all 88 raw reader doubts have journal coverage.
- Complete candidate/state groups: 69 (A 22, B 25, C 22); inventory identities: 132 (A 49, B 39, C 44).
- Original C rows: all 18 parents retained, including the two index occurrences in R02, accent/punctuation scope in R09, and first-U target of R13.

## Findings

### QA024-I01 — coverage_recorded

All 161 raw difference records and all 88 raw doubts have their original own-reader identity in the typed source index and a mapped root journal section.

Source: `out/checks/scan024_source_union_v01.json#/source_locus_union`.

### QA024-I02 — source_only_unmapped_context

These three loci have no dedicated root crop section. Complete A/B/C sources were inspected; their literal core defining RHS, lemma lead-in and first exactly-two passage are present. No raw difference or doubt record is attached to these three loci. Preserve them as complete consensus context in source coverage, without inventing another crop or proof event.

Source: `out/checks/scan024_source_row_skeleton_v01.json#/rows`.

### QA024-I03 — canonical_parent_scopes_preserved

R02 keeps both index occurrences at L03/L04; R09 keeps noun/accent L25 and endpoint L26 under its original parent; R13 is the first-U sign at L47 and only contextual at L52. Root literal outcomes record two resolved rows, fifteen retained rows, and one mixed row (R09).

Source: `out/checks/scan024_root_decisions.json#/decisions`.

### QA024-I04 — own_candidate_scopes_preserved_in_typed_index

All 69 complete own groups and every copied raw candidate/state leaf match their own exact source references. The final assembled public fields have not yet been released for this audit.

Source: `out/checks/scan024_source_row_skeleton_v01.json#/complete_own_group_candidate_scopes`.

### QA024-I05 — local_H_scope_preserved

The sole H ill marker is attached to L56, the right-edge word preceding definit. Its marker does not attach to the verb or adjoining formulas.

Source: `out/checks/scan024_H_marker_catalog.json#/markers/0`.

### QA024-I06 — source_only_S_scope

S catalog has zero direct scan024 reading rows and seven recorded source row scopes. Its source-only review remains outside the crop journal's local ink decisions.

Source: `out/checks/scan024_S_scope.json`.

## Audit bindings

Root journal SHA-256: `e409def8a84a5684e7f8505b758d886707b295a63af779b6e9e3cf75839d5e5f`.

Source union SHA-256: `c933d2361514761da9d136ec31c2427dce502e968dfca43b61786d6f01b7fea0`.

Typed skeleton SHA-256: `5aa8cd3afdd1106771a587b0888acb68feca1a5a52f766aab46eae64880cf839`.

The JSON companion retains every locus-to-section mapping, all 69 exact candidate-source pointers, original C row outcomes, input hashes, and reference replay counts. The source originals, frozen source index and root authorities remain unchanged.
