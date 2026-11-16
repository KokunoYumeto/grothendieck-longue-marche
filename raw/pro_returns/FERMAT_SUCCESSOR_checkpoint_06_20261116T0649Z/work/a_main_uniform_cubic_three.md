# Uniform coefficient-three congruence obstruction for every rational-origin cubic twist

WORK ONLY during the checkpoint06 manuscript freeze. Proposed successor to A.69, not yet integrated.

## Exact statement

Let E_d be the smooth compactification of X³+Y³=dZ³, d∈Q×, with the rational infinity flex O=(1:−1:0) as origin; let D=E_d[3], U_d=E_d−D. Take R∈E_d(Q) of infinite order and the actual joint compact/j-line X(3) quotient Γ3 of A.67 (J=X³/(dZ³)). If a_q=n for every q≠3, with n∈Z, then aκ(R) has a Γ3 Selmer lift if and only if a=n. The statement includes n=0. Every diagonal cubic with a rational infinity cusp is of this form after rational rescaling.

Together with the uniform p≠3 norm argument of A.68, this proves: on EVERY such cubic twist and for EVERY nonzero integer n, the Γ3 Selmer exponents among all finite alterations of n are exactly n. This completes the uniform one-extra-prime mechanism, including the previously exceptional coefficient3. No finite-support baseline-zero assertion at arbitrary other primes on every twist is made here.

## 1. A necessary squareclass condition from a pure3 alteration

Let L=Q(E_d[3]), which contains the CM field. Choose a normalized flex-ratio unit g with divisor3(d1)−3(d0) for distinct cusps in the J1 block and g(O)=1. Its quadratic Kummer character factors through Γ3,L by A.67.

Write B=nR and δ=a3−n. Suppose δ≠0. Over L the full proper3-torsion and R-division tower is pro3. By A.61, quadratic disjointness, and zero-primary Chebotarev, the global g-character must be κ2(g(B)) if n≠0; when n=0 it is trivial because g is regular atO with value1 and kills cusp inertia.

For any3-primary torsion point S with B+S outside the divisor ofg, choose a3-primary T such that δT=S. Over a sufficiently deep3-torsion field T is rational. A.68's prescribed-primary lemma then forces

             g(B+S)/g(B) to be a square

in the finite3-torsion field defining S (or in any sufficiently deep such field). Otherwise its quadratic extension remains nontrivial under the odd extension defining T and is disjoint from the pro3 division/Kummer tower; Chebotarev simultaneously prescribes R3=T and nontrivial quadratic Frobenius, contradicting the forced global g-character. For n=0 use g(B)=g(O)=1 and omit S in D.

We will contradict this necessary condition at the dyadic place. Only torsion translations and unit evaluations occur; no claim about a full punctured-cover lift is needed.

## 2. The local cubic untwisting and the torsion fields

Let E0 be E9:y²+y=x³−1, with the same j-line coordinate and flex unit

 g0=(b²ζ²x−y−2)/(b²x−y−2), b³=3, ζ²+ζ+1=0,

as in A.69. The curve E_d is isomorphic to the Fermat model of E9 over a cube root t of9/d, by (X,Y,Z)↦(tX,tY,Z). This map preserves J and O. Hence it takes the J1 cusp block to that of E9. Choosing the two corresponding flexes and normalizing value1 atO makes the transported unit exactly g0.

Every unit in Q2× is a cube (Hensel, since3 is odd), so the isomorphism is defined either over Q2 or over a totally ramified cubic extension. Set K2=Q2(ζ), the unramified quadratic extension, and F=K2(t). Thus either F=K2 or F/K2 is cyclic, totally ramified, of degree3. In the latter case a generator τ changes the isomorphism by one of the CM automorphisms [ζ] or [ζ²]. If B' denotes the image of the Q2-rational point B, then

                 τ(B')=[ζ]^k B',       k=1 or2.

The good curve E0 has all its3-torsion over K2 (b³3 has its odd root inQ2). Therefore the local3-torsion field of E_d is exactly F: in the nontrivial case the CM order3 action on E0[3] is faithful. Every higher3-torsion field becomes F M_r, where M_r/K2 is unramified, since E0 has good reduction at2. The global squareclass condition from section1 consequently holds in these local fields F M_r for all translated3-primary torsion points.

## 3. Subtract the torsion reduction

In the unramified case B' lies in E0(Q2), so its reduction is in E0(F2), a group of order3. Let B0∈E0[3](Q2) be its unique prime-to2 torsion lift.

In the ramified cubic case τ acts trivially on the residue field, so reduction of τB'=[ζ]^k B' gives [ζ]^k Bbar=Bbar. Thus Bbar lies in ker([ζ]−1), an order3 subgroup. Let B0 be its unique3-torsion lift; it belongs to E0[3](K2), is fixed by [ζ], and is fixed by τ.

In either case Bf=B'−B0 lies in the formal group. If B is nontorsion, then Bf≠O. The necessary squareclass condition is unchanged by this torsion shift: divide the condition at S−B0 by the condition at−B0. Consequently

              g0(Bf+T)/g0(Bf) is a square

in the relevant field F M_r for EVERY3-primary torsion point T for which the values are ordinary. If B=O, use Bf=O and the same condition directly. In the ramified case τBf=[ζ]^kBf remains true.

Use the standard integral formal parameter z=−x/y on E0. It satisfies the exact identity z([ζ]Q)=ζz(Q), not merely a first-order approximation. Write h=v_F(z(Bf)) when Bf≠O, using normalized integer valuation on F. Then h≥1.

## 4. Odd formal height

If h is odd, take T=d0, the pole ofg0. Translation by d0 is an isomorphism of the good integral model. The threefold pole has unit leading coefficient: its denominator reduces to x+y, whose intersection with the reduced curve is (x+1)³; the numerator is nonzero at d0. Therefore

        v_F(g0(Bf+d0))=−3h,
        v_F(g0(Bf))=0.

The ratio has odd valuation. All extensions M_r are unramified, so it cannot be a square in anyF M_r. This contradicts section3.

## 5. Even formal height in the unramified case

Suppose F=K2 and h is even, hence h≥2. Then Bf isO modulo4 in the formal group, and g0(Bf)≡1mod4. For every T∈E0[9]−E0[3], its reduction is outside the divisor ofg0 and

          g0(Bf+T)/g0(Bf) ≡ g0(T) mod4.

The ratio is a square in an unramified dyadic field. Arithmetic Frobenius σ4 fixes Bf and acts on T by[-2], since E0(F2) has3 points. For a square unitu², σ4(u²)≡(u²)^4mod4. Applying this to the ratio gives

                  g0([-2]T)≡g0(T)^4 mod4.

By the exact A.69 calculation, every such Tbar is a zero of the nonzero function Fbar with exact pole order23. There are |E[9]−E[3]|=81−9=72 distinct reductions, because reduction is injective on odd torsion. This is impossible. The same argument applies to Bf=O.

## 6. Even formal height in the ramified cubic case

Suppose [F:K2]=3 and h is even, hence h≥2. Let M/K2 be an unramified field containing a chosen T∈E0[9]−E0[3] and any other torsion needed. The fields F andM are disjoint. Since τz(Bf)=ζ^k z(Bf), one has

        z(Bf)^3∈K2,       v2(z(Bf)^3)=h≥2.

For a formal variable z, translation of T by the corresponding formal point has good integral coordinates, and g0 is a unit at the reduction ofT. Hence g0(T+Q(z)) is an integral formal power series over O_M, constantg0(T). Its product over z,ζz,ζ²z is invariant under z↦ζz, so it is a power series in z³ with integral coefficients and constantg0(T)^3. It follows that

 N_{FM/M}(g0(Bf+T))
       =product_{i=0}² g0(T+[ζ]^iBf)
       ≡g0(T)^3 mod4.

The denominator norm is exactly1:

             product_{i=0}² g0([ζ]^iBf)=1,

because the three tangent-line ratios telescope. (For Bf=O useg0(O)=1.) The norm of the square ratio in section3 is therefore a square unit in the unramified fieldM and is congruent to g0(T)^3 modulo4.

Apply σ4 to this norm. It fixes its coefficients in K2 and takesT to[-2]T. The square-unit congruence gives

                 g0([-2]T)^3 ≡ g0(T)^12 mod4.

Modulo2, g0([-2]T)=g0(T)^4 automatically. Thus the factor

 g0([-2]T)^2 + g0([-2]T)g0(T)^4 + g0(T)^8

is a unit. Factoring the difference of cubes implies

                 g0([-2]T)≡g0(T)^4 mod4.

Again all72 reductions of E[9]−E[3] would be zeros of the same A.69 function of pole order23. Contradiction.

## 7. Scope and remaining cases

This proves the pure coefficient3 statement for all rational-origin cubic twists, including twists ramified at2 and baseline0. Combined with A.68 it gives the complete finite-alteration classification around every NONZERO integer on every such twist, so every one-extra-coefficient-prime ghost in that family dies already at the actual joint X3 quotient. For E9, A.69 additionally settles all finite support around0. This argument does not determine arbitrary infinite alterations or finite quotient fibres, and does not claim a result for a cubic torsor without a rational origin.

The only new local algebra beyond A.69 is the exact CM identity z([ζ]Q)=ζz(Q), the integrality of good-reduction translation, and the norm power-series invariance. No new arithmetic tables, analytic rank computation, or unopened theorem is used.
