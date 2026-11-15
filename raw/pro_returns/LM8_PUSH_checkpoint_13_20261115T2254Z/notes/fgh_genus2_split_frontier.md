# The residual genus-two target: exact models and failed component argument

Status: working mathematics after the A54 integration; no additional numbered theorem. The target is

\[
 G:v^2=w^5-1,\qquad G^\circ=G\setminus\{(0,i),(0,-i),\infty\},
\]

defined over the original field Q(i). It is the actual three-cusp quotient in A54 after finite scaling. Its map to the tripod is degree5. This is not an open pro-ell embedding for ell other than5.

## Exact good model at two

Adjoin beta with beta^5=−4. The literal substitutions

\[
 v=i(1+2Y),\qquad w=\beta X
\]

give

\[
 Y^2+Y=X^5.
\]

This has smooth proper genus-two reduction in characteristic2: it is an Artin–Schreier cover of the X-line with its single pole of order5. The three original cusps specialize to (X,Y)=(0,0),(0,1), and infinity, respectively. They remain distinct. The order5 automorphism rotates X and has precisely those three fixed points; the hyperelliptic involution becomes Y→Y+1. Thus the pointed curve is potentially good at2. There is no nonzero semistable monodromy derivation here after the finite extension.

## Exact good model at five

Put pi=zeta5−1, adjoin sqrt(pi), and make the literal substitutions

\[
 w=1+\pi X,\qquad v=\pi^{5/2}Y.
\]

Then

\[
 Y^2=X^5+\frac5\pi X^4+\frac{10}{\pi^2}X^3+
       \frac{10}{\pi^3}X^2+\frac5{\pi^4}X.
\]

The pi-valuations of the nonleading coefficients are respectively3,2,1,0. The cyclotomic equation

\[
 5+10\pi+10\pi^2+5\pi^3+\pi^4=0
\]

gives 5/pi^4≡−1. Hence the special curve is

\[
 Y^2=X^5-X,
\]

which is smooth of genus2; the derivative in X is−1. The order5 automorphism becomes X→X+1, with Y unchanged. Its unique fixed point is infinity. In its Artin–Schreier presentation X^5−X=Y^2, the jump is2, and the wild genus bound is exactly (5−1)(2−1)/2=2. The actual genus attains this bound, so the order argument from A48 cannot rule it out.

Both finite cusps have X=−1/pi and Y=±i/pi^(5/2), so they, and the original infinity cusp, reduce to infinity. A regular parameter there is u=X^2/Y. On the three marked sections its values are −i sqrt(pi), +i sqrt(pi), and0. Their common-radius blowup therefore separates them on a rational component, with three distinct finite marks after scaling by sqrt(pi), and the attaching point at infinity. There is one positive-genus component, the smooth genus-two component above.

The local separating-edge derivation, based on that rational marked component, acts on every proper handle v by m[Omega,v] and fixes the boundary letters, where m>0. An arbitrary selected tangent packet adds an inner term lambda ad(t). Therefore its degree-two value on any proper leading vector is

\[
 [m\Omega+\lambda t,v]\in[v,L_2].
\]

The necessary normalizer equation from A25/A47 has no obstruction at this degree. This is a precise failure of this test, not a construction of a normalized procyclic subgroup.

At every residue prime other than2 and5 the displayed curve and its three marks have good reduction. Thus the available non-coefficient local monodromy gives no additional proper component splitting. The four distinct CM characters over Q(zeta5), conjugated by G_Q(i), all occur on the same genus-two component. Their distinctness does not itself contradict the existence of a normalized line.

## A notes-only fixed-subgroup observation

This observation does not solve the requested split normalizers and has not been registered. Let Delta be the closed commutator kernel for Q(i), and choose a finite normal field L/Q(i) over which the curve, cusps, all CM endomorphisms and a given packet are defined. Put Gamma=G_L intersect Delta, with Gamma contained in the given open Delta subgroup. The proof of the general A38 criterion uses only that Gamma is normal, G_L/Gamma is abelian, and chi(Gamma)=1, so it applies with this Gamma if its Tate-graded hypothesis is verified.

The weight-graded geometric Lie algebra is free on four proper characters psi1,...,psi4 of weight1 and two boundary characters chi of weight2. Polarization gives psi1 psi4=psi2 psi3=chi. Any character in weight d is a monomial eta=psi1^n1 ... psi4^n4 chi^r with n_j,r nonnegative and d=sum n_j+2r.

If eta is trivial on Gamma, it factors through G_L/Gamma and is invariant under conjugation by G_Q(i): for g in G_Q(i), h in G_L, ghg^(−1)h^(−1) lies in Gamma. Since Q(zeta5) intersects Q(i) trivially, the four translates of the primitive CM type {1,2} all occur. Labelled Hodge–Tate comparison forces

\[
 n_1+n_2=n_2+n_4=n_3+n_1=n_4+n_3.
\]

Thus n1=n4 and n2=n3, and the actual character is eta=chi^(n1+n2+r)=chi^(d/2), using the exact polarization identities rather than only its Hodge weights. The proper-plus-boundary graded representation is a direct sum of such characters after scalar extension, so its Gamma-fixed part is pure Tate in every even weight and zero in odd weights. The same holds for the graded closure of the actual fixed subgroup. The proof of A38 would then give full selected inertia at every coefficient prime and packet.

This target is not a cover of the original once-punctured elliptic curve: its simple quartic-CM Jacobian admits no nonconstant map to that elliptic curve. The observation is retained only as an auxiliary comparison; it does not transfer fixed groups backwards through the quotient from the genus51 source and does not exclude an arithmetically normalized line carrying a non-Tate CM character.
