# Part 4: mathematical and source audit

This contribution contains nine numbered statements in sections/boundary.tex, with one matching row per statement in boundary_results.csv. The final reconstruction includes the full étale-stack scope, the simultaneous-coordinate admissibility lemma, the degree-zero support check, the explicit connectedness needed by reduced H^0, and the good projective product examples.

## Scope and corrections

P4a1 gives a free C2 quotient of C4 times C* whose rank-3/2/1 component flags violate the Segal identity. One selected composable pair has two triple components with two distinct composites. The internal analytic category is sound; taking components does not preserve its fibre product.

P4a2 retains every full strict flag before taking components. Its semisimplicial realization is the barycentric subdivision of the ordinary coarse symmetric-delta complex. The actual closed oriented face is formed as a geometric fibre product before taking homotopy types. Full étale Čech descent retains arbitrary discrete inertia. Functors have groupoid target Pi_infty(Delta); their categorical fibres are defined in infinity-categories, and only their groupoid completions are identified with spatial homotopy fibres. The left Kan extension formula includes paths and coherences and is not a single-stratum assertion. A constant BH gerbe leaves coarse component data unchanged and adds BH to the diagrams, total homotopy types, and fibres.

P4b distinguishes D from U_infty. Contractibility of closed normalized intersections proves D equivalent to Delta. A nonempty compact oriented link has nonzero rational cohomology in degree 2n-1, whereas Delta has dimension at most n-1. Proper finite orbifold stabilizers, including ineffective ones, do not remove this obstruction. No finite-inertia condition is inserted into the first, purely homotopy-colimit assertion.

P4c1 requires simultaneous normal-crossings coordinates for the smooth centre. For a connected nonstratal centre, at least one centre coordinate is nonboundary everywhere; hence no deeper stratum component is contained in the centre. The usual deletion set Delta_Z^0 is therefore empty in this case. Disconnected centres are handled componentwise. Components of D_sigma intersect Z agree with the corresponding components for sigma union R; the exceptional coface with all containing branches is a projective-space bundle of dimension s-1. This proves compatibility of the barycentric contraction with disconnected intersections and branch permutations. The analytic weak-factorization consequence is restricted to compact complex manifolds with a bimeromorphic extension of the specified open isomorphism. Proper algebraic DM independence uses Harper, including boundary roots.

P4c3 refutes unrestricted analytic independence, even for good pairs. The toric compactification of (C*)2 has square dual and link T3. The Jordan Hopf quotient g(z,w)=(alpha z+w,alpha w) has elliptic boundary and point dual. The correct coordinate is u=alpha z/w; then g acts by (u,v)->(u+1,alpha v). The invariants exp(2 pi i u), v exp(-u log alpha) identify the complement with (C*)2. The meridian has winding vector (0,1), so injects. The normal coordinate w/z has transition alpha*t/(alpha+t), with derivative one; the link is again T3.

P4c2 gives all nonnegative degrees of the weight-zero link comparison. Support duality gives weights of H_D^a(X) at least a, but at a=0 that bound alone is insufficient: H_D^0(X)=0 is separately proved. The compact-support formula is reduced in degree one and explicitly assumes X connected, or is applied componentwise relative to H^0(X). Tubach supplies the stack Hodge formalism, proper purity, duality and weight compatibility. No unrestricted analytic mixed-Hodge comparison is claimed.

P4d1 uses ordinary simplex quotients for tropical links. Graph automorphisms are retained in a graph category, which computes a different object: at (1,1) that category is BC2 while the coarse link is a point. The no-edge graph belongs to the full tropical cone and is excluded from the length-one link.

P4d2 identifies every simplex and face with a laminar family and gives the complete inverse tree construction before applying the verified Whitehouse-complex theorem. The finite computations are exact over the integers. They are not computations of the infinite P_k of Part 5.

P4e now includes good projective examples: X_g=C_g times B, D_g=C_g times {p}, with B elliptic and g=1,2. The puncture meridian is a nontrivial commutator in a free group and injects. Both duals are points, but the links C_g times S1 have b1=3,5. The line/conic comparison separately isolates normal Euler numbers 1,4; no goodness claim is made for those plane pairs.

## Executed computations

The restored Python and JavaScript programs were rerun successfully in the restored VM on 12 November 2026. Their full outputs are in code/boundary_checks_output.json and code/boundary_analytic_checks_output.json.

The Python program computes the face vectors (3), (10,15), (25,105,105); constructs signed integer boundary matrices; checks that their composition is zero; contracts a spanning forest; and computes the Smith normal form over ZZ. For n=6 the projected matrix is 81 by 105, and all 81 nonzero Smith entries are one. Thus H1=0 integrally and H2=Z24. For n=5 H1=Z6; for n=4 reduced H0=Z2. It also verifies the component-Segal orbit counts, the loop-graph C2 automorphisms and bar differential, and the two normal-bundle cokernels.

The JavaScript program uses exact rational arithmetic at alpha=1/2. It checks the affine shift u'−u=1, the normal derivative, the primitive nonzero meridian vector supplied by the analytic proof, the square versus point graph homology, and the binomial homology ranks of T3. It does not pretend to establish the analytic quotient by numerical sampling.

## Manuscript readings

The original scan MPL_149_091-136_scan133.jpg was visually inspected before the outages. On folio 66 the final U_infty is legible and is retained. The inserted maquette and overwritten solide wording does not license silently changing U_infty to D. The replacement D is explicitly marked as a mathematical correction.

MPL_147_048-137_scan114.jpg was rechecked against official MPL147 PDF page 114 on 13 November 2026. Folio 56 is visibly written at the top; the printed scan footer is 113. Formula (169) gives the objects, arrows, source/but, identity and fibre-product composition of a structure de categorie analytique. Section 11 is retained only as the task indexing, since no section heading appears on this page. The overwritten opening descent terminology and marginal annotations remain unresolved. The internal analytic construction is retained: P4a1 challenges the subsequent inference after applying pi0, not the underlying composition.

## Verified primary references and exact locations

1. Payne (2013), Boundary complexes and weight filtrations, Michigan Mathematical Journal 62(2), 293–322. DOI 10.1307/mmj/1370870374. Theorem 1.1; Proposition 4.2; Theorem 4.4; Stepanov's lemma and Remark 5.1, published p.307. Original PDF opened repeatedly, including the final admissibility audit: https://web.ma.utexas.edu/users/sampayne/pdf/BoundaryComplex.pdf . Final retrieval refs turn114view0, turn115view0–1.

2. Thuillier, preprint 10/2006, 28 July 2006. Theorem 3.25; Proposition 4.5; Theorem 4.6, application pp.41–44. DOI 10.5283/epub.561. https://epub.uni-regensburg.de/561/1/10-2006.pdf . Checked refs turn15view0, turn16view0; metadata turn90view3. The journal article, Manuscripta Mathematica 123(4) (2007), 381–451, DOI 10.1007/s00229-007-0094-2, was checked for publisher metadata and abstract. The preprint theorem numbers are not presented as verified journal numbering.

3. Abramovich, Karu, Matsuki and Wlodarczyk (2002), Torification and factorization of birational maps, JAMS 15(3), 531–572. DOI 10.1090/S0894-0347-02-00396-X. Theorem 0.3.1, including compact complex manifolds and clause (6). https://personal.math.ubc.ca/~karu/papers/semist.pdf . Refs turn13view0, turn15view1.

4. Harper (2017), Factorization for stacks and boundary complexes, arXiv:1706.07999. Theorems 1.1–1.2; characteristic-zero scope in section 1.4; Definition 2.1.4. https://arxiv.org/pdf/1706.07999 . Initial refs turn28view0, turn29view2; reopened turn116view0 confirms that the common open may itself be a stack.

5. Durfee and Saito (1990), Mixed Hodge structures on the intersection cohomology of links, Compositio Mathematica 76(1–2), 49–67. Definitions 2.7–2.8; Propositions 2.9, 3.5. https://www.numdam.org/item/CM_1990__76_1-2_49_0.pdf . Refs turn13view1, turn16view1, turn40view1; metadata turn90view1.

6. Chan, Galatius and Payne (2021), Tropical curves, graph complexes, and top weight cohomology of M_g, JAMS 34(2), 565–594. DOI 10.1090/jams/965. Definition 5.2, Lemma 5.4, Corollaries 5.6–5.7, Theorem 5.8, pp.586–588. https://web.ma.utexas.edu/users/sampayne/pdf/TopWeightCohomologyOfMg.pdf . Refs turn42view0, turn43view0–2.

7. Abramovich, Caporaso and Payne (2015), The tropicalization of the moduli space of curves, Annales Scientifiques ENS 48(4), 765–809. DOI 10.24033/asens.2258. Theorem 1.2.1; Corollary 7.2.2; section 7.3 in arXiv v2. https://arxiv.org/pdf/1212.0373 . Published metadata: https://www.numdam.org/item/ASENS_2015__48_4_765_0/ . Refs turn29view1, turn39view0, turn40view2, turn25search0.

8. Readdy (2005), The pre-WDVV ring of physics and its topology, Ramanujan Journal 10(2), 269–281. DOI 10.1007/s11139-005-4850-1. Unnumbered definition in section 2, preprint p.3; Theorems 4.7 and 5.2. It is not Definition 2.2. https://arxiv.org/pdf/math/0511420 . Author metadata https://www.ms.uky.edu/~readdy/papers.html . Refs turn25view1, turn28view2, turn40view0, turn41search3.

9. Feichtner (2006), Complexes of trees and nested set complexes, Pacific Journal of Mathematics 227(2), 271–286. DOI 10.2140/pjm.2006.227.271. Theorem 3.1; Corollary 3.2. https://msp.org/pjm/2006/227-2/pjm-v227-n2-p02-s.pdf . Refs turn25view0, turn28view3.

10. Ueda (1979), Compactifications of C times C* and (C*)2, Tohoku Mathematical Journal, Second Series 31(1), 81–90. DOI 10.2748/tmj/1178229879. Theorem 2 p.81; section 4(d) and (e) p.88; Proposition 3 pp.89–90. Publisher metadata https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_81/_article/-char/en . Original paper inspected at https://scispace.com/pdf/compactifications-of-c-c-and-c-2-29mxk57nsw.pdf . Refs turn77view0, turn78view0–1. The Hopf example is type (1); the ruled elliptic/Serre example is type (2).

11. Tubach (2025), Mixed Hodge modules on stacks, Forum of Mathematics, Sigma 13, e175. DOI 10.1017/fms.2025.10122. Theorem 4.1.1; Propositions 4.2.5–4.2.6, 4.3.5–4.3.6; Corollary 4.3.7. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EA17D66A509792ECFF343C8060554F99/S2050509425101229a.pdf/mixed-hodge-modules-on-stacks.pdf . Refs turn61view0, turn62view0–3, turn63view0–2.

## Additional comparison not needed in the numbered counterexample

The ruled elliptic/Serre model uses (z,w) modulo (z,w)~(z+1,w) and (z,w)~(z+i,w+1), with w in P1. The infinity section has point dual and trivial normal line. On its complement the functions exp(2 pi i (z−iw)) and exp(2 pi i w) identify the analytic open with (C*)2. Its meridian is killed by the affine-line fibre, so this completion is not good. Ueda's type (2) verifies the classification context. The Jordan Hopf example used in P4c3 is stronger because both compared completions are good.

No priority claim is made for the standard dual-complex, tropical, or weight results. The concrete counterexamples, precise hypothesis distinctions, and independently executed finite checks are explicitly separated from the cited known theorems.
