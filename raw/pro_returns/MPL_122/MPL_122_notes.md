# MPL_122 — Research notes

## 1. Scope, evidence, and principal findings

This report concerns **122.pdf, scans 003–018 and 020–035**, the 32 supplied nonblank faces. The diplomatic transcription was frozen at **2026-11-17 11:24:06 UTC**; the context archive was opened at **11:24:15 UTC**. All reading comparisons below are subsequent to that freeze and leave the transcription unchanged.

There are **17 handwritten mathematical faces and 15 reused typed or printed faces**. The handwritten sequence develops duality for manifolds with boundary, a gluing model with a circle base, a dictionary with generic and special fibres, derived triangles with monodromy, and local cohomological bounds; the last face changes to finiteness conditions on inductive adic systems. The reused material includes valuation and module exercises, an Efimov lecture announcement, and a separate English quotient-construction text with two figure sheets.

| Finding | Evidence | Notes |
|---|---|---|
| The Book I étale-cohomology/monodromy placement is supported, but the fibration is an input to the model | 122/013, 015, 017, 020, 022 | RN001, RN009–RN011 |
| The manuscript explicitly leaves the algebraic comparison and compatibility of duality with derived invariants unproved | 122/022, 024 | RN017–RN023 |
| Several supposed corrections in Hua’s interpretation are differences from this independent reading of the ink | 122/007, 017, 022, 026 | RN005, RN011, RN019, RN025–RN026 |
| The last middle-degree diagram is cancelled; the preceding live sequence still warrants study | 122/032 | RN038–RN040 |
| The two spheres must be distinguished: the ambient space is W, the binding/link is W₀ | 122/028, 032, 034 | RN029, RN040–RN042 |
| The final finiteness warning concerns cokernels first and kernels dually, opposite to Hua’s reading | 122/035 | RN045–RN048 |
| The supplied results register has no directly resolved or advanced open problem from these pages | RS orientation and five matched Open rows | RN062–RN068; §7 |
| No handwritten title sheet or explicit total-page count is present among the supplied faces | All retained scans | §9 |

### Locators and status conventions

A locator such as **122/024:L13–23** means archive file **122.pdf**, scan **024**, logical lines 13–23 of **pages/MPL_122_122_scan024.tex**. These are stable lines in the frozen page fragment, not a claim that the manuscript has numbered lines; physical positions are also supplied where useful. Quoted text follows that witness, including abbreviations. A question mark inside an unsure macro is an editorial reading alternative unless specifically identified below as an authorial question.

**RS** means the supplied **context/notes/RESULTS_STATE.md**, read in full before these notes were written. Its Open, Proved, Refuted, and Known labels are the research returns’ claims, except where RS expressly records review; its earlier package notes are first-pass leads, and its war-game entries are unchecked plans. References to other cotes and source CSVs below are **references reported by RS**, not claims that those absent scans, CSVs, or complete previous reports were inspected. Only the four files supplied in the context archive were available.

**Hua** means **Hua, modernised reading of cote 122**, supplied as **context/hua_project/122.modern.tex** and read in full. Each use below names its section or subsection. It is an AI-produced interpretation, credited to Michel Hua’s project, not an independent proof and not the transcription used here. Its page labels usually refer to the small numbers on the sheets: its “page 23” is archive scan 024.

Every numbered note has a recorded context query. The full query-to-file/line record is in **work/context_searches.json**; the relevant comparison is given beside the note. “No direct RS entry” means no direct entry in the supplied selected register, not a claim about the whole archive or the project’s unprovided records. Mathematical reconstructions and examples are explicitly labelled as editorial ideas. External comparisons are listed with exact checked scope in §10.

## 2. Boundary duality, gluing, and the dictionary

### RN001 — What the preliminary placement gets right

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 013:L2–33, 017:L2–15, 020:L2–35, 028:L23–41; opening model and algebraic dictionary.  
**Context search:** monodrom|étale|Lefschetz|fibr. **Comparison:** README, “This package in our plan” and “What our planning document asks”; RS, “Orientation for this package”; Hua, “Le modèle : un livre ouvert (pages 12 à 16)” and “Les triangles de la fibre de Milnor (pages 19 à 21)”; supports the placement, limits the theorem claim.

The phrases “fibrés diff.”, “dans catégorie dérivée de Λ[π]”, and “Lefschetz local” confirm a programme connecting topology with the cohomology of a local algebraic degeneration. The pages do not develop heights, local symbols, representability, or a section-conjecture argument, so the broader rank-22 umbrella does not describe their immediate mathematical contribution. Hua’s Milnor/open-book interpretation is a useful model for these constructions, but the scans themselves do not prove a fibration theorem or name Milnor.

### RN002 — Compactness and coefficient hypotheses require separate attention

**Kind:** own idea. **Witness:** 122.pdf, scan 003:L3–37; upper half.  
**Context search:** paracompact|compacte|coefficients|Poincar. **Comparison:** Hua, “Variétés à bord et dualité (pages 2 à 4)” and “Le dossier, sa charpente et ses notations”; agrees that extra hypotheses matter; RS, returned-package lead MPL_11_002-042 O06, reported scans 017, 027, 034, 042, not a theorem about this P. **Confidence:** high for the explicit noncompact counterexample; it tests the claimed identification without deciding the intended later hypotheses.

The opening reads “para” inserted before “compacte”, while the comparison of ordinary relative cohomology with compactly supported cohomology needs more than paracompactness alone. For example, if P is the real line with empty boundary, ordinary H⁰(P) is nonzero whereas compactly supported H⁰(P) is zero, so that identification cannot be used for arbitrary noncompact P. The margin’s locally constant finite-dimensional vector-space coefficients helps the linear-dual interpretation, but does not supply compactness. Hua explicitly supplies compactness; this should remain an interpretive hypothesis, not a silent reading of the opening line.

### RN003 — The abandoned collar comparison has a live replacement

**Kind:** withdrawn in the same text. **Witness:** 122.pdf, scans 003:L49–53, 005:L2–10 and L24–40, 009:L20–28; lower first page and next two handwritten faces.  
**Context search:** collier|épaississement|excision|cinq. **Comparison:** Hua, “Variétés à bord et dualité (pages 2 à 4)” and “Les trois suites et leurs duales”; supports the later excision route; no directly settled RS entry.

The tentative homotopy comparison on scan 003 and the “lemme des cinq” argument at the top of scan 005 are struck out. The live replacement on scan 005 passes through Hᶦ with support in P′ and relative cohomology “mod ∂P”, and scan 009 makes the excision comparison explicit. A reconstruction should cite the live pair and excision maps rather than reuse the cancelled inclusion of pairs.

### RN004 — Q is literally defined as the boundary before being used as the complementary piece

**Kind:** reading question. **Witness:** 122.pdf, scan 007:L4–16; opening.  
**Context search:** adhérence|complémentaire|lapsus. **Comparison:** Hua, “Une variété coupée en deux (pages 6 à 10)”; same discrepancy identified, but Hua replaces the definition; no direct RS entry.

The witness says “Soit Q=P−P̊”, followed by W=P∪Q and P∩Q=∂P=∂Q. The first formula makes Q the boundary of P and cannot describe the stated decomposition except in a degenerate case. Hua reads Q as the closure of W−P, which makes the subsequent picture coherent; this is a proposed correction in the notes, not the frozen text.

### RN005 — Mayer–Vietoris is explicitly a conjectural identification, and the degree reading differs from Hua

**Kind:** self-flagged. **Witness:** 122.pdf, scan 007:L21–35; central sequence and following sentence.  
**Context search:** Mayer|Thom|sans doute. **Comparison:** Hua, “Les trois suites et leurs duales”; supports the proposed identification, differs on the exponent read in the source; no direct RS entry.

“This relative sequence” is said to be “sans doute” the Mayer–Vietoris sequence. A proof must identify the support sequence through the codimension-one Thom map and fix the sign of the difference of the two restrictions, not merely compare the groups. Hua reports an Hⁱ⁺¹(R,…) term and corrects it to Hⁱ(R,…), whereas the frozen witness already reads the exponent as unsure i; that alleged correction is therefore a disagreement between readings, not a demonstrated error in this transcription.

### RN006 — One missing coefficient dual must not be regularised away

**Kind:** reading question. **Witness:** 122.pdf, scan 007:L37–43; bottom dual sequence.  
**Context search:** coefficients|transposée|orientation. **Comparison:** Hua, “Les trois suites et leurs duales”; differs by giving the uniformly dualised formula; RS lead MPL_11_002-042 O06 supplies only a general Poincaré/Künneth comparison.

The last line has F in the P term and F∨ in the Q term, although the line above has F∨ in both. A transposition argument for general local systems would require a consistent dual coefficient system and the orientation sheaf. Hua normalises this, but the present evidence is a coefficient discrepancy to check, not permission to erase it.

### RN007 — The support comparison is reconsidered rather than simply assumed

**Kind:** self-flagged. **Witness:** 122.pdf, scans 009:L3–27 and 011:L20–30; cancelled comparison, later excision square, and rotated cancelled block.  
**Context search:** support|excision|isomorphisme. **Comparison:** Hua, “Les trois suites et leurs duales” and “Le tableau de la page 10”; supports the excision explanation, with the source’s provisional state retained.

The initial comparison to H!ᶦ(P̊) on scan 009 is cancelled and then replaced by a square labelled “excision”. The rotated cancelled block on scan 011 still places “≃ ?” beside Hᶦ_Q(W) and H!ᶦ(W−P). The natural question is whether all these identifications commute with the connecting maps and coefficient duality, since an objectwise isomorphism does not by itself identify the full triangles.

### RN008 — R, T, and the compact Mayer–Vietoris notation have not been stabilised

**Kind:** reading question. **Witness:** 122.pdf, scans 007:L14–33 and 011:L13–54; recap tables.  
**Context search:** Récapitulation|tableau|Mayer. **Comparison:** Hua, “Le tableau de la page 10”; agrees on the intended four-sequence organisation, normalises several names; no direct RS entry.

The recap uses R in the upper table, T in the lower formulas, and MV!(W,R) before MV!(W,P,Q). This appears to be a change of names within the same boundary decomposition, but it is not a definition of three different Mayer–Vietoris functors. The four labels Φ, Φ′, Ψ, Ψ′ are useful research anchors only after the support convention and the coefficient changes in RN006 have been fixed.

### RN009 — The bundles and their boundary trivialisations are assumptions

**Kind:** unproved claim. **Witness:** 122.pdf, scans 013:L13–41 and 015:L2–29; gluing construction.  
**Context search:** fibration|trivialisations|construction. **Comparison:** Hua, “La construction” under “Le modèle : un livre ouvert”; supports the model and explicitly treats the fibration as given; RS orientation question 1.

“On suppose donnés” introduces the gluing identifications, and the preceding lines already assume P and Q are differentiable bundles. The later specialisation to a circle and a contractible N explains the open-book shape, but does not establish that an arbitrary isolated singularity admits it. Thus these pages supply the cohomological organisation of such a model, not the analytic existence theorem for the model.

### RN010 — Boundary triviality is stronger than needed for the homotopy equivalence

**Kind:** unpursued implication. **Witness:** 122.pdf, scan 015:L8–19; upper half.  
**Context search:** collier|trivialité|homotopie. **Comparison:** Hua, “La construction”; restates its collar observation; no direct RS entry.

The sentence makes the triviality of the boundary bundle imply that W−Q=P−∂P→P is a homotopy equivalence. A collar of the boundary already gives that equivalence for a manifold with boundary; the trivialisation has a different role in constructing the boundary product and gluing map. This separates the homotopy argument from the stronger data later needed to trivialise the monodromy action at the boundary.

### RN011 — The geometric generic fibre is already distinguished in the frozen reading

**Kind:** reading question. **Witness:** 122.pdf, scan 017:L2–15 and L58–61; dictionary and lower lattice.  
**Context search:** dictionnaire|géométrique|générique. **Comparison:** Hua, “Le dictionnaire (page 16)”; supports the dictionary but contradicts its claim that the bar is not marked; RS lead MPL_33_147-181+34_002-017 D21, reported 33/166:L6–18, offers a neighbouring analytic/algebraic programme only.

The row under M contains X′ with a barred unsure η/γ, whereas the row under P has an unbarred subscript. Hua says the manuscript does not mark the geometric bar and supplies it editorially. This independent reading instead finds that distinction already present, while retaining uncertainty over the underlying letter; the two lattices should be compared at the level of the displayed maps, not by importing Hua’s simplified diagram.

### RN012 — The count “40 … 80 … mais” is an unfinished enumeration

**Kind:** unpursued implication. **Witness:** 122.pdf, scan 017:L33–48, L65–74, L89–91; margins.  
**Context search:** 40|80|dénombrement|binom. **Comparison:** Hua, “Le dictionnaire (page 16)”; same unfinished count, but no established count in RS.

“Cela fait 80 suites exactes, mais” stops without its qualification. The sheet lists ten triples, partial totals 20, 14, 2, 4, and a binomial expression whose displayed intermediate arithmetic does not equal its stated total. A useful follow-up would enumerate the actual admissible pairs and triples of spaces, quotient by symmetry only after identifying the induced maps, and determine what the unfinished “mais” was limiting.

### RN013 — The boundary pairing is a concrete bridge to the later u construction

**Kind:** unpursued implication. **Witness:** 122.pdf, scan 017:L76–87; bottom diagrams.  
**Context search:** accouplement|compact-to-ordinary|Poincar. **Comparison:** Hua, “Le dictionnaire (page 16)”; RS lead MPL_11_043-058+56 N045, reported cote 56 scan 020, and MPL_11_002-042 O06; adds this specific boundary-degree model, does not establish either earlier lead.

The displayed pairing Hᶦ(Q)×Hⁿ⁻ⁱ⁻¹(P)→Hⁿ⁻¹(R)≃Λ makes the loss of one dimension at the common boundary explicit. It is a more specific comparison with the compact-to-ordinary map reported in N045 than the shared word “duality”, but the present n is the ambient dimension of this early section, not yet the half-dimension parameter of scan 022. No identification with the earlier package’s norm-2 annotation follows from the supplied extract.


## 3. Derived triangles, equivariance, and signs

### RN014 — The boundary action and the cup-compatible restriction are part of the data

**Kind:** unproved claim. **Witness:** 122.pdf, scan 020:L2–18; triangles (a) and (b).  
**Context search:** triviale|compatible|monodromie. **Comparison:** Hua, “Les triangles de la fibre de Milnor (pages 19 à 21)”, paragraphs (a) and (b); supports the interpretation; RS LM7 C.1 [Known, return’s claim], reported §51.13–14, folios 719–724, scans 143–153, is a different duality statement.

The annotations “on met dessus op. triviale de π” and “ρ compatible aux cup” specify more than a list of cohomology groups. Hua explains the trivial boundary action using the supplied boundary trivialisation, which is consistent with the topological model. Any algebraic comparison must identify this equivariant restriction map and its product structure; the Picard 1-motive duality in LM7 C.1 neither supplies nor verifies that comparison.

### RN015 — A shift and a Tate twist must not be collapsed into one parenthesis

**Kind:** reading question. **Witness:** 122.pdf, scans 020:L11–18 and L31–32, 024:L18–20; circle factor and relative triangle.  
**Context search:** torsion|Tate|décalage|modérée. **Comparison:** Hua, “Les triangles de la fibre de Milnor (pages 19 à 21)”, paragraph (b) and its footnote; supports a topological shift, adds an étale interpretation; no direct RS result.

The frozen text has the mixed forms “(−1]” and “(−2]”, a separate “(−1)” at β’s target, and the unambiguous [−1] in the later circle decomposition. The cohomological degree of the circle factor is therefore well supported, but a Tate twist cannot be inferred merely by turning every parenthesis into a bracket. Hua supplies L(−1)[−1] for tame étale inertia; that comparison requires an explicit coefficient category and inertia hypothesis absent from these formulas.

### RN016 — β is described by a degree-lowering boundary map, even where the word is doubtful

**Kind:** reading question. **Witness:** 122.pdf, scan 020:L16–20 and L28–35; right margin and triangle (d).  
**Context search:** résidu|Gysin|cobord|dévolution. **Comparison:** Hua, “Les triangles de la fibre de Milnor (pages 19 à 21)”, paragraphs (b) and (d); supports the map’s role, normalises the prose; RS MPL_60_002-035 F48 is only a related duality lead, not a residue calculation here.

The doubtful word is transcribed “dévolution”, while the surrounding sentence explicitly relates Hᶦ(W−W₀) to Hⁱ⁻¹(W₀). The later note “c’est le β de (b)” supplies a second anchor for identifying this with the connecting map in the support/Gysin triangle. “Residue” is consequently a defensible modern description, but remains a description of the map rather than a replacement reading of the disputed word.

### RN017 — The comparison u₀ is an isomorphism whose identification is still deferred

**Kind:** self-flagged. **Witness:** 122.pdf, scan 022:L9–15; first NB.  
**Context search:** identifier|excision|theta|u_0. **Comparison:** Hua, “Les triangles de la fibre de Milnor (pages 19 à 21)”, final morphism-of-triangles paragraph; Hua supplies excision, while the witness explicitly defers the identification; RS MPL_131 RN001 is a construction-technique lead, reported 131/002:L13 and 131/017:L25, not this proof.

“Un isom u₀ qu’on aura à identifier” leaves the compatibility with the canonical object identifications unfinished. The other two components are specified as u₁=ρ₀ and u₂=inj₁, so the missing step is a naturality comparison between two triangles, not merely the assertion that their first objects are isomorphic. Hua’s excision explanation is a candidate completion to check with the same boundary and sign conventions.

### RN018 — The algebraic case is expressly left to be proved

**Kind:** self-flagged. **Witness:** 122.pdf, scan 022:L16; slanted left margin.  
**Context search:** algébrique|justification|dualité analytique|descent. **Comparison:** Hua, “Les triangles de la fibre de Milnor (pages 19 à 21)”, last footnote, calls the margin almost unreadable; RS MPL_33_147-181+34_002-017 D21 [first-pass lead], reported 33/166:L6–18; adds a concrete unresolved comparison to that broader programme.

The margin reads “à [unsure prouver] dans le cas algébrique”, followed by less secure words about formal justification and self-duality. This is positive evidence that the topological diagram was not being treated as an automatic algebraic proof. The connection to D21’s analytic duality and cohomological-descent programme is methodological; the supplied extract contains no result resolving this precise comparison.

### RN019 — Perfectness does not by itself remove universal-coefficient terms

**Kind:** reading question. **Witness:** 122.pdf, scans 022:L20–40 and 030:L32–33; derived dual and its group-level use.  
**Context search:** parfait|auto-injectif|Ext|coefficients. **Comparison:** Hua, “Le dossier, sa charpente et ses notations”, coefficient convention, and “L’application u”; supports the need for coefficient hypotheses, differs on the first shift read in the ink; RS LM7 C.1 concerns separately specified integral realisations.

“K• parfait rel. à Λ” supports the tensor–derived-Hom identification, but does not alone identify cohomology of the derived dual with the ordinary dual of each cohomology group. Hua explicitly assumes a field or self-injective coefficient ring; that is a supplied convention, and an integral version needs a universal-coefficient analysis or suitable torsion-freeness. Its claim that the first displayed shift is initially [2n] also differs from the frozen scan 022:L22, which reads [−2n].

### RN020 — Equivariant u requires a class before forgetting the action

**Kind:** own idea. **Witness:** 122.pdf, scan 022:L24–40; boxed u and following “i.e.”.  
**Context search:** cohomologie de|relèvement|Lambda.*pi|parfait. **Comparison:** Hua, “L’application u”; credits its equivariant correction and adds the possible lifting ambiguity; no direct RS result. **Confidence:** high under a perfect Λ-complex, a genuine π-action, and the stated derived-Hom convention; the distinction is functorial.

The source places u in D(Λ[π]) but then writes H²ⁿ(K⊗ᴸK) without derived π-invariants. Following Hua’s distinction, the equivariant morphism is represented by H²ⁿ(RΓ(π,K⊗ᴸK)), whose image after forgetting equivariance is the displayed ordinary class. For π=ℤ the two-column group-cohomology spectral sequence also allows an H¹(π,H²ⁿ⁻¹(K⊗ᴸK)) contribution, so an invariant ordinary class need not determine a unique equivariant lift. This gives a precise additional question for the algebraic comparison without changing the source’s formula.

### RN021 — The sign of transposition is authorially unresolved

**Kind:** self-flagged. **Witness:** 122.pdf, scan 022:L42 and scan 024:L2–11; bottom statement and next face.  
**Context search:** signe|rotation|transposés. **Comparison:** Hua, “L’application u”; same unresolved sign, with a modern parity interpretation; RS MPL_11_002-042 O06 is a general duality lead only.

“ρ et ρ′ sont transposés l’un de l’autre (signe ?)” is an explicit request to settle the sign. A completion must specify the trace orientation, the dual of a triangle, and the sign in its rotation, then check the boundary morphism with those conventions. The expected middle-degree symmetry of an intersection pairing does not by itself settle the chain-level sign of every arrow.

### RN022 — “Commutation” with derived invariants is itself marked for verification

**Kind:** self-flagged. **Witness:** 122.pdf, scan 024:L13–23; triangle (b′) and boxed margin.  
**Context search:** commutation|expliquer|Gamma.*pi|dimension.*1. **Comparison:** Hua, “Les triangles (c′) et (b′)”; the supplied one-dimensional duality formula answers the topological version conditionally; RS orientation question 3.

The page says “[expliquer comment ?]” and “vérifier la commutation de RΓ^π à RHomΛ(−,Λ)”. Its displayed shift changes from −2n to −2n−1, so literal unshifted commutation would not give the claimed triangle. Hua supplies the circle’s one-dimensional duality; the remaining task is to make that identification compatible with the actual maps and, separately, formulate the correct algebraic analogue.

### RN023 — A two-term calculation isolates the extra shift

**Kind:** own idea. **Witness:** 122.pdf, scans 022:L22–26 and 024:L18–22; duality shifts.  
**Context search:** groupe de dualité|contragrédiente|décalage. **Comparison:** Hua, “Les triangles (c′) et (b′)”; verifies the shift in its proposed topological explanation, not an additional RS theorem. **Confidence:** high for a bounded finite-projective Λ-complex with an invertible chain-level monodromy T; it follows from dualising a two-term resolution.

Compute RΓ(ℤ,K) as Cone(T−1:K→K)[−1], with contragredient action (T⁻¹)∨ on K∨. Dualising this two-term complex gives RΓ(ℤ,K∨)≃RΓ(ℤ,K)∨[−1], since (T⁻¹)∨−1 differs from −(T−1)∨ by an invertible factor. Consequently the shift −2n−1 in scan 024 is the expected one, after choosing the orientation of the circle. This calculation addresses the shift only; it does not fix RN021’s triangle signs or prove an unrestricted inertia version.

### RN024 — The λ and μ degrees explain why their targets differ by one

**Kind:** unproved claim. **Witness:** 122.pdf, scan 024:L34–49; lower pairings.  
**Context search:** lambda|mu|accouplements|données nouvelles. **Comparison:** Hua, “Les données nouvelles”; agrees with the final degree pattern and supplies a construction; RS MPL_60_002-035 F48, reported 60/035, is analogous duality bookkeeping, not a height formula for these spaces.

The revised exponents give λ a total degree 2n and μ a total degree 2n−1, followed by “je dis que c’est β” and “je dis que c’est α”. With Poincaré duality on W₀ of dimension 2n−1, those pairings indeed have targets Hⁱ⁻¹(W₀) and Hⁱ(W₀), respectively. Identifying them with the previously defined α and β still requires the compatible trace and boundary maps; their degree agreement alone is insufficient.

### RN025 — The frozen reading already pairs triangles (d) and (e)

**Kind:** reading question. **Witness:** 122.pdf, scan 026:L12–14; underlined sentence and NB.  
**Context search:** transposés|types|données nouvelles. **Comparison:** Hua, “Les données nouvelles” and “Sans hypothèse de non-singularité”; differs from both reported letter readings; no direct RS result.

The underlined sentence reads “les triangles (d) et (e) sont transposés”, and the next paragraph lists (a),(b),(c) as pairing with their own types and (e) with (d). Hua instead first reports (a) and (b), then explains why they cannot be transposes of one another, and later repairs a different type list. Those repairs should not be attributed to the present witness, whose letters already support the coherent type pairing.

### RN026 — The nonsingularity hypothesis is retained in this reading

**Kind:** reading question. **Witness:** 122.pdf, scan 026:L14; coefficient NB.  
**Context search:** non-singularité|singulière|Verdier|coefficients généraux. **Comparison:** Hua, “Sans hypothèse de non-singularité”; contradicts the asserted removal of the hypothesis; RS MPL_33_147-181+34_002-017 D21 remains only a possible programme-level connection.

The NB reads “sous hyp. de … non singularité sur W”, after “singularité” has been deleted. Hua interprets the paragraph as dispensing with nonsingularity by using Verdier duality. That generalisation may be mathematically available in an appropriate category, but it is not what this frozen reading of the sentence asserts.

### RN027 — A singular-space extension would change the dual coefficients

**Kind:** own idea. **Witness:** 122.pdf, scans 022:L20–22 and 026:L14; nonsingularity and “coefficients ‘duaux’”.  
**Context search:** Verdier|duaux|Dualité analytique. **Comparison:** Hua, “Sans hypothèse de non-singularité”, credited as the proposed extension; RS MPL_33_147-181+34_002-017 D21 [lead], reported 33/166:L6–18. **Confidence:** medium as a research route; the required constructibility, dualising complex, and functorial identifications are not supplied on these pages.

One can test Hua’s extension by replacing the constant shifted orientation object with the actual dualising complex and retaining the six-functor localisation triangles. The formal pairing of an open–closed localisation triangle with its dual then becomes a plausible framework, but it will not generally leave the same constant-coefficient formulas unchanged on a singular W. The useful next task is to specify that category and the dual coefficients before claiming that the handwritten hypothesis can be dropped.

## 4. Sphere hypotheses, vanishing, and the unfinished middle degrees

### RN028 — The upper-degree calculation is revised and depends on connectedness

**Kind:** withdrawn in the same text. **Witness:** 122.pdf, scans 026:L22–25 and 028:L2–14; cancelled endpoint argument and replacement.  
**Context search:** connexe|degrés du haut|Gysin. **Comparison:** Hua, “La suite de Gysin”; supports the endpoint repair; no direct RS result.

The endpoint sequence and the following equality on scan 026 are cancelled and replaced by the larger diagram on scan 028. The annotation “si W₀ est connexe” is needed for its identification of the top cohomology of W₀ with one copy of Λ; an arbitrary open-book binding need not be connected merely because n≥2. The subsequent appeal to local Lefschetz indicates the additional geometric setting in which that connectedness is expected.

### RN029 — The cohomological-sphere criterion concerns the ambient W

**Kind:** unproved claim. **Witness:** 122.pdf, scan 028:L16–20; left margin.  
**Context search:** sphère cohomologique|réciproque|fermée connexe. **Comparison:** Hua, “La suite de Gysin”; explicitly supplies closedness, connectedness, and orientability; RS orientation question 2 asks a related but different intersection-form question.

The margin asserts “W sph. coh. ⇔” the residue isomorphisms outside degrees 0 and 2n, together with injectivity at 2n. Its converse must be read with hypotheses ensuring the low and top groups of W and the Gysin sequence; Hua makes W a closed connected oriented manifold and W₀ a nonempty codimension-two binding. This is a criterion for W, whereas a nondegenerate middle pairing of a page is naturally a criterion about its boundary W₀ under further vanishing hypotheses.

### RN030 — Local Lefschetz is invoked, not proved or fully formulated

**Kind:** unproved claim. **Witness:** 122.pdf, scan 028:L23–29; lower opening.  
**Context search:** Lefschetz local|régulier|profondeur|Milnor. **Comparison:** Hua, “Lefschetz local”; supports the intended bound, adds named analytic and étale comparisons; RS orientation questions 1 and 3.

“Supposons que X soit régulier en x” is followed by the local Lefschetz restriction map and no proof. The first bound is frozen as n−unsure(2|1), and the next line says monomorphism in degree n−1. The geometric morphism, coefficients, and local hypotheses needed for an étale version must be recovered elsewhere before this can be cited as a theorem in that generality.

### RN031 — Dualising the local bound is a useful consistency test, not a reading rule

**Kind:** own idea. **Witness:** 122.pdf, scan 028:L27–38; paired restriction and Gysin bounds.  
**Context search:** transposé|Lefschetz local|bornes. **Comparison:** Hua, “Lefschetz local”; agrees with its degree calculation while retaining the witness alternatives. **Confidence:** high conditional on perfect Poincaré pairings in dimensions 2n+1 and 2n−1; it is a direct index conversion.

If the restriction is an isomorphism in degree j≤n−2 and injective at j=n−1, duality converts it into an isomorphism Hⁱ(W₀)→Hⁱ⁺²(W) for i=2n−1−j≥n+1 and a surjection at i=n. This supports the n−2 alternative and the expected critical degree, but does not prove which overwritten stroke was made. The frozen inequalities and their alternatives therefore remain intact.

### RN032 — The vanishing list has low-dimensional collisions

**Kind:** reading question. **Witness:** 122.pdf, scans 028:L40–41 and 030:L2–24; vanishing lists and n=1 case.  
**Context search:** annulations|n = 1|degrés. **Comparison:** Hua, “Les annulations”; same main pattern, with a modern explanatory example; no direct RS result.

The sphere case gives possible link degrees 0,n−1,n,2n−1 and complement degrees 0,1,n,n+1. The separate “Si n=1” calculation is mathematically significant because some listed degrees coincide, so generic formulas must not be counted as independent rows in that case. Hua’s trefoil example illustrates one connected binding, but is not on the manuscript and does not cover all possible component counts.

### RN033 — The limit passage needs its actual system and maps

**Kind:** unproved claim. **Witness:** 122.pdf, scan 030:L26–30; boxed fibre vanishing.  
**Context search:** passage|limite|Wang|annulations. **Comparison:** Hua, “Les annulations”; agrees that a missing justification remains, but does not assume its Wang objection refutes every possible limit argument; RS orientation question 3.

“Par passage à la limite” connects a revised vanishing bound for W−W₀ with Hᶦ(M,Λ)=0 for i>n. The pages do not specify the indexing system, the transition maps, or a comparison identifying that limit with the fibre. Hua correctly observes that one mapping-torus vanishing statement is insufficient, but the author’s mention of a limit deserves a separate investigation, especially with finite coefficients and finite covers.

### RN034 — A monodromy test shows precisely what the single-space argument misses

**Kind:** own idea. **Witness:** 122.pdf, scan 030:L26–33; “par passage à la limite” and the following relative sequence.  
**Context search:** gamma|Wang|bijectif|limite. **Comparison:** Hua, “Les annulations”; credits its Wang-sequence objection and sharpens its scope; no direct RS result. **Confidence:** high for the stated algebraic test, limited as an interpretation of the unspecified geometric limit.

For the abstract monodromy module V=ℚ with T=2, both ker(T−1) and coker(T−1) vanish although V does not, and the same is true for every positive power Tᵐ. Thus the invariants and coinvariants of a single local system, even through these power tests over ℚ, need not detect its nonzero fibre. This is not a counterexample to an unstated finite-coefficient limit argument: for a finite module an automorphism has finite order, so some finite cover removes the monodromy obstruction. The missing hypotheses determine which inference is legitimate.

### RN035 — The verified Milnor comparison supplies stronger input in a specified setting

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 013:L13–33, 028:L25–41, 030:L29, 032:L19–22.  
**Context search:** Milnor|bouquet|complexe cellulaire|fibration. **Comparison:** Hua, “La construction”, “Lefschetz local”, “Les annulations”, and “La suite exacte des degrés du milieu”; supports its named complex-hypersurface comparator, without assigning its proof to the pages; RS orientation questions 1 and 5. **External comparison:** [Milnor68], §§4–6, especially Theorems 5.1, 5.2, 6.5.

Milnor’s 1968 treatment proves the small-sphere fibration, finite n-dimensional CW type for the fibre, (n−2)-connectivity of the link, and, for an isolated critical point, a bouquet of n-spheres. In that complex-hypersurface setting these results supply Hⁱ(M)=0 for i>n and the stronger Hⁿ⁻¹(M)=0 when n≥2. The handwritten argument is more tentative and retains Hⁿ⁻¹(M), so the stronger reduction belongs to the external comparison, not to its finished conclusions.

### RN036 — The successor term in the long exact sequence tests the sign of the exponent

**Kind:** reading question. **Witness:** 122.pdf, scan 030:L32–33; last display.  
**Context search:** 2n-i-1|suite exacte longue|milieu. **Comparison:** Hua, “La suite exacte des degrés du milieu”; proposes the negative-one exponent; no direct RS result.

The frozen successor term reads H²ⁿ⁻ⁱ⁺¹(M)∨ with −1 retained as the alternative for the final sign. Applying cohomology to the triangle K∨[−2n]→K→L gives Hⁱ⁺¹(K∨[−2n]), hence H²ⁿ⁻ⁱ⁻¹(M)∨ under the coefficient assumptions of RN019. This supplies a mathematical reason for the alternative, not a retrospective alteration of the ink-priority reading.

### RN037 — The bound and its parenthetical explanation disagree under one reading

**Kind:** reading question. **Witness:** 122.pdf, scan 032:L6–13; top live formulas and margins.  
**Context search:** n-3|épim|bornes|milieu. **Comparison:** Hua, “La suite exacte des degrés du milieu”; differs by choosing n+2 from the explanatory inequality and by reading a different epimorphism degree.

The first range is frozen as i≥n+unsure(1|2), but its parenthesis says “donc 2n−i−1≤n−3”, which fits n+2. Hua normalises the earlier bound to n+2 before strengthening it using the n-dimensional fibre bound, while the margin’s epimorphism degree also differs between the two readings. These are separate reading questions; they should not be collapsed into a theorem with all the bounds silently harmonised.

### RN038 — The live “surj” forces the next middle map to vanish

**Kind:** unproved claim. **Witness:** 122.pdf, scan 032:L13–17; upper serpentine exact sequence.  
**Context search:** surj|noyau|intersection|milieu. **Comparison:** Hua, “La suite exacte des degrés du milieu”; same mathematical objection, with its example treated as interpretation; no direct RS result.

The live arrow Hⁿ⁻¹(W₀)→Hⁿ(M)∨ carries “surj”. Exactness would then force the next map Hⁿ(M)∨→Hⁿ(M), the middle-degree u, to be zero. No such hypothesis is supplied there, so this label requires proof or qualification even before discussing the cancelled diagram below.

### RN039 — The final middle-degree diagram is withdrawn, not a settled boxed theorem

**Kind:** withdrawn in the same text. **Witness:** 122.pdf, scans 030:L32–36 and 032:L13–31; general sequence, live revision, and final cancelled block.  
**Context search:** encadré|zigzag|six termes|milieu. **Comparison:** Hua, “La suite exacte des degrés du milieu”; contradicts its treatment of the final crossed-out block as a live conclusion; RS orientation question 2 must be answered with this qualification.

The phrase “et la suite exacte précédente devient” and the final two-line diagram are inside a deletion in the frozen witness. Hua treats the strokes as symmetry or Euler-characteristic markings and presents that diagram as a conclusion. The preceding live sequence remains evidence for the middle-degree programme, but a reconstructed six-term theorem must be labelled as reconstruction, with its hypotheses and the unproved “surj” distinguished from the cancelled material.

### RN040 — A unimodular criterion would concern the link under stronger vanishing

**Kind:** own idea. **Witness:** 122.pdf, scans 022:L26–40, 032:L13–31, 028:L16–20; u, middle groups, and ambient criterion.  
**Context search:** intersection|unimod|homology|noyau|conoyau. **Comparison:** Hua, “La suite exacte des degrés du milieu”, final footnote; credits its kernel–cokernel reduction and answers the additional question in RS “Orientation for this package”, item 2. **Confidence:** high with the explicitly added compact oriented manifold, connected boundary, finite-free integral middle cohomology, and bouquet-type vanishing assumptions; not an unconditional reading of the scans.

Assume n≥2, M is a compact oriented 2n-manifold with connected boundary W₀, and its reduced integral cohomology is finite free and concentrated in degree n. The pair sequence and duality then give 0→Hⁿ⁻¹(W₀)→Hⁿ(M)∨→ᵘHⁿ(M)→Hⁿ(W₀)→0, with all other reduced link groups outside its top degree zero. Consequently W₀ is an integral homology sphere exactly when u is unimodular; over a field the corresponding assertion is nondegeneracy over that field. This characterises W₀, not the ambient W of RN029, and is not established on these pages, which have not eliminated Hⁿ⁻¹(M).

### RN041 — The last special-fibre vanishing omits the top link degree

**Kind:** reading question. **Witness:** 122.pdf, scan 034:L21–24, compared with scans 028:L10–14 and 032:L19–22.  
**Context search:** termes de fibres|link|V_s|V_.*xi. **Comparison:** Hua, “En termes de fibres (page 33)”; same conflict, but its proposed reinterpretation as the Milnor fibre is not established; no direct RS result.

After “singularité isolée”, the witness writes Hⁱ(Vₛ)=0 for i≠0,n−1,n. If Vₛ retains the dictionary’s link meaning and n≥2, this loses the nonzero top degree 2n−1 present in the preceding link formulas. Hua proposes that the fibre rather than the link is intended, but the nearby subscript is frozen as unsure ξ|bar s and does not settle that change of object.

### RN042 — The final page shows one implication and altered endpoint notation

**Kind:** reading question. **Witness:** 122.pdf, scan 034:L2–19; top criterion and endpoint sequence.  
**Context search:** termes de fibres|critère|conoyau. **Comparison:** Hua, “En termes de fibres (page 33)”; differs by writing an equivalence and normalising Wη to Vη; related to RN029 rather than a new RS result.

The visible initial relation is a downward implication from “V une sphère cohomologique”, while Hua presents an if-and-only-if statement. Scan 028 already proposes a converse under its implicit hypotheses, so an equivalence may be reconstructible, but it is not the arrow drawn here. The same passage switches to Wη in the 2n term and labels one vanishing “si n>1”, differences that a critical comparison must preserve before normalising the formulation.

### RN043 — Monodromy is present, but no Picard–Lefschetz or tame–wild theorem is stated

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 017:L2–15, 020:L4–18, 022:L26–40, 024:L13–23; dictionary and π-equivariance.  
**Context search:** Picard|quasi-unipot|modérée|wild|prime-to. **Comparison:** RS “Orientation for this package”, question 4, and FLAGGED_149 B9 [Open, return’s claim], reported cote 149 §1, manuscript p.17, scans 35–36; Hua’s tame-inertia remark in “Les triangles de la fibre de Milnor” adds a hypothesis absent from the witness.

The pages encode a π-action and derived invariants, but contain no Picard–Lefschetz formula, quasi-unipotence assertion, or explicit separation of tame and wild monodromy. The generic-fibre dictionary therefore supplies an object-level analogy, not the prime-to-p versus p-primary comparison required by B9. No step towards that open row can be claimed from these scans alone.

### RN044 — Dating and publication comparisons support a milieu, not a source identification

**Kind:** reading question. **Witness:** 122.pdf, scan 018:L22–28 and handwritten scans 013, 017, 020, 028.  
**Context search:** 1968|1971|SGA|datation. **Comparison:** README’s archival dating; RS “Orientation for this package”, question 5; Hua, “Le dossier, sa charpente et ses notations”; supports compatibility, not exact dating. **External comparison:** [Milnor68] bibliographic record; [SGA7-I] publisher’s title and dates.

The reused announcement says “jeudi 25 Avril 1968”, and the supplied archival description places the undated notes around 1968–1971. Milnor’s book appeared in 1968, while the publisher identifies SGA 7 I with the 1967–1969 seminar and a 1972 volume. These facts make a common mathematical setting plausible, but neither the announcement nor the thematic parallel dates the composition or proves that this is a draft of a particular SGA exposé.

## 5. The final finiteness warning

### RN045 — The warning concerns cokernels, and its categorical notation is still uncertain

**Kind:** self-flagged. **Witness:** 122.pdf, scan 035:L2–3; opening paragraph.  
**Context search:** conoyau|noyau|AB5|finitude. **Comparison:** Hua, “Un autre sujet : finitude et noyaux (page 34)”; reverses the stability directions and supplies Ext notation not secured here; RS has no directly matching result.

The paragraph says that natural finiteness conditions on the inductive systems “ne semblent pas stables par conoyaux”, and dually that the artinian conditions “ne semblent pas stables par noyaux”. Hua reverses those directions and reads Ext where the frozen witness has unsure adⁿ|ad° with uncertain remaining arguments. This is an expressed suspicion, marked “!!”, whose category and finiteness condition must be defined before it becomes a testable closure statement.

### RN046 — The proposed counterexample is entirely cancelled and ends at Q=

**Kind:** withdrawn in the same text. **Witness:** 122.pdf, scan 035:L5–9; lower half, with the warning at L2–3 on the same scan.  
**Context search:** Exemple|régulière|Q =|finitude. **Comparison:** Hua, “Un autre sujet : finitude et noyaux (page 34)”; agrees on cancellation and the unfinished Q; no direct RS result.

The example begins with a noetherian ring, two elements f,g and an M-regularity condition, then displays P=M_f/M and its direct-limit presentation. The whole block is struck through and stops at “Q=”. It is therefore evidence for a construction Grothendieck considered, not a completed counterexample to either closure property.

### RN047 — The surviving algebraic calculation can be checked in ordinary modules

**Kind:** own idea. **Witness:** 122.pdf, scan 035:L5–7; cancelled direct-limit display.  
**Context search:** cohomologie locale|M_f|injectifs|régulière. **Comparison:** Hua, “Un autre sujet : finitude et noyaux (page 34)”, final footnote; credits its local-cohomology suggestion and supplies a restricted check; no directly settled RS entry. **Confidence:** high in ordinary modules over a commutative noetherian A, with f injective on M; not a definition of the unclear category C. **External comparison:** [Stacks0952], Lemma 47.9.1.

The maps M/fᵐM→M/fⁿM given by fⁿ⁻ᵐ are injective when f is M-regular, and the compatible map sending a residue class of m to m/fⁿ identifies their colimit with M_f/M. The principal-ideal Čech complex identifies this quotient with H¹_(f)(M), while its degree-zero support group vanishes under that regularity assumption. This verifies the displayed P calculation in a specified setting without completing the deleted example.

### RN048 — Multiplication by g is a useful test, but does not supply the missing counterexample

**Kind:** own idea. **Witness:** 122.pdf, scan 035:L5–8; regular pair and missing Q.  
**Context search:** multiplication|régulière|contre-exemple|finitude. **Comparison:** Hua, “Un autre sujet : finitude et noyaux (page 34)”, final footnote; follows its suggested g test but limits the conclusion; no direct RS entry. **Confidence:** high for the module calculation, low for its identification with the author’s intended Q, because Q and the finiteness class are absent.

If g is injective on M/fM and f is M-regular, the filtration by powers of f shows g is injective on every M/fⁿM and hence on P. Its cokernel is the colimit of M/(fⁿM+gM), so the obvious multiplication-by-g experiment still has an explicit presentation of the same general form. It does not by itself exhibit failure of a finiteness property, and it gives no warrant to write a formula after the manuscript’s unfinished Q=.

## 6. Reused texts: separate witnesses and research leads

### RN049 — Reused material must not be attributed to the singularity argument

**Kind:** reading question. **Witness:** 122.pdf, scans 004, 006, 008, 010, 012, 014, 016, 018, 021, 023, 025, 027, 029, 031, 033.  
**Context search:** reused|dactylograph|autres mains|quotient. **Comparison:** Hua, “Le dossier, sa charpente et ses notations”, explicitly omits these texts; RS MPL_136_095-141 §1.5 and MPL_136_189-234 R008 [first-pass leads] warn of analogous reused-material distinctions in cote 136.

The typed “dual torique” exercises and the English “counter-examples” section are different texts carried on reused faces. Their themes can suggest comparisons, but their presence is not evidence that Grothendieck applied those results to the handwritten singularity notes. This package adds their full content to the record where Hua’s reading deliberately passes them over.

### RN050 — The Hensel instruction needs a restriction on n

**Kind:** own idea. **Witness:** 122.pdf, scan 004:L5–9; exercise 7(a).  
**Context search:** Hensel|valuation|uniformisante. **Comparison:** no matching argument in the supplied context; Hua omits the reused exercise, and RS LM1 D.11 is an unrelated arithmetic-descent problem. **Confidence:** high; the Frobenius calculation is elementary and directly tests the printed parenthesis.

The instruction says that xⁿ=1+z has a solution “pour tout n>0” by Hensel’s lemma. In K=𝔽_p((t)), with z=t and n=p, every pth power has only exponents divisible by p, so 1+t is not a pth power. This refutes the unrestricted auxiliary instruction, not necessarily the exercise’s conclusion about u: using sufficiently many n prime to the residue characteristic may still supply the required divisibility argument.

### RN051 — Purity and countability are substantive hypotheses in the splitting exercise

**Kind:** unproved claim. **Witness:** 122.pdf, scan 008:L7–17; exercise 6(a)–(f).  
**Context search:** pur|valuation|dénombrable|compact. **Comparison:** no direct corresponding theorem in RS; Hua omits the reused text.

“Montrer que” introduces a chain from the principal-ideal test for purity to simultaneous choices of representatives and splitting into rank-one modules. The countable-basis condition in part (c), the linear compactness assumptions, and the purity of the finite-rank submodule in part (d) should all be retained if this is pursued as a reusable lemma. The exercise supplies proof hints, not a proof in the handwritten argument, and offers no stated extension to arbitrary rank.

### RN052 — Completeness and linear compactness are deliberately separated

**Kind:** unproved claim. **Witness:** 122.pdf, scans 006:L14–18, 010:L5–17, 008:L5; printed pages 42–44 in their textual order.  
**Context search:** complet|linéairement compact|valuation|Hahn. **Comparison:** no direct match in the supplied results register; Hua omits these faces.

The reused exercises request both a complete topological field that is not locally rétrobornée and a field K₀ with the same value group and residue field as a larger series field but without its linear compactness. The sentence ending on scan 010 continues at the top of scan 008, confirming that PDF scan order is not the exercise text’s reading order. These are potential counterexample templates for overstrong completeness claims, but no link from them to the final adic-system warning is stated.

### RN053 — The toric-dual exercise needs its omitted conventions before importing it

**Kind:** reading question. **Witness:** 122.pdf, scans 004:L21, 012:L6–16; exercise 9 across printed pages 45–46.  
**Context search:** dual torique|K/A|artinien|noethérien. **Comparison:** Hua omits this text; RS LM7 C.1 [Known, return’s claim] concerns a Picard 1-motive duality, not this Hom(M,K/A) construction; RN045 offers only a possible future comparison.

The phrase “tout A-module monogène” embedding in K/A cannot include A itself for a nonfield DVR, because K/A is torsion and A is torsion-free. A torsion qualification may be missing from the typescript, but it is not inserted into the transcription. Its “rang un” convention also lists K/A and A/πʰA, so the ordinary rank over the fraction field cannot be assumed without recovering the referenced definition.

### RN054 — The separatedness hint has the opposite membership sign from the needed argument

**Kind:** reading question. **Witness:** 122.pdf, scan 016:L17; exercise 10(e), with scan 014:L5–9 continuing the exercise.  
**Context search:** séparé|orthogonal|dual torique|topologique. **Comparison:** no direct corresponding statement in the supplied context; Hua omits the reused text.

The hint for finding a continuous character nonzero on x says to choose an open submodule U “tel que x∈U”. The usual separatedness argument requires an open submodule excluding x, so that x survives in M/U before applying the dual. This makes x∉U a proposed correction to the printed hint, not a reading silently substituted for its visible membership sign.

### RN055 — The Hironaka example has a category-sensitive quotient conclusion

**Kind:** unproved claim. **Witness:** 122.pdf, scan 029:L13 and scan 033, Figure 7; printed p.4.12 and its figure.  
**Context search:** Hironaka|quotient|represent|construction. **Comparison:** RS MPL_131 RN001 and MPL_131 §2 [first-pass leads], reported construction/representability criteria; Hua omits this text; adds a separate obstruction example, not a counterexample to any stated criterion in RS.

The typed text constructs V₃ by blowing up two conics in opposite orders near P₁ and P₂, then attributes failure of a geometric quotient by ℤ₂ to Hironaka. The category of the proposed quotient and the hypotheses of the cited earlier results must be fixed before comparing this with representability or descent criteria. The surviving figure and paragraph do not justify replacing that claim by a statement about quotients in every enlarged category.

### RN056 — Properness of an action is contrasted with existence of its geometric quotient

**Kind:** unproved claim. **Witness:** 122.pdf, scans 031:L10 and 029:L3–11; printed pp.4.11–4.12.  
**Context search:** Nagata|proper|quotient|stable points. **Comparison:** no direct RS theorem matches this example; RS MPL_131 §2 is a representability lead only; Hua omits the reused text.

The section announces proper SL(n)-actions on quasi-projective schemes with no geometric quotient, then gives Nagata’s open set of plane quintics with four explicit exclusions. Its proof is referred to the preceding section and the bibliography rather than given on the retained leaves. The closing contrast between algebraic stable points and analytic quotients is therefore a separate typed-text research lead, not a conclusion of the local-singularity manuscript.

### RN057 — “A local computation” leaves the resolution charts unavailable here

**Kind:** unproved claim. **Witness:** 122.pdf, scans 027:L3 and 025:L5–16; printed pp.4.13–4.14.  
**Context search:** local computation|blowing|transform|singularities. **Comparison:** no direct supplied-context proof; Hua omits the reused text; the EGA 2 reference is present in the source but its text was not supplied or used to repair this witness.

“One verifies readily” identifies line centres and blow-ups, followed by “A local computation shows” that four singular lines are resolved into ruled surfaces. To validate the construction one would need local equations for the birational joint, the ideal of H₄, and the relevant blow-up charts, then check the claimed orbit spaces on the exceptional pieces. The figure supports the intended geometry but cannot replace those computations.

### RN058 — The involution relation changes form across adjacent printed pages

**Kind:** reading question. **Witness:** 122.pdf, scans 025:L18–20 and 021:L4; printed pp.4.14–4.15.  
**Context search:** semi-direct|sigma|involution|linearization. **Comparison:** no matching relation in the supplied context; Hua omits these faces; LM4 D.12 concerns different profinite torsion questions.

The relation on p.4.14 contains an unsure extra minus before α⁻¹, whereas p.4.15 writes σα=α⁻¹σ. Before interpreting this as an inconsistency, one must decide whether the mark is a sign and whether the formulas use scalar representatives of projective transformations or the abstract torus parameter. It supplies no information about the profinite involutions in LM4 D.12.

### RN059 — The linearisation step is stated briefly, and the induced construction breaks off

**Kind:** unproved claim. **Witness:** 122.pdf, scan 021:L6–14; printed p.4.15.  
**Context search:** linearization|linearisation|very ample|PGL. **Comparison:** no direct supplied-context argument; Hua omits the reused text; RS MPL_131 RN001 is only a general construction-technique comparison.

“It is easy to check” asserts a G-linearisation on σ*Lⁿ⊗Lⁿ, after which a PGL-associated construction is defined by its geometric points. A proof would check the semidirect-product cocycle, the locally closed subscheme structure, and the quotient comparison; the retained page ends at “Then one sees easily that a”. No missing continuation or final quotient conclusion is reconstructed as if it were present.

### RN060 — Figures 7 and 8 are witnesses, but the earlier cited diagrams are absent

**Kind:** reading question. **Witness:** 122.pdf, scans 023 and 033; references in scans 027:L3, 025:L14, 029:L13, 031:L6–8.  
**Context search:** figure|diagramme|reused|dactylograph. **Comparison:** Hua’s “Le dossier, sa charpente et ses notations” excludes these reused pages; no direct RS entry.

The retained Figure 7 belongs with the opposite-order blow-ups and Figure 8 with the birational-joint and ruled-surface construction. The references to Diagrams 5 and 6 on printed p.4.11 have no corresponding supplied figures. Their absence limits verification of the stability-function discussion and must not be filled with a drawing inferred from the formulas.

### RN061 — A modern affine cohomological bound is a conditional algebraic comparator

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 028:L40–41 and 030:L26–30; complement and fibre bounds.  
**Context search:** affine|Lefschetz|cohomological|S19. **Comparison:** README’s S19 planning pointer; Hua, “Les annulations”; RS MPL_33_002-049 §2 records an earlier print/Stacks comparison programme, not a theorem for this M. **External comparison:** [Stacks0F0P], Proposition 59.95.6 and Lemma 59.95.2.

The Stacks Project gives cd(X)≤dim(X)+cd(k) for a finite-type affine scheme over a field, and a bound for directed limits with affine transition morphisms. If the intended geometric fibre can be placed in that setting over a separably closed field, this supplies a route to the n-dimensional torsion-cohomology bound. The scans do not supply those identifications, so the reference tests a precise possible completion rather than proving the unspecified “passage à la limite”.

## 7. Disposition of the supplied research questions

### RN062 — LM7 E.23: no arithmetic section map is calculated

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 020:L7–18 and 024:L13–22; derived π-invariants.  
**Context search:** E\.23|metabelian|section classes|Gamma. **Comparison:** RS, “Open items”, line 349, **LM7 E.23 [Open, return’s claim]**; source LM7_FERMAT_TOWER_results.csv, §51.16, folios 733v–736v, scans 172–178, formulas (369)–(379); status unchanged.

“Dans catégorie dérivée de Λ[π]” provides equivariant cohomology, but identifies neither the metabelian arithmetic quotients of U₃/ℚ nor their section map to E.16. The images and fibres requested by E.23 are not computed, so this is a thematic comparison rather than a proof, counterexample, or new case of that row.

### RN063 — FLAGGED_149 B9: the possible prime-to-p connection remains unmade

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 022:L16, 026:L14, 034:L21–24; algebraic proof request, coefficients, isolated singularity.  
**Context search:** B9|prime-to|p-primary|finite field. **Comparison:** RS, “Open items”, line 350, **FLAGGED_149 B9 [Open, return’s claim]**; source FLAGGED_149_results.csv, cote 149 §1, manuscript p.17, scans 35–36; RS orientation line 15 proposes the possible connection.

“À [unsure prouver] dans le cas algébrique” and “coefficients généraux” do not specify the compatible p-primary point differences on prime-to-p covers required by B9. The manuscript therefore leaves that selected Open status unchanged. RS’s newer ANABELIAN_SUCCESSOR A.3 claim concerns a more specific finite-field point-section result and is only partly checked there; it is not a reason to turn cote 122 into a proof of the broader B9 formulation.

### RN064 — LM1 D.11: a torus with an involution is not an integral classification

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 021:L4 and 025:L20; reused semidirect-product construction.  
**Context search:** D\.11|mu_2|integral|semi-direct. **Comparison:** RS, “Open items”, line 351, **LM1 D.11 [Open, return’s claim]**; source LM1_GROUP_SCHEMES_results.csv, supplied locator “49; 608–609; 610; task D.c integral classification”; status unchanged.

The reused text gives “the semi-direct product” of G_m and ℤ₂ with an inversion relation. It supplies no mixed-characteristic model, arithmetic descent argument, or integral μ₂-extension classification at 2. The shared presence of a torus and order two is insufficient to identify it with D.11.

### RN065 — LM4 D.12: the reused involutions are not identified with GT torsion

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 025:L20 and 029:L13; reused order-two automorphisms.  
**Context search:** D\.12|torsion|GT_0|involution. **Comparison:** RS, “Open items”, line 352, **LM4 D.12 [Open, return’s claim]**; source LM4_FINITE_GROUP_ACTIONS_results.csv, §25 bis, folios 157v–160, scans 312–317, and §30, folio 194v, scan 384; status unchanged.

“An automorphism … of order 2” occurs in the quotient construction, not as an element of the full profinite GT₀ or a low-type mapping-class group. No peripheral system or torsion-conjugacy calculation is supplied here. These examples therefore do not alter D.12 or its reported finite-recognition counterexample D.29.

### RN066 — LM4 F.7: quotient failure does not compute a profinite centralizer

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 029:L11–13 and 031:L10; reused proper actions and quotients.  
**Context search:** F\.7|centralizer|normalizer|A_5. **Comparison:** RS, “Open items”, line 353, **LM4 F.7 [Open, return’s claim]**; source LM4_FINITE_GROUP_ACTIONS_results.csv, §30, folios 194–196, scans 383–387, Parts D(b) and F(b); status unchanged.

The assertion that SL(3) “acts properly” on a quintic locus addresses a geometric quotient question. It does not identify a geometric A₅ subgroup, its centralizer, or the comparison with a mapping-class-group completion required by F.7. No new case of the nonsolvable comparison is established by these leaves.

### RN067 — WG H2: local vanishing-cycle language needs an arithmetic comparison map

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 017:L2–15, 020:L4–7, 034:L21–22; dictionary, π-action, “singularité isolée”.  
**Context search:** WG H2|limit action|vanishing cycle|conjugacy. **Comparison:** RS, “Questions of our planning document”, line 459, **WG H2 [hunch, Believe; unchecked]**; source WARGAME_MATH_HUNCHES_20261112.md; Hua, “Résumé”, supplies vanishing-cycle search terminology.

The local degeneration makes monodromy and vanishing cycles natural topics for a future comparison with H2. The pages do not identify its profinite limit action or an invariant conjugacy class under an open arithmetic Galois subgroup of a smooth proper hyperbolic curve. Neither part of that hunch is proved or refuted here.

### RN068 — EXIT_TOWER B.27: a shared gluing method, without a finite groupoid model

**Kind:** unpursued implication. **Witness:** 122.pdf, scans 013:L4–41, 015:L24–29, 017:L17–31; gluing diagrams.  
**Context search:** B\.27|groupoid|colimit|boundary. **Comparison:** RS, “Headline results … / EXIT_TOWER”, lines 42–44, B.27 [presented as a settled return claim]; reported finite-groupoid colimit for surfaces with boundary; Hua, “La construction”, gives the open-book model.

The handwritten gluing “suivant leurs bords” supplies spaces, inclusions, and fibrations whose homotopy invariants could be compared with a groupoid construction. The diagrams themselves are cohomological and geometric, not the finite diagram of finite groupoids claimed in B.27. No reproof or extension of that registered result is offered; a future comparison would have to specify the groupoid functor and its descent maps.

### RN069 — The étale twist in Hua needs a convention check

**Kind:** own idea. **Witness:** 122.pdf, scans 022:L20–26 and 020:L11–18; untwisted derived dual and ambiguous parentheses.  
**Context search:** torsion|Tate|dualité|Lambda. **Comparison:** Hua, “L’application u”, footnote at supplied line 603, says an étale twist (n) is added; its “Les triangles de la fibre de Milnor” already supplies tame-inertia twists; no direct RS result. **Confidence:** high as conditional bookkeeping under the stated trace and dual conventions, not as a recovered manuscript assertion.

With K=RΓ(M,Λ), K∨=RHomΛ(K,Λ), and the trace convention RΓ_c(M,Λ(n))[2n]→Λ, the duality formula reads RΓ_c(M,Λ)≃K∨(−n)[−2n]. Thus Hua’s isolated addition of (n) requires checking which side of the duality is being twisted. The manuscript does not specify that étale convention, so this is a check on reuse of the interpretation rather than a correction of its frozen formula.

### 7.1. Closest earlier results and package leads

These entries are cited at the level actually supplied by RS. The underlying files and earlier scans were not included in the context archive.

| Entry and supplied status | Exact RS location; reported source and earlier locator | What cote 122 adds or leaves unchanged |
|---|---|---|
| MPL_33_147-181+34_002-017 D21 — first-pass observation lead | “Research notes …”, line 436; MPL_33_147-181+34_002-017_notes.md; 33/166:L6–18 | Concrete algebraic proof request, dual-invariants check, and adic finiteness concern; RN018, RN027, RN045 |
| MPL_11_002-042 O06 — first-pass observation lead, own idea/unpursued implication | Same section, line 445; MPL_11_002-042_notes.md; 11/017, 027, 034, 042 | Particular boundary-duality and coefficient setting, not a proof of the earlier Künneth/Poincaré programme; RN002, RN006, RN013 |
| MPL_11_043-058+56 N045 — first-pass lead, unproved claim | Same section, line 446; MPL_11_043-058+56_notes.md; 56/020, middle table | A concrete compact-to-ordinary map, with no identification of the prior uncertain target or norm 2; RN013 |
| MPL_60_002-035 F48 — first-pass reading/implication lead | Same section, line 443; MPL_60_002-035_notes.md; 60/035, lower margin | Degree-duality analogy, no new height construction; RN016, RN024 |
| MPL_60_002-035 §2 and MPL_60_036-070 §2 — first-pass observation leads | Same section, lines 421, 430; corresponding notes files; reported 60/003–035 and 037–061 | Boundary corrections and duality are shared topics, but no determinant L-function is identified here |
| MPL_131 RN001 and §2 — first-pass construction/representability leads | Same section, lines 433–434; MPL_131_notes.md; RN001 reports 131/002:L13 and 131/017:L25 | The reused quotient examples suggest category-sensitive comparisons; no representability criterion is proved or refuted; RN017, RN055 |
| MPL_136_095-141 §1.5 and MPL_136_189-234 R008 — first-pass reused-text leads | Same section, lines 423, 435; corresponding notes files; 136/103, 107 and the listed 189–234 reused faces | Supports separating reused typescripts from the principal handwritten argument; RN049 |
| LM7 C.1 — Known, return’s claim | “Settled in our registers”, line 375; LM7_FERMAT_TOWER_results.csv; §51.13–14, folios 719–724, scans 143–153, (299)–(323) | No comparison between its Picard 1-motive and the present boundary complex is constructed; RN014, RN019, RN053 |
| FLAGGED_149 F17.1 — Known, return’s claim; F17.7 — Proved, return’s claim | Same section, lines 359, 374; FLAGGED_149_results.csv; cote 149 §3, manuscript pp.49–51, scans 100–103, especially 101–103 | Potential future monodromy/reduction comparators; no nonabelian good-reduction criterion is obtained here |
| LM7_PUSH E.64 — Proved, expressly limited referee check; E.67 — Proved, general statements refereed but 48 per-word fibres not recomputed | Same section, lines 360–361; LM7_PUSH_results.csv | No identified application to cote 122; the record’s review limitations remain in force |
| GALOIS B.13 and STRATA A.6 — Open rows in the run inventory | “Our runs …”, lines 188–190 and 277–279 | Accessibility or unrestricted-coefficient vocabulary is too broad to turn scan 035 into an answer; no common category or comparison is specified |
| FINMON and S2COUNT headline claims | “Headline results …”, lines 81–87 and 104–107 | “Finitude” in scan 035 does not mean finite-category or finite-monoid realisation of a homotopy type |

The detailed return claims about Fermat curves, sections over ℚ, norm maps, Selmer images, and GT actions are not rederived. No map from the objects on these pages to those arithmetic constructions is specified in the retained text or the supplied excerpts. This bounded lack of a direct application agrees with RS’s own orientation, while retaining the positive methodological comparisons above.

### 7.2. Every displayed war-game planning row

The two WG entries below are **hunches labelled “Believe; unchecked”**, from WARGAME_MATH_HUNCHES_20261112.md. The six WG2 entries are **round-2 questions or plans, unchecked**, from PROGRAM_WARGAME_ROUND2_20261112.md. These eight are all the entries actually displayed under RS’s heading “8 of 10 matching entries”; no content is invented for the two unprovided matches.

| Exact planning ID | RS line | Disposition from the retained scans |
|---|---:|---|
| WG H9 | 452 | The pairings on 024 and local Lefschetz on 028 do not identify the proposed Néron–Tate/Mordell–Weil lattice formula for cycles in a Lefschetz pencil; neither proof nor refutation |
| WG2 §1.1 #3 | 453 | The Book II organisation around cotes 16, 44, 47, 54 receives a distinct local-singularity dossier, not an additional motive/Jacobian/abelian-variety theorem |
| WG2 §2.1 #2 | 454 | No grading projectors πᵢ or universal ring ℤ[L₀,Λ₀] is present; the coefficient Λ and “Lefschetz local” are different data |
| WG2 §1.1 #2 | 455 | The derived map u is not identified with a Fourier functor, universal vector extension, or height-bearing Pⁱ(X) |
| WG2 §2.3 #12 | 456 | No algebraic representative Zⁱ_alg/Zⁱ_alb, polarization, dimension bound, or complementary-cycle height formula is constructed |
| WG2 §2.3 #13 | 457 | No verification of the later existence/descent literature on algebraic representatives; reused linearisation and adic finiteness are different subjects |
| WG2 §Summary #2 | 458 | No new correspondence-algebra or abelian-scheme result for that synthesis; the positive addition is the local duality programme and its unfinished checks |
| WG H2 | 459 | Monodromy supplies a possible future comparison only; no arithmetic invariant conjugacy class or exclusion theorem; RN067 |

### 7.3. Answers to the five cote-specific orientation questions

| RS orientation question | Answer |
|---|---|
| Is the fibration proved, assumed, analytic, algebraic, or étale? | The differentiable bundles and gluing data are assumed on 013–015. The algebraic dictionary is explicit on 017, and an algebraic proof is deferred on 022. RN009, RN011, RN018 |
| Six terms, u, and a homology-sphere/unimodularity criterion? | A live middle sequence exists on 032, with an unproved surjectivity label; its final version is cancelled. The conditional unimodular criterion concerns W₀, requires stronger fibre vanishing and integral hypotheses, and is not stated here. RN038–RN040 |
| Do the duality degrees agree? | The −2n/−2n−1 change and λ/μ degree sums are consistent under the stated model; the successor exponent, overwritten bounds, coefficient duals, and signs still need the distinctions recorded in RN006, RN019, RN021–RN024, RN031, RN036–RN037, RN069 |
| Picard–Lefschetz, quasi-unipotence, characteristic p, or ℓ-adic variant? | No such theorem is stated. π-equivariance alone does not establish one; the tame-inertia twist is Hua’s supplied interpretation. RN015, RN043 |
| Relation to Milnor 1968 and SGA 7 dating? | The thematic comparison is strong and the dates compatible; no exact draft/source identification or composition date follows. RN035, RN044 |

## 8. Standing question: steps expressly marked as unverified

The first table records the manuscript’s own doubt, demand for proof, or deferred identification. It does not promote every abbreviated proof, overwritten exponent, or editorial unsure mark into an authorial question. The second table records associated unfinished work and revisions whose status is also material.

| Scan and frozen locator | Source words or mark | What remains unverified |
|---|---|---|
| 007:L35 | “n’est sans doute autre que la suite exacte de Mayer-Vietoris” | Identification of the support sequence with Mayer–Vietoris, including maps and sign; RN005 |
| 011:L24, in cancelled rotated block | “≃ ?” | Support/compact-support comparison in that abandoned diagram; RN007 |
| 022:L15 | “qu’on aura à identifier” | Identification of u₀ with the canonical isomorphisms; RN017 |
| 022:L16, slanted margin | “à [unsure prouver] dans le cas algébrique” | Algebraic counterpart of the comparison; reading of “prouver” remains uncertain; RN018 |
| 022:L42 | “sont transposés l’un de l’autre (signe ?)” | Transposition sign for ρ,ρ′; RN021 |
| 024:L11 | “dire que c’est encore un triangle autotransposé” | An instruction to state the self-duality after forgetting the action; not itself a written proof |
| 024:L14 | “[expliquer comment ?]” | Passage to triangle (b′); RN022 |
| 024:L22 | “vérifier la commutation de RΓ^π à RHomΛ(−,Λ)” | Shifted duality/invariants compatibility and its functorial maps; RN022–RN023 |
| 035:L3 | “ne semblent pas stables par conoyaux”; dually “ne semblent pas stables par noyaux” | Suspected failure of closure of the stated finiteness conditions; RN045 |

| Scan(s) | Unfinished or withdrawn material | Status |
|---|---|---|
| 003:L49–53; 005:L2–10; 009:L3–27 | Abandoned collar/comparison arrows and five-lemma argument, followed by live excision | The later live route is distinguishable from the rejected attempt; RN003, RN007 |
| 017:L89–91 | “40 … suites exactes”; “Cela fait 80 suites exactes, mais” | Enumeration stops at its qualification; RN012 |
| 024:L25–30; 026:L12–14 | Abandoned formulations followed by the explicit (d),(e) transpose pair | Later live text supplies the intended pair; RN025 |
| 026:L24–25; 028:L2–14 | Cancelled top-degree sequence followed by a replacement and connectedness condition | Revised argument, not two independent conclusions; RN028 |
| 024:L47–48 | “je dis que c’est β”; “je dis que c’est α” | Asserted identifications without an accompanying proof or explicit doubt marker; RN024 |
| 030:L26–30 | “par passage à la limite” | A claimed argument without its system or comparison maps; no question mark is attached; RN033 |
| 032:L24–31 | Final middle-degree sentence and diagram cancelled | Withdrawn synthesis; earlier live sequence remains; RN039 |
| 035:L5–9 | Cancelled “Exemple”, ending “Q=” | No completed counterexample; RN046 |

The reused English text also leaves computations to the reader: “one verifies readily” (027:L3), “A local computation shows” (025:L5), and “it is easy to check” (021:L6). These are proof obligations in a separate typed text, not handwritten self-flags in Grothendieck’s singularity argument. The French exercise pages repeatedly say “Montrer que”; their exercise status should likewise be retained rather than reclassified as his conjectures.

## 9. Standing question: title sheets, numbering, and page counts

### 9.1. What is actually present

No retained face is a cover or handwritten title sheet, and none states a total such as “32 pages” or “Pages 1–34”. The title **“Point singulier isolé de la fibre : notes manuscrites (s.d.)”** and the approximate 1968–1971 date are supplied archival metadata, not a heading found on these scans. The inventory’s 17 text / 15 reused_typed classification describes supplied faces; whole-leaf counts and the original order of a bound text cannot be inferred from it.

There are 34 archive scan numbers in the requested interval 002–035, of which 002 and 019 were supplied as omitted blank pages, leaving 32 image faces. The three image versions per face are one full image and two overlapping halves, not additional pages. The small sheet numbers and the printed pagination belong to different numbering systems; their authorship is not established by using the required mspage macro.

| Archive scan | Small sheet/page mark in the frozen witness | Separate printed page or heading |
|---:|---|---|
| 003 | 2 | — |
| 004 | 3 | −45−; n° 387 |
| 005 | 4 | — |
| 006 | 5 | −42−; n° 387; §5 |
| 007 | 6 | — |
| 008 | 7 | −44−; n° 387 |
| 009 | 8 | — |
| 010 | 9 | −43−; n° 387 |
| 011 | 10 | “Récapitulation” is an internal heading |
| 012 | Uncertain marginal W or 11; not confidently treated as a numeral | −46−; n° 387 |
| 013 | 12 | — |
| 014 | 13 | −48−; n° 387 |
| 015 | 14 | — |
| 016 | 15 | −47−; n° 387 |
| 017 | 16 | Counts 40 and 80 concern exact sequences, not pages |
| 018 | 17 | Efimov lecture announcement; title and date below |
| 020 | 19 | Lettered triangles (a)–(d), not page counts |
| 021 | 20 | −4.15− |
| 022 | 21 | Triangle (e) and (a′) |
| 023 | 22 | Figure 8 |
| 024 | 23 | Triangles (c′), (b′) |
| 025 | 24 | −4.14− |
| 026 | 25 | — |
| 027 | 26 | −4.13− |
| 028 | 27 | “Lefschetz local” is an internal heading |
| 029 | 28 | −4.12− |
| 030 | 29 | — |
| 031 | 30 | −4.11−; boxed §3 |
| 032 | 31 | — |
| 033 | 32 | Figure 7 |
| 034 | 33 | — |
| 035 | 34 | “Inconvénient sérieux”; cancelled “Exemple” |

### 9.2. Titles and text-specific sequences

| Witness | Title or numerical evidence | Interpretation and limit |
|---|---|---|
| 018:L2–28 | Faculté des Sciences / Institut Henri Poincaré; N. EFIMOV; “LE PROBLEME DES IMMERSIONS HYPERBOLIQUES”; first lecture “jeudi 25 Avril 1968”, 14 heures, salle 116 | A printed announcement, not a title or date of the handwritten singularity notes |
| 006:L4; reused French pages | §5, n° 387, printed pages 42–48 | A seven-page exercise sequence distributed as 006→010→008→004→012→016→014; n° 387 is not asserted to be a page count |
| 031, 029, 027, 025, 021 | Printed pp.4.11–4.15, in reverse PDF scan order | A distinct English text; §3 begins on 4.11, without an overall book or chapter title on the retained faces |
| 033 and 023 | Figure 7 and Figure 8 | Figure numbering for the reused English construction, not pagination |
| 017:L89–91 | 40 and 80 | Counts of exact sequences, explicitly unfinished, not a count of sheets |
| Hua’s front matter | Editorial pages{1}{34}, archival folder title and dating | Metadata in the interpretation, not an additional title sheet or source page-count statement |

## 10. Primary comparisons and verification limits

The following public sources were consulted **after** the transcription freeze. They were used to delimit possible mathematical completions and publication context, never to repair the diplomatic text. The individual note, not a broad bibliographic resemblance, states what each comparison supports.

| Key | Primary source and precise inspected scope | Use and limitation |
|---|---|---|
| **Milnor68** | Milnor, J. (1968), *Singular Points of Complex Hypersurfaces*, Annals of Mathematics Studies 61, Princeton University Press; [publisher-hosted JSTOR record and chapter excerpts](https://www.jstor.org/stable/j.ctt1bd6kvv); original-book text available in a [digital reproduction](https://djvu.online/file/kCFrJq27uCPRi), §§4–6, Theorems 5.1, 5.2, 6.5 | RN035’s theorem comparison and RN044’s publication date; the digital reproduction’s extracted text is imperfect, and this was a theorem-level comparison, not a collation of the entire book |
| **Stacks0F0P** | The Stacks Project, [§59.95, tag 0F0P, “Cohomological dimension”](https://stacks.math.columbia.edu/tag/0F0P), especially Lemma 59.95.2 and Proposition 59.95.6 | RN061’s affine and limit bounds; does not identify the manuscript’s geometric fibre or limit system |
| **Stacks0952** | The Stacks Project, [§47.9, tag 0952, “Local cohomology”](https://stacks.math.columbia.edu/tag/0952), Lemma 47.9.1 | Principal-ideal Čech model used conditionally in RN047; does not settle the undefined adic finiteness category |
| **SGA7-I** | Deligne, P., Raynaud, M., Rim, D. S., Grothendieck, A., and Raynaud, M., *Groupes de monodromie en géométrie algébrique I*, Lecture Notes in Mathematics 288; [Springer publisher record](https://link.springer.com/book/10.1007/BFb0068688), subtitle, contents, and bibliographic dates | RN044’s seminar/publication chronology only; no particular SGA theorem or textual dependence was verified |

The README invokes S19 without supplying its complete text; the bounded print/Stacks comparisons above answer the available instruction without inventing a fuller questionnaire. No claim of novelty, historical priority, or identification with a particular published draft is made. In particular, the SGA 2, SGA 4, Gabber, Andreotti–Frankel, and Winkelnkemper comparisons mentioned by Hua were not independently established here and are not used as proof of an unrestricted algebraic statement.

The separate work audits record checks of the supplied results register, Hua’s interpretation, and the conditional mathematics. They are research-phase checks of the frozen text, not additional palaeographical readers. The transcription’s uncertainties, deletion states, and SHA-256 freeze remain the evidentiary boundary for all these notes.
