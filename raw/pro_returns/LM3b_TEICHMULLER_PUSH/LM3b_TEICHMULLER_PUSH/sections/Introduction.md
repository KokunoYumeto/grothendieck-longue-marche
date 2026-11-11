# Conventions and scope

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).** Prepared on 11 November 2026 from the attached manuscript, prior response, review, and primary sources. We claim no priority. “Proved” means that the exact assertion has a proof in this paper, using the cited external theorems where specified. “Known” means that we derive the requested formulation from a named theorem. “Refuted” applies to the assertion expressly negated, in the completion specified. “Open” means that the exact obligation remains unresolved in this work; the text distinguishes a recognized open problem from an incomplete comparison in this audit.

We fix the principal manuscript notation before making any comparison. New auxiliary letters in a proof are declared there and do not claim a manuscript counterpart. An unadorned surface group in an assertion about profinite automorphisms is fully profinite; a pro-prime group always carries the superscript or the explicit qualification “pro-$\ell$.” The bracket grading in the computations is the ordinary lower-central grading.

| Our notation | Grothendieck's notation; introducing scan | Meaning |
|:---|:---|:---|
| $(g,n)$ | $(g,\nu)$; 204–205 | Genus and number of punctures; hyperbolic means $2g-2+n>0$. |
| $\Pi_{g,n}$, $\widehat\pi_{g,n}$ | $\Pi_{g,\nu}$, $\widehat\Pi_{g,\nu}$; 221, 328 | Discrete surface group and full profinite completion, with peripheral classes. |
| $\Gamma_{g,n}$, $P\Gamma_{g,n}$ | $\mathcal T^+$, $\mathcal T^{!+}$; 226, 323, 328 | Orientation-preserving mapping class group, respectively its pure subgroup. |
| $O_{g,n}$ | $\widehat{\widehat{\mathcal T}}$; 321–324 | Continuous loop-preserving outer automorphisms, with a common peripheral unit multiplier. The double hat is not iterated completion. |
| $\Sigma_{g,n}$ | $\widehat{\mathcal T}^{+}=\Sigma$; 323–324 | Geometric image, the closure of the orientation-preserving mapping class action; it need not be its abstract profinite completion. |
| $\Gamma^{\mathrm{norm}}_{g,n}$ | $\mathcal N_\Sigma/\Sigma=\Gamma_\Sigma$; 324–326 | The normalizer quotient of §26. |
| $\Gamma^{\mathrm{arith}}_{g,n}$ | $N_{g,\nu}/\Sigma$; 370–371 | The arithmetic-image quotient of §29. |
| $G_K$, $\chi_K$ or $\lambda$ | $\mathbb I\Gamma_K$, $\chi$; 327, 323 | Absolute Galois group and cyclotomic character, or the ambient peripheral multiplier. |
| $\mathcal M_{g,[n]}$ | $M_{g,\nu}$; 326–329 | The moduli **stack** with an unordered puncture divisor; $\mathcal M_{g,n}$ retains labels. |
| $f_i$, $\theta_i$ | The filling maps (1)–(2); 348–349, 367–368 | Outer filling and its genuine target action after selecting filled-cusp inertia. |
| $\mathfrak s_r$, $V_n$, $W_n$, $C_n$ | No corresponding fixed symbol | Special outer derivations, the two equation spaces of F, and the exit category of H. |

All homomorphisms of profinite groups are continuous; all subgroup closures, kernels, and quotient topologies are understood. A morphism “outer” to a group $H$ is taken modulo conjugation by $H$, unless a smaller conjugating group is named. Geometric base-point changes induce that stated inner ambiguity. We distinguish a mapping class group's full completion from its image in the automorphism group of a completed surface group. The latter is the procongruence group.

# What the numbered results settle

The full profinite filling sequence marked “??” fails at $(0,4)\to(0,3)$: B.5 constructs an element of its kernel outside point-pushing. The map is nevertheless onto, by B.4. B.6 identifies the exact replacement on the normalizer of the point-pushing subgroup. This also refutes full profinite normality of the geometric subgroup at $(0,4)$, by A.6. These conclusions do not depend on lifting an arbitrary pro-prime automorphism to a free profinite group.

The finite pro-$2$ covering certificate C.5 refutes the requested normalizer-times-geometric factorization for the degree-two tripod cover; C.10 transfers the obstruction to the characteristic Klein-four cover. D.3 proves uniqueness of a whole Galois-invariant loop structure for every affine hyperbolic type over a number field. H.8 proves the first strict-category versus profinite-stratified comparison, at $\overline{\mathcal M}_{0,4}$. The full profinite tripod normality and GT strictness questions, the unrestricted elliptic inertia comparison, and genus-three congruence are kept separate from these results.

The following table is a guide to the earlier open rows, not an additional set of unnumbered theorems.

| Earlier row | Conclusion in this paper | Numbered results |
|:---|:---|:---|
| LM3 B.7: normality | Counterexamples in all three requested pro-prime types and in the full profinite four-puncture case; exact remaining tripod lifting problem. | A.1–A.16 |
| LM3 C.8: filling | Full profinite sequence false in the middle; surjectivity and repaired normalizer sequence proved; the all-degree kernel presentation remains open. | B.1–B.11 |
| LM3 B.14: coverings | Geometric descent/injectivity established for the test covers; both pro-$2$ surjectivity claims refuted; remaining comparisons isolated. | C.1–C.10 |
| LM3 D.23: loops | Whole invariant loop structures unique; bare maximal-procyclic criterion remains stronger. | D.1–D.5 |
| LM3 D.23: admissible splittings | Localized-tower and AA characterizations derived; equality for an explicitly arithmetically marked section family. | D.6–D.14 |
| LM3 E.14, F.16: elliptic types | Precise automatic-inertia and clutching-coherence obligations; open-arrow 2-group and boundary modification group computed; modular-topos comparison derived. | E.1–E.9 |
| LM3 E.8: Galois and GT | Pro-$\ell$ two-relation strictness for $\ell\geq5$; full profinite comparison remains unresolved; abelian and characteristic class-two finite families settled. | F.1–F.13 |
| LM3 B.3: congruence | Exact centralizer criterion and an explicit finite representation beyond base homology; no genus-three solution. | H.1–H.5 |
| LM3 F.18: higher completion | Affirmative comparison at $n=4$; a precise chain-comparison condition for larger $n$. | H.6–H.9 |
| LM3 D.7, D.13, E.26: manuscripts | Requested steps of 019, 031, and 008 rederived; independent direct pentagon calculation and all-weight upper-bound reduction. | G.1–G.11; F.2 |

The primary-source theorem numbers below refer to the actual versions opened. A bibliography entry marked **verified** means that the source was opened and the cited locus inspected; it is not a claim that every theorem in that source was independently reproved. In particular, the 2026 manuscripts retain their manuscript status. We verify the obligations named in G and do not certify every assertion of 019 or 031.

# Manuscript loci and exceptional types

We use section, manuscript folio, and scan together. Where the transcription also supplies a running number at the bottom of a verso, the folio reference follows the surrounding recto/verso sequence; the scan is the unambiguous locator. The folio alternative on scan 328 is retained. Statements about the new computational leads, or about the 2026 manuscripts, are auxiliary to the indicated passage and have no verbatim 1981 counterpart. The result register records that distinction. The reading register separates mathematical support for an alternative from a palaeographic decision.

The quoted sentence “Ce n'est pas la peine” is treated as the conjectural sentence about a whole loop structure, followed by a distinct proposed test for individual subgroups. We also retain the question marks on the filling sequence and the subsequent correction on scans 367–370. A withdrawn assertion is not restored as a theorem.

The nonhyperbolic types excluded from the principal assertions must be treated separately. For $(0,0)$ and $(0,1)$ the geometric group is trivial; its outer automorphisms cannot detect arithmetic. For $(0,2)$ it is $\widehat{\mathbb Z}$, and for $(1,0)$ it is $\widehat{\mathbb Z}^{\,2}$. Their nontrivial centers invalidate the center-free extension arguments in B and D. These elementary identifications follow from the sphere, punctured sphere, cylinder, and torus presentations. Thus none of the hyperbolic recognition statements is extended to them by deleting a hypothesis.

The profinite surface groups of the hyperbolic types used below are center-free, including the tripod and once-punctured torus. Mapping class groups may still have centers, especially the order-two elliptic center; E treats that distinction explicitly. The integral lifting and determinant proofs include primes two and three. Coprime fixed-point lifting in F.3 explicitly excludes them. All surfaces in the mapping class arguments are oriented, and orientation-reversing maps are included only where the extended geometric group is specified. Real arithmetic, when used as a subgroup generated by complex conjugation, is not replaced by the finite-index number-field Galois group in the recognition arguments; nonorientable surfaces and real section problems are not claimed as consequences.

