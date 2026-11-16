# Notation and doubts — MPL 57, scans 271–315

## Package notation table

This is the final pre-context notation register. The primary reader compared the recurring forms during the second visual reading and revisited the differing C/Q/Z alphabets before the freeze; local differences that the ink does not resolve remain marked in the transcription. Upright `\operatorname{Pic}` and `\mathrm{Pic}` render the same alphabet; their choice does not distinguish two manuscript objects.

| Visible convention | LaTeX rendering | Scans / decision |
|---|---|---|
| Ordinary Latin capitals and lower-case letters | `X,Y,S,A,B,C,D,F,G,L,M,N,V,W`; `x,y,s,t,p,n,u,v` | Case retained, including `F_0` with `B_0` alternative on 289. |
| Typewritten mathematical letters | Ordinary math letters; printed indices retained | 271, 273, 295–296, 299, 301, 303, 307, 312; missing typewritten arrows/signs on 307 are not supplied. |
| Doubled field/ring capitals | `\mathbb C`, `\mathbb Q`, `\mathbb Z` | 272, 281, 285, 289, 291–292 compared together; Q on 281 remains `\unsure{\mathbb Q\|\mathbf Q}`. The forms agree with 296, 300, 302. |
| Script L, O, D, P, R | `\mathcal L`, `\mathcal O`, `\mathcal D`, `\mathcal P`, `\mathcal R` | 271, 272 onward, 302, 304; local alternatives for R/P and L/F retained. |
| Gothic M | `\mathfrak M` | 291, distinct from ordinary M in the final covariant formula and on 292; first occurrence marks the alphabet uncertainty. |
| Gothic g versus script T | `\unsure{\mathfrak g\|\mathcal T}` | 294, 297; the same preferred letter is used, with visible underlining on 294 only. |
| Gothic X versus script X | `\unsure{\mathfrak X\|\mathcal X}` | 300; retained as an unresolved alphabet distinction. |
| Greek letters | `\alpha,\beta,\gamma,\lambda,\mu,\nu,\rho,\sigma,\tau,\varphi,\Phi,\xi,\Gamma,\Lambda,\Omega` | Original case kept; gamma/sigma and Gamma/sigma ambiguities marked locally in 297, 304. |
| One / two underline strokes | `\uline{...}`, `\uuline{...}` | Both math and words; nested legacy underline encodings were converted without changing the stroke count. The two O underlines on 285 remain doubtful. |
| Pic / Nér / NS / Hom | Upright names, with one or two underlines as drawn | 275–290; no global replacement of single by double underlining. |
| Accented Nér and Néron in formulas | `\operatorname{N\acute{e}r}`, `\mathrm{N\acute{e}ron}` | Encoding preserves the written accent and avoids a dropped glyph in pdfLaTeX. French prose accents remain UTF-8. |
| Overwritten Pol → Nér | `\deleted{...}\inserted{...}` | 275–280; untouched instances of Pol remain unchanged. |
| Prime, double prime, plus | `'`, `''` or `\prime\prime`, `+` | 275–281; prime strokes were checked independently of word-ending exclamation-like abbreviation strokes. No mathematical exclamation exponent is inferred. |
| Zero / tau / positive part | `^0`, `^\tau`, `^+` | Kept distinct throughout; crossed superscripts retain deletion and doubt markers. |
| Two loops / infinity | `\unsure{00\|\infty}` | 294 and 311; the separate-loop reading leads in both. |
| Action invariants / coinvariants | `A^\Gamma`, `A_\Gamma`, `t_{A'}`, `(t_A)'` | 284–288, 297; exponent/subscript and position of the prime are not normalized. |
| Left torsion prefix | `{}_nM`, `{}_pM`, `{}_{p^n}M`, `{}_2A'` | 285, 291–292, 313; not rewritten as a right subscript. |
| Tate-type functors | `T_p` and `T^p` | 291–292; lower and upper p remain distinct. |
| Hats and checks | `\widehat A`, `\widehat X`, `\widehat Y`, `\check V` | 272, 294, 297; doubtful letters under the marks are not harmonized from meaning. |
| Structure sheaf and differential underlining | `\uline{\mathcal O}`, `\uline{\Omega}` where drawn | 287–288, 294, 302, 304, 315; plain and underlined occurrences remain locally distinct. |
| Quotient styles | `\mathbb Z/2\mathbb Z`, `\mathbb Z/2`, `\mathbb Z_2` | 285, 300, 302; the shortened quotient/subscript forms are not expanded. |
| Products / tensor products | `\times`, `\otimes`, `\prod_{Y/S}` | Products on 287 and the relative product on 283–284 retained; no substitution of direct-sum notation. |
| Limits | `\varprojlim`, `\varinjlim`, with written indices | 291–292, 296; direction is read from the source arrows. |
| Inequalities and inclusions | `\leq,\geq,\subset,\not\subset,\ne` | 289–292, 296, 313; the third hypothesis on 289 was rechecked as an equality, while its subscript remains doubtful. |
| Plain line versus arrow | `\mathbin{\unsure{-\|\to}}`, or `\arrow[...,dash]` | 272, 289, 297, 300, 309; doubtful heads are not supplied confidently. |
| Isomorphism signs | `\simeq`, `\overset{\sim}{\longrightarrow}` | Kept separate from equality and bare arrows. |
| Equals-like shorthand | `=`, `\overline{=}`, with local `\unsure` | 280, 285, 286, 309, 310, 313; never expanded to the word “même” in the transcription. |
| Double quotation marks | Two backticks and two apostrophes | French and English quoted phrases; two ditto marks on 313 remain unexpanded. |
| Guillemets | `«` and `»` | The angular pair at the end of 288 is retained. |
| Printed running numbers | `\margin{...}` | 271, 273, 312; the damaged first digit in 312 remains doubtful. |
| Printed page numbers and lower pencil foliation | `\mspage{...}` | Printed surrounding dashes are literal text; the lower foliation is retained separately, even where the printed sequence is out of order. |
| Cancellations, insertions and marginal matter | `\deleted`, `\inserted`, `\margin` | Includes overwritten symbols and partial words; crossed passages are not silently discarded. |
| Diagrams / non-diagram line work | `\diagram{\begin{tikzcd}...}` / `\figure{\begin{tikzpicture}...}` | Objects and labels are transcribed; hand-drawn line shapes are approximations of their visible relative geometry. |

## Current doubts

Every `\unsure` and `\illegible` occurrence in the final page files is indexed below, in scan order. “Line” gives the approximate location through the numbered line of the page fragment, plus a nearby manuscript phrase when available; long manuscript paragraphs can occupy one LaTeX line. Confidence concerns the proposed reading, not the mathematical plausibility: **medium** means a plausible ink reading with a residual ambiguity, **low** means substantial ambiguity or overwritten/faint ink; no uncertainty has been upgraded merely because the mathematics fits.

The older candidate readings in `records/` document the working history. Where they differ, this table and the frozen page fragment give the final pre-context reading; a dash in the alternatives column means that no second positive reading is proposed, not that the first is certain.

| File / cote | Scan | Line approximately | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|---|
| 57.pdf / 57 | 271 | LaTeX line 12; beside \|D\| | ` $\sim W$ ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` ? ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` et ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` \operatorname{Sp} ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` \operatorname{Sp} ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` est ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2; opening | ` mor! ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` C'est ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 2 | ` un ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4; (i), first line | ` tte image universelle ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` -- ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` n ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` ? ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` on a ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` \Longleftrightarrow ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4; (i), bracket | ` élément ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` - ` | ` \to ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` n ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` - ` | ` \to ` | low |
| 57.pdf / 57 | 272 | LaTeX line 4 | ` n ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 6 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 272 | LaTeX line 8 | ` \widehat Y ` | ` \widehat X ` | low |
| 57.pdf / 57 | 272 | LaTeX line 10 | ` N.B. ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 12 | ` pt ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 16; last question | ` Que se passe-t-il si ` | ` — ` | medium |
| 57.pdf / 57 | 272 | LaTeX line 16; last line | ` Alg. ` | ` — ` | low |
| 57.pdf / 57 | 272 | LaTeX line 17; left margin | ` Mumford's ` | ` — ` | medium |
| 57.pdf / 57 | 274 | LaTeX line 2; title line 1 | ` Polarisation ` | ` Polarisations ` | medium |
| 57.pdf / 57 | 274 | LaTeX line 4; title line 2 | ` Sévéri ` | ` Séveri ` | medium |
| 57.pdf / 57 | 275 | LaTeX line 2; definition, fibre condition | ` équivalent ` | ` — ` | medium |
| 57.pdf / 57 | 275 | LaTeX line 2; definition, Deux | ` éléme ` | ` — ` | medium |
| 57.pdf / 57 | 275 | LaTeX line 4 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 4; second paragraph | ` équivalts ` | ` — ` | medium |
| 57.pdf / 57 | 275 | LaTeX line 4; overwritten notation, all instances | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 4 | ` \operatorname{N\acute{e}r} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 4; deleted flatness clause | ` qu. cpt ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 4; base-change paragraph | ` changt ` | ` — ` | medium |
| 57.pdf / 57 | 275 | LaTeX line 4 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 6; overwritten notation, all instances | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 6 | ` \operatorname{N\acute{e}r} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 6; overwritten notation, all instances | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 6 | ` \operatorname{N\acute{e}r} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 10; sheaf condition deletion | ` qu. cpts ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 10; overwritten notation, all instances | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 10 | ` \operatorname{N\acute{e}r} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 10; overwritten notation, all instances | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 275 | LaTeX line 10 | ` \operatorname{N\acute{e}r} ` | ` — ` | low |
| 57.pdf / 57 | 276 | LaTeX line 4; opening | ` élémt ` | ` — ` | medium |
| 57.pdf / 57 | 276 | LaTeX line 4 | ` X/S ` | ` — ` | low |
| 57.pdf / 57 | 276 | LaTeX line 4; overwritten names | ` \operatorname{Pol} ` | ` — ` | medium |
| 57.pdf / 57 | 276 | LaTeX line 8; overwritten names | ` \operatorname{Pol} ` | ` — ` | medium |
| 57.pdf / 57 | 276 | LaTeX line 8; before category (Sch) | ` (\operatorname{Ens}) ` | ` — ` | low |
| 57.pdf / 57 | 276 | LaTeX line 8; overwritten names | ` \operatorname{Pol} ` | ` — ` | medium |
| 57.pdf / 57 | 276 | LaTeX line 8 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 276 | LaTeX line 8; last deletion | ` qu. cpt ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 4 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 4; Corollaire 1 deletion | ` représentable ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 6 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 6; Corollaire 2 insertion deletion | ` plat et ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 6 | ` f_*(\mathcal O_X)=\mathcal O_S ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 7; left margin | ` Nér géo ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 9; after plat in last paragraph | ` sur ` | ` — ` | low |
| 57.pdf / 57 | 277 | LaTeX line 9 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 4; cancelled opening | ` Noter qu'une ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 4 | ` \operatorname{Pic}(X/S) ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 4 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 279 | LaTeX line 4 | ` no. ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 4; cancelled last line | ` qui est ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 4 | ` Physically unreadable: estimated 2 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 279 | LaTeX line 6; left cancelled note | ` défini par ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 6 | ` Physically unreadable: estimated 2 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 279 | LaTeX line 6; left cancelled note | ` inversible ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 6 | ` Physically unreadable: estimated 2 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` X' ` | ` X ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` X/S ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` 0 ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` pseudo ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8; terminology replacements | ` néronisations ` | ` — ` | medium |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8; after multiplicatif cancellation | ` donc ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 279 | LaTeX line 8; after contravariant functor | ` au moins un préfaisceau ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 9 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 9 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 11 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 11 | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 11; after Un élément de | ` On pose ` | ` — ` | medium |
| 57.pdf / 57 | 279 | LaTeX line 11 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 11 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 11 | ` pseudo ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 11; terminology replacements | ` néronisations ` | ` — ` | medium |
| 57.pdf / 57 | 279 | LaTeX line 13 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 13 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 15; bottom insertion deletion | ` rel. ample ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 15 | ` que ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 15; last line | ` équiv. à $0$ ` | ` — ` | low |
| 57.pdf / 57 | 279 | LaTeX line 15; last line | ` rel. ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 2 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 2 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 2 | ` = ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 2 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 2 | ` l'i ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 2; first paragraph | ` torsion. ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 4 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 4 | ` grp ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 4; bracketed quotient condition | ` graphe ` | ` — ` | medium |
| 57.pdf / 57 | 280 | LaTeX line 4; middle deletions | ` on prouve ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 4 | ` \operatorname{Pol} ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 4; middle deletions | ` Alors ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 4; middle deletions | ` en outre ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 9; before amples | ` abs ` | ` — ` | low |
| 57.pdf / 57 | 280 | LaTeX line 9 | ` + ` | ` — ` | low |
| 57.pdf / 57 | 281 | LaTeX line 2; after polarisation | ` positive ` | ` — ` | low |
| 57.pdf / 57 | 281 | LaTeX line 2; left insertion | ` plongé dans le groupe ` | ` — ` | medium |
| 57.pdf / 57 | 281 | LaTeX line 4 | ` \mathbb Q ` | ` \mathbf Q ` | medium |
| 57.pdf / 57 | 281 | LaTeX line 4; cone paragraph ending | ` intérieurs ` | ` — ` | medium |
| 57.pdf / 57 | 281 | LaTeX line 4 | ` --- ` | ` — ` | medium |
| 57.pdf / 57 | 283 | LaTeX line 2; title | ` Exemples ` | ` — ` | medium |
| 57.pdf / 57 | 283 | LaTeX line 7 | ` Y, ` | ` — ` | medium |
| 57.pdf / 57 | 283 | LaTeX line 7 | ` , ` | ` / ` | medium |
| 57.pdf / 57 | 283 | LaTeX line 10 | ` \Gamma(S,\prod_{Y/S}\uline{\operatorname{Pic}}) ` | ` — ` | medium |
| 57.pdf / 57 | 283 | LaTeX line 19; insertion after à droite | ` et splitting ` | ` — ` | low |
| 57.pdf / 57 | 283 | LaTeX line 29 | ` \tau ` | ` 0 ` | medium |
| 57.pdf / 57 | 284 | LaTeX line 2; top deletion | ` on suppose que ` | ` — ` | low |
| 57.pdf / 57 | 284 | LaTeX line 7 | ` \mathrm{pr}_1 ` | ` — ` | low |
| 57.pdf / 57 | 284 | LaTeX line 21; left vertical margin | ` Sévéri ` | ` — ` | medium |
| 57.pdf / 57 | 284 | LaTeX line 30 | ` --- ` | ` — ` | low |
| 57.pdf / 57 | 284 | LaTeX line 30; cancelled bottom clause | ` le groupe ` | ` — ` | low |
| 57.pdf / 57 | 284 | LaTeX line 30; cancelled bottom clause | ` qui ` | ` — ` | low |
| 57.pdf / 57 | 284 | LaTeX line 30 | ` Physically unreadable: estimated 3 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 284 | LaTeX line 30 | ` opère par translations ` | ` — ` | low |
| 57.pdf / 57 | 285 | LaTeX line 10 | ` $=$ ` | ` — ` | medium |
| 57.pdf / 57 | 285 | LaTeX line 10; before simple | ` séparé ` | ` — ` | low |
| 57.pdf / 57 | 285 | LaTeX line 11; cancelled sentence after surface | ` Cela étant ` | ` — ` | low |
| 57.pdf / 57 | 285 | LaTeX line 11 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 285 | LaTeX line 11 | ` \uline{\mathcal O} ` | ` \mathcal O ` | medium |
| 57.pdf / 57 | 285 | LaTeX line 15 | ` k ` | ` K ` | medium |
| 57.pdf / 57 | 285 | LaTeX line 15 | ` \uline{\mathcal O} ` | ` \mathcal O ` | medium |
| 57.pdf / 57 | 285 | LaTeX line 15; penultimate sentence | ` égales ` | ` — ` | medium |
| 57.pdf / 57 | 286 | LaTeX line 4 | ` \rho ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 5; N.B. opening | ` Il n'était ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 5 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 286 | LaTeX line 8 | ` A' ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 8 | ` A' ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 11; right marginal gloss | ` bi-inversibles ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 12; left marginal note | ` sous les ` | ` — ` | medium |
| 57.pdf / 57 | 286 | LaTeX line 17 | ` tout ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 17; middle hypothesis | ` ensemblist! ` | ` — ` | medium |
| 57.pdf / 57 | 286 | LaTeX line 33 | ` $=$ ` | ` — ` | low |
| 57.pdf / 57 | 286 | LaTeX line 33 | ` M ` | ` A ` | low |
| 57.pdf / 57 | 287 | LaTeX line 2 | ` p_* ` | ` f_* ` | low |
| 57.pdf / 57 | 287 | LaTeX line 9; paragraph after first display | ` plus ` | ` précis ` | low |
| 57.pdf / 57 | 287 | LaTeX line 11 | ` p_* ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 13 | ` $(*)$ ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 22 | ` H^0(X/k,\Omega^1_{X/k}) ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 24; last paragraph deletions | ` enfin ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 24; last paragraph deletions | ` de cette ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 24; last paragraph deletions | ` \operatorname{cor} ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 24; last two lines | ` valeur du paramètre ` | ` — ` | medium |
| 57.pdf / 57 | 287 | LaTeX line 24; last paragraph deletions | ` par un ` | ` — ` | low |
| 57.pdf / 57 | 287 | LaTeX line 24; last two lines | ` spécialisant ` | ` — ` | medium |
| 57.pdf / 57 | 288 | LaTeX line 2 | ` th ` | ` — ` | medium |
| 57.pdf / 57 | 289 | LaTeX line 13 | ` a) ` | ` i) ` | low |
| 57.pdf / 57 | 289 | LaTeX line 13 | ` \ne 0 ` | ` — ` | low |
| 57.pdf / 57 | 289 | LaTeX line 14 | ` a') ` | ` ii) ` | low |
| 57.pdf / 57 | 289 | LaTeX line 15 | ` a'') ` | ` — ` | low |
| 57.pdf / 57 | 289 | LaTeX line 15; third condition label | ` iii) ` | ` a'') ` | low |
| 57.pdf / 57 | 289 | LaTeX line 15 | ` 1 ` | ` 0 ` | low |
| 57.pdf / 57 | 289 | LaTeX line 29 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 289 | LaTeX line 29; cancelled bracket | ` sinon ` | ` — ` | medium |
| 57.pdf / 57 | 289 | LaTeX line 29 | ` F_0 ` | ` B_0 ` | low |
| 57.pdf / 57 | 289 | LaTeX line 31; last insertion | ` ordre ` | ` — ` | low |
| 57.pdf / 57 | 290 | LaTeX line 2; top insertion | ` fini ` | ` — ` | low |
| 57.pdf / 57 | 290 | LaTeX line 2; opening second line before que | ` d'acc. ` | ` d'accord ` | low |
| 57.pdf / 57 | 290 | LaTeX line 10 | ` ( ` | ` — ` | low |
| 57.pdf / 57 | 290 | LaTeX line 10 | ` ) ` | ` — ` | low |
| 57.pdf / 57 | 290 | LaTeX line 12; deleted word before spéciale | ` géné ` | ` générique ` | low |
| 57.pdf / 57 | 291 | LaTeX line 4; cancelled transition | ` Les ` | ` — ` | low |
| 57.pdf / 57 | 291 | LaTeX line 4 | ` \mathfrak M ` | ` M ` | low |
| 57.pdf / 57 | 291 | LaTeX line 4 | ` p ` | ` — ` | low |
| 57.pdf / 57 | 291 | LaTeX line 5 | ` Les $\mathfrak M$ en question ` | ` — ` | low |
| 57.pdf / 57 | 291 | LaTeX line 11 | ` n ` | ` — ` | low |
| 57.pdf / 57 | 291 | LaTeX line 11 | ` $n\in\mathbb Z$ ` | ` — ` | low |
| 57.pdf / 57 | 292 | LaTeX line 6; item c | ` anti- ` | ` — ` | low |
| 57.pdf / 57 | 292 | LaTeX line 6; item c | ` équiv. ` | ` — ` | low |
| 57.pdf / 57 | 292 | LaTeX line 6; end of item c | ` catégories ` | ` — ` | low |
| 57.pdf / 57 | 292 | LaTeX line 8 | ` n ` | ` — ` | low |
| 57.pdf / 57 | 292 | LaTeX line 14 | ` $T_p(M)$ ` | ` — ` | low |
| 57.pdf / 57 | 292 | LaTeX line 18; iii | ` épim ` | ` — ` | low |
| 57.pdf / 57 | 294 | LaTeX line 4 | ` 00 ` | ` \infty ` | low |
| 57.pdf / 57 | 294 | LaTeX line 4 | ` U ` | ` S ` | low |
| 57.pdf / 57 | 294 | LaTeX line 5 | ` \uline{\mathfrak g}_{X_0} ` | ` \uline{\mathcal T}_{X_0} ` | low |
| 57.pdf / 57 | 294 | LaTeX line 14 | ` U ` | ` S ` | low |
| 57.pdf / 57 | 294 | LaTeX line 14 | ` 2 ` | ` 1 ` | low |
| 57.pdf / 57 | 294 | LaTeX line 15 | ` d ` | ` — ` | low |
| 57.pdf / 57 | 294 | LaTeX line 15 | ` 2 ` | ` 1 ` | low |
| 57.pdf / 57 | 294 | LaTeX line 15 | ` 2 ` | ` 1 ` | low |
| 57.pdf / 57 | 294 | LaTeX line 21 | ` \sigma ` | ` 0 ` | low |
| 57.pdf / 57 | 294 | LaTeX line 21 | ` (X_0/k) ` | ` — ` | low |
| 57.pdf / 57 | 295 | LaTeX line 5 | ` 0 ` | ` o ` | medium |
| 57.pdf / 57 | 295 | LaTeX line 7 | ` d'ns ` | ` dans ` | medium |
| 57.pdf / 57 | 295 | LaTeX line 13 | ` 0 ` | ` o ` | medium |
| 57.pdf / 57 | 295 | LaTeX line 13; last paragraph | ` khânonique ` | ` khanonique ` | medium |
| 57.pdf / 57 | 296 | LaTeX line 15 | ` $2^e$ ` | ` — ` | medium |
| 57.pdf / 57 | 296 | LaTeX line 23; left margin beside Proposition 2 | ` Non filtré ? ` | ` — ` | medium |
| 57.pdf / 57 | 297 | LaTeX line 3; top tangent factor | ` \Gamma ` | ` \sigma ` | low |
| 57.pdf / 57 | 297 | LaTeX line 4; top tangent factor | ` \Gamma ` | ` \sigma ` | low |
| 57.pdf / 57 | 297 | LaTeX line 5; middle arrow label | ` \text{nul sur le facteur} ` | ` — ` | low |
| 57.pdf / 57 | 297 | LaTeX line 5 | ` t_B ` | ` — ` | low |
| 57.pdf / 57 | 297 | LaTeX line 17 | ` \mathfrak g ` | ` \mathcal T ` | low |
| 57.pdf / 57 | 297 | LaTeX line 18; middle arrow label | ` \text{nul sur le facteur} ` | ` — ` | low |
| 57.pdf / 57 | 297 | LaTeX line 18; central horizontal arrow label, second line | ` \text{provenant de }A ` | ` \text{provenant de }B ` | low |
| 57.pdf / 57 | 297 | LaTeX line 20 | ` \mathfrak g ` | ` \mathcal T ` | low |
| 57.pdf / 57 | 297 | LaTeX line 38 | ` * ` | ` \tau ` | low |
| 57.pdf / 57 | 297 | LaTeX line 38; top tangent factor | ` \Gamma ` | ` \sigma ` | low |
| 57.pdf / 57 | 297 | LaTeX line 39 | ` 2 ` | ` 1 ` | low |
| 57.pdf / 57 | 297 | LaTeX line 39 | ` \to\mu_2 ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 12 | ` re ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 18 | ` X ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 23; after phi1 | ` induit ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 23 | ` $k[t]\to$ ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 25 | ` \varphi_1^*x ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 27 | ` Z ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 27 | ` 1/t ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 29 | ` = ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 40; lower statements about X' and X | ` quasi-affine ` | ` — ` | medium |
| 57.pdf / 57 | 298 | LaTeX line 42; lower statements about X' and X | ` ne l'est pas, car ` | ` — ` | medium |
| 57.pdf / 57 | 298 | LaTeX line 44; Gamma(X,O_X) | ` anneau ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 44; Gamma(X,O_X) | ` sous-anneau ` | ` — ` | low |
| 57.pdf / 57 | 298 | LaTeX line 46 | ` (t,0) ` | ` — ` | low |
| 57.pdf / 57 | 299 | LaTeX line 7 | ` s ` | ` S ` | medium |
| 57.pdf / 57 | 299 | LaTeX line 7 | ` s ` | ` S ` | medium |
| 57.pdf / 57 | 300 | LaTeX line 2; opening corrections | ` ce qui exige ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 2 | ` d'où : ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 2 | ` f_1=f_2 ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 2 | ` g_1 ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 2 | ` g_2 ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 2 | ` g_i ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 2; underlined conclusion | ` pts ` | ` — ` | medium |
| 57.pdf / 57 | 300 | LaTeX line 4 | ` prendre ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 4 | ` permutation ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 4 | ` - ` | ` \to ` | low |
| 57.pdf / 57 | 300 | LaTeX line 5; left margin | ` en réalité ? ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 11 | ` où ` | ` si ` | low |
| 57.pdf / 57 | 300 | LaTeX line 11; quotient comparison | ` comme ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 11; quotient comparison | ` sinon ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 13; bottom corrections | ` tte ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 13; bottom corrections | ` trajectoire ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 13; bottom corrections | ` trajectoire ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 14; last two lines | ` div ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 14 | ` \mathfrak X ` | ` \mathcal X ` | low |
| 57.pdf / 57 | 300 | LaTeX line 14; last two lines | ` contenant le zéro ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 14; last two lines | ` ne contenant pas ` | ` — ` | low |
| 57.pdf / 57 | 300 | LaTeX line 14 | ` \mathfrak X ` | ` \mathcal X ` | low |
| 57.pdf / 57 | 300 | LaTeX line 14 | ` \mathfrak X ` | ` \mathcal X ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2; first three lines | ` applications ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2; first three lines | ` correspondants ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2; first three lines | ` classes de ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` \mathcal L_i ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2; after H1 | ` telles que ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` un ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` \times ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2; gluing isomorphism | ` requis ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2; gluing isomorphism | ` restrictions ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` \uline{L}_i ` | ` \mathcal F_i ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` \simeq ` | ` : ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` Y ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 2 | ` P ` | ` — ` | low |
| 57.pdf / 57 | 302 | LaTeX line 4; last cancellation | ` faisant opérer ` | ` — ` | medium |
| 57.pdf / 57 | 303 | LaTeX line 16; quoted abbreviation for differentials | ` diffelles ` | ` diffélles ` | medium |
| 57.pdf / 57 | 304 | LaTeX line 9 | ` \uline{R} ` | ` \uline{\mathcal R} ` | low |
| 57.pdf / 57 | 304 | LaTeX line 11 | ` p_*(\uline{\mathcal O}_X^*) ` | ` — ` | low |
| 57.pdf / 57 | 304 | LaTeX line 14; third vertical map | ` \gamma ` | ` \sigma ` | medium |
| 57.pdf / 57 | 304 | LaTeX line 36 | ` \uline{\mathcal P} ` | ` \uline{P} ` | low |
| 57.pdf / 57 | 304 | LaTeX line 41 | ` 0 ` | ` \cdot ` | low |
| 57.pdf / 57 | 306 | LaTeX line 2 | ` \varphi ` | ` — ` | low |
| 57.pdf / 57 | 306 | LaTeX line 2 | ` \xi ` | ` 6 ` | low |
| 57.pdf / 57 | 306 | LaTeX line 9 | ` \varepsilon_x ` | ` — ` | low |
| 57.pdf / 57 | 306 | LaTeX line 9 | ` à ` | ` : ` | low |
| 57.pdf / 57 | 306 | LaTeX line 11; crossed clause after trivialement sur Y | ` C'est bien entendu ` | ` — ` | low |
| 57.pdf / 57 | 306 | LaTeX line 13 | ` \Rightarrow ` | ` — ` | low |
| 57.pdf / 57 | 306 | LaTeX line 14; crossed projective-family draft | ` espace projectif ` | ` — ` | low |
| 57.pdf / 57 | 306 | LaTeX line 14; crossed projective-family draft | ` avec famille de dim finie ` | ` avec la famille de dim finie ` | low |
| 57.pdf / 57 | 307 | LaTeX line 2 | ` g ` | ` — ` | low |
| 57.pdf / 57 | 307 | LaTeX line 2; typewriter cancellations | ` réun ` | ` — ` | low |
| 57.pdf / 57 | 307 | LaTeX line 2; first paragraph stable pourla loi | ` pourla ` | ` pour la ` | medium |
| 57.pdf / 57 | 307 | LaTeX line 2; typewriter cancellations | ` $u$ est ` | ` — ` | low |
| 57.pdf / 57 | 307 | LaTeX line 2; typewriter cancellations | ` en part ` | ` — ` | low |
| 57.pdf / 57 | 307 | LaTeX line 4; typewriter cancellations | ` a la fin ` | ` — ` | low |
| 57.pdf / 57 | 307 | LaTeX line 6 | ` 6 ` | ` 5 ` | low |
| 57.pdf / 57 | 307 | LaTeX line 6; typewriter cancellations | ` les ` | ` — ` | low |
| 57.pdf / 57 | 307 | LaTeX line 6; typewriter cancellations | ` tou ` | ` — ` | low |
| 57.pdf / 57 | 308 | LaTeX line 2; title | ` ouvertes ` | ` ouverts ` | medium |
| 57.pdf / 57 | 309 | LaTeX line 9 | ` a' ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 9 | ` b ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 11; a labels and cancellations | ` le schéma ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 11 | ` ouvert ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 14; paragraph after a double prime | ` aurait ` | ` — ` | medium |
| 57.pdf / 57 | 309 | LaTeX line 14; a labels and cancellations | ` simple ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 14; a labels and cancellations | ` normal ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 14 | ` propre ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 14; paragraph after a double prime | ` \overline{=} ` | ` — ` | medium |
| 57.pdf / 57 | 309 | LaTeX line 15; slanted left margin | ` l'équiv ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 15; slanted left margin | ` fait ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 15; slanted left margin | ` que ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 15; slanting left marginal note, final two lines | ` connexe ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 15; slanting left marginal note, final two lines | ` des fibres en soit complet ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 19; quotient notation | ` \mathrm{NSL} ` | ` — ` | medium |
| 57.pdf / 57 | 309 | LaTeX line 23 | ` correspondant ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 28 | ` via ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 28 | ` un ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 28; right of d | ` irrégularité ` | ` irréductibilité ` | low |
| 57.pdf / 57 | 309 | LaTeX line 28; right of d | ` Géom. formelle ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 29; right d, last parenthesis | ` primaires ` | ` prénormales ` | low |
| 57.pdf / 57 | 309 | LaTeX line 32 | ` représentable ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 34 | ` f ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 34 | ` b' ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 34; b prime and last h display | ` Min. ` | ` Dim. ` | low |
| 57.pdf / 57 | 309 | LaTeX line 37 | ` f ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 37; continuity question | ` \ell ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 37; continuity question | ` rang ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 38 | ` comp. connexes ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 40 | ` (X\times_S Y) ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 41 | ` géom. intègres ` | ` géom. connexes ` | low |
| 57.pdf / 57 | 309 | LaTeX line 41; deleted right g | ` nécessaire ` | ` — ` | low |
| 57.pdf / 57 | 309 | LaTeX line 45 | ` k ` | ` u ` | low |
| 57.pdf / 57 | 309 | LaTeX line 45 | ` k ` | ` u ` | low |
| 57.pdf / 57 | 309 | LaTeX line 45; h displays | ` Isom? ` | ` Sous? ` | low |
| 57.pdf / 57 | 309 | LaTeX line 48 | ` k ` | ` u ` | low |
| 57.pdf / 57 | 309 | LaTeX line 48 | ` - ` | ` \to ` | low |
| 57.pdf / 57 | 309 | LaTeX line 48; b prime and last h display | ` \tau ` | ` 0 ` | low |
| 57.pdf / 57 | 309 | LaTeX line 48 | ` k ` | ` u ` | low |
| 57.pdf / 57 | 309 | LaTeX line 48; h displays | ` surjectif ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 2; 1 after normal | ` universellement ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 2 | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 310 | LaTeX line 6 | ` univ. ouvert sur $S$ ? ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 8 | ` univ$^t$ ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 9 | ` en les pts ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 9; right 3, correction | ` dont la ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 9 | ` de ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 9; right 3, correction | ` \tau ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 9 | ` ? ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 11 | ` 4 ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 11 | ` $\uline{\mathrm{Pic}}^\tau$ est de type fini ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 12; 4 under univ ouverte | ``` pour $n$ ``qcq'' ``` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 13 | ` expliciter ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 17; above 6 | ` sans ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 21; 5 bracket | ` normal ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 21; 5 bracket | ` lisse ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 21 | ` \overline{=} ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 23 | ` 5' ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 23 | ` dans tous les cas ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 25 | ` \mathrm{NS} ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 25 | ` X_s/k(s) ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 33; boxed counterexample caption | ` surjective ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 33 | ` Physically unreadable: estimated 2 word(s) ` | ` No positive reading retained ` | low |
| 57.pdf / 57 | 310 | LaTeX line 33; boxed counterexample caption | ` ouverte ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 33; boxed counterexample caption | ` comp. irréductibles ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 35 | ` est ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 35; 6 | ` $S$-points d'ordre $n$ ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 35; right continuation of 6 | ` Non ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 37; right continuation of 6 | ` au dessus ` | ` en dehors ` | low |
| 57.pdf / 57 | 310 | LaTeX line 37; right continuation of 6 | ` non vide convenable ` | ` dense de $S'$ constructible ` | low |
| 57.pdf / 57 | 310 | LaTeX line 40; 7 | ` \mathrm{rang} ` | ` — ` | medium |
| 57.pdf / 57 | 310 | LaTeX line 43 | ` $\uline{\mathrm{Pic}}^\tau$ est de type fini sur ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 46 | ` par ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 47 | ` \overline M ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 47 | ` pas aussi évidente ici ` | ` pas asymptotiquement liée ` | low |
| 57.pdf / 57 | 310 | LaTeX line 47; 8 marginal reply | ` d'invariants ` | ` — ` | low |
| 57.pdf / 57 | 310 | LaTeX line 47; 8 marginal reply | ` stables ` | ` étales ` | low |
| 57.pdf / 57 | 310 | LaTeX line 53; lower right, first starred question | ` platitude ` | ` flèche ` | low |
| 57.pdf / 57 | 311 | LaTeX line 6 | ` 00 ` | ` \infty ` | medium |
| 57.pdf / 57 | 311 | LaTeX line 6; third item first case | ` local ` | ` — ` | medium |
| 57.pdf / 57 | 311 | LaTeX line 14; right margin | ` modulaire ` | ` — ` | medium |
| 57.pdf / 57 | 312 | LaTeX line 3 | ` 2 ` | ` 1 ` | medium |
| 57.pdf / 57 | 313 | LaTeX line 19; N.B.2 ending | ` davantage ` | ` — ` | low |
| 57.pdf / 57 | 313 | LaTeX line 19 | ` la ` | ` $S$ ` | low |
| 57.pdf / 57 | 314 | LaTeX line 3; left cancelled margin | ` plt. suffit ` | ` — ` | low |
| 57.pdf / 57 | 314 | LaTeX line 3; left cancelled margin | ` en fait ` | ` — ` | low |
| 57.pdf / 57 | 314 | LaTeX line 7; Corollaire deleted word | ` alg ` | ` — ` | low |
| 57.pdf / 57 | 314 | LaTeX line 9; proof deletions | ` ouvert ` | ` — ` | low |
| 57.pdf / 57 | 314 | LaTeX line 9; proof deletions | ` ouvert ` | ` — ` | low |
| 57.pdf / 57 | 314 | LaTeX line 9; proof deletions | ` encore ` | ` — ` | low |
| 57.pdf / 57 | 314 | LaTeX line 9 | ` a ` | ` — ` | low |
| 57.pdf / 57 | 315 | LaTeX line 2 | ` \uline{X}_t ` | ` X_t ` | medium |
| 57.pdf / 57 | 315 | LaTeX line 2; before i.e. | ` Physically unreadable: estimated 1 word(s) ` | ` No positive reading retained ` | low |

## Abbreviations met

Expansions below are explanatory proposals only. They are not inserted into the transcription, and an uncertain abbreviation does not gain certainty through this list.

| Written abbreviation | Probable expansion or qualification |
|---|---|
| ` i.e. / ie. ` | id est; that is |
| ` n° / N° / n^circ ` | numéro |
| ` ord ` | ordre |
| ` resp. ` | respectivement |
| ` N.B. ` | nota bene |
| ` O.K. / OK ` | okay; affirmative check |
| ` C.Q.F.D. ` | ce qu’il fallait démontrer |
| ` cf. ` | confer; compare |
| ` th. ` | théorème |
| ` prop. ` | proposition |
| ` cor. ` | corollaire |
| ` chap. / Chap. ` | chapitre |
| ` App. ` | appendice |
| ` éd. ` | édition |
| ` p. ` | page when bibliographic; the mathematical p is not expanded |
| ` ex. / p. ex. / p.ex ` | exemple / par exemple |
| ` exer. ` | exercice |
| ` loc. ` | localement |
| ` fid. / fid ` | fidèlement |
| ` plat / plt. ` | plat / plate, as abbreviated in context |
| ` qu. cpt / q. cpt / qu. cpts ` | quasi-compact / quasi-compacts |
| ` tte / tt / ttes ` | toute / tout / toutes |
| ` tjrs ` | toujours |
| ` qcq ` | quelconque |
| ` ens ` | ensemble |
| ` éléme / élémt ` | élément(s); ending retained as written |
| ` changt ` | changement |
| ` f. et s. ` | faut et suffit |
| ` ssi / sss ` | si et seulement si; the doubled-s form is kept |
| ` ss- ` | sous- |
| ` pt / pts ` | point / points |
| ` nb ` | nombre |
| ` inv. ` | inversible |
| ` rel. / rel! ` | relativement; the final shorthand stroke is not a mathematical exponent |
| ` abs ` | absolument; cancelled reading remains doubtful |
| ` alg. / algt. ` | algébriquement or algébrique according to the phrase |
| ` Alg. ` | algèbre in bibliographic references; final abbreviation on 272 is uncertain |
| ` géom. / géom^t / géo ` | géométrique / géométriquement; géo on 277 remains uncertain |
| ` Géom. ` | géométrie |
| ` gén. ` | général / généralement |
| ` car. / car / caract. ` | caractéristique |
| ` rés. ` | résiduelle(s) |
| ` noeth. ` | noethérien |
| ` prés. ` | présentation |
| ` proj. ` | projectif |
| ` lin. ` | linéairement |
| ` équiv. ` | équivalence / équivalent |
| ` équivalts ` | équivalents |
| ` isom / isom. ` | isomorphisme |
| ` Hom ` | homomorphismes; upright mathematical operator |
| ` Pic / Pic. ` | Picard |
| ` Nér / N.S. / NS ` | Néron / Néron–Severi, with the written name changes preserved |
| ` comp. ` | composantes |
| ` ext. ` | extension |
| ` can. ` | canonique |
| ` univ. / univ^t ` | universellement |
| ` indép. ` | indépendantes |
| ` hyp. ` | hypothèse |
| ` d’acc. ` | d’accord; uncertain abbreviation on 290 |
| ` mor! ` | morphisme; ending on 272 uncertain |
| ` ensemblist! ` | ensemblistement |
| ` trivial! ` | trivialement |
| ` diffelles / diffélles ` | différentielles; quoted abbreviation on 303 |
| ` anots ` | probably anneaux noethériens; the expansion remains uncertain and the spelling is not repaired |
| ` géné ` | générique; cancelled, uncertain shortened word on 290 |
| ` Min. / Dim. ` | possibly minimum / dimension; first reading Min. on 309 remains doubtful |
| ` no. ` | uncertain short cancelled abbreviation on 279; no reliable expansion |

## Legibility and limits of confidence

The clean typed pages are generally the most secure, although missing typewriter signs, overtyping, damaged digits and original word spacing require care (especially 307 and the running number on 312). The handwritten definitions and larger displays are more legible than the compressed connecting prose; quotations, accents, index positions and the ends of abbreviated words remain significant sources of uncertainty.

The least secure passages are the heavily cancelled opening of 279, the crossed final clause on 284, parts of 286–287, the pale gluing discussion on 298–302, the cancelled projective-family draft on 306, and especially the slanting left note on 309 and the boxed/marginal comments on 310. The final two lines of the left note on 309 should be treated as a provisional sequence of ink readings, not as a reliable mathematical sentence. The opaque cancelled word on 315 and the other numbered unreadable spans were retained only after enlarged visual inspection; word counts are estimates, and no mathematical symbol has been replaced by an illegibility count.

The main reader viewed every supplied whole image and both halves, completed a second page-by-page visual audit, and then compared recurring notation across the package before freezing. No OCR or context-derived correction was used. The TikZ line work preserves the visible structure and labels but is not a metric facsimile: long insertion strokes and cancellation enclosures have approximate shapes, and their association is also carried by the insertion/deletion macros and inventory positions.

The frozen transcription is an auditable reading with explicit uncertainty, not a claim that every ambiguous letter has been solved. Mechanical compilation confirms that the fragments can be processed with the documented macro wrapper; it cannot establish a manuscript reading.
