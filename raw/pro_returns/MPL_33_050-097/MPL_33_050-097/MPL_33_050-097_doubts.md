# Notation table and doubts

## Package notation table

This table was maintained from the first scan and completed by direct cross-page comparison **before opening the context**. Distinct positions, arrows and cancellations have not been harmonized merely because the mathematics might suggest a different expression.

| Manuscript sign or alphabet | LaTeX rendering | Comparison and limits |
|---|---|---|
| Doubled-stem derived-functor capitals R and L on the handwritten sheets | `\mathbb{R}`, `\mathbb{L}` | Same recurring alphabet in scans050,056,068,088,096; checked across the handwritten sequence. The doubled stem is represented, while variable R on the reused EGA sheets remains plain. |
| Upper exclamation mark | `f^!`, `i^!`, `\mathbb{R}^!f` | Compared throughout050–096. The raised stroke plus dot is distinguished from a prime. The author shifts the ! between R and the morphism; its actual position is retained. |
| Genuine raised prime(s) | `f'`, `i'`, `X''`, `X'''`, `\operatorname{gr}'`, `\operatorname{gr}''` | Factorizations050–068 and EGA sheets087–091. These are not rewritten as exceptional-inverse-image signs. |
| Lower exclamation mark and lower star | `i_!`, `j_!`, `f_*`, `\mathbb{R}_!f_*` | Both lower ! and lower * can occur in the same expression. The compound notation on054,074,078,092 is preserved. Overwritten alternatives in090 retain both cancellation and uncertainty. |
| Upper star | `f^*`, `g'^*` | Distinguished from the preceding true prime and from !. Moved lower/upper stars on096 are marked as deletion/insertion. |
| Categories underlined in the English typescripts | `\underline{A}`, `\underline{D}`, `\underline{F}`, `\underline{S}` | Underlining belongs to the source, not to a newly supplied categorical convention. Ordinary object letters remain ordinary. |
| Typed left/right-root operators | `\mathrm{Lr}`, `\mathrm{Rr}` | Direct comparison057,061,063,065 confirms the same ordinary typed operator. Rendering made consistent; letters and indices unchanged. |
| Derived and complex category capitals | `\mathrm{D}`, `\mathrm{C}` | Retain source C versus D, bounds + versus b, and source/target order; in particular the C(Y)→C(X) line on050 is not repaired. |
| Sheaf-valued cohomology/support symbols | `\underline{H}`, `\underline{\Gamma}_Y`; elsewhere `\mathcal H` | Underlining and script-like H are represented where seen; ordinary H for cohomology groups is distinct. |
| Hom, Ext, Tr, gr, Ass, Supp | `\operatorname{Hom}`, `\operatorname{Ext}`, `\operatorname{Tr}`, `\operatorname{gr}`, etc. | Source underlining is additional, not implied by operator spelling. Indices, primes and arguments are copied independently. |
| Root coordinates and Greek letters | `\varepsilon_i`, `\alpha_i`, `\omega_i`, `\Gamma_o` | Root-system sheets075,077,079 use epsilon-shaped coordinates. Plain typed R and Z are not silently converted to blackboard-bold fields or rings. |
| Undecided sign function in root formulas | `\unsure{\vartheta|\delta}` | Same candidate order on075 and077; the ink does not justify a confident choice. |
| EGA ideals, indices and graded marks | `\underline J`, `\underline K`, `\underline L`, `\operatorname{gr}_\bullet`, `\operatorname{gr}^\bullet` | Underlining, subscript bullet versus superscript bullet, and true primes are retained separately;087 differs from the surrounding graded-module notation. |
| Outlined operators and script letters on097 | `\mathbb S`, `\mathbb H`, `\mathcal G`, `\mathcal S` | Outlined S/H are distinct from plain sphere S_x and S(M); handwritten script G/S remain script. |
| Round lower-case o in typescripts | `A_o`, `\Gamma_o`, `f_o`, `M_{\tau,o}` | Compared057,073,077,079,095. The typed round character is not silently changed to a numeral zero. |
| Strict and non-strict inequalities | `>`, `\geq`, `<`, `\leq` | Read stroke by stroke; the two strict >0 signs on075 differ visibly from the later ≥0. |
| Horizontal stroke with no secure arrowhead | `\unsure{-|\longrightarrow}` or an explicitly headless TikZ arrow | Headless factorization/trace lines are retained; visible arrowheads are reproduced. Upward arrows are not reversed to fit expected variance. |
| Short paired vertical strokes linking annotations | `\Vert` in aligned brace annotations | Rechecked078,080,096. These are graphic links on the page, not additional asserted equalities supplied by the editor. |
| Single/double underline | `\uline`, `\uuline` | Includes headings, theorem statements and emphatic formula parts. |
| Double quotation marks | TeX opening double backticks and closing double apostrophes | Compared handwritten “lissifiable”, “formulaire”, “induit” and theorem names; only source double quotation marks receive this rendering. No guillemets were supplied. |
| Abbreviations and visible unfinished words | Literal source spelling | `pt`, `tt`, `cplxe`, `préadi-`, `s'identi` and other incomplete forms are not expanded in the transcription. Expansions appear only in the table below. |
| Blank formula arguments and terminal dots | `\hspace{...}` inside the source parentheses; literal dots/dashes | Blank parentheses on096 are genuinely blank. Source ellipses and four terminal strokes on078 are not editorial omissions. |

## Occurrence table

Every `\unsure` and `\illegible` occurrence, including nested occurrences inside cancellations and formulas, is indexed below. **Locations are line numbers in the individual page's TeX file**, supplied as reproducible approximate locators rather than claimed physical manuscript line numbers; source regions and the reasons for doubt are also recorded scan by scan in `records/doubt_details.md` and `records/audit_details.md`. “Low” means that the reading is a weak stroke-based candidate, often under cancellation; “medium” means a plausible visible reading whose exact letters, attachment or sign remain unresolved; “high” is reserved below for visually secure but mathematically surprising readings. An empty alternative field means no second defensible reading was found, not that the first reading is certain.

| File | Scan | Approximate location | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|---|
| 33 | 050 | TeX l. 3 | `21` | — | medium |
| 33 | 050 | TeX l. 4 | `thm` | — | medium |
| 33 | 050 | TeX l. 6 | `dém.` | — | medium |
| 33 | 050 | TeX l. 6 | `s'applique` | — | medium |
| 33 | 050 | TeX l. 6 | `pour` | — | medium |
| 33 | 050 | TeX l. 6 | `morphisme` | — | medium |
| 33 | 050 | TeX l. 6 | `également` | — | medium |
| 33 | 050 | TeX l. 11 | `triviale` | — | medium |
| 33 | 050 | TeX l. 15 | `inutile` | — | medium |
| 33 | 050 | TeX l. 15 | `injectives` | — | medium |
| 33 | 050 | TeX l. 19; deletion | `i` | — | low |
| 33 | 050 | TeX l. 27 | `ouverte` | — | medium |
| 33 | 050 | TeX l. 30; deletion | `\mathbb{R}` | — | low |
| 33 | 050 | TeX l. 32 | `unique` | — | low |
| 33 | 050 | TeX l. 34 | `p.ex.` | — | low |
| 33 | 050 | TeX l. 40 | `il` | `la` | low |
| 33 | 050 | TeX l. 40; deletion | `foncteur` | `formule` | low |
| 33 | 050 | TeX l. 40 | `existe` | `évidente` | low |
| 33 | 050 | TeX l. 40 | `isom.` | — | low |
| 33 | 050 | TeX l. 41 | `nature` | — | low |
| 33 | 050 | TeX l. 41; deletion | `i` | — | low |
| 33 | 050 | TeX l. 42 | `ouverte` | — | low |
| 33 | 050 | TeX l. 42 | `entre` | — | low |
| 33 | 050 | TeX l. 42 | `fait` | — | low |
| 33 | 052 | TeX l. 3 | `général` | — | medium |
| 33 | 052 | TeX l. 3 | `ouverts` | — | medium |
| 33 | 052 | TeX l. 4 | `qu'on` | — | medium |
| 33 | 052 | TeX l. 4 | `isom.` | — | medium |
| 33 | 052 | TeX l. 6; deletion | `un` | — | low |
| 33 | 052 | TeX l. 6; deletion | `un` | — | low |
| 33 | 052 | TeX l. 6; deletion | `foncteur` | — | low |
| 33 | 052 | TeX l. 10 | `ouverts` | — | medium |
| 33 | 052 | TeX l. 13; deletion | `on` | — | low |
| 33 | 052 | TeX l. 18 | `-` | `\longrightarrow` | medium |
| 33 | 052 | TeX l. 20 | `ouverte` | — | medium |
| 33 | 052 | TeX l. 22; deletion | `aux` | — | low |
| 33 | 052 | TeX l. 22 | `sur` | — | medium |
| 33 | 052 | TeX l. 27; deletion | `$\mathbb{R}i$` | — | low |
| 33 | 052 | TeX l. 30 | `*` | `!` | medium |
| 33 | 052 | TeX l. 30; deletion | `i` | — | low |
| 33 | 052 | TeX l. 30; deletion | `)` | — | low |
| 33 | 052 | TeX l. 32 | `essentiellement` | — | medium |
| 33 | 052 | TeX l. 32 | `triviale` | — | medium |
| 33 | 053 | TeX l. 16 | `f_{V'}` | `f'_V` | medium |
| 33 | 054 | TeX l. 4; deletion | `commutant` | — | low |
| 33 | 054 | TeX l. 4; deletion | `produits` | — | low |
| 33 | 054 | TeX l. 10 | `G^\bullet` | `U^\bullet` | medium |
| 33 | 054 | TeX l. 18 | `C^\bullet` | `G^\bullet` | medium |
| 33 | 054 | TeX l. 21; deletion | `(G^\bullet(G))` | — | low |
| 33 | 054 | TeX l. 26 | `explicite` | — | medium |
| 33 | 054 | TeX l. 26 | `-` | `\longrightarrow` | medium |
| 33 | 054 | TeX l. 30; deletion | `G` | — | low |
| 33 | 054 | TeX l. 33 | `même` | — | medium |
| 33 | 056 | TeX l. 5 | `i` | — | medium |
| 33 | 056 | TeX l. 7 | `S` | — | medium |
| 33 | 056 | TeX l. 10; deletion | `absolu` | — | low |
| 33 | 056 | TeX l. 14; deletion | `lisse` | — | low |
| 33 | 056 | TeX l. 14; deletion | `pour` | — | low |
| 33 | 056 | TeX l. 14; deletion | `f` | — | low |
| 33 | 056 | TeX l. 16; deletion | `suivante` | — | low |
| 33 | 056 | TeX l. 18 | `f_*` | `g_*` | medium |
| 33 | 056 | TeX l. 20 | `G^\bullet` | — | medium |
| 33 | 056 | TeX l. 21; deletion | `C` | — | low |
| 33 | 056 | TeX l. 27 | `réduit` | — | medium |
| 33 | 056 | TeX l. 33 | `f^*` | `f^!` | medium |
| 33 | 056 | TeX l. 36; deletion | `si` | — | low |
| 33 | 056 | TeX l. 39; deletion | `transitivité` | — | low |
| 33 | 056 | TeX l. 40; deletion | `et` | — | low |
| 33 | 056 | TeX l. 42 | `quelconques` | — | medium |
| 33 | 056 | TeX l. 44 | `alors` | — | medium |
| 33 | 056 | TeX l. 44; deletion | `pour` | — | low |
| 33 | 056 | TeX l. 44; deletion | `être` | — | low |
| 33 | 056 | TeX l. 45 | `dès qu'on a` | — | medium |
| 33 | 056 | TeX l. 45 | `voulus` | — | medium |
| 33 | 056 | TeX l. 45 | `ces` | — | medium |
| 33 | 056 | TeX l. 45 | `immers.` | — | medium |
| 33 | 056 | TeX l. 46 | `can.` | — | medium |
| 33 | 056 | TeX l. 47 | `cup-produits` | — | medium |
| 33 | 056 | TeX l. 52 | `\sim` | — | medium |
| 33 | 056 | TeX l. 53 | `\ldots` | `--` | medium |
| 33 | 056 | TeX l. 56; deletion | `avec` | — | low |
| 33 | 056 | TeX l. 56; deletion | `f` | — | low |
| 33 | 057 | TeX l. 10 | `resp.` | — | medium |
| 33 | 058 | TeX l. 3 | `\ldots` | `--` | medium |
| 33 | 058 | TeX l. 9 | `On` | — | medium |
| 33 | 058 | TeX l. 9 | `formule` | — | medium |
| 33 | 058 | TeX l. 12 | `de` | — | medium |
| 33 | 058 | TeX l. 12 | `f` | `j` | medium |
| 33 | 058 | TeX l. 14 | `-` | `\longrightarrow` | medium |
| 33 | 058 | TeX l. 24 | `i` | — | medium |
| 33 | 058 | TeX l. 30 | `shiftant` | — | medium |
| 33 | 058 | TeX l. 34; deletion | `*` | — | low |
| 33 | 058 | TeX l. 36; deletion | `par` | — | low |
| 33 | 058 | TeX l. 41; deletion | `ainsi` | — | low |
| 33 | 058 | TeX l. 42 | `suppose` | — | medium |
| 33 | 058 | TeX l. 43 | `ennui` | — | medium |
| 33 | 058 | TeX l. 43 | `degré` | `degrés` | medium |
| 33 | 058 | TeX l. 44 | `complexe` | — | medium |
| 33 | 060 | TeX l. 3; deletion | `foncteurs` | — | low |
| 33 | 060 | TeX l. 3 | `foncteurs` | — | low |
| 33 | 060 | TeX l. 3 | `au` | — | low |
| 33 | 060 | TeX l. 3 | `départ` | — | low |
| 33 | 060 | TeX l. 5 | `haut` | — | low |
| 33 | 060 | TeX l. 7 | `connu` | — | low |
| 33 | 060 | TeX l. 9; deletion | `lisse` | — | low |
| 33 | 060 | TeX l. 9; deletion | `sur` | — | low |
| 33 | 060 | TeX l. 9; deletion | `affine` | — | low |
| 33 | 060 | TeX l. 9; deletion | `\ldots` | `--` | low |
| 33 | 060 | TeX l. 13; deletion | `\mathbb{R}` | — | low |
| 33 | 060 | TeX l. 13; deletion | `cohomol` | — | low |
| 33 | 060 | TeX l. 13; deletion | `\Gamma'` | — | low |
| 33 | 060 | TeX l. 15 | `Affinement` | — | low |
| 33 | 060 | TeX l. 15; deletion | `$\mathbb{R}$` | — | low |
| 33 | 060 | TeX l. 15; deletion | `ne` | — | low |
| 33 | 060 | TeX l. 15; deletion | `dépend` | — | low |
| 33 | 060 | TeX l. 15; deletion | `pas` | — | low |
| 33 | 060 | TeX l. 15; deletion | `de` | — | low |
| 33 | 060 | TeX l. 15; deletion | `X^c` | — | low |
| 33 | 060 | TeX l. 15; deletion | `peut-être` | — | low |
| 33 | 060 | TeX l. 16; deletion | `des` | — | low |
| 33 | 060 | TeX l. 16; deletion | `raisons` | — | low |
| 33 | 060 | TeX l. 16; deletion | `des` | — | low |
| 33 | 060 | TeX l. 16; deletion | `coefficients` | — | low |
| 33 | 060 | TeX l. 16; deletion | `2` | `l` | low |
| 33 | 062 | TeX l. 5 | `-` | `\longrightarrow` | medium |
| 33 | 062 | TeX l. 5 | `-` | `\longrightarrow` | medium |
| 33 | 062 | TeX l. 5 | `nous` | — | low |
| 33 | 062 | TeX l. 5 | `on sait` | `savons` | low |
| 33 | 062 | TeX l. 7 | `\lhook\joinrel-` | `\hookrightarrow` | medium |
| 33 | 062 | TeX l. 16; deletion | `\mathbb{R}f^!` | — | low |
| 33 | 062 | TeX l. 17 | `-` | `\longrightarrow` | medium |
| 33 | 062 | TeX l. 21; deletion | `(F)` | — | low |
| 33 | 062 | TeX l. 21 | `i` | `f` | low |
| 33 | 062 | TeX l. 23 | `---` | — | low |
| 33 | 062 | TeX l. 23 | `dans` | — | low |
| 33 | 062 | TeX l. 23 | `---` | — | low |
| 33 | 064 | TeX l. 6 | `!` | `*` | low |
| 33 | 064 | TeX l. 12 | `donné` | — | low |
| 33 | 064 | TeX l. 12 | `\sigma` | — | medium |
| 33 | 064 | TeX l. 12 | `une factorisation` | — | low |
| 33 | 064 | TeX l. 13 | `à prouver` | `à préciser` | low |
| 33 | 064 | TeX l. 15 | `absolue` | — | low |
| 33 | 064 | TeX l. 16 | `droit` | `décal.` | low |
| 33 | 064 | TeX l. 16 | `\ldots` | — | medium |
| 33 | 064 | TeX l. 17; deletion | `isom` | — | low |
| 33 | 064 | TeX l. 17; deletion | `au` | — | low |
| 33 | 064 | TeX l. 17 | `moyen` | — | low |
| 33 | 066 | TeX l. 2; deletion | `des variances` | — | low |
| 33 | 066 | TeX l. 4; deletion | `!` | — | low |
| 33 | 066 | TeX l. 4; deletion | `*` | — | low |
| 33 | 066 | TeX l. 4; deletion | `!` | — | low |
| 33 | 066 | TeX l. 4; deletion | `*` | — | low |
| 33 | 066 | TeX l. 4 | `le définira` | — | low |
| 33 | 066 | TeX l. 4; deletion | `respect.` | — | low |
| 33 | 066 | TeX l. 4 | `un` | — | low |
| 33 | 066 | TeX l. 4 | `*` | — | low |
| 33 | 066 | TeX l. 8; deletion | `i` | — | low |
| 33 | 066 | TeX l. 17 | `\cdot` | — | medium |
| 33 | 066 | TeX l. 18 | `-` | `\longrightarrow` | medium |
| 33 | 066 | TeX l. 18; deletion | `morphisme` | — | low |
| 33 | 066 | TeX l. 18; deletion | `de` | — | low |
| 33 | 066 | TeX l. 18 | `X'` | — | low |
| 33 | 066 | TeX l. 18 | `sur` | — | low |
| 33 | 066 | TeX l. 22; deletion | `X'` | — | low |
| 33 | 066 | TeX l. 24 | `\sigma` | — | medium |
| 33 | 068 | TeX l. 4 | `A` | `\alpha` | medium |
| 33 | 068 | TeX l. 5; deletion | `(\mathbb{R}^!g)` | — | low |
| 33 | 068 | TeX l. 5; deletion | `!` | — | low |
| 33 | 068 | TeX l. 7; deletion | `et` | — | low |
| 33 | 068 | TeX l. 16 | `A` | `\alpha` | medium |
| 33 | 068 | TeX l. 18; deletion | `!` | — | low |
| 33 | 068 | TeX l. 18; deletion | `\sigma` | — | low |
| 33 | 068 | TeX l. 19; deletion | `!` | — | low |
| 33 | 068 | TeX l. 24 | `g'` | — | low |
| 33 | 068 | TeX l. 24; deletion | `!` | — | low |
| 33 | 068 | TeX l. 25; deletion | `\mathbb{R}^!\operatorname{id}_{\mathrm D^+(Y')}` | — | low |
| 33 | 068 | TeX l. 32; deletion | `(\mathbb{R}i^!)` | — | low |
| 33 | 068 | TeX l. 35; deletion | `\mathbb{R}i^!` | — | low |
| 33 | 068 | TeX l. 36; deletion | `(a)` | — | low |
| 33 | 068 | TeX l. 42; deletion | `\mathbb{R}i^!` | — | low |
| 33 | 068 | TeX l. 45 | `$Y$-schémas` | — | low |
| 33 | 068 | TeX l. 45 | `lisses envisagés` | — | low |
| 33 | 068 | TeX l. 45 | `\ldots` | — | medium |
| 33 | 069 | TeX l. 11 | `object` | — | medium |
| 33 | 069 | TeX l. 13 | `injectives` | — | medium |
| 33 | 070 | TeX l. 2; deletion | `la $\Omega^d$` | — | low |
| 33 | 070 | TeX l. 9 | `\ldots` | — | medium |
| 33 | 070 | TeX l. 12 | `l'admettrons` | `l'admettons` | medium |
| 33 | 070 | TeX l. 12 | `saurait` | — | medium |
| 33 | 070 | TeX l. 12 | `énoncées` | — | medium |
| 33 | 072 | TeX l. 2; deletion | `par une immersion` | — | low |
| 33 | 072 | TeX l. 4; deletion | `À généraliser` | — | low |
| 33 | 072 | TeX l. 5 | `un` | `aussi` | low |
| 33 | 072 | TeX l. 5 | `pt technique` | — | low |
| 33 | 072 | TeX l. 6; deletion | `si $f$ est défini` | — | low |
| 33 | 072 | TeX l. 9 | `-` | `\longrightarrow` | medium |
| 33 | 073 | TeX l. 7 | `.:` | — | medium |
| 33 | 074 | TeX l. 3; deletion | `lisse` | — | low |
| 33 | 074 | TeX l. 5; deletion | `ferm.` | — | low |
| 33 | 074 | TeX l. 14 | `redéfinir` | — | medium |
| 33 | 074 | TeX l. 15; deletion | `\mathbb{R}_!g_*` | — | low |
| 33 | 074 | TeX l. 20 | `i` | `g` | medium |
| 33 | 074 | TeX l. 26; deletion | `\mathbb{R}^{2r}` | — | low |
| 33 | 074 | TeX l. 27 | `+` | `-` | medium |
| 33 | 074 | TeX l. 28; deletion | `+2d` | — | low |
| 33 | 074 | TeX l. 30; deletion | `-2d` | — | low |
| 33 | 074 | TeX l. 30 | `)` | — | medium |
| 33 | 074 | TeX l. 39; deletion | `*` | — | low |
| 33 | 075 | TeX l. 16 | `\vartheta` | `\delta` | low |
| 33 | 075 | TeX l. 16 | `\vartheta` | `\delta` | low |
| 33 | 075 | TeX l. 16 | `\vartheta` | `\delta` | low |
| 33 | 075 | TeX l. 16 | `\vartheta` | `\delta` | low |
| 33 | 076 | TeX l. 3; deletion | `4` | `5` | low |
| 33 | 076 | TeX l. 20; deletion | `\mathbb{R}_!f` | — | low |
| 33 | 076 | TeX l. 23 | `-` | `\longrightarrow` | medium |
| 33 | 076 | TeX l. 31 | `rend` | — | medium |
| 33 | 077 | TeX l. 26 | `\vartheta` | `\delta` | low |
| 33 | 077 | TeX l. 28 | `\vartheta` | `\delta` | low |
| 33 | 078 | TeX l. 2 | `un` | — | medium |
| 33 | 078 | TeX l. 3; deletion | `fais` | — | low |
| 33 | 078 | TeX l. 3 | `cplxe` | — | medium |
| 33 | 078 | TeX l. 4 | `on a commutativité dans` | — | medium |
| 33 | 078 | TeX l. 14; deletion | `\mathbb{R}i^!\mathbb{R}` | — | low |
| 33 | 078 | TeX l. 17 | `i_!` | `i_*` | medium |
| 33 | 079 | TeX l. 21 | `\gamma` | `\chi` | medium |
| 33 | 080 | TeX l. 2; deletion | `isomorphismes` | — | low |
| 33 | 080 | TeX l. 5; deletion | `en` | — | low |
| 33 | 080 | TeX l. 5 | `se servira parfois de` | — | medium |
| 33 | 080 | TeX l. 11 | `dém.` | — | medium |
| 33 | 080 | TeX l. 15; deletion | `G^\bullet` | — | low |
| 33 | 080 | TeX l. 21; deletion | `g^!` | — | low |
| 33 | 080 | TeX l. 21; deletion | `-2d` | `2d` | low |
| 33 | 080 | TeX l. 31; deletion | `h` | — | low |
| 33 | 080 | TeX l. 31 | `partout` | — | medium |
| 33 | 080 | TeX l. 35 | `+` | `\,` | medium |
| 33 | 080 | TeX l. 35 | `d_{X/Y}` | — | medium |
| 33 | 080 | TeX l. 43 | `relative absolue` | — | low |
| 33 | 081 | TeX l. 4 | `m` | — | medium |
| 33 | 081 | TeX l. 17; deletion | `R` | — | low |
| 33 | 081 | TeX l. 21 | `15.7.1.7` | `19.7.1.7` | medium |
| 33 | 081 | TeX l. 29; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 081 | TeX l. 46 | `d` | — | medium |
| 33 | 081 | TeX l. 47; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 082 | TeX l. 2 | `trouve` | — | medium |
| 33 | 082 | TeX l. 3 | `lissité` | — | medium |
| 33 | 082 | TeX l. 6; deletion | `Z` | — | low |
| 33 | 082 | TeX l. 16 | `globalement` | — | medium |
| 33 | 082 | TeX l. 21 | `-` | `\longrightarrow` | medium |
| 33 | 082 | TeX l. 26 | `d'abord` | — | medium |
| 33 | 082 | TeX l. 28 | `qu'on` | — | medium |
| 33 | 083 | TeX l. 19; deletion | `physically unreadable: estimated 3 word(s)` | `no recoverable reading` | low |
| 33 | 083 | TeX l. 19; deletion | `\underline p` | — | low |
| 33 | 083 | TeX l. 19; deletion | `physically unreadable: estimated 2 word(s)` | `no recoverable reading` | low |
| 33 | 083 | TeX l. 21; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 083 | TeX l. 36; deletion | `physically unreadable: estimated 5 word(s)` | `no recoverable reading` | low |
| 33 | 083 | TeX l. 52; deletion | `canoniquement` | — | low |
| 33 | 083 | TeX l. 54; deletion | `homogènes` | — | low |
| 33 | 083 | TeX l. 57; deletion | `homogènes` | — | low |
| 33 | 084 | TeX l. 3; deletion | `$\mathbb{R}^!f$` | — | low |
| 33 | 084 | TeX l. 8; deletion | `et` | — | low |
| 33 | 084 | TeX l. 12 | `-` | `\longrightarrow` | medium |
| 33 | 084 | TeX l. 18 | `-` | `\longrightarrow` | medium |
| 33 | 084 | TeX l. 19; deletion | `\mathbb{R}\Gamma\mathcal H` | — | low |
| 33 | 084 | TeX l. 20 | `-` | `\longrightarrow` | medium |
| 33 | 084 | TeX l. 30 | `\textcircled{$*$}` | — | medium |
| 33 | 084 | TeX l. 39 | `-` | `\longrightarrow` | medium |
| 33 | 084 | TeX l. 40; deletion | `\mathbb{R}^i` | — | low |
| 33 | 085 | TeX l. 5; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 085 | TeX l. 19 | `M` | `N` | medium |
| 33 | 085 | TeX l. 24; deletion | `physically unreadable: estimated 2 word(s)` | `no recoverable reading` | low |
| 33 | 085 | TeX l. 26; deletion | `des` | — | low |
| 33 | 085 | TeX l. 30; deletion | `prouvé` | — | low |
| 33 | 085 | TeX l. 35; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 085 | TeX l. 37; deletion | `identifie` | — | low |
| 33 | 086 | TeX l. 2; deletion | `6` | — | low |
| 33 | 086 | TeX l. 3; deletion | `Trans` | — | low |
| 33 | 086 | TeX l. 4; deletion | `L'hom des homomorphismes de Gysin` | — | low |
| 33 | 086 | TeX l. 7 | `opérations entre espaces diff.` | — | low |
| 33 | 086 | TeX l. 8 | `opérations internes` | — | low |
| 33 | 086 | TeX l. 11 | `par préschémas relatifs` | `par préschémas locltft` | low |
| 33 | 086 | TeX l. 18; deletion | `\mathrm{Trs}*1` | — | low |
| 33 | 086 | TeX l. 19 | `\mathrm{Trs}*2` | — | medium |
| 33 | 086 | TeX l. 19 | `f` | `g` | low |
| 33 | 086 | TeX l. 23 | `\mathrm{Trs}!1` | — | medium |
| 33 | 086 | TeX l. 24 | `\mathrm{Tr}` | — | medium |
| 33 | 086 | TeX l. 45; deletion | `pour des` | — | low |
| 33 | 086 | TeX l. 45 | `se borne seulement à` | — | low |
| 33 | 086 | TeX l. 49 | `prendre ceci` | — | low |
| 33 | 087 | TeX l. 11 | `identifier aux précédents` | — | low |
| 33 | 087 | TeX l. 12 | `oublier que comme d'ident des deux dernières flèches` | — | low |
| 33 | 087 | TeX l. 14; deletion | `gr` | — | low |
| 33 | 087 | TeX l. 21 | `vicieuse` | — | low |
| 33 | 087 | TeX l. 22 | `1` | — | low |
| 33 | 087 | TeX l. 31 | `N` | `M` | low |
| 33 | 087 | TeX l. 60; deletion | `donc` | — | low |
| 33 | 087 | TeX l. 66 | `\operatorname{gr}_\bullet` | `\operatorname{gr}^\bullet_\bullet` | medium |
| 33 | 088 | TeX l. 2 | `décomposent` | — | medium |
| 33 | 088 | TeX l. 11 | `Q` | `2` | medium |
| 33 | 088 | TeX l. 12 | `Q` | `2` | medium |
| 33 | 088 | TeX l. 18 | `compatibilités` | `compatibilité` | medium |
| 33 | 088 | TeX l. 20; deletion | `Isom` | — | low |
| 33 | 089 | TeX l. 27 | `\operatorname{gr}''(j)` | `\operatorname{gr}'(j)` | medium |
| 33 | 089 | TeX l. 41; deletion | `conjonction` | — | low |
| 33 | 089 | TeX l. 43; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 089 | TeX l. 44; deletion | `f)` | — | low |
| 33 | 089 | TeX l. 54 | `préadi-` | — | medium |
| 33 | 090 | TeX l. 2; deletion | `Pour.` | — | low |
| 33 | 090 | TeX l. 3 | `ici, ce qui simplifie` | — | low |
| 33 | 090 | TeX l. 20 | `\mathbb{R}f` | `\mathbb{R}f_*` | medium |
| 33 | 090 | TeX l. 24 | `\mathbb{R}_{\deleted{\unsure{!}}}f_*` | `\mathbb{R}_!f` | medium |
| 33 | 090 | TeX l. 24; deletion | `!` | — | low |
| 33 | 090 | TeX l. 25 | `\mathbb{R}_{\deleted{\unsure{!}}}f_*` | `\mathbb{R}_!f` | medium |
| 33 | 090 | TeX l. 25; deletion | `!` | — | low |
| 33 | 090 | TeX l. 28; deletion | `Idem pour` | — | low |
| 33 | 090 | TeX l. 30 | `const. au $f$` | — | low |
| 33 | 090 | TeX l. 31 | `fais` | — | low |
| 33 | 090 | TeX l. 31; deletion | `on` | — | low |
| 33 | 090 | TeX l. 31; deletion | `constructible` | — | low |
| 33 | 090 | TeX l. 32; deletion | `physically unreadable: estimated 4 word(s)` | `no recoverable reading` | low |
| 33 | 090 | TeX l. 32; deletion | `changement` | — | low |
| 33 | 090 | TeX l. 32; deletion | `physically unreadable: estimated 3 word(s)` | `no recoverable reading` | low |
| 33 | 090 | TeX l. 32; deletion | `\mathbb{R}f_*` | — | low |
| 33 | 090 | TeX l. 34; deletion | `for` | — | low |
| 33 | 090 | TeX l. 42; deletion | `\mathbb{R}` | — | low |
| 33 | 091 | TeX l. 13; deletion | `le` | — | low |
| 33 | 091 | TeX l. 27; deletion | `\operatorname{gr}_{\underline K}^\bullet(A)` | — | low |
| 33 | 091 | TeX l. 30; deletion | `canonique` | — | low |
| 33 | 091 | TeX l. 38; deletion | `\operatorname{gr}_\bullet(R)` | — | low |
| 33 | 091 | TeX l. 47; deletion | `\operatorname{gr}_{\underline K}^\bullet(A)` | — | low |
| 33 | 091 | TeX l. 54 | `\{` | `f` | medium |
| 33 | 091 | TeX l. 57; deletion | `nous` | — | low |
| 33 | 092 | TeX l. 2 | `\ldots` | — | medium |
| 33 | 092 | TeX l. 6 | `à être` | `: être` | medium |
| 33 | 092 | TeX l. 22 | `à priori quelle` | — | medium |
| 33 | 092 | TeX l. 22 | `?` | — | medium |
| 33 | 092 | TeX l. 27; deletion | `*` | — | low |
| 33 | 092 | TeX l. 29; deletion | `*` | — | low |
| 33 | 092 | TeX l. 30; deletion | `\mathbb{R}^*` | — | low |
| 33 | 092 | TeX l. 30; deletion | `*` | — | low |
| 33 | 092 | TeX l. 36; deletion | `*` | — | low |
| 33 | 092 | TeX l. 36; deletion | `*` | — | low |
| 33 | 092 | TeX l. 42 | `se décompose en cas lisse` | — | medium |
| 33 | 092 | TeX l. 65 | `\ldots` | — | medium |
| 33 | 093 | TeX l. 3; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 093 | TeX l. 4; deletion | `$\operatorname{gr}_{\underline K}^\bullet(M)$` | — | low |
| 33 | 093 | TeX l. 4; deletion | `physically unreadable: estimated 6 word(s)` | `no recoverable reading` | low |
| 33 | 093 | TeX l. 6 | `)` | `/` | medium |
| 33 | 093 | TeX l. 11; deletion | `et` | — | low |
| 33 | 093 | TeX l. 11; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 093 | TeX l. 14; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 093 | TeX l. 15 | `M` | — | medium |
| 33 | 093 | TeX l. 16; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 093 | TeX l. 16; deletion | `physically unreadable: estimated 1 word(s)` | `no recoverable reading` | low |
| 33 | 093 | TeX l. 17; deletion | `physically unreadable: estimated 5 word(s)` | `no recoverable reading` | low |
| 33 | 094 | TeX l. 9 | `s` | — | low |
| 33 | 094 | TeX l. 11; deletion | `$\mathbb{L}$` | — | low |
| 33 | 094 | TeX l. 12 | `si le premier est` | — | low |
| 33 | 094 | TeX l. 12; deletion | `borné` | — | low |
| 33 | 094 | TeX l. 13; deletion | `degré` | `de` | low |
| 33 | 094 | TeX l. 15; deletion | `C'est local, on peut supposer` | — | low |
| 33 | 094 | TeX l. 15; deletion | `passage à la limite on peut supposer que` | — | low |
| 33 | 094 | TeX l. 15; deletion | `est noethérien` | — | low |
| 33 | 094 | TeX l. 20; deletion | `$\mathbb{R}$` | — | low |
| 33 | 094 | TeX l. 20; deletion | `F'` | `G'` | low |
| 33 | 094 | TeX l. 20; deletion | `-` | `\longrightarrow` | low |
| 33 | 094 | TeX l. 21; deletion | `donc pour` | — | low |
| 33 | 094 | TeX l. 22; deletion | `tout ceci on peut supposer que` | `toute cette on peut supposer que` | low |
| 33 | 094 | TeX l. 23; deletion | `\mathbb{R}` | — | low |
| 33 | 094 | TeX l. 23; deletion | `G'` | `F'` | low |
| 33 | 094 | TeX l. 25; deletion | `si fini` | — | low |
| 33 | 094 | TeX l. 26; deletion | `a une présentation` | — | low |
| 33 | 094 | TeX l. 27; deletion | `somme directe de` | — | low |
| 33 | 094 | TeX l. 28; deletion | `-` | `\longrightarrow` | low |
| 33 | 094 | TeX l. 29; deletion | `étale` | — | low |
| 33 | 094 | TeX l. 29; deletion | `affine` | — | low |
| 33 | 094 | TeX l. 30; deletion | `de là que cela revient au cas où` | — | low |
| 33 | 096 | TeX l. 3 | `F'` | `F` | medium |
| 33 | 096 | TeX l. 22 | `-` | `\longrightarrow` | medium |
| 33 | 096 | TeX l. 36 | `X'` | `X` | medium |
| 33 | 096 | TeX l. 38 | `X'` | `X` | medium |
| 33 | 096 | TeX l. 39; deletion | `*` | — | low |
| 33 | 096 | TeX l. 39; deletion | `X` | — | low |
| 33 | 096 | TeX l. 43; deletion | `$f^*$` | — | low |
| 33 | 096 | TeX l. 45 | `étant` | — | medium |

## Secure-looking anomalies deliberately preserved

These entries prevent the uncertainty table from being mistaken for a list of proposed corrections.

| File | Scan | Approximate source location | Reading retained | Possible expectation, not substituted | Confidence in the ink |
|---|---|---|---|---|---|
| 33 | 050 | middle functor definition | C(Y)→C(X) | Reversing the categories to fit the inverse-image variance | high |
| 33 | 053 | proof, second half | x∈V∈U; later f=f′ without tildes | Replacing membership by inclusion or supplying tildes | high |
| 33 | 055 | first diagram | upper label r_xU | r_xV from the apparent endpoints | high |
| 33 | 057 | middle/lower typescript | diagramatics; dim lim; A_ij | Modernized spelling, dir lim, or A_i | high |
| 33 | 059 | Hom formula | Hom(G.A_i) | A comma | high |
| 33 | 061 | middle calculation | missing closing parenthesis | Balancing the printed expression | high |
| 33 | 063 | sheaf diagram | F(U_i) at both ends of the restriction arrow | F(U_j) as its target | high |
| 33 | 065 | first paragraph | A→B iff B⊃A, with “reversal of order” | Reversing the displayed inclusion | high |
| 33 | 067 | proof | k_i h; A_i in the B_i discussion | A corrected factor order or object letter | high |
| 33 | 069 | condition iv | e xact | Closing the visibly typed space | high |
| 33 | 071 | upper proof | D′(i)′; for for; open exact sequence | Removing the extra prime/word or adding a zero | high |
| 33 | 073 | diagramatic axiom | g=dir lim A_i→Y; Ker g : l.u.b. | Replacing = or : by expected punctuation | high |
| 33 | 074 | final cohomology target | T_X/S | A twist on a different scheme | high |
| 33 | 075 | root calculations | two strict >0 signs; 2α_1+α_3; 3≤i≤8 | Corrected inequalities, roots or endpoint | high |
| 33 | 080 | two successive twist formulas | no inverse on first T_Y/Z; inverse on next | Inserting a missing inverse in the first line | high |
| 33 | 085 | definition of P | unclosed parenthesis | Completing the definition typographically | high |
| 33 | 089 | final word fragment | préadi- | Completing it to préadique before the next sheet | medium |
| 33 | 090 | projection displays | first RHom argument placement; no inverse image on G in tensor RHS | Rewriting to a standard projection formula | high for the visible letters; operator overwrites remain uncertain |
| 33 | 091 | first paragraph | sous-gr_L(A)-algèbre | sous-module | high |
| 33 | 093 | upper formula | repeated equality at line turn | Dropping one equality mark | high |
| 33 | 095 | homotopy display | F_U then F_u | Making both subscripts capital U | high |
| 33 | 096 | display chain | blank parentheses; f′* inside Rj!; extra ) after j_!F′ | Filling arguments or repairing the domain/parenthesis | medium to high; ambiguous letters remain marked |
| 33 | 097 | first paragraph and ending | theelements; final “by” | Inserting a space or supplying the absent next formula | high |

## Abbreviations encountered

Expansions here are editorial hypotheses only. An abbreviation is never expanded inside the transcription; punctuation variants remain as written.

| Written form | Tentative expansion or interpretation |
|---|---|
| th, th., Th., thm | théorème / theorem, according to language |
| hom | homomorphisme |
| isom, isom. | isomorphisme |
| can., can | canonique |
| cat. | catégorie / category |
| imm., immers. | immersion |
| ferm. | fermée |
| dém. | démonstration |
| p.ex., p. ex., ex. | par exemple; context distinguishes a numbered example |
| i.e. | id est / that is |
| resp., respect. | respectivement / respectively |
| cf, cf. | confer / compare |
| prop., Prop. | proposition |
| cor. | corollaire |
| chap. | chapitre |
| n°, N° | numéro |
| pp. | pages |
| éd. | édition |
| Alg. comm. | Algèbre commutative |
| Ex. | Example or Exercice, as appropriate to the reference |
| § | section |
| loc, loc. | localement / locally |
| loc. const., loc. constant | localement constant |
| dim, dim. | dimension |
| rel. | relative |
| codim. | codimension |
| sup. | supérieur / supérieure |
| diff. | différents / différentes |
| ch., chang., changt | changement |
| fond | fondamentale(s) |
| cohomol | cohomologique / cohomologie; the cancelled occurrence060 is uncertain |
| fais | faisceau |
| cplxe | complexe |
| hyp | hypothèse |
| pb | problème |
| pt | point, in the uncertain phrase “pt technique” on072 |
| tt | tout, on074; abbreviation preserved |
| locltft | localement de type fini; candidate reading is uncertain and subordinate to the revised “relatifs” on086 |
| N.B., NB | nota bene |
| CQFD | ce qu'il fallait démontrer |
| Ob | objets |
| id | identité |
| Tr | trace |
| gr | gradué associé |
| Ass | associated primes / idéaux premiers associés |
| Supp | support |
| Ker, ker | kernel / noyau |
| Cok, cok | cokernel / conoyau |
| dir lim, dir. lim | direct limit; the separate source reading “dim lim” is not corrected |
| inv lim | inverse limit |
| l.u.b, l.u.b. | least upper bound |
| SGA | Séminaire de géométrie algébrique; the cancelled volume numeral on076 remains uncertain |

## Legibility and limits

The handwritten duality pages are substantially harder than the reused typescripts: long words often collapse into a few joined strokes, superscripts can overlap corrections, and several very small marginal passages remain weak readings. Least reliable are the bottom of050, the cancellations on060, the prose joins on062/064/066/068/072, the last annotation on080, the small heading and bottom corrections on086, the upper-right margin on087, the shaded left margin on090, and the nested abandoned reductions on094. In the EGA sheets081–093, much of the live typescript is clear but several blacked-out prose deletions are physically unrecoverable; the estimated word counts do not assert that the lost words have been identified.

All 48 whole images and both supplied halves were personally inspected without OCR, then each page received a second visual audit. The upside-down EGA sheets were rotated only for inspection. Faint mirror-image show-through was distinguished from writing on the exposed face; it was not reconstructed as an additional text. Lower-left pencil foliation is recorded with `\mspage` without attributing it to the author. The supplied archive attribution does not establish authorship of every reused typescript, and the transcription makes no such inference.

TikZ represents shapes, connectors and positions approximately, while preserving written labels and visible arrow directions; it is not a facsimile. Source errors, unfinished words, open parentheses and blank arguments remain in place. No reading was silently completed from another manuscript, a publication, or the context archive. The first-pass records are retained as a history of the work; where an audit changed a reading, the final page file and this table govern.
