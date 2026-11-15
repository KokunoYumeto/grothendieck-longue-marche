# Research notes on cote 134-8, scans 043–087

## Scope, witnesses, and status language

These notes concern the 44 supplied scans of cote 134-8, with scan 060 omitted by the supplier as blank. The diplomatic transcription was completed and audited against the images before the context contents were opened: the 44 page files and their exact concatenation were frozen at **2026-11-15 11:49:57 UTC**, and context extraction began at **11:50:22 UTC**. An earlier intake had listed the context archive's filenames and sizes, but had not read its file contents; that limited access is disclosed in the work records. All reading questions raised after the freeze belong here, and the frozen text remains the evidence for what was read.

References to a scan mean the scan number in `134-8.pdf`, not a page number in the typescript or an inferred date. Approximate line locations below refer to the corresponding file in `pages/`; visible manuscript page numbers are separately catalogued. References such as PS VII §134, p.559 identify the supplied `ps_chapters_VI_VII/ps7.tex` and its `\pspage` marker; DER references identify the supplied companion's chapter, manuscript page, and, where available, printed page. Brief quotations preserve the frozen reading, including uncertainty where it affects the comparison.

The context's `notes/RESULTS_STATE.md`, `NEW_RESULTS.md`, and `DOSSIER_STATEMENTS_WITH_STATUS.md` are registers of research-return claims. A status such as Proved, Refuted, Known, or Open is attributed to that register; a review label is reported only where the register supplies one. No entry acquires an independently verified mathematical status merely through its inclusion in these notes. “No form located” is a bounded textual finding about these 44 scans and the specified searches, and makes no assertion that the mathematical subjects lack a relationship.

## Main register: linearization, intervals, and resolutions

### R001 — 134-8, scans 043–044, diagram blocks; unpursued implication

The opening leaves contain diagrammatic work without a surrounding proposition that fixes all the objects and hypotheses. Their fraction, cylinder, and comparison diagrams should be collated with the later localization argument, without supplying an unlabelled adjunction or a theorem statement from context. Compare PS VII §134, pp.557–560, where the localized comparison is explicitly proposed, and the later, more legible formulations on scans 047–055; RESULTS_STATE GALOIS G.6 and RESIDUE I.7 remain the relevant open coefficient-framework leads, without a solution on these two leaves.

### R002 — 134-8, scan 045, interval calculation; reading question

The leaf writes `(x,y)\longmapsto(x+y,\lambda(y))` and then `(x,-x)\longmapsto(0,\lambda(x))`. Direct substitution into the first displayed rule gives `(x+(-x),\lambda(-x))=(0,\lambda(-x))`, so the two displayed second components require a sign or convention check that the leaf does not spell out. The frozen formulas are retained; compare the interval/contractor problem in PS VII §134, pp.559–560, and the endpoint calculations on scans 081 and 084, with RESULTS_STATE GALOIS G.6 as a methodological lead only.

### R003 — 134-8, scan 045, `Add(\Delta_1)` and the hypotheses on `J`; unproved claim

The construction links an additive interval to the objects `J` and `J^+`, while the surrounding finite/free hypotheses are revised on the page. A reconstruction must keep track of the actual maps from the two endpoints and the augmentation before using the construction in the localization argument. PS VII §134, p.560 asks for an interval with suitable extra structure, and scan 081 later supplies an augmented-algebra formulation; RESULTS_STATE GALOIS G.6 does not certify this particular construction.

### R004 — 134-8, scan 046, acyclicity assumptions; unproved claim

The page distinguishes `L_i\varphi(\mathbb Z_{\mathcal M})=0` for positive degrees from the requirement on `J^+\otimes x` in **all** degrees, including the circled degree-zero case. Scan 053 makes the latter emphasis explicit in words, “on le veut pour i=0 aussi,” and scan 055 rewrites the assumptions again. This is a concrete addition to PS VII §134's contractor question, and bears on the exact-colimit questions RESULTS_STATE TOTASPH D.7 and RESIDUE F.5 only through the written derived-vanishing formulas; no implication from categorical total asphericity to exactness is supplied here.

### R005 — 134-8, scan 046, deleted `J^+` choice; withdrawn in the same text

The page strikes the suggestion “On peut prendre `J_{\mathcal M}^+=\mathbb Z_{\mathcal M}`” and changes the projectivity wording to a `\unsure{résolution}` “avec augmentation!!”. Both states must remain visible in the genealogy of assumptions, alongside the positive/all-degree distinction in R004. Compare scans 048 and 050 for the later flatness/projectivity checks and PS VII §139, pp.587–590 for the typescript's account of which argument must actually be resolved; no corresponding RESULTS_STATE entry settles this local replacement.

### R006 — 134-8, scan 047, `\kappa,\varphi` and “condition d'asphéricité”; unproved claim

The written comparison `l\xleftarrow{\sim}\varphi\kappa(l)\simeq L\varphi\kappa(l)` locates the proposed asphericity condition in the adjunction between the coefficient category and `\mathcal M`. Compare PS VII §134, equations (1)–(3), pp.557–558, which display the concrete constant-coefficient pair `p_!\dashv p^*`; scan 055 later supplies the written degree-zero comparison `\lambda^*(U)\simeq\kappa(U)` for the chain-model adjunction. RESULTS_STATE RESIDUE I.7 and GALOIS G.6 are relevant open framework questions; the leaf supplies this comparison, not the full coherence and reconstruction requested there.

### R007 — 134-8, scan 047, lower proof sketch; unproved claim

The page introduces an acyclic subcategory by vanishing of positive `L_i\varphi` and starts an argument involving enough projectives, exactness of `\kappa`, and an unfinished `\operatorname{Hom}` expression. The missing end of that expression prevents treating the page as a completed proof of the following localization statement. Compare scans 049 and 054, PS VII §134, pp.558–560, and RESULTS_STATE GALOIS G.6/RESIDUE I.7; the local addition is the proposed route through projective resolutions.

### R008 — 134-8, scan 048, “Hypothèse-clef”; unproved claim

The “Hypothèse-clef” requires a map from the unit to `J` that remains monic after tensoring with every `x`, together with vanishing of the derived homology of `J\otimes x`. The accompanying `k`-bilinearity, exactness/limit, enough-projectives, and unit-acyclicity assumptions belong to the statement and cannot be discarded in reading scan 049's “Thm(?)”. PS VII §134, pp.559–560 asks the interval question in less explicit form; the connection to RESULTS_STATE TOTASPH D.7/RESIDUE F.5 is the displayed universal tensor condition, whose passage to a category-level total-asphericity hypothesis is not provided.

### R009 — 134-8, scan 048, marginal projectivity question; self-flagged

“Qu'en est-il …” asks about the projectivity of the free objects indicated by `\mathbb Z^{(I)}` while nearby “projectif” is replaced by “plat”. Scan 050 asks the corresponding tensor-resolution question explicitly, so these leaves document a qualification of the proposed proof rather than an unmarked use of projectivity. The comparison passage is PS VII §138, pp.584–586, which traces preservation of projectives through discrete cofibering functors; RESULTS_STATE's open linear-coefficient items GALOIS G.6 and RESIDUE I.7 remain unsolved by the marginal question.

### R010 — 134-8, scan 049, “Thm(?)”; self-flagged

The leaf labels the proposed equivalence `W_{\mathcal M}^{-1}\mathcal M\longrightarrow\mathrm D_\bullet(Ab_k)` “Thm(?)” under its listed assumptions a–d. Its closest typescript counterpart is the suspected equivalence in PS VII §134, equation (8), p.559, so the handwriting adds a tentative hypothesis list and a route to a proof. The question mark remains part of the evidential status; RESULTS_STATE GALOIS G.6 and RESIDUE I.7 record broader open coefficient questions and do not turn this proposal into a verified theorem.

### R011 — 134-8, scan 049, corollary and adjoint pair; unproved claim

The corollary introduces a resolving functor `\Lambda=\lambda_!` and its right adjoint `\lambda^*`, and asserts compatibility of the weak-equivalence classes and quasi-inverse localized functors. The following leaves examine precisely the counit and projectivity steps this assertion uses, especially scans 050–055. Compare PS VII §134, pp.558–560 and §135, pp.560–564; RESULTS_STATE GALOIS G.6/RESIDUE I.7 supply the open framework context, while the proof obligations here are the explicit adjunction, descent, and counit comparisons.

### R012 — 134-8, scan 049, `F_{/x}\longrightarrow F_{/y}` sketch; unpursued implication

The lower sketch uses the slice comparison `F_{/x}\longrightarrow F_{/y}` in a homological argument, without stating a general relative Theorem A in a complete general form. That exact map is the bridge for comparison with RESULTS_STATE GALOIS B.1, B.3 and D.2, whose claimed absolute, relative, and coefficient refinements are separately registered. This leaf should therefore be collated with those formulas, without identifying its abbreviated sketch with their complete statements.

### R013 — 134-8, scan 050, margin beside `L\varphi^J`; self-flagged

The question “ceux-ci sont-ils projectifs ?” concerns the terms `J\otimes L_i^a` in the proposed resolution of `J\otimes a`. The displayed comparison between `L\varphi(J\otimes a)` and the expression obtained by tensoring a resolution gives the exact place at which preservation of projectives, or a proved acyclicity substitute, must be checked. Compare PS VII §138, pp.584–586 and §139, pp.588–589; RESULTS_STATE RESIDUE F.5 and TOTASPH D.7 remain open exactness leads and provide no missing projectivity proof here.

### R014 — 134-8, scan 050, rotated counit diagram; self-flagged

The two rows `\lambda_!\lambda^*(l_\bullet)\longrightarrow l_\bullet\longrightarrow 0` and its primed analogue carry “?” on the final arrows. These must be read with scan 051's “qu. iso ?” and scan 053's proposed equivalent conditions, not as already verified exact rows. The corresponding typescript problem is PS VII §134, equation (8), and the related open register entries are GALOIS G.6 and RESIDUE I.7.

### R015 — 134-8, scan 050, rotated slice diagrams; unpursued implication

The marginal data `(a,f,y,u)` and `u:y\longrightarrow x` spell out an objectwise comparison involving `A_{/a}`, `X`, and a slice over a selected object. Those data add a concrete route for examining the fiber calculations behind the neighboring localization sketch. Compare PS VII §135, pp.561–564, §138, pp.583–585, and the status claims GALOIS B.1/B.3/D.2 in RESULTS_STATE; preserving the displayed variance and comma-object choices is necessary before matching the formulas.

### R016 — 134-8, scan 051, exactness annotations; unproved claim

The margin asserts that `\lambda_!` and `\lambda^*` are exact, expressing the latter through `x\mapsto\operatorname{Hom}(\lambda(x),L_\bullet)`. The upper condition on `\lambda(x)` is therefore substantive, and scan 054 later rewrites the assumptions as preservation of monomorphisms and epimorphisms. Compare PS VII §139, pp.589–590, which returns to enough-projective/injective hypotheses for functor categories; the open RESULTS_STATE GALOIS G.6/RESIDUE I.7 questions require more than this asserted exactness.

### R017 — 134-8, scan 051, counit margin; self-flagged

The arrow from `\lambda_!\lambda^*(l_\bullet)` to `l_\bullet` is accompanied by the uncertain frozen reading “qu. iso ?”. Scan 053 subsequently isolates that same counit as one of the proposed equivalent conditions, and scan 055 attacks it first in degree zero and then for acyclic projective complexes. The primary comparison is PS VII §134, equation (8), with GALOIS G.6/RESIDUE I.7 retained as open context rather than a validation of this step.

### R018 — 134-8, scan 051, tensor comparison; withdrawn in the same text

Beside `F\otimes\xi\longrightarrow F\otimes\eta`, the word “quiso” is deleted and “équiv. faible (abélienne)” is written. The lower diagram `0\mathbin{-}x\to J\otimes x\to x[1]\mathbin{-}0` supplies the actual tensor/shift mechanism under discussion, so the replacement of the label must be preserved when comparing weak classes. Compare PS VII §134's definition of `W_A^{ab}` and RESULTS_STATE GALOIS D.2's claimed coefficient refinement; no equality of all these weak classes is established by the replacement alone.

### R019 — 134-8, scan 052, splitting calculations; unproved claim

The leaf develops `L_i\simeq B_i\oplus H_i\oplus B_{i-1}` and a product of Hom groups to analyze maps into a complex with projective terms, vanishing positive homology, and projective degree-zero homology. Several expressions stop in mid-construction, including `\operatorname{Hom}(` and a later `L_i\simeq`, so the calculation is evidence for an intended lifting argument rather than a complete conclusion. It bears directly on scans 051 and 053–055 and PS VII §139's resolution discussion; no specific RESULTS_STATE theorem is identified with this unfinished calculation.

### R020 — 134-8, scan 052, additive category `\Theta`; unpursued implication

The displayed `\mathrm{Ch}_\bullet(\mathcal M)\simeq\underline{\operatorname{Hom}}_k(\Theta,\mathcal M)` is accompanied by generating differential and identity morphisms in `\Theta`. This provides a concrete presentation to inspect when reconstructing the adjunction used in the nearby proof attempt, including the written direction of its arrows. Compare the `k`-linear enlargement proposed in PS VII §139, pp.590–591 and the open framework entries GALOIS G.6/RESIDUE I.7; the page does not spell out the relations and coherence needed for the broader construction.

### R021 — 134-8, scan 053, upper margin; self-flagged

The margin asks whether existence of `\overline{\lambda^*}` already makes `\overline\lambda_!` and the written `\overline\lambda_*` “adjoints l'un de l'autre ??”, independently of the preceding assumptions. The star/subscript variation is retained as a reading question, while the double question mark makes the descent-of-adjunction step explicitly unverified. Compare PS VII §134, equations (7)–(8) and the related open GALOIS G.6/RESIDUE I.7 entries; neither context passage supplies a proof of this exact marginal assertion.

### R022 — 134-8, scan 053, “Conditions équivalentes”; unproved claim

The page lists localized quasi-inverseness, a quasi-isomorphic counit, and progressively restricted tests on projective or acyclic complexes as “Conditions équivalentes”. These are the concrete tests that the earlier “Thm(?)” would have to connect, and the repeated numbering and uncertain labels are retained in the frozen text. Compare scans 054–055 for the argument being assembled, PS VII §134, p.559, and RESULTS_STATE GALOIS G.6/RESIDUE I.7; the enumeration itself is not a proof of every equivalence.

### R023 — 134-8, scan 053, “Lemme 3”; unproved claim

“Lemme 3” combines a `k`-bilinear tensor structure, the adjunction to `H\mapsto H\otimes_k1_{\mathcal M}`, positive-degree unit acyclicity, and a universally monic unit-to-`J` map with `L\varphi(J\otimes x)=0`. The margin insists “on le veut pour i=0 aussi,” so replacing this by positive-degree acyclicity would change the stated assumption. Compare scans 046, 048 and 055, PS VII §134's interval question, and the open exactness questions TOTASPH D.7/RESIDUE F.5 through these explicit tensor-derived formulas.

### R024 — 134-8, scan 054, rewriting before “Lemme 1”; withdrawn in the same text

The page cancels an initial hypothesis package and inserts that `\lambda_!` takes monomorphisms to monomorphisms and `\lambda^*` takes epimorphisms to epimorphisms, followed by the bracketed projective-preservation consequence. This local revision belongs with the projectivity questions on scans 048 and 050 and the exactness assertions on scan 051. Compare PS VII §138, pp.584–586 for a specific geometric mechanism ensuring preservation of projectives; the context's GALOIS G.6/RESIDUE I.7 status entries do not remove the leaf's stated hypotheses.

### R025 — 134-8, scan 054, “Lemme 1” and its proof; unpursued implication

“Lemme 1” gives a bicomplex argument for identifying `c\Lambda_\bullet(x)` with `(L\varphi)(x)` using a projective resolution `P_\bullet^x\to x` and exactness in the other direction. The written “Dém.” gives the two resolution arguments for the displayed quasi-isomorphisms in the nonnegative complex setting used on these leaves; its concrete proof is useful for assessing which subsequent counit tests still remain open. Compare PS VII §135, pp.560–564 and §139, pp.587–590; its concrete bicomplex method is relevant to GALOIS G.6/RESIDUE I.7 without resolving those open frameworks.

### R026 — 134-8, scan 054, “Lemme 2”; unproved claim

The end of the leaf defines `W_{\mathcal M}=\Lambda_\bullet^{-1}(W_{\mathrm{Ch}_\bullet(A)})` after asserting exactness, projective preservation, and `c\circ\lambda_!\simeq L\varphi`. The final “Alors conditions équivalentes” is deleted, and scan 053 carries the corresponding list in the supplied scan order. This is a visible drafting relationship, not a date claim; compare PS VII §134's definition of the abelian weak class and the open GALOIS G.6/RESIDUE I.7 entries.

### R027 — 134-8, scan 055, reformulated assumptions; withdrawn in the same text

The assumptions are rewritten around “fortement plat,” specified by preservation of monomorphisms and products by `\kappa`, and around a resolving `\lambda_!` with a right adjoint. The deleted assertion that the unit is projective should be compared with the live flatness of the terms `\lambda_{!i}(1_{\mathcal M})` and the separately stated augmentation isomorphism. PS VII §138, p.586 explicitly ties existence of a left adjoint to exactness and products and then to finite projectivity in its ringed setting; this is a precise comparison for RESULTS_STATE's open linear-coefficient entries, not a transfer of that ringed conclusion to every `\mathcal M` on the leaf.

### R028 — 134-8, scan 055, degree-zero coefficient argument; unproved claim

The written chain `\operatorname{Hom}_{\mathcal M}(x,\kappa(U))\simeq\operatorname{Hom}_k(\varphi(x),U)\simeq\operatorname{Hom}_{\mathrm{Ch}}(\lambda_!(x),U)` is used to claim `\lambda^*(U)\simeq\kappa(U)`. The subsequent tensor expression for `\lambda_!\lambda^*(U)` is the concrete degree-zero step toward scan 053's counit test, and its terminal arrow is underlined “iso” in the source. Compare PS VII §134, equation (8), and GALOIS G.6/RESIDUE I.7; a reconstruction must retain the degree-zero placement of `U` and verify the displayed naturality rather than infer a statement about every complex.

### R029 — 134-8, scan 055, final “A prouver”; self-flagged

After “OK”, the page turns to a projective acyclic `l_\bullet`, says it is homotopic to zero, and explicitly leaves “A prouver que `\lambda_!\lambda^*(l_\bullet)` aussi.” This is the unfinished second test in the counit argument, continued through the interval sketches on scans 056–059. The comparison remains PS VII §134's localized equivalence question and the open GALOIS G.6/RESIDUE I.7 leads.

### R030 — 134-8, scan 056, margin “asphérique ?”; self-flagged

The proposed counit `\lambda_!\lambda^*(l_\bullet)\to l_\bullet` receives the inserted question “asphérique ?”, followed by tentative conditions including an epimorphism with quasi-null kernel and preservation of quasi-isomorphisms. The unfinished `iv_1,iv_2` and partial `\lambda^*(` indicate that this list remains a working outline. Compare scans 053 and 055, PS VII §134, p.559, and GALOIS G.6/RESIDUE I.7; none of the fragments supplies a complete verification of the question-marked step.

### R031 — 134-8, scan 057, isolated symbols and cancelled Hom expression; unpursued implication

The surviving `\unsure{A_\bullet(x)|\Lambda_\bullet(x)}` and cancelled Hom expression sit beside two detached vertical arrows without a written conclusion. Their nearest textual continuation is the `\lambda^*`/interval work on scans 056 and 058, and PS VII §134 provides the surrounding localized-abelianization question. No complete proposition is extracted from this sparse leaf, and no RESULTS_STATE item is treated as settled by it.

### R032 — 134-8, scan 058, acyclic interval conditions; unproved claim

The leaf compares acyclicity of `\lambda^*(l_\bullet)\otimes x`, null-homotopic coefficient complexes, and an inclusion `1_M\xrightarrow\alpha J` whose tensor products are monic and acyclic. Its kernel formula `\unsure{\widetilde W_h^P(I)}\otimes F=\operatorname{Ker}(F^{(I)}\longrightarrow F)` is the written comparison with the presheaf interval `I`; the uncertain left-hand notation remains part of that comparison. Compare PS VII §134, pp.559–560; this bears on RESULTS_STATE TOTASPH D.7/RESIDUE F.5 through a coefficient construction, with the page's actual hypotheses retained.

### R033 — 134-8, scan 058, “J est tot asph.”; unproved claim

The phrase “i.e. `J` est tot asph.” follows a lemma comparing acyclicity of `J\otimes x` for all objects with the test on projective objects, under the stated tensor-flatness assumption. The written comparison is therefore the evidence to use when collating this occurrence with total asphericity in DER II and XII: it supplies neither the sentence “totalement asphérique ⇒ filtrant” nor strong W(7)'s cube comparing two cover squares. RESULTS_STATE TOTASPH C.10 and NEW_RESULTS #11 record the reviewed counterexample claim to the former conjecture; RESULTS_STATE TOTASPH A.9 and the TOTASPH A.13 review reported in NEW_RESULTS #8 concern the latter, and their complete mappings appear below.

### R034 — 134-8, scan 058, unfinished corollary; self-flagged

“Corollaire Car si c'est vrai” stops without a completed corollary, below the proposed reduction to projective `x`. This is an explicit unfinished argument even though it carries no separate question mark. Compare scans 050 and 053–055 for its projectivity and tensor-acyclicity prerequisites, PS VII §134's contractor question, and the still-open TOTASPH D.7/RESIDUE F.5 exactness entries.

### R035 — 134-8, scan 059, arrow `J\to\lambda^*(\widetilde\Theta)`; self-flagged

The arrow after `1_M\hookrightarrow J` is marked “?” and is followed by the adjoint-side expression `\lambda_!(J)\to\widetilde\Theta`. These are the explicit maps to investigate in relating the page's abstract interval to a chain-complex interval; the lower tensor/`\lambda^*` comparison is also only sketched. Compare PS VII §134, p.560, scans 061–063 and 081–086, and GALOIS G.6/RESIDUE I.7 as open framework leads.

### R036 — 134-8, scan 061, tensor/Hom and cycle formulas; unproved claim

The upper diagram maps `Hom(X,P)\otimes_k Hom(Y,Q)` into `Hom(X\boxtimes Y,P\boxtimes Q)` and the page writes `Z_n(P)\otimes Z_m(Q)\simeq Z_{n,m}(P\boxtimes Q)`. The later tests using `k` and the shifted `\Theta[n]` record how the comparison is being checked on elementary complexes, without an accompanying general proof of the displayed isomorphism. Compare PS VII §139, pp.587–590, where internal tensor/Hom computations still require resolutions, and RESULTS_STATE GALOIS G.6/RESIDUE I.7 for the open coefficient-framework task.

### R037 — 134-8, scan 061, `ch`, `Ch` and completions; reading question

The lower half distinguishes written lower-case `ch` from `Ch` and uses uncertain raised signs in formulas ending in `\mathrm{Ch}_\bullet(A)`, together with the phrase “complexes de chaînes dans A qui sont homotopes à un complexe constant”. PS VII §139, pp.590–591 supplies a reason to compare these with his proposed linearized categorical constructions, but does not identify every angular mark on this leaf. The uncertainty remains in the transcription; GALOIS G.6/RESIDUE I.7 are relevant framework leads and provide no paleographic resolution.

### R038 — 134-8, scan 062, mapping-cone and interval diagrams; unpursued implication

“Mapping cone sur `l_\bullet`” labels the tensor factor in `\lambda^*(l_\bullet\otimes\Theta)`, and the adjacent expression `\lambda^*(l_\bullet)\otimes\lambda^*(\Theta)` displays the comparison required for the null-homotopy argument. The diagrams therefore give a concrete continuation of scan 055's “A prouver”, while the braces and shifted `k,\Theta` sequence retain information about the intended elementary complexes. Compare PS VII §134, p.560 and §139's internal-operation discussion, with GALOIS G.6/RESIDUE I.7 as open context.

### R039 — 134-8, scan 063, diagonal comparison; unproved claim

The square with `\delta_M^*`, `\delta_{\mathrm{ch}_\bullet}^*` and `(\lambda\boxtimes\lambda)^*` is followed by a second diagram whose two outer composites are labelled `id`. These diagrams make the proposed tensor compatibility more explicit than PS VII §134's interval question and can be compared with the linearized-object and coalgebra program in PS VII §139, pp.590–591. A proof still has to construct the displayed transformations with their stated variance and justify the identifications; RESULTS_STATE GALOIS G.6/RESIDUE I.7 do not settle that task.

### R040 — 134-8, scan 064, copying instructions; unpursued implication

“Recommandations pour la … xérographie de ``Modelizing Story'', pages 259 à 381” requests three copies, an additional copy of p.275, and “trois pages de table des matières”. Its warning that pp.274–275 were typed recto-verso provides a concrete collation instruction for any recovery of that batch, while the August return request supplies no written year. Compare the titles in `PURSUING_STACKS_CONTENTS.md` and the context README's catalogue description; this is a provenance witness, with no RESULTS_STATE mathematical item assigned.

### R041 — 134-8, scan 065, proposed `ch\to ch_{\bullet\bullet}`; self-flagged

The arrow from `\mathrm{ch}_\bullet(Ab)` to `\mathrm{ch}_{\bullet\bullet}(Ab)` is followed by “??”, and the Hom-adjunction formula separately asks whether `\delta(L_\bullet)` lies in the indicated small bicomplex category. These are two distinct checks on existence and target membership of the proposed diagonal construction. Compare scan 063 and PS VII §139, pp.590–591; the exact maps, rather than a general resemblance of vocabulary, make these leaves useful for the open GALOIS G.6/RESIDUE I.7 coefficient-framework questions.

### R042 — 134-8, scan 065, tensor comparison labels; self-flagged

The `\lambda^*` tensor comparison is labelled `W_M ?`, and the final triangular comparison has a separate “qu.iso ?” beside an arrow and “EZ” on another. The leaf does not write a proof identifying both arrows with established comparison maps, so “EZ” remains a source label and a possible Eilenberg–Zilber lead, not a certification. Compare PS VII §134, pp.559–560 and §139, pp.587–590; GALOIS G.6/RESIDUE I.7 remain open, and a reconstruction must verify each displayed morphism.

### R043 — 134-8, scan 065, changed weak-equivalence wording; withdrawn in the same text

For `\lambda_!(a\otimes y)\to\lambda_!(a)\otimes\lambda_!(y)`, “asph” is struck and “qu.iso” inserted; for the `\lambda^*` comparison the “qu.iso” label is struck while `W_M ?` remains. These local revisions should be collated with scan 051's change from “quiso” to “équiv. faible (abélienne)”, without reversing either change to force uniform terminology. PS VII §134 defines the abelian weak class through homology, and RESULTS_STATE GALOIS D.2 is a related coefficient-detection lead, not a proof that every displayed comparison satisfies the same criterion.

### R044 — 134-8, scan 066, coflatness lemma; unproved claim

The English lemma states a derived-cohomology comparison for `u_a(x)=Hom(a,x)` and the proof uses preservation of injectives, followed by the French list “les projectifs sont plats”, “les injectifs sont coplats”, and injectivity of `Hom(a,b)`. The displayed tensor/Hom adjunction is the actual mechanism relating those clauses, and its hypotheses include enough injectives/projectives and limits. Compare PS VII §139, pp.589–590 and RESULTS_STATE GALOIS G.6/RESIDUE I.7; this supplies a coefficientwise method requiring its stated assumptions, rather than the full bare-derivator construction requested in those open entries.

### R045 — 134-8, scan 066, `Hom(a,x)` annotation; self-flagged

The term with `a` projective and `x` injective is underbraced “inj ?”. This marks the exact preservation-of-injectives step on which the preceding derived comparison depends, even though the later three-condition list asserts the intended relationship. Compare the renewed question on scan 068, PS VII §139's resolution caution, and RESULTS_STATE GALOIS G.6/RESIDUE I.7; the note does not erase the question mark by appealing to the list that follows it.

### R046 — 134-8, scan 067, `v(R\Gamma)` comparison; self-flagged

The page writes `v(R\Gamma(B,F))\overset{?}{\simeq}R\Gamma(B,v\circ F)` and relates the latter expression to homology on an opposite category, with the letters and degrees preserved as frozen. The surrounding `Hom(-,\xi)` construction, `\xi` injective, gives an explicit dualization route to inspect. Compare PS VII §139, pp.588–590 and RESULTS_STATE IMPL I1's claimed exact-colimit/inverse-limit duality and open IMPL P1; the leaf does not determine the general `lim^1` placement requested there.

### R047 — 134-8, scan 067, reused corrections sheet; unpursued implication

The underlying title is “Problèmes ouverts en théorie des Intersections. A. Grothendieck. Exposé XIV” with “Corrections à Faire après tirage” and five page/line instructions. Those instructions are a separate provenance and collation witness carried by this sheet, with their own page numbering, and they are fully transcribed. The title and the homological annotations must be recorded with their own textual locations; no mathematical result in RESULTS_STATE is inferred from their physical coexistence.

### R048 — 134-8, scan 068, slice homology criterion; unproved claim

The page spells out a slice map `A_{/b}=A/f^*(b)\to B_{/b}` and then `LH_\bullet(A,f^*F)\to LH_\bullet(B,F)`, with a `k`-additive coefficient category having enough projectives. These formulas give a precise bridge to PS VII §135, pp.561–564, and §138, pp.583–585 and to the claimed relative/absolute/coefficient Theorem A entries GALOIS B.1, B.3 and D.2 in RESULTS_STATE. The top weak-class subscript is frozen as `W_h|W_k` and the later line explicitly says `W_k`; a general theorem with corrected variance and uniform subscripts cannot be silently substituted for the leaf.

### R049 — 134-8, scan 068, final Hom question; self-flagged

After `x\mapsto Hom(a,x)` the page asks “transforme injectifs en … ?” and answers “OK si a est k-plat et projectif”, next to a tensor/Hom formula whose last argument remains uncertain in the reading. This is the local test linking scan 066's coflatness lemma to the coefficient comparison above. Compare PS VII §139, pp.589–590 and RESULTS_STATE GALOIS G.6/RESIDUE I.7; the source's two assumptions and the reading uncertainty remain part of the record.

### R050 — 134-8, scan 069, coasphericity and dual coefficients; unproved claim

The leaf gives a coasphericity comparison under enough `k`-flat projectives, injectives, and limits, then experiments with `Hom(-,I)` and writes `\mathbb Q` and `\mathbb Q_p/\mathbb Z_p`. The opposite-category/injective-projective switches make this a concrete dualization worksheet for scans 067–071, while the displayed `LH` degrees remain uncertain. Compare PS VII §139, pp.589–590 and RESULTS_STATE IMPL I1/P1 and GALOIS G.6; the page supplies a method to collate, not a complete derivation of those registered questions.

### R051 — 134-8, scan 069, “assez d'inj.”; self-flagged

“assez d'inj. k-co… ?” asks whether the requisite supply of coflat injectives is available, immediately before “OK”. The surrounding unfinished `Hom(J,I)` expression means the written “OK” should be reported with the question and the intended opposite-category passage, rather than treated as a missing proof. Compare scans 066 and 070–071, PS VII §139, and the open GALOIS G.6/RESIDUE I.7 coefficient-framework entries.

### R052 — 134-8, scan 070, derived composite; self-flagged

The explicit question is `RHom(a,R\Gamma(B,F))\overset{?}{\simeq}R\Phi(F)`, followed by “si Γ transforme injectifs en injectifs”. The unfinished Ext and Hom expressions record that the derived-composite justification is still being worked out, and the small table compares enough-projective/injective assumptions with flatness/coflatness. Compare PS VII §139, pp.588–590 and RESULTS_STATE GALOIS G.6/RESIDUE I.7; the page expressly asks for the written preservation-of-injectives condition and leaves the derived-composite comparison under a question mark.

### R053 — 134-8, scan 071, coefficient-change comparison; self-flagged

The page again writes `u(R\Gamma_{\mathcal M}(F))\overset{?}{\simeq}R\Gamma_{\mathcal M'}(u(F))` and asks “est elle Γ…-acyclique ?” of the proposed transported resolution. It then writes `C` injective but concludes about `u(F)`; that letter change is retained and belongs in a reading/reconstruction question. Compare scans 066–070, PS VII §139, pp.588–590, and GALOIS G.6/RESIDUE I.7; the explicit acyclicity question is the point to check before any use of the formula.

### R054 — 134-8, scan 071, projective probes; unpursued implication

The last paragraph applies `Hom(a,-)` to both members for projective `a`, defines `F^a(b)=Hom(a,F(b))`, and records `f^*(F^a)=(f^*F)^a`. This is a concrete objectwise comparison for reducing a coefficient-valued assertion to `Ab_k`, with the earlier flat/coflat assumptions still visible. Compare PS VII §139, pp.589–590 and RESULTS_STATE GALOIS G.6/RESIDUE I.7; checking that these probes detect the relevant comparison is a research action, not a theorem completed on this leaf.

### R055 — 134-8, scan 072, additive enlargement and slices; unpursued implication

The page juxtaposes `A\to B`, `add A\to add B`, their abelian presheaf categories, and `A_{/f^*(b)}\to B_{/b}`, under the label “W_k-asphérique”. These are the written maps linking its additive formulation to the slice-homology test on scan 068. Compare PS VII §135, pp.561–564, §138, pp.583–585, and §139, and RESULTS_STATE GALOIS B.3/D.2/G.6; the uncertain `f_!|f^!` is left unresolved in the transcription.

### R056 — 134-8, scan 073, unit and triangular identity; self-flagged

The unit `y\xrightarrow{\varepsilon_y}f^*f_!y` is followed by `\in W_{\mathcal M}^{!} ?`, and `f_!(\varepsilon_y)` in the next triangle is labelled “iso ?”. The triangle gives the exact morphisms to examine, including the separately displayed counit through `f_!(1_M)\otimes\xi`. Compare PS VII §134's localization question, scans 075–076, and RESULTS_STATE GALOIS G.6/RESIDUE I.7; the bang exponent was read from the ink before context access and remains a bang.

### R057 — 134-8, scan 073, unit epimorphism; self-flagged

The rotated margin asks whether `y\to1_M\otimes\kappa_!(y)` is “épi ??”, then writes a kernel sequence and the dual-looking evaluation map `1_M\otimes_k Hom(1_M,z)\to z`. Scan 077 returns to this precise epi/mono question with a module example, so the two scans should be studied together. Compare PS VII §138, p.586 for finite-projectivity and adjoint-existence hypotheses; RESULTS_STATE's open GALOIS G.6/RESIDUE I.7 entries do not assert the extra epimorphism property.

### R058 — 134-8, scan 074, realization of an object by `f_!(1_N)`; unproved claim

The page asks for a setting with `f_!` exact, `1_N` projective, and `f_!(1_N)=F`, then writes `N={F\in\underline M^{\unsure{\flat|b}}\mid a\otimes_kF\in M}` and maps involving `k^{(x)}`. The deletion of the earlier occurrence of the unit-image condition and its reappearance as c) show active rearrangement of hypotheses. Compare PS VII §138, pp.584–586 and §139, pp.590–591, and GALOIS G.6/RESIDUE I.7; the maps and the tensor-membership condition are the concrete contribution, while the construction's universal property is not completed here.

### R059 — 134-8, scan 074, binomial margin; unpursued implication

The formulas `1+at+P(a)t^2` and `P(a+b)=P(a)+P(b)+ab` have an exact counterpart in PS VI §119, pp.501–503, where multiplication in the truncated-power-series group produces the same equation for a splitting. The frozen line is `n!\,\unsure{P_n(t)}=t(t-1)\ \inserted{P}\,(t-n+1)`; together with “binomial”, it invites comparison with PS VI §119's explicit product formula and `Symbin` question and §120, pp.506–507, while its uncertainty and inserted `P` remain unresolved. This gives a specific connection between the scratch and the schematization program, with no corresponding completed result located in RESULTS_STATE and no relative date established for the two witnesses.

### R060 — 134-8, scan 075, implication diagram; unproved claim

The list starts from `H_i(M,f^*y)` on objects `y` of `N` and proceeds to `LH_\bullet(M,f^*G)\to LH_\bullet(N,G)`, weak-class preservation/reflection, and an equivalence of localizations. Its phrase “argument de résolution … par des sommes d'objets de N” identifies the proposed passage from representables to general coefficients, while two returning arrows visibly carry extra hypotheses on asphericity and epimorphic units. Compare PS VII §135, pp.563–564 and §138, pp.583–585, with RESULTS_STATE GALOIS B.3/D.2 as already claimed relative/coefficient results; the handwriting contributes these augmented-additive tests and their unfinished implication network.

### R061 — 134-8, scan 075, item (v′); reading question

The displayed equality is `W_N=f^{*-1}(W_M)`, but its following biconditional begins with the frozen `u\in W_M` and ends with `f^*u\in W_M`. The source triangle has `f:M\to N`, and the page's own use of `f^*` on `G\in N` supplies the concrete variance check: the argument of that restriction functor is on the `N` side. This raises a reading or drafting question about the first subscript, without changing it; compare PS VII §134's preimage definition of the weak class and RESULTS_STATE GALOIS D.2.

### R062 — 134-8, scan 075, lower proof attempt; withdrawn in the same text

The proposed `(iv)⇒(i)` proof refers to a lemma below, deletes “et est épi”, removes an “iso” on the counit, and removes an isomorphism sign on the final derived comparison. These cancellations are material evidence about the strength of the argument still available after revision, and they must be collated with the extra epimorphism assumption written on the curved implication arrow above. Compare scan 073's “épi ??” and scan 077's rank example, PS VII §138, p.586, and the coefficient-framework leads GALOIS G.6/RESIDUE I.7.

### R063 — 134-8, scan 076, first corollary; reading question

The corollary says “Supposons que `\kappa_!(1_M)\xrightarrow{\alpha_k}1_k`, alors …” and concludes that the counit is an isomorphism, followed by “κ* est pl. fid” and “κ! une localisation”. No isomorphism mark is written on that first hypothesis in the frozen reading, whereas the later hypothesis on the same page explicitly writes two such marks in `L\kappa_!(1_M)\to\kappa_!(1_M)\to1_k`. The preceding commutative square identifies the counit with `\alpha_k\otimes\xi`, providing the exact map whose assumed property needs clarification; compare PS VII §134 and §138, p.586, with GALOIS G.6/RESIDUE I.7 as open context.

### R064 — 134-8, scan 076, derived unit on projectives; unproved claim

Under its later, explicitly marked derived-unit hypothesis, the page calculates `L\kappa_!(1_M\otimes\kappa_!x)` for projective `x` and concludes that `x\to\kappa^*\kappa_!x` lies in `W_M`. The written reason is that `\kappa_!x` is projective, following a cancelled attempt to state the projective-preservation and derived-adjunction steps more generally. Compare scan 075's condition network and PS VII §138, pp.584–586; this gives a local computation relevant to GALOIS G.6/RESIDUE I.7 while retaining the actual projectivity and augmentation assumptions.

### R065 — 134-8, scan 077, two-sided adjoints; unproved claim

The page describes `\kappa^*: \xi\mapsto1_M\otimes_k\xi` with both adjoints and replaces “commute aux produits” by commutation with `\varprojlim`; it also records a generator assumption. In the concrete module example, “X plat de prés. finie i.e. X proj. de t. f.” parallels the finite-projectivity criterion explicitly stated in PS VII §138, p.586. The comparison is through the actual functor `X\otimes_k-` and its displayed dual-module adjoint, and bears on GALOIS G.6/RESIDUE I.7 without proving existence for their broader coefficient framework.

### R066 — 134-8, scan 077, unit epi/counit mono; self-flagged

Two “a-t-on” formulations ask whether `x\to\kappa^*\kappa_!x` is epic, and the margin asks `f^*f_*z\to z` “mono ?”. The Hom chain is the written map relating those tests, and the final module example assigns the epi/mono assertions to a rank-`\leq1` condition. Compare scan 073 and PS VII §138, p.586; the source gives a concrete test case, while the broader open GALOIS G.6/RESIDUE I.7 entries supply no blanket epi/mono assertion.

### R067 — 134-8, scan 078, SGA7 production instruction; unpursued implication

“SGA 7 Exposé VIII” and “p 95. Cette dernière page est très serrée. Voir pour tirage photo-offset” identify another internal page reference on a reused production sheet. The “dernière page” wording associates p.95 with that text's extent, without establishing that the present set contains its preceding 94 pages. Compare the separate cancelled SGA7 Exposé IX heading on scan 076 and the supplied task's distinction between reused sheets and the present notes; no RESULTS_STATE mathematical status is attached to this production note.

### R068 — 134-8, scan 079, dual description of `j_!`; unproved claim

The boxed `j_!x=\operatorname{Hom}_{\unsure{M^\flat|M}}(x,1_M)^\vee` is accompanied by “pour x dans M” and the assumption that the relevant Hom module is projective of finite type. The preceding adjunction `Hom_k(j_!x,\xi)\simeq Hom_M(x,1_M\otimes\xi)` provides the exact proposed representing relation; its dualization must retain the written finiteness qualification. Compare scan 077 and PS VII §§138–139, pp.586–591, and RESULTS_STATE GALOIS F.8/G.6/RESIDUE I.7 as open reconstruction/coefficient leads.

### R069 — 134-8, scan 079, opposite-unit comparison; self-flagged

The proposed comparison of `j'_!x=Hom_M(x,1_M)` with `Hom_{M^o}(x^o,1_{M^o})^\vee` carries an explicit “?”. The following pairing and the later `H_0`/dual-complex formula indicate the duality mechanism being sought but do not identify the two unit objects. Compare PS VII §139's dual homology/cohomology program, and RESULTS_STATE IMPL I1/P1 and GALOIS F.8; this is a source question, not a completed equivalence.

### R070 — 134-8, scan 081, augmented multiplicative interval; unproved claim

The leaf specifies an augmented algebra `J`, “pas néc comm. ni assoc.”, two endpoint sections, and tensor stability of `J\to1_M`, named `UW_M`. It assigns the unit role to `\delta_0` and the absorbing-element role to `\delta_1` through the displayed multiplication composites. This is explicit additional structure for the interval question of PS VII §134, p.560, and a method relevant to GALOIS G.6/RESIDUE I.7; the source's relaxed associativity/commutativity wording remains part of the construction to check.

### R071 — 134-8, scan 081, transfer to `J′`; reading question

“Je dis qu'alors” introduces tensor-stable weak equivalence of the second augmentation after a written comparison `J'\to J`, whereas the next diagram draws `J\otimes x\to J'\otimes x`. The two displayed morphism directions must be reconciled before reconstructing the proposed transfer argument; neither has been reversed in the transcription. Compare PS VII §134, p.560 and scans 059/084/086, with GALOIS G.6/RESIDUE I.7 as contextual leads rather than a proof of this transfer.

### R072 — 134-8, scan 084, attempted endpoint comparison; unproved claim

The upper diagram proposes `\beta:\lambda_!J\to\underline{\delta^1}` with `\beta=\delta_0\alpha\lambda_!(\varepsilon)`, and its two written evaluations give `\beta\lambda_!(\delta_0)=\delta_0\alpha` and `\beta\lambda_!(\delta_1)=\delta_0\alpha`. The final, adjoint-side diagram instead uses a map `\beta:J\to\lambda^{\unsure{*|\prime}}(\underline{\delta^1})` and writes the target conditions `\beta\delta_0=\delta_0\alpha`, `\beta\delta_1=\delta_1\alpha`. The page thus records an unresolved second-endpoint requirement and a proposed factorization through `H_0(L_.)`, without crossing out the upper candidate or completing a replacement; compare scan 059's questioned map, scan 086's extension condition, PS VII §134, p.560, and GALOIS G.6/RESIDUE I.7.

### R073 — 134-8, scan 084, augmentation direction; reading question

The middle diagram draws the augmentation from `J` upward to `1_M`, while the last left-hand vertical arrow is drawn from `1_M` down to `J` with the same `\varepsilon` label. The actual endpoint and adjoint maps around it are retained as drawn, so reconstruction needs a direction/label check at this exact place. Compare PS VII §134's interval discussion and the explicit interval of scan 081; the context does not authorize choosing one reading for both diagrams.

### R074 — 134-8, scan 086, extension map `u`; self-flagged

The comparison square labels its top arrow “u ?”, following the adjoint pair of interval diagrams `I\to j^*(\Delta^1)` and `j_!I\to\Delta^1`. The final line offers “J/1_M projectif, ou seulement `Ext^1(\lambda_{0!}(J/1_M),k)=0`”, specifying a concrete obstruction test for the unfinished lift. Compare scans 059 and 084 and PS VII §134, p.560; the open GALOIS G.6/RESIDUE I.7 entries are not resolved, and the final mathematical leaf in this range supplies no completed construction of `u`.

### R075 — 134-8, scans 080, 083, 087, reused typed p.3; unpursued implication

These three scans carry the typed Kimchi text numbered 3, including section “3. Le matériel nécessaire …”, with each copy's overtyping, clipping, and the additional rotated mark on scan 087 preserved separately. The visible page number is a witness to the pagination of that other text; the extract supplies no title page or total page count for it. Compare the supplied task's reused-sheet instructions and the manuscript-number table below; no RESULTS_STATE item is inferred from the sheet reuse.

### R076 — 134-8, scans 082 and 085, reused typed p.4; unpursued implication

These scans carry typed p.4, continuing the previous page and beginning section “4. La préparation et la conservation du Kimchi …”, including the deletion of “panier” and copy-specific imperfect letters. The text continues off the supplied page, so neither this numeral nor the section number supplies a total extent. Compare R075 and the supplied task's reused-sheet instructions; this is bibliographical evidence retained without a mathematical RESULTS_STATE assignment.

## Additional research actions and explicit calculations

### R077 — 134-8, scans 073 and 077; own idea / explicit calculation

Use the source's module example at `k=\mathbb Q`, `X=\mathbb Q^2`, and `x=\mathbb Q`, with the explicit symmetry `\tau:X\otimes X^\vee\to X^\vee\otimes X`, `v\otimes f\mapsto f\otimes v`. Under `\tau` and the ordered basis `e_1^*\otimes e_1,e_1^*\otimes e_2,e_2^*\otimes e_1,e_2^*\otimes e_2`, the unit `\eta_{\mathbb Q}(1)=\sum_i e_i\otimes e_i^*` becomes `(1,0,0,1)`, while the source's two evaluation counits, with this stated identification of tensor order, send `(a,b,c,d)` to `a+d`. The unit has one-dimensional image in `\mathbb Q^4` and three-dimensional cokernel, while evaluation has kernel spanned by `(0,1,0,0),(0,0,1,0),(1,0,0,-1)`, so this specific unit is not epic and these specific counits are not monic. **Confidence: high**, from the explicit maps and the displayed symmetry, consistent with scan 077's rank warning and PS VII §138, p.586; this calculation is not presented as new or as a verdict on GALOIS G.6/RESIDUE I.7.

### R078 — 134-8, scans 050, 053–055; own idea / research action

Reconstruct the counit argument as three separately indexed maps: the degree-zero comparison, the map for a contractible projective complex, and the passage through a projective resolution of the coefficient complex. Attach each use of exactness and projective preservation to its actual functor in scan 054's bicomplex, and compare the resulting restrictions with the cone example in PS VII §139, pp.588–589. **Confidence: high that this audit is useful**, because scans 050, 053 and 055 explicitly flag those three stages; GALOIS G.6/RESIDUE I.7 remain the broader open tasks and no new conditional theorem is being proposed.

### R079 — 134-8, scans 058 and 068; own idea / research action

Make a typed comparison ledger with three entries: scan 058's `J\otimes F`, scan 068's `LH(A,f^*F)\to LH(B,F)`, and DER XII ms.88–91's category-of-elements maps for `p_!H`. Record the actual domain, codomain, coefficient assumptions and quantifiers of every map before testing any passage between them. **Confidence: high that this prevents an unsupported identification**, because each witness visibly supplies different input data and a specific comparison map; it targets the still-open TOTASPH D.7/RESIDUE F.5 without re-deriving the recorded refutation in TOTASPH C.10.

### R080 — 134-8, scans 066–071; own idea / research action

Check the coefficient-change construction on the exact diagram `F^a(b)=Hom(a,F(b))` and retain the natural equality `f^*(F^a)=(f^*F)^a` as the starting comparison. Then audit the transported resolution term by term against the written “Γ-acyclique ?”, rather than replacing the `C/F` letter change by an assumed proof. **Confidence: high that this is the relevant audit**, from the explicit questions on scans 070–071 and PS VII §139's discussion of resolving coefficients; it bears on GALOIS G.6/RESIDUE I.7 and offers no general derived-commutation theorem.

### R081 — 134-8, scans 059, 084 and 086; own idea / research action

Assemble the interval problem around its two written endpoint equations, recording the evaluated candidate on scan 084 and the extension group on scan 086 in a single chain-level worksheet. Locate the exact short exact sequence and extension class to which the written `Ext^1` expression refers, and compare its map with the questioned adjoint map on scan 059. **Confidence: high that the worksheet is well motivated**, because the same desired endpoint comparison recurs on all three leaves and in PS VII §134, p.560; confidence in an eventual construction is left unassigned, and no proposed theorem is asserted.

### R082 — 134-8, scan 074; own idea / explicit calculation

Take `P(t)=t(t-1)/2`, as PS VI §119 explicitly writes, to check the equation for `P` on scan 074: expansion gives `P(a+b)-P(a)-P(b)=[(a+b)^2-(a+b)-a^2+a-b^2+b]/2=ab` in `\mathbb Q[a,b]`. This verifies the written binomial calculation and pinpoints the same expression used in PS VI §119, p.501, without establishing the later `Symbin` comparison question. **Confidence: high**, from the explicit polynomial identity; no corresponding completed RESULTS_STATE entry or novelty claim is assigned.



