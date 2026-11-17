# Research contribution: modular maps, ring definitions, and five-point geometry

Prepared only after the root reader froze the transcription (17:10:31 UTC) and opened the context (17:10:36 UTC), 17 November 2026. No scan image was read by this researcher, and no transcription file was edited. Current-page evidence below is the frozen transcription; context transcriptions and earlier notes retain their supplied status, including the Esquisse's explicit “not yet checked by eye” warning. The manuscript reader should integrate or reject these proposed notes.

## Findings for the three requested questions

The answer to the first question is **yes for the specifically defined principal-congruence/Farey map**, namely the quotient of the modular triangulation by the image of Γ(n) in PSL₂(ℤ), supported by X(n) and its morphism to X(1); it is **not an identification established by the present 43 scans**. The context already makes the low-level identification in LM 140-2 scans 571–572, whereas these local pages turn to general trace invariant theory and a cube organizing four matrix variables. The ring question has a clear conceptual answer in Esquisse §4—an equivariant geometric realization of a regular cartographic object over a base ring, with a pinned universal reflection construction—but the supplied local leaves do not provide its full axioms. The five-point comparison concerns labelled moduli, its boundary incidence and A₅/S₅ symmetries, not a literal equality between M₀,₅ and the one-dimensional modular curve X(5).

## Proposed atomic notes

### MC01 — Scope of the local package

**File / scans:** 83 / 183, 190, 193–205, 207. **Kind:** reading question. **Quote:** “on veut expliciter sa structure multiplicative”; “Cas de quatre variables”.

The local goal is reconstruction and invariant theory for a rank-four Azumaya algebra, followed by four-variable trace data, and no local statement defines a level-n polyhedron or identifies it with X(n). The four-variable quotient is even described as dimension 13 on scan 193, so identifying this entire parameter space with M₀,₅ would contradict the stated dimension. **Context:** `README.md`, planning questions B5/B6; `LM_140-2_text.tex`, scans 571–574; `Esquisse_cote119_copy1_API_transcription.tex`, scan 119/8. **Bears on:** the package orientation in `RESULTS_STATE.md`; LM4 F.7; LM4_SUCCESSOR B.38–B.41; these pages do not settle those rows.

### MC02 — The conditional X(n) identification

**File / scans:** 83 / 183, 205, 207; contextual identification elsewhere. **Kind:** unpursued implication. **Quote:** “s correspond à un triple”; “f correspond à la permutation circulaire”.

If “level n” means the principal-congruence quotient of the modular triangular map, its supporting compact Riemann surface is X(n) and its quotient morphism is X(n)→X(1), with the three distinguished branch values normalized to 0,1,∞. This is the Farey-map construction, whose face/vertex valencies are 3 and n, rather than an inference from the cube's cyclic trace labels. **Context:** `LM_140-2_text.tex`, scans 570–572, table (75); Singerman–Strudwick, *The Farey maps modulo n*, §§1–6. **Bears on:** B5 in `README.md`; LM2 C.d1 and C.r1–C.r3 (unreviewed return claims).

### MC03 — A check at level five

**File / scans:** 83 / 205, 207; comparison with the planning question. **Kind:** own idea. **Quote:** “28 variables”; “32 relations !”.

For the principal-congruence map at n=5, the degree is 60 and the counts V=60/5=12, E=60/2=30, F=60/3=20 give the icosahedral triangulation. Confidence is high for this conditional comparison because it follows from the group order and the three cycle lengths, but it provides no reason to read the local cube as that icosahedron. **Context:** `LM_140-2_text.tex`, scans 571–572; Singerman–Strudwick, §6, index formula and Example 2. **Bears on:** LM4_SUCCESSOR B.38; no centralizer or profinite-kernel assertion follows from these finite counts.

### MC04 — Composite-level notation requires a convention

**File / scans:** 83 / 190–192, contextual comparison. **Kind:** own idea. **Quote:** “si 2 non inv. dans k”.

For a general integer n, write the deck quotient explicitly as SL₂(ℤ/nℤ)/⟨−I⟩ when defining the principal-congruence modular map: a notation “PSL₂(ℤ/nℤ)” that instead kills every determinant-one scalar can give a different quotient at composite level. Confidence is high because scalar units a with a²=1 need not all equal ±1 globally—for instance the four such units modulo 8 are 1,3,5,7. **Context:** `LM_140-3_text.tex`, scans 27–30, where primed central quotients are explicitly distinguished; `LM2_CONGRUENCE_ROWS.md`, LM2 C.r3. **Bears on:** LM2 C.d1/C.r3; this is a convention check, not a new result about GT.

### MC05 — B5 is an outer-action assertion, not the map identification

**File / scans:** 83 / 183–194. **Kind:** reading question. **Quote:** “invariantes par G”; “G=Aut(𝒜)”.

The automorphism group acting in these pages is the algebra automorphism group used for simultaneous matrix invariants, not the arithmetic or GT group of B5. `LM2_CONGRUENCE_ROWS.md` separates kernel preservation (C.d1), square-class outer images (C.r1), loss of a unique multiplier after passing to outer actions (C.r2), and genuine versus outer actions (C.r3); the README's short bridge should be read through those distinctions. **Context:** `LM_140-3_text.tex`, §39, scans 22–30, especially the square quotient on 23–24; `LM2_CONGRUENCE_ROWS.md`. **Bears on:** LM2 C.d1, C.r1–C.r3, all explicitly unreviewed in the supplied source; the present leaves add no proof or counterexample to them.

### MC06 — B5 must not be confused with the unresolved K₅ problem

**File / scans:** 83 / 183, 193–205. **Kind:** reading question. **Quote:** “structure multiplicative”; “espace quotient”.

The finite congruence quotient A₅ and preservation of its kernel under specified GT₀ actions do not establish the separate profinite centralizer/comparison assertion recorded as K₅=1. The current pages contain neither a geometric A₅ action on a punctured sphere nor a calculation of its profinite centralizer, so their Azumaya algebra calculations do not close that gap. **Context:** `RESULTS_STATE.md`, LM4 F.7 and LM4_SUCCESSOR B.38, B.39, B.41; `LM_140-2_text.tex`, scan 571 for the finite group comparison. **Bears on:** those open IDs; their status remains open here.

### MC07 — What “over a ring” means in the supplied Esquisse

**File / scans:** 83 / 183, 185, 192. **Kind:** unpursued implication. **Quote:** “sur k”; “l'anneau de base k”; “en car. 2”.

The local insistence on arbitrary base rings and characteristic two belongs naturally beside the Esquisse's projective geometric realization of vertices, edges, and faces over an arbitrary ring, rather than merely assigning coefficients to an abstract finite graph. The supplied Esquisse then singles out pinned objects: fundamental reflections act by universal formulas in n parameters, and the object is recovered by translating the pinned flag under the generated group. **Context:** `Esquisse_cote119_copy1_API_transcription.tex`, scans 119/21–23, especially 119/22–23; this context transcription is not eye-checked. **Bears on:** the ring-definition question in `README.md`; it supplies a compatible programme, not a definition proved on these local leaves.

### MC08 — A precise working definition, expressly ours

**File / scans:** 83 / 183, 205; not an authorial definition on these pages. **Kind:** own idea. **Quote:** “structure spéciale orthogonale”; “sommets adjacents”.

For a commutative ring R, one conservative definition of an R-realized regular 2-map is an abstract regular map with flag automorphism group G, a rank-4 projective R-module E with a homomorphism G→PGL(E)(R), and an injective G-equivariant realization of its vertices, edges, and faces as rank-1, rank-2, and rank-3 locally direct summands of E, such that incidence is exactly containment and every realized maximal flag comes from the map. With an initial flag identifying its flag set with G, geometric automorphisms act on the left, whereas flag adjacency acts on the right as g↦g sᵢ, with sᵢ²=1 and (s₀s₂)²=1; those two commuting actions must not be identified. Local direct-summand conditions survive base change, but distinct flags can coalesce, new containments can appear, and the represented group can acquire a kernel, so preserving this strict definition under specialization requires extra fiberwise hypotheses or a broader sheaf-based definition. Confidence is high that this is a precise strict model and only medium that it fits all the intended degenerations, and it is not presented as the author’s recovered definition. **Context:** Esquisse scans 119/22–25; `README.md`, ring-definition question; no register entry settles the equivalence.

### MC09 — The pinned universal-family version and its present limit

**File / scans:** 83 / 183, 192. **Kind:** reading question. **Quote:** “det,1 sans e ne suffisent”; “en car. 2”.

For the pinned subtheory, the Esquisse proposes defining objects over R by specialization ℤ[α₁,…,αₙ]→R of a universal reflection-and-flag construction, which is more specific than the general incidence definition above. Caleb Ji's primary research note gives an explicit two-parameter interpretation but acknowledges an unresolved cosine-versus-double-cosine normalization discrepancy, so that paper is useful constructional evidence rather than a certified identification of all the author's intended integral models. **Context:** Esquisse scan 119/23; Ji, *A note on regular polyhedra over finite fields*, §2 and its Remark (arXiv:2304.03345). **Bears on:** the ring-definition planning item; local orientation data and bad-characteristic restrictions are reasons to retain the ambiguity.

### MC10 — M₀,₅ is a surface, and the relevant link is geometric/combinatorial

**File / scans:** 83 / 193–205. **Kind:** reading question. **Quote:** “4+4+6=14”; “dim 4×4−3=13”.

After fixing three ordered marks at 0,1,∞, M₀,₅ is the two-dimensional open set with coordinates x,y satisfying xy(x−1)(y−1)(x−y)≠0, whereas X(5) is a curve and the local four-matrix quotient has the written dimension 13. The Esquisse's statement that five-point geometry is closely related to the icosahedron therefore asks for a correspondence of structures, not an isomorphism among these spaces. **Context:** Esquisse scan 119/8; Keel, introduction, pp. 545–546; `MPL_146_001-099_notes.md`, R097 (source cote146 scan074). **Bears on:** PUSH_ORDER5_FRAME Itemsfromt 2 / O.20 and EXIT_TOWER B.12/B.25; no frame or pentagon equation is supplied by the present cube.

### MC11 — The five-point boundary gives a testable incidence dictionary

**File / scans:** 83 / 199–205, comparison only. **Kind:** own idea. **Quote:** “diagonale”; “si δ(a)={i,j}”.

For five labels I, the boundary divisors of the stable compactification are labelled by the ten two-element subsets, and two meet exactly when their labels are disjoint, producing fifteen intersections and the Petersen incidence graph. This independently specified S₅-set is a better comparison target than matching a drawing by its apparent shape; confidence is high from the stable-partition rule, but the cube's four-index labelling has not been identified with it. **Context:** `MPL_147_048-137_notes.md`, N066-01–03 and N067-01, reporting cote147 scans066–067 (the underlying transcription is not supplied here); Keel, preliminary Facts 2 and 4, pp. 551–553. **Bears on:** EXIT_TOWER B.12/B.25 and the bi-icosahedron question; this is a comparison proposal, not a claim that 83 proves those results.

### MC12 — Full S₅ versus the oriented A₅ geometry

**File / scans:** 83 / 193–205. **Kind:** unpursued implication. **Quote:** “l'action du groupe … ⊂ S₄”.

The supplied notes on cote147 report that scans067–068 identify an oriented polyhedral picture through A₅ and explicitly ask for the full S₅ action in bi-icosahedral language; the boundary labels themselves already carry S₅. That unresolved realization problem differs from the present S₄ organization of four matrix variables, and no fifth label or five-point coherence is constructed here. **Context:** `MPL_147_048-137_notes.md`, N067-02 and N068-02 (source scans067–068); `MPL_146_001-099_notes.md`, R072, R075–R076 (source scans058,060,062,064,066). **Bears on:** PUSH_ORDER5_FRAME Itemsfromt 2 / O.20, LM4 F.7, LM4_SUCCESSOR B.39; these earlier notes remain leads.

### MC13 — Do not identify the three order-120 groups

**File / scans:** 83 / 183–194; contextual terminology question. **Kind:** reading question. **Quote:** “mod passage à l'inverse”.

LM 140-2 scan571 writes PGL₂(𝔽₅) beside “groupe du biicosaèdre”, and that projective group is S₅, whereas SL₂(𝔽₅) is a central double cover of A₅ and the ordinary full orthogonal icosahedral group is A₅×C₂. Hua, modernised reading of cote83, VI “Les groupes”, supplies a fourth relevant group, GL₂(𝔽₅)/{±I} of order240 acting on a complementary pair on twelve vertices, whose quotient by antipodality is precisely PGL₂(𝔽₅) of order120 (checked in MC16–17). The older context note `LM_140-2_notes.md` S2 correctly distinguishes the first three groups but its blanket “fails as written” verdict is unjustified without specifying whether the author means the full complementary pair or its antipodal quotient. **Context:** `LM_140-2_text.tex`, scan571; `LM_140-2_notes.md`, S2; `MPL_147_048-137_notes.md`, N068-02 (source147/068); Calegari, *The Artin conjecture for some S₅-extensions*, proof of Lemma3.1, for PGL₂(𝔽₅)≅S₅. **Bears on:** the README's bi-icosahedron question and LM4_SUCCESSOR B.39/B.41; the local pages do not decide the intended definition.

### MC14 — The two symbols Δ must not be conflated

**File / scans:** 83 / 185–192. **Kind:** reading question. **Quote:** “Δ=τ−τ′”.

Here Δ is a trace difference/orientation expression in a rank-four algebra, whereas the results register's Δ in LM7_PUSH E.65 and EXIT_TOWER E.49 is a continuous character of a profinite GT-type group. No map relating the two is constructed on these leaves, so sharing a symbol or a quadratic sign is not evidence that the manuscript tests E.49. **Context:** `RESULTS_STATE.md`, package orientation and the refereed-status paragraph; `LM2_CONGRUENCE_ROWS.md`, which concerns another specified family of outer actions. **Bears on:** LM7_PUSH E.65 (reported refereed) and EXIT_TOWER E.49 (explicitly unrefereed); neither status is changed.

### MC15 — What an actual bridge would have to construct

**File / scans:** 83 / 190–205, 207. **Kind:** own idea. **Quote:** “À vérifier”; “32 relations !”.

A credible bridge from these invariant coordinates to five-point geometry would need an explicitly defined locus in the four-matrix quotient, a map to the ordered or unordered five-point moduli problem, its behavior under S₄/S₅, and compatibility with the boundary and forgetful maps. Confidence is medium that such a comparison is worth testing, because both programmes organize group actions by finite incidence data; the large dimension difference and the still-unverified local presentation prevent an identification at present. **Context:** `MPL_147_003-047_notes.md`, N075 (source147/003,035–047), on boundary compatibility; `RESULTS_STATE.md`, EXIT_TOWER E.35 and B.12/B.25. **Bears on:** those IDs and PUSH_ORDER5_FRAME O.20; this is a proposed research obligation, not a novelty or existence claim.

### MC16 — Hua’s twelve-vertex model passes an exact finite check

**File / scans:** 83 / 193–205, comparison with earlier contextual leaves; no claim that these local pages contain the construction. **Kind:** own verification of a context finding. **Local quote:** “quatre variables”. **Context:** Hua, modernised reading of cote83, VI “Orientations (pages52 à55)” and “Les groupes (pages55 à59)”, especially its explanatory footnote on p58. **Bears on:** the README bi-icosahedron question; no reviewed register row proves this finite model.

Credit for this model belongs to Hua’s project: take the twelve classes of nonzero vectors in 𝔽₅² modulo ±1, join classes when their determinant is ±1 for the first graph and ±2 for the second, and use multiplication by2 for antipodality. An exact finite enumeration gives each graph 30 edges and20 triangular faces, five-cycle vertex links, and120 automorphisms; the automorphisms preserving or globally exchanging the two graphs form the240 distinct permutations induced by GL₂(𝔽₅)/{±I}. Confidence is high for this finite calculation, recorded in `scripts/check_biicosahedron.py` and `records/biicosahedron_check.json`, but it verifies the supplied contextual interpretation rather than the handwriting of the earlier leaves.

### MC17 — The order-120 quotient has a concrete role

**File / scans:** 83 / 183, 193–205, contextual comparison only. **Kind:** own verification of a context finding. **Local quote:** “mod passage à l’inverse”. **Context:** Hua, modernised reading of cote83, VI “Les groupes (pages55 à59)”; `LM_140-2_text.tex`, scan571; `LM_140-2_notes.md`, S2. **Bears on:** the README bi-icosahedron question; LM4_SUCCESSOR B.39/B.41 remain separate open problems.

In Hua’s twelve-vertex model the scalar2 has order2 after quotienting by ±I, is central and fixed-point-free, and its six orbits are the points of P¹(𝔽₅), so quotienting the240-element group by this antipodality yields PGL₂(𝔽₅)≅S₅ of order120. The determinant map instead has kernel PSL₂(𝔽₅)≅A₅ of order60 and quotient 𝔽₅×≅C₄, while its determinant-±1 subgroup of order120 is A₅×C₂ and preserves the two graphs separately. Confidence is high from the explicit action and group kernels, and these distinct quotients explain why the LM bi-icosahedron terminology should be resolved against its intended object instead of dismissed by comparing only binary and ordinary full icosahedral groups.

## Primary web sources inspected

These sources are for the research notes only, never for changing the transcription. URLs are recorded so the root reader can reopen them before citing. No long passage is reproduced above.

1. David Singerman and James Strudwick, “The Farey maps modulo n”, *Acta Mathematica Universitatis Comenianae* 89(1) (2020), 39–52, especially §§1–6 and Example2. [Publisher PDF](https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/download/913/785). Web refs `turn745263684view0`, `turn835024716view2` (same source). The publisher landing page is dated 21 October2019, while the printed issue says2020.
2. Caleb Ji, “A note on regular polyhedra over finite fields”, arXiv:2304.03345v1 (2023), §2 and its normalization Remark. [Author paper](https://arxiv.org/pdf/2304.03345). Web refs `turn924142993view0`, `turn835024716view3` (same source). The abstract and introduction expressly call this one interpretation of the programme.
3. Sean Keel, “Intersection theory of moduli space of stable n-pointed curves of genus zero”, *Transactions of the AMS*330(2) (1992),545–574; introduction and preliminary Facts2/4, pp551–553. [Paper PDF hosted by Colorado State](https://www.math.colostate.edu/~renzo/teaching/Topics10/keel.pdf). Web refs `turn453810938view0`, `turn835024716view1` (same source). The paper is over an algebraically closed field of arbitrary characteristic; it is not being cited here as an unexamined integral proof over ℤ.
4. Frank Calegari, “The Artin conjecture for some S₅-extensions”, *Mathematische Annalen*, DOI10.1007/s00208-012-0839-4; proof of Lemma3.1 explicitly invokes PGL₂(𝔽₅)≅S₅. [Author PDF](https://www.math.uchicago.edu/~fcale/papers/S5.pdf). Web refs `turn835024716view0`, `turn970036929view0`.

## Search coverage and limits

Searched all four `LM_140-*_text.tex` files and supplied package notes for polyhedron/icosahedron/bi-icosahedron, congruence, level, five-point, pentagon, and relevant group notation; read the decisive ranges in LM140-2 scans570–575, LM140-3 scans22–30, Esquisse119/8 and119/21–27, and the returned-note items cited above. The supplied context has no text file for cote147: its manuscript quotations and scan descriptions are therefore cited through the supplied notes, not presented as independently inspected manuscript evidence. No relation or full-polyhedron definition was invented to fill the absence in local scans178–222.
