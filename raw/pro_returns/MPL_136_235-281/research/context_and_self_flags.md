# Context mapping and frozen-text self-flag catalogue

## Scope and provenance

These two research memos were prepared after the parent reader froze the transcription. The context mapping uses only the supplied context files. The self-flag/title catalogue uses all 46 frozen individual LaTeX page files and their inventory sheet classifications. No manuscript images were consulted for either research memo, no readings were reconsidered, and no frozen transcription files were changed.

Context paths below are relative to /workspace/scratch/93e3dfb1ac44/context/. Scan-and-line references in the second memo refer to pages/MPL_136_235-281_136_scanNNN.tex within the deliverable directory. Page numbers for Pursuing Stacks are its \pspage markers, not PDF scan indices.

# Memo A. Supplied-context mapping

## A1. What the context does and does not supply

The context does not contain neighboring cote 136 scans or transcriptions. Its six files are README.md, notes/RESULTS_STATE.md, PURSUING_STACKS_CONTENTS.md, ps_chapters_VI_VII/ps6.tex, ps_chapters_VI_VII/ps7.tex, and the license. README.md, lines 16 and 27, explicitly says the first 45 scans' probe return was not yet available.

The most directly relevant retrospective, PS §94, “De Rham complex with divided powers,” is listed but absent: see PURSUING_STACKS_CONTENTS.md, line 120. Chapter VI starts at §110. Likewise, the original account of categorical coalgebras, §109, appears only in the contents at line 135 and later retrospective references.

README.md, lines 17–25, identifies S11 and the de Rham topos, sheafification, lecture-plan, and examples questions as the planning document's guesses and questions. The supplied chapters do not themselves establish S11.

## A2. Mapped primary-context evidence

| Topic | Exact locator | Evidence and appropriate use |
|---|---|---|
| Divided powers and a universal construction | ps_chapters_VI_VII/ps6.tex, §111, pp. 450–451, lines 370–404 | The proposed universal polynomial map is \(x\mapsto\exp(x)=\sum_{i\ge0}x^{(i)}\), first into \(\Gamma_k(M)\), then corrected to require completion \(\widehat\Gamma_k(M)=\prod_i\Gamma_k^i(M)\). Lines 403–404 say the induced maps preserve diagonal maps rather than multiplication. This is direct overlap of vocabulary and objects; identifying it with the lecture's “constructions universelles” would be a proposed comparison. |
| Universal free-module construction versus quasi-coherent replacement | ps6.tex, §115, pp. 482–484, lines 1982–2057; p. 486, lines 2174–2201 | \(X\to\mathscr O_k^{(X)}\) is characterized by a Hom adjunction valid in a ringed topos. A desired quasi-coherent envelope leads instead to pro-objects; \(X\to WL(X)\) prorepresents maps into \(W(N)\). Useful for comparing universal properties. This does not define the “topos de De Rham” or identify its “faisceautisation.” |
| Coalgebras and the completion distinction | ps6.tex, §117, pp. 493–495, lines 2540–2584 and 2614–2638 | Polynomial maps between finite projective modules are interpreted through topological augmented coalgebras \(\widehat\Gamma_k\). Discrete symmetric algebras/topological divided-power coalgebras correspond to ordinary schemes; completed symmetric algebras/discrete divided-power coalgebras correspond to formal schemes. The text explicitly declines to expect general equality of the associated invariants. A comparison with the manuscript should retain the completion distinction. Editorial caution: lines 2550–2552 state that the typesetter added some dual-module marks to make formulas meaningful. |
| Failure of a naive integral comparison | ps6.tex, §119, pp. 500–502, lines 2899–2998 | The expectation that \(H_*(K(\pi,n))\) is computed through derived functors of \(\Gamma_{\mathbb Z}\) is reported false. Lines 2917–2949 give the \(K(\mathbb Z,1)\)/non-split additive-group extension discussion; lines 2951–2988 motivate binomial rather than ordinary integral-polynomial algebra. Lines 2981–2988 explicitly contrast the divided-power de Rham approach with a possible binomial approach through unipotent bundles. This refutes that particular schematic/discrete comparison, not automatically the manuscript's proposed cochain theorem S11. |
| Operations and universal algebra | ps6.tex, §120, pp. 506–507, lines 3136–3197 | Divided powers, \(\lambda\)-operations, binomial operations, and Adams-type operations are discussed under Lazare “analyzers.” The text distinguishes divided powers on a suitable ideal from operations on rings with units. This supports a proposed universal-algebra comparison; it does not identify the precise universal constructions of cote 136. |
| De Rham divided-power algebras and schematic homotopy | ps6.tex, §121, p. 508, lines 3227–3239; §124, p. 521, lines 3938–3980 | The text explicitly names three approaches: divided-power de Rham complexes, small categories with diagonal maps, and semisimplicial schemes. §124 says the homology functor is tautological in the earlier approaches. Lines 3965–3974 reject the naive construction of a right adjoint by forgetting a chain complex's \(k\)-module structure and taking the de Rham complex of its underlying semisimplicial set; the author calls the existence of the right adjoint doubtful. Lines 3977–3980 distinguish the directions of comparison with ordinary homotopy types. These are direct named overlaps and explicit limitations, not an equivalence theorem between the models. |
| Topos and sheaf-theoretic setting | ps6.tex, §127, pp. 535–536, lines 4716–4749 | Semisimplicial sheaves on schemes/affines over \(k\), for a topology such as fpqc, provide a broad setting; Illusie's derived category of a topos supplies a notion of weak equivalence. This is a possible comparison framework only. The passage does not name a de Rham topos or its sheafification. |
| Categorical coalgebras, coefficient formalism, and open questions | ps_chapters_VI_VII/ps7.tex, §139, pp. 590–591, lines 1716–1768 | The \(k\)-additive envelope with its diagonal map triggered the schematization discussion. The author asks whether six operations and Steenrod operations carry over, and suggests that much commutative-coefficient information may survive in \(P=\operatorname{Add}_k(A)\). He doubts that noncommutative information is generally recoverable. This is a categorical coalgebra proposal, not a supplied construction or theorem about strictly cocommutative cochains. |

## A3. Explicit negative findings

Neither ps6.tex nor ps7.tex contains “Fourier,” “Chern,” “faisceautisation,” “sheafification,” or “de Rham topos”; neither names abelian varieties. The two generic “variety” occurrences in ps7.tex are at lines 830 and 948 and do not concern abelian varieties. The examples question occurs in README.md, line 21 only.

Consequently, the supplied context cannot itself answer the lecture-example question or supply the missing definition of the de Rham topos. That must remain grounded in the frozen manuscript reading. Likewise, the explicit divided-power de Rham references do not by themselves establish their historical identity with this particular 1976 lecture; that identity is a comparison to make, not an additional transcription fact.

## A4. Relevant RESULTS_STATE entries

| ID | Status and exact locator | Source recorded there; appropriate connection |
|---|---|---|
| WG2 §2.4 #5 | “question or plan item of the war game (round 2; unchecked)”; notes/RESULTS_STATE.md, line 119 | Source: grothendieck_archive_montpellier/PROGRAM_WARGAME_ROUND2_20261112.md, listed at line 145. Connects integral Lefschetz-ring questions in cote 16 scan 14 and divisibility questions in cote 47 scan 9 to divided powers on cochains. Those earlier source pages are absent here. Use as a proposed link, not an established implication. |
| WG H6 | “hunch of the war game (Believe; unchecked)”; line 120 | Source: grothendieck_archive_montpellier/WARGAME_MATH_HUNCHES_20261112.md, listed at line 146. Suggests a finite-dimensional-local-system localizer whose localization is schematization. The supplied PS passages do not prove this particular assertion. The schematic comparisons above bear on its motivation and required distinctions only. |
| 136-shadow-full-faithfulness | “conjecture (unsearched) \| Lean card: holds, more generally”; line 127 | Introduced at lines 123–125 as Hua's AI-produced findings register, explicitly “claims to check, not results.” The project identified is github.com/Commutator-IO/grothendieck-project; no complete local findings-register source file or proof is supplied. The claim concerns recovering \(M\) from tails of \(M\otimes_k k\{T\}\), with a binomial arithmetic core. The entry is truncated. Cite “Hua, findings register, 136-shadow-full-faithfulness” and distinguish what the actual pages support from the stronger formulation. |
| GALOIS G.6 and GALOIS E.11 | “Open (the return's claim)”; lines 13 and 32 | Source: derivateurs_companion_20261109/pro_returns_20261110/4_GALOIS/GALOIS/GALOIS_results.csv, listed at line 141. These concern functorial higher-coefficient constructions for bare derivators without specified monoidal enhancement. Relevant only if a research note proposes extending concrete cochain constructions to arbitrary derivators; such an extension is not settled by the PS parallels. |
| WG2 §Week #3 | “question or plan item of the war game (round 2; unchecked)”; line 121 | Source: grothendieck_archive_montpellier/PROGRAM_WARGAME_ROUND2_20261112.md. Names the future R-SCHEM reading program. It supplies an organizational link rather than a mathematical result. |

RESULTS_STATE.md, lines 7–8, distinguishes run claims from specifically reviewed entries. None of the directly relevant entries above is presented there as a reviewed proof of S11, a definition of the de Rham topos, or an identification of its sheafification.

# Memo B. Self-flags, cancellations, titles, and pagination in the frozen transcription

## B1. Author's explicit question marks

There are 11 definite question loci, containing 12 question-mark characters because scan 279 has “??”. There is one additional uncertain reading on reused typed scan 238; it must not be counted as a confirmed author question. This count distinguishes literal question marks from the transcriber's \unsure macros.

| Scan; line | Brief exact quotation or marked expression | Kind and status within the frozen text |
|---|---|---|
| 239; 35 | “quel est exactement l'idéal \(S^{[i]}\) engendré par les \(\dfrac{p^j}{j!}\) pour \(j\geq i\) ?” | Live question. The valuation calculation on scan 241 is the immediate continuation to examine. |
| 248; 7 | \(\operatorname{Hom}_{\mathcal M_{N'}}(\tau_{N',N}(M),P)\overset{?}{\sim}\operatorname{Hom}_{\mathcal M_N}(M,\rho_{N,N'}P)\) | Live proposed adjunction. A formula for \(\rho\) follows on the page; scan 250 gives the subsequent Hom comparison. |
| 249; 5 | \((\lambda z)^{(\alpha)}\overset?=\lambda^\alpha z^{(\alpha)}\) | Question inside a cancelled draft. Line 44 concludes only “OK si \(\eta y=0\).” |
| 249; 46 | \((z^{(\alpha)})^{(\beta)}\overset?=z^{(\alpha\beta)}\dfrac{(\alpha\beta)!}{\beta!(\alpha!)^\beta}\) | Question inside a cancelled draft. The calculation reaches “OK” at line 78. Retain both the initial question and the whole-block cancellation. |
| 249; 85 | \(z^{(p)}z^{(q)}\overset?=\dfrac{(p+q)!}{p!q!}z^{(p+q)}\) | Question inside a cancelled draft. The coefficient calculation ends “OK.” at line 96. |
| 257; 6 | “bijectif?” | Live question, subsequently claimed answered on the same page. It concerns \(\varinjlim\unsure{\varphi_N\vert\rho_N}\tau_NP\to\unsure{\varphi_\infty\vert\rho_\infty}\tau_\infty P\); lines 34–37 say “Donc” and mark the map as an isomorphism. The \vert in this table represents the alternatives separator of the frozen \unsure macro, not additional manuscript notation. |
| 271; 16 | \(R^*\psi(L^\bullet_\infty)\xleftarrow{\overset{?}{\sim}}\psi(L^\bullet_\infty)\) | Question inside a cancelled argument. Especially relevant to the live reservation that \(\psi\) may not be exact. |
| 273; 10 | \(\operatorname{Hom}(R\sigma(K),L)\overset{?}{\sim}\operatorname{Hom}(K,R\psi(L))\) | Live proposed derived adjunction. The page later asserts “pl. fid.” and “compatible avec multiplication”; those assertions do not erase the recorded question mark. |
| 277; 18 | \(T(Q)/\operatorname{Im}T(P)\simeq T(Z')\xrightarrow{?}T(R)\) | Live question on the arrow. Do not silently interpret the mark as specifically asking for injectivity: the frozen text only places “?” on that arrow. |
| 279; 37 | \(\operatorname{Hom}_{\mathcal M}(s,\tau^N N\otimes_k s)\simeq\unsure{N_0\vert N}\quad??\) | Live double question mark. The right-hand object itself carries a separate transcriber doubt, between \(N_0\) and \(N\). |
| 281; 14, 16 | \(\boxed{(M\otimes_k s)\boxtimes_s C\simeq M\otimes_k C}\qquad ?\), followed by margin “NON” | Live questioned formula with an immediately following negative annotation. This is the strongest same-page candidate for the “withdrawn” category; association of the margin must follow the parent reader's visual reading. |

Unconfirmed question mark: scan 238, line 12, has the alternatives \unsure{\overset{?}{\simeq}|\simeq} in typed formula (13.5.7). This is an editorial reading alternative, on a reused typed sheet, not a confirmed mathematical self-flag.

## B2. Verbal self-flags, expectations, and existence reservations

### Live manuscript writing

| Scan; line | Exact words | Classification |
|---|---|---|
| 244; 36 | “donc on s'attend à trouver des adjoints à g. et à dr.” | Expectation. The right adjoint is written immediately below; scan 246 treats the left adjoint. Record the expectation and its subsequent treatment. |
| 246; 29 | “mais en général pas à gauche, sans doute” | Explicit uncertainty about left exactness of \(q_{N',N}\). |
| 246; 29 | “on ne s'attend pas qu'il ait encore un adj. à g.” | Negative expectation concerning a further left adjoint of \(q_{N',N}\). |
| 246; 29 | “On s'attend à en trouver un foncteur adjoint à droite.” | Expectation for \(\tau_{N',N}\), pursued on scans 248 and 250. |
| 269; 13 | “on aimerait un isom dans \(D(C).\)” | Desired strengthening, followed by explicit additional hypotheses: \(i\) fully faithful with right adjoint \(\kappa\), and \(\kappa\) exact at line 17. This is a goal and conditional construction, not a conjecture without hypotheses. |
| 271; 10 | “mais \(\psi\) peut-être pas exact” | Explicit doubt, following deletion of “\(\psi\) exact” at line 8. |
| 275; 39 | “Dans la mesure où ça existe” | Existence reservation for the internal Hom and tensor constructions just defined. |

### Conditional checks in cancelled drafts

These deserve notes, although they are conditional verification statements, not unexplained question marks:

- 247, line 91: \(\boxed{\text{OK si }yy'=0}\), within the whole cancelled draft.
- 249, line 44: “OK si \(\eta y=0\).”, within the whole cancelled draft.
- 249, lines 78 and 96: “OK” concludes the iteration and product calculations; both remain within the cancelled draft.

### Genuine self-flags on reused typed mathematical sheets

| Scan; line | Exact words | Classification |
|---|---|---|
| 240; 5 | “Il semble que la méthode de démonstration de 13.5.2 doive permettre aussi de prouver le résultat analogue pour tout espace analytique \(B\) propre sur \(S\).” | Expectation in reused typed material, not in the live divided-power notes. |
| 240; 5 | “Plus délicate sans doute est la question de savoir si” | Introduces the open algebraization question for a proper analytic \(X/S\) whose formal completion along \(X_s\) is algebraizable. |
| 268; 5 | “J'ignore si de tels \(M_n\) existent nécessairement (et en doute fort).” | Explicit ignorance and doubt in reused typed material concerning descent of the indicated ample invertible modules. |

### Deferred proofs and details, distinct from self-confessed doubt

These are useful for the unproved/deferred-claim notes, but should not inflate the count of explicit uncertainty:

- 242, line 3: “comme il serait facile à établir grâce aux résultats du type GAGA relatifs [10]” — the asserted full faithfulness of analytification; reused typed sheet.
- 260, line 18: “qui sera étudié plus en détail plus bas”; lines 39–40: “Ce dernier groupe sera déterminé dans 11.10” — forward references, reused typed sheet.
- 266, line 10: “On peut prouver, sans hypothèse de normalité sur \(S\), que \(\hat B\) est toujours algébrisable” — with a reduction referred to 13.5.3 a); reused typed sheet.
- 274, line 5: “du moins (pour le moment) en inégales caractéristiques” and “Indiquons le principe de la vérification de ces assertions.” — scope restriction and proof sketch, reused typed sheet.
- 278, line 4: “que nous laissons au soin du lecteur à expliciter.” — omitted compatibilities, reused typed sheet.
- 265, line 8: “et si on sait que” introduces the displayed essential-image hypothesis. This is an explicit conditional premise, not itself an admission that the premise is false or unknown.
- 263, line 45: “je dis qu'alors” is an assertion followed by a proposed argument, not a doubt marker.
- 262, lines 6–8: “il suffit de vérifier” is immediately followed by a reduction to a known case; not a self-flagged unverified step.
- 245, line 29: “Sans doute, je pourrais…” belongs to Lafon's administrative letter, not a mathematical statement.

No live mathematical occurrence of “à vérifier,” “sauf erreur,” “je présume,” or “admis” was found.

## B3. Substantive cancelled claims and arguments

The files contain 150 \deleted occurrences, including nested deletions and single-symbol changes. The following are the substantive propositional or argumentative cancellations; cancellation alone must not be described as a proved mathematical refutation.

| Scan; lines | Cancelled material |
|---|---|
| 235; 48–50 | The unfinished conclusion beginning “l'inclusion” and the displayed \(\mathrm{Fil}^1\widehat A_*^0\to\widehat A_*^0\). The arrow itself has a transcriber doubt in the frozen source. |
| 237; 2–5 | “On trouve donc” and the unfiltered formula \(H^i(C_{\mathrm{DR}}^*(X,\widehat A_*^*))=H^0(X,S)\) for \(i=0\), \(H^i(X,S^+)\) otherwise. Do not use this as a surviving theorem. |
| 237; 21–29 | Intermediate homotopy calculations, index conditions, and the abandoned start “on en conclut la suite spectrale (pour \(p\) fixé).” The surviving filtered comparison follows at lines 31–34. |
| 239; 36 | Candidate ideal formula \unsure{S^{[i]}=(\frac{p^n}{n!}\mathbb Z_p)}. |
| 241; 33 | The local boxed condition \(i_0\leq p-2\) is struck. This is a local calculation edit, not automatically withdrawal of the surrounding equivalences. |
| 247; 2–93 | Entire draft of graded differential divided-power axioms and the odd/even expansion test, ending “OK si \(yy'=0\).” Includes local deletions such as \(x^{(\alpha)}=0\) and \((x+y)^2=x^2+y^2+xy+yx\). |
| 248; 18–28 | Provisional formulas for \(\rho_{N,N'}(P)_i\), replaced by the subsequent displayed construction. |
| 249; 3–98 | Entire scalar, iteration, and product divided-power verification draft, including all three question marks catalogued above. |
| 251; 3–67 | Entire cochain-construction draft, including “dépend de façon contravariante de \(X\)” and “covariante de \((A,\pi,\gamma)\),” plus the differential divided-power algebra description. The \(\pi\) reading has a transcriber doubt in the frozen source. |
| 252; 18 | “qui a comme adjoint à gauche.” The page also cancels a provisional diagram and the fragment \(\tau_{N-\alpha,0}S\to0\), at lines 37–42 and 59. |
| 253; 3–58 | Entire draft beginning \(J\subset A\), “\(H^*(X,J)^{\unsure{*}}\) à p.d.”, with proposed cohomology/divided-power maps. |
| 257; 32–33 | The additional “Hyp Tout idéal gradué \(J\) de \(S\), tq que \(S/J\) soit négligeable \unsure{finie.|fini.}” is cancelled. Its uncertain ending prevents a more precise paraphrase. |
| 261; 24–25 | Provisional Hom-composition identity and its derived version. The subsequent argument explicitly introduces projectivity at line 43. |
| 263; 19–35 | Essential-image membership of \(P\) followed by asserted higher-derived vanishing and Ext vanishing. A different formulation using an exact functor \(i:C\to\mathcal M_{N'_0}\) follows at lines 37–58. |
| 269; 11 | Abandoned “Je dis que l'hom d'augmentation \(L^\bullet\to\)”. |
| 269; 23–34 | “Lemme Cet hom est un quasi-isomorphisme” for the underived-to-derived comparison, and the resulting underived reconstruction “Corollaire.” |
| 271; 8 | “\(\psi\) exact,” explicitly followed by the live reservation at line 10. |
| 271; 14–33 | Comparison with \(R\psi\), the spectral-sequence argument, and the proposed cohomology identity. |
| 271; 34–47 | Reconstruction formulas and \(D(\operatorname{Mod}(k))\to D(\mathcal M_\infty)\), labelled “pl. fidèle.” |
| 273; 2 | Strict equality \(\psi\sigma=\operatorname{id}\), with an isomorphism retained in the margin at line 6. This is not a withdrawal of the isomorphism statement. |
| 277; 5 | The provisional pair \(P\to Z\to0\), \(0\to Z\to Q\to Z'\to0\). Other cancellations on this page are incomplete Hom and coefficient-map fragments. |
| 281; 28 | Incomplete \(V(s)\otimes V(C)\to V(C')\) fragment. |
| 281; 38–83 | Entire lower/inverted coalgebra draft: coproduct formula, exponential expression, completed coalgebra diagram, extension-of-scalars formula, duality formula, and the labelled coalgebra construction. |

Especially strong same-text revision pairs: scans 237 → 237–239; 263 → later part of 263 and 265; 269 → 271; and 281's “?” → “NON.” Describe what is deleted and what is subsequently written before drawing any conclusion about mathematical correction.

## B4. Titles, title-sheet status, and page counts

No sheet is classified “cover” in the inventory. No explicit page-count statement occurs in the frozen text: neither “page” nor “pages” appears as a word. The numerical pagination below must not be turned into a claimed total page count.

| Scan; location | Title/heading | Provenance |
|---|---|---|
| 244; line 2 | “Généralités sur modules gradués / sur certains anneaux gradués” | Live manuscript heading on reused support. The slash indicates the line break in the title. This is the principal internal mathematical title in the supplied live notes. |
| 244; lines 32, 38; 246 line 12; 248 line 4 | “Étude de l'inclusion (pl. fid.)”; “Adjoint à droite … de”; “Adjoint à gauche … de”; “Adjoint à droite … de” | Internal subsection headings of that module study; the omitted intervening material is the displayed functor notation, not an omitted independent title. |
| 252; lines 19, 44 | “Conditions équivalentes” | Repeated internal headings. |
| 236; line 12 | “14. Liens avec la théorie transcendante : cas rigide-analytique. L'homomorphisme canonique” \(\underline M_K\to A_K^{\unsure{\natural\vert\sharp}0}\) | Reused typed mathematical sheet. The superscript reading is uncertain between natural and sharp in the frozen source. |
| 242; line 3 | “13.5. Cas d'une situation relativement algébrique” | Reused typed mathematical sheet. |
| 254; lines 13, 19; 255 lines 9, 15 | “SEMINAIRE D'ANALYSE CONVEXE”; “Diffusions réfléchies.” | Printed announcement; readings on scan 254 are inside \unsure, while scan 255 supplies the clear printed text. |
| 258; lines 12–21 | “AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE … SPECIALITE : CHIMIE”; thesis title “Synthèse et réactivité d'organomagnésiens perfluorés. Application à la préparation d'acides perfluorosulfoniques et carboxyliques.” | Reused printed thesis notice, not a mathematical lecture title. The ellipsis in the notice heading marks only the layout break between the two printed lines. |
| 272; line 6 | “7. L'extension de Raynaud” \(G^{\unsure{\natural\vert\sharp}}\) “sur \(S\) attachée au schéma abélien \(A_K\) à réduction semi-stable. Dualité des schémas abéliens \(B,B'\) sur \(S\).” | Reused typed mathematical sheet; the superscript reading is uncertain. |
| 276; line 4 | “10.5. Réduction de 10.4 à un cas particulier.” | Reused typed mathematical sheet. |
| 280; line 16 | “Théorème 3.6. (théorème de réduction semi-stable)” | Named theorem on a reused typed sheet, not a title sheet. |

The cancelled printed administrative label on 244, line 47, includes “MATHÉMATIQUES / PROFESSEUR / M. GROTHENDIECK ALEXANDRE / 5-856”; 5-856 is not presented as a page count. Similarly, scan 258's “2 ans” is a research-duration field, not pagination.

### Complete \mspage register

| Scan | Frozen \mspage value | Sheet status |
|---|---:|---|
| 236 | 188 | reused_typed |
| 238 | 186 | reused_typed |
| 240 | 185 | reused_typed |
| 242 | 182 | reused_typed |
| 260 | 99 | reused_typed |
| 262 | 94 | reused_typed |
| 264 | 76 | reused_typed |
| 266 | 84 | reused_typed |
| 268 | 83 | reused_typed |
| 270 | 82 | reused_typed |
| 272 | 81 | reused_typed |
| 274 | 80 | reused_typed |
| 276 | 127 | reused_typed |
| 278 | 108 | reused_typed |
| 280 | 33 | reused_typed |
| 281 | 281 | text; marker at line 84 |

All other page files lack \mspage. The many separate \margin numerical labels are distinct from this register.

## B5. Literal-term result and the examples question

“Fourier,” “Chern,” “topos,” and “faisceautisation” do not occur anywhere in the frozen page text. This is a bounded result about these 46 transcribed pages.

Abelian schemes occur repeatedly on the reused typed mathematical sheets, for example scans 236, 242, 262, 272, and 280. They should therefore not be reported as examples supplied by the live divided-power lecture notes merely because they occur inside the same physical package.
