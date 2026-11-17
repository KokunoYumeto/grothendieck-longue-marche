# Notation table

This is the single notation key used throughout the package, reconciled against the images before freezing. It records visible forms, not a modernization of the notation. A vertical bar inside an `unsure` argument separates alternatives; it is not manuscript punctuation. The same letter can legitimately have a different decoration in a different occurrence.

| Manuscript sign or convention | LaTeX reading | Cross-page comparison and remaining limits |
|---|---|---|
| O with a separate lower bar | `\underline{O}` | Structural-sheaf occurrences on019–027 and046 have a visible lower bar. They are not silently converted to script O. |
| Unbarred local-ring O | `\unsure{O\|\mathcal O}` | Scan039 has no securely separate lower bar; the alphabet remains doubtful. |
| Ideal I | `\unsure{I\|\mathcal{I}}` | Recurs in019,020,022,023. The plain/script distinction remains uncertain and is marked consistently. |
| Module J, and J with bar | `J`, `\bar J` | Kept distinct from I; subscripts0,n and quotient notation are read locally. |
| F, L, A, B with a lower bar | `\underline F`, `\uline{F}`, and analogous letters | These commands both reproduce a lower stroke; they do not assert different mathematical objects. Scan037's F retains an explicit plain-underlined/script alternative. |
| V with a check and lower bar | `\underline{\check V}` | Clearly present on038; related checked V on037 remains locally doubtful. A check is not transcribed as a prime. |
| Graph letter gamma | `\Gamma` | Compared in019–025 and036; overwritten Gamma/P subscripts on024 remain in-place doubts. |
| Script restriction-functor initial | `\unsure{\mathcal R\|\mathcal G}` | Both occurrences on034 use the same unresolved script-letter reading. No Gamma is supplied from the subject matter. |
| Plain W with lower bar and small circle | `\underline W^\circ` | Outline034; retain the circle and the local doubts on its other occurrences. |
| Outlined Z, underlined Z, overwritten Z | `\mathbb Z` (035), `\underline Z` (044), `\unsure{Z\|T}` (053) | Rechecked separately: the last is overwritten, not confidently a bold letter. |
| Projective-space P | `\unsure{P\|\mathbf P}` | Both045 occurrences have the same alphabet doubt. Heavy ink alone does not establish bold type. |
| Parameter pi | `\pi` |019 calls it a parameter; its repeated exponent is consistently `\unsure{n+1\|-n}`. This table does not strengthen the word to uniformizer. |
| xi, eta and successive primes | `\xi`, `\eta`, `'`, `''`, `'''` |019–022 checked together; primes distinguish successive classes. No exclamation-mark exponent was securely identified in this package. |
| f pushforward / pullback | `f_*`, `f^*` | Subscript star and superscript star are kept distinct throughout. Overwriting on049 remains `\unsure{f_*\|f^*}`. |
| Looped subscript on étale f | `\unsure{f_\alpha^{\mathrm{ét}}\|f_*^{\mathrm{ét}}}` | The second occurrence on057 and the bottom two on058 are looped; clearer stars elsewhere remain stars. No bang is inferred. |
| phi variants | `\phi`, `\varphi` | The letter is preserved in the local form used for the morphism/functor; the prime on031's phi is a prime. |
| Absolute component count nu | `\nu`, `\nu_s`, `\nu(s)` |048–055; distinguished from ordinary n and d. The multiplier on049 is explicitly nu/d doubtful; the total degree n is separate on054. |
| Differential Omega | `\Omega`, `\Omega^{\unsure{1}}` |020 has an uncertain small1;022 does not acquire that superscript by analogy. |
| Underlined Hom, Isom, Aut versus ordinary Hom | `\underline{\operatorname{Hom}}` or `\uline{\operatorname{Hom}}`; ordinary `\operatorname{Hom}` | The lower bar is preserved, especially in the internal/global Hom comparison057–058 and the typed letter031–032. |
| Ambiguous operator on049 | `\unsure{\operatorname{Spec}\|\operatorname{Sym}}` | Both instances compared with clearly written Spec and the checked-V formula038; uncertainty remains. No symmetric-algebra correction is made. |
| Products / coproducts | `\prod`, `\coprod`, `\amalg` | Their written index positions are retained, including the reversed-looking product on028. |
| Literal dash in a list or product | `-`, or `\unsure{-\|\cdots}` |047–048 and053 contain solid strokes; ellipses are used only where dots are visible. |
| Ditto/equality-like shorthand in prose | `$=$` | The repeated short double stroke is retained in020–022,027–029,041,049–050,052,054,056. Possible expansion “même” is confined to the abbreviation list. |
| Double quotation marks | two backticks and two apostrophes | Same LaTeX form throughout; no conversion to guillemets. |
| Underline and double underline | `\uline{…}`, `\uuline{…}` | Visible emphasis retained; circled words and callouts are drawn in TikZ. |
| A connecting stroke and uncertain arrowhead | `\unsure{\longrightarrow\|\text{—}}`, or `dash` in tikz-cd | No direction is supplied solely from the expected mathematics; clear paired heads on050–051 are represented as such. |
| Dashed arrows, hooks, surjections, paired heads | tikz-cd `dashed`, `hook`, `two heads`, `<->` | Endpoints and decorations checked against each diagram. Curves and enclosures use TikZ paths. |
| Archival foliation | `% archive foliation: n` | Not treated as the author's numbering. No secure independent authorial page number was identified. |
| Deletion, insertion, margin | `\deleted`, `\inserted`, `\margin` | Nested cancellation is retained. Uncertain cancellation of the large injection block041 is explicitly wrapped in `\unsure`. |
| Abbreviations | literal form in the transcription | Proposed expansions appear only in the separate list below, never substituted into the transcription. |


# Doubt register

Line references below are approximate lines of the individual page fragment (including its page markers); the quoted reading is the primary locator. Every uncertainty macro is registered, including repeated signs. Confidence rates the visual reading only. Long or especially difficult marginal/cancelled readings are low; other tentative readings are medium. No unmarked reading is guaranteed.

| File | Scan | Approx. line | Reading | Alternatives | Confidence |
|---|---:|---:|---|---|---|
| 91 | 19 | 4 | `marqués` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 4 | `+` | `4` | medium |
| 91 | 19 | 5 | `droit du bas` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 5 | `\Longrightarrow` | `\longrightarrow` | medium |
| 91 | 19 | 9 | `1` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 9 | `1` | `2` | medium |
| 91 | 19 | 12 | `dans` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 15 | `I` | `\mathcal{I}` | medium |
| 91 | 19 | 17 | `$\unsure{I&#124;\mathcal{I}}$` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 17 | `I` | `\mathcal{I}` | medium |
| 91 | 19 | 18 | `I` | `\mathcal{I}` | medium |
| 91 | 19 | 20 | `tensorise par` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 20 | `A_{0\eta}` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 21 | `localise en` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 21 | `\eta` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 23 | `n+1` | `-n` | medium |
| 91 | 19 | 25 | `n+1` | `-n` | medium |
| 91 | 19 | 30 | `n+1` | `-n` | medium |
| 91 | 19 | 33 | `I` | `\mathcal{I}` | medium |
| 91 | 19 | 36 | `I` | `\mathcal{I}` | medium |
| 91 | 19 | 39 | `\bmod` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 40 | `I` | `\mathcal{I}` | medium |
| 91 | 19 | 42 | `donc vérifier qu'il ne faut pas remplacer` | `Unresolved; no reliable alternative` | low |
| 91 | 19 | 42 | `par` | `Unresolved; no reliable alternative` | medium |
| 91 | 19 | 42 | `ci-dessus` | `Unresolved; no reliable alternative` | medium |
| 91 | 20 | 3 | `mb` | `Unresolved; no reliable alternative` | medium |
| 91 | 20 | 5 | `(P_0;)` | `Unresolved; no reliable alternative` | medium |
| 91 | 20 | 6 | `I` | `\mathcal{I}` | medium |
| 91 | 20 | 6 | `I` | `\mathcal{I}` | medium |
| 91 | 20 | 7 | `1` | `Unresolved; no reliable alternative` | medium |
| 91 | 20 | 9 | `et` | `Unresolved; no reliable alternative` | medium |
| 91 | 20 | 33 | `démontre` | `démontrera` | medium |
| 91 | 20 | 35 | `donc` | `Unresolved; no reliable alternative` | medium |
| 91 | 21 | 6 | `Cet` | `Unresolved; no reliable alternative` | medium |
| 91 | 21 | 6 | `et` | `Unresolved; no reliable alternative` | medium |
| 91 | 21 | 10 | `\varphi_\eta` | `Unresolved; no reliable alternative` | medium |
| 91 | 21 | 11 | `l'on` | `Unresolved; no reliable alternative` | medium |
| 91 | 21 | 12 | `obstructions` | `constructions` | medium |
| 91 | 21 | 14 | `de` | `$\Rightarrow$` | medium |
| 91 | 21 | 24 | `en ce quotient` | `de cet espace` | medium |
| 91 | 21 | 27 | `\eta` | `Unresolved; no reliable alternative` | medium |
| 91 | 21 | 30 | `admettrons` | `démontrons` | medium |
| 91 | 21 | 31 | `\eta` | `\eta'` | medium |
| 91 | 22 | 9 | `X_0` | `Y_0` | medium |
| 91 | 22 | 15 | `th` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 17 | `S_0` | `S` | medium |
| 91 | 22 | 20 | `ne peut` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 22 | `les autres` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 23 | `on a dit` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 23 | `l'obstruction à relever étant` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 24 | `dans la question de relever` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 25 | `étant indépendante` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 27 | `de la question` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 28 | `de savoir` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 29 | `la possibilité de` | `Unresolved; no reliable alternative` | medium |
| 91 | 22 | 31 | `I` | `\mathcal{I}` | medium |
| 91 | 23 | 3 | `noeth.` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 3 | `qcoh.` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 4 | `\varphi` | `v` | medium |
| 91 | 23 | 8 | `\varphi_0` | `v_0` | medium |
| 91 | 23 | 8 | `\longrightarrow` | `\text{—}` | medium |
| 91 | 23 | 13 | `situation déduite` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 15 | `donc l'obstruction à relever` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 20 | `I` | `\mathcal{I}` | medium |
| 91 | 23 | 23 | `$E'$` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 25 | `I` | `\mathcal{I}` | medium |
| 91 | 23 | 32 | `I` | `\mathcal{I}` | medium |
| 91 | 23 | 33 | `I` | `\mathcal{I}` | medium |
| 91 | 23 | 36 | `P'_4` | `P'_0` | medium |
| 91 | 23 | 36 | `P_4` | `P_0` | medium |
| 91 | 23 | 36 | `en` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 36 | `avec` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 38 | `\}` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 39 | `Considérons, puis on` | `Unresolved; no reliable alternative` | medium |
| 91 | 23 | 41 | `Ce qui dérive` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 4 | `q_*` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 4 | `\Gamma_0` | `P_0` | medium |
| 91 | 24 | 5 | `q'_*` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 5 | `\Gamma'_0` | `P'_0` | medium |
| 91 | 24 | 19 | `\lambda` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 27 | `\pi` | `\pi'` | medium |
| 91 | 24 | 32 | `Il` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 38 | `K` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 41 | `condition définie pour l'existence de` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 46 | `s'annule` | `Unresolved; no reliable alternative` | medium |
| 91 | 24 | 46 | `$R_2=$` | `Unresolved; no reliable alternative` | medium |
| 91 | 25 | 5 | `\alpha` | `Unresolved; no reliable alternative` | medium |
| 91 | 25 | 25 | `7^\circ` | `1^\circ` | medium |
| 91 | 25 | 25 | `8^\circ` | `2^\circ` | medium |
| 91 | 25 | 35 | `algébrique` | `Unresolved; no reliable alternative` | medium |
| 91 | 25 | 40 | `Il` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 3 | `à 7` | `est` | medium |
| 91 | 26 | 3 | `contenus` | `contenu` | medium |
| 91 | 26 | 7 | `loc. noeth.` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 13 | `radiciel` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 13 | `ou` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 25 | `séparé` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 27 | `Il suit que` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 29 | `un entier` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 29 | `n` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 32 | `\operatorname{Hom}` | `Unresolved; no reliable alternative` | medium |
| 91 | 26 | 37 | `quasi-proj.` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 2 | `X/k` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 4 | `pour` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 4 | `les différents` | `les définitions` | low |
| 91 | 27 | 4 | `néc.` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 4 | `sép.` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | `différent du` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | `précédent ?` | `Unresolved; no reliable alternative` | low |
| 91 | 27 | 5 | `car les` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | `sont les mêmes` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | `l'un` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | `pt de` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | `P` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 7 | `un schéma` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 7 | `irrédundant` | `irréductible` | medium |
| 91 | 27 | 10 | `Attention à la quasi-compacité` | `Unresolved; no reliable alternative` | low |
| 91 | 27 | 10 | `lorsqu'on` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 10 | `diff. exemples` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 12 | `plat` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 12 | `Ceci` | `Ainsi` | medium |
| 91 | 27 | 12 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 14 | `\longrightarrow` | `\text{—}` | medium |
| 91 | 27 | 14 | `\eta(k(U))` | `\eta(U)` | medium |
| 91 | 27 | 15 | `de type fini` | `Unresolved; no reliable alternative` | medium |
| 91 | 27 | 5 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 27 | 5 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 27 | 5 | Physically unreadable span (1 estimated words) | — | low |
| 91 | 27 | 10 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 27 | 15 | Physically unreadable span (1 estimated words) | — | low |
| 91 | 28 | 2 | `est` | `Unresolved; no reliable alternative` | medium |
| 91 | 28 | 2 | `l.f.f.` | `Unresolved; no reliable alternative` | medium |
| 91 | 28 | 2 | `séparé` | `Unresolved; no reliable alternative` | medium |
| 91 | 28 | 4 | `l.f.f.` | `l.f.t.` | medium |
| 91 | 28 | 6 | `Remplaçant` | `Remplaçons` | medium |
| 91 | 28 | 6 | `fpqf` | `Unresolved; no reliable alternative` | medium |
| 91 | 28 | 8 | `\underline{\operatorname{Isom}}` | `Unresolved; no reliable alternative` | medium |
| 91 | 29 | 2 | `plat` | `Unresolved; no reliable alternative` | medium |
| 91 | 29 | 2 | `étale` | `Unresolved; no reliable alternative` | medium |
| 91 | 29 | 2 | `\longrightarrow` | `\text{—}` | medium |
| 91 | 29 | 2 | `plat` | `Unresolved; no reliable alternative` | medium |
| 91 | 31 | 14 | `X` | `Unresolved; no reliable alternative` | medium |
| 91 | 31 | 20 | `onem` | `one` | medium |
| 91 | 31 | 20 | `functorz` | `functors` | medium |
| 91 | 31 | 20 | `Z_i` | `Unresolved; no reliable alternative` | medium |
| 91 | 31 | 20 | `subshhemes` | `subschemes` | medium |
| 91 | 32 | 2 | `aby` | `any` | medium |
| 91 | 32 | 2 | `Matsumurds` | `Matsumura's` | medium |
| 91 | 32 | 2 | `descebt` | `descent` | medium |
| 91 | 32 | 4 | `geométric` | `geometric` | medium |
| 91 | 32 | 4 | `sectionx` | `section` | medium |
| 91 | 32 | 6 | `gix` | `fix` | medium |
| 91 | 32 | 6 | `onesx` | `ones` | medium |
| 91 | 32 | 8 | `,` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 2 | `F` | `E` | medium |
| 91 | 34 | 4 | `\mathcal R` | `\mathcal G` | medium |
| 91 | 34 | 6 | `Foncteurs de Greenberg` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 6 | `Serre-Lang` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 8 | `W^\circ(t)` | `W(t)` | medium |
| 91 | 34 | 12 | `fibrés` | `plats` | medium |
| 91 | 34 | 16 | `7` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 16 | `App` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 16 | `\mathcal R` | `\mathcal G` | medium |
| 91 | 34 | 16 | `\longrightarrow` | `\text{—}` | medium |
| 91 | 34 | 17 | `reporter à la fin` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 20 | `8` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 22 | `8` | `Unresolved; no reliable alternative` | medium |
| 91 | 34 | 22 | `\nu(s)` | `v(s)` | medium |
| 91 | 34 | 24 | `des` | `du` | medium |
| 91 | 35 | 22 | `immersité` | `immersivité` | medium |
| 91 | 35 | 27 | `absolument` | `de dimension 3` | medium |
| 91 | 35 | 27 | `$L$` | `Unresolved; no reliable alternative` | medium |
| 91 | 35 | 27 | `\bar L` | `L` | medium |
| 91 | 35 | 29 | `\bar L` | `L` | medium |
| 91 | 35 | 29 | `\longrightarrow` | `\text{—}` | medium |
| 91 | 36 | 2 | `constate` | `Unresolved; no reliable alternative` | medium |
| 91 | 36 | 2 | `L` | `K` | medium |
| 91 | 36 | 2 | `K` | `L` | medium |
| 91 | 36 | 2 | `sous $G$` | `Unresolved; no reliable alternative` | medium |
| 91 | 36 | 3 | `ce raisonnement` | `Unresolved; no reliable alternative` | medium |
| 91 | 36 | 7 | `L` | `Unresolved; no reliable alternative` | medium |
| 91 | 36 | 7 | `L` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 13 | `intervertir` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 18 | `Conditions de descente` | `Unresolved; no reliable alternative` | low |
| 91 | 37 | 18 | `d'une famille` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 18 | `de schémas` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 18 | `projectifs ?` | `Unresolved; no reliable alternative` | low |
| 91 | 37 | 19 | `Les théorèmes` | `Les résultats` | low |
| 91 | 37 | 19 | `vus au` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 19 | `ne sont pas utilisés au` | `Unresolved; no reliable alternative` | low |
| 91 | 37 | 19 | `7` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 20 | `1` | `5` | medium |
| 91 | 37 | 22 | `technique` | `théorie` | medium |
| 91 | 37 | 24 | `géom. injectif` | `géom. projectif` | low |
| 91 | 37 | 26 | `\check V(\underline F)` | `\check V(\mathcal F)` | low |
| 91 | 37 | 27 | `Propriétés diverses de permanence` | `Unresolved; no reliable alternative` | low |
| 91 | 37 | 31 | `Hyperproblèmes` | `Hyperschémas` | medium |
| 91 | 37 | 34 | `ce qui suit` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 34 | `f_*` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 34 | `entièrement` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 34 | `obligerait` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 34 | `longuement` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 36 | `4` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 36 | `Cas particuliers` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 40 | `2` | `Unresolved; no reliable alternative` | medium |
| 91 | 37 | 43 | `ensemble ?` | `Unresolved; no reliable alternative` | low |
| 91 | 38 | 2 | `\mathcal F` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 2 | `O` | `\mathcal O` | medium |
| 91 | 39 | 11 | `on` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 11 | `grand` | `petit` | medium |
| 91 | 39 | 11 | `F'` | `F` | medium |
| 91 | 39 | 18 | `forment` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 18 | `une famille filtrante décroissante` | `Unresolved; no reliable alternative` | low |
| 91 | 39 | 18 | `f^*(F_i)` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 18 | `complet` | `surjectif` | medium |
| 91 | 39 | 19 | `on sait même que` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 20 | `f^*(F_i)` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 20 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 25 | `pour un` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 25 | `O` | `\mathcal O` | medium |
| 91 | 39 | 25 | `définition` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 25 | `en vrai sens` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 25 | `\bigcap_iF_i` | `Unresolved; no reliable alternative` | medium |
| 91 | 39 | 25 | `l'inf dans les faisceaux qu. coh.` | `Unresolved; no reliable alternative` | low |
| 91 | 39 | 26 | `ss les` | `sous les` | medium |
| 91 | 39 | 27 | `Arranger les notations` | `Unresolved; no reliable alternative` | low |
| 91 | 40 | 6 | `S'` | `Z'` | medium |
| 91 | 40 | 14 | `affine relatif` | `affine` | medium |
| 91 | 40 | 14 | `famille d'ouverts donnée` | `famille donnée` | medium |
| 91 | 40 | 14 | `f_i=f(U_i)` | `f_i=f\vert U_i` | medium |
| 91 | 40 | 16 | `de la finité` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 22 | `on` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 22 | `tout` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 22 | `$\exists i:\ \in f_{i*}(U_i/T)$` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 23 | `faites dans le` | `posées dans le` | medium |
| 91 | 40 | 23 | `---` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 25 | `remplace` | `complète` | medium |
| 91 | 40 | 26 | `quelconque` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 26 | `relatif` | `Unresolved; no reliable alternative` | medium |
| 91 | 40 | 23 | Physically unreadable span (1 estimated words) | — | low |
| 91 | 41 | 3 | `considère` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 3 | `se trouvent vérifiées` | `se vérifient` | low |
| 91 | 41 | 3 | `les` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 8 | `\text{induit }\forall i` | `\text{induit par}` | low |
| 91 | 41 | 9 | `H=` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 10 | `pour $H_i$ est le plus gd ss-ouv de $H$` | `que $H_i$ est le plus gd ss-ouv de $H$` | low |
| 91 | 41 | 10 | `contenu` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 10 | `dont l'image` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 10 | `\xi_i^{-1}` | `\xi_i\to1` | medium |
| 91 | 41 | 10 | `ouvert en` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 10 | `est le` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 10 | `$\varphi^{-1}(U_i)$` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 10 | `de $\varphi$` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 11 | `H` | `S` | medium |
| 91 | 41 | 11 | `sur $S$` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 11 | `quelconque` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `\deleted{\unsure{Il y a} \uline{injection}, car si \deleted{\unsure{on a}} \inserted{deux} \deleted{\unsure{hom}} \deleted{\unsure{homomorphismes}} sections \deleted{$\unsure{S,S'}$} $u,v:S\longrightarrow H$ \deleted{$\unsure{S}\longrightarrow T$}, définissent le $=$ \deleted{\unsure{section}} \inserted{homomorph.} $T\longrightarrow X$, les images inverses $T_i$ par ce dernier \deleted{\unsure{des ouverts}} des $U_i$ \uline{recouvrent} $T$,}` | `Unresolved; no reliable alternative` | low |
| 91 | 41 | 16 | `Il y a` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `on a` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `hom` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `homomorphismes` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `S,S'` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `S` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `section` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 16 | `des ouverts` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 18 | `S` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 18 | `H` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 19 | `S\times T` | `Unresolved; no reliable alternative` | medium |
| 91 | 41 | 19 | `U_i` | `Unresolved; no reliable alternative` | medium |
| 91 | 42 | 4 | `strictement formel` | `Unresolved; no reliable alternative` | medium |
| 91 | 42 | 7 | `$\operatorname{Hom}$` | `Unresolved; no reliable alternative` | medium |
| 91 | 42 | 8 | `l'on ait dans` | `Unresolved; no reliable alternative` | medium |
| 91 | 42 | 8 | `géom. injectif` | `purement injectif` | medium |
| 91 | 42 | 9 | `t\in S` | `s\in S` | medium |
| 91 | 42 | 11 | `condition Hyp.` | `Unresolved; no reliable alternative` | medium |
| 91 | 42 | 11 | `enfin si tt partie` | `Unresolved; no reliable alternative` | medium |
| 91 | 43 | 3 | `ci-dessus` | `du th. précédent` | medium |
| 91 | 43 | 5 | `géométrt` | `géométriquement` | medium |
| 91 | 43 | 10 | `soit` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 7 | `*` | `+` | medium |
| 91 | 44 | 10 | `donner un énoncé` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 10 | `dans le cas` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 10 | `$f$ étale` | `$f$ fidèle` | low |
| 91 | 44 | 12 | `vérifie que le produit` | `Unresolved; no reliable alternative` | low |
| 91 | 44 | 16 | `fermées` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 16 | `l'on a une hyp. qui assure` | `Unresolved; no reliable alternative` | low |
| 91 | 44 | 16 | `pourvu que` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 16 | `finies` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 20 | `Les` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 20 | `autres assertions` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 21 | `déduite` | `établie` | medium |
| 91 | 44 | 22 | `que le $=$ visé est même : à vérifier;` | `Unresolved; no reliable alternative` | low |
| 91 | 44 | 25 | `(1)` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 26 | `faire détail dans le cas actuel` | `Unresolved; no reliable alternative` | low |
| 91 | 44 | 28 | `préciser par descente` | `Unresolved; no reliable alternative` | low |
| 91 | 44 | 29 | `noeth.` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 30 | `X/S` | `Y/S` | medium |
| 91 | 44 | 32 | `applications` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 32 | `\otimes_T` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 32 | `\subset X` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 32 | `X\supset Y\otimes_T Z` | `X=Y\otimes_T Z` | low |
| 91 | 44 | 34 | `si on $X_T\longrightarrow Y/T$` | `Unresolved; no reliable alternative` | low |
| 91 | 44 | 34 | `du` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 34 | `Il vaut` | `Unresolved; no reliable alternative` | medium |
| 91 | 44 | 26 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 44 | 28 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 45 | 3 | `rel. ample` | `très ample` | low |
| 91 | 45 | 3 | `etc` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 9 | `est un caractère` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 9 | `(1)` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 9 | `est ramené` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 9 | `que ce résultat` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 9 | `P` | `\mathbf P` | medium |
| 91 | 45 | 9 | `P` | `\mathbf P` | medium |
| 91 | 45 | 9 | `ce qui est` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 9 | `produits` | `chg. de base` | low |
| 91 | 45 | 11 | `Sur le réseau plat` | `Sur le réseau fidèle` | low |
| 91 | 45 | 14 | `f_*(U/T)\longrightarrow f_*(X/T)` | `Unresolved; no reliable alternative` | low |
| 91 | 45 | 16 | `Rien de si simple` | `Rien de plus simple` | low |
| 91 | 45 | 16 | `n'est pas de` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 16 | `pourquoi` | `prouver` | medium |
| 91 | 45 | 16 | `les puissances` | `que le faisceau` | low |
| 91 | 45 | 16 | `constitue l'imm. projective` | `Unresolved; no reliable alternative` | low |
| 91 | 45 | 16 | `on trouve les` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 16 | `sections` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 16 | `en nombre` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 16 | `fini` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 16 | `On le prouve pour` | `Donc pour` | low |
| 91 | 45 | 16 | `(quasi-cohérent)` | `Unresolved; no reliable alternative` | medium |
| 91 | 45 | 18 | `en` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 3 | `alg.` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 3 | `alg.` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 4 | `non` | `sur` | medium |
| 91 | 46 | 4 | `B` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 4 | `F'_1/\uline{F}'` | `\uline{F}'/F'_1` | medium |
| 91 | 46 | 4 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 6 | `\uline{E}=\uline{A}^n` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 14 | `b'_i` | `Unresolved; no reliable alternative` | medium |
| 91 | 46 | 14 | `1\leq i\leq(n-k)d` | `1\leq\gamma\leq(n-k)d` | medium |
| 91 | 46 | 16 | `la` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 5 | `que` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 5 | `A` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 15 | `F_1/F` | `M=B^k` | medium |
| 91 | 47 | 15 | `n` | `k` | medium |
| 91 | 47 | 16 | `des` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 16 | `éléments` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 16 | `soit` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 16 | `un` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 16 | `par` | `Unresolved; no reliable alternative` | medium |
| 91 | 47 | 17 | `préciser un th., en complétant` | `préciser un peu, en complétant` | medium |
| 91 | 47 | 17 | `tenant compte des conditions de validité encore` | `tenant compte des conditions de validation encore` | low |
| 91 | 47 | 3 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 48 | 3 | `reste` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 5 | `réserves` | `conditions` | medium |
| 91 | 48 | 7 | `toute` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 7 | `aff.` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 8 | `Prouvons` | `Prenons` | medium |
| 91 | 48 | 8 | `X` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 10 | `X^\nu` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 10 | `-` | `\cdots` | medium |
| 91 | 48 | 14 | `-` | `\cdots` | medium |
| 91 | 48 | 16 | `Pour voir` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 16 | `quasi` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 20 | `(X_s)^\nu` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 20 | `pris dans un même ouvert affine` | `Unresolved; no reliable alternative` | medium |
| 91 | 48 | 21 | `rédiger convenablement` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 3 | `or implique` | `or ceci implique` | medium |
| 91 | 49 | 3 | `O.K.` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 5 | `\operatorname{Spec}` | `\operatorname{Sym}` | medium |
| 91 | 49 | 5 | `\uline F` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 7 | `\operatorname{Spec}` | `\operatorname{Sym}` | medium |
| 91 | 49 | 7 | `\check F` | `\uline F` | medium |
| 91 | 49 | 10 | `Corollaire` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 10 | `f_*` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 10 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 12 | `f_*` | `f^*` | medium |
| 91 | 49 | 12 | `\nu` | `d` | medium |
| 91 | 49 | 12 | `f_*` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 13 | `\varepsilon^2` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 13 | `d` | `Unresolved; no reliable alternative` | medium |
| 91 | 49 | 13 | `A` | `k` | medium |
| 91 | 49 | 14 | `voir précisé` | `voir préciser` | medium |
| 91 | 50 | 19 | `fini et plat` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 19 | `pas néc. fini\ldots` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 23 | `que` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 23 | `\longrightarrow` | `,` | medium |
| 91 | 50 | 25 | `Supposons` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 25 | `affine` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 31 | `fini` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 33 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 33 | `S'` | `S'_1` | medium |
| 91 | 50 | 36 | `étant` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 36 | `réduit` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 36 | `par` | `Unresolved; no reliable alternative` | medium |
| 91 | 50 | 36 | Physically unreadable span (1 estimated words) | — | low |
| 91 | 51 | 3 | `car` | `Unresolved; no reliable alternative` | medium |
| 91 | 51 | 3 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 51 | 3 | `uniformément` | `Unresolved; no reliable alternative` | medium |
| 91 | 51 | 3 | `uniformes` | `Unresolved; no reliable alternative` | medium |
| 91 | 51 | 4 | `donner une` | `donner un` | medium |
| 91 | 51 | 4 | `condition` | `contre-ex.` | medium |
| 91 | 51 | 4 | `de fin.` | `non fini` | medium |
| 91 | 51 | 8 | `les` | `où` | medium |
| 91 | 51 | 8 | `désignent` | `désigne` | medium |
| 91 | 51 | 9 | `trouve` | `aura` | medium |
| 91 | 51 | 11 | `resp.` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 5 | `Corollaire 2` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 7 | `$T/S$ fini` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 8 | `Soit` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 14 | `\leq` | `=` | medium |
| 91 | 52 | 16 | `géom.` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 16 | `égales à $\nu$` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 16 | `et` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 16 | `f` | `g` | medium |
| 91 | 52 | 16 | `tt. leurs pts` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 16 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 19 | `f. plat` | `plat` | medium |
| 91 | 52 | 21 | `donc` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 21 | `de` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 23 | `alors` | `Unresolved; no reliable alternative` | medium |
| 91 | 52 | 7 | Physically unreadable span (2 estimated words) | — | low |
| 91 | 53 | 7 | `un` | `Unresolved; no reliable alternative` | medium |
| 91 | 53 | 8 | `g_2` | `Unresolved; no reliable alternative` | medium |
| 91 | 53 | 8 | `Y'` | `Y` | medium |
| 91 | 53 | 11 | `D'` | `Unresolved; no reliable alternative` | medium |
| 91 | 53 | 11 | `g_2` | `g_1` | medium |
| 91 | 53 | 11 | `et` | `Unresolved; no reliable alternative` | medium |
| 91 | 53 | 12 | `g_2` | `g_1` | medium |
| 91 | 53 | 14 | `Z` | `T` | medium |
| 91 | 53 | 16 | `où` | `Unresolved; no reliable alternative` | medium |
| 91 | 53 | 16 | `Z` | `2` | medium |
| 91 | 54 | 13 | `X_s` | `Y_s` | medium |
| 91 | 54 | 13 | `k` | `Unresolved; no reliable alternative` | medium |
| 91 | 54 | 16 | `f` | `Unresolved; no reliable alternative` | medium |
| 91 | 54 | 16 | `d` | `Unresolved; no reliable alternative` | medium |
| 91 | 54 | 17 | `n` | `Unresolved; no reliable alternative` | medium |
| 91 | 54 | 20 | `bloquer` | `Unresolved; no reliable alternative` | medium |
| 91 | 54 | 20 | `3` | `bis` | medium |
| 91 | 54 | 22 | `fini ét.` | `étale` | medium |
| 91 | 54 | 22 | `un $=$ de gr.` | `un de gr.` | medium |
| 91 | 54 | 24 | `on déduit par le principe` | `Unresolved; no reliable alternative` | medium |
| 91 | 54 | 32 | `est` | `Unresolved; no reliable alternative` | medium |
| 91 | 55 | 3 | `f` | `Unresolved; no reliable alternative` | medium |
| 91 | 55 | 3 | `puis sur les définitions` | `Unresolved; no reliable alternative` | low |
| 91 | 55 | 6 | `X,Y,T,S` | `Unresolved; no reliable alternative` | medium |
| 91 | 55 | 8 | `f` | `Unresolved; no reliable alternative` | medium |
| 91 | 55 | 8 | `soit` | `sur` | medium |
| 91 | 55 | 10 | `faibles` | `faiblement` | medium |
| 91 | 55 | 10 | `faibles` | `faiblement` | medium |
| 91 | 55 | 11 | `Première assertion` | `Unresolved; no reliable alternative` | low |
| 91 | 55 | 11 | `conséquence triviale des définitions` | `Unresolved; no reliable alternative` | low |
| 91 | 55 | 13 | `fini` | `Unresolved; no reliable alternative` | low |
| 91 | 55 | 13 | `simples` | `simple` | low |
| 91 | 55 | 13 | `pour` | `Unresolved; no reliable alternative` | low |
| 91 | 55 | 13 | `des` | `Unresolved; no reliable alternative` | low |
| 91 | 55 | 8 | Physically unreadable span (1 estimated words) | — | low |
| 91 | 55 | 13 | Physically unreadable span (1 estimated words) | — | low |
| 91 | 56 | 5 | `revêtem.` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 5 | `lisse` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 5 | `G\times_S` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 6 | `Dans le résumé` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 6 | `supposera` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 6 | `bien que` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 6 | `si on sait que la démonstration est générale` | `Unresolved; no reliable alternative` | low |
| 91 | 56 | 8 | `non vide` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 8 | `un` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 8 | `étant` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 11 | `qui` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 12 | `exact` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 13 | `prendre pour` | `Unresolved; no reliable alternative` | medium |
| 91 | 56 | 13 | `principe` | `Unresolved; no reliable alternative` | medium |
| 91 | 57 | 5 | `fini de $T$ sur $S$` | `Unresolved; no reliable alternative` | low |
| 91 | 57 | 5 | `noté` | `Unresolved; no reliable alternative` | medium |
| 91 | 57 | 6 | `ou` | `Unresolved; no reliable alternative` | medium |
| 91 | 57 | 6 | `f_\alpha^{\mathrm{ét}}` | `f_*^{\mathrm{ét}}` | medium |
| 91 | 57 | 10 | `élt` | `élémt` | medium |
| 91 | 57 | 10 | `T` | `\bar T` | medium |
| 91 | 57 | 14 | `l'on désirait un` | `Unresolved; no reliable alternative` | medium |
| 91 | 57 | 17 | `inutile?` | `Unresolved; no reliable alternative` | low |
| 91 | 57 | 17 | `raisonner directement` | `Unresolved; no reliable alternative` | low |
| 91 | 57 | 18 | `Un th. gén.` | `Alors la` | low |
| 91 | 58 | 3 | `\mapsto` | `\to` | medium |
| 91 | 58 | 3 | `et elle` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 3 | `a` | `c` | medium |
| 91 | 58 | 3 | `donne naissance` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 3 | `le` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 3 | `associée` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 4 | `essayer de coiffer par` | `Unresolved; no reliable alternative` | low |
| 91 | 58 | 4 | `compatibilité` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 4 | `résulte` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 4 | `si on considère` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 4 | `des ens.` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 7 | `f_*` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 11 | `du` | `des` | medium |
| 91 | 58 | 11 | `mbs` | `mb` | medium |
| 91 | 58 | 12 | `les sections` | `Unresolved; no reliable alternative` | medium |
| 91 | 58 | 12 | `les deux foncteurs` | `Unresolved; no reliable alternative` | low |
| 91 | 58 | 14 | `f_\alpha^{\mathrm{ét}}` | `f_*^{\mathrm{ét}}` | medium |
| 91 | 58 | 16 | `f_\alpha^{\mathrm{ét}}` | `f_*^{\mathrm{ét}}` | medium |
| 91 | 58 | 16 | `on tire` | `on trouve` | medium |

# Abbreviations

Expansions are editorial suggestions, in French where appropriate; they do not alter the transcription. Punctuation variants are grouped here only. A doubtful abbreviation remains doubtful even when a likely expansion is available.

| Abbreviation or shorthand encountered | Possible expansion / meaning |
|---|---|
| aff. | affine |
| alg., alg. clos | algébrique; algébriquement clos |
| Ass | associated points / points associés |
| Aut | automorphismes |
| can. | canonique |
| cf. | confer / compare |
| Ch. | chapitre |
| chgt, chg. | changement |
| coh. | cohérent |
| comp. | composantes |
| cond. | condition(s) |
| Cor., cor. | corollaire |
| Coker | conoyau |
| décr. | décroissant(s) |
| déf., définit. | définition / définitive, depending on the local phrase; the tiny marginal reading is uncertain |
| Dém | démonstration |
| det | déterminant |
| deg | degré |
| diff. | différents; not expanded where the cancelled phrase is unclear |
| dim, dim. | dimension |
| ens, ens., Ens | ensemble(s) |
| ess. | essentiellement |
| ét., ét | étale(s) |
| etc. | et cetera; present only when written |
| ex., Ex | exemple |
| ext. | extension |
| Ext | extension groups / derived Hom functor |
| f. et s. | faut et suffit |
| f. plat | possibly fidèlement plat; the f. itself is uncertain on052 |
| fid plt | fidèlement plat |
| fin. | finitude / fini, according to the uncertain margin051 |
| fpqc | fidèlement plat quasi-compact |
| fpqf | fidèlement plat quasi-fini; the manuscript supplies “fid plt quasi fini” on028 |
| gd | grand |
| gén. | général / généralement |
| géom., géométrt | géométrique / géométriquement; abbreviated ending on043 uncertain |
| gr. | degré in the margin054; not silently expanded in the text |
| hom, hom., Hom | homomorphisme(s) |
| homomorph. | homomorphisme |
| hyp., Hyp. | hypothèse(s) |
| i.e. | id est / c'est-à-dire |
| imm. | immersion |
| Im | image |
| Isom | isomorphismes |
| isom, isom. | isomorphisme |
| Ker | noyau |
| l.f.f. / l.f.t. | Possibly a rapid form for localement de présentation finie / localement de type fini; the letters on028 are not secure, and no definitive expansion is asserted. |
| loc, loc. | localement |
| mb, mbs | membre(s), in a formula |
| nb, Nb | nombre |
| N.B. | nota bene |
| néc. | nécessaire / nécessairement |
| noeth, noeth. | noethérien(ne) |
| OK, O.K. | okay / agreement mark |
| p., ex. (in p. ex.) | par exemple |
| P., Pb, pb | problème; P. in a cancelled heading is uncertain |
| pr. (in qu. pr.) | projectif / projective |
| pr₁, pr₂ | projections |
| prés. | présentation |
| préschém. | préschéma |
| proj. | projectif / projective |
| Prop., prop. | proposition |
| pt, pt., pts | point(s) |
| qcoh., qu. coh. | quasi-cohérent |
| qu., qu. proj., quasiproj. | quasi; quasi-projectif |
| quelc | quelconque |
| rel. | relativement / relatif |
| repr. | représentable / représenté |
| resp. | respectivement |
| rev., revêtem., Rev | revêtement(s) |
| SGA | Séminaire de géométrie algébrique; the manuscript reference on023 is “SGA3 III4.2” |
| Spec | spectre |
| ss, ss-faisceau, ss-schéma, ss-ouv | sous, sous-faisceau, sous-schéma, sous-ouvert |
| sss | si et seulement si |
| suffis. | suffisante |
| surj | surjectif |
| th. | théorème |
| top, top. | topologie |
| tq, t.q. | tel que |
| tt, tt., ttes | tout / tous / toutes, with the written agreement retained |
| élt / élémt | élément; competing abbreviation readings on057 |
| = used within prose | Probably the ditto shorthand for même(s); the actual sign is retained. |


# Legibility and reliability

The transcription is a personal visual reading of all38 whole scans and both supplied halves, without OCR or delegated reading. All38 pages received a separately logged second visual audit before the context archive was opened. The typed letter031–032 is substantially clearer than the rapid handwriting, although overtyping and apparent spelling errors remain marked rather than corrected; faint reverse-side show-through was distinguished from foreground writing.

The least secure passages are the minute margins on019 and027; the heavily revised outline037; the intersection notes039; the crowded construction and uncertain cancellation041; the descent/ampleness margins044–045; the cancelled dimension discussion052; the clipped last line055; and the compressed annotations and abandoned drafts056–058. Several multiword tentative readings there are low confidence even if a recognizable mathematical interpretation exists. The short superscripts, overwritten field letters, local rank indices, Gamma/P, script/plain I and O, and the looped f-subscript057–058 also remain vulnerable.

The doubt register reproduces every in-place uncertainty and illegibility mark, including nested and repeated marks. Confidence describes the visual reading, not the truth of a mathematical assertion. “Medium” means a plausible visual candidate with unresolved strokes; “low” covers long compressed/cancelled readings, explicit unreadable spans, and the specially difficult marginal passages. No confidence rating certifies unmarked surrounding words. The one-word unreadable span at the foot of055 and other illegible cancellations were inspected at additional magnification after attempted readings.

Diagrams retain their written direction, partial objects and cancellation state; enclosures and nonverbal marks have TikZ approximations. The supplied fragment has no preamble or macro definitions. Mechanical checks cover page order, concatenation, markers, inventory, braces, delimiters and environments; a full LaTeX render was not available because this environment lacks the LaTeX class/format and TikZ packages. Thus typography, especially nested diagram/callout placement, has not been render-verified.

Several apparent mathematical inconsistencies are intentionally preserved, including028's product ordering,046's doubtful quotient ordering,052's displayed dimension relation, and053's disputed étale-map subscript. Any interpretation suggested by the later context belongs only in the research notes. The transcription hashes are the boundary between the visual work and that later research.
