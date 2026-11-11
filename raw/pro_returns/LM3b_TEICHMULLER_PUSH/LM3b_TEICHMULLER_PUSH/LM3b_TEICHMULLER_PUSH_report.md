# LM3b_TEICHMULLER_PUSH: audit and research report

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)**

Prepared 11 November 2026. This report accompanies the paper, result and reading registers, verified-source bibliography, and reproducible computation files. We make no novelty or priority claim. References below use the theorem numbering of the primary versions inspected; the bibliography records those versions and their publication status.

## 1. Outcome and interpretation of the register

The completed package contains **93 numbered statements: 53 Proved, 11 Refuted, 14 Open, and 15 Known**. These counts include the separately registered all-degree filling presentation B.11, automatic elliptic inertia E.9, and the class-two finite-image theorem F.13. A numbered statement can contain several related assertions, so these are register counts, not a count of logically atomic propositions.

“Proved” refers to the exact assertion and hypotheses written in the paper, with external inputs identified. “Known” records a reduction from a specified theorem to the requested formulation. “Refuted” negates the statement in the completion expressly named. “Open” records a precise residual mathematical obligation after the attack described there. An unperformed audit of another manuscript is not itself labelled a mathematical gap.

The central full profinite conclusions are as follows. The unrestricted filling sequence fails in the middle already for the four-punctured sphere, although both the outer filling map and its genuine based version are onto (B.4–B.5). Restriction to the point-pushing normalizer restores an exact sequence (B.6). A whole Galois-invariant loop structure is unique for every affine hyperbolic curve over a number field (D.3). The strict finite-category comparison with profinite stratified homotopy is proved at the first compactified level, four marked points (H.8).

Different conclusions have different scopes. Nonnormality of the geometric subgroup is proved in all three requested pro-prime types, and in the full profinite four-puncture type. Both covering-surjectivity counterexamples are pro-2 results. The all-weight Grothendieck–Teichmüller freeness result concerns the rational equation Lie algebra and its prounipotent completion. None of these is used to identify the full profinite Galois and GT groups.

## 2. Disposition of the six leads

### Lead 1: integral lifting — proved in its pro-prime scope

A.1 proves the lifting statement over every integral ring \(\mathbb Z_\ell\), including \(\ell=2,3\). Corrections use surjective integral bracket maps and converge in the actual free pro-\(\ell\) group because every finite \(\ell\)-group quotient is nilpotent. The relative argument preserves the quotient obtained by killing a generator; the strengthened version also controls the genuine based filling map. The ordinary lower-central graded identification is checked against Koch, Kukkuk, and Labute (1998, Theorem 2.1), including its applicability at two. A.12 supplies the elliptic counterpart fixing the entire group commutator exactly. These arguments do not construct arbitrary full profinite lifts: nonnilpotent finite quotients remain an additional requirement.

### Lead 2: pro-prime tripod nonnormality — proved and extended

A.2 recomputes the complete \(S_3\)-character through weight twelve. In weight five the special outer space is the sum of a trivial representation and the two-dimensional standard representation. An explicit integral non-invariant vector lifts by A.1, giving nonnormality for every prime (A.3). The same question is settled for the pro-prime four-puncture sphere and once-punctured torus (A.6, A.14). In the elliptic argument, the geometric central involution is characteristic and negates a degree-seven outer derivation; saturation ensures that \(2D\neq0\), also over \(\mathbb Z_2\). The three pro-prime conjugacy-orbit spaces are Cantor spaces containing closed copies of \(\mathbb Z_\ell\) (A.9).

### Lead 3: the filling kernel exceeds point-pushing — proved, including a separate full profinite construction

B.1–B.3 verify the proposed degree-three obstruction and extend the computation through degree six. The minimal generators of the kernel as an ideal of the ambient special Lie algebra have dimensions

\[
2,0,3,0,13,0.
\]

Thus adding only the three degree-three directions to point-pushing is insufficient; thirteen further degree-five generators are required. The all-degree split graded surjection and group-level surjectivity are proved separately. B.5 constructs a full profinite counterexample using an exponent-one arithmetic tripod automorphism extended across a free factor; it does not transfer the pro-prime counterexample by assumption. B.10 identifies the unrestricted kernel as \(Q\rtimes K\), with \(Q=\ker\theta\neq1\) and \(K\) point-pushing. A complete minimal presentation remains B.11.

### Lead 4: graded strictness — corrected and integrated away from two and three

The naive identification using only the lowest homogeneous antisymmetry and three-cycle equations is false. F.1 retains the cabling condition and proves that the resulting space is exactly the \(S_3\)-invariant special outer space. An explicit weight-four polynomial demonstrates why cabling cannot simply be dropped from that comparison.

The pentagon cuts the invariant dimension from two to one in weight seven (F.2). Coprime fixed-point lifting integrates this discrepancy for every \(\ell\geq5\), proving strictness of the multiplier-one pro-\(\ell\) pair group before and after imposing the pentagon (A.11, F.3). The corresponding fixed-point lifting at two and three, and realization in the full profinite pair group, remain F.4. No full profinite inequality \(\widehat{\mathrm{GT}}\neq\widehat{\mathrm{GT}}_0\) is claimed.

### Lead 5: scalar coinvariants — the calculation is correct, the character inference needs more

F.7 computes the ideal generated by \(u^w-1\) exactly. For odd \(\ell\), the quotient vanishes unless \(\ell-1\mid w\), and otherwise has order \(\ell^{1+v_\ell(w)}\). At two it is \(\mathbb Z/2\) for odd \(w\), and \(\mathbb Z/2^{2+v_2(w)}\) for even \(w\). These integral classes cannot be dismissed by rational weight arguments.

They also do not automatically yield characters of the full GT group. F.8 identifies the extension transgression and refutes the general extension inference with the explicit quaternion counterexample: the nonzero invariant character of the central \(C_2\subset Q_8\) extends to no character of \(Q_8\). This is not a nonextending character inside GT. For odd \(\ell\) and \(\ell\)-primary coefficients, the local cyclotomic transgression target with quotient \(\mathbb Z_\ell^\times\) vanishes, so an actual invariant kernel character would extend; constructing it from the graded coinvariants is still required. At two, the torsion factor can also obstruct extension. The local vanishing is not a statement about the different full profinite quotient \(\widehat{\mathbb Z}^{\times}\) or its kernel. F.9 proves the rational pro-algebraic abelianization statement, while F.12 retains the integral profinite problem.

### Lead 6: weights and open arithmetic normalizers — the decisive distinction is between a loop structure and an arbitrary subgroup

D.4 establishes the virtual-homology argument carefully for a topological generator. After passing to a finite cover, its nonzero line either lies in boundary homology, with potentially cyclotomic character, or projects to Jacobian homology. Complex multiplication permits the latter linear phenomenon. It does not supply a compatible cyclic subgroup in the nonabelian inverse limit.

For an entire alternative loop structure, D.1's determinant identity forces the necessary finite-twist cyclotomic condition; Nakamura's recognition theorem then proves uniqueness, including type \((1,1)\) (D.2–D.3). The stronger criterion for arbitrary maximal procyclic subgroups remains D.4. D.5 gives a complete counterexample on the class-two pro-5 quotient of \(y^2=x^3-x\) over \(\mathbb Q(i)\). Its normalizer projects onto the whole arithmetic group, but the subgroup is noncuspidal. This is explicitly a nilpotent-quotient counterexample, not a counterexample in the full geometric group.

## 3. Normalizers, filling, and covering comparisons

The genus-zero normalizer calculation is exact through degree six (A.5). The elliptic computation identifies the actual relative-completion geometric image, rather than merely a candidate algebra. Hain and Matsumoto (2020, Theorem 10.7, Proposition 20.1, Corollary 20.2, Theorem 22.3, and Corollary 23.3) supply the generation and grading comparison. Its positive geometric dimensions through ordinary degree twelve are

\[
0,0,0,3,0,5,0,10,0,24,0,50.
\]

The normalizer quotient for the **full** algebra \(\mathfrak{sl}_2\ltimes\mathfrak u\) has one-dimensional pieces only in degrees six and ten in that range (A.15). The degree-ten necessary bracket equation gives an upper bound; Hain and Matsumoto's Proposition 29.1 and Remark 29.3 supply actual arithmetic normalizer elements and the matching lower bound. Consequently no necessary equation is promoted to a sufficient all-degree test.

For filling, Hoshi and Mochizuki (2011, Theorem 6.1), together with Hoshi, Minamide, and Mochizuki (2022, Corollaries 2.6(i) and 2.8(i)), gives the repaired tripod sequence with image \(\widehat{\mathrm{GT}}\times S_3\) (B.6). The general repair retains FC-admissibility; automatic preservation of all required configuration fibres is not inferred merely from normalizing one point-pushing group (B.7–B.8).

For coverings, C.1 corrects the premise: the degree-two tripod subgroup is normal but not characteristic. C.2 distinguishes restriction into genuine automorphisms from the normalizer quotient describing the outer source. C.3 proves injectivity on prediscretization cosets in both full profinite test cases and their pro-2 versions. The source theorem is Boggi and Zalesskii (2025, Theorem A(iii), Theorem 4.3). For the pro-prime closure, its arbitrary-dense-embedding formulation is used only after proving the required comparison for all discrete coefficient modules.

C.5 proves pro-2 nonsurjectivity by a finite certificate. C.10 transfers that obstruction to the characteristic Klein-four covering using the intermediate subgroup and geometric transitivity on the three order-two deck subgroups. The latter is a group-theoretic transfer, not an unperformed rank-five enumeration. Arithmetic-image quotients compare as the identity of \(G_K\) over the field of definition (C.6); a comparison of §26 normalizer quotients requires the further implication isolated in C.7.

## 4. Arithmetic recognition and the category of curves

The uniqueness proof uses Nakamura (1994, Theorem 2.1.1 and Lemma 2.1.4) in the full profinite setting. Boggi and Zalesskii (2019, Proposition 3.6) supplies the normalizer statement for every nonzero profinite exponent, including a component supported at one prime. At type \((1,1)\), the primitive commutator in \(\Gamma_2/\Gamma_3\cong\widehat{\mathbb Z}\) gives the exponent comparison without discarding primes.

D.6 derives an arithmetic-image characterization from Pop (2018, Theorem 2.7(1)). The required enrichment is a cofinal system of opens of \(\mathcal M_{0,5}\), with restricted maps \(s,t,t-s\). The difference map requires localization; it is not a global forgetting map. D.7 translates Hoshi, Mochizuki, and Tsujimura (2025, Definition 5.12 and Theorem 5.17(ii)): maximal closed AA subgroups are the GT-conjugates of the arithmetic image. Belyi diagrams, covers, Kummer data, function fields, and second-configuration compatibility remain part of the assertion. A marking is needed to select a particular conjugate.

D.8–D.9 prove equality with Galois for the stabilizer of geometric section images retaining their actual arithmetic domains. This is a precise marked criterion, not intrinsic recognition of all abstract complements. D.10 retains the Kummer and Nakamura–Schneps relations with their path and coboundary ambiguities.

Mochizuki (1999, Theorem A/16.5) yields curve centralizers \(\operatorname{Aut}_K(U)\) and the open-Hom description of dominant morphisms (D.11, D.13). Type \((0,4)\) permits a nonsplit compactifying conic. These curve centralizers are distinguished from Nakamura's moduli centralizers, whose Theorems A and B retain their odd-prime hypotheses (D.12). D.14 constructs the essential image by open arithmetic tripod subgroups and Galois-stable cusp filling; Belyi (1980, Theorem 4) is used over the original number field, without an unstated extension-and-descent step.

## 5. Elliptic coherence, modular stacks, and congruence

E.1 identifies the inertia-preserving decorated elliptic normalizer quotient with GT using Boggi (2026, Theorem 3.12 and Theorem A(ii)). The automatic-inertia assertion remains E.9: a centralizer theorem for already recognized twists does not characterize all twists among arbitrary elements.

The open elliptic forgetting arrow has automorphism 2-group with \(\pi_0=\widehat{\mathrm{GT}}\) and \(\pi_1=1\) (E.2), using Minamide and Nakamura (2022, Proposition 3.2, Theorem 4.3, and Corollary C). The decorated boundary pair also has trivial \(\pi_1\) (E.3). The residual problem includes existence and uniqueness of coherent clutching data, rather than an automatic surviving \(C_2\) from the one-point elliptic center (E.4). The two requested orbifold correspondences have well-defined cone-order quotient and even-parity restriction maps, but their preservation of the full geometric normalizers and their identification with the same GT parameter require the additional comparison registered in E.4. Hyperelliptic comparisons retain orbifold cone inertia (E.5).

The quilt compatibilities retain the actual refined subgroups and relations of Nakamura and Schneps (2000, Theorems 1.2–1.4) and Hatcher, Lochak, and Schneps (2000, Theorems A–C). They are not extended to arbitrary finite coverings without proof (E.6). Boggi (2026, Theorem 6.23 and Corollary 6.24) yields the whole procongruence outer-tower theorem; equality for the full profinite tower remains conditional on congruence (E.7). E.8 derives the modular-stack exact sequence and preserves the distinction between its arithmetic-image quotient and the §26 normalizer quotient. The tripod stack is \(BS_3\); its coarse point would lose essential information.

## 6. GT equations and finite arithmetic images

F.2 computes the pentagon in the actual infinitesimal braid algebra through weight twelve. The dimensions in weights three through twelve are

\[
1,0,1,0,1,1,1,1,2,2.
\]

Rational candidate spaces are constructed exactly. Their integral bases retain full rank modulo 65521, where pentagon ranks give rigorous rational upper bounds. Brown (2012, Theorem 1.1 and the introductory faithful-action consequence) supplies the matching free motivic lower bound. The finite calculation is independent of the all-weight arguments in G.

F.5 enumerates all **792 two-generated abelian isomorphism types of order at most 500**, and all their scalar images are realized cyclotomically. Genuine abelian shadow half-parameters are handled modulo twice the shadow order when necessary, following Dolgushev, Le, and Lorenz (2024, Theorem B.2 and Remark B.3).

F.13 strengthens arithmetic exhaustion to **every characteristic finite quotient of nilpotency class at most two**. The GT commutator parameter becomes central, so the automorphism is determined by the multiplier-powers of the two chosen generators. This does not identify it with the power map on every element of a nonabelian group. Cyclotomic surjectivity supplies a Galois element with the same action. The explicit characteristic \(Q_8\) quotient has genuine image of order two and trivial outer image. Its genus-two example is a geometrically Galois three-point cover defined over \(\mathbb Q\), with geometric deck group \(Q_8\) and the displayed deck marking over \(\mathbb Q(i)\):

\[
Y^2=X^5-X,\qquad t=(X^2+1)^2/(4X^2).
\]

There is no enumeration of all nonabelian quotients through order 500, and no unrealized genuine shadow is reported. Class three is the first nilpotency class beyond this argument; nonnilpotent quotients also remain untreated (F.6). The rational parenthesized-braid theorem is derived from Bar-Natan (1998, Claim 2.6, Proposition 5.3, and Theorems 4–5), with braiding multiplier and associator dependence explicit (F.10).

## 7. The three manuscript audits

The requested steps of 019 and 031 were independently rederived from the supplied October 2026 versions. No gap was found in those designated steps. That verdict does not certify every assertion of either manuscript.

For **019, Proposition 5.2**, G.1–G.2 establish the stable model, toric uniformization, slope-one character, analytic root estimates, and a root on every inverse annular component after one multiplication pullback. Residue characteristic two and divisibility of the root degree by the residue characteristic are included. The curve obtained is connected over the stated field, as the proposition requires. Baker and Rabinoff (2015, Proposition 6.1 and Corollary 6.6, with the cited uniformization sections) supplies the precise skeleton compatibility. The full collar-to-global section-conjecture argument is outside this targeted certification.

For **031, Lemma 3.1**, G.3 proves the zero estimate through translated components, affine Bézout, and an interpolation determinant with the product formula. No Leopoldt hypothesis is introduced. G.4–G.5 verify the finite-character amplification and Frobenius-generation argument for Proposition 4.3; only the required subgroup equivariance is used. G.6 proves Proposition 5.3's bound uniformly in the auxiliary prime and twist-killing extension. G.7 derives the stated surjectivity and cyclotomic-logarithm consequence. Hoshi (2025, Theorem 3.4) requires full cyclotomic compatibility; a logarithmic equality is not silently substituted for it.

For **008, Proposition 3.2 and §4**, G.8 proves the filtered normal-form transfer with its exact length qualification, and G.9 proves the deletion and residual-kernel induction. The reduction is of a saturated lattice of rational solutions, not an arbitrary mod-two equation space. G.10 rederives the independent reconstruction route in Willwacher (2026, Theorems 1.1 and 2.2, Proposition 3.2). Its operator identity gives an injective projection and bounds its image by a free Lie algebra on the odd generators. Brown supplies the lower bound, proving the all-weight rational result. G.11 records the shared characteristic-two setup and the distinct upper-bound mechanisms; neither method's independent discovery is claimed. Both 2026 sources retain their manuscript status.

## 8. Computation certificates and their evidential limits

The code is independently written and does not import the supplied reviewer's program. Exact rational calculations, finite-field calculations, and infinite proofs are identified separately.

| Certificate family | What was checked |
|---|---|
| `ab_*.py` | Lyndon coordinates, special derivations, filling and ideal indecomposables, explicit integral witnesses, and complete elliptic geometric recursion. The degree-seven elliptic witness raises inner rank 18 to 19. The degree-fourteen geometric rank is 109, rising to 111 after the three degree-ten bracket tests. |
| `ceh_pro2_cover.cpp`, `ceh_pro2_verify.py` | A characteristic quotient in the units of the degree-four truncated noncommutative algebra over \(\mathbb F_2\). The based geometric image has order 128 and its deck-conjugation orbit has 64 elements. All 64 possible inner-intertwiner systems have explicit dual certificates giving \(0=1\); the independent verifier checks the recorded row sums without reusing the search elimination. |
| `fg_prepare.py`, `fg_pentagon.cpp`, `fg_certify.py` | Exact rational candidate spaces, pentagon evaluation in a faithful free-fibre semidirect presentation, modular ranks, and preservation of basis ranks modulo 65521. |
| `g_operator.py` | All 15 braid-relator forms on 484 basis inputs, giving 7,260 vanishing checks. The paper separately proves the operator identities in every word length. |
| `fh_finite.py`, `quaternion_shadow.py` | The abelian enumeration, 72 scalar-coinvariant tests, 38 cohomology modulus tests, quaternion characters, all 24 generating-pair automorphisms, and the explicit quaternion Belyi/deck identities. |
| `ceh_checks.py`, `dg_checks.py` | Finite-cover chain matrices, elliptic compatibility-sign orbits, CM Heisenberg conjugation, the determinant/Pfaffian identity, character stabilizers, and interpolation inequalities. |

The covering computation does not enumerate the entire automorphism group of its finite quotient. It excludes even arbitrary truncated units as intertwiners, which is sufficient. The class-four certificate is realized by an actual pro-2 lift; it is not merely a rational dimension discrepancy.

## 9. Genus three and higher completion

H.1 proves \(C_{3,0}\cong C_{\widehat{P\Gamma}_{3,1}}(\widehat\pi_{3,0})\). Boggi's procongruence center theorem gives the center inclusion in H.2, not centrality or torsion-freeness of the full kernel. H.3 proves finite-cover homology representations are congruence representations by constructing their characteristic quotient. H.4 gives a quotient of order \(64\cdot3^{258}\) detecting a separating twist: its auxiliary ten-dimensional homology action has a rank-one unipotent part of order three. This goes beyond base symplectic homology but cannot detect a congruence kernel by construction. No quantum quotient was produced.

H.6 constructs a cofinal strict finite-category quotient system at \(n=4\); H.7 computes constant finite-coefficient cohomology as the coefficient group in degrees zero and two and zero elsewhere. H.8 supplies the stronger stratified comparison using finite local systems and the rank-one spatial décollage. The exact inputs are Barwick, Glasman, and Haine (2020, Example 2.6.4, Theorem 2.7.4, Construction 2.8.8, equation (2.8.9), and Corollary 12.6.7). Constant cohomology alone is not used to assert equivalence. At \(n=5\), longer stratum chains introduce the additional compatibility isolated in H.9.

## 10. Exact remaining obligations

The fourteen Open rows are retained explicitly:

| IDs | Next obligation after the proved partial results |
|---|---|
| A.4 | Realize a noncentralizing pro-prime tripod witness by a full profinite peripheral automorphism, or prove the contrary restriction on that image. |
| A.16 | Settle full profinite elliptic normality and the all-degree elliptic normalizer quotient; degree fourteen is the first unclosed even Lie degree. |
| B.8 | Deduce full FC-admissibility from the bare point-pushing-normalizer conditions in general type. |
| B.11 | Give all-degree minimal generators and relations for the filling Lie kernel; degree seven is the first uncomputed ideal-indecomposable degree. |
| C.7 | Show that restriction of a downstairs geometric normalizer normalizes the entire upstairs geometric group. |
| C.9 | Decide full profinite covering surjectivity for the two test covers, beyond their pro-2 refutations. |
| D.4 | Force a potentially cyclotomic nonzero prime component from the bare maximal-procyclic open-normalizer hypothesis, or construct a full-group counterexample. |
| E.4 | Establish the elliptic clutching compatibilities and prove the full-geometric-normalizer and same-GT-parameter comparisons for the two orbifold correspondences; the two-puncture case also retains E.9. |
| E.9 | Recognize nonseparating twist inertia intrinsically from the specified elliptic fibre, cusp, and transposition decorations. |
| F.4 | Integrate the invariant nonpentagon direction at two and three, and settle full profinite strictness. |
| F.6 | Compute genuine arithmetic exhaustion beyond class-two characteristic quotients, beginning with the free class-three exponent-five quotient and its compatible lifting data. |
| F.12 | Determine the full profinite cyclotomic abelianization kernel, including integral lattices and transgressions. |
| H.5 | Decide genus-three kernel triviality, centrality, and torsion-freeness. |
| H.9 | Prove the compatible chain-groupoid completion and homotopy-fibre-product comparisons beginning at five marked points. |

## 11. Source and reading discipline

We read the attached prompt, prior response and review at the cited reductions, the targeted manuscript versions, and the primary sources identified above. Additional primary retrieval addressed precise theorem scopes and metadata, particularly the finite-subgroup normalizer theorem, lower-central integrality, elliptic relative completion, and the arithmetic Hom criterion. “Verified” in the bibliography means the source and cited locus were opened; it does not mean every theorem in that source was reproved.

The scan work includes visual inspection of 320, 322, 348, 355–356, 399, 479, and 483–488, with further loci recorded in the reading register. Scan 363 was available through the supplied transcription, not an attached image. Mathematical typing favors the upstairs group in the deck normalizer and the plus sign in \(2g+n-1\); the open-Hom theorem supports the inserted restriction to dominant morphisms. These are editorial evidence, not declarations that doubtful handwriting has been settled. Folio, spelling, and barred-symbol ambiguities with no mathematical consequence remain identified as such.

The package consequently records both completed arguments and their exact limits. Full profinite arithmetic exhaustion, the remaining isolated normalizer comparisons, and higher coherence are not inferred from rational freeness, finite examples, or already recognized inertia.

## 12. Final computational reproduction

The final quick verification reran ten programs and passed all twelve artifact comparisons in 26.206 seconds. The full run reran all sixteen mathematical programs, compiled both C++ programs afresh, and passed all nineteen artifact comparisons in 166.515 seconds. Both runs began outside the package directory, used the final quaternion source and records, and verified that the shipped outputs remained unchanged. The code ran under Python 3.12.14, SymPy 1.14.0, and GCC 14.2.0. The reports, logs, and regenerated comparison artifacts are included under `audit/reproduction/`. These runs verify the listed finite computations; the infinite-group and source-dependent arguments remain the proofs in the paper.
