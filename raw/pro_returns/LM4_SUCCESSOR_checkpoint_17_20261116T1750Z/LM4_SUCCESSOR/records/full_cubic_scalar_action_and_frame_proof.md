# The actual full cubic scalar action and finite frame certificate

We work over k=F8 with X^3+X+1, with36 physical weights paired by
lambda ↔ minuslambda. This note supplies the action and norm comparison
for the actual128-dimensional cubic scalar cover. The complete scalar
kernel and its stabilization require the separate A68 upper-bound proof.
The original full negative order and cofinality questions remain Open.

## 1. Correct raw cocycles and stem quotient

For four cusp coordinates a_i and sixteen ordinary coordinates z_ri,
the ordinary product has correction a_r^2 b_i. Define the64 raw central
coordinates by

    f_rij((a,z),(b,w)) = z_ri b_j^4 + a_r^2 w_ij^4.

Every raw coordinate is a normalized cocycle: its two surviving
coboundary terms cancel because (b_i^2 c_j)^4=b_i c_j^4. Its scalar
weights are7 and14, so the full monomial head acts trivially on the
central coordinates before permuting physical weights. Sum over those
weights to obtain the actual globally central raw k^64 cover.

Let sigma send t in coordinate(r,i,j) to t^2 in(i,j,r). Then sigma^3=1.
N=1+sigma+sigma^2 is an idempotent onto Fix(sigma), and Q=sigma+sigma^2
is an idempotent onto kerN. These spaces have binary dimensions64 and128.
We apply Q to the raw cocycle. A commutator of ordinary Z_ri(z) with
A_j(a) has t=z a^4 in(r,i,j) and t^4 in(j,r,i); hence its raw value is
(1+sigma^2)(t e_rij). These values span imQ. The quotient by Fix(sigma)
is therefore stem and its128 coordinates are attained by third
commutators. This is not64 independent coordinatewise trace quotients.

## 2. Actual normalized old-center projection

The old A56 center is the symmetric-square coefficient module on its
eight affine rows. Let E be the verified four-row free-cusp change of
basis, and let g be its verified cochain gauge. Project the old center
by the induced symmetric-square map, producing ten k-coordinates m_ij.
The explicit36-column map is saved in the certificate. Its value on the
old C4 carry QS is zero.

Conjugation by(g,0) makes the four cusp rows equal to their normalized
source cocycles. A possible remaining central parity character is
subtracted to make S pure; in the stored witness this central shift is
itselfzero. The image of R equals the conjugate of pure r by its
prescribed affine vector, since both have orderthree. The code checks
these source identities, the actual old-law homomorphism equations,
and that the stored W0 positive action is identity on this whole free
center factor. Thus these coordinates are an actual source projection,
not a formal vector-space replacement of the old group.

For an oriented opposite-weight pair(left,right), put

    q_ij = sum a_i,left a_j,right,
    p_ij = sum a_j,left a_i,right.

The old central product in offdiagonal m_ij is

    k_ij(a,b)=sum(a_i,left b_j,right+a_j,left b_i,right).

Set C_ij=m_ij+q_ij for i≠j, and C_ii=q_ii. Each C_ij is invariant under
the monomial head: opposite scalars cancel, while an orientation flip
adds q_ij+p_ij to m_ij and interchanges q_ij,p_ij. Its coboundary is

    delta C_ij = sum a_j,partner b_i.

The corresponding reversed C_ji has coboundary sum a_i b_j,partner.
This identity includes the diagonal case, without a spurious factor2.

## 3. Lifting all canonical-c ordinary shears

Let L_ri,s be the actual16-by4 canonical-c coefficient matrix. The
ordinary shear adds sum_s L_ri,s j3(a_s) to z_ri, where
j3(a)_lambda=a_(minuslambda)^4. Its change in the raw scalar cocycle is

    sum_s L_ri,s (sum a_s,partner b_j)^4
      + sum_s L_ij,s^4 (sum a_r b_s,partner)^2.

Consequently the following actual scalar cochain lifts the shear:

    psi_rij(a,m)=sum_s L_ri,s C_js^4
                       +L_ij,s^4 C_sr^2.

Apply Q to psi for the128-dimensional stem cover. The displayed
coboundary identity proves multiplicativity. The shear fixes a and m,
so its square is one and these shears commute. Monomial head invariance
of C_ij proves equivariance, including orientation reversals.

For a diagonal scalar quotient this specializes to

    pi[L(m_ij+q_ij)^4+L^4(m_ij+p_ij)^2]       (i≠j),
    pi[L q_ii^4+L^4 q_ii^2]                  (i=j),

where pi:k→kerTr is t↦t+Tr(t). The older center is essential in the
mixed-row formula. A selected diagonal cover after forgetting that
center must not simply be declared c-stable.

Compose the lifted shear with the actual monomial c action and the
prescribed affine/ordinary inner terms. All are genuine automorphisms
of the displayed group. The result has the correct image on the
ordinary source. Its S error can only be in old central m and new
central u; a parity character removes that error. For the stored
normalization both error vectors arezero. Its R image and S R^-1 S
differ by a central element of exponenttwo, while both have orderthree;
therefore they agree. The source is onto by the actual original-base
Frattini argument. It follows that the automorphism is canonical c
and squares toone on the entire actual source quotient.

The root program directly checks S^2=R^3=1, the source projection,
c(S)=S, c(R)=S R^-1 S, c(T)=T^-1, c^2 on source generators, and
independent multiplicativity pairs for the shear and canonical action.
The finite code supplements the cocycle and source proof; it is not
used as an exhaustive substitute for those identities.

## 4. Exact simultaneous frame equation

The W0 positive action is identity on this free source factor. The
saved full20 frame centralizes S but initially has a nonzero128-scalar
negative square. Ordinary homogeneous corrections Z have scalar norm

    Q sum_weights[ Z_ri (beta t_j)^4
                     +(beta t_r)^2 Z_ij^4 ],

where t is the actual normalized free-frame difference. Old central
corrections contribute the linear shear at a=0. CE independently
matched this formula against every one of the519 original-law columns
in the first restricted calculation.

Restricting ordinary multiplicities to kerJ gave scalar rank79 and
missed the target. This is only a restricted failure. Allowing all
ordinary joint S/D-fixed corrections gives rank88; adding old central
norm-zero corrections gives rank90 and contains the target. The
corrections must also preserve the four UT4 norms.

We therefore solve one system with1119 binary variables:
576 ordinary joint-fixed columns;216 lower-T joint-fixed columns;
240 S-fixed U columns; and87 old central norm-kernel columns. Their
outputs retain both the entire UT4 residue and the128-scalar residue.
The lower-T contribution is

    (beta t_i) T_jk + T_ij (beta t_k),

and U contributes its ordinary coefficient norm. The target is zero
in UT4 and the stored128-scalar square. The system has rank234 and is
solvable. The stored solution uses only ordinary Z and lower T; its
oldM and U correction vectors arezero.

The actual full20 law verifies that the correction centralizes S and
preserves every old, lower, ordinary, and UT4 norm. All72 field-basis
lower-T formulas were also checked against that original group law.
Root then reconstructed the corrected frame in the independent full128
cover. Both its zero-central-coordinate representative and the literal
product of the old frame with the correction centralize S and have
negative normone. Their difference is an allowed central128 element.

Files: code/check_diagonal_scalar_frame_lift.py --full-cubic
--verify-correction work_A/A68_simultaneous_scalar_frame_solution.json;
records/check_full_cubic_scalar_frame_verified.out;
records/full_cubic_scalar_frame_verified.json. The first failed
restricted solve remains in full_cubic_scalar_frame_lift.json. The
complete simultaneous matrix, target, labels, solution, and full20
frame are in work_A/A68_simultaneous_scalar_frame_solution.json.

The construction-selected initial transporter and A16 supply an
involutory r-frame at this actual pro-two quotient, with its exact
initial C-image. This is an existence proof and does not purport to
give r-frame coordinates that were never computed.

## 5. Exact remaining scope

These computations prove the finite scalar-refined action and frame
claims once paired with the actual source and scalar-kernel proofs.
A further issue is retention through the entire integral tower: a
central-half correction at the first mod2-to-mod4 step can alter the
new scalar square. This compatibility is being checked separately.
No full negative-order assertion, cofinality assertion, or arbitrary
frame-conjugacy assertion follows from the finite certificates.
