# Checkpoint 16 quality and preservation record

The frozen paper contains **298 statements: 250 Proved, 8 Refuted, 10 Known
and 30 Open**, on **600 pages**. The eleven new statements are A.75--A.79,
C.45--C.47 and D.90--D.92. All 80 lead/task items are mapped. The final PDF
has 3,954,102 bytes and SHA-256
`84d632d01d093a6c28be39fbf7c2e64c46bea2fef85329b93acb54d4377a0ebd`.
The exact registered statement comparison and source hashes are retained.

## Clean build and actual visual inspection

The first full four-pass LuaLaTeX/BibTeX build succeeded. Each of its four
passes has **zero overfull boxes**, so the before and after counts are
both zero and no typesetting repair or second build was required. The
final LaTeX log has zero warnings, zero undefined references and zero
missing characters. Seven existing BibTeX metadata warnings are listed
individually in `notes/checkpoint16_final_build.json`; they concern empty
journal, publisher or year fields and a volume/number combination.

Fifty-nine final pages were rendered and actually opened: 15 by root,
15 by FGH, 15 by DE and 14 by PBC. The disjoint sample covers all eleven
new proofs, changed scope summaries and pages distributed throughout the
paper, including its first and last pages. Images were opened at most two
per result. Every reviewer found the assigned pages readable, without
clipping, overlapping formulas, missing glyphs or margin overflow.

`notes/checkpoint16_visual_review.json` verifies the union of the four
ledgers against the exact rendered-page list and hashes. This is an actual
59-page sample; it is not a claim that every one of the 600 pages was
opened. Every review is tied to the same final PDF hash.

## Frozen sources, bibliography and mathematical audits

All 114 frozen TeX/BibTeX source hashes remain unchanged. The root PDF and
the build PDF are byte-identical. All 148 bibliography entries have a
verified/unverified annotation; 141 entries are used in the paper.
Every newly integrated proof has been read completely by root and by at
least one independent reviewer. Where executable certificates support a
claim, root read and executed them and compared the complete mathematical
output. Separate structural arguments do not claim nonexistent numerical
tests. The A.77 undivided orthogonality refinement preserves the previous
certificate and exact correction. Earlier failed proof routes remain in
the work records.

## Complete history and reversible storage

History is materialized through checkpoint15, accounting for 20267
historical entries using 2961 exact content objects, representing
1,069,537,943 raw object bytes. The index preserves 169 exact restoration
dependencies and individually accounts for three superseded encodings.
A fresh actual restoration verified all 3491 checkpoint15 archive entries
against the saved archive hash. It did not recreate or alter that earlier
immutable ZIP wrapper.

The thirteen existing numerical transforms are unchanged. Four
superseded PDF builds are newly encoded as exact raw-dictionary zstd
deltas against retained final PDFs. Each has two original paths, giving
eight restoration entries. All four standalone decoders were executed
and the entire reconstructed files compared with their originals. The
original 14,254,233 PDF bytes are represented by 246,780 encoded bytes,
their exact retained base PDFs and explicit restoration recipes. No page
content is discarded or rasterized by this representation. The archive
verifier now checks the literal base and payload dependencies as well as
the original hash and count; the previous verifier and exact changes are
retained.

All final and historical review PNGs are preserved by verified byte-exact
regeneration from retained source PDFs. The final storage-plan ledger
records 544 exact image regenerations and 565 total transforms
(13 numerical, eight PDF delta and 544 PNG), and checks every stored
payload hash. Sources, executables, build dependencies and leaf
payloads for the numerical replay recipes remain included. Failed
computations, earlier builds, complete and partial proofs, source checks,
and independent audit notes remain represented in the capture.

The final conservative size forecast is 525,306,227 bytes,
leaving 11,564,685 bytes below the upload limit. It includes
the completed build and QA. Actual archive verification is recorded
separately. The forecast creates no ZIP. Exactly one new
checkpoint ZIP will be captured; its complete CRC, manifest, original
file accounting, history, frozen-source, PDF, review and restoration-input
checks are the final save gates. Its measured byte count must be below
the 536,870,912-byte upload limit.

## Scope and continuation

The paper remains INCOMPLETE. In particular, universal nilpotent
fixedness, descent surjectivity on the symmetric gentle subgroup,
independence of every iterated character, arbitrary rank-two section
images and higher-derived lifting are not declared solved. C.48 and the
next wreath-cover analysis remain notes-only after the source freeze.
The hourly decision is CONTINUE because the eleven new statements make
material progress on the named questions.
