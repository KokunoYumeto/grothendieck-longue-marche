# Independent audit of the selected quartic certificates

The producer files were read completely; no producer routine is imported by either verifier. The verification outputs are criterion_quartic5_verify.json/.out and criterion_quartic3_f5_verify.json/.out. All arithmetic is exact, with input SHA-256 hashes retained.

## 1. Geometry common to both computations

The plane quartic C:W^4=X^3 Z−X Z^3 is smooth in characteristics3 and5. In characteristic3 its partials (up to sign) are Z^3,W^3,X^3; they cannot vanish simultaneously at a projective point. In characteristic5, a simultaneous zero with W=0 would require XZ(X^2−Z^2)=0 and 3X^2 Z−Z^3=X^3−3XZ^2=0, which has no nonzero projective solution. Its affine model W^4=X^3−X has genus3 and unique point P above infinity. The degree-two map C→E:y^2=x^3−x is (X,W)↦(X,W^2), with P sent to O.

For a cyclic odd-degree isogeny E_1→E, pullback gives a degree-ell etale cover of C. In the certificates it is connected: its affine Kummer equation w^4=F(x) has a zero of multiplicity one, so F is not a square or fourth power geometrically. Every kernel point is rational over the specified field, and the fibre above P is the kernel, so this is a constant P-split cyclic cover. Normalization supplies the smooth proper curve.

The rational isogeny is X'=N/h^2, Y'=y*g/h^3, g=N'*h−2N*h'. The polynomial identity

 f*g^2=N^3+A' N h^4+B'h^6

verifies its target equation. Its rational X-coordinate is the sum of the translated x-coordinates minus constants. For a pair ±(a,b), the exact term is

 2(3a^2+A)/(x−a)+4b^2/(x−a)^2.

This follows directly by adding the two chord formulas, so no unverified characteristic-restricted Velu formula is used. The trace over the kernel is invariant under translations and has degree ell; sending O to O makes the map an isogeny with the specified kernel.

For p3, the chosen target isomorphism has scale s and shift r with s^4=−A',r^3+A'r+B'=0. Then X=(N/h^2−r)/s^2, W=w/h^2 and F=f*g^2*h^2/s^6. For p5, the forward 3-isogeny and its independently checked dual have target coefficients A*3^4,B*3^6; scaling by3 returns to E. The formula is X=N/(9h^2),W=w/h^2,F=f_1*g^2*h^2/3^6. Both verifiers check the cleared-denominator identity W^4=X^3−X directly.

## 2. The entire regular differential basis and Cartier

In p3 the polynomial F has degree19 and factorization into three simple roots and eight distinct double roots. In p5 it has degree11 with three simple roots and four distinct double roots. All factors are checked squarefree and pairwise coprime.

At a simple root, x−a has valuation4,w valuation1,dx valuation3. At a double root, x−a has valuation2,w valuation1,dx valuation1. At infinity, x has valuation−4, w has valuation−deg(F), and dx valuation−5. Thus for s=1,2,3 the forms h_s*x^j dx/w^s are regular exactly in the displayed ranges, where h_1=1 and h_2=h_3=g*h. Infinity requires

 deg(F)*s−4 deg(h_s)−4j−5 >=0.

This gives 4+1+6=11 forms in characteristic3 and2+1+4=7 forms in characteristic5. Their distinct Kummer characters and x powers make them independent, and Riemann–Hurwitz gives precisely those genera. They are therefore full bases, not subspaces that could miss rational p-torsion.

For general p prime to4, choose t in{1,2,3} with p*t≡s mod4 and put b=(p*t−s)/4. Since w^(p*t−s)=F^b,

 C(h_s*x^j dx/w^s)=w^(−t)*C(h_s*x^j*F^b dx).

The rational differential on the right is polynomial: extract terms of exponent p*a+p−1, take their pth-root coefficients, and divide by h_t to express the result in the checked basis. The independent code derives t by its congruence and uses explicit exponentiation for pth roots. It does not invoke the producer's Cartier function.

The eighth Cartier iterate is formed as the direct ordered product M*sigma^(-1)(M)*...*sigma^(-7)(M), rather than the producer's repeated-semilinear recurrence. Its characteristic polynomial is independently computed through recursive block adjugates without any division in the characteristic, instead of Bareiss elimination. By Serre duality, the corresponding linear coherent Frobenius matrix is its transpose. The Artin–Schreier fixed-space comparison therefore detects rational p-torsion by the eigenvalue1. Base and new parts split on p-primary groups because the cover degree is prime to p.

## 3. Characteristic three: all six degree-five pullbacks succeed

Input quartic_cyclic5.json: exact field F_(3^8), with modulus recorded in that file. The verifier checks its Rabin criterion at exponents4 and8, checks the two independent E[5] generators, and checks that the six kernel lines exhaust all24 nonzero E[5] points. Every rational isogeny and cover map is verified. Every one of the726 Cartier-matrix entries and all six ordered products are checked; each matrix is11 by11.

All six characteristic polynomials are

 X^3 (X+1)^8,

so det(1−C^8)=1 in F3. The base Cartier operator is zero; hence its Jacobian has no geometric3-torsion. Each cover has stable Cartier rank8, so its new dimension-eight factor is ordinary and has no rational3-torsion over F_(3^8). These are actual rational class-number witnesses. For each of these fixed six covers, every odd-degree extension preserves the unit criterion and every even-degree extension fails: all its nonzero mod3 Frobenius eigenvalues are−1. This uses eigenvalues only and does not assume diagonalizability.

A separate small polynomial-field implementation counts the original curve over F3,F9,F27, obtaining4,4,28. Newton identities and the Weil functional equation give

 H_C(X)=(X^2+3)(X^2−3)^2.

Every root modulo5 has fourth power−1 and exact order8. If any nontrivial constant cyclic5 character existed over F_(3^m), Frobenius^m would have eigenvalue1 on the corresponding5-torsion/dual representation. Thus8 divides m. This necessary field minimum does not require semisimplicity of the repeated factor. The six certificates attain it, so8 is the exact least constant degree for any degree-five witness on this marked curve. Since degree3 is the characteristic and the desired prime is odd,5 is also the least possible prime for this example over all extensions.

## 4. Characteristic five: four cubic pullbacks fail

Input quartic_cyclic3_f5.json: exact field F_(5^8). The independent verifier checks irreducibility, all four initial3-torsion kernel lines, each forward isogeny, the stated dual kernel as an image of an independent3-torsion point, the dual isogeny, and the whole pullback identity. It verifies all196 Cartier entries.

For each of the four genus-seven covers, the eighth Cartier iterate is exactly I_7. For the base it is I_3. Thus every new characteristic polynomial is(X−1)^4; every geometric new5-torsion point is rational and the relative class number is divisible by5. This failure persists over every extension. It concerns four explicit elliptic-isogeny pullbacks only; it does not exhaust the364 geometric cubic characters of the quartic.

The separate small point counts are8,44,104 over F5,F25,F125. They give

 H_C(X)=(X^2+2X+5)^2(X^2−2X+5).

Modulo3, either quadratic relation implies lambda^4=−1, so every eigenvalue again has exact order8. Therefore any nontrivial constant cubic character of this curve requires a field degree divisible by8. This sharpens the field obstruction to all cubic characters, but does not show that every cubic character fails at that first field or afterward.
