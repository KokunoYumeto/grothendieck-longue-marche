# Independent review of F.49: small geometric extensions

Reviewer: finite-field agent, 14 November 2026.

**Verdict: PASS in the complete stated sufficient scope.** I read all nine sections of audit/F_small_geometric_extension_candidate.md, checked its use of the integrated F.32, F.40, F.45 and F.46 arguments, and independently reopened the precise Hilbertian sources. No integrated F source was changed.

There is one bibliographic presentation correction, already sent to the author: small Galois extensions of Hilbertian fields are known to be Hilbertian. The candidate's Section6 gives a valid constants-sensitive proof of this input; it should not be presented as a new preservation theorem. The exact current Bary-Soroker version numbers it Theorem4.4, not Theorem12.

## 1. Stated scope and normal descent

The assumptions that D is finitely generated over Q with positive transcendence degree, that k/D is algebraic Galois, and that Qbar is contained in k are used separately. They ensure, respectively, positive geometric dimension for the moved-prime argument, normal arithmetic descent, and all roots of unity. Smallness is a sufficient hypothesis for the Hilbertian input, not an asserted necessary reconstruction condition.

For L finitely generated over k, a finite list of data lies in one finitely generated F/Q with D contained in F and L=Fk. Normality of k/D makes L/F Galois. This is the required normality of G_L inside G_F; it is different from the later geometric group over B=FQbar.

## 2. The weaker divisible-kernel statement

For finite E/k, one finite Galois M/D can contain the finitely many E-generators and the chosen element a while satisfying E contained in Mk. For sigma fixing k and tau fixing M, both preserve the other defining field and commute on M and k. Since sigma fixes all roots of unity, sigma(z_n)/z_n is fixed by Gal(Mk/M), hence belongs to M. Its n-th power is sigma(a)/a. The finitely generated field M has trivial infinitely divisible multiplicative subgroup, so a is fixed by Gal(Mk/k) and belongs to k.

For a finitely generated E/k, a proper normal model over its finite relative constant field k1 first makes a and every chosen root z_n constant: their prime-divisor valuations all vanish. Thus a lies in D(k1*), to which the finite-extension statement applies. The candidate's abbreviated model argument is valid; explicitly mentioning the roots as well as a is a useful optional clarification.

Only D(E*) contained in k* is proved or needed. No assertion that every element of k* is divisible is used later.

## 3. Finite-quotient detection

Hilbertianity passes to finite extensions, while a finitely generated extension of positive transcendence degree over any base is Hilbertian. Consequently every L under the core hypothesis and each finite extension of L has the required specialization property and a nontrivial finite separable extension.

For a curve, Riemann–Roch supplies rational functions of unbounded degree; an arithmetic progression of available degrees suffices if the curve has no rational point. The connected composite Y to P1 has its full arithmetic degree. Hilbert specialization of that connected finite cover gives a field of degree d|G|. The free G-action on the etale fibre then gives a quotient point of degree d and a connected G-fibre of degree |G|. Arithmetic constants are retained. Higher-dimensional detection uses the already proved cover-preserving curve construction with its stated open restrictions.

## 4. Integral Kummer residues

The nontrivial finite extension of L descends after enlarging F, and a finite normal M over a rational-function field contains its defining roots and all puncture data. Thus Mk/L is finite Galois and nontrivial. A nonidentity sigma fixes Qbar, preserves M and acts nontrivially on its geometric function field, exactly as required by the moved-divisor lemma.

After approximation, a single finite S0/D inside k suffices to contain all coefficients of the actual value b_alpha. Because sigma fixes k and preserves M, F'=MS0 also contains sigma(b_alpha). It is independent of the Kummer level n. For roots of an element a of F', the same commuting-automorphism calculation places sigma(z)/z in F'. Applying v_i composed with N_(F'/M) therefore gives the simultaneous integral congruences for [F':M]lambda_i. The passage from an integer multiple in Z to lambda_i in Z inside Zhat is valid prime by prime. No ramified prolongation is silently treated as integer valued.

## 5. Actual point functions need only the inclusion

The generalized Albanese, spanning finite-quotient and finitely generated Tate-Hom arguments use normality, roots of unity, finite actual values and the newly proved residue integrality. The constant Kummer class at the basepoint can be subtracted even though k* is not divisible. The previous unit reconstruction therefore gives xi=kappa(h), with h normalized at x0.

The remaining equality phi(x)=c_x h(x) uses only c_x in k*. For a nonconstant curve function, points of sufficiently large degree have h(x) outside L and therefore outside k. Pulling back T-1 and using one point above the combined pole bound gives an exact affine function identity h1=A h+B with A,B nonzero in k. Comparing all points whose h-value is outside k forces the same scalar c=-A/B. Translating by every b in k* supplies h_b=e_b(ch-b). If h(x) belongs to k, choosing b=ch(x) and using invertibility on the inverse-image open forces phi(x)=ch(x). Basepoint normalization gives c=1.

In the constant case, beta can be chosen outside L in a finite extension L'. Then beta/h is outside k. The inclusion in the divisible-kernel lemma places every phi(x) in h*k, so beta is missed. The inverse-image open for T-beta is therefore the whole source. Its recovered unit takes values in L'; unbounded point degrees make that unit constant. The two scalar relations in k force phi(x)=h. This uses no ability to extract arbitrary radicals in k.

On higher-dimensional sources, the curve comparison has equal Kummer classes. The ratio unit has zero divisor, hence is constant, and its value1 at x0 makes it1. The final full-topos implication is the already checked CHW4.18(5) statement, not a replacement of topoi by fundamental groups.

## 6. Bounded-degree compositum and specialization

Smallness passes to open subgroups and quotients in the ways stated. Since B/K0 is finitely generated, k intersect B is finite over K0. The geometric group Gal(L/B) is thus an open subgroup of the original small group.

For a descended cover and degree D0, finitely many subfields of L/B have degree at most D0. Their finite normal closures remain inside L because L/B is Galois; their compositum S/B is finite Galois. Connectedness over L implies connectedness after base change to S. The complete cover Y_B times S to P1_B therefore has a full-degree Hilbert specialization of degree D0[S:B]. Its residue field is the compositum ES, where [E:B]=D0 and E is linearly disjoint from S.

The field E intersect L has degree at most D0 and is one of the subextensions absorbed into S. Hence E intersect L=B. Since L/B is Galois, this implies E and L are linearly disjoint over B. The quotient point degree d and the G-fibre degree |G| survive. This is the exact intersection argument needed here; merely choosing a specialization disjoint from the cover's constant field would not suffice.

Applying the same proof to the Galois closure of an arbitrary irreducible separable polynomial over L(T) proves Hilbertianity. Every coefficient descends after a finite enlargement. The separate finite-quotient argument therefore agrees with the known general preservation theorem.

## 7. Subfields: a quotient, not an arbitrary closed subgroup

For a positive-transcendence subfield k0, take a finite transcendence basis T and A=Q(T). The relative algebraic closure R of A in F is finite over A, and F/R is regular. Every R-conjugate of Rk0 extends uniquely over the regular base F and lies in the normal extension L/F. Thus the possibly infinite normal closure N/R lies inside L.

Regularity survives the algebraic constant extension: FQbar/RQbar is regular. Since NQbar/RQbar is algebraic, its intersection with FQbar is exactly RQbar; indeed the two are linearly disjoint over that base. Hence Gal(NQbar/RQbar) is the Galois group of its compositum with B over B, a quotient of Gal(L/B). This proves smallness without invoking inheritance by arbitrary closed subgroups.

NQbar/R is algebraic Galois, R is finitely generated of positive transcendence degree, and NQbar/k0 is algebraic. The core theorem and F.32 consequently apply in the stated direction. Algebraic subfields such as Qbar are correctly excluded from this conclusion.

## 8. Both strict examples

For the polynomial family, direct differentiation gives P'_m=(2m+1)(X^m-1)^2. At a critical root zeta, its value is 2m^2*zeta/(m+1), so finite branch values are distinct and every finite inertia is a single3-cycle. Infinity has odd degree2m+1. The geometric group is transitive and generated by conjugates of those finite inertia cycles; a nontrivial quotient unramified except at infinity cannot exist in characteristic zero by Riemann–Hurwitz.

The support-hypergraph proof of alternating monodromy is sound. A triple adding one new vertex enlarges the alternating group; a triple adding two new vertices and a conjugate moving its shared old vertex give A4, reducing to the one-new-vertex case. Thus the group is A_(2m+1). Pairwise nonisomorphic nonabelian simple groups have no common nontrivial quotient with the product of the preceding groups, proving the claimed finite-level linear disjointness and infinite product.

For each finite index d, a continuous action on d points kills every simple factor larger than d!. Continuity kills their whole product, not just its dense direct sum. Only finitely many factors remain, proving smallness. Every open subgroup contains the entire tail and therefore has alternating quotients of unbounded degree. F.46's equivalent algebraic-model description permits the stated strictness argument after adjoining Q(t) to any proposed model; its geometric group becomes an open subgroup of this product, contradicting virtual pro-formation bounds.

The alternative tripod example communicated by the topos agent is also sound: take the maximal extension of Qbar(t) unramified over P1 minus{0,1,infinity}. Its group is the free profinite group on two generators. The rational branch locus makes this field normal over Q(t). Finite generation makes the group small; every open subgroup is free of rank d+1 at index d and has alternating quotients of arbitrarily large odd degree. Hence the same changed-model argument proves strictness. This example uses the standard characteristic-zero etale/topological comparison and free-group presentation already available in the bundle. The explicit polynomial example supplies an independent algebraic realization with its own direct group proof.

## 9. Primary-source reopens and attribution

* Bary-Soroker, *On the characterization of Hilbertian fields*, arXiv0803.0451v3,12June2012: Section4 Definition4.1 and Theorem4.4, authorpp8–9, with complete proof and Remark4.5. Opened https://arxiv.org/pdf/0803.0451 as turn884view0 and turn885view0–1. The versioned URL itself returned a disabled-fetch error; the unversioned URL's displayed header explicitly identifiesv3. The theorem is known and itself cites Fried–Jarden16.11.1.
* Bary-Soroker, Fehm and Petersen, *Hilbert properties under base change in small extensions*, arXiv2312.16219v1,24December2023: Theorem1.2, authorp1, and Corollary4.3 with the preceding bounded-degree compositum proof, authorp5. Opened https://arxiv.org/pdf/2312.16219 as turn884view1 and turn885view2–3. Its scope allows small algebraic extensions and is stronger than the Galois P1 case required here.
* Bary-Soroker and Paran, *Fully Hilbertian fields*, primary https://arxiv.org/pdf/0907.0343, Theorem1.2, authorp2. Independently opened turn883view2. It supplies the positive-transcendence finitely generated Hilbertian input.
* Serre, *Topics in Galois Theory*, second edition: Corollary3.2.2, printedp22; Proposition3.3.1, p23; polynomial interpretation Proposition3.3.5, p24. Independently opened the primary CNRS-hosted PDF as turn883view3 and turn884view2–3. The complete-cover statement permits arithmetic constants; no geometric-connectedness condition was inserted.

The new sufficient reconstruction conclusion must remain distinguished from these existing Hilbertian inputs. No novelty or necessity assertion follows from this review. No numerical experiment is used in place of the infinite group or field arguments.
