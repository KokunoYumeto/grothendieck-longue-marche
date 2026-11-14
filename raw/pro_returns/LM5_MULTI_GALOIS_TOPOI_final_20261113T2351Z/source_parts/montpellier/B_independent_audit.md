# Independent audit of B.3–B.8

**Outcome: passed, with three scope clarifications applied to `work/root/B.tex`.** The effective local group, comparison cone, full-inertia globalization, coefficient generality, and exceptional cases are mathematically consistent. This audit concerns the proof currently in that file, including the changes described below.

## B.3: effective image and the coefficientwise cone

The crossing biset is a transitive `(G × Q_s)`-set whose stabilizer is the closed image `K_s` of `(r_s,q_s)`. Replacing that stabilizer by `H_s` without controlling the kernel is precisely the erroneous step the new theorem avoids. A chain in the two-stratum category has at most one crossing. Its two strings of automorphisms give the two-sided bar construction, with coefficient value `M` at the target and the map from `N_s` induced by specialization. The crossing term is therefore the cochain complex of `BK_s` shifted by the crossing degree. This gives the displayed fibre sequence with the indicated signs and coefficient variance.

The profinite reduction also passes. A finite subset of a continuous torsion module lies in a finite invariant submodule: each orbit is finite and a finitely generated torsion abelian group of bounded exponent is finite. Finite triples and finite diagrams descend to common finite quotients. The coherent-limit continuity argument therefore applies first to finite objects and then to arbitrary discrete torsion objects. The topology induced on the closed subgroup `K_s` by finite quotients of `G × Q_s` is its full profinite topology; no injectivity of the original map from `H_s` is being assumed at this step. The fixed finite set of boundary points avoids an exchange involving infinite products.

On the geometric side, localization and henselian excision give the punctured term `RΓ(H_s,M)`. A strict henselian local scheme has an exact global-section functor because every covering of its terminal object admits a section; Galois descent restores `RΓ(Q_s,N_s)`. Comparing the two fibre sequences gives `Cone(K_s → H_s)[−1]`. The shift is confirmed by the one-cusp rational example: the missing inertia degree-one class appears in geometric degree two.

## B.4–B.5: counterexample and the open comparison

For the characteristic-zero pair `(P1,{∞})`, `G=Q=1` and the mixed topos is the arrow topos. Its global-section functor on abelian objects is evaluation at the source and is exact. The geometric degree-two Kummer class on `P1` is nonzero. This refutes the manuscript's proposition even though `A1` is a `K(π,1)`; the local hypotheses are independent of the open comparison.

The curve `K(π,1)` reductions cover all torsion coefficients. Affine geometric curves have torsion cohomological dimension at most one; finite degree-one classes are effaced by their torsors. For proper positive-genus curves, prime-to-characteristic degree-two classes are killed by finite étale covers of appropriately divisible degree. In characteristic `p`, Artin–Schreier and the surjectivity of `F−1` on coherent degree-one cohomology kill degree two, including the genus-zero case. Compatible Hochschild–Serre sequences descend the result to the ground field. Filtered unions account for infinite discrete torsion modules.

A wording clarification was applied: when a smooth curve is connected but not geometrically connected, first regard it over the finite separable algebraic constant field in its function field. This makes the written Hochschild–Serre reduction applicable without changing the scheme's étale topos or its fundamental group.

## B.6: full wild inertia and tame inertia

The finite-germ domination criterion is exactly the criterion for a closed embedding of profinite groups. Both cyclic globalization constructions are valid. Prime-to-characteristic local cyclic extensions are determined by their valuation class. Two cusps permit the Picard-divisibility Kummer construction; one cusp on a positive-genus curve permits a finite unitriangular quotient whose peripheral commutator has the desired order.

For a cyclic degree-`p` germ, the principal-parts sequence and surjectivity of `F−1` on `H1(O)` supply a global Artin–Schreier function with the prescribed local class. The principal parts at other cusps are changed only by Artin–Schreier coboundaries; the integral local remainder is also a coboundary over the strict henselian local ring. No extra branch point in the open curve is introduced.

Every finite local Galois group is a wild `p`-group extended by a prime-to-`p` cyclic group and is therefore solvable. A cyclic-prime-degree tower can consequently be globalized successively. If an auxiliary global cover was used, composita with the next local step remain cyclic or trivial; this is the necessary bridge that avoids requiring an exact initial globalization. The Artin–Schreier positive-genus cover of `A1` provides that bridge in the exceptional initial case. Subsequent separable covers preserve positive genus, or preserve the existence of two boundary points. Thus the argument applies at every induction step. Completion versus excellent henselization does not alter the finite-extension category. Full inertia is injective for every affine curve in characteristic `p`; tame inertia retains the one-cusp rational exception.

## B.7–B.8: arithmetic and exact exceptions

The full-group exception table is correct: proper geometric genus zero with empty boundary in every characteristic, and the one-puncture rational pair in characteristic zero. The former defect is `RΓ(k,M^(p′)(−1))[−2]`; the latter is `RΓ(k,M(−1))[−2]`. These cones do not require a splitting of the structural derived direct image. In particular the nonsplit real-conic example correctly has its first failure in degree three, although the relative cone starts in degree two. No full-group exception remains for `p`-primary coefficients in characteristic `p`.

For arbitrary imperfect ground fields, a clarification now explicitly passes to the perfect closure and takes the reduced boundary. Purely inseparable invariance preserves the étale sites and local finite-cover categories. The remaining residue fields are finite separable, their Galois groups embed in the ground-field group after a choice of embedding, and the kernel of `(r_s,q_s)` is the geometric inertia kernel controlled by B.6. This supplies the precise descent behind the original short argument.

The tame prime-to-`p` comparison is also valid: after trivializing a tame local system, a torsor under its prime-to-`p` additive group remains tame, since wild inertia has no nontrivial homomorphism to that group. The tame exception has now been phrased geometrically, `(X_kbar,(S_kbar)_red)=(P1,{∞})`. Over an imperfect field it can include a nonsplit genus-zero curve with one purely inseparable boundary point; it need not be the split pair over the original field. Finally the explicit `A1` Artin–Schreier counterexample now assumes the ground field algebraically closed when calling its tame group trivial. The class of `x` is nonzero by the displayed degree argument.

No further mathematical obstacle was found in B.3–B.8. These are proof and scope checks; no new numerical test was needed or used to replace an infinite argument.
