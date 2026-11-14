# Part D and Lead 4: completion and verification

| Prompt item | Statements | Outcome |
| --- | --- | --- |
| What is to be settled: sphere two-isotopic item | D.1–D.16 | (a) for the topological reconstruction and five-stage extension; (b) for the unrestricted arithmetic gerbe classification and incorrect fidelity bounds, with complete replacements |
| Lead 4 | D.16 | (b): topological portion made precise; BPGL2 is distinguished from the imposed crossed-module quotient and its B²μ2 stackification |
| D(a) | D.1–D.3 | (a): cover constructed, relative uniqueness proved, pair equivalence proved; unrigidified unique-isomorphism wording corrected by a complete counterexample |
| D(b) | D.4–D.9 | (a): two proofs through dimension three, explicit failure in dimension four, complete Postnikov classification through dimension five retaining all homotopy witnesses |
| D(c) | D.10 | (b): the proposed bounds are false; all four cumulative notions have sharp uniform bound dimension ≤1 |
| D(d) | D.11–D.15 | (b): bare-gerbe classification over arbitrary schemes is false; crossed-module construction, module-enhanced object classification, two-stackification, field image and exact automorphism loss are proved |

All sixteen statement rows have proofs or complete counterexamples with their replacements. The finite and symbolic checks have been run. Their output is in `code/spheres_checks.out`.

## Manuscript read and images inspected

Read the complete transcription of scans233–250, with surrounding scans231–232, in LM_P024 and LM_P025. Directly inspected attached scans233,234,236,237,238,239,241,243,247,248,249,250. The thirteen entries of `readings.csv` identify the mathematically consequential readings and doubts. Their support is explicitly mathematical evidence, not a claim to have settled the editors' transcription.

## Main mathematical decisions

The semilinear extension fixes the reflection-square-+1 cover. Its uniqueness is a relative uniqueness with a specified restriction isomorphism; forgetting that isomorphism leaves a nontrivial automorphism and permits the other Pin extension.

The topological pair is complete on the two-type. For bundles, object classes are classified by it through dimension three. The full mapping two-groupoid has a substantially smaller uniform equivalence range: dimension at most one. The calculation at S² produces an explicit integer kernel on π₂ and resolves the conflicting margins.

The fourth Postnikov stage is a homotopy pullback. The homotopy in its definition is indispensable in the presence of torsion. The Moore space M(Z/4,3) produces four bundles with zero w₂ and p₁. The opened version of Antieau–Williams contains an unqualified uniqueness sentence in Definition2 that fails in this example; the paper's low-degree cohomology calculation and nonzero next invariant are separately checked and retained. Dold–Whitney's original introduction explicitly warns that characteristic classes alone do not classify general four-complexes. We fix the sign of p₁ by p₁=-c₂ of the complexification, so that ρ₄p₁=P(w₂). This also differs from the unadjusted signed formula printed in the opened Antieau–Williams preprint.

The degree-six invariant of the fifth stage is normalized by its fibre restriction and its restrictions along two explicit representations, SO₂ and the diagonal Klein four subgroup. This uniquely specifies it and avoids a noncanonical unidentified complementary cohomology class. The classification on all five-complexes is stated in coherent lifting data with the loop-slant action on H⁵; no unjustified product decomposition of the set of lifts is used.

On the arithmetic side, the fixed-base automorphism group is PGL₂; there is no variable topological orientation torsor. A μ₂-gerbe alone loses the rank-two twisted module. The two projective bundles on P¹ in D.12 prove the failure even for neutral gerbes. Over fields the object image consists exactly of classes of index at most two. D.14 supplies a finitely generated characteristic-zero counterexample to essential surjectivity. The reduction of automorphisms is computed as reduced norms modulo squares, with a real quaternion example and exhaustive F₂,F₃ checks.

The manuscript's final phrase “not even 0-faithful” is correct as ordinary nonfaithfulness after passing to homotopy classes of automorphisms. With the explicit earlier technical definition, the ordinary groupoid source has π₂=0, so that statement is literally false. Both meanings are recorded rather than silently identified.

## Literature verification and search record

Searched for sphere-homeomorphism deformation retractions, the fourth and fifth Postnikov stages of BSO₃, Dold–Whitney torsion qualifications, and arithmetic lifting gerbes. Opened these primary sources:

- Dobbins (2021), arXiv:2108.02134, Theorem1.1: https://arxiv.org/pdf/2108.02134 . Tool source ref `turn20view1`.
- Edwards and Kirby (1971), Corollary1.1: https://math.berkeley.edu/~kirby/papers/Edwards%20and%20Kirby%20-%20Deformations%20of%20spaces%20of%20imbeddings%20-%20MR0283802.pdf . Tool refs `turn21search24`, `turn34view0`.
- Antieau and Williams (2013 revision), arXiv:1209.2219v2, complete four-page text, especially Definition2 and Corollary3: https://arxiv.org/pdf/1209.2219 . Tool ref `turn1view1`.
- Dold and Whitney (1959), original PDF and indexed introductory text: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/doldwhit.pdf . Tool refs `turn19search8`, `turn20view0`.
- Serre (1953), §2 Theorems2 and3 and §9 examples: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf . Tool ref `turn42view0`.
- Hatcher (2002), Corollary4J.4, Theorems4.69 and4.71: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf . Tool refs `turn34view2`, `turn40view1`, `turn40view2`.
- Stacks Project, §59.62, especially Lemma59.62.1: https://stacks.math.columbia.edu/tag/0A2J . Tool ref `turn34view1`.
- Stacks Project, §59.61 and Lemma59.61.5: https://stacks.math.columbia.edu/tag/03R1 and https://stacks.math.columbia.edu/tag/03R6 . Tool refs `turn39view1`, `turn39view2`.

The Stony Brook URL for Milivojević's sixth-invariant note returned404. An author's-page link to a Drive copy was opened but did not expose the document text; it is not used or counted as verified. Kudo's original transgression PDF was opened but yielded no readable text; it is not used. The relevant Steenrod/transgression facts are instead located in the opened Serre text. No priority or novelty claim is made.

## Reproducible computations

`code/spheres_checks.py` uses only Python's standard library. It exhaustively checks the two four-element central extensions, the automorphism quotient for PGL₂ over F₂ and F₃, the adjoint Chern-root calculation, the Moore-space cokernel and its p₁ map, the degree-six characteristic polynomials, and all4096 triples and256 pairs in the signed quaternion basis multiplication. All checks passed.

`code/build_registers.py` writes the sixteen statement rows and thirteen reading rows, with its output recorded.

## Integration

`D.tex` is a self-contained fragment using only ordinary LaTeX, amsmath/amssymb commands and `\cite`. No custom theorem environments are needed. The main author should merge the bibliography entries, the CSV rows, and the two code/output pairs. PDF compilation and visual inspection belong to the integrated paper; no standalone PDF is asserted here.

## Final provenance audit

All sixteen numbered statements now include an explicit manuscript problem locus in the LaTeX text, with section, manuscript folio (including versos), and scan. The scope is §20, folios116v–125v, scans233–250; scan237 bears folio119 rather than being inferred as118v. The CSV has the same exact locations. Statements D.6–D.9 explicitly distinguish the modern Postnikov developments from the manuscript's motivating question; D.7 identifies the later Antieau–Williams uniqueness claim it refutes. Status labels are normalized to Known, Proved, or Refuted. All eight bibliography entries carry a verified-opened note. Dobbins Theorem1.1 was rechecked directly on page1 and indeed concerns Homeo(S²), despite the projective-plane title.
