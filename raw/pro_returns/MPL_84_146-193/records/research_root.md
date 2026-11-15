# Root research synthesis and literature comparison

This is an intermediate component of the final research notes. The transcription was frozen at 2026-11-15 11:56:21 UTC; the context was opened at 11:56:32 UTC, and its README, entire results-state register, and LM2 table were read before research-note drafting. These notes analyse the frozen transcription and do not change it. The photographs were read and audited by the root in one sequential stream; subsequent parallel work concerns research analysis of that already frozen text only.

## Evidence and scope

The packet contains 24 handwritten mathematical pages (even scans 146–192) alternating with 24 fully transcribed reused typescript pages (odd scans 147–193). The mathematical sequence concerns extensions, χ-trivialisations, duality, tensor comparison maps and quadratic algebras of rank two; the reused text concerns the author's reflective treatment of yin/yang, parental figures, creativity and later revisions of that treatment. Its dates belong to the reused text and cannot by themselves date the mathematical writing on the other sides. Archival pencil numbers 145–192, original typescript pagination, footnote numbers, and dates are separate numbering systems.

The supplied context consists of only `README.md`, `LM2_CONGRUENCE_ROWS.md`, and `notes/RESULTS_STATE.md`; the larger files named inside the last register were not supplied. A register excerpt can establish what an earlier run claimed and what review status was reported, but cannot substitute for examining its omitted proof. In particular, the claim status of each LM2/LM4/LM7 entry remains as stated in that register; no such theorem is upgraded by these notes.

## The requested conic–Azumaya–SO(3) bridge (B12)

### R01 — No explicit use of B12 in this packet

**Source:** `pages/MPL_84_146-193_84_scan170.tex`, upper definition; `pages/MPL_84_146-193_84_scan172.tex`, opening algebra; `pages/MPL_84_146-193_84_scan192.tex`, opening equations; comparison over scans 146–193. **Kind:** reading question / scope finding.

The positive mathematical evidence is “extensions” on scan 170 and the two equations `u_i^2+b_i u_i+c_i=0` on scan 192: this interval develops rank-two extension and algebra constructions, and contains no explicit identification of forms of P¹ with conics, rank-four Azumaya algebras, or ternary quadratic forms. The query for “SO”, “GP”, “conique”, “Azumaya”, “P¹”, “rang 3”, and related forms finds the proposed bridge in `README.md`, under B12, but not as a construction in these pages. This answers the planning question with a negative finding for the supplied interval, not a claim about the rest of cote 84 or the neighbouring cotes 77 and 82. The context labels B12 an unchecked question inferred from folder titles, so these pages change its placement rather than refute the mathematical correspondences themselves.

### R02 — A rank-four tensor product here is not a quaternion algebra

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, upper and middle diagrams, “A₁⊗A₂”; scan 192, defining equations. **Kind:** unpursued implication.

Under the displayed quadratic-algebra interpretation, `A₁⊗A₂` has rank four but is commutative; its centre is the entire rank-four algebra, so it is not the degree-two central Azumaya algebra required by B12 over a nonzero base. The distinction matters because rank alone does not connect this tensor product with a quaternion algebra or a conic. The context search finds “Azumaya” only in `README.md`'s proposed B12, while `notes/RESULTS_STATE.md`, Hua's `84-chi-trivialised-extension-product`, instead concerns the rank-two product; the present observation separates those two leads.

### R03 — What a future B12 identification would need

**Source:** `pages/MPL_84_146-193_84_scan160.tex`, “loc. libres de rang fini” and duality assertion; scan 192, algebra/module displays. **Kind:** own idea. **Confidence:** medium as a search direction, low as an identification of this manuscript's intent.

A further manuscript could connect these rank-two objects to B12 by supplying a regular ternary quadratic form and its even Clifford algebra, or a PGL₂-torsor and its associated conic, but no such connecting datum is written here. Over a field of characteristic different from two, the conic/quaternion/similarity correspondence is treated in Voight (2021, §§5.2–5.5); its hypotheses must be checked afresh before using a scheme or characteristic-two version. The context comparison is `README.md`, B12, which supplies the proposed destination but no map from the extensions on scans 160–192. The confidence is limited because the common folder title is evidence for looking, not evidence for an existing construction.

### R04 — Rank-two module data do not already provide a twisted P¹

**Source:** `pages/MPL_84_146-193_84_scan160.tex`, two extension sequences and duality statement; scan 170, “E₁∨E₂” and “E₁∧E₂”. **Kind:** own idea. **Confidence:** high for the distinction; low for a connection to the author's intended later work.

If an actual rank-two vector bundle E is given, its projectivization and endomorphism algebra provide a split-type projective bundle/Azumaya example, but that construction alone supplies no nontrivial Brauer class. A proposed B12 reading therefore needs descent data or a genuinely twisted object, not merely the symbols E and A in the displayed dualities. Searching the context for “torsor”, “Azumaya”, “P¹” and “extension” gives B12 as an unchecked target and Hua's extension-product claim as the only direct match to these scans; neither supplies the missing identification. The confidence in this caution comes from the distinction between an endomorphism algebra and an arbitrary degree-two Azumaya algebra, not from an interpretation of unclear ink.

## Literature comparisons, separated from manuscript claims

### R05 — The local algebra product has a precise published counterpart

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, “b=b₁b₂”, “c=b₁²c₂+b₂²c₁−4c₁c₂”; scan 192, “u₁*u₂”. **Kind:** unpursued implication / literature identification.

Voight (2016, Construction 3.14, Remark 3.17) gives the same quadratic-algebra law: with his parameters t=−b₁, s=−b₂, n=c₁, m=c₂, his generator w is the manuscript's u+b₁b₂, so his relation w²−b₁b₂w+c=0 becomes u²+b₁b₂u+c=0. This is a precise local comparison, independently checked by the included polynomial calculation, and does not identify the manuscript's entire category of χ-trivialised extensions with that paper's objects. Context: Hua, findings register, `84-chi-trivialised-extension-product`, in `notes/RESULTS_STATE.md`, records a candidate without a located reference; the literature supplies a close known algebraic specialisation, while leaving the stronger all-χ statement to be checked. No priority or novelty conclusion follows from this match.

### R06 — Tensor realization and abstract product must be separated

**Source:** `pages/MPL_84_146-193_84_scan192.tex`, “ça croule si 2=0, b₁=b₂=0” (words partly doubtful in the frozen reading); scan 172, injection qualification. **Kind:** unpursued implication / literature comparison.

The abstract monic quadratic algebra remains free of rank two even when its proposed generator has zero image in A₁⊗A₂; the manuscript's collapse warning concerns that realization. Voight (2016, Remark 3.17) explicitly makes the same distinction, while his Corollary 3.20 constructs the monoid on isomorphism classes. Context: this adds a necessary qualification to Hua's `84-chi-trivialised-extension-product` and to the broad B12 placement in `README.md`, without supplying the categorical coherence omitted from the displayed calculations.

### R07 — Loos is a relevant comparison, not a verified identification

**Source:** `pages/MPL_84_146-193_84_scan170.tex`, “On définit de façon can.” (the abbreviation is doubtful); scan 172, quadratic product. **Kind:** own idea. **Confidence:** medium, because the object classes overlap only in a specialisation established here.

Loos (1996) constructs an associative and commutative tensor product of unital quadratic forms extending the separable quadratic-algebra product, according to the article's primary abstract. Comparing its morphisms, base point and coherence maps with the manuscript's χ-trivialisation would be a concrete next step, but the full article was not inspected here and no equivalence is asserted. Context: Hua's `84-chi-trivialised-extension-product` is the direct candidate to compare; the unchecked conic/SO(3) target B12 is broader and is not proved by this bibliographic match.

### R08 — Binary forms with modules offer a second, different comparison

**Source:** `pages/MPL_84_146-193_84_scan192.tex`, “(x₁*x₂,e₁⊗e₂)” and the accompanying quadratic equation; scan 160, algebra/module pairings. **Kind:** own idea. **Confidence:** medium as a comparison problem, low for an equivalence without further structure.

Wood (2011, Theorems 1.4–1.6 and 2.1) relates line-bundle-valued binary quadratic forms to quadratic algebras with traceable modules over an arbitrary base, with primitive forms corresponding to invertible modules. To compare the manuscript's E with such a module, one must exhibit the algebra action, verify equality of the two trace maps, and specify the line-bundle orientation; a perfect base-module pairing alone does not provide these data. Context: this gives a possible way to formulate the invertibility clause in Hua's `84-chi-trivialised-extension-product`, but the claimed T₀ criterion is not written in the supplied interval and is not identified with Wood's primitivity criterion. The confidence is limited by those missing structures rather than by any claim of novelty.

### R09 — No demonstrated route to the LM2 congruence questions

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, “δ=δ₁δ₂”; comparison across scans 146–193. **Kind:** reading question / context comparison.

The multiplicative discriminant formula is a calculation in quadratic algebras, whereas `LM2_CONGRUENCE_ROWS.md` concerns arithmetic and GT actions on congruence quotients, including the still-open two-coordinate realization problem `LM2 C.d5`. Neither a modular curve X(n), a regular polyhedron over a ring, nor an action of GT is constructed in these pages, so the formula supplies no demonstrated step toward C.d5, `LM2 B.f7`, or `LM2 E.3`. The common vocabulary of determinants, norms, extensions or quadratic data does not establish a map between the problems; B5 remains an unchecked planning bridge here. The other open IDs in `notes/RESULTS_STATE.md` are consequently not reported as settled or advanced by this packet.

### R10 — A research-register claim needs several separate verdicts

**Source:** `pages/MPL_84_146-193_84_scan154.tex`, “une indétermination”; scan 160, “Je dis que”; scan 170, “une application can. d'extensions”; scan 192, collapse warning. **Kind:** reading question / source-claim audit.

The context's only direct entry, Hua's `84-chi-trivialised-extension-product`, combines existence of a product, symmetry/associativity, a split-coordinate formula, an invertibility criterion, and agreement of two constructions in one ellipsized claim. These pages support studying the products and their comparison, but the visible parameter checks and unresolved choices do not establish every one of those assertions, and no T₀/V(χ) criterion occurs in the supplied mathematical pages. Other page ranges cited by Hua are outside this packet, so an absence here cannot refute their content. The component-by-component audit in the final notes therefore distinguishes local evidence, conditional calculations, and claims still requiring the missing passages or a proof.

### R11 — A local rank-one groupoid has a multiplication without division

**Source:** `pages/MPL_84_146-193_84_scan146.tex`, coordinate changes; scan 164, complementary matrices; scan 170, χ-trivialisation identities. **Kind:** own idea. **Confidence:** high for this declared local model, because the laws are verified as polynomial identities; identification with a global manuscript category remains conditional.

With fixed trivial rank-one ends, write π=(χ,τ), ϖ=(−τ,χ)ᵗ and represent a change of splitting by an arrow a:τ→τ+χa; the product of objects τ,σ is τσ, and the product of arrows a,b has coordinate aσ+τb+χab. The target, composition, associativity, symmetry and unit laws are polynomial identities over the integers, verified in `records/recompute_chi_groupoid.py` and explained in `records/chi_groupoid_derivation.md`, so this local construction is a strict symmetric monoidal groupoid with unit object 1. Context: this gives a positive local mechanism for the all-χ and coefficient-product parts of Hua's `84-chi-trivialised-extension-product`, independently of the obstruction to a particular comparison map on scans 154–170. Descent for varying line bundles and identification of the manuscript's global functor still require proof.

### R12 — The same model gives the expected local invertibility criterion

**Source:** `pages/MPL_84_146-193_84_scan146.tex`, “b=b₁b₂” and coordinate changes; scan 170, extension objects; interpreted through R11. **Kind:** own idea. **Confidence:** high for the local criterion, because both implications have an explicit algebraic witness; medium for its proposed identification with the context's global criterion.

In the groupoid of R11, τ has an inverse up to isomorphism exactly when τσ+χa=1 for some σ,a∈R, equivalently (τ,χ)=R, or τ mod χ is a unit in R/(χ). Necessity reads off the arrow from the product to the unit, and sufficiency uses σ as the inverse object with that same arrow. Context: this is the local trivial-line version suggested by the “T₀ generates L on V(χ)” clause of Hua's `84-chi-trivialised-extension-product`, not evidence that the named T₀ or its global descent is supplied on these pages. The computation supports the criterion under explicit identifications, and does not establish that the separately drawn pushout and pullback products agree.

### R13 — Automorphisms survive when χ has an annihilator

**Source:** `pages/MPL_84_146-193_84_scan146.tex`, coordinate changes; scan 154, “une indétermination”; interpreted through R11. **Kind:** own idea. **Confidence:** high within the explicit model, because automorphisms are exactly arrows whose target equals their source.

An object τ in R11 has automorphism group Ann_R(χ), so replacing this groupoid by the orbit set R/χR loses data whenever χ has nonzero annihilator. For an invertible object, multiplication by τ is invertible on that automorphism group: if τσ+χa=1, multiplication by σ is its inverse there. Context: this refines the categorical content of Hua's `84-chi-trivialised-extension-product`, whose conjectural summary does not specify how automorphisms are retained; it is also compatible with, but does not identify, scan 154's Hom-valued ambiguity. The finite-ring examples in the script illustrate this distinction without serving as a proof of the global category claim.

## Primary bibliography and verification limits

- Grothendieck, A. (n.d.). *[Formes quadratiques]* [Unpublished manuscript and reused typescript, Montpellier archive, cote 84, scans 146–193]. User-supplied scan set; exact archival dating remains the supplied catalogue attribution, not a date inferred from the reused text.
- The Stacks Project Authors. (n.d.). *The Stacks project* (Lemma 20.5.1, Tag 0B3A; §105.2, Tag 072J; §53.8, Tag 0BY6). Retrieved November 15, 2026, from https://stacks.math.columbia.edu/tag/0B3A, https://stacks.math.columbia.edu/tag/072J, and https://stacks.math.columbia.edu/tag/0BY6. These entries supply the extension/cohomology correspondence and the genus-one cohomology fact used in E170.4; the manuscript-specific sign calculation is derived separately.
- Loos, O. (1996). Tensor products and discriminants of unital quadratic forms over commutative rings. *Monatshefte für Mathematik, 122*, 45–98. https://doi.org/10.1007/BF01298455. Primary abstract and publication metadata inspected; full proof not inspected.
- Voight, J. (2016). Discriminants and the monoid of quadratic rings. *Pacific Journal of Mathematics, 283*(2), 483–510. https://doi.org/10.2140/pjm.2016.283.483. Author's revised manuscript dated January 17, 2021 inspected at https://jvoight.github.io/articles/monoid-011721.pdf; section numbering above refers to that manuscript.
- Voight, J. (2021). *Quaternion algebras* (Graduate Texts in Mathematics, Vol. 288). Springer. https://doi.org/10.1007/978-3-030-56694-4. Chapter 5, §§5.2–5.5, inspected at https://link.springer.com/chapter/10.1007/978-3-030-56694-4_5; its field/characteristic hypotheses are retained.
- Wood, M. M. (2011). Gauss composition over an arbitrary base. *Advances in Mathematics, 226*(2), 1756–1771. https://doi.org/10.1016/j.aim.2010.08.018. Primary manuscript inspected at https://arxiv.org/abs/1007.5285 and https://arxiv.org/pdf/1007.5285.

The supplied `README.md` (November 12, 2026), `LM2_CONGRUENCE_ROWS.md`, and `notes/RESULTS_STATE.md` (November 14, 2026, 20:11 UTC) are cited as internal planning and claim registers, not as independent literature. “Hua, findings register, 84-chi-trivialised-extension-product” refers only to the excerpt supplied in RESULTS_STATE; the original project and omitted page ranges were not independently inspected. No exterior transcription of the manuscript was consulted.
