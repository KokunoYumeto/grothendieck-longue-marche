# Independent A186 descent and arithmetic audit

Auditor: local_preprint. Date: 2026-11-16 UTC.

## Outcome and exact scope

The complete arithmetic certificate `code/point3_fermat8_genus2_rank_certificate.gp` was independently read and rerun, using `/tmp/birational-pari-runtime/pari-2.19.1/gp`. All assertions passed. The exact descent, Weil-pairing, local-isotropy and support maps described below also pass. This audit precedes the author's final theorem source; that saved source will receive a separate wording/map audit.

For the six curves in A182, the proved Selmer upper bound is two. A182 supplies a non-torsion rational Jacobian point in each case, and the factorization into a rational linear factor and one irreducible quartic gives rational two-torsion dimension one. The finite Kummer exact sequence therefore gives rank one, Selmer dimension two, and vanishing of the entire two-primary Tate--Shafarevich subgroup for each of these six Jacobians. Together with A185 and the actual A182 isogeny, their ranks sum to fourteen. This argument does not identify the two-primary Tate--Shafarevich group of the whole Fermat Jacobian across that isogeny.

## Actual curve and coefficient maps

For `G_(A,B): Y^2=A X^5+B X`, the map

    x=A X, y=A^2 Y

has the literal inverse `X=x/A, Y=y/A^2` and gives `C_c: y^2=x^5+c x`, where `c=A^3 B`. It extends between the smooth projective models. The six values of `c` are

    -54, 648, -432, 13824, 27, -4608.

Put `K=Q(theta)`, `theta^4+c=0`, and `L=Q x K`. Each quartic is irreducible, as independently checked in the certificate. There are exactly two irreducible factors of `x^5+cx`.

Let `D_i=[W_i-infinity]` for the five finite branch points. The identities

    div(x-r_i)=2 W_i-2 infinity,
    div(y)=sum_i W_i-5 infinity

give the unique relation `sum_i D_i=0`. Normalizing the common pole at infinity in the Weil-pairing formula gives

    e_2(D_i,D_j)=(r_j-r_i)/(r_i-r_j)=-1 (i != j),
    e_2(D_i,D_i)=1.

Consequently the actual map `D -> (e_2(D,D_i))_i` identifies `J[2]` with `ker(product:mu_2^5 -> mu_2)`. It sends `D_i` to the vector with four minus signs and one plus sign at position `i`. The coordinate dot pairing agrees with the Weil pairing: distinct such supports have intersection size three and a support with itself has size four. These vectors span the four-dimensional kernel. The diagonal copy of `mu_2` splits the product map because five is odd. Applying Galois cohomology and Kummer gives exactly

    H^1(Q,J[2]) = ker(N:L^*/L^{*2} -> Q^*/Q^{*2}).

In particular there is no additional diagonal quotient. The literal isomorphism from `K^*/K^{*2}` to that kernel is

    eta -> (N_(K/Q)(eta), eta).

Indeed the product norm of this pair is `(N eta)^2`; conversely the first component of every norm-kernel pair equals `N eta` modulo rational squares.

## Local row and its isotropy

For an actual local point `(q,y)` with `q(q^4+c)=y^2 != 0`, the class of `(q,y)-infinity` has Kummer coordinates `(q,q-theta)`. The norm identity is `N_(K/Q)(q-theta)=q^4+c`. The coordinate Weil pairing and the norm/corestriction projection formula therefore give

    (N eta,q)_p * product_(P|p) (eta,q-theta)_P
      = product_(P|p) (eta,q(q-theta))_P.

This is precisely the product evaluated by the program. Changing any representative by a square leaves all entries unchanged. The rational linear factor is accounted for by the factor `q`, rather than discarded.

Under the canonical principal polarization, the local Kummer image `J(Q_p)/2J(Q_p)` is its own annihilator for the finite Weil-cup pairing. In particular it is isotropic. Thus pairing a locally soluble global Selmer class with any of these actual local point classes gives zero. Only this necessary condition is used; the computation does not assume the listed points generate every local Kummer image.

Primary source checked directly: Milne, *Arithmetic Duality Theorems*, second edition, Chapter I, proof of Theorem 3.2, printed p.42 (PDF p.49), supplies the finite Kummer/Ext duality diagram. Remark 3.5, printed p.44 (PDF p.51), identifies the pairing with the Weil-cup pairing. The characteristic-zero local-field theorem includes the place two.

## Completeness of the global candidate space

The literal discriminant is `disc(x^5+cx)=256 c^5`, supported on two and three. Stoll's Corollary 4.7 therefore places every Selmer class in squareclasses with even valuations outside the primes above two and three. In the quartic factor, the exact ideal sequence is

    0 -> O_(K,S)^*/O_(K,S)^{*2}
      -> {eta in K^*/K^{*2}: outside-S valuations even}
      -> Cl(O_(K,S))[2] -> 0.

The certificate proves every relevant S-class group is trivial. Hence the complete candidate group is the S-unit squareclass group. The free rank and the one even-order torsion-unit squareclass give dimensions

    5, 6, 5, 4, 4, 5.

Every hardcoded generator is checked by `bnfisunit(B,G[j],U)` against the full `bnfunits(B,S)` group; the resulting square coordinate matrix is full rank modulo two. Thus the displayed literal bases span the entire candidate space, not just a subgroup discovered by a search.

The program calls `bnfinit(F,1)` to retain full units and then calls `bnfcertify(B)` with its default flag zero. The official PARI manual explicitly makes return value one the unconditional certification of the class/unit data. All six returns equal one. The fourth quartic field has ordinary class number two; its S-class group is nevertheless trivial, and the proof uses the latter exact group. The other five ordinary class groups are trivial.

## Executed finite checks

The independently rerun certificate checks all six irreducibilities, curve and field discriminants, integral bases, certified class/unit groups, S-prime ideals, full squareclass bases, and seventeen local point rows. Every local point has a nonzero curve value with even valuation and square unit residue (modulo eight at two, modulo three at three), so it is an actual local point.

The row ranks and remaining dimensions are:

| c | candidate dimension | row rank | remaining dimension |
|---:|---:|---:|---:|
| -54 | 5 | 3 | 2 |
| 648 | 6 | 4 | 2 |
| -432 | 5 | 3 | 2 |
| 13824 | 4 | 2 | 2 |
| 27 | 4 | 2 | 2 |
| -4608 | 5 | 3 | 2 |

All primewise Hilbert symbols and their products are retained in the author's output. The rerun ended with the exact PASS line for all six cases. No mathematical correction was found.

## Primary references opened

- Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arithmetica 98.3 (2001): Lemma 4.1, Proposition 4.2, Lemma 4.3, Corollary 4.7 and Lemma 4.9. https://www.impan.pl/shop/publication/transaction/download/product/83397
- Milne, *Arithmetic Duality Theorems*, Chapter I, Theorem 3.2 proof and Remark 3.5. https://www.jmilne.org/math/Books/ADTnot.pdf
- Official PARI manual, `bnfcertify`, `bnfunits`, `bnfisunit`, `bnfsunit`, `nfhilbert`. https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html

## Final saved-source audit

The complete source `sections/point3_fermat8_genus2_ranks.tex` was subsequently read end to end. PASS, with no mathematical correction.

All twenty-nine changes from polynomial representatives to the displayed integral bases were checked literally. In particular the minus signs in the bases for `c=-432` and `c=-4608` produce exactly the original certified generators. Every displayed matrix and kernel agrees with the executed output. The local valuation proof of quartic irreducibility is valid in every row. The branch Kummer value `(c,-theta)` and its resulting second Hilbert argument `-c theta` also agree with the same coefficient map.

The source uses the rational symmetric theta divisor and `O(2 Theta)` to apply Poonen--Rains, *Random maximal isotropic subspaces and Selmer groups*, Section 4.1, Corollary 4.7, Propositions 4.9 and 4.11. I independently opened the author PDF and read these precise passages: https://math.mit.edu/~poonen/papers/selmer.pdf . They prove the required Weil-cup isotropy for the actual multiplication-by-two Kummer image. The minus sign in the source's bilinear polarization has no effect on the order-two Hilbert pairing.

I also independently checked the additional ordinary-class assertion in the fourth row: with `B=bnfinit(x^4+13824,1)` and `bnfcertify(B)=1`, the `bnfisprincipal` class coordinates of both the unique prime over two and the unique prime over three are `[1]` in the certified cyclic class group of order two.

The final finite-to-all-two-power conclusion follows from the finite Kummer exact sequences and the elementary fact that every nonzero finite two-power-order element has a nonzero multiple of order two. It invokes no finiteness theorem for the whole Tate--Shafarevich group. The exact rank-fourteen conclusion uses the actual isogeny of A182 and the factor ranks of A185. The source retains the stated scope concerning sections and local Chabauty sets.
