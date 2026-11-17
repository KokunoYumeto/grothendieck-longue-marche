# The central three-adic sign twist preserves both quotient negative-frame equations

Checkpoint34 research corollary. The actual original full-group frame in A111 remains fixed and indispensable. This result concerns what fails if it is replaced by an arbitrary quotient frame. No actual full-GT CM value is asserted.

## 1. A central involution in the ACTUAL quotient

Use the proved actual product from
`work_DE/actual_central_quotient_product_and_odd_obstruction34.md`:

    E1 = P2 x (G3 x_(C3) Z3^2)
            x product_(p>=5) (Gp x Z_p^2),
    E1' = P2' x G3' x product_(p>=5) Gp.

Here P2=F^(2)/[M2,F^(2)] and Gp=SL2(Z_p). Define c_* in E1' by its EXACT product coordinates: the P2' coordinate is one, the G3' coordinate is -I, and every p>=5 coordinate is I. Its abelian coordinates are all zero. The three-adic character of -I is zero, so this is an element of the displayed actual fiber product and of its derived subgroup. Its square is one and it is nonidentity.

It is central in E1 because its only nonidentity coordinate is scalar. It also commutes with BOTH original modular generators s and r. Indeed on E1' the original rho=Ad(r) acts by the actual induced pro-two action and odd conjugation by the integral matrix J. The cyclic central sign vanishes because all abelian coordinates are zero. The original iota=Ad(s) similarly acts by its induced pro-two action and signed conjugation by S0 on each odd factor. Both actions fix the identity pro-two coordinate and all the scalar odd coordinates. Thus

    c_* in Z(B1),       c_*^2=1,
    q4(c_*)=I,          q3(c_*)=-I.                          (1)

The actual alpha also fixes c_*. Its pro-two action is the natural descended one, and its odd signed action is the actual matrix conjugation of A104. Both fix these coordinates. To spell out the dyadic descent used here: q2 alpha=Ad(K_Phi)q2 preserves M2, so the automorphism alpha of the full free pro-two quotient preserves M21=[M2,F^(2)] as well. Hence

    alpha(c_*)=c_*.                                         (2)

This is stronger than merely choosing a fixed lift through a central pro-two extension: the actual product allows c_* to have order exactly two and to be central in the full B1.

## 2. Both negative-frame equations remain true

For e=d mod3 and R_e=y^epsilon r, use the ORIGINAL full-group word J_e^alpha from A111, then its image J in B1. It satisfies

    alpha(R_e)=J R_e^(-1) J^(-1),       alpha(J)J=1.          (3)

Put J'=J c_*. Centrality, (1) and (2) give

    alpha(R_e)=J' R_e^(-1) (J')^(-1),
    alpha(J')J'=alpha(J)c_* J c_*=alpha(J)J c_*^2=1.         (4)

The S3 coset, abelian normalization and signed modulo-four normalization of the frame are unchanged. This can also be realized by replacing the QUOTIENT pure r-frame image(A_r) by image(A_r)c_* while keeping the s-frame unchanged. For epsilon=0, J=s phi A_r immediately changes to Jc_*. For epsilon=1, J=A_r s does too because c_* commutes with s. The quotient automorphism itself does not change.

## 3. The coherent class still depends on the original negative frame

Let T_e=C_E1(R_e). The two frame choices (3)--(4) induce the SAME involution on T_e:

    kappa(t)=J^(-1)alpha(t)J
            =(J')^(-1)alpha(t)J',

because c_* is central. It lies in T_e and satisfies kappa(c_*)=c_*.

For any of the actual positive quotient factor frames h of A108, the two coherent defects are

    w_h=J^(-1)alpha(h)^(-1) v h,
    w'_h=(J')^(-1)alpha(h)^(-1) v h=c_* w_h.                 (5)

Since c_* is central, fixed by kappa and of order two, multiplication by c_* preserves the cocycle condition and respects the equivalence w~a^(-1)w kappa(a). It therefore gives a continuous involution of H^1(C2,T_e). It has no fixed point: A111's actual scalar comparison has trivial action and no nontrivial coboundaries, while

    q3(w'_h)=-q3(w_h).                                      (6)

In the exact odd-product description, this toggles only the three-adic binary coordinate. It is a homeomorphism of the compact cohomology space, not a pointed automorphism; it sends the basepoint to the nonbase class of c_*.

Thus the two negative-frame equations (3), even together with purity/abelian/signed normalization, do not determine the original coherent class from the unframed quotient action. The original full-group marking in A111 is additional data and cannot be dropped.

## 4. Exact boundary and finite image evidence

This does not modify A111: that theorem uses the unique ORIGINAL full-group A_r and therefore one specified J_e^alpha. The alternative quotient frame in (4) is not asserted to be the image of that full frame. Indeed c_* has no rho-fixed lift in F': the full original centralizer is trivial. Its C3 lifting obstruction is the nonbase element corresponding to c_* under the proved homeomorphism H^1(C3,N1)~=C_E1(r).

The finite signed image in (1) is exactly the already executed A110 certificate h12=5I, whose original LM7_PUSH rational-three-line and delta values are recorded in
`work_DE/original_quotient_frame_ambiguity34_certificate.json`
and its genuine producer/output/exit receipt. This corollary runs no new finite computation and infers no continuous element from that certificate: c_* is constructed in the proved actual product above.

No change of the unique full-group frame, no new actual GT element, no determination of epsilon_A, and no CM or main-problem conclusion is made.
