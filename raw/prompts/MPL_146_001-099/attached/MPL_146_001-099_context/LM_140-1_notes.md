# ===== LM_C1-001-019 (first-pass notes) =====

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


# ===== LM_C1-020-037 (first-pass notes) =====

# LM_C1-020-037 — Editorial apparatus and research notes

## 1. Source, numbering, and editorial scope

The transcription is based on the 18 supplied JPEG images, whose filenames run from `LM_C1-020-037_scan020.jpg` to `LM_C1-020-037_scan037.jpg`. The task identifies them as Alexander Grothendieck’s *La Longue Marche à travers la théorie de Galois*, brouillon, Montpellier cote 140-1 (catalogued as 1981). The filename number is the `\scanpage` number: the archival folio visible on each image is one lower. The supplied catalogue year does not establish the date of every reused sheet or every mathematical addition.

The circled `7` on scan 20 is retained with `\mspage{7}`. The pencil folios 19–36 are retained with `\margin`, because their attribution and function are not certain. The modern Montpellier URL and address footer are archival apparatus and are excluded. The fragment begins with `\scanpage{20}` and contains no preamble or macro definitions. Standard mathematical LaTeX, TikZ, and tikz-cd are used together with the editorial macros specified in the task; a temporary wrapper defining those macros was used for compilation and visual checking and is not part of the deliverable.

### Whole-sheet exceptions explicitly permitted by the task

| Scan | Visible archival folio | Treatment |
|---|---|---|
| 22 | 21 | `% blank`; the marginal numeral is retained. |
| 24 | 23 | `% not manuscript`: the unrelated printed *Plurielles* film leaflet, with a diagonal stroke; its folio is retained. |
| 26 | 25 | `% not manuscript`: an unrelated printed research-sector classification sheet, headed by printed page number “− 4 −”; its folio is retained. |
| 28 | 27 | `% not manuscript`: the inverted printed thesis-defence notice concerning Yoon Suk-Im’s *Algèbres de Rees*; its folio is retained. |
| 37 | 36 | `% not manuscript`: the inverted, unfilled university thesis-defence form, “ANNEXE II”; its folio is retained. |

These sheets were inspected in full, including rotation where needed. The exception is not applied to mixed sheets: the postal label on scan 27 and the separate sideways billet on scan 34 are transcribed. The latter’s date and uncertain signature belong to that billet, not automatically to the mathematical writing.

Writing sectors with different orientations are read locally upright and retained in scan order. Large cancellation strokes are represented by encompassing `\deleted` groups; smaller cancellations inside them remain separately marked. The exact chronology of overlapping pen strokes is not asserted. Diagrams retain visible node and arrow data, including unfinished expressions, a literal question-mark node, apparent unmatched punctuation, and unexpected signs or inequalities. Layout spacing and label offsets prevent accidental typesetting collisions; they do not supply mathematical relations.

The large Teichmüller glyph is rendered as `\mathcal T` where that is the best reading, but its precise alphabet is not always secure. Doubled D-stems on scans 27 and 29 are rendered `\mathbb D`, whereas thinner forms on scan 31 are rendered ordinary D; this is a visual distinction, not an assertion that the author intended different groups. No published transcription was consulted. External literature cited in §5 was consulted only for a separately labelled research comparison and was not used to settle the French or mathematical readings.

## 2. Table of doubts

Positions refer to the supplied scan, except where a rotated writing sector is identified. Confidence concerns the reading, not the validity of its mathematics. A high-confidence entry can record a surprising but clear mark, such as the lower bar in `n≤6`; low confidence means that the proposed reading remains tentative. “No secure alternative” does not make the proposed reading certain. Repeated occurrences can be grouped here; §2.2 provides a locator for every explicit doubt marker in the final LaTeX.

### 2.1 Contextual register

| Scan | Approximate manuscript line or position | Reading | Alternatives or limitation | Confidence |
|---|---|---|---|---|
| 20 | Main group diagram, repeated glyph | `\mathcal T_{11}` | The handwriting resembles a large tau; the choice of calligraphic T is not fully determined by the pen form. | medium |
| 20 | Symmetric-group glyph in the two right-hand formulas | `\mathfrak S_3` | Script/calligraphic S is another possible alphabet. | medium |
| 20 | Upper-left main sequence, first character | `1` | Small dark mark; could be an unfinished endpoint stroke. | low |
| 20 | Above T_11, overwritten expression | `\Pi_{0,3}^{D}` | Several ink strokes overlap; only the Pi-like form and superscript are tentatively recoverable. | low |
| 20 | Above T_11, slanting underlined words | `identifié à` | Final strokes and attachment overlap the neighboring formula. | medium |
| 20 | Above T_11, small inserted product | `S\mathcal T_{11}\times_{\Pi_{0,3}^{D}}\mathbb Z/12\mathbb Z` | The product connector, subscript attachment, and final modulus are crowded. | low |
| 20 | Below rho_0, above sigma_0 | `\Pi_{0,3}` | Could be an attached subscript rather than a separate scribble. | low |
| 20 | rho tilde maps to 2, deleted glyph | `4` | Heavily overwritten numeral or letter before the final 2. | low |
| 20 | Upper-centre-right annotation | `pour T_11 identifié à` | First word may be `avec`; the ending of `identifié` is abbreviated. | low |
| 20 | Right-hand question, opening | `A-t-on bien` | The A is overwritten and the second word is highly cursive. | medium |
| 20 | Tiny label above Z-to-S T_11 line | `1 - omega bar = omega^2` | A mapsto head is not securely visible; plain dash is the primary reading, mapsto the alternative. | medium |
| 20 | D'3-to-D3 horizontal arrow | `cart` | `can`; the final pen stroke does not securely separate the two labels. | low |
| 20 | Immediately before PM_11 | `\mathcal T_{11}` (deleted) | Could instead be a crossed-out `que` or another abbreviated symbol. | low |
| 20 | Parenthesis below tangent | `PU_{0,3}` | The P is overwritten; the letters U and indices are clearer. | medium |
| 21 | Upper-left parameter array and conjugation equation | `g_i` | `q_i`; the descending loop changes form between occurrences. | medium |
| 21 | Three vertical membership signs, upper-left box | rotated `\in` | These are upward-facing membership signs; the smallest third one overlaps the subscript. | medium |
| 21 | Upper horizontal sequence | `\pi_1(\operatorname{Aut}(X)` | Only one right parenthesis is visible; the apparent unmatched parenthesis is retained, not supplied from expected syntax. | medium |
| 21 | Centre term in upper-left group diagram | `\mathfrak Z\pi` | `\mathfrak z\pi`; the initial glyph has a 3-like form. | low |
| 21 | Middle automorphism column | `\operatorname{Aut}^{+}_{!}(\widetilde X)` | Exclamation-mark subscript clear; the exact placement relative to Aut is cramped. | medium |
| 21 | Two-row extension, top-left term | `\widetilde F` | `\widehat F`; the accent is overwritten. | low |
| 21 | Two-row extension, bottom-left term | deleted `E`, inserted `F` | Several former strokes are superposed; the underlying letter may not be E. | low |
| 21 | Beside G | `\mathfrak S_n\ast\mathbb T^n` | Dot rather than star; no semidirect-product sign has been supplied. | low |
| 21 | Cancelled sentence below extension | `Op. ext. de pi_0 sur F` | Initial abbreviation has an overwritten first letter. | medium |
| 21 | Below pi_1-to-F arrow | `central` | Ending and precise attachment are abbreviated. | medium |
| 21 | Beside curved arrow to centre(F) | `compatible avec pi_0` | First letters intersect a diagonal cancellation. | medium |
| 21 | Lower-right sentence | `extérieurement` | Final syllables are reduced to a long cursive stroke. | medium |
| 21 | Both occurrences of centre(F) | `\mathfrak Z(F)` | `\mathfrak z(F)`; handwriting does not securely settle case/alphabet. | low |
| 21 | Lower-right crossed-out line | `compatible avec l’op. ext.` | The first word is extensively crossed; the remaining words are clearer. | low |
| 21 | Penultimate lower sequence, F | `F` | Lower serif or additional stroke is overwritten; no subscript has been inferred. | medium |
| 21 | Penultimate lower sequence, next-to-last term | `\pi_0` | `\pi_\infty`; the index has an extra loop. | low |
| 21 | Bottom sequence, initial two terms | deleted `1`, deleted `\pi_1` | Both are overwritten, particularly the second term. | low |
| 21 | Below penultimate-sequence pi_0 | Short diagonal slash | Retained beneath the node; it may be an unfinished connector, but no target or arrowhead is supplied. | medium |
| 21 | Large lower-left curved arrows | Arrow paths retained | Their exact textual attachment is less secure than the separate node labels. | low |
| 23 | First line, deleted adjective | `satisfaisant` | `strictement`; the long descender and first few strokes survive, but the middle is struck through. | low |
| 23 | After “Alors” | deleted `H^1` | The overwritten mathematical fragment is not fully recoverable. | low |
| 23 | Parenthesis about characteristic 2 | inserted `pt gén.` | `si gén.`; deletion below appears to read `résiduelle`. The relationship of these short strokes to the deleted word is crowded. | low |
| 23 | Diagonal margin heading | `Dém` | The acute accent and final m support Dém in three independent readings; the initial D has a number-like curl. | high |
| 23 | First marginal cohomology term | `H^1(S_3,H^0(U_03,G_m)` | The outer closing parenthesis is not securely visible and has not been silently supplied. | medium |
| 23 | Final nonzero term in second marginal sequence | `h_1(V(J))` | `h^1(V(J))`; the operator and the small stroke beside h are unclear. | low |
| 23 | Opening of “dis que si” | `Je` | The presumed opening word overlaps the diagonal margin; “dis que si” itself is clear. | low |
| 23 | Overwritten scheme name in definition | deleted `U_{0,3}`, inserted `Sigma_J` | The final Sigma_J is clearer than its cancelled predecessor. | low |
| 23 | At right edge after P(V_J) | `i.e.` | Only a dot and short cursive strokes are clearly resolved. | low |
| 23 | “fibré principal” | `principal` | Several medial and final letters are reduced to strokes. | medium |
| 23 | P Sigma definition | `\check V(\mathcal O_{\Sigma_J}(1))^*` | Sigma_J is written directly below O, inside the parentheses; attachment to O rather than to the outer V is supported by independent close readings. | medium |
| 23 | Generator cohomology arguments | `Sigma_J^*`, `S_J` | Replacements overlap cancelled U_03/S_3-like characters and a correction arrow. | medium |
| 23 | “Je vais d’abord ...” | `trouver` | The word is abbreviated by long connected strokes. | medium |
| 23 | Tensor-bundle comparison | `\mathcal T^{\otimes3}(\omega)` | `\mathcal J^{\otimes3}(\omega)`; the long descending loop does not settle the letter. | low |
| 23 | Slanting insertion below O(6) | `sur Sigma bar tout entier` | The final two words are compressed; no grammatical correction to “toute entière” is made. | low |
| 23 | Deleted parenthetical clause | `ne s’annule que` | The horizontal strike starts after the retained `(qui`; the rising line above qui is treated as an insertion connector. No closing parenthesis is securely visible. | low |
| 23 | Insertion above deleted clause | `est, inversible` | Comma and the final ending of inversible are uncertain. | low |
| 23 | Before Gamma display | deleted `prenant` | Could be `prend`; the ending is struck out. | low |
| 23 | Product section, first two triangular symbols | `\varphi` | `\Delta`; these two symbols have a long descending stem, unlike the clear final Delta in the NB. | medium |
| 23 | Deleted term after product symbol equals | `sum_{i in J}` | The index and crossed summation sign are overwritten. | low |
| 23 | “groupe structural” | `structural` | `structurel`; final letters are compressed. | medium |
| 23 | After “groupe structural” | deleted `de` | Small overwritten word. | low |
| 23 | Lower Sigma_J and P Sigma_J superscripts | `*` | `\wedge`; only two or three strokes are visible. | low |
| 23 | Before invariant algebra | deleted `Sym` | Struck through and retraced. | low |
| 23 | Two generators inside O(...) | `gamma_2`, `gamma_3` | `varphi_2`, `varphi_3`; both letters are overwritten. | low |
| 23 | Gamma_3 product, first sign | minus | plus; the visible horizontal stroke supports minus, and no correction from expected invariant theory is made. | medium |
| 25 | First crossed line, initial word | `Si` | The initial letter and following short stroke are traversed by the cancellation. | medium |
| 25 | First crossed line, after 2 | `inversible` | Several medial letters are hidden by the strike, though the final tall loop and ending survive. | medium |
| 25 | First crossed line, after on | `aura donc` | The two groups of reduced cursive strokes are not securely resolved. | low |
| 25 | Crossed invariant-algebra display | `W_J` | `V_J`; the letter has two visible troughs, favouring W. No surrounding parentheses are securely visible. | low |
| 25 | Same display, group index | `J` | `3`; the small group index is crossed by the long cancellation. | low |
| 25 | Same display, final expression | `O[` | The expression stops after the opening square bracket; no missing generators or closing bracket are supplied. | high |
| 25 | Short crossed line below display | `Remarque` | The first two letters and a final tall stroke are visible, but most of the word is struck through. The final stroke may be t, which weakens the proposed complete reading; no firm alternative is resolved. | low |
| 25 | After first en | deleted `les` | The thick horizontal stroke obscures the final letters. | medium |
| 25 | First vanishing point | `P_omega` | `P_m`; the subscript is a shallow two-lobed form with no clear dot. | low |
| 25 | After O(n)* and before sur | deleted `pour` | A p-like initial descender and rounded terminal stroke support this very tentative reading; mathematical notation cannot be excluded. | low |
| 25 | First Sigma_J superscript | `*` | Wedge; this mark is more wedge-like than the distinct star on O(n)*. | low |
| 25 | Deleted words after Sigma_J | `en degré <` | The words are struck through; the final less-than sign is clearer. | medium |
| 25 | Bound on n | `n <= 6` | The separate lower bar is visible. The weak inequality is retained even though it raises a question when compared with the preceding degree-six construction. | high |
| 25 | After ce qui | `prouve` | The middle and ending are reduced to separated cursive strokes. | medium |
| 25 | Last line before mixte | `H^1` | The H is retraced and the superscript is cramped. | medium |
| 27 | Upper-right square, lower-left node | `M_{11}(\widetilde{2}^{\sim})` | `M_{11}(2^{\sim})`; two separate small strokes around 2 may be retracing rather than two marks | low |
| 27 | Upper-right square, lower-right equality | `M_{11}(2)` | The small argument resembles an n-shaped numeral; no different argument secure | medium |
| 27 | Short cancelled map below square | `x` | Beginning is heavily overwritten; no alternative secure | low |
| 27 | Same cancelled map, target | `x^2\wedge\omega_0` | The operator between the power and the last symbol may be a lambda-like mark; entire target is doubtful | low |
| 27 | Display below the cancelled map | `H^1(TU_{03},\mathbb D_3;\mu_2)` | Initial superscript is poorly separated from H | medium |
| 27 | Middle-left diagram, first diagonal label, deleted | `\mathcal D/\Pi_{0,3}` | The prefix and fraction stroke are overwritten | low |
| 27 | Middle-left diagram, after upper-right `M_{11}(2)` | `-` | Prime | low |
| 27 | Middle-right diagram, two downward labels | `gerbe` | Last letters run together; no alternative secure | medium |
| 27 | Bottom-left diagram, crossed label near upper diagonal | `{1,\omega}` | Deleted strokes overlap the D-label | low |
| 27 | Bottom-left diagram, right downward label | `2-gerbe`, with `gerbe` underlined | Initial mark may be another short prefix; the reading as the numeral 2 is uncertain | low |
| 27 | Bottom-left diagram, left downward label | `2-gerbe` | Same doubtful initial mark as the other downward label | low |
| 27 | Bottom-left diagram, two group names | `Sl(2,\mathbb Z)` | Capitalization of l/L is not securely distinguishable | medium |
| 29 | Cancelled top graph, label on its top incoming arrow | `''` | `1`; two short upright strokes | low |
| 29 | Cancelled top graph, left upper object | `\widetilde\varepsilon` | `\widetilde E` | low |
| 29 | Cancelled top graph, first fibre product | `\mathbb Z/12\mathbb Z` | Middle strokes can also resemble n; numeral 12 is the best reading | medium |
| 29 | Cancelled top graph, subscript of second fibre product | `\mathbb Z/2\mathbb Z` | Slash and numeral overlap; not silently supplied from the preceding product | medium |
| 29 | Cancelled top graph, final object after equality | `\varepsilon` | `E` | medium |
| 29 | Cancelled top graph, lower-left D-object | `\widetilde{\mathbb D}_3^{*}` | `\widetilde{\mathbb D}'_3`; overwritten superscript may be a sharp-like mark | low |
| 29 | Cancelled top graph, long horizontal line from the upper Z | An unheaded line | A worn arrowhead cannot be excluded; the ink does not securely support one | low |
| 29 | Central graph, upper-left object | `\mathbb Z_{(\omega/2)}` | The 2 could instead label the downward arrow; the parenthesis/fraction arrangement is difficult | low |
| 29 | Central graph, first lifted Pi-node | Superscript `\circ` | Small filled mark, possibly 0 | low |
| 29 | Central graph, faint overwritten object after that node | `\widetilde\Pi_{0,3}` | Subscript is very faint beneath the horizontal stroke | low |
| 29 | Central graph, second lifted Pi-node | Superscript prime | Small grey stroke might be another annotation | low |
| 29 | Central graph, beneath `\mathbb D''_3` | `12` | `10`; pale earlier annotation | low |
| 29 | Left of the final Z in the central graph | `fond` | `bon`; short crowded word | low |
| 29 | Central graph, between Z/12Z and Z/6Z | Bidirectional horizontal arrow, label 2 | Two oppositely directed heads appear on separated stretches of the line; no algebraic interpretation is imposed | medium |
| 29 | Lower two-row sequence, downward Z-map | A second `4` below the clear 4 | May be a repeated pen stroke rather than a separate annotation | low |
| 29 | Bottom row, group at the right of the literal `?` | `Sl(2,\mathbb Z)` | First letters have been retraced | medium |
| 30 | Top line, cancelled mark after `V_J` | `\simeq` | Could be a failed initial symbol rather than a completed relation | low |
| 30 | Top-line insertion | `\Gamma(X,\uline{\mathcal O}(1))` | Opening parenthesis merges with the Gamma-like letter; the underline on O is visible | low |
| 30 | Top line | `engendré` | Final letters compressed | medium |
| 30 | Cancelled expression starting next line | `\Pi(e_i-e_j)` | `P(e_i-e_j)`; initial letter is crossed and retraced | low |
| 30 | Upper prose, first word | `comment` | Several medial letters are only strokes | medium |
| 30 | Upper prose | `sections` | Final letters compressed | medium |
| 30 | Upper prose | `sont` | Short word represented by a low connected stroke | low |
| 30 | Upper prose, following line | `permutées` | Several retraced letters; no secure alternative | low |
| 30 | Cancelled display left of `e_i-e_j=` | `\mathcal O(6)` | `\mathcal O(1)` | low |
| 30 | Isolated symbol below that display | `\xi_i.` | Subscript and final point not fully separated | low |
| 30 | Upper-right calculation, fibre notation | `\uline{\mathcal O}_x(1)` | Subscript a | low |
| 30 | Below the same fibre notation | Vertically oriented `\in` | Shape resembles a small upsilon/psi because of orientation | medium |
| 30 | Middle-left extension, subscript of lifted Pi | `03` | Small compressed loop; no comma confidently visible | low |
| 30 | Same extension, superscript of unlifted Pi | `\sharp` | `\ast`; superscript is overdrawn | low |
| 30 | Middle-right evaluation, underlined point | `Q_n` | `Q_k`; the Q-like glyph is highly cursive | low |
| 30 | Crossed expression beneath that evaluation | `e_i-e_j` | Middle strokes are obscured by cancellation | low |
| 30 | Expression above the small numerical array | `e_i-e_j(Q_k` | The Q-like symbol is cancelled; no closing parenthesis is securely visible and none was added | low |
| 30 | Lower, rotated, first sentence: deletion | `surface` | Most of the first half is concealed by the cancellation | low |
| 30 | Lower, rotated, above first sentence | `cellulation` | `cellulaire`; placed after the deleted noun and before “combinatoire” | low |
| 30 | Lower, rotated, beginning of second line | `donne` | Medial letters reduced to strokes | medium |
| 30 | Lower, rotated, after “lieu” | `à` | Colon | low |
| 30 | Lower, rotated, first paragraph and question | `opérateurs` | `opérations`; the ending is uncertain | low |
| 30 | Lower, rotated, before first displayed relation | `satisfaisant` | Final inflection is only a short stroke | medium |
| 30 | Lower, rotated, orientation question | `quels` | `quelles` | low |
| 30 | Lower, rotated, orientation question | `correspondants` | `correspondantes` | low |
| 30 | Lower, rotated, two occurrences before representatives | `provient` | Final t/n/t strokes are compressed | medium |
| 30 | Lower, rotated, repeated involution subscript | `m` | `n`; every occurrence is marked, and the choice was not derived from an expected presentation | low |
| 30 | Lower, rotated, before “la classe” | `donc` | Final letters reduced to a wavering line | medium |
| 30 | Lower, rotated, before “t on a donc” | Deleted `E` | A heavily retraced initial E may not be an intentional deletion | low |
| 30 | Lower, rotated, last parenthesis | `plaisant` | Ending almost entirely a horizontal stroke | low |
| 30 | Lower, rotated, transverse right marginal note, first term | `\widetilde Q_m` | `\widetilde R_m`; initial glyph and subscript both uncertain | low |
| 30 | Same marginal note, second term | `\widetilde Q_j` | `\widetilde R_j` | low |
| 30 | Transverse note, cancelled initial symbol on second line | `\xi` | No alternative secure | low |
| 30 | Transverse note, second line | `\gamma_h\ i\gamma_h` | Gamma-like glyphs and their subscripts are not securely identified | low |
| 30 | Transverse difference calculation | `=` | A separate equality sign is not securely resolved from the short strokes | low |
| 30 | Same calculation, last subscript | `j` | `n` | low |
| 31 | Top cancelled sequence, lower target | `D''_3` | Initial part of D is heavily overwritten | low |
| 31 | Upper kernel equality, after the right `\Pi_0` | Raised point | Prime | low |
| 31 | Main graph, lifted D subscript | `3` | `0` | low |
| 31 | Above the middle exact sequence, cancelled symbol before Z | `\widetilde\Pi` | Mark above Pi is crowded by cancellation | low |
| 31 | Middle sequence, cancelled lower branch | `D_3` | Stem and subscript are crossed through | low |
| 31 | Bottom display between Pi-prime and Pi | `\subset` | Leftward arrow | low |
| 31 | Bottom-left cancelled product, first factor | `\widetilde\Pi` | Tilde and letter partially overwritten | low |
| 31 | Same cancelled product, final factor | `\mathbb Z/4` | `\mathbb Z/4\mathbb Z`; no separate terminal Z is securely resolved | low |
| 32 | 1, over « construction » | inserted « ne » | abbreviated correction, attachment uncertain | low |
| 32 | 1 | « peut se continuer indéfiniment » | compressed word endings | medium |
| 32 | 2–3 | « on pose alors σa_n = ρa_0 » | final index on a may be n rather than 0 | medium |
| 32 | 4 | « se prolonge indéfiniment » | compressed final letters | medium |
| 32 | 5, deleted parenthesis | « soit que l'on ... a un cycle fini » with « donc » added | wording heavily obscured by cancellation | low |
| 32 | 6 | « ou un cycle infini » | finite/infinite cycle wording | low |
| 32 | 6 | « On ne définit pas ρâ alors » | a rather than â; entire clause compressed | low |
| 32 | upper left marginal bracket | « notion de connexité définie dans un sens restreint » | individual words uncertain | low |
| 32 | 7 | « prolongé », replacing « défini » | annotation is compressed and overlaps the cancellation | low |
| 32 | 7–8 | « sur tt A et que = pour l'orientation inverse » | « tt » or quantifier; the short sign after « que » uncertain | low |
| 32 | 9 | « propriétés combinatoires » | word ending compressed | medium |
| 32 | 10 | « autom. » | « action » | low |
| 32 | 10–11 | bar S and hat S; subset sign | equality sign in the latter position | low |
| 32 | 12 | « compactifier partiellement X en X̂ » | Final letters remain faint; « compléter ponctuellement » is less well supported by the enlarged strokes. | medium |
| 32 | 13–14 | « ajoutant les pts ... (ainsi que : K°) » | K° and inserted Π₀,₃ reading uncertain | low |
| 32 | 14–16 | « l'image inverse Â′ ... contient A′ et ... st. ∀ par ρ et σ » | short stability notation uncertain | low |
| 32 | 16–17, cancellation and insertion | « mais n’est pas néc. égal à A′ »; inserted « A tt entier » | « ce n’est pas »; « avec »; inserted « A est entier ». The longer reading « A est engendré par A′ » is not supported and is not in the transcription. | low |
| 32 | lower left circled note | « st. liberté de l'action en passant de A′ : Â′ ? » | question and relation sign uncertain | low |
| 32 | 18–20 | « satisfaisant ... doivent ... s’identifier » | « s’identifient »; the short word tentatively read « doivent » is not secure, so it does not settle the following ending. | medium |
| 32 | 21 | « ens. quelc. » | final abbreviated word uncertain | medium |
| 32 | 23 | « On retrouve A′ comme l'ens des él. » | « retrouve » compressed | medium |
| 33 | top diagram, downward arrow to Z/qZ | « nul sur Π̃₀, can sur Zω̄ » | short words and placement of bar uncertain | medium |
| 33 | top right, deleted formula | β ∈ (Z/qZ)* | initial letter heavily crossed | low |
| 33 | middle diagram, bottom horizontal arrow | q | tiny superscript-like label could be two strokes rather than q | low |
| 33 | deleted heading above class formula | « L'extension est [one unreadable word] : » | heavy cancellation makes final word unrecoverable | low |
| 33 | extension-class formulas | ζ, ζ′ | ξ, ξ′ | low |
| 33 | first class formula | Ext¹ with deleted Z subscript | power/subscript interwoven with correction | low |
| 33 | pullback formula | cl(Π̃₀(q)) followed by prime | cl(Π̃₀ q); final small stroke possibly punctuation | medium |
| 33 | bottom right and final left formula | δ* | δ′ | medium |
| 34 | top deleted line | « 4) SL̃(2,Z) ≃ T₁,₁ SL Π » | heavily overwritten group symbols; initial number uncertain | low |
| 34 | top identity, fibre-product subscript | Z/6Z | first Z overwritten | medium |
| 34 | below top identity, small cancelled symbol | α | scribble has no certain recovery | low |
| 34 | inverted network, branch from top edge | Π → D₃″ → Z/ | final quotient label unfinished; double stroke on D uncertain | low |
| 34 | inverted network, separate right-hand label | Π₀ × 7 | Π₀ × 1 | low |
| 34 | inverted lower square | underlined « cart » | « can » | medium |
| 34 | sideways reused-paper note, signature | R. Boucher | surname uncertain | low |
| 35 | numeric specialization, crossed symbols | p; p′+ | overwritten remnants | low |
| 35 | below circled −α | cancelled φ | partly overwritten symbol | low |
| 35 | prose beside residue map | « revêt » plus cancelled « ement » | abbreviation or cancelled ending unclear | low |
| 35 | prose, last two lines | « multisection canonique de O_U(4)* » | « multiplication »; numeral 1; earlier deleted O(1) notation uncertain | medium |
| 35 | left inclusion diagram, lower label | μ₆-revᵗ | superscript or overwritten end of « revêt » | low |
| 35 | left inclusion diagram, isolated mark | + | small ink stroke not certainly a plus | low |
| 35 | central diagram, bottom horizontal arrow | equality label | short bar may be part of retraced arrow | low |
| 35 | lower left cancelled formula | Π̃₀,₃ᴰ Z/4Z → | symbols heavily crossed; no recovery of a connecting operation | low |
| 35 | generator definitions near foot | ρ̃♯ and σ̃♯ | primed generators, or another superscript | low |
| 35 | last presentation, underbrace | ω′⁻¹ = ω | ω̃⁻¹ = ∞; annotation heavily overwritten | low |
| 35 | last presentation, cancelled clause | ω ∈ Z | fully overdrawn initial relation sign | low |
| 36 | above first Z | ω′ = ω⁻¹ | ω′ = ω̄′; superscript placement favours inverse | medium |
| 36 | after presentation above SΠ₀,₃ᴰ | cancelled ω | cancelled ∞ or further central-symbol annotation | low |
| 36 | upper-right NB, first factor | dotted ω̄⁴ | ω̄⁴ with stray dot above the bar | low |
| 36 | upper-right NB, central factor | ω⁻¹ | overwritten omega may have additional decoration | medium |
| 36 | after final ω′ in NB | cancelled ω | no certain recovery of overdrawn symbol | low |
| 35 | very pale marks immediately right of residue rows | Γ / √, ξ₀′ / ξ₀, t′r / t′h | may be verso show-through or erased pencil; not attributed to the front-page argument | low |

### 2.2 Locator index of explicit uncertainty marks

This index is exhaustive for `\unsure` and `\illegible` in the delivered fragment. “LaTeX line” identifies the physical line of that file, not a reconstructed manuscript line; use the scan and contextual register above for the manuscript location. Contents are recorded literally, so a vertical bar separates proposed readings as specified in the task. The single `\illegible{1}` concerns a deleted prose word on scan 33, not a mathematical symbol.

| Scan | LaTeX line | Macro | Literal contents |
|---|---|---|---|
| 20 | 15 | `\unsure` | `\Pi_{0,3}^{D}` |
| 20 | 16 | `\unsure` | `identifié à` |
| 20 | 17 | `\unsure` | `S\mathcal T_{11}\times_{\Pi_{0,3}^{D}}\mathbb Z/12\mathbb Z` |
| 20 | 23 | `\unsure` | `\Pi_{0,3}` |
| 20 | 28 | `\unsure` | `1` |
| 20 | 29 | `\unsure` | `-\|\mapsto` |
| 20 | 30 | `\unsure` | `4` |
| 20 | 36 | `\unsure` | `cart\|can` |
| 20 | 46 | `\unsure` | `pour` |
| 20 | 46 | `\unsure` | `identifié à` |
| 20 | 49 | `\unsure` | `A-t-on` |
| 20 | 49 | `\unsure` | `bien` |
| 20 | 54 | `\unsure` | `\mathcal T_{11}` |
| 20 | 58 | `\unsure` | `PU_{0,3}` |
| 21 | 72 | `\unsure` | `g_i\|q_i` |
| 21 | 80 | `\unsure` | `g_i\|q_i` |
| 21 | 80 | `\unsure` | `g_i\|q_i` |
| 21 | 91 | `\unsure` | `\mathfrak Z\pi\|\mathfrak z\pi` |
| 21 | 124 | `\unsure` | `\widetilde F\|\widehat F` |
| 21 | 125 | `\unsure` | `E` |
| 21 | 126 | `\unsure` | `\ast\|\cdot` |
| 21 | 130 | `\unsure` | `Op.` |
| 21 | 133 | `\unsure` | `compatible` |
| 21 | 134 | `\unsure` | `\mathfrak Z(F)\|\mathfrak z(F)` |
| 21 | 136 | `\unsure` | `central` |
| 21 | 138 | `\unsure` | `extérieurement` |
| 21 | 139 | `\unsure` | `\mathfrak Z(F)\|\mathfrak z(F)` |
| 21 | 145 | `\unsure` | `compatible` |
| 21 | 157 | `\unsure` | `F` |
| 21 | 157 | `\unsure` | `\pi_0\|\pi_\infty` |
| 21 | 161 | `\unsure` | `1` |
| 21 | 161 | `\unsure` | `\pi_1` |
| 23 | 172 | `\unsure` | `satisfaisant\|strictement` |
| 23 | 174 | `\unsure` | `H^1` |
| 23 | 178 | `\unsure` | `résiduelle` |
| 23 | 178 | `\unsure` | `pt gén.\|si gén.` |
| 23 | 180 | `\unsure` | `Dém` |
| 23 | 187 | `\unsure` | `h_1(V(J))\|h^1(V(J))` |
| 23 | 190 | `\unsure` | `Je` |
| 23 | 191 | `\unsure` | `U_{0,3}` |
| 23 | 191 | `\unsure` | `i.e.` |
| 23 | 195 | `\unsure` | `principal` |
| 23 | 200 | `\unsure` | `U_{0,3}` |
| 23 | 201 | `\unsure` | `\mathfrak S_3` |
| 23 | 203 | `\unsure` | `trouver` |
| 23 | 206 | `\unsure` | `\mathcal T^{\otimes3}(\omega)\|\mathcal J^{\otimes3}(\omega)` |
| 23 | 209 | `\unsure` | `tout entier` |
| 23 | 210 | `\unsure` | `ne s'annule que` |
| 23 | 211 | `\unsure` | `est` |
| 23 | 211 | `\unsure` | `inversible` |
| 23 | 212 | `\unsure` | `prenant` |
| 23 | 219 | `\unsure` | `\varphi\|\Delta` |
| 23 | 220 | `\unsure` | `\varphi\|\Delta` |
| 23 | 221 | `\unsure` | `\sum_{i\in J}` |
| 23 | 226 | `\unsure` | `U_J` |
| 23 | 226 | `\unsure` | `*\|\wedge` |
| 23 | 226 | `\unsure` | `structural\|structurel` |
| 23 | 227 | `\unsure` | `de` |
| 23 | 228 | `\unsure` | `*\|\wedge` |
| 23 | 232 | `\unsure` | `\operatorname{Sym}` |
| 23 | 234 | `\unsure` | `\gamma_2\|\varphi_2` |
| 23 | 234 | `\unsure` | `\gamma_3\|\varphi_3` |
| 23 | 240 | `\unsure` | `-\|+` |
| 25 | 253 | `\unsure` | `Si` |
| 25 | 253 | `\unsure` | `inversible` |
| 25 | 253 | `\unsure` | `aura` |
| 25 | 253 | `\unsure` | `donc` |
| 25 | 255 | `\unsure` | `W_J\|V_J` |
| 25 | 255 | `\unsure` | `J\|3` |
| 25 | 257 | `\unsure` | `Remarque` |
| 25 | 259 | `\unsure` | `les` |
| 25 | 259 | `\unsure` | `\omega\|m` |
| 25 | 261 | `\unsure` | `pour` |
| 25 | 262 | `\unsure` | `*\|\wedge` |
| 25 | 262 | `\unsure` | `en degré` |
| 25 | 266 | `\unsure` | `prouve` |
| 25 | 267 | `\unsure` | `H^1` |
| 27 | 292 | `\unsure` | `\widetilde{2}^{\sim}\|2^{\sim}` |
| 27 | 294 | `\unsure` | `2` |
| 27 | 299 | `\unsure` | `x` |
| 27 | 299 | `\unsure` | `x^2\wedge\omega_0` |
| 27 | 302 | `\unsure` | `H^1` |
| 27 | 307 | `\unsure` | `\mathcal D/\Pi_{0,3}` |
| 27 | 308 | `\unsure` | `-\|'` |
| 27 | 316 | `\unsure` | `\mathrm{gerbe}` |
| 27 | 317 | `\unsure` | `\mathrm{gerbe}` |
| 27 | 328 | `\unsure` | `\{1,\omega\}` |
| 27 | 329 | `\unsure` | `2\text{-}\uline{\mathrm{gerbe}}` |
| 27 | 330 | `\unsure` | `\mathrm{Sl}(2,\mathbb Z)` |
| 27 | 331 | `\unsure` | `2\text{-}\mathrm{gerbe}` |
| 27 | 334 | `\unsure` | `\mathrm{Sl}(2,\mathbb Z)` |
| 29 | 346 | `\unsure` | `''\|1` |
| 29 | 349 | `\unsure` | `\widetilde\varepsilon\|\widetilde E` |
| 29 | 352 | `\unsure` | `12` |
| 29 | 353 | `\unsure` | `2` |
| 29 | 357 | `\unsure` | `\varepsilon\|E` |
| 29 | 363 | `\unsure` | `\widetilde{\mathbb D}_3^{*}\|\widetilde{\mathbb D}'_3` |
| 29 | 376 | `\unsure` | `\mathbb Z_{(\omega/2)}` |
| 29 | 377 | `\unsure` | `\circ` |
| 29 | 378 | `\unsure` | `\widetilde\Pi_{0,3}` |
| 29 | 382 | `\unsure` | `'` |
| 29 | 394 | `\unsure` | `12\|10` |
| 29 | 403 | `\unsure` | `fond\|bon` |
| 29 | 407 | `\unsure` | `4` |
| 29 | 433 | `\unsure` | `\mathrm{Sl}(2,\mathbb Z)` |
| 30 | 442 | `\unsure` | `\simeq` |
| 30 | 442 | `\unsure` | `\Gamma(X,\uline{\mathcal O}(1))` |
| 30 | 443 | `\unsure` | `engendré` |
| 30 | 445 | `\unsure` | `\Pi(e_i-e_j)\|P(e_i-e_j)` |
| 30 | 446 | `\unsure` | `comment` |
| 30 | 446 | `\unsure` | `sections` |
| 30 | 446 | `\unsure` | `sont` |
| 30 | 447 | `\unsure` | `permutées` |
| 30 | 466 | `\unsure` | `\mathcal O(6)\|\mathcal O(1)` |
| 30 | 470 | `\unsure` | `\xi_i` |
| 30 | 474 | `\unsure` | `\uline{\mathcal O}_x(1)\|\uline{\mathcal O}_a(1)` |
| 30 | 474 | `\unsure` | `\in` |
| 30 | 481 | `\unsure` | `03` |
| 30 | 482 | `\unsure` | `\sharp\|\ast` |
| 30 | 487 | `\unsure` | `Q_n\|Q_k` |
| 30 | 488 | `\unsure` | `e_i-e_j` |
| 30 | 494 | `\unsure` | `Q_k` |
| 30 | 510 | `\unsure` | `surface` |
| 30 | 511 | `\unsure` | `cellulation\|cellulaire` |
| 30 | 512 | `\unsure` | `donne` |
| 30 | 512 | `\unsure` | `à\|:` |
| 30 | 512 | `\unsure` | `opérateurs\|opérations` |
| 30 | 513 | `\unsure` | `satisfaisant` |
| 30 | 518 | `\unsure` | `quels\|quelles` |
| 30 | 519 | `\unsure` | `opérateurs\|opérations` |
| 30 | 519 | `\unsure` | `correspondants\|correspondantes` |
| 30 | 521 | `\unsure` | `provient` |
| 30 | 522 | `\unsure` | `provient` |
| 30 | 522 | `\unsure` | `m\|n` |
| 30 | 524 | `\unsure` | `m\|n` |
| 30 | 525 | `\unsure` | `m\|n` |
| 30 | 526 | `\unsure` | `m\|n` |
| 30 | 526 | `\unsure` | `m\|n` |
| 30 | 527 | `\unsure` | `m\|n` |
| 30 | 528 | `\unsure` | `m\|n` |
| 30 | 530 | `\unsure` | `donc` |
| 30 | 530 | `\unsure` | `m\|n` |
| 30 | 533 | `\unsure` | `E` |
| 30 | 535 | `\unsure` | `m\|n` |
| 30 | 536 | `\unsure` | `m\|n` |
| 30 | 537 | `\unsure` | `m\|n` |
| 30 | 537 | `\unsure` | `m\|n` |
| 30 | 538 | `\unsure` | `m\|n` |
| 30 | 550 | `\unsure` | `plaisant` |
| 30 | 556 | `\unsure` | `\widetilde Q_m\|\widetilde R_m` |
| 30 | 557 | `\unsure` | `\widetilde Q_j\|\widetilde R_j` |
| 30 | 560 | `\unsure` | `\xi` |
| 30 | 560 | `\unsure` | `\gamma_h\ i\gamma_h` |
| 30 | 563 | `\unsure` | `=` |
| 30 | 563 | `\unsure` | `j\|n` |
| 31 | 577 | `\unsure` | `D''_3` |
| 31 | 582 | `\unsure` | `.` |
| 31 | 588 | `\unsure` | `3\|0` |
| 31 | 603 | `\unsure` | `\widetilde\Pi` |
| 31 | 612 | `\unsure` | `D_3` |
| 31 | 632 | `\unsure` | `\subset\|\leftarrow` |
| 31 | 635 | `\unsure` | `\widetilde\Pi` |
| 31 | 635 | `\unsure` | `\mathbb Z/4\|\mathbb Z/4\mathbb Z` |
| 32 | 647 | `\unsure` | `ne` |
| 32 | 647 | `\unsure` | `peut` |
| 32 | 647 | `\unsure` | `indéfiniment` |
| 32 | 648 | `\unsure` | `pose` |
| 32 | 651 | `\unsure` | `indéfiniment` |
| 32 | 653 | `\unsure` | `soit que` |
| 32 | 653 | `\unsure` | `l'on` |
| 32 | 653 | `\unsure` | `donc` |
| 32 | 653 | `\unsure` | `a un cycle fini` |
| 32 | 653 | `\unsure` | `ou un` |
| 32 | 654 | `\unsure` | `infini` |
| 32 | 654 | `\unsure` | `définit` |
| 32 | 654 | `\unsure` | `\widehat a\|a` |
| 32 | 654 | `\unsure` | `alors` |
| 32 | 657 | `\unsure` | `notion de connexité` |
| 32 | 657 | `\unsure` | `définie dans un` |
| 32 | 657 | `\unsure` | `sens restreint` |
| 32 | 662 | `\unsure` | `défini` |
| 32 | 662 | `\unsure` | `prolongé` |
| 32 | 662 | `\unsure` | `tt` |
| 32 | 663 | `\unsure` | `$=$` |
| 32 | 663 | `\unsure` | `inverse` |
| 32 | 664 | `\unsure` | `combinatoires` |
| 32 | 665 | `\unsure` | `autom.` |
| 32 | 665 | `\unsure` | `\overline S` |
| 32 | 666 | `\unsure` | `\subset\|=` |
| 32 | 667 | `\unsure` | `compactifier` |
| 32 | 667 | `\unsure` | `partiellement` |
| 32 | 667 | `\unsure` | `$\overline X$` |
| 32 | 668 | `\unsure` | `ajoutant` |
| 32 | 669 | `\unsure` | `K^\circ` |
| 32 | 669 | `\unsure` | `$\simeq\Pi_{0,3}$` |
| 32 | 670 | `\unsure` | `contient $A'$ et` |
| 32 | 671 | `\unsure` | `st.` |
| 32 | 671 | `\unsure` | `$\forall$` |
| 32 | 672 | `\unsure` | `n'est pas\|ce n'est pas` |
| 32 | 672 | `\unsure` | `à\|avec` |
| 32 | 673 | `\unsure` | `tt entier\|est entier` |
| 32 | 676 | `\unsure` | `st. liberté de l'action` |
| 32 | 676 | `\unsure` | `en passant de` |
| 32 | 685 | `\unsure` | `satisfaisant` |
| 32 | 686 | `\unsure` | `doivent` |
| 32 | 687 | `\unsure` | `s'identifier\|s'identifient` |
| 32 | 687 | `\unsure` | `triples` |
| 32 | 688 | `\unsure` | `quelc.` |
| 32 | 690 | `\unsure` | `retrouve` |
| 33 | 698 | `\unsure` | `nul sur ` |
| 33 | 698 | `\unsure` | `can sur ` |
| 33 | 703 | `\unsure` | `\beta` |
| 33 | 708 | `\unsure` | `q` |
| 33 | 717 | `\unsure` | `L'extension est` |
| 33 | 717 | `\illegible` | `1` |
| 33 | 719 | `\unsure` | `\zeta'\|\xi'` |
| 33 | 719 | `\unsure` | `\zeta\|\xi` |
| 33 | 721 | `\unsure` | `1` |
| 33 | 721 | `\unsure` | `\mathbb Z` |
| 33 | 725 | `\unsure` | `=` |
| 33 | 726 | `\unsure` | `\zeta'\|\xi'` |
| 33 | 728 | `\unsure` | `(q)\|q` |
| 33 | 728 | `\unsure` | `\zeta\|\xi` |
| 33 | 729 | `\unsure` | `'` |
| 33 | 732 | `\unsure` | `\zeta\|\xi` |
| 33 | 739 | `\unsure` | `\zeta'\|\xi'` |
| 33 | 741 | `\unsure` | `*\|' ` |
| 33 | 742 | `\unsure` | `*\|'` |
| 34 | 748 | `\unsure` | `4)` |
| 34 | 748 | `\unsure` | `\widetilde{\mathrm{SL}}` |
| 34 | 749 | `\unsure` | `\mathcal T_{1,1}` |
| 34 | 749 | `\unsure` | `\mathrm{SL}` |
| 34 | 749 | `\unsure` | `\Pi` |
| 34 | 758 | `\unsure` | `\mathbb Z/6\mathbb Z` |
| 34 | 762 | `\unsure` | `\alpha` |
| 34 | 770 | `\unsure` | `\Pi` |
| 34 | 773 | `\unsure` | `\mathbb Z/` |
| 34 | 776 | `\unsure` | `7\|1` |
| 34 | 779 | `\unsure` | `cart` |
| 34 | 790 | `\unsure` | `Boucher` |
| 35 | 801 | `\unsure` | `p` |
| 35 | 804 | `\unsure` | `p'+` |
| 35 | 825 | `\unsure` | `\varphi` |
| 35 | 827 | `\unsure` | `\Gamma\|\sqrt{\phantom{x}}` |
| 35 | 827 | `\unsure` | `\xi_0\prime\|\xi_0` |
| 35 | 827 | `\unsure` | `t\prime r\|t\prime h` |
| 35 | 830 | `\unsure` | `revêt` |
| 35 | 830 | `\unsure` | `ement` |
| 35 | 832 | `\unsure` | `multisection\|multiplication` |
| 35 | 833 | `\unsure` | `\mathcal O(1)` |
| 35 | 833 | `\unsure` | `4\|1` |
| 35 | 839 | `\unsure` | `(1)` |
| 35 | 841 | `\unsure` | `\mathrm{rev}^{\mathrm t}` |
| 35 | 841 | `\unsure` | `+` |
| 35 | 844 | `\unsure` | `\longrightarrow` |
| 35 | 849 | `\unsure` | `=` |
| 35 | 860 | `\unsure` | `\widetilde\Pi_{0,3}^D` |
| 35 | 860 | `\unsure` | `\mathbb Z/4\mathbb Z` |
| 35 | 863 | `\unsure` | `\sharp\|'` |
| 35 | 864 | `\unsure` | `\sharp` |
| 35 | 864 | `\unsure` | `\sharp` |
| 35 | 865 | `\unsure` | `\sharp\|'` |
| 35 | 872 | `\unsure` | `\omega'^{-1}\|\widetilde\omega^{-1}` |
| 35 | 872 | `\unsure` | `\omega\|\infty` |
| 35 | 873 | `\unsure` | `\omega\in\mathbb Z` |
| 36 | 880 | `\unsure` | `\omega\|\infty` |
| 36 | 881 | `\unsure` | `\omega^{-1}\|\overline\omega'` |
| 36 | 886 | `\unsure` | `\dot{\overline\omega}\|\overline\omega` |
| 36 | 886 | `\unsure` | `\omega^{-1}` |
| 36 | 887 | `\unsure` | `\omega` |

## 3. Abbreviations met

Expansions in this table are editorial suggestions only. They have not been substituted into the diplomatic transcription. Mathematical initials whose verbal expansion is not supplied securely are left unexplained.

| Form as written | Tentative expansion or meaning | Scan(s) |
|---|---|---|
| `can` | canonique | 20, 29, 33 |
| `cart`, `Cart` | cartésien / cartésienne; some readings remain doubtful | 20, 27, 34 |
| `Aut` | automorphismes | 21 |
| `SAut` | Probably a group of automorphismes fixing boundary data; the initial S is not securely expanded | 21 |
| `Op.`, `op.` | opération / opère, depending on the note | 21 |
| `ext.` | extérieure / extérieurement | 21 |
| `Pic` | groupe de Picard | 23 |
| `car.` | caractéristique | 23 |
| `pt gén.` (uncertain) | point générique | 23 |
| `Dém` | démonstration | 23 |
| `i.e.` | id est, « c’est-à-dire »; one occurrence is uncertain | 23, 30, 32 |
| `NB` | nota bene | 23, 36 |
| `Sym` | algèbre / puissance symétrique, according to the exponent | 23, 25 |
| `cl` | classe | 25, 33 |
| `MR` | Monsieur; printed postal-label abbreviation | 27 |
| `ALEX.` | Alexander / Alexandre; abbreviated given name on the postal label | 27 |
| `gal` | galoisien / galoisienne | 27 |
| `mod` | modulo | 30, 35 |
| `int` | intérieur; conjugation notation | 30 |
| `Sl`, `SL` | Special linear group notation; differences in case are preserved, not silently standardized | 27, 29, 34 |
| `PM`, `PU`, `TU` | No secure verbal expansion supplied by these pages; retained as mathematical notation | 20, 27, 35 |
| `tt` (uncertain) | tout | 32 |
| `autom.` | automorphisme | 32 |
| `pts` | points | 32 |
| `st.` (uncertain) | stable / stabilité, depending on context | 32 |
| `néc.` | nécessairement | 32 |
| `ens.`, `ens` | ensemble | 32 |
| `ss pt fixe` | sans point fixe | 32 |
| `quelc.` | quelconque | 32 |
| `él.` | éléments | 32 |
| `hom. can.` | homomorphisme canonique | 33 |
| `pr` | projection | 33 |
| `Ext` | Extension-functor notation | 33 |
| `M.` | Monsieur; in the separate reused-paper billet | 34 |
| `revêt`, `revᵗ` (uncertain) | revêtement | 35 |

## 4. Legibility and limits

The main objects in the group diagrams are generally more legible than their small labels, overwritten decorations, and surrounding prose. The least secure continuous passage is the faint text on scan 32, especially its parenthesis, marginal notes, and overlapping corrections. Scan 30 is also difficult because it combines two writing orientations, compressed French, and transverse marginal calculations. Small annotations above scan 20’s first diagram, the cancelled prose on scan 21, the diagonal and corrected passages on scan 23, and the cancelled opening of scan 25 require particular editorial caution.

The manuscript’s apparent quotient in scan 23’s NB, its minus-first candidate for the γ₃ factor, the distinction between a stemmed φ-like symbol and the final Δ, and scan 25’s weak inequality `n≤6` are preserved rather than made consistent with expected mathematics. The extremely pale marks beside scan 35’s residue rows are retained as uncertain marginal marks and may instead be verso show-through. The supplied resolution and overwritten ink do not permit a definitive edition: the transcription is complete in coverage, but the marked readings and the attribution or scope of some strokes remain open. Every scan was inventoried and compared with its transcription; all inventory rows are marked `yes`, meaning represented, not certain.

## 5. Research notes — English, separate from the transcription

These items identify questions for subsequent checking against the surrounding manuscript and the literature. They do not establish novelty, complete the author’s proofs, or alter the transcription. All scan-specific quotations and claims refer to the supplied primary images (Grothendieck, 1981, indicated scan); the year is the task’s catalogue designation. “Unproved claim” means that a complete proof is not given on these supplied pages, even where a sketch or calculation is present. Items labelled “own idea” are editorial proposals with their confidence and reason stated.

1. **Scan 20, right upper-middle; conjecture (explicit question).** The explicit question “A-t-on [bien]” followed by `S T_11 ≃ S Pi^D_03 ??` asks whether two central-extension objects agree. Any investigation must first settle precisely which projections and identifications the crowded upper diagram assigns to these symbols; the double question mark is not a proof or assertion.

2. **Scan 20, right middle and lower; conjecture (expectation).** “il semblerait plutôt, pourtant” introduces a tentative comparison `PM_11 ≃ (T*U_03, S_3)`, followed by a proposed fundamental-group identification. The annotation “fibré tangent (et non PU_03 !!)” makes the distinction between the indicated tangent object and the P-object worth checking, without changing either symbol in the transcription.

3. **Scan 20, main diagram; unproved claim.** Several regions are labelled “cart”/“Cart” and several arrows “can”. A verification would require definitions of the displayed group homomorphisms and a direct universal-property or explicit fibre-product check; no such proof is written on this page.

4. **Scan 20, generators above main diagram; own idea.** A presentation-level comparison using the written pairs for rho and sigma may expose whether the candidate group identification depends on a choice of central generator or on a sign convention. **Confidence: medium**, because the displayed generator images and cyclic quotients give a concrete test, but some relevant subscripts and the small fibre-product formula remain uncertain. This is a proposed check, not an established consequence or a claim of novelty.

5. **Scan 21, upper parameter box and equation; unpursued implication.** The written equation `u(l_i)=g_i l_{sigma(i)}g_i^{-1}` suggests that the automorphism and permutation data are accompanied by chosen conjugators, rather than merely their existence. An investigation can compare the group of such triples with the stated extension by pi, keeping track of the ambiguity in the chosen conjugators; the page gives diagrams but no explanatory derivation.

6. **Scan 21, upper and middle sequences; unproved claim.** The diagram links `SAut^+(X)`, `Aut^+(X)`, boundary automorphisms, and a term identified with `S T`; the boundary group is compared with the underlined product `S_n·T^n`. A proof would need the definitions of the topological automorphism groups, the exact boundary condition represented by S and the exclamation-mark subscript, and the relevant lifting or restriction properties.

7. **Scan 21, middle repeated sequence; unproved claim.** The annotation “0 ou Z” beneath `pi_1 Aut^+(X)` asserts a restricted pair of possibilities without giving hypotheses or a proof here. Those possibilities should be checked against the class of surfaces intended on surrounding pages, including any exceptional surfaces.

8. **Scan 21, lower-right prose; unproved claim.** “pi_0(G)=pi_0 opère extérieurement sur F / donc opère sur [centre](F)” records passage from an outer action to an action on the centre. A direct verification would show why changing an automorphism representative by an inner automorphism leaves its restriction to the centre unchanged; whether all the displayed groups are discrete or topological must remain explicit.

9. **Scan 21, lower-left boundary map; own idea.** The map `pi_1(G)→F`, the centre target, and the component-group action can be checked together using path lifting in the depicted group extension. **Confidence: medium**, because the page explicitly places these objects together, but the construction of the extension and some arrow attachments are not fully legible. This proposes a verification of the diagram, not a completed proof.

10. **Scan 23, top lemma; unproved claim (proof sketch).** The lemma states `H^1(U_03,S_3;G_m) ≃ Z/6Z` for a regular integral scheme with `Pic(S)=0` and the stated condition on the characteristic of its generic point. The page supplies a construction and marginal cohomology sequences, but a complete verification would have to establish both generation and exact order, with all base-scheme and action hypotheses fixed.

11. **Scan 23, parenthesis below lemma; unproved claim.** The phrase “est 2, on trouve Z/3Z” records a characteristic-2 variant, although its short subject is partly overwritten. This deserves a separate argument rather than an automatic reduction of the characteristic-not-2 case, particularly because the relevant finite group schemes and equivariant line-bundle data can change with characteristic.

12. **Scan 23, diagonal margin; unpursued implication.** “on utilise suite exacte” introduces mixed-cohomology and global-unit sequences, with an inner H^1 term explicitly braced to 0. These sequences may furnish an alternative algebraic proof of the same line-bundle order, but the small terminal operator before V(J) and the exact equivariant module structure first need to be resolved.

13. **Scan 23, middle bundle definition; unproved claim (proof sketch).** The statement “est un générateur” identifies the indicated principal bundle with a generator of an H^1 group. A proof must connect the tautological construction on P(V_J) with the equivariant structure and explain why no additional classes arise from the base under the written Picard-group hypothesis.

14. **Scan 23, lower middle; unproved claim (proof sketch).** “le groupe structural ... est réduit à mu_6” follows the construction of a degree-six section. To verify this step one must check that the section is invariant and nowhere zero on the indicated open subset, then formulate exactly the induced reduction of structure group, including in residue characteristics dividing 6.

15. **Scan 23, NB at bottom; conjecture (explicit uncertainty).** “Sauf erreur” introduces the displayed invariant-algebra formula, definitions of gamma_2 and gamma_3, and `Delta=gamma_2^3`. The author's qualification should remain attached to these formulas; the overwritten generators, apparent quotient, and uncertain first sign of gamma_3 warrant independent examination rather than editorial normalization.

16. **Scan 23, product and NB; own idea.** Expand the candidate polynomials separately for the literal minus reading and the alternate plus reading in gamma_3, and compare their relations with the written degree-six product. Keep the stemmed phi-like symbol distinct from the final Delta until their relationship is justified by the manuscript. **Confidence: medium**, because this is a concrete algebraic check, while the readings and intended normalizations remain uncertain; no identity or novelty is asserted.

17. **Scan 23, lemma hypotheses; own idea.** Test the construction over bases with residue characteristic 3 while retaining the written generic-characteristic condition, since only 2 is explicitly singled out in the statement. **Confidence: medium**, because the proposed order and reduction both involve 6, but the page does not spell out all relevant base-change hypotheses. This is a proposed special-case check, not a counterexample or correction.

18. **Scan 25, main paragraph; unproved claim (proof sketch).** The argument begins “Comme gamma_2 s’annule” at the indicated P-point and similarly places gamma_3 at the Q_i, then infers absence of invariant sections in the written degree range. A complete proof would require the definitions of these loci, precise vanishing multiplicities, and an account of why every relevant invariant section is controlled by the indicated generators.

19. **Scan 25, final three lines; unproved claim (proof sketch).** “l’ordre de cl(O(1)) ... est bien 6” and “un générateur du H^1 mixte” state exact order and generation. The page sketches the order argument but does not independently establish that the entire mixed H^1 group is cyclic; this should be related carefully to the lemma and marginal sequences on scan 23.

20. **Scan 25, bound on n compared with scan 23; own idea.** Compare the literal weak inequality `n <= 6` with the earlier construction involving O(6), while distinguishing arbitrary invariant sections, sections of the punctured line bundle, and the direction of dualization. **Confidence: high that the scope needs checking**, because the lower bar is visibly present and both pages single out degree six; this is an editorially separate question, not a correction of the inequality or a claim that the argument is false.

21. **Scan 25, crossed opening; unpursued implication.** The cancelled phrase beginning “[Si] 2 [inversible]” appears to impose a stronger base condition than a statement merely about generic characteristic. The reason for abandoning this route could be investigated against the surviving argument, but the unclear remainder of the cancelled sentence must not be treated as an established theorem.

22. **Scan 27, upper-right square — conjecture.** The identification `PM_{11}(2^{\sim}) \overset{?}{\simeq} PU_{0,3}` carries a literal question mark. The precise level/tangent decorations must be read and defined before testing whether this is an isomorphism of spaces, stacks, or torsors; the square alone does not settle that category. The nearby cohomological notation may be relevant, but its initial `H^1` is itself a doubtful reading (Grothendieck, 1981, scan 27).

23. **Scan 27, upper-right square — unproved claim.** The square is labelled “cart”. A proof would require explicit definitions of all four objects and maps and a comparison with their fibre product, including whatever ineffective action is suggested by the pair `(U_{0,3},\{1,\omega\})`. The manuscript supplies a diagram rather than a proof on this sheet (Grothendieck, 1981, scan 27).

24. **Scan 27, lower quotient diagrams — unproved claim.** Several arrows are labelled “gal”, with groups `D'_3`, `D_3`, and `{1,\omega}`, while other arrows carry the tentative reading “gerbe”. Verifying these descriptions requires specifying the actions and stabilizers, and determining when a displayed map is an effective covering and when it retains an ineffective kernel. No assertion about these kernels should be imported merely from the familiar names of the groups (Grothendieck, 1981, scan 27).

25. **Scan 29, middle network — unproved claim.** The diagram compares successive D-groups and cyclic groups `Z/12Z`, `Z/6Z`, `Z/4Z`, and `Z/2Z`, with labels “2”, “3”, and “12”. A proof would need presentations or explicit homomorphisms sufficient to check the kernels, all indicated composites, and the compatibility of the central Z-maps. The handwritten leftward head between two cyclic groups is particularly worth checking against the surrounding development (Grothendieck, 1981, scan 29).

26. **Scan 29, bottom exact sequence — conjecture.** The middle group in `1 — Z → ? → Sl(2,Z) — 1` is left as a literal “?”. Its position below the extension with quotient `Pi^D_{0,3} × Z/4Z` suggests an identification problem for a pulled-back extension, but that interpretation remains to be verified from the missing definitions and maps (Grothendieck, 1981, scan 29).

27. **Scan 29, bottom comparison — own idea. Confidence: medium; reason: the sheet visibly compares extensions with a common infinite cyclic kernel.** After fixing the relevant actions and identifying whether the kernels are central, compute the extension classes and their restrictions along the displayed map from `Sl(2,Z)`. This could determine the group represented by “?” and distinguish a pushout on the kernel from a restriction on the quotient; it is a proposed calculation, not a claimed result or novelty.

28. **Scan 30, upper prose — conjecture.** The line beginning “comment ces sections sont elles” appears to ask how the sections `e_i-e_j` are “permutées entre elles”, with the latter word explicitly doubtful. A useful next step is to identify the acting group and calculate its action on the individual differences, retaining any signs, rather than considering only the span indicated by the tentative top-line identification of `V_J` (Grothendieck, 1981, scan 30).

29. **Scan 30, upper-right calculation — unproved claim.** The displayed relation `\lambda^6=\prod_{i,j}\xi_{ij}(x)` gives a root construction but does not define its index set or global gluing on this page. Establishing a global torsor or line-bundle interpretation would require identifying the sheaf containing each factor, the multiplicities, and the locus on which the product is invertible. These are questions prompted by the display, not corrections to it (Grothendieck, 1981, scan 30).

30. **Scan 30, lower rotated prose — conjecture.** The explicit question begins “Si on prend l’orientation inverse” and asks for the corresponding barred operators. It is followed on the same page by the candidate formulas `\bar\rho'_s=\bar\rho_s^{-1}` and `\bar\rho'_f=\mathrm{int}(\sigma)\bar\rho_f^{-1}`. The calculation should be checked against the definitions of the representatives in `A^L_+`, `A^L_-`, and the involution whose subscript is doubtful (Grothendieck, 1981, scan 30).

31. **Scan 30, final operator identities — own idea. Confidence: high as a conditional algebraic check; reason: it follows formally from the displayed transformation if sigma is an involution fixed by it.** Under that explicit hypothesis, applying the proposed orientation-reversal transformation twice should recover both original operators. Checking this directly is a small consistency test, but it cannot establish that the geometric orientation change is represented by these formulas or that the hypothesis on sigma holds in the author’s conventions.

32. **Scan 31, lower two-row diagram — unpursued implication.** The two rows have the same displayed kernel `Pi_0`, and the middle and right vertical maps are drawn as inclusions. It is worth checking whether `Pi'` is the inverse image of `D'_3` under the map `Pi × Z/4Z → D_3 × Z/4Z`; the picture suggests this comparison but does not explicitly label that square cartesian. A proof must identify the maps and verify equality of the resulting subgroup, not merely compare the printed kernels (Grothendieck, 1981, scan 31).

33. **Scan 31, middle and bottom diagrams — own idea. Confidence: medium; reason: the same decoration `(4)` recurs together with a new `Z/4Z` quotient.** Determine whether the construction denoted `\widetilde\Pi(4)` is a pushout of the infinite cyclic kernel, a pullback, or another modification. Computing one explicit presentation and following the distinguished generator of Z through the two diagrams would separate these possibilities without assuming that `(4)` means a level-four congruence subgroup.

34. **Scan 32, opening cases — unproved claim.** The clauses beginning « La construction ... » distinguish termination, expressed through `σa_n ∉ A′`, from indefinite continuation. A proof would need the preceding definition of the iterative construction, in particular what determines the sequence and why the displayed closing assignment to `ρa_0` has the required properties; the reading of the opening negation remains uncertain.

35. **Scan 32, middle — unproved claim.** The passage « Alors ρ sur A est un ... » appears to claim that the extension is an automorphism, and then defines a quotient and the part corresponding to finite orbits. To justify it one must check both bijectivity and the compatibility of the extension with the previous partial permutation; the manuscript wording is too compressed to substitute a reconstructed proof for it.

36. **Scan 32, final paragraph — unproved claim.** The asserted identification of quadruples `(A,σ,A′,ρ)` with triples `(A,σ,ρ)` includes the conditions « σ d'ordre 2 ss pt fixe » and `A′ ∪ σA′ = A`, while recovering `A′` from finite `ρ`-orbits. The exact axioms referred to in this fragment are not stated here, so any proof requires them and must show that the recovery procedure is inverse to forgetting `A′`.

37. **Scan 32, final paragraph — own idea; confidence: medium.** On the tentative reading of `A′` as the set of finite `ρ`-orbits, finite and infinite test examples of pairs of permutations `(σ,ρ)` could determine which direction of the asserted equivalence uses `A′ ∪ σA′ = A`. This is a proposed diagnostic, not an established conclusion or a claim of novelty; the reason for moderate confidence is the explicit final displayed condition despite uncertainty in the preceding prose.

38. **Scan 33, top and central diagrams — unproved claim.** The simultaneous diagrams of `Π̃₀(q)` assert compatibility between an extension by `Z`, the quotient to `Z/qZ`, and the product `Z/pZ × Z/qZ`. A proof must specify the maps on generators, including the chosen `α`, and verify the displayed squares; the sheet itself largely consists of the diagrams.

39. **Scan 33, lower formulas — unproved claim.** The equations `δ_p*(η_p) = q′η_μ` and `δ_q*(η_q) = p′η_μ` supply the arithmetic of the pullback of the extension classes. A verification must determine the definitions of `p′`, `q′`, and `μ` and the normalizations of the generator classes from the surrounding manuscript, rather than assume them from conventional notation.

40. **Scan 33, cancelled formula — own idea; confidence: medium.** The cancellation of the expression lacking `α`, followed by `δ_p*(αη_p) = q′αη_μ`, suggests checking dependence on the identification of the cyclic quotient before comparing extensions. This is an editorial diagnostic prompted by the visible correction, not an assertion that the manuscript has proved a general classification result.

41. **Scan 34, top identity — unproved claim.** The chained identifications beginning `ST₁₁ ≃ SL̃(2,Z)` and the presentation `ρ³ = σ²` are asserted alongside a fibre product over `Z/6Z`. To prove that the indicated isomorphisms respect the extensions, one would need explicit maps on the displayed generators and the identification of the central generator marked `ω`.

42. **Scan 34, inverted lower square — conjecture.** A visible question mark labels the upward arrow from `Π̃` to `Π̃(4)`, next to a word tentatively read as « cart ». The question may concern the map or the Cartesian nature of the square; the sheet does not specify which, so the research issue is to determine the intended square and test its universal property.

43. **Scan 34, source-sheet note — own idea; confidence: high as a source-critical caution.** The distinct sideways billet reads « 27-11-81 », « M. Grothendieck », and « A remplir d'urgence ». It should be kept separate from the mathematical author's assertions; its date alone does not determine when the mathematical additions were written, and the signature is not read securely.

44. **Scan 35, top numeric specialization — conjecture.** The explicit parenthesis « (α = −1 ?) » leaves a sign choice open at the point where `p=6`, `q=4`, and `μ=12` are substituted. The displayed residue maps and later circled `α′` offer evidence to investigate the intended convention, but they should not be used to erase the written question.

45. **Scan 35, prose to the right of the residue map — unproved claim.** The map from `Π₀,₃ᴰ` to `Z/6Z` is said to be « défini directement par l'action » on a principal covering associated with a canonical multisection, the latter noun read with some doubt. A proof would need the construction of this covering, its equivariance for the displayed symmetry group, and a direct computation of the residues of `ρ` and `σ`.

46. **Scan 35, lower extension diagram — unproved claim.** The diagram identifies a group written `Π̃₀,₃ᴰ(4)` with `π₁(PU₀,₃, S₃ × μ₄)` and relates the lower group to a fibre product over `Z/2Z`. Verification requires checking that the two vertical maps preserve the distinguished central subgroups and the group action on the total space.

47. **Scan 35, final presentation — unproved claim.** The final relation `ρ̃³ = σ̃²` is followed by an isomorphism to the displayed lifted Teichmüller group. The preceding generators carry an uncertain extra superscript and an annotation involving `ω′`; a proof must first fix these distinctions and then show that the presentation has neither additional relations nor a larger central kernel.

48. **Scan 35, top and final formulas — own idea; confidence: medium.** Computing the residue maps on the two displayed generators and comparing the image of their common central power could test the sign convention without using an external presentation. This is a proposed consistency check, not a correction of the manuscript; the reason for moderate confidence is that the residues are legible, whereas the decorated lifted generators are not.

49. **Scan 36, main comparison diagram — unproved claim.** The displayed maps on generators, including `ρ ↦ ρω̄²`, `σ ↦ σω̄³`, and `ω² ↦ ω̄⁴ = ω′`, are asserted to fit the three rows of extensions. A proof should check the relations in the explicitly written presentation of `SΠ₀,₃ᴰ(4)` and the compatibility of the chosen central generators; the sheet supplies formulas rather than a written verification.

50. **Scan 36, upper-right presentation and main diagram — own idea; confidence: medium.** Substituting the displayed generator images directly into the relation `ρ³ = σ² = ω̄⁻⁴` provides a possible test of the comparison maps and the inverse convention relating `ω` and `ω′`. This is an editorial consistency test, not a correction or a claim that all identifications follow from it; moderate confidence reflects legible exponents in the presentation but overwritten notation in NB.

51. **Scan 36, inverted foot annotation — unproved claim.** The group `SΠ₀,₃ᴰ(4)` is annotated as `π₁(U₀,₃, S₃ × μ₄)` over a map to `Π₀,₃ᴰ`. The visible base symbol has no P in this foot annotation, whereas the preceding sheet writes P in a related identification; establishing the intended objects would require the author's definitions, and the difference has been preserved.

52. **Scans 23, 25, 27, and 35–36, equivariant classes and cyclic quotients — own idea; confidence: medium.** Compare the manuscript’s degree-six class and its quotients of orders 4, 6, and 12 with Fulton and Olsson’s (2010, Theorem 1.1) identification of $\operatorname{Pic}(\mathcal M_{1,1,S})$ with $\mathbb Z/12\mathbb Z\times\operatorname{Pic}(\mathbb A^1_S)$ when $S$ is reduced or is a $\mathbb Z[1/2]$-scheme. Their Lemma 2.2, in the section where 6 is invertible, places the compatible characters at the order-4 and order-6 stabilizers in a common order-12 subgroup. A comparison would require actual morphisms of the relevant quotient stacks and an identification of the manuscript’s bundle with a specified power or dual of the Hodge bundle; shared orders alone do not identify them. Confidence is medium because the explicit orders and bundle trivializations give a concrete comparison to test, while the required identifications and base hypotheses are not established in these sheets.

## References

Fulton, W., & Olsson, M. (2010). The Picard group of $\mathcal M_{1,1}$. *Algebra & Number Theory, 4*(1), 87–104. [https://doi.org/10.2140/ant.2010.4.87](https://doi.org/10.2140/ant.2010.4.87)

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois: Brouillon* [Handwritten manuscript draft, cote 140-1; supplied scans 20–37]. Université de Montpellier. (Identification and catalogue year supplied with the task.)
