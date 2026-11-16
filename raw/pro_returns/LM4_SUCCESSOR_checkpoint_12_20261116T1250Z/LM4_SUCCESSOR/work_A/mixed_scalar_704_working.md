# Proposed exact scalar refinement above the mixed32 layer

Research after checkpoint10. No formal statement number is allocated.
The action/frame equations on the new scalar cover have not been solved.

## Proposed result

Let W_n be the actual source kernel after adjoining all32 mixed ordinary
cups to the A69 quotient at integral level n. Then the proposed exact
new scalar kernel is

    W_n/[W_n,Pi] = C2^576,

and its next scalar refinement is stable. Including the128 globally
central free-cusp scalar directions already retained in A69, the total
N-invariant third subgroup is C2^704. The same kernel maps should be
compatible across n and over older finite distinct-type families.

The explicit704-dimensional target and its old128/new576 split are
proved by the exact commutator certificate below. The following actual
upper/source proof is submitted for independent review.

## Actual mixed32 quotient used as the starting point

The normalized multiplicity actions are P=(45)(67), C=(67), and negative
PC=(45), with free rows0..3 fixed. All48 ordinary slots (r,i) with at
least one free row are stable under these permutations. Sixteen were
already present in A66; the other32 are the mixed slots.

The mixed slots split into binary6/7 and binary4/5 halves. Both explicit
source group laws, canonical-c actions, peripheral positive corrections,
negative-square repairs, and complete s-frame norms have now been
computed. The binary6/7 half has zero initial square. The binary4/5 half
has a nonzero initial inner square, removed by the explicit regular-C2
cusp-fixed inner correction. Their actual source image is the whole
joint fiber product: free/binary one-weight commutators vanish in every
old opposite-weight/free-only cubic factor and span the two new ordered
slots by (a^2b,b^2a). Thus all32 new modules lie in derived/Frattini and
the old eight-cocycle Frattini surjectivity gives the actual image.

These statements concern the actual quotient before its scalar
refinement. They do not presume a full source automorphism realizing the
new mixed frames. The old free-only integral/cubic action and s-frame
are unchanged; new r-frames can be selected over the literal initial C
frame via A16, with compact choices rather than arbitrary-frame lifting.

## Actual upper bound

Work over the INITIAL C=Pi/R, with R relatively perfect, not over a new
base for which H1 may fail. The residual Q_n still has abelianization
A_n=L_n^4 plus four binary V copies, and H1(C,A_n^dual)=0. Its derived
group comprises old M_n, free T6 and U4, all48 ordinary Z slots, and the
already retained globally central free scalar128. Its class is three.
The only nonzero [T,A] is the old free U operation. The ordinary free Z
has its old scalar128 third commutators; new mixed Z is central at this
stage.

In any cofinal finite actual scalar refinement, the A53 duality argument
keeps residual abelianization A_n. The refined residual is a two-group,
since any odd central factor would survive abelianization. The entire
preimages of old M_n and old scalar128 centralize the residual: their
new commutators are globally scalar pairings with (A_n)_N=0.

The A68 gamma4 proof therefore still applies. The only old non-scalar
third block is U3lambda, represented by [[a_i(lambda),a_j(lambda)],
a_k(lambda)]. Its possible scalar partner has weight4lambda. The bracket
[T2lambda,A4lambda] projectszero and has nontrivial scalar weight6lambda,
so it vanishes. Jacobi reduces [U,A] to [T,Z]; ordinary Z lifts lie in the
second upper center because their commutators project into the old
scalar128 whose full preimage centralizes. Hence [T,Z]=1 and gamma4=1.

The third subgroup is elementary abelian: every derived square projects
into the old M_n or old scalar128, whose preimages centralize. Thus
[g,x]^2=[g^2,x]=1. The class-two quotient has derived group a quotient of
wedge^2_Z A_n. Its odd-invariant part surjects old M_n with a globally
scalar new kernel; its action has two-group image and factors H/O^2(H).
The exact old wedge coinvariant M_n gives the reverse order bound, so
no new scalar survives outside gamma3.

Potential T,A scalar triples still vanish by opposite-physical-weight
Jacobi, exactly as in A68. Scalar triples can only come from ordinary
Z and A at the three weights lambda,2lambda,4lambda of one physical
weight. Let F be the four free row indices and B the four binary row
indices. An ordinary bracket is allowed precisely when at least one of
its two indices belongs to F.

For a triple of row indices, the three cyclic bracket branches therefore
have the following actual Jacobi bounds:

- all three free: three branches minus one relation;64 triples give128;
- exactly two free: three branches minus one relation;192 triples give384;
- exactly one free: two branches minus one relation;192 triples give192;
- all three binary: no branch, giving0.

The total is704 over k after scalar extension. The N-invariant third
subgroup is an extension of the old globally trivial128 by the new
scalar, so its head action has two-group image and factors H/O^2(H).
The regular O^2(H)/N orbit identifies the36 physical weights. The final
order-two stabilizer acts1 on the weight line and does not mix rows.
Frobenius descent therefore gives a bound of704 over F2. Since128 is
already retained, the NEW scalar kernel has dimension at most576.

## Explicit704-dimensional central cover

Use the ordinary class-two group on a in k^8 and z in the48 allowed
ordered slots, with multiplication

    z''_(i,j)=z_(i,j)+w_(i,j)+a_i^2 b_j.

A triple (i,j,k) admits the cocycle

    F_ijk((a,z),(b,w))=z_ij b_k^4+a_i^2 w_jk^4

precisely when both adjacent slots(i,j),(j,k) exist. There are320 such
triples, split as follows.

1. The256 triples containing at least two free indices are closed under
   cyclic rotation. On their raw k^256 center apply the same cyclic-
   Frobenius idempotent sigma+sigma^2 as in A68. The fixed complement has
   binary dimension256; the resulting stem block has dimension512.
2. The64 triples with i,k binary and j free retain their entire raw k^64
   center, of binary dimension192. Their two available bracket branches
   have one Jacobi relation. There is no separate coordinatewise trace
   quotient and no cyclic projection on this nonclosed index set.

The resulting center has dimension704. The algebraic cocycle cancellation
is the same identity (b_j^2 c_k)^4=b_j c_k^4 for every valid triple.
An exact binary-basis commutator computation verifies that ALL704 center
directions are attained by third commutators. The all-free projection
is exactly the old128-dimensional A68 block. The remaining projection
has rank576.

Producer and exact output:
  check_mixed_scalar_704.py
  check_mixed_scalar_704.out
Full projection columns and24^3 triple columns:
  mixed_scalar_704_certificate.json

The certificate also checks idempotence of the projection and all512
local field cancellation identities. It does not substitute for the
actual source argument below.

## Actual source attainment and comparison with old128

Take36 physical weight copies and push their704-dimensional centers out
by summation. The weight-seven/fourteen invariance gives a strict H-action.
Pair this cover with the old mixed quotient using the IDENTICAL free128
projection, not an independent duplicate of that old center. The new
kernel is therefore576-dimensional.

The normalized source S has zero free coordinates and z(S)=0 in every
allowed ordinary slot. Consequently S^2=1 literally in the new scalar
cover: every ordinary square involves a free coordinate, and the scalar
cocycle vanishes on the two zero-z inputs. For R, conjugate pure r by the
same actual affine lift with abelian coordinate r e(r) and zero higher
coordinates. This gives literal order3 and projects onto the already
retained source R, including its free128 component. The old full source
C4 carry remains in the old factor; it is not replaced by a fictitious
pure full S.

The exact triple matrix attains all704 scalar coordinates. Coprime
averaging on the elementary gamma3 isolates them from the nontrivial
old U weight modules. In particular the new576 kernel lies in the
actual abstract residual's derived/Frattini subgroup. Its Frattini
quotient is unchanged, so the actual source R image is the entire fiber
product by the eight-cocycle Frattini surjectivity. This attains576 new
scalar directions and meets the upper bound.

## Proposed stability and limits

In the next scalar refinement the full old704 scalar block centralizes
its entire preimage, by (A_n)_N=0. The same gamma4, exponent, and degree-
two arguments apply. The N-invariant gamma3 block is a two-group-action
extension of the globally trivial old704 by the new scalar. It again
factors H/O^2(H), and the identical Jacobi tensor bound is704. Since it
surjects the old704, no further scalar kernel remains.

All704 cocycles and the new576 coordinates use modulo-two data, so their
source transition maps agree across n. The finite-image compactness
argument from A68 gives the exact constant new576 kernel and relative
perfectness after one scalar step at the infinite integral level.
For earlier distinct-type families use C_old with the established
H1(C_old,A_n^dual)=0 and the actual residual product; no automatic H1
vanishing over the A69 base is assumed.

## Remaining action/frame gate

The negative action now permutes binary rows4,5 on the704-dimensional
scalar module; unlike the free-only128 it is not globally identity.
Canonical-c and positive-action lifts must retain the complete old
36-dimensional center and their actual source power corrections. In
particular the new positive action is nontrivial on binary rows, so
literal cusp fixation and s-conjugacy in this scalar cover cannot be
inferred from identity on a free factor. These equations have not yet
been constructed or solved. Exact source scalar closure alone does not
settle them or the full involution problem.
