# D.52 — full invariant-boundary repair in the exact marked finite source

## Result and scope

The literal marked group \(A_5\times(S_3\times C_3)\), of order 1080, now has an evaluated nonidentity multiplier-one peripheral automorphism on the full class-two exponent-four source. This replaces the particular finite homology representative excluded in D.51.

The complete corrected cusp word has 6,352,056 letters in \(s,r,r^{-1}\). Direct collection gives identity in the full target, including the invariant central coordinates. Both torsion relations pass. The induced homology matrix has rank 181, deviation rank 96, and preserves the actual intersection form.

The arithmetic \(G_3\) source of D.49–D.51 is not replaced by this group. Its chosen actions and invariant residual remain unchanged. No transfer of the finite solution to that arithmetic parameter space is asserted.

## Actual correction and transgression constraints

The allowed moving space has dimension 120. The marked cusp action satisfies that \(1-t\) is invertible on this module. Every allowed pair is therefore
\[
 b=(1-t)^{-1}s(1-r)w,\qquad a=w+b.
\]
These produce actual crossed-homomorphism values on the two torsion generators, with zero cusp value. Their restrictions are actual equivariant homology maps with zero transgression. The proof does not enlarge this space to all abstract equivariant homomorphisms.

Integral odd-deck averaging and an exact modulo-four cusp correction lift each basis pair. Literal commutators with an actual order-three deck lift put the conjugators in the moving normal subgroup. Their cusp errors are computed in the full class-two group.

## Full quadratic invariant equation

The invariant central module has dimension 3600. Its actual augmentation matrix has rank 3587, leaving 13 obstruction coordinates. All 13 dual functionals annihilate every augmentation column.

The full group cusp product is
\[
 C(A,B)=B\,s(B)^{-1}s(A)\,t(A)^{-1}.
\]
Class-two collection gives its exact cross term
\[
 (1+s)b'\wedge s(a+b).
\]
This produces 13 explicit quadratic equations in the 120 allowable binary parameters. The certificate contains all linear and quadratic coefficients. The program independently checks the complete central cross term, and its quotient coordinates, on 36 literal word products.

The solved parameter is 0x2fc2bc437a2c2a199b32d59580fd1f, with least significant bit first. It has weight 60 and occurs at deterministic trial 5784. Its full invariant error is in the evaluated augmentation image; the program solves for actual central conjugator corrections, realizes them by free-generator commutator words, and checks the complete corrected word.

## The pairing-only attempt was insufficient

The linearized pairing equations have rank 9 and kernel dimension 111. A selected nonidentity allowed action with derivation rank 16 preserves the pairing and is invertible. Its actual invariant cusp obstruction is nevertheless nonzero.

All 120 moving modulo-four homology variations retaining that modulo-two conjugator pair were also evaluated in the exact central Frattini group. Their additional image in the 13-dimensional obstruction space has rank zero. Thus the positive result uses the full quadratic boundary equations, rather than treating the pairing condition as sufficient. This unsuccessful route and its actual output are retained.

## Complete homology continuation

The successful full class-two action has a compatible continuation through the complete two-adic homology tower of this same marked free kernel. Its actual common quotient with that tower is the abelian kernel of exponent four.

At every higher step, the cusp correction remains in the integral moving summand. The unchanged invertible modulo-two matrix proves generation; the conjugators retain their exact modulo-four common coordinates, so the entire evaluated class-two action remains fixed. The inverse limit gives one automorphism and one conjugator pair on the actual fibre-product source. Its projection kernels are the 16,290-dimensional exterior commutator module and \(4U_*\), respectively.

The program verifies the new coordinates and cusp identities through exponents 4, 8 and 16. An exploratory continuation initially used parity lifts without first projecting them by the integral odd-deck idempotent; it failed at the next level. Its exact source and stderr remain in raw_trials/continuation_unaveraged. The final program performs the integral projection at every correction and passes.

## Exact remaining kernel

The new full-source kernel is still nonzero. Its exact image in the class-two exponent-eight target is twice the commutator module over \(\mathbb Z/4\). The actual word \([g_0,g_1]^2\), for the first two marked free graph generators, has 272 \(B\)-letters. It is identity in the exponent-four target, has zero complete homology image, and has nonzero commutator coordinate 2 in the exponent-eight target. The complete word and both evaluations are retained.

## Reproduction and validation

Run the three standard-library Python programs in this order:

1. code/d_cm_symplectic_search.py
2. code/d_cm_invariant_repair.py
3. code/d_cm_full_class2_search.py

The sole externally retained runtime input is the frozen D.51 pairing certificate code/d_class2_diagnostic.json. The first program produces the intermediate input used by the next two. Each writes its JSON beside its source; its actual stdout is retained in the matching .out.

All three passed a fresh copied-source/input rebuild. Every JSON field agrees with the original after excluding only /summary/elapsed_seconds. Control-character, display and environment lint passed. All exploratory sources and outputs remain under raw_trials, with their actual outcomes documented. Root and peer audits are complete: PASS. Root rebuilt all three complete programs with the exact D51 input, comparing every JSON/stdout field except only elapsed time. The peer verified the full proof and computed the exact pair-to-derivation map:120 pair parameters,102-dimensional kernel and18-dimensional derivation image. The stated pairing and ranks are over F2. Both intended types are explicit in the presented paper, with a retained author-confirmed source diff.

Historical author raw_trials are preserved at code/d52_historical with their exact source/output hashes and explicit archive map.
