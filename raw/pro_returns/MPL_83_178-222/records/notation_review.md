# Authoritative notation review before context

The sole manuscript reader compared the recurring signs across the page images before freezing the transcription. This table records the resulting conventions; an unresolved difference remains explicitly doubtful in the page files rather than being settled from mathematical expectation. The occurrence-level register below gives the exact current encodings.

| Sign or feature | LaTeX used | Scans / decision |
|---|---|---|
| Small circle above a module or map | `E_i^\circ`, `f^\circ` | 178–180: circle, distinguished from the primes on `L',L''` in 181. |
| Product of extensions | `\mathop{*}`, `\mathbin{*}_{\lambda}` | 178–181: star and its written subscript retained; not replaced by tensor product. |
| Tensor product | `\otimes`, `\bigotimes` | 178–181: distinct from the star operation. |
| Lowercase b and u | `b_i`, `u_i` | 178–180: the two letterforms remain distinct, with local doubts where a stroke does not decide. |
| Uppercase X and lowercase x | `X_i`, `x_i` | 179: the written relation `X_i=x_i+\alpha_i` fixes their distinct shapes. |
| Prime and double prime | `'`, `''` | Throughout: no automatic conversion to exclamation marks; the exceptional raised mark in 209 is recorded as <code>\unsure{a^!&#124;a&#x27;}</code>. |
| Double prime resembling a digit 4 | <code>\delta^{\unsure{\prime\prime&#124;4}}</code> | 213, 215: the joined strokes remain doubtful locally; they are not silently normalized. |
| Script Azumaya-algebra A | `\mathcal{A}` | 183, 186, 190, 192: looped capital distinguished from the straight coordinate-ring `A`; the first occurrence in 183 retains alphabet doubt. |
| Straight coordinate-ring A | `A` | 190 onward: not identified typographically with `\mathcal A`. |
| Dual/check over A | `\check{\mathcal{A}}` | 192: visible check shape, distinct from a prime or exclamation. |
| Trace | `\operatorname{Tr}` | 183 onward: capital T, lowercase r; no normalization to `tr`. |
| Determinant, discriminant, automorphisms | `\det`, `\operatorname{dis}`, `\operatorname{Aut}` | Written operator names retained. |
| The two forms with phi-like names | `\Psi_{\det}`, `\varphi` | 183, 188: separate signs retained; differing definitions of `\varphi` are not editorially reconciled. |
| Two cyclic triple traces | `\tau`, `\tau'` | 183 onward: the order and signs in each formula are retained even when they differ between pages. |
| Sum, product, and difference invariants | `\Sigma`, `\Pi`, `\Delta` | 184–194: capitals, distinct from the later lowercase edge invariants. |
| Scalar orientation signs | `\varepsilon`, `\varepsilon_0` | 185–186: separate from the trace letters. |
| Three families of coordinates | `b,b',b''`, `c,c',c''`, `t,t',t''` | 184 onward: each written prime and subscript is preserved; the mathematical role is not used to repair a formula. |
| Symmetric-group letter | `\mathfrak S` | 189 onward: florid/looped capital, with alphabet uncertainty recorded at the initial occurrence. |
| Plus on an alternating subgroup | `\mathfrak S_3^+` | 199–200: superscript plus retained. |
| Open angular P | <code>\unsure{\mathcal P&#124;P}_2</code> | 193, 205: compared directly; the script-versus-plain ambiguity remains in both places. |
| Hooked capital T | `\mathcal T` | 205, 207: the same alphabet is used for the recurring sign; initial alphabet doubt remains explicit. |
| Lowercase edge invariants | `\sigma`, `\pi` | 203, 205, 207 onward: not converted to the earlier capitals. |
| Tilde positioned over an index | `\tau_{\tilde f}`, `\Sigma_{\tilde a}` | 201: tilde placed on the index, not the whole invariant. |
| Face label and its primes | `f,f',f''` | 201: distinguished from a group letter g. |
| Uppercase cube vertices and lowercase edges | `A,B,C,A',B',C'`; `a,b,c,a',b',c'` | 199–221: relative case is retained, including compound endpoint labels. |
| Three direction parameters | `\lambda,\mu,\nu` | 221: Greek lowercase signs. |
| Visible unheaded strokes | TikZ `\draw` or tikz-cd `dash` | 180, 195 and the drawings: no arrowhead is supplied from a presumed mathematical direction. A locally uncertain head is marked in place. |
| Grouping braces versus arrows | TikZ curves | 203: the interlaced right-hand curves are grouping strokes, not three connecting arrows. |
| An ambiguous exponent looking like 3 | <code>b^{\unsure{3&#124;&#x27;}}</code> | 217: ink-first digit candidate retained, although a prime would be mathematically plausible. |
| Double quotation marks | two backticks and two apostrophes | Throughout: a single package convention; no guillemets have been substituted. |
| Typed letter spacing | `\enspace` or thin spaces between the actual letters | Reused typed sheets: spacing is retained without rewriting the words. |
| Typewriter X-overstrikes | `\deleted{...}` | Reused typed sheets: the recoverable underlying letters, not literal strings of x, are transcribed; uncertainty stays inside the deletion. |
| Single and double underlining | `\uline`, `\uuline` | Both states retained; in 218 the double underline belongs to “respect”, not the whole phrase. |
| Repeated manuscript sheet identifiers | `\mspage{L 17}`, etc. | 198 and 204 are distinct scans/revision states even though both carry L 17; no deduplication. |

This review does not claim to settle every letterform. The local uncertainty macros, especially on sign changes, cancellations, and inserted text, take precedence over any abbreviated description in this table.
