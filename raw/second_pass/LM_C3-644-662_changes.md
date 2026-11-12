# LM_C3-644-662 — second-pass changes (scans 644–662)

Witness coverage: no witness has the text of these pages (§49 V end and §49 VI, upper ms. numbers 625–633). Searches of
the CSG draft, the IUT text and the Carmona–Kuenzer text for "bisection", "raffinement", "Je vois mieux", "Admettant ce
point", "assez gros", "surcharger", "plongement central", "Zρ,σ", "Mρ,σ", "γρ,σ", "τZ", "δZ", "εG" find nothing from these
pages (CSG and IUT stop long before §49; Carmona–Kuenzer has §49 only as a table line and a running head). The
Grothendieck Circle table gives §49 V "Les groupes Mρ,σ généraux (contexte profini)" at p. 577 and §49 VI "Les groupes
Mρ,σ généraux: récapitulation et raffinement de la construction précédente" at p. 628, the upper number of scan 651; it
was used only where stated (rows 30, 31, 53). Every other reading was settled on the ink. The previous package's checked
file (606–624) was used for the shapes it had already settled (the looped 𝒢₃, Γ̃_Q). Crops are in
`second_pass/work_LM_C3-644-662` (s644_c1 … s662_c2). The checked file compiles (pdflatex, 15 pages, with simple
stand-in definitions of the editorial macros).

| # | Scan | Place | First-pass reading | Corrected reading | Evidence | Confidence |
|---|---|---|---|---|---|---|
| 1 | 644 | first letter of the page | `\unsure{v\|\sigma}` | `\unsure{v\|u}` | Full page and s644_c7: an open u/v-shaped letter with no top bar, so not σ. The proof ending on scan 643 (first pass of 625–643) defines v = α⁻¹u, and the sentence ends "est égale à celle de u", so v is meant; u kept as the alternative. | low |
| 2 | 644 | first line, "dans … /Im Π̂₀" | `\mathrm{GL}(2,\widehat{\mathbb Z})` | `\mathrm{Gl}(2,\widehat{\mathbb Z})` | s644_c7: capital G followed by a looped lower-case l, his "Gl(2,Z)^" of scan 651 (already `\mathrm{Gl}` in the first pass there). | medium |
| 3 | 644 | second diagram, lower object | `\mathrm{GL}(2,\mathbb Z/4\mathbb Z)` | `\mathrm{Gl}(2,\mathbb Z/4\mathbb Z)` | Full page: same G + looped l. | medium |
| 4 | 644 | last line, "(cf p. …)" | `\unsure{554\|594}` | `\unsure{594\|554}` | Full page: the middle digit has a closed upper loop and a tail, like 9; the crop cuts the loop, so 554 stays as alternative. | low |
| 5 | 645 | "centre de 𝒢⁺/Π ≃ … est trivial" | `\unsure{\mathfrak S_3\|\mathcal G_3}` | `\mathcal G_3` | Full page: the looped 𝒢 of 𝒢⁺/Π on the same line, with subscript 3. Package 606–624 (checked, scans 616–617) settled the same letter as 𝒢₃. | medium |
| 6 | 645 | inserted correction, struck word after "Ker(ε₃\|M″!)" | `\deleted{\unsure{précisé}}` | `\deleted{mais}` | s645_c4: a struck "mais", the same shape as the "mais M″!₀" with which the sentence resumes in the margin; the parenthesis was squeezed in after it. | medium |
| 7 | 645 | margin, "(qui contient en fait μ …)" | `\unsure{;\|!}` | `;` | s645_c4: a dot over a comma. | medium |
| 8 | 645 | cancelled diagram D_ρ ↪ N_ρ*/M°(…) | `-\unsure{\bar\jmath\|\jmath}` | `-\bar\jmath` | Full page: the bar over j is written as in the other two M°(−j̄) of the page. | medium |
| 9 | 645 | cancelled "Admettons provisoirement ce …," | `fait` | `\unsure{fait\|point}` | Full page: the word after "ce" has a descender at its start and a short body; "point" (the word of "Admettant ce point" on scan 646) is as likely as "fait". Alternative added. | low |
| 10 | 646 | "Je vois mieux — … la" | `\unsure{essayons}` | `essayons` | Full page: e-s-s-a-y-o-n-s legible. | medium |
| 11 | 646 | cancelled Proposition, filtration of 𝒢∧/Π₀∧ | `\unsure{\mathfrak S_3\|\mathcal G_3}` | `\mathcal G_3` | As row 5. | medium |
| 12 | 646 | cancelled Proposition, filtration of M | `\unsure{\mathfrak S_3\|\mathcal G_3}` | `\mathcal G_3` | As row 5. | medium |
| 13 | 646 | Ker(N_ρ* → 𝒢/Π₀) … N_ρ* ∩ M″!₀ | `\unsure{\simeq\|=}` | `=` | Full page: two heavy bars, no tilde. | medium |
| 14 | 646 | "et comme N_ρ* ∩ M₀! = Z!_{ρ0} = …" | `M^!(-\bar\jmath)` | `M^{\prime}(-\bar\jmath)` | Full page: one short stroke over M, without the dot of the "!" written on M₀! and Z!_{ρ0} in the same line; it matches the M′ of the next display (row 15). Scan 650 lists M′(−j̄), M‴(−j̄) among the subgroups. | medium |
| 15 | 646 | "le noyau cherché est égal à : … ∩ M″ = M°(−j̄)" | `M^{\unsure{\prime\|!}}(-\bar\jmath)` | `M^{\prime}(-\bar\jmath)` | s646_c3: one prime, no dot. With M′ = Ker ε₃, M″ = Ker ε₂ and M° = M′ ∩ M″ (scan 643: M°(0) = {ε₂ = ε₃ = 1}) the display is an identity. | medium |
| 16 | 646 | "on a bien un hom injectif …" | `\unsure{(46)\|(45)}` | `(46)` | Full page: the digit closes in a lower loop (6), unlike the 5 of "(45)" on scan 644; (46) is N_ρ*/M°(−j̄) → 𝒢/Π₀, stated on scan 643. | medium |
| 17 | 647 | (49), label under M(0) | `M_{0,\unsure{3\|1}}^{\sim}(0)` | `M_{0,3}^{\sim}(0)` | Full page: the subscript is the 3 written as in 𝒢₃. | medium |
| 18 | 647 | (49), γ_{ρ,σ} ≝ … | `\overset{\mathrm{d\acute ef}}{=}` | `\overset{\mathrm{dfn}}{=}` | Full page: "dfn" over the sign, the abbreviation of (17), (27), (29); the "def" over (48) on the same page is kept. | medium |
| 19 | 647 | (49), γ_{ρ,σ} ≃ … (← M(0)) | `\unsure{\widetilde{\Gamma}_{\mathbb Q}\|\widetilde{\Pi}_{\mathbb Q}}` | `\widetilde{\Gamma}_{\mathbb Q}` | One stem with the top bar running right and no second leg; scan 651 "Γ_Q~ = M/𝒢⁺" shows the letter plainly. Package 606–624 (checked) writes Γ̃_Q. | medium |
| 20 | 647 | (52), first row | same | `\widetilde{\Gamma}_{\mathbb Q}` | As row 19. | medium |
| 21 | 647 | (52), insertion over γ_{ρ,σ} | same | `\widetilde{\Gamma}_{\mathbb Q}` | As row 19. | medium |
| 22 | 647 | (49), last row | `N_\sigma^{\unsure{*}}` | `N_\sigma^{*}` | Full page: the same star as on N_ρ*. | medium |
| 23 | 648 | (53), sign under ⊂ | `\Vert\,\mathrm{d\acute{e}f}` | `\Vert\,\mathrm{dfn}` | s646_c3 (tile 4): "‖dfn". | medium |
| 24 | 648 | (53), first factor | `\unsure{N_{\rho}^{?}}` | `N_{\rho}^{?}` | s646_c3: the exponent curls at the top (?), unlike the straight ! on Z!_{σ0}; the N is retraced, not doubtful. | medium |
| 25 | 648 | central embeddings, lower branch | `\mathcal{G}_{\rho,\sigma}^{+}\equiv\mathcal{G}^{+}` | `\mathcal{G}_{\rho,\sigma}^{+}=\mathcal{G}^{+}` | Full page: two bars. | medium |
| 26 | 648 | last line, "d'où des … canoniques" | `\unsure{hom.}` | `\unsure{homs\|hom.}` | Full page: a final s after "hom"; plural after "des". | low |
| 27 | 649 | left margin, Γ^♮_{ρ,σ} ≝ … | `\overset{\mathrm{d\acute{e}f}}{=}` | `\overset{\mathrm{dfn}}{=}` | s646_c3 (tile 5, rotated): "dfn". | medium |
| 28 | 649 | first prose word | `\unsure{Évidemment}` | `Évidemment` | Full page: legible. | medium |
| 29 | 650 | (60), label under the brace | `\unsure{\widetilde{\Gamma}_{\mathbb{Q}}\|\widetilde{\Pi}_{\mathbb{Q}}}` | `\widetilde{\Gamma}_{\mathbb{Q}}` | As row 19. | medium |
| 30 | 651 | heading | `\unsure{raffinements\|raffinement}` | `raffinement` | s651_c1 and s646_c3: the word ends "-ment" and the full stop follows; no s. Circle table: "récapitulation et raffinement". | high |
| 31 | 651 | "Ce sont celles de … 1°) (p. 577)" | `\unsure{V\|IV}` | `V` | s646_c3: a retraced V. Circle table: §49 V begins at p. 577, the page cited; scan 659 has "Procédant comme page 577". | medium |
| 32 | 651 | end of (1), "invariant dans 𝒢…" | `\mathcal{G}^{\unsure{*}}` | `\mathcal{G}^{\unsure{*\|+}}` | s652_c1: a small cross with one extra stroke; + is as possible as *. Alternative added. | low |
| 33 | 651 | "dans … = M/𝒢⁺" | `\unsure{\widetilde{\Gamma}_{\mathbb{Q}}\|…}` | `\widetilde{\Gamma}_{\mathbb{Q}}` | scan651_b: Γ with tilde, plainly. | medium |
| 34 | 651 | "un sous-groupe image … ouvert" | `\unsure{\widetilde{\Gamma}_{\mathbb{Q}}\|…}^{♮}` | `\widetilde{\Gamma}_{\mathbb{Q}}^{\unsure{\natural\|\sharp}}` | As row 33. | medium |
| 35 | 652 | "ρ et σ,τ n'engendrent … 𝒢⁺ que modulo groupe fini" | `pas alors` | `\unsure{peut être\|pas alors}` | s652_c1, s652_c2: a p with a flat stroke, then a hatted letter and a crossed t, the same two shapes as "peut être" one line below; "n'engendrent pas … que modulo" would contradict the "i.e. ils engendrent peut être seulement un ss-groupe ouvert" that follows. | medium |
| 36 | 652 | "seulement un … ouvert" | `s-groupe` | `ss-groupe` | s652_c2: two linked s, as in "d'un ss-groupe" on scan 657. | medium |
| 37 | 652 | "J'hésite à introduire … notations" | `ces` | `des` | s652_c2: the first letter has the ascender loop of d. | medium |
| 38 | 653 | (4), sign under Z_{ρ,σ} ⊂ … | `\Vert\,\mathrm{def}` | `\Vert\,\mathrm{dfn}` | s652_c2: "‖dfn". | high |
| 39 | 653 | "τ(σ) = −…" | `\unsure{\sigma}` | `\unsure{\sigma\|\varepsilon}` | s653_c2: the last letter is open like ε and has no top bar; σ fits τσ = −στ of scan 655. Alternative added. | low |
| 40 | 653 | "il est clair que la condition … définit un sous-groupe" | `\unsure{c')\|b')}` | `c')` | s653_c2: a plain c, no ascender. b′) is meant (see notes). | medium |
| 41 | 654 | (6), second added line | `\unsure{\alpha_{\mathcal G}\|\varepsilon_{\mathcal G}}(\alpha')` | `\alpha_{\mathcal G}(\alpha')` | s654_c1: the same α as in α′ beside it, not the ε of the line above; a slip for ε_𝒢. | medium |
| 42 | 654 | "Prouvons … que u′u ∈ g" | `\unsure{Prouvons} que` | `\unsure{Prouvons} \deleted{$\unsure{\varepsilon_3}$} que` | s654_c1: a struck ε₃ written after the verb. | low |
| 43 | 655 | "qui implique u′(σ)˙ = … σ̇" | `\deleted{\unsure{\varepsilon_2'}}\inserted{\unsure{(\varepsilon'_2)^{\cdot}}}\dot{\sigma}` | `\varepsilon'_2\,\deleted{\text{\illegible{1}}}\dot{\sigma}` | s655_c1: ε with the prime above and 2 below stands unstruck; a struck blot follows; there is no dotted (ε′₂)˙. | medium |
| 44 | 655 | "choisir ε de façon que −εε′₃ = …" | `\unsure{\dot{\varepsilon}'_2\|\varepsilon'_2}` | `\varepsilon'_2` | Half image: prime, no dot. | medium |
| 45 | 655 | last line, "… conclusion dans le cas premier" | `\overline{\mathrm m}` | `\overline{\mathrm M}` | Half image: capital M with bar opening the sentence. | medium |
| 46 | 656 | example a) | `\operatorname{SL}(2,\mathbb{Z})^{\wedge}` | `\mathrm{Sl}(2,\mathbb{Z})^{\wedge}` | Half image: S + looped lower-case l, as in his Gl. | medium |
| 47 | 656 | right margin, first word | `\unsure{expliciter}` | `expliciter` | s656_c1 (rotated): legible. | medium |
| 48 | 656 | right margin, (ε₀,1,1,1) … Z_{ρ,σ} | `\unsure{\notin\|\in}` | `\notin` | s656_c1: ∈ with a slash. | medium |
| 49 | 657 | "se fait par le …" | `\unsure{caractère}` | `caractère` | s657_c2. | medium |
| 50 | 657 | exponent on ε₂ | `\unsure{\#\|\prime}` | `\unsure{*\|\#}` | s656_c3 (tile 3): a star-shaped blot, no prime; perhaps a call mark (see notes). | low |
| 51 | 657 | (17) | `\overset{\mathrm{def}}{=}` | `\overset{\mathrm{dfn}}{=}` | Half image 657_b: "dfn". | medium |
| 52 | 658 | NB margin, "cf. exemple c) ci-dessus…" | `\unsure{\ldots}` | `\ldots` | s658_c1: three dots. | medium |
| 53 | 659 | "Procédant comme page …" | `\unsure{577\|579}` | `577` | Half image: two crossed 7s, as in "(p. 577)" on scan 651; Circle table: §V at 577. | medium |
| 54 | 661 | Proposition, noun over "couples" | `\unsure{quadruples\|quadrupliens}` | `\unsure{quadruplets\|quadruples}` | s661_c1: the ending after "quadru-" runs to -lets/-les; "quadrupliens" is not a word, and Grothendieck writes "quadruplet" (CSG draft l. 7304). | low |
| 55 | 662 | cancelled line, first word | `\unsure{injectif}` | `\unsure{induit\|injectif}` | s662_c1: an ascender (d) in mid-word and no j or f descender. | low |
| 56 | 662 | Remarque, "Cette … fait apparaître" | `\unsure{projection\|présentation}` | `proposition` | Half image and s662_c1: two p descenders and the ending -sition; the remark follows the Proposition (38)–(44). | medium |
| 57 | 662 | Remarque, "la … construction faite ici" | `la construction` | `la \deleted{\illegible{1}} construction` | s662_c1: a short struck word between "la" and "construction". | low |
| 58 | 662 | last line, after "pr" | `\unsure{desserrer\|donner} le \unsure{moule\|modèle}` | `dessus le \unsure{marché}` | s652_c2, s662_c1: "dessus" with double s, a retraced "le", then a word ending -ché with its accent: "pr dessus le marché" (par-dessus le marché). | medium |

Counts: 58 changes — 2 high, 45 medium, 11 low.

## Places still unresolved

1. 644: first word v|u; "factorisé" (ending); the overwritten pair in the last paragraph (upper word, read "de groupe top."; the struck lower word begins like "exp…" rather than "régulière"); "automs"; M(ω|0); p. 594|554; the struck object under (ℤ/4ℤ)* (perhaps Gl(2,ℤ/2ℤ)).
2. 645: "En fait, on … reconnaît" (a short word stands between "on" and the verb); "en fait|effet μ;"; 𝒢/Π₀ or 𝒢[Π₀] on line 2; "ce fait|point".
3. 646: the exponents ∧/* in the first filtration; "des" retraced or struck before "isomorphismes".
4. 647: in (50) the ink has N_σ* on both rows (N_ρ* expected for N_ρ?); kept as written.
5. 648: the closing mark after 𝒢⁺ in the embeddings.
6. 649: γ|Γ at the end of (57); μ_σ|μ_ρ in "μ_ρ×𝒢⁺_{ρ,σ}/μ_…"; "bisection"; the labels of (58).
7. 650: the subscript of M!_a[0]; M(ω|0) in the inserted equalities; {M(½)}.
8. 651: the subscript 0|a of 𝒢^♮ in (1) (a small round mark, sometimes filled); formé|formés; the cancelled normalis- ending; "néct.".
9. 652: the overwritten first symbol 𝒢; the exponent +|* in line 5.
10. 653: right margin "cf. page 635 suite … cette condition"; the cancelled left margin (wording); g or G for the auxiliary groups.
11. 654: "on gagne" (perhaps "on y gagne"); product or quotient 𝒢^♮_τ𝒢⁺; ⇒|↪.
12. 655: the arrangement of "On distingue encore deux cas" over the cancelled "on aurait, puisque στ = −τσ".
13. 656: left-margin diagram (tilde on M_{0,3}, superscripts, circled 𝒢_{0,3}); the struck margin block at (14); "p.r.v.|p.r. au"; the letters b)/a) of the cancelled remark are as written (see notes).
14. 657: cancelled margins (induise|produise, "nouvelle version", trop/petit); the mark after μ in (16), more likely an insertion caret for the parenthesis than a struck ⊂; the tail of the final remark.
15. 658: "ce qui surprend"; "déduites"; the second kernel of the cancelled (24).
16. 659: "ds.|dans"; "me|on ferait"; i_{L₀,S₀G|G}; the label "(25)" overlapped by the margin note.
17. 660: "noté" in (34).
18. 661: ε₂|ε_τ in (39) b); objects of the cancelled corollary.
19. 662: i_{L₀,SG|S₀G}; "(on m̄ a|en besoin"; "définirait|définissait"; "marché"; words of the cancelled sentence below (42).
20. Global: the recurring zigzag exponent stays `\unsure{\natural|\sharp}`. On these pages it is one stroke (down, slant, down), closer to a written ♮ than to ♯, but the sign should be fixed once for the whole series, not here. Two-lobed arguments of M stay ω|0.

## Witnesses' own errors noticed

None of the witnesses has the text of these scans, so no reading could be collated. In the Carmona–Kuenzer text the
table line "49. Les groupes ρ,σ généraux" and the running head "§ 49. — LES GROUPES ρ,σ GÉNÉRAUX" have lost the M of
M_{ρ,σ}, which the heading on scan 651 has. The Circle table's "récapitulation et raffinement de la construction
précédente" is the author's later wording of the heading that scan 651 writes "récapitulation, raffinement." (not an error).
