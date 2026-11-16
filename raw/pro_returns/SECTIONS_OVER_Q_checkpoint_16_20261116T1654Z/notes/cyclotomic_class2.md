# C1: exact first lower-central stage for the cyclotomic pair

## Statement (proved)

Put F=Q(mu_infinity), U=P^1_F minus {0,1,infinity}, xi=zeta_6, and eta=xi^{-1}. Take full continuous point sections, modulo conjugation by the geometric profinite fundamental group Pi. Their images in the geometric abelianization coincide. Their images in the quotient by the closed third lower-central subgroup Gamma_3(Pi) are distinct. More precisely, a geometrically connected finite etale Galois cover of U, of degree 27 and with constant geometric deck group the exponent-three Heisenberg group, distinguishes them. Thus class two is the first stage in the lower-central filtration that distinguishes this pair. This is an indexed assertion about that filtration; it does not assert that the poset of all finite quotients has a least separating member.

No local section theorem is used.

## Arithmetic input, with its sharper conclusion retained

Let E be the Fermat cubic w^3+v^3=1, with origin (1:-1:0). In Weierstrass coordinates,

X=12/(w+v), Y=36(w-v)/(w+v), E: Y^2=X^3-432.

The inverse formulas are w=(36+Y)/(6X), v=(36-Y)/(6X). Let a=zeta_18, omega=a^6, lambda=1-omega, and P=(a,a^{-1}) on the Fermat model. The exact field is Q[a]/(a^6-a^3+1). The endomorphism omega sends (X,Y) to (omega X,Y).

We first prove E(F)[3^infinity] is killed by lambda^3. The Tate module T_3E is free of rank one over O=Z_3[omega]. Indeed, it is free of rank two over Z_3, the action of omega has minimal polynomial T^2+T+1, irreducible over Q_3, and O is the valuation ring of Q_3(omega): (omega-1) satisfies the Eisenstein polynomial T^2+3T+3. The O-module is torsion-free and finite, hence free, of rank one. The quotients T_3E/3^n identify equivariantly with E[3^n].

The curve has good reduction at 7 and #E(F_7)=9, hence arithmetic Frobenius has trace -1 and determinant 7 on T_3E. Since 7 splits in Q(omega), that Frobenius commutes with O and therefore acts by alpha=1+3omega or its conjugate; these are the two roots of T^2+T+7. Complex conjugation acts semilinearly on O, interchanging omega and omega^2. The commutator of a Frobenius lift with complex conjugation therefore acts by bar(alpha)/alpha, or its inverse. Every commutator fixes F because every cyclotomic extension of Q is abelian. Consequently each R in E(F)[3^infinity] is killed by alpha-bar(alpha). The scalar alpha is a 3-adic unit, its norm being 7. The exact identity

alpha-bar(alpha)=3+6omega=-(1-omega)^3=-lambda^3

proves lambda^3 R=0. This retains more information than the old degree-81 argument, which multiplied this relation by a further factor and retained only 9R=0.

The external standard statements used here were opened in Milne, Elliptic Curves, second edition, 2021, https://www.jmilne.org/math/Books/EC2.pdf : II Proposition 6.3 (prime-to-characteristic torsion has rank two), II Proposition 6.4 (Tate characteristic polynomial agrees with the endomorphism characteristic polynomial), II Proposition 6.7 (faithfulness of endomorphisms on the Tate module), V Proposition 8.1 (unramifiedness at good primes away from the Tate prime), and V Proposition 8.3 (Frobenius trace from the point count). The determinant may equivalently be obtained from the Weil pairing. These apply to the indicated characteristic-zero elliptic curve and prime 3, at its good prime 7.

## The nine differences

The program `code/cyclotomic_class2_check.py` calculates by the exact chord-and-tangent law and obtains

3P=(0,24a^3-12), lambda^2 P=(0,12-24a^3), lambda^3 P=O.

In particular 3P is nonzero of order three and is fixed by omega. The nine points above eta under phi:E->P^1, phi(w,v)=w^3, are

Q_ij=(omega^i a^{-1},omega^j a), 0<=i,j<3.

For every i,j it verifies

3(Q_ij-P)=3P, lambda^2(Q_ij-P) != O, lambda^3(Q_ij-P)=O.

There is also a short structural proof of the triples. The deck group of phi is mu_3^2, acting by independent scaling of w,v. Its subgroup fixing the origin is mu_3, and its translation subgroup is E[lambda]. The swap (w,v)->(v,w) is negation. Thus every Q_ij has form T-omega^r P with T in E[lambda]. On 3P the action of omega is trivial, and 3T=0, so

3(Q_ij-P)=-(omega^r+1)3P=-2(3P)=3P.

Since lambda^2=-3omega, this proves nonvanishing of lambda^2(Q_ij-P) from 3P!=O. The program records all nine cases independently.

## The degree-27 cover and its field of definition

Define M:E_F->E_F by M(R)=[lambda]R+P and f=phi o M. Its restriction

W=f^{-1}(U) -> U

is finite etale of degree 27. The map phi has degree nine and ramification only over {0,1,infinity}; the endomorphism lambda has degree three and is etale in characteristic zero, and translation by P is an F-isomorphism. The open W is nonempty in the geometrically integral curve E, so it is geometrically connected.

The degree-three claim for lambda can also be checked directly. Its kernel consists of the fixed points of (X,Y)->(omega X,Y): O and (0,+/-12sqrt(-3)). Since the characteristic is zero, its degree equals this kernel's order. The identity lambda^2=-3omega gives E[lambda^2]=E[3].

We now identify all its geometric deck transformations, including their fields of definition. For each b in E[3], translation t_b is a deck transformation: lambda b belongs to E[lambda], the translation subgroup of the deck group of phi. Define

h(R)=omega R-P.

Then M(h(R))=omega M(R), and phi(omega Q)=phi(Q), so h is a deck transformation. Also h^3=1. Conjugation satisfies

h t_b h^{-1}=t_{omega b}.

Thus these transformations form E[3] semidirect <h>, of order 9*3=27. As the degree is 27, they are the full geometric deck group, and f is Galois. All transformations are defined over F: P belongs to Q(zeta_18), omega belongs to Q(zeta_3), and all of E[3] is rational over Q(omega), as one sees from its nonzero points

(0,+/-12sqrt(-3)), (12omega^i,+/-36), i=0,1,2.

Hence W->U is a torsor under a constant group over F.

The commutators [h,t_b]=t_{(omega-1)b} form exactly the order-three group E[lambda]. This subgroup is central because omega fixes it. The action on E[3] is nontrivial, so the group has class exactly two. Every element has order dividing three: translation elements do, and

(t_b h)^3=t_{(1+omega+omega^2)b}=1.

It is therefore the exponent-three Heisenberg group of order 27. The program verifies its entire multiplication table, all 19,683 associativity identities, its exponent, and its center/commutator subgroup. Its action matrix on O/3 is [[0,-1],[1,-1]] modulo three.

## Separation of the point sections

The fibre over xi contains the F-point R=O. Suppose that the fibre over eta had an F-point R. Then lambda R=Q_ij-P for some i,j. Since the right-hand side is killed by lambda^3, R is killed by lambda^4, so it is 3-primary torsion. (One may instead use 9(Q_ij-P)=0 to obtain lambda^5R=0, which suffices.) The arithmetic input therefore gives lambda^3R=0. Applying lambda^2 to lambda R=Q_ij-P gives lambda^2(Q_ij-P)=0, contrary to the nine-difference calculation. Hence that fibre has no F-point.

For a finite etale cover, its fibre is the finite continuous G_F-set obtained by pulling back the monodromy action along the point section. Geometrically conjugate sections give isomorphic such G_F-sets. Our fibres have different fixed-point sets. The constant G-torsor here gives a continuous quotient of the arithmetic fundamental group to G, and its restriction Pi->G is surjective. Because Gamma_3(G)=1, this restriction kills Gamma_3(Pi). Thus the differing fibre actions already distinguish the sections modulo Gamma_3(Pi), with exactly the required geometric conjugacy ambiguity.

Finally the geometric abelianization of the tripod is Zhat(1)^2, with the two coordinates induced by the morphisms t and 1-t to G_m. The Kummer classes of xi, eta, 1-xi=eta, and 1-eta=xi all vanish over F, because every root of unity has roots of every order in F, compatibly. Therefore the two point sections have identical abelianized classes. Class two is the first lower-central stage separating them.

## Relation to the background

This calculation uses the same elliptic curve and Frobenius-7 commutator as CYCLOTOMIC_KERNEL D4, but retains the annihilator lambda^3 and replaces [3] by [lambda]. It strengthens the old degree-81 construction to an explicitly Galois degree-27 construction, and identifies the first lower-central stage. No priority is claimed. Source passage answered: cote149 scans 61-62, together with prompt C1.

# C1: descent proof of point injectivity over every finitely generated extension of F

Let K/F be finitely generated and U=P^1_K minus {0,1,infinity}. Let x,y in U(K), and suppose their full point sections are geometrically conjugate on the cyclotomic kernel. Because all roots of unity lie in K, this kernel is G_K itself.

Choose a finitely generated field k/Q inside K containing x,y and a finite collection of generators and coefficients presenting K/F, so that K=k(mu_infinity). This is possible by placing all finitely many coefficients from F in one finite cyclotomic subfield before taking k. In particular K/k is algebraic. Take a common algebraic closure; then G_K is exactly the closed normal subgroup H_k=ker(chi_k) of G_k. Characteristic-zero geometric base change identifies the geometric fundamental groups, and the arithmetic group over K is the pullback E_{U/k} times_{G_k} H_k. These are the exact comparison maps.

Choose representatives s_x,s_y over k, and gamma in Pi satisfying s_y(h)=gamma s_x(h) gamma^{-1} for every h in H_k. The conjugator is unique. Indeed LM6-F.7 / CYCLOTOMIC_KERNEL D0b (R15) proves that the point section s_x restricted to H_k fixes one and only one completed geometric pro-point. Any element of Pi centralizing s_x(H_k) preserves that unique point, which lies over the interior point x. The action of Pi on that interior fibre is free, so that element is 1. This checks exactly the point-case centralizer consequence of R15 being used; no assertion over a field outside R15's finitely generated-over-Q hypothesis is inserted.

For sigma in G_k define gamma_sigma=s_y(sigma) gamma s_x(sigma)^{-1}. This lies in Pi, because its arithmetic projection is sigma*1*sigma^{-1}=1. Normality of H_k gives, for h in H_k,

gamma_sigma s_x(h) gamma_sigma^{-1}=s_y(sigma) s_y(sigma^{-1}h sigma) s_y(sigma)^{-1}=s_y(h).

Uniqueness forces gamma_sigma=gamma. Thus s_y(sigma)=gamma s_x(sigma) gamma^{-1} for every sigma in G_k: the conjugacy descends to the full group over k.

Now the morphism t:U_k->G_{m,k} sends this equality to equality of the Kummer classes kappa_k(x)=kappa_k(y), so x/y is an nth power in k for every positive integer n. The Kummer map k^*->lim_n k^*/k^{*n} is injective for k finitely generated over Q. Here is the required elementary arithmetic proof. Let k_0 be the relative algebraic closure of Q in k; it is a number field. On a normal proper model of k/k_0 every prime-divisor valuation of an infinitely divisible element is divisible by every n and hence zero. The element and its inverse are everywhere regular, so the element lies in k_0^*. Every root of it in k is algebraic over k_0 and therefore also lies in k_0. Its valuations at the finite primes of k_0 vanish, so it lies in the finitely generated unit group O_{k_0}^*. A finitely generated abelian group has zero intersection of all n-multiples (choose n divisible by its torsion exponent and then arbitrarily high multiples on its free part). Hence the element is 1. Therefore x=y.

This proves the tripod assertion for all K/F finitely generated, with R15 used only over the actual field k/Q. The same conjugator descent works for any hyperbolic curve defined over K after descending its equation and the two points to k; the final point-injectivity over k then follows from the usual generalized-Jacobian/Kummer proof or its positive-genus finite-cover version. For the requested tripod no additional curve theorem is needed.
