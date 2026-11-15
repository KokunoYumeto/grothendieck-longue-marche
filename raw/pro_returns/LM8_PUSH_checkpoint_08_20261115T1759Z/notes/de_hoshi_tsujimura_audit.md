# The infinity cusp in the June 2021 Hoshi–Tsujimura preprint

## Source and exact scope of this check

Verified primary source: Yuichiro Hoshi and Shota Tsujimura, *Construction of Abundant Explicit Nongeometric Pro-p Galois Sections of Punctured Projective Lines*, RIMS preprint 1950, June 2021:

https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1950.pdf

The source was opened in full, including Theorem A on printed pages 2–3, Proposition 1.4(ii) on printed page 6, and Corollary 2.5 and Remark 2.5.1 on printed pages 10–11. Retrieval references: turn515view0, turn515view1; page screenshots: turn516view0, turn516view1. The observation below concerns exactly that version. No statement about another version is inferred.

None of D.1–D.52, or of Part E, uses this preprint as an input. In particular D.52's abelian slope is (1,2), not a diagonal slope.

## Explicit counterexample to the stated exclusion of all geometric lifts

Take the odd regular prime p=3, F=Q(zeta_3), and x_1=x_2=3. These elements lie in the specified maximal extension unramified outside p and are p-units, as required by Theorem A. They are not roots of unity of order prime to p.

There cannot be roots of unity zeta_1,zeta_2 with

\[
1=3\zeta_1+3\zeta_2.
\]

Otherwise 1/3 would be an algebraic integer. Thus the hypothesis of Theorem A(ii), and all the additional hypotheses of its part (iii), hold.

Nevertheless the pro-p torus section with Kummer coordinates

\[
(\kappa_F(3),\kappa_F(3))
\]

has a geometric cuspidal lift at infinity. Here is the full calculation, including its tangent normalization. On the tripod X=P^1 minus {0,1,infinity}, choose the uniformizer u=1/t at infinity, and take the rational tangent vector a=1/3 in that coordinate. Under the tangential specialization u=a epsilon, the leading terms of the two units defining the torus embedding are

\[
t=a^{-1}\epsilon^{-1},
\qquad
1-t=-a^{-1}\epsilon^{-1}(1-a\epsilon).
\]

The associated tangential Galois section therefore has abelian Kummer coordinates

\[
(\kappa_F(a^{-1}),\kappa_F(-a^{-1}))
 =(\kappa_F(3),\kappa_F(3)).
\]

The second equality uses kappa_F(-1)=0 for odd p. The factor 1-a epsilon has leading unit 1 and contributes no constant Kummer class. This is an actual rational tangential section of the full arithmetic fundamental group, hence also of its geometric pro-p quotient; its image lies in the infinity decomposition subgroup. It contradicts the assertion in Theorem A(iii), repeated in Corollary 2.5(iii), that every lift with these coordinates is nongeometric.

The same example works with every odd regular p and x_1=x_2=p. It is already enough to take p=3.

## The precise missing case and its repair

Proposition 1.4(ii) lists an ordinary point case and the finite punctures a_i, but does not list the puncture at infinity. In its coordinates a_i-t, a tangent at infinity has the same Kummer coordinate at every i. Thus the list requires the additional condition

\[
x_i/x_1\in\bigcap_{n\ge 1}(K^\times)^{p^n}
\quad\text{for every }i.
\]

For a number field or a finite extension of Q_p this infinitely p-divisible subgroup is exactly the group of roots of unity of order prime to p: valuations vanish, and the remaining unit factors have no infinitely p-divisible non-torsion element. For the two-coordinate Theorem A, the sufficient nongeometricity condition is consequently the stated ordinary-point exclusion together with

\[
x_1,\quad x_2,\quad x_1/x_2
\quad\text{all not roots of unity of order prime to }p.
\]

The first two conditions exclude the finite cusp packets, and the third excludes the infinity packet. This is an elementary correction of the cusp exclusion, not a challenge to the separate lifting assertion Theorem A(i), which is not used here.

The claimed examples in Remark 2.5.1 therefore need n_1 distinct from n_2, in addition to both being nonzero, when (x_1,x_2)=(p^{n_1},p^{n_2}). D.52 already uses exactly such a nonperipheral slope.
