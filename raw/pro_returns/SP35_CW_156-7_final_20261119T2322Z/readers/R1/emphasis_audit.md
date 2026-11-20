# Documentary emphasis audit — gated scans 002–007

**No consolidated decision should automatically receive `diff_H=false` solely as a same-span `emph` → `uline/uuline` conversion.** The 284 decisions currently contain 255 `diff_H=true` entries; this audit makes no automatic numerical reduction.

The style says `emph` represents Grothendieck’s own emphasis and deliberately retains ordinary LaTeX rendering (`grothendieck.sty`, lines45–47). It does not explicitly identify that marker with a physical manuscript underline. `uncertain`, conversely, renders transcriber doubt using `uline` (lines154–155). The supplied CONTRIBUTING file has no additional emphasis/underlining rule.

## Exact decisions needing documentary/category clarification

| ID | Recommended correction; no record edited |
|---|---|
| **004-32** | Keep `diff_H=true`; use **omission**. H already marks *fine* with `emph`; the discrepancy is unmarked *intersection*, not the rendering of *fine*. |
| **005-13** | Keep `diff_H=true`; use **omission**, not deletion-state disagreement. H’s note explicitly describes the older word as underlined and struck (H line164); it does not transcribe the tentative literal reading *éléments*. |
| **005-15** | Correct H’s description to `emph{lieux}` plus its note locating it above an underlined/cancelled word. Do not call the live word explicitly underlined by H. The other placement, punctuation and connector differences keep this row substantive. |
| **005-46** | Describe H literally as `emph{Relation}`, not “underlined Relation.” `kind=other` is suitable. No automatic `diff_H` change: final is plain, so this is not an `emph`/`uline` same-span conversion; documentary evidence alone does not prove an invented physical underline. |
| **006-33** | Likewise describe `emph{Notation}` as authorial emphasis, not as an asserted manuscript underline. Keep the distinction between final plain rendering and the absence of an ink rule explicit. |
| **006-19, 006-23** | Correct “no emphasis marked”: marginal body text is plain, but H line260 explicitly says the marginal notes are underlined. Any retained difference is the exact marked spans/placement, not total omission of the existence of underlining. |
| **005-07** | H marks *déploiement* with `emph`; retain the spelling discrepancy and missing emphasis on the two *strates* occurrences, not a supposed omission on *déploiement*. |
| **005-23** | H emphasizes the entire *Critère d’inclusion des figures par strates*. Preserve the genuine span difference excluding *Critère* in the final, alongside the independent wording differences. |

## Differences that remain substantive

- **002-09** concerns the interlinear insertion of *proprement*; equivalent emphasis markup does not remove the placement difference.
- **004-18** marks *At* alone in the final versus H’s whole *At 0* argument: different extent, not only different macros.
- H genuinely leaves the relevant emphasis unmarked at **004-21**, **004-38**, **005-21**, **005-27** (the labels inside the Scholie), **006-54**, and the *At* component of **007-55**. Partial omissions at **004-32** and **005-07** are specified above.
- **005-50** is punctuation; H’s equivalent emphasis on *figures compatibles* is not a separate discrepancy.
- **007-07**, **007-49**, and **007-55** retain their actual word/arrow/placement differences. H page6 has no `emph` invocation.
- **004-03** records top and bottom bars on VI, not a generic emphasis conversion.

No current decision in these records explicitly turns only on single versus double underline. `emph` does not encode that multiplicity; no number of ink lines has been inferred from it.

All six record hashes were checked before/after writing this finding and remain unchanged. No consolidated TeX was written. No scan009 material was opened during this documentary audit.
