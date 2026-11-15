# MPL_136_189–234: notation and doubts

## Recurring notation table

This table was maintained during the image reading, before the context archive was opened. A doubtful individual occurrence remains marked in its page file even when the usual form is clear elsewhere.

| Written sign or form | LaTeX treatment | First occurrence / remarks |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes, ` ``…'' ` | 136 scan 189; no conversion to guillemets |
| Long handwritten lowercase ell | `\ell` | 136 scan 189, typed sheet with handwritten mathematical symbols |
| Generic-point subscript eta | `\eta` | 136 scan 189 |
| Superscript f | `^f` | 136 scan 189 |
| A circular superscript | `^{\unsure{0|o}}` if the glyph is undecidable | 136 scan 189 |
| Printed foliation | `\mspage{…}` within its printed punctuation | Used to preserve the sheet's own pagination, without attributing the typing to a particular hand |
| Archive pencil numbers and labels | Separate `\margin{…}` occurrences | Preserved even when a label repeats a pencil number; these are not treated as authorial pagination |


### Handwritten algebra notation (scans 190–208)

| Ink / usage | LaTeX transcription | Reading policy |
|---|---|---|
| Script A with simplex index | `\mathcal A_n`, `\mathcal A_*` | Distinguished from the ordinary `A_0`, `A_1` used for components in the early calculations. |
| Cursive phi | `\varphi` | Indices and degree superscripts retained separately. |
| Parenthesized exponent | `X^{(i)}` | Divided-power notation; ordinary unparenthesized exponents are retained where written, including scan 202. |
| Ideal suffix pd / p.d. | `_{pd}`, `_{p.d.}` | The actual punctuation is retained at each occurrence. |
| Cursive xi | `\xi_i`, `\xi_{ri}` | Questioned indices have local doubt marks. |
| Simplex maps | `\sigma_r^*`, `\mathcal A^*(\sigma)` | Do not replace one notation with the other. |
| Continuation dash in variable lists and sums | `-` | A drawn dash is not silently changed to `\cdots`. |
| Endomorphism monoids | `G_k`, `H_k`, `\Omega_k`, `G'_k`, `H'_k` | Prime marks retained; overwritten letters and unclear primes marked locally. The Latin letters are cursive handwritten capitals. |
| Element written as expression in braces | `\lambda\{T\}` | Braces are not silently changed to parentheses. |
| Half-simplicial abbreviation | `$\frac12$ simplicial` | Retains the written fraction rather than expanding it. |
| Order and inclusion signs | `\geq`, `\leq`, `\subset` | Read independently at each occurrence; no mathematical normalization. |
| Underlined mathematical letter in typed leaves | `\underline M`, `\underline m` | Underlining is part of the printed notation. |
| Asterisks and primes | `*`, `'` | Neither is silently converted to an exclamation-mark exponent. The first secure normalization exponents `^!` occur in scan 227; see below. |

### Later handwritten calculations (scans 210–234)

| Ink / usage | LaTeX transcription | Reading policy |
|---|---|---|
| Symmetric, divided-power, and exterior algebras | `\operatorname{Sym}^*M`, `\Gamma^*M`, `\Lambda^*M` | Parentheses and displayed tensor factors follow each occurrence. A change from Sym to Γ is not inferred from the differential. |
| Two differentials | `d`, `\delta` | The manuscript's occasional use of `d` in a paragraph about `\delta` is retained, notably scan 220. |
| Euler operator | `\theta=d\delta+\delta d` | Scan 222; the written cohomology indices are retained even where total degree and cochain degree might need to be distinguished mathematically. |
| Graded modules and ideals | `M^0+M^1`, `A^0+A^1`, `J^0+J^1` | Superscript 0/1 belongs to the parity grading here; these are not the circular superscripts of the reused typed sheets. |
| Script module and script algebra | `\mathcal M`, `\mathcal A` | Cursive mathematical capitals are distinguished from ordinary component letters `M`, `A_i`. |
| Φ and Ψ | `\Phi`, `\Psi` | Their overwriting in scan 227 is shown through deletion/insertion macros. An unresolved occurrence remains `\unsure{\Psi\|\Phi}`. |
| Stars versus dots | `*`, `\bullet` | The superscript/subscript position is preserved; unclear dot/star occurrences on scans 225–226 are marked. |
| Normalized complex exponent | `^!` | Read from the stem and dot in scans 227, 229, and 231; never replaced by a prime. The source's missing exponent on the last term of the cancelled sequence in scan 229 is not supplied. |
| Actual primes | `'` | Retained on `G'_k`, `H'_k`, `A'_1`, `M'`, and the primed objects of the reused text; distinct from `^!`. |
| Homotopy groups | `\pi_i`, `\pi_j`, `\pi_\ell` | Indices and the arguments under the homology displays on scan 231 are transcribed literally, including the second occurrence of `A_*\otimes B_*`. |
| Shifts | `k[1]`, `k[+i]`, `k[i]`, `k[0]_\bullet` | A plus sign is supplied only where written. |
| Derived functors and truncation | `(L\Lambda^i)`, `\tau^{\leq p}`, `\mathbb R\Gamma` | Scan 233: the uncertain intermediate Hom/Γ and truncation exponent remain marked. |
| Suspension notation | `\unsure{\Omega_a^i\|\operatorname{Susp}_a^i}` | Scan 229 contains a heavily retraced sign; the later written explanation `\operatorname{Susp}_a` does not settle that earlier glyph by itself. |
| Unheaded connecting line | `\mathbin{-}` or a TikZ arrow with `dash` | No arrowhead is added merely because a map is intended. When the head is uncertain, the dash is the first alternative if that is what is visible. |
| Underbrace / overset annotations | `\underbrace`, `\underset`, `\overset` | Preserve nearby identifications and degree labels; the two labels over the stars in scan 231 are marked as insertions. |
| Circled items and boxed formulas | `\textcircled`, `\boxed` | Retain the enclosing mark independently of whether its content is a number, letter, or formula. Double boxes remain double. |
| Handwritten natural signs added to typed W | `W_K^{\inserted{\natural}}` | Both instances in scan 234; distinguished visually from a flat sign. |

### Alphabets and marks on reused sheets

| Visible form | Treatment | Location / qualification |
|---|---|---|
| Double-stroked integer, rational, and multiplicative-group letters | `\mathbb Z`, `\mathbb Q`, `\mathbb G` | Typed mathematical text; the handwritten rational-field glyph in scan 208 remains uncertain. |
| Underlined character-group letter | `\underline M`, `\underline{M'}` | The same notation is rendered consistently across the reused IX sheets. |
| Upright textual superscripts | `\mathrm{an}`, `\mathrm{ab}`, `\mathrm{ef}` | Preserve the actual superscript and its position relative to the subscript and prime. |
| Formal completion | `\widehat G`, `\widehat{A^{\unsure{0\|o}}}` | In scans 232–234, the hat's scope is retained; it is not replaced by an analytification sign. |
| Small circular glyph, typed or handwritten | `\unsure{0\|o}` or `\unsure{o\|0}` | First alternative follows the local shape and position, not a global assumption that all circles denote zero. |
| Latin-letter underlining in Stoia's typescript | `\underline{…}` | Scans 216 and 218 preserve the visible editorial notation rather than silently typesetting its intended final alphabet. |
| Circles, pale oval, and double circle in Stoia's legend | `\figure{\begin{tikzpicture}…\end{tikzpicture}}` | Scan 218 names “latine,” “gothique,” “grec,” and “ronde”; the legend itself is drawn. |
| Circled m / Greek letter / script O on Stoia's sheets | `\textcircled{…}` with the visible internal letter | This records the mark on the page; it does not silently substitute the alphabet instructed by the legend. |

### Consistency review

Before freezing, the recurrent signs were compared across the page files and the doubtful occurrences were checked against their images during the audits: primes versus `^!`; stars versus dots; 0 versus o; Λ/Γ/Φ/Ψ; the script and ordinary A/M; underlined M; headed and unheaded arrows; parenthesized divided powers; and quotation marks. Differences that are visible or unresolved in the ink remain local differences, with doubt marks where appropriate. Double quotation marks are consistently encoded by two backticks and two apostrophes; double quotation marks used as TikZ label syntax are not transcribed punctuation.
