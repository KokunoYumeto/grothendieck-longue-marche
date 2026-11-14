# Independent D5 construction: an action with no normalized finite quotient

Status: complete proof independently reviewed and accepted by the root agent, 14 November 2026; directly insertable version in `sections/D_extension.tex`, claims D.10–D.11. This note belongs to the Part F agent's cross-review work. It does **not** settle the universal assertion that every abstract action has a unique fixed pro-point. It constructs an abstract action that has exactly one fixed pro-point and normalizes no deck group of any finite hyperbolic quotient.

## Statement

Let U = P1 over Qbar minus {0,1,infinity}, let Omega be the union of the function fields of its connected finite étale covers, and let the universal pro-cover be the corresponding inverse limit of affine curves. There exists a semilinear action rho of G_Q on that pro-cover such that:

1. the orbit of the base coordinate lambda in Omega is infinite;
2. rho normalizes no deck group of a finite hyperbolic quotient;
3. the fixed set of G_Q^circ on the completed pro-cover consists of precisely one geometric closed pro-point, the chosen cusp above lambda = 0.

All uses of a completed pro-point mean compatible systems of geometric closed points, as in D.7, and exclude the generic scheme point.

## 1. Modular realization and a finite-adele group of automorphisms

Choose an embedding Qbar into C. The classical modular function lambda identifies H/Gamma(2) with U(C). Put q = exp(pi i tau). Its expansion is

    lambda(q) = 16q - 128q^2 + 704q^3 + ... in Q[[q]].

The precise product formula, rationality, and uniformization are in the primary published source Calegari, Dimitrov, and Tang (2025), equation (1.0.2) and the following paragraph, p. 628. The proof below uses this classical setup, not the unbounded-denominators theorem proved in that paper.

Use the cusp tau = i infinity to embed Omega in the field of formal Puiseux series

    P = union_(n>=1) Qbar((q^(1/n))).

Equivalently, an element of Omega is realized as a meromorphic modular function on H for some finite-index subgroup of Gamma(2), meromorphic at the cusps, with its selected algebraic Puiseux germ at infinity. The analytic cover is the analytification of its algebraic finite étale cover. The field embedding is faithful, and the coordinate ring of the pro-cover consists of those functions holomorphic on H, with poles allowed only at cusps.

Write A_f for the additive finite adeles and Zhat for its standard compact open subgroup. The quotient A_f/Zhat is canonically Q/Z: every finite adele is r+z with r rational and z in Zhat, and Q intersect Zhat = Z. Choose the character

    psi : A_f -> Q/Z -> mu_infinity(C),  psi(r+z) = exp(2 pi i r).

For a in A_f define a formal automorphism T_a of P by

    T_a(sum_k c_k q^(k/n)) = sum_k c_k psi(k a/n) q^(k/n).

This is independent of the denominator used to write a Puiseux expansion; multiplication of the denominator by m replaces k by mk and leaves the factor unchanged. The maps satisfy T_a T_b = T_(a+b), fix Qbar, and preserve the q-valuation.

### Preservation of Omega and of the affine pro-cover

For z in Zhat, T_z fixes q and hence lambda(q). It is the usual cusp-inertia action on Puiseux roots, and preserves Omega because Omega is normal over Qbar(lambda), with allowed branch locus {0,1,infinity}. It also preserves the affine coordinate ring.

For r in Q, T_r is analytically the substitution tau -> tau + 2r. Its matrix has rational entries and commensurates Gamma(2). Explicitly, after clearing a denominator d, conjugation of Gamma(2d^2) lands in Gamma(2); applying the same observation to the inverse gives commensurability. Hence if f is invariant under a finite-index subgroup Gamma_f of Gamma(2), then f(tau+2r) is invariant under the finite-index subgroup

    Gamma(2) intersect u(2r)^(-1) Gamma_f u(2r).

The transformed function is meromorphic at every cusp. It is thus algebraic over C(lambda), and its associated covering is unramified over U(C). Its Puiseux coefficients are still algebraic, since T_r multiplies the original coefficients by roots of unity. To verify descent without presuming a chosen modular correspondence model, take a polynomial relation over C(lambda). After clearing its denominators, the finitely many possible monomials in lambda and T_r f satisfy a homogeneous linear system whose coefficients lie in Qbar, obtained by comparing Laurent coefficients. A nonzero solution over C implies a nonzero solution over Qbar: the rank is determined by finite minors. Thus T_r f is algebraic over Qbar(lambda). Its branch locus is still contained in {0,1,infinity}, so it belongs to Omega. If f has no poles on H, neither does f(tau+2r), and therefore this also preserves the affine coordinate ring. Apply the argument to -r for the inverse.

Every a is r+z, so T_a preserves Omega and the universal pro-cover. No unique-root assertion in the full automorphism group is needed.

The action extends to the completed pro-cover: the image of a finite-level function field lies in some further finite level, and the induced rational map of smooth proper compactifications extends uniquely everywhere by properness and normality for curves. These extensions commute with the transition maps and composition. The inverse operators make them automorphisms of the completed pro-object.

### Faithfulness and the stabilizer of lambda

From the first term 16q of lambda(q),

    T_a(lambda) = lambda  iff  psi(a) = 1  iff  a belongs to Zhat.

For a in Zhat, the functions lambda^(1/n) belong to Omega for every n, and their leading Puiseux terms show that an element acting trivially on all of Omega satisfies psi(a/n)=1 for every n. Thus a is in every n Zhat, hence a=0. Therefore a -> T_a is an injective group homomorphism

    A_f -> Aut_Qbar(universal pro-cover),

and the stabilizer of the single function lambda in A_f is precisely Zhat. All these automorphisms fix the selected completed cusp.

## 2. Exact cyclotomic Galois normalization

Let rho_0(g) act coefficientwise on P, fixing q^(1/n) for every n. Since lambda(q) has rational coefficients, this restricts to the continuous tangential semilinear action on Omega. One may regard it as the splitting supplied by Spec Q((q)) -> U, lambda -> lambda(q). A rational formal parameter is sufficient; q need not be an element of Omega.

For every a and g, coefficientwise evaluation gives

    rho_0(g) T_a rho_0(g)^(-1) = T_(chi(g) a).

Indeed g(psi(a/n)) = psi(chi(g) a/n), where chi(g) acts coordinatewise on A_f. This verifies Galois stability and its precise character directly on faithful germs, including the nonintegral rational translations.

## 3. A surjective Kummer quotient on G_Q^circ

Fix any odd prime ell, and enumerate distinct rational primes p_i different from ell. Choose coherent ell-power roots of the p_i and of unity. The Kummer cocycles give a continuous product cocycle

    kappa : G_Q -> V = product_(i>=1) Z_ell,
    kappa(gh) = kappa(g) + chi_ell(g) kappa(h).

Its restriction to G_Q^circ is a continuous surjective homomorphism. Here is a finite-level proof including the abelian-intersection issue.

For a finite set of indices and m>=1, let K=Q(mu_(ell^m)) and L=K(p_i^(1/ell^m)). The extension K/Q is unramified at each p_i, so the valuations at these primes make the classes of the p_i independent and of full order in K^*/K^(*ell^m). Kummer theory gives

    T = Gal(L/K) = (Z/ell^m)^r.

The extension L/Q is Galois. A lift sigma of a cyclotomic automorphism with character 2 modulo ell acts on T by that scalar. Consequently [sigma,T]=T, since chi(sigma)-1 is a unit. The quotient Gal(L/Q)/T is abelian, so T is exactly the commutator subgroup and L intersect Qab = K. Therefore G_Q^circ maps onto T. Surjectivity to V follows from all these finite-level surjections and compactness.

## 4. An unbounded linear functional with dense kernel

The coordinate vectors e_i are linearly independent in the Q_ell-vector space V tensor_(Z_ell) Q_ell. Extend them to a basis and choose a Q_ell-linear functional taking e_i to ell^(-i). Restriction supplies a Z_ell-linear function

    f : V -> Q_ell,  f(e_i)=ell^(-i).

The basis extension uses the axiom of choice. This is a specified abstract cocycle construction, not an effective algorithm to evaluate it on arbitrary Galois elements.

Its image contains ell^(-i) Z_ell for every i and hence is all Q_ell. Its kernel is dense in V: given finitely many prescribed coordinates, realize them by a finitely supported vector v. Choose j outside those coordinates so large that ell^j f(v) belongs to Z_ell, and replace v by

    v - ell^j f(v)e_j.

The result has the prescribed coordinates and is killed by f. This argument proves density for every extension of the stated values; no special basis choice or unjustified automatic continuity is used.

Embed Q_ell in A_f by its ell component and zero at the other primes, and put a_g = f(kappa(g)). Linearity gives

    a_(gh) = a_g + chi(g) a_h.

Define rho(g) = T_(a_g) rho_0(g). Section 2 and this identity give the action law. It is semilinear for the specified usual action on Qbar. On G_Q^circ its image under a is all Q_ell, while

    K_0 = ker(a|G_Q^circ)

is dense in G_Q^circ because kappa is a continuous surjective homomorphism of profinite groups and ker(f) is dense in its quotient. Continuous surjective homomorphisms of compact groups are open quotient maps.

## 5. The infinite orbit rules out every normalized finite hyperbolic quotient

The action rho_0 fixes lambda. Hence rho(g)(lambda)=T_(a_g)(lambda). Since a(G_Q^circ)=Q_ell and Stab_(A_f)(lambda)=Zhat, the orbit contains a copy of Q_ell/Z_ell and is infinite.

Suppose, to the contrary, that rho normalizes the deck group H of a finite hyperbolic quotient W. It descends to a semilinear action on W and on its function field F=Omega^H. Choose a finite number field K over which W and finitely many function-field generators are defined. For g in G_K, compare the descended action to the natural coefficient action associated to that K-model. The quotient is a geometric automorphism of W. The latter group is finite because W is hyperbolic. Thus the chosen generators have finite orbits under G_K, and then under G_Q since G_K has finite index. Constants have finite orbits as well, so every element of F has a finite orbit.

Every element of Omega is algebraic over F. Its polynomial equation has coefficients in F with finite orbits, so its G_Q orbit lies among the roots of finitely many polynomials and is finite. This contradicts the infinite orbit of lambda. The argument uses no continuity assumption and no unproved congruence-quotient comparison.

## 6. Determination of the fixed set

All T_a and rho_0(g) preserve the q-valuation and the selected cusp, so that cusp is fixed by the full action.

If a completed geometric closed pro-point P is fixed by rho(G_Q^circ), it is fixed by rho_0(K_0), because a vanishes on K_0. The stabilizer of P under the continuous action rho_0 is closed: use cofinal characteristic finite levels, each descending over Q under rho_0; the stabilizer of the algebraic closed point at any such level is open and closed, and intersect these stabilizers. Density of K_0 implies that P is fixed by rho_0(G_Q^circ).

For completeness, the unique fixed cusp for rho_0 follows from the same abelian-variety Kummer argument already proved in D.7 (or F.3). If another fixed pro-point existed, choose a characteristic cover separating it from the selected cusp and dominating the degree-nine Fermat cover x^3+y^3=1 of U. The compactification then has positive genus. It descends over Qab under rho_0, and the two projected Qab-rational points have the same section class of its proper fundamental group. Their Abel–Jacobi difference has zero Kummer class. Injectivity of the Kummer map for abelian varieties over finite extensions of Qab makes the difference zero. Distinct points on a positive-genus proper smooth curve cannot have principal difference, since that would give a degree-one map to P1. This contradiction proves uniqueness.

Thus the constructed action has exactly the original selected cusp as its G_Q^circ-fixed set.

## Scope

The action is not a refutation of the first, universal fixed-point assertion in D5: it satisfies that assertion. It answers the second demand by proving existence of actions outside all the finite-quotient normalization cases of R19. The proof does not assert that no logically different reduction of B-prime to B is possible. It does show that direct finite-quotient descent cannot cover all abstract actions.

## Opened primary references

- Calegari, F., Dimitrov, V., and Tang, Y. (2025). The unbounded denominators conjecture. *Journal of the American Mathematical Society, 38*, 627–702. https://doi.org/10.1090/jams/1053. Published offprint opened at https://www.math.uchicago.edu/~fcale/papers/UDC.pdf. Equation (1.0.2) and the following paragraph, p. 628, supply the lambda expansion and the finite-index modular-cover description. No use is made of their main unbounded-denominators theorem.
- SGA 1, XII, Theorem 5.1, in the supplied full source: the algebraic/analytic finite-cover comparison already opened in Part F. The algebraic-germ descent in Section 1 is written out independently.
- The abelian Kummer input is the exact Tsujimura 2020 Theorem 3.1 and its extension proved in F.3; alternatively use the explicit Ribet argument in D.7.

Additional background opened but not necessary as an independent theorem input: Milne, *Modular Functions and Modular Forms*, version 1.31 (2017), https://www.jmilne.org/math/CourseNotes/MF.pdf; Fresán, Bourbaki exposé 1197 (2022), pp. 2–3, https://www.bourbaki.fr/TEXTES/Exp1197-Fresan.pdf. The primary CDT source above has the correct product formula and is the preferred citation.
