# Parts A and F: construction and verification report

## Scope and interpretation

Part A fixes the conventions that determine every later comparison. The manuscript's homeomorphism group preserves the puncture set; it is not pure and does not impose orientation. We separate the permutation and orientation characters, the discrete mapping class group, its abstract profinite completion, and its geometric image in continuous outer automorphisms. The modular object in §26 retains isotropy and unordered punctures. In particular the labelled three-point moduli object is Spec Q, whereas the unordered stack is B S3. This distinction matters in the computation of the early normalizer quotient.

The definitions of N and its quotient change in §29. We use separate superscripts for the full normalizer and the arithmetic image. This resolves a central ambiguity in the prompt: surjectivity from G_Q to the revised image quotient is definitional, whereas surjectivity onto the independently defined GT-like normalizer quotient is additional mathematics. A.9 proves the comparison maps and A.10 proves the torsor assertion without assuming normality in the whole ambient automorphism group.

The covering operation is a correspondence involving the stabilizer of the covering subgroup and a chosen lift. It is not a canonical homomorphism of all outer automorphism groups. A.4 retains deck ambiguity. The filling operation on the surface group is different from the Birman map on mapping class groups. A.3 and Part C distinguish them.

A.13 writes out the universal-lift construction of §21. The kernel over the discrete mapping class group is a direct product A^circ×Π in the specified pullback, so this gives mathematical evidence for the doubtful multiplication symbol. We explicitly use a universal principal A-space, for example Milnor EA, for the homotopy-quotient argument. An arbitrary contractible free topological A-space without a principal-bundle hypothesis would not justify that argument.

## Corrections in exceptional types

The type (0,2) exposes two distinct signs. Inversion z↦1/z exchanges the punctures and preserves orientation; conjugation z↦bar(z) fixes the punctures and reverses orientation. Both induce -1 on the fundamental group Z. Thus rho_pi=rho_permutation·epsilon. The literal identification of these two rho maps on scan225 is false, and so is the rank-one determinant-one assertion on scan227. The table in A.11 is the corrected statement, retaining the independent orientation datum. The torus determinant-one statement remains valid.

The fundamental groups of (0,3) and (1,1) are both free of rank two, but their peripheral structures are different. The once-marked torus and unmarked torus have the same mapping class group SL2(Z); forgetting the mark does not have an injected Z² point-push kernel. Real and nonorientable cases are described separately, and finite elliptic isotropy is retained at primes2 and3.

## The profinite category constructed in Part F

We take Jansen's category with its actual transporter composition. Its arrows smooth nodes; the opposite category has arrows of degeneration. We use a finite skeleton indexed by stable labelled trees. This is an equivalence of categories, not groupoid completion.

F.2 defines a strict pro-object using all finite objectwise composition congruences. Its transition functors keep the objects and are surjective on Hom sets. The inverse-limit category in profinite sets is proved equivalent to this pro-object at the level of continuous functors and natural isomorphisms. The finite-object hypothesis and actual transitions are used in the proof.

F.3 supplies a finite counterexample to inverting arbitrary natural transformations: [1] and a point become indistinguishable under that operation, although their set-valued representation topoi have respectively three and two subobjects of the terminal object. The category and its noninvertible arrows therefore cannot be replaced by its fundamental groupoid. This respects the CATHOT warning rather than treating it as a substitute for the exit category.

F.4 distinguishes finite representations, arbitrary representations factoring through one finite stage, and all continuous discrete actions. The continuous action of Zhat on the disjoint union of Z/m!Z for all m has no common finite quotient. The attached GALOIS F.4 is not refuted: Hoyois explicitly calls the finite-stage objects split and distinguishes them from the classifying topos.

The main completion argument is F.5–F.7. Boggi's profinite curve complex is taken from its actual definitions, with closures of curves and multicurves in the profinite surface group. We use the stabilizer theorem and multitwist normalizer theorem in the procongruence group, and only then use genus-zero CSP to identify the full completion. F.6 proves that a discrete stabilizer inherits its full profinite topology by comparing the cutting extension before and after completion. This is stronger than residual finiteness.

For a finite-index normal V in G_n, the finite quotient category has the same stable-tree objects and Hom sets given by the finite images of the transporters modulo the finite images of their source multitwist groups. F.7 proves these quotients are cofinal among all finite functors. In genus zero a nonempty transporter is one stabilizer coset, because labels identify the relevant source submulticurve uniquely. A finite functor is therefore controlled by finitely many restrictions to stratum automorphism groups; the full induced stabilizer topology supplies one ambient V killing their kernels. This proves the proposed transporter completion, not just a candidate formula.

Forgetting, clutching and relabelling extend using actual finite congruences and their pullbacks. Relabelling is retained as a coherent pseudo-action. No splitting of a symmetric-group extension is introduced.

## Geometric comparison and Galois action

BGH's stratified Riemann existence theorem, applied with Jansen's exit calculation, gives the finite constructible-sheaf comparison. We retain the stalk/evaluation functors. Covariant finite representables recover each finite Hom set; inverse limits recover the profinite Hom sets. Thus the finite-set exodromy object is the category we constructed.

We distinguish this result from the full stratified infinity-categorical profinite completion. BGH identifies that stronger object, but interchanging strict finite-category completion with nerve and full profinite homotopy completion requires an additional argument. F.18 states the precise remaining comparison. The first nontrivial test is n=4. This is an audit limitation, not an asserted counterexample.

Galois descent acts by inverse pullback to give a left action. It is coherent and continuous on finite data and is compatible with the maps defined over Q. Local Kummer covers give the common cyclotomic exponent on all node inertia. The action is faithful from the open four-point stratum and remains so at higher levels through surjective forgetting.

For q_{12,34}, forgetting the fifth mark sends the two independent node twists to the same primitive twist. The kernel on Zhat² is the diagonal (a,-a), hence the lifting groupoid is B Zhat. Its H^1 with F_l coefficients is nonzero, which proves failure of the homotopy-smoothness test. This is not claimed to be a failure detectable by ordinary set-valued connectedness. Galois acts on the difference twist by its common cyclotomic exponent.

## Automorphisms and rational limitations

F.12 proves detection by the open stratum: outgoing coset bimodules recover multitwist stabilizers, their normalizers recover stratum automorphisms, and injective postcomposition recovers every crossing arrow. Inertia-preserving group automorphisms extend using the profinite curve complex and its incidence. F.13 then reduces the decorated two-level automorphism theorem exactly to Harbater–Schneps, with its common inertia exponent and coherent symmetric-group condition. Centre-free stratum groups make the compatibility isomorphisms unique and establish coherence. F.14 extends the result to the full genus-zero decorated boundary tower.

The resulting group is GT, containing the faithful G_Q action. Equality with the arithmetic subgroup remains the profinite question E.8. It would be incorrect to claim that the categorical construction identifies the revised arithmetic image with all automorphisms merely by definition.

For (1,1) and (1,2), F.15 proves the analogous strict transporter completion and stack comparison. Stabilizer quotients retain finite graph and half-edge symmetries. The boundary object of the one-point elliptic category has group C2; passing to a coarse moduli space would erase it. The cofinality argument works with finite unions of closed transporter cosets. F.16 states the precise positive-genus automorphism comparison not completed here; it does not misreport existence of positive-genus GT actions as open.

The established rational analogue is defined separately using algebraically enriched completed parenthesized braid/chord-diagram groupoids and their operadic operations, with Drinfeld and Bar-Natan's exact theorems. Its motivic consequence has exactly the conditional status of E.20. We corrected an initial draft that too quickly identified these groupoids with termwise unipotent boundary transporters. A quotient U/Delta is a homogeneous space, generally not a torsor, and completion does not make a smoothing arrow invertible. An additional enriched boundary-automorphism comparison would need its own proof.

## Sources read and editorial scope

The complete prompt and the supplied manifest were read. For Part A the transcriptions from LM_P021, LM_P023, LM_P026, LM_P027 and LM_P033 were read in the relevant sections, with the following manuscript images inspected directly: scans204,205,320,321,325,326. The owners of B/D/E additionally inspected the scans listed in their reports. We do not claim image evidence for a scan absent from the archive. In particular scan261's proposed switched-subscript correction is mathematical evidence, not a visual reading.

The root reading register includes the base-point enumeration at204; equality of the empty-set stabilizer at206; pointed versus punctured at222; cylinder signs at225–227; the U versus universal-cover symbol and product at252; the action inverse at253; homotopy indices at258; genus reductions at260; the impossible varying-genus Teichmüller chain at261; the extra-point index at263; and a typed groupoid Hom at266. The last is an editorial observation outside the deductions. The closure terminology at321 and doubtful folio328 are also recorded. A grammatical or symbol alternative with no mathematical consequence is not silently used to alter a theorem.

Primary sources actually opened for A/F include:

- Farb and Margalit (2012), Theorems4.6,8.1,8.8,10.6 and §10.6.3. The book supplies the Birman, Dehn–Nielsen–Baer and Teichmüller-coordinate inputs; their scopes were checked.
- Jansen (2023), Construction3.18, Proposition3.23, Corollary6.6 and Theorem6.7 in the supplied v2. We use the stable-type condition of the definitions rather than reproduce the misprinted inequality in the final sentence of Theorem6.7.
- Barwick, Glasman and Haine (2020), Proposition12.6.4, Corollaries12.6.6–12.6.7, Proposition13.9.17 and Corollary13.9.19, in both the supplied source and opened primary PDF.
- Boggi (2020), Definitions3.3–3.4, Theorems3.5–3.6 and4.2, Corollaries4.3 and4.7; the class of finite quotients and full/procongruence substitution were checked.
- Boggi and Funar (2023), Theorem4.11, Corollary4.12 and Proposition7.2, for multitwists, normalizers and incidence.
- Boggi (2026), arXiv2011.15075v6, Proposition3.5 and the specific tower statements checked in Part E.
- Harbater and Schneps (2000), introductory definition and Main Theorem, with the four-point/five-point distinction.
- Hoyois (2018), the notation before Definition2.10, Theorem3.13 and Corollary3.20, especially the meaning of split representations.
- Drinfeld and Bar-Natan through the exact original-source checks in Part E.

We searched these primary sources and the supplied/current tower literature before formulating the completion and automorphism deductions. No claim of novelty or priority is made. The 2026 status check opened the current records and original texts identified in E's report.

## Reproducible finite checks and review

The standard-library program af_checks.py checks:

- the three-versus-two subterminal count;
- a seventeen-arrow finite model of C4 with open group S3 and inertia orders2,2,3;
- every composable triple in that model and every composable pair under the sign quotient transition;
- the four stable-tree types at n=4 and twenty-six at n=5, with every fifth-point forgetting image;
- the node-difference kernel and its stability under all unit multipliers modulo every m from2 through24;
- the nonzero finite Hom models for the H^1 obstruction;
- the torus relations S²=(ST)³=-I and detection of the central involution modulo4.

The infinite statements are proved in the paper, not extrapolated from those bounds. The code records exactly what was enumerated.

Independent reviews within this AI-produced work checked A.4/A.8/A.10; the added A.11/A.13 corrections; F.5–F.14's stabilizer, cofinality, detection and coherence arguments; F.1–F.4 and F.9–F.11's coefficient and descent claims; and F.15's graph-isotropy extension. These are internal checks, not human refereeing or independent external certification. Their concrete corrections were incorporated. The final build and validation record is in the main report.

