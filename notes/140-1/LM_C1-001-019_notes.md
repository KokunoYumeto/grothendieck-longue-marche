# LM_C1-001-019 — Editorial and research notes

## 1. Scope and source handling

The source consists of the nineteen supplied JPEGs, in filename order, and the accompanying task prompt. Scan 1 is the archive cover; scans 2–19 reproduce archive sheets numbered 1–18. The cover identifies cote 140-1 and describes a larger item of 36 pages. This transcription covers only the nineteen supplied scans, not unseen leaves of that larger item. The accompanying prompt calls the work “(1981)”; the supplied cover instead gives undated draft notes and bracketed archival date information. Neither a precise composition date nor a sequence of composition is inferred from the reused paper.

The twelve manuscript-bearing scans are 2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18, and 19. The cover and scans 3, 5, 7, 9, 11, and 13 are handled with the prompt's explicit `% not manuscript:` exception. Scan 13 is a letter ending signed “Escofier,” in a visibly different hand, not a mathematical passage by Grothendieck. Scans 5 and 7 are separate copies of a June 1978 examination question, the latter inverted. These whole-page exception markers are recorded as status elements in the inventory; “yes” for these records means that the requested exception marker has been entered, not that the unrelated document has been transcribed.

Printed reproduction footers, page furniture, logos, the archive URL, and show-through from the reverse are not treated as autograph content. Small pencil numerals at sheet edges that match the archive sequence are retained as `\margin{...}` on manuscript-bearing sheets; this does not assert that they are in Grothendieck's hand. `\mspage` identifies the author's internal numerals where distinguishable. The page sequences must not be conflated.

### Scan concordance

The scan marker follows the filename, including the cover. The archive-sheet number and the author's internal manuscript number are separate sequences.

| Scan | Archive sheet | Author's internal number | Treatment |
|---|---|---|---|
| 1 | — | — | Cover; explicit non-manuscript marker |
| 2 | 1 | — | Matrix calculations |
| 3 | 2 | — | Administrative circular; explicit non-manuscript marker |
| 4 | 3 | 1 | Central extensions and products of lifted generators |
| 5 | 4 | — | Printed examination; explicit non-manuscript marker |
| 6 | 5 | 2 | Invariance questions and conjugation calculations |
| 7 | 6 | — | Inverted examination copy; explicit non-manuscript marker |
| 8 | 7 | 3 | Group diagrams and extension presentations |
| 9 | 8 | — | Administrative minutes; explicit non-manuscript marker |
| 10 | 9 | — | Finite quotients and group diagrams |
| 11 | 10 | — | Administrative rules; explicit non-manuscript marker |
| 12 | 11 | 4 | Lift calculations and diagonal marginal proposition |
| 13 | 12 | — | Letter ending signed Escofier; explicit non-manuscript marker |
| 14 | 13 | 4bis | Continuation of lift and congruence calculations |
| 15 | 14 | — | Mathematics over printed administrative text; both included |
| 16 | 15 | 5 | Moduli, fibre-product diagrams, and small drawing |
| 17 | 16 | — | Polyhedra and incidence relations; cancelled material retained |
| 18 | 17 | 6 | Central extension and inverted cancelled prose |
| 19 | 18 | — | Formula and drawing field with ambiguous diagonal strokes |

### Reading and encoding conventions

The French and mathematical readings are diplomatic, including unfinished expressions, inconsistent-looking notation, deletions, and insertions. No word or formula was supplied from a published transcription. Candidate readings remain inside the requested uncertainty macros; they are not silently resolved by algebraic consistency. Diagrams follow the visible connections, and the TikZ drawings approximate the source's ink positions. Cases where the extent or function of a stroke is uncertain are documented below; scan 19's two long diagonals remain unclassified.

The inventory contains 363 element records, each marked `yes`. This records coverage, not certainty of reading. Whole-page exclusions use the prompt's exception and are recorded as status elements, as explained above.

## 2. Table of doubts

Confidence means confidence in the proposed reading of the supplied image. It does not certify the mathematical correctness of the expression. Locations refer to the physical scan unless a LaTeX line is explicitly identified.

### Scan 2

Locations are approximate physical positions on the scan, supplemented by the element IDs in the LaTeX comments and inventory. “Confidence” applies to the proposed reading, not to the underlying mathematical assertion.

| Scan | Approximate line / element | Reading | Alternatives or reason for doubt | Confidence |
|---|---|---|---|---|
| 2 | Upper-left beginning, E02 | Cancelled underlined `u` followed by an arrow-like mark; then `alpha = u a^{-1}` | The cancelled mark could be an equals sign; the following dot could be punctuation. | low |
| 2 | Throughout, first in E03 | `v`, `v_1` | Greek `nu`, `nu_1` cannot be distinguished securely from the rounded Latin forms. These occurrences are marked locally. | medium |
| 2 | Upper-right determinant, E05 | `det(d rho+c)` | The final `c` inside the determinant is overwritten; no additional factor is recoverable with confidence. | medium |
| 2 | Middle second matrix, E11 | Upper entries `mu`, `lambda`, over earlier `A`/`B` and `B` | The underlying capital-like letters and chronology of the overwriting are not securely recoverable. | low |
| 2 | Across the fold, E12 | Upper-left entry `d mu`, with cancelled `d`/`delta` below | The fold and retracing interfere with the deleted glyph. | low |
| 2 | End of E12 | `d_0 rho+c_0` | Last coefficient may look like `d_0`; marked rather than reconciled to the earlier matrix. | medium |
| 2 | Below the fold, E13 | `c_0 = d mu / delta_alpha` | The oblique stroke is reinforced and can resemble `ne`. | medium |
| 2 | E13 denominator | `-v^2+wcd+c^2` | No independent `d` is confidently visible between the first `v` and the superscript. The earlier detached expression reads `-v d^2+wcd+c^2`; the two are not harmonized. | low |
| 2 | Deleted line E14 | `-v b d^2+v_1 a c d+w b c d` | The cancellation crosses all three terms, especially the first coefficient; the right parenthesis is unwritten. | low |
| 2 | E15 | `d_0 v` | The `v`-shaped factor is heavily retraced; possible `nu`. | low |
| 2 | Cancelled bottom-left calculation, E19 | `det a = det` and a fraction with numerator `u` or `mu` | The cancelled numerator and the detached denominator are uncertain; no missing operand has been supplied. | low |
| 2 | Beside box, E20 | Cancelled underlined `a` | Heavy overwriting. | low |
| 2 | Box, E21 | Minus sign before `c/v` | A second short stroke makes an equals-sign reading possible; both readings are represented. | low |
| 2 | Last determinant, E23 | Sign before `dc/v` | The ink is a blot; minus and plus are both possible. | low |

### Scans 4, 6, and 8

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 4 | Top left, presentation and first exact sequence | `\widetilde{\Pi}_n^{\circ D}` | `\widetilde{\Pi}_n^D`; the apparent circle may belong to a revision | low |
| 4 | Top left, sign before presentation | `\simeq` | `=`; overwritten strokes and a deleted brace overlap | low |
| 4 | Top right, following boxed relation | élément | The word is highly compressed but central is clear | medium |
| 4 | Definition of `\tilde\rho_i` | exponent i | The exponent is overwritten | medium |
| 4 | Right of definitions, above relève | deleted + | An isolated crossed pen mark may be a cancelled character | low |
| 4 | Second line of product expansion | deleted `\rho_0` after `\tilde\rho^{-1}` | A short overinked character, perhaps only 0 | low |
| 4 | Right edge of second expansion line | facteurs | The end reaches the sheet edge; the following `\tilde\rho_0` is on a lower line | medium |
| 4 | Text preceding nth-power calculation | donc | Compressed final strokes | medium |
| 4 | Three struck-through lines below boxed product | le sous-groupe de ... engendré; invariant | The cancellation crosses letter bodies and the group decoration | low |
| 4 | Insertion above the struck-through sentence | en | dans; a short connecting word before `\widetilde\Pi_n^D` | low |
| 4 | Cancelled left-margin formula beside Soit | `\widetilde\Pi_n^D\neq\tilde\rho_{n-1}\tilde\rho_{n-2}` | The initial group and relation are heavily crossed | low |
| 4 | Below second Soit, left margin | `\tilde\rho` | `\rho`; possibly an abandoned initial character | low |
| 4 | Above `\Pi_n` in last exact sequence | deleted can | A short overwritten sign or word, uncertain whether lexical | low |
| 4 | Under last exact sequence | engendré par | The first word is compressed | medium |
| 4 | Final identification | `\simeq` | `\subset`; first group has a blackened superscript, retained as a deleted possible circle | low |
| 4 | Last two lines | `\bar\omega`, `\omega` and the map `\bar\omega_0\to\omega_0^2` | Subscripts are absent in the preceding identification and have not been supplied | medium |
| 6 | Top parenthesis and upper left margin | ss-groupe; ss-gr. engendré par les | Full sous-groupe may be compressed into the apparent abbreviation | medium |
| 6 | Top question and next line | Invariant | Invariance; the last compressed stroke is ambiguous | low |
| 6 | Before clair | c'est | The initial characters are abbreviated in one continuous stroke | medium |
| 6 | All sigma-action formulae | superscript `\ast` | `-1`; in some occurrences it resembles a hooked arrow or a sharp sign | low |
| 6 | First sigma-action row, third argument | `\rho_2` | `\rho_n` | low |
| 6 | Lifted general action | last conjugating subscript `n+2-i`; `\tilde z_i` | Middle digit compressed; z decoration may be a hat | medium |
| 6 | Abelianized row | zeta symbols | gamma or rho symbols; the first argument has an overwritten/inserted upper character | low |
| 6 | Abelianized row before z_0 | cancelled rho-like symbol | Its internal loops are obscured by cancellation | low |
| 6 | Exponents in parity condition | `\nu_i` | `\gamma_i` | medium |
| 6 | Parity paragraph | invariance; essayer; calculer | Word endings are compressed | medium |
| 6 | Group in parity paragraph | `\widetilde\Pi_n^\circ` | `\Pi_n^\circ`; short upper stroke may be part of capital Pi | medium |
| 6 | First conjugation calculation, penultimate equality | `\tilde\omega_0^{-1}` | `\tilde\omega_1^{-1}`; subscript is a small nearly closed stroke | medium |
| 6 | First conjugation calculation end and below brace | deleted z_0; deleted rho-like character | Overinked symbols | low |
| 6 | Second conjugation calculation, first factors | `\tilde\rho^{-1}\tilde\sigma^{\ast}` | Sigma's raised black mark may be 2 or an unrecognizable cancellation | low |
| 6 | Second calculation, two nested brace labels | `\omega_0^{-2}` | `\omega_0^{-1}`; the visible exponent looks like 2 and has not been repaired by the algebra | low |
| 6 | Initial mark beside final rho_i expansion | cancelled sigma | rho; dense overink | low |
| 6 | Last standalone product | subscript `n+2-i` | `n-2-i` in first occurrence | medium |
| 8 | Matrix-group names throughout | Gl and Sl | GL and SL; the second letter is a cursive l whose case is not certain | medium |
| 8 | Rightmost object of large diagram | `\widetilde{\mathrm{Gl}}(2,\mathbb Z)` | First argument resembles n | medium |
| 8 | Large diagram, last upper diagonal | doubled/overtraced arrow | Two nearly coinciding strokes have been reproduced; no categorical meaning is assigned to the doubling | medium |
| 8 | Margin note | extension; les 2; qui relèvent | Small joined letters, an inserted phrase connected to the generator expression | medium |
| 8 | Margin-note generator expressions | `\rho_{\mathbb D'_3}` and `\rho_{\mathbb D_3}` | sigma in place of rho | low |
| 8 | Margin-note orders | 6, non 3 | Numerals and the reading of the preceding generators require checking together | medium |
| 8 | Margin-note final word | contrairement | Compressed angled word; the colon-like mark is visible | low |
| 8 | First short exact sequence | numerator `\mathbb Z` | Repeated strokes obscure the numerator | medium |
| 8 | Upper right paired sequences, first matrix group | Sl | Gl; initial letter is overwritten | low |
| 8 | Lowest pair of sequences, quotient of bottom group | `\mathbb D_3\times\{1,\tau\}` | The second factor could be `\{\pm1\}`; it is overinked | low |
| 8 | Vertical identification below Gl prime | `\simeq` | Two short strokes, one curved, form the vertical relation | medium |
| 8 | Last fundamental-group expression | `U_{0,3}` | `M_{0,3}`; capital is compressed | medium |
| 8 | Last fundamental-group expression, finite group | `\mathbb D_3\times\{1,\tau\}` | Overwritten D and first entry; final letter may be gamma | low |

### Scans 10, 12, 14, and 15

Positions refer to the manuscript image, not the LaTeX source line numbers. The scans contain several parallel calculation columns, so an approximate line number is supplemented by a region. Every local `\unsure` occurrence in these four fragments is represented below; repeated entries denote distinct occurrences. A low-confidence symbolic reading is a reading of surviving ink, not a restored relator.

| ID | Scan | Approximate line / region | Reading | Alternative | Confidence | Reason |
|---|---:|---|---|---|---|---|
| M10-D01 | 10 | top diagram, approximately ll. 1–7 | `\rtimes` | `\cdot` | low | The action/product sign is obscured by retracing. |
| M10-D02 | 10 | top diagram, approximately ll. 1–7 | `Can` | — | medium | The abbreviation can also look like Cont; its final strokes are compressed. |
| M10-D03 | 10 | top diagram, approximately ll. 1–7 | `Can` | — | medium | The abbreviation can also look like Cont; its final strokes are compressed. |
| M10-D04 | 10 | top diagram, approximately ll. 1–7 | `Can` | — | medium | The abbreviation can also look like Cont; its final strokes are compressed. |
| M10-D05 | 10 | top diagram, approximately ll. 1–7 | `\rho_1` | — | medium | The subscript in the equality is crowded. |
| M10-D06 | 10 | top diagram, approximately ll. 1–7 | `\mathrm S\ell(2,\mathbb Z)/\varepsilon` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D07 | 10 | top diagram, approximately ll. 1–7 | `\mathbb Z/2\mathbb Z` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D08 | 10 | top diagram, approximately ll. 1–7 | `Can` | — | medium | The abbreviation can also look like Cont; its final strokes are compressed. |
| M10-D09 | 10 | top diagram, approximately ll. 1–7 | `\sim` | — | medium | Detached two-stroke mark adjacent to D3-prime. |
| M10-D10 | 10 | first two presentations, approximately ll. 8–9 | `\omega` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D11 | 10 | quotient presentation and projection diagram, approximately ll. 10–12 | `2` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D12 | 10 | E presentation and its underbrace, approximately ll. 13–15 | `\rho` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D13 | 10 | E presentation and its underbrace, approximately ll. 13–15 | `\omega` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D14 | 10 | E presentation and its underbrace, approximately ll. 13–15 | `\text{est}` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D15 | 10 | E presentation and its underbrace, approximately ll. 13–15 | `\text{par}` | — | medium | Short connective with a compressed final stroke. |
| M10-D16 | 10 | projection to Z/12Z, approximately ll. 16–18 | `10` | `14` | medium | The second digit is overwritten; 10 is preferred from the visible closed form. |
| M10-D17 | 10 | projection to Z/12Z, approximately ll. 16–18 | `\leftrightarrows` | — | low | The small opposed-stroke glyph is poorly differentiated. |
| M10-D18 | 10 | epsilon0 and rho0 images, approximately ll. 19–22 | `(\sigma\rho)^2\omega=\rho_0` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D19 | 10 | epsilon0 and rho0 images, approximately ll. 19–22 | `\mathbb Z/3\mathbb Z` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D20 | 10 | D3-prime presentation, approximately l. 23 | `(\sigma\rho)^2\omega` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D21 | 10 | lower mapping diagram, approximately ll. 25–31 | `(\sigma\rho)^2\omega` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D22 | 10 | lower mapping diagram, approximately ll. 25–31 | `\mathbb Z/3\mathbb Z` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D23 | 10 | lower mapping diagram, approximately ll. 25–31 | `(\mathbb F_3\times\mathbb F_3)\rtimes\{1,\sigma\}` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M10-D24 | 10 | lower mapping diagram, approximately ll. 25–31 | `Can` | — | medium | The abbreviation can also look like Cont; its final strokes are compressed. |
| M12-D01 | 12 | diagonal proposition, approximately ll. 2–5 | `$\rho$` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D02 | 12 | diagonal proposition, approximately ll. 2–5 | `mbres` | — | medium | The short abbreviation is preferred to expanding it in the transcription. |
| M12-D03 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `l'un des` | — | low | Raised insertion is compressed among the surrounding formula and cancellation. |
| M12-D04 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `pour tous` | — | low | The cancellation prevents a secure word-by-word reading. |
| M12-D05 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `\uline{quantité bien définie}` | `\deleted{quantité bien définie}` | low | Both the wording and whether the long stroke is underlining or cancellation remain uncertain. |
| M12-D06 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `mod` | — | low | The short word sits among overwritten strokes. |
| M12-D07 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `indépendamment` | — | low | The visible word is long but many internal strokes merge. |
| M12-D08 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `n^2+1` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D09 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `$\mathbb Z$` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D10 | 12 | diagonal proposition, heavily revised middle, approximately ll. 5–8 | `ou` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D11 | 12 | diagonal proposition, two-value set, approximately l. 9 | `(` | — | low | The putative inner delimiter may instead be a correction stroke. |
| M12-D12 | 12 | diagonal proposition, two-value set, approximately l. 9 | `)` | — | low | The putative inner delimiter may instead be a correction stroke. |
| M12-D13 | 12 | diagonal proposition, uniqueness clause, approximately ll. 10–12 | `un` | — | medium | Article is reduced to a short connected stroke. |
| M12-D14 | 12 | diagonal proposition, uniqueness clause, approximately ll. 10–12 | `unique` | — | medium | The word and its final stroke are compressed. |
| M12-D15 | 12 | diagonal proposition, uniqueness clause, approximately ll. 10–12 | `uniquement` | — | medium | The beginning is readable; the word ending is a running stroke. |
| M12-D16 | 12 | diagonal proposition, uniqueness clause, approximately ll. 10–12 | `déterminés` | — | medium | The terminal letters/accent are not securely separated. |
| M12-D17 | 12 | diagonal proposition, concluding presentation, approximately ll. 13–14 | `Ainsi trouvons` | `Ceci fournit` | low | The short final prose before the presentation is compressed; neither candidate is secure. |
| M12-D18 | 12 | diagonal proposition, concluding presentation, approximately ll. 13–14 | `présentation` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D19 | 12 | diagonal proposition, concluding presentation, approximately ll. 13–14 | `\nu_0` | `\nu` | low | Possible small zero is entangled with the closing brace. |
| M12-D20 | 12 | main calculation, chosen lifts and powers, upper centre | `\widetilde\omega^{n+1}` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D21 | 12 | main calculation, alpha value, upper right | `!` | `?` | low | The punctuation after n=3 has an unresolved upper stroke. |
| M12-D22 | 12 | main calculation, central adjustment equation and overwritten exponent | `\beta` | — | medium | Beta is partly overwritten by the adjacent power or adjustment. |
| M12-D23 | 12 | main calculation, central adjustment equation and overwritten exponent | `n\beta-2\gamma` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D24 | 12 | main calculation, cancelled scratch work by Diophantine equation | `n` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D25 | 12 | main calculation, adjusted rho, lower left | `\beta` | — | medium | Beta is partly overwritten by the adjacent power or adjustment. |
| M12-D26 | 12 | main calculation, adjusted sigma, lower left | `4` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M12-D27 | 12 | main calculation, adjusted sigma, lower left | `\frac{n^3-n}{2}` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M14-D01 | 14 | initial coordinate equations, approximately ll. 1–2 | `*` | `n` | low | Unexpected superscript on the first coordinate equality is retained with alternatives. |
| M14-D02 | 14 | common-power equation, approximately l. 3 | `2` | `n` | low | The superscript resembles n; the candidate 2 remains uncertain and is not normalized. |
| M14-D03 | 14 | cancelled scratch equation, upper centre | `\beta=` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M14-D04 | 14 | numerical modular example, right middle | `n=3` | — | low | The small label to the left of 5 mod6 is highly compressed. |
| M14-D05 | 14 | polynomial expansion, second parity branch, below fold | `-` | — | low | The mark is filled in; a minus is only the best local reading. |
| M14-D06 | 14 | second parity case for lifts, lower third | `n` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M14-D07 | 14 | concluding prose and lift identity, approximately ll. 19–20 | `trouve` | — | low | The middle word is written as a sparse running line. |
| M14-D08 | 14 | concluding prose and lift identity, approximately ll. 19–20 | `un` | — | low | The final small word is a short curved stroke. |
| M14-D09 | 14 | concluding prose and lift identity, approximately ll. 19–20 | `n` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M14-D10 | 14 | allowed-value set, approximately l. 21 | `2` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M14-D11 | 14 | last sentence, approximately l. 22 | `caractériser` | — | medium | The middle letters are compressed and the ending is not secure. |
| M14-D12 | 14 | last sentence, approximately l. 22 | `\nu` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M15-D01 | 15 | first line, fibre-product set definition | `g''` | `g'` | low | Two small marks follow g, but it is uncertain whether both are primes. |
| M15-D02 | 15 | first line, fibre-product set definition | `\mathrm{sg}^{+}` | `\mathrm{sg}^{t}` | low | The superscript after sg could be a plus or a small t. |
| M15-D03 | 15 | cancelled superscript or word above abelianization, approximately l. 2 | `\mathrm{ext}` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M15-D04 | 15 | mod-3 tensor calculation, approximately l. 3 | `V` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |
| M15-D05 | 15 | mod-3 tensor calculation, approximately l. 3 | `0` | `1` | low | Small exponent after the 3 in the right-hand module is blotted. |
| M15-D06 | 15 | Chinese-remainder-style quotient display, approximately l. 6 | `\mathbb Z/2\mathbb Z` | — | medium | The modulus has been overwritten; the first factor label 6 is clear. |
| M15-D07 | 15 | presentation, overwritten relator after sigma squared, approximately l. 8 | `\omega\rho_0` | — | low | Heavily obliterated relator fragment; omega rho0 is only a best symbolic reading, not a mathematical completion. |
| M15-D08 | 15 | first cancelled commutator expansion, approximately l. 10 | `-1` | — | low | The inverse exponent lies on the line used to strike through the whole expansion. |
| M15-D09 | 15 | first cancelled commutator expansion, approximately l. 10 | `-1` | — | low | The inverse exponent lies on the line used to strike through the whole expansion. |
| M15-D10 | 15 | first cancelled commutator expansion, approximately l. 10 | `-1` | — | low | The inverse exponent lies on the line used to strike through the whole expansion. |
| M15-D11 | 15 | right margin, isolated marks below sigma rho sigma rho=1 | `.` | — | low | The isolated spot before 2 may be punctuation or a pen mark. |
| M15-D12 | 15 | right margin, lower map source | `\sigma` | — | medium | The source letter is retraced over the upside-down printed text. |
| M15-D13 | 15 | bottom peripheral-generator list | `5` | `\varepsilon` | low | Small detached glyph could be a digit in the opposite orientation. |
| M15-D14 | 15 | bottom equality, cancelled letters after rho0= | `\rho\sigma` | — | low | Ink is crossed, overwritten, or too abbreviated to secure the exact form. |

#### Additional layout and state uncertainties

- **Scan 10, upper mapping diagram:** The main arrow directions have been checked from the heads, including the arrow from the lower tilde Sℓ object up-left to Sℓ. The headless upper-left connector belongs to the diagram and is retained. Some long arrows are retraced or interrupted by annotations; one visible map is rendered for a retraced pair of strokes rather than treating the retracing as two independently asserted maps. The finite-field semidirect-product notation and several short “Can” labels remain less secure than the objects and principal arrowheads.
- **Scan 10, lower mapping diagram:** The independent long slash and the short vertical rule beside the finite-field annotation are retained. The allocation of the two upper diagonal arrows to the upper cyclic-group objects is the best spatial reading of a crowded draft; the mathematical interpretation has not been used to repair the topology.
- **Scan 12, diagonal proposition:** This is the least secure prose in these four scans. In particular, the raised insertion, the crossed wording near “quantité bien définie,” the transition before the presentation, and the optional zero on the final exponent remain unresolved. The neighbouring arithmetic has not been used to supply missing words. The apparent inner parentheses in the two-value set are explicitly uncertain.
- **Scan 12, central calculations:** The author's distinct labels rho0-tilde / rho-tilde and sigma0-tilde / sigma-tilde are retained even where the later power equations might invite a mathematical correction. A vertical separator between the lower calculation columns is represented by a rule beside the two elementary identities.
- **Scan 14, initial equations:** The unexpected superscripts on the initial coordinate assignments are retained rather than silently changing them to definitions. A relation resembling an isomorphism sign before the second common power is also retained. The modular arithmetic lower down is considerably clearer than those initial superscripts.
- **Scan 15, cancelled calculations:** The two adjacent sigma cancellations within the commutator are distinguished from the long cancellation of the entire expansion. Several inverse exponents cross that long stroke. The large rho^-2 beneath the first expansion is an underbrace label, not an extra factor appended to the next line. The last small detached glyph by the peripheral generators may be an oppositely oriented digit 5 from the reused sheet; its status is unresolved.

#### Mixed substrate and cancellation scope

Scan 15 contains mathematical handwriting over an upside-down printed administrative sheet. Both are retained: the mathematical reading order comes first, then the printed substrate in its own upright reading order, identified by a LaTeX comment. Word divisions at printed line ends have been joined; paragraph divisions and headings are retained. The printed dashed underlines below ARTICLE 5 and ARTICLE 6 are represented by the required `\uline` macro.

Two long diagonal strokes on scan 15 cross most of the upper mathematics. Their broad cancellation scope is represented by an outer `\deleted` block, with the shorter local cancellations also retained inside it. The exact intended extent of those diagonal strokes cannot be proved from the scan; the right-margin calculations and final bottom lines are outside that outer block. On scan 10 the long independent diagonal stroke across the lower diagram is rendered as a free stroke, without assigning it an invented source or target object.

### Scans 16–19

Positions refer to the supplied scan orientation, except where “rotated” is stated. Confidence concerns the proposed reading of the ink, not the truth of the mathematics. A low-confidence candidate is retained in place in the transcription; it is not an editorial completion. Where no second candidate is given, the principal reading remains uncertain.

| Scan | Approximate line / position | Reading used | Alternatives or unresolved detail | Confidence |
|---|---|---|---|---|
| 16 | Upper diagram, first object | `D_3 =` Gothic `S_3` | The second initial also resembles Gothic `G`; the alphabet is not secure. | medium |
| 16 | Paragraph below upper square, line 1 | `non triviale` | `bien triviale`; the initial curve may contain the opening parenthesis and first letter together. The candidate is not settled from the extension. | low |
| 16 | Same paragraph, after semicolon | Cancelled `lorsque` | A looped initial and a q-like descender support this tentative reading after a further close review; most interior letters remain under the strike. | low |
| 16 | Same paragraph, line 3 | `avec trivialité` | The letters are strongly compressed; the phrase is not established merely by the factorization through `D_3`. | low |
| 16 | Same paragraph, line 4 | `noyau` | The final two letters are a short run of strokes. | medium |
| 16 | Same paragraph, right end | `D'_2 → D_2` | `D'_3 → D_3`; the local subscripts look like 2, even though 3 would be mathematically expected. | low |
| 16 | Note below `T_{11}`, third/fourth lines | `au dessus` | First word/spacing uncertain. | medium |
| 16 | Same note, final line | `on prend` | `ou prendre`; the ending is particularly abbreviated. | low |
| 16 | Beneath the preceding note | Underlined `a`-like mark | Could be a short equality-like check mark rather than a letter. | low |
| 16 | Tiny marks immediately above lower diagram | `Pi_rho` / `Pi_0`, and `Pi_{0,3}` | Both appear to be abandoned or repeated notation; the first subscript and their precise attachment are uncertain. | low |
| 16 | Lower diagram, middle left object | Cancelled `Z/4Z`, replacement `D'_3` | The two notations overlie one another; the assigned cancellation/replacement order is tentative. | low |
| 16 | Lower diagram, middle right object | Cancelled `Z/2Z`, replacement `D_3` | The two notations overlie one another; the assigned order is tentative. | low |
| 16 | Inside the two lower squares | `cart` | Short, undotted handwriting; no expansion is made in the transcription. | medium |
| 16 | Lower-right explanatory note, first line | `On remonte` | The second word ends in a few strokes. | medium |
| 16 | Same note, before primed generators | Cancelled `rho,sigma`-like notation | Could be a group/Pi-like trial notation instead; the blackened glyphs cannot be disentangled reliably. | low |
| 16 | Coordinate of `sigma'` | Cancelled `2`, inserted `3` | Overwriting sequence is inferred from the two visible shapes, not certain. | medium |
| 16 | Before the power relations | `on a` | The first sign is nearly a dot; the entire short phrase is marked. | medium |
| 16 | Slanted note at right edge | Presentation after `On vérifie alors aisément que` | Exponents `6,4` and `3,2` are tentative readings; the black scan edge clips the end. Both relations carry doubt marks. | low |
| 16 | Bottom paragraph, first line | `apparaît` | Compressed word between the isomorphism and `comme extension`. | low |
| 16 | Bottom paragraph, second line | Cancelled `de` | Underlying letters uncertain. | low |
| 16 | Bottom paragraph, third line right | `resp.` | Could be a different short connective; edge compression matters. | medium |
| 16 | Bottom paragraph, fourth line after composite | Cancelled `D_3` | The object is overwritten by the continuation towards `Z/2Z`. | low |
| 16 | Bottom paragraph, last clause | `C'est`, `gr.`, `de base` | All are compressed/clipped; especially `de base` should not be accepted from mathematical plausibility. | low |
| 16 | Extreme bottom right | Long dash-like continuation | Could be the beginning of further clipped text. No word is supplied. | low |
| 16 | Right of lower diagram | Loose curved callout arrow, parenthesis/brace strokes | Their shapes are reproduced separately in TikZ; precise attachment to the reflowed marginal text is approximate. They are not interpreted as additional group homomorphisms. | medium |
| 17 | Top diagram | `X_0` | The subscript may be a dot/bullet. | medium |
| 17 | Before three quotient injections | `i.e.` | `i.a.`; the second character is very small. | low |
| 17 | Third quotient injection | Hooked arrow | An inclusion sign is also possible. | medium |
| 17 | Third quotient numerator | Cancelled `G_0` / `H_S`-like glyph | Heavy overwritten numerator. The visible denominator is `H_A` and is retained, although it repeats the preceding quotient's denominator. | low |
| 17 | Left slanted heading | `Cas non orienté` | The first word has a large loop; the final ending is abbreviated. | medium |
| 17 | Fourth line of functor list | Cancelled `A` | `R`; the glyph is heavily crossed. | low |
| 17 | First incidence-table parenthesis | `arêtes orientées` | Endings are abbreviated; the whole phrase is marked, rather than normalized from grammar. | medium |
| 17 | Third incidence-table row | `S et F` | The first letter also resembles `B`. | low |
| 17 | `R` formula, cancelled object | `A_3` | The index is the clearest part of the overwritten object. | low |
| 17 | Between cancelled object and product | `simeq` | An ordinary equality sign is possible. | medium |
| 17 | Cancelled phrase above fold | `relation d'incidence entre S et F` | Initial `relation` remains uncertain under the horizontal crossing stroke. | medium |
| 17 | Replacement phrase above cancellation | `triplets ou drapeaux` | `triplets de drapeaux`; both first word and connective are difficult. | low |
| 17 | Condition after `(s,a,f)` | `s ≤ a < f` | The lower stroke of `≤` may belong to the deleted line underneath, in which case the first sign is `<`. | low |
| 17 | Orientation-identification display | Middle object `A_{2,Omega}` | Overwritten middle index/object; the candidate is retained with doubt. | low |
| 17 | Isolated first `Pol` expression | Subscript `tau` | Latin `t`. | medium |
| 17 | Superscript of second `Pol` | `or` | First letter is overwritten; the abbreviation is a candidate, not an expansion. | medium |
| 17 | Final right-hand suffix | Cancelled `/Omega`, lower inserted `/Omega` | The erased upper suffix and the attachment of the lower slash are unclear; slice notation is only a possible interpretation. | low |
| 17 | Long diagonal stroke | Cancellation of the main block through the orientation display | It begins at the top and ends below that display with a hook; the final `Pol` line lies outside its extent. The classified extent is an editorial judgment, and all affected content remains transcribed. | medium |
| 18 | First line | `image inverse` | Both words are compressed into a few strokes. | medium |
| 18 | First line, last group | Overwritten `GL`, then `SL(2,R)^tilde` | `GL(2,R)^tilde` without a distinguishable replacement; the initials are not reliably separable, and the alternative remains explicit. | low |
| 18 | Under central element in presentation | Opening-parenthesis-like stroke; abbreviated `élém` with raised `t` | The curve may be a leader rather than a literal parenthesis; `él` with raised `mt` is also possible. No closing parenthesis is supplied. | medium |
| 18 | Left and right abelianization headings | Both read `(T_{11})_ab` | An initial `S` on the left would reconcile the displayed groups, but I do not see it and have not inserted one. | high |
| 18 | Left column, image of `omega` | `6` | `8`; the digit has an extra loop/stroke. | medium |
| 18 | Top horizontal arrow in central diagram | Cancelled `T_ab`-like notation | Letter and subscript are overwritten. | low |
| 18 | Kernel annotation at left of diagram | Tilde `omega` | Bar `omega`; the mark is short and wavy. | low |
| 18 | Same annotation, after exponent 2 | Cancelled `4`-like mark | It may be another overwritten exponent or an unresolvable stroke. | low |
| 18 | Rotated bottom paragraph, first and third lines | `normalisation` | `uniformisation`; letter sequence remains uncertain even after rotation and magnification. | low |
| 18 | Rotated paragraph, first line | `(K,N)` | `(K,k_0)`; the second entry is particularly unclear. | low |
| 18 | Same line | `alors` | Compressed into a short sequence; no alternative settled. | medium |
| 18 | Same line, final adjective | `spéciale` | Word ending and initial strokes are uncertain. | low |
| 18 | Rotated paragraph, second line | `K'_f N` | `K'_{fN}`; positions of the prime/index and letter `N` are uncertain. | low |
| 18 | Same line, after dash | One cancelled unreadable word | Estimated one word, physically masked by its own cancellation. | low |
| 18 | Rotated paragraph, third line | `rev.` between Delta symbols | `i.e.`; the repeated Delta-like glyphs themselves are more secure than the connective. | low |
| 18 | Same line | `a` before `une unique` | Short connective could be a different stroke. | medium |
| 18 | Rotated paragraph, fourth line | `la projection est` | `la projection soit`; independent visual review favors `soit`, and neither has been left confident. | medium |
| 18 | Same line | `un morphisme de` | Ending of `morphisme` remains compressed; the word is marked. | medium |
| 18 | Following line | `normalisés` | Not securely readable; not inferred from the earlier candidate `normalisation`. | low |
| 18 | Bracketed qualification | `ça ne marche`, underlined `pas` | The phrase preceding `pas` is difficult, and only the underlined negative is moderately secure. | low |
| 18 | Bracketed qualification, end | `strictes normalisations` | Could be a different word beginning `stricte...` followed by the earlier `uniformisation` candidate; exact wording unresolved. | low |
| 18 | Bracketed qualification, final sign | Barred `m` | `néc.`; the available strokes support neither confidently. | low |
| 18 | Rotated final item number | `8.` | Greek `beta.`; shape is open and cursive. | medium |
| 18 | Final item title | `Groupes`, `fondamentaux` | Singular `Groupe`, `fondamental`; endings are abbreviated. | medium |
| 18 | Final item, second sentence | `On montrera` | `On montre`; independent reader also found `montrera` plausible. | medium |
| 19 | Top-left isolated cancellation | `Z` | Tilde `sigma`; the ink is nearly obliterated. Both are shape-based guesses. | low |
| 19 | Top-centre-left cancellation | Tilde `rho` | Plain `rho`; this is a heavily overwritten trial. | low |
| 19 | Incomplete upper-left equality | `tilde rho_0^n = tilde sigma_0^n =` | The second exponent visibly resembles `n` and has not been changed to 2 to match the right column. | high |
| 19 | Cancellation under first right-hand equality | `tilde rho_0 bar omega` | A single `bar omega`-like trial; quantity and identity of original symbols are unresolved. | low |
| 19 | Cancellation before first mapping | Tilde `rho` | Tilde `sigma`; underlying symbol uncertain. | low |
| 19 | Cancellation after second mapping arrow | Parenthesized `omega` | Parenthesized `rho`; parentheses and middle symbol are compressed/overwritten. | low |
| 19 | Both right-hand sigma factors | Subscript `0` | `a`; the apparent subscript is blackened. | low |
| 19 | Sigma-power line, first exponent | `2` | `n`; the two shapes are very similar in this hand. | low |
| 19 | Sphere: above northern point, upper-right arc, equator right | Three small `i`-like labels | `1` or, in one or more positions, small directional strokes; all three are retained with alternatives. | low |
| 19 | Left of long formula above paths | `R_i` | `R^i`; vertical placement of the little `i` is ambiguous. | medium |
| 19 | Long formula's first symbol | `tilde R_i` | The index is short and not securely separated from the capital. | medium |
| 19 | Difference in that formula | `e_j - e_k` | `e_g - e_K`; both indices are unclear. | low |
| 19 | Following factor | `lambda^omega_{jk}` | `h^omega_{gK}`; the main letter and indices are independently uncertain. | low |
| 19 | Below the preceding formula | `t_omega, h_omega` | `epsilon_omega, h_1`; the first symbol is heavily inked. | low |
| 19 | Left of paths | `V(omega)` | `V(w)`. | medium |
| 19 | Label at common starting point | `phi_omega(tilde R_K)` | Lowercase `k` for `K`; tilde/bar distinction is also not fully secure. | medium |
| 19 | Cancelled label near start, above fold | `t_omega` | `R_omega`; overdrawn first letter and suffix. | low |
| 19 | Cancelled label right of `P_i` | `H_i` | `H_2`; the crossing stroke itself resembles a large 2. | low |
| 19 | Replacement/right-hand label | `u tilde omega^i` | `u omega^i`; the short mark above omega may be part of the superscript or overwriting. | low |
| 19 | Caption below curves | `opèrent` | `opérant`; the ending is a long abbreviated stroke. | medium |
| 19 | Same caption, last noun on first line | `sentiers` | `entiers`; an initial s-like curve makes the first reading plausible, but the word is not supplied merely because the drawing contains paths. | low |
| 19 | Isolated cancelled expression below caption | `R_K R` | `R_kappa R`; no relation sign is discernible between the capitals. | medium |
| 19 | Two long diagonals through formulas and paths | Unclassified strokes reproduced in the coordinated TikZ field | They may be cancellation marks, separators, or part of the graphic construction. A blanket `\deleted` would assert more than the ink establishes. | low |

### Index of in-place uncertainty markers

This locator index lists every distinct `\unsure` or `\illegible` argument on each scan and all its line numbers in the delivered LaTeX fragment. The editorial confidence assessments and physical locations are in the tables above; repeated occurrences are grouped here. A vertical bar inside an uncertainty argument separates candidate readings, and an illegible-word marker gives the estimated word count.

| Scan | LaTeX line(s) | Marker | Argument as transcribed |
|---|---|---|---|
| 2 | 9 | `unsure` | `\Rightarrow\|=` |
| 2 | 9 | `unsure` | `\,\cdot\,\|\,;\,` |
| 2 | 14, 31, 42, 48, 49, 74, 81, 86, 98, 111, 122 | `unsure` | `v\|\nu` |
| 2 | 22 | `unsure` | `c` |
| 2 | 31, 41, 81 | `unsure` | `v_1\|\nu_1` |
| 2 | 57 | `unsure` | `A\|B` |
| 2 | 57 | `unsure` | `\mu` |
| 2 | 58 | `unsure` | `B` |
| 2 | 58 | `unsure` | `\lambda` |
| 2 | 66 | `unsure` | `d\|\delta` |
| 2 | 69 | `unsure` | `c_0\|d_0` |
| 2 | 73 | `unsure` | `/\|\ne` |
| 2 | 74, 120 | `unsure` | `v^2\|\nu^2` |
| 2 | 74 | `unsure` | `c^2` |
| 2 | 102 | `unsure` | `\,\cdot\,` |
| 2 | 104 | `unsure` | `u\|\mu` |
| 2 | 104 | `unsure` | `\delta_\alpha\|\delta` |
| 2 | 107 | `unsure` | `\underline{a}` |
| 2 | 111 | `unsure` | `-\|=` |
| 2 | 121 | `unsure` | `vv_1\|\nu\nu_1` |
| 2 | 122 | `unsure` | `-\|+` |
| 4 | 134, 145 | `unsure` | `\widetilde{\Pi}_n^{\circ D}\|\widetilde{\Pi}_n^D` |
| 4 | 135 | `unsure` | `\simeq\|=` |
| 4 | 136 | `unsure` | `\{` |
| 4 | 140 | `unsure` | `élément` |
| 4 | 158 | `unsure` | `i` |
| 4 | 160 | `unsure` | `+` |
| 4 | 170 | `unsure` | `\rho_0` |
| 4 | 171 | `unsure` | `facteurs` |
| 4 | 183 | `unsure` | `donc` |
| 4 | 196 | `unsure` | `sous-groupe` |
| 4 | 196 | `unsure` | `\widetilde\Pi_n^D\|\Pi_n^D` |
| 4 | 196, 226 | `unsure` | `engendré` |
| 4 | 197 | `unsure` | `en\|dans` |
| 4 | 198 | `unsure` | `invariant` |
| 4 | 199 | `unsure` | `\widetilde\Pi_n^D` |
| 4 | 199 | `unsure` | `\neq` |
| 4 | 210 | `unsure` | `\tilde\rho\|\rho` |
| 4 | 224 | `unsure` | `\mathrm{can}` |
| 4 | 231 | `unsure` | `\circ` |
| 4 | 232 | `unsure` | `\simeq\|\subset` |
| 6 | 247 | `unsure` | `ss-groupe` |
| 6 | 248 | `unsure` | `ss-gr.` |
| 6 | 248 | `unsure` | `engendré` |
| 6 | 251, 253 | `unsure` | `Invariant\|Invariance` |
| 6 | 252 | `unsure` | `c'est` |
| 6 | 258, 259, 260, 261, 267, 268, 269, 279, 282, 284, 297, 320 | `unsure` | `\ast\|-1` |
| 6 | 260 | `unsure` | `2\|n` |
| 6 | 270 | `unsure` | `n+2-i` |
| 6 | 270 | `unsure` | `\tilde z_i\|\hat z_i` |
| 6 | 280 | `unsure` | `\zeta` |
| 6 | 280, 281, 316 | `unsure` | `\tilde\rho` |
| 6 | 281, 282 | `unsure` | `\zeta_1\|\gamma_1` |
| 6 | 283 | `unsure` | `\zeta_0\|\gamma_0` |
| 6 | 284 | `unsure` | `\zeta_i\|\rho_i` |
| 6 | 285 | `unsure` | `\zeta_{n+1-i}\|\gamma_{n+1-i}` |
| 6 | 289, 291 | `unsure` | `\nu_i\|\gamma_i` |
| 6 | 290 | `unsure` | `invariance` |
| 6 | 290 | `unsure` | `\widetilde\Pi_n^\circ\|\Pi_n^\circ` |
| 6 | 292 | `unsure` | `essayer` |
| 6 | 292 | `unsure` | `calculer` |
| 6 | 312 | `unsure` | `\tilde\omega_0^{-1}\|\tilde\omega_1^{-1}` |
| 6 | 313 | `unsure` | `z_0` |
| 6 | 326 | `unsure` | `\tilde\rho^{-1}` |
| 6 | 327 | `unsure` | `\ast\|2` |
| 6 | 329 | `unsure` | `\tilde\sigma^{-1}` |
| 6 | 330, 330 | `unsure` | `-2\|-1` |
| 6 | 334 | `unsure` | `\sigma\|\rho` |
| 6 | 343 | `unsure` | `n+2-i\|n-2-i` |
| 8 | 356, 368 | `unsure` | `\mathrm{Sl}\|\mathrm{SL}` |
| 8 | 362, 370, 400, 407, 410 | `unsure` | `\mathrm{Gl}\|\mathrm{GL}` |
| 8 | 362 | `unsure` | `2\|n` |
| 8 | 381 | `unsure` | `extension` |
| 8 | 382 | `unsure` | `2` |
| 8 | 382 | `unsure` | `\rho_{\mathbb D'_3}\|\sigma_{\mathbb D'_3}` |
| 8 | 383 | `unsure` | `relèvent` |
| 8 | 383 | `unsure` | `\rho_{\mathbb D_3}\|\sigma_{\mathbb D_3}` |
| 8 | 384 | `unsure` | `6` |
| 8 | 384 | `unsure` | `3` |
| 8 | 385 | `unsure` | `contrairement` |
| 8 | 391 | `unsure` | `\mathbb Z` |
| 8 | 397 | `unsure` | `\mathrm{Sl}\|\mathrm{Gl}` |
| 8 | 411 | `unsure` | `\simeq` |
| 8 | 412 | `unsure` | `\{1,\tau\}\|\{\pm1\}` |
| 8 | 413 | `unsure` | `U_{0,3}\|M_{0,3}` |
| 8 | 414 | `unsure` | `\mathbb D_3` |
| 8 | 414 | `unsure` | `1` |
| 8 | 414 | `unsure` | `\tau\|\gamma` |
| 10 | 427 | `unsure` | `\rtimes\|\cdot` |
| 10 | 428, 432, 433, 444, 541 | `unsure` | `Can` |
| 10 | 437 | `unsure` | `\rho_1` |
| 10 | 439 | `unsure` | `\mathrm S\ell(2,\mathbb Z)/\varepsilon` |
| 10 | 443 | `unsure` | `\mathbb Z/2\mathbb Z` |
| 10 | 451 | `unsure` | `\sim` |
| 10 | 462, 484 | `unsure` | `\omega` |
| 10 | 475 | `unsure` | `2` |
| 10 | 484 | `unsure` | `\rho` |
| 10 | 485 | `unsure` | `\text{est}` |
| 10 | 486 | `unsure` | `\text{par}` |
| 10 | 496 | `unsure` | `10\|14` |
| 10 | 501 | `unsure` | `\leftrightarrows` |
| 10 | 507 | `unsure` | `(\sigma\rho)^2\omega=\rho_0` |
| 10 | 509, 529 | `unsure` | `\mathbb Z/3\mathbb Z` |
| 10 | 518, 528 | `unsure` | `(\sigma\rho)^2\omega` |
| 10 | 535 | `unsure` | `(\mathbb F_3\times\mathbb F_3)\rtimes\{1,\sigma\}` |
| 12 | 562 | `unsure` | `$\rho$` |
| 12 | 562 | `unsure` | `mbres` |
| 12 | 564 | `unsure` | `l'un des` |
| 12 | 565 | `unsure` | `pour tous` |
| 12 | 566 | `unsure` | `\uline{quantité bien définie}\|\deleted{quantité bien définie}` |
| 12 | 567 | `unsure` | `mod` |
| 12 | 567 | `unsure` | `indépendamment` |
| 12 | 569 | `unsure` | `n^2+1` |
| 12 | 570 | `unsure` | `$\mathbb Z$` |
| 12 | 570 | `unsure` | `ou` |
| 12 | 573 | `unsure` | `(` |
| 12 | 573 | `unsure` | `)` |
| 12 | 576 | `unsure` | `un` |
| 12 | 576 | `unsure` | `unique` |
| 12 | 579 | `unsure` | `uniquement` |
| 12 | 579 | `unsure` | `déterminés` |
| 12 | 580 | `unsure` | `Ainsi trouvons\|Ceci fournit` |
| 12 | 580 | `unsure` | `présentation` |
| 12 | 585 | `unsure` | `\nu_0\|\nu` |
| 12 | 617 | `unsure` | `\widetilde\omega^{n+1}` |
| 12 | 627 | `unsure` | `!\|?` |
| 12 | 630, 648 | `unsure` | `\beta` |
| 12 | 634 | `unsure` | `n\beta-2\gamma` |
| 12 | 640 | `unsure` | `n` |
| 12 | 658 | `unsure` | `4` |
| 12 | 662 | `unsure` | `\frac{n^3-n}{2}` |
| 14 | 697 | `unsure` | `*\|n` |
| 14 | 705 | `unsure` | `2\|n` |
| 14 | 718 | `unsure` | `\beta=` |
| 14 | 743 | `unsure` | `n=3` |
| 14 | 755 | `unsure` | `-` |
| 14 | 772, 778 | `unsure` | `n` |
| 14 | 776 | `unsure` | `trouve` |
| 14 | 776 | `unsure` | `un` |
| 14 | 782 | `unsure` | `2` |
| 14 | 785 | `unsure` | `caractériser` |
| 14 | 785 | `unsure` | `\nu` |
| 15 | 793 | `unsure` | `g''\|g'` |
| 15 | 794 | `unsure` | `\mathrm{sg}^{+}\|\mathrm{sg}^{t}` |
| 15 | 798 | `unsure` | `\mathrm{ext}` |
| 15 | 804 | `unsure` | `V` |
| 15 | 805 | `unsure` | `0\|1` |
| 15 | 822 | `unsure` | `\mathbb Z/2\mathbb Z` |
| 15 | 830 | `unsure` | `\omega\rho_0` |
| 15 | 846, 846, 847 | `unsure` | `-1` |
| 15 | 863 | `unsure` | `.` |
| 15 | 867 | `unsure` | `\sigma` |
| 15 | 871 | `unsure` | `5\|\varepsilon` |
| 15 | 874 | `unsure` | `\rho\sigma` |
| 16 | 905 | `unsure` | `\mathfrak S_3\|\mathfrak G_3` |
| 16 | 911 | `unsure` | `non triviale\|bien triviale` |
| 16 | 911 | `unsure` | `lorsque` |
| 16 | 911 | `unsure` | `avec trivialité` |
| 16 | 911 | `unsure` | `noyau` |
| 16 | 911 | `unsure` | `\mathbb D'_2\|\mathbb D'_3` |
| 16 | 911 | `unsure` | `\mathbb D_2\|\mathbb D_3` |
| 16 | 920 | `unsure` | `au dessus` |
| 16 | 920 | `unsure` | `on prend\|ou prendre` |
| 16 | 920 | `unsure` | `a` |
| 16 | 924 | `unsure` | `\Pi_\rho\|\Pi_0` |
| 16 | 924 | `unsure` | `\Pi_{0,3}` |
| 16 | 938 | `unsure` | `\mathbb Z/4\mathbb Z` |
| 16 | 938 | `unsure` | `\mathbb D'_3` |
| 16 | 938, 939 | `unsure` | `\mathrm{cart}` |
| 16 | 938 | `unsure` | `\mathbb Z/2\mathbb Z` |
| 16 | 938, 961 | `unsure` | `\mathbb D_3` |
| 16 | 946 | `unsure` | `On remonte` |
| 16 | 946 | `unsure` | `\rho,\sigma` |
| 16 | 947 | `unsure` | `2` |
| 16 | 948 | `unsure` | `on a` |
| 16 | 953 | `unsure` | `\rho'^{\,6}=\sigma'^{\,4}=1` |
| 16 | 953 | `unsure` | `\rho'^{\,3}=\sigma'^{\,2}` |
| 16 | 961 | `unsure` | `apparaît` |
| 16 | 961 | `unsure` | `de` |
| 16 | 961 | `unsure` | `resp.` |
| 16 | 961 | `unsure` | `C'est` |
| 16 | 961 | `unsure` | `gr.` |
| 16 | 961 | `unsure` | `de base` |
| 16 | 961 | `unsure` | `---` |
| 17 | 968 | `unsure` | `X_0\|X_\bullet` |
| 17 | 976 | `unsure` | `i.e.\|i.a.` |
| 17 | 980 | `unsure` | `\hookrightarrow\|\subset` |
| 17 | 980 | `unsure` | `G_0\|H_S` |
| 17 | 987 | `unsure` | `Cas non orienté` |
| 17 | 996 | `unsure` | `A\|R` |
| 17 | 1001 | `unsure` | `\text{arêtes orientées}` |
| 17 | 1003 | `unsure` | `S\|B` |
| 17 | 1007 | `unsure` | `A_3` |
| 17 | 1007 | `unsure` | `\simeq\|=` |
| 17 | 1009 | `unsure` | `relation` |
| 17 | 1010 | `unsure` | `triplets ou drapeaux\|triplets de drapeaux` |
| 17 | 1010 | `unsure` | `\leq\|<` |
| 17 | 1028 | `unsure` | `{A_2}_{\Omega}` |
| 17 | 1032 | `unsure` | `\tau\|t` |
| 17 | 1033 | `unsure` | `\mathrm{or}` |
| 17 | 1034 | `unsure` | `/\Omega` |
| 18 | 1042 | `unsure` | `image inverse` |
| 18 | 1042 | `unsure` | `\deleted{\mathrm{GL}}\mathrm{SL}(2,\mathbb R)^{\sim}\|\mathrm{GL}(2,\mathbb R)^{\sim}` |
| 18 | 1046 | `unsure` | `(` |
| 18 | 1046 | `unsure` | `élém\textsuperscript{t}\|él\textsuperscript{mt}` |
| 18 | 1058 | `unsure` | `6\|8` |
| 18 | 1064 | `unsure` | `\mathcal T_{\mathrm{ab}}` |
| 18 | 1065 | `unsure` | `\widetilde\omega\|\bar\omega` |
| 18 | 1065 | `unsure` | `4` |
| 18 | 1072, 1072 | `unsure` | `normalisation\|uniformisation` |
| 18 | 1072 | `unsure` | `N\|k_0` |
| 18 | 1072 | `unsure` | `alors` |
| 18 | 1072 | `unsure` | `spéciale` |
| 18 | 1072 | `unsure` | `K'_fN\|K'_{fN}` |
| 18 | 1072 | `illegible` | `1` |
| 18 | 1072 | `unsure` | `rev.\|i.e.` |
| 18 | 1072 | `unsure` | `a` |
| 18 | 1072 | `unsure` | `est\|soit` |
| 18 | 1072 | `unsure` | `morphisme` |
| 18 | 1072 | `unsure` | `normalisés` |
| 18 | 1072 | `unsure` | `ça ne marche` |
| 18 | 1072 | `unsure` | `pas` |
| 18 | 1072 | `unsure` | `strictes normalisations` |
| 18 | 1072 | `unsure` | `$\overline{\mathrm m}$\|néc.` |
| 18 | 1074 | `unsure` | `8.\|$\beta$.` |
| 18 | 1074 | `unsure` | `Groupes\|Groupe` |
| 18 | 1074 | `unsure` | `fondamentaux\|fondamental` |
| 18 | 1074 | `unsure` | `montrera\|montre` |
| 19 | 1083 | `unsure` | `\mathbb Z\|\widetilde\sigma` |
| 19 | 1084 | `unsure` | `\widetilde\rho\|\rho` |
| 19 | 1087 | `unsure` | `\widetilde\rho_0\bar\omega\|\bar\omega` |
| 19 | 1088 | `unsure` | `\widetilde\rho\|\widetilde\sigma` |
| 19 | 1090 | `unsure` | `(\omega)\|(\rho)` |
| 19 | 1091, 1092 | `unsure` | `0\|a` |
| 19 | 1092 | `unsure` | `2\|n` |
| 19 | 1115, 1116, 1117 | `unsure` | `i\|1` |
| 19 | 1121 | `unsure` | `R_i\|R^i` |
| 19 | 1122 | `unsure` | `i` |
| 19 | 1122 | `unsure` | `e_j\|e_g` |
| 19 | 1122 | `unsure` | `k\|K` |
| 19 | 1122 | `unsure` | `\lambda\|h` |
| 19 | 1122 | `unsure` | `jk\|gK` |
| 19 | 1123 | `unsure` | `t_\omega\|\epsilon_\omega` |
| 19 | 1123 | `unsure` | `h_\omega\|h_1` |
| 19 | 1124 | `unsure` | `\omega\|w` |
| 19 | 1125 | `unsure` | `\widetilde R\|\bar R` |
| 19 | 1125 | `unsure` | `K\|k` |
| 19 | 1127 | `unsure` | `t_\omega\|R_\omega` |
| 19 | 1128 | `unsure` | `H_i\|H_2` |
| 19 | 1129 | `unsure` | `\widetilde\omega^{,i}\|\omega^i` |
| 19 | 1140 | `unsure` | `opèrent\|opérant` |
| 19 | 1144 | `unsure` | `sentiers\|entiers` |
| 19 | 1146 | `unsure` | `R_KR\|R_\kappa R` |

## 3. Abbreviations met

### Scan 2

| As written | Tentative expansion | Location |
|---|---|---|
| `det` | déterminant | Scan 2, several calculations |
| `Tr` | trace | Scan 2, upper-right display |

### Scans 4, 6, and 8

| As written | Tentative expansion |
|---|---|
| ext. | extension |
| i.e. | id est |
| ss-groupe, ss-gr. | sous-groupe |
| ab | abélianisé / abélianisation |
| NB | nota bene |

### Scans 10, 12, 14, and 15

These expansions are editorial suggestions only; none is substituted into the transcription.

| Form on page | Suggested expansion or function | Confidence / qualification |
|---|---|---|
| `Prop` | Proposition | High; the word is underlined on scan 12. |
| `mbres` | membres | Medium; reading of the short form itself is uncertain. |
| `mod` | modulo | High for the ordinary arithmetic occurrences; the occurrence inside the diagonal proposition is less secure. |
| `ab` | abélianisé / abélianisation | High as a mathematical label; the author does not expand it here. |
| `Can` | canonique | Medium; the final pen strokes might support a different short form such as Cont. |
| `i.e.` | id est | High. |
| `déf` | définition | Medium; used over the equality signs in scan 12. |
| `pr₁` | première projection | High as the arrow label in the lower scan-10 diagram. |
| `ext` (cancelled candidate) | extérieur / extension | Low; both the reading and intended expansion are unresolved. |
| `sg` with uncertain superscript | possibly signature | Low; this is only a contextual gloss, not a resolved transcription. |
| `U.S.T.L.` | Université des Sciences et Techniques du Languedoc | High; it belongs to the printed administrative substrate, not the mathematical handwriting. |

### Scans 16–19

These expansions belong only to this list. Candidate abbreviations remain tentative when their reading is marked in the transcription.

| Written form | Tentative expansion / interpretation |
|---|---|
| `can` | canonique |
| `cart` | cartésien; the fuller word `cartésien` is also cancelled on scan 18 |
| `pt` | point |
| `ext.` | extension |
| `gr.` | groupe |
| `resp.` | respectivement |
| `rel.` | relation |
| `ens` | ensemble |
| `cat.` | catégorie |
| `rev.` | revêtement(s), if this is the correct reading of the inverted passage |
| `top.` | topologique |
| `élém` with raised `t`, or `él` with raised `mt` | élément |
| `ab` | abélianisé / abélianisation |
| `id` | identité |
| `Im` | image |
| `exp` | exponentielle |
| `mod` | modulo |
| `or` | orienté(s), tentative superscript on `Pol` |
| `Pol` | polyèdres, as suggested by the nearby category paragraph; notation not formally defined here |
| `i.e.` | id est, if the ambiguous letters are indeed `i.e.` |
| `néc.` | nécessairement, one possible reading at the end of the inverted qualification |
| barred `m` | même, the competing reading at that position |
| `SL` | special linear group notation; not expanded in the manuscript text |
| `GL` | general linear group notation, only a possible reading of overwritten initials on scan 18 |
| `OK` | affirmative check mark in words; preserved without interpreting it as a supplied proof |

## 4. Legibility and limits

The large formulas are generally more readable than the small superscripts, joined French word endings, and layered cancellations. The least dependable areas are scan 2's overwritten matrix entries and final sign; the action superscripts on scan 6; the small right-hand notes on scan 8; the dense diagram labels on scan 10; the diagonal proposition on scan 12; the cancelled calculations on scan 15; the clipped foot of scan 16; and the inverted cancelled prose on scan 18. Those areas remain explicitly provisional.

Scan 19 was checked through its final labels and caption. Its formulas, sphere, paths, and long diagonal strokes share one coordinate-based TikZ reconstruction, preserving their relative placement without assigning the long strokes an unproved editorial meaning. This is an approximation of handwriting and curvature, not a facsimile; uncertain letters and numbers remain marked. The separate administrative sheets and the differently signed letter are represented by the requested exception markers, not silently omitted.

### Technical form

The `.tex` file is deliberately a fragment, with no preamble or macro definitions. It was compiled in a temporary XeLaTeX wrapper defining the requested editorial macros and loading `amsmath`, `amssymb`, `tikz-cd`, and the TikZ libraries `arrows.meta`, `decorations.pathreplacing`, and `calc`. The editor must supply the macro definitions and the desired treatment of deletion and uncertainty; the archive does not include the temporary proof document. Explicit `ampersand replacement=\&` keys make the TikZ matrices usable inside the argument-taking `\diagram` macro; nested ordinary arrays retain their ordinary separators.

## 5. Research notes

These notes are separate from the transcription. A claim described as unproved is unproved in the indicated local passage of this supplied extract, not necessarily elsewhere in the manuscript or literature. Questions and possible implications are recorded even when later pages may address them. All items labelled **own idea** are proposed checks or interpretations, with confidence and reasons; none is asserted to be new.

### Scan 2

### R02.1 — Scan 2, bottom left — conjecture (question)

Grothendieck writes a question mark over the equality in `det a = delta_alpha^{-1} mu`. This is a local computational question, not a conjecture about a named theory. A check would first require establishing exactly which matrix is denoted by `alpha`, whether `delta_alpha` is its determinant, and the readings of the overwritten triangular matrix entries; those definitions are not made explicit on this sheet.

### R02.2 — Scan 2, lower-right box — unpursued implication

The boxed expression `a = (mu/delta_alpha)(-c/v rho+d)` suggests an expression for `a` in the algebra generated by `rho`. The relevant denominators and the sign in the box require verification before one can formulate the domain on which such an expression is valid. The unfinished calculation of its determinant is a natural continuation, but any completed identity belongs in commentary and must not replace the draft.

### R02.3 — Scan 2, determinant formulas — own idea

One could compare the two determinant computations using a purely symbolic calculation with separate variables for every ambiguous coefficient, then inspect which alternatives are compatible with the written matrix product. Confidence: high that this would be a useful diagnostic, because it would expose consequences of each reading without choosing one from context. It would not establish what the ink says, and consistency must not be used as a silent emendation.

### Scans 4, 6, and 8

1. **Scan 4, top and middle — unpursued implication.** The presentation `\{\tilde\rho,\tilde\sigma\mid\tilde\rho^n=\tilde\sigma^2\}` and the displayed product `\tilde\rho_{n-1}\cdots\tilde\rho_0=\tilde\omega_0^2` suggest comparing the central generator of the ambient extension with the product of peripheral lifts. The calculation on the page is directed at the displayed product in its notation, but the consequences for the extension class are not developed here.
2. **Scan 4, lower third — unproved claim.** The page writes an exact sequence involving the presentation with the relation “central i.e.” and then an identification involving `\mathbb Z\bar\omega` and `\mathbb Z\omega`. A proof of that presentation and identification would need to establish the kernel and the absence of further relations, rather than only the displayed product relation.
3. **Scan 4, final lines — own idea.** It may be useful to formulate the final identification as a change of central kernel along the displayed map `\bar\omega_0\to\omega_0^2`, and to check it directly from the two presentations. **Confidence: medium:** the map and the two cyclic central groups are visible, but the final binary operation and some decorations are uncertain; this is a proposed verification, not an assertion about the intended construction or its novelty.
4. **Scan 6, top — conjecture (question).** The explicit question is “est-il invariant dans” the decorated ambient group, followed by another question “par” `\tilde\sigma` “?”. The page contrasts the clear action of `\tilde\rho` with the action of `\tilde\sigma`, whose effect is then calculated on peripheral generators.
5. **Scan 6, top and parity paragraph — unproved claim.** The parenthesis “ss-groupe d'indice 2” and the condition that the central exponents be congruent to zero modulo 2 are stated without a separate proof on this page. Verification would require a precise characterization of the subgroup in terms of the parity of the central coordinate and justification that checking the displayed generators is sufficient.
6. **Scan 6, middle to bottom — unpursued implication.** The intention “On va essayer de les calculer au moins” `z_0,z_1` is followed by two products ending in 1, then the start of a general-index calculation. The displayed special calculations suggest checking whether all correction factors vanish, while the unfinished general product leaves that broader verification open on this page.
7. **Scan 6, parity paragraph — own idea.** A useful independent check would be to reduce the central correction exponents modulo 2 and test whether the resulting obstruction to invariance is a homomorphism or a cocycle for the visible action. **Confidence: medium:** the text explicitly supplies central powers and a parity condition, but the action convention and some superscripts remain uncertain, so this is a research procedure rather than an established interpretation.
8. **Scan 8, upper-right margin — unproved claim.** “Cette extension n'est pas scindée” is asserted next to the presentation of `\mathbb D'_3` and the central extension by `\mathbb Z/2\mathbb Z`, with a short parenthetical explanation about orders. A careful proof should compare the orders of lifts of the quotient generators; the parenthetical generator and numeral readings are not secure enough to use as an unquestioned proof.
9. **Scan 8, large diagram and right-hand sequences — unpursued implication.** The nested central groups and the arrows labelled `\mathbb Z/2\mathbb Z`, `\Pi_{0,3}`, and `\mathbb D_3` invite checking that the successive quotient descriptions yield the same finite-group and matrix-group extensions. The sheet supplies the diagrams but no separate verification of exactness and commutativity for every displayed path.
10. **Scan 8, last identification — unproved claim.** The matrix-group quotient is identified with a fundamental group written `\Pi_1(\ldots;P_+)`. To verify this identification, one would need to settle the object and action in the partly overwritten argument, specify the base point, and match the presentations or monodromy maps; none of those details is supplied in the adjacent diagram.
11. **Scan 8, marginal order explanation — own idea.** If the small parenthesis really says that both lifts of rho have order 6, it should be tested directly by multiplying a lift by the central element in the displayed presentation. **Confidence: medium for the proposed check, low for the exact premise:** the parenthesis may instead name another generator or different numerals, so a possible algebraic discrepancy must remain separate from the diplomatic reading and must not be used to change it.

### Scans 10, 12, 14, and 15

### Grothendieck's questions, provisional claims, and implications

1. **Scan 10, upper right; kind: conjecture (question).** The quotient annotation explicitly leaves a “sous-groupe d'ordre 2” “à déterminer.” The immediate task is to identify which subgroup, ambient group, and map the annotation is intended to describe, then check the kernel and the surrounding cyclic projections. The nearby order 36 is visible, but the crowded arrows should be resolved before attributing a final quotient claim to the author.

2. **Scan 10, middle presentation of E; kind: unproved claim.** The draft labels the group 36 and writes that the indicated relator is “invariant” and “d'ordre |3.” These lines do not contain a complete finite-order proof. An explicit model and mutually inverse presentation maps, or a normal-form argument with a matching lower bound, would be needed to establish the order and verify the listed images of rho, sigma, and omega.

3. **Scan 10, upper and lower diagrams; kind: unpursued implication.** The same order-18 fibre product is displayed together with a tentative finite-field product description and maps to D3 and Z/6Z. An explicit comparison of those descriptions would determine which order-two action is intended on the two three-element factors and which factor is detected by each projection. The transcription leaves the action/product sign uncertain, so that comparison should be reported independently of the palaeographic reading.

4. **Scan 12, diagonal proposition and lower calculations; kind: unproved claim.** The proposition begins “Il existe des relèvements” and ends with a presentation after the assertion of uniqueness. The accompanying equations give part of the arithmetic construction, and scan 14 continues the parity calculation, but a full argument would also need to justify how the chosen central extension is identified by those lift relations and how the claimed uniqueness depends on the chosen exponent. Several words in the proposition are uncertain, so its exact scope must be fixed before treating it as a theorem statement.

5. **Scan 14, final two-value set; kind: unpursued implication.** The concluding condition is “nu impair” for the two values -(n-1)/2 and (n+1)/2. For odd n, their parity selects the positive representative when n is 1 modulo 4 and the negative representative when n is 3 modulo 4. This reformulation would make the dependence on n transparent without changing the manuscript's calculation or the surviving notation.

6. **Scan 15, quotient display under diagonal cancellation; kind: unproved claim.** The cancelled display places the numbers 72, 6, and 24 under the quotient and its two factors. An independent verification would require the reduction map modulo 6, its relation to the two reductions modulo 2 and modulo 3, and the exact identification of the central sign quotient. Because the block is crossed, it should be recorded as a draft calculation rather than an endorsed final statement.

### Own ideas and proposed checks

7. **Scan 10 upper diagram, compared with scan 15 quotient display; kind: own idea. Confidence: high as a consistency check, not as a reading correction.** Explicitly compare the adjacent order-36 label and “d'ordre 2” annotation with the factor orders 6 and 24 written on scan 15. Counting those factors and the proposed kernel would test whether the annotations belong to the same quotient or to different stages of the diagram. This is a reason to investigate the maps, not to replace the printed order or subgroup size in the transcription.

8. **Scans 12 and 14, lift adjustments; kind: own idea. Confidence: high.** Revisit what changes when n is even, rather than formally substituting an even n into alpha=(n-1)/2. The homogeneous relation 2 gamma=n beta has integral solutions generated by (2/d,n/d), where d=gcd(2,n); the author's beta=2x, gamma=nx uses the odd case. This elementary distinction offers a precise test of which existence or uniqueness statements actually require the initial “n impair.”

9. **Scan 15, mod-3 tensor line; kind: own idea. Confidence: medium.** Investigate the permutation action on F3^3/F3, where the denominator denotes the diagonal line in the most direct reading. In characteristic 3 that diagonal line lies in the sum-zero subspace, so the latter yields a one-dimensional subquotient. This could clarify the crossed or blotted superscript in the neighbouring expression and the role of the three peripheral generators, but the proposed interpretation must not be substituted for the uncertain exponent 0|1.

10. **Scan 15, cancelled commutator expansion; kind: own idea. Confidence: medium.** Check the displayed word in a concrete matrix or finite-group model using the relations actually written on that page, then compare intermediate reductions with each surviving cancellation. Such a calculation may expose which assumption the author was testing or rejecting. It cannot settle an invisible inverse exponent or prove what an obliterated relator originally said.

These research notes are observations and possible verification tasks grounded in the four supplied scans. They make no claim of priority or novelty and have not been used to amend the transcription.

### Scans 16–19

These are working research prompts, not corrections to the diplomatic text. No external transcription has been used to settle a reading. A claim noted here may be proved elsewhere in the manuscript; these notes record only what is left open in the supplied local passage.

### Scan 16, upper-left margin — unproved claim / explicit verification marker

The words “à vérifier” and the later-looking “OK” occur together beside the initial construction. The object of the verification is not attached by an unambiguous insertion sign, so it should not automatically be restricted to either the pullback square or the asserted identification of `M_{1,1}`. The local pages do not supply the check that the `OK` may record.

### Scan 16, upper square and paragraph — unproved claim

The text calls `D'_3` an extension “non triviale” and specifies an action through `D_3`, followed by a compressed statement about the central kernel acting trivially. A proof should first fix the actual group in the square and the meaning of the pair `(U_{0,3},D'_3)`, then establish the pullback and the claimed kernel action. The ambiguous final subscripts in the prose must be resolved independently of this expected construction.

### Scan 16, upper square — own idea

If the diagram is the fiber product of `D_3 → Z/2Z` and `Z/4Z → Z/2Z`, restrict it to an order-two subgroup mapping nontrivially to `Z/2Z`; its inverse image should be cyclic of order four, providing a direct test of non-splitting. **Confidence: high for this conditional group calculation, medium for its applicability to the uncertain local notation.** This is a verification route, not a claim of a new result.

### Scan 16, middle identification — unproved claim

The equation identifying `T_{11}` with the pointed fundamental group of `(U_{0,3},D'_3)` is accompanied by a choice of a point in the Poincaré half-plane over `P_+`. A proof should state the fundamental-group convention for an action with ineffective kernel, construct the covering or groupoid model, and track the point choice. The note “dépend du choix” is material: a bare unpointed abstract isomorphism would not reproduce all that is asserted here.

### Scan 16, right slanted margin — unproved claim

“On vérifie alors aisément que” introduces a presentation identified with `SL(2,Z)`. Once the clipped exponents are securely recovered, one could verify the proposed lifts by matrices and check that the displayed relations give the whole group, not just relations satisfied in a quotient. The note's wording is more legible than its final presentation, so the precise proposition should remain provisional.

### Scan 16, lower squares — unpursued implication

The factorization “via `D_3`” appears to retain an order-two ineffective central action when forming the group-theoretic extension. It is worth checking explicitly how this kernel survives in the pointed action-groupoid fundamental group and what is lost by replacing the action-groupoid quotient by its coarse orbit space. This consequence is conditional on the reading of the kernel paragraph; it is not an additional assertion inserted into the manuscript.

### Scan 17, upper third, cancelled block — unproved claim

The three pairwise stabilizer-intersection equations are followed by injections into products of quotient sets. The group-theoretic implication from a trivial intersection to the corresponding injection is straightforward once the coset conventions are fixed; the geometric assertion requiring proof is that the chosen stabilizers have those intersections. The third written quotient repeats `H_A`, so its intended geometric role must not be reconstructed by silently changing that denominator.

### Scan 17, middle, cancelled block — unproved claim

The formula `R ≃ A_1 ×_A A_2` and the three image formulas appear to package incidence data or flags. A proof needs the precise definitions of `S,A,F` and the incidence objects, together with the conditions ensuring that the fiber product gives exactly the intended triples. The uncertain first inequality in the inserted description matters for that formulation.

### Scan 17, orientation display and final line — unproved claim

The cancelled identifications after passage to `Omega` are followed by an uncancelled-looking equivalence involving `Pol_tau^or` and `Pol_tau` with a corrected `/Omega` suffix. It is necessary first to determine whether that suffix denotes a slice, another fiber construction, or a quotient, and then construct the proposed equivalence with its morphisms. An interpretation based solely on objects would not establish the categorical statement.

### Scan 17, incidence reconstruction — own idea

Test the written incidence reconstruction on a small explicit polyhedron, keeping separately the unoriented flags and choices of orientation, and enumerate the resulting fiber products and images. **Confidence: medium**, because this is a useful consistency test but the precise categorical conventions and two handwritten labels remain unresolved. The test should preserve the manuscript's repeated denominator as a separate case rather than repair it beforehand.

### Scan 18, top presentation — unproved claim

The statement “image inverse” identifies `ST_{1,1}` with a subgroup of a covering group, followed by the presentation `rho^3=sigma^2`. A proof would need a precise choice of the ambient covering group and lifts of generators, then an identification of the central element represented by the common power. The overwritten ambient initials are therefore a substantive palaeographic issue, not cosmetic notation.

### Scan 18, central square — unproved claim

The margin says that `ST_{11}` “se déduit” from `T_{11}` by inverse image of the canonical extension of `Z/12Z` by `Z`. To verify this, show that the homomorphism to `Z` has the displayed values on generators and identifies the kernel map with multiplication by 12, then prove the square is a pullback. The word “cartésien” is itself cancelled in the drawing, while the marginal prose states the inverse-image construction; both states of the draft should be kept in view.

### Scan 18, two abelianization headings — own idea

Compare the two literal headings `(T_{11})_ab` with the presentation and quotient line before making any editorial decision: the displayed target groups are `Z` and `Z/12Z`. Computing the abelianization of the group presented by `rho^3=sigma^2` and of the indicated central quotient may identify the intended distinction, but it cannot establish that an unseen `S` was written. **Confidence: high that this is a useful conditional algebraic check; low that it resolves the handwriting without another witness.**

### Scan 18, rotated cancelled qualification — unproved claim / caution requiring decipherment

The words “Mais attention” and an underlined negative occur in a qualification about the preceding normalization-like construction. The technical noun, the adjective beginning `stricte...`, and the sentence's exact restriction are too uncertain to state as a theorem or counterexample. The first research step is to recover those words and the object `(K,...)`; no mathematical completion has been proposed in the transcription.

### Scan 18, rotated final cancelled item — unproved claim left for later

“On montrera” announces a relation between topological and algebraic construction after the title about groups and fundamental groupoids. The supplied passage gives an outline, not the comparison construction or its hypotheses. A future check should determine the intended categories and the precise comparison morphisms before importing a standard comparison theorem.

### Scan 19, upper-right calculations — unpursued implication

The replacements of the lifted generators by powers of the central element culminate in `1+2s=(1-n)/2` and “OK si” that last quantity is odd. This suggests a parity obstruction to making the two altered powers coincide with the chosen central power. The conclusion must remain conditional on the ambiguous exponent in the sigma line and on the relation between barred and unbarred omega.

### Scan 19, parity condition — own idea

For integer `n`, the literal condition that `(1-n)/2` be odd is equivalent to `n ≡ 3 (mod 4)`, and the written linear equation would give `s=-(n+1)/4`. **Confidence: high for this arithmetic consequence of the displayed equation; medium for its intended role**, because the altered-generator calculation has two uncertain symbols. Testing `n=3` and `n=7` is a useful check of the signs before attempting a general interpretation.

### Scan 19, drawings and caption — own idea

Reconstruct a combinatorial description of the sphere routes and the distinguished-path field, including basepoints, directions and labels, before identifying an action of the two named generators. The tentative caption reading “sentiers distingués” is compatible with that route, but must not decide the uncertain labels or the role of the two long diagonals. **Confidence: low**, because several overwritten labels and the caption ending are unresolved; this is a proposed investigation, not an established geometric interpretation.

## Literature checks and further verification

These comparisons concern the research notes only. No external edition, published transcription, or later account was used to supply a missing manuscript reading. The cited literature does not establish the meaning of an ambiguous symbol on these scans, and the proposed checks are not claims of novelty.

### L1 — Scans 16 and 18, moduli and central-extension displays — own idea

Compare the displayed “image inverse” description and the relation `rho^3 = sigma^2` with Hain's account of the fundamental group of the moduli space of elliptic curves with a nonzero tangent vector, its description using the inverse image of `SL(2,Z)` in the universal cover of `SL(2,R)`, and its braid-group presentation (Hain, 2014, §§8.1–8.3). **Confidence: high that this is a relevant comparison:** the extension, matrix group, and two-generator relation are visibly present, although identifying every decorated manuscript group still requires checking its definitions. A verification should distinguish the full central subgroup from the kernel of the particular quotient to `SL(2,Z)`, since these need not have the same chosen generator.

### L2 — Scans 4, 8, and 16, peripheral generators and fundamental-group diagrams — own idea

Use the configuration-space and mapping-class-group constructions reviewed by Birman and Brendle (2005, §§1.1–1.3) to set up an independent topological model for the displayed generators and quotient maps. **Confidence: medium:** the manuscript visibly involves fundamental groups and central lifts, but the identification of the relevant action and marked configuration is incomplete in this supplied extract. Such a model could test exactness and the effect of changing lifts; it would not justify replacing the manuscript's arrows, indices, or orders by more familiar ones.

## References

Birman, J. S., & Brendle, T. E. (2005). Braids: A survey. In W. Menasco & M. Thistlethwaite (Eds.), *Handbook of knot theory* (pp. 19–103). Elsevier. https://doi.org/10.1016/B978-044451452-3/50003-4. Author preprint: https://arxiv.org/abs/math/0409205

Grothendieck, A. (n.d.). *La “Longue Marche” à travers la théorie de Galois* [Handwritten draft, cote 140-1, supplied scans 1–19]. Université de Montpellier, Institut Montpelliérain Alexander Grothendieck. Source for the diplomatic transcription: the images supplied with this task; the catalogue cover's date information is discussed above.

Hain, R. (2014). *Lectures on moduli spaces of elliptic curves* (Version 3, arXiv:0812.1803) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.0812.1803
