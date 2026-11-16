# Independent DE audit of A.65

**Verdict: PASS.** The complete draft `notes/fgh_A65_draft.tex`, its full exact certificate, and its source ledger were read on November 15, 2026. The certificate was independently executed without modifying the author's files; the entire resulting JSON equals the author's result. The retained output is `notes/de_A65_certificate_rerun.out`.

## Actual subgroup and ordinary model comparison

The elementary Heisenberg subgroup dichotomy is exact: a subgroup not containing the centre injects into an isotropic line and is either trivial or noncentral of order p. Its generic action on the proper curve is free because all generic stabilizers are contained in the centre. The quotient therefore has the stated genus, degree and cusp count, and the elliptic isogeny square is the actual quotient square.

At an ordinary prime, the two Gaussian places have different connected CM lines. Every selected noncentral translation line has nonzero reduction at one of them. Equivariance with the good elliptic model then excludes every special stabilizer, including nodes. A free action of the constant group scheme Z/p is an étale torsor even in residue characteristic p. Étale descent therefore gives a semistable quotient. Distinct marks inside one rational cluster cannot become identified, since every nonidentity subgroup element moves that cluster. The rational companion criterion is consequently applied to genuine quotient marks and paths.

## Inert model comparison

The norm makes the quotient Jacobian a quotient of the original Jacobian, so good reduction descends after the common finite extension. The semistable dual graph is then a tree. The rational-map resolution uses only point blowups of regular surfaces, hence adds only rational components. The graph-image descent of the map to the good elliptic model is valid: each exceptional projective line maps constantly, the graph image is proper quasi-finite and birational over the normal original surface, and so is an isomorphism.

Resolving the actual proper map from the original curve to the quotient gives a surjective proper model map. Every positive-genus target component must be dominated by an original positive-genus source component; a new exceptional projective line cannot dominate one, even inseparably, by Lüroth. The unique nonconstant source component is radicial over the good elliptic curve. The intervening target component and both factor maps are thus radicial. All other positive target components have constant image different from O. No commutation of wild quotient with reduction is assumed.

All quotient cusps lie above O. The tree and the unique O-point on the main elliptic component force their rational parts into a single attachment subtree. Smooth separated marked sections cannot remain at its attaching node. Thus every selected cusp has a distinct rationally joined companion. This is precisely the established A.41/A.42 input, with no transfer of fixed subgroups through an arbitrary surjective pro-prime quotient. The normalizer conclusion uses A.59 separately.

The intrinsic exponent-p, class-two formulation is also valid: a two-generator nonabelian quotient of the universal order-p cubed Heisenberg group has that full order, so its kernel is the same characteristic kernel. Arithmetic twists and isomorphisms are handled after finite extension, within the already proved all-packet/open-derived scope.

## Fresh primary checks

- **verified:** Liu, Proposition 9.2.5 and Theorem 9.2.7, printed pp.396–397; fresh exact opening `turn1026view0`. The regular fibre-surface and projective-target hypotheses match the draft. Lemma 7.5.18(b), pp.312–313, freshly read as `turn1026view1`; Remark 10.4.24, p.542, as `turn1024view2`. The semistable fibre is reduced, so its multiplicity gcd is one. URL: https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf .
- **verified:** Silverman, Theorem V.3.1, printed pp.144–146, fresh exact opening `turn1026view2`; the ordinary/supersingular torsion and purely inseparable assertions used here agree with the theorem. URL: https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf .
- **verified:** Serre–Tate, Theorem 1 and Corollary 2, printed p.493, fresh indexed primary opening `turn1031view0`, including the explicit surjective-homomorphism statement and proof. The direct scan lacked extracted text; its screenshot placeholder was not counted as an actual visual review. The readable indexed original supplies the exact statement. URL: https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf .

No general nilpotent-cover fixedness or cofinality assertion is part of this audit.
