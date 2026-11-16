# Consequences of the A1 proof: existence and module questions

Date: 16 November 2026. This note assumes the accepted AG.40–AG.42 proof chain and records its logical consequences. It does not edit the aggregate outcomes.

## Exact scope table

| Requested item | Consequence of A1 | What remains separate |
|---|---|---|
| A3, nontrivial rational relative class-number witness | A3 still implies A1 by the independently proved criterion. The new A1 proof does not establish its converse. | Universal existence of a nontrivial odd prime-to-p cover with p-unit relative class number remains unresolved. The literal degree-one convention is vacuous and must still be excluded. |
| A5, a cover with a point-separating family of maps to collision-free curves | The literal universal assertion is now true. Take the identity cover and the identity map to C, which is collision-free by A1 over every finite field of definition and extension. | Universal prime-to-p correspondences to supersingular curves, and membership in the closure generated solely by the old R4/R6 seeds, are not supplied by this argument. |
| A10(a), construction and additivity | The norm-module construction and its conditional additivity remain valid as proved. | Additivity for independently based towers still needs the specified path identification. |
| A10(b), collision produces a fixed free-orbit vector | The implication remains a valid structural statement. A1 says that no vector arising from a distinct pair of actual points occurs. | It is not a converse from arbitrary module elements to point-section collisions. |
| A10(c), no arbitrary fixed free-orbit vector for all genus-two curves in characteristic two | No new universal conclusion follows just from A1. | The all-curves assertion remains open; every original F_4-pointed pair is already settled by the independently computed L1 witnesses. |
| A10(d), rational tests as module projections | The proved projection and averaging statements remain valid. | Their universal existence is not established by eliminating point-origin vectors. |
| L5, collision-dependent correspondence implications | All such implications, including the unqualified effective-divisor equality, are now true by A1. | Their direct rational-field proof still requires the qualifications explained in AG.1. The independent universal supersingular-correspondence existence assertion in A5 is not thereby proved. |
| L8, Frobenius-orbit formula | The formula remains proved; the new A1 proof is independent of primitive rank-zero covers. | Nonordinariness alone remains an invalid replacement for nilpotence, and the universal nontrivial primitive-cover assertion is refuted by the explicit A6 example. |
| L11, ghost module | The module and the map from a collision to its compatible point differences are valid. The point-origin subcollection contains no nonzero collision class. | The slogan identifying A1 with absence of every arbitrary free-orbit element in M is not justified. The stronger module assertion has its own unresolved existence question. |

## 1. Why A3 does not follow

The relative class-number criterion kills an entire rational new p-primary subgroup. A1 proves that two actual points do not define the same section. These assertions have different objects and quantifiers. The cuspidal proof identifies points through finite covers, proper r-adic cohomology, and Kummer evaluations of functions. It never produces a new Jacobian factor with trivial rational p-torsion.

Thus the prompt's sentence “With A2 this is A1” is valid as a sufficiency statement, not as a proved equivalence. The odd-order solvability reduction still shows that a nontrivial constant-deck witness can be reduced to a prime cyclic witness, and the specially controlled nonconstant-deck reduction remains valid. Neither reduction constructs a witness on an arbitrary pointed curve.

The computed F_4 witnesses continue to settle the requested rational existence problem for all original F_4-rational pointed genus-two models. They are not consequences of the new cuspidal theorem and should retain their exact computational scope. A1 now covers all the other curves as point-separation statements, even where the requested least-prime witness computation remains unfinished.

## 2. A5 has two genuinely different existence assertions

For a curve over Fbar_p, choose a finite field of definition. A1 over every finite extension proves that the curve itself is a valid collision-free target. The identity family separates its geometric points. This is exactly the reverse implication already recorded in AG.2, so the literal first universal assertion in A5 is settled.

Even if a nonidentity cover were intended, choose any connected geometric cyclic étale cover of prime degree different from p, descend it to a finite field, and take its identity map as the point-separating target. Its genus is at least two, so A1 applies to it. This observation does not give a map to a supersingular curve or to a curve in a previously specified seed list.

The stronger supersingular-correspondence assertion therefore retains the status established by AG.9 and the specific positive families in AG.10–AG.14. Likewise, the statement that L6 reaches every curve from the old R4/R6 seeds is not a consequence of knowing that every curve belongs to the final collision-free class. Adding A1 as a new universal seed would make the closure statement tautological and would not answer the historical constructive question.

## 3. The norm module retains its point-origin restriction

The module M_P is an inverse limit of full Jacobian p-primary torsion groups. Its definition does not record that a coordinate is the Abel image of one point minus a chosen lift of P. A1 rules out compatible coordinates of the special form [Q_D-P_D] arising from one distinct point Q and compatible section paths. It places no immediate restriction on other compatible torsion vectors.

The proof of AG.40 also uses actual point labels at its decisive steps: a section comes from P or Q; finite neighborhoods carry actual points; and the final function has the divisor p^e(P-Q). An arbitrary element of M supplies none of these data. Substituting a module vector into that proof would lose the rational function and its controlled two-point divisor.

The exact sandwich AR.18 remains useful and unchanged. A relative rational witness with both source and base normal over C excludes all-normal free vectors. Conversely, nonexistence of those vectors implies a relative prime cyclic witness over a normal intermediate base, with source possibly nonnormal. Failure of every such hereditary relative test produces an actual fixed element in M_P[2] with all-normal free orbits. The construction does not produce a collision, so it is compatible with A1 being true.

Consequently neither A1 -> A10(c) nor A1 -> universal hereditary relative-witness existence has been proved. No actual curve carrying such an arbitrary module vector is asserted here either. Both overclaiming its existence and overclaiming its absence would exceed the proof.

## 4. Primitive covers and L8

The geometric orbit formula is independent of A1:

    f_p(P_n(D)) = sum over primitive p-orbits O of |O| times stable_rank(F^|O| on H^1(C,L^i)).

Stable rank zero, equivalently nilpotence, is the relevant annihilation condition. Noninvertibility of one map is weaker in dimensions greater than one. The actual cover counterexample in AG.11 and the exact linear example in AG.4 remain refutations of the proposed weakening. They are not examples of collisions.

The explicit A6 counterexample is especially important for scope: its Jacobian has p-rank zero, so it already satisfied A1 at the abelian level, while it has no nontrivial odd cyclic primitive-rank-zero cover. Thus primitive-cover existence cannot be inferred from point separation, even before the new universal theorem. The literal degree-one-permitted variant retains its separately stated caveat.

## 5. A weaker finite-cover existence statement that does follow

A1 does give a useful exact finite-quotient statement, substantially weaker than a class-number witness. Fix P in C(k). There is a geometrically connected finite étale cover D -> C over the original field k, with geometrically prime-to-p Galois group and a rational lift of P, such that no other point of C(k) has a rational lift to D. The geometric deck group need not be constant over k.

Here is the proof. Use s_P to write the arithmetic group as Delta semidirect G_k, with Frobenius automorphism alpha. For Q different from P write its Frobenius as a_Q F. Equality up to geometric conjugacy is the existence of g in Delta satisfying the corresponding alpha-twisted conjugacy equation. Since there is no solution by A1, compactness gives an alpha-stable open normal subgroup N_Q of Delta for which that equation has no solution in Delta/N_Q. Such subgroups are cofinal: a finite geometric cover has a finite Frobenius orbit, so intersect that orbit.

Intersect the finitely many N_Q. The pointed model D_N supplied by s_P has a rational point over P. Its Q-fiber has Frobenius action a_Q alpha on the finite geometric fiber Delta/N. A rational point in that fiber is exactly a solution of the excluded twisted conjugacy equation. Thus the image of D_N(k) in C(k) is {P}.

This statement concerns rational points on the cover, not rational p-primary points of its Jacobian. Extending constants to make all deck transformations rational can change its rational fibers, and the construction does not give a p-unit relative class number. It therefore does not resolve A3 or A10(c).

No aggregate claim or outcome was changed while preparing this note.

## 6. The complete L5 assessment, including its finite spectral test

The unrestricted implication from a distinct-point collision is now true because A1 excludes that premise. It should not remain marked OPEN merely because the original direct proof used deck translates that need not all be rational. The direct assertions and field qualifications in AG.1 remain useful explanations of what the rational projector itself proves without invoking A1.

The construction of the morphism C -> Sym^N(X_0), its nonconstancy when phi is nonconstant, and the fact that its equal-fiber locus is proper are already directly proved in AG.1. A nonconstant map alone is not a point-separating family.

The finite spectral test is correct in the following exact form. For a smooth proper D/F_q, its Jacobian has a nonzero supersingular isogeny factor if and only if one Frobenius eigenvalue alpha satisfies alpha/sqrt(q) in the roots of unity. One may test this on the numerator P_D(T). For a constant abelian cover, factor P_D into its character factors, including the trivial character if the entire Jacobian is being tested; the nontrivial factors test only the new part. For a constant nonabelian cover, use the full irreducible Artin factorization with the usual representation multiplicities. For a non-Galois cover, use its actual permutation representation or P_D directly. These formulations avoid an unsupported assumption that every cover has a one-dimensional character decomposition.

The supersingular equivalence follows by applying the Newton-slope criterion to the simple isogeny factors. Oort's authored chapter, sections 21.20 and 21.21(3), states exactly this criterion and its equivalence with geometric isogeny to a power of a supersingular elliptic curve. The opened final chapter is at https://math.nyu.edu/~tschinke/books/finite-fields/final/05_oort.pdf, PDF pages 61–62. Its publication identity and pages 123–188 are verified in the author's publication list at https://www2.ae-info.org/attach/User/Oort_Frans/Publications/oort_frans_publications.pdf, entry 100. The bibliography key is AC_Oort2008.

Here is an elementary finite stopping bound for the spectral test. Put h=g(D) and H_D(X)=X^(2h)P_D(1/X). Test whether

    gcd(H_D(X), X^(2n)-q^n) has positive degree

for each integer 1 <= n <= 8h^2. A positive test gives the required root of unity immediately. Conversely, if alpha has the required form, beta=alpha^2/q is a root of unity of some order n and [Q(beta):Q]=phi(n) <= [Q(alpha):Q] <= 2h. The elementary inequality phi(n)^2 >= n/2 follows prime by prime: the factor (l-1)^2/l is at least one for every odd prime l, and the possible l=2 factor is at least 1/2. Thus n <= 8h^2 and one of the finitely many tests succeeds. This is an exact algebraic test, requiring no numerical recognition of a root of unity.

The test concerns a fixed cover D. A supersingular factor supplies a nonconstant geometric map to a supersingular elliptic curve after finite extension, via the Jacobian and an elliptic isogeny factor. It does not automatically supply jointly point-separating maps, an étale cover with that factor, or the requested prime-to-p degree of such an as-yet-unconstructed cover. Accordingly the strongest accurate L5 outcome is: its collision implications and fixed-cover spectral test are proved; the associated universal supersingular-correspondence existence question stays open under A5.


## 7. Final section-origin advance and remaining existence gap

AC.45 now identifies M_P^F exactly with the Frobenius coinvariants of N^(ab,p), where N is the full geometric kernel discarded by prime-to-p completion. Every class has an actual full arithmetic section representative with the same geometrically prime-to-p projection as s_P. Nonzero classes are not point-theoretic: A1 identifies a hypothetical point with P, and ST Lemma1.7 then forces its geometric conjugator into N, where the class is a coboundary. This strengthens the understanding of the module without asserting free orbits.

The norm projections on rational p-primary groups are split surjective. Consequently M_P^F surjects onto J_C(k)[p-infinity], and it is often nonzero. The exact retained example y²+y=x+1/x+1/(x+1) over F2 has N1=N2=3, P_C(T)=1−T²+4T⁴ and J_C(F2)=(Z/2)². Its norm module therefore has actual nonzero non-point-theoretic full-section classes. All three point sections remain distinct. This is an actual-curve illustration of the distinction, not a free-orbit counterexample.

The explicit AG.38 geometric curve also sharpens the finite-prime limitation. For every finite list of odd primes, one may enlarge its finite definition field so that all geometric covers of those degrees are constant and P-split and each has a rational nonzero new two-torsion point. Uniqueness of the P-split cyclic twist exhausts the finite list. All listed degrees then fail (R) over every further extension. This does not exclude witnesses at other primes over that same field.

As of the final 12:30 progress assessment, no further finite argument toward universal A3 or all-level freeness has emerged. Fixed-r cuspidal recognition requires actual rational points in finite neighborhoods; a full arithmetic section supplied by AC.45 need not have that property. The hereditary relative-witness criterion and the scalar-Frobenius descent are exact reductions, but neither supplies the missing cover. The existing different-prime Iwasawa sources do not supply a bound on rational p-primary exponents for the changing Jacobians in the actual Abel tower. Continuing those routes would presently require a new existence or torsion theorem, not another census or a refinement of an already proved reduction.
