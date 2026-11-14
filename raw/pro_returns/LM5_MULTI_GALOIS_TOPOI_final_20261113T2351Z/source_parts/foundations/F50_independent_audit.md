# Independent audit of F.50

**Verdict:** the draft `work/montpellier/F50.tex` read on 13 November 2026, 23:09–23:13 UTC passes. Its conclusion is the stated pinned étale reconstruction theorem for every subfield of a finitely generated extension of the maximal abelian extension of the rational numbers. This audit establishes the additional inputs needed beyond F.47; it makes no claim of priority.

## Constants and finite extensions

Work in one algebraic closure of the ambient finitely generated field. The algebraic closure of the subfield `k` inside it contains all algebraic numbers, even when `k` itself has positive transcendence degree. Every finite extension `L/k` in this algebraic closure embeds in `ML`, a finite extension of the ambient `M`, so the ambient field class is stable under all finite extensions used for points and divisors.

For a finitely generated extension `E/Qab`, the relative algebraic closure `E0` of `Qab` is finite over `Qab`. A finite set of generators of this finite algebraic extension consists of algebraic numbers; consequently `E0 = F0 Qab` for a number field `F0`. In characteristic zero, `E/E0` is regular. A proper normal geometrically integral model has divisor map with kernel exactly `E0*`. Its image is a subgroup of a free abelian divisor group, hence free. The exact sequence from `E0*/mu_infty` to `E*/mu_infty` therefore splits. The verified freeness theorem for the constant field gives freeness for `E*/mu_infty`.

The argument for infinitely divisible elements also passes: their divisors vanish, and the divisor of each chosen root vanishes. Thus the element and every root lie in `E0`; the uniform height bound applies there. No assertion that `L` itself contains all roots of unity is required. Only its divisible elements are shown to lie among roots of unity in the ambient algebraic closure.

## Abelian varieties

The one-model specialization argument is sound and supplies the uniformity that cannot be obtained by infinitely many successive shrinkings. Spread one abelian variety and the chosen point over a single normal integral finite-type `Qab`-scheme. For each positive integer, the division fibre is finite étale over that same scheme. A rational section of a finite étale cover over a normal integral base extends everywhere: the generic section selects a finite birational component, whose map to the normal base is an isomorphism. Specialization at every closed point therefore retains every division. Those residue fields are finite over `Qab`; the established arithmetic input kills the specialized point. Density of closed points and separatedness kill the original section.

This proves the actual intersection of all division images is zero, not merely a claim about one chosen Tate-compatible system. Injection after extension to `ML` then proves the assertion over `L`. The Picard and total Tate-module consequences used in F.47 consequently remain valid, with the same Néron–Severi torsion argument.

## Independent probes when punctures are transcendental

The smooth integral model over `Z[1/N]` can contain the punctures and all inverse differences because only finitely many functions are involved. A nonempty smooth generic fibre spreads to a smooth model after one localization. Smoothness makes its image open in `Spec Z[1/N]`, so infinitely many nonempty fibres remain.

At a generic point of a component of a good vertical fibre, the local ring is a discrete valuation ring and the rational prime has value one. The latter fact follows from reducedness of the fibre; the height-one property follows from the principal ideal theorem and flatness. Unit differences give distinct residue values. Even when a residue is transcendental over the prime field, at most the number of punctures among prime-field elements are forbidden, so the prescribed prime-field constants exist.

The Chinese remainder congruences modulo the squares of distinct rational primes produce an identity valuation matrix for the ratios. Thus their classes are independent modulo torsion, and remain so in any common overfield: any proposed relation is already the same equality among elements of the smaller field. A finite collection of integer characters on the free multiplicative quotient gives a nonsingular integer matrix. Its adjugate proves that every profinite exponent is rational; integrality at every prime proves it is an integer. The rational-source Kummer lemma therefore extends with all its original hypotheses met. It never requires a discrete valuation on `L` itself.

## High degrees over coefficient fields

Let `N/Qab` be any finitely generated coefficient field inside the algebraic closure of `k`; its coefficients may be transcendental. Its algebraic constant field `N0` is finite over `Qab`, and regularity gives linear disjointness of `N` and the algebraic numbers over `N0`. Therefore an algebraic number has the same degree after adjoining it to `N` as after adjoining it to `N0`.

These degrees are unbounded. Otherwise the primitive-element theorem would bound all finite subextensions of the algebraic closure over `N0`, forcing that extension to be finite. A finite degree over `Qab` for all algebraic numbers contradicts the uniform height lower bound applied to roots of 2 of arbitrarily large order. A finite map from the descended proper curve to the projective line therefore supplies closed points of arbitrarily large residue degree over `N`.

The zero divisor of any nonzero linear combination of the fixed rational functions has a common degree bound. High-degree points exclude such vanishing and any prescribed finite exceptional set. All coefficients of a particular relation lie in one finitely generated `N/Qab`; the ambiguity coefficients lie in `Qab`. Thus the translated-function argument uses exactly this proved degree property and does not assume that the full algebraic closure is algebraic over `Qab`.

## Geometric and categorical conclusion

The remaining F.47 steps use characteristic zero, the curve assertions after finite extensions, abelian-variety Kummer faithfulness, and root-of-unity ambiguity. Each is verified above. In particular the conclusion is obtained through the all-regular-affine-source criterion and its sliced étale objects, rather than solely from agreement on the geometric points of the multiplicative group. The full-site bridge previously audited for F.47 remains in place.

## Primary source verification

Tsujimura, S. (2022). *Birational anabelian Grothendieck conjecture for curves over arbitrary cyclotomic extension fields of number fields*. RIMS-1957, 24 February 2022. https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1957.pdf

The primary full text was opened directly. Proposition 1.2(ii), printed pp.9–10, asserts stability of abelian-variety Kummer faithfulness under finitely generated extension; Remark 1.1.2 records passage to subfields. Proposition 4.9, printed pp.33–35, supplies the free multiplicative quotient and includes the parameter value `f=1` used here. The present draft provides its own uniform specialization argument and proves the additional divisor and degree reductions explicitly. The other arithmetic and categorical sources are those already verified in F.47 and the F.50 bibliography.
