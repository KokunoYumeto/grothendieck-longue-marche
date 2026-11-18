# Corrections to root research-note locators and documentary attributions

Reviewed `documentation/root_research_items.json`, including the expansion from 73 to 79 items and the added R10, R11, and SF14. This was a comparison with frozen page-file text, context metadata, the doubts register, and the inventory; no scan image was opened and no transcription or draft-note item was edited. The list below contains corrections only.

## Further corrections

| Note | Correction | Exact supporting location |
|---|---|---|
| **SF12** | Replace the comparison's claim that Hua “retains the future tense.” Suggested wording: **“Hua summarizes representability in important cases but does not retain the source's explicit promise of later study.”** The body correctly records the source's future promise and can remain. | Frozen scan 179 L9 says “qui seront étudiés par la suite”; `context/hua_project/57.modern.tex` L2011–2012 instead says that the final Picard object “l'est « dans des cas suffisamment importants »”, in the present tense, without the promise of future study. |
| **P02** | Replace “compresses this warning” by **“stops at the monomorphism step without reproducing the nonfinite-type warning.”** Hua summarizes the proof but does not actually express the source's objection. | Frozen scan 135 L20 gives the warning and the constant-integer-group example. Hua L1719–1727 ends the reduction at “un monomorphisme” and then relates it to the Murre letter; the warning is absent. |
| **R06** | Expand the source locator from **176 L14–23** to **176 L13–23** (or L12–23) so it includes the uncertain marginal quasi-compact/quasi-separated condition discussed in the third sentence. | Frozen scan 176 L13 is `\margin{($X$ supposé \unsure{q.c. qs} sur $S$)}`. L14 is blank; the corollary starts at L15. |
| **C04** | Change **149 L8** to **149 L9** in the locator. | Frozen scan 149 L8 is blank. L9 contains “partie additive”; the remaining L20–23 and 151 L38 references are usable. |
| **R07, SF08** | Start the Hua projective-section reference at **L1859**, not L1854. When naming the section, use **“Plongements projectifs et foncteur de Picard (pages 156 à 163)”**, L1859–1895. | Hua L1854–1856 still belongs to the preceding **“Courbes stables (pages 152 et 154)”** footnote. L1858 is a `\pagerange` command; the projective section's actual heading is L1859. |

For the requested exact-title convention, **D02 and D03** currently use the descriptive label “projective-morphism subsection”; replace it with the same actual heading, **“Plongements projectifs et foncteur de Picard (pages 156 à 163)”**, retaining the narrower L1885–1895 passage citation. This is a heading-precision change, not a change of the cited mathematical topic. D01 already has the correct title; its range may likewise begin at L1859 if the heading itself is being cited.

## Corrections already sent during the review

These are recorded here so the report retains the complete correction list; some were already incorporated into the live JSON while the review continued.

| Note | Correction | Exact supporting location |
|---|---|---|
| **R02** | Replace **147 L30–58** with **147 L30–54**. | The frozen scan-147 file has 55 lines; the outer deleted block closes at L54. The equation is at L34 and the outer deletion begins at L37. |
| **T08** | Use **134 L42**, not L46, for the Čech heading. Drop **161 L7**, retaining L17 for the cited proposition label. Suggested locator: **134 L42; 154 L11; 159 L12; 161 L17**. | At scan 134, L42 is “2. Cohomologie de Cech d'un recouvrement ouvert”; L46 is the displayed definition of M. At scan 161, L7 continues the preceding set-theoretic sentence, while L17 contains Corollaire (1.1.5). |
| **T05** | Replace “references to Chapters II/III” by **“references to Chapter III and the numbered sections”** or similarly precise wording. | Frozen scan 163 L26 explicitly names Chapter III and its §3; it refers generally to “chapitres suivants” but does not explicitly name Chapter II. The ten-section count is a section count, not a page total. |
| **T09** | Remove the attribution **“README cautions against dating packets by order.”** Keep the chronological limitation as the note's own documentary conclusion, or attribute only the actual broad catalogue description to the README. | Neither `context/README.md` nor `context/hua_project/README.md` states that warning. The former provides broad catalogue dates and warns that contextual guesses are leads; the later-package notes supply analogous documentary cautions, but that is a different source. |

All references to Hua in this report are to `context/hua_project/57.modern.tex`. “Frozen scan N Lx” means line x of `pages/MPL_57_133-179_57_scanNNN.tex`. This report proposes no alteration to those files.
