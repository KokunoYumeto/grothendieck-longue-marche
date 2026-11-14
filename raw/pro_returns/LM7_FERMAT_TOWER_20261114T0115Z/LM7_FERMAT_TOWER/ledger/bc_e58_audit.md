# Independent audit of E.58

Status: PASS. Audited by bc_fermat on 2026-11-13.

I read the complete theorem and proof in `research_e58/sections/E_elliptic_frobenius.tex`, opened the original EMS publication of Nakamura (2013), DOI 10.4171/PRIMS/110, and checked Sections 3.6 and 5.9, Theorem 5.2.4, Proposition 5.7.3 and its proof, and Theorem 6.10.3. The official full text is https://ems.press/content/serial-article-files/41205?nt=1 .

The following comparisons were checked directly.

- The plane-cubic map and its displayed inverse give the stated Weierstrass equation. The local parameter is s/3 to first order; composing with the actual multiplication-by-three map gives the unit tangent, with no further tangent Kummer character.
- In the integral completed ring, the intersection J intersect m^2 equals Jm: comparing the linear coefficients forces both constant coefficients to vanish over Z_3. This proves the actual fiber-product map, including surjectivity. The eleven-vector ring has the stated two independent carry laws and continuous inverse presentation.
- The ideals J^3+PJ^2, Jm, m^2 and J give the exact quotient maps. The 54-dimensional truncated ring has precisely three primitive additional relations, proving rank51. The free module maps give the asserted rank40, rank48, rank8 and rank2 kernels.
- The identities (X-1)P=3U, (Y-1)P=3V, UP=9U and VP=9V prove the actual lower-central lattices and the finite (Z/9)^2 summands. The quotient preserves the full ten-dimensional abelianization.
- Nakamura's equation (3.6.3) identifies the actual Tate-kernel action with conjugation by c^E, with the sign fixed by z=c^{-1}. Theorem 6.10.3 gives augmentation kappa_Delta/12. Consequently the kernel of the actual (Tate,kappa_Delta) pair acts through Jm on N and through m^2 on the ambient commutator module. This proves the asserted arithmetic factorization on the displayed quotients, without asserting a section of an unrestricted matrix group.
- The reference Tate map fixes the cusp with multiplier four, and its exact metabelian substitute has the same ambient class-three action. Their ratio is inner by an augmentation-zero element, which is precisely enough to vanish on R. The actual braid twists give the diagonal reference and discriminant increment. The root-system change has coherent exponent1/2 and Frobenius coboundary3/2, giving the integral Dehn-twist comparison and the inner correction c^{1/8} with the stated sign.
- The good model has three points over F_2; Frobenius at the K-prime over two is -2 on the Tate module. The resulting thirteen generator images agree with the exact word collection.

Fresh copies of both `a_elliptic_frobenius.py` and `a_elliptic_rank13.py` were run in this audit directory. Both JSON outputs are identical to the supplied certificates. The checks include1331 ring associativity identities,144 group/action comparisons,156 power identities, the integer right inverse of the ambient projection, and all displayed path-transport formulas. No correction is required.
