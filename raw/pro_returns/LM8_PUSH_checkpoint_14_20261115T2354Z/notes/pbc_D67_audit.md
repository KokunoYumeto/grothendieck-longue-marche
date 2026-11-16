# Independent full audit of D.67

Verdict: **PASS**, 2026-11-15. I read `notes/de_profive_baire_draft.tex` in full and independently checked the primary local input and every transition from actual sections to finite cocycles and back. This is a proof audit, not a finite-level experiment.

## Primary-source scope

I reopened Hoshi's RIMS1742 preprint, including the Appendix A setup on printed pages 36–37, Definition A.3 and Remark A.3.1 on page 38, Lemma A.5, and Proposition A.6 on pages 41–42. The setup explicitly uses an arbitrary section of the **geometrically pro-Σ fundamental exact sequence**, so the local result is not restricted to birational sections. With residue characteristic `q != 5` and `Σ={5}`, the geometric specialization map is an isomorphism. Proposition A.6 identifies nontrivial specialized section inertia with a nontrivial closed subgroup of a cuspidal inertia group. These are exactly the two source inputs used by the draft.

URL: https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1742.pdf

Verified references: `turn811view0`, `turn812view1`, `turn812view2`, `turn813view0`, `turn814view0`.

The fresh-prime step also uses Milne, *Class Field Theory* V.3.23, independently opened during the D.66 audit (`turn796view0`, `turn797view0`).

## Actual local cusp conclusion

The Magnus centralizer proof works for every nonzero `b in Z5`, including nonunits. The series `(1+X)^b-1` has nonzero linear coefficient and therefore a formal compositional inverse over `Q5`. Commuting with it forces commutation with `X`. Coefficient comparison eliminates every word containing `Y`, so the centralizer in the formal algebra is `Q5[[X]]`. Evaluating `Y=0` is the actual group retraction to `<x>`; injectivity of the Magnus embedding then identifies the original group element with a power of `x`.

A geometric normalizer of the nonzero closed subgroup `<x^b>` acts on it by a unit exponent. Abelianization forces that exponent to be one, hence the normalizer is `<x>`. The corresponding result for the other two primitive cusp generators follows by a free-basis change.

For an element of the specialized arithmetic group normalizing the section-inertia subgroup, choose the unit tangential lift with the same residue-Galois image. That lift already normalizes the whole cusp subgroup and its closed subgroups. The remaining geometric factor must therefore belong to `<x>`. Hence the specialized section image lies in the cusp decomposition group. The cartesian specialization square pulls this back to the **actual** pro-five local cusp packet. The kernel of specialization is already contained in that packet, so no hidden geometric kernel is lost.

When `a_q != 0`, the exact abelian inertia direction picks the zero cusp. The primitive cusp inclusion makes its local Kummer class equal to the reference class. After combining the geometric and cusp-inertia adjustments, the actual abelian cocycles agree. The conjugator's abelian image is therefore fixed by local Galois. Frobenius multiplies it by `q`, and the torsion-free module has no such invariants because `q-1 != 0`. Thus the conjugator lies in `H=P'`, as required for the actual `H`-coboundary assertion.

When `a_q=0`, a nonzero specialized inertia subgroup would have a nonzero abelian image in one of the three primitive cusp directions, which is impossible. Trivial specialized inertia, together with the cartesian square and the unramified reference section, gives `c(I_q)=1` in the actual group. This proves both local alternatives used later.

## Fibre identification and finite capture

The action `Int(x^{a(g)}) sigma0(g)` is an action by the Kummer cocycle identity. A section with abelian class `(a,0)` can be conjugated to have exactly the reference abelian cocycle, leaving an actual `H`-valued nonabelian cocycle. Global `H0(Z5(1)^2)=0` removes the potential extra abelian stabilizer quotient; the fibre is precisely the stated nonabelian `H1` set.

Iterated Frattini subgroups are characteristic and open in the finitely generated free pro-five group. Their images are the corresponding Frattini series in every finite five-group, so they are cofinal. The elementary induction `g^(5^r) in P_r` proves the stated exponent bound. Their intersections with `H` therefore induce its actual topology.

The finite action on `H_r` and the finite support set are constant on each `5^r K` coset. At primes outside the support, the local `H`-coboundary has trivial reduced inertia because the conjugating power of `x` is a multiple of the exponent of `Q_r`; the zero-inertia case was already proved. Thus the **actual reduced cocycle**, and not merely its class, factors through the finite-ramification Galois group.

The finite nonabelian cocycle set is finite: each member is a homomorphism to a fixed finite semidirect-product group with prescribed second coordinate. Bounded-degree extensions with fixed finite ramification set are finite in number. No nonexistent transition maps between arbitrary finite cocycle sets are assumed.

## Nonabelian Baire argument

An exceptional cocycle supplies an actual element `(z(delta),1)` with nonidentity translation in its finite affine image. Conjugation preserves identity linear part and nonidentity translation, even when the translation group is nonabelian. Thus Chebotarev applies to precisely the required conjugacy class.

The chosen deep coefficient additions preserve all finite data and avoid cancellation at the fresh primes. Openness uses only finitely many exceptional cocycles at each precision and nonzero coordinates at chosen witness primes. Completeness then gives the dense G-delta set. This is the same valid parameter-topology mechanism as D.66, with no linearity assumption on the cocycles themselves.

For a parameter in that set, an exceptional reduction of an integral cocycle contradicts the local `H`-coboundary at its witness prime, whose finite action is the identity. Hence every reduction kills its actual action kernel. The integral cocycle kills the full kernel and descends continuously through the compact quotient to the actual operator image.

The image of a chosen nonzero inertia subgroup is normal because the actual action sends `x` to `x^chi`. Its fixed subgroup in `H` is `H intersect <x> = 1`. A single local `H`-coboundary makes the descended cocycle trivial on this normal subgroup. Comparing its values on `ng=g(g^-1ng)` then places every value in that fixed subgroup, hence makes it trivial globally. This is an exact nonabelian argument.

## Existence, packet scope and inverse limits

The completed cusp section supplies the section class in each asserted fibre; uniqueness is only asserted in the full **free pro-five** fibre, not in the full profinite fibre. Intersecting with the D.66 dense G-delta and with infinitely supported parameters is legitimate. Puncture permutations transport the actual packet sections and their fibres.

Every finite five-group is nilpotent, so the closed lower-central quotients recover `P`. For a compatible sequence of section classes, the conjugator at each adjacent level can be lifted to the next quotient, giving compatible actual representatives and therefore a continuous limit section. Conversely, conjugacy at every level gives nested nonempty closed conjugator sets in compact `P`, so it gives one full conjugator. The draft correctly assumes compatibility of the classes and does not infer it merely from separate existence at arbitrarily high levels.

No mathematical gap or necessary correction found. The result is substantially stronger than the metabelian statement, and the proof supplies the necessary actual-group comparison throughout.
