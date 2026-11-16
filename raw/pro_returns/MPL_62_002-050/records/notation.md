# Final notation register

Readings are based only on the supplied scans. The primary reader compared recurring forms before the freeze, after the second visual reading of all 46 pages. Differences retained below reflect visible variants or explicit doubts, not normalization from mathematical expectations.

## Cross-page alphabet and punctuation decisions

- Straight divisor-bundle L is `\underline L`; curved Lie and graded-quotient letters are `\mathcal L`, with the independent underline retained as `\underline{\mathcal L}` where visible. The lower-half graded quotients on 006 were compared directly with 007 and corrected to the curved form. Ordinary L in the field-level argument on 007 remains straight.
- Script E in the elliptic-curve section is `\mathcal E`; typed module E remains ordinary E. The doubled-looking affine-space E on 011 is explicitly `\unsure{\mathbb E|E}`. It is never replaced by A.
- The independently doubled diagonal of handwritten Z is `\mathbb Z`, including the quotient-group diagrams. Filled/retraced Z on 019 and the live Z_2 on 032 retain explicit plain/doubled-letter alternatives. Typed double underlines under Q and Z on 035 and 037 remain `\underline{\underline Q}` and `\underline{\underline Z}`.
- Most projective-space P letters have one stem and are ordinary P. The possibly doubled stem on 005 is `\unsure{\mathbb P|P}`; the reinforced central P on 050 is `\unsure{\mathbf P|P}`. The thin marginal P on that same leaf remains plain. G_m uses ordinary G, distinct from the ornate symmetric-group sign `\mathfrak S`.
- Underlined structure-sheaf O is `\underline O`, not calligraphic O. The typewritten m and n on the n°276 sheets are upright `\mathrm m`, `\mathrm n`; the underlined ideals on n°272 are separately `\underline{\mathrm p}` and `\underline{\mathrm m}`.
- Short slanting accents are primes; pullback stars are `^*`; circumflexes are hats; the visibly wavy initial-form accents on 049 are tildes, while the straight accents on 047 are bars. No exponent was converted to an exclamation mark from mathematical context.
- Double quotation marks are two opening backticks and two closing apostrophes. The detached double-stroke repetition mark on 019 is retained as a repetition mark, not paired with invented closing quotation marks.
- Arrowheads, equal signs, inclusions and headless strokes are distinguished in the code. A headless handwritten correspondence is not silently promoted to a map. Repeated equation number (11) on 040 is retained.
- Abbreviations remain unexpanded in the LaTeX. Their proposed expansions are listed separately below in the final doubts document.

## Scan 004

- Straight L with one independent underline: `\underline L`; the letter's foot is not a second underline.
- Curved L: `\mathcal L`; E-like script: `\mathcal E`.
- The tangent-sheaf glyph is very stylized; compared with 007 and retained as underlined T, with the script-T alternative explicitly marked at its first occurrence.
- Double quotation marks: two opening backticks and two closing apostrophes.
- Tensor powers have a circled multiplication sign: `^{\otimes n}`, not a prime or exclamation mark.
- Several connecting strokes have no visible arrowhead; these are represented by `dash` in tikz-cd.

## Scan 005

- `coh.` is not expanded; `ssi` retained. `RR` kept without added punctuation.
- Genus letter g has an open lower loop; distinguish from index n.
- Ordinary ≥ has a second stroke; the manuscript also uses > and possibly ≫, explicitly distinguished.

## Scan 006

- Direct-sum-like handwritten symbol consists of a flat base and two upward strokes; transcribed `\coprod`, not silently replaced by `\bigoplus`.
- The upper graded quotients have curved L without a separate underline; the lower graded quotients have curved L with an independent underline. Comparison with 007 resolved the latter as underlined calligraphic L, not underlined ordinary L.
- `isom.` and `comm.` remain abbreviations.

## Scan 007

- Underlined curved L in the corollary and derivation formula is represented `\underline{\mathcal L}`. Its shape was compared directly across 004–007; the straight L in the direct proof is a visible variant, not silently unified.
- `exp. car.` retained as written; `pt` not expanded.
- A straight, unadorned L occurs in the direct proof with f and g; retained as ordinary L.

## Scan 010

Discriminant written as triangular Δ; circled formula treated as marginal content. Plain P used for the handwritten projective-space symbol. Homogeneous equation uses capital Φ, affine φ.

## Scan 011

Discriminant appears as lowercase δ on this page, unlike triangular Δ in the preceding margin: retain the actual variants. Affine-space letter is E, not A; its doubled-looking left stroke is explicitly uncertain between mathbb E and plain E. Manuscript page number10 bottom left.

## Scan 012

Greek λ, μ and γ occur in a triangular 3×3 matrix; lower γ has a left hook and horizontal top, retained as γ. Capital X/Y in affine change are retraced and explicitly uncertain. Prime mark is a short slant, not an exclamation exponent.

## Scan 013

Category glyph resembles calligraphic D: use \mathcal D. Parenthetical quotation marks around provienne reproduced as ``provienne''. F is ordinary capital F, not script.

## Scan 014

This page clearly distinguishes script ℒ in auxiliary line bundle from straight L in opening paragraph. Explicit triangular matrix weights λ², λ³. Greek β and γ exchange column positions relative to scan012; keep actual matrix. Use \Gamma for sections and ordinary G_m.

## Scan 016

Automorphism here is handwritten s, not a closed Greek sigma. Quotient uses Z sub2. Underlined V denotes the geometric vector-bundle construction. Retain uncertainty of heavily retraced exponents rather than normalize silently.

## Scan 017

Main involution denoted s. Subbundle L3 is plain upright-looking L (not script); in one later line the letter looks E3 and is kept uncertain. Margin differential label ∂/ϑ unresolved. Brackets/cancellation outlines are editorial state, not separate mathematical drawings.

## Scan 019

- Scan 019: handwritten Kummer groups Z/3 and Z/2; quotients A^{*(n)} retain parenthesized exponent. H-like abbreviated Hom notation is not silently expanded; alternatives marked. O/0/U remains uncertain in the bottom diagram.

## Scan 020

- Scan 020 (reused typewritten sheet): upright typewritten m is rendered \\mathrm m; typed p≥k, subset and tensor signs retained. The final polynomial visibly uses lowercase x, whereas the preceding A[X], E[X] and a_pX^p use uppercase X. Printed -20- and n°276 are distinguished from handwritten sheet 19.

## Scan 022

- Scan 022: typewritten slanted inequalities are rendered \\leqslant. Printed PROPOSITION is uppercase, Max has initial capital. Distinguish printed page9/n°276 from handwritten21.

## Scan 028

- Scan028: recurring Greek phi (loop with long stem) is \\varphi; psi is \\psi; involutions lambda, mu, nu are \\lambda, \\mu, \\nu. Products in3 are baseline; conjugation expressions4–5 use subscripts. Ornate group sign rendered \\mathfrak S, with final subscript6|3 uncertainty.

## Scan 029

- Scan029 reused typewritten page39/n°272: ideal letters p,m have underlining, rendered \\underline{\\mathrm p}, \\underline{\\mathrm m}; this is visually distinct from ordinary subscripts and the m in n°276 sheets. Gamma_i and gamma_i handwritten/type-added Greek remain uppercase/lowercase.

## Scan 032

The ornate symmetric-group glyph was compared with 028–030 and the later torsor pages: continue \mathfrak S_3. This is distinct from plain G in the extension diagram. The extra involution is written Z_2 here, whereas diagram has Z/2.

## Scan 033

Typed n°272 retains roman ring/field letters and handwritten ψ, Ω and section-number insertions; φ-shaped empty-set sign marked uncertain.

## Scan 034

Capital wedge-shaped Λ is transcribed \Lambda_S. Prime on S in \overline{S'} is visible inside bar; x', x'' are genuine primes, not exclamation marks.

## Scan 035

The double strokes under typed Q,Z are retained as double underlining, not silently converted to blackboard bold. Handwritten Γ has retraced cap; v' index is prime.

## Scan 036

Here three parallel headless strokes indicate ramification index3, two index2, and single line nonramification. Retained as parallel no-head TikZ arrows; crossed diagonals marked deleted.

## Scan 038

Local auxiliary maps u and v (v glyph close to ν), pullback stars ^*, inverse pullback v^{-1*}; stars must not become primes. x',x'' are roots with primes and cubic powers.

## Scan 039

Scan039 makes the family index omega ω clear. Prime on v and on A in L_{A'} must be distinguished from the star in L_ω^*.

## Scan 040

Equation number (11) appears twice; retained. Box split by vertical rule between the pullback expression and j. Double primes on σ'' are visible, not inverse exponents.

## Scan 041

Clear circumflexes in typed completion sheets are \hat{}, never primes. Preserve unadorned A in the one topology clause where no circumflex is visible.

## Scan 042

New terminology trisection / bisection retained without modernizing. First line Br. Severi abbreviated. Possible σ_S subscript remains doubtful.

## Scan 043

Two-level completion has a large circumflex over already hatted E/F: \widehat{\hat E/\hat F}. Plain quotient completion \widehat{E/F} distinguished from \hat E/\hat F.

## Scan 044

The replacement invariant was visually compared with the later occurrences: initial i and later j remain different, with explicit alternatives where retraced. No normalization between them is made. The section morphism is visibly p:S→P¹_S, distinct from quotient j:X→P¹_S.

## Scan 045

U(g) printed with plain g; no guessed Gothic alphabet. Lower map to H lacks a visible hat, retained.

## Scan 046

- Scan 046: invariant written $i$; keep it distinct from $j$ on prior pages. `tt` retained as abbreviation. Normalization clause says ramifié (no confidently visible final e).

## Scan 047

- Scan 047: typewritten ideal m is upright roman, compared with 020, 024, 026 and 049; Lie algebra g remains plain, as scan 045. Pencil ellipses retained as TikZ around the selected phrases.

## Scan 049

- Scan 049: initial forms have wavy typewritten accents, rendered with tilde. Congruence lacks a visible summation sign. Preserve typographic semicolon in n°;276 and des;éléments.

## Scan 050

- Scan 050: comparison action written bar-sigma(t), with overwritten symbol, marked unsure; λt=1/t and μt=1−t remain explicit. `s. s. s.` and superscript t in alg.^t retained. Local ring O is plain capital O; the sheaf letter is the same plain O with an independent underline.
