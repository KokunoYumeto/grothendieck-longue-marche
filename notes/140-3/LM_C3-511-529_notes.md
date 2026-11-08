# LM_C3-511-529 — Editorial and research notes

## Scope, numbering, and transcription conventions

These notes accompany the diplomatic French LaTeX fragment for the 19 supplied scan files, 511–529. The filenames govern `\scanpage`; they are one greater than the archive footer numeration. Both upper and lower handwritten page numbers are retained with `\mspage` wherever visible. The typeset archive imprint and URL beneath each manuscript image are not part of the handwritten transcription. The primary source is the supplied manuscript, not an external transcription (Grothendieck, 1981).

| Scan | Handwritten page numbers visible, in page order |
|---|---|
| 511 | 558; 510 |
| 512 | 559; 511 |
| 513 | 512 |
| 514 | 560; 513 |
| 515 | 514 |
| 516 | 561; 515 |
| 517 | 516 |
| 518 | 562; 517 |
| 519 | 518 |
| 520 | 563; 519 |
| 521 | 520 |
| 522 | 564; 521 |
| 523 | 522 |
| 524 | 565; 523 |
| 525 | 524 |
| 526 | 566; 525 |
| 527 | 526 |
| 528 | 567; 527 |
| 529 | 528 |

The broad doubled-contour ambient letter is represented by `\mathcal{G}`; the narrower long-descender solution-set letter is represented by `\mathscr{G}`, with doubtful alphabet readings marked. Plain `G` remains distinct. Overwritten T/Gamma-like symbols retain explicit alternatives. No expected group-theoretic identity was used to replace a visible index, arrow direction, prime, hat, word, or repeated equation number.

The transcription is a fragment: it contains no preamble, document class, or editorial-macro definitions. A host document must define the requested editorial macros. Mathematical typesetting uses standard LaTeX facilities from `amsmath`, `amssymb`, `mathrsfs`, `graphicx`, and `tikz-cd`; diagrams use an explicit ampersand replacement so that they remain valid inside the required `\diagram{…}` argument. Standard mathematical underlines distinguish underlined variables, while `\uline` and `\uuline` record textual emphasis.

## 1. Table of doubts

The contextual table gives approximate manuscript lines, display numbers, or margin anchors. Repeated instances of a single reading are sometimes grouped. A dash in the alternatives column means that no defensible second reading was obtained; it does not indicate certainty. Confidence is a qualitative reading judgment, not a probability.

| Scan | Approximate manuscript line / location | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 511 | 1, 7, 10, 21, 23–25; (40), (42), (43), (46), (47), NB | `\mathcal{T}` | `\Gamma`; these signs have been densely overwritten | low |
| 511 | 3, after «sur» | `S\mathcal{T}'` | `S\Gamma'`; exponent appears prime here, not the revised zero | medium |
| 511 | margin beside (42) | «noté» | «not» | low |
| 511 | margin beside (42), final reference | «II», `#` | Roman numeral or revision sign unclear | low |
| 511 | 8, reference before «induit» | (38) | (39) | medium |
| 511 | after (43), deleted formula | `\simeq Z_\rho\times Z_\sigma` | overstruck final factor not securely readable | low |
| 511 | (44), ambient-group alphabet | `\mathcal{G}` | ornamental capital G; exact typographic alphabet uncertain | medium |
| 511 | (44), second line | `SZ_\rho`, `Z_\rho`, `\Gamma_{\rho,2}` | corresponding indices may be `\sigma`; retained rather than corrected by symmetry | low |
| 511 | (45), first line | `\Gamma_{\rho\sigma}` | comma between indices possibly absent | medium |
| 511 | (47), deleted initial glyph | `S` | dense overwritten capital or initial prefix | low |
| 511 | NB, after `S_0\mathcal{T}_{\rho,\sigma}^0` | superscript 4 | #; revision mark | low |
| 511 | NB, final reference | II | 11; numeral underlined | medium |
| 511 | NB, deleted word before «les» | physically unreadable one-word blot | no reliable reading after magnification | low |
| 511 | 4 and (43), long-descender solution-set alphabet | `\mathscr{G}` | `\mathcal{G}`; distinct handwriting from the ornate ambient G | medium |
| 512 | (49), superscript after zero | # | * | low |
| 512 | (49), revised group symbol | `\mathcal{T}` | `\Gamma` | low |
| 512 | (49), inside parenthesis | subset sign | equals sign | medium |
| 512 | (51), deleted start of target | `(u` | a partially overwritten preliminary coordinate | low |
| 512 | line after the projection diagrams | «redonnant» | ending indistinct; no secure second reading | medium |
| 513 | line 1, deleted short word | «de» | unidentified short overwritten word | low |
| 513 | line 3, before `S_0M` | open parenthesis | heavily retraced initial mark | low |
| 513 | underbraces in (56), repeated (49) | `\mathcal{T}` | `\Gamma` | low |
| 513 | (57), initial deleted symbol | `\Gamma_\rho` | `T_\rho` | low |
| 513 | (57), ornate group alphabet | `\mathcal{G}` | exact letter alphabet uncertain; chosen distinct from the long-descender solution-set symbol | medium |
| 513 | (57), middle group | `M'` | `M^0` | low |
| 513 | (57), label on arrow | `\delta_M^#` | `\delta_M^*` | low |
| 513 | line after (57), deleted word | «posé» | no second reliable reading | medium |
| 513 | deleted display number below (57) | (48) | (58) | low |
| 513 | centralizer display, two occurrences | underlined `Centr` with deleted `aut` below | the small deleted letters are fused; double underlining was an initial alternative | low |
| 513 | repeated (50), quotient letter | capital `\Gamma` | lower-case `\gamma` | medium |
| 514 | (52), ornate kernel letter | `\mathcal{G}` | exact alphabet uncertain | medium |
| 514 | (52), (53), revised quotient symbol | `\mathcal{T}` | `\Gamma` | low |
| 514 | left margin (53′), quotient | `G` | `G_1`; lower right stroke may belong to G itself | medium |
| 514 | line after (54) | «voit» | retraced short verb; no secure alternative | medium |
| 514 | line after (54), deleted next word | unreadable one-word deletion | no reliable reading after magnification | low |
| 514 | (55), solution-set alphabet | `\mathscr{G}` | `\mathcal{G}` | medium |
| 514 | (57), (58), cocycle symbol (three occurrences) | zeta | xi | medium |
| 514 | (58), after `f^{-1} alpha` | # | zeta; possibly a cancellation mark | low |
| 515 | (59), first cancelled factor | `int(alpha)` | underlying strokes heavily cancelled; no secure alternative | low |
| 515 | (59), second cancelled factor | `int(beta)` | underlying strokes heavily cancelled; long descender compatible with beta | low |
| 515 | (59), first cocycle glyph | zeta | xi | medium |
| 515 | short deleted line beneath (59) | «et», then `zeta,eta` and a stop | middle glyphs could be a different short formula; no recoverable prose reading | low |
| 515 | underlined heading | Remarque | Remarq.; terminal letters compressed | medium |
| 515 | after (20), tiny deleted letter | b | a short retraced mark rather than a letter | low |
| 515 | before «sauf», deleted short word | et | physically fused lettering; no secure alternative | low |
| 515 | (60), first member of each pair and first cocycle | zeta | xi | medium |
| 515 | (60), ambient factor after membership sign | ornate G | Sigma with rho subscript under the retracing | low |
| 515 | (60), second action expression | `u(sigma)` | `u sigma)`; opening parenthesis unclear | low |
| 515 | after (60), deleted wording before inserted Sigma | «les (5)» | short article may be «le»; final glyph may be an earlier Sigma rather than a 5 | low |
| 515 | after the inserted reference (cf (8)) | closing parenthesis | may belong to the cancelled earlier reference | low |
| 515 | cancelled application, reference above it; and (61) | (28) | (20); looped last digit favours 8 | medium |
| 515 | cancelled paragraph, after «son image» | est | sera | low |
| 515 | right of cancelled paragraph | puis; bij. | par; bis | low |
| 515 | cancelled application and all occurrences in (61) / last line | solution-set `mathscr G` | `mathcal G`; handwriting has the distinct long descender | medium |
| 516 | 1 | isomorphe | — | medium |
| 516 | 1, after isomorphe | à | : | low |
| 516 | (62), solution-set alphabet | \mathscr{G} | \mathcal{G} | medium |
| 516 | 1; (62) | \mathcal{T} | \Gamma | low |
| 516 | (64), arrow label, deleted | \varepsilon_2 | — | low |
| 516 | (64), codomain, deleted | \times\{\pm1\} | — | low |
| 516 | (64), congruence modulus | 3 | — | medium |
| 516 | (64), deleted modulus | 12 | — | low |
| 516 | below (64), deleted line | three unreadable words | — | low |
| 516 | below (64), deleted line | deux facteurs | — | low |
| 516 | after et soit, deleted | M_{0,3}^{\prime\sim} | — | low |
| 516 | (65) | Image inv. | Im. inv. | medium |
| 516 | (67) | \sigma_{\mathcal{G}} | overwritten letter resembling rho | medium |
| 517 | margin, first item | a) | — | medium |
| 517 | margin b, overwritten subscript | \mathcal{G} | — | low |
| 517 | margin b, first composition subscript | M | \mathcal{G} | low |
| 517 | margin, item before c prime | c) | b) | low |
| 517 | margin final lines, deleted | eff. | — | low |
| 517 | margin final lines | automatique | autom. | low |
| 517 | margin final lines, underlined | effectif | — | medium |
| 517 | 3, tuple, two occurrences | u | \psi | low |
| 517 | 4, before G | autom. | autom | medium |
| 517 | 5, deleted | u_{\mathcal{G}}\rho | — | low |
| 517 | 13, before u | tt | tout | medium |
| 517 | 16, deleted suffix | [0] | — | low |
| 517 | last line | le | — | medium |
| 518 | (71), deleted source prefix | S_0 | — | low |
| 518 | (71), deleted source superscript | * | — | low |
| 518 | (71), deleted target prefix | S_0 | — | low |
| 518 | deleted (72), upper arrow label | \varphi | i | low |
| 518 | deleted (72), deleted old top-right object | \mathcal{G} | — | low |
| 518 | deleted (72), deleted old bottom-left object | \mathcal{G} | — | low |
| 518 | left margin | bien sûr en | — | medium |
| 518 | 8, deleted | u\in | — | medium |
| 518 | 9, membership or equality sign | = | \in | low |
| 518 | 11, equation des lacets subscript | \ell_1 | \ell_0 | medium |
| 518 | 12, deleted old target | M_{\rho_{\mathcal{G}},\sigma_{\mathcal{G}}}^{0} | — | low |
| 518 | lower (72), right vertical label | \psi_{\mathcal{T}} | \psi_{\Gamma} | low |
| 518 | lower (72), lower-right quotient | \mathcal{T} | \Gamma | low |
| 519 | (73), targets | Z_rho, Z_sigma | T_rho, T_sigma | medium |
| 519 | 4, deleted symbol after Pour | u | — | low |
| 519 | deleted formula before (75), and (75) | T_rho, T_sigma | Gamma_rho, Gamma_sigma | medium |
| 519 | deleted formula before (75), second argument | y | dot x | low |
| 519 | deleted formula before (75), final expression | psi u | psi(x) | low |
| 519 | (75), deleted fragment | delta_G( | — | low |
| 519 | (77), mark above lower arrow | 1 | upward small arrow | low |
| 519 | (77), lower diagonal delta_G arrow | gamma → G | G → gamma | medium |
| 519 | (79), overwritten letter | M | — | low |
| 520 | upper-left margin, first words | Il aurait | — | medium |
| 520 | 10, overwritten homomorphism subscript | varphi_M | varphi_SM | low |
| 520 | 10, verb | passe | — | medium |
| 520 | 10, preposition after quotient | en | à | medium |
| 520 | (83), first target | Z_{rho,sigma} | Sigma_{rho,sigma} | medium |
| 520 | b, inserted then deleted phrase | sont induits par | sont définis par | low |
| 520 | (84), deleted word | uniquement | — | low |
| 520 | (84), small mark before revient | b | se | low |
| 520 | d, deleted verb | désignant | — | medium |
| 521 | 1–3 | `cela` | `elle` | medium |
| 521 | 1–3 | `\varphi_{S_0M}` | — | medium |
| 521 | 5–10 | `\varphi_{S_0M^0}` | — | low |
| 521 | 5–10 | `transforme` | — | low |
| 521 | 11–13; display (88) | `\mathcal G` | — | low |
| 521 | 11–13; display (88) | `M_0` | `M^0` | low |
| 521 | 14–20 | `th.` | — | medium |
| 521 | 14–20 | `mettant` | — | low |
| 521 | 14–20 | `vaut` | — | medium |
| 521 | left margin beside lines 16–19 | `suppl.` | — | low |
| 521 | 21 | `expliciter` | — | low |
| 521 | 23–25; display (90) | `0` | — | low |
| 521 | 23–25; display (90) | `\prime` | `0` | medium |
| 521 | 23–25; display (90) | `\prime` | `0` | medium |
| 521 | 23–25; display (90) | `0` | — | low |
| 521 | 23–25; display (90) | `0` | — | low |
| 521 | 23–25; display (90) | `\left(-\frac13\right)` | `\left(\frac13\right)` | low |
| 521 | 23–25; display (90) | `0` | — | low |
| 521 | 23–25; display (90) | `\prime` | `0` | medium |
| 522 | 1–2; display (91) | `(91)` | `(92)` | medium |
| 522 | 1–2; display (91) | `\simeq` | `=` | medium |
| 522 | 1–2; display (91) | `G_{\rho',\sigma'}=` | — | low |
| 522 | 1–2; display (91) | `G` | — | low |
| 522 | upper-left margin; (92) | `\Gamma` | `\mathcal T` | low |
| 522 | upper-left margin; (92) | `cf.` | — | low |
| 522 | 4–8 | `0` | — | low |
| 522 | left margin, alongside lines 4–10 | `Ceci m'avait été inspiré dans le cas` | — | low |
| 522 | left margin, alongside lines 4–10 | `couple modulaire` | — | low |
| 522 | left margin, alongside lines 4–10 | `qui ne résulte pas de` | — | low |
| 522 | left margin, alongside lines 4–10 | `mais dans ce cas` | — | low |
| 522 | 9–10; display (93) | `\Gamma_{\rho,\sigma}` | — | low |
| 522 | 9–10; display (93) | `*` | — | low |
| 522 | 16–17 | `expliciter` | — | medium |
| 522 | 19–29; display (94) | `\mathrm{Gl}(\widehat{\mathbb Z})/\mu_2(\mathbb Z)` | — | low |
| 522 | 21; G row of (94) | `G\,\mathbb Z\,B/\mu_2` | — | low |
| 522 | 22; Zρ row of (94) | `T_\rho` | `\mathcal T_\rho` | medium |
| 522 | 22; Zρ row of (94) | `voir le` | — | low |
| 522 | 22; Zρ row of (94) | `T_\rho` | — | low |
| 522 | 22; Zρ row of (94) | `avec notations du` | — | medium |
| 522 | 23–25; Zσ row of (94) | `\{t\sigma+u\mid t^2+u^2\in\widehat{\mathbb Z}^{*}\}/\pm1` | — | low |
| 522 | 23–25; Zσ row of (94) | `sous-groupe` | — | low |
| 522 | 27; M row of (94) | `est le` | — | low |
| 522 | 27; M row of (94) | `SM''_{\rho,\sigma}` | `SM'_{\rho,\sigma}` | low |
| 522 | 27; M row of (94) | `SM'_{\rho,\sigma}(\widehat{\mathbb Z})` | — | low |
| 522 | left margin, alongside lines 4–10 | `2 physically unreadable words` | — | low |
| 523 | 3; G row of (95) | `\}` | `)` | medium |
| 523 | 10; S₀Γ row of (95) | `S_0\mathcal T'_{\rho,\sigma}` | `S\mathcal T'_{\rho,\sigma}` | medium |
| 523 | 13; cancelled section III | `M_{\rho,\sigma}` | `M_\rho` | low |
| 523 | 15–17; cancelled display (1) | `d'image` | — | low |
| 523 | 15–17; cancelled display (1) | `L_0^{\mathcal G}` | — | low |
| 523 | 18–19 | `le` | — | low |
| 523 | 18–19 | `l'image` | — | low |
| 523 | 18–19 | `se factorise` | — | low |
| 523 | 18–19 | `sur un` | — | low |
| 523 | 20; cancelled display (2) | `*` | — | low |
| 523 | 23 | `i.e. se factorise` | — | low |
| 523 | 23 | `hom.` | — | medium |
| 524 | 1–3 | `+` | — | low |
| 524 | 9–13 | `M` | — | low |
| 524 | 15–16 | `p.` | — | low |
| 524 | above diagram (3) | `\tau_\infty(\epsilon_0)=\epsilon_0^{-1}` | — | low |
| 524 | 17–20; diagram (3) | `M_{0,3}` | — | low |
| 524 | 17–20; diagram (3) | `N_{1,1}^{\sim}` | `N_{0,3}^{\sim}` | medium |
| 524 | 17–20; diagram (3) | `\downarrow` | — | low |
| 524 | 17–20; diagram (3) | `\downarrow` | — | low |
| 524 | 17–20; diagram (3) | `1` | — | low |
| 524 | 17–20; diagram (3) | `1` | — | low |
| 524 | 21–23 | `\mathcal T_{1,1}^{\wedge}` | — | low |
| 524 | 21–23 | `un` | — | medium |
| 524 | bottom-left margin | `\mathrm{Gl}(2,\mathbb Z)_{\wedge}` | `\uline{\mathrm{Gl}(2,\mathbb Z)}` | low |
| 525 | 2; display (4) | `\mathrm{Gl}(2,\mathbb Z)^\wedge` | `\mathrm{Sl}(2,\mathbb Z)^\wedge` | low |
| 525 | 2; display (4) | `M` | — | low |
| 525 | 5–6; diagram (5) | `\wedge` | — | medium |
| 525 | 15–17 | `cette` | — | medium |
| 525 | 18; display (8) | `\sharp` | `\prime` | medium |
| 525 | 19–20 | `que` | `qui` | medium |
| 525 | 19–20 | `la` | `là` | medium |
| 525 | 19–20 | `hom. composé de` | — | low |
| 526 | Upper paragraph, after l' | isom. (deleted) | unresolved abbreviation | low |
| 526 | Diagram (10), upper left | Sl(2,Z)^wedge | Sl(2,hat Z)^wedge; overwritten mark over Z | low |
| 526 | Diagram (10), right vertical | q can | q' can | low |
| 526 | Paragraph preceding (11) | tilde gamma | tilde nu | medium |
| 526 | Deleted phrase after un couple | d'élts | abbreviated ending uncertain | low |
| 526 | Deleted first factor of (11) | ornate G with 0,3 | exact subscript/adornments overwritten | low |
| 526 | Underbrace of (11) | {1,tau infinity} | first character heavily overwritten | low |
| 526 | Before l'équation | de (deleted) | à | low |
| 526 | After (12), upper-right adornment of Sl | prime | short oblique quotient notation | low |
| 526 | Bottom deleted parenthesis | côté + two unreadable words | no secure alternative after enlargement | low |
| 526 | Bottom insertion | notée underline u | notée underlined alpha | low |
| 526 | Before diagram (10) | utilisons | utilisant | medium |
| 526 | (11), first Pi superscript | cancelled wedge | cancelled prime | low |
| 527 | (14), first symbol | tilde u | underlined u | medium |
| 527 | (14)–(15), subscript on i | T_0 | Gamma_0 | low |
| 527 | (16), second row | underlined eta | overwritten glyph | medium |
| 527 | (16), subscript on epsilon | phi | rho | low |
| 527 | Left marginal note | ne sont déterminés; qu'au signe près | qu'à un signe près | low |
| 527 | Left marginal note, ending | sans ambiguïté | univoques | medium |
| 527 | Above par rho et sigma | top. | abbreviation without clear final point | medium |
| 527 | Lower prose, sous-groupe | central | centre | medium |
| 527 | (18), deleted expression | int zeta (rho) | zeta could be another long-descender glyph | low |
| 527 | (18), argument of u, second row | sigma | overwritten rho | medium |
| 527 | Just below (18) | et | abandoned letter-like stroke | low |
| 528 | Cancelled beginning above first (20) | Si maintenant | connective after Si heavily ruled through | low |
| 528 | Right of first (20) | car (deleted) | short overinked word | low |
| 528 | Insertion to right of hom | surj | surj. | medium |
| 528 | Before (22) | satisfaisant | satisfont | medium |
| 528 | Deleted commutator, following words | ce qui suffit | final letters touch page boundary | medium |
| 528 | Deleted words below corrected commutators | à impliq. | unfinished impliq without point | low |
| 528 | Left marginal note, final punctuation | . . | ellipsis | low |
| 528 | Lower paragraph | élmts | abbreviated spelling of éléments | medium |
| 528 | Insertion above u_G | endom. | autom. | low |
| 528 | Last line | nos | aux | low |
| 529 | First-line deletion | en général | long strike hides several letter joints | medium |
| 529 | Top-right insertion | néc superscript t. | abbreviation's final raised character uncertain | low |
| 529 | Three cancelled superscripts in (24) | ornate G | hats or previous script adornments | low |
| 529 | Tiny cancelled sign in epsilon_1 line | = | ink blot after product | low |
| 529 | Left marginal note | jusqu'à | contracted ending | medium |
| 529 | (27), deleted prefix | {1,tau} | heavily cancelled bracketed expression | low |
| 529 | (27), superscript on ornate G | bullet | prime | low |

### Complete occurrence register

This register lists every `\unsure` and `\illegible` occurrence in the delivered fragment (271 occurrences in total), including repeated and nested symbols. “LaTeX line” is an exact locator in `LM_C3-511-529_transcription.tex`, not a claim about manuscript lineation. Confidence follows the contextual judgment where a matching reading is available; otherwise the entry is conservatively labelled low. The original uncertainty remains in place in the transcription.

| Scan | LaTeX line | Macro | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
| 511 | 6 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 11 | `unsure` | `S\mathcal{T}'_{\rho,\sigma}` | `S\Gamma'_{\rho,\sigma}` | low |
| 511 | 12 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | medium |
| 511 | 18 | `unsure` | `noté` | — | low |
| 511 | 18 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 18 | `unsure` | `II` | — | low |
| 511 | 18 | `unsure` | `\#` | — | low |
| 511 | 20 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 22 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 26 | `unsure` | `38` | `39` | medium |
| 511 | 29 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 29 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | medium |
| 511 | 31 | `unsure` | `\simeq Z_\rho\times Z_\sigma` | — | low |
| 511 | 34 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 42 | `unsure` | `\mathcal{G}` | — | medium |
| 511 | 43 | `unsure` | `\rho` | `\sigma` | low |
| 511 | 43 | `unsure` | `\rho` | `\sigma` | low |
| 511 | 43 | `unsure` | `2` | `\sigma` | low |
| 511 | 54 | `unsure` | `\rho\sigma` | `\rho,\sigma` | medium |
| 511 | 61 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 61 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 64 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 69 | `unsure` | `S` | — | low |
| 511 | 69 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 72 | `illegible` | `1 physically unreadable words` | — | low |
| 511 | 72 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 72 | `unsure` | `4` | `\#` | low |
| 511 | 72 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 511 | 72 | `unsure` | `II` | — | low |
| 512 | 82 | `unsure` | `\#` | `*` | low |
| 512 | 83 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 512 | 84 | `unsure` | `\subset` | `=` | low |
| 512 | 102 | `unsure` | `(u` | — | low |
| 512 | 127 | `unsure` | `redonnant` | — | medium |
| 513 | 139 | `unsure` | `de` | — | low |
| 513 | 143 | `unsure` | `(` | — | low |
| 513 | 146 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 513 | 152 | `unsure` | `\Gamma_\rho` | `T_\rho` | low |
| 513 | 152 | `unsure` | `\mathcal{G}` | — | medium |
| 513 | 152 | `unsure` | `M_{\rho,\sigma}'` | `M_{\rho,\sigma}^{0}` | medium |
| 513 | 152 | `unsure` | `\#` | `*` | low |
| 513 | 155 | `unsure` | `posé` | — | medium |
| 513 | 157 | `unsure` | `48` | `58` | low |
| 513 | 159 | `unsure` | `\mathrm{aut}` | — | low |
| 513 | 160 | `unsure` | `\mathrm{aut}` | — | low |
| 513 | 166 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 513 | 173 | `unsure` | `\Gamma` | `\gamma` | low |
| 514 | 192 | `unsure` | `\mathcal{G}` | — | medium |
| 514 | 192 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 514 | 196 | `unsure` | `G` | `G_1` | medium |
| 514 | 202 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 514 | 211 | `unsure` | `voit` | — | medium |
| 514 | 211 | `illegible` | `1 physically unreadable words` | — | low |
| 514 | 213 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | medium |
| 514 | 226 | `unsure` | `\zeta` | `\xi` | medium |
| 514 | 232 | `unsure` | `\zeta` | `\xi` | medium |
| 514 | 234 | `unsure` | `\#` | `\zeta` | low |
| 514 | 235 | `unsure` | `\zeta` | `\xi` | medium |
| 515 | 247 | `unsure` | `\operatorname{int}(\alpha)` | — | low |
| 515 | 248 | `unsure` | `\zeta` | `\xi` | medium |
| 515 | 249 | `unsure` | `\operatorname{int}(\beta)` | — | low |
| 515 | 253 | `unsure` | `et` | — | low |
| 515 | 253 | `unsure` | `\zeta` | `\xi` | medium |
| 515 | 253 | `unsure` | `\eta` | — | low |
| 515 | 253 | `unsure` | `.` | — | low |
| 515 | 255 | `unsure` | `Remarque` | `Remarq.` | medium |
| 515 | 255 | `unsure` | `b` | — | low |
| 515 | 255 | `unsure` | `et` | — | low |
| 515 | 261 | `unsure` | `\zeta` | `\xi` | medium |
| 515 | 261 | `unsure` | `\mathcal{G}` | `\Sigma_\rho` | low |
| 515 | 262 | `unsure` | `\zeta` | `\xi` | medium |
| 515 | 262 | `unsure` | `u(\sigma)` | `u\sigma)` | low |
| 515 | 266 | `unsure` | `\zeta` | `\xi` | medium |
| 515 | 266 | `unsure` | `les` | — | low |
| 515 | 266 | `unsure` | `(5)` | — | low |
| 515 | 266 | `unsure` | `)` | — | low |
| 515 | 270 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | low |
| 515 | 272 | `unsure` | `28` | `20` | medium |
| 515 | 272 | `unsure` | `est` | `sera` | low |
| 515 | 273 | `unsure` | `puis` | `par` | low |
| 515 | 273 | `unsure` | `bij.` | `bis` | low |
| 515 | 278 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | low |
| 515 | 281 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | low |
| 515 | 282 | `unsure` | `28` | `20` | medium |
| 515 | 286 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | low |
| 516 | 293 | `unsure` | `isomorphe` | — | medium |
| 516 | 293 | `unsure` | `à` | `:` | low |
| 516 | 293 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 516 | 295 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 516 | 295 | `unsure` | `\mathscr{G}` | `\mathcal{G}` | medium |
| 516 | 310 | `unsure` | `\varepsilon_2` | — | low |
| 516 | 311 | `unsure` | `\times\{\pm1\}` | — | low |
| 516 | 312 | `unsure` | `3` | — | medium |
| 516 | 312 | `unsure` | `12` | — | low |
| 516 | 315 | `illegible` | `3 physically unreadable words` | — | low |
| 516 | 316 | `unsure` | `deux facteurs` | — | low |
| 516 | 318 | `unsure` | `M_{0,3}^{\prime\sim}` | — | low |
| 516 | 321 | `unsure` | `Image inv.` | — | medium |
| 516 | 330 | `unsure` | `\sigma_{\mathcal{G}}` | — | medium |
| 517 | 342 | `unsure` | `a)` | — | medium |
| 517 | 347 | `unsure` | `\mathcal{G}` | — | low |
| 517 | 348 | `unsure` | `M` | `\mathcal{G}` | low |
| 517 | 352 | `unsure` | `c)` | — | low |
| 517 | 356 | `unsure` | `eff.` | — | low |
| 517 | 356 | `unsure` | `automatique` | `autom.` | low |
| 517 | 358 | `unsure` | `effectif` | — | medium |
| 517 | 364 | `unsure` | `u` | `\psi` | low |
| 517 | 364 | `unsure` | `u` | `\psi` | low |
| 517 | 366 | `unsure` | `autom.` | — | medium |
| 517 | 366 | `unsure` | `u_{\mathcal{G}}\rho` | — | low |
| 517 | 379 | `unsure` | `tt` | — | medium |
| 517 | 380 | `unsure` | `[0]` | — | low |
| 517 | 384 | `unsure` | `le` | — | medium |
| 518 | 393 | `unsure` | `S_0` | — | low |
| 518 | 393 | `unsure` | `*` | — | low |
| 518 | 394 | `unsure` | `S_0` | — | low |
| 518 | 398 | `unsure` | `\varphi` | `i` | low |
| 518 | 398 | `unsure` | `\mathcal{G}` | — | low |
| 518 | 399 | `unsure` | `\mathcal{G}` | — | low |
| 518 | 402 | `unsure` | `bien sûr en` | — | medium |
| 518 | 407 | `unsure` | `u\in` | — | medium |
| 518 | 408 | `unsure` | `=` | `\in` | low |
| 518 | 410 | `unsure` | `\ell_1` | `\ell_0` | medium |
| 518 | 411 | `unsure` | `M_{\rho_{\mathcal{G}},\sigma_{\mathcal{G}}}^{0}` | — | low |
| 518 | 415 | `unsure` | `\psi_{\mathcal{T}}` | `\psi_{\Gamma}` | low |
| 518 | 416 | `unsure` | `\mathcal{T}` | `\Gamma` | low |
| 519 | 426 | `unsure` | `Z_\rho` | `T_\rho` | medium |
| 519 | 427 | `unsure` | `Z_\sigma` | `T_\sigma` | medium |
| 519 | 436 | `unsure` | `u` | — | low |
| 519 | 438 | `unsure` | `T_\rho` | `\Gamma_\rho` | medium |
| 519 | 438 | `unsure` | `T_\rho` | `\Gamma_\rho` | medium |
| 519 | 438 | `unsure` | `y` | `\dot x` | low |
| 519 | 438 | `unsure` | `\psi u` | `\psi(x)` | low |
| 519 | 440 | `unsure` | `\delta_G(` | — | low |
| 519 | 441 | `unsure` | `T_\rho` | `\Gamma_\rho` | medium |
| 519 | 441 | `unsure` | `T_\sigma` | `\Gamma_\sigma` | medium |
| 519 | 451 | `unsure` | `1` | — | low |
| 519 | 460 | `unsure` | `M` | — | low |
| 520 | 476 | `unsure` | `Il aurait` | — | medium |
| 520 | 487 | `unsure` | `\varphi_M` | `\varphi_{SM}` | low |
| 520 | 487 | `unsure` | `passe` | — | medium |
| 520 | 487 | `unsure` | `en` | `à` | medium |
| 520 | 490 | `unsure` | `Z_{\rho,\sigma}` | `\Sigma_{\rho,\sigma}` | medium |
| 520 | 498 | `unsure` | `sont induits par` | — | low |
| 520 | 501 | `unsure` | `uniquement` | — | low |
| 520 | 503 | `unsure` | `b` | `se` | low |
| 520 | 514 | `unsure` | `désignant` | — | medium |
| 521 | 523 | `unsure` | `cela` | `elle` | medium |
| 521 | 523 | `unsure` | `\varphi_{S_0M}` | — | medium |
| 521 | 528 | `unsure` | `\varphi_{S_0M^0}` | — | low |
| 521 | 528 | `unsure` | `transforme` | — | low |
| 521 | 531 | `unsure` | `\mathcal G` | — | low |
| 521 | 531 | `unsure` | `M_0` | `M^0` | low |
| 521 | 541 | `unsure` | `th.` | — | medium |
| 521 | 541 | `unsure` | `mettant` | — | low |
| 521 | 541 | `unsure` | `vaut` | — | medium |
| 521 | 542 | `unsure` | `suppl.` | — | low |
| 521 | 543 | `unsure` | `expliciter` | — | low |
| 521 | 550 | `unsure` | `0` | — | low |
| 521 | 552 | `unsure` | `\prime` | `0` | medium |
| 521 | 554 | `unsure` | `\prime` | `0` | medium |
| 521 | 555 | `unsure` | `0` | — | low |
| 521 | 556 | `unsure` | `0` | — | low |
| 521 | 557 | `unsure` | `\left(-\frac13\right)` | `\left(\frac13\right)` | low |
| 521 | 558 | `unsure` | `0` | — | low |
| 521 | 562 | `unsure` | `\prime` | `0` | medium |
| 522 | 577 | `unsure` | `(91)` | `(92)` | medium |
| 522 | 579 | `unsure` | `\simeq` | `=` | medium |
| 522 | 580 | `unsure` | `G_{\rho',\sigma'}=` | — | low |
| 522 | 581 | `unsure` | `G` | — | low |
| 522 | 588 | `unsure` | `\Gamma` | `\mathcal T` | low |
| 522 | 590 | `unsure` | `cf.` | — | low |
| 522 | 593 | `unsure` | `0` | — | low |
| 522 | 594 | `unsure` | `Ceci m'avait été inspiré dans le cas` | — | low |
| 522 | 594 | `unsure` | `couple modulaire` | — | low |
| 522 | 594 | `unsure` | `qui ne résulte pas de` | — | low |
| 522 | 594 | `unsure` | `mais dans ce cas` | — | low |
| 522 | 594 | `illegible` | `2 physically unreadable words` | — | low |
| 522 | 599 | `unsure` | `\Gamma_{\rho,\sigma}` | — | low |
| 522 | 601 | `unsure` | `*` | — | low |
| 522 | 608 | `unsure` | `expliciter` | — | medium |
| 522 | 618 | `unsure` | `\mathrm{Gl}(\widehat{\mathbb Z})/\mu_2(\mathbb Z)` | — | low |
| 522 | 622 | `unsure` | `G\,\mathbb Z\,B/\mu_2` | — | low |
| 522 | 624 | `unsure` | `T_\rho` | `\mathcal T_\rho` | medium |
| 522 | 625 | `unsure` | `voir le` | — | low |
| 522 | 625 | `unsure` | `T_\rho` | — | medium |
| 522 | 625 | `unsure` | `avec notations du` | — | medium |
| 522 | 626 | `unsure` | `\{t\sigma+u\mid t^2+u^2\in\widehat{\mathbb Z}^{*}\}/\pm1` | — | low |
| 522 | 626 | `unsure` | `sous-groupe` | — | low |
| 522 | 628 | `unsure` | `est le` | — | low |
| 522 | 629 | `unsure` | `SM''_{\rho,\sigma}` | `SM'_{\rho,\sigma}` | low |
| 522 | 630 | `unsure` | `SM'_{\rho,\sigma}(\widehat{\mathbb Z})` | — | low |
| 523 | 649 | `unsure` | `\}` | `)` | low |
| 523 | 660 | `unsure` | `S_0\mathcal T'_{\rho,\sigma}` | `S\mathcal T'_{\rho,\sigma}` | medium |
| 523 | 666 | `unsure` | `M_{\rho,\sigma}` | `M_\rho` | low |
| 523 | 678 | `unsure` | `d'image` | — | low |
| 523 | 678 | `unsure` | `L_0^{\mathcal G}` | — | low |
| 523 | 686 | `unsure` | `le` | — | low |
| 523 | 686 | `unsure` | `l'image` | — | low |
| 523 | 686 | `unsure` | `se factorise` | — | low |
| 523 | 686 | `unsure` | `sur un` | — | low |
| 523 | 689 | `unsure` | `*` | — | low |
| 523 | 698 | `unsure` | `i.e. se factorise` | — | low |
| 523 | 698 | `unsure` | `hom.` | — | medium |
| 524 | 716 | `unsure` | `+` | — | low |
| 524 | 731 | `unsure` | `M` | — | low |
| 524 | 738 | `unsure` | `p.` | — | low |
| 524 | 740 | `unsure` | `\tau_\infty(\epsilon_0)=\epsilon_0^{-1}` | — | low |
| 524 | 744 | `unsure` | `M_{0,3}` | — | low |
| 524 | 745 | `unsure` | `N_{1,1}^{\sim}` | `N_{0,3}^{\sim}` | medium |
| 524 | 747 | `unsure` | `\downarrow` | — | low |
| 524 | 749 | `unsure` | `\downarrow` | — | low |
| 524 | 750 | `unsure` | `1` | — | low |
| 524 | 750 | `unsure` | `1` | — | low |
| 524 | 753 | `unsure` | `\mathcal T_{1,1}^{\wedge}` | — | low |
| 524 | 753 | `unsure` | `un` | — | medium |
| 524 | 754 | `unsure` | `\mathrm{Gl}(2,\mathbb Z)_{\wedge}` | `\uline{\mathrm{Gl}(2,\mathbb Z)}` | low |
| 525 | 763 | `unsure` | `\mathrm{Gl}(2,\mathbb Z)^\wedge` | `\mathrm{Sl}(2,\mathbb Z)^\wedge` | low |
| 525 | 764 | `unsure` | `M` | — | low |
| 525 | 771 | `unsure` | `\wedge` | — | medium |
| 525 | 796 | `unsure` | `cette` | — | medium |
| 525 | 798 | `unsure` | `\sharp` | `\prime` | medium |
| 525 | 800 | `unsure` | `que` | `qui` | medium |
| 525 | 800 | `unsure` | `la` | `là` | medium |
| 525 | 800 | `unsure` | `hom. composé de` | — | low |
| 526 | 817 | `unsure` | `utilisons` | `utilisant` | medium |
| 526 | 817 | `unsure` | `isom.` | — | low |
| 526 | 822 | `unsure` | `\mathbb Z` | `\widehat{\mathbb Z}` | low |
| 526 | 829 | `unsure` | `q` | `q'` | low |
| 526 | 836 | `unsure` | `\widetilde{\gamma}` | `\widetilde{\nu}` | medium |
| 526 | 838 | `unsure` | `d'élts` | — | low |
| 526 | 843 | `unsure` | `\mathcal{G}_{0,3}` | — | low |
| 526 | 844 | `unsure` | `\wedge` | `\prime` | low |
| 526 | 845 | `unsure` | `\{1,\tau_\infty\}` | — | low |
| 526 | 849 | `unsure` | `de` | `à` | low |
| 526 | 858 | `unsure` | `\prime` | — | low |
| 526 | 871 | `unsure` | `côté` | — | low |
| 526 | 871 | `illegible` | `2 physically unreadable words` | — | low |
| 526 | 872 | `unsure` | `\underline{u}` | `\underline{\alpha}` | low |
| 527 | 886 | `unsure` | `\widetilde{u}` | `\underline{u}` | medium |
| 527 | 887 | `unsure` | `i_{T_0}` | `i_{\Gamma_0}` | low |
| 527 | 894 | `unsure` | `i_{T_0}` | `i_{\Gamma_0}` | low |
| 527 | 907 | `unsure` | `\underline{\eta}` | — | low |
| 527 | 908 | `unsure` | `\varphi` | `\rho` | low |
| 527 | 916 | `unsure` | `ne sont déterminés` | — | low |
| 527 | 916 | `unsure` | `qu'au` | `qu'à un` | low |
| 527 | 918 | `unsure` | `sans ambiguïté` | `univoques` | medium |
| 527 | 935 | `unsure` | `top.` | — | medium |
| 527 | 936 | `unsure` | `central` | `centre` | medium |
| 527 | 945 | `unsure` | `\zeta` | — | low |
| 527 | 947 | `unsure` | `\sigma` | `\rho` | medium |
| 527 | 951 | `unsure` | `et` | — | low |
| 528 | 976 | `unsure` | `maintenant` | — | low |
| 528 | 980 | `unsure` | `car` | — | low |
| 528 | 983 | `unsure` | `surj` | — | medium |
| 528 | 998 | `unsure` | `satisfaisant` | `satisfont` | medium |
| 528 | 1004 | `unsure` | `ce qui suffit` | — | medium |
| 528 | 1009 | `unsure` | `impliq.` | — | low |
| 528 | 1013 | `unsure` | `. .` | — | low |
| 528 | 1016 | `unsure` | `élmts` | — | medium |
| 528 | 1019 | `unsure` | `endom.` | `autom.` | low |
| 528 | 1029 | `unsure` | `nos` | `aux` | low |
| 529 | 1036 | `unsure` | `en général` | — | medium |
| 529 | 1037 | `unsure` | `néc\textsuperscript{t}.` | — | low |
| 529 | 1048 | `unsure` | `\mathcal{G}` | `\wedge` | low |
| 529 | 1049 | `unsure` | `\mathcal{G}` | `\wedge` | low |
| 529 | 1050 | `unsure` | `\mathcal{G}` | `\wedge` | low |
| 529 | 1052 | `unsure` | `=` | — | low |
| 529 | 1060 | `unsure` | `jusqu'à` | — | medium |
| 529 | 1080 | `unsure` | `\{1,\tau\}` | — | low |
| 529 | 1081 | `unsure` | `\bullet` | `\prime` | low |

## 2. Abbreviations met

Expansions in this table are editorial suggestions only; they have not been substituted into the transcription. Punctuation and uncertain abbreviated forms remain as observed in the fragment.

| As written | Proposed expansion or function |
|---|---|
| g. | gauche |
| ds | dans |
| dfn | définition; compact mark above an equality |
| Im | image |
| Ker | noyau |
| Centr | centralisateur |
| NB | nota bene |
| § | section / paragraphe |
| hom; hom. | homomorphisme(s) |
| cf; cf. | confer / comparer / voir |
| i.e. | id est |
| resp. | respectivement |
| épi | épimorphisme / épimorphique |
| can | canonique |
| p. | page |
| hyp. | hypothèse |
| eff | effectif / effectifs |
| néc. | nécessairement |
| int | automorphisme intérieur / conjugaison |
| bij. (uncertain; alternative bis) | bijection / bijectif |
| Aut | automorphismes |
| autom. (uncertain) | automorphisme; the distinct uncertain marginal word may be automatique |
| tt (uncertain) | tout |
| p.r. | par rapport |
| Image inv.; Im. inv. (uncertain) | image inverse |
| th. (uncertain) | théorème |
| suppl. (uncertain) | supplémentaire |
| etc | et cetera |
| t.q. | tel que / tels que |
| id | idem |
| iso. can. | isomorphisme canonique |
| bis | additional item bearing the same number |
| Sl; Gl | Special and general linear group notations; lowercase l is retained |
| cart | cartésien |
| isom. (deleted, uncertain) | isomorphisme |
| d'élts (deleted, uncertain) | d'éléments |
| top. | topologiquement |
| ssi | si et seulement si |
| surj | surjectif |
| impliq. (deleted, uncertain) | impliquer |
| élmts (uncertain) | éléments |
| mod | modulo |
| endom. (uncertain; alternative autom.) | endomorphisme / automorphisme |
| néc superscript t. (uncertain) | nécessairement |
| 1/2 direct | semi-direct |
| $\overline{\mathrm m}$ | même / mêmes |

## 3. Honest assessment of legibility and coverage

The surviving running prose and many undisturbed formulas are moderately legible. The main risks are short word endings, small indices and accents, competing hats and primes, and words partly covered by cancellation strokes. Enlarging and rotating crops improves orientation but cannot restore ink hidden by overwriting. In particular, the typographic alphabet of some ornamental group letters remains an editorial approximation explicitly qualified where doubtful.

The least secure passages are the diagonal margin and revised quotient symbols on scan 511; the deleted factors and lower cancelled paragraph on scan 515; the erased congruence definition on scan 516; the crowded diagonal margin on scan 517; the overwritten/cancelled diagram on scan 518; the revised conditions and atypical arrow in (77) on scan 519; the successive b)/(84) layers on scan 520; the margin and cancelled (94) formulas on scan 522; the cancelled lower section III on scan 523; the revisions at the foot of scan 524; the cancelled words and superscripts on scan 526; the underlined formulas and margin on scan 527; the overlapping commutator revisions on scan 528; and the cancelled superscripts and first-line deletion on scan 529.

Every scan has been read as a whole and against its transcription, with an inventory checked before proceeding. Independent rereading was used for selected difficult passages and all four final scans. The last-page check removed an unsupported inverse on the final rho-expression in (24); two uncertain word readings were broadened rather than made artificially definite. Repeated equation numbers, unclosed authorial parentheses, visibly unusual indices, and the observed arrow directions remain as written.

The inventory contains 438 elements, all marked `yes`; this status records that the inventoried content is represented, not that every reading is secure. There are 266 `\unsure` occurrences and 5 physically unreadable prose spans. No mathematical symbol is replaced by an `\illegible` placeholder. The closing paragraph of the final scan is included.

## 4. Research notes — English, separate from the transcription

These are source-based research leads, not additions to the manuscript and not a literature review. An “unproved claim” means a statement whose proof is not supplied at the cited place; it may be justified earlier or later in the manuscript. “Conjecture / question” also covers an explicit question or proposed construction and does not by itself identify a formal conjecture. Own ideas are labelled, include confidence and a reason, and are not presented as established or new. No external edition or published transcription was used to settle a reading.

### R01

**Scan 511, (42)–(43); kind: unproved claim.** The text says «on trouve que … induit une bijection canonique» after quotienting by the image of `L_0`. Checking the canonicity requires the earlier map (38 or 39, the reference is uncertain here), compatibility with the stated left translation, and a proof that its fibres are exactly the `L_0`-orbits. (Grothendieck, 1981, scan 511).

### R02

**Scan 511, (44)–(47); kind: unpursued implication.** The displayed kernel descriptions and exact sequences invite a comparison of the extension represented before and after the `L_0` quotient. A rigorous comparison should first resolve the written indices in the second line of (44), without treating their expected symmetry as evidence for the transcription. (Grothendieck, 1981, scan 511).

### R03

**Scan 511, final NB; kind: unproved claim.** «on retrouve … de § 48» identifies the modular example with previously introduced objects. Verifying this identification needs the definitions and conventions in that earlier section; the NB alone does not supply an explicit isomorphism. (Grothendieck, 1981, scan 511).

### R04

**Scan 512, (49)–(52); kind: unproved claim.** The passage states «dont le noyau est formé des … d'où une suite exacte». The displayed kernel computation identifies `L_0`, but verification of exactness at the last nontrivial term also needs surjectivity of the projection, hence the appropriate lifting assertion for `B_{rho,sigma}` over the common quotient. (Grothendieck, 1981, scan 512).

### R05

**Scan 512, (53)–(54); kind: unpursued implication.** The canonical projections to `G`, `Z_rho`, `Z_sigma`, and `B` make the fibre-product construction accessible through its components. One can check which of these projections remain surjective when the underlying lifting hypotheses are weakened; that issue is not addressed on this page. (Grothendieck, 1981, scan 512).

### R06

**Scan 513, (55); kind: unproved claim.** «l'extension … est l'image inverse de l'extension» identifies the `L_0` extension as a pullback. A proof should explicitly compare the inclusion of the kernel and the quotient map, since an isomorphism of underlying groups alone does not identify extensions. (Grothendieck, 1981, scan 513).

### R07

**Scan 513, (56)–(57); kind: unproved claim.** «comme … sont épi» gives the hypothesis used to deduce the exact sequence of the fibre product. This page supplies the surjectivity premise that was only implicit in scan 512; verification still requires the earlier definitions of the three maps and of their kernels. (Grothendieck, 1981, scan 513).

### R08

**Scan 513, final (51); kind: unpursued implication.** The map `U ↦ (1,1,U)` singles out the ambient group inside the larger group constructed from triples. Its normality and its quotient are natural questions at this point, and the next page expressly pursues an exact sequence associated with it. (Grothendieck, 1981, scan 513).

### R09

**Scan 514, annotation under (52); kind: conjecture / question.** «parfois noté … ?» is a question about the appropriate designation of the kernel group, rather than a securely stated new theorem. Its question mark should remain visible when comparing the several group notations used in this section. (Grothendieck, 1981, scan 514).

### R10

**Scan 514, (54)–(55); kind: unproved claim.** «cela induit une bijection» relies on the corollary on manuscript p. 557. Reconstructing the inverse from the three displayed coordinates is a useful verification problem; the claim is a bijection, and these lines do not themselves assert that the displayed product is a direct product of groups. (Grothendieck, 1981, scan 514).

### R11

**Scan 514, (55); kind: own idea.** **Confidence: medium.** Transporting the group law through the indicated bijection may reveal an action or a twisting factor rather than componentwise multiplication. This is suggested by the coordinate expressions `u a^{-1}`, `u b^{-1}`, and `u U^{-1}`; it is an investigation to perform, not an established identification or a novelty claim. (Grothendieck, 1981, scan 514).

### R12

**Scan 514, (58); kind: unpursued implication.** The formulas compare the pairs of cocycle-like expressions before and after conjugating their coordinates by `f^{-1}`. They suggest a change-of-trivialization calculation, but the precise action conventions must be checked against the earlier definitions before applying a cohomological interpretation. (Grothendieck, 1981, scan 514).

### R13

**Scan 515, remark before (60); kind: unpursued implication.** «on n'a pas vraiment utilisé la soi-disante “hyp. fondamentale” … sauf la partie a)» narrows the hypotheses actually used. One should trace each preceding construction to determine precisely which assertions require part b), especially surjectivity onto the formally defined set of pairs. (Grothendieck, 1981, scan 515).

### R14

**Scan 515, (60)–(61); kind: unpursued implication.** The text introduces «couples effectifs» as pairs realized by an element of `B_{rho,sigma}`, and then takes their inverse image under the indicated map. This separates satisfaction of the displayed defining conditions from realization by an acting element; the distinction is visible in the source rather than imposed by the transcription. (Grothendieck, 1981, scan 515).

### R15

**Scan 515, final line continuing onto scan 516; kind: unproved claim.** «et c'est sur … qu'on aura une structure» postpones the structural assertion to the continuation. A verification must keep track of the restriction to the effective inverse image, not transfer the group structure to every formal pair merely because the formulas have the same shape. (Grothendieck, 1981, scan 515).

### R16

**Scan 515, (60); kind: own idea.** **Confidence: medium.** Testing an example where the realization map fails to be surjective could isolate the role of the discarded hypothesis b). The definition of the effective image gives a concrete place to measure that failure, but existence of such an example is not asserted on this page or established here. (Grothendieck, 1981, scan 515).

### R17

**Scan 516, lines 1–4; (62) — unproved claim**

The assertion that the effective locus carries a transported group structure is accompanied by the words “par l’isomorphisme (qui remplace (38))”. Verifying it requires checking both the asserted bijection and the compatibility of the transferred multiplication with the previously defined effective locus; this page invokes the earlier construction. (Grothendieck, 1981, scan 516).

### R18

**Scan 516, (64)–(66) — unpursued implication**

The restricted subgroup is defined before an arbitrary continuous surjection \(\psi\) is introduced. It is worth tracking precisely which congruence character survives the deletions in (64), because that character controls the scope of the descent construction on the following pages. (Grothendieck, 1981, scan 516).

### R19

**Scan 516, (66)–(68) — own idea**

Confidence: medium. One can test the subsequent descent assertions on small finite quotients generated by elements satisfying the two displayed power relations. This would check the role of the kernel-stability condition in explicit examples; it is a proposed check, not a claim of novelty or a theorem. (Grothendieck, 1981, scan 516).

### R20

**Scan 517, left margin, a–c prime — unproved claim**

The marginal instruction “l’introduire par conditions équivalentes” proposes several formulations involving effectivity, induced automorphisms, and extensions \(\psi_M,\psi_G\). Their equivalence needs a careful distinction between descent of individual automorphisms and a continuous homomorphism on the whole extension; the final marginal wording is uncertain. (Grothendieck, 1981, scan 517).

### R21

**Scan 517, lower paragraph after (70) — unproved claim**

The text says that the kernel-stability condition is “automatiquement remplie” under condition (20)b). Checking this requires recovering that earlier hypothesis and verifying that it really gives stability under the whole displayed group, not only the subgroup with suffix [0]. (Grothendieck, 1981, scan 517).

### R22

**Scan 517, (69)–(70) — own idea**

Confidence: high as a proposed proof strategy. Formulate effectivity as invariance of a closed normal kernel under the relevant automorphism group, then derive continuity of the descended action separately. This isolates what the square proves from the extra topological assertion; it is an interpretive check rather than an established result. (Grothendieck, 1981, scan 517).

### R23

**Scan 518, Théorème; (71) — unproved claim**

The theorem asserts “il existe un hom unique” for an effective surjection. The prescription by the three invariants states what the map should do, but a proof must establish independence of the choice of representatives and compatibility with multiplication and topology. (Grothendieck, 1981, scan 518).

### R24

**Scan 518, Corollaire; lower (72) — unproved claim**

The corollary asserts a homomorphism of exact sequences. The main check is that the descended map carries the specified normal subgroup into the target normal subgroup and induces the displayed quotient map; the cancelled square should not be treated as an additional surviving hypothesis. (Grothendieck, 1981, scan 518).

### R25

**Scan 518, margin and (71)–(72) — own idea**

Confidence: medium. Compare the marginal S_0-level map with the unprefixed theorem and identify precisely the passage by a quotient that connects them. This may clarify whether uniqueness is being asserted before or after removing the auxiliary data, without changing the transcription. (Grothendieck, 1981, scan 518).

### R26

**Scan 519, (75)–(77) — unproved claim**

The assertion “les trois hom composés … sont égaux” is the compatibility needed for the three component maps to land in the fiber-product group. A verification must use the same quotient map for each component; the visible lower diagonal arrow in (77) points the opposite way from that expected from this assertion and has been preserved. (Grothendieck, 1981, scan 519).

### R27

**Scan 519, (78)–(80) — unpursued implication**

The restriction formula and the square express compatibility of the extended map with conjugation on the normal subgroup. Together they invite a direct comparison between a homomorphism of extensions and a descended action on the quotient, while the page does not supply that equivalence as a separate proof. (Grothendieck, 1981, scan 519).

### R28

**Scan 519, (73), (77) — own idea**

Confidence: high as an editorial check. Keep the missing prime on the second source in (73), and the change from Z targets there to T targets in (77), separate from the mathematical proof. Compare them with the earlier definitions before judging whether they are authorial slips or deliberate distinctions; no correction is warranted from this page alone. (Grothendieck, 1981, scan 519).

### R29

**Scan 520, lines 1–9; (81)–(82) — unproved claim**

The text frames the construction as an “énoncé de fonctorialité” and asserts a unique induced homomorphism for a surjection preserving the specified generators. A proof should check that the component maps respect all defining relations and that passage to the chosen quotient is independent of auxiliary representatives. (Grothendieck, 1981, scan 520).

### R30

**Scan 520, left margin; (83)–(85) — unproved claim**

The margin says the induced homomorphism is determined by the four component maps; the revised discussion narrows the needed information toward the G-component and then the B-component using the factorization displayed below (85). The successive determinations should be checked against the relations between the factors and their intersection. (Grothendieck, 1981, scan 520).

### R31

**Scan 520, upper-left margin — unpursued implication**

The remark “mieux valu prendre” a map in the reversed naming convention is an editorial expectation about making specialization easier, not a reversal of the surviving arrow in (81). Following this suggestion later may explain changes of primes without changing the covariant direction of the construction. (Grothendieck, 1981, scan 520).

### R32

**Scan 520, (85)–(86) — own idea**

Confidence: medium. Treat the two squares as a candidate universal characterization of the descended homomorphism, then test preservation of composition for two successive surjections. If uniqueness applies at the same level on both sides, composition should follow without a new coordinate calculation; the scope of that uniqueness still needs checking. (Grothendieck, 1981, scan 520).

### R33

**Scan 521, lines 5–13, (88); unproved claim.** The coordinate rule is introduced as “Une autre façon, plus directe”. These lines assert that applying φ separately to α, β, and f produces the induced group homomorphism; a proof would need to verify preservation of the defining parameter relations and the multiplication law, not only the displayed coordinate formula. (Grothendieck, 1981, scan 521, eq. 88.)

### R34

**Scan 521, lines 14–20 and left margin; unpursued implication.** The phrase “cas universel” is qualified in the margin by “tout au moins” and the relations ρ³ = 1, σ² = 1. The qualification deserves separate examination: the exact universal property and the class of groups or morphisms to which it applies must be extracted from the hypotheses, without treating the adjective alone as a proof. (Grothendieck, 1981, scan 521.)

### R35

**Scan 521, lines 21–25, (90); unproved claim.** “Il est bon d’expliciter” introduces identifications of the auxiliary groups in the universal example. The overwritten decorations make some specific identifications uncertain, but the stated comparison between the abstract construction and the groups with subscript 0,3 is a substantive claim whose compatibility with all projections would need checking. (Grothendieck, 1981, scan 521, eq. 90.)

### R36

**Scan 522, lines 4–14, (93); unpursued implication.** The author explicitly calls the earlier notation “inadéquates” and introduces primes while removing certain superscript zeros. This change is consequential for later comparisons: an index of identifications should distinguish a mere renaming from an actual quotient, since primes already occur in matrix-group notation on the same page. (Grothendieck, 1981, scan 522, eq. 93.)

### R37

**Scan 522, lines 18–29, (94); unproved claim.** “Autres cas particuliers importants à expliciter” leads to a table for the projective modular example. A verification should derive the B, G, and Z descriptions from the original definitions and establish precisely which scalar subgroup is factored out; the cancelled Zσ formula and its replacement must be treated as separate stages of the calculation. (Grothendieck, 1981, scan 522, eq. 94.)

### R38

**Scan 523, lines 1–11, (95); unproved claim.** “Prenons” introduces the nonprojective modular example and its centralizer/normalizer formulas without a derivation on this page. A proof would need to justify the polynomial description cρ+d, the stated unit condition, and the decomposition of Zσ using Tσ and τ∞, including the role of the displayed diagonal matrix. (Grothendieck, 1981, scan 523, eq. 95.)

### R39

**Scan 523, cancelled section III, (1)–(4bis); unpursued implication.** The deleted construction associates an automorphism character to the procyclic subgroup generated by ε₀, using the phrase “nul sur L₀”. Although cancelled, this records a possible route from the B action to a character on the quotient γ and then on G; the needed checks concern the kernel J, the action on the image of the profinite integers, and independence of representatives. This is a note about a discarded argument, not an endorsement of its validity. (Grothendieck, 1981, scan 523, cancelled eqs. 1–4bis.)

### R40

**Scan 524, lines 9–16, (2)–(3); unproved claim.** The group N is described as an “image inverse”, followed by “un hom. de suites exactes”. The natural verification is to construct the pullback explicitly, identify its central kernel with {±1}, and check the diagram’s maps against the previously defined canonical homomorphism. (Grothendieck, 1981, scan 524, eqs. 2–3.)

### R41

**Scan 524, (3); own idea — confidence: medium.** One could compare this pullback extension through its classes on finite quotients, keeping the {±1} kernel explicit. The reason is the displayed central extension and its common kernel: finite-level extension classes may help separate a canonical pullback from a choice of splitting; this is a proposed check, not a claim of novelty or an established result. (Grothendieck, 1981, scan 524).

### R42

**Scan 525, lines 3–11, (5)–(6); unproved claim.** The restriction is said to fit into “une suite exacte canonique”, and three vertical arrows are labelled “épi”. A proof should establish injectivity of the geometric map, identify the quotient, and verify surjectivity of each vertical comparison rather than inferring these facts solely from the diagram. (Grothendieck, 1981, scan 525, eqs. 5–6.)

### R43

**Scan 525, lines 12–20, (7)–(8); unproved claim.** “On peut écrire” introduces a product labelled “semi-direct”, and the page ends by promising “un iso. can.”. The required argument should identify the subgroup written M(0), prove that it supplies the relevant complement, and check the compatibility of its map to the matrix quotient with the preceding central extension. (Grothendieck, 1981, scan 525, eqs. 7–8.)

### R44

**Scan 525, comparison diagram (6); own idea — confidence: medium.** Track the kernel of the arrow from the completion of Sl(2,Z) to Sl(2,Ẑ) as an additional object when comparing the constructions. The reason is the manuscript’s distinct source and target notations and its explicit epimorphism: identifying them without a kernel calculation would discard information; no assertion about that kernel’s structure is made here. (Grothendieck, 1981, scan 525).

### R45

**526, paragraph before (10); unproved claim.** “une opération” and “que je voudrais expliciter” announce an explicit description of the action obtained from the decomposition (9). A check would have to identify the action determined by the selected splitting and verify that the formulas on the chosen generators extend continuously and respect the relations; this note does not assert that the surrounding manuscript omits that verification permanently. (Grothendieck, 1981, scan 526, (9)–(13).)

### R46

**526, (10) and final paragraph; unpursued implication.** “diagramme cartésien” and “ce qui est compatible” place the generator formulas beside the matrix quotient. It would be useful to isolate exactly which compatibility is asserted for the completed discrete group and which for the group over the completed coefficient ring, without identifying those groups merely because their notation is similar. (Grothendieck, 1981, scan 526, (10), (13).)

### R47

**526, (9)–(13); own idea, medium confidence.** One possible verification strategy is to test the claimed lifted action first on finite quotients while tracking the central sign, then check compatibility under refinement. This is a proposal prompted by the quotient arrows and the forthcoming sign formulas, not a claim that a finite test alone proves the profinite statement or that the idea is new. (Grothendieck, 1981, scan 526).

### R48

**527, (14)–(19); unproved claim.** “On aura, de façon précise” precedes explicit formulas involving the multiplier and the sign character. A direct verification would need to check the action on both generators with the stated central sign and compare the underlined matrix images with their tilded lifts, keeping the doubtful subscript in (16) unresolved until the ink is independently checked. (Grothendieck, 1981, scan 527, (14)–(19).)

### R49

**527, left marginal note and (19); unpursued implication.** The note says that the conjugators are determined “au signe près,” while the resulting quantities are “sans ambiguïté” (the latter reading has qualified confidence, with “univoques” retained as an alternative). This suggests isolating a lemma on independence of the expressions from the chosen central-sign representatives; the note records a task for verification, not a completed proof. (Grothendieck, 1981, scan 527, margin beside (16)–(17), (19).)

### R50

**528, lower paragraph and (23); conjecture / question.** “essayer de trouver” explicitly presents a descent problem for an endomorphism (the inserted abbreviation could instead be “autom.”). The issue is whether the prescribed images of the two generators define the required map on the image group; any proof must distinguish satisfaction of the displayed relations from preservation of all additional relations in that particular quotient. (Grothendieck, 1981, scan 528, (21)–(23).)

### R51

**528, margin beside (22); own idea, high confidence as a point to check.** The phrase “élément central canonique involutif” should be checked against quotients in which the displayed central element becomes the identity. The presentation only prompts the question whether “involutif” here means square equal to the identity or strictly order two; this note does not change the manuscript's wording. (Grothendieck, 1981, scan 528, margin beside (22).)

### R52

**528, first (20); unproved claim.** “Notons aussi” introduces the formula for the image of epsilon_0 under u without a calculation on this page. A proof would compare the chosen cusp element with the action on the two generators and the multiplier convention already in use. (Grothendieck, 1981, scan 528, first (20).)

### R53

**529, left marginal note beside (24); unpursued implication.** “ce qui n'est pas la convention habituelle” explicitly flags a change of convention (the following “jusqu'à” has qualified confidence). Earlier cusp-element formulas should therefore be compared only after recording the changed order and signs in (24), rather than being used to silently repair this page. (Grothendieck, 1981, scan 529, (24), left margin.)

### R54

**529, (25)–(27); unproved claim.** “qui impliquent, via (24) et (22)” announces the two inversion identities, after which a semidirect product is introduced. A verification should check the identities, the square of the proposed involution on the generators, and descent to any extra quotient relations; the displayed calculation alone must not be treated as a blanket descent theorem. (Grothendieck, 1981, scan 529, (25)–(27).)

### R55

**529, final paragraph; unproved claim.** “paraphraser des constructions déjà faites par ailleurs” signals reuse rather than a worked construction in these pages. The next research step would be to locate the intended earlier construction and identify the precise hypotheses transferred to the enlarged group. (Grothendieck, 1981, scan 529, final paragraph.)

### R56

**529, (22) on the preceding scan and (25); own idea, medium confidence.** One could separate two checks: that the proposed involution acts on the group given solely by the displayed generator relations, and that it preserves the kernel of the map to the particular image group. The distinction is suggested by the passage from a universal presentation to the image of Psi; it is a proposed proof organization, not an assertion of a new result. (Grothendieck, 1981, scan 529).

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished handwritten manuscript, cote 140-3, archive file covering pages 293–650; supplied scans 511–529, lower handwritten numeration 510–528]. Université de Montpellier archive.

