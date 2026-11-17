# Post-freeze context evidence: groupoids, flags, tame signatures, oriented surfaces

Research-only memo for the root transcriber. No scan images were opened and no frozen transcription or supplied context file was changed. The evidence below comes from the frozen page TeX and the supplied textual context. Locators are file line numbers, with the context's own `scanpage` numbers stated separately; they are not fresh visual readings of the manuscripts.

## Provenance and pagination

`context/README.md` and `context/hua_project/README.md` were read before this comparison. The supplied `LM_140-*_text.tex` files describe themselves as second-pass source transcriptions; they are evidence for what that supplied transcription says, not independently checked images here. `context/hua_project/138.modern.tex` is **Hua, modernised reading of cote 138**, an AI-produced interpretation, not a transcription and not this project's result. Its page numbers are normally the archival foliation: its pages 57–62 correspond to our scans 058–063; page 63 to scan064; page 67 to scan068; pages 70–74 to scans071–075; pages 76–77 to scans077–078. Scan067 is the printed thesis notice, not a mathematical continuation.

`context/notes/RESULTS_STATE.md`, lines 5–8 and 32–37, requires attribution of statuses to the research returns, with separate referee status where given. The orientation digest's line 22 says its digests contain no Hua findings on these scans, but the full supplied Hua file does contain §§6–10 covering them; the full file is the relevant evidence. Nothing here upgrades a return's claim to an independently verified theorem.

In the locators below, a frozen filename beginning `MPL_138_046-089_138_scanNNN.tex` is in `MPL_138_046-089/pages/`.

## G01 — The target category hypothesis in the groupoid corollaries

**Frozen evidence:** scan058 lines 5–6 explicitly has “C un groupoïde, C′ une catégorie”; lines 23–40 classify functors over an object map by transports and homomorphisms of automorphism groups. Scan059 lines 12–21 separately requires `Isom(f0(x),f0(y)) → Hom(f0(x),f0(y))` to be bijective. Scan061 lines 3–23 gives the component/object/automorphism-group tests without explicitly restating that every arrow in C′ is invertible.

**Exact context:** Hua §6, “Foncteurs d'un groupoïde au-dessus d'une application des objets,” lines 1009–1057, especially 1046–1057, explicitly restricts the corollaries to C′ a groupoid and explains that the second condition can otherwise fail. The more general supplied source parallel is `context/LM_140-2_text.tex`, §1, scan11, lines 314–334: Prop. 1.11/1.10 relates morphisms of multigaloisian topoi to functors between their fundamental groupoids. It does **not** reproduce the exact elementary corollaries with arbitrary target category.

**Relation / possible note:** The pages support Hua's distinction between the general target-category proposition and the specialized groupoid corollaries, and **differ** from his modernized statement by leaving the specialization implicit. A precise reading question is whether scan061 is tacitly returning to the case C′ a groupoid; the frozen text must retain “catégorie.” This is a hypothesis question, not a settled RESULTS_STATE entry.

**Searches used:** `groupo[iïî]de`, `Automorphismes de groupoïdes`, `foncteur`; Hua subsection and LM §1 read directly after the hits.

## G02 — Connectedness and object permutations

**Frozen evidence:** scan060 lines 3–13 puts `C ... groupoïde connexe` and the first exact sequence in a cancelled block, then lines 14–31 gives the live automorphism sequences and the torsors `Isom(a,x)`. Scan061 lines 26–30 says `Aut(C) → S_C0` is a surjection; scan062 lines 3–5 gives `Aut^0(C,a) ≃ ∏_{x≠a} π_x`.

**Exact context:** Hua §6, same subsection, lines 1059–1080, retains the connectedness hypothesis and explicitly notes at 1074–1078 that it is only written in the crossed-out passage. Without connectedness, the object permutations must preserve components and their automorphism-group types, which is the compatibility already recorded in scan061's second corollary.

**Relation / possible note:** This **restates** the connected calculation while **adding** a warning about the scope of the surviving exact sequences. The context supports a hypothesis question, not rewriting the cancelled hypothesis as live text. No specific RESULTS_STATE row settles this local scope issue.

**Searches used:** `groupo[iïî]de`, `commutant`, then direct reading of Hua lines 1059–1080 and frozen scans060–062.

## G03 — The graph K(I), normalizer, and canonical involution

**Frozen evidence:** scan062 line 13 defines a polygonal structure of order n≥2 and a dihedral automorphism group written D/𝔻; the n=2 supplementary edge set remains uncertain. Lines 15–24 define the graph with two vertices and its edge incidence, and an involution τ fixing the edge set and exchanging the vertices, commuting with G. Lines 32–34 call C(I) the fundamental **groupoid**, use the letter G for its action, and visibly replace “commutant” by “normalisateur de G”; scan063 line3 completes “G dans Aut C(I)” and says there is a canonical element τ, stopping there.

**Exact context:** Hua §6, “Le graphe K(I),” lines 1083–1096, describes the same graph, renames the acting group consistently D, and calls it the “carte de l'orange.” His footnote says he replaced “groupe fondamental” by groupoid, whereas the frozen scan062 line32 already reads “groupoïde fondamental.” These are differences between two textual readings, not authority to alter the frozen page. Literal searches for `orange` and `K(I)` in the four LM source-transcription files and the supplied Esquisse transcription returned no matches.

**Relation / possible note:** The construction **supports** Hua's graph interpretation, but the source retains the D/G naming shift and the specific commutant-to-normalizer revision. A precise question is whether G here is the polygon's dihedral group D or an implicitly retained acting group; Hua's normalization does not settle that palaeographic question. The source has announced an investigation of the normalizer, not computed it.

**RESULTS_STATE:** The broad later claim **EXIT_TOWER B.27** is in lines 46–50: a surface-with-boundary fundamental groupoid as a colimit of finite diagrams. It is only a later thematic comparison: this two-object graph construction neither gives the five elementary pieces nor proves that return's claim. Do not use it as a proof of normalizer or tower assertions.

**Searches used:** `orange|polygone|commutant|Aut.*C\(I\)|K\(I\)`; separate exact-string searches `orange` and `K(I)` over `LM_140-1_text.tex` through `LM_140-4_text.tex` and `Esquisse_cote119_copy1_API_transcription.tex`.

## G04 — The bipyramid and the three permutations

**Frozen evidence:** scan064 lines 19–23 has E±, D01/D12/D20, S0/S1/S2 and the p/π/φ arrows. Lines 29–33 define the ρ permutations and state `ρ2+ ρ1+ ρ0+ = id`; lines37–39 identify the Si with orbit sets. At least the ρ index in line30 and an index in line38 remain explicitly doubtful.

**Exact context:** Hua §7, “La double pyramide,” lines 1099–1128, interprets the diagram as the positive/negative barycentric triangles of an oriented map, gives the permutation product, and interprets the Si as orbit sets. At lines1125–1128 he expressly says he restored overloaded indices by the pattern of the other formulas, and that the figure returns on archival page77 (our scan078). This is interpretation and reconstruction, not a second independent manuscript reading.

**Relation / possible note:** Scan064 **supports** the diagram/permutation interpretation and the product-one relation. The context explains the role of the diagram, while **differing** from the literal record by resolving doubtful indices. Do not erase those doubts or attribute Hua's explanatory prose or modern historical names to the page.

**Searches used:** `drapeau|cartograph|double pyram|groupo[iïî]de|paradigme`; direct Hua §7 and frozen scan064.

## G05 — Flag fiber product, and a cancelled LM flag draft

**Frozen evidence:** scan077 lines3–9 gives R→S,A,F with q′/q″; lines46–65 constructs `E=(R,q′)×_A(R,q″)`, the replacement by `(s,a,bar f)`, the three projections, and the positive part. Lines68–70 contain doubtful barred/indexed terms in the three σ formulas. Scan078 lines6–12 redraws the bipyramid; lines14–31 labels the triangular subdivision with s0/s1/s2, dij, e+.

**Exact source context:** `context/LM_140-1_text.tex`, scan17, lines979–1021, contains a **cancelled** non-oriented polyhedra draft. In particular lines992–1002 introduce incidence sets A1,A2,A3, then `R = A1×_A A2` and “triplets ou drapeaux / triplets de drapeaux (s,a,f)”; lines1004–1014 give R→S,A,F. Its cancellation and uncertainty are part of the evidence. Hua §10, “Quelques problèmes spéciaux : les drapeaux,” lines1229–1247, follows the present E fiber product, describes the orientation splitting and the repeated bipyramid, and expressly declines to restore the detailed σ formulas because the indices are doubtful.

**Relation / possible note:** Scan077 **adds** a specific fiber-product and orientation-splitting construction to the cancelled LM draft's incidence idea; the symbols R and E are not identical across the two texts. Hua's explanation is supported at the construction level, while the exact σ formulas remain a reading question. A comparison should preserve both the LM draft's cancelled status and the current transcription's doubtful indices.

**Searches used:** `drapeau`, `cartograph`, `pyramide`, `repères`; the LM140-1 `drapeaux` hit at line1002 led to full scan17 inspection.

## G06 — The marked points beside φ on scan078

**Frozen evidence:** scan078 lines44–58 draws `P¹_Qbar ←φ P¹_Qbar` and the marked points −1,0,1/2,1,2,−j,−jbar on two circles. It gives no equation for φ and no explanatory covering/group-action text there.

**Exact source context:** `context/LM_140-3_text.tex`, §38, scan9, lines432–447 gives the quotient for `X=U03^an, G=S3`, with

`f(z) = (27/4) z²(z−1)²/(z²−z+1)³`,

and maps `{0,1,∞}→0`, `{2,−1,1/2}→1`, `{−jbar,−j}→∞`. Lines450–483 identify the corresponding cartographic generators; scan10 lines494–546 gives the oriented and unoriented group presentations, with the source's own uncertainty about a possible inverse at line487.

**Relation / possible note:** The coincidence of all marked points is a particularly precise contextual parallel and **adds** an explicit rational-quotient description in LM. It suggests asking whether scan078's φ is that S3 quotient; the present page itself does not state the equation. Do not import the equation or a Galois-faithfulness claim into the scan078 transcription or present that identification as explicit manuscript text.

**Searches used:** `cartograph` in LM140-3, then direct inspection of §38 scans9–10.

## G07 — Tame signatures versus a proof reconstructed by Hua

**Frozen evidence:** scan065 line4 explicitly titles the discussion “Sous groupes finis de GP(1) (cas tame).” Scan066 lines9–20 gives Riemann–Hurwitz and its positive genus-zero expression; lines22–71 separates the cases and lists `(2,2,p), (2,3,3), (2,3,4), (2,3,5)` with orders 2p,12,24,60. Scan068 lines14–27 continues the exclusion of at least four branch points; line16 retains the weak `≥1` immediately before “impossible,” following a strict preceding inequality. Its upper lines3–13 and lower lines29–52 are cancelled, but the middle argument is live in the frozen record.

**Exact context:** Hua §8, “Sous-groupes finis de PGL2, cas modéré,” lines1131–1158, reproduces the Riemann–Hurwitz setup and the signatures. His lines1150–1154 replace the multi-line ≥4 discussion with the observation that each ramification contribution is at least 1/2 and explicitly say the one-line argument is his own. His description of archival page67 as “entièrement barrée” differs from the frozen record's live middle block. The name “classification de Klein” and replacement of GP(1) by PGL2 are expressly his modern identifications.

**Relation / possible note:** The signature list **supports** Hua's mathematical identification, but his shortened proof and total-cancellation description **differ** from the present source record. The precise reading question is whether the weak inequality in scan068 line16 is a retained slip following the strict inequality in line15; no replacement is proposed. The page lists necessary numerical types and later explores their groups, not a new proof of every modern profinite finite-action assertion.

**Searches used:** `sous.groupes finis|ramification|modéré|sauvage|Klein`, then direct frozen scans065–068 and Hua §8. Scan067 inspected solely as frozen text: it is the university thesis notice dated 28 June1978; this is the printed notice's date and does not directly date the mathematical writing.

## G08 — Cancelled wild cases must stay cancelled

**Frozen evidence:** all of scan068 lines29–52 is in a single cancelled block. It covers the cyclic case `(N,N)`, the tentative p|N extension with a doubtful word “inséparable,” the unipotent p-subgroup discussion and `(Z/pZ)^r`, a conflicting/doubtful marginal `(Z/p^rZ)^ν`, and a Kummer base-change treatment of `(N,2,2)` ending in a genus-zero verification phrase. The letter in “premier à 2|p” remains doubtful.

**Exact context:** Hua §8 lines1160–1173 interprets the p|N passage as outside the tame setup, normalizes the p-group to elementary abelian `(Z/p)^r`, and notes both cancellation and the doubtful marginal exponent. He gives the Kummer reduction as a coherent modern argument. These are readings of a cancelled experiment, not a live classification of wild covers established here.

**Relation / possible note:** The page **supports** the presence of a cancelled excursion beyond the tame hypothesis and **differs** from an unqualified modern narrative by preserving its doubts, contradictory-looking margin, and unfinished verification. A useful reading question concerns the apparent “inséparable” in the cancelled p-extension: is that really the retained word, and what extension was meant? Its conceptual difficulty is not grounds for changing the frozen transcription.

**Searches used:** `ramification`, `modéré`, `sauvage`, `Klein`; direct scan068 and Hua lines1160–1173.

## G09 — Oriented surfaces, compactification, and two sorts of marked points

**Frozen evidence:** scan071 lines7–13 introduces orientable paracompact surfaces, the two-element orientation set ω, `T=Z∧_(Z/2)ω`, and the compactification by a finite missing set in each component. Scan072 lines5–12 gives the category equivalences, with J a discrete marked set; scan073 lines3–5 makes S and J disjoint and deliberately retains their asymmetry. The Čech phrase at scan071 line15 continues on scan072 line3 and is not an explicit Freudenthal citation.

**Exact source context:** `context/LM_140-2_text.tex`, §12 “L'analogie topologique,” scans89–90, lines2579–2634, introduces exactly the orientation torsor, the twisted rank-one T, the punctured surface U=X\S, its peripheral fundamental-groupoid diagram, and the T-lacet structure. Scan101 lines2953–2988 places these structures in an isotopic category with an operator group Γ and explicitly retains the closed-surface cohomological extra datum. Hua §9 lines1176–1196 describes the same setup but says “compactification de Freudenthal” is his modern name.

**Relation / possible note:** The present pages **anticipate/restate** the orientation and peripheral formalism elaborated in LM §12, and **add** the explicit distinction between punctures S and marked objects J in the chosen groupoid. The context supports a conceptual link, not importing Freudenthal's name or a theorem citation into the source. No RESULTS_STATE arithmetic-image result follows merely from this topological paradigm.

**Searches used:** `paradigme`, `isotopi`, `groupo[iïî]de`; direct LM §12 scans89–103 and Hua §9.

## G10 — Peripheral quotient and the closed-surface orientation display

**Frozen evidence:** scan074 lines13–27 gives the exterior group Π, the map `S→Homext(T,Π)`, and the compactified group as a quotient by the peripheral images. Lines28–34 contains the crowded closed-surface orientation display involving the dual of an exterior square. Scan075 lines13–18 repeats a map, with doubtful isomorphism sign, from T to that exterior-square dual.

**Exact source context:** `context/LM_140-2_text.tex`, §12, scan91, lines2651–2660, replaces the peripheral datum for empty S by `H²(π,Z)≃T`; scan101 lines2985–2988 insists on compatibility of the action with this datum. Scan103 lines3035–3040 even comments that the twist should be `T^(⊗−1)≃H²(π,Z)`, with the canonical self-duality of the integral orientation module. Hua §9 lines1206–1208 instead uses an injection `T↪(∧²Π_ab)^∨` and lines1219–1221 acknowledges reconstructing the difficult marginal sentence.

**Relation / precise reading question:** The peripheral quotient **restates** the later T-lacet setup, while the closed-surface formula presents a specific reading question: is its intended datum a primitive alternating form (an element or rank-one orientation line in the exterior-square dual), rather than an isomorphism onto the whole dual? For genus g≥2 the full exterior-square dual of Z^(2g) has rank g(2g−1), so it cannot be isomorphic to rank-one T; this rank observation is our reasoning, not a new source reading. LM's rank-one H² formulation and Hua's injection are distinct contextual evidence, neither a warrant to alter the frozen display.

**Searches used:** `T.structure`, `isotopi`, `paradigme`; direct LM scans91/101/103 and Hua lines1198–1221.

## G11 — The infinity-isotopy exceptions and the marginal verification flag

**Frozen evidence:** scan074 lines35–38 claims a 1-isotopic and infinity-isotopic description except `(g,ν)=(0,2),(1,0)`; scan075 lines3–5 supplies `K(Z,1)` and `K(Z²,1)`. Scan075 lines7–21 replaces the group by the fundamental groupoid based at nonempty J and claims infinity-isotopy even in those two cases; line22 is the explicit margin “vérifier.”

**Exact source context:** `context/LM_140-2_text.tex`, §19, scan217, lines6917–6924, gives the same two homotopy types. Scan218, lines6946–6958, says the stabilizer of a chosen point is contractible in those exceptional cases. Scan222, lines7057–7060, states the isotopic category equivalence for the anabelian range and explicitly calls it an infinity-isotopic equivalence because the relevant identity components are contractible. Hua §9 lines1211–1226 gives a smooth modern summary but does not reproduce scan075's verification flag.

**Relation / possible note:** The LM passages **support** the mathematical mechanism behind the exception list and the improvement after adding a marked object; the present source **adds** its explicit request for verification. They do not remove that flag or automatically prove every version with an arbitrary discrete J. A precise verification target is the topology of the identity component of homeomorphisms fixing the selected marked objects, including the topology/isotopy convention being used.

**RESULTS_STATE, only if discussing operator groups:** **LM4 C.12**, line354, is **Open (the return's claim)** and concerns an infinite operator group and the kernel `π1(C_A0(u(Γ)),1)`. Its source passage is LM §23, scans279–281, lines8572–8609, where centralizer connectivity and simple connectivity are separated and the general case is flagged “Trop brutal!” This is a **different, stronger equivariant question** than the ordinary marked-surface claim on scan075, so the latter does not settle C.12.

**Searches used:** `contractil|contractib|K\(.*mathbb|cas.*exception|composante.*neutre|C.*A_0`, `isotopi`, and exact `scanpage{279}`, `scanpage{280}`, `scanpage{281}`.

## G12 — What the tame polyhedral list contributes to the finite-action programme

**Exact source context:** `context/LM_140-2_text.tex`, §37, scans571–572, lines16779–16824, identifies the level3/level5 groups and then tables D3,A4,S4,A5 with the modular curves and spherical triangle polyhedra. This is an exact later parallel for scan066's orders12,24,60 and the dihedral family, but the arithmetic level identification occurs in LM, not in scan066. The broader finite-action passage in LM §30, scans383–387, lines11273–11346, explicitly treats geometric/discretizable finite groups and centralizers with conditional or conjectural language; it does not give a general profinite comparison theorem.

**RESULTS_STATE:** **LM4 F.7**, line352, is **Open (the return's claim)** for the nonsolvable centralizer comparison; the row separately claims the solvable genus≤2 comparisons have been proved. **LM4_SUCCESSOR B.38**, line359, remains **Open (the return's claim)** for K5 and levels7/11. **LM4_SUCCESSOR B.39**, line360, also labels the nonsolvable direction open while claiming the solvable centralizer-closure argument. **LM4 D.12**, line349, is open on full profinite torsion; an ordinary geometric involution τ from scan062 cannot settle it.

**Relation / possible note:** The current tame signatures **supply geometric examples/antecedents** for the later polyhedral and finite-action programme; they do not compute completion centralizers, congruence kernels, or torsion in full profinite GT. If a note connects the icosahedral case to B.38 or F.7, it should explicitly say the entry remains open and that these pages contribute the geometric genus-zero model, not a solution. This is the substantive limit of the connection.

**Searches used:** `icosa|tétra|octa|platoni|groupes finis|sous.groupes finis`; exact LM scans383–387 and results IDs `LM4 F.7`, `LM4_SUCCESSOR B.38`, `LM4_SUCCESSOR B.39`, `LM4 D.12`.

## Additional guardrails for the final notes

- Source-level “on va regarder,” a cancelled experiment, and a marginal “vérifier” should remain distinct kinds of evidence.
- No external source was browsed by this research subtask. Historical names and citations mentioned inside Hua's file are credited as his additions and were not independently verified here.
- The provided first-pass notes for cotes147/149 were searched for `groupo[iïî]de|drapeau|surfaces.*orient|pyramide|classif.*fini|normalisat`; no independently checked same-diagram source was obtained from those notes. They are leads, not substitutes for the exact LM passages above.
- **EXIT_TOWER E.24** (RESULTS_STATE line356, Open) concerns an arithmetic-image problem. **EXIT_TOWER E.35/E.39** (lines386/396, Proved as the return's claims) concern the full framed/completed exit system. Neither should be advertised as settled or newly proved by the isolated flag diagrams and ordinary surface groupoids in this assigned subset.
- This memo makes no proposed edits to the frozen files. All questions are for research commentary and future checking under the user's workflow.
