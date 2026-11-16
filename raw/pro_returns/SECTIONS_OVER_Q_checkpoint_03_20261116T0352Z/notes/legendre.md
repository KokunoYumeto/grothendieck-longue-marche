# Legendre route audit and proved steps

AI-produced by GPT-6 Astra (OpenAI), for the SECTIONS_OVER_Q project. No priority claim.

## Sources opened

1. Attached AP `sections/D_legendre_modularity_extension.tex`, claim D.30, read in full. Its absolute-irreducibility argument and rational-system realization are as described below. Its explicit limitation on finite ramification is essential.
2. Attached AP `sections/D_finite_cusp_extension.tex`, D.31, read in full.
3. Attached AP `sections/D_modular_unit_obstruction.tex`, D.32, statement and construction read; no claim here to have independently rechecked its entire cusp-orbit computation.
4. Attached AP `sections/D_canonical_lifting_extension.tex`, D.27, read in full, and `D_neighbourhood_residue_extension.tex`, D.28, read in full.
5. Attached LM6 paper, B.14/B.15, D.4, E.7 read; B.14 supplies the finite-support transfer, and E.7's cyclic-4 construction has been checked below.
6. Attached Stoll source `literature/stoll_finite_descent/src_arXiv_math_0606465/main.tex`, proof of Proposition 8.5, Theorem 8.6 and Corollary 8.8 (labels Dom, CorMor, ModCurves), opened. Also author PDF https://www.mathe2.uni-bayreuth.de/stoll/papers/covers-revised.pdf retrieved in web search. Corollary 8.8 applies to positive genus X_0(N), X_1(N), X(N), including genus one. The real-component erratum must be retained in the parent paper.
7. Pan, *The Fontaine--Mazur conjecture in the residually reducible case*, arXiv:1901.07166v2, 3 September 2021, https://arxiv.org/pdf/1901.07166, opened. Conjecture 1.0.1 explicitly assumes a continuous irreducible representation, ramification at finitely many places, potential semistability at the coefficient prime, and oddness. Theorem 1.0.4 adds distinct Hodge--Tate weights, with the exceptional residual condition only for p=3, and proves eigenform origin up to twist. Thus the use for coefficient prime >=5 in AP-D.30 checks out at this step; Pan supplies no finite-ramification theorem.
8. Mazur, *Rational isogenies of prime degree*, Invent. Math. 44 (1978), 129--162, author PDF https://www.math.columbia.edu/~goldfeld/Mazur-Goldfeld1978.pdf opened. Theorem 1 supplies the prime-degree list. Page 131 discusses composite degrees and isolates the unresolved-at-that-time values 169, 91, 65, 39, 125; none is divisible by 4. The completed classification is in Kenku 1982. Kenku primary PDF https://core.ac.uk/download/pdf/82233672.pdf was located but tool fetch returned 403, so that PDF is not marked opened. Publisher abstract https://www.sciencedirect.com/science/article/pii/0022314X82900257 opened through search; not a substitute for full theorem text.

Web search before any novelty claim: “Lue Pan 2022 Theorem 1.0.4 Fontaine Mazur conjecture residually reducible representations”; “Mazur Kenku rational cyclic isogenies full 2 torsion X0(4p) rational points”; “Mazur Kenku rational cyclic isogeny degree 20 28 4p theorem all degrees 1 19 21 25 27 37”; “Stoll finite descent modular curves X0(N) Corollary 8.8”; “Mazur Rational isogenies prime degree 1978 pdf theorem rational cyclic isogenies 20 4N”; “Kenku On the number of Q-isomorphism classes of elliptic curves in each Q-isogeny class 1982 pdf”; “compatible system infinitely ramified representations rational traces elliptic curve local every prime section conjecture finite ramification Legendre”; “Stix Legendre family sections modularity infinitely ramified representations integral points density one”. No novelty claimed for the consequences below.

## A3/L5: residual irreducibility for primes >=5

**Status:** the complete reduction is proved for noncuspidal Selmer sections, using Stoll and the rational-isogeny exclusion. For arbitrary sections, passing to Selmer sections uses the supplied local theorem and must be marked in the parent register. The exact composite-isogeny source opening is the remaining bibliographic task, not a new mathematical conjecture.

Let s:G_Q -> pi_1(U) be a continuous noncuspidal Selmer section. For an odd prime l, the finite étale U-scheme Z_l = P(E[l]) parametrizes cyclic subgroups of order l, hence is a finite étale cover of degree l+1. The representation bar rho_{s,l}:G_Q -> GL_2(F_l) has an invariant line exactly when the finite G_Q-set s^*Z_l has a fixed point. Under the Galois-category equivalence, choosing that point gives a lift of the actual section to the corresponding open subgroup pi_1(Z_l) of pi_1(U). The geometric monodromy contains SL_2(F_l), which acts transitively on P^1(F_l); therefore this cover is geometrically connected. Choices of geometric base point change the lift by geometric conjugacy.

For each geometric elliptic fibre, use the universally labeled points P=(0,0), Q=(1,0). Put phi:E -> E'=E/<P> and let phi':E' -> E be the dual 2-isogeny. The subgroup H_4=(phi')^{-1}(<Q>) has order four. For phi'(R)=Q, one has 2R=phi(Q) !=0, so H_4 is cyclic. It is a finite flat subgroup scheme defined over the base. The image phi(C_l) has order l and is defined over the base of Z_l. Since (4,l)=1, H_4+phi(C_l) is cyclic of order 4l. This constructs the Q-morphism Z_l -> Y_0(4l). Its j-invariant is nonconstant: an isogeny class of fixed degree two contains finitely many j-invariants, while j(E_t) is nonconstant. Thus the morphism extends to a finite nonconstant map of smooth projective completions.

At every finite place, the lifted section remains point-or-cuspidal. For an ordinary point, this follows because the Galois-fixed sheet is a rational point of the finite étale fibre. At a cusp, the lifted image stabilizes a cusp above it, and surjectivity to G_{Q_p} makes that cusp Q_p-rational. Consequently the compactified lifted section gives a finite-descent adelic point; applying any finite torsor and taking its section-selected arithmetic twist proves this directly. Its image on X_0(4l) survives finite abelian descent. The index and cusp counts give g(X_0(4l))=(l-3)/2>0 for l>=5. Stoll Corollary 8.8 therefore puts this image in X_0(4l)(Q), with its finite-place coordinates equal to that rational point. The rational-isogeny classification excludes a noncuspidal rational point for degree 4l>=20. Its preimage under the finite map is a finite subscheme contained in the boundary of Z_l. The finite-support theorem applied to the lifted section makes it cuspidal, hence s cuspidal, contradiction.

Thus bar rho_{s,l} is irreducible for every l>=5. It is also absolutely irreducible. A two-dimensional F_l-irreducible representation which becomes reducible over Fbar_l is the sum of two Frobenius-conjugate characters. Complex conjugation has eigenvalues in {1,-1}, both fixed by F_l-Frobenius, so these two characters have equal value at complex conjugation and determinant +1. Here det rho(c)=chi_l(c)=-1, excluding this case.

Khare--Wintenberger then supplies a modular residual representation, but one must open and cite its precise theorem before marking that additional statement Known. The current proof establishes no bound on the union of prime-to-l ramification supports.

## A3: the small coefficient primes

**Proved counterexample at l=3.** Take the actual rational point lambda=32/27 of U. The 3-division polynomial for y^2=x(x-1)(x-lambda) is

    psi_3(x)=3x^4-4(1+lambda)x^3+6lambda x^2-lambda^2.

At x=4/3 it vanishes. The curve value is y^2=16/243, so the two nonzero points in the cyclic subgroup have rational x-coordinate and opposite y-coordinates in Q(sqrt 3). That order-three subgroup is G_Q-stable. Thus bar rho_{s_lambda,3} is reducible, although s_lambda is an ordinary rational point section. Exact factorization is in code/legendre_checks_output.txt.

**Proved at l=2.** The universal sections O, (0,0), (1,0), (t,0) trivialize E[2] over U, giving an isomorphism of finite étale group schemes E[2] ~= (Z/2)^2_U. Pullback along any arithmetic section gives the trivial two-dimensional F_2 representation. The comparison morphism is the reduction map GL_2(Z_2) -> GL_2(F_2), applied to rho_{s,2}. This calculation says nothing against the absolute irreducibility of rho_{s,2} tensor Q_2: AP-D.30's character-and-Hasse argument addresses that rational representation separately.

## A7/L16: explicit local ordinary counterexample

**False:** an integral local p-adic Tate module, even with Weil pairing, determines the Legendre parameter at a good ordinary prime.

Take p=17 and the curves E_4 and E_9 over Q_17. Their discriminants are 16 lambda^2(1-lambda)^2, units at 17. Counting their reductions gives #E_4(F_17)=#E_9(F_17)=16 and Frobenius trace 2. They have good ordinary reduction because 17 does not divide the trace.

Define over Q the degree-two isogeny E_4 -> E' by

    X=x-5+4/x,    Y=y(1-4/x^2),
    E': Y^2=X(X+1)(X+9).

The identity Y^2=X(X+1)(X+9) follows by direct substitution (checked symbolically). This rational map extends to the smooth projective elliptic curves; its kernel is {O,(0,0)}, and the equation for x over X is quadratic, proving degree two. Hensel's lemma applied to 4 mod17 gives i in Q_17 with i^2=-1. The map E' -> E_9 is z=-X, w=Y/i. Their composition phi is a Q_17-isogeny of degree two.

The continuous G_{Q_17}-equivariant map T_17(phi):T_17(E_4)->T_17(E_9) is an isomorphism: its dual composite is [2], and 2 is a unit in Z_17. For the Weil pairings,

    <T_17(phi)v,T_17(phi)w> = 2 <v,w>

in additive Tate-module notation. Hensel's lemma applied to 6 mod17 gives h in Z_17^x with h^2=2. Therefore h^{-1}T_17(phi) is a continuous symplectic G_{Q_17}-equivariant isomorphism. However

    j(E_4)=35152/9,    j(E_9)=1556068/81,

which are unequal. Consequently the elliptic curves are not geometrically isomorphic and the parameters 4 and 9 are unequal. All numerical and polynomial checks appear in code/legendre_checks.py and its output.

The replacement actually proved here is that prime-to-p isogenies induce integral p-adic Tate-module isomorphisms; the multiplier is the isogeny degree, and a square degree unit permits a symplectic rescaling. This explicit map proves exactly the failure claimed. No conclusion about equality of complete global section classes follows from this local example.

## A8/L17 and correction to R9

The modular unit identity is exactly

    u(t)=1-1728/j(t)
        = ((t-2)^2(t+1)^2(2t-1)^2)/(4(t^2-t+1)^3).

Its zero divisor is 2[-1]+2[1/2]+2[2], its pole divisor is three times the degree-two divisor t^2-t+1=0, and u(0)=u(1)=u(infinity)=1. Thus u is a nonconstant unit on U' obtained by deleting these five geometric points. The two equianharmonic points form a single degree-two closed point over Q, rather than two rational punctures; its reciprocity coefficient torus is Res_{Q(sqrt(-3))/Q}G_m, with restriction/corestriction maps required.

Let a lifted noncuspidal Selmer section on U' have ordinary integral local points outside a finite set, and let every local cuspidal centre belong to the original three cusps (equivalently, its projection to U has no local point at a deleted harmonic or equianharmonic point which becomes a new cusp). Then the local Kummer value of u is an actual nonzero local number at every place, and is a unit at almost every finite place. At an old cusp it is 1 independently of its tangent class. The completed-rationality lemma makes the global Kummer class a rational number, and finite support in u^{-1}(a) yields a rational point section. This is AP-D.31's argument with exactly the necessary boundary conditions.

More generally, the u-criterion requires u to be regular and nonzero at EVERY occurring cuspidal centre of the lifted section. The unit u has zeros/poles at the five newly deleted points, so a lift can have new local cusps there. The words “whatever the cusp labels” are valid for the OLD three labels only; they require additional treatment for the new labels. For a globally noncuspidal s, local special values at some primes are not excluded by its noncuspidality.

Two separate missing steps in L17: (i) cofinite integrality on U does not establish cofinite integrality on U' (contact with new punctures is not tested by t and 1-t), and (ii) the new cusp labels can obstruct the actual-local-number hypothesis for u. These are gaps in that proposed derivation, not counterexamples to the section conjecture.

R9, as summarized in the prompt, overstates the opened AP source. AP-D.27 proves a necessary and sufficient condition for the prescribed local classes to come from one global COMPLETED KUMMER CLASS / canonical CENTRAL lift. It requires BOTH unramified local classes at almost every place at each finite modulus and orthogonality to all dual characters. It explicitly says in its final sentence that the NONABELIAN lifting problem is unresolved. The comparison is the quotient from the geometric kernel of pi_1(U') -> pi_1(U) to the cuspidally central Tate module; the reciprocity theorem addresses the image in this quotient. It does not produce a section of the full group pi_1(U'). Thus the phrase in R9 “a lift over a new puncture exists under reciprocity tests” needs its word “central”, its restricted-product hypothesis, and prescribed local tangent data restored.

## A7/L15: removing the integral-lattice and quadratic-twist ambiguities

**Proved statement for the specified finite-ramification class.** A noncuspidal Selmer section of U/Q satisfying the finite-ramification condition of AP-D.30 has an elliptic realization as an ACTUAL Legendre curve E_{lambda_0}/Q at the level of the full integral Tate system, with the universally specified ordered level-two structure. This uses the rational realization in AP-D.30 and the residual irreducibility proved above. It does not yet place the conjugator inside the closure of the geometric Legendre monodromy.

Write L_l=s^*T_l(E). AP-D.30 gives E/Q and rational G_Q-isomorphisms V_l(E) ~= L_l tensor Q_l at every l. For l>=5, L_l/l is irreducible. Two G_Q-stable Z_l-lattices in that rational representation are homothetic: rescale one into the other so its reduction is nonzero; the reduction is all by irreducibility, and Nakayama gives equality. Thus choose integral comparisons for all l>=5. At l=2,3, rescale the rational comparison so the transported L_l contains T_l(E). The finite quotient L_l/T_l(E), viewed inside V_l(E)/T_l(E) ~= E[l^infinity], is a G_Q-stable finite subgroup. Let H be the product of these two subgroups and put E'=E/H. Under the rational Tate-module identification induced by E -> E', the lattices of E' are precisely the prescribed lattices at 2 and 3 and the original lattices elsewhere. Consequently

    product_l L_l ~= product_l T_l(E')

as continuous Zhat[G_Q]-modules. The isomorphism at l=2 identifies the universal ordered 2-torsion points with an ordered pair P1,P2 in E'[2](Q). Put E' into a monic rational Weierstrass form

    y^2=(x-e1)(x-e2)(x-e3),

with Pi=(ei,0), i=1,2, and all e_i rational and distinct.

Here is the mod-four computation that detects the twist, including the actual comparison map. Choose

    a^2=e1-e2,  b^2=e1-e3,  c^2=e2-e3,  i^2=-1,

and let R1 and R2 be halves of P1 and P2 with coordinates

    R1=(e1+ab,-ab(a+b)),
    R2=(e2+iac,-iac(ia+c)).

They form a basis of E'[4]. For sigma in G_Q let A,B,C,I in F_2 be its sign characters on a,b,c,i. The translation formula on the elliptic curve gives

    sigma R1 - R1 = A P1 + (A+B) P2,
    sigma R2 - R2 = (I+A+C) P1 + (I+A) P2.

Therefore its E'[4]-matrix is

    [[1+2A, 2(I+A+C)], [2(A+B), 1+2(I+A)]] modulo 4.

For example, changing a to -a changes R1 by P1+P2, while changing b to -b changes R1 by P2; this follows by the chord formula with (e2,0). The same formula with base point P2 proves the second column. Its (2,2) entry is 1+2 kappa_2(e2-e1)(sigma), since I+A is the sign on ia=sqrt(e2-e1).

This matrix is independent of the choices of halves: a new basis lifting the same P1,P2 differs by I+2M, and all G_Q matrices are themselves I+2N, so the conjugation is trivial modulo 4. The continuous reduction map T_2(E') -> E'[4] thus recovers the squareclass of e2-e1 from the labeled integral G_Q-module.

For the Legendre family, e1=0,e2=1,e3=t. We have A=I, B=I+kappa_2(t), C=kappa_2(1-t), so the universal mod-four matrix is

    [[chi_4, 2 kappa_2(1-t)], [2 kappa_2(t), 1]].

In particular its lower-right entry is identically 1 as a character of pi_1(U). Pullback along s and the integral isomorphism above make kappa_2(e2-e1)=0. Thus e2-e1=d^2 for d in Q^x. The explicit Q-isomorphism

    x=e1+d^2 X,    y=d^3 Y

identifies E' with E_{lambda_0}, where lambda_0=(e3-e1)/(e2-e1) in Q minus {0,1}. It respects P1=(0,0), P2=(1,0). This fixes the quadratic twist by a verified mod-four invariant rather than omitting it.

**Exact remaining issue in L15/A7.** The geometric closure is H=product_(l odd) SL_2(Z_l) times the subgroup of SL_2(Z_2) with even off-diagonal entries and diagonal entries 1 mod4. Powers of U(2),L(-2) with exponents in Zhat isolate each coefficient prime. At 2, Gauss decomposition and the identity diag(a,a^-1)=U(2)L((a-1)/2)U(-2/a)L(-a(a-1)/2), for a=1 mod4, prove the displayed closure exactly. Absolute irreducibility makes the multiplier class det(g) in Zhat^x/(Zhat^x)^2 independent of the chosen labeled integral conjugator g. An H-conjugator exists exactly when that class is trivial: rescale g to determinant1 and, if necessary, multiply its 2-component by -I to put both diagonal entries into1 mod4. Thus the extra 2-adic sign is removable, not an independent obstruction. The multiplier squareclass itself has not been shown trivial, and equality of full section classes from the congruence image remains unproved.

## A4/L4: the exact prime-residual loss at cusp parameters

The reduction maps Zhat -> F_l, for l prime, have simultaneous kernel product_l l Z_l. Consequently prime-residual data can lose nonzero integral-adic information even when all coefficient primes are considered. This is an explicit calculation of the comparison morphism, rather than an unsupported claim about distinct theories.

Enumerate rational primes p_j. Let b=(l)_l in product_l Z_l=Zhat and a_{p_j}=j! b. For each n, all but finitely many a_{p_j} vanish modulo n. The valuation coordinates therefore define A in Qhat^x=lim_n Q^x/(Q^x)^n, with positive sign. At each prime l, all coordinates vanish modulo l, so kappa_l(A)=0 globally. For every fixed l and every p_j, the l-adic valuation coordinate is j! l, which is nonzero in Z_l. Thus the l-adic Kummer class has infinitely many ramified localizations.

Choose the tangent-one splitting of the cusp-zero decomposition extension and twist by kappa(A). This gives an actual continuous globally cuspidal section. At t=0 the Legendre Tate parameter has leading term q=t^2/256; after its fixed quadratic split-multiplicative twist, the extension class changes by 2 kappa_l(A). For p_j different from 2 and l, residual inertia modulo l is trivial; its reference tangent class 1/256 and the quadratic character are unramified there. Hence all the prime-residual supports, omitting the coefficient primes, lie in {2}. Nevertheless, at every p_j different from 2 and l, the l-adic tame inertia exponent is 2 j! l !=0. Every l-adic representation of this cuspidal section is infinitely ramified.

This does not refute A4's statement for NONCUSPIDAL sections. It proves that the reduction to prime-residual support cannot be used without an additional argument controlling the local cusp parameters of the noncuspidal section. For ordinary local points, a nonzero contact order m is an honest integer and the local tame unipotent survives modulo every l>2|m|. A locally cuspidal parameter is a general element of Zhat, so that argument does not automatically apply.

### The L4 equivalence is nevertheless proved for noncuspidal Selmer sections

The following equivalence repairs L4 by a global modularity argument. It does not assert that every section satisfies the equivalent properties. Let s be a noncuspidal Selmer section of U/Q. The following properties define the same class of such sections:

1. One finite set S contains the prime-to-l ramification support of bar-rho_(s,l) for every prime l>=5.
2. At least one rho_(s,l), l>=5, is finitely ramified.
3. The local sections are ordinary point sections with x_p in U(Z_p) at all but finitely many p.
4. A single finite set contains the prime-to-l ramification support of every rational rho_(s,l).

Properties 2, 3, 4 are the equivalence proved in AP-D.30, with Pan's finite-ramification hypothesis checked above. Property 4 implies 1 by the continuous reduction map GL_2(Z_l)->GL_2(F_l). We now prove 1 implies 4; this implication avoids assuming that a profinite cusp contact is detected modulo all large primes.

Put 2 and 3 into S. By AP-D.25 there is a density-one set D of primes p for which s_p is the section of x_p in U(Z_p). Let a_p=p+1-#E_(x_p)(F_p), for p in D other than 2. This integer is the trace of every rho_(s,r)(Frob_p), r different from p. For each coefficient prime l in D minus S, bar-rho_(s,l) is the l-torsion of the good-reduction elliptic curve E_(x_l)/Q_l, so it is finite flat at l and has Serre weight two. L5 proves its absolute irreducibility, and the Weil pairing gives its odd cyclotomic determinant.

Choose primes l in D satisfying

    l = 5 mod72,   l = 2 mod p for every p in S, p>=5.

The Chinese remainder theorem defines a residue class prime to its modulus. Dirichlet's theorem makes its prime set positive density. Its intersection with D is therefore infinite. The order of GL_2(F_l) is l(l-1)^2(l+1). Under these congruences its 2-primary part has order at most 2^5, its 3-primary part has order 3, and none of the primes p>=5 in S divide it. Thus the wild inertia image at each p in S has those respective bounds. The local Artin-conductor estimate used by Helm--Voloch, Proposition 6, pp. 6--7 (Serre's Proposition 9 and corollary), gives

    v_2(N_l)<=14,   v_3(N_l)<=5,   v_p(N_l)<=2 (p>=5),
    N_l | N := 2^14 * 3^5 * product_(p in S,p>=5) p^2.

This part of Helm--Voloch's proof concerns the finite residual representations only: it uses their ramification support and the order of the wild inertia image, not finite ramification of the original l-adic representations. Their displayed constants therefore apply here.

Serre modularity, in the precise optimal-weight and optimal-level form stated in Helm--Voloch Theorem 5, now attaches a weight-two eigenform f_l of level dividing N to each selected residual representation. There are finitely many normalized newforms of weight two and level dividing N, allowing nebentypes. One form f, with coefficient field K, occurs for infinitely many distinct residue characteristics l, with primes lambda_l of K. Fix p in D outside S. For all these l other than p, the trace comparison is

    a_p(f) = a_p modulo lambda_l.

The difference a_p(f)-a_p is an algebraic integer. A nonzero algebraic integer has norm a nonzero rational integer, which can have only finitely many rational prime divisors. Hence a_p(f)=a_p. Comparing determinants in the same way gives epsilon_f(p)=1 for these p; Chebotarev applied to its finite-order nebentype gives epsilon_f=1.

For every embedding tau of K, the compatible representations of f and f^tau have identical traces at all p in D outside their finite ramification sets, since a_p is rational. This density-one set of Frobenius conjugacy classes is dense in every finite quotient of G_Q. To see the exact inference, take any finite quotient and any conjugacy class in it. Its unramified Frobenius set has positive density by Chebotarev, so removing the density-zero complement of D leaves a nonempty set. Continuity therefore gives identical characteristic-zero characters. Semisimplicity and Brauer--Nesbitt give isomorphic representations, then equality of all good-prime eigenvalues. Newform multiplicity one gives f^tau=f. Consequently K=Q and every Fourier coefficient of f is an integer.

Eichler--Shimura supplies an elliptic curve E/Q attached to f. Fix ANY coefficient prime r. The traces of V_r(E) and rho_(s,r) agree at every p in D outside the finite bad set of E and p=r. The preceding density argument remains valid even before rho_(s,r) is known to be finitely ramified: each continuous finite quotient of its image is ramified at finitely many primes, and Chebotarev is applied to that finite quotient. Thus the continuous characters agree on G_Q. Brauer--Nesbitt identifies the semisimplification of rho_(s,r) with V_r(E). The latter is absolutely irreducible, so rho_(s,r) itself is irreducible and isomorphic to it. Alternatively AP-D.30's independent absolute-irreducibility proof can be used here. It follows that every rho_(s,r) is unramified outside the bad primes of E and r, proving property 4.

This gives a substantive positive answer to the equivalence asserted in L4/L5. What remains in A4 is to prove that the union of the residual ramification supports is finite; neither this argument nor L5 bounds that union for an arbitrary noncuspidal Selmer section. The preceding globally cuspidal example still disproves the unrestricted version and explains why the direct contact-order argument cannot substitute for the modularity proof.

Primary source opened in full: D. Helm and J. F. Voloch, *Finite descent obstruction on curves and modularity*, Bull. London Math. Soc. 43 (2011), 805--810, doi:10.1112/blms/bdr015, author preprint https://web.ma.utexas.edu/users/voloch/Preprints/modularity.pdf . Theorem 5, Proposition 6 and its local-conductor calculation are on pp. 6--7 of that preprint. The extension here replaces their cofinite set of good local elliptic curves by a density-one set plus the uniform residual-support property.

## Correction to the raw-representation clause of R4/L6

LM6-E.8, as actually written, retains a quadratic twist before asserting semisimplification 1+chi and ramification supported on 2l. The prompt's abbreviated R4 omits that twist. The omission is detected by a cuspidal section of the genuine Fermat cover, without invoking any nonpoint section.

Take the Fermat curve X^5+Y^5+Z^5=0 with the complement of XYZ=0 removed. Its rational cusp [1:-1:0] has local parameter u=Z/X, and the map to the tripod is

    t=-(X/Z)^5=-u^(-5),    1-t=-(Y/Z)^5.

Choose the global cuspidal splitting determined by the rational tangent u=7. At the rational prime 7 its tangent Kummer cocycle has valuation one. The geometric Legendre monodromy at infinity, in the standard basis, is

    C = [[1,-2],[2,-3]] = -I+M,   M^2=0.

The map has cusp ramification degree five, so its mod-five inertia matrix on the Fermat curve is C^5=-I modulo5. Pulling back along the chosen tangent cocycle makes the inertia at 7 act by this nonidentity matrix. The reference tangent-one cusp representation is unramified at 7; its constants and the nodal quadratic twist have support contained in {2,5}. Thus the raw residual Legendre representation of this actual cuspidal Selmer section is ramified at 7, although 7 is outside {2,5}. The quadratic character supplied by the tangent squareclass cancels this scalar inertia, exactly as LM6-E.8 requires.

The direct matrix computation is retained in code/legendre_checks.py. This corrects the shortened statement R4, not the quadratic-twisted version in LM6. For L6, a claimed conductor bound must name and retain the twisting character, or enlarge its bad-prime set by that character's ramification. For a fixed global section a fixed mod-two Kummer class has finite support, but it must be compared explicitly with the varying Fermat twists before it is absorbed into one uniform set.

## A6/L12(i): independently checked root counterexample

The root supplied the point t=5 at q=5. Its pro-5 abelian Kummer coordinates are (kappa_5(5), kappa_5(-4)). The fifth powers of units modulo25 are {1,7,18,24}, while -4=21 mod25, so kappa_5(-4) is nonzero. Cusp0 forces the second coordinate to vanish; cusp1 forces the first to vanish; cusp infinity forces equality of the coordinates, since kappa_5(-1)=0. Valuations 1 and 0 exclude the latter two. Thus this local section is not cuspidal in the geometric pro-5 abelian quotient.

The underlying Legendre elliptic curve has discriminant 6400, valuation2 at5, and c4=336, a unit at5. It has multiplicative reduction of type I2. The nodal tangent slopes are plus/minus sqrt(-1), which lie in Q5, so the reduction is split multiplicative. Every prime-to-5 Tate representation has nontrivial tame inertia exponent2. Thus this is an honest ramified point and tests precisely the all-coefficient-primes formulation; a prime-to-residue-characteristic punctured-disc comparison must state that restriction.

## A10: a positive-rank cubic with explicit profinite multiples excluded

The root proposed this useful density obstruction. The following verifies it and supplies a concrete positive-rank class without relying on a rank table.

Let C be X^3+Y^3=9Z^3, let O=(1:-1:0), and let V=C minus the divisor XYZ=0. The finite map

    t=X^3/(9Z^3),    1-t=Y^3/(9Z^3)

restricts to a degree-nine finite etale morphism V->U. It is the cubic twist with completed mod-three Kummer class (1/9,1/9). The point P=(1:2:1) lies in V(Q). The explicit functions

    x=12Z/(X+Y),    y=12(X-Y)/(X+Y)

identify (C,O) with the elliptic curve E:y^2=x^3-48, taking P to (4,-4). The inverse projective map is

    (X:Y:Z)=(12+y:12-y:2x).

Substitution gives X^3+Y^3-9Z^3=72(y^2-x^3+48), and the displayed maps are inverse on their affine domains and extend over the smooth projective curves. The point at infinity of E maps to O. The symbolic forward identity is retained in the computation script.

The exact finite-field counts are #E(F_5)=6 and #E(F_13)=21. Reduction at either prime injects the rational torsion subgroup: its kernel is the formal group with parameter in pZ_p, whose formal logarithm is an injective homomorphism into the torsion-free additive group pZ_p for p>=5. Hence rational torsion has order dividing gcd(6,21)=3. The chord formula gives 2P=(28,148), which differs from -P=(4,4). Thus P is not killed by three and has infinite order. In particular this cubic class has positive Mordell--Weil rank.

Fix a coefficient prime l>=5 and the idempotent e_l in Zhat which is one in Z_l and zero in every other factor. For every nonzero a in Z_l, the element a e_l P of the profinite completion E(Q)^hat is nonzero. NONE of these elements is the compactified Kummer class of a Selmer section of V. This is a proved exclusion of an explicit family of profinite multiples, not a classification of all multiples in this positive-rank class.

Indeed, take primes p of good reduction with p=2 mod3 and p=1 mod l. They form a positive-density set by Dirichlet. Cubing is a bijection of F_p, so summing the quadratic character of x^3-48 over F_p gives zero. Thus #E(F_p)=p+1, which is congruent to 2 mod l. The reduction exact sequence

    0 -> E_1(Q_p) -> E(Q_p) -> E(F_p) -> 0

has a pro-p kernel and finite quotient of order prime to l. Therefore E(Q_p) has no l-primary factor, and the image of a e_l P in E(Q_p)^hat is zero. (The coefficient prime p differs from l.) The local Kummer map E(Q_p)->E(Q_p)^hat is injective: E(Q_p) is compact, with an open subgroup isomorphic to Z_p, so the intersection of all nE(Q_p) is zero.

Suppose now that a Selmer section of V had compactified Kummer class a e_l P. At every prime in this positive-density set, the local point or cusp centre would have zero class in E(Q_p)^hat, hence would equal O. Since O is deleted, the local section is cuspidal there. Push the section along V->U. AP-D.25 proves that a globally noncuspidal Selmer section of U has ordinary integral local points at density one; the positive-density cusp set contradicts that conclusion. The pushed section is therefore globally cuspidal.

Here the passage back to V is an explicit decomposition-group intersection. The finite etale cover identifies pi_1(V) with an open subgroup H of pi_1(U). If the pushed image lies in a cusp decomposition group D_c, then the original section lies in H intersect D_c, after the corresponding conjugation. This intersection is the decomposition group of the extended valuation at a boundary point of the normalization C. Its image in G_Q is all of G_Q, so that boundary point is rational. The only rational point of XYZ=0 on C is O: X=0 or Y=0 would force 9 to be a rational cube, and Z=0 gives the sole rational solution (1:-1:0). Hence the original section is cuspidal at O. Compactification kills its inertia, and the induced compactified Kummer class is zero. This contradicts a e_l P nonzero and completes the exclusion.

The argument applies directly to actual Selmer sections and uses no unproved claim that every profinite Mordell--Weil element supplies a full section. The remaining A10 classification includes profinite multiples with infinitely many nonzero primary components, for which the stated local annihilation argument does not provide a positive-density cusp set.
