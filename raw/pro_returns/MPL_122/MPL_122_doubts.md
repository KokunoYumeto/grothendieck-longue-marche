# MPL_122 — Doubts and notation

## Package notation table

The table began with scan 003 and was completed in the cross-page audit before the context archive was opened. It records visual conventions, not a reconstruction of the intended mathematics. Differences that the ink does not resolve remain marked locally; a recurring symbol is not made certain merely because it has a plausible meaning elsewhere.

| Manuscript sign / alphabet | LaTeX used | Cross-page reading and limits |
|---|---|---|
| Ordinary Latin space labels | `P,Q,R,W,M,N,S,T` | Preserve the letters at each occurrence, including the apparent `Q=P-\mathring P` in scan 007 and the change from `V` to `W` in scan 034. |
| Small hollow circle above a space | `\mathring P`, `\mathring Q`, `\mathring M` | Interior notation in scans 003–015 and 020–026; distinguished from a prime. |
| Dot over a letter in the comparison table | `\dot M`, `\dot N` | The table in scan 017 has dots; these have not been replaced by boundary signs. |
| Boundary sign | `\partial P`, `\partial M`, etc. | Read separately from a lower-case delta; repeatedly checked in scans 003–017 and 020–026. |
| Prime on a space or arrow label | `P'`, `V'`, `X'`, `\rho'`, `\alpha'`, `\beta'` | Prime strokes in scans 003–005, 017, 022–024; never used as a substitute for the compact-support exclamation mark. |
| Exclamation mark below cohomology or sections | `H_!^i`, `\Gamma_!`, `(\Gamma,\pi)_!` | Compact-support style signs in scans 003–011 and 020–028. Scan 028 retains a local doubt on its very small subscript. |
| Star below a sections symbol | `\Gamma_{\unsure{*}}`, `(\Gamma,\pi)_{\unsure{*}}` | The small marks in scan 020 are not silently converted into exclamation marks. |
| Underline below cohomology | `\underline H` | Scan 003; distinct from ordinary `H`. |
| Tilde over a boundary or space | `\widetilde{\partial P}`, `\widetilde P` | Collar/thickening notation in scans 003–009. |
| Vee denoting a dual | `F^\vee`, `K^\vee`, `H^i(M)^\vee` | The cohomological handwritten sequence uses a vee; scans 003–011 and 017, 022–032. |
| Asterisk and prime on module duals | `M^*`, `M^{**}`, `M'` | Kept distinct in the reused French typescript, scans 012, 014, 016. These are not changed to vees. |
| Circle on an orthogonal | `N^\circ`, `U^\circ` | Reused French typescript, scans 012, 014, 016; distinguished from the hollow circle above the interior of a manifold. |
| Orientation letter | `T`; locally `\unsure{\mathcal T|\tau}` | Ordinary `T` on scan 003; the cursive mark in scans 007, 009, 011 remains script-T/tau uncertainty. The unambiguous trivialization `\tau` on scan 013 is retained separately. |
| Generic-fibre-like subscript | `\unsure{\eta|\gamma}` | Repeated uncertain hooked letter in scans 017 and 034; the same alternative order is used throughout. The upper left label in one scan 017 diagram also has `\eta|S`. |
| Greek gamma on the conics | `\gamma_1`, `\gamma_2` | Clear conic labels in the reused English material, scans 029 and 033; not merged with the doubtful generic-fibre-like subscript. |
| Other Greek letters | `\alpha,\beta,\rho,\sigma,\tau,\varphi,\phi,\lambda,\mu,\pi,\Lambda` | Retain the local alphabets and indices; `\rho'` is a prime, while `(-)^\vee` is a dual. The function in scan 031 remains `\nu|v`. |
| Capital Phi and Psi | `\Phi,\Phi',\Psi,\Psi'` | Four arrangements in the recap of scan 011. |
| Doubled R for derived functors | `\mathbb R\Gamma`, `\mathbb R\operatorname{Hom}` | Consistent visual transcription of the doubled R in scans 020, 022, 024, 026. |
| Complex degree dots | `K^\bullet`, `L^\bullet`, `R^\bullet` | Scans 020–026. The missing dot in the visible `R^\omega` on scan 020 is not supplied. |
| Trivial action / invariant / forgetful superscripts | `\mathrm{triv}`, `\pi`, `\omega`, `\mathrm{oub}` | `\omega` in scan 020 and the three-letter `oub` in scan 024 are preserved as different written forms. |
| Upright categories and operators | `\mathrm D`, `\operatorname{Hom}`, `\operatorname{ob}`, `\mathrm{SL}`, `\operatorname{PGL}` | Typographical rendering of the visible names, not additional definitions. |
| Script letters | `\mathcal A`, `\mathcal C` | Last finiteness sheet, scan 035. Its category names and exponents remain substantially uncertain. |
| Gothic letter on final sheet | `\unsure{\mathfrak B|\mathfrak I}` | Scan 035: the two-loop/vertical mark is not secure; the B-like reading is first after the second audit. |
| Underlined ideals and number field symbol | `\underline p`, `\underline a`, `\underline m`, `\underline r`, `\underline Q` | French reused typescript, scans 004–012. Do not modernize them to Gothic ideals or blackboard-bold Q. |
| Underlined structure-sheaf letter | `\underline{o}`, `\uline{o}` | English reused typescript, scans 021 and 027; the visible lower-case underlined letter is not replaced with `\mathcal O`. |
| Outlined / doubled projective, group, and integer letters | `\mathbb P`, `\mathbb G_m`, `\mathbb Z_2` | English reused material, scans 021–033. The overline on G in scan 025 and the Q/C letter in scan 031 remain doubtful. |
| Small round subscript in English typescript | `_o`; locally `_{\unsure{o|0}}` | The rounded subscript is transcribed as lower-case o where that is visually favoured; ambiguity is retained in scan 025. A similar ambiguity remains in scan 010. |
| Equality, isomorphism, and homotopy-like wave | `=`, `\simeq`, `\sim` | Kept as drawn, including vertical equivalence marks in diagrams; scan 015's small Q-to-T label remains `\simeq|2`. |
| Straight arrow, hook, two heads, double implication | TikZ-cd `\arrow`, `hook`, `leftrightarrow`, `Rightarrow` | Read from the endpoints. The large lattices in scan 017 and the endpoint equalities in scan 028 were separately checked for their actual grid destinations. |
| Plain connecting stroke | `\mathbin{-}`, `\arrow[r,dash]`, or `\arrow[r,no head]` | An absent arrowhead is not supplied from exactness. Ambiguous short connectors in scan 030 have `\unsure{\mathbin{-}|\longrightarrow}`. |
| Dashed connecting stroke | `dashed`, sometimes together with `dash` | A dashed shaft and an arrowless shaft are distinct properties, both retained in scan 020. |
| Reversed or altered bounds | `\le`, `\ge`, `\ne`, with local `\deleted` / `\inserted` | Especially scans 026–034. Degree changes and suspect signs are retained; no uniform mathematical correction was applied. |
| Written interval / shift delimiters | Literal `(-1]`, `(-2]`, `(-1)`, or brackets as present | Mixed delimiters on scan 020 remain literal. Missing parentheses in scans 011 and 034 are likewise not silently supplied. |
| Handwritten and typed double quotes | Two backticks and two apostrophes | All quotation pairs are consistent. The three repeated closing-quote-like marks on scan 015 are ditto marks and remain separate. No guillemets were supplied. |
| Circled labels and underlining | `\textcircled`, `\uline`, `\uuline` | Preserve a/b/c/d/e and primed triangle labels, single versus double underlining, and the circled dimension condition. |

Abbreviated words are listed, with proposed expansions, only in the abbreviations section below. The table's mathematical descriptions are editorial aids and do not form part of the transcription.


## Reading doubts

| Cote | Scan | Approximate location | Reading | Alternatives / difficulty | Confidence |
|---|---:|---|---|---|---|
| 122 | 3 | line 1 insertion | para | Small circled insertion; read as prefix to compacte. | medium |
| 122 | 3 | exact-sequence duality line | n-i | Exponent overwritten; no distinct earlier exponent recoverable. | medium |
| 122 | 3 | right margin | fibre | fibres; final stroke uncertain. | medium |
| 122 | 3 | Poincaré sentence | topologique | Long compressed word; not expanded from an abbreviation with confidence. | medium |
| 122 | 3 | cancelled last two lines | l’isom. à prendre entre; collar objects | Several letters and decorations obscured by the cancellation strokes. | low |
| 122 | 3 | phi display | plain dash | No clear right arrowhead; deliberately retained as a dash. | high |
| 122 | 4 | 7, throughout | underlined p | Underline preserved literally; no conversion to Gothic type. | high |
| 122 | 4 | 8 polynomial display | two dots between factors | Two printed dots are visible, not silently changed to three. | high |
| 122 | 4 | pencil lower-left number | 3 | Attribution of pencil foliation to Grothendieck is not established. | medium |
| 122 | 4 | 8 polynomial, before first 1 | < | Small handwritten angled mark; possibly a correction mark rather than a mathematical inequality. | low |
| 122 | 5 | cancelled display | H^i(P-partial P) | Right-hand H has no clear support subscript; retained without one. | medium |
| 122 | 5 | left marginal diagram | isomorphism sign after collar minus boundary; =P-P prime | Small partly crowded signs and their attachment. | low |
| 122 | 5 | right marginal caption | équivalences d’ | Caption stops after the small final strokes; no completion supplied. | low |
| 122 | 5 | main diagram | support P prime; exponent i | Support overwritten; upper-right exponent partly overwritten. | medium |
| 122 | 5 | last display | H^i_?; P prime or interior P prime; deleted mod | Several superposed strokes; lower index may be a question mark. | low |
| 122 | 6 | 1 a), first Top. gén. reference | 3e éd. | 2e éd.; digit has an overstrike. | medium |
| 122 | 6 | 2, locally retrobounded | rétrobornée | Second image audit resolves the typography as one word; retained here as a resolved earlier reading question. | high |
| 122 | 6 | 1 b), 3 a) | underlined R and r | Literal underlines retained rather than converting to Gothic. | high |
| 122 | 7 | line 1 deleted word | par | Only initial p and dense horizontal cancellation remain. | low |
| 122 | 7 | definition of Q | P minus interior P | The first letter reads P, not W; this is retained despite the later decomposition. | high |
| 122 | 7 | dimension sentence | dim | codim; long initial stroke ambiguous. | medium |
| 122 | 7 | after Soit R | précisera | Cancelled word partly overlaid. | low |
| 122 | 7 | orientation sheaf, repeated | calligraphic T | tau; same looped handwritten sign retained consistently here. | medium |
| 122 | 7 | relative sequence third term exponent | i | Overwritten addition or cancellation adjacent to exponent; no secure extra digit. | low |
| 122 | 7 | after Mayer-Vietoris | alpha | Reference symbol matches the mark beside W=P union Q. | medium |
| 122 | 7 | square-bracket phrase | en faisant transposée | Abbreviated/compressed initial words. | medium |
| 122 | 7 | last sequence first object | W-T | W-R; letter is faint and narrower than most R’s. | medium |
| 122 | 7 | last line second space | Q | R; heavy overwritten letter. | low |
| 122 | 7 | last line first coefficient | F without dual sign | No vee visible over first F; do not harmonize with preceding line. | high |
| 122 | 8 | first line | K_o | K_0; circular subscript indistinguishable in type. | medium |
| 122 | 8 | 6 f) | directe.d’un | The dot may be an accidental mark rather than punctuation. | medium |
| 122 | 9 | cancelled upper-left margin | si compact | Two very small words heavily crossed out; alternative reading not secure. | low |
| 122 | 9 | cancelled cohomology support | ! | Subscript overwritten by dense strokes. | low |
| 122 | 9 | final sequence | dash connections | Arrowheads not visible on these horizontal strokes. | medium |
| 122 | 9 | final duality orientation sign | calligraphic T | tau, as in scan 007. | medium |
| 122 | 10 | opening paragraph | repeated de A est alors V. Donner un exemple | Repetition is visible in the typescript and retained, including unmatched parenthesis. | high |
| 122 | 10 | 5 a), citation | l’exerc. de Ens. | No exercise number is printed between exerc. and de. | high |
| 122 | 10 | 5 b) | K_o, v_o | Zero versus lower-case o not distinguishable. | medium |
| 122 | 10 | 3 c) | rétrobornée | Second image audit resolves the typography as one word; retained here as a resolved earlier reading question. | high |
| 122 | 11 | top diamond first expression | H^(i-1)(R,F | Closing parenthesis not visibly written; left incomplete. | medium |
| 122 | 11 | central circled caption cancelled word | ordinaires | Dense overwriting before pour P subset W. | low |
| 122 | 11 | left boxed second row | P | Last letter overwritten; P preferred. | medium |
| 122 | 11 | right rotated 1° | S times T | R=T; cancellation line intersects the letters. | low |
| 122 | 11 | right rotated last line | H_Q^i(W) times H^(n-i)(Q plus/comma | Unfinished formula; trailing stroke crosses boundary of cancellation. | low |
| 122 | 11 | recapitulation Psi prime row | H - duals - | Initial repeated/ditto-like sign overwritten. | low |
| 122 | 11 | recapitulation Phi parenthesis | deleted pas de H(T) | A long crossing stroke traverses it; whether inherited from the older rotated cancellation is uncertain. | low |
| 122 | 11 | orientation sign | calligraphic T / tau | Consistent provisional reading with scans007 and009. | medium |
| 122 | 11 | rotated cancelled block, fourth cohomology line | Q-\partial Q | Q,\partial Q; short horizontal stroke partly crossed by cancellation. | low |
| 122 | 12 | pencil upper-right | W | 11; the mark resembles a W rather than two digits, so retained as a marginal mark. | low |
| 122 | 12 | d, final sentence | top ologie | Visible internal space retained. | high |
| 122 | 12 | orthogonal notation | N circle | Small round exponent, not silently converted to zero. | high |
| 122 | 13 | before first fibration diagram | deux | des; word retraced. | medium |
| 122 | 13 | base-manifold qualification | cptes | Abbreviation for compactes appears likely, without expanding it in transcription. | medium |
| 122 | 13 | left marginal cancelled mark | W | Small overwritten isolated letter. | low |
| 122 | 14 | below text | -:-:-:- | The typewritten closing ornament is blurred; four short strokes and three colon-like pairs. | medium |
| 122 | 15 | line 1 | suppose | Very compressed verb; “suppose” is the best letter-based reading. | medium |
| 122 | 15 | line 3 | communs (deleted) | A cancellation masks most internal letters. | low |
| 122 | 15 | upper middle | On peut; On aura (deleted) | Two abandoned starts, heavily struck. | low |
| 122 | 15 | after l’inclusion | un (deleted) | Only a short wavy trace survives beneath the strike. | low |
| 122 | 15 | middle | En fait; On a donc (deleted) | Crossed-out starts; endings obscured. | low |
| 122 | 15 | diagram, Q→T | \simeq&#124;2 | Small curved mark along the Q-to-T arrow resembles the rotated isomorphism mark seen elsewhere, with 2 retained as an alternative. | low |
| 122 | 15 | diagram, N | D_1 | The 1 appears at baseline/subscript height, not confidently as a superscript. | medium |
| 122 | 15 | diagram centre | ∂ (deleted) | Small crossed mark after ∂M may be an abandoned boundary sign. | low |
| 122 | 15 | diagram right | S^1 | A thick extra stroke below the superscript is not confidently separable. | medium |
| 122 | 16 | e), parenthesis after u(x)≠0 | x∈U | The visible membership sign has no confident negation stroke; retained despite the surrounding argument. | high |
| 122 | 17 | header and diagrams | η&#124;γ | Repeated descending Greek letter; provisional consistent first reading η, alternative γ. | medium |
| 122 | 17 | table N entry | D (deleted), ∼e | The black overwritten letter and relation are indistinct. | low |
| 122 | 17 | upper central diagram | s; s; T; crossed × on S→N | Labels overlap hatching; arrows and oval outlines intersect. | low |
| 122 | 17 | upper central diagram | M→P and P→W hooks | Both ends are heavily retraced; hook tails are retained, with directions from the visible heads. | medium |
| 122 | 17 | upper right count | (5 choose 2)=5.4.3/12.=10 | Numerator and denominator copied literally; no missing factor supplied. | high |
| 122 | 17 | left cancellation | H^{n+i}; H^i(B | Upper exponent incomplete/overwritten; lower expression has no secure closing parenthesis. | low |
| 122 | 17 | lower central diagram | η&#124;S; S¹; X′s | Black corrections and intersecting outlines obscure these separate labels. | low |
| 122 | 17 | lower cohomology diagram | n−i−1 | Stroke before 1 is thick and blot-like; marked within both occurrences. | medium |
| 122 | 17 | last cohomology arrow | H^{n−i}(P)vee | Exponent is overwritten and partly raised above the original baseline. | low |
| 122 | 17 | right bottom prose | relative | Last word is compressed against the edge; no final plural s established. | medium |
| 122 | 20 | a), after derived R | (Γ,π) (deleted) | Dense scribble before Γ; only the best reading can be offered. | low |
| 122 | 20 | a), Γ subscripts | * | Small star-like marks beneath both Γ occurrences; distinct from ! in the left object. | medium |
| 122 | 20 | a), notation R | mathbb R | The derived-functor R is drawn with doubled vertical stems, unlike the separate object R. | high |
| 122 | 20 | b), product formula | (-1] | Round opening and square closing marks retained as visible. | high |
| 122 | 20 | b), β annotation | dévolution | Word after “suite exacte de” is compressed; do not substitute a familiar name for the sequence. | low |
| 122 | 20 | c), superscripts | R^ω, K^{bullet ω} | No separate bullet securely visible on the R object. | medium |
| 122 | 20 | d), lower left object | (-2] | Again a round opening with square closing shift mark. | high |
| 122 | 20 | last bracketed note | Cohomologie&#124;cohomologie | Initial letter much larger than the following letters. | medium |
| 122 | 21 | first paragraph, α∈ | overline G_m&#124;G_m | A horizontal line appears above the doubled G, possibly a separate bar. | medium |
| 122 | 21 | coset-space paragraph | β(g), twice | Both letters are visibly lower-case; the later displayed β(G) is upper-case. | high |
| 122 | 21 | middle paragraph and φ* | underlined o(1) | The sheaf symbol is a small underlined o, not silently replaced by calligraphic O. | high |
| 122 | 22 | middle NB | induit | A heavy stroke passes through the middle letters, possibly retracing rather than deletion. | medium |
| 122 | 22 | pair (W,Q) | Q with W0 added beneath | No secure strike through Q; the addition and its adjacent black mark are retained. | low |
| 122 | 22 | last line before rule | aux isos canons aux ≃ objets ....) | Very compressed unfinished parenthetical phrase; word division and final noun uncertain. | low |
| 122 | 22 | slanted left margin | à prouver ... donnera la justif. formelle ... une donnée de ce type | Least secure prose on this sheet; each uncertain group is marked in place after rotated enlargement. | low |
| 122 | 22 | cancelled expression before H^{2n} | RΓ(Λ) | Dense overwriting leaves only parts of R, Γ and a parenthesis secure. | low |
| 122 | 22 | last line | (signe ?) | This is the author’s own question mark, distinct from editorial reading doubt. | high |
| 122 | 24 | c′, K superscripts | oub | Three small letters appear, rather than a single ω as on scan 020. | medium |
| 122 | 24 | b′ top object final sign | I&#124;l | A single vertical stroke follows the final ≃, with no secure foot or dot. | low |
| 122 | 24 | left of b′ | 1 (deleted) | Isolated scribbled numeral/letter; best reading 1. | low |
| 122 | 24 | cancelled prose | Et les triangles d et e deviennent chacun | The initial phrase is overlapped by the cancellation zigzag. | medium |
| 122 | 24 | after nouvelle | donnée (deleted) | Only parts of the abandoned word remain visible. | low |
| 122 | 24 | cancelled u1 target | H&#124;K | Two vertical strokes remain; the expected complex name is not silently supplied. | low |
| 122 | 24 | cohomology pairings | revised exponents | Original exponents heavily overwritten; current values and best readings of deleted values are distinguished. | low |
| 122 | 24 | before β | le (deleted) | Small black retraced word, possibly an abandoned article. | low |
| 122 | 25 | first paragraph | opensubset | No space between open and subset is visible in the typewriting. | high |
| 122 | 25 | above H4 | ∼∼ | Tiny detached wavy ink marks; lexical status unclear, retained without inventing a word. | low |
| 122 | 25 | Note also | σ_o&#124;σ_0 | The subscript is round and not distinguishable as letter or digit. | medium |
| 122 | 25 | iii), conjugation formula | σ.α.σ^{-1}=−α^{-1} | A separate short dash is visible before α^{-1}; possibly a stray mark, therefore marked. | medium |
| 122 | 25 | iii), group symbol | overline G_m&#124;G_m | As on scan 021, an extra horizontal stroke may belong to the double-stroked G rather than an overbar. | medium |
| 122 | 26 | line 1 | remarquables | Rapidly reduced middle syllables. | medium |
| 122 | 26 | boxed pairing | accoupl. | Abbreviated word overwritten at its end. | low |
| 122 | 26 | NB line 2 | deleted boundary sign | Overwritten loop immediately before W0. | low |
| 122 | 26 | NB line 4 | les preuves | Two struck-through words. | low |
| 122 | 26 | NB line 6 | transposées | Ending reduced to a stroke. | medium |
| 122 | 26 | left lower margin | plus bas | Small sloping pencil note. | medium |
| 122 | 26 | sphere paragraph | exacte; deleted d) | Final e and crossed short item uncertain. | medium |
| 122 | 26 | bottom cancelled sequence | 0 H^{2n+1}(W-W0), 0 H^{2n}(W0) | Several superposed cancellation strokes and possible replacement zeros; sequence retained with doubts. | low |
| 122 | 27 | line 1–2 | projection embeddings | The typescript reads pro- / jection, not projective. | high |
| 122 | 27 | lines 10–19 | subscript o | Round subscripts written as o; may denote zero. | medium |
| 122 | 27 | line 15 | underlined o | Small underlined o, not silently replaced by calligraphic O. | high |
| 122 | 27 | line 18 | be v_j be | Repeated be is present in the typescript. | high |
| 122 | 28 | upper right cloud | conclusion visible de | First two words compressed; Lefschetz affine local plus bas clear. | low |
| 122 | 28 | above left NB | supposons | Heavily scribbled-out word. | low |
| 122 | 28 | left NB | sph. coh.; deleted W-W0 | Abbreviated words and cancelled opening difficult. | low |
| 122 | 28 | left NB middle | deleted W; de plus | Overwritten fragments. | low |
| 122 | 28 | first Lefschetz bound | i le n-2 &#124; n-1 | Final overwritten numeral resembles 2; retain alternative. | medium |
| 122 | 28 | mono bound | deleted -2 | Black cancellation between n and -1. | low |
| 122 | 28 | above cancelled line | dualité cela s’interprète | Insertion crosses the cancelled sentence; wording partly reduced. | medium |
| 122 | 28 | dual map | H^i_!(W0) | Small mark below H could be ! or a residual ink mark. | low |
| 122 | 28 | dual bounds | i ge n+1; i ge&#124;= n deleted +1 | Both endpoints overwritten; relation in second line ambiguous. | low |
| 122 | 29 | base point subscripts | o | Round subscript shape retained consistently with reused pp4.13–14; may denote zero. | medium |
| 122 | 30 | top right deletion | n,n+1 and ] | Heavy overwriting after i ne. | low |
| 122 | 30 | right crossed inequalities | n+1 ne 2n+1 | First left-hand n overwritten. | medium |
| 122 | 30 | n=1 second sequence | deleted Lambda | Small overwritten mark after W0. | low |
| 122 | 30 | lower prose | passage; deleted les les | Rapid handwriting and two crossed small words. | medium |
| 122 | 30 | lower vanishing bounds | deleted +1 | Both terminal groups are blacked out. | low |
| 122 | 30 | lower right | Indépendt; même | Abbreviated opening and short added word. | medium |
| 122 | 30 | last exact sequence | 2n-i+1 &#124; 2n-i-1 | The ink before 1 appears plus-like; mathematical expectation not used to resolve it. | low |
| 122 | 30 | last object | H^{i+1}(W0) | Small crowded exponent. | medium |
| 122 | 30 | short exact sequences and final relative sequence | \mathbin{-}&#124;\longrightarrow | Some short horizontal connectors have no distinct arrowhead; the visible dash is placed first, with an arrow retained as an alternative. | low |
| 122 | 31 | function after norm | nu &#124; v superscript o(1) | Small v-like glyph; superscript is small o, not silently made calligraphic O. | medium |
| 122 | 31 | section 3 base field | mathbb Q &#124; mathbb C | Circular double-stem letter has apparent descending tail; context expectation not used. | medium |
| 122 | 31 | section 3 references | Converse 1.12; Proposition 0.7 | Both labels transcribed as printed. | high |
| 122 | 32 | top cancelled prose | triangle | Last word crosses a heavy strike. | low |
| 122 | 32 | top cancelled formulas | i ne i&#124;1; i=n+1; 2n-i=n-1 | Very compressed unfinished calculation. | low |
| 122 | 32 | left margin | intéressant | Small sloping word. | low |
| 122 | 32 | upper bound | i ge n+1 &#124; n+2 | Bold revised numeral; following parenthesis retained literally. | low |
| 122 | 32 | right margin first | épim si i=n-1 &#124; n | Tiny terminal degree against page edge. | low |
| 122 | 32 | middle prose | H^q &#124; H^* | Superscript resembles handwritten q/asterisk. | medium |
| 122 | 32 | middle sequence | 2n+1 &#124; n+1 | Overwritten exponents and cancelled labels. | low |
| 122 | 32 | lower vanishing | i over deleted n-2; cancelled H^{n-2}(M)=0 | Revised and scribbled-over degree expressions. | low |
| 122 | 32 | bottom first nonzero object | H^{n-1}(M)^vee &#124; H^{n+1}(M)^vee | Overwritten and underlined degree; full diagram cancelled. | low |
| 122 | 32 | bottom faint isolated letter | H | Pencil mark beneath diagram. | low |
| 122 | 32 | upper cancelled endpoint and lower cancelled sequence first object | 2n+1&#124;n+1; n−1&#124;n+1 | The second audit places the ink-favoured readings first; surrounding mathematics has not been used to normalize these degrees. | low |
| 122 | 34 | generic-point subscript throughout | eta &#124; gamma | Loop with long descending stroke; package comparison required. | medium |
| 122 | 34 | condition replacement | i ne 0,2n; deleted +1 | Last cancelled group overwritten. | low |
| 122 | 34 | second brace conoyau | deleted ne | Small overwritten relational sign. | low |
| 122 | 34 | right bracket | demand | Abbreviated or incomplete word before n ge 1. | low |
| 122 | 34 | middle sequence first term | H^{2n}W_eta) | No opening parenthesis visible; retained. | high |
| 122 | 34 | lower right map | xi &#124; bar s | Dense three-stroke subscript, distinct from the clear s at target. | low |
| 122 | 34 | below text left | dash | Isolated ink dash; no readable word. | low |
| 122 | 35 | heading last word | solution &#124; notation | Rapid strokes; solution fits visible opening better. | low |
| 122 | 35 | initial category | ad^n &#124; ad^circ (S,J&#124;I;mathcal A) | Category superscript and second argument uncertain. | low |
| 122 | 35 | after AB5 | fraktur I &#124; fraktur B, S noethérien | Isolated Gothic-looking symbol; its attachment is unclear. | low |
| 122 | 35 | natural finiteness parenthesis | loc noeth | Abbreviated adjective. | medium |
| 122 | 35 | list of systems | fst ann. adiques | Heavily compressed abbreviated group; no expansion in transcription. | low |
| 122 | 35 | dual bracket | dualemt; cc&#124;ad; AB5alpha&#124;star; condns | Several abbreviated words and superscript uncertain. | low |
| 122 | 35 | cancelled example | deleted mathcal A; tel que; M-régulier | Crossing cancellation lines obscure the letter and agreement ending. | low |

## Supplementary enumeration of every `\unsure` occurrence

This table is extracted mechanically from the page fragments. The line number is the physical line in the named `.tex` page, not a manuscript line. Confidence defaults to medium; it is low for a reading inside `\deleted`, or an exact textual match to a manually recorded low-confidence reading. These defaults do not replace the manual judgments above. Nested uncertainty marks each receive their own row.

| Cote | Scan | Page `.tex` line | First reading | Alternatives | Confidence | Basis |
|---|---:|---:|---|---|---|---|
| 122 | 3 | 3 | para | — | medium | default; see manual table where applicable |
| 122 | 3 | 13 | donc | — | low | inside deletion |
| 122 | 3 | 24 | n-i | — | medium | default; see manual table where applicable |
| 122 | 3 | 27 | fibre | fibres | medium | default; see manual table where applicable |
| 122 | 3 | 37 | topologique | — | medium | default; see manual table where applicable |
| 122 | 3 | 49 | l'isom. | — | low | inside deletion |
| 122 | 3 | 49 | à | — | low | inside deletion |
| 122 | 3 | 49 | prendre | — | low | inside deletion |
| 122 | 3 | 49 | entre | — | low | inside deletion |
| 122 | 3 | 51 | \widetilde{\partial P} | — | low | inside deletion |
| 122 | 3 | 51 | \widetilde{\partial P} | — | low | inside deletion |
| 122 | 4 | 15 | < | — | low | manual low-confidence reading |
| 122 | 5 | 13 | \simeq | — | medium | default; see manual table where applicable |
| 122 | 5 | 15 | =P-P' | — | medium | default; see manual table where applicable |
| 122 | 5 | 23 | équivalences | équivalence | medium | default; see manual table where applicable |
| 122 | 5 | 23 | d' | — | medium | default; see manual table where applicable |
| 122 | 5 | 25 | P' | — | medium | default; see manual table where applicable |
| 122 | 5 | 25 | i | — | medium | default; see manual table where applicable |
| 122 | 5 | 26 | \partial P | — | low | inside deletion |
| 122 | 5 | 38 | ? | — | medium | default; see manual table where applicable |
| 122 | 5 | 38 | P' | \mathring P' | medium | default; see manual table where applicable |
| 122 | 5 | 38 | \mathrm{mod} | — | low | inside deletion |
| 122 | 6 | 8 | 3 | 2 | medium | default; see manual table where applicable |
| 122 | 7 | 2 | par | — | low | inside deletion; manual low-confidence reading |
| 122 | 7 | 10 | \alpha | — | medium | default; see manual table where applicable |
| 122 | 7 | 12 | dim | codim | medium | default; see manual table where applicable |
| 122 | 7 | 12 | dim | codim | medium | default; see manual table where applicable |
| 122 | 7 | 14 | précisera | — | low | inside deletion; manual low-confidence reading |
| 122 | 7 | 19 | H^i(W) | — | low | inside deletion |
| 122 | 7 | 19 | H^i(W,F) | — | low | inside deletion |
| 122 | 7 | 25 | R | — | medium | default; see manual table where applicable |
| 122 | 7 | 29 | i | — | low | manual low-confidence reading |
| 122 | 7 | 29 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 7 | 35 | \alpha | — | medium | default; see manual table where applicable |
| 122 | 7 | 37 | en faisant | — | medium | default; see manual table where applicable |
| 122 | 7 | 39 | T | — | medium | default; see manual table where applicable |
| 122 | 7 | 41 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 7 | 41 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 7 | 42 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 7 | 42 | Q | R | low | manual low-confidence reading |
| 122 | 7 | 42 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 8 | 5 | o | 0 | medium | default; see manual table where applicable |
| 122 | 8 | 17 | directe.d'un | directe d'un | medium | default; see manual table where applicable |
| 122 | 9 | 5 | ! | — | low | inside deletion; manual low-confidence reading |
| 122 | 9 | 8 | si | — | low | inside deletion |
| 122 | 9 | 8 | compact | — | low | inside deletion |
| 122 | 9 | 27 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 10 | 17 | o | 0 | medium | default; see manual table where applicable |
| 122 | 10 | 17 | o | 0 | medium | default; see manual table where applicable |
| 122 | 10 | 17 | o | 0 | medium | default; see manual table where applicable |
| 122 | 10 | 17 | o | 0 | medium | default; see manual table where applicable |
| 122 | 11 | 4 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 11 | 4 | \mathcal T | \tau | medium | default; see manual table where applicable |
| 122 | 11 | 10 | ordinaires | — | low | inside deletion; manual low-confidence reading |
| 122 | 11 | 15 | P | — | medium | default; see manual table where applicable |
| 122 | 11 | 20 | S\times T | R=T | low | inside deletion |
| 122 | 11 | 27 | n-i | — | low | inside deletion |
| 122 | 11 | 27 | - | , | low | inside deletion |
| 122 | 11 | 30 | n-i | — | low | inside deletion |
| 122 | 11 | 30 | + | , | low | inside deletion |
| 122 | 11 | 40 | H | — | medium | default; see manual table where applicable |
| 122 | 12 | 2 | W | 11 | low | manual low-confidence reading |
| 122 | 13 | 13 | deux | des | medium | default; see manual table where applicable |
| 122 | 13 | 17 | W | — | low | inside deletion; manual low-confidence reading |
| 122 | 13 | 22 | cptes | — | medium | default; see manual table where applicable |
| 122 | 14 | 11 | -:-:-:- | — | medium | default; see manual table where applicable |
| 122 | 15 | 2 | suppose | — | medium | default; see manual table where applicable |
| 122 | 15 | 2 | communs | — | low | inside deletion |
| 122 | 15 | 4 | On peut | — | low | inside deletion |
| 122 | 15 | 6 | On aura | — | low | inside deletion |
| 122 | 15 | 8 | un | — | low | inside deletion |
| 122 | 15 | 14 | En fait | — | low | inside deletion |
| 122 | 15 | 21 | On a donc | — | low | inside deletion |
| 122 | 15 | 26 | \simeq | 2 | low | manual low-confidence reading |
| 122 | 15 | 26 | 1 | — | medium | default; see manual table where applicable |
| 122 | 15 | 27 | \partial | — | low | inside deletion |
| 122 | 15 | 27 | S^1 | — | medium | default; see manual table where applicable |
| 122 | 17 | 4 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 4 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 4 | V'_s | — | medium | default; see manual table where applicable |
| 122 | 17 | 4 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 14 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 14 | D | — | low | inside deletion |
| 122 | 17 | 14 | \sim | — | medium | default; see manual table where applicable |
| 122 | 17 | 14 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 29 | s | — | medium | default; see manual table where applicable |
| 122 | 17 | 29 | s | — | medium | default; see manual table where applicable |
| 122 | 17 | 29 | \times | — | medium | default; see manual table where applicable |
| 122 | 17 | 29 | T | — | medium | default; see manual table where applicable |
| 122 | 17 | 40 | n+i | — | low | inside deletion |
| 122 | 17 | 58 | \eta | S | medium | default; see manual table where applicable |
| 122 | 17 | 59 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 60 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 60 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 60 | S^1 | — | medium | default; see manual table where applicable |
| 122 | 17 | 61 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 17 | 61 | X'_s | — | medium | default; see manual table where applicable |
| 122 | 17 | 62 | \cdot | — | medium | default; see manual table where applicable |
| 122 | 17 | 81 | -1 | — | medium | default; see manual table where applicable |
| 122 | 17 | 85 | -1 | — | medium | default; see manual table where applicable |
| 122 | 17 | 86 | n-i | — | medium | default; see manual table where applicable |
| 122 | 17 | 89 | relative | — | medium | default; see manual table where applicable |
| 122 | 20 | 4 | (\Gamma,\pi) | — | low | inside deletion |
| 122 | 20 | 4 | * | — | medium | default; see manual table where applicable |
| 122 | 20 | 5 | * | — | medium | default; see manual table where applicable |
| 122 | 20 | 20 | dévolution | — | low | manual low-confidence reading |
| 122 | 20 | 34 | Cohomologie | cohomologie | medium | default; see manual table where applicable |
| 122 | 21 | 4 | \overline{\mathbb G}_m | \mathbb G_m | medium | default; see manual table where applicable |
| 122 | 22 | 7 | a | — | low | inside deletion |
| 122 | 22 | 11 | induit | — | medium | default; see manual table where applicable |
| 122 | 22 | 11 | W_0 | — | medium | default; see manual table where applicable |
| 122 | 22 | 11 | W | — | low | inside deletion |
| 122 | 22 | 15 | aux isos canons aux | — | medium | default; see manual table where applicable |
| 122 | 22 | 15 | \simeq | = | medium | default; see manual table where applicable |
| 122 | 22 | 15 | objets | — | medium | default; see manual table where applicable |
| 122 | 22 | 16 | prouver | — | medium | default; see manual table where applicable |
| 122 | 22 | 16 | donnera | — | medium | default; see manual table where applicable |
| 122 | 22 | 16 | la justif. formelle | — | medium | default; see manual table where applicable |
| 122 | 22 | 16 | une donnée de ce type | — | medium | default; see manual table where applicable |
| 122 | 22 | 30 | \mathbb R\Gamma(\Lambda) | — | low | inside deletion |
| 122 | 24 | 16 | 1 | — | low | inside deletion |
| 122 | 24 | 18 | I | l | low | manual low-confidence reading |
| 122 | 24 | 25 | Et les | — | low | inside deletion |
| 122 | 24 | 27 | donnée | — | low | inside deletion |
| 122 | 24 | 29 | H | K | low | inside deletion; manual low-confidence reading |
| 122 | 24 | 42 | 2n-i | — | low | inside deletion |
| 122 | 24 | 43 | 2n-1-i | — | low | inside deletion |
| 122 | 24 | 47 | 2n- | — | low | inside deletion |
| 122 | 24 | 47 | le | — | low | inside deletion |
| 122 | 25 | 6 | \sim\sim | — | medium | default; see manual table where applicable |
| 122 | 25 | 18 | o | 0 | medium | default; see manual table where applicable |
| 122 | 25 | 20 | - | — | medium | default; see manual table where applicable |
| 122 | 25 | 20 | \overline{\mathbb G}_m | \mathbb G_m | medium | default; see manual table where applicable |
| 122 | 26 | 2 | remarquables | — | medium | default; see manual table where applicable |
| 122 | 26 | 5 | accoupl. | — | low | manual low-confidence reading |
| 122 | 26 | 14 | \(\partial\) | — | low | inside deletion |
| 122 | 26 | 14 | les preuves | — | low | inside deletion; manual low-confidence reading |
| 122 | 26 | 14 | transposées | — | medium | default; see manual table where applicable |
| 122 | 26 | 17 | plus bas | — | medium | default; see manual table where applicable |
| 122 | 26 | 18 | e | — | medium | default; see manual table where applicable |
| 122 | 26 | 18 | d) | — | low | inside deletion |
| 122 | 26 | 24 | 0 | — | low | inside deletion |
| 122 | 26 | 24 | H^{2n+1}(W-W_0) | — | low | inside deletion |
| 122 | 26 | 24 | 0 | — | low | inside deletion |
| 122 | 28 | 13 | conclusion visible de | — | low | manual low-confidence reading |
| 122 | 28 | 15 | supposons | — | low | inside deletion; manual low-confidence reading |
| 122 | 28 | 16 | \(W-W_0\) | — | low | inside deletion |
| 122 | 28 | 18 | W | — | medium | default; see manual table where applicable |
| 122 | 28 | 19 | de plus | — | low | inside deletion |
| 122 | 28 | 27 | 2 | 1 | medium | default; see manual table where applicable |
| 122 | 28 | 28 | -2 | — | low | inside deletion |
| 122 | 28 | 33 | dualité cela s'interprète | — | medium | default; see manual table where applicable |
| 122 | 28 | 35 | ! | — | medium | default; see manual table where applicable |
| 122 | 28 | 35 | 1 | — | medium | default; see manual table where applicable |
| 122 | 28 | 36 | \ge | = | medium | default; see manual table where applicable |
| 122 | 28 | 36 | +1 | — | low | inside deletion |
| 122 | 30 | 4 | n,n+1 | — | low | inside deletion |
| 122 | 30 | 4 | ] | — | low | inside deletion |
| 122 | 30 | 9 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 10 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 11 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 14 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 15 | n+1\ne2n+1 | — | low | inside deletion |
| 122 | 30 | 21 | \Lambda | — | low | inside deletion |
| 122 | 30 | 22 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 26 | passage | — | medium | default; see manual table where applicable |
| 122 | 30 | 26 | les les | — | low | inside deletion |
| 122 | 30 | 27 | - | — | medium | default; see manual table where applicable |
| 122 | 30 | 27 | +1 | — | low | inside deletion |
| 122 | 30 | 29 | +1 | — | low | inside deletion |
| 122 | 30 | 30 | Indépendt | — | medium | default; see manual table where applicable |
| 122 | 30 | 30 | même | — | medium | default; see manual table where applicable |
| 122 | 30 | 33 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 33 | 2n-i | — | medium | default; see manual table where applicable |
| 122 | 30 | 33 | \mathbin{-} | \longrightarrow | low | manual low-confidence reading |
| 122 | 30 | 33 | +1 | -1 | medium | default; see manual table where applicable |
| 122 | 30 | 33 | i+1 | — | medium | default; see manual table where applicable |
| 122 | 31 | 8 | \nu | v | medium | default; see manual table where applicable |
| 122 | 31 | 10 | \mathbb Q | \mathbb C | medium | default; see manual table where applicable |
| 122 | 32 | 2 | triangle | — | low | inside deletion; manual low-confidence reading |
| 122 | 32 | 3 | i | 1 | low | inside deletion |
| 122 | 32 | 4 | i=n+1 | — | low | inside deletion |
| 122 | 32 | 4 | 2n-i=n-1 | — | low | inside deletion |
| 122 | 32 | 5 | intéressant | — | low | manual low-confidence reading |
| 122 | 32 | 7 | 1 | 2 | medium | default; see manual table where applicable |
| 122 | 32 | 10 | n-1 | n | medium | default; see manual table where applicable |
| 122 | 32 | 13 | q | * | medium | default; see manual table where applicable |
| 122 | 32 | 13 | q | * | medium | default; see manual table where applicable |
| 122 | 32 | 13 | n | — | low | inside deletion |
| 122 | 32 | 13 | n | — | low | inside deletion |
| 122 | 32 | 15 | 2n+1 | n+1 | low | inside deletion; manual low-confidence reading |
| 122 | 32 | 15 | \simeq | — | low | inside deletion |
| 122 | 32 | 15 | n | — | medium | default; see manual table where applicable |
| 122 | 32 | 16 | \rho | — | low | inside deletion |
| 122 | 32 | 19 | est | — | medium | default; see manual table where applicable |
| 122 | 32 | 21 | n-2 | — | low | inside deletion |
| 122 | 32 | 21 | H^{n-2}(M)=0 | — | low | inside deletion |
| 122 | 32 | 22 | 2n | — | low | inside deletion |
| 122 | 32 | 27 | n-1 | n+1 | low | inside deletion |
| 122 | 32 | 30 | H | — | low | inside deletion; manual low-confidence reading |
| 122 | 34 | 5 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 34 | 6 | +1 | — | low | inside deletion |
| 122 | 34 | 8 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 34 | 9 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 34 | 9 | \ne | — | low | inside deletion |
| 122 | 34 | 13 | demand | — | low | manual low-confidence reading |
| 122 | 34 | 16 | 0 | — | medium | default; see manual table where applicable |
| 122 | 34 | 16 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 34 | 16 | \eta | \gamma | medium | default; see manual table where applicable |
| 122 | 34 | 24 | \xi | \bar s | medium | default; see manual table where applicable |
| 122 | 34 | 26 | - | — | medium | default; see manual table where applicable |
| 122 | 35 | 2 | solution | notation | low | manual low-confidence reading |
| 122 | 35 | 3 | \operatorname{ad}^{n} | \operatorname{ad}^{\circ} | medium | default; see manual table where applicable |
| 122 | 35 | 3 | J | I | medium | default; see manual table where applicable |
| 122 | 35 | 3 | \mathfrak B | \mathfrak I | medium | default; see manual table where applicable |
| 122 | 35 | 3 | noeth | — | medium | default; see manual table where applicable |
| 122 | 35 | 3 | fst ann. adiques | — | low | manual low-confidence reading |
| 122 | 35 | 3 | dualemt | — | medium | default; see manual table where applicable |
| 122 | 35 | 3 | \mathrm{cc} | \operatorname{ad} | medium | default; see manual table where applicable |
| 122 | 35 | 3 | J | I | medium | default; see manual table where applicable |
| 122 | 35 | 3 | \alpha | * | medium | default; see manual table where applicable |
| 122 | 35 | 3 | condns | — | medium | default; see manual table where applicable |
| 122 | 35 | 5 | \(\mathcal A\) | — | low | inside deletion |
| 122 | 35 | 5 | tel que | — | low | inside deletion |
| 122 | 35 | 5 | $M$-régulier | — | low | inside deletion |

## Abbreviations

Expansions are editorial suggestions only. An uncertain abbreviation remains uncertain; the proposed meaning has not been inserted into the LaTeX text.

| Written form | Tentative expansion / meaning | Scans or setting |
|---|---|---|
| `i.e.` | id est | Throughout, French and English sheets |
| `NB`, `NB.` | nota bene | 020, 022, 026, 028 |
| `cf.` | confer / compare | Reused typescripts |
| `resp.` | respectivement | 006, 012, 013, and other typed exercises |
| `loc`, `loc.` | localement | 003, 026, 035 |
| `const-ts` | constants | 003 |
| `dim` | dimension | 003, 007, 026 |
| `hom`, `hom.` | homomorphisme(s) | 003, 005, 022 |
| `isom`, `isom.` | isomorphisme(s) | Handwritten cohomology sequence |
| `isos` | isomorphismes | Doubtful phrase, 022 |
| `canons` | canoniques, possibly abbreviated; the reading itself is doubtful | 022 |
| `coh.` | cohomologie / cohomologique, according to the phrase | 007, 011, 017, 028 |
| `diff`, `diff.` | différentiable(s) | 013 |
| `cptes` | compactes | 013, uncertain handwriting |
| `inj` | injectif / injection | 028, 034 |
| `surj` | surjectif / surjection | 028, 032 |
| `mono` | monomorphisme | 028, 032 |
| `épim` | épimorphisme | 028, 032 |
| `op.` | opération | 020 |
| `triv` / `triv.` superscript | trivial(e), the trivial action | 020, 022, 024, 026 |
| `oub` superscript | oubli | 024 |
| `ob` | objet(s) | 022 |
| `rel.` | relativement | 022 |
| `justif.` | justification | 022, doubtful margin |
| `accoupl.` | accouplement | 026, uncertain letters at the box edge |
| `p.r. à` | par rapport à | 026 |
| `hyp.` | hypothèse | 026 |
| `ex.tes` | exactes | 026 |
| `sph. coh.` | sphère cohomologique | 028 |
| `tjrs` | toujours | 028 |
| `f.` | faut | 028 |
| `Indépendt` | Indépendant | 030, uncertain ending |
| `loc noeth`, `[noeth]` | localement noethérienne; noethérien | 035 |
| `co. adiques` | coadiques; the punctuation may separate a prefix | 035 |
| `fst ann. adiques` | Expansion unresolved; possibly a compound finiteness/annihilation qualification, but this cannot be established from the visible letters | 035, low confidence |
| `dualemt` | dualement | 035, uncertain abbreviation |
| `condns` | conditions | 035, uncertain abbreviation |
| `chap.` | chapitre | Reused French exercises |
| `§` | paragraphe / section | Reused typescripts |
| `n°` | numéro | Reused French exercises and printed headers |
| `exerc.` | exercice | Reused French exercises |
| `éd.` | édition | Reused French references |
| `prop.` | proposition | Reused French exercises |
| `cor.` | corollaire | 006 |
| `Alg.` | Algèbre | Reused French references |
| `Top. gén.` | Topologie générale | Reused French references |
| `Ens.` | Théorie des ensembles / Ensembles | 010 reference; title expansion is tentative |
| `1-PS` | one-parameter subgroup | 031 |
| `EGA` | Éléments de géométrie algébrique | 027; acronym retained in the text |
| `MV`, `MV_!` | Mayer–Vietoris notation | 011 recap; mathematical labels, not expanded |

The prefixes and symbols `ad`, `cc`, `AB 5`, and its superscripted variant on scan 035 are retained as uncertain mathematical nomenclature rather than expanded into definitions not present on the sheet.


## Legibility and limits

All 32 kept whole-page images and their two supplied halves were inspected directly, in scan order, without OCR. Each page was saved separately with an inventory before proceeding, and every page received a later image-against-text audit. The context archive remained unopened during those readings and during the cross-page notation comparison.

The reused French and English typescripts are generally much more legible than the handwritten argument, although their handwritten mathematical additions, overtyped letters, tiny indices, and literal repetitions still require care. Repeated or surprising printed wording has been retained, including the repetition on scan 010, “projection embeddings” and “be v_j be” on scan 027, and the Q/C ambiguity on scan 031. Their presence does not justify using an external edition to change the transcription.

The least secure passages are the cancellations at the ends of scans 003 and 005; the rotated, crossed-out margin in scan 011; the small labels and crowded pencil overlays in the two large lattices of scan 017; the oblique margin and last phrase of the upper paragraph on scan 022; the overwritten exponents and abandoned arrow on scan 024; the heavily cancelled endpoint calculation on scan 026; the revised inequalities and boxed side note on scan 028; the short connectors and final dual degree on scan 030; the numerous overwritten degrees and entirely cancelled last sequence on scan 032; and the category notation, abbreviations, and cancelled example on scan 035. These parts should receive priority in any subsequent human collation. The uncertainty macros provide actual proposed readings, not placeholders for omitted material.

A confidence label describes the reading of the ink, not the truth of a mathematical assertion. “High” in the manual table can record a resolved earlier doubt; “medium” is a plausible but not secure reading; “low” marks substantial ambiguity or cancellation. The supplementary table exhaustively locates every uncertainty macro by its physical line in the page `.tex` file and explains its mechanical confidence default. Its defaults should not override the fuller local explanation in the manual table.

Diagrams are represented by TikZ-cd objects, connectors, labels, and directions. The drawing geometry in the collar pictures and Figures 7 and 8 is a hand-coded TikZ approximation of the visible curves, regions, rulings, and labels; it is not a pixel facsimile. Large diagrams and marginal matter may require a generous page size or suitable layout definitions in the receiving edition. The LaTeX deliverable is the requested fragment, with no preamble and no definitions of the editorial macros. A host document must provide those macros, the standard mathematical packages, TikZ/TikZ-cd, `ulem` for the underlines, and TikZ's `shapes.geometric` library for the elliptical outlines. Editorial wrappers must accept both text and mathematical/block material, including a deleted whole diagram; a text-only strikeout definition is insufficient. Some `\diagram` contents are mathematical arrays or boxed expressions and need a math-aware wrapper.

The structural checks cover balanced groups and environments, allowed editorial macro names, page ordering, exact concatenation, inventory coverage, and diagram grid destinations. A full TeX rendering was not possible in this environment because the installed engines lacked the LaTeX formats and required package files. Thus the output has been source-checked and visually collated against the scans, but it has not been certified by a successful full compilation. No mathematical repair, external text, or later context has been substituted for the ink.

