# Checkpoint15 quality and preservation record

The frozen paper contains **287 statements: 239 Proved, 8 Refuted,
10 Known and 30 Open**, on **566 pages**. The ten newly integrated statements
are A.70--A.74, C.44 and D.86--D.89. All 80 lead/task items remain mapped.
The exact statement/source comparison is retained separately. The final PDF
has 3,752,460 bytes and SHA-256
`d9e922269fb665cf7d799408f2a03a65a139dfab860c54cb7386ad80c3c55f75`.

## Build inspection and repair

The first four-pass build had one unique overfull display, repeated in
each of the four passes: D.86.4 on page500, protruding by 53.49773pt.
Root rendered and actually inspected the affected page. The displayed
definitions were split across three lines without changing their mathematics.
The entire first PDF, build log, console output, bibliography log, affected
source, source hashes, diagnostics and overflow image are retained in
`notes/checkpoint15_build_attempt1/`.

The corrected source was frozen again, and a complete second four-pass
LuaLaTeX/BibTeX build was executed. **Every pass has zero overfull boxes.**
The final LaTeX log has zero warnings, zero undefined references and zero
missing characters. The seven existing BibTeX metadata warnings remain
explicitly listed in `notes/checkpoint15_final_build.json`; they concern
empty journal/publisher/year fields and one volume/number combination.
No new build was needed after the final actual page review.

## Actual visual review

Sixty-one final pages were rendered and actually opened. The disjoint
reviews cover 15 root pages, 15 FGH pages, 17 DE pages and 14 PBC pages.
They include the repaired page500, samples across every newly integrated
proof, the corrected scope summaries and pages distributed throughout the
whole paper, ending with page566. All reviewers found the pages readable,
with no clipped formulas, collisions or missing glyphs. Root's earlier
five-image call was truncated and was not counted: all assigned images
were then reopened in calls containing at most two images.

`notes/checkpoint15_visual_review.json` assembles the exact page list and
the four individual ledgers. Every PDF and PNG hash is checked against the
final frozen version. This is an actual 61-page visual sample, not a claim
that every one of the 566 pages was opened.

## Source, bibliography and register integrity

All 106 frozen TeX/BibTeX source hashes remain unchanged. The delivered
root PDF is byte-identical to the final build PDF. All 147 bibliography
entries carry a verified/unverified annotation, and 140 entries are used.
Each new mathematical proof has a full root audit and an independent
audit. Executable certificates were rerun and their mathematical outputs
compared; structural proofs are identified as such. No unexecuted numerical
claim was substituted for a proof or a certificate.

## Complete history and reversible storage

History through checkpoint14 accounts for all 16,776 historical entries
using 2,694 exact content objects, representing 1,039,470,304 raw object
bytes, with 169 exact restoration dependencies and three individually
accounted superseded encodings. A fresh actual restoration verified all
3,175 checkpoint14 entries against the saved archive hash. It did not
recreate or alter the earlier immutable ZIP wrapper.

The checkpoint15 storage plan preserves exactly the same thirteen
non-PNG transforms and supplies 485 verified, byte-exact PNG restorations,
for 498 transforms altogether. Its three exact prefix reconstructions and
seven replay recipes retain the necessary original sources, executables,
build dependencies and leaf payloads. All recorded stored-payload hashes
were verified. The unchanged numerical traces, failed approaches, earlier
builds, source checks and independent audits remain represented.

The read-only conservative size forecast is 530,425,138 bytes before a
discretionary future-work reserve, below the 536,870,912-byte upload limit.
The final build and all final QA images are already included in that
forecast. Adding an unnecessary eight-MiB future-work reserve would exceed
the limit, so no such additional work payload is planned before capture.
The actual archive byte count and every manifest/hash/restoration-input
check are to be recorded by the complete post-capture verifier. The
forecast itself created no ZIP.

## Scope of the frozen checkpoint and next work

The registered paper remains incomplete. The universal fixed-element
problem, full descent surjectivity and general section classifications
are not declared solved. Later A.75, A.76, C.45 and D.90 candidates and
the middle-valuation calculation remain explicitly in notes and outside
this frozen paper. Their stronger partial conclusions are being audited
before any later canonical integration. The hourly assessment is CONTINUE
because the named main questions have made substantive progress.
