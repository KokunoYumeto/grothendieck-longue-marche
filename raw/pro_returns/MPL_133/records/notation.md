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
