# Independent D.50 audit

Reviewer: bc_fermat. Outcome: **PASS**.

The full frozen statement and proof were read. The section SHA256 is
4f83e868595f54847a2d6ca5205051f4f037e937dee17ae7d236dfb1a90a05da.
The independent executable copy and its complete actual output are retained in
this directory. The original finite computation was rerun from the copied
source; verify_audit.py compares the complete regenerated JSON, excluding only
the explicitly reported elapsed-time field.

## Mathematical checks

1. The edge map is the actual map induced by the peripheral word homomorphism.
   Its path identity includes the basepoint term
   \(D p(g)=p(\psi(g))+(g-1)p(\beta)\), which vanishes on the specified kernel.
   The two vertex maps are invertible because the images of the two
   conjugators centralize their corresponding torsion generators.
2. The nilpotent Fitting summand of the regular edge module lies in the cycle
   module and then in the moving submodule. It is a direct summand of the
   regular group algebra, so its projectivity is established in the actual
   ambient module. The projection supplies the required derivation.
3. The cyclic norm equation follows from the fixed cusp cycle. Restriction of
   the projective module to the cyclic cusp subgroup is projective; coefficient
   sums in a free cyclic module prove exactness of the norm equation. The
   argument does not divide by the even cusp order.
4. The corrected endomorphism is \(T+e\) on the full cycle module. It is
   invertible on both Fitting summands. The explicit derivation formulas keep
   the two torsion conjugacy classes, the cusp identity, and the entire common
   quotient.
5. The higher common quotient is exactly
   \(J_k/(2^{k-1}W_k)\). Its intersection and sum of quotient kernels give the
   displayed fibre product. Compatible actual conjugators lift through the
   onto cusp maps; invertibility of their reduction modulo two proves
   generation at every finite level, and the inverse limits give actual
   automorphisms.
6. The image of the source residual is the integral moving direct summand:
   averaging proves both inclusions through the pronilpotent residual.
   The remaining class-two image contains \(W_1\wedge V\) by the displayed
   commutators of actual preimages. The proof claims precisely this inclusion,
   without replacing it by an unproved equality.

## Execution scope

The exact finite check has marked base \(A_5\times(S_3\times C_3)\), of order
1080. The original rank 141 is repaired to 181; the moving dimension is 120
and the nilpotent projective dimension is 48. The code checks every cycle,
the retraction, peripheral identities, and compatible exponents 2, 4, 8, 16.
This is the finite certificate explicitly stated in D.50. The enormous actual
arithmetic base is handled by the proved construction, not by this separate
numerical example.

No mathematical correction is requested.
