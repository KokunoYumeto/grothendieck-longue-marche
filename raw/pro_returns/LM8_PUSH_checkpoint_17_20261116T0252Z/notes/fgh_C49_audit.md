# Independent full audit of C.49 — PASS

I read the complete 281-line candidate and its complete exact program, and reread the precise canonical C.20, C.26 and C.47 dependencies. The earlier oversized dependency-read output was truncated; I repeated the needed reads in bounded calls before completing this audit.

## Actual-image and normalization gates

The two projective CM coordinates each admit one global sign normalized to one modulo four. This normalization is multiplicative and does not allow independent odd-prime signs. The cubic norm calculation forces the second coefficient to vanish modulo eight, with all four odd scalar residues lifting by the displayed odd-derivative Hensel equation. The Gaussian calculation correctly uses the exact norm equation modulo sixteen: the congruence modulo eight alone overcounts. The Cayley representatives supply precisely the four liftable signed residues. The scalar square-root argument at odd primes also applies at the ramified Eisenstein prime three.

Canonical C.20 supplies actual adelic surjectivity, so the finite paired images are genuinely realized. C.26's primitive abelianization is zero at multiplier one; inverse/marking changes preserve zero. Thus the actual cubic frame belongs to F', and its signed reduction modulo four is the identity. The normalized lower-right-one intertwiner then fixes the global sign in A=VT^{-1}. The exact source-derived images give the stated shear congruences at eight/four and three; the certificate recomputes these groups from the literal source matrices.

The new level-five realization is valid. The actual Tate parameter z^2/256 times a formal unit with constant one gives t=-8 kappa_2 in the stated tangential normalization. I freshly opened Milne's author PDF and read III section 3 equations (23)--(26), printed 102--103, including the integral power-series and Tate uniformization statements (web refs turn1259view0, turn1260view0, turn1260view1). The splitting field of X^5-2 has derived C5, so this shear is onto C5 on the actual closed derived Galois subgroup. The paired arithmetic image has order 288, prime to five; therefore its kernel still supplies the full shear C5. This proves actual independent realization with both CM coordinates fixed, rather than only a finite compatibility assertion.

The coordinate law is additive/multiplicative on the actual multiplier-one group. The parity k+l modulo two agrees with the retained signed formula from C.47. Since it factors through modulus twelve, every finite parity-zero pair has an adelic parity-zero lift. The independent arithmetic shear then gives exactly the claimed arithmetic framed kernels and cyclic factors.

## Executed exact certificate

The retained read-only replay is code/fgh_C49_certificate_rerun.py. It executes the owner's functions without invoking its writer and reconstructs the entire JSON, including the owner-source hash. The output notes/fgh_C49_certificate_rerun.json is byte-identical to the owner JSON; stdout is retained separately. It reproduces signed pure orders 768 and 11520, derived orders 16 and 960, paired orders 96 and 576, actual framed orders 96 and 2880, and arithmetic orders 48 and 1440. It also checks the complete cyclic generator closures, all permitted shears, parity kernels, raw frame-pair injectivity and the local lifting formulas.

No mathematical or source correction is required. The statement is correctly restricted to actual multiplier-one retained frames. It does not claim an arbitrary-multiplier image or that these coordinates alone determine every gentle-group character.
