# Root review of the framed principal cubic cover

Verdict: PASS for the frozen comparison subresult. The arithmetic values of
the two residual intrinsic handle coordinates remain to be evaluated.

The complete note `notes/principal_cubic_cover.md` and the complete program
`code/a_principal_cubic_cover.py` were read. Their SHA-256 values are
`cdb3a97fcd124242b0447020c2803e01e5678f3fde5c00fe7968078ba496213b`
and `23aff671a197fccdbf95f38622c34ed0f8bee79688293d46a15a14af334f480b`.
The frozen manifest has SHA-256
`e26f6e1ab7d3998b0d530a2f8e0be3c5aeb41c20a7255c74afab6b0ea5de18f3`.

## Proper cover, tangent and isogeny

The three cubic coordinate functions in (C2) have no common zero on (C1).
Their substitution in the Fermat equation is the stated multiple of (C1),
and their two coordinate sums give the literal pullback
`q*f_A0=(u/v)^3`. The displayed combination of the three affine partial
derivatives is 3; it proves smoothness away from 3, including characteristic
2. The partial derivatives at v=0 are nonzero as well. The nonzero divisor
class A0-O proves that f_A0 is not a cube, and its divisor gives an unramified
connected degree-three proper cover. The chosen point Q0 makes the map an
isogeny. The local expansion has linear coefficient one, so the indicated
r-tangent maps to the original s-tangent without an additional unit.

The frozen theta distribution identity gives the cube of the lift in (C5).
The pole coefficient at Q0 then selects `gamma=9*zeta^2` among its three
possible cube roots. The other roots give the two other deck translates.
The resulting proper morphism has degree seven and fixes Q0. The displayed
matrices give the two literal squares with q_*=diag(1,3), and their pairing
identity gives omega_C=omega_E by injectivity of multiplication by 3 on
Z3. The marking transport q_*^-1 B q_* is integral for the stated B=I mod3;
the full free-group marking transport remains the one already proved in
the logarithm-torsor note.

At the selected prime above 7, the lift constant reduces to one. Its
reduction and seventh-power Frobenius both lift the indicated base
endomorphism and fix Q0. Their difference is a deck translation fixing
Q0, hence is zero. The finite-point calculation is consistent with this
proper equality. The affine degree-seven source is X_pi. Both its isogeny
map and its open filling map to X remain explicit. The formal-disc path
from the scaled tangent has the stated negative Kummer inertia correction;
the ratio of the chosen compatible roots gives that sign directly. No
affine arithmetic-action value follows by replacing these two maps with
one another.

## Actual subgroup and central comparison

The Kummer unit row identifies the based cover with
K=ker(l_A0 mod3). Reidemeister--Schreier rewriting gives B=b^3 and the
three based lifts of each of the other nine generators, hence rank 28.
Collecting these words in the class-two group gives both L and eta in
(C9); the factor 1/2 is integral in Z3. The stored exterior map has rank
45, diagonal entries 1 repeated 36 times and 3 repeated nine times,
and a primitive rank-333 kernel with explicit inverse coordinates.

Conjugation by b has the actual last wrap B*g_0*B^-1. Its third power is
Int(B), with the corresponding nonzero central correction. The program
checks this full group identity and the comparison square, not only the
three-cycle on the abelianized basis.

Both retained residual differences take values in the exterior square of
the peripheral lattice. The peripheral generators all lie in K, so those
values are commutators in K and map to zero in K^ab. Their ordered
commutator lifts define actual automorphisms of the free pro-three group:
the Frattini map is the identity and the cover character is preserved.
Inside K/gamma3(K) the corrections are central. Collecting the images of
b^3 and b^j*a*b^-j gives exactly the norm sum and the three translated
columns in (C11), with zero correction on the peripheral lifts. Both
displayed comparison identities are checked for both residual basis
vectors.

The two coefficients of d_(1,0) wedge d_(2,0), on a_0 and B, give the
matrix [[0,-1],[1,0]]. Its determinant is one and its recorded inverse
recovers both integral residual parameters. The antisymmetric tensors in
I_K/I_K^3 provide this explicit detector. The previous homology comparison
and this next augmentation comparison are connected by the actual quotient
map, whose kernel contains these commutators.

## Complete independent execution

`principal_cubic_replay.py` verified all five owned files and seven declared
immutable inputs, copied the source and inputs into a fresh directory, and
executed the complete program. Exit status was zero and stderr was empty.
The entire stdout, stderr and 95,054-byte JSON agree byte for byte with
the frozen originals. No field was removed. All twelve declared files
were rechecked after execution and the author tree was unchanged.

The exact JSON SHA-256 is
`a7069b133ee697e0adfc2c6111a0ba9ff1819780ff5ef1764329e1fbc2ea77cd`.
The two preliminary interface failures remain in the declared history.
The successful comparison does not assign either residual arithmetic
coefficient, and no additional numbered theorem is claimed for that
remaining evaluation.
