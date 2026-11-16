# Checkpoint 17 quality and preservation record

This record describes the frozen checkpoint-17 paper and the checks completed
before its single hourly archive capture. The hourly decision is **CONTINUE**;
the mathematical work is incomplete. The exact continuation assessment is in
`notes/checkpoint17_hourly_assessment.md`.

## Frozen mathematical scope

The paper has 304 numbered statements: 256 Proved, 8 Refuted, 10 Known and
30 Open. All 27 leads and 53 tasks (80 items) remain mapped. The six newly
registered proved statements are A.80, A.81, C.48, C.49, C.50 and D.93.
There are 117 frozen TeX/Bib source hashes. The bibliography contains 149
entries, of which 142 are used in this paper.

A.80 proves the actual degree-eight genus-two cover and its non-CM Prym
application, with the explicit order-64 wreath closure constructed. A.81
extends the actual double-cover argument and supplies the stated wild
enlargement family. These statements do not assert the still-pending full
genus-17 closure theorem. C.48 proves the sharp derived depth four for the
outer obstruction on the full group. C.49 computes the actual multiplier-one
frames at levels 24 and 60 and proves the precisely stated restriction
consequence for characters on the full group. C.50 constructs an explicit
finite outer detector for the multiplier-one subgroup, with derived length
at most five and only the primes 2 and 3. D.93 gives the all-depth ordinary
finite-kernel Smith decomposition, with the actual maps and norm-extension
calculation. None of these claims settles all remaining open rows.

Each new proof received a complete root review and independent proof review.
The root ledgers are `root_A80_audit`, `root_A81_audit`, `root_C48_audit`,
`root_C49_audit`, `root_C49_full_character_audit`, `root_C50_audit`,
`root_D93_audit` and `root_D93_smith_audit`, in `notes/`. These ledgers
distinguish proof reading, primary-source reading, exact comparison maps,
executed certificates and limitations. The integration verification compares
the canonical proofs and executed outputs against the audited candidates;
all 13 recorded comparisons passed. Numerical certificates were actually
executed. The enormous finite group in C.50 was not enumerated, and no
enumeration is claimed.

Further C.51, D.94 and A.82 work remains in notes during the checkpoint-17
source freeze. Its presence in the complete archive does not register it as
a theorem in the frozen paper.

## Build and visual review

The final PDF has 623 pages and 4,092,498 bytes. Its SHA-256 is
`d86b5f1021fe1030f4e263b81efc0bf4e7f6c29a228291485486bcf204045001`.
The final full four-pass LuaLaTeX/BibTeX build has zero overfull boxes,
zero LaTeX warnings, zero undefined references/citations and zero missing
characters. Seven pre-existing BibTeX metadata warnings remain explicitly
listed in `notes/checkpoint17_final_build.json`; they concern incomplete or
conflicting bibliographical fields, not unresolved citations.

The first build had two distinct overfull boxes, repeated across the four
passes: the C.49 program path by 59.34825 pt, and the D.93 four-congruence
display by 20.6145 pt. The path was made breakable and the display was split
into two aligned lines. There was no mathematical change. The original
sources, PDF, build log, console output, frozen-state records and first
rendered pages are preserved. The exact source changes are recorded in
`notes/checkpoint17_layout_and_preservation.diff`.

Four reviewers actually opened 13 final page images each, for a disjoint
total of 52 sampled pages spread through the 623-page paper. The sample
includes both repaired pages (336 and 567), every new proof interval, the
changed older passages, and the beginning and end of the paper. Every
sampled page passed visual review. This is a 52-page visual sample, not a
claim that all 623 pages were visually inspected. The four individual
ledgers and their exact union are recorded in
`notes/checkpoint17_visual_review.json` and the associated reviewer files.

## Exact historical preservation

The materialized history through checkpoint 16 accounts for 24,074
historical entries, 3,236 unique objects containing 1,083,704,010 raw bytes,
173 exact current restoration dependencies, and three superseded encodings.
An actual checkpoint-16 restoration verified all 3,807 entries. Every one
of the 173 current dependencies was rehashed after the checkpoint-17 decoder
changes and remained unchanged. See the history inventory, materialization
and restoration-test outputs retained in `notes/`.

The final storage plan has 669 reversible transforms: 13 retained numerical
record encodings, eight retained PDF deltas, one new exact PDF delta and
647 exact PNG encodings. Three exact prefix reconstructions are also
retained. The three unmatched old PNGs remain literal files. Complete
mathematical proof records, failed attempts, audit notes, code and logs are
retained or exactly reconstructable; this procedure does not replace any
proof by a summary.

The first checkpoint-17 PDF (4,092,457 original bytes, SHA-256
`6a9cfa1d16d71be5f3ea1e0942e8e38ccb3f3bfe15d518e1a299efe6233fb193`)
has a 32,147-byte exact zstd dictionary delta against the final frozen PDF.
The standalone decoder was executed and its entire output compared with
the original PDF. The PNG decoder now also supports a verified PDF-delta
source when the original PDF is absent. All 647 encoded PNG outputs were
compared byte for byte with their originals. In addition, all 51 superseded
checkpoint-17 page images were actually restored by separate standalone
decoder processes in a minimal fixture in which their original source PDF
was absent; every complete output matched. The exact programs, manifests,
tests and previous decoder/plan versions are retained.

The first size forecast exceeded the 512 MiB upload ceiling. It is retained
alongside the precise lossless correction. The later conservative forecast
was 535,821,087 bytes, including a 1 MiB reserve, below the 536,870,912-byte
ceiling. This is a read-only forecast and did not create a preliminary ZIP.
The final refreshed forecast and the actual single archive's measured size,
hashes, CRCs and dependency checks are recorded separately. Archive
verification and upload outcome are recorded after capture; this
pre-capture note does not claim an upload has already succeeded.

## Reviewable record and next boundary

The report generator will be rerun before capture to incorporate the final
notes and this quality record. Frozen source hashes, statement counts,
status counts, bibliography and PDF identity are checked again before the
single immutable archive is captured. All agent file writers pause during
capture. The scheduled save is 2026-11-16 03:00:00 UTC, under the new name
`LM8_PUSH_checkpoint_17.zip`; no earlier checkpoint is overwritten and no
extra preflight archive is created. Post-capture verification and the actual
save receipt are retained for the following checkpoint.
