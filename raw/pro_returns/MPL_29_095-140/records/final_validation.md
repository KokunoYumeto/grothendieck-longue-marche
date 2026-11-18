# Final validation — MPL_29_095-140

Report written 2026-11-18 06:43:48 UTC.

## Source and transcription boundary

The supplied manifest governs the 31-page scope: scans 095–101, 103–112, 117–118, 124, 126, 129–133, 135, and 137–140 of cote 29. The prompt's isolated “46 pages” does not match the supplied manifest. No omitted earlier-run scan has been added.

All source images were read by the root reader in one sequential stream, without OCR or parallel image readers. The second visual audit and notation reconciliation preceded the freeze at 2026-11-18 06:04:22 UTC. Context was opened at 06:04:34 UTC. Subsequent research agents used the frozen text and textual context only.

The final hash verification recorded in `progress.log` found **all 32 SHA-256 values unchanged**: 31 individual page files and their exact combined fragment. The complete frozen digest list is `records/transcription_hashes.json`.

## Mechanical validation

The final run of `records/check_mechanical.py --final --compile` returned:

- 31 of 31 expected individual page fragments, in the specified order.
- 521 inventory elements, all marked transcribed.
- 31 sequential completion entries and all required audit entries.
- Exact byte concatenation of individual fragments into the combined transcription.
- Valid checked braces, environments, allowed structural conventions, and inventory metadata.
- Successful temporary pdfLaTeX syntax compilation, exit code 0, with 0 overfull-box warnings.

The compile wrapper used a temporary local format from installed sources. Its PDF is a syntax-check intermediate and is not included in the deliverable. Compilation is separate from, and does not replace, the completed visual audits against the scans.

## Research validation

The finished register contains **56 notes**, with one-to-four-sentence bodies, allowed kinds, source witnesses, brief source words, contextual relations, and applicable RESULTS_STATE links. All 14 own ideas have a confidence assessment and reason. Both standing questions have their own sections.

There are **261 recorded fixed-string context searches**, **47 mathematical check events**, and **nine explicitly defined refinement IDs**. The check-event schema is `statement_id,date,who,type,outcome`; the effort setting is honestly recorded as not exposed. An event under `29-formal-tame-pi1-self-intersection` targets only the unrestricted centrality clause, not the whole geometric theorem.

The independent final register review confirmed 56 sequential IDs, matching Markdown/JSON bodies, 47 valid event rows, all nine refinements, all 22 local links, and all 24 proof references. Detailed reports are `records/review_notes_register_final.md`, `records/review_local_checks.md`, and `records/review_torsor_checks.md`.

The check proofs retain their limits: the cusp example targets the declared repaired broad minimality assertion; the gluing example targets Cartesian local data without the appropriate geometric neighborhood control; neither is advertised as a full sufficiency theorem. The field-extension comparison distinguishes conditions and does not resolve uncertain source words. The full exact-functor, pro-representability, formal-inertia, and local-monodromy programmes remain outside the proved scope.

## Packaging

The final archive includes all deliverables and current work records, scripts, supporting arguments, reviews, and logs. Supplied scans, attached ZIPs, full context source files, temporary rendered files, and earlier checkpoint archives are excluded. The archive helper performs a full ZIP CRC check before reporting completion; the final archive is also checked for the required members and exact frozen TeX bytes.
