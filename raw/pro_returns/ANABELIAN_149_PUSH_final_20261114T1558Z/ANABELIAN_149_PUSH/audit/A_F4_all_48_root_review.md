# Root review: the complete large-conductor theta packet

Date: 14 November 2026. Reviewed candidate: `audit/A_F4_all_48_candidate.md`, Sections 1–8. Independent mathematical review: `audit/A_F4_large_theta_degeneration_review.md`.

**Decision: accept A.C2.25 in its exact scope.** It proves point separation for the two classes omitted from A.C2.22 and therefore completes the 48 ordinary genus-two geometric classes fixed by fourth-power Frobenius. It does not settle arbitrary genus-two moduli points, nonordinary genus-two classes not otherwise covered, or universal A1/A2.

## 1. Independent finite verification

Root ran the fixed canonical verifier, which passed all 1296 exact theta-multiple identities and 60,773 divisor operations. It independently constructs the binary field, uses the pre-existing coefficient-list Cantor arithmetic rather than the C search implementation, and computes the quotient of the unit group by doubling using a general integer Hermite normal form. Its fixed input has SHA-256 `edcf6ed3d425eb72837ae72f521f7221ee91c8a53c1b005885a4c1280d530ae6`.

Root also wrote and ran `code/A_F4_large_theta_root_orbits.py`. It imports no search arithmetic, Jacobian implementation, discrete-log normalization, or Hermite routine. It verifies the field modulus by the binary irreducibility criterion; checks all 1296 original Artin–Schreier equations by shift/XOR polynomial arithmetic; recomputes the curve and Jacobian orders by integer Newton recurrences; and distinguishes all 1296 global doubling orbits by local doubling cycles and the elementary generalized-CRT compatibility criterion. Its input discovery file has SHA-256 `5158fb82718066afba081edc7a844e9120be81535f0960c346cf1af07b7c8eb9`.

The local doubling periods are 3, 5, 1251 and 753. Their least common multiple is 1,570,005, and the unit group has order 2,034,726,480. Thus exactly 1296 primitive orbits exist. The independent signatures are pairwise distinct, so the certificate exhausts them. Multiplying all indices by the inverse of the chosen theta-generator index permutes the quotient classes; the code verifies every reindexing explicitly.

The canonical checks prove that the displayed theta generator has exact order M = 2,454,499,369. They also prove that the independent order-seven class is outside its order-seven line. Together with the exact group order 4·7M, this establishes the entire odd module C7² ⊕ C31 ⊕ C2503 ⊕ C4519. This module structure was not inferred from its order alone. The positive cover theorem needs only the exact order and theta witnesses; the additional module check certifies the discovery procedure as well.

## 2. Curve and Raynaud theta origin

The three Artin–Schreier poles are simple and distinct, so the model is ordinary of genus two. With h = z²+z+alpha and Y = hv, the polynomial equation is Y²+hY = h(z³+z²+z+alpha²), of degree five. It is smooth at the finite branch points because the factor multiplying h is nonzero there; elsewhere the Y derivative is nonzero. The smooth proper model has one point at infinity.

The different exponents are all two. Pulling back the divisor of dz on the line gives div(dz) = 2(W1+W2−W∞). Hence the locally exact differential identifies Raynaud's degree-one line bundle with B = W1+W2−W∞. The implemented class T = (h,0) is W1+W2−2W∞, of order two. Therefore P−W∞+T equals P−B in Picard degree zero. The sign and origin used by the program are exactly those required by the theta criterion; ordinary Abel images based only at infinity would not suffice.

The coordinate change splitting h gives unordered parameters with polynomial Z³+alpha Z²+alpha², class 203. Coefficientwise squaring gives class 302. This field automorphism carries the full divisor and cover construction, not merely the point count. The identification with the existing 48-class enumeration is therefore exact.

## 3. Polynomial arithmetic is a divisor certificate

Root independently opened the complete author PDF of Lange, *Formulae for Arithmetic on Genus 2 Hyperelliptic Curves*, at `https://www.hyperelliptic.org/tanja/preprints/expl.pdf` (retrieval `turn814view0`). Theorem 2.2 and Algorithms 3.1–3.2, author pages 5–6, allow the general equation Y²+hY=f and characteristic two. The TU/e publication record independently confirms the journal metadata: Lange (2005), *Applicable Algebra in Engineering, Communication and Computing, 15*(5), 295–328, DOI 10.1007/s00200-004-0154-8.

The candidate's two extended-gcd formulas agree with the opened general composition algorithm. The quotient U1U2/d² removes the paired opposite-point contributions, including ramified fibres. The Bezout identity supplies the corresponding second generator of the product ideal. The reduction step follows from the norm of Y+V and hyperelliptic conjugation. Making a polynomial monic changes no divisor. The general gcd implementation covers repeated points and the identity; it does not assume generic-position denominators.

Every polynomial division in the canonical implementation is exact and every resulting Mumford pair is checked on the curve. Uniqueness of the reduced representative makes comparison of these pairs an exact Picard-group test. Binary multiplication therefore verifies the asserted finite divisor equalities, not a numerical approximation or a probabilistic group membership test.

## 4. From theta incidence to point separation

An exact-order-M line bundle with a chosen trivialization of its Mth power gives a finite étale mu_M torsor. M is odd, and exact order makes the torsor geometrically connected. The construction and its cyclic deck group descend after a finite constant extension. Riemann–Hurwitz gives genus M+1.

For every primitive character, the relevant cohomology space has dimension one. The Raynaud exact sequence makes its Frobenius arrow zero precisely at a theta multiple. Each primitive doubling orbit contains one of the certified multiples, so Frobenius is nilpotent on the whole primitive conductor-M summand. Consequently that primitive Jacobian factor has two-rank zero. No vanishing assertion is made for characters of smaller conductor.

A.C2.19, or equivalently the all-genus A.C2.20 criterion, now applies. The four prime factors give a sixteen-term primitive operator and M is larger than the required 225 bound; the already reviewed geometric support and controlled-field proof supplies the section conclusion. The finite calculation is an input to that proof, not a replacement for it.

Collision is preserved by finite extension. Every form in the stated scope becomes isomorphic to the certified curve after a finite extension, where the cover data are also defined. Thus a collision on the original form would contradict the criterion after extension. Functoriality to the smooth compactification handles the hyperbolic opens. The coefficient conjugation proves the other class, and A.C2.22 supplies the preceding 46.

## 5. Retained limitations

The theorem is positive and needs no exhaustive negative scan. The previous exclusions of small primary packets, the entire 73-power primitive-zero route, and the specified mixed packets remain valid. They do not exclude this four-prime conductor. The theorem does not contradict the no-fixed-finite-prime-set result, and it does not establish the existence of such a complete packet for every curve. Earlier unresolved language referring specifically to these two F4 classes should be replaced by a forward reference to A.C2.25 while the general unresolved obligations remain.
