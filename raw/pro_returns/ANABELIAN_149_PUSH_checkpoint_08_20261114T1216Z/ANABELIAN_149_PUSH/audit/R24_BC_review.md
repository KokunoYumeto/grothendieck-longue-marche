# Independent review of R24, §§2–4

Reviewer: degeneration agent. Date: 2026-11-14. Scope: the supplied local copy `tmp/pdf_text/padic_section_conjecture_2026.txt`, lines approximately220–637, plus the exact primary lifting and RNS statements. This review does not promote the paper's section-conjecture theorem or assess its later §§5–7.

## Outcome

No specific mathematical gap was found in §§2–4 after an adversarial check of the four requested interfaces: whole-collar roots, the separating stable-edge construction on every sheet, stable-model domination, and evaluation at the specified H-valued point. The arguments in these sections use the cited hypotheses in their stated scopes. The checks below identify the steps that would have failed under weaker formulations, and why the actual text avoids those failures.

## 1. Patching and evaluation (§§2–3)

The completion H contains the specified completed algebraic constant field Ω because the universal étale field contains the chosen algebraic closure of the constant field. The H-valued point of X_Ω retains both embeddings, K0→H and Ω→H. Its support on X_Ω may be closed even though its projection to X over the algebraic constants is generic; the proof explicitly allows this situation.

Lemma3.1 is local in characteristic zero, not a claim of tame reduction. After sufficiently shrinking around a ramification point, the analytic unit in t=u^e a(u) admits an e-th root even when p divides e. The displayed valuation threshold permits the p-adic logarithm and exponential. Properness then ensures that a smaller base disk has its **entire** inverse image inside the chosen finitely many coordinate disks. Distinct branch disks can avoid the fixed analytic point because that point is not one of the algebraic branch points.

In Proposition3.2 the exterior region and the inverse inner disks form an actual open cover of Y. On each overlap the assumed root is defined on the whole inverse annulus. Every local factor Z^e−g*t splits; different factors are comaximal because their difference is a nonzero constant times an analytic unit. Small absolute value of a root-of-unity difference does not affect its invertibility in an Ω-analytic algebra. Thus one obtains a trivialization of all d sheets, sufficient to glue finite étale analytic algebras. Disjoint branch disks remove triple-overlap conditions involving different disks. A nonempty connected component of the resulting finite étale cover still surjects to connected Y.

Lemma3.3 does not replace the valued point by its underlying Berkovich point. An embedding of the descended function field V into H gives an H-point of V; adjoining the fixed Ω-structure gives an H-point of V_Ω, and the isomorphism over X_Ω preserves the original H-point on X_Ω. The analytic map on the exterior can therefore be evaluated using the embedded completed residue field. Projecting the resulting H-point to C has generic support over the algebraic constants, since its image in X does and C→X is finite. It therefore yields the required K0-field embedding of kbar(C) into H. No descent of the exterior analytic map is needed. For normal F/K0, every K0-embedding into the common overfield has the specified image F because its minimal polynomials split in F; this is the final step in Proposition4.4.

Lemma3.4 keeps the horizontal ramification condition separate from reduction in characteristic p. Completed local fields at these horizontal points are kbar((t)), with residue characteristic zero and algebraically closed residue field. Their ramified extensions of index e are the Kummer fields kbar((t))(t^(1/e)). Composita and Galois closure therefore preserve the bound e|ell. The argument does not assume that two arbitrarily ramified covers may be composed without increasing their indices; the only upper composition it uses is étale.

## 2. Whole open annuli (§4.1)

An analytic unit and its inverse on a circle of radius in |Ω*| reduce to inverse Laurent polynomials. Hence the reduction is a monomial and exactly one Laurent term dominates. The dominant exponent cannot change inside an open annulus without a tie. Because coefficient valuations and the relevant edge lengths are rational, a tie radius lies in |Ω*|, where the reduction argument excludes it. Uniform convergence on compact subannuli makes this argument valid even for infinite Laurent expansions. This supplies a single factorization cS^d(1+h) on the whole open annulus, not only a middle subannulus. Compactness of each closed subannulus gives a uniform bound |h|<1 there, so the prime-to-p binomial roots glue. The analogous disk argument gives the constant-norm statement used in §4.2.

For a circuit edge, the residue cyclic cover has two totally ramified marked points and no other ramification. Picard divisibility supplies the required divisor class, and orders congruent to±1 modulo ell ensure both connectedness and total ramification. All other marked fibres have ell distinct points. The chosen graph edges account for every marked fibre, including chords and loops. The two ramification contributions are exactly the two edge contributions in the augmented Riemann–Hurwitz formula, so the map is a tame covering, not merely a harmonic morphism.

For a separating edge, each side must contain a circuit or a positive-genus vertex: a rational tree with N vertices and one outgoing half-edge has total valence2N−1, which contradicts stability's lower bound3N. The construction gives a **connected** degree-ell cover of each side. Matching the ell boundary fibres produces ell bridge edges between these two connected covers. Removing any one still leaves a connecting bridge, so every edge above the original separating edge is nonseparating. The identity residue pieces and the chosen unramified positive-genus cover have zero augmented ramification. The resulting triangulation remains stable by multiplication of 2g−2+valence by the local degree.

Applying the circuit construction separately to all lifted edges and taking any nonempty connected component of their finite étale fibre product preserves every constructed root. Each projection from that component is surjective because it is finite étale over a connected curve. Consequently this operation does not retain merely a preferred sheet. The same argument combines a finite collection of original annuli.

## 3. Exact use of ABBR

Opened original author PDF: Amini, Baker, Brugallé, and Rabinoff, *Lifting harmonic morphisms I: Metrized complexes and Berkovich skeleta*, https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf.

Exact passages checked: Definition2.21 (printed p10), Definition4.25 (p26), Definition4.31 (p27), and Theorem7.7 (p45). Web refs: turn332view0, turn334view0–2, turn336view2–4.

Theorem7.7 lifts tame coverings, including loop edges, to tame coverings of triangulated punctured curves. Definition4.31 requires the puncture set to contain the branch locus; taking no punctures therefore gives a genuinely étale cover. Definition4.25 supplies inverse-image equality for the vertex set and the complete skeleton. This is stronger than merely mapping one skeleton into another.

That inverse-skeleton equality also justifies the whole-annulus assertion. An off-skeleton ball maps into one off-skeleton ball downstairs. Continuity sends its attachment point to the attachment point downstairs, so retractions commute. The inverse image of the retraction tube of an open edge is therefore precisely the union of the source open-edge tubes. Those are the entire source node annuli. There are no extra off-skeleton sheets omitted from the root construction.

## 4. RNS domination and irrational levels (§4.2)

All algebraic curve, branch-point and rational-parameter data descend to a finite extension of the p-adic base. Blowups at successive reductions of a smooth marked section introduce the stated node annuli. The quotient t/u is an analytic unit of constant norm on a sufficiently small disk, so these are also concentric annuli for t. Forgetting the markings can leave an unstable model; the argument deliberately uses domination of that model, not the false assertion that its nodes survive stabilization on the original curve.

Opened original primary PDF: Mochizuki and Tsujimura, *Resolution of Nonsingularities, Point-theoreticity, and Metric-admissibility for p-adic Hyperbolic Curves*, version30March2024, https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf.

Exact passages checked: TheoremA (printed p4), Proposition2.4(iv) (p50), and its proof (pp53–54). Web refs: turn332view1, turn334view3, turn336view0–1. The full prime set satisfies the cardinality and residue-prime conditions. For a finite p-adic base, RNS supplies, after finite base extension, a finite étale cover whose compactified **stable** model maps to the prescribed compactified model. It does not require that model morphism to be finite, and the argument in R24 does not use such a requirement.

At an irrational valuation level within a target node annulus, no source model vertex can occur, because such a type2 point gives rational valuation to the pulled-back coordinate. No source smooth-point tube can occur either: if it meets that level, reduction compatibility sends its entire open disk to the target node annulus, where the coordinate is a unit; its norm is then constant and belongs to |Ω*|. Thus every point over the irrational level lies in one of the finitely many source node annuli mapping to that target node.

The complement of that finite union of open annuli in the proper analytic source is compact. Intersecting with the preimage of a closed target subannulus keeps it compact. The continuous valuation function has compact image avoiding the irrational level, which gives an open interval with rational endpoints whose **entire** preimage lies in the chosen node annuli. Stable-node root extraction then applies on each whole source annulus. This is exactly the point where a preferred-branch argument would have been insufficient; the compact-complement argument supplies the required all-sheet collar.

## Review boundary

This review found no failure step within the stated scope. It does not validate the arbitrary-order root construction in §5, the completed universal-tower argument in §6, the valuation comparison in §7, or the paper's final local/global section-conjecture statements. Those remain outside this independent review.
