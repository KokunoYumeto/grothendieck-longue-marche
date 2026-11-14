# Root review of D.66

Verdict: PASS for the complete statement D.66 as frozen. The full profinite
realization questions D.13 and D.19 remain on the active list.

Reviewed proof: `D66_EXPERIMENTS/sections/D_quadratic_compact_source.tex`,
SHA-256 `b2df75eff503c02197e89e81c360756d60638bd11d63cba10a0604fd377c5184`.
Frozen manifest: SHA-256
`1d77562247b199c5c78f1a4a8b71d4474a3e7d9d3031f43c3dce7ff5ddb71ada`.
Root replay audit: SHA-256
`719316f60577048f7720d3c550bc26ac999dfcb7901faab2133bcf888fa7d12f`.

## Proof and dependency review

The complete final statement and proof were read. All nine final mathematical
programs were read, including the edge-extension, quadratic-group and relative
source-correction implementations. The final proof explicitly includes the
integral averaging coefficients 1/9 and 1/3, their reductions modulo four,
the distinction between the original cusp order 36 and its order-12 image
through the specified quotient, and preservation of J65 before composition
of the two cusp errors.

The exact source intersections were checked against the retained D.58 proof.
There the onto map S57 -> L is proved by lifting a prescribed integral
homology vector through R_h and then removing its actual small central image
through R50 -> Z_*. The central image of R50 intersect L_{*,2} is the full
comparison kernel K, with both inclusions obtained from source elements.
These are the two source results used in D.66.22--D.66.24.

D.60.10 was read with its actual source-word map. Odd averaging identifies
the relevant 2-adic homology blocks of K3 with those of K-dagger; the quotient
kernel has odd order. D.60.12 was checked with the actual unordered-character
stabilizer, including its character-exchanging involution. Its projective
compact summands, and the integral lifting argument already retained there,
support the integral maps in D.66. The edge-module extension uses a lattice
with free underlying quotient and relative injectivity of the projective
target. The stated 1/9 and 1/3 factors give exactly the modulo-four averages
in the executed certificate.

D.64.11 and its proof were read: the cusp map is onto, with width ratio
three, and L maps onto the actual compact comparison kernel. The proof of
joint surjectivity of the four compact exterior maps was also read. Its
subtraction occurs in R wedge U and preserves the chosen compact coordinate.
This supplies the compatible affine section sigma in D.66.21 and the central
lift in D.66.22. The D.64 and D.65 passages giving the final augmentation
corrections and the post-involution moving repair were checked. The latter
repair follows the source-involution words in the stated order.

## Exact finite maps

The complete central map C -> C_* has hexadecimal columns
(2,1,4,2,8,8,1,4). The four columns 09,30,42,84 of the comparison-kernel
coinvariants are independent and have precisely that kernel as image.
The actual full-norm kernel maps to V0 = span(09,42). In particular its
four coinvariant generators have image of rank two; the proof retains this
map and does not infer injectivity for that different four-dimensional
coinvariant space.

The bilinear law B gives the asserted associative class-two group. Its
commutator is the polarized Hermitian quotient, which spans C; its square
is (2v,q(v mod 2)), and its fourth power is one. The scalar-equivariant
quadratic primitive has zero additive ambiguity because the relevant
odd-character module has no homomorphism to the trivial scalar module.
That equality proves the deck composition identities and both full
class-two comparison squares, including their quadratic coordinates.

The literal source elements are conjugates of s and r, and hence retain
their orders two and three. The evaluated product has zero homology
coordinate and central mask 26. With ell(c)=c4+c5, ell(26)=1. Every relative
isometry has central map I+v ell with v in V0, and this map fixes the entire
comparison kernel pointwise. The retained differences d_s and d_r have
zero full small image. The program evaluates both source conjugations,
their product, and the eighteenth power for all 32 cases.

## Transfer to the original source

The two integral conjugator vectors sigma((delta-I)b) and
sigma((delta-I)(w+b)) are in L. Their actual source cochain vanishes at t,
and I+sigma(delta-I)p is invertible, acting by delta on sigma(M) and by
identity on ker p. The onto map S57 -> L and the actual central lift
R50 intersect L_{*,2} -> ker(C -> C_*) give literal source elements with
both prescribed integral homology and the required full quadratic images.
This proves q_E delta_B = F_delta q_E on the two marked generators and
therefore on their source. The argument uses this square without assigning
a descent of the preliminary D.65 action to E.

The source kernel is preserved through its three defining maps. The small
class-two component, integral homology component and W_h component retain
their actual markings. Their invertibility and the retained D.58 fibre
product prove the required source automorphism. The correcting elements
are in R_h, which is contained in the original commutator-gauge kernel;
this preserves the normalized parameter comparison.

The earlier repairs have zero M-homology, so their E-images are central;
their conjugations leave the displayed E-square unchanged. The isometry
and the identity on the orthogonal extra-projective summands retain the
previous orientation tests. The proof explicitly preserves J65 using
the first three compact kernels, the fourth small square, and commutation
with the full norm. Thus both transported and newly produced cusp errors
remain in J65. Choosing v=q_E(z) gives exactly
delta_C(q_E(z))+(delta_C-I)c_t=q_E(z)+v=0.
The injection of the fourth compact comparison-kernel coinvariants into C
then places the remaining fourth error in augmentation. Joint surjectivity
of all four compact maps supplies corrections with the other three
coordinates zero. Their actual source lifts remove this augmentation.

The resulting kernel is J66 with the stated original projection. The
dimension and coinvariant assertions concern the complete stored maps:
ker(nu4) has dimension 1918 and coinvariants of dimension four;
J63/J66 has dimension 9600 and coinvariants of dimension 28. The specified
remaining block has dimension 274560. The proof records that remaining
kernel and leaves its arithmetic correction active.

## Independent execution

`replay.py` copied only the nine programs and ten declared immutable inputs
to a fresh directory. It executed every stage successfully, with empty
stderr, and compared every entire resulting JSON and stdout with the frozen
author output. The only removed values were `/summary/elapsed_seconds` in
JSON and the corresponding elapsed-seconds value in stdout. No mathematical
field, matrix, source hash or input hash was excluded. Each fresh raw output
was preserved. A frozen raw dependency was restored for the next stage
only after its entire-result comparison had passed. All 144 owned files
and all ten immutable inputs were hashed before and after execution;
the author tree was unchanged. This is an independent execution of the
reviewed code, with the comparison policy and every raw result retained.
