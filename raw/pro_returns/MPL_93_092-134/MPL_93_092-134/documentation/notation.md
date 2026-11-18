# Notation table — reconciled before the transcription freeze

The same root reader transcribed and audited all 42 scans. This table records the final visual conventions; it does not silently repair mathematical inconsistencies. Braced and unbraced TeX arguments (for example `\mathcal{H}` and `\mathcal H`) have the same meaning.

| Recurring written sign | LaTeX used | Visual distinction / scope |
|---|---|---|
| Upper-case omega | `\Omega` | Distinct from the smaller, often underlined lower-case omega. Retracing alone does not change the alphabet. |
| Lower-case omega, underlined where drawn | `\omega`, `\underline\omega` | Underlining is retained locally, including in powers and tensor products; it is not supplied where absent. |
| Differential bundle with upper 1 | `\Omega^1_{X/S}` | A small vertical 1 can resemble a prime; compared with the other occurrences on the sheet. |
| Powers versus tensor powers | `\omega^2`, `\omega^{\otimes2}` | A tensor-product sign is included only when visible. No global replacement of one by the other. |
| Cursive Lie-algebra bundle H | `\mathcal H` | Compared in scans 092–109 and 134. The final four occurrences retain `\unsure{\mathcal H}` because their rapid letter shape is less secure; the earlier Gothic-g alternative was withdrawn. |
| Cursive L | `\mathcal L` | Distinguished from the plain quotient line `L` used in scans 097–100 and 112. |
| Cursive torsor T | `\mathcal T` | The looped T of scans 111–114 is not the Greek capital Gamma. |
| Section functor / space of sections | `\Gamma` | Angular Gamma in expressions such as `\Gamma\underline\omega`; compared with the cursive torsor T. |
| Cursive P | `\mathcal P` | The sheaf of local projective coordinates or the written principal-parts algebra, according to the page. The transcription does not disambiguate equal written letters by inventing notation. |
| Plain principal-parts P | `P^1_{X/S}`, `P^2_{X/S}`, `P^3_{X/S}` | Kept plain where that is the written letter; the exponent is the order. |
| Projectivization / projective-space doubled P | `\mathbb P` | Early `\mathbf P` was reconciled to the doubled-stem form seen on the sheets. Generic variable `P` remains plain where written plain. |
| Doubled complex and real field capitals | `\mathbb C`, `\mathbb R` | Early `\mathbf C` and later `\mathbb C` represented the same written alphabet and were reconciled before freeze. |
| Doubled affine-space E | `\mathbb E^1` | The visible E in scans 108, 112, 113 was rechecked and the A alternative removed. It is not modernized to A. Later E occurrences use the same alphabet. |
| Doubled group/field capitals | `\mathbb G`, `\mathbb F` | Written G for additive/multiplicative groups and F for finite fields. |
| Vector-bundle constructions V and W | `\mathbb V`, `\mathbb W` | Scan 130 distinguishes these written letters; the bundle variable itself is plain `V`. |
| Structure sheaf | `\mathcal O`, sometimes underlined or plain `O` | Local visible underlines and alphabet are retained; ordinary zero is `0`. |
| Augmentation ideal | `\mathcal J` | The hooked cursive letter in scans 109, 133; not silently changed to I. |
| Quotient connection torsor C | `\mathcal C`, `\operatorname{Conn}` | Both written forms occur. The refined `\operatorname{Conn}^{0}` is distinct from the ordinary torsor in scan 121. |
| Projective linear group | `\mathrm{GP}(1)` | His GP notation is retained, not replaced by PGL. Abbreviated/retraced forms remain doubtful where necessary. |
| Group H versus cursive bundle H | `H`, `\mathcal H` | Plain H in scans 117–121 is the acting group; the handwriting, not the mathematical role alone, determines the font. |
| Filtration index | `\operatorname{Fil}_1` | Subscript is preserved, not converted to a superscript. |
| Connection components | `c_{2,3}`, `\omega_0`, `\omega_1`, `\omega_2` | Overwritten 2/3 and rapid indices retain local alternatives, especially scans 092 and 124. |
| Bar on a coefficient/form | `\bar\omega_1`, `\bar\omega_2` | A bar is not silently supplied to parallel occurrences. |
| Tildes and formal-completion hats | `\widetilde X`, `\widehat P`, `\widehat p` | Each follows the local stroke; weak marginal forms remain uncertain. |
| Ordinary derivatives / primes | `s'`, `s''`, `s'''`, `\lambda'` | The derivative primes were checked as strokes, independently of the formula expected. No exclamation-mark exponent was identified in this package. |
| Inverse-image superscript | `f^{-1}` | The negative numeral in scans 118–121 is not a prime or `^!`. |
| Divided derivative notation | `D^{(1)}`, `D^{(2)}`, `D^{(3)}` | Parentheses are retained; ordinary `D^n` where written is not silently converted. The conflicting orders on scan 122 remain doubtful. |
| Dual vector bundle | `\check E` | Scan 134; not replaced by a star merely because it denotes a dual. |
| Simple or double underlining | `\uline`, `\uuline` | Underlined words and labels remain underlined; mathematical underlines are also represented with standard `\underline`. |
| Author's double quotation marks | two backticks and two apostrophes | No guillemets were substituted. TikZ quotation syntax is separate from textual quotation marks. |
| Relation versus decorated map | `\simeq`, `\xrightarrow{\sim}`, `\xrightarrow[\sim]{p}` | Relation and arrowhead are distinguished by the ink. |
| Long stroke without visible arrowhead | `\text{---}`, TikZ `no head`/`dash`, or a doubtful alternative | No head is inferred from the expected diagram; scans 098, 112, 120, 128 were checked particularly. |
| Literal ellipsis | `\ldots` | The dots on scans 114–115 were revisited: these are marks on the page, not placeholders for omitted content. |
| Deletions and insertions | `\deleted`, `\inserted` | Even readable cancelled formulas remain cancelled. Insertion placement follows the local caret/line, not later mathematical arguments. |
| Manuscript sheet numbers | `\mspage` | Only the author's numbered drafts, scans 101–106; the doubtful last numeral remains 9/4. Archive pencil foliation is a TeX comment. |

