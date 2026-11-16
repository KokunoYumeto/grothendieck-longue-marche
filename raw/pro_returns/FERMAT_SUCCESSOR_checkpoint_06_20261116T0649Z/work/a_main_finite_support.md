# A.69: all finite-support exponents at the actual level-three joint quotient

This completes the baseline-zero case left open in A.68. Together with A.68 it proves: on E:y²+y=x³−1, R=(1,0), U=E−E[3], the actual joint compact/X(3) quotient Γ3 admits a Selmer lift of aκ(R), for an exponent a differing from an integer n at only finitely many coefficient primes, if and only if a=n. No assertion about arbitrary infinite alterations or the finite quotient's fibres is made.

Set K=Q(ζ), ζ²+ζ+1=0, b³=3, L=K(b)=Q(E[3]), and

 g=(b²ζ²x−y−2)/(b²x−y−2).

This is the genuine Γ3 character already proved in A.67 by its kernel argument. Its divisor is 3(d1)−3(d0), d_i=(bζ^i,1), and it extends as a unit at O with g(O)=1. A hypothesized Γ3 Selmer section supplies a global quadratic class β in L×/L×². At an interior forced compact centre Q its local value is g(Q); at O its value is1 regardless of cusp tangent, because g kills cusp inertia there.

## 1. A common division-tower argument

Let P be the nonempty finite support of a. Let F0/K be a finite abelian extension and let T∞/F0 be the joint torsion and R-division tower for p in P. Put A∞=F0(E[p∞]:p in P). Its Galois group over K is abelian because all CM endomorphisms of E are defined over K and the Tate representation is a rank-one module over the CM algebra; F0/K is abelian too. The translation kernel

 J=Gal(T∞/A∞) ⊂ product_{p in P} T_p E

is a closed additive subgroup, hence is the product of its p-primary subgroups J_p. The joint torsion image preserves every J_p.

If 2 is absent from P, every homomorphism Gal(T∞/F0)→C2 kills J. If 2 is present and the residual E[2] image over F0 is C3, the same conclusion holds. Indeed choose an element A of the joint torsion image whose 2-component has residual order3. Then det(A−I) is a 2-adic unit. Cayley–Hamilton expresses (A−I)^−1 as an integral polynomial in A, so (A−I)J_2=J_2. A quadratic character kills the commutators [A,J_2]=(A−I)J_2 and kills all the odd J_p. Consequently every quadratic extension of F0 contained in T∞ lies in A∞ and is Galois (in fact abelian) over K.

Suppose L⊂T∞. Then √β⊂T∞. Otherwise, over the finite field F0L⊂T∞, the quadratic extension defined by β is disjoint from the Galois tower. A.61's simultaneous zero-primary Frobenius condition can be imposed together with its nontrivial quadratic Frobenius, by Chebotarev. At those good places R_p=0 for every p in P; therefore aR=O. Full local compact Kummer injectivity identifies the local Selmer centre as O. Since g(O)=1 and g kills its cusp inertia, β must be locally trivial, contradiction.

Now suppose there are p in P with a_p≠0, a p-primary torsion point S outside E[3], and h=g(S)∈F0×, such that F0(√h)/K is not Galois. The preceding character argument gives √h∉T∞. Choose a p-primary torsion point T with a_p T=S and take a finite field F_r⊂T∞ containing F0L, √β, and T. Such T exists by dividing by the finite valuation of a_p and inverting its unit part. Since √β lies in the tower but √h does not, F_r(√(h/β)) is quadratic and disjoint from T∞. Apply A.68's prescribed-primary Frobenius lemma after this particular base extension: prescribe R_p=T and R_q=0 at all other q in P, together with nontrivial Frobenius in that quadratic extension. The compact local centre is then aR=S, an interior point, so Selmer compatibility says h/β is a local square. This contradicts the imposed Frobenius.

This argument requires no independence after a base extension that kills the residual C3: noncontainment of √h in the whole tower was proved over F0 first, and is retained under every finite intermediate extension. Only √β∈T∞ is needed; it need not be placed in the torsion subfield after extending F0.

## 2. The coefficient-two witness

Assume 2∈P. Let c³=2 and F0=K(c). The classes of2 and3 are independent in K×/K×³: the valuation at the prime above2 first forces the coefficient of2 to be divisible by3, and the valuation v_(1−ζ)(3)=2 then forces the coefficient of3 to be divisible by3. Thus b∉F0.

Put r=b/c², so r³=3/4, and S=(r,−1/2) is a nonzero point of E[2]. Its field is F0(S)=F0(b)=F0L. In particular L lies in T∞ and the residual E[2] image over F0 is C3. Moreover

 h=g(S)=(ζ²c−1)/(c−1) ∈ F0×.

At the prime31 embedding c≡4, ζ≡25, h≡27, and 27^15≡−1 mod31. The defining polynomials have simple roots there, so h is a nonsquare in F0. Its three conjugates under c→ζc have product1. If F0(√h)/K were Galois, the squareclass of h would be invariant under Gal(F0/K)=C3. Taking the product of the three conjugate squareclasses would then give [h]^3=[h]=1, contradiction. This supplies every hypothesis of section1, and excludes every finite-support exponent with a_2≠0, regardless of its other components.

## 3. A uniform coefficient-p witness for every p≥5

Let p≥5. The CM Galois image on E[p] over K is the full Cartan (O_K/p)×. Here is the exact local input, with no appeal to a global CM surjectivity theorem. If p splits, the two idempotents of O_K⊗Z_p split the p-divisible group into height-one factors; one is formal and one is étale. Good ordinary inertia at either prime of K above p acts through one full F_p× factor. The conjugate prime gives the other factor, and these generate the whole split Cartan. If p is inert, the good reduction is supersingular: an ordinary connected height-one factor would not admit the unramified quadratic CM action. Since K_p/Q_p is unramified, the e=1 supersingular inertia theorem gives the full nonsplit Cartan F_{p²}×. These are exactly the primary statements checked in Serre1972, Propositions11–12, printed pp273–275.

In either case the inertia groups at p generate the entire group Gal(K(E[p])/K). Since L/K is unramified at p, this proves K(E[p])∩L=K. Therefore Gal(L(E[p])/L) is the full Cartan.

Choose a nonzero S∈E[p] in the inert case, and choose S with both split CM components nonzero in the split case. Its orbit over L has size p²−1 in the inert case and (p−1)² in the split case. These sizes are at least24 (p5) and36 (p7), respectively.

We prove that h=g(S) is nonsquare in F0=L(E[p]) by one exact dyadic calculation. E has good reduction at2 and E(F2) has3 points, so Frobenius_4=[−2] on its reduction. The field L splits over K at2: choose b∈Q2 with b³=3, b≡3 mod4; then b²≡1 mod4. Every completion of F0 above this embedding is unramified over Q2, since p is odd and E has good reduction. For every p-torsion point A, Frobenius_4 acts on A as [−2]A, by injectivity of prime-to2 torsion reduction.

If g(A)=u² in this unramified local field, then σ4(u)≡u^4 mod2 and hence

 g([−2]A)=σ4(g(A))≡g(A)^4 mod4.

All these values are units: nonzero p-torsion reduces away from E[3], which supports the divisor of g. Set g0=(ζ²x−y−2)/(x−y−2). Replacing b² by1 changes g only by a multiple of4 at these points. With m=3x²/(2y+1), the coordinates of [−2]A are X=m²−2x and Y=y−m(x−X). The exact reduced numerator of g0(X,Y)−g0(x,y)^4 is divisible by2. Its half, reduced modulo2 on E/F4, is

 F=(ζ+1)x^11+ζx^10y+x^9+(ζ+1)x^8y+x^6y+x^6+ζx^4y+(ζ+1)x²+ζxy.

The reduced denominator modulo2 is (x+y)^8. Its only affine zero on the curve is (1,1), an order-three point, so the denominator is a unit at every nonzero p-torsion reduction. Thus g(A) square implies F(Abar)=0.

The nonzero function F has exact pole order23 at O: x has pole order2, y pole order3, and the unique term of maximum pole order is ζx^10y. It has at most23 geometric zeros. If h=g(S) were a square in F0, every value at the full Cartan orbit of S would be a square in F0. Reducing all those points at the chosen dyadic place would give at least24 distinct zeros of F, because reduction is injective on odd torsion. Contradiction. Therefore h is nonsquare in F0.

Now F0/K is abelian. The disjointness K(E[p])∩L=K supplies an order-three automorphism τ that fixes S and sends b to ζb. The three values h,τh,τ²h have product1, by telescoping the three tangent-line ratios. Since h is nonsquare, the same squareclass argument as in section2 shows F0(√h)/K is not Galois.

Finally F0 is unramified at2, whereas E[2] requires a cube root of3/4, of dyadic valuation−2/3. Its residual C3 therefore survives over F0. Thus section1 applies whether or not2 belongs to P. (For the conclusion it is enough to use this case when2 is absent, but the stronger assertion costs nothing.) This excludes every finite-support exponent with a nonzero p-component for some p≥5.

## 4. Conclusion and certificate

Every nonzero finite-support exponent has either a nonzero2-component, a nonzero p≥5 component, or support exactly{3}. The first two cases have just been excluded; A.68 excludes the third. The zero exponent is realized by the rational O-cusp. Together with A.68 for nonzero integer baselines, this proves the stated exact exponent classification for all finite alterations of all integers.

The exact symbolic identities, the reduced denominator, the pole bound, the cubic-conjugate norm identities and the nonsquare at31 are executed in deliverable/code/a_main_finite_support.py with its raw output a_main_finite_support.out. The orbit argument is uniform in p; no finite range of primes is substituted for it. Root and B independently audited the common tower argument and the dyadic/Cartan proof.
