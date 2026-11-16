# Independent review of AG.39

Reviewer: F agent, 16 November 2026. Reviewed the complete file `agent_geometric/configuration_proodd_obstruction_draft.tex`. No mathematical gap found. Two missing LaTeX backslashes before `longrightarrow` in the initial draft were reported to its author.

## The completion argument

The normal-core qualification is essential and is supplied by the construction. If H is a subgroup of E containing K normal in E with finite odd quotient E/K, and N is normal of odd index in H, then N∩K is normal of odd index in K. Its E-conjugates are indexed by the finite quotient E/K. Their intersection L is normal in E, K/L embeds in a finite product of odd groups, and E/L is odd. Thus the topology induced from the pro-odd completion of E is the full pro-odd topology on H. An arbitrary subgroup of odd index would not suffice; the draft correctly uses a three-group Galois core.

The total cover and its fiber cover both have such a core, since their towers have three-group Galois closures. The fiber subgroup is the intersection of the covering subgroup with the original fiber subgroup. Consequently an injection for the original completed fiber induces an injection of the completed punctured fiber of S° into the completed total group of S°. The finite covering/fibration identifications, not a general left-exactness assertion, establish this step.

The discrete punctured fiber group is normal in the discrete total group. Its image is dense in the injected completed fiber, and the discrete total group is dense in its completion. The completed fiber is therefore a closed normal subgroup K of the completed total group H. Both compactness and the assumed injection are used here.

For an odd prime ell, let N be the kernel of the quotient K→H1(S_z,F_ell), where S_z is the compact fiber. Monodromy preserves the peripheral conjugacy classes, so the dense discrete total group normalizes N. The subgroup N is closed in the compact K and hence in H; its normalizer is closed. Therefore all of H normalizes N.

The resulting action H→Aut(K/N) is continuous. One can see this without even invoking finite generation: choose finitely many representatives for the finite quotient K/N. For each representative k, the map h↦hkh^{-1} is continuous into K, and its composite to K/N is continuous. The finite intersection of the stabilizers is therefore open. A continuous finite image of a pro-odd group has odd order.

Finally the discrete total group surjects onto pi1(B), and conjugation by the fiber acts trivially on its compact abelian homology. Thus the action just constructed is exactly the usual mod-ell monodromy representation of pi1(B), not a smaller auxiliary image. Density identifies its image with that of H. This is the central passage requested for independent review, and it is sound.

## Geometry and the contradiction

The diagonal pullback has three disjoint graph components because the mod-three homology cover factors through the cyclic degree-three cover. In the Kunneth decomposition of its mod-three divisor class, both degree-two terms vanish by the covering degrees and the cross term vanishes because the mod-three homology cover kills H1(C,F3). Integral cohomology is torsion-free. The Lefschetz (1,1) theorem and divisibility of Pic0 then give the required cube root line bundle.

The local equation w³=t gives a smooth cyclic cover and a smooth fibration over B. The three reduced branch points make every fiber connected. Riemann--Hurwitz gives g(C')=3g−2 and g(S_z)=9g−5. The punctured fiber has three punctures and its degree over C minus one point is nine.

Nonisotriviality follows from the finiteness of degree-three maps from a fixed genus-(9g−5) curve to C'. The fixed-degree Hom scheme is of finite type, and all its tangent spaces vanish because the pulled-back tangent bundle of C' has negative degree. The branch sets vary through the surjective map B→C. Hence the fibers cannot all be isomorphic.

Oddness of every finite mod-ell monodromy image gives solvability by Feit--Thompson. The uniform derived-length bound for linear groups is independent of the field. Thus one fixed derived subgroup of the integral monodromy reduces to the identity modulo every odd prime and is itself trivial. Deligne then forces finite monodromy: a solvable algebraic group with semisimple connected component has trivial connected component. Trivializing the finite integral local system on a finite etale cover produces a period map from a compact curve to a bounded realization of Siegel space, which is constant. Torelli contradicts the established nonisotriviality.

I independently opened Newman's primary digitization, Section1, printed p59, which states precisely the field-independent bound used here: https://gdz.sub.uni-goettingen.de/fulltext/PPN266833020_0126/00000065?_format=xml . I also independently opened Deligne, *Théorie de Hodge II*, Corollary4.2.9(a), printed p48: its hypotheses are a smooth connected separated complex base and a proper smooth morphism; the identity component of algebraic monodromy is semisimple. URL: https://www.numdam.org/item/PMIHES_1971__40__5_0.pdf . Both match this family.

## Specialization and scope

The pointed curve and the product with diagonal form smooth proper pairs with relative normal-crossing boundary. The prime-to-two specialization comparison is therefore the appropriate one, and the inclusion x↦(x,P) is compatible with it. The argument uses the Hodge-theoretic contradiction only in characteristic zero, then transfers the completed fiber-inclusion map through the functorial specialization diagram. The explicit y²+y=x⁵ model has the stated smooth infinity chart v²+u³v=u.

The conclusion concerns injectivity after completing the entire configuration group to pro-odd. It does not replace the full tame base by its pro-odd quotient without explanation, and it does not imply a collision of point sections. In particular this is a refutation of the proposed configuration exactness route, not of A1 itself. No individual finite monodromy matrix or explicit profinite kernel element has been computed in this review.

## Independent review of the all-primes extension

Reviewed the complete `agent_criteria/configuration_all_primes_extension.tex` after the original pro-odd argument. Verdict: **passed, no mathematical gap found**.

### Congruence lemma

The finite-index subgroup in the connected Zariski component is finitely generated and dense. For the simply connected central covering, the connecting map to H1(Q,Z) is genuinely a homomorphism: when rational elements are lifted, the two cocycles multiply because their values lie in the central finite kernel. The cohomology group is abelian of exponent dividing the order c of that kernel. The image of a finitely generated group is therefore finite. Choosing rational lifts of generators of its kernel gives a finitely generated subgroup mapping onto that kernel. Its Zariski closure surjects under the finite isogeny, and dimension plus connectedness gives density in the entire simply connected group.

Spreading out the group, central isogeny and both faithful representations after finitely many primes is legitimate. The finite-field comparison kernel has order at most c, and the comparison gives the original matrix reduction of the finite-index subgroup, not an unrelated representation.

I independently opened the primary Nori paper, *On subgroups of GL_n(F_p)*, Inventiones88(1987),257–275, through its full digitized author text at https://www.academia.edu/106966459/On_subgroups_ofGL_n_F_p_. Section5, printed273–274, defines R=Z[S^-1] and its product of local integer rings. Theorem5.4 on printed274 states the required congruence openness when the complex algebraic group is connected and simply connected. This is exactly the hypothesis of the simply connected semisimple covering used here. Web source references: turn522view0, turn523view0. The source is directly checked, rather than inferred from a secondary citation.

An open subgroup of that compact product contains every factor outside a finite set. Smoothness makes reduction onto the finite-field group surjective, hence the generated group has full reduction at all remaining primes. A finite Galois splitting field containing the needed p-power roots of unity gives infinitely many split primes. The included elementary proof of this weak splitting assertion is correct: f(b+dRt)/d is an integer polynomial congruent to1 modulo every prime in R; assuming only those prime divisors forces its absolute value to be1, contradicting nonconstancy. Outside the discriminant and index, a polynomial root gives residue degree1; Galoisness makes the rational prime completely split. The split positive-rank torus supplies the asserted p-power divisibility, and the central comparison loses at most v_p(c). This proves arbitrarily large p-parts for the original congruence images.

### Family and group topology for general p

Taking r=2 for odd p and r=3 for p=2 works without any new parity obstruction. The two Kunneth degree terms are divisible by r and the full mod-r homology cover kills the cross term. Torsion-free integral H2, Lefschetz(1,1), and Pic0 divisibility give the rth root of the branch-divisor line bundle. Its branch divisor is a disjoint union of r sections, so the cyclic cover is smooth with connected smooth fibers. Riemann–Hurwitz gives the displayed fiber genus. The finite-Hom argument still proves nonisotriviality.

Both total-space and fiber towers have r-group Galois cores. The induced pro-p′ topology argument needs, and has, a normal subgroup of prime-to-p index; oddness or solvability is not used. Under the assumed fiber injection, compact homology with F_ell coefficients, ell≠p, is a finite quotient of the closed normal completed fiber. Its monodromy-invariant kernel is normalized by the entire completed total group by density and closedness. The resulting continuous finite action has prime-to-p image. Because the discrete total group surjects onto pi1(B) and the fiber acts trivially on its own abelianized compact homology, this is exactly the reduction of the integral family monodromy.

Deligne gives semisimple connected algebraic monodromy. It is nontrivial by the already verified compact period-map/Torelli argument. The congruence lemma therefore contradicts the prime-to-p orders. Finally, pointed-curve lifting and functorial prime-to-p specialization for the two smooth proper pairs transfer the noninjectivity to characteristic p; the Hodge argument is used only on the characteristic-zero lift. The extension produces no point collision and asserts no solution of A1.

## Source conflict discovered during the Green-route review, 11:35 UTC

A material source conflict is now under active review. Mochizuki's older author version of *Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves*, printed11, defines the geometric configuration group as the maximal cuspidally pro-Sigma-dagger quotient of the maximal pro-Sigma tame geometric group. With Sigma=Sigma-dagger=all primes other than p, this is literally the full pro-p′ configuration group. Proposition1.6(ii), printed14–15, then identifies the inverse image of a point decomposition group with the full punctured-curve group, citing a homotopy exact sequence. This appears to conflict with AG39. I directly opened both the conventions and the proposition; retrieval references turn555view0 and turn555view1. The geometric agent reports the current87-page author version and February2014 comments retain the corresponding assertion.

This conflict is not silently resolved by changing the group completion. The intended all-primes Green application is on hold until the actual source scope is reconciled. A renewed independent check of the AG39 construction still finds no error: the root line bundle exists by integral divisor divisibility; the punctured tower has an r-group Galois core; the assumed injection embeds the completed punctured fiber as a closed normal subgroup; a monodromy-stable finite homology quotient then carries a continuous action of the pro-p′ completed total group. The finite action is therefore prime to p, contradicting the independently checked semisimple monodromy/strong-approximation argument. The source conflict is nevertheless a concrete unresolved audit issue and should be retained explicitly in any resulting source discussion.
