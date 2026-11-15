# Final research review record

The primary reader assembled and checked the research after the transcription freeze of 2026-11-15 17:31:36 UTC. The final notes contain 93 numbered research items, 17 standing unverified-step entries, four title/count entries, the requested four-row comparison table, the standard-conjecture lettering table, the S15 table, and supporting calculations A–E.

## Primary-source checks by the primary reader

The primary reader reopened the cited primary texts after receiving the research contributions. The checked passages include Jannsen pp.447–448, Grothendieck's indexed §3 p.196, Kleiman §§2.3, 2.9 and 3.9, Beauville Theorem 3.3, and Künnemann's indexed introduction p.85 equation (2). For the modern comparisons, the checks include Choudhury–Gallauer Theorem 9.1, Arapura Theorems 6.3.3/6.4.1 and Corollary 6.3.4, Kahn Theorem 5.10 and §10, Deligne–Milne Theorems 4.16–4.17, Proposition 5.8, Proposition 6.17 and Remark 6.19, and Huber's formal evaluation map.

The arithmetic checks include Tate's Honda–Tate exposé, Theorem 1(i) and the cited CM construction; Tate 1966's main Hom theorem; Mochizuki's Theorem A with the sub-p-adic base and geometric-inner-conjugation quotient; Milne's Jacobian comparison; and Milne's decomposition-group Propositions 8.10–8.11. The quadratic-field norm and ideal-class calculations are supplied explicitly in the notes, alongside the LMFDB primary data record. Oda's supplied Corollary 5.11 was checked in text and visually on printed p.131 (PDF page 70), including the submodule/Hodge-sequence identification and the attribution in the following remark.

The reused-text checks include the matching Steinberg paragraphs, the SGA 4 deferred-proof references, SGA 3 VIII 7.10 and 7.13, the Moishezon publication record and Cartier's English-mimeograph bibliography entry. The English projectivity witness remains a provenance lead, with its title page and translator unverified. Ayoub's author PDF was checked at introduction equations (11)–(13) and Theorem 4.4.2/Remark 4.4.3, printed p.234; the presheaf, coefficient spectra and pro-system domains are preserved explicitly.

## Corrections made only to research notes

- Preserved the literal source/target twists m/m′ on scan 111 and attached the common-twist argument to the actual vanishing input on scan 113.
- Specified Ayoub's presheaf and spectral scope, the pro-system used in the introduction, and printed p.234.
- Added the Frobenius inversion/duality calculation, the zero-weight realization, and the negative-weight norm obstruction.
- Restricted the root-integrality claim to the manuscript's integral scalar and supplied the explicit field inclusions and conjugation identities.
- Added the full rational Artin correspondence construction and the remaining comparison triangle with M′.
- Located the later Giraud citation in Deligne–Milne Proposition 5.8 without claiming to have inspected Giraud's section or using its publication date to date the sheet.
- Made the finite cokernels of the integral valuation span explicit on M(2) and M(8).
- Clarified “in odd degree” in the synthesis table to avoid an ambiguity with vector-space dimension.
- Attached the complex embedding locally to the Arapura comparison, the continuity/open-kernel requirement to the Artin construction, and the semilinear representation map to the descent comparison.
- Rendered transcription-only uncertainty macros as literal code or textual alternatives in research quotations, without changing any transcription macro.

## Reproducibility

The research branch records preserve the detailed contributions and their context-search accounts. The main notes are assembled by records/assemble_notes.py, which writes only the notes and their assembly report. It does not write any frozen page or the combined transcription. The page-writing and rebuilding functions in the earlier workflow.py are historical transcription-stage tools and were not invoked after the freeze.

The final hash and package checks are recorded separately in progress.log and final_validation.txt. Mechanical checks establish the reported structure and integrity; the visual reading and transcription judgments are documented in the page audit records and doubts file. The missing TeX distribution prevented a successful compiled rendering, as recorded in mechanical_qa.md.

## Final validator layout correction

The first final run with the optional macro report produced 41 false page-presence warnings because the early validator recognized the old heading `Doubt register` and a cote-number first column, while the final occurrence register uses `Current doubt register` and page filenames. The parser was updated to recognize that exact final layout and verify the filename/scan agreement. The earlier output is retained as final_validation_initial.txt; the corrected run is final_validation.txt. No transcription, inventory, or doubts content was changed by this correction.
