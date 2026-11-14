# Diplomatic transcription: notation and doubts

## Notation table — checked before freezing

The table records the glyphs read in this package and their LaTeX representations. The same root reader transcribed and audited all 43 pages from the images, without OCR or access to the context ZIP. Recurrence was checked across the pages; unresolved differences remain marked at their actual occurrences. A clearer neighbouring formula has not been used to supply a stroke absent from another occurrence.

| Ink / usage | LaTeX representation | Scans and comparison outcome |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes | Throughout; no typographic double quotation marks substituted. |
| Single / double underline | `\uline{…}`, `\uuline{…}` | Throughout. The short descending stroke of handwritten g in *singulier* on 026–027 has not been treated as a separate underline. |
| Cancellation / insertion / independent margin | `\deleted{…}`, `\inserted{…}`, `\margin{…}` | Throughout; surviving cancelled letters retained, including inside diagrams. |
| Circled words, labels and objects | `\textcircled`, TikZ ellipse/circle | 011, 017, 041, 043; circles checked separately from ordinary parentheses. |
| Square enclosure | `\boxed`, TikZ straight enclosure | 043; retained alongside circled objects. |
| Ordinary set family F | `F`, with subscripts as drawn | 004–024; cancelled earlier initials separately marked. |
| Closed-member family | `F_0` | 006–010, 019; the 0 is a subscript. |
| Family restricted to a subset | `F_A`, `F_U`, `F_B` | 019–024; not replaced by sheaf notation. |
| Partition and its associated family | `\mathcal P`, `F_{\mathcal P}` | 011–022; looped P read consistently, with the uncertain alphabet recorded in the page doubts. |
| Script function algebra | `\mathcal A_F`, `\mathcal A_{(F_{\mathcal P})}` | 004–005, 011. |
| Double-stroked integer and real letters | `\mathbb Z`, `\mathbb R`, `\mathbb N` | 004, 022, 024, 043; ordinary Z in diagrams remains ordinary Z. |
| Triangular capital / lower-case coefficient letter | `\Lambda`, `\lambda` | 004–005, 011, 039; overwritten K/Λ retained as uncertain. |
| Characteristic-function letter | `\varphi_A` | 004–005; distinct visible forms of φ, Φ, π checked individually rather than inferred by role. |
| Upright algebra abbreviation | `\operatorname{Et}(X,\Lambda)` | 004–005; letters preserved. |
| Power-set letter | `\mathfrak P(X)` | 006–007, 015, 019; looped double-stroke P, medium confidence. |
| Interior circle / closure bar | `A^\circ`, `\overline A` | 005–024, 031–037; every bar and circle checked against its occurrence. |
| Dotted boundary letter | `\dot A`, `\dot Y` | 005–006, 009, 015, 018; explicit dot retained. |
| Boundary written with b | `bA`, `bF_i` | 006, 031–032; the literal b remains where written. |
| Complement sign | `\complement` | 005–009, 015, 018; unresolved grouping on 005 remains marked. |
| Greek condition labels | `\alpha`, `\beta`, `\gamma`, `\delta`, `\gamma'` | 007–009, 019; prime on γ′ checked. |
| Implication and inclusion signs | `\Rightarrow`, `\Longrightarrow`, `\Leftarrow`, `\subset`, `\supset`, `\leq`, `\geq` | Throughout. Literal d)/f) references on 012–013 and 018 are retained; the direction is read independently of the claimed proof. |
| Incidence order | `<`, uncertain `<`/`\le`, `\Longleftrightarrow` | 012–014, 031–034; uncertain first sign on 012 remains marked. |
| Finite family Phi | `\Phi`, `\Phi'` | 006, 015–018; prime positions retained. |
| Refinement-set letter | `\unsure{\mathcal E|\mathcal D}` | 016; both occurrences carry the same uncertainty. |
| Regularity family and subscripts | `F_r`, `Y_{\mathrm{reg}}`, `Y_{\mathrm{sing}}` | 017–018. |
| Regularity condition label | circled `\unsure{B|S}`; `\unsure{S|B}` | 017–018. Recomparison retains the two-lobed overwritten glyph on 017 and open S-like glyph on 018; their intended identification remains unresolved. |
| Ring over Y in regularity proof | `\mathring Y_{\mathrm{sing}}` | 018; retained in addition to the separately dotted Y. |
| Sheaf of subset germs | `\underline{\mathcal P}_X` | 020. |
| Generated sheaf / family of sections | `\underline F`, `\overline F`, `\overline{\overline F}` | 020, 023–024; underlines and one/two overbars counted separately. |
| Alternative sheaf notation | `\Phi_F`, `\Gamma(X,\Phi_F)` | 021; the change of notation is literal. |
| Compactified-real example | `\widehat{\mathbb R}` and a marked P¹(R)/S¹ reading | 022; the precise displayed uncertain alternatives are retained in the page. |
| Local finiteness / terminal index | literal `loc$^t$`, `X_{\unsure{n+2|n+1}}` | 023; the last digit has a curled 2-like stroke, without correction to an expected index. |
| Uniform dimension axiom | `(e_n)`, `\underline F`-dim | 024. |
| Mobility order | `\nu`, `\nu(x)`, `\nu_0` | 026–028; Greek ν compared with dimension indices n on 047. |
| Open mobility loci / complementary filtration | `\operatorname{Mob}^i(X)`, `F_i(X)`, `Y_i` | 027–028; literal uncertain `F_{3|2}` retained. |
| Pointed normal space | `(N,a)`, `(N_{i|\xi},a)` | 026–028; the literal uncertain a/N wording and y/x in Proposition C remain marked. |
| Script diagram of spaces | `\mathcal X=(X_i)_{i\in I}` | 030, 034, 039; plain X remains plain. |
| Primes on local charts | `X'`, `Y'`, `Z'` | 015–018, 030, 036–037; no prime converted to an exclamation mark. |
| Vertical isomorphism-like mark | `\unsure{\wr|2}` | 030; all four marks compared, with arrowhead/headless differences retained. |
| Filtration / entrance / closed leaf | `F_i`, `bF_i`, `\overline F_{i,\alpha}` | 031–037; *entrantes* and its uncertain endings preserved. |
| Sets of leaves | `\Phi_i`, `\Phi'_i` | 034, 037; margin on 037 visibly writes `\overline F'_i`, retained alongside body `\Phi'_i`. |
| Sheaf letters on a gluing diagram | `\mathcal F`, `\mathcal G`, `\mathcal X` | 039, 043; script style maintained. |
| Primes on gluing maps | `i'`, `p'` | 039; the unprimed p in the pushout diagram is retained as written. |
| Exceptional functor mark | `q_!`, `q^!`, `\alpha_!`, `\alpha^!` | 039; clear exclamation marks kept separate from primes. The two cramped `i^{*|!}` occurrences remain uncertain. |
| Upper / lower stars | `p^*`, `p_*`, `i^*`, `i'_*`, `p'_*` | 039; position of each star checked. |
| Stratum-index letters | `\Sigma`, `I`, `J`, `X_{I,J}`, `\alpha_{I,J/I',J'}` | 039. |
| Dualizing-complex mark | `K^\bullet_{X,\Lambda}` | 039; round raised dot retained. |
| Manifolds with boundary | `V_i^\circ` | 041, 043–047; the superscript circles have not been removed on semantic grounds. |
| Infinity-like superscript | `\unsure{\infty|\circ}` | 042; the two-loop ink remains the first reading despite neighbouring circles elsewhere. |
| Boundary operator and iterates | `\partial`, `\partial_j`, `\partial_{j,h}`, `\partial_{j>h>\ell>m}` | 039, 041–047; comma/order signs and missing base letters retained as locally written. |
| Dotted boundary / bullet | `\dot\partial`, `\partial^\bullet` | 041; unresolved placements explicitly marked. |
| Relative boundary | `\partial_{i/j}`, `\partial_{0/(j)}`, `\partial^{\unsure{\mathrm{pr}|\mathrm{rel}}}` | 041, 047; forms retained separately, without forcing a common notation. |
| Short index letters | `h`, `k`, `\ell` with local alternatives | 041, 047; the h/k switches are explicitly uncertain. |
| Facet / leaf letters | `\Phi_i`, `\Psi_i`, `F_i` | 041, 043; Φ and Ψ shapes checked at each occurrence. |
| Projection letters and decorations | `\pi`, `\pi'`, `\bar\pi`, `\partial\pi` | 043; the circled `\pi_{2,1,2|1}` retains first reading 2, beside the literal `\partial\pi_{2,1,1}`. |
| Prime and circle order | `V^{\circ\prime}`, `V^{\prime\circ}`, `U'`, `U''` | 044–045; order and multiplicity retained. Literal `\partial U` in item6 of044 has not received added primes. |
| Upper / lower-case u | `U_i`, `u_i` and marked alternatives | 045; drawing labels checked separately from the top diagrams. |
| Roman section labels | I, II, III | 045 drawings; retained as written. |
| Short heading on faint sheet | `\unsure{\Phi D|\Phi B}` | 046; one contour after Φ favours D, but remains uncertain. |
| Dimensions below objects | `\underset{n_i-r}{…}` | 047; `n_{j|i}-2` retained where the source appears to switch index. |
| Ordinary arrow / headless stroke | TikZ-CD `\arrow`, `dash`, `no head` | Throughout; headless strokes on 030 and 043 remain headless. |
| Hook at source / curl at terminal end | TikZ-CD `hook`; `-{Hooks[harpoon]}` | 044–047. Both endpoints checked; terminal curls have been reproduced at the terminal end. |
| Product-square crosses | phantom `\times` | 047; each visible cross retained in its diagram cell. |
| Flat bracket / pointed brace | `\underbracket`, `\underbrace` | 041, 047; the flat and pointed shapes were compared and are represented separately. |
| Missing terminal circle | no added `^\circ` | 047 lower grid, last objects of rows3–4; absence retained despite circles in other rows. |

