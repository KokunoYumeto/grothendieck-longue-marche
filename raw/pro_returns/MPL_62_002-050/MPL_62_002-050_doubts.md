# MPL_62_002-050: Notation, doubts and abbreviations

## Notation table

This is the package-wide notation table finalized before the context archive was opened. Font choices and retained variants were compared by the primary reader against the supplied images.

| Scan or scope | Reading and LaTeX encoding |
|---|---|
| General | Readings are based only on the supplied scans. The primary reader compared recurring forms before the freeze, after the second visual reading of all 46 pages. Differences retained below reflect visible variants or explicit doubts, not normalization from mathematical expectations. |
| Cross-page alphabet and punctuation decisions | Straight divisor-bundle L is `\underline L`; curved Lie and graded-quotient letters are `\mathcal L`, with the independent underline retained as `\underline{\mathcal L}` where visible. The lower-half graded quotients on 006 were compared directly with 007 and corrected to the curved form. Ordinary L in the field-level argument on 007 remains straight. |
| Cross-page alphabet and punctuation decisions | Script E in the elliptic-curve section is `\mathcal E`; typed module E remains ordinary E. The doubled-looking affine-space E on 011 is explicitly `\unsure{\mathbb E\|E}`. It is never replaced by A. |
| Cross-page alphabet and punctuation decisions | The independently doubled diagonal of handwritten Z is `\mathbb Z`, including the quotient-group diagrams. Filled/retraced Z on 019 and the live Z_2 on 032 retain explicit plain/doubled-letter alternatives. Typed double underlines under Q and Z on 035 and 037 remain `\underline{\underline Q}` and `\underline{\underline Z}`. |
| Cross-page alphabet and punctuation decisions | Most projective-space P letters have one stem and are ordinary P. The possibly doubled stem on 005 is `\unsure{\mathbb P\|P}`; the reinforced central P on 050 is `\unsure{\mathbf P\|P}`. The thin marginal P on that same leaf remains plain. G_m uses ordinary G, distinct from the ornate symmetric-group sign `\mathfrak S`. |
| Cross-page alphabet and punctuation decisions | Underlined structure-sheaf O is `\underline O`, not calligraphic O. The typewritten m and n on the n°276 sheets are upright `\mathrm m`, `\mathrm n`; the underlined ideals on n°272 are separately `\underline{\mathrm p}` and `\underline{\mathrm m}`. |
| Cross-page alphabet and punctuation decisions | Short slanting accents are primes; pullback stars are `^*`; circumflexes are hats; the visibly wavy initial-form accents on 049 are tildes, while the straight accents on 047 are bars. No exponent was converted to an exclamation mark from mathematical context. |
| Cross-page alphabet and punctuation decisions | Double quotation marks are two opening backticks and two closing apostrophes. The detached double-stroke repetition mark on 019 is retained as a repetition mark, not paired with invented closing quotation marks. |
| Cross-page alphabet and punctuation decisions | Arrowheads, equal signs, inclusions and headless strokes are distinguished in the code. A headless handwritten correspondence is not silently promoted to a map. Repeated equation number (11) on 040 is retained. |
| Cross-page alphabet and punctuation decisions | Abbreviations remain unexpanded in the LaTeX. Their proposed expansions are listed separately below in the final doubts document. |
| Scan 004 | Straight L with one independent underline: `\underline L`; the letter's foot is not a second underline. |
| Scan 004 | Curved L: `\mathcal L`; E-like script: `\mathcal E`. |
| Scan 004 | The tangent-sheaf glyph is very stylized; compared with 007 and retained as underlined T, with the script-T alternative explicitly marked at its first occurrence. |
| Scan 004 | Double quotation marks: two opening backticks and two closing apostrophes. |
| Scan 004 | Tensor powers have a circled multiplication sign: `^{\otimes n}`, not a prime or exclamation mark. |
| Scan 004 | Several connecting strokes have no visible arrowhead; these are represented by `dash` in tikz-cd. |
| Scan 005 | `coh.` is not expanded; `ssi` retained. `RR` kept without added punctuation. |
| Scan 005 | Genus letter g has an open lower loop; distinguish from index n. |
| Scan 005 | Ordinary ≥ has a second stroke; the manuscript also uses > and possibly ≫, explicitly distinguished. |
| Scan 006 | Direct-sum-like handwritten symbol consists of a flat base and two upward strokes; transcribed `\coprod`, not silently replaced by `\bigoplus`. |
| Scan 006 | The upper graded quotients have curved L without a separate underline; the lower graded quotients have curved L with an independent underline. Comparison with 007 resolved the latter as underlined calligraphic L, not underlined ordinary L. |
| Scan 006 | `isom.` and `comm.` remain abbreviations. |
| Scan 007 | Underlined curved L in the corollary and derivation formula is represented `\underline{\mathcal L}`. Its shape was compared directly across 004–007; the straight L in the direct proof is a visible variant, not silently unified. |
| Scan 007 | `exp. car.` retained as written; `pt` not expanded. |
| Scan 007 | A straight, unadorned L occurs in the direct proof with f and g; retained as ordinary L. |
| Scan 010 | Discriminant written as triangular Δ; circled formula treated as marginal content. Plain P used for the handwritten projective-space symbol. Homogeneous equation uses capital Φ, affine φ. |
| Scan 011 | Discriminant appears as lowercase δ on this page, unlike triangular Δ in the preceding margin: retain the actual variants. Affine-space letter is E, not A; its doubled-looking left stroke is explicitly uncertain between mathbb E and plain E. Manuscript page number10 bottom left. |
| Scan 012 | Greek λ, μ and γ occur in a triangular 3×3 matrix; lower γ has a left hook and horizontal top, retained as γ. Capital X/Y in affine change are retraced and explicitly uncertain. Prime mark is a short slant, not an exclamation exponent. |
| Scan 013 | Category glyph resembles calligraphic D: use \mathcal D. Parenthetical quotation marks around provienne reproduced as ``provienne''. F is ordinary capital F, not script. |
| Scan 014 | This page clearly distinguishes script ℒ in auxiliary line bundle from straight L in opening paragraph. Explicit triangular matrix weights λ², λ³. Greek β and γ exchange column positions relative to scan012; keep actual matrix. Use \Gamma for sections and ordinary G_m. |
| Scan 016 | Automorphism here is handwritten s, not a closed Greek sigma. Quotient uses Z sub2. Underlined V denotes the geometric vector-bundle construction. Retain uncertainty of heavily retraced exponents rather than normalize silently. |
| Scan 017 | Main involution denoted s. Subbundle L3 is plain upright-looking L (not script); in one later line the letter looks E3 and is kept uncertain. Margin differential label ∂/ϑ unresolved. Brackets/cancellation outlines are editorial state, not separate mathematical drawings. |
| Scan 019 | Scan 019: handwritten Kummer groups Z/3 and Z/2; quotients A^{*(n)} retain parenthesized exponent. H-like abbreviated Hom notation is not silently expanded; alternatives marked. O/0/U remains uncertain in the bottom diagram. |
| Scan 020 | Scan 020 (reused typewritten sheet): upright typewritten m is rendered \\mathrm m; typed p≥k, subset and tensor signs retained. The final polynomial visibly uses lowercase x, whereas the preceding A[X], E[X] and a_pX^p use uppercase X. Printed -20- and n°276 are distinguished from handwritten sheet 19. |
| Scan 022 | Scan 022: typewritten slanted inequalities are rendered \\leqslant. Printed PROPOSITION is uppercase, Max has initial capital. Distinguish printed page9/n°276 from handwritten21. |
| Scan 028 | Scan028: recurring Greek phi (loop with long stem) is \\varphi; psi is \\psi; involutions lambda, mu, nu are \\lambda, \\mu, \\nu. Products in3 are baseline; conjugation expressions4–5 use subscripts. Ornate group sign rendered \\mathfrak S, with final subscript6\|3 uncertainty. |
| Scan 029 | Scan029 reused typewritten page39/n°272: ideal letters p,m have underlining, rendered \\underline{\\mathrm p}, \\underline{\\mathrm m}; this is visually distinct from ordinary subscripts and the m in n°276 sheets. Gamma_i and gamma_i handwritten/type-added Greek remain uppercase/lowercase. |
| Scan 032 | The ornate symmetric-group glyph was compared with 028–030 and the later torsor pages: continue \mathfrak S_3. This is distinct from plain G in the extension diagram. The extra involution is written Z_2 here, whereas diagram has Z/2. |
| Scan 033 | Typed n°272 retains roman ring/field letters and handwritten ψ, Ω and section-number insertions; φ-shaped empty-set sign marked uncertain. |
| Scan 034 | Capital wedge-shaped Λ is transcribed \Lambda_S. Prime on S in \overline{S'} is visible inside bar; x', x'' are genuine primes, not exclamation marks. |
| Scan 035 | The double strokes under typed Q,Z are retained as double underlining, not silently converted to blackboard bold. Handwritten Γ has retraced cap; v' index is prime. |
| Scan 036 | Here three parallel headless strokes indicate ramification index3, two index2, and single line nonramification. Retained as parallel no-head TikZ arrows; crossed diagonals marked deleted. |
| Scan 038 | Local auxiliary maps u and v (v glyph close to ν), pullback stars ^*, inverse pullback v^{-1*}; stars must not become primes. x',x'' are roots with primes and cubic powers. |
| Scan 039 | Scan039 makes the family index omega ω clear. Prime on v and on A in L_{A'} must be distinguished from the star in L_ω^*. |
| Scan 040 | Equation number (11) appears twice; retained. Box split by vertical rule between the pullback expression and j. Double primes on σ'' are visible, not inverse exponents. |
| Scan 041 | Clear circumflexes in typed completion sheets are \hat{}, never primes. Preserve unadorned A in the one topology clause where no circumflex is visible. |
| Scan 042 | New terminology trisection / bisection retained without modernizing. First line Br. Severi abbreviated. Possible σ_S subscript remains doubtful. |
| Scan 043 | Two-level completion has a large circumflex over already hatted E/F: \widehat{\hat E/\hat F}. Plain quotient completion \widehat{E/F} distinguished from \hat E/\hat F. |
| Scan 044 | The replacement invariant was visually compared with the later occurrences: initial i and later j remain different, with explicit alternatives where retraced. No normalization between them is made. The section morphism is visibly p:S→P¹_S, distinct from quotient j:X→P¹_S. |
| Scan 045 | U(g) printed with plain g; no guessed Gothic alphabet. Lower map to H lacks a visible hat, retained. |
| Scan 046 | Scan 046: invariant written $i$; keep it distinct from $j$ on prior pages. `tt` retained as abbreviation. Normalization clause says ramifié (no confidently visible final e). |
| Scan 047 | Scan 047: typewritten ideal m is upright roman, compared with 020, 024, 026 and 049; Lie algebra g remains plain, as scan 045. Pencil ellipses retained as TikZ around the selected phrases. |
| Scan 049 | Scan 049: initial forms have wavy typewritten accents, rendered with tilde. Congruence lacks a visible summation sign. Preserve typographic semicolon in n°;276 and des;éléments. |
| Scan 050 | Scan 050: comparison action written bar-sigma(t), with overwritten symbol, marked unsure; λt=1/t and μt=1−t remain explicit. `s. s. s.` and superscript t in alg.^t retained. Local ring O is plain capital O; the sheaf letter is the same plain O with an independent underline. |

## Reader’s doubt register

Approximate locations refer to the manuscript layout. This table records uncertain words, symbols, attachment, cancellation extent and graphic features, including decisions resolved during the visual audit. Earlier working observations have been reconciled here with the final page files; their original versions remain in the work records. Confidence concerns the reading, not the validity of the mathematics.

| File | Scan page | Approximate line or location | Final reading or retained decision | Alternatives or qualification | Confidence |
|---|---:|---|---|---|---|
| 62.pdf | 004 | cancelled Proposition 1 | cohomolgt plats en ttes dimension | cohomologt; toute; cancellation obscures the endings | low |
| 62.pdf | 004 | tangent formulas | underlined T | script T; heavily stylized glyph | medium |
| 62.pdf | 004 | first chain and right margin | n+h; relatives | final exponent letter and adjective unclear | low |
| 62.pdf | 004 | before first chain | d'injections linéaires | d'injection; final word and plural endings faint | medium |
| 62.pdf | 004 | cancelled Proposition 1 | ttes | toute | low |
| 62.pdf | 004 | parenthesis before first chain | d'injections linéaires | singular/plural and very faint last word uncertain | medium |
| 62.pdf | 005 | proposition, rank and ampleness | n with deleted +1; deleted très | black correction after n; crossing versus underline at très | low |
| 62.pdf | 005 | proof, degree formula | deleted −(g−1) | heavily cancelled expression | low |
| 62.pdf | 005 | cancelled two lines at fold | par suite les L^⊗n est très ample pour n≫0 | connective faint; final comparison possibly >0 | low |
| 62.pdf | 005 | lower paragraph opening | Ceci suffit | initial word faint | medium |
| 62.pdf | 005 | diagonal left margin | quelconque | rapid compressed ending | medium |
| 62.pdf | 005 | Proposition 1 final clause | n≥3 | n>3 | medium |
| 62.pdf | 005 | projective-space symbol in the very-ampleness argument | \mathbb P | P; two closely adjacent stem strokes may be retracing rather than an intended doubled letter | medium |
| 62.pdf | 006 | Proposition 2 interlinear correction | n≥0; L_0=O_S; les L_i, soit i≠1 | 0 overwritten on 2; cancelled formula and connective severely entangled | low |
| 62.pdf | 006 | Proposition 2 cancelled comparison | L^⊗k | exponent partly crossed; possibly n | low |
| 62.pdf | 006 | graded algebra paragraph | Γ_* with possible superscript E; gr. ann. | extra mark may be a correction rather than superscript | low |
| 62.pdf | 006 | last lines | ramenons nous … au voisinage | three cancelled words physically obscured; connective uncertain | low |
| 62.pdf | 007 | direct multiplication proof end | provient par déf. de | middle word not fully resolved; apparently refers to image of product | low |
| 62.pdf | 007 | Proposition 3 parenthesis | ou deleted est un épim. | last abbreviation may be different | low |
| 62.pdf | 007 | upper corollary | hom induits | last letters light | medium |
| 62.pdf | 007 | direct proof final line | L_(n+m) | L_(n+m)^0; final loop and under-stroke may be part of overwritten index | low |
| 62.pdf | 008 | end of cancelled corollaries | L_2^2 ≃ L^⊗2 | upper black mark may be a cancelled exponent or blot | low |
| 62.pdf | 008 | boxed conclusion | L_(n+1) ≃ L^⊗(n+1), n≥2 | left subscript possibly n after overwriting | low |
| 62.pdf | 008 | cohomology sequence | R^1(f,L^⊗n) | initial cohomology glyph overwritten; first arrow in preceding sequence lacks head | medium |
| 62.pdf | 008 | left marginal instruction | intervertir | insertion? first word rapid | medium |
| 62.pdf | 009 | cancelled description of line | droite des points de l'infini | middle words under long strike | low |
| 62.pdf | 009 | bottom cancelled normalization | définie à unité; homothétie; multiplication près par u | interlinear wording and placement heavily entangled | low |
| 62.pdf | 009 | cancelled cubic | ax^2+by^3 | x exponent possibly changed toward 3; marginal x^3 y^2 recorded separately | low |
| 62.pdf | 009 | bottom-edge insertion | suppl. de E_1 dans E_2 et x de E_2 dans E_3 | abbreviation and last subscripts crowded at page edge | low |
| 62.pdf | 009 | flag in lower paragraph | curved arrow then two curved headless strokes below inclusions | very weak endings on last two curves might be arrowheads | medium |
| 62.pdf | 010 | top deleted continuation | que vérifie aussi bien à priori; vérifiée par | word order obscured by cancellation; à priori may be a priori | low |
| 62.pdf | 010 | after E6 | composante de; Γ_*(f,L^⊗3)≃∐ E_i | abbreviated connection and exponent overworked; right index may be 3i | medium |
| 62.pdf | 010 | end of middle paragraph | de même E3, y3 (deleted); à valeurs en E9, E3 (deleted) | several cancelled strokes superposed | low |
| 62.pdf | 010 | homogeneous equation | ay³ followed by cancelled z; no eyz² term | the stroke after y³ may be a rewritten plus sign; no missing term supplied | medium |
| 62.pdf | 010 | lower paragraph | P_S³ | P_S²; glyph looks 3 | medium |
| 62.pdf | 010 | upper left slanted margin | d'ailleurs, est essentiellement primitive | éventuellement; last word provisoire | low |
| 62.pdf | 010 | deleted single words | la; notre; d'une | overwritten and crossed through | low |
| 62.pdf | 010 | graded modules throughout | script E | previous plain E encoding corrected after visual comparison | high |
| 62.pdf | 011 | top insertions | coeff. a,b...; deleted a before une telle équation | coeff without full stop; overwritten short letter uncertain | medium |
| 62.pdf | 011 | proposition deleted words | avec; unité | first may be avec abbreviated; quotation mark and last letters of unité partly obscured | medium |
| 62.pdf | 011 | proposition discriminant condition | δ(a,b,c,d,e,f)≠0 | =0; cancellation/inequality slash not distinct | low |
| 62.pdf | 011 | last deleted words | Faisons opérer dessus | Faisons opérer dans | low |
| 62.pdf | 011 | last display, affine-space symbol | \mathbb E | E; the long left stroke appears doubled, but ordinary retracing is possible | medium |
| 62.pdf | 012 | top cancelled block | puis schéma en groupes; qui repr. est représenté matriciellement par | opening word and overwritten repr. uncertain | low |
| 62.pdf | 012 | beginning of live paragraph | G.; GL(n)_Z | first glyph could belong to cancelled continuation; GL(3)_Z | low |
| 62.pdf | 012 | polynomial | BXY² and CY³ (alternative CY²); cancelled X²+AXY² | The small exponents are retained from the ink; the first cancelled symbol is overwritten | medium |
| 62.pdf | 012 | affine substitution | Y'=λY+α | X'=λX+α; both Y/X glyphs heavily retraced | low |
| 62.pdf | 012 | bracketed explanation | ce sera plus clair; vecteur | ce qui est plus clair; vectoriel abbreviation | low |
| 62.pdf | 012 | revised subspace wording | sous-module (deleted), schéma (inserted), de dimension (deleted) rang 6 | insertion and deletion extents uncertain; schéma may be linéaire | low |
| 62.pdf | 012 | functor paragraph | l'ens. before inserted l'ens des classes à isom près | faint overwritten short wording | low |
| 62.pdf | 012 | last line | éléments | liens; visible beginning is éli/élé | low |
| 62.pdf | 012 | live polynomial | CY³ | CY² | medium |
| 62.pdf | 012 | live polynomial first sign | + | − | low |
| 62.pdf | 013 | top deleted word | donc | deux; overtraced | low |
| 62.pdf | 013 | interlinear G description | linéaire | lisse | medium |
| 62.pdf | 013 | principal bundle parenthesis | clivage | découpage; letters not all distinct | medium |
| 62.pdf | 013 | before D-représentable | pro (deleted) | unreadable retraced short prefix | low |
| 62.pdf | 013 | lower paragraph | obtenir cet énoncé | savoir cet énoncé; initial word uncertain | low |
| 62.pdf | 013 | last three lines | quelc (de façon triangulaire quotient par un groupe projectif---) | quelconque abbreviation; triangulaire/prim...; quotient may be conjugué | low |
| 62.pdf | 014 | first paragraph | i₂(D), i₃(D) | ι₂(D), ι₃(D); i/ι graph cannot decide alphabet | medium |
| 62.pdf | 014 | auxiliary structure | splitting où les facteurs successifs; d'un isom | short connector only a horizontal stroke; d'un/en isom | medium |
| 62.pdf | 014 | group paragraph cancelled words | formé; triplets | fourni; éléments | low |
| 62.pdf | 014 | cancelled and inserted transition below first matrix | La fixation de la structure ainsi conduit à une équation; isomorphe; le sous-groupe du précédent/groupe plein | multiple revision layers and attachment uncertain; phrase ending and inserted groupe plein low confidence | low |
| 62.pdf | 014 | right of matrix | Γ(G_mS/S)=Γ(S,O_S*) | first argument may have extra script m or underline; star reads unit group | medium |
| 62.pdf | 014 | bottom | en l'équation plus haut | dans l'équation plus haut; visible short preposition is en | medium |
| 62.pdf | 015 | second line deleted word | type | short word with doubled crossing strokes | low |
| 62.pdf | 015 | descent parenthesis | ou à simples | ou m. simples; abbreviated/repeated morphismes not clear | low |
| 62.pdf | 015 | trivializations | sections λ; 12.ième (ou même 24.ième) | D for λ; parenthetical connector ambiguous | medium |
| 62.pdf | 015 | last sentence cancelled words | en ce; les | overwritten two short expressions | low |
| 62.pdf | 015 | trivialisations de L | script L | plain L | medium |
| 62.pdf | 016 | first formula | a with a dot | a with incidental ink dot | low |
| 62.pdf | 016 | second formula | −axy | +axy; sign retraced over a plus-shaped mark | medium |
| 62.pdf | 016 | boxed formula | x²=y³ | overwritten exponents resemble3 and2 respectively | medium |
| 62.pdf | 016 | geometry margin | quotient | quotients | medium |
| 62.pdf | 016 | geometry paragraph | Brauer-Sévéri; marquée | Brauer-Severi; unique | medium |
| 62.pdf | 016 | deleted geometry words | le schéma; s'identifie est isomorphe | cancellation boundaries uncertain | low |
| 62.pdf | 016 | line bundle revisions | faisceau inverse; fibré qui est loc. libre; fibré vectoriel; de rang un | several superposed lines obscure exact wording; all attempted readings flagged | low |
| 62.pdf | 016 | last two lines | dans les fibres (deleted); E (deleted) | dans la fibre; cancelled initial symbol uncertain | low |
| 62.pdf | 017 | first deleted line | que tous les corps résiduels de | initial and middle cancelled words uncertain; may say car. résiduelles | low |
| 62.pdf | 017 | upper middle interlinear deleted passage | Il en résulte aussitôt qu'il opère trivialement dans E2 [car il y opère trivialement] | overlapping three lines; second trivialement and attachment low confidence | low |
| 62.pdf | 017 | second cancelled block | stable qui sera le lieu s opère | last words under heavy strike unreadable in part; best attempted reading | low |
| 62.pdf | 017 | E2 action bracket | sans la condition | sous la condition | medium |
| 62.pdf | 017 | left margin | considération; différentielle; compatible avec tt changement de base S | construction; differential-related word and final compatibility wording uncertain | low |
| 62.pdf | 017 | left margin morphism label | ∂ | ϑ | low |
| 62.pdf | 017 | normalization paragraph | x soit une base de E3 | L3; visible glyph appears E | medium |
| 62.pdf | 017 | u³−v² relation | deleted λ before u³ | retraced short symbol | low |
| 62.pdf | 017 | left marginal differential | script L tensor cube | plain L tensor cube | medium |
| 62.pdf | 019 | heading and upper case label | unité; local normal | unité ending; local is highly compressed | medium |
| 62.pdf | 019 | upper two conditions | (par idéal) | parentheses phrase unresolved; second numerator 1\|j; right edge cut | low |
| 62.pdf | 019 | left slanting margin | à vérifier géométriquement | second word is overwritten and abbreviated-looking | low |
| 62.pdf | 019 | Kummer conditions | Si A ss élémts nilpotts | ss may be sans or n'a; word endings compressed | low |
| 62.pdf | 019 | Kummer c quotient | A^{*(3)} | A^{*(6)} | medium |
| 62.pdf | 019 | middle underlined phrase | module p | unité pr; very compressed | low |
| 62.pdf | 019 | middle sixth root | t with cancelled t in numerator | cancelled exponent or further symbol | low |
| 62.pdf | 019 | drawn marks | best TikZ reproduction | minor pen strokes and shading cannot be exact | medium |
| 62.pdf | 019 | lambda exponents | 3/6, -2/6, 1/6 | second numerator overwritten | medium |
| 62.pdf | 019 | bottom b exponent | cancelled 3 | dense cancellation; no secure digit | low |
| 62.pdf | 019 | bottom right functor diagram | underlined H, alternatively underlined Hom | compressed final letters; O versus 0 or U; E tilde versus bar | low |
| 62.pdf | 019 | bottom diagram top object | H_O(E,O) | H_0(E,U); Hom rather than H | low |
| 62.pdf | 019 | Kummer extension of order 2, group letter | Z | \mathbb Z; the diagonal is heavy and its doubling is not decisive, unlike the order-3 letter | medium |
| 62.pdf | 020 | typed notation throughout | upright m | a different typeface/overtyped character may have been intended; visibly not handwritten script | medium |
| 62.pdf | 020 | after Lemme d'Artin-Rees | dash | vertical ink attached to dash; possible overtyped punctuation | medium |
| 62.pdf | 020 | left curves and strokes | visible marks reproduced as drawing | may be offset or show-through from another face rather than intentional drawing | low |
| 62.pdf | 021 | first product | i≠j; denominator x_j-x_i | initial i overlaps relation; j may be cancelled or incidental pen stroke | medium |
| 62.pdf | 021 | upper right | (y+u)^3 | first y is retraced, possibly x; curved enclosing mark | medium |
| 62.pdf | 021 | middle sentence | on trouve | two compressed words | medium |
| 62.pdf | 021 | Delta expansion | 3b^2 sum x_i^2 } | closing brace may be a stray stroke | medium |
| 62.pdf | 021 | boxed Delta | cancelled9\|4 | dense cancellation obscures original coefficient | low |
| 62.pdf | 021 | last cancellations | (sum x^2)^2; x_1x_2; x_1x_2 | first bottom scribble is not securely resolved | low |
| 62.pdf | 021 | cancelled expansion below Delta | c^{3} | c^{2} | low |
| 62.pdf | 022 | handwritten margin by Corollaire1 | fait général pour les top. métrisables | first two words faint; abbreviation terminal point uncertain | medium |
| 62.pdf | 022 | proof underlining | résulte underlined | handwritten wavy emphasis rendered with allowed uline macro | high |
| 62.pdf | 023 | top fraction equality | =- | = only with a retraced adjacent stroke | low |
| 62.pdf | 023 | top numerator first factor | minus before x_2 | revised sign is inked over | medium |
| 62.pdf | 023 | upper left cancellation | x_1x_2x_3 | subscripts obscured | low |
| 62.pdf | 023 | small middle cancellation | (a/3) | heavily scribbled, could be further factor | low |
| 62.pdf | 023 | sqrt expansion | 3a^2; cancelled a after27 twice; 9b in penultimate line | 2 retraced; cancellations uncertain; no a visible before b in penultimate line | medium |
| 62.pdf | 024 | pencil margin | Dire que la top. est celle de la conv. simple des coefficients. | most words are compressed or faint, especially top. est and conv. simple | low |
| 62.pdf | 024 | insertion above par | engendré | middle letters faint | medium |
| 62.pdf | 024 | B definition | B='A[[X]] | apostrophe may be accidental ink | medium |
| 62.pdf | 024 | last summand | a_in | e_in | medium |
| 62.pdf | 025 | deleted cubic | a x^3+b x^2 | coefficient a and exponent2 heavily overwritten | medium |
| 62.pdf | 025 | four-point diagram | x_4 | x retraced but index4 clear | medium |
| 62.pdf | 025 | connecting brackets | headless links joining infinity to t/1 and 0 to t/1 | dark endpoints might contain arrowheads; retained as lines | medium |
| 62.pdf | 025 | tuple | ((x_1,x_2,x_3,x_4)) | first three indices very fast, order could be2,3,1; no correction from mapping | low |
| 62.pdf | 025 | small cancellation | x_3 | overwritten symbol unresolved | low |
| 62.pdf | 025 | Si x_4=infinity | on trouve | compressed strokes | medium |
| 62.pdf | 025 | right margin equality | = | dot or cancelled symbol | low |
| 62.pdf | 026 | drawing upper right | 59/60 on bar;59 and60 on smaller object | first59 overlaps a circular ornament; loops reproduced geometrically, no secure word in them | medium |
| 62.pdf | 028 | top paragraph | pts; S_3 | pts abbreviated, initial stroke unclear; script group letter resembles ornate S | medium |
| 62.pdf | 028 | margin right | renommer;lambda t=1-t;mu t=t/(t-1);nu t=1/t;?? | heading compressed; formula ends partly cut at right edge | low |
| 62.pdf | 028 | 3a deletion | psi^2=phi | phi^2=psi; dense cancellation | low |
| 62.pdf | 028 | lower left first line | gr. gr. cyclique | first repeated-looking abbreviation uncertain | low |
| 62.pdf | 028 | 4 and5 | subscripts indicate conjugation | lower symbols are positioned below main letters; kept distinct from products of3 | high |
| 62.pdf | 028 | last line | permutant à : S_6 (c'est d'ailleurs le seul, sauf | S_3; avec; the parenthesis continues on scan030; no editorial ellipsis substitutes for words | low |
| 62.pdf | 028 | final words | sauf | avec | low |
| 62.pdf | 029 | ideal letters throughout | underlined upright p and m | typewriter serif may account for some lower strokes; repeated line under p/m retained | medium |
| 62.pdf | 030 | normalizer margin | Prouver : le normalisateur ... S_3 times(Z/2) | Z retraced and inked over | high |
| 62.pdf | 030 | different paragraph | formé; pts de un des cinq opérateurs | ending and word after pts compressed; could abbreviate fixed points, but no supplied word | low |
| 62.pdf | 030 | fixed sections | (1,-1)(infinity,1/2)(infinity\|0,2) | third first symbol looks two-looped; not normalized from transformation | medium |
| 62.pdf | 030 | bracket after sections | st.ble par sigma | stable possibly unabridged | medium |
| 62.pdf | 030 | cancelled words | Le; distinct de sigma | the cancelled phrase is not securely legible | low |
| 62.pdf | 030 | bottom paragraph | globalement; rev. | globalement letters overlap; rev. likely abbreviated | medium |
| 62.pdf | 030 | bottom left margin | les exceptns qu'il y a pour car.2 ou3 deS | very faint and compressed; first three lines least secure | low |
| 62.pdf | 031 | le nombre des A_i est | apostrophe-like mark before ≤n | possibly accidental type/ink | low |
| 62.pdf | 032 | diagram and throughout | \mathfrak S_3 | ornate group letter resembles G; compare recurring glyph on scans 028–030 | medium |
| 62.pdf | 032 | quotient clause, cancellation and supralinear replacement | il est / est isomorphe / encore | qui est under the cancellation; the supralinear replacement is retained at its visible attachment | low |
| 62.pdf | 032 | transitivity clause, struck word | simplement | word beneath heavy rule | low |
| 62.pdf | 032 | bottom cancellation | le schéma du revt | les schémas des pts | low |
| 62.pdf | 032 | cancelled quotient clause | il est | qui est | low |
| 62.pdf | 032 | live paragraph, factor Z_2 | Z | \mathbb Z; diagram and final quotient have distinct doubled diagonals, while this occurrence is filled/retraced | medium |
| 62.pdf | 033 | first line | \varnothing | slashed circle is written like φ | medium |
| 62.pdf | 033 | end of first paragraph | pui sque | puisque with unusually large typed gap | medium |
| 62.pdf | 033 | section heading | 3° | 3 with correction stroke | low |
| 62.pdf | 034 | first line | ramification | letter sequence compressed; retained rather than mathematical correction | medium |
| 62.pdf | 034 | upper two cancellations | un domaine de / descente | heavily ruled through | low |
| 62.pdf | 034 | lower paragraph | fibration | word initial overwritten; possibly description or flèche | low |
| 62.pdf | 034 | lower paragraph notation | G_{mS} | G_m with S close to subscript; no parentheses visible | medium |
| 62.pdf | 035 | first paragraph | \underline{\underline Q}, \underline{\underline Z} | two short strokes visibly below typed Q and Z | high |
| 62.pdf | 035 | after proposition 3 | que la | typed quela with hand separation stroke | medium |
| 62.pdf | 035 | before Lemme 1 | doit | dit | medium |
| 62.pdf | 035 | proof of proposition 4 | inserted k | handwritten over typed character, underlying character cannot be distinguished | medium |
| 62.pdf | 036 | diagram under triples | P1∞, G_m; P1m | almost completely crossed-out mathematical labels; shape-based guesses | low |
| 62.pdf | 036 | diagram after f | section | sections; overwritten abbreviation | low |
| 62.pdf | 036 | diagram descending diagonals | cancelled paths with ~ | scribbled paths, no reliable original arrowheads | low |
| 62.pdf | 036 | middle deleted base | Z_m | Z followed by a retraced subscript | low |
| 62.pdf | 036 | bottom deleted line | ∈ A, donc de la forme 2^α3^β | possible star after A; deleted initial signs overlap rule | low |
| 62.pdf | 036 | unit coefficient of g | underlined O_S^* | plain O_S^* | high |
| 62.pdf | 037 | first index | ω | w | medium |
| 62.pdf | 037 | proof of corollary 1 | sedond | second; apparent type defect | medium |
| 62.pdf | 037 | editorial bracket | lo / en'fait | le / en fait; type blemishes possible | medium |
| 62.pdf | 038 | first paragraph ramification qualification | normalisée en | compressed phrase before deux sections disjointes | low |
| 62.pdf | 038 | second paragraph beginning | En fait | En ...; initial two words incompletely formed | low |
| 62.pdf | 038 | first formula cancelled prefactors | λ | heavily blackened symbols | low |
| 62.pdf | 038 | expanded numerator | deleted superscript 2 on x'', x', and t | overwritten dark ink could be correction rather than separately struck exponent | medium |
| 62.pdf | 038 | last cancellation | x''³-x'³=(x''-x')(x''²+x'x''+x'²)=0 | final term may be 0 or another overstruck expression | low |
| 62.pdf | 038 | diagram and pullback identities | u, v; f*(t) | v resembles Greek ν, star placement compressed | medium |
| 62.pdf | 039 | equation (2), coefficient indices | iα | typed i resembles 1; compared with x_i and repeated coefficient | medium |
| 62.pdf | 039 | equation (3) | v'(a_j)-v'(a_i) | only j and i visible, no β or α added | high |
| 62.pdf | 039 | lead-ins before (2), inequality, and (4) | ; | :; lower dot has comma tail | medium |
| 62.pdf | 040 | boxed left expression | g*(t)=(gf)*(t) | f*g*(t)=(gf)*(t); overlapping strokes and left box rule | low |
| 62.pdf | 040 | middle insertion | à partir de (G_a)_S | first three words indistinct | low |
| 62.pdf | 040 | last sentence | serait / prouver / pour σ dans ce dernier cas | serait may be est; prouver may be trouver; last clause very compressed | low |
| 62.pdf | 040 | non-ramification locus | G_m | G_a | low |
| 62.pdf | 041 | first paragraph after donnée | no period before Ehat | faint punctuation possible | medium |
| 62.pdf | 041 | second paragraph topology | la topologie de A | no hat visible here although nearby Ahat letters have clear hats | high |
| 62.pdf | 041 | second paragraph quotient index | \hat A_n | n resembles m in typeface | medium |
| 62.pdf | 042 | upper noun | trisection | underlined word compressed but initial tri and ending ction probable | medium |
| 62.pdf | 042 | upper conditions | sur X, d'ordre 3 sur X | both letters look X; no substitution of S | high |
| 62.pdf | 042 | structural object | schém. structural | first abbreviation not fully resolved | low |
| 62.pdf | 042 | automorphism clause | intr. σ_S | σ without subscript; abbreviation may be autre | low |
| 62.pdf | 042 | association converse | on restitue X' | short clause before X' indistinct | low |
| 62.pdf | 042 | bottom cancellation | [en ses points / f / puis | strongly overwritten | low |
| 62.pdf | 042 | last display lead-in | par : / comp. car | pour : / comp. au | low |
| 62.pdf | 043 | pencil beside lemma | topologt | topol.?; faint final characters; pointer aims toward start of u:E→F line | low |
| 62.pdf | 043 | lemma adjective | telle que | typed singular feminine retained | high |
| 62.pdf | 043 | lemma exacte underlining | double underline | printed rule and curved pencil emphasis, represented by double underlining | medium |
| 62.pdf | 044 | upper marginal gloss | aux dits pts | right edge cropped and final word looped | low |
| 62.pdf | 044 | invariant naming | i | j; first visible replacement has dot and no descender | medium |
| 62.pdf | 044 | next paragraph invariant twice | j | i over an earlier j; heavy retracing | low |
| 62.pdf | 044 | last bracket | À déduire des formalismes | À déduire les formules; the phrase continues on scan046 | low |
| 62.pdf | 044 | deleted fragments | ∞, et, est, _S, j, x, section, et | several are strongly overwritten and marked in place | low |
| 62.pdf | 044 | final bracketed phrase | À déduire des formalismes | À déduire les formules | low |
| 62.pdf | 045 | reference after Rappelons | Top. Gén..; | unfilled/garbled reference punctuation; no chapter supplied | medium |
| 62.pdf | 045 | lower extension map | Ehat → H | no hat visible on H, unlike clearly hatted E | high |
| 62.pdf | 045 | first paragraph | g | plain lower-case typed g, not confidently Gothic | medium |
| 62.pdf | 046 | upper line 3, cancellation | toute | indeterminate short word | low |
| 62.pdf | 046 | middle after underlining | comme on connaît; revêt | initial words and abbreviated ending run into strokes | medium |
| 62.pdf | 046 | lower middle | se pose la | several very compressed strokes | medium |
| 62.pdf | 047 | right handwritten marginal drawing | (0,1,∞); (2,1/2,−1); (x′,x″) | shape and endpoint of braces uncertain; center is a crossing of strokes, no definite arrowhead | medium |
| 62.pdf | 048 | top cancellation | Supposons i est égal à 0 | heavy horizontal cancellation obscures most of the wording | low |
| 62.pdf | 048 | upper interlinear bracket | donc X′ | small insert above a une section | medium |
| 62.pdf | 048 | upper main text | Tout | initial letter has a strongly oblique stroke | low |
| 62.pdf | 048 | middle bracket | grâce | very abbreviated handwritten form | medium |
| 62.pdf | 048 | lower opening cancellation | Donc | overwritten zigzag, perhaps another introductory word | low |
| 62.pdf | 048 | lower interlinear replacement | ce fibré conique | compressed middle word | medium |
| 62.pdf | 048 | lower insertion | X″ | X‴ | medium |
| 62.pdf | 048 | bottom | naturelle en question | several words are largely horizontal connecting strokes | medium |
| 62.pdf | 048 | bottom diagram, t to it^2 | headless dash | right arrow | medium |
| 62.pdf | 049 | typed top and bottom initial forms | tilde x_i, tilde a_i | short wavy accents, possibly imperfect bars in some occurrences | medium |
| 62.pdf | 049 | typed opening congruence | x ≡ a_i x_i (mod. E_(n+1)) | no summation sign is visible before a_i x_i | high |
| 62.pdf | 050 | upper insertion | simples | small word written above courbes de | medium |
| 62.pdf | 050 | bracket opening | revêtement S3 non ramifié | small S3 and adjacent overwriting may be a cancelled qualification | low |
| 62.pdf | 050 | cancelled middle formula | X ≃ P¹_S ×_(S,S3) | heavy zigzag crossing makes several factors uncertain | low |
| 62.pdf | 050 | action formula | bar sigma(t), cancelled phi | overwritten group-action symbol; bar rather than tilde uncertain | medium |
| 62.pdf | 050 | lower cancelled parenthesis | (car. ≠2,3) | scribbled through; replacement above is clearer | low |
| 62.pdf | 050 | bottom cancellation after Alors | X ≃ P¹_S | long crossing stroke obscures middle characters | low |
| 62.pdf | 050 | bottom insertion | Donn. non canoniq. par quoi | Donn. non canonique; possibly Donc; final two short words exceptionally uncertain | low |
| 62.pdf | 050 | bottom cancelled formula | t(t−1)∈Z | last character may be an overwritten expression in t | low |
| 62.pdf | 050 | last line | représ. | abbreviated noun before isomorphes only partly resolved | low |
| 62.pdf | 050 | last line cancellation | si et | short crossed connective | medium |
| 62.pdf | 050 | lower interlinear insertion after équivaut | Donn. non canoniq. par quoi | Donn. non canonique; final two words uncertain | low |
| 62.pdf | 050 | central associated-bundle expression, live projective-space letter | \mathbf P | P; this letter is visibly reinforced, while the marginal P has a single thin stem | medium |

## Abbreviations and proposed expansions

Expansions are supplied only in this register, never in the transcription. A low-confidence entry may concern both the ink and the expansion. Mathematical letter names, sentence-final full words, and accidental lexical candidates are excluded.

| Form as encountered | Scan(s) | Proposed expansion or explanation | Confidence |
|---|---|---|---|
| alg.; alg. with superscript t | 005, 050 | algébriquement | high |
| Br. | 042 | Brauer, in Br. Severi | high |
| C.Q.F.D | 035 | ce qu’il fallait démontrer | high |
| can. | 034 | canoniquement | high |
| canoniq. | 050 | canonique; the reading of the abbreviated form is uncertain | low |
| car.; car | 007, 008, 015, 017, 030, 032, 042, 044, 050 | caractéristique | high |
| cf. | 010, 022, 029 | confer; compare / see | high |
| Ch.; Chap. | 029, 041, 043 | chapitre | high |
| chgt | 017 | changement | high |
| coeff. | 011, 012 | coefficients | high |
| coh. | 005–007 | cohomologiquement in coh. plat; cohomologique in platitude coh. | high |
| cohomolgt / cohomologt | 004 | cohomologiquement; exact abbreviated spelling uncertain | medium |
| comm. | 006 | commutative | high |
| comp. | 042 | compatible, possibly a different compressed word; unfinished parenthesis | low |
| conv. | 024 | convergence | medium |
| cor. | 029, 031, 035, 037 | corollaire | high |
| diff | 007 | différentielle or différentiation; the cancelled abbreviation is not securely read | low |
| dim | 005 | dimension | high |
| Donn. | 050 | donnée(s), if the first word is correctly read; Donc remains possible | low |
| ds | 034 | dans; this is an alternative in an uncertainty mark | medium |
| déf. | 007 | définition | medium |
| ens.; ens | 012, 030 | ensemble(s) | high |
| etc | 008 | et cetera; the manuscript’s own abbreviation is retained | high |
| except with superscript ns | 030 | exceptions | medium |
| Exerc. | 022 | exercice(s) | high |
| exp. car. | 007 | exposant caractéristique | high |
| ext.; Ext. | 015, 019 | extension(s) | high |
| faisc. | 004 | faisceau | high |
| fid. plat | 013 | fidèlement plat; cancellation retained | high |
| gal. | 042 | galoisiens / galoisien | high |
| gr.; gr | 019, 028 | groupe; the repeated gr. gr. on 028 is uncertain | medium |
| gr. ann. | 006 | probably gradué / anneau gradué associé; exact abbreviated expression unresolved | low |
| hom | 006, 007 | homomorphisme(s) | high |
| i.e. | 004, 008, 009, 014, 015, 017, 022, 024, 030, 041, 042, 044, 050 | id est; c’est-à-dire | high |
| intr. | 042 | intrinsèque, possibly another adjective | low |
| inv. | 004, 005, 014 | inversible | high |
| inv. | 007 | invariante, qualifying a derivation | high |
| isom.; isom | 006, 012–014 | isomorphisme / isomorphie, according to the construction | high |
| loc. | 004–006, 014, 016 | localement | high |
| m. | 015 | morphismes, if this alternative reading is right; not the ideal symbol m of the typed sheets | low |
| mod. | 029, 039, 049 | modulo | high |
| N. | 022 | probably an unfilled exercise-number reference, not a supplied exercise number | low |
| N.B. | 017 | nota bene | high |
| nilpotts | 019 | nilpotents | medium |
| n°; n with superscript o or circle | reused typed sheets | numéro | high |
| p.ex. | 038, 040 | par exemple | high |
| pr | 019 | possibly pour; occurs only as an uncertain alternative to another reading | low |
| pro | 013 | possibly the prefix pro-; cancelled, and no fuller word can be supplied | low |
| prop.; Prop | 005, 008, 009, 012, 029, 031, 033, 035, 037, 039, 043 | proposition | high |
| pt; pts | 007, 010, 016, 028, 030, 032, 042, 044 | point; points | high |
| quelc | 013 | quelconque; the abbreviated reading is uncertain | medium |
| repr. | 012 | représente / représenté; cancelled abbreviated word | low |
| représ. | 050 | représentations, possibly another abbreviated noun | low |
| resp.; resp with superscript t | 024, 028, 031, 037, 049 | respectivement | high |
| rev.; revt; revêt; revêtts | 030, 032, 036, 042, 046 | revêtement(s) | high |
| RR | 005 | Riemann–Roch | high |
| s. s. s. | 050 | si et seulement si; unusual spacing/letter sequence retained | medium |
| schém. | 042 | schéma; the abbreviated word itself remains uncertain | low |
| ss-schéma; ss-groupe | 042, 032 | sous-schéma; sous-groupe | high |
| ss élémts nilpotts | 019 | sans éléments nilpotents; the abbreviated phrase is uncertain | medium |
| ssi | 005, 007, 008 | si et seulement si | high |
| st.ble | 030 | stable | medium |
| suppl. | 009 | supplément | medium |
| surj. | 013 | surjective | high |
| th. | 033 | théorème | high |
| tjrs | 032 | toujours | high |
| top. | 022, 024 | topologies / topologie | high |
| Top. Gén.; Top.Gén. | 041, 043, 045 | Topologie générale, the cited work | high |
| topologt / topol.? | 043 | topologiquement / topologique; faint handwritten annotation | low |
| tt; tte; ttes | 004, 005, 008, 010, 012, 013, 016, 017, 046 | tout / tous; toute; toutes, according to the visible abbreviated form | high |
| Évidt | 042 | Évidemment | high |
| élémts | 019 | éléments | medium |
| épim. | 007 | épimorphisme | medium |
| Aut; Hom; id; GL; Max; Spec; Symm | mathematical operators, where present | automorphismes; homomorphismes; identité; groupe linéaire général; maximum; spectre; construction symétrique | high |

## Complete index of inline uncertainty marks

This mechanical index includes every `\unsure` and `\illegible` occurrence in the final page files, including nested marks, cancelled passages, formulas, and diagram labels. Locations are exact lines in the saved page LaTeX, not a claim to reproduce manuscript lineation; the preceding reader’s table supplies the manuscript-location descriptions and confidence judgments. The vertical bar inside an argument separates the preferred reading from its alternative.

| File | Scan | Saved LaTeX line | Macro | Exact argument |
|---|---:|---:|---|---|
| 62.pdf | 004 | 7 | \unsure | \underline T_{C/S}\|\underline{\mathcal T}_{C/S} |
| 62.pdf | 004 | 11 | \unsure | cohomolgt\|cohomologt |
| 62.pdf | 004 | 11 | \unsure | ttes\|toute |
| 62.pdf | 004 | 13 | \unsure | \mathcal L |
| 62.pdf | 004 | 20 | \unsure | évidente |
| 62.pdf | 004 | 24 | \unsure | d'injections linéaires |
| 62.pdf | 004 | 26 | \unsure | h |
| 62.pdf | 004 | 28 | \unsure | relatives |
| 62.pdf | 004 | 29 | \unsure | d'où |
| 62.pdf | 004 | 29 | \unsure | un |
| 62.pdf | 005 | 3 | \unsure | tte |
| 62.pdf | 005 | 3 | \unsure | +1 |
| 62.pdf | 005 | 3 | \unsure | Le |
| 62.pdf | 005 | 3 | \unsure | très |
| 62.pdf | 005 | 3 | \unsure | \geq\|> |
| 62.pdf | 005 | 5 | \unsure | donc |
| 62.pdf | 005 | 5 | \unsure | -(g-1) |
| 62.pdf | 005 | 6 | \unsure | quelconque |
| 62.pdf | 005 | 7 | \unsure | Et puisque |
| 62.pdf | 005 | 8 | \unsure | par suite |
| 62.pdf | 005 | 8 | \unsure | les |
| 62.pdf | 005 | 8 | \unsure | \gg\|> |
| 62.pdf | 005 | 10 | \unsure | \mathbb P\|P |
| 62.pdf | 005 | 12 | \unsure | Ceci suffit |
| 62.pdf | 006 | 3 | \unsure | hom |
| 62.pdf | 006 | 12 | \unsure | locale |
| 62.pdf | 006 | 13 | \unsure | n |
| 62.pdf | 006 | 13 | \unsure | 0\|2 |
| 62.pdf | 006 | 13 | \unsure | $\mathcal L_0=\underline O_S$ |
| 62.pdf | 006 | 13 | \unsure | les $\mathcal L_i$, soit $i\neq1$ |
| 62.pdf | 006 | 13 | \unsure | k |
| 62.pdf | 006 | 17 | \unsure | faisant de |
| 62.pdf | 006 | 17 | \unsure | une |
| 62.pdf | 006 | 19 | \unsure | avec\|grâce à |
| 62.pdf | 006 | 21 | \unsure | \mathcal E |
| 62.pdf | 006 | 21 | \unsure | \longrightarrow\|- |
| 62.pdf | 006 | 21 | \unsure | gr. ann. |
| 62.pdf | 006 | 23 | \unsure | \longrightarrow\|- |
| 62.pdf | 006 | 25 | \unsure | et pour |
| 62.pdf | 006 | 25 | \unsure | ramenons nous |
| 62.pdf | 006 | 25 | \illegible | 3 |
| 62.pdf | 006 | 25 | \unsure | au voisinage |
| 62.pdf | 007 | 5 | \unsure | induits |
| 62.pdf | 007 | 7 | \unsure | L_{n+m}\|L_{n+m}^{0} |
| 62.pdf | 007 | 7 | \unsure | provient |
| 62.pdf | 007 | 7 | \unsure | déf. de |
| 62.pdf | 007 | 11 | \unsure | $\underline T$ |
| 62.pdf | 007 | 16 | \unsure | \longrightarrow\|- |
| 62.pdf | 007 | 16 | \unsure | est |
| 62.pdf | 007 | 16 | \unsure | épim. |
| 62.pdf | 007 | 18 | \unsure | diff |
| 62.pdf | 008 | 15 | \unsure | on a |
| 62.pdf | 008 | 19 | \unsure | \underline{\mathcal L}_3\simeq\mathcal L_2\otimes\mathcal L |
| 62.pdf | 008 | 21 | \unsure | 2 |
| 62.pdf | 008 | 23 | \unsure | 2 |
| 62.pdf | 008 | 26 | \unsure | \longrightarrow\|- |
| 62.pdf | 008 | 30 | \unsure | 0 |
| 62.pdf | 008 | 34 | \unsure | R^1 |
| 62.pdf | 008 | 39 | \unsure | n+1\|n |
| 62.pdf | 008 | 41 | \unsure | intervertir |
| 62.pdf | 008 | 42 | \unsure | A |
| 62.pdf | 009 | 13 | \unsure | des points de |
| 62.pdf | 009 | 13 | \unsure | l'infini |
| 62.pdf | 009 | 24 | \unsure | unité |
| 62.pdf | 009 | 24 | \unsure | homothétie |
| 62.pdf | 009 | 24 | \unsure | u |
| 62.pdf | 009 | 26 | \unsure | 2\|3 |
| 62.pdf | 009 | 29 | \unsure | suppl. |
| 62.pdf | 010 | 3 | \unsure | que vérifie aussi bien à priori |
| 62.pdf | 010 | 3 | \unsure | vérifiée par |
| 62.pdf | 010 | 8 | \unsure | composante de |
| 62.pdf | 010 | 8 | \unsure | de même $\mathcal E_3$, $y^3$ |
| 62.pdf | 010 | 8 | \unsure | $\mathcal E_3$ |
| 62.pdf | 010 | 10 | \unsure | la |
| 62.pdf | 010 | 12 | \unsure | z |
| 62.pdf | 010 | 14 | \unsure | notre |
| 62.pdf | 010 | 14 | \unsure | d'une |
| 62.pdf | 010 | 15 | \unsure | d'ailleurs, est essentiellement primitive |
| 62.pdf | 011 | 11 | \unsure | avec |
| 62.pdf | 011 | 11 | \unsure | \neq\|= |
| 62.pdf | 011 | 17 | \unsure | \mathbb E\|E |
| 62.pdf | 011 | 17 | \unsure | dessus\|dans |
| 62.pdf | 012 | 3 | \unsure | puis schéma en groupes |
| 62.pdf | 012 | 3 | \unsure | repr. |
| 62.pdf | 012 | 5 | \unsure | $G$. |
| 62.pdf | 012 | 5 | \unsure | n\|3 |
| 62.pdf | 012 | 9 | \unsure | X^2 |
| 62.pdf | 012 | 9 | \unsure | +\|- |
| 62.pdf | 012 | 9 | \unsure | 3\|2 |
| 62.pdf | 012 | 13 | \unsure | Y\|X |
| 62.pdf | 012 | 13 | \unsure | Y\|X |
| 62.pdf | 012 | 15 | \unsure | ce sera plus clair |
| 62.pdf | 012 | 15 | \unsure | vecteur |
| 62.pdf | 012 | 15 | \unsure | schéma |
| 62.pdf | 012 | 15 | \unsure | dimension |
| 62.pdf | 012 | 15 | \unsure | rang |
| 62.pdf | 012 | 18 | \unsure | l'ens. |
| 62.pdf | 012 | 18 | \unsure | éléments |
| 62.pdf | 013 | 3 | \unsure | donc |
| 62.pdf | 013 | 3 | \unsure | linéaire\|lisse |
| 62.pdf | 013 | 3 | \unsure | clivage |
| 62.pdf | 013 | 5 | \unsure | pro |
| 62.pdf | 013 | 5 | \unsure | obtenir cet énoncé |
| 62.pdf | 013 | 5 | \unsure | quelc |
| 62.pdf | 013 | 5 | \unsure | triangulaire |
| 62.pdf | 013 | 5 | \unsure | quotient |
| 62.pdf | 014 | 5 | \unsure | où |
| 62.pdf | 014 | 6 | \unsure | formé |
| 62.pdf | 014 | 6 | \unsure | triplets |
| 62.pdf | 014 | 13 | \unsure | conduit à une équation |
| 62.pdf | 014 | 13 | \unsure | le |
| 62.pdf | 014 | 13 | \unsure | précédent |
| 62.pdf | 015 | 3 | \unsure | type |
| 62.pdf | 015 | 3 | \unsure | de |
| 62.pdf | 015 | 3 | \unsure | à\|m. |
| 62.pdf | 015 | 3 | \unsure | \mathcal L\|L |
| 62.pdf | 015 | 3 | \unsure | \lambda\|D |
| 62.pdf | 015 | 3 | \unsure | ou même |
| 62.pdf | 015 | 3 | \unsure | en ce |
| 62.pdf | 015 | 3 | \unsure | les |
| 62.pdf | 016 | 5 | \unsure | \dot a\|a |
| 62.pdf | 016 | 9 | \unsure | -\|+ |
| 62.pdf | 016 | 13 | \unsure | 2\|3 |
| 62.pdf | 016 | 13 | \unsure | 3\|2 |
| 62.pdf | 016 | 17 | \unsure | quotient |
| 62.pdf | 016 | 18 | \unsure | le schéma |
| 62.pdf | 016 | 18 | \unsure | Brauer-Sévéri |
| 62.pdf | 016 | 18 | \unsure | marquée |
| 62.pdf | 016 | 18 | \unsure | faisceau inverse |
| 62.pdf | 016 | 18 | \unsure | qui est |
| 62.pdf | 016 | 18 | \unsure | fibré vectoriel |
| 62.pdf | 016 | 18 | \unsure | de rang un |
| 62.pdf | 016 | 20 | \unsure | dans les fibres |
| 62.pdf | 016 | 20 | \unsure | $E$ |
| 62.pdf | 017 | 3 | \unsure | que tous les corps résiduels de |
| 62.pdf | 017 | 6 | \unsure | Il en résulte aussitôt qu'il opère trivialement dans $\mathcal E_2$ [car il y opère trivialement] |
| 62.pdf | 017 | 10 | \unsure | stable qui sera le lieu $s$ opère |
| 62.pdf | 017 | 11 | \unsure | sans\|sous |
| 62.pdf | 017 | 11 | \unsure | le |
| 62.pdf | 017 | 12 | \unsure | considération |
| 62.pdf | 017 | 12 | \unsure | différentielle |
| 62.pdf | 017 | 13 | \unsure | \mathcal L\|L |
| 62.pdf | 017 | 13 | \unsure | \partial\|\vartheta |
| 62.pdf | 017 | 14 | \unsure | compatible avec tt changement de base $S$ |
| 62.pdf | 017 | 17 | \unsure | \mathcal E_3\|L_3 |
| 62.pdf | 017 | 19 | \unsure | \lambda |
| 62.pdf | 019 | 6 | \unsure | unité |
| 62.pdf | 019 | 8 | \unsure | local |
| 62.pdf | 019 | 11 | \unsure | (\text{par idéal}) |
| 62.pdf | 019 | 11 | \unsure | A^* |
| 62.pdf | 019 | 12 | \unsure | (\text{par idéal}) |
| 62.pdf | 019 | 12 | \unsure | 1\|j |
| 62.pdf | 019 | 17 | \unsure | géométriquement |
| 62.pdf | 019 | 24 | \unsure | a |
| 62.pdf | 019 | 24 | \unsure | ss élémts nilpotts |
| 62.pdf | 019 | 26 | \unsure | 3\|6 |
| 62.pdf | 019 | 29 | \unsure | Z\|\mathbb Z |
| 62.pdf | 019 | 34 | \unsure | ss élémts nilpotts |
| 62.pdf | 019 | 52 | \unsure | j |
| 62.pdf | 019 | 52 | \unsure | \text{module}\ p\|\text{unité}\ pr |
| 62.pdf | 019 | 56 | \unsure | t |
| 62.pdf | 019 | 65 | \unsure | !\|1 |
| 62.pdf | 019 | 82 | \unsure | -2/6 |
| 62.pdf | 019 | 83 | \unsure | 2 |
| 62.pdf | 019 | 91 | \unsure | 3 |
| 62.pdf | 019 | 99 | \unsure | Hom |
| 62.pdf | 019 | 99 | \unsure | \widetilde E |
| 62.pdf | 019 | 104 | \unsure | \underline{\mathrm H}\|\underline{\mathrm{Hom}} |
| 62.pdf | 019 | 104 | \unsure | O\|0 |
| 62.pdf | 019 | 104 | \unsure | \underline O\|\underline U |
| 62.pdf | 019 | 105 | \unsure | \underline{\mathrm H}\|\underline{\mathrm{Hom}} |
| 62.pdf | 019 | 105 | \unsure | \underline{\mathrm H}\|\underline{\mathrm{Hom}} |
| 62.pdf | 020 | 20 | \unsure | -- |
| 62.pdf | 021 | 5 | \unsure | i\ne j |
| 62.pdf | 021 | 5 | \unsure | x_j\|x |
| 62.pdf | 021 | 8 | \unsure | y\|x |
| 62.pdf | 021 | 22 | \unsure | on trouve |
| 62.pdf | 021 | 30 | \unsure | \} |
| 62.pdf | 021 | 34 | \unsure | 3\|2 |
| 62.pdf | 021 | 40 | \unsure | = |
| 62.pdf | 021 | 46 | \unsure | 9\|4 |
| 62.pdf | 021 | 53 | \unsure | x^2 |
| 62.pdf | 021 | 59 | \unsure | x_1x_2 |
| 62.pdf | 022 | 19 | \unsure | fait général |
| 62.pdf | 022 | 19 | \unsure | . |
| 62.pdf | 023 | 4 | \unsure | =-\|= |
| 62.pdf | 023 | 4 | \unsure | - |
| 62.pdf | 023 | 6 | \unsure | x_1x_2x_3 |
| 62.pdf | 023 | 11 | \unsure | - |
| 62.pdf | 023 | 23 | \unsure | (a/3) |
| 62.pdf | 023 | 27 | \unsure | 2 |
| 62.pdf | 023 | 28 | \unsure | a |
| 62.pdf | 023 | 29 | \unsure | a |
| 62.pdf | 023 | 37 | \unsure | = |
| 62.pdf | 024 | 11 | \unsure | engendré |
| 62.pdf | 024 | 12 | \unsure | Dire que la |
| 62.pdf | 024 | 12 | \unsure | top. est |
| 62.pdf | 024 | 12 | \unsure | celle de |
| 62.pdf | 024 | 12 | \unsure | conv. simple |
| 62.pdf | 024 | 14 | \unsure | ' |
| 62.pdf | 024 | 24 | \unsure | a_{in}\|e_{in} |
| 62.pdf | 025 | 7 | \unsure | a |
| 62.pdf | 025 | 7 | \unsure | 2 |
| 62.pdf | 025 | 10 | \unsure | x_4 |
| 62.pdf | 025 | 17 | \unsure | 1 |
| 62.pdf | 025 | 17 | \unsure | 2 |
| 62.pdf | 025 | 17 | \unsure | 3 |
| 62.pdf | 025 | 28 | \unsure | x_3 |
| 62.pdf | 025 | 32 | \unsure | on trouve |
| 62.pdf | 025 | 38 | \unsure | =\|\cdot |
| 62.pdf | 026 | 10 | \unsure | 59 |
| 62.pdf | 028 | 3 | \unsure | pts |
| 62.pdf | 028 | 15 | \unsure | renommer |
| 62.pdf | 028 | 16 | \unsure | t |
| 62.pdf | 028 | 16 | \unsure | t-1 |
| 62.pdf | 028 | 16 | \unsure | 1/t |
| 62.pdf | 028 | 18 | \unsure | \psi^2=\varphi\|\varphi^2=\psi |
| 62.pdf | 028 | 28 | \unsure | gr. gr. cyclique |
| 62.pdf | 028 | 28 | \unsure | \textsuperscript{t} |
| 62.pdf | 028 | 35 | \unsure | de |
| 62.pdf | 028 | 39 | \unsure | permutant à |
| 62.pdf | 028 | 39 | \unsure | \mathfrak S_6\|\mathfrak S_3 |
| 62.pdf | 028 | 39 | \unsure | sauf\|avec |
| 62.pdf | 030 | 8 | \unsure | \mathbb Z |
| 62.pdf | 030 | 10 | \unsure | formé |
| 62.pdf | 030 | 10 | \unsure | de |
| 62.pdf | 030 | 10 | \unsure | distincts |
| 62.pdf | 030 | 10 | \unsure | 1 |
| 62.pdf | 030 | 10 | \unsure | \infty\|0 |
| 62.pdf | 030 | 10 | \unsure | st.ble |
| 62.pdf | 030 | 18 | \unsure | Le |
| 62.pdf | 030 | 20 | \unsure | distinct de $\sigma$ |
| 62.pdf | 030 | 22 | \unsure | ens. |
| 62.pdf | 030 | 30 | \unsure | globalement |
| 62.pdf | 030 | 31 | \unsure | les except\textsuperscript{ns} qu'il y a pour car. $2$ ou $3$ de $S$ |
| 62.pdf | 031 | 16 | \unsure | ' |
| 62.pdf | 032 | 7 | \unsure | \mathfrak S_3 |
| 62.pdf | 032 | 7 | \unsure | Z\|\mathbb Z |
| 62.pdf | 032 | 7 | \unsure | il est\|qui est |
| 62.pdf | 032 | 7 | \unsure | est isomorphe |
| 62.pdf | 032 | 7 | \unsure | y |
| 62.pdf | 032 | 7 | \unsure | simplement |
| 62.pdf | 032 | 7 | \unsure | le schéma du revt |
| 62.pdf | 033 | 5 | \unsure | \varnothing |
| 62.pdf | 033 | 5 | \unsure | pui sque |
| 62.pdf | 033 | 9 | \unsure | 3$^\circ$\|3 |
| 62.pdf | 034 | 2 | \unsure | ramification |
| 62.pdf | 034 | 2 | \unsure | dans\|ds |
| 62.pdf | 034 | 2 | \unsure | un domaine de |
| 62.pdf | 034 | 2 | \unsure | descente |
| 62.pdf | 034 | 4 | \unsure | fibration |
| 62.pdf | 035 | 19 | \unsure | doit\|dit |
| 62.pdf | 036 | 3 | \unsure | section |
| 62.pdf | 036 | 3 | \unsure | P^1_{\infty} |
| 62.pdf | 036 | 3 | \unsure | G_m |
| 62.pdf | 036 | 3 | \unsure | é |
| 62.pdf | 036 | 3 | \unsure | P^1_m |
| 62.pdf | 036 | 3 | \unsure | x |
| 62.pdf | 036 | 4 | \unsure | x' |
| 62.pdf | 036 | 4 | \unsure | \sim |
| 62.pdf | 036 | 4 | \unsure | \sim |
| 62.pdf | 036 | 8 | \unsure | se |
| 62.pdf | 036 | 8 | \unsure | \mathbb Z_m |
| 62.pdf | 036 | 8 | \unsure | \{ |
| 62.pdf | 036 | 8 | \unsure | $\in A$, donc de la forme $2^\alpha3^\beta$ |
| 62.pdf | 037 | 5 | \unsure | \omega\|w |
| 62.pdf | 037 | 9 | \unsure | sedond\|second |
| 62.pdf | 037 | 11 | \unsure | lo\|le |
| 62.pdf | 037 | 11 | \unsure | en'fait\|en fait |
| 62.pdf | 038 | 2 | \unsure | défini |
| 62.pdf | 038 | 2 | \unsure | normalisée en |
| 62.pdf | 038 | 4 | \unsure | En fait |
| 62.pdf | 038 | 6 | \unsure | \lambda |
| 62.pdf | 038 | 6 | \unsure | \lambda |
| 62.pdf | 038 | 6 | \unsure | \lambda |
| 62.pdf | 038 | 6 | \unsure | \lambda |
| 62.pdf | 038 | 11 | \unsure | x |
| 62.pdf | 038 | 26 | \unsure | 2 |
| 62.pdf | 038 | 26 | \unsure | 2 |
| 62.pdf | 038 | 26 | \unsure | 2 |
| 62.pdf | 038 | 41 | \unsure | x''^3-x'^3 |
| 62.pdf | 038 | 41 | \unsure | =(x''-x')(x''^2+x'x''+x'^2)=0 |
| 62.pdf | 040 | 8 | \unsure | g^*(t)\|f^*g^*(t) |
| 62.pdf | 040 | 10 | \unsure | (G_a)_S |
| 62.pdf | 040 | 10 | \unsure | à partir de |
| 62.pdf | 040 | 10 | \unsure | m\|a |
| 62.pdf | 040 | 27 | \unsure | serait |
| 62.pdf | 040 | 27 | \unsure | prouver |
| 62.pdf | 040 | 27 | \unsure | pour $\sigma$ dans ce dernier cas |
| 62.pdf | 042 | 2 | \unsure | trisection |
| 62.pdf | 042 | 2 | \unsure | schém. |
| 62.pdf | 042 | 2 | \unsure | intr. |
| 62.pdf | 042 | 2 | \unsure | \sigma_S\|\sigma |
| 62.pdf | 042 | 2 | \unsure | on restitue |
| 62.pdf | 042 | 2 | \unsure | [en ses points |
| 62.pdf | 042 | 2 | \unsure | f |
| 62.pdf | 042 | 2 | \unsure | puis |
| 62.pdf | 042 | 2 | \unsure | par |
| 62.pdf | 043 | 18 | \unsure | topologt\|topol.? |
| 62.pdf | 044 | 2 | \unsure | pts |
| 62.pdf | 044 | 6 | \unsure | \infty |
| 62.pdf | 044 | 6 | \unsure | et |
| 62.pdf | 044 | 6 | \unsure | est |
| 62.pdf | 044 | 7 | \unsure | aux dits pts |
| 62.pdf | 044 | 10 | \unsure | _S |
| 62.pdf | 044 | 10 | \unsure | j |
| 62.pdf | 044 | 10 | \unsure | j |
| 62.pdf | 044 | 10 | \unsure | i\|j |
| 62.pdf | 044 | 12 | \unsure | j\|i |
| 62.pdf | 044 | 12 | \unsure | j\|i |
| 62.pdf | 044 | 12 | \unsure | x |
| 62.pdf | 044 | 12 | \unsure | et |
| 62.pdf | 044 | 12 | \unsure | À déduire des formalismes\|À déduire les formules |
| 62.pdf | 045 | 9 | \unsure | .; |
| 62.pdf | 046 | 4 | \unsure | toute |
| 62.pdf | 046 | 6 | \unsure | comme on connaît |
| 62.pdf | 046 | 6 | \unsure | revêt |
| 62.pdf | 046 | 8 | \unsure | se pose la |
| 62.pdf | 048 | 2 | \unsure | Supposons |
| 62.pdf | 048 | 2 | \unsure | est égal à |
| 62.pdf | 048 | 2 | \unsure | 0 |
| 62.pdf | 048 | 4 | \unsure | donc $X'$ |
| 62.pdf | 048 | 4 | \unsure | Tout |
| 62.pdf | 048 | 4 | \unsure | Supposons |
| 62.pdf | 048 | 4 | \unsure | grâce |
| 62.pdf | 048 | 8 | \unsure | Donc |
| 62.pdf | 048 | 8 | \unsure | ce dernier |
| 62.pdf | 048 | 8 | \unsure | ce fibré conique |
| 62.pdf | 048 | 8 | \unsure | deux |
| 62.pdf | 048 | 8 | \unsure | X''\|X''' |
| 62.pdf | 050 | 2 | \unsure | Autre façon |
| 62.pdf | 050 | 4 | \unsure | simples |
| 62.pdf | 050 | 6 | \unsure | X |
| 62.pdf | 050 | 6 | \unsure | revêtement |
| 62.pdf | 050 | 6 | \unsure | \mathfrak S_3 |
| 62.pdf | 050 | 6 | \unsure | non |
| 62.pdf | 050 | 8 | \unsure | X\simeq P^1_S\times_{(S,\mathfrak S_3)} |
| 62.pdf | 050 | 8 | \unsure | \mathbf P\|P |
| 62.pdf | 050 | 16 | \unsure | \varphi |
| 62.pdf | 050 | 16 | \unsure | \bar\sigma |
| 62.pdf | 050 | 26 | \unsure | (car. $\ne2,3$) |
| 62.pdf | 050 | 28 | \unsure | X\simeq P^1_S |
| 62.pdf | 050 | 28 | \unsure | Donn. non canoniq.\|Donn. non canonique |
| 62.pdf | 050 | 28 | \unsure | par |
| 62.pdf | 050 | 28 | \unsure | quoi |
| 62.pdf | 050 | 28 | \unsure | t(t-1)\in\mathbb Z |
| 62.pdf | 050 | 28 | \unsure | représ. |
| 62.pdf | 050 | 28 | \unsure | si et |

## Legibility and limits

The typed reused sheets are generally much more legible than the rapid manuscript prose, although type defects, overtyping, punctuation, underlines, and added handwriting still create local doubt. The handwritten mathematical displays are often clearer than their connecting prose. Long near-horizontal pen movements can conceal word endings; neither grammatical agreement nor mathematical plausibility has been used to silently complete them.

I trust least the intertwined revisions on scans 006, 009, 013–017; the compressed Kummer qualifications and lower diagram on 019; the right-edge naming note on 028 and faint margin on 030; the structural-object wording on 042; and the small interlinear insertion near the bottom of 050. Those passages carry explicit doubt marks. The final two words attempted as “par quoi” on 050 are especially insecure. The three physically unreadable cancelled words on 006 are the only use of \illegible; no formula or diagram symbol has been replaced by that macro.

All 46 pages received a second visual reading by the same primary reader, and recurring alphabets and accents were compared before freezing. TikZ reproductions preserve the observed shapes, labels, connections, and rough relative placement; they are approximations of the pen drawings, not facsimiles. Compilation verifies syntax only. The presence of uncertainty marks and a complete inventory does not certify an error-free transcription or an independently reviewed reading.

The final register contains 233 detailed reader observations and 348 inline uncertainty occurrences. Repetition and nested marks are counted separately in the latter figure.
