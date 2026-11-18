# Notation table and reading doubts

## Package notation table

This table records the primary reader's comparison of recurring signs before the transcription was frozen and before the context archive was opened. A shared doubt is kept shared; resemblance of mathematical roles was not used to identify two different shapes. TeX grouping braces and math-mode delimiters are editorial typesetting syntax, not extra manuscript content.

| Written sign or convention | LaTeX treatment | Comparison and remaining caution |
|---|---|---|
| Plain Latin category and object letters | `C`, `E`, `F`, `G`, `H`, `K`, `P`, `S`, `T`, `X`, `Y`, with the visible case | A curved or quickly written capital is not automatically made calligraphic; case and alphabet doubts remain local. |
| Calligraphic category and sheaf letters | `\mathcal C`, `\mathcal E`, `\mathcal P`, `\mathcal O` | Kept distinct from plain capitals where the script stroke is visible; particularly the categorical pages 159–161 and the sheaf pages. |
| Crossed-out Gothic group-category name | `\mathfrak{G}`, locally `\unsure{\mathfrak{G}}` | Scan 141; the cancelled occurrence is less secure than the following one. |
| Looped descending torsor-functor name | `\unsure{\mathfrak{Z}}` | All occurrences on 141 and 143 were compared directly. The alphabet/name remains unresolved; the same tentative Gothic Z is used throughout those pages. |
| Barred and crossed Gothic F-shaped letter | `\mathfrak F` / `\mathfrak{F}` | Scan 152 has a visibly different shape from the looped symbol on 141/143. These were compared again before freeze and were not conflated. |
| Small looped symbol in group formulas | `\unsure{\mathfrak z|\zeta}` | Repeated on 177; the same ordered alternatives are kept, including inside Hom and arrow targets. |
| Raised `gr` on Hom | `\operatorname{Hom}^{\mathrm{gr}}` | Scan 141: an abbreviation in the exponent, not a prime. |
| Underlined Hom and sheaf letters | `\underline{\operatorname{Hom}}`, `\underline A` | The underline is retained; a proposed alternate script alphabet is not substituted. |
| Lowercase fundamental-group and component signs | `\pi_1`, `\pi_0` | Kept distinct from uppercase Pi, including the repeated component and simplicial formulas on 179–186. |
| Uppercase Pi, superscript/subscript 1 | `\Pi^1`, `\Pi_1` | The location of 1 follows the ink, not an imposed convention for group versus torsor functor. |
| Large title on 175 | `\unsure{\pi_2|\Pi_2}` | Size alone does not settle case; the doubt survives comparison. |
| Replaced functor name on 165–170 | `\Pi^1` and `\Phi`, with struck predecessors inside `\deleted` | The live round Phi on 166–169 differs visibly from Pi on 165/170. Revision is retained instead of harmonizing the entire section. |
| Tilde and bar over letters/groups | `\widetilde{...}`, `\overline{...}` | Checked separately from primes and show-through. Later unbarred or untilde occurrences are not silently supplied with the earlier mark. |
| Pointing letter in torsor formulas | `\xi` where clear | Distinct from the provisional Gothic functor letter; the point in the diagram on 181 has a clear xi-like form. |
| Pointing letter on 185–186 | `\unsure{\zeta|\xi}`, and the corresponding powers | Compared together: the single upper loop and long descender favour zeta, but the alphabet remains uncertain. All live occurrences use the same ordered alternatives. |
| Greek parameters and arrows' labels | `\alpha`, `\beta`, `\gamma`, `\lambda`, `\varphi`, etc., with local doubts | Labels are read separately from objects; examples of unresolved forms include Lambda/A on 145 and S/delta on 172. |
| Primes, double primes and triple primes | `'`, `''`, `'''` | Kept separately from superscript circles, powers and punctuation. Unclear primes on 142, 147, 177 and 187 remain marked. |
| Circle-like superscripts | `^\circ`, `^{(0)}`, `^0`, according to visible placement | Not all are read as a numeral zero. Scan 170's small circle and scan 168's different forms are retained. |
| Stars and their positions | `_*`, `^*`, `u_*(\alpha)` | Subscripts and superscripts are not interchanged; especially the simplicial indices on 179–186. |
| Ambiguous degree on 176 | `\unsure{I|2}`, `\unsure{2|1}`, as locally written | No cohomological degree is supplied from what a spectral sequence would normally require. |
| E/F discrepancies | The visible `E` or `F`, or `\unsure{E|F}` in context | In particular, `E_S` on 169 and the final `E` in both functors on 186 are retained; scan 158's final expression remains E/F uncertain. |
| Directed inverse and direct limits | `\varprojlim`, `\varinjlim` | Used where a direction is actually visible, rather than inferred from the argument. |
| Limit with a plain underline | `\underline{\lim}`, sometimes with an index below | Scan 176 was rechecked: several lower strokes have no arrowhead, unlike the explicit direct-limit arrow in the upper H² chain. |
| Plain connecting strokes | `-`, `\mathbin{-}`, or TikZ `dash` | A morphism is not given an arrowhead merely because it is a morphism. Headless strokes remain on 142, 145, 151, 153, 157, 159, 162, 181 and 187. |
| Parallel diagram arrows | Separate shifted TikZ arrows | Arrow number, direction, headlessness and labels follow the image; the simplicial diagrams retain two and three separate arrows. |
| Equality-like shorthand in prose | Literal `$=$` | For example `de = de` on 156, `des =` on 185, and the signs around the question on 180. Not expanded to a French word. |
| Double quotation marks | Two backticks and two apostrophes | Used for manuscript quotation marks. A ditto mark in the component diagram on 181 is retained as a separate pair of strokes. |
| Underlining | `\uline`, `\uuline`, or ordinary math `\underline` | Separate underlined words are not merged automatically; the double underline on `ponctué` on 186 is retained. |
| Strikes and insertions | `\deleted{...}`, `\inserted{...}` | An insertion follows its caret/connecting stroke where recoverable; a crossed readable word is never made live merely because it completes the sentence. |
| Circles and transposition strokes | TikZ inside `\figure` | The circle around `universels` on 160 and the circled inserted `loc` on 180 are retained, as are the free drawings on 176, 183 and 184. |

## How to use the doubt tables

The current-doubt table below is generated from the final page fragments, so its readings agree with the frozen transcription. It distinguishes the preferred reading from any alternative inside the macro; a single tentative reading does not imply that no other reading is possible. Confidence is deliberately conservative, and **low** means that the ink does not support a confident identification, not that an alternative has been proved correct.

The line locators refer to physical lines of the individual TeX page fragment, **not to a claimed count of handwritten lines**: paragraphs were reflowed as the prompt permits. The scan number and local text identify the corresponding place on the image; selected difficult loci are described more precisely after the table. The auxiliary `doubts_rows.tsv` and `audit_changes.tsv` preserve the reading history, including superseded first-pass proposals; they are not competing final transcriptions.

