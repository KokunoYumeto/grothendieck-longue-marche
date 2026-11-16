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


## Reading doubts

Locations use the approximate line in the corresponding page fragment, not a reconstructed manuscript line.

| File | Scan | Approximate line | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
| 106 | 002 | TeX 3 | `Cat. d'obj. cofibrants` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 4 | `C1 . C3` | C1 : C3 | medium |
| 106 | 002 | TeX 4 | `pour mé. C0` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 6 | `\mathrm{cof}_{W_e}` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 29 | `\varnothing` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 34 | `\alpha_y` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 34 | `\alpha'_y` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 37 | `comme un des` | Unresolved; no secure alternative | low |
| 106 | 002 | TeX 39 | `lors` | alors | medium |
| 106 | 002 | TeX 43 | `y` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 49 | `quitte à introduire` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 50 | `on a deux relèvements` | Unresolved; no secure alternative | low |
| 106 | 002 | TeX 50 | `$\underset{g=f\alpha_x}{y}=\tilde y'$` | Unresolved; no secure alternative | low |
| 106 | 002 | TeX 50 | `que $\tilde y$` | Unresolved; no secure alternative | low |
| 106 | 002 | TeX 55 | `y'` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 58 | `g` | Unresolved; no secure alternative | low |
| 106 | 002 | TeX 70 | `x` | Unresolved; no secure alternative | medium |
| 106 | 002 | TeX 75 | `W` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 10 | `y` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 11 | `w` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 19 | `x` | a | medium |
| 106 | 003 | TeX 24 | `x` | a | medium |
| 106 | 003 | TeX 25 | `\bar y''` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 35 | `x\amalg x` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 44 | `r` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 45 | `i_1f` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 66 | `x` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 66 | `g` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 68 | `j_1` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 68 | `j'_2` | j_2 | low |
| 106 | 003 | TeX 71 | `\bar y` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 76 | `a` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 76 | `w` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 83 | `x` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 85 | `x` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 100 | `g` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 109 | `\varnothing` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 110 | `x\amalg x'` | Unresolved; no secure alternative | medium |
| 106 | 003 | TeX 114 | `x` | Unresolved; no secure alternative | low |
| 106 | 003 | TeX 118 | `x\amalg x` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 4 | `\varphi` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 8 | `\tilde x` | Unresolved; no secure alternative | medium |
| 106 | 004 | TeX 12 | `\tilde f` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 13 | `u` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 23 | `En` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 30 | `faire voir` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 30 | `donnent` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 30 | `égaux` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 33 | `va` | on va | low |
| 106 | 004 | TeX 35 | `\Psi\Phi\overset{\mathrm{def}}{=}` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 42 | `[\alpha_x]` | Unresolved; no secure alternative | medium |
| 106 | 004 | TeX 42 | `\text{donc}` | Unresolved; no secure alternative | medium |
| 106 | 004 | TeX 51 | `\alpha` | Unresolved; no secure alternative | low |
| 106 | 004 | TeX 51 | `x` | Unresolved; no secure alternative | low |
| 106 | 005 | TeX 2 | `\texttt{I}` | \texttt{1} | medium |
| 106 | 006 | TeX 2 | `7` | 3 | medium |
| 106 | 006 | TeX 7 | `*` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 15 | `C1 : C3` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 15 | `qui` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 24 | `i.e.` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 24 | `équi. faible couniverselle` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 30 | `x` | a | low |
| 106 | 006 | TeX 30 | `\varphi` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 31 | `k` | Unresolved; no secure alternative | medium |
| 106 | 006 | TeX 34 | `g'f` | Unresolved; no secure alternative | low |
| 106 | 006 | TeX 36 | `g'g` | g'f | medium |
| 106 | 006 | TeX 36 | `kj` | Unresolved; no secure alternative | medium |
| 106 | 008 | TeX 3 | `par` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 9 | `appl.` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 11 | `compatibles à` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 12 | `x` | y | medium |
| 106 | 008 | TeX 15 | `2` | ? | medium |
| 106 | 008 | TeX 18 | `ni` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `ni` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `en se contentant` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `\mathrm{Couniv.}W` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `si` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `pas néc.` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `W` | Unresolved; no secure alternative | low |
| 106 | 008 | TeX 18 | `\mathrm{Couniv.}W` | Unresolved; no secure alternative | low |
| 106 | 009 | TeX 119 | `P` | 9 | medium |
| 106 | 009 | TeX 135 | `849` | Unresolved; no secure alternative | medium |
| 106 | 010 | TeX 4 | `lemme` | lemma | medium |
| 106 | 010 | TeX 6 | `\varphi` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 9 | `et` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 11 | `\alpha g=\operatorname{id}_y` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 14 | `W` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 18 | `f` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 23 | `tjs` | Unresolved; no secure alternative | medium |
| 106 | 010 | TeX 30 | `\Phi` | \varphi | medium |
| 106 | 010 | TeX 32 | `injectif` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 32 | `À priori que` | Unresolved; no secure alternative | low |
| 106 | 010 | TeX 32 | `produit` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 5 | `le foncteur inverse serait forcément donné par` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 5 | `envisager` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 5 | `ce que` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 6 | `entraînerait` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 12 | `\simeq` | Unresolved; no secure alternative | medium |
| 106 | 012 | TeX 15 | `ttes` | Unresolved; no secure alternative | medium |
| 106 | 012 | TeX 17 | `=^{\mathrm{s}}` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 17 | `et définie ainsi par les flèches de $x\longrightarrow y$` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 17 | `ayant pour` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 17 | `définie maintenant` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 19 | `x` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 19 | `\longrightarrow` | Unresolved; no secure alternative | low |
| 106 | 012 | TeX 19 | `y` | Unresolved; no secure alternative | low |
| 106 | 013 | TeX 276 | `\longrightarrow` | Unresolved; no secure alternative | low |
| 106 | 013 | TeX 280 | `\Phi` | \varphi | medium |
| 106 | 014 | TeX 4 | `deux` | un | low |
| 106 | 014 | TeX 4 | `foncteurs` | foncteur | low |
| 106 | 014 | TeX 6 | `C\longrightarrow` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 13 | `$f\in W$` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 20 | `Et on trouve les composés` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 20 | `et on a donc` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 21 | `[\,]^{x}` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 23 | `définissons le` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 28 | `\alpha` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 28 | `g` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 30 | `donc $\bar y$ cof` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 31 | `w.k lifting lemma` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 38 | `un` | une | low |
| 106 | 014 | TeX 41 | `\alpha` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 41 | `f_0` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 41 | `\operatorname{cof}` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 41 | `\alpha` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 41 | `\alpha` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 43 | `$x\longrightarrow y$` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 43 | `$f''$` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 43 | `\diagram{\begin{tikzcd}x\arrow[r]&y''\end{tikzcd}}` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 43 | `permet de` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 43 | `reçoit` | réduit | low |
| 106 | 014 | TeX 43 | `comme on voit dans les diagrammes` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 45 | `comme préc.` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 45 | `dans un produit` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 47 | `f` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 48 | `\bar y` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 48 | `i` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 50 | `(les deux isos)` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 52 | `1_y` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 52 | `x` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 52 | `f` | Unresolved; no secure alternative | low |
| 106 | 014 | TeX 53 | `\alpha` | Unresolved; no secure alternative | low |
| 106 | 015 | TeX 141 | `y` | Unresolved; no secure alternative | low |
| 106 | 015 | TeX 142 | `p` | \rho | medium |
| 106 | 015 | TeX 147 | `y` | Unresolved; no secure alternative | low |
| 106 | 015 | TeX 147 | `y'` | x' | low |
| 106 | 015 | TeX 148 | `\amalg` | Unresolved; no secure alternative | medium |
| 106 | 016 | TeX 5 | `\{f_0\vee f'_0\}` | Unresolved; no secure alternative | medium |
| 106 | 016 | TeX 9 | `\alpha''` | Unresolved; no secure alternative | medium |
| 106 | 016 | TeX 9 | `\alpha''` | Unresolved; no secure alternative | medium |
| 106 | 016 | TeX 12 | `On en a donc` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 12 | `la section de` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 14 | `i''` | i' | low |
| 106 | 016 | TeX 14 | `\alpha''` | \alpha' | low |
| 106 | 016 | TeX 14 | `i'` | i'' | low |
| 106 | 016 | TeX 14 | `et` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 14 | `,` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 24 | `*` | Unresolved; no secure alternative | medium |
| 106 | 016 | TeX 26 | `(deux $i,i'\in W$)` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 26 | `pour deux telles sections $i,i'$` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 28 | `x` | Unresolved; no secure alternative | low |
| 106 | 016 | TeX 34 | `?` | Unresolved; no secure alternative | medium |
| 106 | 016 | TeX 38 | `suffis\textsuperscript{t}` | Unresolved; no secure alternative | medium |
| 107 | 002 | TeX 3 | `Formalisme` | Unresolved; no secure alternative | medium |
| 107 | 002 | TeX 7 | `relatifs` | relatif | medium |
| 107 | 003 | TeX 19 | `Y` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 21 | `X_0` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 24 | `\mathrm{Hom}` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 31 | `A` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 31 | `What about` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 38 | `\(L\in\mathrm{Ob}A^\wedge\)` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 41 | `complex with value` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 45 | `\Gamma_A` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 49 | `second hand side` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 49 | `we` | Unresolved; no secure alternative | low |
| 107 | 003 | TeX 57 | `a` | a_1 | low |
| 107 | 003 | TeX 58 | `\varphi` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 8 | `p_A` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 17 | `\mathrm{Hom}(X,Y)=` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 18 | `A` | B | medium |
| 107 | 004 | TeX 21 | `qques` | Unresolved; no secure alternative | medium |
| 107 | 004 | TeX 23 | `q_b` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 23 | `A^\wedge` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 24 | `\simeq` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 24 | `A^\wedge` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 25 | `\simeq\mathrm{Hom}` | Unresolved; no secure alternative | low |
| 107 | 004 | TeX 27 | `B` | Unresolved; no secure alternative | medium |
| 107 | 004 | TeX 28 | `\downarrow` | Unresolved; no secure alternative | medium |
| 107 | 004 | TeX 31 | `B` | A | medium |
| 107 | 004 | TeX 31 | `A` | B | medium |
| 107 | 004 | TeX 38 | `B^\wedge` | A^\wedge | medium |
| 107 | 004 | TeX 38 | `a` | b | medium |
| 107 | 004 | TeX 38 | `a` | b | medium |
| 107 | 004 | TeX 38 | `B` | A | medium |
| 107 | 006 | TeX 3 | `On peut aussi décrire les mêmes foncteurs` | Unresolved; no secure alternative | low |
| 107 | 006 | TeX 6 | `écrivant` | Unresolved; no secure alternative | medium |
| 107 | 006 | TeX 7 | `A` | Unresolved; no secure alternative | medium |
| 107 | 006 | TeX 8 | `\Gamma_b` | Unresolved; no secure alternative | low |
| 107 | 006 | TeX 10 | `(X)` | Unresolved; no secure alternative | low |
| 107 | 006 | TeX 16 | `\Gamma_M''` | Unresolved; no secure alternative | medium |
| 107 | 006 | TeX 20 | `''` | ' | medium |
| 107 | 006 | TeX 26 | `X''` | Unresolved; no secure alternative | low |
| 107 | 006 | TeX 26 | `A` | Unresolved; no secure alternative | low |
| 107 | 006 | TeX 26 | `\underline{\mathrm{Hom}}` | Unresolved; no secure alternative | low |
| 107 | 006 | TeX 26 | `A\times B^\wedge` | (A\times B)^\wedge | low |
| 107 | 006 | TeX 27 | `A` | Unresolved; no secure alternative | medium |
| 107 | 006 | TeX 30 | `\({}^{\mathrm{el}}\)` | Unresolved; no secure alternative | medium |
| 107 | 007 | TeX 4 | `PREDONTA` | PREDDNTA | medium |
| 107 | 007 | TeX 4 | `\#` | \& | medium |
| 107 | 007 | TeX 7 | `\deleted{0}` | Unresolved; no secure alternative | low |
| 107 | 007 | TeX 8 | `\deleted{0}` | Unresolved; no secure alternative | low |
| 107 | 007 | TeX 24 | `SYSPPP` | SYSPFP | medium |
| 107 | 007 | TeX 29 | `SYSPPP` | SYSPFP | medium |
| 107 | 008 | TeX 3 | `\Gamma` | E | low |
| 107 | 008 | TeX 6 | `\wedge` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 10 | `Je ne sais pas` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 12 | `au` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 14 | `ou nous rest. aux ensembles de fins homot.` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 15 | `\({}^{\mathrm{t}}\)` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 27 | `construire` | avoir | low |
| 107 | 008 | TeX 27 | `M` | B | low |
| 107 | 008 | TeX 27 | `(pour b donné)` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 27 | `un élém.` | un élément | low |
| 107 | 008 | TeX 27 | `objt` | Unresolved; no secure alternative | low |
| 107 | 008 | TeX 27 | `OK ssi` | Unresolved; no secure alternative | low |
| 107 | 009 | TeX 32 | `4` | Unresolved; no secure alternative | low |
| 107 | 009 | TeX 35 | `SYSPPP` | SYSPFP | medium |
| 107 | 010 | TeX 5 | `\mathop{=}\limits^{\mathrm{déf}}` | Unresolved; no secure alternative | low |
| 107 | 010 | TeX 5 | `M` | Unresolved; no secure alternative | low |
| 107 | 010 | TeX 7 | `Relation` | Unresolved; no secure alternative | medium |
| 107 | 010 | TeX 7 | `mais nous` | mais ici | medium |
| 107 | 010 | TeX 7 | `intéressons` | Unresolved; no secure alternative | medium |
| 107 | 010 | TeX 13 | `tantôt` | d'hab. | medium |
| 107 | 010 | TeX 13 | `les sommes` | Unresolved; no secure alternative | medium |
| 107 | 010 | TeX 18 | `X(b)` | Unresolved; no secure alternative | low |
| 107 | 010 | TeX 21 | `non` | Unresolved; no secure alternative | medium |
| 107 | 010 | TeX 24 | `b` | Unresolved; no secure alternative | low |
| 107 | 011 | TeX 14 | `PPP` | PFP | medium |
| 107 | 011 | TeX 33 | `PPP` | PFP | medium |
| 107 | 011 | TeX 43 | `\sqcup` | Unresolved; no secure alternative | medium |
| 107 | 011 | TeX 43 | `\sqcup` | Unresolved; no secure alternative | medium |
| 107 | 012 | TeX 8 | `Récapitulation` | Récapitulat$^\circ$ | medium |
| 107 | 012 | TeX 11 | `\Gamma` | E | medium |
| 107 | 012 | TeX 11 | `{}^g a` | Unresolved; no secure alternative | medium |
| 107 | 012 | TeX 12 | `p_B^*` | Unresolved; no secure alternative | low |
| 107 | 012 | TeX 17 | `\simeq` | Unresolved; no secure alternative | low |
| 107 | 012 | TeX 20 | `A` | B | medium |
| 107 | 012 | TeX 31 | `Y` | X | medium |
| 107 | 012 | TeX 38 | `B` | A | medium |
| 107 | 013 | TeX 16 | `PPP` | PFP | medium |
| 107 | 013 | TeX 19 | `3` | Unresolved; no secure alternative | low |
| 107 | 013 | TeX 32 | `PPP` | PFP | low |
| 107 | 014 | TeX 6 | `\mathrm{Ens}\,\widehat A` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 11 | `mais est équiv.` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 13 | `qui` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 15 | `L` | X | low |
| 107 | 014 | TeX 15 | `\text{---}` | \longrightarrow | low |
| 107 | 014 | TeX 19 | `\mathrm{Hom}` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 21 | `(A\times B)^\wedge` | (\widehat A\times\widehat B)^\wedge | low |
| 107 | 014 | TeX 21 | `élém.` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 22 | `can.` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 25 | `contravariant` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 25 | `considéré qu'il représente` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 29 | `Hom-` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 31 | `*` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 33 | `L'\in A` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 39 | `et le` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 39 | `les deux mbs` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 40 | `ce qui est le cas` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 40 | `et il paraît que` | Unresolved; no secure alternative | low |
| 107 | 014 | TeX 45 | `M` | Unresolved; no secure alternative | low |
| 107 | 015 | TeX 9 | `X_2` | Unresolved; no secure alternative | low |
| 107 | 015 | TeX 22 | `a` | Unresolved; no secure alternative | low |
| 107 | 015 | TeX 22 | `e_B` | Unresolved; no secure alternative | low |
| 107 | 015 | TeX 36 | `PPP` | PFP | medium |
| 107 | 015 | TeX 54 | `PPP` | PFP | medium |
| 107 | 015 | TeX 60 | `IEBUPDTE` | Unresolved; no secure alternative | medium |
| 107 | 016 | TeX 4 | `$d^{\circ}$` | Unresolved; no secure alternative | low |
| 107 | 016 | TeX 6 | `M'=e_{\widehat B},M=` | Unresolved; no secure alternative | low |
| 107 | 016 | TeX 14 | `flèche can.` | flèche | low |
| 107 | 016 | TeX 14 | `la` | cette | low |
| 107 | 016 | TeX 16 | `catégories` | catégorie | low |
| 107 | 016 | TeX 16 | `munie de produits` | Unresolved; no secure alternative | low |
| 107 | 016 | TeX 16 | `fini` | Unresolved; no secure alternative | low |
| 107 | 016 | TeX 18 | `même` | Unresolved; no secure alternative | low |
| 107 | 016 | TeX 20 | `L\in\operatorname{Ob}\widehat A` | L\operatorname{Ob}\widehat A | low |
| 107 | 017 | TeX 6 | `tt` | Unresolved; no secure alternative | low |
| 107 | 017 | TeX 8 | `catégorie` | Unresolved; no secure alternative | medium |
| 107 | 017 | TeX 13 | `g` | ? | low |
| 107 | 017 | TeX 30 | `\deleted{TRK}\inserted{CYL}` | CYL | low |
| 107 | 017 | TeX 38 | `PFP` | PPP | medium |
| 107 | 017 | TeX 50 | `2` | Unresolved; no secure alternative | low |
| 107 | 017 | TeX 54 | `PFP` | PPP | medium |
| 107 | 019 | TeX 10 | `\Delta` | a | medium |
| 107 | 019 | TeX 12 | `-` | \omega | medium |
| 107 | 019 | TeX 22 | `is` | Unresolved; no secure alternative | medium |
| 107 | 019 | TeX 24 | `\in` | Unresolved; no secure alternative | low |
| 107 | 019 | TeX 26 | `mut` | Unresolved; no secure alternative | low |
| 107 | 019 | TeX 26 | `As` | Unresolved; no secure alternative | low |
| 107 | 019 | TeX 26 | `is equivalent` | Unresolved; no secure alternative | low |
| 107 | 019 | TeX 30 | `Y` | Unresolved; no secure alternative | medium |
| 107 | 021 | TeX 3 | `as` | Unresolved; no secure alternative | low |
| 107 | 021 | TeX 14 | `g` | Unresolved; no secure alternative | low |
| 107 | 021 | TeX 16 | `is` | Unresolved; no secure alternative | medium |
| 107 | 021 | TeX 28 | `II` | I | medium |
| 107 | 021 | TeX 28 | `2.4` | 2.9 | medium |
| 107 | 021 | TeX 30 | `iff` | Unresolved; no secure alternative | low |
| 107 | 021 | TeX 30 | `J` | I | low |
| 107 | 021 | TeX 30 | `o` | Unresolved; no secure alternative | low |
| 107 | 021 | TeX 30 | `possibly` | Unresolved; no secure alternative | low |
| 107 | 022 | TeX 38 | `a` | Unresolved; no secure alternative | medium |
| 107 | 022 | TeX 48 | `\mathrm{fib}` | Unresolved; no secure alternative | medium |
| 107 | 022 | TeX 51 | `\partial_1` | Unresolved; no secure alternative | low |
| 107 | 022 | TeX 55 | `Y_x` | Unresolved; no secure alternative | medium |
| 107 | 023 | TeX 2 | `e` | c | low |
| 107 | 023 | TeX 12 | `h` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 17 | `\text{and}` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 23 | `considering that` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 26 | `=` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 27 | `\bar\theta` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 35 | `for` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 46 | `forgetting` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 46 | `shortcircuiting` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 47 | `and we want a` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 47 | `unfortunately` | Unresolved; no secure alternative | low |
| 107 | 023 | TeX 53 | `\times 0` | Unresolved; no secure alternative | low |
| 107 | 024 | TeX 3 | `\varphi` | \psi | medium |
| 107 | 024 | TeX 4 | `\varphi` | \psi | medium |
| 107 | 024 | TeX 40 | `S00101` | SO0101 | medium |
| 107 | 025 | TeX 5 | `\lim` | Unresolved; no secure alternative | low |
| 107 | 025 | TeX 28 | `\varphi_i` | \psi_i | low |
| 107 | 025 | TeX 29 | `i-1` | i+1 | low |
| 107 | 025 | TeX 29 | `i-1` | i+1 | low |
| 107 | 025 | TeX 29 | `i-1` | i+1 | low |
| 107 | 025 | TeX 34 | `h'\!\!\!/` | Unresolved; no secure alternative | low |
| 107 | 025 | TeX 34 | `i-1` | i+1 | low |
| 107 | 025 | TeX 36 | `h?` | Unresolved; no secure alternative | low |
| 107 | 025 | TeX 41 | `i-1` | i+1 | low |
| 107 | 025 | TeX 50 | `on` | our | low |
| 107 | 025 | TeX 50 | `contrary` | Unresolved; no secure alternative | low |
| 107 | 025 | TeX 52 | `Z_i` | Z | low |
| 107 | 026 | TeX 26 | `5302` | 5802 | medium |

## Legibility and limits

The printed reused sheets are generally more legible than the mathematical cursive, although broken dot-matrix letters and digits sometimes leave P/F, 3/8, and other alternatives unresolved. The least secure passages are the overwritten factorization argument in 106/014; the cancelled draft in 107/003; the cramped right margin and lower lines of 107/008; the propositions and deletions in 107/014; the compressed middle of 107/016; the cancelled diagrams and prose of 107/023; and the small indices and revised lower diagrams of 107/025. Low confidence means that the proposed reading should be checked in the scan before being quoted or used mathematically; medium confidence is still an explicit doubt, not a verification. Some diagram geometry and unlabelled pen strokes are necessarily represented approximately in TikZ. The second visual reading corrected both literal readings and missing small features, but it cannot certify that every unmarked reading is right. The fragments preserve visibly anomalous formulas, incomplete punctuation, abbreviations, and unfinished strokes. All explicit doubt macros in the final fragments are indexed above; no illegible-word macro was needed.
