# Notation table

This table was maintained from the first page and completed by a comparison of recurring forms against the scans before the transcription was frozen. It records visible forms, not a normalization to an expected mathematical statement; uncertainty remains explicit in the page files.

| Recurring visible form | LaTeX encoding | Evidence and limits of the reading |
|---|---|---|
| Double-stroked derived-functor capitals | `\mathbb R`, `\mathbb L` | Handwritten pages throughout; an undoubled `L` above a tensor is retained where that is what is visible, e.g. 100 and 102. |
| Raised exclamation mark attached to a functor | `f^!`, `\mathbb R^!f`, `\mathbb L^!f` | Scan 98 contains different placements. A prime is not substituted for `!`; the doubtful first exponent is marked. |
| Lower exclamation mark attached to R | `\mathbb R_!f`, `\mathbb R_!f_*` | Both forms occur, including 110–120; the additional star is retained only where visible. |
| Pullback star, pushforward star, and prime | `f^*`, `f_*`, `f'` | Read separately from an exclamation mark. The `f'`/`f^*` ambiguity on 102 is marked. |
| Dots on complexes | `L_\bullet`, `M^\bullet`, `K^\bullet` | Both upper and lower positions occur. They have not been made uniform; 134 even has an unadorned final `M`. |
| Derived tensor product | `\overset{\mathbb L}{\otimes}` or `\overset{L}{\otimes}` | Decoration follows the ink. An ordinary tensor, including the right side on 142, is not supplied with a derived decoration. |
| Curled/script initial H in Hom | `\mathcal Hom` | Clear in 98–106, 134, 144 and 146. The top three cursive forms on 136 are marked `\unsure{\mathcal Hom\|\operatorname{Hom}}`; the straighter middle forms remain plain. |
| Plain Hom and derived-category Hom | `\operatorname{Hom}`, `\operatorname{Hom}_{D(A)}` | Distinguished from the curled initial where visible, particularly on 104 and 136. This is a letterform decision, not a decision based on the expected category. |
| Script cohomology H and script O | `\mathcal H`, `\mathcal O` | Used when visible; an underlined O versus script O ambiguity on 102 is retained. |
| Typescript script F, G, H, S | `\mathcal F`, `\mathcal G`, `\mathcal H`, `\mathcal S` | Scan 99, including handwritten mathematical characters within the typescript. |
| Typescript doubled/overstruck H and S | `\mathbb H`, `\mathbb S` | Scan 99. These are distinct from the script alphabets on that page. |
| Typescript exterior-form-space capital | `A_x^p` | Scan 99: the visible A is not replaced by a wedge or Lambda. |
| Gothic letter in the ramification typescript | `\unsure{\mathfrak g\|\mathfrak J}` | Scan 121; the particular Gothic letter remains uncertain. |
| Underlined variables in reused typescripts | `\uline{p}`, `\uline{m}`, `\uline{N}`, etc. | An underline is encoded separately rather than converted to a Gothic alphabet. The plain typed `m` on 145 remains plain. |
| Uppercase/lowercase typescript ambiguities | `\unsure{S\|s}`, `\unsure{V\|v}` | Exponents on 125, 127 and 131, and the subscript of M on 139, respectively; neither has been silently regularized. |
| Dual sign and primes | `^\vee`, `'` | Dual signs on 134–146 are distinct from primes on resolutions and from complex dots. |
| Trace notation | `\operatorname{Tr}_*`, `\operatorname{tr}^*`, `\operatorname{Tr}` | Position and case are retained per occurrence; the extra doubtful mark on 132 remains marked. |
| Tor notation and bounds | `\operatorname{Tor}_i`, `[N,M]`, `[N,N']`, `[N-2d,M]` | The changes of endpoint letters on 138–142 remain visible, including the overwritten `M`/`N'` ambiguity. No sign conversion between homological and cohomological grading is imposed. |
| Isomorphism sign | `\simeq`, or a tilde over an arrow when visible | A horizontal isomorphism sign is not automatically made an arrow. |
| Plain horizontal connector versus arrow | `-`, `\text{---}`, or `\to` with an explicit `\unsure` alternative | Missing or doubtful arrowheads remain missing/doubtful, e.g. 100, 112 and 140. Diagram arrows likewise follow visible heads. |
| Literal diagram objects and labels | `tikzcd` inside `\diagram{...}` | The objects, labels and directions are transcribed even where an algebraic inconsistency results. Drawings and cancellation strokes are separate TikZ figures. |
| Single and double underlining | `\uline{...}`, `\uuline{...}` | Only visible strokes are encoded; heavy typewriter serifs on the headings of 139 and 143 are not underlining. |
| Double quotation marks | LaTeX opening two backticks and closing two apostrophes | Applied consistently; no guillemets were substituted for handwritten quotation marks. |
| Two short horizontal strokes in prose | `$\unsure{=}$` | Scans 124 and 144; retained as the sign, not expanded to a word in the transcription. A possible verbal expansion is listed below. |
| Circled section/part identifiers | `\textcircled{...}`, with `\margin` where marginal | 26 on 100, 30 on 124, 31 on 138, 32 on 144; subsections 1, 2, 3 on 100, 108, 122; letters a and b on 144, 146. They are not treated as a stated total page count. |
| Visible foliation and typescript page numbers | `\mspage{...}` | The small foliation 97–145 is retained, as are independently visible page numbers on reused typescripts. No missing number is supplied. |
| A versus Lambda on a coefficient sheaf | Literal `A_X` or `\Lambda_X` | Scan 128 retains the letter change visible there. |
| Struck and added text | `\deleted`, `\inserted` | A readable cancellation remains transcribed; additions are placed at the indicated attachment. Nested deletion within insertion is retained, including `et borné` on 146. |

## Editorial conventions for the doubts register

The register below includes every `\unsure` and `\illegible` occurrence in the final individual page files. “Line” means the approximate line in that page's UTF-8 LaTeX source, counted from its first line, not a reconstructed physical manuscript line; several short lines of handwriting can occur within one source paragraph. Alternatives are reported without replacing the first reading in the transcription. Confidence measures the first reading, not the truth of its mathematics: **high** means a residual small uncertainty, **medium** a plausible but genuinely uncertain reading, and **low** damaged, crossed, clipped or severely compressed strokes.
