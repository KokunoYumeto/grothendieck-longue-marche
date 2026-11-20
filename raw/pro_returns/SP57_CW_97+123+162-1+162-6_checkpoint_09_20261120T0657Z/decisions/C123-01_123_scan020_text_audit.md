# C123-01_123_scan020: text-only apparatus audit

## Scope and result

Compared the complete C and H witnesses, all three complete `reading.tex` returns, all three complete `report.json` returns, and the conventions/v08 brief. No image, OCR, web source, other page's text, or mathematical reconstruction was used. Statements about source appearance below are the readers' reported evidence, not independent visual findings.

The planned hybrid has **17 distinct substantive witness-difference loci**: R2's 16 loci plus R3 D16, the marginal layout. R1 has 15 difference rows, R2 16, and R3 16. No further substantive witness-difference locus was found after the v08 macro-only exclusions. These are reading/apparatus loci, not 17 demonstrated errors in H.

## Omissions and differences needing explicit treatment

| Locus | Complete-return comparison | Apparatus consequence | Macro-only? |
|---|---|---|---|
| Slanted marginal layout | R1 and R3 retain five rows and the separate `ex` placement; R2 flattens the words and records slant only in a comment. R1 anchors beside `un Borel` with `\reversemarginpar`; R3 supplies the more detailed staggered layout. | The geometry already present in R1's text is missing from R1's differences. It is also absent from R2's differences. R3 D16 supplies the required additional locus for the hybrid. Root's announced left-margin anchoring resolves the placement difference. | No: physical layout. |
| Marginal `unipotents` | R2 marks the word uncertain; R1 and R3 give it without doubt. | R2-14 records this substantive confidence difference. Preserve its doubt when moving the words into R3's layout. R3's lack of this row agrees with its own confident text; it must not remove the row from the hybrid. | No: uncertainty state. |
| Cancelled `de` | R1 has `\deleted{d\unsure{e}}`; R2 and R3 have `\deleted{de}`. | Covered by R1-04/R2-04/R3 D04. Root has separately resolved `de`; this audit makes no glyph decision. No additional locus. | No: uncertainty state. |
| Final marginal noun | R1 retains capital-first `Borels`/`borels`; R2 and R3 use lowercase-first `borels`/`Borels`. | Covered by R1-15/R2-16/R3 D15. Preserve the announced lowercase-first candidate order in the hybrid. | No: preferred reading. |
| Two middle cells of `principale` | R1 overlays whole `pa` and `ap` pairs; R2 lays out four letters in two cells; R3 uses two separate overlay pictures. R1/R2 limit `\unsure` to the mixed cells; R3 wraps the whole word. | All reports cover the overprints. The narrower uncertainty boundary in the chosen R2 text should remain explicit; the chronological order remains unresolved. This is variation within one existing locus. | Geometry/uncertainty differences are not mere equivalent macros. |
| Final `la` | R1's `\unsure` includes the following `a`; R2/R3 leave `a` outside it. R3 draws the additional short upper-right trace and high point, as well as loops and lower extensions. | Original R2-12 has an **empty `reading` value**. The saved root spec supplies a nonempty `final` override; its preview contains the adopted R3 drawing plus definite `a`, with corresponding evidence and remaining doubt. R1's broader word-level doubt is not inherited. | No: graphical content and uncertainty scope. |
| Raised `ceux` and connected leader | R1/R3 include `de la forme` in the baseline node; R2 includes only `de` and continues `la forme` afterward. All preserve the same words and a connected unheaded curve, with different geometric approximations. | Covered by each reader's first difference. R2's selected representation requires no new locus. Do not count each coordinate or node grouping as a separate correction. | Node grouping is encoding; the represented curve is substantive and already counted. |

## Explicit exclusions

Under v08, H's `\emph` for the two `par` occurrences and marginal `ex` can represent source underlining. Missing `\handwritten` wrappers in H's different macro system do not establish a contradictory medium. Those are **macro-only** differences and require no additional collation rows. The `Cas principal` bold-versus-rule difference is substantive and already recorded.

Equivalent `\add`/`\inserted`, `\struck`/`\deleted`, `\marginal`/`\margin`, `\mathrm`/`\operatorname`, colon spacing, and math-mode grouping around the two marginal A expressions add no loci. H's page 19 versus scan 20/archive-comment 19 follows the stated numbering convention. Its editorial expectation before `(1)=0` is not source text to import. The physical blank versus H's explicit illegibility marker is already a substantive reported locus.

## Combined inventory

R1 inventories 26 elements, R2 21, and R3 33. R3's **33-row inventory covers every distinct element retained in the announced hybrid**: both body blocks, raised typed insertion, separate curved leader, individual handwritten formula fills, underlines, internal punctuation, both blanks, three cancelled fragments/qualifications, both mixed `principale` cells, typed indices/operators, the final mixed cell, marginal example and its separate `ex` underline, and archive number.

R2's fewer rows aggregate several formula fills and leave the condition blank, `Z_o`, `Dyn_c`, and the `ex` rule within broader rows. These are inventory-granularity gaps, not missing text. Adopting R3's full inventory closes them without inventing extra source elements. Preserve R2's marginal `unipotents` doubt in the combined text, difference row, and remaining-doubts list; retain lowercase-first `borels`/`Borels`. The detailed final-cell description may be incorporated in its existing R3 inventory row rather than inventing a separate item for every stroke.

## Saved root spec and preview

The saved spec's single text replacement matches the R2 source once and reproduces the saved preview exactly. Its union has 17 unique difference identifiers; all 33 R3 inventory element names are present, with every item marked transcribed. The preview retains the local `principale` doubt, the R3 final-cell drawing with definite following `a`, both blanks, deleted `de`, typed `Z_o`, and the five-row left-margin arrangement beside the Borel clause. The margin retains uncertain `unipotents` and lowercase-first `borels`/`Borels`. The six remaining doubts agree with these choices. No material mismatch remains in the checked spec/preview.

No reader or final-page file was changed by this audit.
