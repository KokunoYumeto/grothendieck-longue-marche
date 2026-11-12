# Shared notation table

This table governs transcription throughout the package. It records transcription conventions; entries marked “verify locally” do not assert that a particular glyph has already been identified. Distinct forms on the scans are retained, and uncertain identities are marked in place. No mathematical expectation licenses normalisation.

| Visible form | LaTeX rendering | Reading discipline |
|---|---|---|
| Exclamation-mark superscript | `^!` | Inspect both upright stroke and dot; never replace by prime. |
| Prime / double prime | `'` / `''` | Inspect at each occurrence; distinguish from exclamation marks. |
| Straight or curved double quotation marks | two backticks to open, two apostrophes to close | Use ` ``...'' `; use `« ... »` only for visible guillemets. |
| Script capitals | `\mathcal{A}`, etc. | Verify alphabet locally; use `\unsure` for an unresolved script/plain distinction. |
| Gothic capitals or lowercase | `\mathfrak{A}`, `\mathfrak{g}`, etc. | Verify locally; do not infer from conventional category names. |
| Bold capitals | `\mathbf{A}`, etc. | Preserve visible weight when meaningful. |
| Blackboard bold | `\mathbb{Q}`, etc. | Use only when ink/type identifies it. |
| Plain mathematical letters | ordinary math italic, e.g. `H`, `X`, `f` | Do not substitute a fancier alphabet. |
| Roman mathematical words | `\operatorname{Hom}`, `\operatorname{End}`, `\operatorname{Tr}`, etc. | Only spell the letters actually present. |
| Subscripts and superscripts | `_{...}`, `^{...}` | Preserve nesting and placement; retain all `0`, `1`, `l`, degrees, signs. |
| Bar, hat, tilde, overarrow | `\bar{...}`, `\hat{...}`, `\tilde{...}`, `\overrightarrow{...}` | Choose observed decoration, not expected object. |
| Ordinary arrow | `\to`, `\leftarrow`, `\longrightarrow` | Inspect arrowhead and direction at every use. |
| Inclusion / injection | `\subset`, `\subseteq`, `\hookrightarrow` | Distinguish relation from arrow by ink. |
| Equality / equivalence / isomorphism | `=`, `\equiv`, `\simeq`, `\cong`, `\approx` | Preserve drawn sign; mark ambiguity. |
| Inequalities | `<`, `>`, `\leq`, `\geq`, `\neq` | Read direction from ink. |
| Visible abbreviations | exact visible text | No expansions in transcription; expansions are confined to the abbreviation list below. |
| Underlining / double underlining | `\uline{...}` / `\uuline{...}` | Keep distinction from deletion and from a fraction bar. |
| Deletion | `\deleted{...}` | Include recoverable original, including struck formulae. |
| Insertion / separate margin note | `\inserted{...}` / `\margin{...}` | Follow caret or leader; do not relocate by semantic convenience. |
| Uncertain reading | `\unsure{reading}` or `\unsure{reading\|alternative}` | First reading follows ink. Use at symbol level in formulae/diagrams. |
| Physically unreadable words | `\illegible{n}` | Only after attempted reading; never as a formula-symbol placeholder. |
| Diagram / table | `\diagram{\begin{tikzcd}...\end{tikzcd}}` or array | All objects, arrowheads, labels, cancellations retained. |
| Non-diagram drawing | `\figure{\begin{tikzpicture}...\end{tikzpicture}}` | Reproduce geometry and labels; no embedded scan or verbal substitute. |

## Observed recurring forms

Specific recurring forms will be added and checked against their scans during reading and independent audit. The initial rules above are shared before page assignments begin.

| Observed form and location | Shared rendering | Scope / cautions |
|---|---|---|
| Projectors and subring, 16:3–6 | `\pi_i`, `\mathcal E`; degree `\nu` | Greek nu must be inspected separately from Latin v. |
| Tail projectors, 16:5 | `\varphi_i`, `\psi_{2n-i}` | Two different symbols; no unification. |
| Lefschetz generator and checked dual, 16:25 | `\xi`, `\check V` | Check is a locally observed dual form, not a global substitute for star. |
| Tangent spaces and duals, 54:2–3 | `t_A`, `t_B`, superscript `\vee` | Retain local dual convention. |
| Universal extensions, 54:3 | `S_A`, `S_B` | Overwritten first S remains uncertain; later S is clearer. |
| Weak inverse / lowering operator, 16:7–18, 51, 53, 55 | `v_i`, `w_i`, `\Lambda`, `u_i` as locally written | These are distinct constructions and letters. A common mathematical role does not justify replacing one glyph by another. |
| Model operators, 16:14–16 | bold or plain `L`, `\Lambda`, `\pi_i` according to local strokes | The model algebra and a general graded ring are not typographically unified; unresolved weight is marked at its occurrence. |
| Decomposition symbols, 16:25–43 | `\coprod` versus `\oplus` / `\bigoplus` | The two uprights joined by a baseline, without an enclosing circle, are retained as coproduct-shaped notation even where an internal direct sum is intended. |
| Polynomial-form conjecture subscript, 16:44–50 | leading reading `\ell`, with `\unsure{\ell\|\chi}` where the loop/crossing is unresolved | Compared across typed letters and the manuscript definition; a glyph of doubtful typeface is not silently normalized. The proposition label in 16:48 has its own `\ell\|1` doubt. |
| Pullback / pushforward marks, 16:33–50 and 47 | `\varphi^*`, `\varphi_*`; `\unsure{+\|*}` at 16:50 | Plus and star are read separately. In 16:50 a simple cross is the leading reading, although a star is mathematically tempting. |
| Underlined structure sheaves, 47:6–7 | `\uline{\mathcal O}_K`, `\uline{\mathcal O}_B`, `\uline{\mathcal O}_S` where underlining is visible | Underlining is local; it is not inserted on every calligraphic O elsewhere in the file. |
| Derived categories, 47:3, 5 | `D_{\unsure{\mathrm{parf}\|\mathrm{prof}}}` | The repeated subscript is unresolved, not two securely established different category names; the marginal word parfaits is clear. |
| Fourier functors and virtual transforms, 47 | `\Phi_{\mathcal L}`, `\varphi_{\mathcal L}`, `\psi_D` | Preserve capital/lowercase distinctions and local kernel `L` / `\mathcal L` forms; do not impose a modern notation. |
| Checked object and dual result, 47:11 | `\check F`, `\check x` versus superscript `\vee` | The visible check over the input is different from the vee on the result; no implicit definition is added. |
| Typed underlined coefficient letters, 16:19 | `\uline{\mathrm Z}`, `\uline{\mathrm Q}` | Explicit typewritten underlining is retained, rather than replaced by blackboard bold. |
| Handwritten coefficient letters, 47:8, 10 | local `\unsure{\mathbb Z\|\mathbf Z}`, `\unsure{\mathbb Q\|\mathbf Q}` | Retraced strokes do not always decide the alphabet. Other plain or weighted occurrences remain as independently read. |
| Operator label following L, 16:51 | `L\unsure{!}` | A slanted stroke and hollow dot after L at baseline suggest a bang; it is not encoded as a superscript or silently read as a prime or zero. |
| Restricted-power labels, 54:5, 7 | `p^A`, `p^B` | Raised A/B are retained as superscripts, distinct from ordinary indices. |
| Repeated institutional cover emblem, all four cotes, scan 1 | TikZ polygons with pale grey-blue and olive fills | The repeated geometry was compared across covers; colors are approximations of the scanned print, not claims about an original color specification. |
| Center symbol, 16:5–6 | local `\unsure{Z\|\mathfrak Z}` in 5 and `\unsure{\mathfrak Z\|\mathcal Z}` in 6 | Direct comparison found an open curved top, mid-crossstroke and hooked lower stroke in 5, and more looped forms in 6; the ink does not securely establish different alphabets. A further calligraphic alternative for 5 is recorded in the doubts table. |

# Doubts

| File | Scan | Approximate position | Reading | Alternatives / uncertainty | Confidence |
|---|---:|---|---|---|---|
| 16 | 3 | under title | comm. | commutatif abbreviated; final strokes weak | medium |
| 16 | 3 | top insertion | non-gradué (le produit) | very compressed script; latter parenthesis especially uncertain | low |
| 16 | 3 | first equation label | 1.2 | overwritten earlier numbering | low |
| 16 | 3 | degree variable in Hom display | ν | v | medium |
| 16 | 3 | before pr_ν | u | dense cancellation | low |
| 16 | 3 | before donnée | par | crossed short word | low |
| 16 | 3 | boxed display number | 1.3 | overwritten earlier number | low |
| 16 | 3 | crossed lower-right equivalence | ⇔u=π_(i+ν)uπ_i | ink overwritten; individual symbols uncertain | low |
| 16 | 3 | last-line reference | 1.3 | overwritten number | low |
| 16 | 3 | foot | 2 | different numbering from top 1 | medium |
| 16 | 3 | under title, final word | fixé | fixe; small accent-like stroke visible | medium |
| 16 | 3 | above lower paragraph | intrinsèque | intrinsèquement; final word compressed after q-descender, not certainly full adverb | low |
| 16 | 4 | top line | E* | superscript compressed; possibly (ν) | medium |
| 16 | 4 | after graduation | E^(ν) | E* expected mathematically; not silently corrected | medium |
| 16 | 4 | product exponent | ν−ν′ | ν+ν′ | medium |
| 16 | 4 | left margin | groupe | gr. abbreviated? | low |
| 16 | 4 | crossed calculation | la relation; π_(i+ν)uπ_i=π_j uπ_i | several overwritten indices | low |
| 16 | 4 | above crossed calculation | E_i^j | free small notation or intended insertion unclear | low |
| 16 | 4 | lower sum | π_(j+ν)u=Σ_i π_(j+ν)uπ_α | j/i and i/α appear inconsistent; preserved with doubt | medium |
| 16 | 4 | paragraph 3 cancelled opening | Nous voulons | second word uncertain | medium |
| 16 | 4 | paragraph 3 cancelled syllable | supp | first attempt at suppose | medium |
| 16 | 4 | top first line, overwritten noun | deleted algèbre replaced by anneau | old descender visible beneath revised word; exact extent of overwrite uncertain | medium |
| 16 | 4 | cancelled calculation opening | d’où la relation | first tiny cursive word above la relation was not in first reading | medium |
| 16 | 4 | cancelled calculation right side | π_(i+ν)uπ_i | π_j uπ_i; subscript has an i and a wavy ν-like tail | low |
| 16 | 5 | cancelled head | les π_i de degré zéro, et que | dense cross-hatching over several words | low |
| 16 | 5 | head | voudra | considère | low |
| 16 | 5 | above intervalle | (pair) | fixe? small cursive | medium |
| 16 | 5 | crossed after unicité | Supposons, établie l’unicité | first word partly abbreviated or unfinished | low |
| 16 | 5 | boxed insertion last word | Restons | ending compressed | low |
| 16 | 5 | φ_i and ψ_(2n−i) definitions | Σπ_i | summation variable is α; ink looks i | medium |
| 16 | 5 | component display initial word | ou | possibly a cancelled connective | low |
| 16 | 5 | component display | deleted φ; final ) | overwritten mark and unmatched parenthesis | low |
| 16 | 5 | penultimate equality | π_(i+2n−2i) | α corrected to i? | medium |
| 16 | 5 | final block subscript | E_(2n−i,i) | earlier index cancelled densely | low |
| 16 | 5 | last line | u_i | π_i | low |
| 16 | 5 | final block index correction | 2n−i,i replacing cancelled lower index | replacement is physically above E, possibly a superscript rather than displaced correction; mathematical indexing not used to decide | low |
| 16 | 5 | centre notation in first full paragraph | Z or Gothic Z | calligraphic Z also possible; open curved top, short mid-crossstroke and hooked lower stroke do not securely distinguish an alphabet from the more 3-like and looped occurrences on scan6 | low |
| 16 | 6 | first line | u_(2n−i) | π_(2n−i) | low |
| 16 | 6 | first line | donc; deleted qui | pale cursive, isolated overwritten word | medium |
| 16 | 6 | conditions and paragraph | fraktur Z | calligraphic Z; centre notation | medium |
| 16 | 6 | deleted hypotheses | π_αu=0 (α≠i/2n−i) | cross-hatched, especially the quantification | low |
| 16 | 6 | deleted expression after implique | π_i(Z E^0) | dense crossing | low |
| 16 | 6 | first condition number | 4.1 | overwritten | medium |
| 16 | 6 | (4.2) and inserted map (4.3) | dash between M^i and M^(2n−i) | arrowhead not securely visible | medium |
| 16 | 6 | (4.2) cancelled word | à | tiny crossed mark | low |
| 16 | 6 | cancelled restriction in (3.1) | π_αu=0 (α≠i) | there may be an additional initial quantifier or α-like mark; dense cancellation prevents isolation from hatching | low |
| 16 | 7 | opening map | dash | arrowhead not visible | medium |
| 16 | 7 | proof cancelled mark before u | u | overwritten short mathematical mark | low |
| 16 | 7 | proof cancellation at equality | = | overwritten equality / final stroke | low |
| 16 | 7 | reference at end of proof | 4.4 | overwritten digits | medium |
| 16 | 7 | marginal reference | cf 5. v. p 5bis | spacing and small v/p compressed | medium |
| 16 | 7 | new section number | 6 | overwritten 5? | medium |
| 16 | 8 | upper ring description | sur-anneau | sous-anneau | medium |
| 16 | 8 | cancelled induction sentence | Raisonnons par récurrence sur i | middle words overwritten | low |
| 16 | 8 | induction insertion | deleted que | possible reinforced underline rather than cancellation | low |
| 16 | 8 | tail-projector insertion | d’où | donc | medium |
| 16 | 8 | crossed replacement phrase | remplaçons v_i,w_i par; alors | crossed words weak | low |
| 16 | 8 | before final computation | comme underlined; deleted donc | layering of two short connectives | low |
| 16 | 8 | bottom cancelled equality | =π_i | dense overwriting | low |
| 16 | 8 | upper paragraph, before à (1.3) | correspondantes | correspondant; final strokes compressed, first reader had singular participle | medium |
| 16 | 9 | labels (6.1),(6.2),(6.4) | 6 | 5 overwritten as6 | medium |
| 16 | 9 | (6.2) cancelled right phrase | dans E_(2n−i)^i | letters and indices partly obliterated | low |
| 16 | 9 | before L’ensemble | Ceci | cancelled short word | low |
| 16 | 9 | last intrinsic reference | 1.7 | 1.3; enlarged ink favours the angular 7, not a rounded lower loop | medium |
| 16 | 9 | before morceaux | can. | canoniques abbreviated or another short cancelled word | low |
| 16 | 9 | primitive decomposition terminal marks | horizontal dashes | not dots; intended continuation unspecified | high |
| 16 | 10 | (6.5) | six dots after left brace | count/spacing approximate; no definition written | medium |
| 16 | 10 | cancelled item(ii) | La graduation ... pour que ... tels que | layered overwritten prose and formulae | low |
| 16 | 10 | margin(ii) | two illegible words | physical overwriting prevents letters being recovered | low |
| 16 | 10 | (iii) insertion | défini Λ | définit Λ; abbreviated form possible | low |
| 16 | 10 | (v) insertion | définis comme formant | very pale and compressed | low |
| 16 | 10 | cancelled(vi) inner deletion | par les | dense short crossing | low |
| 16 | 10 | labels6.6 and6.7 | 6 | old5 overwritten | medium |
| 16 | 10 | proof exponent | n−i | end strokes overwritten | medium |
| 16 | 10 | proof last reference | 6.7 | cancelled reference heavily overwritten | low |
| 16 | 10 | cancelled item(ii), beginning and end | Une graduation; pour un; tel choix | La graduation; pour que; tels que, initial reading; the overlying hatching obscures several letters | low |
| 16 | 10 | cancelled item(vi), degree of L | 1 | 2; enlarged superscript has a nearly vertical central stroke, so expected degree 2 is not silently supplied | low |
| 16 | 10 | bottom proof, inserted phrase | a déjà dit | a déjà dit que; attachment of final short strokes is unclear before the main-text que | low |
| 16 | 10 | proof exponent | (n−i) | both parentheses visible but overwritten at the ends | medium |
| 16 | 11 | crossed upper display | j∈ | last symbol overwritten; no legible continuation | low |
| 16 | 11 | insertion after (iv) | ascendante | descendante | medium |
| 16 | 11 | deleted word before descendante | sur | short blacked-out word | low |
| 16 | 11 | deleted formula before (6.8) | π_jα | indices partly obscured by crossing | low |
| 16 | 11 | last sum | π_(i,α) | π_(i,α′); no clear prime after the final α | medium |
| 16 | 11 | bottom overwritten symbol | E | same calligraphic letter partly cancelled | low |
| 16 | 11 | cancelled paragraph opening | Car | Cela; enlarged strokes are compressed and do not securely distinguish the two | medium |
| 16 | 12 | opening mapping | plain dash | right endpoint may be a very small arrowhead | medium |
| 16 | 12 | first isomorphism exponent | n−i−2α | n−i+2α | medium |
| 16 | 12 | first isomorphism arrow | ⇒ | ordinary arrow thickened by retracing | medium |
| 16 | 12 | (6.9), right edge | π_(i,α′) | term partly clipped; closing parenthesis not visible | low |
| 16 | 12 | before large cancellation | égalt | compressed abbreviation, ending uncertain | low |
| 16 | 12 | inside crossed block | prendre; poser; L^(n−i+α) | layered strokes partly conceal these earlier readings | low |
| 16 | 12 | after (6.10) | π_(2n−i) | heavily blacked-out operator | low |
| 16 | 12 | (6.11), crossed indices | j≤n | several ink layers prevent a secure reading | low |
| 16 | 12 | (6.11), right crossed expression | +sum_(0≤i≤n) π_(i,0)Λ | summation and indices highly uncertain; Λ visible at right | low |
| 16 | 12 | last crossed expression | Λπ_(i,α) | π_(i,α); a separate triangular Λ is visible at the left of the deleted layer, the remaining indices still obscured | low |
| 16 | 13 | (6.12) first exponent | α−1 | tiny overwrite above L | medium |
| 16 | 13 | (6.13), crossed factor | π_(2n−i,α) | dense horizontal overwriting | low |
| 16 | 13 | (6.13) condition | i≤n−1 | i<n−1; enlargement shows a separate lower stroke under the angle | high |
| 16 | 13 | Remarque degree of Λ | (2) | (−2); no clear minus visible | high |
| 16 | 13 | after π_i in Remarque | cancelled α | may be another short overwritten sign | low |
| 16 | 13 | right margin before system | π_(2n−i) | heavily scribbled fragment | low |
| 16 | 13 | (6.14) row2 | two cancelled π_(2n−i) | indices not securely recoverable | low |
| 16 | 13 | (6.14) row3 overwritten operator | w_(i−2α) | replaced in situ by Λ power | medium |
| 16 | 13 | (6.14) row7 condition | α≤n−1 | i≤n−1 | medium |
| 16 | 13 | between rows5 and6, above Λ exponent | cancelled α | detached correction mark; its attachment to the powers below is not secure | medium |
| 16 | 14 | second line of (6.15) | cancelled 2 before j | overwritten earlier index; exact digit uncertain | low |
| 16 | 14 | Question deletion | générateurs | crossed word partly obscured | low |
| 16 | 14 | Question connective | de relations | des relations; preceding cancelled et | low |
| 16 | 14 | left margin | cf. ci-† | ci-dessus or cross-reference sign | low |
| 16 | 14 | module/operator alphabet | bold M₀, L₀, Λ₀ | deliberately doubled strokes; plain lettering is an alternative | medium |
| 16 | 14 | last insertion | M_Z* | M₀*; subscript overwritten | low |
| 16 | 14 | last reference | (6.1)(i) | (6.1)_i | low |
| 16 | 14 | last deletions | donc; ξ | short crossed fragments | low |
| 16 | 14 | first operator definition and final muni de | bold L, without secure subscript | bold L₀; the filled terminal stroke may conceal a0, but no separate0 is resolved as it is in the algebra formula | medium |
| 16 | 14 | inserted dual form | ξ* | ξ₀*; the zero is not separately resolved on this occurrence | medium |
| 16 | 15 | first cancelled words | Donc le | two words crossed through | low |
| 16 | 15 | abandoned upper expression | L^jπ_(i,α) | L^βπ_(i,α); tiny upright glyph with lower loop favours j | low |
| 16 | 15 | cancelled upper ranges | i,j; i<j | partial overwritten fragments | low |
| 16 | 15 | upper left margin | peut être remplacé | first verb compressed; va/doit possible | low |
| 16 | 15 | cancelled lower range | 0≤i≤2n | 0≤i≤n | low |
| 16 | 15 | product-law previous condition | i−2α≠j−2β | heavily overwritten; revised condition clearer | low |
| 16 | 15 | product equality | equals sign | not separately clear at live product level | low |
| 16 | 15 | enclosed margin | devront | doivent; ending compressed | medium |
| 16 | 15 | parenthesis after M₀,ξ₀ | qui au fond unique est | two pale words not securely deciphered | low |
| 16 | 15 | proposition deletion | sous-algèbre | overwritten by anneau | medium |
| 16 | 15 | first condition | endom | abbreviated ending uncertain | medium |
| 16 | 15 | last condition label | (iii) | (ii) | medium |
| 16 | 15 | inserted definitions, second condition | cancelled β−α below α≥β | β≤α; old comparison/correction partly concealed by a heavy horizontal stroke | low |
| 16 | 15 | first prose after abandoned basis | ne bien sûr dépend pas du choix | ne is compact; dépend is visibly on the next line after bien sûr, confirmed by both readers | medium |
| 16 | 15 | model operators on this page | single-stroke L₀ and Λ₀ | some letters heavily retraced, but no consistent doubled outline as on14/16 | high |
| 16 | 16 | top cancelled continuation | respectant la graduation de E par les π_i | long overlaid crossing | low |
| 16 | 16 | upper deleted word | quelque | small partly erased word | low |
| 16 | 16 | left diagonal underlined word | réalisation or fidèle | graduation; tall looped initial and dense ascending strokes do not yield a secure word after cancelled représentation | low |
| 16 | 16 | left diagonal connective | telle or fait | dense overwrite; no secure recovery | low |
| 16 | 16 | left diagonal last item | par Φ-module fidèle | un Φ-module fidèle; the underlined ring glyph can also resemble Θ; incomplete outline | low |
| 16 | 16 | cancelled proof | voit donc; degré0 | line partly intersected by cancellation strokes | medium |
| 16 | 16 | definition of Λ′ | φ(Λ) | φ(Λ₀); no clear 0 in this occurrence | medium |
| 16 | 16 | last uniqueness paragraph | several attempted crossed phrases | multi-layer revision; attachment and word readings remain low confidence | low |
| 16 | 16 | last reference | 6.14 | last digits overwritten | medium |
| 16 | 16 | left diagonal final parenthesis | pour la graduation induite | donnée; indiquée also conceivable; the last word has a dotted and compressed middle rather than a securely readable initial d | low |
| 16 | 16 | far left of cancelled L-power relation | avec | on a or a separate revised connective; physical placement before relation retained, without normalizing the resulting cancelled sentence | low |
| 16 | 16 | cancelled cross-reference | Cf Proposition ci-dessous | first reader ci-dessus corrected: dessous begins the next source line | high |
| 16 | 16 | final uniqueness paragraph, first model Λ | doubled Λ without distinct zero | Λ₀; no separately discernible 0 in enlarged occurrence | medium |
| 16 | 16 | below diagonal margin enclosure | short detached stroke and looped crossed trace | possibly a letter or a directional mark; represented graphically without assigning linguistic content | low |
| 16 | 17 | middle deleted phrase | En l’absence des π_i | crossed small writing | low |
| 16 | 17 | small circled symbol | π′_i | π_i; preceding word may be present | low |
| 16 | 17 | inverse criterion | π_(2n−i), earlier i deleted | index partly overwritten; no second identity supplied | low |
| 16 | 17 | criterion trailing marks | cancelled =0 then quotation then =0 | ordering and quote shape uncertain | low |
| 16 | 17 | small faithful-module note | par sa graduation coïncide avec π_i; Tout précédent | very compressed overwritten wording; no secure continuous sentence | low |
| 16 | 17 | second faithful-module formulation | E* (définie par les π_i∈End(M*)) | several insertions obscure the syntax | low |
| 16 | 17 | Question verb | pourrait-il | serait-il; source appears to omit être | low |
| 16 | 17 | small faithful-module note, projector and connective | coïncide avec π_i; Tout précédent | not independently confirmed from enlarged ink; π_i is now marked locally uncertain; compressed overwritten words remain low confidence | low |
| 16 | 17 | end of second faithful-module formulation | seven small punctuation strokes, then a separate heavy point | first five are dot-like; last two elongated, slightly rising strokes may be dashes; represented graphically without supplying missing prose | high |
| 16 | 17 | Question parenthetical insertion | elle sera définie à posteriori par les π_i=u(π_i) | source parenthesis lies between the Question opening and the line beginning E: ...; the curved leader does not securely fix a verbal attachment within pourrait-il vrai, so the insertion is retained as a separate callout | medium |
| 16 | 18 | definition parenthesis | cette; au nᵒ; (pair); qu'un système de\|qui un système de | Fragmentary reading through crossing and reverse-side show-through. Independent enlargement favors qu’un (no secure dot of i), while the former qui un remains explicit. The first word has further ci-like terminal traces; celle-ci or celui-ci is also conceivable but not secure enough to replace the leading uncertain cette. | low |
| 16 | 18 | three cancelled words | illegible, estimated three | no secure letters recoverable after magnified inspection | low |
| 16 | 18 | crossed line before L’élt | En dehors (φ(Φ)=E*) | formula and words heavily crossed | low |
| 16 | 18 | lowering terminology | adjoint pour; anti replaced by co. | Overwritten cancelled phrases; the revised co. has a visible dot, with no secure hyphen. A separate compact raised mark immediately before l’élément is preserved as an uncertain opening double quote. | low |
| 16 | 18 | after E* in NB | ξ₀ | crossed symbol | low |
| 16 | 18 | before transposition | transposé | cancelled word | low |
| 16 | 18 | nonredundancy phrase | nombre2n | word compressed | medium |
| 16 | 18 | equivalence cancellations | braces; π_(2n) | overlaid ink | low |
| 16 | 18 | circled marginal comment | déjà pour | two short words not secure | low |
| 16 | 18 | after crossed glyph following E* in NB | short horizontal dash | A distinct visible dash remains before the comma; its relation to the cancelled notation is uncertain and no mathematical meaning is supplied. | medium |
| 16 | 18 | equivalence 3′, exponent over Λ | n\|- | The superscript is a very flat short stroke, flatter than the nearby n over L; n remains the leading uncertain reading without normalization from the equivalence. | low |
| 16 | 18 | underlining in final sentence | algèbre underlined; réciproque plain | Independent enlargement locates the straight underline beneath algèbre on the last source line; no underline occurs beneath réciproque. | high |
| 16 | 18 | below marginal callout arrowhead | short detached vertical stroke | Represented graphically without interpreting it as a numeral or an apostrophe. | medium |
| 16 | 19 | before Pic_U^0 désignant | cancelled où | overtyped short word | medium |
| 16 | 19 | overwritten pairing adjective | symétrique | canonique; original type partly obscured by handwritten correction | low |
| 16 | 19 | whole page strokes | possible whole-sheet cancellation | scope cannot be established securely; strokes reproduced separately | medium |
| 16 | 19 | last Pic(U) zero | subscript0 | earlier formulae have superscript0; low printed placement retained | high |
| 16 | 19 | dont l’ordre n’est autre, after Z^r display | ordre | The medial r/d positions show dark overlapping type strokes. The final word is readable, but an earlier underlying letter order cannot be recovered reliably; no deleted lexical form has been invented. | medium |
| 16 | 20 | top cancellation | b′ | isolated heavily overwritten mark | low |
| 16 | 20 | E product first degree | 2i | i; upper loop may belong to scriptE | low |
| 16 | 20 | first arrow target | M^(2n) | M^n; first superscript curl | medium |
| 16 | 20 | canceled scaling line | Lambda lambdaL tilde | line crossing through glyphs could conceal map sign | low |
| 16 | 20 | word between scaling formulas | alors | sur; very compressed | low |
| 16 | 20 | P(L expression | Lambda=P(L | no closing parenthesis visible; not supplied | high |
| 16 | 20 | operator denominator | Delta(L)^−N | Delta could be another triangular glyph | medium |
| 16 | 20 | right canceled identity | LL′ L′²=LL′ | initial two glyphs heavily struck | low |
| 16 | 20 | H0 H1 ... curved arrow | H0→H4;H1→H3 | straight arrow starts belowH1 and ends belowH3, curved arrow belowH0toH4 | high |
| 16 | 20 | rank row arrows | dashes | slight terminal ticks not clear arrowheads | medium |
| 16 | 20 | rank abbreviations | rg1,rg2,rg2,rg1 | r/g heavily cursive but repeated | medium |
| 16 | 20 | Sym expression | Sym²(V)—V— | small exponent2 uncertain; final dash unfinished | low |
| 16 | 20 | isolated glyph under Sym | k | 2; small overwritten character | low |
| 16 | 20 | last barred equality | doublebarL′ | singlebarL′; upper bar layering uncertain | low |
| 16 | 20 | bottom ring final term | L doubleprime | L prime; two short strokes visible, no secondL supplied | low |
| 16 | 21 | canceled t after où | t^(i−1)(X,l) | typewritten x-overstrikes obscure initialt | medium |
| 16 | 21 | 8.5 canceled coefficient tail | l^nu Z | blackened glyphs might be different earlier coefficient notation | low |
| 16 | 21 | 8.6 canceled initial glyph | T | completely inked; shape T-like | low |
| 16 | 21 | 8.6 opening parentheses | (H^i(X,mu)^0 | two opens and one close visible; unmatched outer parenthesis retained | high |
| 16 | 21 | word canceled before finis | dant | d’ordre; densely overtyped short word | low |
| 16 | 21 | Kummer correction | les suites exactes→la suite exacte | final s letters canceled, article visibly revised | high |
| 16 | 21 | small deletion marks in prose | x; x; à/x | may be typographic cancellation signs rather than recoverable words | low |
| 16 | 21 | Severi accents | Sévéri | both acute accents visible in typescript | high |
| 16 | 22 | opening canceled upper-right phrase | E^{-2n} engendré par Lambda_0^n | The verb is traversed by thick cancellation, and the subscript/superscript of Lambda are partially lost; Lambda^n remains possible. | low |
| 16 | 22 | second canceled line after de E^{2n} | two unreadable words, de L-prime | The long wavy cancellation masks the intervening words; no confident reconstruction. | low |
| 16 | 22 | proof alpha factor | alpha | A heavily retraced alpha resembles varphi; retained locally as unsure. | medium |
| 16 | 22 | concluding powers of L_0 and Lambda_0 | prime n | Tiny strokes above the zero-subscripted letters may be primes or the initial strokes of n. No replacement by the mathematically expected L-prime/Lambda-prime is made. | low |
| 16 | 22 | left side of implication | L-prime | The isolated superscript looks cross-like, so star remains possible. | medium |
| 16 | 22 | small insertion underneath implication | Et si [deleted Lambda] on a/choisi bar-Lambda une base de E^{-2n}, pour polyn(L) alors | This is the weakest passage: several words are exceedingly abbreviated/light, and the overwritten letter and brace labels remain uncertain. The visible bar over Lambda and exponent -2n are retained. | low |
| 16 | 22 | start of lower discussion | On veut; Ça | On peut; Ce. The cursive first verb and the tiny final vowel of Ça are ambiguous. | medium |
| 16 | 22 | basis table | degree labels0,2,4; last degree blank | No visible6 beneath L^3. It is not supplied from the progression. | high |
| 16 | 22 | small words beneath insertion brace | le cas in the main sentence dans le cas où | placement under the brace initially made them look like labels; independent first-reader recheck agrees they continue the main sentence and should occur only once | medium |
| 16 | 23 | canceled first phrase | D’après il est | The typewriter-x cancellation obscures spaces and some letters; il est is the best literal reading despite the unfinished syntax. | medium |
| 16 | 23 | after X [15] | deleted question mark | Small hatch could be another discarded mark, not recoverable with confidence. | low |
| 16 | 23 | three Br superscripts in Tate modules | deleted prime | Dense identical hatching hides the original superscript. A prime is consistent with the visible residual stroke, but is marked uncertain rather than silently restored. | medium |
| 16 | 23 | before groupe fini | gour | grou; the final two overtyped letters are difficult to distinguish. | low |
| 16 | 23 | under posées | faites | Initial f and medial i are mostly hidden under x strokes; visible a,t,e,s support this reading. | medium |
| 16 | 23 | last citation | SGAA XIX, with XIX both overlined and underlined | The extra A is visibly typed; it is not normalized to SGA. | high |
| 16 | 23 | following8.9, before valable | inserted opening parenthesis | The curved ink stroke overlaps the typed v; no closing parenthesis is supplied on the visible continuation. | high |
| 16 | 23 | handwritten coefficient and prime glyph throughout | ell (\ell) | The slanted hooked/crossed form matches the neighboring typed excerpt scan21; rendering changed from plain l after direct comparison, without changing any index value. | high |
| 16 | 25 | upper right | appl. | compressed abbreviation before bil. alt. | medium |
| 16 | 25 | crossed line | Point de vue | partially masked by heavy deletion | low |
| 16 | 25 | reconstruction sentence | Q | bar Q; upper stroke may be letter construction | medium |
| 16 | 25 | reconstruction sentence | isom. | first abbreviated word very faint | low |
| 16 | 25 | multiplication table i=2 | ρ'(w,x) | ρ^1(w,x); exponent/prime unclear | low |
| 16 | 25 | multiplication table i=3 | ⟨x,y′⟩ | possible overwritten + sign before pairing | medium |
| 16 | 25 | cancelled i=4 row | xξ²=0 | heavy overwriting obscures last sign | low |
| 16 | 25 | composition sentence | Quelle que soit la donnée | word endings faint | medium |
| 16 | 25 | diagonal margin | toutes les var.! | tous les var.! | low |
| 16 | 25 | Poincaré second line | itou | last letters faint | medium |
| 16 | 26 | Page43 instruction | diogramme | diagramme; typed vowel indistinct | medium |
| 16 | 26 | deleted citations | Exp. | heavily scribbled abbreviations | low |
| 16 | 26 | Page46 citation | X,4.8( a) | punctuation partly handwritten and overwritten | medium |
| 16 | 26 | Page123 citation | Exp.; dot after III | deleted text almost obscured | low |
| 16 | 26 | whole page | diagonal stroke | possible cancellation of entire sheet; reproduced geometrically | medium |
| 16 | 27 | top right parenthesis | (H^1)H^3 | second H overwritten; possible (H^1)^3 | low |
| 16 | 27 | upper crossed paragraph | Par exemple si W≠0, dans le cas alg. clos cela se réalise néc. ainsi | long crossing strokes obscure multiple words | low |
| 16 | 27 | upper crossed paragraph | impaire | paire; inserted de dim above | low |
| 16 | 27 | Q sentence | étant donné | Second reader sees étant donné in enlarged crop; first reader had tout arbitraire. Rapid thin cursive keeps a local uncertainty marker. | medium |
| 16 | 27 | induced form parenthesis | kξ+V | kξ+W; final letter looks V | medium |
| 16 | 27 | curved-arrow label | épi. | can.; short faint abbreviation | low |
| 16 | 27 | first paragraph ending | non isotrope | non dégénérée would be mathematically expected but is not the observed word | medium |
| 16 | 28 | entry23 | Notes.at | Notes at; possible spot rather than punctuation | medium |
| 16 | 29 | cancelled title | Prenons φ non dég. | crossing line masks endings | medium |
| 16 | 29 | cancelled formula | d’où φ̌∈∧²V | heavy cancellation after φ̌ | low |
| 16 | 29 | cancelled sentence | Alors χ comme forme sur ∧²V est non | last word incomplete-looking | low |
| 16 | 29 | main paragraph twice | au facteur scalaire | compressed phrase; “au ... scalaire” certain | low |
| 16 | 29 | power notation | φ̌² / φ̌^(2) | later parenthesized exponents clearer than first two | medium |
| 16 | 29 | Q notation | Q:Qχ′ | Q=Qχ′ | medium |
| 16 | 29 | orbit assertion | pourront être infinis | infinies; second reader sees infinis without a clear e, with tense/number still weakly formed. | medium |
| 16 | 29 | bottom insertion | linéairement engendrées et pleines | very light cramped script; the last word especially uncertain | low |
| 16 | 29 | last parenthesis | quand dimV croissant | croissante; final letters faint | low |
| 16 | 33 | formula4 ranges | n≤i≤2n / 0≤i≤n | old overwritten bounds tentatively recovered in deleted marks | medium |
| 16 | 33 | cancelled4′ and4″ | L_X and projector sums | multiple overlapping cancellation layers obscure several original operators and indices | low |
| 16 | 33 | cancelled5′ | uncertain leading1/2 or phi_*; Lambda_X L_X^2 | Both readers independently confirm the raised2 and printed X under Lambda in enlarged crop. Leading overwritten sign remains uncertain, with fraction1/2 preferred.; confidence detail: medium for operators and exponent; low for leading sign | medium |
| 16 | 33 | reference before7 | 3* | 3′; dark overwritten superscript | low |
| 16 | 33 | cancelled RHS7 | 4L_X(id_X−φ_*Λ_Yφ*)+2(id_X−φ_*Λ_Yφ*)L_X | operator order and coefficients poorly recoverable under ruled cancellation | low |
| 16 | 33 | bottom margin | A° | A^0; circle resembles degree sign | medium |
| 16 | 33 | critical-degree map | H^{(2n)−2}→H^{(2n)+2} | first exponent heavily overwritten; plus2 alternative retained | low |
| 16 | 33 | bottom-margin explanatory phrase | (condition du degré critique, with visible opening parenthesis | No closing prose parenthesis is visible at the torn bottom/right edge; none supplied. | high |
| 16 | 34 | top proposition second line | si i | cancelled condition too heavily crossed for certainty | low |
| 16 | 34 | upper square initial object | deleted P, H^i(X) | overtraced H alone | low |
| 16 | 34 | upper square lower arrow | L_Y^{n-i}, cancelled +1 | cancelled -1 or another exponent | low |
| 16 | 34 | upper square lower right object and upward arrow | 2(n-1)-i; phi_{2(n-1)+i} | Upward-arrow plus sign confirmed by second reader; object’s overwritten sign remains uncertain.; confidence detail: high for upward plus; low for overwritten object | high |
| 16 | 34 | upper square condition | deleted forall | overtraced mark of different shape | low |
| 16 | 34 | middle heading | Cor | Lem or a rewritten heading | low |
| 16 | 34 | middle and lower decompositions | coprod | Two uprights and a common baseline are independently confirmed; distinct circled-plus elsewhere is retained as oplus. Mathematical sum interpretation remains separate.; confidence detail: high for graphic form | high |
| 16 | 34 | first corollary revised phrase | deleted qui est un; inserted c’est; induit | cancellation and insertion attachment uncertain | low |
| 16 | 34 | exceptional map target | cancelled P^{n-1} | other initial P expression | low |
| 16 | 34 | kernel insertion | égal à celui de L_X, i.e. | Enlargement favors égal à, rather than first reading c’est; local uncertainty retained. | medium |
| 16 | 34 | kernel summand | coprod_{j>=n}P^i(X) | index of P might be j, although i-shaped dot is visible | medium |
| 16 | 34 | kernel cancelled parenthesis | (qui est un idéal) | middle words obscured by cancellation | low |
| 16 | 34 | final map | plain dash between H groups | faint arrowhead possible | medium |
| 16 | 34 | upper square vertical isomorphism-like labels | wr-shaped vertical mark | The two tiny vertical marks look like the numeral2; rendered with local wr/2 uncertainty rather than the horizontal tilde used by first reader. | medium |
| 16 | 35 | introductory K^0 relation | approx | simeq; the handwriting shows two wavy strokes without a straight lower line | medium |
| 16 | 35 | upper left of title | arrowlike graphic trace, preserved without textual interpretation | possibly paper puncture/damage rather than an intentional ink arrow; two readers concur that origin cannot be determined securely | low |
| 16 | 36 | top equation label | alpha | a or alpha followed by parenthesis | low |
| 16 | 36 | piece in operation paragraph | P^j(X) | P^i(X); superscript has a loop/descender unlike the preceding i | medium |
| 16 | 36 | operation paragraph deletion | un isom | one or two crossed words, not fully recoverable | low |
| 16 | 36 | cancelled piece before E^{n-1} | coprod_{0<=i<=n-1} L_X^{n-i}P^i(X) + | bounds and degree partly buried by zigzag cancellation | low |
| 16 | 36 | cancelled comparison | par l’isom can.; n-1<=i<=2(n-1) | short words and lower bound obscured by horizontal line | low |
| 16 | 36 | corollary cancelled kernel | coprod_{n-1<=j<=2n-1}P^j(Y) simeq Ker | bounds, variable, and final relation heavily overstruck | low |
| 16 | 36 | parenthetical last Im expression | cancelled =I | possibly a live unfinished =I; no following letters seen | low |
| 16 | 36 | small projector formulas | p_j^X and p_{j-2}^Y; n+1<=i<=2n | indices may be i; inequality lower bound overwritten | low |
| 16 | 36 | boxed lower margin | par dualité / généralisation; variante | first line crossed and both words insecure | low |
| 16 | 36 | bottom cancelled proof first line | on note que les deux mbs | short words crossed by a long rule | low |
| 16 | 37 | lemma prime ideal | fraktur p | handwritten looped p; plain p possible | medium |
| 16 | 37 | proof supports of E_i and I | bar {X} | bar {x}; handwritten crosses are large, whereas proposition support has a clearly smaller x | medium |
| 16 | 38 | top initial mark | deleted A | overtraced section label rather than deletion | low |
| 16 | 38 | upper equality | coprod_{i>=n+1}P^j(X) | P^i(X); superscript appears j-shaped | medium |
| 16 | 38 | kernel statement revision | deleted l’injectivité / l’égalité; inserted que le noyau | old word partly crossed | low |
| 16 | 38 | kernel coproduct bounds | left: uncertain full bound 0<=i<=n-1; right: 0<=i<=n+1 | right n-1 remains possible, but both readers independently see a short upright on the plus; the left second inequality is heavily overdrawn | medium |
| 16 | 38 | after kernel display | deleted donc | short stroke conceals word | low |
| 16 | 38 | large rejected block first equation | Lambda_Y phi^*=Lambda_X before phi^* Lambda_X | opening is heavily crossed and over-written | low |
| 16 | 38 | rejected verification | prem.; P^j(X)=; i.e. les ...; y est nul; le deuxième | revision sequence and final unfinished phrase uncertain | low |
| 16 | 38 | lower first brace right sum | p_X^j, bound n-1<=j<=2(n-1) | n+1 lower bound possible; enlarged ink favors a single dash before 1, unlike the preceding sum; subscript remains visibly X-like, not normalized to Y; minus sign before sum overwritten | medium |
| 16 | 38 | cancelled end of first projector identity | =p_Y^{j-2}Lambda_Y phi^* | most of expression covered by dense strokes | low |
| 16 | 38 | margin identity | bar Sigma; tt | bar may belong to drawn sigma; tt is compact | medium |
| 16 | 38 | bottom projector identity | phi^* twice, then phi_* | superscript stars appear above first two phi; not changed to subscripts to repair domains | medium |
| 16 | 39 | bibliographic spelling | Schopf; Uber | No umlaut is visible; not changed to Schöpf or Über | high |
| 16 | 39 | prime ideal symbols throughout | fraktur p | same looped handwritten form as scan037; plain/script p possible | medium |
| 16 | 40 | under first operator product | upper bound 2n | n, heavily overwritten; no repair from expected formula | low |
| 16 | 40 | generalization heading | Plus gén. | the enlarged looped initial and following strokes favor Plus; earlier Rem. alternative withdrawn | high |
| 16 | 40 | generalization second sum | p_X^i | p_X^j, index looks i-shaped despite j in bound | medium |
| 16 | 40 | derivation annotation | zero above bracket covering p_X^j and Lambda_X | bracket crosses intervening closing parenthesis; typeset as a single annotated group | high |
| 16 | 40 | C(X) implication deleted word | équivaut | old word largely hidden beneath horizontal line | low |
| 16 | 40 | lower projector formula inserted glyph | L | Lambda or annotation/correction stroke; companion margin explicitly reads L? | low |
| 16 | 40 | lower projector condition | i+j<n-1 | i+j<=n-1; thick inequality stroke does not clearly show lower bar | medium |
| 16 | 40 | after lower formula conditions | cancelled algébrique | quelconque; looped descender and late dotted stroke are visible, but dense cancellation leaves both readings insecure | low |
| 16 | 40 | bottom algebraicity condition | forall i+j<n | leading glyph may be a stray/incomplete j; strict inequality retained | low |
| 16 | 40 | bottom remaining projectors | rest. en susp. sont les; 0<=i<=2n | first abbreviation and final bound are overwritten/pale | low |
| 16 | 41 | case b threshold | n_0 | n_o; printed circular subscript does not distinguish perfectly | medium |
| 16 | 42 | first display | ψ^i_ξ | independent enlargement confirms a three-turn ξ-like glyph; previous unspecified-subscript doubt substantially resolved | high |
| 16 | 42 | first display, restriction | Λ_Xφ_i \| H^i(Y) | independent enlargement shows a dotted lower i, distinct from the explicit stars in the next formulas; earlier star alternative withdrawn | high |
| 16 | 42 | first display | φ^i:H^i(X)−H^i(Y) | plain dash without visible arrowhead retained | medium |
| 16 | 42 | first display deletion | et | small triangular cancellation may conceal another word | low |
| 16 | 42 | N.B. insertion | H^{2(n−1)} | last numeral overwritten; 2 possible | low |
| 16 | 42 | N.B. insertion right edge | m=dim X×Y | last Y is cut by sheet edge | low |
| 16 | 42 | N.B. paragraph | polarisons | pale cursive ending | medium |
| 16 | 42 | Or deletion | ξ_X⊗1+ | heavily cancelled partial expression | low |
| 16 | 42 | underbrace cancelled line | Λ_XL_Xφ_* φ_* 2id_X | connecting content obscured by cancellation; expression not silently completed | low |
| 16 | 42 | bottom cancelled line | X~Y, Y_α | subscript and relation obscured | low |
| 16 | 42 | last sentence | des sections | rapid pale cursive; possible découpés | low |
| 16 | 42 | pale repeated printing | Condor | Cordor; Concorde; six-letter Condor favored by rotated enlarged marks, but pale ink and partial occlusions prevent certainty | low |
| 16 | 42 | deleted right-hand side sum | n<=i<=2n | 0<=i<=2n; both readers see an open arch favoring n in the first glyph | medium |
| 16 | 43 | header | 977 | handwritten first digit may be 9 or q-like | medium |
| 16 | 43 | before n de B | son | heavily blacked out word | low |
| 16 | 43 | before le morphisme | donc | heavily blacked out word, final c-like glyph | low |
| 16 | 43 | cancelled first morphism | ^a u:Spec(A)→Spec(B) | initial notation under black hatching; possible f or additional X,Y labels | low |
| 16 | 43 | reference | 18.11.3.3 | final digit overwritten | medium |
| 16 | 43 | cancelled differential formula | Ω̂^1_{A/k}⊗_A A′→Ω̂^1_{A′/k} | almost completely blacked out; best trace-based attempted formula only | low |
| 16 | 43 | before Il y a | donc | short blacked-out word | low |
| 16 | 43 | before contenu | et | qui possible; cancellation very dense | low |
| 16 | 43 | before p′ | un | two blacked-out glyphs | low |
| 16 | 43 | before Spec(A′) | ^a u′: | blacked-out operator name; possibly Spec(u′) | low |
| 16 | 43 | after où | u est injectif et | blacked-out phrase; most letters no longer independently distinguishable | low |
| 16 | 43 | before isomorphisme local | immersion ouverte | immersion fermée possible; thick deletion over old underline | low |
| 16 | 43 | left margin | Virer (ii) sauf raison sérieuse ! | Vider for the first word: enlarged rotated ink has a tall third-letter stroke; raison remains slightly uncertain, sérieuse and the exclamation clear | medium |
| 16 | 43 | first paragraph, au-dessus de/du | au-dessus' de | du; raised apostrophe-like mark and overprinting are visible, but the order of layers cannot be reconstructed | low |
| 16 | 44 | subscripts and standalone parameter, throughout | ℓ\|χ | Both independent readers compared the repeated enlarged printed forms: ascending diagonal with a crossed or looped stroke and horizontal terminals. No identifying type feature securely resolves ℓ from χ; a γ-like silhouette is also possible in heavier impressions. The alternative is explicit at each occurrence, without normalization from subject matter. | low |
| 16 | 44 | after polarization in characteristic zero | subscript x | visible low printed x; may be a cancellation over former punctuation | medium |
| 16 | 44 | formula after in terms of A | XxX and YxY | typed x glyph retained as upright x, not supplied cross sign | high |
| 16 | 44 | after C(X) expression | two dots .. | two visible dots; enclosing prose parenthesis is not visibly closed | high |
| 16 | 44 | before so that | inserted ( and so | dark overwriting before s; possible additional struck glyph | medium |
| 16 | 44 | dimension expression | C^{n−i} | last exponent thick; 1 possible | medium |
| 16 | 44 | independant of [blank]) | blank retained | no visible ℓ or polarization symbol in that gap | high |
| 16 | 44 | after blank parenthesis | bu | no visible final t; not corrected to but | high |
| 16 | 44 | before A_ℓ(X,ξ) | A(X) | cancelled with overtyped x marks | low |
| 16 | 44 | C_ℓ argument | ξ | long simple handwritten stroke; fewer lobes than other ξ | medium |
| 16 | 44 | before priori | a | small black cancellation at preceding line end | low |
| 16 | 45 | top first operator | A | Q-like exterior oval and tail overlap A-like inner strokes; the order of the overwriting is not established. | low |
| 16 | 45 | repeated parameter glyph | printed ℓ\|χ; handwritten ℓ\|l in the second and third terms of (v) | The printed crossed forms match scan44 but do not identify the letter conclusively; both readers agree on the explicit ℓ\|χ alternative. In (v), the last two parameters are visibly handwritten short curved l-like strokes, unlike the printed first parameter; the local form is retained separately. | low |
| 16 | 45 | polarization arguments | ξ | long simple handwritten curves; graphical identification uncertain | medium |
| 16 | 45 | proposition heading | Condititions; verieté | visible typographical forms retained rather than corrected | high |
| 16 | 45 | (ii) exponent | deleted 0 | small overtyped block with oval trace | medium |
| 16 | 45 | (ii) cancelled phrase | où l’exposant 0 | overtyped x characters across text | medium |
| 16 | 45 | (iv) cancelled beginning | Pour tout n\|O\|0 | A possible n-like right stem or hump overlaps a conspicuous large oval under the x-strikes. Both independent readers see the oval but cannot identify one secure final glyph or the order of overtyping. | low |
| 16 | 45 | (iv) operator | Λ_Xφ_* | lower star is rapidly drawn and omega-like | medium |
| 16 | 45 | (iv bis) target exponent | j with inserted −2 | 2 clear, minus indistinct; target closing parenthesis clipped away | low |
| 16 | 45 | corollary first word | Cés | accent-like black mark over e; Ces possible | low |
| 16 | 45 | condition (v) ending | plus sign followed by blank then comma | no visible dots supplied | high |
| 16 | 45 | bottom insertion | non sing. | rapid handwritten abbreviation; first word somewhat overwritten | medium |
| 16 | 46 | top condition (vi) | A_{ℓ} | Heavy hooked crossed glyph may be χ; compared visually with scan45 adjacent thin ℓ-like subscripts. γ was the earlier alternative, now less supported by the stroke comparison. | low |
| 16 | 46 | first paragraph | thhe | the with overtyping | low |
| 16 | 46 | second paragraph opening | thenproof | the proof; damaged or overwritten spacing | low |
| 16 | 46 | typed deletion in second paragraph | are of course implied by (i) because of the stabilities because C_ℓ(X) et C_ℓ(Y) | Heavy hooked crossed glyph may be χ; compared visually with scan45 adjacent thin ℓ-like subscripts. γ was the earlier alternative, now less supported by the stroke comparison. | low |
| 16 | 46 | cohomology chain at right edge | H^i(X) | last argument cropped by page edge; all three connectors appear plain strokes | low |
| 16 | 46 | deleted symbol before Λ formula | φ_* | overstruck symbol before parenthesis | low |
| 16 | 46 | N.B. formula at right edge | id_X | final parenthesis and subscript cut at scan boundary | medium |
| 16 | 46 | last paragraph | dim 0 | car 0 overtyped; preserve visible dim rather than correcting the mathematics | low |
| 16 | 46 | bottom handwritten addition | also if for 1-cycles, τ-equiv. = num. équivalence .... | for, τ and abbreviation ending uncertain | low |
| 16 | 47 | bibliographic reference in paragraph 1 | Soc. | final c overtyped; Seeies clearly retained as typed | medium |
| 16 | 47 | paragraph 3, I ... look | wihl | will with overtyping | low |
| 16 | 47 | paragraph 3, first birationally | biratmonally | birationally with overtype over i/o; typed spcialisation retained | low |
| 16 | 48 | C,D subscripts throughout | ℓ | Heavy hooked crossed glyph may be χ; compared visually with scan45 adjacent thin ℓ-like subscripts. Heading may also be 1 after overtyping. | low |
| 16 | 48 | first line | a inserted-space few | vertical pencil stroke may only mark typographic separation | medium |
| 16 | 48 | b, coefficients | coefficients | last letters faint | medium |
| 16 | 48 | proof, codomain of v | 2n-i | first digit overtyped | medium |
| 16 | 48 | proof, before algebraic isomorphism | the | overtyped/handwritten letters | medium |
| 16 | 48 | Hamilton-Cayley formula | u^h, u^{h-1} | w^b; the first visible letter resembles u and exponents resemble h; no mathematical correction made | low |
| 16 | 48 | last line | coefficients | word clipped at right edge | medium |
| 16 | 49 | corollary subscript | Cℓ | Heavy hooked crossed glyph may be χ; compared visually with scan45 adjacent thin ℓ-like subscripts. γ was the earlier alternative, now less supported by the stroke comparison. | low |
| 16 | 49 | corollary codomain and insertion | δ | d; overtyped loop/ascender; Z visibly underlined | low |
| 16 | 49 | lower paragraph, But to get ... | it | overtyped final letter | medium |
| 16 | 49 | last line | of | an under overtyping | low |
| 16 | 50 | throughout | ℓ subscripts | Heavy hooked crossed glyph may be χ; compared visually with scan45 adjacent thin ℓ-like subscripts. γ was the earlier alternative, now less supported by the stroke comparison. | low |
| 16 | 50 | opening paragraph | paragraph | faint a in middle | medium |
| 16 | 50 | second condition deletion | of H^i(Y) whose image in / algebraic, is algebraic is | first word and last overwritten is are uncertain; x-strikes and handwriting overlap | low |
| 16 | 50 | specifications paragraph | us, crittcal | critical; worn letters not silently normalised | low |
| 16 | 50 | proposition opening | Cℓ(X) | Heavy hooked crossed glyph may be χ; compared visually with scan45 adjacent thin ℓ-like subscripts. γ was the earlier alternative, now less supported by the stroke comparison. | low |
| 16 | 50 | proof, Aχ argument | X deleted ×X | crossed characters compressed into a dark patch | low |
| 16 | 50 | first factorization, last object | H^{2m+2} deleted X (X) | crossed baseline letters may number two | low |
| 16 | 50 | factorization arrows | dash for last even connector and both odd connectors | small terminal ticks may be incomplete arrowheads; first two even arrows are clear | low |
| 16 | 50 | odd map before second factorization | 2m+1-1 | small handwritten curved mark beneath m/plus; exact grouping unclear | medium |
| 16 | 50 | middle, second-case inverse formula | simple cross superscript on phi | plus \| star | medium |
| 16 | 51 | lemma insertion | de degré deleted 2n -2(n-i) | crossed term before negative degree not fully clear | low |
| 16 | 51 | left margin | (et vice versa) | last word may be abbreviated; leader points at composite | low |
| 16 | 51 | lemma conclusion | L! | L followed by an exclamation-like slanted mark at baseline; not treated as superscript | low |
| 16 | 51 | after L | deleted les π | last deleted glyph may be a different projector sign | low |
| 16 | 51 | lemma factor name | élémentaires | compressed handwriting; reading follows broad letter pattern | low |
| 16 | 51 | lemma factors and proof | ξ^j P^i | j placement resembles subscript ξ_j; retained explicitly uncertain | low |
| 16 | 51 | deleted inequalities | et i+2j≤n ou i+2j≤2n-i ou | connective words and second right-hand bound crossed through | low |
| 16 | 51 | corollary ii | 1≤i<n | upper relation could be ≤ | low |
| 16 | 51 | corollary ii, inverse de | J^i | ξ^i; tall hooked glyph not the ξ form of lemma opening | low |
| 16 | 51 | corollary consequence | facteurs décomposition | facteurs élémentaires; tightly compressed word unresolved | low |
| 16 | 52 | Fitting name three occurrences | Filting | Fitting; typewritten first medial consonant resembles l rather than t | medium |
| 16 | 52 | above p. f. | ! | two small black marks may be pen annotation or nontextual blemish; transcribed provisionally as a doubtful mark | low |
| 16 | 53 | first line | prouvé | short compressed word after lemme | medium |
| 16 | 53 | projectors throughout upper paragraph | p_i, p_j, p_k | ρ_i, ρ_j, ρ_k; loop form is ambiguous | low |
| 16 | 53 | second line | Alg | A with trailing/subscript character; visible letters resemble Alg | low |
| 16 | 53 | T_{k′} bound | k′≤k | strict < | low |
| 16 | 53 | H superscript in nullity assertion | j | i; following phrase says j≠k | low |
| 16 | 53 | u subscript in equation | k | n | low |
| 16 | 53 | deleted word after comme on voit | ainsi | crossed tightly written word | low |
| 16 | 53 | middle map label | ξ^{n-k-j} | ξ^{n-k+j}; preceding expression clearly uses plus, arrow label appears minus | low |
| 16 | 53 | middle right annotation | qui est nul / deleted sur / inserted de noyau N | overlapping cancellation and leader make exact state and attachment uncertain | low |
| 16 | 53 | lower crossed phrase | coïncide à 1 | first two words and final character obscured by cancellation | low |
| 16 | 53 | last operator sentence | est, nul | tiny est is compressed and punctuation may be a pen mark | low |
| 16 | 54 | opening continuation | localisée et une | localisée d’une; type appears to read et une | medium |
| 16 | 54 | ideal symbols throughout | q, m | handwritten forms may have been intended as Gothic letters; no clear distinct Gothic strokes | medium |
| 16 | 55 | opening operator | n-k+j | n-k-j; small sign before j not fully distinct | medium |
| 16 | 55 | primitive factor letters | p^{i′}, then P^i | P^{i′}, p^i; case varies visually and must not be regularised from convention | low |
| 16 | 55 | deleted word before comme | de | scribbled short word | low |
| 16 | 56 | ideal symbols throughout | p, q | handwritten forms may be intended as Gothic, but no distinctive Gothic alphabet is visible | medium |
| 16 | 56 | last line | x∈B′ | x∈B; raised printed mark after B resembles a prime, though B′ is only introduced on printed page 3 | low |
| 47 | 2 | title, first line at right edge | convolution | ending is compressed against the edge, with a terminal horizontal stroke; no additional word resolved | medium |
| 47 | 3 | top cancelled line after X un schéma sur S | tel que … géométriques | heavy cancellation obscures about three intervening words; final reading tentative | low |
| 47 | 3 | cancelled phrase after et tel que | pour que … | four-word estimate beneath heavy horizontal cancellation | low |
| 47 | 3 | derived-category subscripts, three occurrences | parf | prof; the middle vowel is compressed; no expansion silently imposed | medium |
| 47 | 3 | left marginal generalization, after D_qcoh(A) | on peut enfin généraliser en / ou bien: accouplement / [deleted un] accouplement | the succession of the two accouplement phrases and their cancellation status is difficult; diagonal writing crosses the bracket | low |
| 47 | 3 | left margin, after et même pas | besoin du groupe | compressed words may read autrement; the following C and et partir de quelconques are clearer | low |
| 47 | 3 | left margin, deletions before F,G and before final kernel identity | parf.; tel; R | the cancelled fragments are heavily overwritten and only partial letterforms remain | low |
| 47 | 3 | bottom (*) | L-derived star; Rπ_* | star written over an earlier tensor-like shape; subscript star also resembles α | medium |
| 47 | 3 | main definition and bottom external product | ⊗, with subscript S at bottom | no square outline discernible; not normalized to ⊠ | high |
| 47 | 3 | first main Φ category line and marginal π line | plain horizontal stroke | arrowhead not visible; retained as a dash | medium |
| 47 | 3 | upper right, parenthesis explaining s | pt | est | medium |
| 47 | 4 | first cancelled formula, upper right | Rpr₂*(Lpr₁*(F L⊗ G)⊗L) | Lf* may replace Lpr₁*; dense scribble prevents exact reading of inner pullback | low |
| 47 | 4 | rightmost expansion of first formula | π_* | Rπ_*; there may be an attached R before the small addition-map symbol | medium |
| 47 | 4 | Künneth line | Rpr₂(F⊗L) | star not visibly present after first pr₂; retained omission rather than inserted | medium |
| 47 | 4 | theorem symmetry operator, three occurrences | s_A / s_A* | σ_A / σ_A*; the handwritten form is angular and very short | medium |
| 47 | 4 | theorem first line, cancelled fragment before L | B | overwritten two-stroke fragment cannot be identified securely | low |
| 47 | 4 | main formula jump after associativity | blank parentheses with return line to previous right-hand side | the argument is supplied by a drawn leader, not rewritten; the transcription keeps the blank and a connecting line | high |
| 47 | 4 | arrowheads in first diagram and K-theory maps | bottom pr₂ and both K-theory maps as plain strokes | tiny terminal swelling might be an abbreviated arrowhead; other arrowheads on the page are clearer | medium |
| 47 | 4 | upper middle, theorem-of-the-square product | second projection subscript looks 13 again | 23 | medium |
| 47 | 5 | category subscripts throughout | parf | prof; repeated short form retained with uncertainty; margin spells parfaits clearly | medium |
| 47 | 5 | top determinant formula | Λ with n written immediately above, followed by t_A and t_B | small overmark could be a hat; retained as an uncertain n in the observed overhead position | medium |
| 47 | 5 | top cancelled identity phrase | identique, … | two following words beneath cancellation cannot be resolved | low |
| 47 | 5 | circled cancellation upper right | de catégories | possibly mathematical letters; almost completely overwritten | low |
| 47 | 5 | corollary number and newly defined operator | 3; D_L | number2; operator/subscript glyph could differ | low |
| 47 | 5 | first corollary displayed input | F L⊗ G | star and tensor were overwritten; retained tensor/star uncertainty | medium |
| 47 | 5 | kernel category | M∈D_parf(A) | only A is written, despite the subsequent kernel calculation on A×A; not repaired | high |
| 47 | 5 | kernel formula first derived letter | R | L-like under-stroke beneath retracing; later text explicitly says Rpr₁₃* | medium |
| 47 | 5 | final line φ map target | φ:A–B | no star visible after B, although adjacent prose twice says B* | high |
| 47 | 5 | cancelled word before produit de Convolution | couple | coupu / coup…; heavily struck | low |
| 47 | 6 | diagram and lemma product factors | star on first B, cancelled star on second B | ink on second superscript is densely overwritten; some first-star occurrences are faint | medium |
| 47 | 6 | lemma conclusion after e_* | deleted O_B*[−n]⊗τ_B* | O_S may replace O_B*; the deleted tensor/twist segment is highly uncertain | low |
| 47 | 6 | lemma zero-section subscript | e_{0*} | e_{B* *}; the subscript is a filled blob | low |
| 47 | 6 | left margin differential formula | ω=det*(Ω¹_B*/S) | det e*; denominator could be A; copied locally without imposing a standard determinant convention | low |
| 47 | 6 | corollary first display | Lψ*(τ_B*[−n]) | small crossed fragment after τ_B* may contain a superscript rather than a star; no e_* is visible in this display | medium |
| 47 | 6 | last paragraph φ target | C* | B* would fit surrounding notation, but the observed letter is a clear open C; preserved C* | high |
| 47 | 6 | last cancelled phrase | le même résultat | le …; line heavily crossed and final word compressed | low |
| 47 | 6 | projection indices | pr₁/pr′₁ in diagram and corollary, pr₂/pr′₂ in the initial base-change equations | indices are visibly different; not normalized | high |
| 47 | 6 | last line | modulo dém. du Lemme1 | first word and abbreviation are lightly written but readable | medium |
| 47 | 7 | Lemme2 variety label in cohomology | H^i(X,L), H⁰(X,L) | the prose uses B but the formulas visibly use X; preserved | high |
| 47 | 7 | upper cancelled boxed material | si L≄O_B; H⁰(X,L)=k si L≃O_B | large angular cancellations cross the condition and some equals signs; exact first si is uncertain | medium |
| 47 | 7 | cancelled lemma proof last clause | si i>0 | last comparison/zero lies beneath double cancellation lines | low |
| 47 | 7 | Nous allons … et nous … | montrer | montrerons; ending compressed at right margin | medium |
| 47 | 7 | canonical-map cancelled targets | e_*O_S[−n], e_*O_S, and [−n] | some first operator glyphs are fully overwritten; reconstruction limited to visible e/O/S/brackets | low |
| 47 | 7 | before e*R^np_*W | eq. | e_B*; short heavy mark may be a label rather than formula | low |
| 47 | 7 | last cancelled phrase | fera correspondre | first word may be fera; second word almost fully crossed | low |
| 47 | 7 | diagram q edge | plain vertical stroke | no arrowhead distinguishable; other three arrowheads clear | medium |
| 47 | 8 | derived pointwise test | x∈B* and Li_x* | b∈B* and Li_b*; first point glyph has several overlapping strokes | medium |
| 47 | 8 | complement of unit section | B*−e₁(S) | B*−e(S); a vertical small stroke is visible below e | medium |
| 47 | 8 | remark1b surviving convolution formula | Φ_L(F)*e_t | no minus visible before t although preceding two formulas use e_{−t}; not harmonized | high |
| 47 | 8 | remark1b cancelled factors | ω[n] and ω[n]e | characters beneath diagonal crossout partly lost; trailing e-like character may be subscripted | low |
| 47 | 8 | remark1b opening brace | { before Φ_L(F)*e_t | no matching closing brace clearly visible on the line | medium |
| 47 | 8 | rank margin | r-g virtuel | rang virtuel; first word is abbreviated or highly compressed | medium |
| 47 | 8 | cancelled start of remark2 | sur les VA relatives | first two words uncertain; VA and relatives more legible | low |
| 47 | 8 | determinant operation | det*∘Φ_L | star clearly raised; not replaced by an unstarred determinant | high |
| 47 | 8 | left margin, coefficient group in H0 | doubled-stroke Z | bold Z | medium |
| 47 | 9 | small raised mark after φ(λ) | ε | star or corrected small sign; no clear reading from enlarged image | low |
| 47 | 9 | Chern-character argument | cl L | λ; overwritten letters at the argument cannot be distinguished securely | low |
| 47 | 9 | total Chern class argument | λ | L; retraced glyph | medium |
| 47 | 9 | notation for total Chern class | ct on a common baseline | c_t; t is not visibly lowered, so rendered as operator ct | high |
| 47 | 9 | total Chern-class expansion denominators | 2χ; 3!χ²; n!χ^(n−1) | these powers appear one lower than expansion of the preceding binomial expression; recorded as written, with uncertainty only in faded final1 | high |
| 47 | 9 | last divisibility denominator | k!χ^(k−2) | 2 is visibly written; not replaced with k−1 | high |
| 47 | 9 | heuristic cancelled factor between χ and L′ | cl | tensor sign; tightly hatched cancellation | low |
| 47 | 9 | last cancelled factor | χ | small crossed mark could be another scalar; retained uncertainty | low |
| 47 | 9 | left Mumford note | indépendant des résultats de Mumford | du résultat in the middle line | medium |
| 47 | 9 | last general coefficient exponent | n−1 | final1 very faint; photographed as short dot/stroke | medium |
| 47 | 10 | first identity label and final reference | a) | α); handwritten loop resembles Greek alpha; uncertain locally | medium |
| 47 | 10 | ambient group for D | Gr¹(A×A) | A×B would align with later kernel discussion, but both visible letters here are A | high |
| 47 | 10 | definition of ψ_D | lowercase ψ_D | capital Ψ_D; pen form is a trident with long descender | medium |
| 47 | 10 | cancelled central first identity | ψ_D(xy) | no distinct star between x and y visible; retained ordinary juxtaposition | medium |
| 47 | 10 | central cancelled passage restarts | Alors; ce qui précède | short initial word and several cancelled words partly obscured by broad outline | low |
| 47 | 10 | first surviving RR comparison | ψ_D(ch(a))T | x instead of a inside ch; the shape is an open loop and differs from nearby x strokes | medium |
| 47 | 10 | last boxed formula first argument | a*b | a may retain an overdrawn ch-prefix; source is retraced | medium |
| 47 | 10 | map Gr•(A)_Q–Gr•(B)_Q | plain horizontal stroke | no arrowhead distinguishable | high |
| 47 | 10 | penultimate deleted term and factor | ch(x*y); T | dense local overwriting does not allow exact recovery beyond these shapes | low |
| 47 | 10 | coefficient symbol of both graded groups | \mathbb Q | \mathbf Q; visibly retraced circular/diagonal form does not settle font weight | medium |
| 47 | 11 | reference after appliquer ch | a) | α), as on previous scan | medium |
| 47 | 11 | factor between transformed classes in second and boxed displays | juxtaposition | no distinct convolution star is visible here, though the top K-theory identity has a star | high |
| 47 | 11 | second display punctuation | extra closing parenthesis after ψ_D(chy) | opening parenthesis may have been absorbed in the cancelled restart; preserved rather than balanced | high |
| 47 | 11 | slanted margin graded symbol | Gr•(A)_Q | Gr(A)_Q; tiny mark after Gr may be punctuation rather than degree mark | medium |
| 47 | 11 | word cancelled under démontrées | différentielles | letters traversed by a heavy horizontal cancellation; ending appears -iques or -ielles | low |
| 47 | 11 | parenthetical after démontrées | cas spéciaux | final word very cursive; possible cas fibrés, cannot establish exact wording | low |
| 47 | 11 | second Kleiman name | Kleiman followed by cancelled n | possibly terminal retracing rather than an additional letter; name itself ends clearly before the blot | medium |
| 47 | 11 | two derived duality displays | Φ_L with same kernel subscript on both sides; checkF and superscript∨ on result | no separate dual mark visible on the kernel L; first argument is explicitly checked, distinct from result’s superscript vee | medium |
| 47 | 11 | boxed duality formula ending | [n] with no closing parenthesis | right boundary of box is visible but no distinct parenthesis before it | high |
| 47 | 11 | automorphism formula last argument | f | F; the right-hand glyph is lowercase-shaped, unlike first F | medium |
| 47 | 11 | final line abbreviations | Id. then another Id.-like insertion before pourφ_L | far-right tall mark may be a cancellation or connective; lower short abbreviation overlaps the line edge | low |
| 47 | 11 | first derived duality display, shift | [n] | [-n]; long low horizontal first stroke of n may be a separate minus, unlike clearer [n] in the boxed repetition | medium |
| 54 | 2 | title line 1 | Dualité | compressed middle strokes and final accent | medium |
| 54 | 2 | title line 2 | des | rapidly connected strokes | medium |
| 54 | 3 | top-right descriptor | Ch. | Coh.; shortened initial word before de Hodge-DeRham | low |
| 54 | 3 | second tangent formula | n | H exponent is compressed; Ω exponent reads n−1 | medium |
| 54 | 3 | first sequence label | S_A | overwritten initial S | low |
| 54 | 3 | first sequence middle object | H^1(A) | H reinforced/overwritten | medium |
| 54 | 3 | side note | car. | abbreviation ending compressed | medium |
| 54 | 3 | middle paragraph | interprétation | rapid compressed middle letters | medium |
| 54 | 3 | revised middle sentence | se / classifie / est | overwritten syntax and placement; all visible text retained | low |
| 54 | 3 | middle formula | uline V_A | V reinforced; underline and subscript overlap | low |
| 54 | 3 | middle formula deletion | V | small cancelled symbol after = | low |
| 54 | 3 | Hom insertion | comma before V | could be an arrow-like mark; retained in symbol-level doubt | low |
| 54 | 3 | after formula | donc | partly crossed by insertion leader | medium |
| 54 | 3 | universal vector-group symbol | bold V | overwritten strokes resemble W | low |
| 54 | 3 | lower paragraph | transposée | heavily reinforced first letters, underlined | medium |
| 54 | 3 | last line | Plus préc. | Plus gén.; abbreviation indistinct | low |
| 54 | 3 | classification sentence correction layers | lower deleted définie, upper inserted classifie; upper phrase ends se | two readers agree there are probably two overlapping layers; lower word remains uncertain, upper terminal could be est | low |
| 54 | 4 | whole typed block | deleted text | A single diagonal traverses all printed paragraphs; represented as deletion of each paragraph. | medium |
| 54 | 4 | corollary heading | 4.1.1 quater | 4.1.2 quater; X-overtyping obscures digit | low |
| 54 | 4 | proof reference | 4.1.1 bis | overtyped reference, superseded by Prop.A | low |
| 54 | 4 | after un A_f | aux | short overtyped word | low |
| 54 | 4 | right edge line ending | qu’il | last letter at clipped page edge | medium |
| 54 | 4 | proposition new exponents | n+1 | small handwritten superscripts | medium |
| 54 | 4 | handwritten corollary lines1–3 | anneau / module / (I_i) / I=intersection I_i / tels que | heavy strokes and cancellations obscure text; these remain attempted readings rather than reconstructed theorem | low |
| 54 | 4 | handwritten corollary module | M tensor A/I_i; A_i | quotient and subscript uncertain | low |
| 54 | 4 | handwritten corollary revision | Supposons qu’on | word after Supposons revised/overwritten | low |
| 54 | 4 | last deleted words | pour les conditions, alors | partly off lower edge and crossed by heavy line | low |
| 54 | 4 | last formula upper right | M_0 libre sur A_0 | very small subscript and final base-ring symbol | low |
| 54 | 4 | missing operators in typescript | f A-p; A A′; A A_i; i I | Spaces preserved where no membership or arrow symbol is actually visible. | high |
| 54 | 4 | small layer above handwritten noethérien | noeth. | several low connected strokes and a tall h-like stem crossed by a long line; exact abbreviation uncertain | low |
| 54 | 4 | handwritten ideal family and tensor quotient | I_i as originally encoded | glyph may be a p-like ideal letter (e.g. p_i), especially inside intersection and quotient; no normalization made | low |
| 54 | 5 | opening and flag caption | duals | duaux; final cursive stroke ambiguous, spelling not normalized | medium |
| 54 | 5 | first displayed duality | Omega_A^p in H^q(B,...) | Ink resembles A, despite expected B in this place | medium |
| 54 | 5 | reduction line | dim | abbreviation uncertain; could denote degree rather than dimension | low |
| 54 | 5 | after cancelled De plus | or | short replacement word | medium |
| 54 | 5 | middle | suffirait | ending compressed | medium |
| 54 | 5 | Cartier paragraph start | Considérons | rapid long word | medium |
| 54 | 5 | Cartier group notation | p^A and p^B | Could be left-subscript p attached to A/B; visible raised A/B preserved as superscript | low |
| 54 | 5 | first degree | cancelled 2 before d | overwritten initial exponent mark | low |
| 54 | 5 | bottom deletion | Notons que | initial word partly crossed | medium |
| 54 | 6 | first deleted Y hypothesis | réduit | X-overtyping obscures letters | medium |
| 54 | 6 | after fermé | X de | short X-overtyped phrase | low |
| 54 | 6 | all factorization expressions except one inserted arrow | blank spaces between scheme/ring symbols | No arrows supplied where none is visible on typescript | high |
| 54 | 6 | coefficient-zero subscripts throughout proof | o | Could be typewriter lowercase o used for zero; visible shape o retained | medium |
| 54 | 6 | right edge proof line | toute | final letter close to cropped right edge | medium |
| 54 | 6 | last cancellation | l’on | X-overtyping | low |
| 54 | 7 | top diagram final upper object | V | A; ink forms an open V without crossbar | low |
| 54 | 7 | exact sequence first arrows | plain joining strokes | first two arrowheads absent/indistinct; rendered no head | medium |
| 54 | 7 | exact sequence duality letter | D | curved handwritten D | medium |
| 54 | 7 | extension description | cancelled A under F^B | small overwritten subscript or displaced superscript A | low |
| 54 | 7 | bubble | muni | munie; ending joins next word | medium |
| 54 | 7 | bubble p-power term | p-ième | p.ième; punctuation/short connector ambiguous | medium |
| 54 | 7 | p-group notation throughout | p^A | As on scan5, raised A may encode a left-subscript p in conventional notation | low |
| 54 | 8 | first intersection index | M | underlined set symbol partly soft/overtyped, read M | medium |
| 54 | 8 | all circular subscripts in corollary3 and proof | o | 0; typewriter circle does not securely distinguish lowercase letter from zero | medium |
| 44 | 2 | upper right | 7 | question mark; isolated mark | low |
| 44 | 2 | section letter | A | reinforced/overwritten glyph | medium |
| 44 | 2 | theorem1 N argument | xi | zeta; long cursive loop | medium |
| 44 | 2 | theorem1 cancellation | des | donc; short struck word | low |
| 44 | 2 | cycle symbols | calligraphic Z | plain Z; three-stroke curled form differs from straight numerator Z in Th.3 | medium |
| 44 | 2 | cycle quotient subscript | alb | ab; middle small stroke | medium |
| 44 | 2 | theorem3 target symbol | P^i | very cursive initial P | medium |
| 44 | 2 | theorem3 dual index | n−i | n+1−i; first part of superscript overwritten | low |
| 44 | 2 | theorem4 bracket | donc la corr. sur | compressed phrase before underlined P^m | low |
| 44 | 2 | theorem4 final participle | associé | associée; visible ending not grammatically normalized | medium |
| 44 | 3 | opening direct sum | coprod | two upright strokes on a baseline; not circled plus | high |
| 44 | 3 | filtration condition | adique | faint compressed word | medium |
| 44 | 3 | first paragraph A after sur | A_0 | subscript faint | medium |
| 44 | 3 | repeated canceled word before plat | plat | heavily crossed short word | low |
| 44 | 3 | condition on M | TF | two capitals; condition not defined locally | high |
| 44 | 3 | unfinished insertion under first sequence | [M′= | short overwritten bracket/letters, no completed right side | low |
| 44 | 3 | marginal direct sum summand | M_nu | M_i; subscript resembles nu | low |
| 44 | 3 | completed sequence last nonzero term | Mhat prime | double prime; dark overwritten prime mark | low |
| 44 | 3 | tail condition | x_i=0 | x_i≠0; horizontal overwriting | medium |
| 44 | 3 | foot transition | on voit que | very compressed and possibly one word omitted by faded ink | low |
| 44 | 3 | chevron insertion | TF | overwritten letters | low |
| 44 | 3 | whole-page deletion layers | draft canceled, last foot note inserted | relative ordering of final dark note and page cancellation unclear | medium |
| 44 | 4 | top canceled arithmetic | 2n | n; final glyph overwritten | low |
| 44 | 4 | canceled word before Z | même | possibly unrelated short clause | low |
| 44 | 4 | star and cycle alphabet | mathcal Z star | star heavily reinforced but visible | medium |
| 44 | 4 | insertion before i+j=n | et canceled | illegibly overwritten short word | low |
| 44 | 4 | pencil callout | dont toutes les fibres sont géom. intègres | toutes canceled; small word fibers inferred from strokes | medium |
| 44 | 4 | codimension cancellation | en dim | small obliterated phrase | low |
| 44 | 4 | Néron–Tate bracket indices | P^i(Y),P^j(Y) | first superscript faint, second resembles0 | low |
| 44 | 4 | pairing sign exponent | m | small m; retained rather than changed to i | medium |
| 44 | 4 | left NB ending | au sens général | en sens géométrique; final two words weak | low |
| 44 | 4 | right callout | Doit résulter d’un énoncé plus général sur des fibrations | général versus fin; compressed but overall sentence recoverable | medium |
| 44 | 4 | theorem6 struck phrase | Et [est égale àP^i(X)] | first word and phrase layered | low |
| 44 | 4 | theorem6 canceled condition | Si2i=n, n=2i, si n pair et i=n/2 | multiple overwrites; syntactic order uncertain | low |
| 44 | 4 | theorem6 final canceled inequality | 2i≤n+1 | comparison crossed by leader | low |
| 44 | 4 | maps in theorem6 | P^i(X)—P^i(Y) | no unequivocal arrowheads; represented by dash | high |
| 44 | 4 | main line éléments de in theorem 5 | P^i(Y), P^j(Y) | first superscript overwritten; second is a small loop also compatible with 0, as in following bracket | low |
| 44 | 4 | above canceled theorem-6 condition | pour | pair; first reader independently agrees the looped descender favors pour, but heavy cancellation prevents certainty | low |
| 44 | 5 | root-set glyph | Delta | repeated triangular overwritten mark, sometimes top horizontal stroke | medium |
| 44 | 5 | condition1b scalar | n∈Q | right edge tight but Q legible | high |
| 44 | 5 | NB cancellation | étant un | two heavily struck words | low |
| 44 | 5 | NB canceled formula | (x,y)=(x′,y′) | earlier bilinear form expression overwritten beyond secure reading; symbols marked individually | low |
| 44 | 5 | coroot coefficient | gamma_alpha | sigma_alpha; tall looped glyph with attached alpha subscript | medium |
| 44 | 5 | after i.e. les | c | isolated black canceled letter | low |
| 44 | 5 | under provient du | zigzag and parallel strokes | possibly stylized underlining rather than mathematical symbols | medium |
| 44 | 5 | definition2 canceled condition | en dualité | overwritten below accouplés àZ | low |
| 44 | 5 | condition2b old variable | alpha′∈Delta′ | alpha heavily overwritten | medium |
| 44 | 5 | reflection input | xi | gamma; elongated cursive s-shaped variable | low |
| 44 | 5 | condition2b canceled tail | ainsi | word fully hatched | low |
| 44 | 5 | condition2b′ quantified root | gamma | xi; distinct from primed input below but uncertain | low |
| 44 | 5 | last word | invarie | visible nonstandard verb retained | high |
| 44 | 5 | canceled NB formula right edge | terminal equals sign | two short parallel dark strokes follow the closing parenthesis; interior formula remains uncertain | high |
| 44 | 6 | margin attribution | Matsusaka | compressed proper name; begins Mats and ends aka | medium |
| 44 | 8 | first paragraph range | 0 | 1; typewriter character overwritten and heavy, ink reads0 before1 | low |
| 44 | 8 | initial corrected letters | d,g,c | manuscript reinforcements/corrections retained as insertions; overwritten original letters not recoverable separately | medium |
| 44 | 8 | Tate-module index | ell | typewritten l with handwritten loop | high |
| 44 | 8 | cohomology coefficient underline | underlinedZ_l | underline atZ before ell visible | medium |
| 44 | 8 | tangent note relation | subset | in; reinforced left stroke | medium |
| 44 | 8 | tangent note H index | i | very small index byH | medium |
| 44 | 8 | canceled middle margin | H^1(J^i)≃ Alg. de Hodge | first exponent couldi; words crossed by two long strokes | low |
| 44 | 8 | lower margin opening | Ça veut dire | first compressed phrase weak | low |
| 44 | 8 | lower margin ellipsis | four dots | four or five visible ink points | low |
| 44 | 9 | canceled two letters after si tu y tiens | tu | xx cancellation characters over an unrecoverable two-letter word | low |
| 44 | 9 | soient p et q | soient | fourth character combines an e bowl and tall t-like vertical/cross strokes; soi(e\|t)nt retained without inferring correction order | medium |

# Abbreviations encountered

Expansions are editorial hypotheses and never replace the abbreviated forms in the transcription.

| Form on scan | Probable expansion | Locations |
|---|---|---|
| 3e | troisième | 44:7 |
| = (in the prose il en est de = de) | même | 16:55 |
| AGS | artinian group scheme (provisional expansion from adjoining bibliography) | 16:30 |
| Alb | Albanese | 44:2, 44:8, 44:9 |
| Alg | algébrique(s) | 16:53 |
| Alg. | Algèbre | 16:52, 16:54 |
| Alg. | algèbre (canceled marginal reading uncertain) | 44:8 |
| Ann. of Math. | Annals of Mathematics | 16:28 |
| Append. | Appendice | 16:26 |
| Archiv. der. Math. | Archiv der Mathematik | 16:39 |
| BR | cross-reference abbreviation in source, not expanded here | 16:21 |
| BR II | Second part of an internally cited Brauer text; exact bibliographic identification deferred | 16:23 |
| Br | Brauer | 16:23 |
| Br′ | Brauer-type group; prime retained | 16:21 |
| Cf. | Confer | 16:28 |
| Ch. | cohomologie (reading uncertain) | 54:3 |
| Cor | corollaire | 16:17, 16:34 |
| Cor. | corollaire | 44:4 |
| De = | De même (equal-sign shorthand on the manuscript) | 16:7 |
| Dém | Démonstration | 16:51 |
| Dém | démonstration | 16:16 |
| Dém. | démonstration | 16:10 |
| EGA | Éléments de géométrie algébrique | 16:26 |
| Ex | Exemple | 16:29 |
| Exp. | Exposé | 16:26 |
| Gr | gradué (filtration not specified here) | 47:10, 47:11 |
| Gr | gradué (precise filtration not specified on this page) | 47:9 |
| Gr | groupe (associated to the indicated Lie algebra; convention requires verification) | 54:5 |
| IMAG | Institut Montpelliérain Alexander Grothendieck | 54:1, 44:1 |
| IMAG | Institut Montpelliérain Alexander Grothendieck (institutional cover logo; printed line itself lacks the accent) | 16:1 |
| IMAG | Institut Montpelliérain Alexander Grothendieck (spelled out on the cover) | 47:1 |
| Id. | idem (reading uncertain) | 47:11 |
| Im | Image | 16:33 |
| Im | image | 16:21 |
| Int. | International | 16:28 |
| Ker | Kernel | 16:33 |
| Math. | Mathematical | 16:47 |
| Math. J. | Mathematical Journal | 16:28 |
| N.B. | nota bene | 16:42, 16:46, 44:4, 44:5 |
| NB | nota bene | 16:48, 16:49, 44:9 |
| NB. | nota bene | 16:18 |
| NS | Néron–Severi | 16:21, 16:23, 47:8, 47:9 |
| No. | Number | 16:28 |
| Ob | objets | 47:3 |
| PQ / P′Q | rational scalar extension written by juxtaposition; tensor sign not supplied | 44:5 |
| Pac. J. Math. | Pacific Journal of Mathematics | 16:39 |
| Pic | Picard | 16:21, 16:23, 47:8, 47:9, 44:8, 44:9 |
| Proc. | Proceedings | 16:47 |
| Prop | proposition | 16:34 |
| Prop. | Proposition | 16:30, 54:4 |
| R.R. / RR | Riemann–Roch | 47:10 |
| S. G. A. | Séminaire de Géométrie Algébrique | 16:54, 16:56 |
| S.G.A.D. | Séminaire de Géométrie Algébrique, Demazure (editorial expansion tentative) | 16:26 |
| SGAA | Literal citation abbreviation; source identification deferred | 16:23 |
| Soc. | Society | 16:47 |
| Spec | spectre | 16:43 |
| Sym | symétrique / algèbre symétrique (expression incomplete) | 16:20 |
| T.A.M.S. | Transactions of the American Mathematical Society | 16:28 |
| TF | undefined local condition; possibly finite-type tail condition | 44:3 |
| Th. | Theorem | 16:30 |
| Th. | théorème | 47:11, 44:2, 44:6 |
| Th. / th | théorème | 44:4 |
| Top. Alg. | Topologie Algébrique | 16:28 |
| Tors | torsion | 16:23 |
| V. A. | variétés abéliennes | 54:2 |
| V.A. | variété abélienne | 54:3, 44:2 |
| VA | variété abélienne | 44:8 |
| VA | variétés abéliennes | 47:8 |
| VA | variétés abéliennes (provisional expansion from the mathematical title; not expanded in the transcription) | 47:2 |
| Vol | Volume | 16:47 |
| alb | Albanese / équivalence abélienne (notation to be resolved) | 44:2 |
| alg | algébrique | 16:51, 44:2 |
| alg | algébriquement | 44:8 |
| alg clos | algébriquement clos | 47:9 |
| alg équiv | algébriquement équivalents | 44:9 |
| alg. | algèbre | 16:22 |
| alg. | algébriquement | 47:7, 47:8 |
| alg. | algébriquement / algébrique | 47:3 |
| alg. clos | algébriquement clos | 16:27 |
| alg. clos. | algébriquement clos | 47:7 |
| alg. équiv. | algébriquement équivalents | 44:4 |
| alt. | alternée | 16:25, 16:27 |
| appl. | application | 16:27 |
| ass. | associativité | 47:4 |
| autom. | automorphisme | 47:11 |
| bil. | bilinéaire | 16:25 |
| bil. sym. | bilinéaire symétrique | 16:27 |
| bis | second occurrence / inserted second proposition | 54:6 |
| c. à d. | c’est-à-dire | 16:15 |
| can. | canonique | 16:36 |
| can. | canoniquement | 47:5 |
| can. | canoniques (cancelled and uncertain) | 16:9 |
| car | caractéristique | 16:19 |
| car | characteristic | 16:44 |
| car. | caractéristique | 47:9, 54:3, 54:5 |
| car. | caractéristique / characteristic | 16:46, 16:47 |
| car. pol. | characteristic polynomial | 16:48 |
| cart | cartésien | 47:4, 47:6 |
| cf | confer / voir | 16:7 |
| cf. | confer | 16:54, 16:56 |
| cf. | confer / compare | 16:14 |
| ch | caractère de Chern | 47:9, 47:10, 47:11 |
| char. | characteristic | 16:44, 16:49 |
| chgt | changement | 47:6 |
| chgt. | changement | 47:4 |
| ci-† | possibly ci-dessus; visible abbreviated/cross-like ending remains uncertain | 16:14 |
| cl | classe | 47:5, 47:9 |
| co. | co- (prefix as revised) | 16:18 |
| codim | codimension | 44:4 |
| coeff. | coefficients | 47:9 |
| comm. | commutatif | 16:3 |
| conj. | conjecture | 16:44 |
| cor | corollaire | 47:11 |
| cor. | corollaire | 16:54, 54:8 |
| corr. | correspondance | 16:51 |
| corr. | correspondance (reading uncertain) | 44:2 |
| cqfd | ce qu’il fallait démontrer | 54:4 |
| cqfd. | ce qu’il fallait démontrer | 47:4 |
| ct | classe de Chern totale | 47:9 |
| dactylo | dactylographe | 44:7 |
| de = | de même (equal-sign shorthand) | 16:8 |
| dim | dimension | 16:22, 16:27, 16:29, 16:42, 16:43, 16:47, 16:50, 47:4, 47:6, 47:7, 44:4 |
| dim | dimension (in reduction line the intended grading may be different) | 54:5 |
| déf | définition | 47:4 |
| déf. | définition | 16:54 |
| défin. | définissant / définit (uncertain inserted abbreviation) | 16:10 |
| dég. | dégénérée | 16:25, 16:27, 16:29 |
| dém. | démonstration | 47:6 |
| endom | endomorphisme | 16:29 |
| endom | endomorphisme (abbreviated ending uncertain) | 16:15 |
| endom. | endomorphismes | 16:8, 16:22 |
| eq. | équivalent (tentative reading of the isolated label) | 47:7 |
| equiv. | equivalence | 16:46 |
| etc | et cetera | 16:32, 16:50 |
| exp. | exposé | 16:19 |
| gén. | généralement | 16:53 |
| gén. | généralement / général | 16:40 |
| géom. | géométriquement | 44:4 |
| hom | homomorphisme | 16:15, 16:17, 16:42, 16:53, 47:6, 47:8 |
| hom. | homomorphisme | 16:10, 16:16, 47:5, 47:7 |
| i. e. | id est | 16:56 |
| i.e. | id est | 16:5, 16:7, 16:8, 16:15, 16:18, 16:27, 16:29, 16:34, 16:36, 16:38, 16:40, 16:48, 16:53, 47:5, 47:8, 47:9, 47:11, 54:4, 54:5, 54:6, 44:5, 44:9 |
| ibid | ibidem | 16:39 |
| id | identité | 16:29, 16:33 |
| inv. | inversible | 47:7, 47:8, 47:9 |
| isom | isomorphisme | 16:12, 16:18, 16:34, 16:38, 16:53, 47:5, 47:7, 44:3 |
| isom. | isomorphisme | 16:6, 16:9, 16:25, 47:6, 47:11 |
| isom. | isomorphismes | 47:3 |
| isom. can. | isomorphisme canonique | 47:4 |
| loc. | localement | 44:3 |
| loc. cit. | loco citato | 16:19 |
| mbres | membres | 44:4 |
| mbs | membres | 16:36 |
| mod | modulo | 16:21, 47:9 |
| mor | morphisme | 16:34 |
| n.s. | non singulière | 44:4 |
| nb | nombre | 16:3, 44:2 |
| noeth | noethérien | 54:4 |
| noeth. | noethérien/neothérienne | 44:3 |
| num. | numérique / numerical | 16:46 |
| n° | numéro | 16:52, 16:54, 16:56, 54:8, 44:7 |
| n° | numéro(s) | 16:9 |
| néc. | nécessairement | 16:27 |
| nᵒ | numéro | 16:15 |
| p-alg. | p-algèbre (restricted Lie algebra) | 54:7 |
| p. | page | 16:47, 16:52, 16:54, 16:56 |
| p. ex. | par exemple | 16:12, 47:5, 44:7 |
| p. f. | présentation finie | 16:52, 16:56 |
| p.ex. | par exemple | 16:8, 16:22, 47:10, 44:3 |
| par | paragraphe (in “par9”, uncertain) | 54:6 |
| parf | parfaits (provisional reading of the category subscript) | 47:3 |
| polyn | polynôme (reading uncertain) | 16:22 |
| pr | projection | 47:3 |
| prem. | première | 16:38 |
| proj. | projection | 47:4 |
| prop. | proposition | 16:52, 16:54, 16:56, 47:5, 47:10, 47:11, 54:8 |
| préc. | précisément (reading uncertain) | 54:3 |
| prés. | présentation | 47:6 |
| pt (uncertain reading) | point | 47:3 |
| puiss. | puissance | 54:7 |
| qcoh | quasi-cohérents | 47:3, 47:5 |
| quad. | quadratique | 44:5 |
| r-g | rang (tentative exact reading) | 47:8 |
| rel | relativement | 47:8 |
| resp. | respectively | 16:41, 16:46 |
| resp. | respectivement | 16:6, 54:4 |
| resp. | respectivement / respectively | 16:50 |
| respé | respectif / respectivement (typed form preserved) | 54:4 |
| rest. | restant / restent (uncertain) | 16:40 |
| rg | rang | 16:20 |
| réd | réduit | 16:19 |
| sing. | singulières | 16:45 |
| ss-espace | sous-espace | 16:27 |
| ssi | si et seulement si | 16:25, 16:52 |
| sss | si et seulement si | 54:4, 54:6 |
| susp. | suspens | 16:40 |
| sym. | symétrique | 16:25 |
| ter | third occurrence / inserted third corollary | 54:6 |
| th. | théorème | 16:15, 16:16, 16:52, 16:54, 47:3, 47:4 |
| th. | théorèmes | 44:2 |
| tjrs | toujours | 16:25 |
| transit. | transitivité | 47:4 |
| transp. | transposition | 16:53 |
| tt | tout | 16:3, 16:6, 16:8, 16:10, 16:16, 16:17, 16:38, 16:51 |
| tt | tout / toute, according to the occurrence | 47:3 |
| ttes | toutes | 16:13 |
| v. p | voir page | 16:7 |
| var. | variables | 16:25 |
| vect. | vectoriel | 16:27 |
| égalt | également (uncertain reading) | 16:12 |
| élt | élément | 16:10, 16:18 |
| élémts | éléments | 16:22 |

# Legibility and limits

The typescript pages are usually clearer than the rapid manuscript drafts, but overwritten type, faint pencil, and small indices still require local doubts. The least secure passages are the heavily canceled lower portion of 16:12, the tiny interlinear construction on 16:22, the crowded theorem revisions on 44:4, and the slanted additions on 47:3; local symbol ambiguities elsewhere are recorded individually above. All pages received an independent visual audit, but the high / medium / low labels are qualitative reading judgments, not measured error probabilities. A surviving mathematical inconsistency was preserved, and unreadable words were marked only after attempted readings at enlarged scale.

- Cote 16, scan 1: Printed institutional cover is clear. The unlabelled polyhedral logo is redrawn in TikZ; geometry, face shading and dotted hidden edges are approximations of the raster mark.
- Cote 16, scan 3: Main formulae are substantially clearer than the pale cursive prose. The top insertion about the underlying module, overwritten equation numbers, and densely cancelled equivalence at lower right are the weakest readings; each is marked explicitly. Two visible numbers are retained at top and foot, without asserting the provenance of the lower number. Independent reader reopened full and both halves, checked local enlargements, made the final-word uncertainties explicit, preserved circled a/b labels, and restored the long enclosure drawing.
- Cote 16, scan 4: Pale prose is uneven but most uncancelled displays are legible. The degree-combination sign, a repeated equation reference, crossed intermediate calculation and small marginal module instruction retain uncertainties. The symbols in the crossed calculation are less secure than those in the replacement block decomposition. Independent audit checked full page, both halves, and magnified overwritten and marginal text; restored the old algèbre, the small d’où, and the marginal brace.
- Cote 16, scan 5: Heavy cancellation at the head and overwriting in the φ/ψ definitions and final block index are difficult. The uncancelled central-idempotent argument and two case splits are comparatively clear. Several apparent index inconsistencies are retained rather than repaired. Independent audit reopened full page and halves, enlarged head, boxed insertion, component sum and final correction. Reproduced open bracket and insertion bubble; moved already-recorded π_i/π_α doubts into the formula itself. Follow-up comparison of exact center glyphs on5 and6 leaves their alphabet distinction unresolved; the plain/Gothic uncertainty is now marked locally, with calligraphic Z retained as a further alternative in the doubts table.
- Cote 16, scan 6: The two main hypotheses have substantial deleted restrictions, overwritten conclusions and a circled block symbol. The logical directions are clear. The centre glyph has uncertain alphabet, and two lower mapping marks have no securely visible arrowhead; those are not silently normalised. Independent audit reopened full/halves and enlarged both deleted restrictions, the first line and reduced-to-zero wording; found no secure mathematical correction. Left bracket is shortened to the first row, matching the asymmetric original, and the circled block uses the prescribed drawing wrapper.
- Cote 16, scan 7: This sheet is less heavily corrected than its predecessors. The opening map has only a thin horizontal mark; the final section number is overwritten, and the compressed marginal cross-reference is retained with a notation doubt. Independent second reader checked full page then both halves against every paragraph and formula; confirmed all principal readings and restored the left marginal leader and vertical rule.
- Cote 16, scan 8: The upper half is readable pale cursive. The induction paragraph and operator replacements contain layered cancellations and small insertions; these receive explicit local doubts. Primes on v′ and w′ are visible and are transcribed as primes, not exclamation marks. Independent audit compared full page and both halves, enlarged the upper participle and soit, the overwritten induction and comme/donc. Formula indices, true primes and insertion attachments agree with the initial reading; folio enclosure restored.
- Cote 16, scan 9: Equation numbers and the cancelled expression in (6.2) are overwritten. The two equivalences in the primitive decomposition and the terminal horizontal strokes are visible: the latter are rendered as dashes, not editorial ellipses. The abbreviation cancelled before “de morceaux” is weak. Independent audit read full image and both halves, magnified the cancelled (6.2) expression, primitive exponents and final intrinsic reference. The exponent n−i+1 is visually confirmed. The upper and middle insertion leaders are now drawn; the final reference favours 1.7 while retaining 1.3 as an alternative.
- Cote 16, scan 10: This is one of the least secure early sheets. Several versions of item(ii) are overlaid and partly blacked out; the unreadable word counts are estimates after magnified inspection. The large crossed-out item(vi) is nevertheless mostly readable and fully included. The six-dot row at (6.5) is manuscript content, not editorial omission. Independent audit examined full page and both halves and magnified every major cancelled region. The original uncertainties remain; Une graduation and tel choix are offered as stronger visual alternatives. Parentheses around the proof exponent are retained, and the superscript of L in the cancelled uniqueness paragraph is explicitly uncertain between 1 and 2. Callout outlines have been drawn.
- Cote 16, scan 11: The main projectors and inequalities are clear. The short crossed display near the top, one overwritten word, the induction-direction insertion and the final summation index are less secure. The multi-line paragraph containing (6.9) has several long diagonal cancellation strokes; the entire affected passage is marked deleted. Independent audit checked all projectors, interval bounds, primes, the strict α′>α and the terminal sum against full page and both halves. The insertion favours ascendante; its leader is drawn. The opening word of the large cancelled paragraph is now marked Car|Cela rather than silently resolved.
- Cote 16, scan 12: The upper proof is fairly readable, but (6.9) runs into the right edge of the scan and its closing portion is clipped. The large middle cancellation is recoverable apart from one overwritten operator. Several heavily blacked-out formula fragments around (6.11) are low-confidence best readings; no mathematical repair has been substituted. Independent audit read the full page and both halves, then enlarged the entire middle cancellation and the blacked-out bottom fragments. The upper minus sign, strict α′>α and clipped (6.9) ending agree with the initial reading. A triangular Λ preceding the last deleted π expression is now included; the remaining dense cancellations cannot be resolved more securely.
- Cote 16, scan 13: The main eight-row system is readable, with local overwriting around rows2 and3. The supplementary proof note is small but mostly clear. The degree of Λ, the boundary conditions, and several cancelled operator fragments are the weakest readings; these remain explicitly doubtful. Independent audit read full image and both halves and magnified (6.12), (6.13), the supplementary proof note, overwritten rows2/3 and the bottom insertion. The lower stroke in the (6.13) comparison favours ≤; a detached crossed α-like glyph above row6 is restored without assigning it mathematically to an exponent. All eight equations and their indices were compared.
- Cote 16, scan 14: The main §7 exposition and operator formulae are readable. The small Question and its margin pointer are considerably less secure; they are retained in full with local doubts. Bold/doubled strokes distinguish the model module and operators from the earlier plain letters, but the tiny subscript in the final insertion is uncertain. Independent audit checked full page and both halves, enlarged the small Question and its margin note, dual-form insertion and final paragraph. Doubled strokes of model M,L,Λ are confirmed. Two occurrences of L and the inserted ξ* lack a securely distinct zero, now marked locally rather than silently supplied. Folio arc, marginal bracket and insertion leaders are drawn.
- Cote 16, scan 15: This is a heavily revised page. The replacement definitions and multiplication rule are mostly recoverable; several abandoned indices, the first crossed words and the parenthetical sentence about the model are low-confidence. Both large cancelled systems and the two marginal notes are included, with the enclosing marginal stroke reproduced in TikZ. Independent audit compared full image and both halves, rotated the diagonal upper margin and magnified both abandoned systems, the replacement definitions, marginal product law and proposition. Model operators here use single strokes, distinguished from doubled14/16. The replacement system has a straight left rule. The verb dépend is restored after bien sûr in its source order, confirmed with the first reader. Other unreadable overwritten fragments remain marked.
- Cote 16, scan 16: The two transported inverse identities and the main proof are clear. The diagonal margin is among the least legible portions of the early file, and the last uniqueness paragraph contains multiple interleaved insertions and crossings. These passages are transcribed as best readings with substantial explicit uncertainty; the final reference is overwritten. Independent audit reread the full page, both halves, the large and rotated diagonal margin, the cancelled proof and final uniqueness paragraph. The cross-reference reads ci-dessous; an omitted low-confidence avec-shaped word before the cancelled relation and detached margin traces are restored. The underlined marginal noun, connective and last word remain low confidence with additional visible alternatives, and no precise extra equivalent is inferred. The last model Λ has no distinct zero. Model operator doubling and all surviving inverse identities were checked.
- Cote 16, scan 17: The main corollary, question and negative answer are mostly readable. The inverse criterion has an overwritten index and a displaced zero/quotation mark. The two small faithful-module additions are low-confidence and partly unfinished; their visible literal dots are retained as manuscript punctuation, not editorial omissions. Independent audit reopened full image and both halves and compared enlarged inverse criterion, both module formulations, circled insertion and Question. The main corollary, changed projector index, trailing criterion marks and negative n=1 answer agree with the first reading. The smaller faithful-module note remains weak and is not independently reconstructed into a complete statement; its uncertain projector is marked locally. Restored underlining, exact visible terminal punctuation strokes, folio arc and insertion leaders; the Question parenthesis retains a separate visual callout rather than a guessed attachment inside the doubtful verb.
- Cote 16, scan 18: Dark handwriting is distinguishable from the mirrored typescript showing through the sheet; the latter is not a second text on this face. Several cancelled phrases in the definition are physically obscured by crossings and overprint and are the least secure portion. The duality note and the nonvanishing formulae are substantially clearer, although the circled marginal two-word comment remains uncertain. Independent audit inspected the whole image and both supplied halves, all inventory items, and magnified the cancelled definition, co. revision, NB, both margins, nonvanishing chains and bottom text. It restored a probable opening quotation mark and visible dash, made the flat Λ exponent uncertain, preserved the marginal separator and detached stroke, and moved the underline from réciproque to the visibly underlined algèbre. Reversed typescript remains identified as show-through from the verso, not an extra text on this face.
- Cote 16, scan 19: The typed body is clear. The word localement is cancelled by typed x characters and lisse et is inserted above it; the singular form is retained. The overwritten word before the pairing is uncertain. Three long strokes cross the sheet and may cancel it as a reused draft; their geometry is reproduced rather than silently assigning a more precise scope. The final Pic(U)₀ is printed with a low 0, unlike the superscript 0 earlier. Independent second-reader audit reopened the whole and both half images, enlarged the three insertion leaders, overwritten pairing word and ordre, and checked every formula and inventory entry. Small leaders were added and the first marginal cross moved to its visible line beside schéma régulier.
- Cote 16, scan 20: Black mathematical scratch over pale mirrored typescript from the reverse. All black expressions, isolated cancellations, brackets, monomial lists and arrow rows included; mirrored type is not duplicated and should be read on its actual face. Whole page, both halves and enlarged details inspected. Several unfinished expressions are left unfinished. Independent audit replaced typographic underbraces with the observed flat lower brackets drawn in TikZ; added the visible terminal dot after the rational operator expression.
- Cote 16, scan 21: Typed French cohomology/Brauer excerpt with substantial hand-filled symbols and amendments. Whole page and both halves inspected, with enlarged cancellation/formula crops. The unreadable remnants are attempted and marked, all equation numbers and arrows retained. Square-bracket Tate twists, underlined coefficient letters and the unmatched parenthesis in8.6 are not normalized.
- Cote 16, scan 22: Handwritten black mathematical draft with several heavy boxed/wavy cancellations and a very small inserted line; main argument and bottom example mostly readable. Pale reversed typescript belongs to the reverse sheet and is not duplicated. All three supplied images and enlarged top/middle/lower/insert/foot crops were viewed; reread against the transcription.
- Cote 16, scan 23: Clear reused typescript with handwritten coefficients, section numbers, references, insertion leaders and several local cancellations. Underlined Z and Q, bracketed twists and visible typographical anomalies are retained. Whole image and both supplied halves were viewed, with additional crops of the canceled phrases, Br superscript and posées correction; transcription reread against all regions. Independent audit reopened the whole page and both supplied halves, then enlarged all canceled words, the Br blots, the opening parenthesis and final insertion leader. The upper marginal x marks were relocated beside their actual lines; visible unmatched punctuation was retained.
- Cote 16, scan 25: Main formulae and table are readable. The crossed preliminary line, cancelled i=4 case, auxiliary rho notation, and diagonal bottom-left annotation are the least secure; these retain explicit doubt marks. Independent second reading viewed whole image and both halves, enlarged the diagonal annotation, upper-right form labels and lower targets; retained checked V and existing local uncertainties. Restored the geometric callout border around the tilde-varphi note.
- Cote 16, scan 26: Typescript is clear apart from inked-out citations. The single page-spanning pencil stroke has uncertain editorial meaning; all text under it remains transcribed.
- Cote 16, scan 27: Many substantial cancellations and very light pencil strokes make the upper example paragraph difficult. The list a–d and its formulae are substantially clearer. The top-right parenthetical formula, the V/W in the induced-form parenthesis, and the curved-arrow label require special audit. Independent whole-image and both-half audit, with enlarged upper cancellation and parenthetic formula; Q phrase revised to étant donné. The unusual non isotrope and V/W ambiguity remain literal and marked.
- Cote 16, scan 28: Clear typescript; only the punctuation between Notes and at in entry23 is uncertain. Printed folio45 is distinguished from handwritten27.
- Cote 16, scan 29: The main argument is pale pencil with darker formula insertions. Cancelled top lines and the final insertion are least trustworthy; the two meanings of the bivector square are preserved with explicit uncertainty in the doubts list. Independent audit viewed whole, both halves, enlarged top deletion, both scalar phrases and full lower insertion. The last insertion remains uncertain after a second reading; no mathematical reconstruction has been substituted.
- Cote 16, scan 30: Clear typescript, with the wavy under-mark on G in G_m reproduced literally as an underset tilde. Printed folio42 and handwritten29 remain distinct.
- Cote 16, scan 31: A nearly empty divider sheet; the heading and handwritten folio are clearly visible. Both halves were inspected for faint additional writing; none was discernible.
- Cote 16, scan 32: A nearly empty divider sheet with a clear heading and handwritten folio. Both halves were inspected; no further text was discernible.
- Cote 16, scan 33: Upper typescript and surviving equations are mostly clear. The lower third contains several overlapping cancellation layers; the recovered formulas4′,4″,5′ and old RHS7 are explicitly tentative and need the strongest independent audit. The critical-degree exponent at the bottom is also overwritten. Independent whole/halves audit plus enlarged bounds and every cancelled block. Both readers confirmed the omitted square and X-subscript in5-prime; opening parenthesis before condition restored. Heavy underlying deleted operators remain explicitly uncertain.
- Cote 16, scan 34: Most live writing is legible. The upper diagram has overwritten signs and exponents, and the lower corrections are substantially less secure; these are retained with local doubt marks. Independent whole/halves and enlarged square/kernel/triangle-label audit confirmed coprod graphic signs, the plus in the upward-arrow index and star on the triangle’s downward phi. Kernel insertion revised to égal à celui de L_X, i.e., retaining uncertainty.
- Cote 16, scan 35: The typescript is very clear. Handwritten category letters and the approximate-equality sign are visible; page-edge damage and faint show-through are not treated as text. A small upper-left arrowlike trace is reproduced with an explicit doubt about ink versus physical damage.
- Cote 16, scan 36: Live operator identities are reasonably clear. Several obsolete decompositions and the margin label are heavily cancelled; their attempted readings are retained at low confidence rather than normalized from the mathematics.
- Cote 16, scan 37: Very clear typescript. The page was inspected in its supplied orientation and in rotated copies of both halves; handwritten prime-ideal and support glyphs have local uncertainty.
- Cote 16, scan 38: The upper live prose and final large formulas are mostly legible. The rejected middle block is heavily overstruck, the formula bounds have corrections, and the star placements in the last relation are surprising; these are explicitly retained with doubts.
- Cote 16, scan 39: Very clear printed text and formulas, inspected in the original orientation and upright rotated halves. The handwritten prime-ideal glyph and unaccented printed proper names are preserved without external correction.
- Cote 16, scan 40: Most live formulas are legible. The generalization heading, overwritten summation bound, added L-shaped factor, and the final abbreviation remain uncertain. The derivation’s bracket annotations are retained, with the zero bracket necessarily spanning the written parenthesis.
- Cote 16, scan 41: Clear typescript, including underlined functors and bullet exponents. Both supplied halves and their upright rotated versions were inspected. Only the 0/o threshold subscript carries a local ambiguity.
- Cote 16, scan 42: Main formulas largely clear; rapid pale prose, the long cancelled formula under the two terms, tiny operator indices, and repeated pale-blue paper lettering are least secure. The paper grid has forty-two repeated diagonal marks; some lie beneath handwriting. Full image, both halves, and enlarged local crops were inspected and checked. Independent reinspection resolves the tiny ξ and dotted i; the cancelled sum lower bound now leads with n, and rotated pale blue marks favor Condor, each unresolved feature retaining explicit alternatives.
- Cote 16, scan 43: Typescript is mostly crisp. Dense black cancellations obliterate substantial earlier wording and one formula; all have attempted doubtful readings. The diagonal handwritten marginal instruction is clearer after rotation but its first word remains uncertain. Full page, both halves and multiple enlarged crops were inspected, with a second comparison against transcription.
- Cote 16, scan 44: Clear typescript with several overtyped and handwritten corrections. Repeated parameter glyphs resemble crossed ℓ; the blank after “independant of” is genuinely blank. Source spellings independant, choosen, one’s, independance, dependance and bu are retained. Full page, both halves and magnified correction crops were inspected and reread. Independent second reading rechecked the whole page and both halves, each correction and inventory entry, and enlarged all repeated parameter forms, the two dimension exponents, overwritten opening parenthesis, conditions and low x. The repeated parameter remains ℓ|χ; the blank and literal source slips are retained.
- Cote 16, scan 45: Printed text is clear, including the actual slips Condititions and verieté. Overtyped cancellations, the repeated crossed subscript, the overwritten top A/Q, and the clipped target of (iv bis) are less secure. Full page, both halves and local enlargement crops were visually read and checked before committing. Independent second reading examined the whole page and both halves, then enlarged the top operator, proposition heading, both cancellations, both handwritten operators, clipped target, corollary parameters and final insertion. Every inventory entry was compared with the source. Printed ℓ|χ is distinguished from the two handwritten ℓ|l forms; the cancelled oval trace in (iv) is made explicit. No mathematical degree or source spelling was corrected.
- Cote 16, scan 46: Typescript generally clear, but right edge clips the cohomology chain and N.B. formula. Typed x-deletions, overtyping, and bottom handwritten equivalence note are the least secure passages; all have explicit uncertainty marks. Subscript comparison: the actual scan45 bottom crop and local glyphs were reread; ℓ is the leading conjecture-subscript candidate with χ retained explicitly, not a normalization from the mathematics.
- Cote 16, scan 47: Mostly clear typescript with one clear handwritten insertion. A few overtyped letters are uncertain; the spellings Seeies, spcialisation, Kleimann, week and your’s are preserved as visible rather than modernised.
- Cote 16, scan 48: Clear annotated typescript, but several formula characters and words have overtyping; right-hand ends are narrowly clipped. The visible u/h in the Cayley–Hamilton line are not silently changed to the mathematically expected w/b. Subscript comparison: the actual scan45 bottom crop and local glyphs were reread; ℓ is the leading conjecture-subscript candidate with χ retained explicitly, not a normalization from the mathematics.
- Cote 16, scan 49: Clear typescript with a small number of handwritten insertions. Degree-shift letter δ/d and overwritten final words are less secure. Plain strokes between some cohomology groups are retained where no arrowhead is visible. Subscript comparison: the actual scan45 bottom crop and local glyphs were reread; ℓ is the leading conjecture-subscript candidate with χ retained explicitly, not a normalization from the mathematics.
- Cote 16, scan 50: The underlying typescript is legible, but this page contains dense overlapping deletions, insertions and formula corrections. The rewritten A″ condition, overwritten C/A in the proposition, deleted product factor, and partially formed arrowheads are the least reliable areas. Subscript comparison: the actual scan45 bottom crop and local glyphs were reread; ℓ is the leading conjecture-subscript candidate with χ retained explicitly, not a normalization from the mathematics.
- Cote 16, scan 51: Fast handwritten French with several heavily crossed terms and compressed words. The main sentence structure and maps are readable, but the operator after L, index placement on ξ, factor terminology and corollary inverse-map glyph remain low-confidence readings.
- Cote 16, scan 52: Clear blue typescript. The Fitting surname is repeatedly typed with an l-like letter; a small exclamation-like mark above p. f. remains doubtful. Surprising wording and A-module presentation are kept as written.
- Cote 16, scan 53: Fast, compressed handwritten continuation with many readable formulae but ambiguous p/ρ, h/k-like shapes, several crossed words and a crowded kernel annotation. Insertion attachment and a plus/minus in the middle arrow label particularly require independent audit.
- Cote 16, scan 54: Very legible blue typescript; handwritten ideal letters q and m are readable but alphabet style is not distinctive. The opening phrase localisée et une is retained with a marked alternative.
- Cote 16, scan 55: Short handwritten conclusion, mostly legible. The sign in the opening exponent and the case of primitive-factor p/P are marked uncertain; the blank lower half was inspected.
- Cote 16, scan 56: Clear typescript with one substantial handwritten cancellation. Ideal letters are handwritten and the final B/B′ distinction is uncertain; the last sentence continues on printed page 3, which occurs earlier in scan order.
- Cote 47, scan 1: Modern printed cover, clear throughout. Whole and both halves visually checked; lettering and solid/dotted polyhedral linework rechecked against TikZ transcription.
- Cote 47, scan 2: Five-line handwritten title in upper right of otherwise blank blue folder; final letters of convolution crowded at right edge. Whole, both halves and enlarged title inspected; bottom pagination 1 retained.
- Cote 47, scan 3: Dense handwritten proposition and proof with a long diagonal marginal continuation, several heavy deletions and small derived-functor decorations. Whole page and both halves inspected, then enlarged main text and rotated margin crops; transcription and inventory reread. Low-confidence local readings remain explicitly marked rather than reconstructed.
- Cote 47, scan 4: Formula-rich handwriting with two Cartesian diagrams, two connecting leader strokes, several overwritten expressions and an extensively revised theorem. Whole image, both halves and four enlarged regions inspected; all formulas and diagram labels reread against the draft. Source omissions and locally ambiguous symbols preserved.
- Cote 47, scan 5: Dense revised handwritten statement and corollary, with top and left marginal insertions and multiple overwritten formulas. Whole page, both halves and enlarged upper, marginal, corollary and proof regions inspected. All surviving statements—including apparent mismatches between revised theorem and old proof—retained; uncertain fragments individually marked.
- Cote 47, scan 6: Handwritten lemma and corollary with corrected product factors, local index inconsistencies, deeply crossed formula segments, and marginal determinant note. Whole and both halves inspected; diagram, lemma, margin, corollary and ending enlarged and compared with the draft. All visible ambiguities and apparent omissions retained.
- Cote 47, scan 7: Many cancellations in the first lemma and in targets of the canonical maps, but main proof readable. Whole and both halves inspected, with enlarged top, middle, bottom and Cartesian diagram. Cancelled formulas retained with local uncertainty, and the admitted lemma kept separate from the subsequent proof.
- Cote 47, scan 8: Proof conclusion mostly clear; lower remarks contain revisions, compressed marginal text and a formula cut off by cancellation. Whole and both halves inspected, plus enlarged proof, remarks, margin and end. Dots marking the omitted compatibility check and all visible sign discrepancies retained.
- Cote 47, scan 9: Handwriting mostly readable; formulas have retraced arguments, small ambiguous raised marks, and faded final exponents. Whole page and both halves inspected, with enlarged upper text, expansions, lower integrality claim and Mumford margin. Coefficients checked against the image individually; apparent algebraic inconsistencies retained and documented.
- Cote 47, scan 10: Long central draft is surrounded and crossed by three diagonal cancellation strokes; all of its readable content is retained inside deleted markup. Whole page and both halves inspected, then enlarged upper formulas, cancelled block and lower restart. Source argument/ambient-space inconsistencies and the final retraced argument are explicitly flagged.
- Cote 47, scan 11: Whole page and both halves read; enlarged upper formulas, slanted left margin, Kleiman paragraph, duality formulas and bottom automorphism paragraph. Several compressed corrections and the final abbreviations remain uncertain. No convolution symbol added where source shows only juxtaposition; missing closing parenthesis and distinct check/vee marks retained.
- Cote 54, scan 1: Printed institutional cover; all lettering is clear. The polyhedral emblem is reproduced geometrically in TikZ, with shading and visible/dotted edges. Independent visual audit confirmed text and all emblem lines; fill colors adjusted to the observed pale grey-blue and olive shades.
- Cote 54, scan 2: Nearly blank folder cover. The two-line heading is rapid cursive; doubtful small words and the compressed opening word are marked. Bottom numeral 1 is clear.
- Cote 54, scan 3: Mathematical blocks mostly legible; rapid French words, reinforced S/H/V letters and the reworked extension-classification sentence are less secure. Full page, both halves, and enlarged crops were checked; uncertainty remains explicitly in the text. Independent audit and author comparison distinguish the probable lower cancelled définie from upper inserted classifie, retaining both as uncertain.
- Cote 54, scan 4: The typescript is readable except X-overtyped references and missing typed mathematical operators, which are not supplied. A page-long diagonal cancels the typed block. The crowded handwritten corollary at the bottom is among the least reliable passages: numerous strokes cross earlier text, and the lowest line approaches the paper edge; all attempted readings and local uncertainties are retained.
- Cote 54, scan 5: Fair mathematical legibility with very compressed cursive prose. The paired-group notation p^A versus a left subscript p, the word duals/duaux, and the unexpected sheaf subscript are explicitly uncertain. Underlines, cancellations, bracketed flag display and continuation at the foot are retained.
- Cote 54, scan 6: Typescript largely clear, with a small number of X-overtyped deletions and handwritten insertions. Missing arrows in typewritten factorizations remain spaces; the single visible handwritten arrow is retained. The o/0 subscripts are typographically ambiguous.
- Cote 54, scan 7: Black manuscript is mostly readable, though the final object of the upper diagram is open-V-shaped and a tiny correction under F^B remains uncertain. Pale blue, upside-down reversed typescript is show-through from the opposite face; the actual typed face is read separately. The encircled note and its leader are reproduced.
- Cote 54, scan 8: Clear blue typescript, originally upside down in the scan; full page and halves were inspected both in supplied orientation and after 180-degree rotation. Underlining is retained phrase by phrase. The circular subscripts are explicitly o/0-uncertain. The handwritten folio7 is distinct from printed page13; the printed face explains the reversed show-through on scan7.
- Cote 44, scan 1: Printed institutional cover; all lettering is clear. The polyhedral emblem is reproduced geometrically in TikZ, with shading and visible/dotted edges. Independent visual audit confirmed text and all emblem lines; fill colors adjusted to the observed pale grey-blue and olive shades.
- Cote 44, scan 2: Light pencil/cursive prose interspersed with reinforced ink formulae. The main assertions are readable, but the opposite duality index, the cycle-equivalence subscript, and the bracketed clause in Th.4 are weak readings. All brackets, marginal callouts and the theorem4 annotation are retained.
- Cote 44, scan 3: Reused handwritten algebra scratch with a page-long top stroke, left boundary and two diagonals canceling the light draft. All legible text and the darker foot addition are transcribed; the relative layer of the final addition is uncertain. Both exact sequences are drawn as lines without clear arrowheads. Important weak readings are marked rather than corrected mathematically.
- Cote 44, scan 4: Dense layered manuscript with several cancellations overwritten again, tiny inserted hypotheses and two large callouts. Whole page, both halves and enlarged/rotated details were read. All theorem text, attempted canceled readings, margins and enclosure geometry are included; several superscripts and discarded clauses remain explicitly uncertain.
- Cote 44, scan 5: Entire handwritten root-system draft crossed by a long diagonal. Main axioms and formulas are legible, but canceled bilinear expression, coroot letter and revised input variables are uncertain. All margins, dual reflection, and normalization insertion are retained. PlainQ/Z and juxtaposedPQ follow the visible notation without supplied tensor signs.
- Cote 44, scan 6: Only three main handwritten lines and one marginal attribution occur on this face. Pale mirrored blue typescript visible through the paper is reverse-side show-through, not a second layer of text on this face; its actual face is scan7. Whole page and both supplied halves inspected. Handwritten folios3 and5 both retained. Subsequent inspection of scan7 identifies the three upper-right dark marks as physical perforations showing through both faces; they are not transcribed as punctuation.
- Cote 44, scan 7: Clear blue French typescript reused as reverse of scan6. Whole page and both supplied halves inspected and reread. Three dark marks at upper left align with reverse-face marks and appear to be physical perforations, not punctuation. Original quoted spellings noeuds/conoeuds and literal three-dot ellipsis retained; line-end word division rejoined.
- Cote 44, scan 8: Readable typed French letter with handwritten mathematical indices, corrections and three tilted marginal notes. Whole and both halves plus rotated detail crops inspected. The lower range endpoint and canceled Hodge margin remain weak readings. The sentence intentionally continues onto scan9; no supplied closing parenthesis or completion.
- Cote 44, scan 9: Clear continuation and end of the typed letter, with two typed interlinear insertions and two canceled fragments. Whole page and both halves read and reread. The source’s Notes spelling, direct x product notation, unaccented A prouver, and absence of a signature after Bien à toi are preserved.
