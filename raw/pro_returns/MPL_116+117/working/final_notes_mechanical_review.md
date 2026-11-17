# Final research-notes mechanical review

Reviewed 2026-11-17 18:53:57 UTC. Input: `MPL_116+117_notes.md` (946 lines).

## Result

PASS: all requested mechanical checks succeeded.

- **255 rendered DSS rows** occur exactly once and in catalogue/source order.
- Every rendered DSS source cell matches the generated exact catalogue value: status, DSS source line, original manuscript locator, and the same-ID RS line where present.
- All **16 absent source locators** are explicitly rendered as `(no manuscript locator supplied)`; none has been reconstructed.
- **15 NR headings** are present in order: NR01–NR12 and NRK1–NRK3. Their source-line metadata matches NEW_RESULTS lines 18–29 and 31–33.
- **44 N-items, 5 Q-items and 13 R-items** are defined once each. All explicit references and intermediate references in same-prefix ranges resolve.
- All **22 Markdown tables** have consistent column counts using an escape-aware pipe parser. No broken table escaping was detected.
- Every heading now has a following blank line; table blocks are separated from following content.

## Context-source metadata

- All **25 named structured RS ID references** in O-items point to their actual source lines.
- The two Hua findings-register entries are verified at **RS 523 and 524**, respectively.
- O09 correctly cites REVERSIBLE_LOCALIZERS F.1 at RS 103–106. H01 now cites RS **37–110**, including the S2COUNT intake qualification on line 110.
- O18 separately identifies GALOIS B.14 at RS 433; O03’s accessibility item identifies GALOIS B.13 at RS 419.
- All **14 explicit Hua file/line ranges** are in bounds and fall in the named sections (the section labels were checked against the source headings). R10’s 393–419 range includes the modern adjunction reference; R11 cites the crossed-conclusion comment at line 419; H02’s 432–440 range includes the all-localizer assertion and its “cité de mémoire” qualification.
- The renderer reads source statuses from `context_catalog.json` by exact ID and preserves the literal `claim (return: ...)` language; inspection confirms no status is inferred from the new comparison’s note kind.

## Corrections verified

- The previously reported H01 source-range endpoint was extended from 109 to 110.
- The assembler now inserts blank lines after headings; the rebuilt notes contain no remaining heading-spacing violation.

## Scope

- This is a mechanical coverage, reference and rendering review. It does not verify manuscript readings, source quotations against scans, mathematical claims, or priority.
- No images, page fragments or combined frozen transcription were read or changed. No research-note or comparison content was edited.
- Context keyword searches are discovery aids, not proofs of occurrence or absence; the root’s scan comparisons remain separate from this mechanical review.

## Reviewed input hash

`MPL_116+117_notes.md`: `690d6db22d63200688a65ae6e8d3ce87bd3dd4fd5fb93ae1ffa18715df00d6f6`
