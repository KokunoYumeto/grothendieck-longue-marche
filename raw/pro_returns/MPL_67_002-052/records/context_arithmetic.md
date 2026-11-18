# Context evidence ledger: cote 67, scans 048–051

Research owner: /root/research_arithmetic. Prepared after the parent reported the transcription frozen at 2026-11-18 00:48:19 UTC. Research only: no scan images inspected; no transcription, combined text, doubts, or inventory file changed. The parent owns final notes and concrete calculations.

## Scope, provenance, and availability

Read before research: context/README.md; context/notes/RESULTS_STATE.md in full; context/hua_project/README.md. Read the frozen page files for scans 048–051 and the relevant portions of Hua's modernised reading, particularly §V and §X. The records below compare those frozen readings with supplied context; they do not decide doubtful ink.

The four LM text files are available supplied transcriptions, described by their headers as second-passed. The notes are available research leads with their own local labels such as “checked”; a checked-note label is attributed to that previous pass. The full proofs, results CSVs, referee reports, war-game documents, and several earlier package transcriptions named by RESULTS_STATE are absent from the supplied context. In particular, ARCH_147_003-137_text.tex, the cote 149 source transcription, LM6_POINTS_AS_SECTIONS_results.csv, EXIT_TOWER_results.csv, LM4_FINITE_GROUP_ACTIONS_results.csv, LM7_PUSH_results.csv, FLAGGED_149_results.csv, and WARGAME_MATH_HUNCHES_20261112.md were not available here.

Consequently a register entry supplies its displayed statement head, status, and explicit review scope. It does not supply omitted hypotheses or a proof that this run has checked. References to cote 147 or 149 scans below identify the source location as quoted in the available notes, rather than claiming direct access to those manuscripts.

Classification terms below describe the relation of the frozen cote 67 wording to the identified contextual passage. “Adds” means additional explicit data or a question on the current sheet; “restates” means an explicitly comparable formulation; “differs” marks a written convention or scope requiring a map or further source evidence. No contradiction with a registered mathematical result was established in this research pass.

## N46 — Normal propagator, outer isomorphism, and based isomorphism

**Frozen anchor:** scan 048, own manuscript page 1, archive foliation 50; “avec propagateur normal N”; “un isomorphisme de Teichmüller”; “un isom de groupes (pas ext. !).”

**Searches:** propagateur, extérieur, point base, scindages, Germarc, tangente; N075, E.35, F.43.

**Direct contextual evidence:**

- context/LM_140-2_text.tex, scan 073: the classes of splittings form a torsor, “forment un torseur,” under the displayed H¹(Γ_i,L_i); the page identifies L_i with the Tate module by κ_i. This gives a precise earlier location for the choices entering an arithmetic tangential base point.
- context/LM_140-4_text.tex, §53 continuation, scans 254–255, author folio 775 on scan 255: scan 254 defines the local groupoid of arc germs and writes the functor Germarc(X,x)→Rev_uni(D_x*); scan 255 compares it with Π₁(S_x), where S_x is the circle of tangent half-lines. These are explicit functors in the supplied text.
- context/MPL_147_003-047_notes.md, N075, source cote 147 scan 003 items 9–12 and scans 035–047: “Structure groupoïdale”; “morphismes de générisation.” The note proposes component groupoids and boundary inertia with coherent gluing/generization.

**Relation:** adds a stable singular curve with a normal datum and a particular Teichmüller isomorphism to the earlier based/outer and tangential constructions. The comparison from actual isomorphisms to outer classes is the quotient by inner conjugations. No construction identifying the precise [Y,N] of this sheet with the LM arc-germ groupoid was checked.

**Register:** MPL_147_003-047 N075 is a first-pass lead. EXIT_TOWER E.35 is “Proved (the return's claim),” concerning labelled framed sewing and recovery of boundary-fixed groupoids; the supplied excerpt and source locations are available, its proof is absent. LM6 F.43 is “Proved (the return's claim),” with the displayed scope of a smooth normal-crossings pair in characteristic zero and labelled normal lines; its statement is truncated.

**Hua comparison:** Hua, modernised reading of cote 67, §V, “Isomorphismes de Teichmüller et questions anabéliennes (pages 47 à 50),” restates the two isomorphism levels. His footnote interprets [Y,N] by a tangential base point and refers to his page 74, beyond this packet. The frozen phrase “il est déterminé” remains uncertain, even though Hua writes a definite determination assertion.

## N47 — Claimed incompatibility of outer Galois actions

**Frozen anchor:** scan 048, lower paragraph: “l'isom extérieur déjà n'est pas compatible avec les actions ext.”; the field is a sufficiently large finite extension as written.

**Searches:** compatible, Gal, cyclotomique, Weil, vanishing, limit action; WG H2, E.24, E.45.

**Direct contextual evidence:**

- context/LM_140-2_text.tex, scan 084, author folio 40: “l'hom extérieur κ_i:T→π est compatible avec l'action extérieure de Γ”; the displayed equality is int(g)κ_i(ξ)=int(α)κ_i(χ(p(g))ξ), with the explicit qualification “α∈π (NB pas seulement α∈E !).”
- context/LM_140-2_text.tex, scan 085: “condition de non-trivialité à la Weil.” This is a proposed arithmetic constraint in the manuscript.
- context/MPL_149_091-136_notes.md, RN103-05, source cote 149 scan 103, author manuscript page 51, approximately lines 11–19, with comparisons to scan 101 lines 1–6 and scan 099: source phrase “ne soient géométriques.” The available note records a Tate-cusp test and a weight obstruction as that note's own calculation. Its direct source proofs were not rederived here.
- The same available file, RN103-03 and RN103-04, records a quadratic-twist test against a broader bad-reduction assertion. These are useful scope cautions from prior notes, without a transfer of either verdict to all objects [Y,N].

**Relation:** adds an explicit arithmetic incompatibility assertion to the geometric isomorphism on the same sheet; restates the broader problem of arithmetic realization seen in the cote 149 notes. The current sheet names no vanishing-cycle witness and gives no proof. Calling this a vanishing-cycle problem is a comparison with WG H2, not additional manuscript wording.

**Register:** WG H2 is explicitly an unchecked war-game hunch. Its displayed head says a limit action carries its vanishing cycle; the full assertion is truncated and its source is absent. EXIT_TOWER E.24 and E.45 remain Open, the return's own statuses; this sheet supplies no exact image computation. Hua §V repeats the incompatibility without a proof.

## N48 — Requested three conjugacy classes

**Frozen anchor:** scan 048, marginal NB: “Mettre en évidence trois classes de conjugaison” of homomorphisms Ẑ(1)→π₁(X); “deux seulement si ν=0”; one is then “le vide.”

**Searches:** trois classes, trois types, conjugaison, séparant, vanishing, cyclotomique.

**Evidence and search limits:**

- Hua §V explicitly says the three classes are not identified; he attributes the disappearing class to the ends. That last description is his interpretation.
- context/LM_140-2_text.tex, scans 083–085, especially scan 084's displayed κ_i:T→π with the cyclotomic character, supplies the peripheral comparison map.
- context/LM_140-3_text.tex, §40, scan 043, gives “exactement trois classes de π'-conjugaison de scindages” of 1→π'→E→Z/2→1, corresponding there to three nonzero points of order two. This search hit has its own explicit extension and objects. No map from those section classes to the three classes requested on cote 67 scan 048 was found in the searched passages.
- context/notes/RESULTS_STATE.md, LM4 D.32, names the three peripherals x, y, (xy)⁻¹ in F̂(x,y) and the subgroup of Out(F) preserving them. This records three specifically named cusps in that row; it does not name the three families left unspecified on scan 048.

**Relation:** the present margin adds a recognition task. The count and ν=0 qualification may be preserved without assigning further names. “Families” is editorial wording; the frozen noun is “classes.”

**Register:** WG H2 unchecked; LM6 F.43 Proved as a return claim, with truncated normal-stratum statement; LM6 A.22 Open, with the specific full-CM-group scope recorded under N50. LM4 D.32 is Proved and expressly refereed 14 Nov 2026 as claimed, but its full result and proof are not supplied.

## N49 — Extension of the anabelian conjecture to the enhanced singular curve

**Frozen anchor:** scan 049, own manuscript page 2, archive foliation 51, question (a): “À examiner”; “Extension de la conjecture fondamentale”; “singulières (stables, avec propagateur normal).”

**Searches:** singuli, anabél, normale, conjecture fondamentale, F.43.

**Direct contextual evidence:**

- context/LM_140-2_text.tex, §34, scan 483, author folio 245, introduces 1→π→E→Γ⁺→1 and asks whether the loop structure must be included in the data; “Une première question : faut-il mettre la structure à lacets.”
- The continuation on scan 484 describes the desired fully faithful functor from algebraic curves to outer profinite groups with arithmetic action, and spells out restriction from Γ to an open subgroup for base extension. This supplies the comparison functor actually written in the LM context.
- context/MPL_149_091-136_notes.md, RN101-04, source scan 101, manuscript page 50, approximately lines 11–13: “structure à l'infini”; the note links stable dual graphs to degeneration data.

**Relation:** adds stable singular curves with normal propagators to the objects explicitly discussed in the earlier anabelian program. The current sheet supplies no fully specified enhanced comparison functor or full-faithfulness proof.

**Register:** LM6 F.43 remains a Proved return claim about the displayed normal-crossing setting. WG2 §1.1 #6 and §1.4 #3 are unchecked plans, describing the cote 149 normal-boundary ending and its possible continuation. Hua §V repeats the question and lists later literature; no broad later theorem was newly checked in this pass.

## N50 — Procyclic recognition, normalizers, and cyclotomic action

**Frozen anchor:** scan 049(b): “est-il vrai qu'on récupère”; classes of subgroups isomorphic to Ẑ, externally invariant under π₁(K); “automatiquement via le caractère cyclotomique.”

**Searches:** procyclic, normalizer, Norm, cyclotom, Sing; A.22, B.27, ZCF6.

**Direct contextual evidence:**

- context/LM_140-2_text.tex, scan 084, folio 40, gives the actual cyclotomic equation for κ_i and the correction β=α⁻¹g lying in the normalizer of its peripheral image.
- context/LM_140-2_text.tex, §34, scan 483, folio 245: “Les sous-groupes à lacets L_i sont les sous-groupes maximaux ... tels que Norm_E(L_i)→Γ⁺” has open image. The margin there says “tout sous-groupe ≠1”; cote 67(b) explicitly specifies Ẑ.
- context/LM_140-2_notes.md, LM_P049 second-pass B4, source scan 483, records the characteristic-commutator-subgroup objection to that unrestricted marginal wording and calls for an abelian/procyclic restriction. This is a prior checked-note claim; no reproof was attempted here.

**Relation:** restates the normalizer-recognition question with an explicit procyclic restriction and adds singular points to the marked-point target. The word “automatiquement” remains an assertion to assess in its arithmetic setting.

**Register and exact IDs:**

- LM6 A.22: Open, return's claim. The visible scope is the full CM group, a nontrivial closed procyclic C⊂R, and arithmetic normalizer image open in G_Q(i). Its source locator is LM8 G.20–G.22. The omitted continuation and full proof are unavailable.
- LM6 B.27: Open, return's claim. The displayed head retains point-surjectivity for zero-cyclotomic-centralizer sections of the tripod over a number field, plus a point-or-cusp problem over specified extensions of Q_p. Source locators include LM §§8–9,32,34, LM_140-2 scans061–079,395–436,480–490.
- **FLAGGED_149 ZCF6** is the exact identifier, including the underscore. Open, return's claim. The title is “The existence assertions retained after the centralizer computation.” The visible location is cote 149 §§2–3, manuscript pp.22–34 and51, scans045,048–049,051,056–057,059–063,066–069,104. The enumerated assertions are truncated, so this supplies only the stated existence-issue background.

**Hua:** §V restates question (b); his accompanying history is an attributed interpretation, not an additional check of the current claim.

## N51 — Compactification and specialization

**Frozen anchor:** scan 049(c): “S'inspirant des compactifications MD des M_gν”; “Comportement par spécialisation ???”

**Searches:** compactification, spécialisation, générisation, normal, torseur, angular, N075.

**Direct contextual evidence:**

- context/LM_140-2_text.tex, scans 402–403, author folio 204 on scan 403: the discussion doubts sufficiency of successive forgetful compatibility; “Il est possible qu'il faille faire intervenir des propriétés des π₁ des M_gν ... liés à la compactification.”
- context/MPL_147_003-047_notes.md, N075, source scan 003 items9–12 and scans035–047, proposes component groupoids, boundary inertia, gluing, and generization compatibility. This is the available full note behind the abbreviated register row.
- context/MPL_147_048-137_notes.md, R122-01, source scan122, equations186–187: “immersion régulière ... de codim1”; R123-01, source scan123, equations190–192: “et par descente on trouve ... un torseur.” These are exact locations for normal-line factors and descent.
- Same file, R127-02, source scan127: the direct generization arrow is cancelled; R133-02, source scan133: the decorated system needs compatible face functors. These available notes preserve the incomplete nature of the source construction.
- context/MPL_149_091-136_notes.md, X01–X04, especially X02, source scan136 display40: “l'action extérieure ‘cyclotomique’”; the note compares the T^J maps with root stabilizers and normal-line torsors, while explicitly retaining injectivity and recognition questions.

**Relation:** restates the search for boundary compatibility and adds the explicit target “compactification anabélienne” with specialization as a named question. The exact named maps and the cancelled source proposals should remain visible in a comparison.

**Register:** N075 first-pass lead; LM6 F.43 and EXIT_TOWER E.35 Proved return claims, full proofs absent; E.24/E.45 Open. WG2 §1.1 #6 and §1.4 #3 unchecked. Hua §V restates the question; see the limited modern local model under N52.

## N52 — Local normal tensor and polar model

**Frozen anchor:** scans048–049, “propagateur normal.”

**Searches:** propagateur, tensor, branches, normal, log; Nakayama Ogus relative rounding.

**Available source evidence:** Hua, modernised reading of cote67, §X, “Des surfaces à bord aux courbes stables (pages73 à81),” writes t_x∈T_{X'',x₁}⊗_C T_{X'',x₂} and calls this a “structure de propagation normale.” His pages73–81 lie beyond this packet; this is his attributed interpretation of later material. His §V footnote points to page74.

**Relation:** adds later explanatory data to the present sheet. The root's coordinate-change calculation is separate work; this agent did not perform or certify it.

**Primary literature actually opened:** Nakayama–Ogus, Relative rounding in toric and logarithmic geometry, Geometry & Topology14 (2010),2189–2241, DOI10.2140/gt.2010.14.2189. Publisher PDF: https://msp.org/gt/2010/14-4/gt-v14-n4-p09-p.pdf . Read pp2189–2190's xy=t example and its polar map ((r₁,r₂),(ζ₁,ζ₂))↦(r₁r₂,ζ₁ζ₂); p2226 Theorem5.1; pp2227–2228's log-inertia and nearby-cycle discussion. The theorem's stated scope includes properness, separation, exactness, relative log smoothness, a fine base, and relative coherence. No theorem about the arithmetic object [Y,N] was applied. The explicit polar map is the concrete comparison supplied here.

**Register:** LM6 F.43 and EXIT_TOWER E.35 retain their recorded statuses. No comparison with their unavailable proofs was certified. Parent was notified to open the publisher URL before citing it.

## N53–N54 — Three presentation programs and the doubtful adjective

**Frozen anchors:** scan050: “Je m'attends à trouver trois types de présentations”; pants/triads, Lego automorphisms and deformation paths, and involutions. The frozen boundary adjective is cubiques|critiques.

**Searches:** Lego, Légo, pantalons, triades, présentation, antiques, cubiques; E.23, E.35, E.39.

**Contextual evidence:**

- context/LM_140-3_text.tex, scan694, diagrams11–14: “Il est tentant de reconstituer G ... une sorte de ‘somme amalgamée’.” The maps from the displayed N_i supply an explicit earlier reconstruction diagram. Cote67 adds the proposed geometric pieces and their deformation paths.
- context/LM_140-4_text.tex, §53, scans234–237, displays the modular covering-group presentations and their reflection generators; exact formulas are recorded below.
- context/MPL_147_003-047_notes.md, N075, is the precise available compatibility lead.
- Hua §V, footnote to presentation(a), source page49=scan050, reads “les plus antiques” and interprets this as maximally degenerate stable curves. This is an exact competing reading only; it does not alter the frozen adjective.

**Relation:** restates a program of assembly by maps and automorphisms, adds three complementary arithmetic presentation aims, and differs from Hua at the unresolved adjective. The future-tense expectation remains on the page.

**Register:** EXIT_TOWER E.23, E.35, E.39 are Proved return claims, unreviewed in this supplied excerpt; E.24 and E.45 Open. E.23's visible source includes cote147 §7 scan060 and §10 scans090–104. N075 remains a first-pass lead. No five-point identity or exact arithmetic-image computation was obtained from the two low-genus examples.

## N55 — Existing modular calculation and reflection dictionary

**Frozen anchor:** scan050 displays ρ³=σ², ρ⁶=σ⁴=1 and the corresponding products of three reflections, with the frozen exponent uncertainties preserved in the page file.

**Searches:** SL, Sl, u4, u6, r_0, r_1, r_infty, réflexion, S01.

**Exact prior calculation already available:**

- context/LM_140-2_notes.md, heading LM_P052, “Second-pass notes (own),” S01, source scans513–516, explicitly records u4=[[0,−1],[1,0]] and u6=[[0,−1],[1,1]], with u4²=u6³=−I and the C4*_{C2}C6 presentation. This is exactly the S,R pair proposed by the parent. Attribute it to the prior checked note and avoid presenting it as a new result.

**Direct manuscript comparison:**

- context/LM_140-4_text.tex, §53, scan234 equation25, scan235 author folio765, equations27–28: the covering-group presentation and its central generator ω₀.
- Scan236 writes r_∞=[[-1,0],[0,1]], r₀=[[0,1],[1,0]], r₁=[[-1,1],[0,1]], with r₁=ρ⁻¹r₀=r₀ρ and r_∞=σr₀=r₀σ⁻¹. The same page gives the infinite-dihedral amalgam and inclusion maps using ρ̃⁻³ and σ̃².
- Scan237, author folio766, equation34: the three involutions obey (r̃₀r̃₁)³(r̃_∞r̃₀)²=1.
- context/LM_140-4_notes.md, heading LM_C4-229-247, R23–R25, source scans236–237, checks the displayed products and discusses the quotient presentation.
- context/LM_140-3_text.tex, scan404, author folio503, equation35 repeats the three reflection matrices; scan406, folio504, retains them in the modular arithmetic construction.
- context/LM_140-3_notes.md, N32 under scans405–406, explicitly records that r₁r_∞ is [[1,1],[0,1]] and r_∞r₀ is S, hence its claimed generation check.

**Relation:** restates the genus-one generator pattern. The parent-owned source-to-source matrix assignment records the precise convention and central sign; no proof of presentation completeness was undertaken here.

**Register:** no displayed RESULTS_STATE row specifically registers this finite matrix multiplication. LM4_SUCCESSOR E.10 remains Open for involution congruence kernels. LM7_PUSH D.44 is broader modular descent, with review restricted to the portions used by D.50 and E.58; it supplies no permission to infer missing presentation details from its abbreviated statement.

## N56 — The low-genus exact sequences and the ambiguous index

**Frozen anchor:** scan051 first diagrams, the index 0|1,1, SL₂(Z)/±1 and SL₂(Z/2). The frozen index is not repaired.

**Searches:** Legendre, S_3, S_4, 0,1, 1,1, prime, rigidification.

**Direct contextual evidence and maps:**

- context/LM_140-2_text.tex, §37, scan533, author folio272: the quotient functor on equivariant covers; scan534 equation1 gives Rev(X,G)→Rev_d(Y) by X'↦X'/G, with normalized fibre product described for the reverse construction.
- Scan535, folio273, equation3 gives the associated extension of G by π₁(X). The example is U_{0,3} with the S3 action.
- Scan536 equations5bis–7 explains the base-path choice and inner-conjugation ambiguity, then writes 1→Π_{0,3}→Π'_{0,3}→S3→1.
- Scan537, folio274, diagram8 places its profinite version in the arithmetic diagram over Γ_Q.
- Scans538–541 distinguish the level-two stack, its quotient by the central symmetry, and the higher-level covers. Scan538 says M_{1,1}[2] is a gerbe over M_{1,1}[2]'; scan541 spells out what the quotient formula produces at levels1 and2.
- context/LM_140-3_text.tex, §38, scans009–010, author folio293 on scan010: the weighted quotient U03/S3, the presentation with orders2 and3, and the primed modular/cartographic groups. The finite quotient map and its weighted ramification are explicit; central/primed conventions stay part of the comparison.

**Relation:** restates the level-two quotient pattern, with the current draft's unresolved genus index and symbols retained. Hua §V, last paragraph and footnote, says the page writes “0,1” and replaces it by (1,1) in his explanation. That replacement is his interpretation.

**Register:** LM7_PUSH D.44 Proved, with only the parts used by D.50/E.58 expressly refereed as claimed; full source absent. LM4 D.32 Proved and refereed as claimed. LM4 D.34 is named in the referee-summary list, but no individual statement is displayed in this digest, so no title or exact scope was inferred for D.34.

## N57 — Unfinished level-four denominator

**Frozen anchor:** scan051, SL(2,Z/4Z)/ followed by an unfinished denominator.

**Searches:** SL/Sl and Z/4, sl(2,F2), 117, quotient, congruence.

**Precise source hit:** context/LM_140-4_text.tex, §51, scan066, equation117, identifies the kernel of SL₂(Z/4)→SL₂(Z/2) with sl₂(F₂), and writes a normal subgroup sl₂(F₂)' of rank two, whose three nonzero elements are λ̇₀,λ̇₁,λ̇_∞. Its margin displays SL₂(Z/4)/sl₂(F₂)' underbraced as G₀⁺/Π₀. Scan066 has no written author-folio marker: scan065 is marked680 and scan067 is marked681; “680 verso” is an inference from that sequence.

**Additional available lead:** context/LM_140-3_notes.md, N31 under scans538–541, source scan539, says the quotient is SL₂(Z/4) “sans prime”; that note records the surviving central sign. It does not identify the missing denominator on cote67 scan051.

**Relation:** adds a precise later quotient to compare with the unfinished draft. No map identifying its denominator with the cote67 dashes was established. The existing rank-two subgroup is a search target, not a transcription repair.

**Register:** LM2 congruence rows retain their own unreviewed statuses; LM4_SUCCESSOR E.10 remains Open. No row was promoted to a verdict on this unfinished notation.

## N58 — Borel quotient and rational lines

**Frozen anchor:** scan051, SL₂(Z)/(±1·Z_Borel), P¹(Z)|P¹_Z and P¹(Q), with the arrow to P¹(Z/2).

**Searches:** Borel, ration, cusps, projective-line formulas in LM_140-2/3/4.

**Evidence:** Hua §V, last paragraph, source page50=scan051, explicitly reads the quotient as the modular cusps. The supplied LM files contain broader Borel constructions, but the searches did not produce an exact predecessor for the displayed integral orbit map within the reviewed passages. The modular matrices at LM_140-4 scans234–236 supply surrounding conventions only.

**Relation:** the root's map g↦g·[1:0], stabilizer, primitive-column argument and reduction modulo2 are root-owned calculations. This agent does not mark them verified. The manuscript and Hua supply the source interpretation, rather than a separate proof recovered here.

**Register:** LM4 D.32 can remain background with its actual three-peripheral scope. D.34's statement is unavailable in this digest. LM2 C.r1/C.r2/C.r3 are relevant convention warnings about outer congruence images, with their return-claim statuses preserved.

## N59 — Peripheral products and the shared seam

**Frozen anchor:** scan051 writes ℓ₀ℓ₁ℓ∞=1 and ℓ∞=ℓ'∞ beside another pants product. The displayed equality contains no inverse.

**Searches:** lacets, ell, produit, seam, sewing, framed.

**Contextual evidence:** context/LM_140-3_text.tex, scan009, writes l'∞l'₁l'₀=1 in its quotient construction; scan010, equation18, records based generator products. These supply explicit differing product orders that require paths and directions in any comparison. EXIT_TOWER E.35's displayed statement names labelled framed sewing, and N075 supplies the available compatibility lead.

**Relation:** the frozen page adds a specific seam equality. Relating the loop words requires a chosen gluing map, orientation convention, and based paths. The parent owns the circle-reversal calculation; this ledger supplies no implicit correction of the written equality.

**Register:** E.35 Proved as a return claim, proof unavailable; PUSH_ORDER5_FRAME Itemsfromt 2 remains Open. No five-point identity was extracted from these words.

## N60 — Forgetting a marked point

**Frozen anchor:** scan051, lower sequence 1→Π_{g,ν−1}→T_{g,ν}→T_{g,ν−1}→1 and the universal-family sketch.

**Searches:** universelle, suite exacte, homotopie, oubli, 2g.

**Exact direct predecessor:** context/LM_140-2_text.tex, scan188, author folio read as 94|99. The source defines the loop automorphism group fixing its labels and orientation, writes “pour 2g+ν≥3,” identifies M_{g,ν+1} as the “courbe complexe universelle ... à ν trous numérotés,” and displays

π₂(M_{g,ν})→π₁(U)→π₁(M_{g,ν+1})→π₁(M_{g,ν})→π₀(U),

with lower row 0→Π_{g,ν}→T^{00}_{g,ν+1}→T^{00}_{g,ν}→1. The margin says its universal cover is contractible.

**Relation:** restates this sequence after replacing the predecessor's puncture count by ν−1. The source's range, marking convention and written superscripts belong to the comparison; the current sketch does not spell them out.

**Further available checked-note caution:** context/LM_140-2_notes.md, C07, source scan220, discusses the kernel in exceptional low types and a proposed correction to their exclusion list. This earlier note's calculation was not rederived here.

**Register:** EXIT_TOWER E.36 is Proved as the return's claim on capping, forgetting, and quotient actions; its full proof is absent. E.45 is Open. Hua §V records the same forgetful pattern.

## N61–N62 — Boundaries of the arithmetic contribution to tower and involution questions

**Searches:** pentagon, commut, clutching, forget, involution, centralizer, K_c, E.10, C.12.

Scan050 explicitly supplies three presentation aims, automorphism groups of pieces and deformation paths. Scan051 explicitly supplies the low-genus diagrams and forgetting sketch. The connection to the five-point frame problem is through those written operations and relations; this research scope supplied no Θ₃/Θ₄/Θ₅ morphism or pentagon evaluation.

RESULTS_STATE orientation identifies PUSH_ORDER5_FRAME Itemsfromt2 as Open; LM4_SUCCESSOR E.10 as Open for congruence-kernel computations of involutions; and LM4_SUCCESSOR B.39 as Open for a nonsolvable centralizer direction. LM6 C.12 is Open for the indicated involution and centralizer classification in full profinite extended mapping-class groups at g≥3, with source LM §33, folios222v–226v, LM_140-2 scans440–448. The finite reflection matrices on scan050 supply comparison representatives; their multiplication does not compute those register objects.

The parent or the parallel metric researcher owns scans026 and032–039. This ledger makes no new finding on the elliptic lattice-cohomology leaf or the fixed-metric computations.

## Congruence-register audit

Read context/LM2_CONGRUENCE_ROWS.md in full. The file explicitly says every row is the unreviewed return's claim. Its scan numbers below are in LM_140-3 unless separately identified by the file's section and folio.

| ID | Recorded status | Exact visible scope and source |
|---|---|---|
| LM2 C.r1 | Proved, return claim | Arithmetic outer congruence image, units modulo squares; §39 fols299–300 scans022–024. |
| LM2 C.r2 | Refuted, return claim | Uniqueness of a multiplier on outer congruence actions; corrected square-class statement; §39 fols300v–301 scans025–026. |
| LM2 C.r3 | Proved, return claim | Actual and outer arithmetic action images with their specified targets; §§39,45 fols299–301,387–388 scans022–026,176–178. |
| LM2 C.d1 | Known, return claim | Preservation of projective congruence kernels by actual GT0 loop automorphisms; §39 scans021–030, §44 scans150–168, §46 scans198–202,218–219. |
| LM2 C.d2 | Proved, return claim | Matrix norm equations and residual characters; §46 fols398,400 scans198(73),202–203(88). |
| LM2 C.d3 | Proved, return claim | Local adelic solution locus and sign compatibility; §46 scans202–205, §48 scans254–266. |
| LM2 C.d4 | Proved, return claim | Intrinsic normalizer fibre product; §46 scans193,204–205, §48 scans254–266. |
| LM2 C.d5 | Open, return claim | Simultaneous realization of two torus coordinates; §46 fol401 scans204–205. |
| LM2 C.r4 | Proved, return claim | Congruence restrictions and the absolute graded-form question; §39 scans021–030, §41 scans054–057, §46 scans198–202. |
| LM2 C.r5 | Proved, return claim | GT0 mapping into Out of full profinite linear modular group; §§45–46 fols384–391 scans170–184. |

The maps in scans048 and051 make the actual/outer and central-quotient conventions worth retaining. No computation of these registered congruence images was attempted, and no value of the CM-parity character LM7_PUSH E.65 was read off from the packet. E.65 is Proved with the register's express referee note “two gaps closed by the referee”; its source and reports are absent. The digest's latest unrefereed EXIT_TOWER E.49 claim is retained with that review status, rather than used to close an open question here.

## Primary-literature and search log

1. Searched for Nakayama–Ogus “Relative rounding in toric and logarithmic geometry” and Deligne “15.23”; then opened the author and publisher PDFs of Nakayama–Ogus. The publisher result was verified through a targeted authoritative search. Facts actually read and allowable use are recorded under N52.
2. Author preprint URL: https://math.berkeley.edu/~ogus/preprints/nakayamaogus.pdf . It has placeholder journal pagination, so the final locator uses the publisher PDF.
3. Opened https://webusers.imj-prg.fr/~pierre.lochak/textes/crelle.pdf for the Hatcher–Lochak–Schneps lead in N075. The retrieval exposed a 24-page PDF with no readable text lines. No theorem from this PDF was newly checked. N075's previously recorded description remains a first-pass contextual lead.
4. No Deligne primary source was successfully retrieved by this focused search; the Deligne references in the supplied notes and in Hua remain attributed references.
5. Root was notified of the publisher URL and the exact checked locations, and must open the source for its own final web citations.

## Draft audit delivered to the parent

- Correct N50's “FLAGGED149 ZCF6” to **FLAGGED_149 ZCF6**.
- Preserve LM6 A.22's full-CM-group and G_Q(i) scope.
- Prefer LM_140-2 §37 scans533–537 for N56's actual quotient maps; LM4 D.32 remains background.
- D.34 has a referee-summary entry, but its statement is absent from the supplied digest.
- Scan066's author folio680v is inferred from scans065/067; cite scan066 equation117 directly.
- The exact S,R matrix pair in N55 already occurs in LM_P052 S01. The new calculation can be limited to the reflection assignment and source conventions.
- The frozen margin in N48 says “classes”; assigning named families remains editorial.

This ledger records textual comparison and source retrieval. It does not create a proof-review event for an abbreviated RESULTS_STATE entry.
