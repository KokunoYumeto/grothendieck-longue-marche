# Independent audit of A.59

**Full proof and finite certificate: PASS.** D/E read the whole notes-only candidate and reran `notes/fgh_A59_certificate.py`. It checked every subgroup of D8 x C3, Q8 x C5, and H3 x C2, including the nonnormal subgroups, for coefficient primes 2, 3, 5, and 7. The general argument is supplied in the proof and does not depend on this finite sample.

The potentially good reduction criterion was freshly reopened in Silverman's primary text, Proposition VII.5.5, printed page 196, PDF page index 212: https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . Browser references turn918view0 and turn919view0 show the statement and its residue-characteristic-two qualification in the proof: the theorem itself has no exclusion of two, and the proof refers that case to Appendix A. The integral invariant j=1728 therefore gives the required good marked elliptic pair after finite extension at every coefficient prime. SGA1 XIII.2.9--2.12 was independently checked earlier in the A56 audit at exactly the prime-to-residue-characteristic scope reused here.

The prime-to-ell geometric Galois closure extends tamely over the good pair after finite descent. The local chart t=z^e with e invertible on the residue field proves smoothness of the proper source and its subgroup quotients. A nonconstant map to E forces genus at least one. A57 applies to genus at least two, and the actual isogeny-with-origin-fiber case of A40 handles genus one. This uses potential good reduction of the curve, not only of its Jacobian.

For the upper cover, C is normal in Pi and contained in H. If N is normal open in H with ell-group quotient, then N intersect C is normal in C and has ell-group quotient there. Intersecting its finite Pi/C orbit gives M normal in Pi, contained in N, and Pi/M an ell-group. This proves the full induced pro-ell topology, not just injectivity in a rational quotient. The image H^(ell) is open and H is the preimage of that image in Pi, since its normal core already has ell-group quotient.

The actual arithmetic map has the preceding injective geometric map and the identity on the common absolute Galois quotient. Its kernel is therefore zero and its image is open. Arithmetic normalizers retain their open image. A geometric pro-ell inertia conjugate lifts to a conjugate in Pi; the ordinary branch double-coset correspondence and the induced-topology equality identify its intersection with H^(ell) exactly with the pro-ell inertia of a cusp of Y. No extra completion kernel can occur.

Finally, for G=S x T of coprime orders every subgroup A splits as (A intersect S) x (A intersect T), by the explicit Chinese-remainder powers in the proof. For B=S x A_T, the two normal cores give G/core_G(B)=T/core_T(A_T) and B/core_B(A)=S/core_S(A_S). Normality of A is unnecessary. These are the actual two geometric Galois closure groups of the intermediate covering maps, proving the required factorization at each coefficient prime, including primes not dividing |G|.

The conclusion concerns all-prime normalizer recognition on every nilpotent-geometric-closure cover. It asserts neither full fixed-group recognition nor cofinality of nilpotent covers among arbitrary finite covers. No included source or register was edited during the checkpoint freeze.

## Pagination correction after checkpoint ten

The theorem number and PDF index above are correct, but the printed page was initially recorded as 196. A fresh opening including the running header (turn947view0, source PDF index 212) shows that Proposition VII.5.5 is on **printed page 197**; page 196 begins the section. The prior checkpoint remains unchanged. This is a locator correction only, with no change to the inspected theorem or proof scope.
