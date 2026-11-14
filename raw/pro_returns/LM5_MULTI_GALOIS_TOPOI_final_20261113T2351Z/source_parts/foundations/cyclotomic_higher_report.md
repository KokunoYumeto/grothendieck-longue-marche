# Higher-dimensional cyclotomic reconstruction: independent proof audit

This addendum belongs to the new F.47 proof assembled by the root and Montpellier agents. The completed A/E files and registers are unchanged.

## Deliverable

`cyclotomic_higher.tex` proves the higher-dimensional step from the separately proved arbitrary smooth affine curve calculation, for every algebraic field `k` contained in `F Q^ab`, with `F` a number field. It is an unnumbered subsection; its internal equations are CH.1–CH.7. It uses no custom macros beyond the existing AMS packages.

The first paragraph specifies the exact curve input. A separate descent paragraph proves that an actual pointwise curve unit also represents the Kummer class when representation of that class was initially obtained only after finite extension. This uses root-of-unity-valued rational functions and the Hochschild–Serre degree-one exact sequence split by a rational point.

## Main safeguards

1. Tsujimura's abelian-variety theorem kills the ordinary intersection of all multiples, not only a chosen coherent divisible subgroup. His proof explicitly factors through `lim A(M)/n A(M)`.
2. The Picard argument includes torsion in the geometric Neron–Severi group: divide by `e n`, then multiply by its torsion exponent `e` before invoking abelian-variety Kummer faithfulness. It only uses the injection of actual algebraically trivial line bundles into the Picard variety's rational points, so a Brauer obstruction does not invalidate it.
3. Boundary residues become integers by restricting to curves transverse to a single boundary component. A local UFD/Kummer calculation proves compatibility at all finite levels simultaneously.
4. No inverse-limit purity theorem is needed. Rational representatives satisfy `div(a_n)=D+nE_n`; the Picard lemma makes `D` principal. Explicit line bundles with nth-power trivialization extend the remaining torsors uniquely to the compactification.
5. The remaining class is constant because the compatible Picard torsion group is zero. Evaluation at one rational point makes that constant an actual field element.
6. A smooth curve through the fixed rational point and any prescribed algebraic point proves pointwise equality in every dimension. Its ratio unit has zero Kummer class for every n, hence zero divisor on the proper curve, hence is constant and equal to one.
7. The conclusion is precisely CHW Theorem 4.18(5) for all regular affine sources, so the theorem supplies all étale-object compatibilities through Proposition 4.14. It is not an inference from point equality for one map.

## Independently verified primary passages

- Tsujimura (2020), *Combinatorial Belyi Cuspidalization and Arithmetic Subquotients of the Grothendieck–Teichmüller Group*, author manuscript: https://www.kurims.kyoto-u.ac.jp/~stsuji/prims.pdf. Theorem 3.1 and its proof, printed p. 35 / PDF p. 35 (zero-based index34). The displayed factorization through `lim A(M)/n A(M)` explicitly verifies the kernel needed here. The root supplies the final `Tsujimura2020` bibliography entry, with publication DOI 10.4171/PRIMS/56-4-5.
- Carlson–Haine–Wolf (2024), https://peterjhaine.github.io/files/reconstruction_of_schemes_from_etale_topoi.pdf. Proposition 4.14, printed pp.22–23; Theorem 4.18 and proof, pp.24–25; the preliminary explanation of Corollary A.9 just before Proposition 4.14. The all-etale-object hypothesis of Proposition4.14 was checked literally.
- Stacks Project, https://stacks.math.columbia.edu/tag/0FD4 and https://stacks.math.columbia.edu/tag/0G4C. Lemmas 33.47.1, 33.47.3 and 37.32.3. Finite prescribed jets are imposed by Serre vanishing; the resulting open smoothness and irreducibility conditions meet over an infinite field.
- Encinas–Hauser (2002), https://arxiv.org/pdf/math/0211423. Unnumbered statement “The result”, pp.1–2, and principalization discussion “Idea of proof”, pp.3–4. This is the primary constructive strong-resolution proof, used to produce a projective smooth compactification and divisorial boundary without altering the given smooth open.
- Cheng–Ji–Larson–Olander (2021), https://chngr.github.io/assets/theorem-of-the-base.pdf. Lemma7.2 and Theorem7.3, printed p.18, including torsion; Theorem7.4 also checked. This supplies the exact geometric Neron–Severi finiteness assertion used in the explicit Picard proof.

The three newly introduced reference entries are in `cyclotomic_references.bib`; Tsujimura2020 and CHW2024 are supplied by the main F bibliography. No numerical computation is claimed for this proof: the assertions are exact algebraic arguments. The earlier foundations computation log remains unchanged.
