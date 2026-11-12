# Shared notation and transcription encoding

This table is an encoding convention, not permission to infer an unread sign. Every occurrence must be checked against its own ink. An unresolved distinction stays in `\unsure{reading|alternative}`; do not harmonize distinct manuscript forms.

| Visible form | LaTeX | Reading discipline |
|---|---|---|
| Ordinary Latin capitals and lower case | `A`, `B`, `E`, `F`, `u`, `n` | Preserve case; explicitly mark ambiguous E/F, u/n, 1/l. |
| Clearly calligraphic capitals | `\mathcal{A}`, `\mathcal{O}`, `\mathcal{F}` | Do not silently make an ordinary letter calligraphic. |
| Clearly Gothic letters | `\mathfrak{a}`, `\mathfrak{m}`, `\mathfrak{X}` | Mark uncertainty between Gothic/script/plain at each unresolved occurrence. |
| Bold/double-struck alphabets | `\mathbf{A}`, `\mathbb{Z}` | Use only if the strokes support the distinction. |
| Greek letters | `\alpha`, `\beta`, `\gamma`, `\delta`, `\epsilon`, `\varphi`, `\psi`, `\omega`, `\Omega` | Preserve variant shapes when distinguishable. |
| Exclamation exponent | `^{!}` | Never replace with a prime; inspect dot and stem. |
| Prime / double prime | `'`, `''` | Never replace with exclamation. |
| Superscript circle / bullet / star | `^{\circ}`, `^{\bullet}`, `^{*}` | Distinguish from zero and multiplication. |
| Hats, bars, tildes, underlines | `\widehat{X}`, `\overline{X}`, `\widetilde{X}`, `\underline{X}` | Keep extent of decoration, as far as ink permits. |
| Ordinary arrows and plain dashes | `\longrightarrow`, `\longleftarrow`, `-` | Add an arrowhead only if visible. |
| Injection/surjection/iso decorations | `\hookrightarrow`, `\twoheadrightarrow`, `\xrightarrow{\sim}` | Direction and decorations from ink, not mathematics. |
| Equality/inequalities/inclusions | `=`, `\ne`, `\le`, `\ge`, `\subset`, `\subseteq`, `\supset` | Preserve strictness and direction. |
| Paired handwritten double quotation marks | two backticks and two apostrophes, e.g. ` ``mot'' ` | Use guillemets only when genuine guillemets are visible. |
| Abbreviations | literal letters and punctuation, e.g. `cat.`, `gr.`, `resp.`, `cf.`, `th.`, `prop.`, `dém.`, `mb.` | Never expand in transcription. Record tentative expansion in doubts only. |
| Underlining / double underlining in prose | `\uline{...}`, `\uuline{...}` | Preserve exact underlined extent. |
| Readable deletion | `\deleted{...}` | Check every word for strike-through before treating it as live. |
| Insertion / independent marginal note | `\inserted{...}`, `\margin{...}` | Locate insertion at its visible caret or link. |
| Diagrams / tables | `\diagram{\begin{tikzcd}...\end{tikzcd}}` / `\diagram{\begin{array}...\end{array}}` | Every object, direction, decoration and label; uncertainty inside diagram. |
| Non-diagram drawings | `\figure{\begin{tikzpicture}...\end{tikzpicture}}` | Reproduce geometry and labels; no verbal substitute. |
| Uncertain words or signs | `\unsure{reading}` or `\unsure{reading|alternative}` | First reading is the visible ink, not a correction. |
| Physically unreadable words | `\illegible{n}` | Only after visual zoom and attempted reading; never for mathematical symbols. |
| Page state | `\cotefile{C}`, `\scanpage{N}`, `\mspage{n}` | Archive cote only at first page; own manuscript number only when visible. |

## Cross-page readings checked against the images

The initial encoding table above was shared before page work began. The following entries record the visual reconciliation undertaken during the independent audit, before the transcription freeze; agreement means agreement about the visible form, and does not erase a change made in the manuscript.

| Recurring sign or form | Encoding retained | Evidence and limits |
|---|---|---|
| Exclamation as an upper or lower index | `f^{!}`; `\alpha_{!}`, `\beta_{!}`, `\omega_{X!}` where placed below | The duality letter 5/050 has an exclamation exponent, whereas the adjoint notation 5/019–020 puts the exclamation below. Neither is encoded as a prime. |
| Closed oval crossed by a stem | `\phi` | The cancelled symbol 6/010, filtration symbol 6/024 and p-divisible-group symbol 6/031–032 were compared visually and use the same glyph encoding, without identifying their mathematical roles. |
| Open curled phi with a descending side stroke | `\varphi` | The handwritten forms 5/017,028 and043 were compared and are visibly distinct from the preceding closed-oval form. Printed forms on 5/004 and036 are preserved as printed. |
| Two-lobed epsilon | `\varepsilon` | The occurrences on 5/004 and036 and the four occurrences on 5/044 share this form; a contextual meaning is not used to select a variant. |
| Very short wavy m beneath a horizontal bar | `\overline{\mathrm m}` in math mode, locally under `\unsure` when needed | Independently compared on 5/016,5/020 and 6/037. The abbreviation is not expanded in the transcription; its possible expansion appears only in the abbreviation list. |
| m with a small raised me | `m\textsuperscript{me}`, within `\unsure` | The circled annotation 6/027 has a different visible construction from the preceding overbarred abbreviation. |
| Looped category letter | `\mathcal L`, with local alternative `\mathcal Q` | The same recurrent letter 5/017–020 is treated consistently; the uncertainty is retained instead of inferred from a category-theoretic name. |
| Handwritten ideal decorated by a flat/b-like superscript | `J^{\unsure{\flat|b}}` | The symbol 5/025 is kept distinct from an ordinary star or plus; further rejected or weaker readings are retained in the doubts table. |
| Divided-power operator with upper/lower n | `\pi^n` and `\pi_n` at their respective places | The explicit alteration of upper indices to lower indices on 5/039 is preserved locally. It does not license changing the earlier definitions or every later occurrence. |
| Gamma versus pi and dotted versus plain Theta | `\Gamma`, `\pi`, `\dot\Theta`, `\Theta` | These are separately inspected letters/decorations in the divided-power calculations, especially 5/005–009 and032–043. No general substitution is imposed. |
| Plain/underlined typewriter letters | `O`, `\underline O`, `M`, `\underline M`, `Z`, `\underline Z`, and the corresponding local forms | The typewritten crystal discussion does not automatically become calligraphic or double-struck notation. Visible underlining is retained. |
| Wavy under-decoration in the handwritten divided-power notation | `\underset{\sim}{M}` and analogous standard LaTeX constructions | The wavy stroke under M or Gamma on 5/022–023 is not replaced by a straight underline or an overhead tilde. |
| Dual, star and prime | `^{\vee}`, `^{*}`, and `'` | In 6/031 the prose and the following sequence differ in the visible dual sign; in 6/032 the rank has g-prime while the filtration type has g-star. Both differences are retained. |
| Unheaded or thick-ended connector | Literal dash or dash-first `\unsure` inside the formula/diagram | The lower marginal sequence 6/034 and the kernel expression 5/028 are not given a confident arrowhead from the expected mathematics. |
| Two visible foliation systems | `\mspage` for the manuscript folio; `\margin` for an additional marginal number whose status is uncertain | Both numbers and their positions are retained where present. The distinction records visible placement and uncertainty; it does not assert the authorship of every numeral. |

All quotation marks used as source quotation marks follow the two-backtick/two-apostrophe convention, except where the source itself supplies another sign. Quotes required internally by TikZ arrow-label syntax are code, not extra source punctuation. The notation table and the doubts record belong to the transcription apparatus; the later literature comparisons belong exclusively to the research notes.


# Doubts by page

| File | Scan page | Approximate line / location | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
| 5 | 3 | diagram upper side objects | conn | com; connection-site abbreviation | medium |
| 5 | 3 | diagram P-labelled objects | \mathbb{P} | P in bold rather than double-struck | medium |
| 5 | 3 | first prose paragraph | gerbienne | galoisienne; confidence qualification: medium; independent visual reread supports gerbienne, but cursive remains compressed | medium |
| 5 | 3 | first paragraph end | intéressantes | word ending compressed | medium |
| 5 | 3 | last paragraph Chern superscript | 1 | prime | medium |
| 5 | 3 | last line deletion | disons | d’un | low |
| 5 | 3 | last paragraph verb subject | on | short faded stroke can resemble a dash | low |
| 5 | 5 | first paragraph deleted phrase | sur [uncertain]; algèbres sur | first short overwritten fragment unresolved; algèbres sur supported by zoomed g descender and b ascender; confidence qualification: medium for algèbres sur, low for initial fragment | low |
| 5 | 5 | second paragraph parenthesis | Cohen | compressed proper name | medium |
| 5 | 5 | second paragraph ideal | mathfrak m_Lambda | mathfrak m Lambda | medium |
| 5 | 5 | W^(nu) final relation deletion | p | overwritten symbol before lambda_0 | low |
| 5 | 5 | bracket first deletion | anneau avec idt | last abbreviation uncertain | low |
| 5 | 5 | middle cancelled parenthesis | c’est un vrai anneau de; mettre\|enlever la relation; qui | heavy cross-out obscures connected words | low |
| 5 | 5 | bottom paragraph | langage | compressed middle letters; possible abbreviation | medium |
| 5 | 6 | proof expanded sum upper bound | p−1 | p; a separate short 1-like stroke is visible after the thick p, while the minus is not cleanly separated | medium |
| 5 | 6 | inserted binomial coefficient | C_i^p | C_alpha^p disfavored by independent zoom: dot and hooked i visible | high |
| 5 | 6 | cancelled constant RHS | lambda_i+1 | Theta_i+1 overwritten | low |
| 5 | 6 | sentence after expansion | p_i | p^i is mathematically expected but i is visibly below the p shoulder | high |
| 5 | 6 | deletion before trivial | c’est le | compressed cancelled words | low |
| 5 | 7 | proof after cond. | deleted de | short overwritten word | low |
| 5 | 7 | corollary theta decoration | dot Theta | small mark is clear but could be image notation stroke | medium |
| 5 | 8 | condition a cancellation | alpha,1≤alpha≤nu−r,pour un | last two words heavily crossed out | low |
| 5 | 8 | small cancellation after inserted multi-index | si | one overwritten short word | low |
| 5 | 8 | corollary E_i cancellation | −r | struck subscript/suffix | low |
| 5 | 8 | mark following W^(nu,r) in quotient isomorphism | looped pen mark reproduced graphically | possibly canceled question mark or unfinished sign; no secure semantic reading | low |
| 5 | 9 | upper cancelled black bar | 5 physically obscured words | solid ink prevents letter recovery | low |
| 5 | 9 | upper cancelled proof | donc | word after a_i≥p compressed | low |
| 5 | 9 | lemma b_nu condition | qq. | qque; quelconque written in shortened form | low |
| 5 | 9 | proof middle cancellations | par sum a_i, puis tous a_i tels; Donc pour sum a_i, si on a | dense intersecting deletions and insertions; provisional readings | low |
| 5 | 9 | proof live connector | Si nous | Si ...; letters compressed | low |
| 5 | 9 | power reduction exponents | a_i prime and alpha_i | q_i may have been intended, but a_i prime visible | medium |
| 5 | 9 | bottom cancellation | multiple de Lambda_nu^p | overwritten curved cancellation | low |
| 5 | 9 | lower carry identity underlining | long line and shorter second line | exact relation to adjacent factors is approximate; strokes end before right-hand equality | medium |
| 5 | 10 | folio beside 34 | 9 in original scan orientation | 6 when the upside-down typescript is rotated upright; number recorded with orientation uncertainty; confidence qualification: high for visible shape, medium for intended orientation | medium |
| 5 | 11 | top superscript cancellation | mu+1 | small crossed superscript | low |
| 5 | 11 | top underbrace cancellation | p^(mu+1) | overwritten symbol | low |
| 5 | 11 | bottom stray symbol between summands | arrow | crossed plus or short word | low |
| 5 | 11 | two strokes connecting lower boxes | parallel oblique strokes | no secure mathematical meaning assigned; confidence qualification: high for geometry | high |
| 5 | 12 | deleted typed word after à | l’infini | overtyped cancellation obscures letter sequence | medium |
| 5 | 12 | xi subscript | 0 | letter o typographically indistinguishable | medium |
| 5 | 13 | top insertion | resp. >0 | small cursive initial word | low |
| 5 | 13 | top text | tout | compressed cursive strokes | medium |
| 5 | 13 | crossed middle line | fonction décroissante de n, tjs <=1 | cancellation passes through each word | low |
| 5 | 13 | left isolated mark | q/6 | ne; abandoned pen mark | low |
| 5 | 13 | digit-sum notation | chif, chiff | one/two f strokes vary and are kept locally | medium |
| 5 | 13 | after (p-1)nu | deleted +1 | heavily overwritten mathematical sign | low |
| 5 | 13 | second Si line | on trouve | on a | low |
| 5 | 13 | word at final box upper left | condition | cancellation obscures ending | low |
| 5 | 13 | right-hand digit argument after si a_nu ne0 | on trouve | on a; long cursive group with t ascender favors trouve | medium |
| 5 | 13 | small isolated stroke below chif(n)≤1 | c | abandoned pen mark | low |
| 5 | 14 | l.48 entry | encore, encore | compressed strokes; latter word may differ | low |
| 5 | 14 | long diagonal strokes | drawn without semantic expansion | cancellation versus completion marks | medium |
| 5 | 14 | last line bibliographic instruction | bibliographie | bibliogr.; terminal strokes highly compressed, abbreviation cannot be excluded | medium |
| 5 | 15 | single heading top right | Frobeniuseries | Frobeniuscria; ending compressed | low |
| 5 | 16 | title | General non-sens | General non-sens, no clearly written accent | medium |
| 5 | 16 | deleted qualification after conditions | en degré convenable | ending of convenable partly crossed | medium |
| 5 | 16 | (1.2) and following formula | plain dash | arrowhead not visible | medium |
| 5 | 16 | (1.3) crossed opening symbol | c_E | F_E; overwritten | low |
| 5 | 16 | deleted prose | on le fait | ending heavily crossed | low |
| 5 | 16 | bottom right | underlined d’où | possibly cancellation stroke | low |
| 5 | 16 | abbreviated même | overbarred m-shaped stroke | même is its contextual expansion; full letters are not written | medium |
| 5 | 17 | initial display and F_E definition | plain dash | arrowhead not visible | medium |
| 5 | 17 | recurring category letter | calligraphic L | calligraphic Q | medium |
| 5 | 17 | crossed line before oubli | Prop. vers X et X′ sont | cancellations conceal short words | low |
| 5 | 17 | label on forgetful arrow | can | ens; short overwritten label | low |
| 5 | 17 | Homtop argument after composés | X | X′ | medium |
| 5 | 17 | final Homtop target argument | X | Y; thick overwritten strokes | low |
| 5 | 17 | insertion des | both inserted des and base-line des retained | one may be intended as replacement without crossing | medium |
| 5 | 17 | morphism glyph in inserted couple and lower paragraph | varphi, with open left curl and descending right stem | phi would suggest closed oval pierced by central stem; the open curl is visible | medium |
| 5 | 18 | Giraud conditions | a) b) c) | small letter forms | medium |
| 5 | 18 | forgetful functor in first paragraph | omega | omega*; no distinct star visible | medium |
| 5 | 18 | middle cancelled block | considère une catégorie; associé aux changts de base u | multiple strokes and displaced inserted replacement | low |
| 5 | 18 | word after cancelled block | remarque | compressed final strokes | medium |
| 5 | 18 | lower cancelled opening | Pour le cas où | Pour que le cas où | low |
| 5 | 18 | final diagram interior | two northeast arrows | xi psi labels; heads are visible | low |
| 5 | 18 | parallel beta/mu strokes | dash without arrowhead | arrow intended but not drawn | medium |
| 5 | 18 | after résultat | five short separated wavy strokes, represented ..... | voulu; no visible tall l, word reading remains uncertain | medium |
| 5 | 18 | lower curved v stroke in first diagram | headless curve | possible rounded arrowhead; unlike upper u arrow, no distinct point is visible | medium |
| 5 | 18 | isolated stroke to right of bottom diagram | a | u or abandoned pen mark | low |
| 5 | 19 | deletion after qu’on | expl | exp; partly completed word | low |
| 5 | 19 | after établir que | deleted de | short overwritten stroke | low |
| 5 | 19 | after acyclique | deleted en | one short illegible-looking word; en is best reading | low |
| 5 | 19 | small marks after transitivité comma | ellipsis | interrupted pen strokes; three faint separate marks before rendant | medium |
| 5 | 20 | abbreviated même | overbarred m-shaped stroke | même is its contextual expansion; full letters are not written | medium |
| 5 | 21 | first heading abbreviation | Th | Alg; two tall stems, no distinct g descender; first letter overwritten | low |
| 5 | 22 | opaque cancellation in 1.2 | sum symbol | overwritten beyond certain reconstruction; mathematical best reading only | low |
| 5 | 22 | number before ter | 1.5.ter | 1.7.ter; digit overwritten | low |
| 5 | 22 | cancelled exponent after pi^n(x) | n | m; dense crossing | low |
| 5 | 22 | cancelled symbols before x^n | n! | several compact strokes | low |
| 5 | 22 | bottom opening word | Que | Si; heavy retracing obscures first looped letter | low |
| 5 | 22 | definition arrow | wavy right arrow without initial bar | mapsto would add an absent vertical bar | high |
| 5 | 23 | (1.6) extra exponent after parenthesis | n | visible short stroke above closing parenthesis; may be displacement | low |
| 5 | 23 | (1.6) x domain | D | J overwritten | low |
| 5 | 23 | two cancelled prose lines | dit que la structure à puissances divisées; compatible; scalaires | central two words physically obscured after enlarged inspection | low |
| 5 | 23 | wave under functor notation | underscript tilde on M and Gamma^{np}(M) | wavy underline | high |
| 5 | 23 | inserted polynomial notation quote | opening double quotation mark | ditto-like paired strokes; no closing mark evident | low |
| 5 | 23 | wavy element arrows | rightward wavy arrows | initial vertical bar is not separately distinguishable from the first turn of the shaft | medium |
| 5 | 24 | line 5 exponent | + | * | medium |
| 5 | 24 | line 9 | dernier joue | compressed cursive; no firm alternative | medium |
| 5 | 24 | line 16 | fonct. | homs / objet | low |
| 5 | 24 | line 16 deletion | anneau | struck through | low |
| 5 | 24 | lines 17–last ideal letters | I | J | medium |
| 5 | 24 | line 18 deletion | n∈N* | n∈N | medium |
| 5 | 24 | line 19 deletion | i | unresolved overwritten small sign | low |
| 5 | 24 | audit: tel ... universel | fourbi | fonct.; visible dot above final i and looping b favour fourbi | medium |
| 5 | 24 | audit: last Gamma argument | J | I or N; dense overwritten glyph has N-like inner strokes | low |
| 5 | 25 | top deleted word | cet | ce | low |
| 5 | 25 | quotient and domain of α, superscript | + | * / overwritten sign | low |
| 5 | 25 | x to x′ notation | ∼ | arrow with absent head | medium |
| 5 | 25 | struck first line pair | (a,X) | (a,x) | low |
| 5 | 25 | after struck second line | je gue. | unresolved compressed wording | low |
| 5 | 25 | N.B., A to Γ connection | - | arrow without discernible head | medium |
| 5 | 25 | audit: superscripts on J in quotient and alpha domain | flat or b | plus or star; enlarged ink has a descending stem and a small right loop | medium |
| 5 | 25 | audit: Greek letter in deleted calculation | zeta | xi; long descending hook favours zeta | medium |
| 5 | 26 | top deleted initial | M | A | low |
| 5 | 26 | isomorphism, RHS exponent | + | * | medium |
| 5 | 26 | above à puissances | de Λ-anneau | deleted overwritten words | low |
| 5 | 26 | Sym augmented, exponent | + | * | low |
| 5 | 26 | bracket paragraph morphism notation | deleted (A,J) → (A′′,J′′) | first pair may be live and overwritten | low |
| 5 | 26 | target phrase universelle | universelle | universel | medium |
| 5 | 26 | sum deletions | λ_i, λ | overwritten coefficients | low |
| 5 | 26 | last sentence | trouve | forme | medium |
| 5 | 26 | audit: source pair in morphism | (A,J) live, heavily overwritten | the arrow shaft begins through the J but no separate cancellation of the whole pair is visible | high |
| 5 | 26 | audit: mark above diagonal margin instruction | §1 | overwritten reference sign with separate underline | low |
| 5 | 27 | first vanishing display cutoff | n | m | medium |
| 5 | 27 | deleted sign before first display | (x) | unresolved struck symbol | low |
| 5 | 27 | line of deleted nilpotentes | nilpotentes | nilpotent | medium |
| 5 | 27 | log sum lower bound | n>0 | n≥0 | medium |
| 5 | 27 | log sign exponent | n | no −1 visible; should be independently checked | high |
| 5 | 28 | insertion replacing triplets | quadruples | quadruplets | medium |
| 5 | 28 | deleted tuple Greek | φ | ρ | medium |
| 5 | 28 | deleted phrase after faisceau | de | d’ / unfinished | low |
| 5 | 28 | parenthetical name of site | stratifiant | strictifiant | medium |
| 5 | 28 | upper left diagram U′ to U | arrow U′→U | direction seems opposite to later i; kept from ink | high |
| 5 | 28 | audit: kernel formula connecting O sheaves | plain dash with round terminal dot | right arrow; no separate arrowhead resolves at enlargement | medium |
| 5 | 28 | canceled original tuple, phi variant | varphi: open left bowl, small closed right loop, descending right stem | closed-oval phi rejected after enlarged visual comparison | high |
| 5 | 29 | crossed draft above diagram | DR(X) | overwritten expression not securely resolved | low |
| 5 | 29 | first paragraph | formt. | formellement abbreviated by superscript t | medium |
| 5 | 29 | before Cris(X) | ces | les | low |
| 5 | 29 | spectral sequence cosimplicial index | ν | p | medium |
| 5 | 29 | audit: leftmost canceled draft object | tilde X with DR subscript | tilde Zar(X); lower strokes resemble DR/Zar and upper symbol is heavily crossed out | low |
| 5 | 29 | audit: spectral-sequence index in two occurrences | nu | gamma or p; ink has a descending loop, marked locally in both occurrences | medium |
| 5 | 30 | upper middle | fonct. | foncteur | medium |
| 5 | 30 | deleted start of bracket | ainsi on | unresolved crossed words | low |
| 5 | 30 | notation adjective | doublement | doublement compressed | medium |
| 5 | 30 | underbrace deleted prefix | ind | unresolved overwritten prefix | low |
| 5 | 30 | underbrace last line | vers | avec | medium |
| 5 | 30 | first limit RHS | Δ without tilde | tilde not visible on first RHS | high |
| 5 | 30 | audit: le ... augmenté | fourbi | fonct.; f-ou-r-bi shape matches the enlarged ink, final i dot visible | medium |
| 5 | 30 | audit: augmentation target O | plain O | no separate underline visible, unlike source O and final O_X | high |
| 5 | 30 | audit: augmentation target argument and repeated underbrace argument | 0 | omega; both have an open double-humped shape | medium |
| 5 | 30 | audit: lower X exponent | 2nu+1 | nu+1 with stray leading stroke; a distinct 2-like glyph precedes nu, unlike the top line | medium |
| 5 | 31 | middle display decoration | tilde over hat over X^(ν+1)_/X | extent of stacked decorations | medium |
| 5 | 31 | middle display terminal parentheses | three closing parentheses | only two openings clearly visible | high |
| 5 | 31 | last display RHS H | double-stroked H | bold H | medium |
| 5 | 31 | audit: first upper Hq closing delimiter | square bracket | round parenthesis; ink is nearly vertical with short lower foot | medium |
| 5 | 31 | audit: middle display terminal parentheses | two closing parentheses | enlarged source shows two, matching the two visible openings; prior count of three corrected | high |
| 5 | 31 | audit: middle display decoration extent | hat over X^(nu+1), /X beneath | tilde spans the hatted expression | high |
| 5 | 32 | top arrow A to B | u over dash | u over arrow | medium |
| 5 | 32 | formal-generator index | x∈J | x∈I | medium |
| 5 | 32 | formal generator rewritten x | Γ_x^n changed to Γ^n(x) | overwritten x position | low |
| 5 | 32 | deleted iterate coefficient | (mn)!/[n!(m!)^n] | denominator heavily crossed | medium |
| 5 | 32 | scalar relation side condition | x∈I, y∈A | ink preserved although roles look reversed | high |
| 5 | 32 | deleted middle sentence | Supposons que + 5 unreadable words | two horizontal strokes obscure text | low |
| 5 | 32 | large deletion | several local tentative readings; 2 obscured words | crosshatching and overwritten ink | low |
| 5 | 32 | valuation argument | n | n! not visible | high |
| 5 | 32 | valuation sum exponent | ν | i | medium |
| 5 | 32 | bottom deleted coefficient | γ^n(x)/n!, a | dense overstriking | low |
| 5 | 32 | audit: canceled iterated-Gamma relation | outer n and inner m | outer m and inner n; crosshatching crosses both superscripts and denominator | low |
| 5 | 32 | audit: subscript of Gamma in large deleted block | A | Lambda; triangular glyph has no securely separate crossbar | low |
| 5 | 32 | audit: mark left of relation brace | où | overwritten short word or opening bracket with letters; kept locally | low |
| 5 | 33 | polynomial algebra deleted prefix | Γ | unresolved single overwritten symbol | low |
| 5 | 33 | relation product exponents | p^m, p^n | overwritten m/n letters | medium |
| 5 | 33 | first marginal question | ne faut-il en passer par les | ne faut-il pas poser les | medium |
| 5 | 33 | second margin opening | il suffit de ? en poser | possibly il suffit d’en poser | low |
| 5 | 33 | bottom after aussi deletion | un | curved overwritten stroke | low |
| 5 | 34 | top product | ∏_i m_i q_ai | m_i printed on baseline, not exponent | high |
| 5 | 34 | subscripts throughout | o | 0 | medium |
| 5 | 34 | before Z_o(A) in lower paragraph | no membership sign visible | possible typescript omission | high |
| 5 | 34 | dual page numbers | typed 41 and handwritten 33 | both retained as page numbers | high |
| 5 | 34 | definition of ξ_o, final q^{-1} | plain q | underlined q; no separate underline is visible in the enlarged image | high |
| 5 | 35 | top second relation deletion | x^nΓ^n(λx)−y^nΓ^n | several symbols obscured by crossing stroke | low |
| 5 | 35 | NB after λx | car; deleted on a | compressed faint words | low |
| 5 | 35 | NB final product | Γ^n(λx)Γ^m(λy) | m,n reversed possible | medium |
| 5 | 35 | polynomial algebra coefficient letter | A | Λ; visibly uncrossed capital | medium |
| 5 | 35 | boxed formula left exponent | p+a | p^a; heavily overwritten | low |
| 5 | 35 | boxed formula crossed expression | Γ^{p^{ν+1}} (a+b)! / | underlying indices obscured | low |
| 5 | 35 | boxed formula numerator and terminal exponent | a p^{ν+1} | e p^{ν+1}; initial letter overwritten | low |
| 5 | 35 | range below box | p≤e<2p−1 | p≤e≤2p−1 | medium |
| 5 | 35 | NB after λx | ici | car; the first thin vertical and final short stroke favor ici | medium |
| 5 | 35 | lower repeated product relation, numerator | (m+n)! | (m+n!; the closing parenthesis and terminal factorial stem are merged/unclear | medium |
| 5 | 36 | opening m subscript | m_o | m_0; typewriter round glyph | medium |
| 5 | 37 | first ring generator after [[x]] | Y | X; heavily retraced strokes | medium |
| 5 | 37 | local algebra hypothesis deletion | Artinien | possibly only part struck; letters overwritten | low |
| 5 | 37 | reference date connector | ou | à | medium |
| 5 | 38 | blackened word before normal | noethérien | substantial typewriter strokes obscured | low |
| 5 | 38 | blackened word after termine | alors | last letters partially visible | low |
| 5 | 38 | blackened word after élémentaire | illegible{1} | no secure letter sequence after enlarged inspection | low |
| 5 | 38 | slash between est and intègre | inserted / | possibly proofreading separation mark rather than textual slash | medium |
| 5 | 39 | heading adjective | égales | positives | low |
| 5 | 39 | crossed display below heading | (x^{(n)})^{(m)}= | first upper index heavily retraced | medium |
| 5 | 39 | a expression before binomial | π^m | blackened incomplete symbol | low |
| 5 | 39 | valuation c_n first factorial argument after −pν_p | n! | m! | medium |
| 5 | 39 | systematic cancelled superscripts | (m),(n),(m+n); m,n,mn,pm,p | some cancellation strokes obscure exact parenthesis bounds | medium |
| 5 | 39 | first c_n valuation line, factorial argument after −pν_p | m! | n!; enlarged letter has two humps, although neighboring lines use n | medium |
| 5 | 40 | embedding example l_p glyph | l_p | 1_p; typewriter glyph ambiguous | medium |
| 5 | 40 | sequence-space subscripts | c_o | c_0; typewriter round glyph | medium |
| 5 | 40 | after l’espace in norm claim | comma before c_o | possibly an incidental mark, retained as visible | medium |
| 5 | 41 | top addition summand y exponent | i | no p− is visible; intended p−i would be conjectural | medium |
| 5 | 41 | top summand deleted coefficient | C_i^p | small blackened symbol | low |
| 5 | 41 | question deleted word | premières | first and middle strokes obscured | low |
| 5 | 41 | large deletion first verb | construira | construit | medium |
| 5 | 41 | large deletion connection before satisfaire | de façon à | compressed partly crossed words | low |
| 5 | 41 | large deletion references | 1.4 for mn<N, 1.5 for m+n<N | first final digit overwritten | medium |
| 5 | 41 | large deletion after N′+ | p | crossed one-letter stroke | medium |
| 5 | 41 | question final π upper index | (p) | p overwritten; parentheses faint | medium |
| 5 | 41 | crossed induction block, bracketed axiom restrictions | les 1.4 ... les 1.5 | first final digit heavily retraced; 1.5 is a local alternative | medium |
| 5 | 42 | groups in item 8-9 | k^{p,q}(X) | K^{p,q}(X); first glyph appears lower case | medium |
| 5 | 42 | parenthesis the - complex | blank space before hyphen | no mathematical symbol visible; no expansion supplied | high |
| 5 | 43 | polynomial coefficient map connector | plain long dash | no secure arrowhead visible; intended arrow possible | medium |
| 5 | 43 | large identity second constraint first q subscript | 1 | 2 | medium |
| 5 | 43 | large identity last constraint q subscript | r,s_r | r,i_r | medium |
| 5 | 43 | large identity rightmost argument at page edge | x_{r,s_r} | part cropped at right; closing parenthesis not visible | low |
| 5 | 43 | margin abbreviation | argts | arguments | medium |
| 5 | 43 | margin replaced verb | remplacé | compressed cursive partly intersecting brace | medium |
| 5 | 43 | last line before réciproque | une | aussi | low |
| 5 | 43 | opening map, marks below M and N | under-tildes | clear wavy marks in enlarged image | high |
| 5 | 43 | coefficient-map row, first M decoration | under-tilde | underline; weaker undulation than in header | medium |
| 5 | 43 | coefficient-map row, connector before N | arrow | plain dash; a small raised triangular terminal stroke is visible | medium |
| 5 | 44 | c second occurrence v_1cos | no θ after cos | visible blank retained; not supplied from first formula | high |
| 5 | 44 | last paragraph signature ordering | type (q,p), group O(p,q) | both orders clearly visible; no harmonization | high |
| 5 | 44 | associated bundle product | typed x with subscript Spin(p,q) | not replaced by a different multiplication glyph | high |
| 5 | 45 | small cancellation in list of elements | et | very short black overstrike | low |
| 5 | 45 | canceled block sign after si | dagger-like mark | cancellation or aborted letter, not secure mathematical dagger | low |
| 5 | 45 | canceled block right-hand monomial | π^(n)z^n | y^n would fit independence argument but ink reads z | high |
| 5 | 45 | brace label and later reference | α | a | medium |
| 5 | 45 | ideal name in insertion | I=πA | opening and later membership use J | high |
| 5 | 45 | abbreviation after choix de y | t.q. | d.q. | medium |
| 5 | 45 | deleted word example 1 | premières | horizontal overstrike obscures letter middles | medium |
| 5 | 45 | localized base ring subscript | o | 0 | medium |
| 5 | 45 | last paragraph reformulation after (p,0) | i.e. | compressed cursive abbreviation | medium |
| 5 | 45 | pale blue diagonal impression R1C1, near (170,230) pixels, opening line | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R1C2, near (450,230) pixels, opening line | \unsure{C}\illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R1C3, near (730,230) pixels, opening line | \unsure{C}\illegible{1}\unsure{n} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R1C4, near (1005,230) pixels, opening line | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R1C5, near (1280,230) pixels, opening line | \unsure{C}\illegible{1}\unsure{n} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R1C6, near (1555,230) pixels, opening line | \unsure{C}\illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R2C1, near (170,520) pixels, donc à définir | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R2C2, near (450,520) pixels, donc à définir | \unsure{C}\illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R2C3, near (730,520) pixels, donc à définir | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R2C4, near (1005,520) pixels, donc à définir | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R2C5, near (1280,520) pixels, donc à définir | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R2C6, near (1555,520) pixels, donc à définir | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R3C1, near (170,810) pixels, outlined deletion | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R3C2, near (450,810) pixels, outlined deletion | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R3C3, near (730,810) pixels, outlined deletion | \unsure{C}\illegible{1}\unsure{n} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R3C4, near (1005,810) pixels, outlined deletion | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R3C5, near (1280,810) pixels, outlined deletion | \unsure{C}\illegible{1}\unsure{n} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R3C6, near (1555,810) pixels, outlined deletion | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R4C1, near (170,1100) pixels, brace identities | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R4C2, near (450,1100) pixels, brace identities | \unsure{C}\illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R4C3, near (730,1100) pixels, brace identities | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R4C4, near (1005,1100) pixels, brace identities | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R4C5, near (1280,1100) pixels, brace identities | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R4C6, near (1555,1100) pixels, brace identities | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R5C1, near (170,1390) pixels, end of NB | \illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R5C2, near (450,1390) pixels, end of NB | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R5C3, near (730,1390) pixels, end of NB | \illegible{1}\unsure{n} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R5C4, near (1005,1390) pixels, end of NB | \illegible{1}\unsure{n} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R5C5, near (1280,1390) pixels, end of NB | \illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R5C6, near (1555,1390) pixels, end of NB | \unsure{C}\illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R6C1, near (170,1680) pixels, definition and independence of x^(n) | \illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R6C2, near (450,1680) pixels, definition and independence of x^(n) | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R6C3, near (730,1680) pixels, definition and independence of x^(n) | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R6C4, near (1005,1680) pixels, definition and independence of x^(n) | \unsure{C}\illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R6C5, near (1280,1680) pixels, definition and independence of x^(n) | \unsure{C}\illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R6C6, near (1555,1680) pixels, definition and independence of x^(n) | \illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R7C1, near (170,1970) pixels, example 1 conclusion | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R7C2, near (450,1970) pixels, example 1 conclusion | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R7C3, near (730,1970) pixels, example 1 conclusion | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R7C4, near (1005,1970) pixels, example 1 conclusion | \unsure{C}\illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R8C1, near (170,2260) pixels, example 2 opening | \unsure{Canson\|CANSON} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R8C2, near (450,2260) pixels, example 2 opening | \unsure{C}\illegible{1}\unsure{on} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R8C3, near (730,2260) pixels, example 2 opening | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R8C5, near (1280,2260) pixels, example 2 opening | \unsure{C}\illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R8C6, near (1555,2260) pixels, example 2 opening | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R9C1, near (170,2550) pixels, last continuation | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R9C2, near (450,2550) pixels, last continuation | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | pale blue diagonal impression R9C3, near (730,2550) pixels, last continuation | \illegible{1} | Reading taken from this impression only. One unreadable-word marker denotes the unrecovered part or whole of its single word; adjoining uncertain letters belong to that same word. No completion from another impression. | low |
| 5 | 45 | upper-left brown marks | nonverbal strokes, dots and curved traces reproduced as a drawing | No secure letters or numerals; authorship and whether ink, transferred marks or surface damage cannot be established visually. | low |
| 5 | 45 | live multiplication identity under the brace, numerator | (m+n)! | (m+n!; closing parenthesis/factorial separation is compressed in the ink | medium |
| 5 | 45 | blue repeated marks, count and extent | 48 individually distinguishable impressions, arranged in nine approximate rows | Six further periodic positions R7C5, R7C6, R8C4, R9C4, R9C5, R9C6 were enlarged but no separate letter-ink could be distinguished confidently from background or overlying text; these were not counted or filled. | medium |
| 5 | 45 | blue repeated marks, origin | unresolved physical imprint versus later overlay | The regular spacing and colour do not establish producer, date, authorship or acquisition history. No institutional attribution is made. | low |
| 5 | 45 | blue repeated marks, fuller specimens | Canson / CANSON, low confidence | Earlier consideration of a copyright-like round first sign was not supported sufficiently to retain it as the preferred reading; no year or institutional name can be read securely. | low |
| 5 | 46 | first word | ïncide | continuation of a word from preceding page | medium |
| 5 | 46 | black cancellations | unreadable words, estimates 1–12 | underlying typescript is physically masked by thick ink | low |
| 5 | 46 | item i deleted phrase | C est un B-module | C est une B-algèbre | low |
| 5 | 46 | item iii cancellation | déterminés de façon unique | strike extent versus editorial bracketing | medium |
| 5 | 46 | left of item iii | style ambigu, with ambigu underlined | independently enlarged and confirmed | high |
| 5 | 47 | top line | satisfont | satisfait | medium |
| 5 | 47 | top reference | α) | other letter or condition sign | low |
| 5 | 47 | example deleted adjective | à valuation | à ... | low |
| 5 | 47 | example deleted line | son corps des fractions soit | son corps des fractions est | medium |
| 5 | 47 | example abbreviation | car. | Car without a stop | medium |
| 5 | 47 | valuation paragraph | on a | alors | medium |
| 5 | 47 | four cancellations in inequality | ρ; e; e; e | overwritten mathematical signs | low |
| 5 | 47 | right margin | Legendre | another abbreviated annotation | medium |
| 5 | 47 | left lower cancellation | déterminer λ(p) | first word uncertain | low |
| 5 | 47 | denominator near foot | r | p; enlarged ink has an r-like shoulder and no visible p loop; visible-first order changed in audit | medium |
| 5 | 47 | question exponent | π^(n) | π^[n]; curved opening and closing strokes favor parentheses | medium |
| 5 | 48 | first paragraph Dér subscript | k | A; overworked subscript | medium |
| 5 | 48 | deleted topological phrase | two unreadable words | ink-obscured typescript | low |
| 5 | 48 | last paragraph deletion | one unreadable word | ink-obscured typescript | low |
| 5 | 48 | radical notation | underlined r | Gothic r convention represented by typewriter underline | high |
| 5 | 49 | upper right name | Deligne | compressed final letters | medium |
| 5 | 50 | first paragraph missing mathematical signs | blank spaces in f:X Y; dim(Y−y) n; f^−1(A) B | no arrow or inequality is visibly present; none supplied | high |
| 5 | 50 | line characteristics | résidueales | résiduelles; overtyping | low |
| 5 | 50 | same line anneaux | anneaux | anneaus; overtyping | medium |
| 5 | 50 | display shift | T_X/Y followed by blank and 2d | brackets or punctuation not visibly present | high |
| 5 | 50 | last paragraph spelling | numéro-ratrappage | numéro-rattrappage not written | high |
| 5 | 50 | first paragraph induction parameter | n=dim X | X is clearly typed; Y would be a contextual emendation and is not adopted | high |
| 5 | 51 | first typewritten cancellation | e relati | relati; x overtyping obscures the e immediately after un and individual letters; continuation on next line | medium |
| 5 | 51 | next-line cancellation | on | en; rounded first letter favours o | medium |
| 5 | 51 | after caractéristique p | caractéristique | another long word ending -ique | low |
| 5 | 51 | De-Rham in middle paragraph | hyphen | overtyped or omitted hyphen | medium |
| 5 | 51 | within faisceaux | ce | two overtyped letters | medium |
| 5 | 52 | convergentes | deleted a | deleted overtyped letter | medium |
| 5 | 52 | ordinary analytic paragraph | ce | overtyping c/e | medium |
| 5 | 52 | same paragraph typo | beamucoup | beaucoup | medium |
| 5 | 52 | Tate recollection | m’avait | n’avait | medium |
| 5 | 52 | Frobenius isomorphism source | underlined O_X | underlined Ω_X; overworked symbol | medium |
| 5 | 52 | last-line first exponent | p changed to n | overtyped exponent | medium |
| 5 | 52 | first comparison map at bottom | plain dash | no arrowhead visibly present | high |
| 5 | 53 | third line canceled word | dans | des | low |
| 5 | 53 | fourth line quoted adjective | vraie | vcaie; enlarged narrow shoulder and stem favour r | high |
| 5 | 53 | p-adique hyphen | hyphen | heavy overdrawn mark with short ascending stroke; no additional letter securely resolved | medium |
| 6 | 2 | R-homomorphisme cancellation | ho | two overtyped letters | medium |
| 6 | 2 | opening spelling | De Rahm | literal transposition in typescript | high |
| 6 | 2 | terminological spelling | croitre | no circumflex visible | high |
| 6 | 2 | two catégorie words in1.0 | catégorie | heavy retouching of té and ri respectively; no different earlier reading securely distinguishable | medium |
| 6 | 3 | whole background | mirrored text transmitted from scan002 | not an independent text on this face | high |
| 6 | 4 | section1.3 Pour s’en assurer | il | id; last letter overtyped | medium |
| 6 | 4 | section1.3 parenthesis after C prime | a | single heavily overtyped letter | low |
| 6 | 4 | section1.4 structure adjective | spplémentaire | supplémentaire; apparent p overtyping at second letter | medium |
| 6 | 4 | section1.5 above k | du | de; canceled two-letter word | low |
| 6 | 4 | section1.5 after lui-même | semicolon augmented from typed period | added lower comma converts punctuation before handwritten insertion | high |
| 6 | 4 | handwritten characteristic-zero insertion | Q | ordinary handwritten Q, no separate underline visible | high |
| 6 | 4 | opening of1.4 | criataux | cristaux; enlarged fourth letter is a-shaped in the typescript | high |
| 6 | 5 | first word | Est | est; initial overtyped | medium |
| 6 | 5 | before vectoriels | one unreadable canceled word | possible esp... or ann...; dense repeated x overtyping prevents a reliable reading after enlargement | low |
| 6 | 5 | before quotation valeur en S | canceled colon | overtyped short punctuation | low |
| 6 | 5 | étale paragraph s’identifient | identifient | ddentifient; i/d overtyping | medium |
| 6 | 5 | 1.7 canceled heading | Relations avec la notion d’objet stratifié | d’objets stratifiés; repeated x overtyping affects several letters | low |
| 6 | 5 | 1.7 after sous- | objet de | schéma; enlarged surviving b-like ascender, j descender, t, and de favour objet de | medium |
| 6 | 5 | 1.7 quasi-cohhérent | cohhérent | cohérent; overtyping at h | medium |
| 6 | 5 | 1.7 three neighbourhood symbols | R canceled and S inserted | R/S overtyping visible, best reading S as final letter | medium |
| 6 | 5 | 1.7 superscript above first S_n | canceled n | dense overtyping of one raised character | low |
| 6 | 5 | 1.7 infinitesimal-neighbourhood prose | de R dans S | literal order in the typescript, not reversed editorially | high |
| 6 | 6 | first line after qu’à | r | n; canceled single letter | low |
| 6 | 6 | second paragraph en effet | effett | effet; final t overtyped | medium |
| 6 | 6 | pseudo-stratification in definition | strratification | stratification; overtyping after st | medium |
| 6 | 6 | formal-unramified paragraph une seule | seule | seube; l overtyped | medium |
| 6 | 6 | equivalence at end of unramified paragraph | F_R | R clearly typed although S would match the stated value functor | high |
| 6 | 6 | last paragraph Ceci défini | d plus handwritten éfini | handwritten completion/reworking of typed word; no separate caret | medium |
| 6 | 6 | typewriter doubling in On and Une | On; Une | displaced duplicate n impressions treated as one overtyped letter | high |
| 6 | 6 | cancelled word before valeur in last paragraph | vlaeur | valeur; enlarged second-letter ascender favours transposed l/a in the cancelled typing | medium |
| 6 | 7 | continuation first paragraph l’exemple | exmple | exemple; handwriting/overtyping partly restores missing letter | medium |
| 6 | 7 | before démonstration | de | la; overtyping | medium |
| 6 | 7 | 1.9 first heading word | UNe | Une; n appears uppercase after overtyping | medium |
| 6 | 7 | 1.9 différentiellepent | différentiellepent | literal p in place normally occupied by m | high |
| 6 | 7 | 1.9 1-donnexion | donnexion | connexion; first letter overtyped | medium |
| 6 | 7 | 1.9 en disant | ddsant | disant; overtyped initial pair | medium |
| 6 | 7 | before de lissité | propriété | proposition; visible propri- and word width favour propriété under overtyping | medium |
| 6 | 7 | Cartier marginal insertion | p.ièmes | pièmes; separator after p faint | medium |
| 6 | 7 | before stratification exclamation | rigidifi | canceled incomplete word | medium |
| 6 | 7 | 1.10 scheme letter | R canceled, S inserted | R/S overlay | medium |
| 6 | 7 | last line canceled phrase | le cas de | heavy handwriting strike-through obscures most letters | low |
| 6 | 7 | curvature endomorphism notation | ENd | capital N visibly typed, underlined | high |
| 6 | 8 | first paragraph after s prime | a | overtyped single canceled letter | low |
| 6 | 8 | before devrait permettre | permett | permet; canceled ending unclear | medium |
| 6 | 8 | last paragraph infinitive | introduite | introduire; last consonant looks t, internal letter overtyped | medium |
| 6 | 8 | last paragraph agreement | une notions duale | literal plural s | high |
| 6 | 8 | inverse-image display | frob_S(M) | no star above frob is visible; not supplied editorially | high |
| 6 | 9 | first paragraph spelling | mulplient | literal mul- / plient across line break; no ti visible | high |
| 6 | 9 | first FV relation cancellation | =VF | dense overwriting of three mathematical signs | low |
| 6 | 9 | first VF relation | VF=id_M(p) | no factor p visible; retained literally | high |
| 6 | 9 | indices in FV/VF identities | M(p) | parenthesized p is on the subscript baseline, not visibly a raised exponent | high |
| 6 | 9 | Tate weight first mention | 2 inserted before i | overworked mark; circled marginal2i supports final visible value | medium |
| 6 | 9 | before morphismes | appliqu | canceled incomplete word, ending concealed by x overtyping | low |
| 6 | 9 | de sorte que correction | sorte replaced by façon | handwritten replacement over the typed word | medium |
| 6 | 9 | two torsion occurrences | torsion | internal letters overtyped | medium |
| 6 | 9 | bottom insertion plural | objet | objets; no distinct final s discernible | medium |
| 6 | 9 | bottom insertion tensor subscript | Z | underlined Z; handwritten lower stroke can be intrinsic letter bar | medium |
| 6 | 9 | Tate tensor-power sentence | weight2i is ith tensor power of weight1 | literal numerals as typed; not harmonized with weight additivity | high |
| 6 | 10 | opening underlined term | isogristaux | literal g-like descender; not regularized to isocristaux | high |
| 6 | 10 | both p exponents before F inverse | canceled2 then i | opaque cancellation before clear i | medium |
| 6 | 10 | first localized category in display | Isbicr | IsBicr; b/B overtyped | medium |
| 6 | 10 | arguments in same display | S,i | S)i; separator and S overtyped | low |
| 6 | 10 | before pleinement fidèle | évidemment | dense handwritten strokes conceal canceled word | low |
| 6 | 10 | inserted prefix before bicristaux | iso- | overworked handwritten prefix | medium |
| 6 | 10 | dual formula object symbol | underlined M repeated for dual | no separate star or prime is visible on the displayed dual M | high |
| 6 | 10 | category-name case | Isbicr then IsBicr | case varies visibly between the first and final displays | high |
| 6 | 10 | cancelled duality parenthesis, enlarged | phi | F under x overtyping; visible oval crossed by a stem agrees with6/024 and031 | medium |
| 6 | 11 | beginning of page | de | page010 ends La noti-; no on appears before de on011 | high |
| 6 | 11 | punctuation after tensoriel | , | . overwritten or supplemented by handwritten comma | medium |
| 6 | 11 | canceled word before Exemple | Isocri | Isocr; visible final dot favours an additional i under x cancellation | medium |
| 6 | 11 | word définie | fi overtyped | underlying letters cannot be separated securely | medium |
| 6 | 11 | between f_W and semi-linéaire | canceled comma | hyphen; black x overlies punctuation | low |
| 6 | 11 | word homomorphisme before V display | morphisme | morpbisme: h/b region overtyped | medium |
| 6 | 11 | domain and arrow in V display | M followed by canceled T | domain M is fully separate and clear; T-like extra letter is crossed by the arrow shaft; confidence qualification: high for M, medium for deleted T | medium |
| 6 | 11 | canceled fraction-field notation at bottom | W tensor underlined Q_p | W with subscript underlined Q_p; heavy handwritten deletion prevents full recovery | low |
| 6 | 11 | deleted exponent on final f_K | -1 | tiny exponent concealed by x cancellation | low |
| 6 | 11 | first Frobenius paragraph grammar | un structure | literal masculine article before feminine noun | high |
| 6 | 11 | inverse-semilinear conclusion | f_W inverse-linéaire | semi is absent here although present in previous sentence | high |
| 6 | 11 | cancelled phrase after toute indiquée | pour recevoir | enlargement resolves recevoir rather than servir | high |
| 6 | 12 | opening descriptions | es | letters compressed and overtyped | medium |
| 6 | 12 | essential-image functor source | Isbicr | Hsbicr; first letters overtyped | medium |
| 6 | 12 | vector-space letter repeated | E | E handwritten over earlier typed character, possibly V | high |
| 6 | 12 | first semi-linéaire | né | overtyping makes accent and letters crowded | medium |
| 6 | 12 | exponent in V=p^i F inverse | i | enlargement resolves separate dot and stem, not numeral1 | high |
| 6 | 12 | second tensorisation, line end continuation | tion | gion; initial glyph overtyped | medium |
| 6 | 12 | canceled partial word before itérés | iétér | itér; five visible positions and two accents favour literal mistyped iétér | medium |
| 6 | 12 | bi-isocristaux after effectifs | is | two letters heavily overtyped | medium |
| 6 | 12 | first Tout in1.13 | Tout | Wout; T overtyped | medium |
| 6 | 12 | canceled prefix before cristal | R- | second sign obscured by x | medium |
| 6 | 12 | canceled word after localiser sur S | Ceci | aussi; third, weaker alternative: ainsi. Four visible positions, rounded c-like interior letters, and final dotted i favour Ceci; aussi is retained as the secondary overtyping reading. | medium |
| 6 | 13 | three early base symbols | R_n | W_n; R/W overtyping visible, final explicit R_n=Spec(W_n) clear | medium |
| 6 | 13 | after Comme S_n | b | isolated typed b is present and not canceled | high |
| 6 | 13 | canceled word after à un | pour | Pour; initial character overtyped | medium |
| 6 | 13 | supposons d’abords | final s | dark overtyped s-like letter follows d’abord | medium |
| 6 | 13 | first underlined coherent-modules assertion | dohérents | literal d, not silently corrected to cohérents | high |
| 6 | 13 | parenthetical dernière | dernière | detnière; r/t region overtyped | medium |
| 6 | 13 | after caractéristique nulle in generic-fibre sentence | on | oj; second letter overwritten | medium |
| 6 | 13 | facilement near end | facilement | central letters multiply overtyped | medium |
| 6 | 13 | generic-fibre stratification base | X_K | literal repeated X_K after relativement à, not changed to K | high |
| 6 | 13 | comparison reference at right edge | EGA III4,5 | no punctuation following5 is visible before next line que | high |
| 6 | 13 | parenthetical de l’espèce F considérée | espàce | espèce; the grave-accented overtyped vowel has an a-like closed bowl; unresolved correction state | medium |
| 6 | 14 | connexion before inserted ex | conn | comn; initial and middle letters overtyped | medium |
| 6 | 14 | canceled short word after fondamental | du | de; two characters under x | low |
| 6 | 14 | constant | st | ss; two letters overtyped | medium |
| 6 | 14 | fourbi terminal deletion | s | small final sign densely canceled | medium |
| 6 | 14 | canceled long word before si par hasard | préliminairement | interior letters heavily x-overtyped | low |
| 6 | 14 | sign before Cela | opening parenthesis | stray overtyped character or correction mark | low |
| 6 | 14 | left margin | effectivement, ça ne marche pas ! | ne cramped; remaining words legible | medium |
| 6 | 14 | formal spectrum | Specf(W) followed by inserted=R | literal Specf, not normalized to Spf | high |
| 6 | 14 | opening of generic-fibre paragraph | Quand à | literal d in Quand retained | high |
| 6 | 14 | formal-lift paragraph after schéma formel X sur | R | B; overtyping leaves two bowl-like masses, while a lower-right diagonal favours R | medium |
| 6 | 15 | line 1, overwritten preposition | de | pour; correction over typewriting | low |
| 6 | 15 | above line 1 | envisagée | envisagé | medium |
| 6 | 15 | line 10, cancelled duplicate | ici | si | low |
| 6 | 15 | line 15, deleted number | 1.14. | 1.13. | medium |
| 6 | 15 | line 17, overstruck phrase | un tel cristal | un cristal | medium |
| 6 | 15 | lines 19–20, overtyped agreement changes | un / à un / est | underlying letters obscured by correction | low |
| 6 | 15 | line 26, overstruck prefix | homo | initial draft of morphismes | medium |
| 6 | 15 | bottom left | 14 | numbering provenance uncertain | high |
| 6 | 16 | line 3 and line 8 | Specf(W) | Spec with handwritten f added; not normalized to Spf | medium |
| 6 | 16 | line 13 | soit | underlying overtyped letters unresolved | medium |
| 6 | 16 | line 17 | 1_{\underline{O}_S} | 1_{\underline{\mathcal O}_S}; typed O is plain | medium |
| 6 | 17 | line 7, overstrike | il | two overstruck letters | medium |
| 6 | 17 | line 27, insertion placement | objets before buts | replacement of buts without visible cancellation | medium |
| 6 | 17 | bottom inserted condition | isom | isom. | medium |
| 6 | 17 | bottom inserted condition | imm. ouverte | immersion ouverte written in abbreviation | medium |
| 6 | 17 | bottom inserted condition | T→T\prime | T-T\prime, arrowhead indistinct | medium |
| 6 | 18 | line 4, corrected number agreement | finie | original fini with added e | high |
| 6 | 18 | line 17, deleted suffix | raphique | handwritten correction obscures original letters | medium |
| 6 | 18 | left marginal parenthesis | faut d’introduire les puiss. div. | faute d’introduire les puiss. div. | medium |
| 6 | 18 | line 23, overstruck phrase | et et comme connexion | exact first words beneath x-overstrike uncertain | low |
| 6 | 18 | line 22, inserted evaluation point | S\prime | S; visible prime retained despite mathematical concern | high |
| 6 | 18 | left margin, parenthesis | faut | faute, final e possibly fused into following stroke | medium |
| 6 | 19 | line 3, overwritten suffix | raphique | underlying word cristallographique partly obscured | medium |
| 6 | 19 | line 27, overwritten source | S prime | S without prime | medium |
| 6 | 19 | end of opening paragraph, after modules. | ? | isolated hooked pen mark or stray ink; no secure letter | low |
| 6 | 20 | line3, overwritten noun | torsion | original word largely overwritten by bure | medium |
| 6 | 20 | spectral sequence coefficient | C_{S^{an}} | C_{X^{an}} expected mathematically but S visible | high |
| 6 | 20 | line21, overstruck phrase | un genre d’énoncé précis | un genre d’énoncés précis | medium |
| 6 | 20 | line23 within deleted passage | sur | overtyped preposition | medium |
| 6 | 21 | line6, isolated small added letter | c | unattached editorial mark rather than lexical content | low |
| 6 | 21 | line10 | cotravariante | contravariante; no n visible in typescript | high |
| 6 | 22 | end of line1, fully inked deletion | unreadable word | attempted ne; no recoverable letters at enlarged crop | low |
| 6 | 22 | line4, Frobenius arrow | X_p^(p/S)→X | direction retained exactly; no p on target X | high |
| 6 | 22 | line10, duality product | p^(2d) | p^d mathematically conceivable; 2d is clear ink | high |
| 6 | 22 | line 4, S-morphisme | S followed by an underlined hyphen | underline intended for S but displaced to the right | medium |
| 6 | 23 | line1 deleted word | additi | additif; final f not visible | medium |
| 6 | 23 | line4 bicristal correction | extra c deleted | overwritten r or other letter | low |
| 6 | 23 | line8 p-divisible | ble with typed correction before b | xble as visible overtype | medium |
| 6 | 23 | handwritten addition after changement de base | sans condition affine sur S | affine appears written with separated strokes | medium |
| 6 | 23 | before la cohomologie de De Rham | deleted H | la; inked correction prevents secure reading | low |
| 6 | 24 | d’expliciter | deleted e | overtyped two strikes may include another letter | medium |
| 6 | 24 | deleted expression before M(S) | DR^1( | last parenthesis struck but recognizable | medium |
| 6 | 24 | functor B↝(A,phi) | phi | Closed oval crossed by stem; reconciled visually with6/031–032 before freeze | high |
| 6 | 24 | base in DR^1(A/A)(S) | A/A | A/S would be expected but A/A is clear | high |
| 6 | 24 | Cet énoncé corrections | Ces énoncés corrected to Cet énoncé | first s overtyped by t; final s crossed | medium |
| 6 | 25 | Serre-Tate | e overwritten with E or inverse | Serre versus SErre | medium |
| 6 | 25 | DR^1 base in first paragraph | S | A overtyped with S; order not certain | medium |
| 6 | 25 | De façon deletion | extra n | s | low |
| 6 | 25 | V(t_A), parenthesis où A est dual de A | A without star in all three positions | star absent although dual A* occurs later | high |
| 6 | 25 | diagram O subscript | S | A, overtype contains both letterforms | low |
| 6 | 25 | G(B/S) at bottom | B/S | B/T not written | high |
| 6 | 26 | DR^1 base in first paragraph | S | A overtype, final state ambiguous | medium |
| 6 | 26 | source of Manin application A(S) | S | A overtype | medium |
| 6 | 26 | punctuation after G=G(A/S) sur S | ? | period overtyped with question mark, visible shape ? | medium |
| 6 | 26 | second Picart-Fuchs correction | y to t | typed final letter could be t already overmarked | medium |
| 6 | 26 | deleted expression before t_G tensor Omega | Gamma( | Gamma(S, | low |
| 6 | 27 | G(B’) deleted mark | comma | extra letter or mathematical sign under overstrike | low |
| 6 | 27 | handwritten vérifiée | vérifiée | vérifié, final e not distinct | medium |
| 6 | 27 | sont deleted extra letter | s | unreadable overtype | low |
| 6 | 27 | dimension bound correction | 1 replaced by0 | oblique link connects below-line0; 1 not fully crossed | medium |
| 6 | 27 | S subscript | rég | réd mathematically plausible but g is visible | high |
| 6 | 27 | left margin beside c), enlarged | peu- | peut-; no secure t is separable in the final stroke | medium |
| 6 | 27 | lower circled margin, enlarged | m with superscript me | même written continuously, or ou; possible abbreviation not expanded | low |
| 6 | 28 | scope of long oblique strike | entire block from J’aurais through handwritten sons | stroke begins line below opening bracket and ends below final paragraph | medium |
| 6 | 28 | left margin top | Faux, ce n’est jamais vrai en car p>0 ! | ce reduced to a curved stroke; en/car split over lines | medium |
| 6 | 28 | left lower marginal note | non, finalement | last word cursive and partly touches typed fallait | low |
| 6 | 28 | opening paragraph term | calcul-clef | calcub-clef overtype on final l | medium |
| 6 | 29 | Prenons deletion | extra n | overtyped consonant, likely duplicate n | medium |
| 6 | 29 | non-variation deletion | de G(A) | letters obscured by typing and handwriting | medium |
| 6 | 29 | family of elliptic schemes deletion | pade | par; final de may be overtyped | low |
| 6 | 29 | S_U and following U | U | overtyped capitals with doubled upper strokes | medium |
| 6 | 29 | la module à stratification | la retained | module à added without clearly changing la to le | high |
| 6 | 30 | typed eependant | eependant | cependant intended but two e forms visible | high |
| 6 | 30 | handwritten insertion | tout-au moins | tout au moins; dash may belong to t stroke | medium |
| 6 | 30 | VA ordinaires punctuation | ? | question mark over earlier punctuation | high |
| 6 | 30 | lower paragraph, tout au mieux ... prêter | de | se, possible overtype; ascender favours d | medium |
| 6 | 31 | chapter numeral deletion | 2 | 4; inked overtype | low |
| 6 | 31 | group notation | phi closed loop with crossing stem | varphi shape; not an empty set symbol | high |
| 6 | 31 | deleted expression before G(phi) varie | underlined H(phi) | final closing parenthesis unclear | medium |
| 6 | 31 | deleted word before ind-étale | formel | heavy crossing obscures middle letters | medium |
| 6 | 31 | formal vector group tangent term | t_phi* without vee | sequence immediately below has t_phi*^vee | high |
| 6 | 32 | en passant deletion | du | à, overwritten first glyph | medium |
| 6 | 32 | adic topology | j-adique | J-adique not printed; j visibly lowercase | high |
| 6 | 32 | module rank | g+g prime | g+g star would match later but prime visible | high |
| 6 | 32 | formel punctuation | deleted comma | inked punctuation could be semicolon | medium |
| 6 | 33 | title Tate-module index | p | handwritten p distinct from l in the book title | high |
| 6 | 33 | bibliographic title | Abelian l-adic representations | literal abbreviated title; no further words supplied | high |
| 6 | 34 | after rank2 deletion | libre | last letters and bracket-like stroke uncertain | low |
| 6 | 34 | side Tate-module note | et T_p(E_barK)_ét=T_p(E_barK) | opening bracket uncertain; bars and K case read from separate occurrences | medium |
| 6 | 34 | inserted abbreviation after rang1 | m. n. ramifié | module non ramifié, but abbreviation not expanded | medium |
| 6 | 34 | later Tate modules | E_K without bar | main rank2 line has explicit bar; later occurrences lack clear bar | medium |
| 6 | 34 | left diagram quotient | L superscript star | vee; thick small mark over L | low |
| 6 | 34 | obliterated expression in H^1 | L^vee tensor L^vee | Hom(L,L^vee); attempted readings only, inked formula not recoverable | low |
| 6 | 34 | annotation under L_0 | valeur en k | valeur sur k | medium |
| 6 | 34 | cancelled noun after grp, enlarged | Module | Modèle or Mordell; middle letters lie on strike | low |
| 6 | 34 | marginal sequence second and fourth connectors | plain horizontal strokes | right arrows with thick but unresolved heads | medium |
| 6 | 34 | marginal sequence terminal object | filled dot | 0, as originally tentatively read | medium |
| 6 | 34 | inverse limit overwritten expression, enlarged | K*/[inserted K* after deleted Z-like sign] to p^n | K* tensor Z/p^n; precise denominator/exponent layout unresolved | low |
| 6 | 35 | opening word | Et | A; highly compressed capital | medium |
| 6 | 35 | underbrace under A** | Eins-einheiten | 1-unités; first and final letters cramped | medium |
| 6 | 35 | bracketed NB first clause | Ça fait donc qu’on a un invariant | On voit donc qu’on a un invariant; first two words pale and compressed | low |
| 6 | 35 | small deletion after carré de | un | u; very short black cancellation | low |
| 6 | 35 | right NB Tate-module argument | E_K | E_barK; bar over K not clear | medium |
| 6 | 35 | right NB last clause | si est d’ordre fini | s’il est d’ordre fini; no clear subject between si and est | low |
| 6 | 35 | left margin after En tous cas | on aura | on a; compressed strokes | low |
| 6 | 35 | left margin bracket ending | gén. | précédent; remaining handwritten strokes not securely resolved | low |
| 6 | 35 | before -simple in b | 1/2 | Q; graph consists of upper vertical, diagonal slash, lower 2-like curve | low |
| 6 | 35 | bottom pi index | superscript 1 | subscript 1 displaced high; literal high position retained | medium |
| 6 | 35 | deleted word after Mais | cq | que; blackened descender and cross-stroke | low |
| 6 | 35 | bottom final clause | valable, les conclusions de cette conjecture valent aussi | valable and valent at lower paper edge, but surviving letters support reading | medium |
| 6 | 36 | heading characteristic inequality | car K>0 | car K≠0; angled stroke with horizontal tail | medium |
| 6 | 36 | cancelled word before Il y a lieu | Cela | Ce cas; dense cancellation obscures middle letters | low |
| 6 | 36 | Tate-module argument in equal-characteristic introductory sentence | T_p(K) | K clearly resembles later K; no E supplied although text might intend E; confidence qualification: medium-high | medium |
| 6 | 36 | A heading | Cas j entier | j resembles descending g but following entier is visible; confidence qualification: medium-high | medium |
| 6 | 36 | start of a | Si quand on | redundant Si/si left as written; no clear cancellation | medium |
| 6 | 36 | lower marginal qualifier | si k alg. clos | first si/qui and compact alg. ambiguous, placement arrow visible | medium |
| 6 | 36 | unfinished parenthesis | pas nulle dans L^-2 tensor | nul; final e-like stroke before dans | medium |
| 6 | 36 | unfinished expression | L^-2 tensor | no further factor or closing parenthesis on this leaf | high |
| 6 | 37 | NB mark before T_p | overlined m | equality/ditto symbol; horizontal top stroke and m-like lower stroke, not expanded to même | medium |
| 6 | 37 | inserted model symbol after Néron | bar E | plain E; separate upper stroke may belong to letter | medium |
| 6 | 37 | torsion object | left subscript p^nu, bar E | n rather than nu; plain E rather than bar E | medium |
| 6 | 37 | torsion subgroup exponent | nu | n; v-shaped handwritten exponent | medium |
| 6 | 37 | sign canonicity qualifier | (de façon canonique mod signe] | opening parenthesis and closing square bracket retained as drawn; confidence qualification: medium-high | medium |
| 6 | 37 | final bracket first word | provenant | provient; pale middle letters compressed | medium |
| 6 | 37 | page sequence | Je conjecture ends037; que cet élément starts036 | likely textual continuation across reversed scan order, but physical folios35 and36 retained; confidence qualification: high for visible endpoints, inference for connection | medium |
| 6 | 37 | NB abbreviation compared with5/016 and020 | overlined upright m | same wavy abbreviated form verified independently; equality-like alternative retained locally | medium |

# Abbreviations encountered

| Form on page | Tentative expansion (only here) |
|---|---|
| $\overline{\mathrm m}$ | même (tentative expansion of overbarred wavy m) |
| Alg | algèbre (alternative reading) |
| Ann. Éc. N. Sc. | Annales de l’École normale supérieure (tentative) |
| Cor. | corollaire |
| Cris | cristallin |
| DR | De Rham |
| DRst | De Rham stratifiant |
| DRst | De Rham stratifiant (tentative) |
| DRstrat | De Rham stratifiant |
| Dém. | démonstration |
| EGA | Éléments de géométrie algébrique |
| Exp | Exposé |
| J. | Journal (in J. de Liouville) |
| MC | multiplication complexe |
| N.B. | nota bene |
| NB | nota bene |
| NB. | nota bene |
| NS | nécessaire et suffisant |
| OK | okay |
| Pb | problème |
| Prop | proposition |
| SGA4 | Séminaire de géométrie algébrique 4 |
| SGAD | Séminaire de géométrie algébrique, schémas en groupes (tentative contextual expansion) |
| Specf | spectre formel |
| Strat | stratifiant |
| Suppr. | supprimer |
| Tel. | Telefono |
| Th | théorie ou théorème (tentative reading) |
| VA | variété abélienne |
| Zar | Zariski |
| alg | algébriquement |
| alg. | algèbre |
| alg. clos | algébriquement clos |
| argts | arguments |
| can. | canonique |
| can. | canoniquement |
| car | caractéristique |
| car. | caractéristique |
| car. | caractéristiques |
| cf | confer |
| cf. | confer |
| changts | changements |
| chgt. | changement |
| coeff. | coefficient |
| coh. | cohomologies |
| comm | commutatif |
| cond. | conditions |
| div | divisées |
| div. | divisées |
| déf. | définition |
| d’ens | d’ensembles |
| etc | et cetera |
| etc. | et cetera |
| ex. à g. | exact à gauche |
| ext. | extension |
| f. et s. | faut et suffit |
| fonct | foncteur |
| fonct. | foncteur (uncertain reading) |
| formt. | formellement (tentative) |
| grp | groupe |
| gén | général |
| gén. | général (uncertain reading) |
| gén. | générateurs |
| hom | homomorphisme |
| homs | homomorphismes |
| i.e | id est |
| i.e. | id est |
| i.ème | i-ième |
| id | idem |
| id | identité |
| idt | idéal (uncertain) |
| imm. | immersion |
| inv. | inversible |
| inv. | inversibles |
| isom | isomorphisme |
| isom | isomorphismes |
| isoms | isomorphismes |
| l. | ligne |
| loc | localement |
| loc.noeth. | localement noethérien |
| m. n. ramifié | module non ramifié (tentative) |
| maj. | majuscule |
| mod. | modulo |
| n.ème | n-ième |
| nb | nombre |
| nbs | nombres |
| nbs. | nombres |
| n° | numéro |
| néc | nécessairement |
| néc. | nécessairement |
| op. | opérations |
| overlined m | même (tentative abbreviation) |
| p. | page |
| p. | page(s) |
| p. ex. | par exemple |
| p.div. | puissances divisées |
| p.ex. | par exemple |
| p.ème | p-ième |
| par. | paragraphe |
| pb | problème |
| prop | proposition |
| prés. | présentation |
| ps-anneau | pseudo-anneau |
| puiss. | puissances |
| puiss. div. | puissances divisées |
| qq. | quelconque (uncertain) |
| rel | relativement |
| rel. | relativement |
| resp | respectivement |
| resp. | respectivement |
| rés. | résiduel |
| ssi | si et seulement si |
| syst. | système |
| sép. clos | séparablement clos |
| t. | tome |
| t.q. | tel que |
| th. | theorem |
| th. | théorème |
| tjrs | toujours |
| tjs | toujours |
| tt | tout |
| val. | valuation |
| zar | Zariski |
| équiv. | équivalence |
| ét | étale |

# Legibility and limits

The main typewritten passages are usually considerably more legible than the rapid handwritten calculations, but overtyping can hide both letters and punctuation. The heaviest obliterations are on cote 5, scans 009,032,046 and048: the surviving portions are transcribed, while estimated word counts are used only for physically obscured prose. Every mathematical uncertainty is represented by an attempted reading, not by a word-count placeholder.

The least secure handwritten material includes the title on 5/015; the dense arithmetic on 5/009,011 and013; the decorated ideal and polynomial-law notation on 5/025,032,035 and041–045; the looped category letter on 5/017–020; and the crowded annotations, crossed formulae and bottom-edge writing on 6/034–037. The uncertain alphabet, superscript, suffix, dash and arrowhead readings in these places are not resolved by the mathematics. Covers and brief dockets were checked as well as mathematical pages.

Several apparent slips are quite legible and are deliberately retained. Examples include conflicting printed indices or weights, omitted arrows on 5/050, the source's use of `dim X` in an argument subsequently localized on Y, the prime/star distinction on 6/032, and unfinished expressions on 6/036–037. Such cases are discussed separately in the research notes and are not silently repaired in the transcription.

The confidence labels assess the visible reading, not the validity of a statement or its historical attribution. “High” therefore does not certify the mathematics; “low” can accompany a coherent mathematical expression whose ink remains weak. An independent visual reader checked every page against its full image and both supplied halves, but this does not justify a numerical accuracy estimate or a claim that no misreadings remain.

The supplied scan order is retained. In particular, the visible endpoints of 6/037 and 6/036 suggest a textual continuation in the opposite order, and 5/048 ends with `co-` where 5/046 begins with the remainder of that word; these observations do not authorize rearranging the delivered pages. Handwritten foliation and other marginal numbers are retained with their locations, without assuming that every number belongs to the same hand or numbering system.

Scan 5/045 also contains faint repeated blue impressions behind the handwriting. Forty-eight impressions were individually recorded where a visible trace was present; six possible grid positions were not supplied from spacing alone. The tentative word `Canson` and its case are low-confidence readings, and partly obscured impressions retain only visible fragments with explicit uncertainty or unreadable portions. Neither the date nor the physical or digital origin of this pattern is established. The neutral geometric transcription of the upper-left brown marks likewise does not attribute them to the author.
