# Independent DE audit of A.69

Status: **PASS** for the complete written proof, verified primary ramified-cover/Deuring–Shafarevich inputs, and independent whole-certificate execution. This is a proof audit, not an inference from the finite sample levels.

## Exact objects read and executed

- Entire `notes/fgh_A69_draft.tex`, including all actual cover maps and intermediate-cover conclusions.
- Entire `notes/fgh_A69_certificate.py`; executed with `runpy` under a non-main name so the author's files were not rewritten. The complete computed JSON equals the author's output.
- Exact hashes and execution summary: `notes/de_A69_certificate_rerun.json`.

## Primary verification

1. Lehr–Matignon, *Automorphisms of curves and stable reduction*, Theorem 6.13, preprint printed p.21 (published p.154): https://arxiv.org/pdf/math/0411059 . Fresh independent open/find refs `turn1148view0`, `turn1149view0`. The statement requires a nilpotent Galois cover of a good proper model, branch closure étale over the valuation ring, and generic tameness explicitly defined by characteristic of the fraction field. It gives a tree/potential good Jacobian. The present characteristic-zero cover with the single branch section O meets these hypotheses. I had also actually viewed the published p.154 image earlier (`turn1130view0`). No marked-fibre p-rank or interior-slope conclusion is inferred from it.
2. Crew, *Etale p-covers in characteristic p*, Corollary 1.8, printed p.35: https://www.numdam.org/item/CM_1984__52_1_31_0.pdf . Fresh open `turn1148view1` and actual screenshot viewed `turn1149view2`. This is the ramified smooth-curve Deuring–Shafarevich formula, including arbitrary finite p-group actions. It is applied to actual smooth components, not to a marked vertical fibre.
3. The one-variable Weierstrass argument was checked directly in the proof. At a smooth special fixed point on a component with nontrivial involution, the reduction of sigma(t)-t is nonzero of finite positive order, so it has no vertical factor and preparation gives finite flat fixed roots. Smooth formal-disc coordinates identify these roots with generic curve fixed points. The author source was subsequently freshly opened and the exact Corollary 2.16/proof read at printed p.23: https://pub.math.leidenuniv.nl/~vonkjb/teaching/2021_topics/Topics.pdf , refs `turn1151view0`, `turn1152view0`. It explicitly isolates the uniformizer-power factor, which is absent here.

## Mathematical gates checked

- The two actual maps factor through elliptic duplication, have degree 2m, four ramification indices m/2, and the displayed r,s really preserve the map. The base m=2 is the unramified elliptic isogeny case.
- The anti-invariant factor has dimension m/2 and a unital Q(zeta_m) action from the primitive odd differential characters. Its special étale rational 2-Tate space is a module over the field Q2(zeta_m) of degree m/2. Thus its p-rank is zero or its full dimension, without any unjustified Hodge-to-Newton implication.
- In the special product of component Jacobians, sigma-exchanged positive-genus components give isogenous invariant/anti-invariant factors, contradicting old rank zero and new ordinarity. A component with trivial sigma contributes only to the old factor and is not incorrectly declared rational.
- For a nontrivial fixed component, norm and pullback identify its invariant factor with the quotient Jacobian up to isogeny. Combining Deuring–Shafarevich with Riemann–Hurwitz forces quotient genus zero, minimum different two, and an ordinary component whenever its Prym is nonzero. The zero-Prym alternative contributes no positive genus.
- For an ordinary curve and a faithful 2-group, subtracting twice Deuring–Shafarevich from Riemann–Hurwitz gives the displayed sum of nonnegative terms. It forces G2=1; then wild inertia embeds through its first coefficient in the additive residue field, excluding cyclic order-four inertia. A fourth root of the hyperelliptic involution necessarily fixes a point over the unique fixed point of the induced projective involution, so that case is excluded.
- The primitive cyclic action forces the component stabilizer order to be two; hence a unique orbit of m/2 ordinary elliptic components accounts for the entire anti-factor. The field argument concerns the actual whole orbit contribution, so it does not assume a componentwise primitive eigenvector.
- Smooth fixed roots genuinely specialize to generic sigma-fixed cusps. These cusps are individually mu-fixed. Consequently none of the orbit elliptic components can contain a smooth sigma-fixed point. No such lifting claim is made at nodes or on sigma-trivial components.
- The root mark determines a mu-fixed vertex. Every ordinary orbit vertex has the same positive depth; its parent node is one sigma-fixed point and its second fixed point gives a child edge. Each child subtree is unmarked, contains no ordinary orbit vertex, and must contain positive genus by marked stability. The subtrees are pairwise disjoint. Their genera plus the elliptic orbit give at least m, contradicting genus m-1.
- The explicit principal divisors kill all four cusp differences by m. Cusp inertia is the Frattini subgroup of the actual dihedral deck group, so every nontrivial proper intermediate has at least two cusps. Norm pushforward has coefficient one on geometric points, not a ramification multiplier. Good reduction and rank zero pass to the Jacobian isogeny quotient. A.41/A.42 and the previously audited nilpotent-normalizer theorem apply at exactly their established scopes.

## Execution and scope

The exact certificate independently verifies the universal rational-function identities, subgroup/Frattini counts through m=512, the finite supporting DS/RH equalities, and the characteristic-two first ramification coefficient. It does not replace the all-level induction or the actual fixed-point lifting argument. The universal arbitrary-cover question remains explicitly open.

## Final author clarifications

The final finite-extension hypotheses, four explicit cusp divisors, elementary Frattini proof, different-sum derivation, and smooth formal-disc/properness sentence were reread and pass. Current draft SHA256: `34c99d85c5b8dc41dce1a4e622d3484190264d2f12c9391c0d60169784211c99`. The exact certificate is unchanged.
