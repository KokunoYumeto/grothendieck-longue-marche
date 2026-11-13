# F.8: the exact seven-point kernel reduction

The twelve seven-point maps in F.7 have the same kernel. The comparison is the identity `f_(hI) = r_h composed with f_I` in the labelled moduli space: multiplying every A4 label on the left by `h` applies the same Möbius map to all seven coordinates, which disappears in the moduli quotient. The certificate lists all twelve left multipliers and target relabellings. Functoriality gives the identical kernel statement after profinite completion.

The completed kernel contains no nonzero power of any source cusp and no conjugate of such a power. A primitive meridian at one of the fourteen source punctures projects to a twist of exponent `e`, with `e=2` or `3`; its lift is a product of twists of exponent one around the `12/e` disks over that branch point. Seven retained labels force an essential disk. Retaining two labels in that disk and two outside maps its multitwist to one twist or two identical twists in the four-punctured sphere. A character sending that twist to one therefore restricts to multiplication by one or two on the full source `Zhat`; both maps are injective. The finite program executes all 84 subset–inertia-partition choices and records each four-label detector.

The same lift calculation excludes every nonidentity reducible element of the discrete source `F13 <= PΓ0,4`. Membership in the source kernel of monodromy forces `e | k`, and `T^k` lifts to same-sign twists of exponent `k/e`. Essential components that become parallel after forgetting add their exponents, so no cancellation occurs.

The base seven-set is `{0,1,2,3,4,7,10}`. It meets the three `V4` cosets in sizes `3,2,2`, and the program checks the corresponding assertion for all twelve sets. A four-label full `V4`-orbit cross-ratio is consequently unavailable as a projection of these seven-point maps.

Files:

- `work/part_a/f_seven_point_continuation.tex`
- `work/part_a/f_seven_point_continuation_results.json`
- `work/part_a/code/seven_point_same_kernel.py`
- `work/part_a/code/seven_point_same_kernel_output.json`
- `work/part_a/code/seven_point_same_kernel_stdout.txt`

The full seven-point map has not been proved injective, and no nontrivial kernel word has been proved. A possible discrete kernel would consist of pseudo-Anosov elements. This does not establish a profinite type classification. F.7's full A5 centralizer comparison remains Open. The separate numerical braid-crossing exploration is explicitly exploratory and is not part of the proof or certificate.
