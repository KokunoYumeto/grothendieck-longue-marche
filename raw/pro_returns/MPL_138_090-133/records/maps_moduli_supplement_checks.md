# Proof record for supplementary notes SR01–SR02

Author: GPT-6 Astra Pro; inherited effort unspecified. Run MPL_138_090-133/maps_moduli_research. Date: 2026-11-17. No source-image reading, source edit, or new external theorem is involved.

## P1. Cubic-star quotient

Use the same left-acting convention as maps_moduli_checks.md P1:
ρ_sρ_fσ=1. On E={1,2,3}, put ρ_s=(123), σ=1, ρ_f=(132). On E0={*}, all three permutations are the identity. The constant map E→E0 commutes with every generator, hence is a morphism of cartographic sets. It is surjective and both actions are transitive.

Both maps are admissible for the q∈{1,2} convention explicitly allowed in frozen scan98. The source has passport (3)|(1,1,1)|(3), the target (1)|(1)|(1). The induced cell maps have the following data:

| Cell type | Source cells and degrees | Target cells and degrees | Fibre cardinality ν | Literal equation at each source cell |
|---|---|---|---:|---|
| Vertices S | one, degree3 | one, degree1 | 1 | 3=1·1, false |
| Edges A | three, degree1 each | one, degree1 | 3 | 1=3·1, false |
| Faces F | one, degree3 | one, degree1 | 1 | 3=1·1, false |

The corresponding analytic diagram is f'=f∘h with f'=z³, f(z)=z and h(z)=z³. The local indices of h are3 at0 and∞ and1 at each cube root of1. Thus the usual identity p'(s')=e_h(s')p(s), and its edge/face analogues, hold exactly; they do not hold with the stated fibre cardinalities.

For a general finite cover of degree D, the relevant local indices satisfy Σ_(x' above x)e_h(x')=D. The number of points above x is a different quantity. In the example, the vertex and face sums are3 through one point of index3, and the edge sum is3 through three points of index1.

The conclusion is conditional only on allowing the usual cartographic equivariant morphisms or branched-cover morphisms. It is not a counterexample if “morphisms” is intentionally restricted to isomorphisms or to some narrower class excluding this quotient. Hua's §13.I footnote1513–1518 explicitly uses only isomorphisms subsequently, so the supplement records the additional problem without attributing a false broader conclusion to that restricted use.

## P2. Failure of composition for the literal weighted-set laws

Construct three precartes C0,C1,C2. At every level take A and F to be singletons of degree1, and make every edge and face map the identity. These always satisfy their displayed equations and q∈{1,2}.

For the vertex sets use:

- S0={a}, p0(a)=1.
- S1={b,c}, p1(b)=p1(c)=2.
- S2={d,e,f}, p2(d)=2 and p2(e)=p2(f)=4.

Define u:S1→S0 by u(b)=u(c)=a, and v:S2→S1 by v(d)=b, v(e)=v(f)=c.

For u, the only target fibre has cardinality2, and both source weights satisfy2=2·1. Thus u obeys the literal p-law.

For v, the fibre over b has cardinality1 and2=1·2; the fibre over c has cardinality2 and both relevant source weights satisfy4=2·2. Thus v also obeys the literal p-law.

For u∘v, the only target fibre has cardinality3, so the required source weight is3·1=3 for every point of S2. The actual weights are2,4,4, so the composite is not a morphism by the same law.

The definition of a precarte in frozen scan98, lines6–11, imposes no equality between Σp,Σq,Σr. Consequently the unequal degree sums in these particular objects do not violate any precarte hypothesis. Frozen scan99's sum equality is a later necessary condition for realizability by a map, so it cannot remove this counterexample to the category as defined.

The underlying mechanism is simple: successive fibre cardinalities multiply only when the second fibre size is uniform over the first fibre. The written law does not impose that uniformity. Replacing fibre cardinalities by the local ratios p_source/p_target gives ratios that multiply under composition; for isomorphisms both the ratios and the fibre cardinalities are1. This describes a mathematical repair, without changing the frozen transcription.

## Context and scope

The context searches used “morphisme,” “Cartcomb,” “precarte/précarte” and the exact ν equation. Hua, modernised reading of cote138, §13.I, lines1513–1518, is the direct supplied-context match. RESULTS_STATE has no direct entry settling this definition or composition issue; the groupoid/generization lead MPL_147_003-047 N075 is not used as a theorem here.

These two examples are independent: SR01 tests the proposed functor against a genuine realizable map morphism, while SR02 tests the category axioms on the full object class actually defined. Neither changes the previously valid use of the isomorphism subcategory for pinning.
