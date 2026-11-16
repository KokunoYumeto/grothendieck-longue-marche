# MPL 106+107 — Notation and doubts

## Package notation table

One reader transcribed and visually audited all 41 pages before opening the context. The table consolidates the notation record kept during that reading; repeated signs were compared across the fragments and their images. Differences actually visible in the ink are retained, including unfinished strokes, inconsistent indices, and changes of notation within an argument.

| Manuscript sign or recurring form | LaTeX representation | Distinction checked / representative scans |
|---|---|---|
| Ordinary capital category and class letters | `C`, `W`, `A`, `B`, `M` | Not silently made calligraphic; 106/002–016, 107/003–025. |
| Cof, cof | `\mathrm{Cof}`, `\mathrm{cof}` | Capital category name versus lower-case object or morphism condition. |
| W with e, 0, or Cof subscript | `W_e`, `W_0`, `W_{\mathrm{Cof}}` | Kept distinct; 106/002, 006, 012. |
| Underlined W | `\underline W` | Different from the unadorned class W; 107/019, 021. |
| Tilde, bar, and prime over/after an object | `\tilde x`, `\bar x`, `x'`, `x''` | Distinguished by the ink rather than the expected replacement construction; 106/002–016. |
| Capital Phi and Psi functors | `\Phi`, `\Psi` | Distinct from lower-case phi in arrows; 106/002, 004. |
| Lower-case phi and psi | `\varphi`, `\psi` | Ambiguous forms carry `\unsure`; particularly 107/024–025. |
| Alpha, beta, gamma, epsilon, theta, rho | `\alpha`, `\beta`, `\Gamma`, `\varepsilon`, `\theta`, `\rho` | Case and shape retained; doubtful rho/p and Gamma/E-like signs are marked locally. |
| Initial or empty-object sign | `\varnothing` | Not silently read as phi; 106/002 and the last formula of 107/025. |
| Cofibrant two-arrow chains | `\underline{\operatorname{Ch}}_0(x,y)` | Underline where present; the written conditions change at 106/012. |
| Components | `\pi_0` | Subscript zero; 106/008–016 and 107/025. |
| Fl | `\operatorname{Fl}` | Literal written abbreviation; 106/008. |
| Hom, underlined Hom, and barred Hom | `\operatorname{Hom}`, `\underline{\operatorname{Hom}}`, `\overline{\operatorname{Hom}}` | Ordinary Hom, underlining, and overline are separate written features; relative Hom in 107/003–017, barred Hom in 107/021. `\mathrm{Hom}` also occurs inside the same underlined typography. |
| Relative Hom with A/B below | `\underline{\operatorname{Hom}}_A`, `\underline{\operatorname{Hom}}_B` | Do not supply a missing underline or hat from the intended adjunction. |
| Low exclamation mark or pair | `\underline{\mathrm{Hom}}_!`, `\underline{\mathrm{Hom}}_{!!}` | Dotted exclamation marks, not primes; low on 107/014. |
| High versus low exclamation mark | `\underline{\operatorname{Hom}}^!`, `\underline{\operatorname{Hom}}_!` | Both occur on 107/017 and are kept at their visible heights. |
| Single and double prime on evaluation operators | `\Gamma'`, `\Gamma''` | Compared in 107/004, 006, 008; no conversion into exclamation marks. |
| Epsilon with M or b below | `\varepsilon_M`, `\varepsilon_b` | Distinct from Gamma evaluation notation; 107/006. |
| Hat over A/B or a product | `\widehat A`, `\widehat B`, `\widehat{A\times B}` | Missing hats in the ink remain missing; 107/003–017. |
| Raised opposite-category o | `^o` | Not changed to `^{\mathrm{op}}`; stacked forms in 107/014, 017 retained. |
| Raised wedge and vee | `A^{o\wedge}`, `A^\vee`, `A^{\vee o}` | Kept as written in the duality calculations, 107/017. |
| Left g/d superscripts | `{}^gX`, `{}^dX`, `{}^ga`, `{}^db` | Left superscripts on 107/012, not primes. |
| Circular tensor, square product, ordinary cross | `\otimes`, `\boxtimes`, `\times` | Read separately, especially 107/010–017, 021–025. |
| Coproduct, indexed coproduct, union, vee | `\amalg`, `\coprod`, `\cup`, `\vee` | Shapes retained rather than made uniform; 106/016 and 107/010, 025. |
| Indexed coproduct with category below/right | `\underset{\sigma\in M(b)}{\coprod_A}` | Category A or Ahat and the indexing set are separate; 107/010. |
| Direct and inverse limits | `\varinjlim`, `\varprojlim` | Arrow direction checked; no substitution of homotopy limits; 107/008–025. |
| Delta with n, dot, or (1) | `\Delta_n`, `\dot\Delta_n`, `\Delta^{(1)}`, `\Delta(1)` | Different placements and dot preserved; 107/015, 025. |
| Homotopy sign and its raised label | `\sim`, `\overset{k}{\sim}`, `\overset{h}{\sim}`, `\overset{l}{\sim}`, `\overset{r}{\sim}`, `\overset{s}{\sim}` | Label k corrected during audit of 107/021; l/r/s remain separate. |
| Underlined Retr | `\underline{\operatorname{Retr}}` | Underlined word and uncertain argument retained, 107/025. |
| Squiggle attached to an arrow | `\sim` as an arrow label | Does not itself supply an arrowhead. |
| Headless connector | `\mathbin{-}` or TikZ `no head` / `-` | Blank or unfinished strokes are not completed from mathematical expectations. |
| Hooked connector, arrow, thick arrow | TikZ `hook`, `->`, `very thick` | Hooks and arrowheads read separately; some hooked connectors are explicitly headless. Thick single arrows are not rendered as logical double arrows. |
| Paired vertical equality strokes | `\Vert` | Vertical proof layout, 107/014; not quotation marks. |
| Written double quotation marks | two backticks followed by two apostrophes | The same TeX convention throughout; no guillemets supplied. |
| Handwritten page numbers and circled letters | `\mspage{...}`, sometimes within a TikZ circle/ellipse | Archive scan number is separate. Uncertain e/c in 107/023 is not regularized from sequence. |
| Printed machine identifiers and digits | `\texttt{...}` | Literal strings; P/F and 3/8 doubts remain even where a program or volume name would suggest a correction. |

## Abbreviations encountered

Expansions are interpretive aids in this file only. They are never substituted into the transcription; an expansion is not a claim that a disputed manuscript word was read securely.

| Abbreviation / shortened form | Proposed expansion or interpretation |
|---|---|
| cat. | catégorie / category, according to language |
| d'obj. / objt | d'objets / objet |
| cof / Cof | cofibrant, cofibration; category of cofibrant objects when capitalized |
| fib / cofib. | fibration / cofibration |
| P. ex / p.ex. | par exemple |
| tt / ttes | tout / toutes |
| tjs | toujours |
| qques | quelques |
| élém. | élément |
| néc. | nécessaire |
| suffis with raised ending | suffisant / suffisante; exact ending follows the ink |
| can. | canonique / canonical |
| str. | strict / strictement |
| cocart | cocartésien |
| w.k | weak; the reading of the abbreviation itself is uncertain |
| id / Id | identité / identity |
| comp. | composante or composition, according to the passage |
| préc. | précédent / précédemment |
| iso / isos | isomorphisme(s) |
| fonct. | foncteur / fonctoriel, according to the passage |
| dém. / Dém. | démonstration |
| Prop. / prop. | proposition |
| Ch. | chapter |
| pg | page |
| pb | problème / problem |
| f.p. | finitely presented, in 107/019 |
| s.th. | such that |
| i.e. | id est / that is |
| d° | ditto |
| mé. | mémoire / pour mémoire; reading uncertain, 106/002 |
| SPS | “suffit pour cela de supposer” is a possible expansion; unverified and not used to alter the text |
| Ob | objets / objects |
| Fl | flèches |
| lim | limite / limit |
| Hom / Hot / Retr | morphisms / homotopy category / retractions; notation, not expanded in the text |
| BLKSIZE, RECFM, LRECL, DCB, DSN, DISP, PGM, COND | Printed program-field abbreviations retained literally; tentative technical expansions are not used as reading evidence |
