# MPL_83_178-222 — notation and doubts

This register is assembled from the reader's page records and the current page fragments. It preserves recorded readings and judgments without resolving them.

## Recurring notation — final visual review

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


## Page-by-page notation observations

Identical pairs of recorded sign and LaTeX representation are grouped; all associated scans and comments are retained. Grouping is exact and does not establish that differently recorded signs are equivalent.

| Recorded sign | LaTeX | Scans | Recorded comments |
| --- | --- | --- | --- |
| small circle superscript | <code>^\circ</code> | 178 | Scans 178: Read as circle, not prime; underlying meaning not used to decide. |
| star with subscript lambda | <code>\mathbin{*}_{\lambda}</code> | 178 | Scans 178: 178 |
| tensor symbol | <code>\otimes / \bigotimes</code> | 178 | Scans 178: 178 |
| double quotes | <code>``...''</code> | 178 | Scans 178: Use only where seen; no guillemet substitution. |
| b&#95;i versus u&#95;i | <code>b_i, u_i</code> | 179 | Scans 179: Distinct forms in the two-factor formulas; do not merge. |
| capital X versus lower x | <code>X_i / x_i</code> | 179 | Scans 179: Defined by underbrace X&#95;i=x&#95;i+α&#95;i. |
| lambda trivialization abbreviation | <code>\lambda-triv.</code> | 180 | Scans 180: 180 |
| solid strokes without heads | <code>\arrow[r,dash] or \unsure{\to&#124;-}</code> | 180 | Scans 180: Preserve visible headlessness rather than supplying arrows. |
| primes on line bundles | <code>L', L''</code> | 181 | Scans 181: 181: differentiated from circle superscripts. |
| iff abbreviation | <code>ssi</code> | 181 | Scans 181: 181, marked uncertain where stroke insufficient. |
| trace | <code>\operatorname{Tr}</code> | 183 | Scans 183: Capital T with r, not lower tr. |
| polar form of determinant | <code>\Psi_{\det}</code> | 183 | Scans 183: 183 onward |
| trace bilinear form | <code>\varphi(x,y)</code> | 183 | Scans 183: 183 |
| opposite cyclic triple traces | <code>\tau, \tau'</code> | 183 | Scans 183: 183 |
| Azumaya algebra letter | <code>\mathcal{A}</code> | 183 | Scans 183: Reconciled pre-context against the looped capital on scans183 and190; first occurrence carries alphabet doubt. |
| trace coordinate shorthand | <code>b,b',b''; c,c',c''; t,t',t''</code> | 184 | Scans 184: 184 top-right definitions; t=Tr yz, t′=Tr zx, t″=Tr xy. |
| symmetric trace sum | <code>\Sigma</code> | 184 | Scans 184: 184 definition |
| orientation-normalized wedge | <code>\Delta</code> | 185 | Scans 185: 185 underbrace definition. |
| triple-trace product polynomial | <code>\Pi</code> | 185 | Scans 185: 185. |
| epsilon notation | <code>\varepsilon, \varepsilon_0</code> | 185 | Scans 185: 185 distinct from τ,τ′. |
| automorphism group | <code>G=\operatorname{Aut}\mathcal A</code> | 186 | Scans 186: 186 |
| standard matrix units | <code>α,α′,x_0,y_0</code> | 186 | Scans 186: 186 explicit matrices. |
| permutation group | <code>\mathfrak{S}_3</code> | 189 | Scans 189: 189 florid S, uncertain alphabet. |
| Azumaya algebra versus coordinate ring | <code>\mathcal{A} versus A</code> | 190 | Scans 190: 190 distinct script A and straight A. |
| underlined generators | <code>\uline{B},\uline{C},\uline{t}</code> | 190 | Scans 190: 190 B/b uncertainty retained. |
| dual mark | <code>\check{\mathcal{A}}</code> | 192 | Scans 192: 192 visible v/check over A, not exclamation or prime. |
| pair trace indexed by a set | <code>t_{\{i,j\}}</code> | 193 | Scans 193: Braces explicitly written. |
| subset family P | <code>\unsure{\mathcal P&#124;P}_2</code> | 193 | Scans 193: Angular open capital, compared with scan205 before freeze; alphabet ambiguity marked in both. |
| symmetric group handwritten script S | <code>\mathfrak S</code> | 194 | Scans 194: Large looped S with lower subscript; consistent with earlier pages. |
| faithfully abbreviation | <code>fidèl superscript t</code> | 195 | Scans 195: Expansion only in doubt glossary. |
| unheaded strokes in ring diagrams | <code>dash edges</code> | 195 | Scans 195: No inferred arrowheads. |
| spaced typed emphasis | <code>letters separated by thin spaces</code> | 196 | Scans 196: Retain letter spacing for idée, publié, dessèchement. |
| typewriter crossed text | <code>\deleted</code> | 196 | Scans 196: X overstrikes are cancellations, not literal runs of x in live text. |
| dash denoting omitted intermediate factors | <code>\text{---}</code> | 197 | Scans 197: Literal long dash in handwritten products. |
| ds | <code>ds</code> | 197 | Scans 197: dans, only glossary expansion. |
| author typed sheet identifier | <code>L 17</code> | 198 | Scans 198: mspage distinguishes it from pencilled archive197. |
| cube edge placeholder labels | <code>t_{\ldots}</code> | 199 | Scans 199: Dots are actually written, not editorial omissions. |
| cyclic permutation groups | <code>\mathfrak S_4,\mathfrak S_3^+</code> | 199 | Scans 199: Plus explicitly visible. |
| intermediate ring | <code>B_1</code> | 200 | Scans 200: Distinguish subscript1 from0 in same diagram. |
| tilde over face/edge index | <code>\tau_{\tilde f},\Sigma_{\tilde a}</code> | 201 | Scans 201: Tildes attached to indices by ink position, not whole invariant. |
| face label | <code>f,f\prime,f\prime\prime</code> | 201 | Scans 201: Long descender loop; distinguish from group letter g. |
| moved parenthesis | <code>\inserted{...}</code> | 202 | Scans 202: Transcribed once at insertion arrow target. |
| typed partial cancelled word | <code>dégra</code> | 202 | Scans 202: Do not expand partial words. |
| edge endpoint pairs | <code>\Sigma_{AB\prime},\Sigma_{CA\prime}</code> | 203 | Scans 203: Uppercase endpoints distinguish from lowercase edge names. |
| pencilled lower-case sigma | <code>\sigma</code> | 203 | Scans 203: Distinct from large capital Sigma in ink. |
| duplicate author folio | <code>L 17</code> | 204 | Scans 204: Separate scan204 and198; distinct revision states. |
| hooked capital T for triple and face traces | <code>\mathcal T</code> | 205 | Scans 205: alphabet is uncertain on this sheet |
| lower-case sigma,pi | <code>\sigma,\pi</code> | 205 | Scans 205: distinguished from uppercase Sigma,Pi on earlier pages |
| delta superscript two joined strokes | <code>\delta^{\unsure{\prime\prime&#124;4}}</code> | 213 | Scans 213: double prime versus digit4 uncertain in lower equations |
| three edge-direction parameters | <code>\lambda,\mu,\nu</code> | 221 | Scans 221: As in upper explanatory label; no new script alphabet. |
| letterspaced typewriter emphasis | <code>\enspace</code> | 222 | Scans 222: Spacing preserved explicitly; double quotation marks as &#96;&#96; and double apostrophes. |

## Reader-recorded doubts

Locations, proposed readings, alternatives, and confidence values below are copied from the page records.

| File | Scan | Approximate location | Reading | Alternatives / recorded explanation | Confidence |
| --- | --- | --- | --- | --- | --- |
| 83 | 178 | upper paragraph | <code>etc.</code> | abridged continuation after limite | low |
| 83 | 178 | λ-definition | <code>semi-hom.; canon. i-linéaire</code> | abbreviated words and i poorly formed | low |
| 83 | 178 | diagonal note | <code>im.; considérer; pour celles qui sont; se donner un; avec</code> | very compressed diagonal script | low |
| 83 | 178 | bottom | <code>en nb premiers; d’ordre</code> | ending cut close to lower edge | low |
| 83 | 178 | superscripts | <code>E_i^\circ</code> | E&#95;i^0 | medium |
| 83 | 179 | first paragraph | <code>(soit g)</code> | (sur g) | low |
| 83 | 179 | crossed display | <code>f(x_1,α_2)</code> | letters overwritten | low |
| 83 | 179 | last equality | <code>x_1</code> | X&#95;1 | medium |
| 83 | 179 | lower connective | <code>veut</code> | a | low |
| 83 | 180 | diagonal note | <code>b_i; façon can.</code> | β&#95;i; last word very compressed | medium |
| 83 | 180 | commutativity paragraph | <code>outre les données</code> | opening overwritten | low |
| 83 | 180 | first sequence | <code>plain strokes between 0,E°,E,F</code> | arrows without clearly visible heads | medium |
| 83 | 180 | after second sequence | <code>Choisissons scindage</code> | initial word and missing article uncertain | low |
| 83 | 181 | first sentence | <code>ssi</code> | si | medium |
| 83 | 181 | item 2 map | <code>plain line M° — M</code> | arrow without visible head | medium |
| 83 | 181 | ideal formula | <code>L″^{-1}</code> | L^{-1}; small primes unclear | medium |
| 83 | 181 | crossed parenthesis term | <code>M/M°</code> | overwritten ink | low |
| 83 | 183 | subscript deletion | <code>(xy)</code> | crossed characters partly covered | low |
| 83 | 183 | last paragraph | <code>ens.</code> | un | medium |
| 83 | 183 | exterior power | <code>Λ^4 A</code> | A faint or compressed | medium |
| 83 | 183 | Azumaya algebra letter | <code>calligraphic A</code> | Plain A possible at first retraced occurrence; looped form compared with scan190. | medium |
| 83 | 184 | xy+yx formula | <code>Tr(xy).1</code> | extra mark after Tr(xy) might be cancelled 1 | low |
| 83 | 184 | boxed first summand | <code>bt</code> | b″t″; primes overwritten | low |
| 83 | 184 | diagonal cancellation | <code>whole lower argument cancelled</code> | extent inferred from continuous strike from Mais to matrix | high |
| 83 | 184 | first linear system | <code>bα; b′α insertion</code> | overwriting of prime and factor | medium |
| 83 | 185 | margin definition | <code>ε_0=[α∧α′∧x_0∧y_0)e^{-1}</code> | first Greek letter and closing bracket uncertain | low |
| 83 | 185 | overwritten factors | <code>1 replaced by 1/2, 1/4</code> | overwriting prevents certainty about earlier factor | low |
| 83 | 185 | formal coefficient ring | <code>Q[[x_ij,y_ij,z_ij]]</code> | double brackets visible; not normalized to polynomial ring | medium |
| 83 | 186 | first display | <code>τ′−τ</code> | written order conflicts with earlier τ,τ′ definitions; not corrected | high |
| 83 | 186 | deleted coefficient | <code>ε</code> | overwritten scalar | low |
| 83 | 186 | cancelled wedge factor | <code>x_0∧y_0∧α∧α′</code> | partly under replacement | low |
| 83 | 187 | crossed polynomial | <code>full first polynomial and extra γ line</code> | indices under cancellation strokes uncertain | low |
| 83 | 187 | final scalar coefficient | <code>η</code> | ρ | medium |
| 83 | 187 | t definition | <code>deleted circle-like superscript</code> | overwritten prime may be present | low |
| 83 | 188 | deleted term after Tr(u) | <code>φ(u,1)</code> | overwritten characters not secure | low |
| 83 | 188 | right marginal mark | <code>où</code> | short stroke and diacritic may be abandoned word | low |
| 83 | 189 | first paragraph | <code>bébête</code> | bête | medium |
| 83 | 189 | group symbol | <code>\mathfrak{S}_3</code> | calligraphic S&#95;3 | medium |
| 83 | 190 | Azumaya rank | <code>2</code> | no silently supplied 4 | medium |
| 83 | 190 | underlined variables | <code>B,B′,B″; C,C′,C″</code> | b,b′,b″; c,c′,c″; capitals strongly formed | medium |
| 83 | 190 | C″ definition | <code>det y</code> | det z | medium |
| 83 | 190 | engendrée | <code>engendrée</code> | engendré | medium |
| 83 | 191 | cancelled connective | <code>termes</code> | word crossed horizontally | low |
| 83 | 191 | equations note | <code>séparément</code> | séparém. | medium |
| 83 | 192 | last line | <code>polynômes</code> | polynomiales | medium |
| 83 | 192 | dual notation | <code>check A^4</code> | vee above A, not prime | high |
| 83 | 193 | counting parenthesis | <code>correspondants aux copies de Num. à 4 éléments</code> | Middle words very compressed; no secure alternative. | low |
| 83 | 193 | bottom coefficient ring | <code>t_i,t_j,t_k</code> | Single subscripts visible despite earlier pair-indexed notation. | medium |
| 83 | 193 | dimension paragraph deletion | <code>deux</code> | The overwritten word is heavily struck. | low |
| 83 | 194 | upper connective | <code>Ce fait</code> | Possibly compressed Ce qui fait, but no distinct qui visible. | low |
| 83 | 194 | rank claim connector | <code>aux&#124;avec</code> | Short word after sur A not secure. | low |
| 83 | 194 | lower generators indices | <code>b_i,c_j,t_{k,l}</code> | Compressed subscripts. | medium |
| 83 | 195 | lower three factors | <code>\mathbf O^3&#124;\mathbf A^3</code> | Oval capitals with a vertical or diagonal inner stroke; not secure. | low |
| 83 | 195 | lower diagram edges | <code>dash</code> | Most connecting strokes have no visible head; top A-to-B has clear upward head. | medium |
| 83 | 195 | top cancelled barred alpha | <code>\bar\alpha prime</code> | Prime/overwriting at upper alpha unclear. | medium |
| 83 | 195 | lower sentence | <code>fidèl superscript t</code> | Compressed faithful-action abbreviation. | medium |
| 83 | 196 | typescript overstrikes throughout | <code>readable deleted phrases with unsure marks</code> | Some stacked type and cross-hatching obscure individual letters; all surviving phrases attempted. | low |
| 83 | 196 | middle paragraph | <code>était&#124;été perdu</code> | First reading follows visible typed sequence; grammatical expectation deliberately not substituted. | medium |
| 83 | 196 | middle paragraph | <code>semble-tèil</code> | Overtyped punctuation/letter after t unclear. | low |
| 83 | 196 | near end of long paragraph | <code>le moment replaced by l’époque</code> | Blue replacement is heavily superimposed. | low |
| 83 | 196 | near exercice | <code>du&#124;un; inserted cancelled pur and de</code> | Layered correction not securely resolved even after enlargement. | low |
| 83 | 196 | lower paragraph | <code>continuation</code> | Typewriter overstrike could hide a different ending. | low |
| 83 | 196 | footnote markers | <code>*&#124;x</code> | Dense typewriter superscript mark, no note text on this sheet. | medium |
| 83 | 196 | before exercice | <code>aride over deleted pur</code> | Blue overlay partly merges with typed pur; de alone was the first reading. | low |
| 83 | 196 | blue addition in first paragraph | <code>futiles</code> | fertiles; compressed middle strokes uncertain. | medium |
| 83 | 197 | cancelled equation first subscript | <code>t14&#124;t1234</code> | Heavily crossed and overwritten. | low |
| 83 | 197 | label under Tr x3x4 | <code>b34&#124;t34</code> | Looped initial letter looks b; earlier notation would suggest t. | low |
| 83 | 197 | underlined t234 annotation | <code>9&#124;?</code> | Closed loop with downward stem. | low |
| 83 | 197 | last pair trace in base ring | <code>t24&#124;t34</code> | Visible first digit resembles 2 and repeats previous pair. | medium |
| 83 | 198 | upper typed cancellation | <code>en représentent aussi les points</code> | Exact plural/last noun obscured by X overstrikes. | low |
| 83 | 198 | upper paragraph at right edge | <code>évoluant en silence</code> | First word partly clipped and overstruck across line break. | low |
| 83 | 198 | lower paragraph | <code>asses&#124;assez</code> | Terminal letter has visible s-form. | medium |
| 83 | 198 | middle paragraph after feminine | <code>cancelled comma</code> | Tiny sub-baseline overstrike may be punctuation. | low |
| 83 | 199 | right degree annotations | <code>A^S4; A^S3; B^S4</code> | Alphabets, superscripts, and overwritten numerals densely layered. | low |
| 83 | 199 | polynomial exponents | <code>8&#124;infinity</code> | Horizontally rounded figure-eight. | medium |
| 83 | 199 | cube labels | <code>t with dots; c_i; 1</code> | Tiny subscripts, especially c&#95;i, less certain. | low |
| 83 | 199 | bottom stables par | <code>+ S3+</code> | Separate plus-shaped stroke before group. | low |
| 83 | 199 | lower-left g action | <code>g tau&#124;g bar tau</code> | Extra stroke on first tau. | low |
| 83 | 200 | typed first line under ink blot | <code>je</code> | Lower portions remain visible; blot hides upper j. | medium |
| 83 | 200 | typed end of autre | <code>cancelled d</code> | Overtyped last mark. | low |
| 83 | 200 | typed last punctuation | <code>cancelled full stop</code> | Small overstrike next to comma. | low |
| 83 | 200 | upper diagram | <code>B1</code> | Subscript heavy but reads1. | medium |
| 83 | 201 | face labels | <code>f</code> | Long looped descenders distinguish from g by repeated face usage and visible upper stroke. | medium |
| 83 | 201 | middle difference equation | <code>=&#124;-</code> | Faint connector immediately before Sigma. | low |
| 83 | 201 | middle rearrangement | <code>dot&#124;plus</code> | Small centred loop without clear vertical arm. | low |
| 83 | 201 | tilde positions | <code>on indices f,a</code> | Waves lie over the lower letters, not over tau/Sigma. | medium |
| 83 | 201 | cube first labels | <code>bar a,bar a prime,f prime,f double prime</code> | Small writing over edges and diagonals. | medium |
| 83 | 202 | upper overtyped articles | <code>des replaced by les</code> | First letters overwritten by handwritten loops. | medium |
| 83 | 202 | middle parenthesis | <code>inconvenante</code> | Typed t before final e is visible, although une was inserted above. | medium |
| 83 | 202 | middle comparison | <code>outée</code> | outrée; r very faint or absent in typing; ink-first order confirmed in the second audit | low |
| 83 | 202 | bottom cancellation | <code>dérision ou mépris</code> | First two words obscured by typewriter X overstrikes. | low |
| 83 | 202 | bottom relocated parenthesis | <code>parmi de nombreux autres</code> | Blue enclosure and long arrow point to immediately after dégradation; encoded once at target with inserted. | high |
| 83 | 202 | footnote symbols | <code>*&#124;x; **&#124;xx</code> | Typewriter superscripts; no footnotes on sheet. | medium |
| 83 | 203 | top list fifth symbol | <code>Sigma_BA prime&#124;Sigma_BC prime</code> | Second capital overwritten. | low |
| 83 | 203 | top cube lower diagonal | <code>w</code> | Looks like w; not replaced by an expected edge label. | low |
| 83 | 203 | bottom sums | <code>plus or minus signs</code> | Several short horizontal strokes lack clear vertical arms; individually marked. | low |
| 83 | 203 | curved arrows between first six equations | <code>1→4,2→5,3→6</code> | Strokes overlap; these are best visible endpoints. | medium |
| 83 | 203 | lower marginal sentence | <code>qui&#124;que donne</code> | Final short relative word compressed. | low |
| 83 | 204 | upper cancelled phrase | <code>en représentent aussi les points</code> | Typewriter overstrike and new handwriting overlap. | low |
| 83 | 204 | upper right cancelled word at line break | <code>évoluant en silence</code> | First word partly clipped; same printed draft state as scan198. | low |
| 83 | 204 | lower inserted temporal phrase | <code>après seulement,&#124;alors seulement,</code> | First word compressed; not expanded from expected sense. | low |
| 83 | 204 | typed stupéfiant sentence | <code>asses&#124;assez</code> | Visible final s retained as first reading. | medium |
| 83 | 204 | new blue correction replacing névralgique | <code>partie la plus délicate et la plus essentielle</code> | Partie lies over plus in prior insertion; encoded at the replacement target. | medium |
| 83 | 205 | top right | <code>b_a=t_bar a</code> | first letter looks like b, whereas earlier box has t&#95;a | medium |
| 83 | 205 | triple and face trace symbol | <code>mathcal T</code> | large retraced T with hooked foot; alphabet uncertain | low |
| 83 | 205 | second sigma expansion | <code>b_s2 b_ss2</code> | second factor resembles b, alternative t | medium |
| 83 | 205 | last pi line | <code>b_ss1,c_ss2</code> | extra s-like strokes in indices retained, alternatives single s&#95;j | low |
| 83 | 205 | crossed old pi line | <code>c_s1 t_ss1 squared plus cyclic terms</code> | superscripts under cancellation | low |
| 83 | 207 | sigma&#95;a second expression | <code>t_a prime a doubleprime</code> | heavily overwritten edge index; underbrace label t&#95;a doubleprime uncertain | low |
| 83 | 207 | crossed line under trace formula | <code>t_s+t</code> | first index and unfinished second term crossed | low |
| 83 | 207 | pi variable list deleted prefix | <code>Tr X_i,d</code> | last letter partly hidden by cancellation | low |
| 83 | 208 | 448, parenthesis il apparait | <code>est apparu</code> | blue overtyping of word ending and marginal est; exact final verb uncertain | medium |
| 83 | 208 | 448, deleted type under Je | <code>Parmi ces editeurs j en conn</code> | typewriter x-overstrike obscures terminal partial word | low |
| 83 | 208 | 450, note number | <code>169_7;169_2</code> | last digit and lowered final digit uncertain; handwritten alternative167&#95;2 | low |
| 83 | 208 | 452, right edge | <code>concrete;vive;pressenti</code> | rightmost letters cut by photocopy edge; readings marked in text | medium |
| 83 | 208 | 452, x-overstruck words | <code>la pulsion de;motivations profon;entrev</code> | partial underlying type remains but terminal letters not secure | low |
| 83 | 209 | large cube, front-right edge | <code>v=u-(d-b)</code> | operation after u is a blackened dash or dot | medium |
| 83 | 209 | large cube, bottom circled label | <code>a prime</code> | possible two strokes rather than one prime | medium |
| 83 | 209 | bottom alternative parametrization | <code>a!</code> | a prime possible; dot of apparent exclamation overlaps faint reverse type | low |
| 83 | 209 | boxed equality continuation | <code>d-b-=u-v</code> | extra horizontal stroke retained as uncertain -= | low |
| 83 | 210 | first paragraph | <code>passionantes;passionant</code> | single n retained from type; not modernized | high |
| 83 | 210 | first paragraph end | <code>edrire</code> | middle consonant looks d; alternative ecrire | medium |
| 83 | 210 | second paragraph | <code>qu un Dr. K.F</code> | overstruck deleted draft | low |
| 83 | 210 | third paragraph | <code>falla</code> | last vowel appears a with accent rather than u | medium |
| 83 | 210 | final paragraph | <code>eleges</code> | typed v resembles g; not silently corrected | medium |
| 83 | 211 | top caption | <code>les sommes</code> | first two words reduced to connected strokes | low |
| 83 | 211 | crossed parameter clause | <code>=a+alpha</code> | very heavy overstrike | low |
| 83 | 211 | S&#95;2 prime coefficient | <code>4c</code> | digit 4 retraced over possible3 | medium |
| 83 | 211 | S&#95;2 prime alpha | <code>alpha with a prime-a written above</code> | curved callout could indicate replacement, no confident cancellation inferred | medium |
| 83 | 212 | first paragraph | <code>reglement</code> | overprinted initial letter | medium |
| 83 | 212 | second paragraph | <code>ccllegues</code> | second letter looks c rather than o in faded copy | medium |
| 83 | 212 | last line | <code>s evanouissent</code> | blue s seems to restore missing or faint second s; layered spelling uncertain | medium |
| 83 | 213 | middle text | <code>reste pour expr.</code> | last abbreviated word reduced to long strokes | low |
| 83 | 213 | gamma solution | <code>+delta doubleprime+b</code> | plus is visible despite preceding relation b-gamma=delta doubleprime | high |
| 83 | 213 | bottom superscripts on delta | <code>double prime or4</code> | two upper strokes merge to4/u shape; retained uncertainty | medium |
| 83 | 213 | beta prime solution prefix | <code>vertical stroke</code> | possible cancelled unfinished sign before plus | low |
| 83 | 214 | first paragraph deletion | <code>d il y avait</code> | x-overstrike; letters d il y avai visible | low |
| 83 | 214 | letter salutation close | <code>Recevez</code> | v/g overprint | medium |
| 83 | 214 | last insertion | <code>faits (depuis treize ans) deja</code> | number word and final heavily cancelled word uncertain | low |
| 83 | 214 | deleted clause before Et je | <code>Par contre, dans les annees qui m</code> | partial clause cut by right margin and x-overstrike | low |
| 83 | 214 | after X années | <code>certes,</code> | civils,; blue cursive insertion, enlarged during audit | low |
| 83 | 215 | second box | <code>delta prime</code> | thick initial loop overlaps other stroke | medium |
| 83 | 215 | last underbrace | <code>epsilon_2</code> | index looks2 though third in list, alternative3 | medium |
| 83 | 215 | sum of deltas | <code>double prime or4</code> | same joined superscript strokes as scan213 | medium |
| 83 | 216 | first paragraph heavy blackout | <code>role plus about five unreadable words</code> | original typed line examined enlarged at4x; dense black ink physically covers characters | low |
| 83 | 216 | blue top insertion | <code>ni la derniere que je suis souffle</code> | quotation word and parenthesis boundaries uncertain | medium |
| 83 | 216 | de principe correction | <code>serait</code> | blue s before typed etait; ending appears retained | medium |
| 83 | 216 | solutionnqui | <code>n</code> | extra type between solution and qui retained as uncertain | medium |
| 83 | 216 | German closing | <code>ho[a]chachtungsvoll</code> | overstruck extra character after ho | medium |
| 83 | 217 | alpha and gamma prime formulas | <code>minus before b prime-b</code> | operation blackened, alternative plus | medium |
| 83 | 217 | beta formula | <code>-(a prime-a)</code> | inner operation blackened | medium |
| 83 | 217 | alpha prime formula | <code>b+b^3</code> | prime as alternative; raised mark looks like 3 in enlarged audit | medium |
| 83 | 217 | beta prime formula | <code>extra c before c prime-c</code> | visible opening stroke could be duplicated parenthesis | low |
| 83 | 217 | bottom caption | <code>Sommes</code> | letters compressed | medium |
| 83 | 217 | cancelled lower right | <code>le facteur 2 est partout !</code> | les signes sont partout !; cancellation heavily covers the letters, enlarged audit | low |
| 83 | 218 | decence | <code>c</code> | blue blot over first c; remaining letterform uncertain | medium |
| 83 | 218 | section reference | <code>9 with deleted5</code> | blue crossing could instead correct underlying digit to5 | low |
| 83 | 218 | right margin next to premiere partie | <code>(!)</code> | small dark mark resembles parenthesized exclamation; possible copy blemish | low |
| 83 | 218 | last cancelled text | <code>Cette constat</code> | typewriter x-overstrike over unfinished clause | low |
| 83 | 219 | first matrix entry | <code>-1</code> | vertical digit blackened | medium |
| 83 | 219 | lower-left cancelled number | <code>27</code> | crossed strokes | low |
| 83 | 219 | isolated approval | <code>OK</code> | K has V-shaped second stroke | medium |
| 83 | 220 | first paragraph quoted word | <code>bonbinage</code> | middle character resembles n, alternative m; no normalization | medium |
| 83 | 220 | second paragraph | <code>pbus;pervenant</code> | typed letterforms retained with possible alternatives plus;parvenant | medium |
| 83 | 220 | after amis | <code>two opening parentheses</code> | first weak parenthesis may be copy impression | low |
| 83 | 220 | top isolated mark | <code>1</code> | short rotated mark above typescript, identity uncertain | low |
| 83 | 221 | left A′,C′ equations | <code>+</code> | The small joining strokes look like plus signs; a minus is also possible. | low |
| 83 | 221 | lower-left sums | <code>+</code> | Very cursive horizontal strokes, each retained with minus alternative. | medium |
| 83 | 221 | last display, before c | <code>−</code> | The visible stroke is horizontal; + is the mathematical expectation but not imposed. | low |
| 83 | 221 | cancelled sign below first group | <code>β</code> | Retraced, blacked sign; reading only conjectural. | low |
| 83 | 222 | first paragraph, qui est un aspect | <code>en; juste</code> | The first blue insertion follows qui; the second appears juste, with partie an alternative. | low |
| 83 | 222 | first paragraph, deleted fragments | <code>que; parf; inspiration; s′</code> | Typewriter x overstrikes partly obscure the original letters. | low |
| 83 | 222 | Siegel parenthesis | <code>****</code> | The number of closely struck asterisks is uncertain; an outer closing parenthesis is not clearly present. | medium |
| 83 | 222 | dessèchement, line ending | <code>men</code> | three overstruck letters; highly tentative reading under typed x strokes | low |

## Occurrence-level concordance

Line numbers refer to `pages/MPL_83_178-222_83_scanNNN.tex`, not the combined fragment or manuscript lines. Every balanced-brace occurrence of `\unsure` or `\illegible` is included, including nested occurrences inside deletions, insertions, and other macros. Alternatives are split only at unescaped vertical bars outside nested braces; no mathematical or linguistic interpretation is applied.

The confidence entries in this concordance are mechanical defaults: **medium** for `\unsure` and **low** for `\illegible`. They are not a fresh assessment and do not supersede the reader-recorded confidence above. For `\illegible`, the reading/argument column gives the macro's argument.

| File | Scan | Page-file line | Macro | Reading / argument | Alternatives | Default confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 83 | 178 | 5 | <code>\unsure</code> | <code>f</code> | <code></code> | medium |
| 83 | 178 | 7 | <code>\unsure</code> | <code>etc.</code> | <code></code> | medium |
| 83 | 178 | 9 | <code>\unsure</code> | <code>semi-hom.</code> | <code></code> | medium |
| 83 | 178 | 14 | <code>\unsure</code> | <code>canon. $i$-linéaire</code> | <code></code> | medium |
| 83 | 178 | 16 | <code>\unsure</code> | <code>tout</code> | <code></code> | medium |
| 83 | 178 | 27 | <code>\unsure</code> | <code>\alpha_1</code> | <code></code> | medium |
| 83 | 178 | 30 | <code>\unsure</code> | <code>im.</code> | <code></code> | medium |
| 83 | 178 | 30 | <code>\unsure</code> | <code>considérer</code> | <code></code> | medium |
| 83 | 178 | 31 | <code>\unsure</code> | <code>v_i</code> | <code></code> | medium |
| 83 | 178 | 32 | <code>\unsure</code> | <code>pour celles qui sont</code> | <code></code> | medium |
| 83 | 178 | 32 | <code>\unsure</code> | <code>se donner un</code> | <code></code> | medium |
| 83 | 178 | 32 | <code>\unsure</code> | <code>\to</code> | <code>-</code> | medium |
| 83 | 178 | 32 | <code>\unsure</code> | <code>avec</code> | <code></code> | medium |
| 83 | 178 | 32 | <code>\unsure</code> | <code>v_i</code> | <code></code> | medium |
| 83 | 178 | 38 | <code>\unsure</code> | <code>en nb premiers</code> | <code></code> | medium |
| 83 | 178 | 38 | <code>\unsure</code> | <code>d'ordre</code> | <code></code> | medium |
| 83 | 179 | 2 | <code>\unsure</code> | <code>f^\circ</code> | <code></code> | medium |
| 83 | 179 | 2 | <code>\unsure</code> | <code>(soit $g$)</code> | <code></code> | medium |
| 83 | 179 | 2 | <code>\unsure</code> | <code>ation</code> | <code></code> | medium |
| 83 | 179 | 4 | <code>\unsure</code> | <code>aura donc</code> | <code></code> | medium |
| 83 | 179 | 10 | <code>\unsure</code> | <code>f(x_1,\alpha_2)</code> | <code></code> | medium |
| 83 | 179 | 15 | <code>\unsure</code> | <code>par</code> | <code></code> | medium |
| 83 | 179 | 22 | <code>\unsure</code> | <code>veut</code> | <code></code> | medium |
| 83 | 179 | 24 | <code>\unsure</code> | <code>x_1</code> | <code>X_1</code> | medium |
| 83 | 180 | 5 | <code>\unsure</code> | <code>ext.</code> | <code></code> | medium |
| 83 | 180 | 5 | <code>\unsure</code> | <code>b_i</code> | <code></code> | medium |
| 83 | 180 | 5 | <code>\unsure</code> | <code>\to</code> | <code>-</code> | medium |
| 83 | 180 | 5 | <code>\unsure</code> | <code>can.</code> | <code></code> | medium |
| 83 | 180 | 5 | <code>\unsure</code> | <code>\to</code> | <code>-</code> | medium |
| 83 | 180 | 6 | <code>\unsure</code> | <code>t</code> | <code></code> | medium |
| 83 | 180 | 8 | <code>\unsure</code> | <code>O</code> | <code></code> | medium |
| 83 | 180 | 8 | <code>\unsure</code> | <code>outre</code> | <code></code> | medium |
| 83 | 180 | 8 | <code>\unsure</code> | <code>données</code> | <code></code> | medium |
| 83 | 180 | 14 | <code>\unsure</code> | <code>Donc les</code> | <code></code> | medium |
| 83 | 180 | 14 | <code>\unsure</code> | <code>Choisissons</code> | <code></code> | medium |
| 83 | 180 | 16 | <code>\unsure</code> | <code>k\to k</code> | <code></code> | medium |
| 83 | 181 | 2 | <code>\unsure</code> | <code>\to</code> | <code>-</code> | medium |
| 83 | 181 | 2 | <code>\unsure</code> | <code>e</code> | <code></code> | medium |
| 83 | 181 | 8 | <code>\unsure</code> | <code>\to</code> | <code>-</code> | medium |
| 83 | 181 | 12 | <code>\unsure</code> | <code>M/M^\circ</code> | <code></code> | medium |
| 83 | 181 | 14 | <code>\unsure</code> | <code>L''</code> | <code></code> | medium |
| 83 | 183 | 4 | <code>\unsure</code> | <code>\mathcal{A}</code> | <code>A</code> | medium |
| 83 | 183 | 4 | <code>\unsure</code> | <code>associée</code> | <code></code> | medium |
| 83 | 183 | 11 | <code>\unsure</code> | <code>(xy)</code> | <code></code> | medium |
| 83 | 183 | 21 | <code>\unsure</code> | <code>ens.</code> | <code></code> | medium |
| 83 | 184 | 8 | <code>\unsure</code> | <code>1</code> | <code></code> | medium |
| 83 | 184 | 12 | <code>\unsure</code> | <code>(xy)z+</code> | <code></code> | medium |
| 83 | 184 | 16 | <code>\unsure</code> | <code>bt</code> | <code>b''t''</code> | medium |
| 83 | 184 | 22 | <code>\unsure</code> | <code>det</code> | <code></code> | medium |
| 83 | 184 | 34 | <code>\unsure</code> | <code>b</code> | <code></code> | medium |
| 83 | 184 | 35 | <code>\unsure</code> | <code>b\alpha</code> | <code></code> | medium |
| 83 | 185 | 6 | <code>\unsure</code> | <code>e^{-1}</code> | <code></code> | medium |
| 83 | 185 | 19 | <code>\unsure</code> | <code>1</code> | <code></code> | medium |
| 83 | 185 | 19 | <code>\unsure</code> | <code>\tfrac12</code> | <code></code> | medium |
| 83 | 185 | 19 | <code>\unsure</code> | <code>\varepsilon</code> | <code></code> | medium |
| 83 | 185 | 23 | <code>\unsure</code> | <code>1</code> | <code></code> | medium |
| 83 | 185 | 23 | <code>\unsure</code> | <code>\tfrac12</code> | <code></code> | medium |
| 83 | 185 | 30 | <code>\unsure</code> | <code>1</code> | <code></code> | medium |
| 83 | 185 | 30 | <code>\unsure</code> | <code>\tfrac14</code> | <code></code> | medium |
| 83 | 185 | 34 | <code>\unsure</code> | <code>1</code> | <code></code> | medium |
| 83 | 185 | 34 | <code>\unsure</code> | <code>\tfrac14</code> | <code></code> | medium |
| 83 | 186 | 9 | <code>\unsure</code> | <code>\varepsilon</code> | <code></code> | medium |
| 83 | 186 | 34 | <code>\unsure</code> | <code>x_0\wedge y_0\wedge\alpha\wedge\alpha'</code> | <code></code> | medium |
| 83 | 186 | 40 | <code>\unsure</code> | <code>x,y</code> | <code></code> | medium |
| 83 | 187 | 3 | <code>\unsure</code> | <code>quatre</code> | <code></code> | medium |
| 83 | 187 | 9 | <code>\unsure</code> | <code>\gamma</code> | <code></code> | medium |
| 83 | 187 | 9 | <code>\unsure</code> | <code>t</code> | <code></code> | medium |
| 83 | 187 | 9 | <code>\unsure</code> | <code>t'</code> | <code></code> | medium |
| 83 | 187 | 11 | <code>\unsure</code> | <code>\eta</code> | <code></code> | medium |
| 83 | 187 | 24 | <code>\unsure</code> | <code>\circ</code> | <code></code> | medium |
| 83 | 188 | 16 | <code>\unsure</code> | <code>\varphi(u,1)</code> | <code></code> | medium |
| 83 | 188 | 34 | <code>\unsure</code> | <code>où</code> | <code></code> | medium |
| 83 | 189 | 2 | <code>\unsure</code> | <code>bébête</code> | <code></code> | medium |
| 83 | 190 | 2 | <code>\unsure</code> | <code>2</code> | <code></code> | medium |
| 83 | 190 | 4 | <code>\unsure</code> | <code>B</code> | <code>b</code> | medium |
| 83 | 190 | 4 | <code>\unsure</code> | <code>B'</code> | <code>b'</code> | medium |
| 83 | 190 | 4 | <code>\unsure</code> | <code>B''</code> | <code>b''</code> | medium |
| 83 | 190 | 9 | <code>\unsure</code> | <code>B</code> | <code>b</code> | medium |
| 83 | 190 | 9 | <code>\unsure</code> | <code>B'</code> | <code>b'</code> | medium |
| 83 | 190 | 9 | <code>\unsure</code> | <code>B''</code> | <code>b''</code> | medium |
| 83 | 190 | 10 | <code>\unsure</code> | <code>y</code> | <code>z</code> | medium |
| 83 | 190 | 14 | <code>\unsure</code> | <code>engendrée</code> | <code></code> | medium |
| 83 | 190 | 22 | <code>\unsure</code> | <code>et</code> | <code></code> | medium |
| 83 | 191 | 11 | <code>\unsure</code> | <code>termes</code> | <code></code> | medium |
| 83 | 191 | 15 | <code>\unsure</code> | <code>ément</code> | <code></code> | medium |
| 83 | 192 | 32 | <code>\unsure</code> | <code>polynômes</code> | <code></code> | medium |
| 83 | 193 | 10 | <code>\unsure</code> | <code>t</code> | <code></code> | medium |
| 83 | 193 | 11 | <code>\unsure</code> | <code>\mathcal P</code> | <code>P</code> | medium |
| 83 | 193 | 14 | <code>\unsure</code> | <code>deux</code> | <code></code> | medium |
| 83 | 193 | 24 | <code>\unsure</code> | <code>correspondants</code> | <code></code> | medium |
| 83 | 193 | 24 | <code>\unsure</code> | <code>copies de Num.</code> | <code></code> | medium |
| 83 | 194 | 4 | <code>\unsure</code> | <code>Ce fait</code> | <code>Ça fait</code> | medium |
| 83 | 194 | 10 | <code>\unsure</code> | <code>aux</code> | <code>avec</code> | medium |
| 83 | 195 | 7 | <code>\unsure</code> | <code>\bar\alpha'</code> | <code></code> | medium |
| 83 | 195 | 23 | <code>\unsure</code> | <code>fidèl\textsuperscript{t}</code> | <code></code> | medium |
| 83 | 195 | 25 | <code>\unsure</code> | <code>\mathbb Z</code> | <code></code> | medium |
| 83 | 195 | 26 | <code>\unsure</code> | <code>\mathbf O^3</code> | <code>\mathbf A^3</code> | medium |
| 83 | 195 | 27 | <code>\unsure</code> | <code>\mathbf O^3</code> | <code>\mathbf A^3</code> | medium |
| 83 | 195 | 28 | <code>\unsure</code> | <code>\mathbf O^3</code> | <code>\mathbf A^3</code> | medium |
| 83 | 195 | 33 | <code>\unsure</code> | <code>=</code> | <code></code> | medium |
| 83 | 195 | 34 | <code>\unsure</code> | <code>\mathbb Z</code> | <code></code> | medium |
| 83 | 195 | 36 | <code>\unsure</code> | <code>t</code> | <code></code> | medium |
| 83 | 196 | 4 | <code>\unsure</code> | <code>burin</code> | <code></code> | medium |
| 83 | 196 | 6 | <code>\unsure</code> | <code>idée, vision,</code> | <code></code> | medium |
| 83 | 196 | 7 | <code>\unsure</code> | <code>idée, même si clairement conçue et formulée soit-elle</code> | <code></code> | medium |
| 83 | 196 | 8 | <code>\unsure</code> | <code>futiles</code> | <code>fertiles</code> | medium |
| 83 | 196 | 10 | <code>\unsure</code> | <code>u</code> | <code></code> | medium |
| 83 | 196 | 11 | <code>\unsure</code> | <code>et avec</code> | <code></code> | medium |
| 83 | 196 | 13 | <code>\unsure</code> | <code>d'</code> | <code></code> | medium |
| 83 | 196 | 18 | <code>\unsure</code> | <code>un</code> | <code></code> | medium |
| 83 | 196 | 19 | <code>\unsure</code> | <code>*</code> | <code>x</code> | medium |
| 83 | 196 | 20 | <code>\unsure</code> | <code>*</code> | <code>x</code> | medium |
| 83 | 196 | 24 | <code>\unsure</code> | <code>s</code> | <code></code> | medium |
| 83 | 196 | 26 | <code>\unsure</code> | <code>dans l'inconscient</code> | <code></code> | medium |
| 83 | 196 | 30 | <code>\unsure</code> | <code>était</code> | <code>été</code> | medium |
| 83 | 196 | 33 | <code>\unsure</code> | <code>e</code> | <code></code> | medium |
| 83 | 196 | 35 | <code>\unsure</code> | <code>général</code> | <code></code> | medium |
| 83 | 196 | 36 | <code>\unsure</code> | <code>è</code> | <code>'</code> | medium |
| 83 | 196 | 38 | <code>\unsure</code> | <code>des stades de la pensée</code> | <code></code> | medium |
| 83 | 196 | 39 | <code>\unsure</code> | <code>à notre</code> | <code></code> | medium |
| 83 | 196 | 40 | <code>\unsure</code> | <code>à la</code> | <code></code> | medium |
| 83 | 196 | 44 | <code>\unsure</code> | <code>etc</code> | <code></code> | medium |
| 83 | 196 | 48 | <code>\unsure</code> | <code>l'époque</code> | <code></code> | medium |
| 83 | 196 | 49 | <code>\unsure</code> | <code>du</code> | <code>un</code> | medium |
| 83 | 196 | 50 | <code>\unsure</code> | <code>aride</code> | <code>de</code> | medium |
| 83 | 196 | 57 | <code>\unsure</code> | <code>anticipe ou</code> | <code></code> | medium |
| 83 | 196 | 58 | <code>\unsure</code> | <code>continuation</code> | <code></code> | medium |
| 83 | 196 | 61 | <code>\unsure</code> | <code>ée</code> | <code></code> | medium |
| 83 | 196 | 62 | <code>\unsure</code> | <code>celle</code> | <code></code> | medium |
| 83 | 196 | 64 | <code>\unsure</code> | <code>la</code> | <code></code> | medium |
| 83 | 197 | 10 | <code>\unsure</code> | <code>t_{14}</code> | <code>t_{1234}</code> | medium |
| 83 | 197 | 25 | <code>\unsure</code> | <code>b_{3,4}</code> | <code>t_{3,4}</code> | medium |
| 83 | 197 | 35 | <code>\unsure</code> | <code>9</code> | <code>?</code> | medium |
| 83 | 197 | 40 | <code>\unsure</code> | <code>t_{24}</code> | <code>t_{34}</code> | medium |
| 83 | 198 | 8 | <code>\unsure</code> | <code>en représentent aussi les points</code> | <code></code> | medium |
| 83 | 198 | 13 | <code>\unsure</code> | <code>évoluant en silence</code> | <code></code> | medium |
| 83 | 198 | 17 | <code>\unsure</code> | <code>,</code> | <code></code> | medium |
| 83 | 198 | 36 | <code>\unsure</code> | <code>asses</code> | <code>assez</code> | medium |
| 83 | 199 | 11 | <code>\unsure</code> | <code>x_4</code> | <code></code> | medium |
| 83 | 199 | 36 | <code>\unsure</code> | <code>c</code> | <code></code> | medium |
| 83 | 199 | 41 | <code>\unsure</code> | <code>\tau</code> | <code></code> | medium |
| 83 | 199 | 42 | <code>\unsure</code> | <code>8</code> | <code>\infty</code> | medium |
| 83 | 199 | 52 | <code>\unsure</code> | <code>A^{\mathfrak S_4}</code> | <code></code> | medium |
| 83 | 199 | 53 | <code>\unsure</code> | <code>A^{\mathfrak S_3}</code> | <code></code> | medium |
| 83 | 199 | 54 | <code>\unsure</code> | <code>B^{\mathfrak S_4}</code> | <code></code> | medium |
| 83 | 199 | 55 | <code>\unsure</code> | <code>4</code> | <code></code> | medium |
| 83 | 199 | 59 | <code>\unsure</code> | <code>\tau</code> | <code>\bar\tau</code> | medium |
| 83 | 199 | 63 | <code>\unsure</code> | <code>8</code> | <code>\infty</code> | medium |
| 83 | 199 | 81 | <code>\unsure</code> | <code>+</code> | <code></code> | medium |
| 83 | 200 | 19 | <code>\unsure</code> | <code>je</code> | <code></code> | medium |
| 83 | 200 | 19 | <code>\unsure</code> | <code>d</code> | <code></code> | medium |
| 83 | 200 | 22 | <code>\unsure</code> | <code>.</code> | <code></code> | medium |
| 83 | 201 | 52 | <code>\unsure</code> | <code>=</code> | <code>-</code> | medium |
| 83 | 201 | 53 | <code>\unsure</code> | <code>\cdot</code> | <code>+</code> | medium |
| 83 | 202 | 3 | <code>\unsure</code> | <code>des</code> | <code></code> | medium |
| 83 | 202 | 5 | <code>\unsure</code> | <code>des</code> | <code></code> | medium |
| 83 | 202 | 5 | <code>\unsure</code> | <code>ou</code> | <code></code> | medium |
| 83 | 202 | 6 | <code>\unsure</code> | <code>,</code> | <code></code> | medium |
| 83 | 202 | 6 | <code>\unsure</code> | <code>ou de</code> | <code></code> | medium |
| 83 | 202 | 8 | <code>\unsure</code> | <code>s</code> | <code></code> | medium |
| 83 | 202 | 15 | <code>\unsure</code> | <code>,</code> | <code></code> | medium |
| 83 | 202 | 21 | <code>\unsure</code> | <code>s</code> | <code></code> | medium |
| 83 | 202 | 22 | <code>\unsure</code> | <code>,</code> | <code></code> | medium |
| 83 | 202 | 22 | <code>\unsure</code> | <code>inconvenante</code> | <code></code> | medium |
| 83 | 202 | 28 | <code>\unsure</code> | <code>outée</code> | <code>outrée</code> | medium |
| 83 | 202 | 31 | <code>\unsure</code> | <code>que dans les</code> | <code></code> | medium |
| 83 | 202 | 38 | <code>\unsure</code> | <code>*</code> | <code>x</code> | medium |
| 83 | 202 | 38 | <code>\unsure</code> | <code>et</code> | <code></code> | medium |
| 83 | 202 | 41 | <code>\unsure</code> | <code>**</code> | <code>xx</code> | medium |
| 83 | 202 | 42 | <code>\unsure</code> | <code>dérision ou mépris</code> | <code></code> | medium |
| 83 | 203 | 12 | <code>\unsure</code> | <code>A</code> | <code></code> | medium |
| 83 | 203 | 15 | <code>\unsure</code> | <code>W</code> | <code>w</code> | medium |
| 83 | 203 | 22 | <code>\unsure</code> | <code>\Sigma_{BA'}</code> | <code>\Sigma_{BC'}</code> | medium |
| 83 | 203 | 62 | <code>\unsure</code> | <code>qui</code> | <code>que</code> | medium |
| 83 | 203 | 65 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 203 | 65 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 203 | 66 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 203 | 68 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 203 | 68 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 203 | 69 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 203 | 69 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 204 | 13 | <code>\unsure</code> | <code>en représentent aussi les points</code> | <code></code> | medium |
| 83 | 204 | 20 | <code>\unsure</code> | <code>évoluant en silence</code> | <code></code> | medium |
| 83 | 204 | 24 | <code>\unsure</code> | <code>,</code> | <code></code> | medium |
| 83 | 204 | 40 | <code>\unsure</code> | <code>après seulement,</code> | <code>alors seulement,</code> | medium |
| 83 | 204 | 46 | <code>\unsure</code> | <code>asses</code> | <code>assez</code> | medium |
| 83 | 205 | 11 | <code>\unsure</code> | <code>b_a</code> | <code>t_a</code> | medium |
| 83 | 205 | 26 | <code>\unsure</code> | <code>\mathcal P</code> | <code>P</code> | medium |
| 83 | 205 | 27 | <code>\unsure</code> | <code>sommets</code> | <code></code> | medium |
| 83 | 205 | 34 | <code>\unsure</code> | <code>\mathcal T</code> | <code>T</code> | medium |
| 83 | 205 | 39 | <code>\unsure</code> | <code>i</code> | <code></code> | medium |
| 83 | 205 | 50 | <code>\unsure</code> | <code>\pi_{\bar s}</code> | <code>\sigma_{\bar s}</code> | medium |
| 83 | 205 | 54 | <code>\unsure</code> | <code>\sigma_s</code> | <code></code> | medium |
| 83 | 205 | 54 | <code>\unsure</code> | <code>b_{ss_2}</code> | <code>t_{ss_2}</code> | medium |
| 83 | 205 | 59 | <code>\unsure</code> | <code>2</code> | <code></code> | medium |
| 83 | 205 | 59 | <code>\unsure</code> | <code>2</code> | <code></code> | medium |
| 83 | 205 | 59 | <code>\unsure</code> | <code>2</code> | <code></code> | medium |
| 83 | 205 | 63 | <code>\unsure</code> | <code>b_{ss_1}^{2}</code> | <code>b_{s_1}^{2}</code> | medium |
| 83 | 205 | 64 | <code>\unsure</code> | <code>b_{ss_2}^{2}</code> | <code>b_{s_2}^{2}</code> | medium |
| 83 | 205 | 65 | <code>\unsure</code> | <code>b_{ss_3}^{2}</code> | <code>b_{s_3}^{2}</code> | medium |
| 83 | 205 | 75 | <code>\unsure</code> | <code>\mathcal T_f=</code> | <code></code> | medium |
| 83 | 205 | 95 | <code>\unsure</code> | <code>NB</code> | <code></code> | medium |
| 83 | 207 | 15 | <code>\unsure</code> | <code>t_s+t</code> | <code></code> | medium |
| 83 | 207 | 16 | <code>\unsure</code> | <code>t_{a'a''}</code> | <code>t_{a''}</code> | medium |
| 83 | 207 | 16 | <code>\unsure</code> | <code>t_{a''}</code> | <code></code> | medium |
| 83 | 207 | 24 | <code>\unsure</code> | <code>d</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>u</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>ma</code> | <code>la</code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>adressé</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>Parmi ces éditeurs j'en conn</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>parmi</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>k</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>n</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>e</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>'a</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>visà</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>l\,u\,i\,-\,m\,ê\deleted{\unsure{e}}\,m\,e</code> | <code></code> | medium |
| 83 | 208 | 6 | <code>\unsure</code> | <code>e</code> | <code></code> | medium |
| 83 | 208 | 13 | <code>\unsure</code> | <code>899</code> | <code></code> | medium |
| 83 | 208 | 13 | <code>\unsure</code> | <code>169_7</code> | <code>169_2</code> | medium |
| 83 | 208 | 13 | <code>\unsure</code> | <code>à travers SGA</code> | <code></code> | medium |
| 83 | 208 | 13 | <code>\unsure</code> | <code>où</code> | <code></code> | medium |
| 83 | 208 | 14 | <code>\unsure</code> | <code>169_2</code> | <code>167_2</code> | medium |
| 83 | 208 | 16 | <code>\unsure</code> | <code>452</code> | <code>451</code> | medium |
| 83 | 208 | 17 | <code>\unsure</code> | <code>--</code> | <code></code> | medium |
| 83 | 208 | 20 | <code>\unsure</code> | <code>concrète</code> | <code></code> | medium |
| 83 | 208 | 20 | <code>\unsure</code> | <code>la pulsion de</code> | <code></code> | medium |
| 83 | 208 | 20 | <code>\unsure</code> | <code>motivations profon</code> | <code></code> | medium |
| 83 | 208 | 20 | <code>\unsure</code> | <code>vive</code> | <code></code> | medium |
| 83 | 208 | 20 | <code>\unsure</code> | <code>entrev</code> | <code></code> | medium |
| 83 | 208 | 20 | <code>\unsure</code> | <code>pressenti</code> | <code></code> | medium |
| 83 | 209 | 10 | <code>\unsure</code> | <code>b'</code> | <code></code> | medium |
| 83 | 209 | 13 | <code>\unsure</code> | <code>u</code> | <code></code> | medium |
| 83 | 209 | 29 | <code>\unsure</code> | <code>-</code> | <code>\cdot</code> | medium |
| 83 | 209 | 34 | <code>\unsure</code> | <code>a'</code> | <code>a''</code> | medium |
| 83 | 209 | 36 | <code>\unsure</code> | <code>-=</code> | <code>=</code> | medium |
| 83 | 209 | 41 | <code>\unsure</code> | <code>a^!</code> | <code>a'</code> | medium |
| 83 | 210 | 3 | <code>\unsure</code> | <code>t</code> | <code></code> | medium |
| 83 | 210 | 3 | <code>\unsure</code> | <code>ne</code> | <code></code> | medium |
| 83 | 210 | 3 | <code>\unsure</code> | <code>édrire</code> | <code>écrire</code> | medium |
| 83 | 210 | 5 | <code>\unsure</code> | <code>qu'un Dr. K.F</code> | <code></code> | medium |
| 83 | 210 | 5 | <code>\unsure</code> | <code>balàder</code> | <code>balader</code> | medium |
| 83 | 210 | 5 | <code>\unsure</code> | <code>à</code> | <code></code> | medium |
| 83 | 210 | 7 | <code>\unsure</code> | <code>*</code> | <code></code> | medium |
| 83 | 210 | 7 | <code>\unsure</code> | <code>fallà</code> | <code>fallu</code> | medium |
| 83 | 210 | 9 | <code>\unsure</code> | <code>élèges</code> | <code>élèves</code> | medium |
| 83 | 210 | 9 | <code>\unsure</code> | <code>qui</code> | <code></code> | medium |
| 83 | 211 | 2 | <code>\unsure</code> | <code>=a+\alpha</code> | <code></code> | medium |
| 83 | 211 | 4 | <code>\unsure</code> | <code>les sommes</code> | <code></code> | medium |
| 83 | 211 | 11 | <code>\unsure</code> | <code>\alpha</code> | <code></code> | medium |
| 83 | 211 | 13 | <code>\unsure</code> | <code>4</code> | <code>\deleted{3}\inserted{4}</code> | medium |
| 83 | 212 | 3 | <code>\unsure</code> | <code>x</code> | <code></code> | medium |
| 83 | 212 | 3 | <code>\unsure</code> | <code>règlement</code> | <code></code> | medium |
| 83 | 212 | 5 | <code>\unsure</code> | <code>ccllègues</code> | <code>collègues</code> | medium |
| 83 | 212 | 5 | <code>\unsure</code> | <code>ci</code> | <code></code> | medium |
| 83 | 212 | 5 | <code>\unsure</code> | <code>s\inserted{s}</code> | <code>ss</code> | medium |
| 83 | 213 | 30 | <code>\unsure</code> | <code>reste pour expr.</code> | <code></code> | medium |
| 83 | 213 | 33 | <code>\unsure</code> | <code>b</code> | <code></code> | medium |
| 83 | 213 | 37 | <code>\unsure</code> | <code>''</code> | <code>4</code> | medium |
| 83 | 213 | 38 | <code>\unsure</code> | <code>\vert</code> | <code>1</code> | medium |
| 83 | 213 | 38 | <code>\unsure</code> | <code>''</code> | <code>4</code> | medium |
| 83 | 213 | 41 | <code>\unsure</code> | <code>''</code> | <code>4</code> | medium |
| 83 | 213 | 42 | <code>\unsure</code> | <code>''</code> | <code>4</code> | medium |
| 83 | 214 | 3 | <code>\unsure</code> | <code>--</code> | <code></code> | medium |
| 83 | 214 | 3 | <code>\unsure</code> | <code>e</code> | <code></code> | medium |
| 83 | 214 | 3 | <code>\unsure</code> | <code>d'il y avait</code> | <code></code> | medium |
| 83 | 214 | 3 | <code>\unsure</code> | <code>;</code> | <code></code> | medium |
| 83 | 214 | 10 | <code>\unsure</code> | <code>Recevez</code> | <code></code> | medium |
| 83 | 214 | 13 | <code>\unsure</code> | <code>b</code> | <code></code> | medium |
| 83 | 214 | 15 | <code>\unsure</code> | <code>x</code> | <code></code> | medium |
| 83 | 214 | 15 | <code>\unsure</code> | <code>que de tels pro</code> | <code></code> | medium |
| 83 | 214 | 15 | <code>\unsure</code> | <code>certes,</code> | <code>civils,</code> | medium |
| 83 | 214 | 15 | <code>\unsure</code> | <code>Par contre, dans les années qui m</code> | <code></code> | medium |
| 83 | 214 | 15 | <code>\unsure</code> | <code>treize</code> | <code>douze</code> | medium |
| 83 | 214 | 15 | <code>\unsure</code> | <code>déjà</code> | <code></code> | medium |
| 83 | 215 | 10 | <code>\unsure</code> | <code>\delta'</code> | <code></code> | medium |
| 83 | 215 | 15 | <code>\unsure</code> | <code>\varepsilon</code> | <code></code> | medium |
| 83 | 215 | 24 | <code>\unsure</code> | <code>''</code> | <code>4</code> | medium |
| 83 | 215 | 27 | <code>\unsure</code> | <code>\varepsilon_2</code> | <code>\varepsilon_3</code> | medium |
| 83 | 216 | 3 | <code>\unsure</code> | <code>soufflé</code> | <code></code> | medium |
| 83 | 216 | 3 | <code>\unsure</code> | <code>)</code> | <code></code> | medium |
| 83 | 216 | 3 | <code>\unsure</code> | <code>rôle</code> | <code></code> | medium |
| 83 | 216 | 3 | <code>\illegible</code> | <code>5</code> | <code></code> | low |
| 83 | 216 | 5 | <code>\unsure</code> | <code>lett</code> | <code></code> | medium |
| 83 | 216 | 5 | <code>\unsure</code> | <code>serait</code> | <code></code> | medium |
| 83 | 216 | 5 | <code>\unsure</code> | <code>n</code> | <code></code> | medium |
| 83 | 216 | 5 | <code>\unsure</code> | <code>a</code> | <code></code> | medium |
| 83 | 216 | 7 | <code>\unsure</code> | <code>n'a</code> | <code></code> | medium |
| 83 | 216 | 7 | <code>\unsure</code> | <code>k</code> | <code></code> | medium |
| 83 | 216 | 9 | <code>\unsure</code> | <code>réçu</code> | <code>reçu</code> | medium |
| 83 | 216 | 9 | <code>\unsure</code> | <code>,</code> | <code></code> | medium |
| 83 | 217 | 3 | <code>\unsure</code> | <code>-</code> | <code>+</code> | medium |
| 83 | 217 | 4 | <code>\unsure</code> | <code>-</code> | <code>+</code> | medium |
| 83 | 217 | 8 | <code>\unsure</code> | <code>3</code> | <code>'</code> | medium |
| 83 | 217 | 9 | <code>\unsure</code> | <code>c</code> | <code></code> | medium |
| 83 | 217 | 10 | <code>\unsure</code> | <code>-</code> | <code>+</code> | medium |
| 83 | 217 | 14 | <code>\unsure</code> | <code>Sommes</code> | <code></code> | medium |
| 83 | 217 | 16 | <code>\unsure</code> | <code>b+c+</code> | <code></code> | medium |
| 83 | 217 | 23 | <code>\unsure</code> | <code>-</code> | <code>=</code> | medium |
| 83 | 217 | 25 | <code>\unsure</code> | <code>a'</code> | <code></code> | medium |
| 83 | 217 | 25 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 217 | 26 | <code>\unsure</code> | <code>le facteur 2 est partout !</code> | <code>les signes sont partout !</code> | medium |
| 83 | 218 | 3 | <code>\unsure</code> | <code>c</code> | <code>e</code> | medium |
| 83 | 218 | 5 | <code>\unsure</code> | <code>5</code> | <code></code> | medium |
| 83 | 218 | 7 | <code>\unsure</code> | <code>(!)</code> | <code></code> | medium |
| 83 | 218 | 9 | <code>\unsure</code> | <code>Cette constat</code> | <code></code> | medium |
| 83 | 219 | 6 | <code>\unsure</code> | <code>-1</code> | <code></code> | medium |
| 83 | 219 | 23 | <code>\unsure</code> | <code>OK</code> | <code></code> | medium |
| 83 | 219 | 24 | <code>\unsure</code> | <code>27</code> | <code></code> | medium |
| 83 | 220 | 2 | <code>\unsure</code> | <code>1</code> | <code></code> | medium |
| 83 | 220 | 4 | <code>\unsure</code> | <code>bonbinage</code> | <code>bombinage</code> | medium |
| 83 | 220 | 6 | <code>\unsure</code> | <code>pbus</code> | <code>plus</code> | medium |
| 83 | 220 | 6 | <code>\unsure</code> | <code>pervenant</code> | <code>parvenant</code> | medium |
| 83 | 220 | 6 | <code>\unsure</code> | <code>(</code> | <code></code> | medium |
| 83 | 221 | 12 | <code>\unsure</code> | <code>\beta</code> | <code></code> | medium |
| 83 | 221 | 14 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 221 | 16 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 221 | 32 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 221 | 33 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 221 | 34 | <code>\unsure</code> | <code>+</code> | <code>-</code> | medium |
| 83 | 221 | 37 | <code>\unsure</code> | <code>-</code> | <code>+</code> | medium |
| 83 | 222 | 4 | <code>\unsure</code> | <code>qye</code> | <code>que</code> | medium |
| 83 | 222 | 4 | <code>\unsure</code> | <code>que</code> | <code></code> | medium |
| 83 | 222 | 4 | <code>\unsure</code> | <code>juste</code> | <code>partie</code> | medium |
| 83 | 222 | 4 | <code>\unsure</code> | <code>parf</code> | <code></code> | medium |
| 83 | 222 | 4 | <code>\unsure</code> | <code>inspiration</code> | <code></code> | medium |
| 83 | 222 | 4 | <code>\unsure</code> | <code>s'</code> | <code></code> | medium |
| 83 | 222 | 6 | <code>\unsure</code> | <code>****</code> | <code></code> | medium |
| 83 | 222 | 6 | <code>\unsure</code> | <code>aplatissement</code> | <code></code> | medium |
| 83 | 222 | 6 | <code>\unsure</code> | <code>f</code> | <code></code> | medium |
| 83 | 222 | 6 | <code>\unsure</code> | <code>men</code> | <code></code> | medium |
| 83 | 222 | 6 | <code>\unsure</code> | <code>s</code> | <code></code> | medium |

## Abbreviations encountered

These are proposed expansions for the glossary only. The diplomatic text retains the abbreviations and their actual punctuation; a doubtful abbreviation remains doubtful even when its likely expansion is clear.

| Written form | Proposed expansion / meaning | Examples and qualifications |
|---|---|---|
| `alg.`, `Az.` | algèbre; Azumaya | 183, 190. |
| `bil.`, `sym.`, `multilin.` | bilinéaire; symétrique; multilinéaire | 188; 186 for multilin. |
| `can.`, `canon.`, `canon.t` | canonique; canoniquement where adverbial | 178–180, 183, 186. The final t is itself uncertain in 180. |
| `car.` | caractéristique | 192. |
| `cat`, `cat.` | catégorie | 181. |
| `ssi` | si et seulement si | 181. |
| `dég.` | dégénérée | 183, “non dég.”; grammatical expansion is a gloss, not supplied text. |
| `ds` | dans | 197. |
| `ens.` | ensemble | 183; the written abbreviation is uncertain. |
| `ex.` | exemple | 187. |
| `expr.` | exprimer, or expression according to syntax | 213, within an uncertain phrase. |
| `ext.` | extensions | 180, cancelled and uncertain. |
| `fidèl` with raised t | fidèlement | 195, uncertain abbreviation. |
| `gén.` | générateurs | 194. |
| `hom.` in `semi-hom.` | homomorphisme | 178, the compound abbreviation is uncertain. |
| `im.` | image | 178, uncertain. |
| `inv.` | inversible; invariant | 181, 185, 186, 191–192 for invertibility; “inv. sous G” in 186 and a ring label in 195 for invariance. These uses must not be collapsed. |
| `i.e.` | id est | Several mathematical sheets. |
| `NB` | nota bene | 180, 191. |
| `nb` | nombre | 178, in a particularly uncertain marginal phrase. |
| `Num.` | unresolved | 193, within `\unsure{copies de Num.}`; no reliable expansion is offered. |
| `op.` | opération | 189, “op. de” a symmetric group; the abbreviation itself is retained. |
| `orient.` | orientation | 185. |
| `orth.` | orthogonal / orthogonale | 184. |
| `circ.` | circulaires | 191, referring to permutations. |
| `perm.` | permutation | 205. |
| `pol.` | polynomiales | 197, “expressions pol.”. |
| `coeff` | coefficients | 197; no final punctuation supplied where none is written. |
| `mod` | modulo | 184 and related calculations. |
| `λ-triv.` | λ-trivialisation | 180. |
| `Tr`, `det`, `dis`, `Aut` | trace; déterminant; discriminant; automorphismes | Operator abbreviations kept in their written form. |
| `id` | identité, or idem in prose | The map notation and prose shorthand should be distinguished. |
| `sg` | signature | 195, in the permutation action. |
| `b. de p.` | bas de page | 208. |
| `p.`, `n°`, `nos` | page; numéro; numéros | Reused typed sheets and cross-references. |
| `Dr.`, `Mme` | docteur; madame | Letter material; personal initials are not expanded from outside knowledge. |
| `SGA` | Séminaire de géométrie algébrique | A conventional title abbreviation in the reused typed text; this gloss does not identify or verify each volume mentioned. |

## Legibility and confidence

The typed base text is generally substantially more legible than the fast mathematical hand. The least secure typed passages are letters hidden by repeated X-overstrikes, overwritten word endings, tiny handwritten interlinear revisions, and the attachment points of long insertion arrows. The mathematical pages are readable in their larger structure, but compressed superscripts, doubled primes, signs written over signs, and the distinction between script and plain capitals remain recurrent risks.

Particular caution is warranted for the marginal conditions on 178, the cancellations and coefficient changes on 184–188, the ring and group labels on 195 and 199–200, the small edge labels and crossed relations on 201–205, the overstruck passage on 208, the raised mark on 209, the tightly joined delta marks on 213–215, and the signs/exponent/cancelled caption on 217 and 221. The five-word `\illegible{5}` on 216 is a heavily blackened cancellation; a tentative readable fragment is retained before it. All other uncertain places receive attempted readings rather than omission marks.

Every whole-page image and both supplied halves were read by the same reader, and all 43 pages received a second visual audit before context access. No OCR was used. The diagrams and drawings preserve the read objects, labels, connections, and visible stroke direction, but their scale and spacing are typographic approximations, not facsimile measurements. A successful LaTeX build establishes syntax and renderability only; it does not certify a reading or prove a mathematical formula.

The manual doubt table contains the reader's confidence judgments. The occurrence concordance is exhaustive for the uncertainty macros and uses declared mechanical default confidence values; those defaults should not be mistaken for an independent judgment on each occurrence. “Medium” means a preferred reading with a real unresolved feature, and “low” marks especially weak recovery; neither is a claim of certainty. The package deliberately preserves anomalous spelling, apparent mathematical errors, unfinished expressions, and differences between repeated drafts.
