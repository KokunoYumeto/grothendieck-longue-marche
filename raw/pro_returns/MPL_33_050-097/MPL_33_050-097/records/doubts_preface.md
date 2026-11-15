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
