# Context dossier: lecture programme, topoi, universal constructions, and examples

Prepared from the frozen text only; no page file or combined transcription changed. References of the form `136/305:15–46` mean cote 136, scan 305, lines 15–46 of `pages/MPL_136_282-327_136_scan305.tex`, not PDF page numbers or later foliation. Every current-page quotation below is from that frozen file. The current inventory distinguishes 10 reused typed faces (282, 284, 286, 288, 290, 292, 294, 296, 298, 300), one cover (301), one cancelled draft (321), and 33 text faces; scan 319 is absent from the supplied current set.

## Evidence and status conventions

`context/README.md` and the entire `context/notes/RESULTS_STATE.md` were read before this dossier was written. The earlier notes were searched and their relevant programme, topos, universal-construction, examples, and mathematical-caution sections read: `context/same_cote_136/MPL_136_047-094_notes.md` (A), `MPL_136_095-141_notes.md` (B), `MPL_136_189-234_notes.md` (C), and `MPL_136_235-281_notes.md` (D). These are explicitly first-pass, unreviewed leads under README lines 33, 39–43; their quotations from earlier scans are reported evidence, not a new verification of those scans.

`R` below means `context/notes/RESULTS_STATE.md`. An entry described as settled *in R* remains a reported result of the earlier project unless a specific review is recorded; this dossier does not independently certify its proof. `WG2 §Week #3`, `WG2 §2.4 #5`, and `WG H6` are unchecked plans or hunches, not theorem statuses. No external search was needed for this bounded comparison, and the dossier does not use the unsupplied text of *Pursuing Stacks* §94 as evidence.

## Direct answers to the assigned questions

| Question | Bounded answer from the current frozen text and supplied leads |
|---|---|
| “Topos de De Rham” and “faisceautisation” | Current 302 names the simplicial presheaf topos viewpoint; 314 proposes the extension of universal abelianization to an arbitrary topos. Neither defines a separate de Rham site. A, R027–R041, reports the earlier operative construction on 080–091: internal PD/exterior resolutions, tensor-universal flasqueness, and a de Rham existence condition. |
| Lecture plan | 301 is an actual title sheet, with the first word still doubtful, followed by 302–318 numbered 1–17 and a programme in 302. This is substantially stronger documentary evidence than the earlier packages, although it neither supplies the complete IHÉS lecture outline nor proves delivery order. |
| “Constructions universelles” | The title is now literal; 303–305 identify the universal cosimplicial simplex object and extension from simplices, 311–314 identify universal additive chains/abelianization, and 315–318 investigate categories of operations with explicit unfinished steps. |
| Abelian varieties and Fourier/Chern examples | Abelian schemes appear on reused Exposé IX leaves; their occurrence does not make them PD lecture examples. No literal “Fourier” or “Chern” occurs in the current text, but live 326 has possible characteristic-class notation `c_1`, `c_2`, and live 327 genuinely investigates a complex curve and a canonical connection. |
| “Ombre”, “tubulure”, and cote 137 | Neither term nor an explicit cote-137 application is present in the current frozen text. The module `M⊗h{T}` on 299 is a precise comparison lead for module shadows; it does not define the terminology or identify a tubulure. |

## Proposed research items

### CL01 — An authored title sheet and a locally numbered exposition are now present

**Current:** 136/301:3–5, `\unsure{Notations|Notions} $\tfrac12$ simpliciales` / “Constructions universelles”; 136/302:2–3, `\mspage{1}` and `1975\quad\unsure{à}\quad1976`; 136/318:2, `\mspage{17}`. **Context:** A, standing title section and R059 (080, 084, 094); B, §§1.4, 3 (095–141); C, R007 (190–234); D, N14 (244–281). **Relation:** adds. **RESULTS_STATE:** `WG2 §Week #3` [unchecked reading plan]; no entry settles authorship, exact date, or delivery order of this numbered unit.

The cover and the seventeen consecutive manuscript page labels establish a distinct local exposition on semisimplicial notation and universal constructions, with an adjacent 1975–1976 date cue whose connective remains uncertain. Earlier packages' statements that their own ranges lacked a cover or authored outline remain valid but no longer describe all supplied cote-136 material. Neither the cover nor the numbering claims seventeen pages for the entire lecture, and the marginal “302” is a different numbering system rather than a page total.

### CL02 — The programme is a systematic study of structured invariants and operations

**Current:** 136/302:22, “Tous les développements qui suivront ont pour objet d'étudier ces objets” and “étude systématique, dans l'esprit de l'algèbre universelle”; 136/312:11–13, “le contenu essentiel de nos réflexions.” **Context:** B, §1.4 (096–141); C, R007 (190–234); D, N14 (235–281); README:17–25. **Relation:** adds. **RESULTS_STATE:** `WG2 §Week #3` [unchecked plan]; `follow-ups @305` [open] for the stronger homotopy-reconstruction goal.

The author's programme moves from simplicial objects to covariant and contravariant invariants, their extra structures, and operations producing new complexes; 312 identifies the systematic study of these structures as the central concern. This directly supports the homotopical tag in R's orientation, while giving a more precise purpose than an inferred sequence of technical headings. The programme itself does not prove that one PD cochain object recovers every integral homotopy type.

### CL03 — Current topos terminology is concrete; the earlier faisceautisation remains a reported construction

**Current:** 136/302:22, “objet d'un topos” / “faisceau sur un topos”; 136/302:9–20, the displayed simplicial presheaf and functor-category notation. **Context:** A, R027–R041 (080–091), especially the reported heading “Faisceautisation du topos De Rham” on 080 and “Condition de De Rham sur Anneau k” on 091; B, §1.2 and N20–N28 (113–119); D, N15 (235–281). **Relation:** adds to the later ranges; differs from a claim that a new geometric site has been identified. **RESULTS_STATE:** `follow-ups @305` [open]; `WG H6` [unchecked hunch]; no result entry identifies a de Rham site here.

The current passage uses the simplicial presheaf topos as one viewpoint on the same combinatorial objects, without giving objects, covers, or an associated-sheaf functor for a separately named de Rham site. A reports that the earlier faisceautisation works internally with an embedding, flat cokernel, positive PD/exterior powers that remain flasque after tensoring, and a resolution of `Z{T}` followed by `k{T}` base change. On that unreviewed evidence, the best operational reading is an internal sheaf-theoretic PD resolution with cohomology comparisons, which must be verified against 080–091 before being promoted to a settled historical definition.

### CL04 — Universal abelianization in an arbitrary topos is a different extension claim

**Current:** 136/314:68–72, “abélianisation” and “doit se maintenir pour un topos quelconque.” **Context:** A, R039–R040 (091), reporting simplicial/topological examples of the de Rham condition and “Est-ce vrai pour … ? Non” for the opposite simplex topos; B, N20 (113). **Relation:** differs; adds a separate universal-property expectation. **RESULTS_STATE:** no directly matching settled entry; `WG H6` [unchecked] is only a broad comparison.

The extension to “un topos quelconque” concerns the preceding universal abelianization argument, not the tensor-acyclic embedding required by the earlier reported de Rham condition. Consequently, it neither proves that condition for every topos nor contradicts the earlier negative annotation about the opposite simplex topos. A useful verification would formulate the two universal problems separately and specify the target additive categories and colimits allowed in 314.

### CL05 — “Demi-simplicial” must be interpreted through the actual indexing conventions

**Current:** 136/302:5–7, “cat. des simplexes” with ordered `[0,n]`; 136/303:46–47, `\operatorname{Hom}_{\mathrm{ord}}` and “objet cosimplicial universel”; 136/306:36–43, “Dold-Puppe” and “non-dégénéré.” **Context:** C, R009 (194, 227, 229, 231), explicitly warning against identification with `Delta_inj`. **Relation:** restates and adds direct definitional evidence. **RESULTS_STATE:** `PRETOT A.12` [Proved return claim; reviewed run] and `TOTASPH C.10` [Refuted return claim] concern `Delta_inj`; neither transfers merely from the word “simplicial.”

The finite ordered simplex notation and normalization equivalence support reading the present formalism with its full simplicial operators, including the degeneracy structure required by the displayed Dold–Puppe discussion. This supplies additional evidence for C's warning: the historical notation `1/2 simplicial` does not by itself denote the modern category of injective simplex maps. The literal functor-category and set-map notation on 302–303 still contains transcription-level or authorial tensions that must remain visible rather than be silently regularized.

### CL06 — Proposition 1 identifies a precise universal construction from simplices

**Current:** 136/305:15–46, “Proposition 1,” evaluation `F\longmapsto F(\Delta^*)`, and “pas seulement pour … Delta, et bien connu.” **Context:** B, §1.3, N44–N48 and O12 (127–129), extension from simplices; C, R006 (204, 215, 225–226), free PD and normalization constructions; D, N13 (235, 248–252, 275, 281). **Relation:** adds the explicit general categorical framework; differs from the particular free PD algebra. **RESULTS_STATE:** no directly matching result entry; `WG2 §Week #3` [unchecked planning question].

Proposition 1 identifies covariant colimit-preserving functors out of simplicial sets with cosimplicial objects, and the contravariant limit version with simplicial objects in the target category. Its category-of-simplices formula supplies the general construction underlying the earlier reported extensions, with the required size and existence-of-limits hypotheses retained. This is a universal property of a presheaf category, not yet a homotopy-invariance or PD-comparison theorem.

### CL07 — The author expressly separates raw representable invariants from homotopy invariants

**Current:** 136/306:17–34, “ce ne sont pas des invariants du type d'homotopie de X_*” and “catégories de fractions.” **Context:** B, O12 (127–129) and N29–N36 (119–121), universal extension versus homotopy invariance and a conjectural calculus of fractions; A, R037–R042 (089–094), comparison zigzags and localization. **Relation:** restates the distinction and adds an explicit programme. **RESULTS_STATE:** `gap g1004` [open]; `follow-ups @305` [open].

The manuscript says that representable or simplex-defined invariants are too coarse in structure to be homotopy invariants directly, and proposes adding structure before inverting arrows induced by homotopy equivalences. This sharpens the interpretation of the earlier localization and uniqueness leads without supplying their missing calculus-of-fractions or coherence proofs. The phrase “de façon plus ou moins complète” also leaves the eventual strength of homotopy-type recovery deliberately qualified.

### CL08 — Free chains are universal for additive invariants at the stated level

**Current:** 136/311:57–69, the boxed Hom formula and “l'invariant additif universel”; 136/313:43–58, Proposition 3 with target `(Ab_\cdot)^o`. **Context:** B, N44–N48 (127–129), chain construction from simplices; C, R006 (225–226), representability of normalization; D, N13 (275). **Relation:** adds an explicit classifier and universal factorization. **RESULTS_STATE:** no matching settled entry; `follow-ups @305` [open] remains a strictly stronger structured-homotopy question.

The displayed formula expresses the relevant contravariant additive invariant as `Hom_\cdot(C_\cdot(X_*),K_\cdot)`, and Proposition 3 proposes its universal factorization through the opposite category of chain complexes. This explains exactly the sense in which free chains serve as the additive invariant, while preserving the opposite-category convention and limit-preservation requirement. It does not state that a bare chain complex determines products, PD operations, or the integral homotopy type.

### CL09 — Multiplication requires extra structure beyond the bare chain complex

**Current:** 136/311:71–74 and 136/312:3–13, “n'est pas reconstructible par / la seule connaissance de C_\cdot” and “structures supplémentaires convenables.” **Context:** D, N40 (273), “compatible avec multiplication”; A, R030 (080–082), binomial weight multiplication; B, N19 and N54 (113, 135), multiplicative structures. **Relation:** adds a direct warning relevant to the earlier open comparison. **RESULTS_STATE:** `gap g1048` [open multiplication problem; earlier linear results reported settled in a repaired setting]; `follow-ups @305` [open].

The author explicitly says that knowing the additive chain complex alone does not reconstruct a richer multiplicative invariant, and that extra structures inherited from the simplicial set must be described. This independently supports keeping the linear reconstruction in R's report of g1048 separate from its still-open multiplication clause. A promising next step is to identify the exact diagonal or operation data retained by the weighted construction and compare their coherence before and after the proposed localization.

### CL10 — Normalization is not asserted to preserve the displayed multiplicative structures

**Current:** 136/318:25–27, “structures multiplicatives — qui ne se correspondent pas par DP et ND” and “sauf de les définir par transport de structure via DP !” **Context:** C, R006 and R009 (225–231), normalization; D, N40 (273), multiplication; B, §1.3 (127–129). **Relation:** adds a structural qualification. **RESULTS_STATE:** `gap g1048` [open]; `follow-ups @305` [open]; no entry turns the additive equivalence into a strict multiplicative identification.

The stated Dold–Puppe equivalence is additive, while the manuscript warns that the multiplicative structures under discussion do not correspond under its two displayed functors. Its remark about exterior, divided, and symmetric powers then explicitly allows transport of structure, so the passage should not be paraphrased as a general nonexistence theorem for all operations on chain complexes. Verification should distinguish the native tensor product from a transported one and specify which operations the PD construction requires.

### CL11 — The operation-category construction remains explicitly unfinished

**Current:** 136/315:75, “à préciser la signification de ces formules”; 136/316:38–55, “principes généraux (que je / n'ai pas détaillés)”; 136/318:20, “Sous réserve que … soit assez gros pour permettre au moins de faire des projecteurs !” **Context:** D, N13 and N41 (275), existence of tensor/internal Hom objects; C, R006 (215), universal free algebra with an unfinished proof. **Relation:** adds explicit reservations and a proposed smaller class of universal operations. **RESULTS_STATE:** no directly matching settled entry; `GALOIS E.11` and `GALOIS G.6` [Open return claims] are only broader cautions about unspecified formalism.

The restricted family of allowed limit or colimit shapes is intended to generate a corresponding category of operations, but the manuscript acknowledges that the general principles and displayed formulas have not been fully spelled out. The projector reservation is substantive because the earlier normalization argument assumes an additive Karoubian target. A useful next verification is to formulate the precise completion and idempotent-splitting requirement, then check its universal mapping property without resolving the frozen variance doubts by fiat.

### CL12 — A marginal variance correction qualifies the later operation formulas

**Current:** 136/317:25, “il s'agit bien des F contravariants à val. dans Ab lui-même (et non dans (Ab)^o …)”; 136/313:39–45, the earlier opposite-category interpretation. **Context:** A, R009 (058–064), sheaf/cosheaf variance; B, O12 (127–129); D, N42 (275), tensor-versus-Hom variance. **Relation:** adds an authorial correction, not a resolution of all surrounding formulas. **RESULTS_STATE:** no directly matching entry; the cited context items are first-pass reading questions.

The margin expressly corrects a confusion between contravariant invariants with values in `Ab` and a formal opposite-category interpretation used earlier. Any reconstruction of the operation categories must carry this distinction through the direction of morphisms, the use of limits versus colimits, and the classification of coefficient objects. The presence of this self-correction is evidence for a working draft, but does not by itself date the draft relative to the lecture.

### CL13 — Totalization signs are deferred rather than fixed by an implicit convention

**Current:** 136/309:33–34, “Il y aurait lieu de fixer une convention de degrés”; 136/310:4, “Je n'ai pas encore besoin urgent d'une telle convention”; 136/310:18–22, “commutent” and “Il faudra donc un signe à la diff. totale.” **Context:** B, N55–N66 (137–141), revised Stokes degree/sign calculations; C, R039 (229–231), chain-boundary and homotopy-label questions. **Relation:** adds an explicit convention warning relevant to the earlier calculations. **RESULTS_STATE:** no matching settled entry; `follow-ups @305` [open] would require a fully specified differential-compatible comparison.

The two differentials commute in the local convention, and the author explicitly reserves a sign for forming the total differential. A later comparison must specify total degree and the sign rule rather than importing an anticommuting bicomplex convention into the frozen formulas. This does not identify or repair any particular earlier Stokes sign without checking that calculation separately.

### CL14 — Finite cutoff localization is not the infinite shadow quotient

**Current:** 136/289:28–44, “suite de 4 foncteurs adjoints”; 136/291:7–20, the graded Hom formula and counit isomorphism; 136/293:6, “c'est précisément la sous-cat M^{N-1}.” **Context:** D, N17–N23 (244–256), adjoints and the distinct negligible classes; D, N39–N40 (273), derived reconstruction. **Relation:** restates and adds explicit all-graded formulas. **RESULTS_STATE:** `gap g1048` [open multiplication problem; g1031, g1041, g1034–g1035, g1080 reported settled in its summary].

The four adjoints and the kernel of the exact cutoff functor describe a localization at one fixed degree bound, with explicit formulas for the right adjoint. The earlier difficulties with unions of bounded-above objects and the repaired infinite quotient therefore do not refute this finite cutoff statement, but neither are they solved by it. The current passage sharpens the ambient-category distinction needed when using the earlier claimed finite-tail and derived results.

### CL15 — The extension to coefficients in an abelian category still requires representability

**Current:** 136/295:19–26, “Construire adjoint à droite” and the question-marked Hom identity, followed by “lorsque C ou C^o est une … cat. de Groth”; 136/297:11–24, the dual adjoint sequence. **Context:** D, N41–N42 (275), “Dans la mesure où ça existe” and variance of tensor/Hom; B, N48 (129), coefficient variation. **Relation:** adds a more explicit existence argument and assumptions. **RESULTS_STATE:** no matching settled entry; `GALOIS E.11` [Open return claim] is a broader coefficient-formalism question, not settled here.

The passage moves beyond ordinary module coefficients by making the right adjoint a representability problem, rather than claiming that `k`-linearity alone produces every needed tensor and Hom object. Its proposed Grothendieck-category alternatives and dualization should be checked with the exact smallness, completeness, and variance assumptions. This is a promising place to turn the earlier representability reservation into a precise theorem, but the question mark and partly uncertain formulas remain evidence of a draft.

### CL16 — Negative components make the ambient grading category consequential

**Current:** 136/299:21–26, `M_{S_h}=M\otimes_h h\{T\}` and `(\varphi_0M_{S_h})_{-d}`; 136/299:37–40, boxed `c_{i,\ell}\xi_{i+\ell}=c_{i-d,\ell}\xi_i`. **Context:** D, N22 (252, 275), explicit distinction between nonnegative and all-`Z`-graded units; D, N44–N45 (277–279), coefficient presentations and negative-degree questions. **Relation:** adds a direct all-graded negative-component calculation. **RESULTS_STATE:** `gap g1048` [open, with finite-tail results reported settled]; no row settles these exact negative-component formulas.

The current draft explicitly computes negative components of the right adjoint, so a theorem about the nonnegative graded category cannot be transferred unchanged to this ambient category. The displayed binomial relations give a concrete target for checking the earlier coefficient-presentation interpretation while leaving the uncertain exponents in the surrounding frozen text untouched. Over a rational coefficient field, the candidate `\xi_i=\binom{i}{d}^{-1}m` already supplies nonzero negative-degree tail maps, illustrating why an unrestricted all-graded unit needs separate treatment.

### CL17 — Shadows have a concrete comparison lead; their terminology is absent here

**Current:** 136/299:21, `M_{S_h}=M\otimes_h h\{T\}`; 136/287:25–26, the two cutoff subcategories; bounded search of all 45 frozen page files for `ombre` and `tubul`. **Context:** R:17–21 and 293–299, `MPL_121_001-048 Q1` and `MPL_152+120 Q1-06`; D, N19–N23 (252–256). **Relation:** adds a concrete formula; does not verify the terminology comparison. **RESULTS_STATE:** `MPL_121_001-048 Q1` [reading question/terminology]; `MPL_152+120 Q1-06` [recorded checked definition of module shadows; comparison unresolved].

Neither “ombre” nor “tubulure” appears in the supplied current frozen text, but `M⊗h{T}` and its tails provide a precise object to compare with the module shadows reported in R. The recorded checked-definition status belongs to the earlier Q1-06 entry, whose underlying source is not supplied in this dossier, and does not identify “tubulure” or establish that every use of “ombre” means this object. The next step is to obtain the exact defining scan cited by Q1-06 and compare its grading, morphisms, and extraction functor with 287–299.

### CL18 — No application to cote 137 is documented in this bounded range

**Current:** 136/301:5, “Constructions universelles”; 136/327:2–4, “X courbe alg. /C” and “à connexion intégrable”; bounded search of the 45 frozen page files for `137`. **Context:** R:20–21, 294 and 457, `MPL_133 B10` (133/009, 028–029), and `WG2 §2.4 #5`; B, N55–N58 refer to **scan 137 of cote 136**, not cote 137. **Relation:** differs from the hoped-for application; leaves the comparison open. **RESULTS_STATE:** `MPL_133 B10` [reading question; first-pass lead]; `WG2 §2.4 #5` [unchecked integrality thread].

The current universal-construction and curve passages supply no explicit reference or map to cote 137. In particular, the earlier notes' scan number 137 must not be turned into a cross-cote citation. The next useful evidence would be an actual statement from cote 137, packages 78 or 79 as identified by R, rather than a thematic inference from characteristic classes or integral connections.

### CL19 — The abelian-scheme occurrences belong to reused typescript

**Current:** 136/284:2–4, “IX” and “critère galoisien de réduction semi-stable”; 136/296:2–6, “IX,” “Définition de l'accouplement de monodromie,” and “A_K ait réduction semi-stable”; inventory sheet kind `reused_typed`. **Context:** A, R057 (055–073, 090, 092); B, §1.5 and R01–R35 (103, 107, 112–116, 124); C, R008 (189–234); D, N16 (236, 242, 262, 272, 280). **Relation:** restates the source-layer distinction with new current evidence. **RESULTS_STATE:** no result entry identifies an abelian-variety PD lecture example; README:21 is a question, not evidence.

Abelian schemes, Tate modules, semistable reduction, and monodromy occur on the reused Exposé IX leaves, which continue the donor-text pattern reported by all four earlier packages. Their occurrence establishes the subject of the reused paper, not that the handwritten PD exposition uses abelian varieties as examples. The current typescript pagination is discontinuous and partly reversed, which further prevents treating its order as the lecture's mathematical progression.

### CL20 — The handwritten class-like symbols qualify a blanket negative answer about examples

**Current:** 136/326:8–14, `\unsure{c_2^*}`, `\tfrac12\unsure{c_2^*}=c'_2`, `c_1`, and the `SL(2)`/`GP(1)` diagrams; bounded search for literal `Fourier` and `Chern`. **Context:** A, R057–R058 (084, 090), donor abéloïde and characteristic-class notice; B, §1.5; C, R008; D, N16. **Relation:** adds live geometric notation while differing from the proposed Fourier-transform example. **RESULTS_STATE:** `MPL_133 B10` [open reading comparison] is only a possible future link; no matching settled entry.

The current handwritten page contains `c_1` and doubtful `c_2` notation near group extensions and bundle-like expressions, so the absence of the literal word “Chern” is insufficient to conclude that characteristic classes are absent from the entire packet. Neither “Fourier” nor “Chern” is named in the frozen text, and no Fourier-transform Chern-class computation is stated. The prudent next step is to identify the classes, spaces, and maps in 326 from adjacent source pages before assigning this material a standard characteristic-class interpretation.

### CL21 — A genuine geometric investigation appears on the final live leaf

**Current:** 136/327:2–6, “X courbe alg. /C” and `g\geq2`; 136/327:18–25, the flat bundle and normalized universal-cover assertion; 136/327:91–95, “Trouver une connexion intégrable / (alg) canonique sur” the displayed projective bundle. **Context:** B, §1.5; C, R008; D, N16, negative findings about abelian/Fourier examples in earlier bounded ranges. **Relation:** adds a new live curve-and-connection problem; does not contradict their bounded negative findings. **RESULTS_STATE:** no directly matching entry; `MPL_133 B10` remains only an unresolved cross-cote comparison.

This leaf genuinely studies a complex curve of genus at least two, a torsor obtained from its universal cover, and a desired canonical algebraic integrable connection. The boxed infinitive “Trouver” marks the final connection construction as a task, even though a separate normalized-cover assertion is labelled “Th.” above it. The text does not identify the curve as an abelian variety, connect it to a Fourier transform, or prove that it is an application of the preceding integral PD construction.

### CL22 — The final PD diagrams translate natural operations into maps on a representing object

**Current:** 136/323:4–14, “La donnée d’un hom de foncteurs cov … équivaut à la donnée d’un élt” and “il suffit de voir le cas universel”; 136/320:48–70, `X=A, f=id_A`, the `u_p` diagrams, and `u_0=1`, `u_1=id`. **Context:** C, R006 (204, 215, 225–226), representability and free PD algebra; B, N37–N43 (123–127), dual coefficient data; D, N49 (281), distinctions among algebra, coalgebra, and polynomial universal problems. **Relation:** adds an explicit natural-operation/Yoneda reduction. **RESULTS_STATE:** `claims #243` [open corrected classification] is related only through the need for explicit PD multiplication identities; no classification proof follows here.

The drafts reduce natural transformations of represented functors to maps `u_p:A→Γ^p(A)` and test identities at the identity map or universal pair, providing a concrete continuation of the universal-constructions programme. The multiplication, composition, unit, and coproduct formulas must be distinguished because the maps are being compared in several algebraic structures. The literal `f^{(1)}=0` on 323 conflicts with the identity language on 320 and `f^{(1)}=f` on 325, so a mathematical reconstruction must flag the mismatch without rewriting the frozen line.

### CL23 — The Hom-PD and uniqueness questions are not supplied as finished theorems

**Current:** 136/324:2–10, “Deux questions de p.d. (la … première connue),” “Cet idéal a-t-il des p.d. ?,” and “Sont ils … les seuls”; 136/325:20–32, items 4–6 ending with unfinished conditions; 136/321:9–61, the cancelled draft block. **Context:** D, N41 and N45–N49 (275, 279–281), internal Hom, duality, and coalgebra qualifications; B, N29–N36 (119–121), a different uniqueness problem for generalized de Rham theories. **Relation:** adds new operation-level questions; differs from theory-level uniqueness. **RESULTS_STATE:** `gap g1004` [open generalized-theory uniqueness] is not settled by these questions; `claims #243` [open classification] remains separate.

The first question asks for a PD structure on a convolution-type Hom ideal, then asks whether its distinguished operations satisfy a composition identity and are uniquely characterized by the written relations. The parenthetical “première connue” does not erase the interrogative formulation or supply a proof in the arbitrary coefficient setting, and the following conditions remain unfinished. The cancelled naturality draft on 321 can illuminate the attempt but cannot be promoted into a retained theorem or merged with the separate uniqueness conjecture on 119–121.

### CL24 — The initial coalgebra sheets continue a tentative universal construction

**Current:** 136/283:60, `P_\infty=\bigcap P_i`; 136/283:74–75, intersection/tensor comparison; 136/283:95, the coalgebra-map interpretation; 136/285:9, “structure d’… algèbre sur V(s) ?” **Context:** D, N45–N49 (279–281), the negative annotation “NON,” the ordinary cofree-comodule calculation, and the completed/ordinary distinction. **Relation:** adds further coalgebra and equivariance diagrams; does not resolve the earlier annotation. **RESULTS_STATE:** no matching settled entry; `WG H6` [unchecked hunch] is only a broad schematic comparison.

The iteration through intersections and the coalgebra-map conditions suggest that the intended construction imposes more structure than a single equalizer of ordinary comodules. This makes the earlier distinction between a valid ordinary cofree-cotensor identity and the manuscript's unexplained “NON” worth preserving, rather than importing the former as a proof of all present diagrams. A promising check is to type every object and universal mapping problem, then test separately the claim that tensoring preserves the indicated infinite intersection.

## Local exposition map

This map records frozen order and explicit numbering, not a claim about delivery order or the full lecture.

| Current scans | Local labels | Content and evidential limit |
|---|---|---|
| 283, 285 | None establishing a lecture chapter | Coalgebra/coaction and equivariant universal-property diagrams; several question marks and intersection issues. |
| 287, 289, 291, 293 | Numbered definitions; Proposition 1 | Graded modules, translation, cutoffs, four adjoints, finite localization. |
| 295, 297, 299 | New coefficient discussion; coefficient relation | Extension to an abelian category, dual adjunctions, negative components and PD-binomial arithmetic. |
| 301 | Title sheet | First word remains `Notations|Notions`; second line is “Constructions universelles.” |
| 302–305 | Manuscript pages 1–4 | Simplicial/cosimplicial notation, universal simplex, Proposition 1 on extension from simplices. |
| 306–310 | Manuscript pages 5–9 | Homotopy-localization programme, Dold–Puppe, mixed indices, postponed totalization signs. |
| 311–314 | Manuscript pages 10–13 | Propositions 2–3, universal additive chains, extra structures, abelianization argument. |
| 315–318 | Manuscript pages 14–17 | Universal operations, restricted index-shape completions, variance correction, projector reservation, multiplicative caveat. |
| 320–325 | No continuation of the 1–17 labels shown | PD naturality and convolution questions; 321 cancelled; several unfinished equivalence conditions. |
| 326–327 | No continuation of the 1–17 labels shown | Group extensions, class-like symbols, bundles, curve uniformization, requested canonical algebraic connection. |
| 282, 284, 286, 288, 290, 296, 298, 300 | Exposé IX printed page numbers | Reused arithmetic geometry typescript; distinct source layer. |
| 292, 294 | “Problème MP 2” on 294 | Reused convergence-exercise typescript; not the title or programme of the PD lecture. |

## Cross-reference ledger and outstanding source checks

| Source | Relevant locations read or checked | Remaining verification |
|---|---|---|
| README | Entire file; especially 17–25, 33, 39–47 | Its lecture and example questions are explicitly planning guesses. |
| RESULTS_STATE | Entire 502-line file; orientation, open items 304–308, prior-package records 288–299, status details | No matching row is allowed to certify an unseen proof; later independent review remains separate. |
| A: 047–094 notes | Programme answers; R026–R047; R052, R054; R057–R059; title/source inventory | Inspect source 080–091 for the actual heading, embedding hypotheses, target `k{T}`, and negative opposite-topos annotation. |
| B: 095–141 notes | §§1.2–1.5, standing questions/title tables; N20–N28, N29–N36, N37–N48 leads; O12; targeted donor and sign searches | Inspect source 113 for the derived-sections diagram, 119–121 for uniqueness, 127–129 for the comparison of extension-from-simplices formulas. |
| C: 189–234 notes | R001–R013, particularly R005–R009; programme/title/example searches | Inspect 215 and 225–231 to compare the stated free PD property and normalization with 305 and 311–318. |
| D: 235–281 notes | N13–N23, N39–N49, programme/examples sections | Check the precise categories at 275–281 and whether the current all-graded right adjoint is the earlier nonnegative one or a different ambient construction. |
| Missing defined objects | Q1-06 module-shadow definition; underlying MPL_133 B10 sources; cote137 packages 78–79; PS §94 text | Obtain these sources before claiming a terminology identity, a cote137 application, or the content of the retrospective. |

## Reference forms for integration into the final notes

Grothendieck, A. (ca. 1975–1976 and later, catalogue dating). *Complexe de De Rham à puissance divisée* [Manuscript, cote 136, scans 282–327; frozen transcription supplied in this package]. The date on 302 and the catalogue date are separate kinds of evidence.

Supplied research context. (2026, November 12–17). *README; RESULTS_STATE; research notes for MPL_136_047-094, MPL_136_095-141, MPL_136_189-234, and MPL_136_235-281* [Unpublished contextual records; earlier research notes explicitly first pass and unreviewed].

The current donor text is locally marked Exposé IX; earlier notes identify its source as Grothendieck and Raynaud's *Modèles de Néron et monodromie* in SGA 7 I (1972). This dossier reports that bibliographical lead without an external collation and does not use it to attribute the live handwritten exposition.
