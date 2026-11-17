# Actual action on the mixed704 scalar refinement

Research after formal A73. The new source/action prefix has been independently
read and rerun by CE. The frame equations remain under investigation.

## Actual source and old-center comparison

The model keeps all eight normalized source cocycles, the complete old
36-coordinate opposite-weight center, and its nonzero C4 source carry.
The old center is transformed by Sym²(E), then by the actual affine gauge;
a parity central character makes the actual S center coordinate zero.
The resulting normalized group law is checked against the original old
source law on source words. In particular it is not the free-four-cusp
projection with a silently discarded source carry.

The ordinary coordinates are all48 pairs with at least one free index.
The scalar coordinates are the A73 projected704 center on320 rawF8 slots.
SourceS has zero free coordinates and ordinary coordinates; sourceR is
an actual conjugate of pureR. Exact sourceS²=R³=1 and the complete old
projection are checked.

## Honest homogeneous lifts

The multiplicities are P=(45)(67), C=(67), B=(45). Physical c remains
monomial. Both P and C preserve the actual48/320 index sets and the
cyclic-Frobenius projection. The old source affine inner terms are
transported through the complete eight-row gauge.

For any ordinary cohomology shear L, retain every old quadratic cochain

  Qij(a,m)=sum over oriented opposite weights a_i,left*a_j,right
           + m_ij when i!=j.

The scalar correction is

  stem sum_l [Lij,l Qkl^4 + Ljk,l^4 Qli^2]

on every valid(i,j,k). Thus the existing actual44-cocycle corrections
lift as honest group automorphisms, not merely formal substitutions.
The producer verifies their group-law identities on source-generated
samples in addition to the algebraic cocycle construction.

Canonicalc is corrected by its actual central parity character to send
S toS andR toS R^-1S. Both literal source identities and c² pass.
The positive action is corrected by its unique central parity character
to fix the actual cusp. Its projection is the already selected mixed32
positive action, including the binary45 regular-module inner repair.
The negative square is one on both actual source generators. Conceptually,
its remaining discrepancy is a central character, killed by the cusp,
which generates the source abelianization.

Files:
  check_mixed_scalar_action.py
  check_mixed_scalar_action.out
  mixed_scalar_action_result.json

## The genuine next frame gate

The stored A69/mixed32 s-frame does not yet conjugate S correctly in the
new scalar cover: its scalar s-class residue is nonzero. Its scalar
negative normalizer norm is also nonzero. Both residues have zero
projection to the old free128 center, as required by the retained data.
No failure of all possible lifts or frames follows from this tuple.

The current simultaneous correction family has zero abelian coordinates
and is abelian. It includes:
- ordinary Z coordinates fixed by both S and the full negative frame
  coefficient involution (1632 binary directions);
- old free T joint-fixed corrections (216 bits);
- old free U S-fixed corrections (240 bits);
- old36-center negative-norm-zero corrections (87 bits);
- the actual new central norm image (168 bits).

The exact output simultaneously records the oldUT4 norm, the scalar
s-class, and the scalar normalizer norm. The scalar class map on an
ordinary correction is

  stem sum_weights [zij aS_k^4 + aS_i^2 zjk^4].

All scalar norm columns are computed in the actual group law. The
UT4 columns use the previously checked pointwise formulas. This is an
explicit homogeneous correction family, not an exhaustion of all old
affine actions or frames.

There is an additional integral-retention condition: arbitrary oldM
norm-zero changes can alter the six integral free offdiagonal center
coordinates. A solution must either have zero projection to these
coordinates or be supplied with a new honest integral half comparison.
The first matrix retains all oldM choices so this constraint can be
imposed by exact additional linear rows without recomputing the model.
