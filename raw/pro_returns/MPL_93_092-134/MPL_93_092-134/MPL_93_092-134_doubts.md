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


## Doubts recorded during the visual reading and audit

Approximate lines count visible manuscript lines or identify the region of the sheet. Earlier alternative readings are retained in this record even where the audit subsequently favoured one; the page files are the authoritative current readings.

| Cote | Scan | Approximate line / region | Reading | Alternative / difficulty | Confidence |
|---|---:|---|---|---|---|
| 93 | 92 | 2 | c_{2,3} | c_{3,3}; first index overwritten | low |
| 93 | 92 | 2 | arrow Omega to omega | plain stroke; head faint | low |
| 93 | 92 | 6 | t.f. | abbreviation has faded first letter | medium |
| 93 | 92 | 8 | Appl. / i.e. | crossed-out and interlinear fragments | low |
| 93 | 92 | 11 | i.e. encore | faint connective before que | low |
| 93 | 92 | 18 | Elles forment / Ce sont les | deleted phrase and replacement | low |
| 93 | 92 | 22 | Omega^{otimes2}, omega | two expressions beneath target underbrace | low |
| 93 | 93 | 3 | -2i_{omega} | -2 id_{omega}; overwritten ending | low |
| 93 | 93 | 3 | Considérons / l’hom. | possible crossing and faint following word | low |
| 93 | 93 | 6 | d^1_omega; P^1_{X/S} | small indices overwritten | low |
| 93 | 93 | 14–17 | quand on a splitting; delta_0=i; recette générale | faint paragraph on printed music rulings; all uncertain portions marked | low |
| 93 | 93 | 17 | P^1(Omega) simeq P^1(O_X) et les | deleted passage | low |
| 93 | 93 | 18 | delta_0 de Omega | interlinear remnant below deleted display | low |
| 93 | 94 | 1 | Donc on a | very faint transition | low |
| 93 | 94 | diagram 2 | alpha prime | beta; circle crossing music ruling | low |
| 93 | 94 | 11–14 | définissant / sous omega / par l’ext. | interlinear placements faint | medium |
| 93 | 94 | 16 | L^ab | small exponent may be other two letters | low |
| 93 | 94 | 20–23 | l’iso; L_omega; Ils sont déterminés par une; famille/section; donnée à | bottom revisions partly overwritten; text doubtful throughout these fragments | low |
| 93 | 95 | margin a) | cela a l’air vraiment vicieux vrai | faint sloping four-line annotation | low |
| 93 | 95 | b) | w fixé, c’est bien lin. | first character could be f; do not regularize | low |
| 93 | 95 | 14 | système | faded end of line | medium |
| 93 | 95 | 17 | H above connexions and crossed H | interlinear letters uncertain | low |
| 93 | 95 | 19 | Omega^2 tensor omega simeq omega^{tensor3} | both exponents faded; 3 resembles small loop | low |
| 93 | 95 | vertical margin | Delta_X(X); prolongeant à un iso des; vois. form. | overwritten phrase and abbreviated closing words | low |
| 93 | 95 | last | de f.t. lisse | abbreviation faint | low |
| 93 | 96 | 5 | en somme | faint fragment before de L en somme directe | low |
| 93 | 96 | 8 | donne | possibly rend; ink indistinct | low |
| 93 | 96 | 10–16 | comme la donnée; choix; mod; précis./préc.; par la | several overwritten connective words, all marked | low |
| 93 | 96 | 14 | -2 bar omega_2 | coefficient overwritten but 2 plausible | medium |
| 93 | 96 | 22 | caractérisation bien | struck fragment above application sentence | low |
| 93 | 96 | 24 | différentielles | struck right-margin adjective | low |
| 93 | 97 | left 1 | affines | word faint and elongated | medium |
| 93 | 97 | left crossed opening | uniformisante; localt; projective | canceled paragraph; no expansion beyond visible ending | medium |
| 93 | 97 | left formula 1 | bar omega_0 in Gamma Omega^-1 tensor omega^1 | small added exponent / mark | low |
| 93 | 97 | left brace | psi_s; Gamma nu_s | overwritten map name and capital Gamma | low |
| 93 | 97 | left expansions | underbraces -2 omega_1 nu_s0 and +omega_1^2 nu_s0 | small subscripts and signs; both marked | low |
| 93 | 97 | left lower crossed calculation | bar omega_2(s); c(nu_s) expansion | heavily crossed formula, several individually unsure terms | low |
| 93 | 97 | left last display | delta d(omega_1 delta^-1) | argument overwritten; no factor inserted from expectations | low |
| 93 | 97 | right 6 | au-delà | faded parenthesis | low |
| 93 | 97 | right 15–18 | s’il y en a une infinité; avoir | sentence faint, apparent assertion preserved with doubt | low |
| 93 | 97 | right 19 | nous; section; sigma prime | interlinear annotation and final prime | low |
| 93 | 97 | right last | lin./l’op. | overwritten qualification before gamma | low |
| 93 | 98 | 1 | 1-diff. | possibly L-diff.; first character indistinct | low |
| 93 | 98 | last 2 | qui | small crossed word after projective | medium |
| 93 | 99 | 3 | a) | faint enumeration after f. et s. | low |
| 93 | 99 | 11–13 | pôles; dégénérescence, et signifie; splitting; il | overwritten passages | low |
| 93 | 99 | 16–18 | comme section nulle au pt envisagé doit être déterminée | wording awkward but visible; no mathematical correction made | medium |
| 93 | 99 | foot | des élts de contact can. d’ordre 1 à trouver dès que fois | ending faint; syntactic discontinuity preserved | low |
| 93 | 100 | line 5, underbrace | pour choix local | pour choix localt; pour choix … | low |
| 93 | 100 | line 7 | coordonnée principale | coord. … principale | low |
| 93 | 100 | line 13, deletion | β | overwritten letter or false start | low |
| 93 | 101 | top cancelled diagram | M_g^G; M_gc | superscript 4; third subscript c uncertain | low |
| 93 | 101 | top curved arrow label | ret. à H sur fibres | ret. à … fibres | low |
| 93 | 101 | upper right isolated line | car Uniquement 1 ≠ autom. | cas; Uniquement; arrow-like sign unresolved | low |
| 93 | 101 | left isolated chain | -ω⊂L⊂H a | truncated initial stroke; final a uncertain | low |
| 93 | 101 | middle deleted line | forme un torseur de ω | first and final words faint/overwritten | low |
| 93 | 101 | middle cancelled words | s’interprètent comme; sections | s’interpr…; isolated word undecided | low |
| 93 | 101 | foot decomposition | ω^2⊕ω⊕ω^0 | first exponent 1 possible | medium |
| 93 | 101 | foot right | ν_s=0+0+1 | initial symbol may be ω_s | low |
| 93 | 101 | foot c(s) inclusion | s⊗ω | L⊗ω | low |
| 93 | 101 | foot annotation | avec ωbar_i=0 ? | φbar_i; index 0 | low |
| 93 | 101 | last expansion | (exp Θ_a1 ⊗ id_ω)^-1 c(s) | inverse exponent and final factors overwritten | low |
| 93 | 102 | upper left cancelled | dt/ds | overwritten fraction | low |
| 93 | 102 | second box subscript | t | σ | medium |
| 93 | 102 | after second box | On cherche | On obtient | low |
| 93 | 102 | middle, logarithmic calculation | 2s‴/s″=3/2 s″/s′; 2log s″=3/2 log s′ | leading 2 and coefficient visibly rewritten; not regularized | low |
| 93 | 102 | left marginal note | s fct homographique de t ! | s fonction homographique de t ! | medium |
| 93 | 102 | lower prose | 3 types d’hom. | 3 types d’élém. | low |
| 93 | 103 | top bracket labels | -2a_1 ν_s0; -2a_1² | last factor in first label overwritten | low |
| 93 | 103 | middle cancelled paragraph | On supp. c provenant d’une conn. c associée à un splitting | first line densely cancelled | low |
| 93 | 103 | middle c(s_0) deletion | φbar_1+ν_s0 | overwritten factors | low |
| 93 | 103 | middle right abandoned expression | (exp Θ_a1⊗id_ω)(a_1)+ | argument and deleted operator uncertain | low |
| 93 | 103 | middle prose | est sa comp. dans ω², et si | est la comp. … | low |
| 93 | 103 | right marginal note | pour un splitting convenable et une base δ de ω | insertion anchoring and cancelled phrase uncertain | medium |
| 93 | 103 | boxed equation | D_1(a_1)+a_1²-ω_2=0 | sign may be +; heavy rewriting | low |
| 93 | 103 | left marginal question | facteur 2 qui manque avant ce calcul ? | several words faint | low |
| 93 | 103 | bottom deleted expression | dλ/dt+λ | exponent or trailing symbols overwritten | low |
| 93 | 104 | line 2 deletion | devoir | d’avoir; deeply overwritten word | low |
| 93 | 104 | line 3 | mb. | membre written in compressed form | medium |
| 93 | 105 | top operator target | ω^2 | exponent partly overwritten; target may be written ω alone | low |
| 93 | 105 | top last line | forme torseur sous ω | forment torseur sous ω | medium |
| 93 | 105 | upper insertion | i.e. si on a une connexion D_1:ω→ω² | abbreviated words and attachment uncertain | low |
| 93 | 105 | middle deleted wording | ce qui donne lieu à une appl. de | last five words faint and struck through | low |
| 93 | 105 | middle verification | Et vérifions | Et vérif. | low |
| 93 | 105 | middle subformula | c_D0+D_0ω_1+ω_1² | coefficient before D_0 not visible; retained without inferred 2 | medium |
| 93 | 105 | middle formula | 2(D_0+ω_1)(ωbar_1)+ωbar_1^2 | initial 2 uncertain; last exponent resembles 1 | low |
| 93 | 105 | foot lead-in | Considérons la connexion | Considérons c connexion | low |
| 93 | 105 | inverted table first row | ρ_aω_1 and cancelled values | ρ or β; several values overwritten | low |
| 93 | 105 | inverted table quadratic row | (α_-1)^2 ω_1 | ω_-1 possible; visible index resembles 1 | low |
| 93 | 106 | author page number | 4 | 9 | medium |
| 93 | 106 | first display | (f)D_tω+fωdf | reordered and overwritten factors; final f uncertain | low |
| 93 | 106 | cancelled first comparison | ω d(ds/dt)dt/ds=ω_1dt/dt | dense overwriting | low |
| 93 | 106 | lower expanded final term | ω dt/dt d(dt/ds) | several cancelled factors and possible missing ds retained with doubt | low |
| 93 | 106 | lower D_sω formula | ds/dt | denominator overwritten | medium |
| 93 | 107 | upper target exponent | ω^(⊗2) | small exponent faint, final digit near paper hole | medium |
| 93 | 107 | upper final line | c’est augmenté de ω_1↦ω_1 ωbar | initial pronoun uncertain; no coefficient 2 visibly present | medium |
| 93 | 107 | lower operator | d_t | D_t | medium |
| 93 | 107 | last line abbreviation | const. | constant compressed | medium |
| 93 | 108 | right insertion | E^1_S | A^1_S; first letter resembles E | medium |
| 93 | 108 | last line deletion | canoniq. | canoniques compressed | low |
| 93 | 108 | last projective bundle | P_(P^1_S/S) | double-struck initial P; no exponent visible | medium |
| 93 | 109 | a′ deleted symbol | P | unresolved overwritten mathematical expression | low |
| 93 | 109 | b type | sl(2) | last digit compressed, could be 1 | medium |
| 93 | 109 | b abbreviation | néc.t | néct; exact abbreviated ending uncertain | medium |
| 93 | 109 | b map label | c_L | c_2 | medium |
| 93 | 109 | b′ parenthesis | L⊂P^1_X/S(ω)⊗ω^-1 }.⊃ω²⊗ω^-1≃ω | first relation and intervening brace are not secure | low |
| 93 | 109 | b′ connexion indices | H_1 | H_X | low |
| 93 | 109 | d group | GPM_X | GPM_S; group abbreviation has M-shaped final letter | low |
| 93 | 109 | d final phrase | équa. par. aux jets d’ordre 3 de sections i.e. morphismes | abbreviation par.; sections/solutions | low |
| 93 | 110 | top insertion | X^an compact | last word could be omitted/unfinished; faint | low |
| 93 | 110 | cancelled two-line question | Quid en structure imposant dans par la forme de connexion projective sur X/S | syntax and several words unresolved despite enlargement | low |
| 93 | 110 | middle torseur insertion | d’iso. locaux | d’iso…; fine faint letters | low |
| 93 | 110 | middle transformation | symétrie systématique | symétrie; second word doubtful | low |
| 93 | 110 | relation line | (gf,y)∼(f,g^-1 y) deleted | cancellation partly coincides with ruling | medium |
| 93 | 110 | foot application | f:U- P^1(C) | no secure arrowhead | medium |
| 93 | 110 | foot source | fournie par (e) | last characters heavily overwritten | low |
| 93 | 110 | bottom trivialization | P\|U≃X^an\|U×P^1 | last factors at edge and staff lines; reading provisional | low |
| 93 | 111 | 3 | analytiques (deleted) | faint cancelled word | low |
| 93 | 111 | 6 | Pour cela on a un | Pour cela encore au | low |
| 93 | 111 | 7 | donc | ou | low |
| 93 | 111 | 12 | y0; deleted point | overwritten point name and cancellation | low |
| 93 | 111 | 15 | car f x0; P x(∋p) | faint parenthetical isomorphism and target | low |
| 93 | 111 | 17 | tilde f x0(x); P an | no added p0 argument; target kept as written | medium |
| 93 | 111 | 21 | U subscript deleted T an; P1 an | heavy cancellation under U | low |
| 93 | 111 | 26 | non horizontales; B u | inserted qualifier; final subscript unclear | low |
| 93 | 112 | 5 | inversible (deleted) | overwritten word after L | low |
| 93 | 112 | 9 | (D,lambda); φ of ω² | φ in pair; ω instead of ω² | low |
| 93 | 112 | 10–11 | pour la connexion D sur ω; cancelled Ramener... | overlapping additions and cancellation | low |
| 93 | 112 | 14 | Applhol(Xan,Can) | terminal target exponent and first letter faint | medium |
| 93 | 112 | 17 | par suite | overwritten connective | low |
| 93 | 112 | 19 | E1(C) | A1(C) | medium |
| 93 | 112 | 20–24 | canonique; régulière; Cela; alors on a donc | faint or cancelled prose | low |
| 93 | 112 | 27 | s’ under brace | s’² | low |
| 93 | 113 | 5 | exp Λ(t) | No minus discernible in first exponential; minus visible in integral | medium |
| 93 | 113 | 8 | E1 | A1 | medium |
| 93 | 113 | 8–10 | du; deleted arrow; deleted -1 | cancellations in torsor identification | low |
| 93 | 113 | 12 | σ’ in insertion; l’ens. | σ; l’une | low |
| 93 | 113 | 16 | algébriques | overwritten inserted adjective | low |
| 93 | 113 | 19 | associées; analyt. sur ω | rapid abbreviated qualifiers | low |
| 93 | 113 | 21 | telles que σ’ disj. de σ | faint insertion over uniformisants | low |
| 93 | 113 | 23 | cDt | cDs suggested by preceding variable, not substituted | medium |
| 93 | 114 | left 2 | E1C | A1C | medium |
| 93 | 114 | left 19 | d) then c) | written order retained; long curved mark links the two blocks | high |
| 93 | 114 | left 22 | subscript Dt-ds’/s’, deleted dt | heavy overwrite in connection label | low |
| 93 | 114 | left 25 | -s’’/s’=λ(t)dt | no dt after first quotient discernible | medium |
| 93 | 114 | left 27 | ou en satisfait à a) | faint phrase following (1) | low |
| 93 | 114 | left foot | On passe de c) à b); deleted dt | partly at edge | low |
| 93 | 114 | right 1 | 2(s’’/s’)’ | a possible minus is very faint; subsequent line has -2 | low |
| 93 | 114 | right 4 | deleted λ’-2λ² | cancelled expression | low |
| 93 | 114 | right 16 | (Ds-Dt)/dt² | c subscripts not visible in first parenthesis | medium |
| 93 | 114 | right 20 | G t tilde(s)=Gt(s)t tilde prime² | first subscript overwritten; no further term discernible | low |
| 93 | 114 | right 27 | s triple prime | s quadruple prime | medium |
| 93 | 115 | 1–3 | multiformes; trouve; ainsi | faint and inserted words | low |
| 93 | 115 | 5 | le = énoncé avec la seule Diff. | same-sign abbreviation retained; Diff. uncertain | medium |
| 93 | 115 | 7 | Pouvons nous la (deleted) | cancelled phrase | low |
| 93 | 115 | 10 | ça donne | faint verb phrase after X→S | low |
| 93 | 115 | 12 | Celles-ci, ont elles | Ceci a-t-il | low |
| 93 | 116 | 8 | ω tensor² | overwritten capital Ω | medium |
| 93 | 116 | 10 | montre (deleted) | short cancelled verb | low |
| 93 | 116 | 11 | as (deleted) | overwritten multiplier before s+b | low |
| 93 | 116 | 17 | Enfin | faint transition | medium |
| 93 | 116 | 25–26 | il ne forme plus de ... où s est holomorphe | inserted clause heavily overwritten; words retained with doubt | low |
| 93 | 117 | 1 | t=r | t=s=r; overwritten first specialization | low |
| 93 | 117 | 6–9 | cancelled paragraph; slanted margin | faint crossed and rotated prose; two words unreadable after enlargement | low |
| 93 | 117 | 15 | ditto mark after second (4) equation | small trailing stroke | medium |
| 93 | 117 | 19 | script P_X | P has one loop and descending stroke | medium |
| 93 | 117 | 22 | mod. matrices diagonales | word reads diagonales; no substitution of scalaires | medium |
| 93 | 117 | 31 | pour s, pour t fixé | faint parenthesis | low |
| 93 | 118 | 1 | unique (deleted) | crossed short word after ∃ | low |
| 93 | 118 | 6 | PX/H (deleted) | cancelled quotient order | low |
| 93 | 118 | 22 | dudit est appelé; inv. | written agreement and abbreviation retained | medium |
| 93 | 118 | 31 | f-1(P_X’) | f-1(P_X); tiny prime-like stroke | low |
| 93 | 118 | 31 | deleted C_X’ | overwritten old target before ConnX’ | low |
| 93 | 119 | 1–3 | faisceau final | read as written; no replacement by a claim about global sections | medium |
| 93 | 119 | 2 | et que; il y a (deleted) | crossed short phrases | low |
| 93 | 119 | 9 | formt. lisse, dim diff relative | abbreviation and insertion retained | medium |
| 93 | 119 | 11 | topologiques (inserted) | small adjective above étales | low |
| 93 | 119 | 17 | topologiques (deleted) | cancelled adjective | low |
| 93 | 119 | 21 | défini par (deleted) | overwritten phrase before inserted un morphisme can. | low |
| 93 | 119 | margin | diff. principales; diff. uniques; P3X/S; Sym(ωX/S) | slanted note very difficult; prose and formula both provisional | low |
| 93 | 120 | 1 | f inverse image exponent -1 | tiny exponent; reads -1 rather than prime or ! | medium |
| 93 | 120 | 16 | cX_t(s) | subscript is a small isolated mark, perhaps cancelled | low |
| 93 | 120 | 28 | énoncera | faint word at bottom edge | low |
| 93 | 121 | left 1 | lisse/S ??; on peut énoncer que | inserted parenthesis and verb faint | low |
| 93 | 121 | left 12 | affine | projective; reads affine despite subject | medium |
| 93 | 121 | left 19–21 | groupe HX/S; opère; argumentation opère | heavily corrected and rapid prose | low |
| 93 | 121 | left bottom margin | 2 et 3 inversibles, p>3; Cf plus bas | qualification small and slanted | medium |
| 93 | 121 | right 1 | si s,t sont deux uniformisants | overlapping deleted and inserted words | low |
| 93 | 121 | right 7–10 | G and G0 formulas without dt² | no dt² discernible after displayed normalized formulas | medium |
| 93 | 121 | right 11 | 12.1S=0 | overwritten comparison sign | medium |
| 93 | 122 | 6 | double arrow H quotient ↔Conn0 | stroke has heads at both ends | medium |
| 93 | 122 | 17 | à qui s’appliquent | faint inserted clause | low |
| 93 | 122 | 24 | Non vérifiée (deleted) | cancelled status; adjacent OK retained separately | low |
| 93 | 122 | 24 | local plus gén. avec Pic(A)=0 | inserted bracket has a possible initial numeral 2 | medium |
| 93 | 122 | 25 | ∀s∈B | ∃s∈B | low |
| 93 | 122 | margin | hypothèse provisoire | second word indistinct | low |
| 93 | 122 | 31 | first exponent (3) in c0 | (2) | low |
| 93 | 122 | 34 | (D(3)s)² and D(2)s on right | unexpected exponents retained; right alternative (3) | low |
| 93 | 122 | 36 | uniques à transformation diagonale | small inserted qualifier | medium |
| 93 | 123 | 1 | OPS par changement α∈Ap puis α=0 | many cancellations and rewritten equality | low |
| 93 | 123 | 2 | rB | radical symbol may be different; no expansion made | low |
| 93 | 123 | 3 | a1+a2t | no factor 2 visible before a2 | medium |
| 93 | 123 | 8 | cancelled 1/(1+a2s^-1) | overwritten rational expression | low |
| 93 | 123 | 9 | s-a2s² | plus/minus ink overwritten | low |
| 93 | 123 | 14 | Si on a (deleted) | cancelled opening phrase | low |
| 93 | 124 | left lines 4-5 | formes d’hog. comme | phrase after résultat uncertain | low |
| 93 | 124 | left line 13 | c_{3,d-3} | c_{2,d-3}; overwritten first index | medium |
| 93 | 124 | left p=2 cancelled lines | d-d0; le cas favorable est celui | overwritten and cancelled prose/formula | low |
| 93 | 124 | left deleted bottom block | c_{d,d-3}; d1=0 | indices and encircled case order as visible | medium |
| 93 | 124 | right line 2 cancelled | 0 <= d1 <= 3 | last digit unclear beneath correction | low |
| 93 | 126 | case 3 and b | X | P; two crossing strokes | medium |
| 93 | 126 | case 3 NB | invariantes; sont deleted | parenthesis and insertion placement uncertain | medium |
| 93 | 126 | corollary case 3 | GP(1,R) = GL(2,R)/R* = SL(2,R)/mu2(R) | no visible positivity restriction retained | high |
| 93 | 127 | left lines 1-5 | d’ailleurs il se trouve; correspond | heavily revised connective phrasing | low |
| 93 | 127 | left alpha | descente du corps de base de C a R | inserted wording | medium |
| 93 | 127 | left margin delta | géodésique non ponctuel | slanted faint words above (=cercle) | low |
| 93 | 127 | left middle | delta et gamma; projective réelle | alpha possible; noun before projective overwritten | low |
| 93 | 127 | Scholie | strict. hom. | first abbreviation uncertain | medium |
| 93 | 127 | right lines 9-10 | munis par pt donné | last words inside parentheses faint | low |
| 93 | 127 | right last line | mathcal P | large looped final bundle letter | medium |
| 93 | 128 | top deleted word | immersion | overwritten under connexion | low |
| 93 | 128 | theorem deleted adjective | décrite | deleted before non sing. | low |
| 93 | 128 | upper margin | un germe p d’hom. anal. possédant des solutions | faint joined handwriting; multiple words uncertain | low |
| 93 | 128 | upper margin end | alors du; explication | prolongement analytique clearly readable between | low |
| 93 | 128 | lower margin | canoniquement définies par; avec des restrictions | connection between visible words uncertain | low |
| 93 | 128 | diagram | plain lines to X | no arrowhead visible | high |
| 93 | 129 | case 1 parenthesis | on donne aucune condition | fast faint phrase between dashes | low |
| 93 | 129 | case 2 corrected lines | autom. sans pt. fixe; analytiques comme de E1C | nested cancellation/insertion attachment uncertain | low |
| 93 | 129 | case 2 ranks | point C; point C* | may read qui donne, abbreviation retained as tentative | low |
| 93 | 129 | left margin | full category/torsor paragraph | several connective phrases very uncertain despite rotations and enlargement | low |
| 93 | 129 | lower paragraph | pourvu d’une structure vectorielle | replacement phrase overlapping deleted text | medium |
| 93 | 129 | last lines | n’honore pas | verb form could be n’ignore pas; visibly n honor... | medium |
| 93 | 130 | first formula | mathbb V and mathbb W | double strokes, V versus W kept distinct | medium |
| 93 | 130 | middle parenthesis | le sous- G_m(C) | words before group faint | low |
| 93 | 130 | last parenthesis | Transport ! | faint final word | low |
| 93 | 130 | lower formula | Xtilde subset X | ink retained despite unusual expression | medium |
| 93 | 131 | top lines 2-3 | retenir | revenir possible but construction unclear | medium |
| 93 | 131 | middle paragraph | dans b) et d) | c) possible; last letter curved | medium |
| 93 | 131 | middle parenthesis | equivaut a; une liaison algebrique | cancelled wording very faint | low |
| 93 | 131 | lower paragraph | le topo de Deligne | les topos possible | medium |
| 93 | 131 | last sentence | tout établir | connector before établir uncertain | low |
| 93 | 132 | top formula | X/C followed by inserted sur C | overwritten base marker | medium |
| 93 | 132 | case 2 | hom.; Xtilde alg | inserted word and superscript faint | low |
| 93 | 132 | upper cancelled margin | Par Deligne le faisceau des sections est algébrique | heavily struck, several words tentative | low |
| 93 | 132 | Question parenthesis | en supposant qu’on se soit muni de; rho_X | short connective phrase and last tuple letter uncertain | low |
| 93 | 132 | lower margin | full OK note | slanted and very faint; low confidence in connecting words | low |
| 93 | 132 | foot formula | (P_X)_{x an} | formal neighbourhood notation may be overwritten | medium |
| 93 | 133 | middle | fibrés de S.B. de rang 1 | S.D. possible, acronym ink abbreviated | medium |
| 93 | 133 | formula | mathcal J; omega^-1 | script ideal letter could be I; exponent -1 visible | medium |
| 93 | 133 | lower lines 1-4 | impliqué; deux premiers jets | faint writing; second noun could be premiers jets | low |
| 93 | 133 | foot | correspondant à | continuation cut at page edge | medium |
| 93 | 134 | top | torseur canonique sur S | S appears as written, not silently changed to X | high |
| 93 | 134 | C underbrace | ensemble des connexions projectives | first tiny word uncertain | medium |
| 93 | 134 | middle insertion | respectant les L. | last handwritten sign may be crochet symbol | low |
| 93 | 134 | Lie algebra letter | mathcal H | fraktur g possible; requires package notation comparison | low |
| 93 | 134 | last lines | applique nécessairement; ext. de omega par omega2 | wordings and parentheses as visible | medium |
| 93 | 92 | footer underbrace | Omega tensor omega, omega | Omega tensor2, omega; overwrite | low |
| 93 | 93 | middle list of coefficients | omega_0=i, omega_1, omega_2 | first list letter previously read delta; reviewed as omega | medium |
| 93 | 95 | torsor line exponent | omega tensor 2 | 3 was first reading; enlarged stroke favours 2; preceding Omega exponent still uncertain | medium |
| 93 | 96 | condition on horizontal section | ssi | small letters above cancelled formula, added in audit | medium |
| 93 | 97 | left half lines 14–17 | gamma in coefficient and differential | nu | low |
| 93 | 98 | line 5 | plain dash in gamma0 map | arrowhead not visible | low |
| 93 | 99 | last three lines | chaque fois | word before fois cramped | medium |
| 93 | 100 | underbrace line 6 | par choix loc.t | pour choix local | low |
| 93 | 101 | top diagram | H¹ sur fibres | H sur fibres | low |
| 93 | 101 | lower third | Omega tensor omega; bar omega0 | script L; subscript i | low |
| 93 | 102 | after second box | On doit | On cherche | low |
| 93 | 105 | verification first line | (D0+omega1)(bar omega1) | no visible 2 before parenthesis; 2 remains in expansion underneath | medium |
| 93 | 106 | author page number | 9 | 4 | low |
| 93 | 106 | middle before boxed equation | c sub D0 | c sub Dt | low |
| 93 | 109 | last paragraph | GP(1) sub X | GPM sub X | medium |
| 93 | 110 | final line | P restricted U isomorphic X-an restricted U | U à X-an restricted U; no visible projective-line factor on this sheet | low |
| 93 | 112 | first display | plain stroke from omega to L | arrowhead uncertain | low |
| 93 | 114 | right half NB | D_s-D_t term struck through | underlining or overwritten correction; medium confidence deletion | medium |
| 93 | 119 | slanted left margin | gr(P³_X/S); arrow; iso en degrés | initial gr and concluding iso more visible on enlargement; middle phrase remains very uncertain | low |
| 93 | 120 | top commutative square | unheaded U–V and V–S strokes | small arrowheads may have faded | low |
| 93 | 121 | left half near Frobenius diagram | rég. after opère | s.ég.; compressed faint abbreviation | low |
| 93 | 122 | c0(s) display near foot | 2 or 3 in the numerator derivative orders | bottom condition visibly has (D^(3)s)^2; no mathematical normalization applied | low |
| 93 | 124 | left half after coefficient-binomial label | c sub 2,d−3 | c sub 3,d−3; blue numeral resembles 2 here | low |
| 93 | 126 | a)(3°) and b) | X in both places | P would fit the surrounding notation, but the visible character is X | high |
| 93 | 127 | left slanting margin δ | géodésique n. ponctuel | The word before ponctuel appears abbreviated; géodésique remains uncertain. | low |
| 93 | 128 | upper long margin, lines 1–2 | prenant des iso transversaux | possédant des solutions; middle words and ending remain very weak | low |
| 93 | 129 | last two lines | n'honore | verb faint; retained as a doubtful reading | low |
| 93 | 129 | rank 0, 1, 2 parenthetical words | point | quotient; compressed word remains doubtful, not silently expanded | low |
| 93 | 130 | lower middle, compact case | Gaga! | GAGA; capitalization and final stroke not entirely clear | medium |
| 93 | 131 | opening paragraph | Gaga | GAGA; case of the handwritten acronym is not fully distinct | medium |
| 93 | 133 | lower paragraph, condition on p | tels que | small linking words; first-pass que omitted the apparent tels | medium |
| 93 | 108 | recurring notation, final comparison | \mathbb E^1 | A alternative resolved by visible E strokes in the inserted morphism | high |
| 93 | 112 | recurring notation, final comparison | \mathbb E^1 | A alternative resolved by the doubled E and three bars | high |
| 93 | 113 | recurring notation, final comparison | \mathbb E^1 | A alternative resolved by comparison of both E forms on this page and scan 108 | high |
| 93 | 134 | recurring notation, final comparison | \mathcal H | matches the recurring cursive H on scan 092; exact script font remains uncertain | medium |

## Abbreviations encountered

These are proposed expansions for this list only. They have not been substituted into the transcription. Several short forms vary in punctuation on the sheets.

| Written abbreviation / short form | Probable expansion / meaning |
|---|---|
| alg., algéb. | algébrique(s) |
| anal., analyt., an | analytique(s), analytification |
| appl., Appl | application(s) |
| Aut, autom. | automorphismes, automorphisme |
| can., canoniq. | canonique(s) |
| car. | caractéristique |
| cat., Cat | catégorie |
| cf | confer / compare |
| i.e. | id est / c'est-à-dire |
| chgt | changement |
| coeff. | coefficient(s) |
| comm. | commutatif / commutativité |
| comp. | compact(e), complète, or composante according to context |
| conn., connex. | connexion(s) |
| conn. (in “conn. et simplement connexes”) | connexe(s) |
| cte | constante |
| dég. | dégénérescence / dégénéré |
| diff., Diff. | différentiel(le), or différence in scan 115 |
| dim | dimension |
| disj. | disjoint(e) |
| ens. | ensemble |
| épi, épi. | épimorphisme / épimorphique |
| équa. | équation |
| équiv. | équivalence / équivalent |
| esp. | espace(s) |
| ét, ét. | étale |
| ext. | extension |
| f. et s. | faut et suffit |
| fibré de S.B. | fibré de Severi–Brauer (probable expansion) |
| gén. | général(e), généralement |
| gr. | groupe |
| hom. | homomorphisme; homogeneous/homogène where used of a domain |
| hor., horiz. | horizontal(e) |
| id | identité |
| inv. | inversible, or inverse in “image inv.” |
| iso, isom. | isomorphisme / isomorphe |
| L. (respectant les L.) | Lie brackets / structure de Lie; abbreviated reading itself is weak |
| lin. | linéaire |
| loc., localt, loc.t | local(e), localement |
| mod. | modulo or module, according to placement |
| morph. | morphisme |
| n. | non, in the doubtful scan-127 margin |
| NB | nota bene |
| non sing., non sing. conn. | non singulier, connexe |
| op., op. diff. | opérateur / opération, opérateur différentiel |
| OPS | on peut supposer |
| p. ex. | par exemple |
| Pb | problème |
| préc. | précédent(e), précédemment |
| proj. | projectif / projective |
| Prop. | proposition |
| pt, pts | point, points |
| rég. | régulier / régulière |
| rel. | relatif / relative |
| rev. | revêtement |
| s.ég. (alternative reading, scan 121) | unresolved alternative; no reliable expansion proposed |
| Spec | spectre |
| ssi | si et seulement si |
| Sym | puissance symétrique |
| t.f. | type fini (probable, scan 092) |
| th., Th. | théorème |
| top. | topologie |
| tt | tout, toute |
| VA | variété abélienne |
| vois. | voisinage |
| GAGA / Gaga | Géométrie algébrique et géométrie analytique; the written capitalization is doubtful in scans 130–131 |


## Legibility and limits of confidence

All 42 supplied nonblank scans were read as whole pages and then in their supplied overlapping halves by one reader, followed by a second complete visual comparison. No OCR was used. Every inventoried element is represented in the page files. All sheets in this package are handwritten notes, several on ruled music paper; no typescript or printed offprint was found. Scan 125 was omitted from the supplied set as blank.

The handwriting ranges from fairly open and readable to highly compressed draft work. The music staves, pale pencil/ink, superposed corrections, and oblique margins are the main obstacles. The least secure passages are the tightly cancelled calculations in scans 097 and 101–107, some labels and constants around scans 119–124, and the long marginal additions on scans 127–129 and 132. Scan 117 has the single `\illegible{2}` occurrence: two words in marginal prose, after enlarged and rotated inspection. No formula or diagram is replaced by that macro.

An `\unsure` mark is a substantive reservation, not a typographical decoration. Long marked passages in the margins can contain more than one uncertain word; an apparently coherent sentence is not evidence that all its letters are secure. The doubt table retains the reading history, including subsequently resolved alternatives, so its row count is not a count of unresolved words. In particular, the last-page H, several derivative orders in scan 122, the page number on scan 106, and the scan-128 and scan-132 margins deserve independent comparison with the originals.

The inventory and mechanical checks provide coverage and structural checks, not a guarantee against visual misreading. A LaTeX compilation was attempted, but the installed TeX engines lack their formats and required packages; execution stopped before the transcription could be parsed. Brace/environment and command checks were therefore used, and no successful rendered-PDF verification is claimed. The deliverable is the requested LaTeX fragment, not a compiled edition.
