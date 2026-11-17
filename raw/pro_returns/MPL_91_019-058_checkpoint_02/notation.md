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
