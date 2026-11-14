# D66: source map for the two remaining compact coordinates

This is the current proof checkpoint, before theorem freeze. The finite maps
below have been executed; the concluding source comparison is stated here in
full so that its maps can be reviewed independently.

## Exact marked finite quotient

Use the old orbit a4, character `(0,1,0,0)`, the actual order-46656 group
Gdagger, and the old integral projective compact cover M16. Induction through
the eight unordered character cosets gives a projective Z2[Gdagger]-lattice
M of rank 256. The actual small compact lattice Mstar has rank 64. Write
phi:M->Mstar for the graph map. Its reduction is the retained D64 map.

Let C be the Gdagger-coinvariants of the odd-invariant exterior self module
of M/2. The retained fibre identifies C with an eight-dimensional binary
space. The actual small map C->Cstar has rank four. Its kernel is exactly
the injected four-dimensional coinvariant space of the D64 compact
comparison kernel. The two remaining ordinary-norm-kernel directions are
`v1=0x09` and `v2=0x42` in C. They inject into C.

The projective edge extension is computed integrally modulo four. Its
restriction to the actual 96-dimensional character cycle module is precisely
the rank-16 compact projection. It satisfies all 72 stabilizer identities.
For the induced edge generator w, solve `(t-1)b=(s-t)w`. The actual projective
cyclic module makes this equation integrally solvable; the modulo-four
coefficient matrix has rank 232. Thus the literal two source cochains are
`eta_s=(1-s)b`, `eta_r=(1-r)(w+b)`, and `eta_t=0`.

Define the class-two exponent-four group N with abelianization M/4 and
central commutator quotient C. In real character coordinates its bilinear
two-cocycle is obtained from the triangular cocycle with diagonal
`q(v)=[v bar(v)^t]` by averaging over the scalar group of order three. Its
commutator is the actual exterior projection. Every deck action has a unique
scalar-equivariant quadratic correction: the difference of its two
bilinear cocycles has the recorded polar form, and averaging the triangular
quadratic primitive fixes its linear term. Uniqueness follows because the
nontrivial scalar module has no map to the trivial central module. This
gives an actual action of Gdagger on N, with all group-composition identities.

In N semidirect Gdagger, use the literal marked source images
`S=Int((b,0))(s)` and `R=Int((w+b,0))(r)`. Then S has order two and R order
three. Their product has zero M/4-coordinate and central coordinate
`c_t=0x26`. The base cusp has order twelve. In particular the original
source t^18 has central coordinate zero and base coordinate t^6; this map
does not replace the source involution by the cusp involution.

The source map Bhat->E=N semidirect Gdagger is onto: its kernel over
Gdagger maps onto M/2 by the actual cycle projection, hence onto N by the
finite Frattini argument. It factors through the full G3 class-two source
because K3 maps into N. The map to the corresponding small group Estar is
the actual base map and the canonical scalar-equivariant class-two map
induced by phi. The latter factors through the actual small source
Tstar,2, since the kernel of Bhat->Gstar maps into a class-two exponent-four
two-group. No identification of unrelated markings is used.

## Complete relative correction family

All 16 a4 isometries in each D64 branch have been enumerated. Relative to
the chosen isometry X0, their matrices delta=X X0^-1 obey
`phi delta=phi`. Their central actions are exactly

    delta_C = I + v ell,
    ell(c)=c_4+c_5,
    v in {0,0x09,0x42,0x4b}.

Each value occurs four times in each branch. They fix the comparison kernel
pointwise. Also `ell(c_t)=1`.

Each relative matrix has an actual equivariant modulo-four lift with
`phi delta_4=phi` exactly. The lift is constructed by first correcting an
ordinary lift into ker(phi), then applying the coefficient-of-one relative
trace from the projective domain. The identical construction over Z2 gives
an integral equivariant automorphism: its reduction is invertible. The
source central action uses only its modulo-two reduction.

Let Fdelta be its unique scalar-equivariant automorphism of N. It commutes
with Gdagger and satisfies `Phi Fdelta=Phi` on the entire small class-two
quotient. The new actual source conjugator differences are

    d_s=Fdelta((b,0)) (b,0)^-1,
    d_r=Fdelta((w+b,0)) (w+b,0)^-1.

Both lie in ker(N->Nstar), including their central coordinates. All 32
direct checks give the literal cusp difference v and zero t^18 difference.
These are actual quadratic identities, not their linearizations.

## Integral source lift and preserved comparisons

Let p:U->M be the actual compact projection. Choose a G-equivariant section
sigma:M->U as follows. Projectivity of M lifts its compact inclusion through
U->P. The small compact module is projective over its actual small deck
group, so choose its equivariant affine section sigmastar. The discrepancy
between theta_U sigma and sigmastar phi lies in the small cusp lattice.
The actual cusp map is onto (width factor three is a unit in Z2), and M is
projective; subtract its lift. Then

    p sigma = I,   theta_U sigma = sigmastar phi,
    sigma(ker phi) is contained in L.

The two source homology conjugators for the relative correction are
`sigma((delta-I)b)` and `sigma((delta-I)(w+b))`. Their cusp cochain is zero
integrally. Their homology automorphism is the identity on ker(p) and delta
on sigma(M), hence is invertible at every level. They have zero actual
small homology and zero W_h image.

Lift these homology vectors through S57->L. Their E-images have the required
linear coordinates. The differences from d_s,d_r are central and in
ker(C->Cstar). D58/D64 identify the image of R50 intersect Lstar,2 on this
central quotient with precisely that kernel. Correct the two lifts by
those source elements. The resulting actual source homomorphism delta_B
induces Fdelta on E and the identity on the full Tstar,2 and W_h. It factors
through X because it preserves the actual G quotient, the characteristic
homology/class-two kernels inside K3, and R_h through the W_h map. Its
invertible homology and exterior maps give an automorphism of X.

It fixes t on Y but can have a central error in K on X. On E that error is
exactly v. The already proved moving, extra-projective, cross, and other
orbit repairs may be applied to bring its error into J65. They preserve
the E map: their homology has zero M-coordinate, and their E-images are
central, so their conjugations are trivial in E. The a4 ordinary norm is
zero by the actual orientation identity and the isometry equation.

Take any preliminary actual lift of alpha65 to X, whose cusp error z lies
in J65. Its image in C lies in span(v1,v2). Choose the relative correction
with v equal to that image. The exact commuting source square gives

    q_E(delta_B alpha65(t) t^-1)
       = delta_C(q_E(z)) + (delta_C-I)c_t = q_E(z)+v = 0.

This uses no descent of alpha65 itself to E. The relative central action
fixes the comparison kernel pointwise. Finally the actual two-conjugator
augmentation map kills the remaining a4 representative with zero
coinvariant, using joint surjectivity from J63. It preserves the other
three compact components and all small/W_h comparisons. This gives the
candidate next kernel

    J66 = ker(J63 -> C1 direct_sum C2 direct_sum C3 direct_sum C4).

Its dimension is dim(J65)-1918. The source-kernel and invariant-kernel
claims still need to be written in the final theorem with the exact
remaining dimensions; no full-profinite realization is asserted.

## Executed files

All paths are under D66_EXPERIMENTS/code:
`d_old_compact_source_cochain.py/.out/.json`,
`d_old_compact_quadratic_source.py/.out/.json`, and
`d_old_compact_relative_correction.py/.out/.json`.
The preceding integral-norm, whole-coinvariant, and all-isometry programs
remain preserved, including both earlier failed executions.
