# MPL 133 — notation and doubts

## Notation table checked before the freeze

The root transcriber compared recurring forms across all 50 pages during the sequential first reading and the separate visual audit. Differences that the ink did not decide remain marked; mathematical expectations did not decide them. The typed articles keep their own typographic conventions.

| Manuscript sign / usage | LaTeX transcription | Visual control |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes: ` ``...'' ` | Guillemets used only where their angular strokes are visible. |
| Single underline | `\uline{...}` | Kept distinct from crossings-out. |
| Double underline | `\uuline{...}` | Two strokes must be visible. |
| Uncertain word, letter, sign or ending | `\unsure{...}` | No reading supplied by mathematical expectations. |
| Struck-through ink | `\deleted{...}` | Includes recoverable mathematical symbols. |
| Number on manuscript sheet | `\mspage{...}` | Distinguished from scan number. |
| Complex-index low dot | `L_\bullet` | Scan 003: low dots distinguished from primes. |
| Grothendieck/Witt group symbol | `WG(S)` | Scan 006: two Roman capital letters, no exponent. |
| Underlined structure-ring symbol | `\uline{O}_S` | Scan 006: underbar is visible. |
| Exterior-power operation | `\lambda^i` | Scan 006: lambda distinguished from the plain x variable. |
| Classifying topos | `B_{O(m)}` | Scan 006: group written beneath B. |
| Dual module, small downward accent above E | `\check E` | Scan 007: accent is above the letter, not a prime. |
| Hyperbolic map arrow label / class formula | `\alpha` / `\varphi` | Scan 007: distinct visual forms retained; see doubt register. |
| Looped symmetric-group letter on scans 018–020 | `\mathfrak S_n` | The looped central bar and upper return stroke are retained as Gothic S; the earliest occurrence on 018 remains explicitly doubtful after audit. |
| Finite-set ring and class | `k_0(G)`, `k_n(G)`, `k_*(G)`, `\operatorname{cl}_n` | Lowercase looped k; class symbol is the connected c-l pair. |
| Total power operation | `\tau^*(E)` | Asterisk is distinct from the degree n and from a prime. |
| Contracted product | `\mathbin{\wedge}_{H}` | Wedge-shaped sign, not silently changed to a product sign. |
| Hom versus Mon | `\operatorname{Hom}`, `\operatorname{Mon}` | Scan 022 has a clear contrast between H-o-m and M-o-n. Audit resolves seven Mon occurrences on 021; the overwritten 020 form retains Mon/Hom doubt. |
| Capital and lowercase total operations | `T^*`, `\tau^*` | Flat capital T is distinct from curved lowercase tau. |
| Category of finite sets and injections | `\mathcal E` | Rounded script E; ordinary E remains the set variable. |
| Functor category | `\uline{\operatorname{Hom}}` | The underline belongs to the source, not to an added semantic convention. |
| Opposite category superscript | `^o` | Small raised round o as written; not expanded to op. |
| Outlined capital Omega | small double-contour TikZ glyph | Double-contour capital Omega in the blue pages; kept distinct from plain omega. |
| Arrowless horizontal connector | `\mathbin{\text{---}}` | Used only where a drawn line has no secure arrowhead. |
| K-theory class variable | `\xi` | Faint blue xi sometimes has only a single long descender; distinct from rho_i. |
| Coefficient polynomials | `\Sigma_{\alpha_1,\ldots,\alpha_n}` | Capital Sigma with subscript names a polynomial; the summation sign to its left is separate. |
| Universal unit in representation component | `\rho_i` | Long descending loop before subscript i. |
| Literal shorthand for même/mêmes | `$=$`, `$=^{s}$` within doubt macros | Scans 026, 033 and 044: two horizontal strokes are not expanded silently. Written Même on 036 and même on 043 were rechecked separately and remain words. |
| Go-board side variable | `\unsure{v\|\nu}` | Scans 030–031: every recurrence, including its square, retains the same unresolved reading. |
| Go count variables | `P,Q,T,N,D`; `p,q,t,n,d` and primes | Scans 030–034: changes of case and primes are preserved. |
| Centre and derived-group names | `Z(G)`, `\operatorname{Cent}`, `DG`, `\operatorname{Der}`, `\operatorname{D\acute{e}r}` | Scans 036–054: spelling and accent variations remain as written; accent-safe encoding changes no reading. |
| Central-intersection letter | `\mathfrak z` | Scans 039–044; uncertain instances remain marked. |
| Crossed-module maps and actions | `d`, `d'`, `D_1`, `D_2`, `\theta`, `\Theta` | Scans 036–047: case, primes and indices compared across diagrams; overwritten initial formulas on 046 remain doubtful. |
| Kernel and action variables | `\zeta`, `\zeta_0`, `\zeta_G`, `\varphi_G`, `\psi_G` | Scans 047–052: repeated Greek forms compared, including barred psi and the doubtful G index on 051. |
| Commutator quotient | `\eta`, `\eta_0` | Scans 052–054: compressed 052 subscript remains doubtful; 053 explicitly shows `(N_{\mathrm{comm}})_M`. |
| Stars and their position | `\pi_0^*`, `\pi_{1*}` | Scans 049–054: cancelled upper stars and inserted lower stars on 054 are both retained. |
| Exclamation-like, prime-like and looped exponents | Literal signs or doubt alternatives | The ambiguous exponent on 023 remains a loop/exclamation alternative; prime/index doubts on 038–039 remain. No global normalization from theory. |
| Headless diagram connectors | `dash` | Directions are not supplied where no secure arrowhead is visible. |
| Headless hooks | `dash,hook` / `dash,hook'` | Scans 037 and 046: option order preserves the hook without adding a terminal arrowhead. |
| Single and double-headed arrows | `\longrightarrow`, `\twoheadrightarrow`, tikz-cd arrows | In particular the first double head on 054 remains although the following condition asks for surjectivity. |
| Underlining versus descenders | `\uline`, `\uuline` only for independent strokes | False underlines removed on 006, 007, 008 and 044 after close inspection. |

All tikz-cd matrices use `ampersand replacement=\&` so that editorial macros can capture diagrams without changing alignment tokenization. The outlined Omega on scan027 is drawn with TikZ because the available AMS blackboard font maps that input to another glyph. These are encoding conventions, not new readings.


## Doubt register

Locations use the approximate line in the page fragment; retained line breaks follow the handwriting where practicable. An entire marked phrase means its uncertain letters or endings could not be separated securely. The first alternative is the visual reading, without grammatical correction.

| Cote | Scan | Approx. fragment line | Reading | Alternative / qualification | Confidence |
|---|---:|---:|---|---|---|
| 133 | 002 | 3 | `groupes` | Uncertain ink; no secure alternative | medium |
| 133 | 002 | 5 | `quadratiques` | Uncertain ink; no secure alternative | medium |
| 133 | 002 | 7 | `1` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 3 | `=` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 3 | `q'''` | q'''' | medium |
| 133 | 003 | 4 | `\circ` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 4 | `\circ 1` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 20 | `C\times C\to C` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 21 | `C\times C\times` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 22 | `x` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 26 | `L'_\bullet` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 26 | `L''` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 31 | `p\otimes L_\bullet` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 34 | `\alpha` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | 40 | `1` | 2 | medium |
| 133 | 003 | 44 | `((x\otimes y)\otimes z)\otimes t` | Uncertain ink; no secure alternative | medium |
| 133 | 003 | top | q primes | Number of prime strokes and adjacent small composition/arrow strokes are insecure | low |
| 133 | 003 | first diagram | L_\bullet | Low dot is used consistently for the complex index; no prime is silently substituted | medium |
| 133 | 003 | last diagram, lower edge | right arrow | Very small terminal stroke; an arrow is the best visual reading | medium |
| 133 | 004 | 7 | `x,x'` | Uncertain ink; no secure alternative | medium |
| 133 | 004 | 7 | `xx'` | Uncertain ink; no secure alternative | medium |
| 133 | 004 | 17 | `\equiv` | = | medium |
| 133 | 004 | 23 | `\xi_i` | \zeta_i | medium |
| 133 | 004 | 27 | `\Vert` | = | medium |
| 133 | 004 | 33 | `B` | Uncertain ink; no secure alternative | medium |
| 133 | 004 | 34 | `q` | Uncertain ink; no secure alternative | medium |
| 133 | 004 | 51 | `beurre, bananes` | Uncertain ink; no secure alternative | medium |
| 133 | 004 | 53 | `J. et D.` | Uncertain ink; no secure alternative | medium |
| 133 | 004 | Q display | cancelled xx prime | Dense overwriting prevents secure recovery of the cancelled term | low |
| 133 | 004 | expense table | J. et D. | The initials and the small linking word are uncertain | low |
| 133 | 006 | 25 | `\lambda^2x` | Uncertain ink; no secure alternative | medium |
| 133 | 006 | 25 | `i-1` | i | medium |
| 133 | 006 | 26 | `\lambda^2y` | Uncertain ink; no secure alternative | medium |
| 133 | 006 | 26 | `i-1` | i | medium |
| 133 | 006 | 38 | `fib` | Uncertain ink; no secure alternative | medium |
| 133 | 006 | 41 | `De =` | Uncertain ink; no secure alternative | medium |
| 133 | 006 | 41 | `donc` | Uncertain ink; no secure alternative | medium |
| 133 | 006 | 41 | `vérifier` | Uncertain ink; no secure alternative | medium |
| 133 | 006 | 16 | `\illegible{1}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 006 | product formula | i>=2 | Closing parenthesis is beyond/right at the cropped edge; not supplied | medium |
| 133 | 006 | final paragraph | De = | Literal shorthand is retained; possibly De même | low |
| 133 | 006 | P_i formula | i-1 / i | Small stroke after i on both terminal lambda powers; ink does not warrant choosing the expected polynomial convention | low |
| 133 | 007 | 7 | `fib` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 8 | `q(a,a')=\langle a,a'\rangle` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 15 | `donc` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 24 | `Module` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 25 | `cet` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 25 | `élément` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 30 | `les` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | 35 | `De =` | Uncertain ink; no secure alternative | medium |
| 133 | 007 | q formula | a versus x | Small argument letters are not secure; entire formula marked | medium |
| 133 | 007 | first/second display versus parenthesis | alpha / varphi | Arrow label looks alpha; formula on E is varphi. Kept distinct rather than harmonized | medium |
| 133 | 008 | 2 | `Laborde` | Lazard | medium |
| 133 | 008 | 6 | `tout` | Uncertain ink; no secure alternative | medium |
| 133 | 008 | 22 | `isom.` | Uncertain ink; no secure alternative | medium |
| 133 | 008 | cancelled criterion | alpha(E)=E plus dual | The alpha(E) annotation is below the cancelled line and not itself clearly struck; retained as insertion | medium |
| 133 | 009 | 3 | `\uline{strict\textsuperscript{mt}}` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 4 | `faisceau dans` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 5 | `On supp.` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 14 | `w(M,q)` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 19 | `x` | m | medium |
| 133 | 009 | 22 | `par splitting` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 22 | `on se ramène à` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 22 | `prouver` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 30 | `que` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 33 | `i` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 38 | `H` | Uncertain ink; no secure alternative | medium |
| 133 | 009 | 30 | `\illegible{3}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 009 | upper-right insertion | p.ex. anneau faisceau dans top. ét | Overlaps earlier line; middle words are low-confidence | low |
| 133 | 009 | cancelled diagonal margin | par splitting ... | Every insecure part is marked; rotation and enlargement did not fully separate cancellation strokes | low |
| 133 | 009 | cancelled NB | 3 unreadable words | Dense zigzag deletion physically obscures the middle of the line | low |
| 133 | 011 | 31 | `s/` | Uncertain ink; no secure alternative | medium |
| 133 | 011 | 34 | `s/` | Uncertain ink; no secure alternative | medium |
| 133 | 011 | 45 | `i` | I | medium |
| 133 | 011 | lemma direct sum | N_j | Printed N_j is retained although the family was introduced as M_i | high |
| 133 | 011 | title/abstract | Skolem-Nother | Printed spelling Nother, without the e of Noether, is retained | high |
| 133 | 012 | 25 | `\mathrm A\,s` | \mathrm A_s | medium |
| 133 | 012 | 31 | `\mathrm A\,s` | \mathrm A_s | medium |
| 133 | 012 | 32 | `\mathrm A\,s` | \mathrm A_s | medium |
| 133 | 012 | 33 | `\mathrm A\,s` | \mathrm A_s | medium |
| 133 | 012 | 33 | `y_1` | y1 | medium |
| 133 | 012 | 34 | `\mathrm A\,s` | \mathrm A_s | medium |
| 133 | 012 | 34 | `\mathrm A\,s` | \mathrm A_s | medium |
| 133 | 012 | proof proposition 4 | minimaux | Printed minimaux retained, although the next sentence uses maximal | high |
| 133 | 012 | proof theorem 1 | B_i V_i | The second index reads i in print; not changed to j | high |
| 133 | 012 | proof proposition 5 | minimals | Printed minimals retained | high |
| 133 | 013 | first diagram | B tensor A | No star is printed on this A; not supplied from the adjacent target | high |
| 133 | 013 | centralizer display | 1 tensor Z(Astar) | Printed 1 rather than A retained | high |
| 133 | 014 | introduction | définit | Printed définit retained | high |
| 133 | 014 | introduction | toute forme quadratiques | Printed agreement retained | high |
| 133 | 014 | section 2 | corps de nombre | Singular nombre retained | high |
| 133 | 014 | item ii | définissant | Printed participle retained | high |
| 133 | 015 | 34 | `\bigoplus` | \bigotimes | medium |
| 133 | 015 | proof product | product LW(K) | Printed K has no v in this product; retained | high |
| 133 | 015 | description N(K) | exponent | Printed exponent retained without changing to exposant | high |
| 133 | 016 | proof lemma2 | le rang pair | Printed le rang pair retained | high |
| 133 | 018 | 3 | `\mathcal A` | \mathcal C | medium |
| 133 | 018 | 3 | `\mathcal A` | \mathcal C | medium |
| 133 | 018 | 3 | `\mathfrak S_n` | \mathcal G_n | medium |
| 133 | 018 | 10 | `\texttt{PORT))}` | Uncertain ink; no secure alternative | medium |
| 133 | 018 | 14 | `\texttt{ASS),}` | Uncertain ink; no secure alternative | medium |
| 133 | 018 | 20 | `\texttt{P'}` | Uncertain ink; no secure alternative | medium |
| 133 | 018 | 28 | `\texttt{SYSDA,}` | Uncertain ink; no secure alternative | medium |
| 133 | 018 | 31 | `\texttt{00040070}` | Uncertain ink; no secure alternative | medium |
| 133 | 018 | 32 | `\texttt{IS A}` | Uncertain ink; no secure alternative | medium |
| 133 | 018 | 6 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 7 | `\illegible{5}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 8 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 9 | `\illegible{5}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 10 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 11 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 12 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 13 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 14 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 15 | `\illegible{5}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 16 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 17 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 18 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 19 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 20 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 21 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 22 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 23 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 24 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 25 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 26 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 27 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 28 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 29 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 30 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 31 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 32 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 33 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 34 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | 35 | `\illegible{6}` | Estimated word count; ink not resolved after enlargement | low |
| 133 | 018 | top | A / C; fraktur S / script G | The category letter is rounded; the last letter has a looped central bar. Kept doubtful without resolving from the formula’s possible meaning. | low |
| 133 | 018 | lower half | machine print visible through paper | Mirrored/rotated inspection resolves the numeric column and a few edge fragments. Very faint overlapping text remains physically unresolved; word counts are rough estimates. The array runs in scanned top-to-bottom order, with readable character orientation restored. | low |
| 133 | 019 | 4 | `\mathcal P_i` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 9 | `\lambda_t` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 9 | `\lambda_{1-t}(E)` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 10 | `t` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 13 | `Q_i` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 13 | `E` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 13 | `j` | i | medium |
| 133 | 019 | 20 | `-` | + | medium |
| 133 | 019 | 26 | `\mathbf Z` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 26 | `\mathbf Q` | \mathbf C | medium |
| 133 | 019 | 31 | `+` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 37 | `t^2` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | 58 | `\mathcal P` | Uncertain ink; no secure alternative | medium |
| 133 | 019 | upper definitions; bottom right | P_i and P_(alpha,beta) | Flag-shaped letter transcribed as script P; alphabet identification is provisional. | medium |
| 133 | 019 | formal series | trailing long strokes | Long continuation strokes are preserved as dashes, without inventing omitted series terms. | high |
| 133 | 020 | 6 | `Suranneau` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 8 | `(K_0)` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 13 | `(K_0)` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 13 | `\prod` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 13 | `(K_0)` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 30 | `finis` | fini | medium |
| 133 | 020 | 32 | `nt` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 33 | `\operatorname{Mon}` | \operatorname{Hom} | medium |
| 133 | 020 | 33 | `(K_0)` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 37 | `t` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 37 | `=` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 37 | `\in` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | 37 | `\in` | Uncertain ink; no secure alternative | medium |
| 133 | 020 | NB | tau^1(E)=cl_0(E) | The subscript after cl is visibly 0; it is retained even though the preceding definition uses cl_n. | high |
| 133 | 020 | definition of tau^n | Mon  /  Hom | First letter is overwritten with tall M-like strokes and an H-like crossbar; Mon placed first from the visible strokes, independently of the later mathematics. | medium |
| 133 | 021 | 2 | `E\amalg F` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 5 | `F` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 6 | `\prod` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 6 | `J` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 6 | `J` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 6 | `J` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 11 | `J` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 11 | `J` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 11 | `J` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 15 | `*` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 22 | `ss-groupe` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 30 | `hom` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | 30 | `p` | Uncertain ink; no secure alternative | medium |
| 133 | 021 | top line right edge | F | End of formula reaches the edge; the terminal argument is partially clipped. | low |
| 133 | 021 | top unions | J | Thick overwritten capital has a box-like loop; J retained with doubt rather than inferred from the index. | medium |
| 133 | 021 | upper three displays | Mon (seven occurrences) | Second visual pass resolves the clear M strokes here; scan020 remains uncertain because its corresponding letter is overwritten. | high |
| 133 | 022 | 6 | `E\in k(G)` | Uncertain ink; no secure alternative | medium |
| 133 | 022 | 27 | `1\leq i\leq n` | Uncertain ink; no secure alternative | medium |
| 133 | 022 | 27 | `n,i` | \alpha,i | medium |
| 133 | 022 | 45 | `*i` | Uncertain ink; no secure alternative | medium |
| 133 | 022 | line below T* definition | on donc encore | A small joining stroke after on may belong to a compressed a; the visible wording is retained without supplying one. | low |
| 133 | 022 | top right edge | E in k(G) | Marginal notation partly clipped. | low |
| 133 | 022 | decomposition subscript | cancelled index | Dense cancellation; best symbolic reading supplied, not a word-count illegibility macro. | low |
| 133 | 023 | 2 | `on` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 4 | `\ell` | ! | medium |
| 133 | 023 | 7 | `\ell` | ! | medium |
| 133 | 023 | 13 | `\text{en}` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 22 | `\alpha_i` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 22 | `\alpha_n` | \alpha_i | medium |
| 133 | 023 | 33 | `\alpha_1,\alpha_2,\ldots,\alpha_n` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 33 | `\nu(\alpha)` | \mu(\alpha) | medium |
| 133 | 023 | 33 | `\mu(\alpha)` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 34 | `\tau` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 37 | `\tau` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 40 | `\mathfrak I` | J | medium |
| 133 | 023 | 41 | `\tau^1(e_i)-e_i` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 43 | `\tau^1(e_i)` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | 44 | `3` | Uncertain ink; no secure alternative | medium |
| 133 | 023 | top phi superscripts | ell / exclamation | The small dark superscript has a loop or hooked return; no confident identification as prime or exclamation is made. Compare recurring forms before freeze. | low |
| 133 | 023 | bottom cancellations | tau^1(e_i)-e_i and ideal symbol | Dense overwriting makes the full relation and the ideal letter uncertain. | low |
| 133 | 025 | 8 | `sommandes` | sommants | medium |
| 133 | 025 | 16 | `donne` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 3 | `spécial par.` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 12 | `$=^{s}$` | mêmes | medium |
| 133 | 026 | 22 | `à g.` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 28 | `\sigma` | \alpha | medium |
| 133 | 026 | 29 | `F` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 29 | `appl.` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 30 | `inj.` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 30 | `on a` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 30 | `F(E)\simeq G(E)` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | 36 | `morphismes` | Uncertain ink; no secure alternative | medium |
| 133 | 026 | blue note | distingué; isom.; à g. | Blue note is faint and the final parenthesis meets the black insertion. First two phrases clear after enlargement; final abbreviation remains doubtful. | medium |
| 133 | 026 | cancelled condition | inj. E to F on a F(E) isomorphic G(E) | Several layers of crossing obscure the abandoned quantifier and formula; this reconstruction is only a low-confidence ink reading. | low |
| 133 | 026 | permanence paragraph | = with small s  /  mêmes | Ink consists of two horizontal strokes and a small final loop; first-pass expansion removed. Exact shorthand form remains uncertain. | medium |
| 133 | 027 | 11 | `formée` | Uncertain ink; no secure alternative | medium |
| 133 | 027 | 31 | `+` | \amalg | medium |
| 133 | 028 | 4 | `\sum` | \bigoplus | medium |
| 133 | 028 | 10 | `=` | \in | medium |
| 133 | 028 | 21 | `sommant` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 21 | `direct` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 24 | `à la` | de la | medium |
| 133 | 028 | 24 | `\xi` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 30 | `*` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 34 | `\Sigma_{\alpha_1,\ldots,\alpha_n}` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 43 | `\alpha_1+\cdots+\alpha_{n-1}+1` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 43 | `x_{\alpha_1+\cdots+\alpha_n}` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 43 | `)` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 43 | `n` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 44 | `\nu_1` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | 44 | `\nu_n` | Uncertain ink; no secure alternative | medium |
| 133 | 028 | diagonal margin | sommant direct; de la H. Weyl | Very faint diagonal ink inspected at two rotations. The phrase and connecting words remain uncertain, although H. Weyl and the question marks are visible. | low |
| 133 | 028 | bottom display right edge | final group of variables and exponent | Final factor extends beyond the available right edge; marked subscript, closing parenthesis and exponent are tentative. | low |
| 133 | 028 | bottom line | élémentaires S_1,S_2,...,S_n en | Line touches the bottom edge and continues; no completion supplied. | medium |
| 133 | 029 | 7 | `sans doute` | Uncertain ink; no secure alternative | medium |
| 133 | 029 | 13 | `engendré` | Uncertain ink; no secure alternative | medium |
| 133 | 030 | 2 | `v` | \nu | medium |
| 133 | 030 | 2 | `v` | \nu | medium |
| 133 | 030 | 11 | `et` | Uncertain ink; no secure alternative | medium |
| 133 | 030 | 22 | `v` | \nu | medium |
| 133 | 030 | 26 | `N` | Uncertain ink; no secure alternative | medium |
| 133 | 030 | 27 | `N'` | Uncertain ink; no secure alternative | medium |
| 133 | 030 | 34 | `-` | + | medium |
| 133 | 030 | 38 | `v` | \nu | medium |
| 133 | 030 | 38 | `-` | + | medium |
| 133 | 030 | 39 | `v` | \nu | medium |
| 133 | 030 | 45 | `v` | \nu | medium |
| 133 | 030 | 45 | `-` | + | medium |
| 133 | 030 | 48 | `v` | \nu | medium |
| 133 | 030 | board size | v / nu | The board-side variable is a rounded v/nu; every repetition and square now carries the same unresolved reading. | medium |
| 133 | 030 | subtractions before epsilon | minus / plus | Several operators are thick overwritten patches; minus is the first visible reading but not asserted from the scoring calculation. | low |
| 133 | 031 | 4 | `indélogeables` | Uncertain ink; no secure alternative | medium |
| 133 | 031 | 8 | `n` | Uncertain ink; no secure alternative | medium |
| 133 | 031 | 15 | `avec pris enlevé` | Uncertain ink; no secure alternative | medium |
| 133 | 031 | 18 | `v` | \nu | medium |
| 133 | 031 | 21 | `Q` | Uncertain ink; no secure alternative | medium |
| 133 | 031 | 26 | `,` | Uncertain ink; no secure alternative | medium |
| 133 | 031 | 29 | `v` | \nu | medium |
| 133 | 031 | 29 | `v` | \nu | medium |
| 133 | 031 | 32 | `-` | + | medium |
| 133 | 031 | territory definition | avec pris enlevé | The three words before les pris. bl. are not resolved securely after enlargement; do not use this phrase to infer scoring conventions. | low |
| 133 | 031 | definition of p | qui ne sont prisonniers virtuels | No separate pas is visible; none is supplied. | high |
| 133 | 031 | d display | opening parenthesis and comma | Source punctuation is unbalanced and a small stroke follows t-prime; retained, not normalized. | medium |
| 133 | 032 | 11 | `case` | Uncertain ink; no secure alternative | medium |
| 133 | 032 | 18 | `Commençant à` | Uncertain ink; no secure alternative | medium |
| 133 | 032 | 20 | `à tour de` | Uncertain ink; no secure alternative | medium |
| 133 | 032 | 27 | `n'en` | n'y | medium |
| 133 | 032 | 30 | `intérieures` | Uncertain ink; no secure alternative | medium |
| 133 | 032 | 30 | `i_1,i_2` | Uncertain ink; no secure alternative | medium |
| 133 | 032 | 31 | `ces deux libertés` | Uncertain ink; no secure alternative | medium |
| 133 | 032 | bottom edge | en i_1,i_2 | The insertion is at the lower-right edge; the punctuation and indices are not securely separated. | low |
| 133 | 033 | 4 | `i.e.` | Uncertain ink; no secure alternative | medium |
| 133 | 033 | 7 | `autre` | Uncertain ink; no secure alternative | medium |
| 133 | 033 | 10 | `]` | Uncertain ink; no secure alternative | medium |
| 133 | 033 | 10 | `$=$` | même | medium |
| 133 | 033 | 19 | `inté` | Uncertain ink; no secure alternative | medium |
| 133 | 033 | 19 | `au $=$` | au même | medium |
| 133 | 033 | upper-right edge | i.e. entourées | Insertion runs to the edge; the abbreviation is compressed. | medium |
| 133 | 033 | lower-middle insertion | au = / au même | Two short interlinear groups are partly struck; literal shorthand retained before its possible expansion. | low |
| 133 | 034 | 5 | `\gamma_i` | y_i | medium |
| 133 | 034 | 7 | `\gamma'_j` | y'_j | medium |
| 133 | 034 | 11 | `T'` | t' | medium |
| 133 | 036 | 4 | `ou unipotent` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 6 | `ou unipotent` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 7 | `extension` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 9 | `sous-groupe` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 15 | `formuler` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 15 | `plus` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 25 | `que la repr. lin. soit` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 25 | `unipotente` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 27 | `\delta` | d | medium |
| 133 | 036 | 29 | `résulte aussitôt du` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 29 | `fait que` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 29 | `(G/R)_{\mathrm{ab}}` | G/R | medium |
| 133 | 036 | 29 | `\simeq` | \to | medium |
| 133 | 036 | 29 | `est linéaire` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 29 | `Mais` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 29 | `Centre` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 32 | `triviale` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 34 | `quasi-unipotent` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 35 | `G` | Z(G) | medium |
| 133 | 036 | 35 | `\times` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 37 | `ainsi` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 37 | `\operatorname{Cent}G` | Z(G) | medium |
| 133 | 036 | 37 | `trouve` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 37 | `dans $Z(G)$` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 39 | `T'` | T | medium |
| 133 | 036 | 39 | `\phantom{T}'` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 44 | `produit` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 44 | `linéaire` | fibré | medium |
| 133 | 036 | 46 | `un` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 47 | `contenu` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 47 | `dans la th. de cls` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 70 | `D_{1\,D_0}` | (D_1)_{D_0} | medium |
| 133 | 036 | 74 | `se reconstruit` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 81 | `étale` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 88 | `fibres` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 88 | `groupes` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 88 | `images inverses` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 92 | `détermination` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 92 | `\ldots` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 93 | `(\ker\delta)^{D_0}` | (\ker\delta) | medium |
| 133 | 036 | 94 | `(\ker\delta)_{D_0}` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 96 | `NB` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | 98 | `DG div. comm. et algébrisable` | Uncertain ink; no secure alternative | medium |
| 133 | 036 | whole page | Grey and blue ink on ruled music paper | Several grey additions overlap staff lines; two visual contrast enlargements were used. Uncertain whole phrases are marked rather than silently reconstructed. | low |
| 133 | 036 | central bracket | p-divisible part and T notation | The primes and interlinear note are faint and overwritten; no structural conclusion has been used to complete them. | low |
| 133 | 036 | bottom-right | ker delta formulas | Arrows and overwritten strokes obstruct both the operation and indices. | low |
| 133 | 036 | isogeny corollary | linéaire  /  fibré | Tall initial stroke and ending resemble the other linéaire on the sheet, but pencil and staff lines do not resolve the whole word. | low |
| 133 | 036 | left margin | Mais | Small underlined word before the centre statement, not represented in first pass. | medium |
| 133 | 037 | 26 | `aussi` | Uncertain ink; no secure alternative | medium |
| 133 | 037 | 38 | `(\operatorname{Cent}G)` | Uncertain ink; no secure alternative | medium |
| 133 | 037 | 41 | `à savoir` | Uncertain ink; no secure alternative | medium |
| 133 | 037 | 48 | `donc` | Uncertain ink; no secure alternative | medium |
| 133 | 037 | lower-right edge | D0 isomorphic G / (Cent G) | The denominator continues into the cropped right edge. | low |
| 133 | 037 | bottom diagram | hooked connections | The visible hooks are preserved without adding full arrowheads to the source connections. | medium |
| 133 | 038 | 6 | `\varphi` | Uncertain ink; no secure alternative | medium |
| 133 | 038 | 8 | `G` | Uncertain ink; no secure alternative | medium |
| 133 | 038 | 8 | `1` | \prime | medium |
| 133 | 038 | 10 | `\operatorname{Cent}` | Uncertain ink; no secure alternative | medium |
| 133 | 038 | 14 | `\text{liné}` | Uncertain ink; no secure alternative | medium |
| 133 | 038 | 14 | `a-tori` | Uncertain ink; no secure alternative | medium |
| 133 | 038 | 19 | `voire` | quasi | medium |
| 133 | 038 | 21 | `\neq` | = | medium |
| 133 | 038 | 21 | `\operatorname{Div}` | Uncertain ink; no secure alternative | medium |
| 133 | 038 | lower circled formula | oval enclosure | The oval source enclosure is represented by a box inside the diagram; the content and question mark are retained. | high |
| 133 | 039 | 3 | `G` | g | medium |
| 133 | 039 | 3 | `Z` | Uncertain ink; no secure alternative | medium |
| 133 | 039 | 3 | `G` | Uncertain ink; no secure alternative | medium |
| 133 | 039 | 7 | `\mathfrak z` | Uncertain ink; no secure alternative | medium |
| 133 | 039 | 7 | `\mathcal G` | G | medium |
| 133 | 039 | 21 | `3` | \mathfrak z | medium |
| 133 | 039 | 24 | `groupe formel` | Uncertain ink; no secure alternative | medium |
| 133 | 039 | 24 | `commutatif` | Uncertain ink; no secure alternative | medium |
| 133 | 039 | 25 | `com.` | Uncertain ink; no secure alternative | medium |
| 133 | 039 | top edge | three clipped ink fragments | Only lower parts of characters survive the crop. G/g, Z, G are tentative glyph readings, not supplied text. | low |
| 133 | 039 | lower diagram | outlined D and H | Heavily retraced capitals represented by blackboard bold, without interpreting this as a new mathematical species. | medium |
| 133 | 040 | 15 | `\varphi` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 15 | `\varphi(y,x)` | \varphi(x,y) | medium |
| 133 | 040 | 15 | `\varphi_{x,y}` | \varphi xy | medium |
| 133 | 040 | 20 | `\simeq` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 23 | `H_a` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 26 | `\widehat G` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 26 | `G'` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 27 | `\mathfrak z` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 33 | `\simeq` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 33 | `\simeq` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 39 | `?` | Uncertain ink; no secure alternative | low |
| 133 | 040 | 40 | `\pi_0` | \pi_1 | medium |
| 133 | 040 | 40 | `?` | Uncertain ink; no secure alternative | low |
| 133 | 040 | 40 | `\sim` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 52 | `\simeq` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 52 | `\simeq` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 57 | `\Phi` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | 59 | `\varphi` | Uncertain ink; no secure alternative | medium |
| 133 | 040 | central and lower diagrams | plain versus headed arrows | Only visible heads were added; uncertain equivalences and indices are marked. | medium |
| 133 | 040 | whole page | capital Psi and Phi | The large forks/loops are distinguished visually from the thinner phi. | medium |
| 133 | 042 | 5 | `H` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 5 | `\mathrm{ab}` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 10 | `A` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 11 | `caractéristiques` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 28 | `(avec sa décomposition` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 39 | `*` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 43 | `de` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | 54 | `par suite` | Uncertain ink; no secure alternative | medium |
| 133 | 042 | first sequence | A superscript ab | Small superscript is heavily retraced; retained as uncertain rather than removed. | medium |
| 133 | 042 | middle substitution | with its decomposition | Cancelled phrase is only partially separable from the replacement; exact wording uncertain. | low |
| 133 | 043 | 3 | `$\varphi$` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 5 | `y` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 8 | `On` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 16 | `\mathfrak z_u\longrightarrow` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 20 | `m` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 22 | `\varphi` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 26 | `sous espace` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 26 | `\Lambda` | A | medium |
| 133 | 043 | 26 | `un` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 28 | `de pt de tors` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 30 | `si` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | 32 | `(et on` | et on | medium |
| 133 | 043 | 33 | `Donc on doit avoir` | Uncertain ink; no secure alternative | medium |
| 133 | 043 | bottom | tau | Small curved letter transcribed tau; it is repeated consistently on this sheet. | medium |
| 133 | 043 | positive-characteristic paragraph | (et on  /  et on | Initial tall curve may be an opening parenthesis; faint on had been mistaken for a dash. | medium |
| 133 | 044 | 3 | `ceux` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 5 | `$=$` | même | medium |
| 133 | 044 | 8 | `qui est nécessaire` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 10 | `par` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 14 | `cette` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 14 | `élémentaire` | est triviale | medium |
| 133 | 044 | 16 | `pour inégales caractéristiques` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 16 | `cat` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 20 | `y` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 20 | `y` | \eta | medium |
| 133 | 044 | 21 | `pts` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | 22 | `$=$` | même | medium |
| 133 | 044 | 26 | `a` | Uncertain ink; no secure alternative | medium |
| 133 | 044 | middle paragraph | groupe affine lisse | Affine is visibly written in the parenthesis; retained even though the surrounding example may create a mathematical tension. | high |
| 133 | 044 | upper NB, line 4; middle NB, penultimate line | = | Two horizontal strokes: shorthand retained literally rather than expanded même. | medium |
| 133 | 044 | middle, above NB | pour inégales caractéristiques | Insertion is compressed and overlaps the marginal note; prior reading isogénies rejected as too confident. | low |
| 133 | 044 | left margin at middle NB | cette note élémentaire sur ce point | Whole phrase weak; possible est triviale. Neither reading is secure. | low |
| 133 | 046 | 6 | `\theta:M\longrightarrow\operatorname{Aut}_{\mathrm{gr}}(N)` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 8 | `\beta:C'\longrightarrow C` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 10 | `1` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 13 | `1` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 14 | `1` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 28 | `z` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 61 | `A` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 87 | `Edgar` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | 88 | `vier` | fünf | medium |
| 133 | 046 | 89 | `H(\beta)` | Uncertain ink; no secure alternative | medium |
| 133 | 046 | top cancellations | theta:M to Aut(N); beta:C prime to C | Heavy crossing overwrites most letter bodies; formulas are tentative ink readings | low |
| 133 | 046 | tuple diamond | z below arrow | The small mark beneath the arrow may be a comma or z; no quotient inserted | low |
| 133 | 046 | right margin, cancelled German, last line | vier | fünf; letters overstruck and partly lost under the cancellation stroke. | low |
| 133 | 047 | 6 | `a` | * | medium |
| 133 | 047 | 15 | `son` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 15 | `déf.` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 20 | `N'` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 26 | `\operatorname{Hom}_{\mathrm{gr}}(M,\pi_1)` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 32 | `Z^1` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 37 | `\operatorname{Hom}_{\mathrm{gr}}` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 50 | `E` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 53 | `donc plus` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | 59 | `\zeta'` | Uncertain ink; no secure alternative | medium |
| 133 | 047 | interlinear image inverse | le ss-groupe invariant de G déf. | Final two or three strokes overwritten; relation to l’image inverse is uncertain | low |
| 133 | 047 | left margin heading | donc plus | Oblique and abbreviated; possible autre reading | low |
| 133 | 048 | 42 | `E. Siau` | Uncertain ink; no secure alternative | medium |
| 133 | 048 | analysis paragraph | parantes; cetacés; phyllogenèse | Unusual spellings appear in the typed original and are retained | high |
| 133 | 048 | signature | E. Siau | Cursive signature is tentative; typed name below is clear | medium |
| 133 | 049 | 18 | `\beta` | Uncertain ink; no secure alternative | medium |
| 133 | 049 | 22 | `choix` | Uncertain ink; no secure alternative | medium |
| 133 | 049 | 34 | `\beta` | Uncertain ink; no secure alternative | medium |
| 133 | 049 | 39 | `ici` | Uncertain ink; no secure alternative | medium |
| 133 | 049 | 46 | `Que faire` | Uncertain ink; no secure alternative | medium |
| 133 | 049 | left margin | Que faire sinon? | First two words in the margin uncertain; pi_0 commutatif?! is clearly a qualification | medium |
| 133 | 049 | sign parenthesis | choix de la droite ou la gauche | The small article before droite is faint; source phrasing retained | medium |
| 133 | 050 | 42 | `E. Siau` | Uncertain ink; no secure alternative | medium |
| 133 | 050 | address label | MR LE PROFESSEUR GROTHENDIECK A. | Label is upside down in source; transcribed in reading orientation | high |
| 133 | 050 | signature | E. Siau | Cursive signature tentative; typed name clear | medium |
| 133 | 051 | 22 | `\pi_0` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | 26 | `\zeta_0` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | 29 | `K` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | 38 | `\operatorname{Im}` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | 40 | `\operatorname{Cent}M` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | 44 | `G` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | 55 | `pour` | Uncertain ink; no secure alternative | medium |
| 133 | 051 | lower bracket cancellation | peut se faire ... injective | The bracket marked annulé! does not make its exact scope wholly certain; adjoining explanatory words remain transcribed | medium |
| 133 | 051 | rightmost formula | Cent M | Right edge clips part of last letters; no mathematical completion beyond marked reading | low |
| 133 | 051 | left cancelled scratch diagram | pi_0 star to Hom/pi_0 | Uncertain quotient in a rotated overlapping cancellation; retained with doubt | low |
| 133 | 052 | 2 | `5` | Uncertain ink; no secure alternative | medium |
| 133 | 052 | 16 | `G` | Uncertain ink; no secure alternative | medium |
| 133 | 052 | 18 | `?` | Uncertain ink; no secure alternative | low |
| 133 | 052 | 35 | `N_1` | Uncertain ink; no secure alternative | medium |
| 133 | 052 | 35 | `\mathrm{comm}\,M` | \mathrm{coinv}\,M | medium |
| 133 | 052 | upper margin | annulé? | Margin flags the preceding condition, but no diagonal crossing; retained as marginal cancellation instruction without silently removing the text | medium |
| 133 | 052 | lower half, eta definition | N_comm M | Subscript structure is compressed; comm is closer to the visible letters than coinv, but exact nesting remains uncertain. | medium |
| 133 | 053 | 7 | `\ell` | Uncertain ink; no secure alternative | medium |
| 133 | 053 | 8 | `G` | N | medium |
| 133 | 053 | 10 | `Comme` | Uncertain ink; no secure alternative | medium |
| 133 | 053 | 11 | `\bar{x}` | Uncertain ink; no secure alternative | medium |
| 133 | 053 | 11 | `\text{ou}` | , | medium |
| 133 | 053 | 11 | `\bar{y}` | Uncertain ink; no secure alternative | medium |
| 133 | 053 | 12 | `q` | Uncertain ink; no secure alternative | medium |
| 133 | 053 | 25 | `est à partir de` | est déduit de | medium |
| 133 | 053 | 36 | `N_0` | Uncertain ink; no secure alternative | medium |
| 133 | 053 | first construction | G / N | Letter overwritten; G appears superposed on N-like strokes | medium |
| 133 | 053 | upper third, vanishing condition | bar x ou bar y | The small bars are overwritten and the joining word is compressed; comma remains possible. | medium |
| 133 | 053 | middle, parenthesis after on trouve | est à partir de | est déduit de; rapid and overwritten phrase, exact wording unresolved. | low |
| 133 | 054 | 14 | `\}` | Uncertain ink; no secure alternative | medium |
| 133 | 054 | 17 | `a` | Uncertain ink; no secure alternative | medium |
| 133 | 054 | 20 | `*` | Uncertain ink; no secure alternative | medium |
| 133 | 054 | 26 | `*` | Uncertain ink; no secure alternative | medium |
| 133 | 054 | 30 | `G_1` | Uncertain ink; no secure alternative | medium |
| 133 | 054 | b) final punctuation | dN=DM } exactement | A curly crossing/bracket after DM has no secure textual value; retained with doubt | medium |
| 133 | 054 | pi_1 decoration | star above cancelled, star below added | Two overwritten stars are visible at each occurrence; exact earlier star shape uncertain | medium |
| 133 | 054 | first induced arrow | twoheaded arrow | Arrow is repeatedly inked and appears doubled; retained despite subsequent epi condition | medium |

## Abbreviations

| Written form | Possible expansion (editorial; not supplied in the transcription) |
|---|---|
| loc. | localement |
| r.f. | rang fini |
| i.e. | id est |
| bil. ass. | bilinéaire associée |
| NB | nota bene |
| str. non. dég. | strictement non dégénérés |
| pol. univ. | polynômes universels |
| coeff. | coefficients |
| p.ex | par exemple |
| resp. | respectivement |
| mercr. | mercredi |
| hom. | homomorphisme |
| loc. lib. | localement libres |
| ext. | extension |
| inv. | inversible |
| tt | tout |
| mod. quad. | modules quadratiques |
| Mod. | Module |
| schém. | schéma |
| isom. | isomorphisme |

- `ens.`: ensemble(s).
- `hom`: homomorphisme, where used in prose.
- `cl`: classe (class symbol).
- `Prop`: proposition.

- `isom.`: isomorphe(s).
- `plus gén.`: plus généralement.
- `él.`: élément(s).

- `chgt`: changement.
- `à g.` (doubtful blue note): à gauche.
- `ss-groupe`: sous-groupe.

- `Fl`: flèches.
- `Ob`: objets.

- `nb`: nombre.
- `sym.`: symétrique(s).
- `th.`: théorème.
- `loc. annelé`: localement annelé.

- `pts`: points.
- `pris. bl.`: prisonniers blancs (reading of the surrounding qualification remains uncertain).

| Additional written form | Possible expansion (editorial only) |
|---|---|
| alg. | algébrique(s) |
| aff. | affine(s) |
| comm., commut | commutatif(s) |
| gr., grpe | groupe(s) |
| ss-grpe, ss-groupe | sous-groupe |
| conn. | connexe(s) |
| unipot., quasi-unip. | unipotent, quasi-unipotent |
| puiss. | puissance |
| car., Car. | caractéristique |
| V.A. | variété abélienne |
| tjrs | toujours |
| sss, ssi | si et seulement si |
| Pb | problème |
| sol. | solution |
| op. | opération(s) |
| déf. | défini / définition; phrase dependent |
| trivialt | trivialement |
| inv (subgroup context) | invariant |
| iso | isomorphisme / isomorphe |
| mono | monomorphisme |
| épi | épimorphisme |
| p.ex. | par exemple |
| t. mult. | type multiplicatif |
| égalis. | égales; compressed form on 044 remains an editorial interpretation |
| =, = with raised s | même, mêmes; literal shorthand retained in the transcription |
| E.S. | entrées-sorties (typed notice 050) |
| U.C. | unité centrale (typed notice 050) |
| U.S.T.L. | Université des Sciences et Techniques du Languedoc |
| C.H.U. | centre hospitalier universitaire |
| St | Saint |
| MR | Monsieur |


## Legibility and limitations

The printed articles (011–017) and university notices (048, 050) are generally clear; apparent spelling and mathematical anomalies are retained. The handwritten pages vary from readable dark ink to very rapid, faint grey notes. All 50 pages had a sequential first reading including the full image and both supplied halves, and a separate visual audit by the same root transcriber; this is not an independently transcribed second version. No OCR was used, and no context member was opened before the freeze.

The least reliable material is the pale machine text visible on the reused sheet 018, where numerous estimated unreadable word groups remain; the dense overlapping additions on music paper 036; the heavily cancelled initial formulas and German margin on 046; and overwritten or clipped passages on 043–044 and 051–054. Scan 044's short marginal note and insertion are especially uncertain as complete phrases. Cancellation can erase the letter bodies themselves, so a plausible marked formula must not be treated as securely recovered text.

TikZ diagrams reproduce objects, connections, relative placement and recoverable decorations. Small pen flourishes and irregular enclosures are approximations, not facsimiles. Signatures are given as doubtful name readings with the recoverable flourish drawn separately. The scope of the lower cancellation on 051 and the instruction “annulé?” on 052 remains explicitly uncertain; inspect the original images when using those passages as mathematical evidence.

Confidence describes the ink reading, not the mathematical truth of a statement. A high-confidence observation can concern an unexpected but clear source form. Detailed page-specific observations qualify the automatic listing of individual doubt macros; a low-confidence whole-phrase or cancellation observation takes precedence over an otherwise generic medium label. The audit record preserves how readings changed before freezing.

