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

## A.63: coefficient-prime Tate transcendence and the full dyadic family

The polished proof is in `work/sections/legendre_tate_transcendence.tex`.
For E/Q potentially multiplicative at p, its actual Tate parameter q0 lies in Qp and has positive integral valuation N. Its class in H1(Qp,Qp(1)) cannot be proportional to the class of any rational r. If vp(r)=0, valuation excludes proportionality; otherwise the scalar is N/vp(r), so q0^vp(r)/r^N lies in the torsion kernel of rational Kummer and is a root of unity. This would make q0 algebraic over Q, contrary to the proved p-adic Mahler--Manin theorem because J(q0)=j(E) is rational. The same assertion after a finite splitting extension follows by restriction/corestriction.

The exact cusp Tate classes are A^2/256, B^2/256 and A^(-2)/256. Their formal unit factors have compatible roots with constant term one and hence vanish on the cusp decomposition section. The coefficient-prime cyclotomic line is unique, so an actual Tate comparison preserves the full extension and its rational Kummer line.

Consequently, if A or B is globally supported only at2, two cusp labels are excluded and A.37 recognizes the section. This recognizes every realization with lambda or1-lambda in {+-2^m:m in Z}, including its six S3 transforms, with arbitrary integral GL intertwiner. The earlier A.54 odd-exponent/determinant restrictions are unnecessary for this entire family.

Opened exact primary statements: coauthor F. Gramain, *Transcendance et fonctions modulaires*, JTNB11(1999), pp73--74, https://www.numdam.org/article/JTNB_1999__11_1_73_0.pdf ; P. Graftieaux, *Theoreme stephanois et methode des pentes*, Sem.Con gres12(2005), p180, https://smf.emath.fr/sites/default/files/2017-08/smf_sem-cong_12_179-213__sample.pdf . Original theorem metadata: Barre-Sirieix--Diaz--Gramain--Philibert, Invent.Math.124(1996),1--9, DOI10.1007/s002220050044. The original publisher full PDF was unavailable; the exact theorem was opened in the two primary accounts. Bib keys LegBDGP1996, LegGramain1999, LegGraftieaux2005 added.

## A.64: the normalized prime-power family with H conjugacy

The complete proof is in `work/sections/legendre_normalized_prime_power.tex`.
For lambda=+-16p^n, p odd and n positive, the curve is potentially good at2. H^ab's separate mod8 characters force the ordinary local valuation pair exactly(4,0), by checking all twelve potentially-good dyadic pairs. The odd labeled Tate lines give A=+-16p^beta globally. Atp, a cusp-zero section would have Tate class p^(2beta), excluded by A.63's rational-line argument. The ordinary p-valuation therefore makes beta one integer in Zhat, so A is rational and finite-support recognition applies. The primitive labeled-isogeny argument identifies the exact point lambda. The geometric-conjugator hypothesis is retained in this family. Actual S3 maps and the central quadratic factor preserve that hypothesis.

## A.67: equal local full H data distinguished by a noncongruence cover

The proof is in `work/sections/local_full_congruence_cusp.tex`; the exact finite arithmetic certificate and output are `work/code/local_congruence_cusp_certificate.py` and `work/code/local_congruence_cusp_certificate_output.txt`.
OverQ5, choose C=16sqrt(q0)=5sqrt(F(5)) with sqrt(F(5)) in1+5Z5. The point5 and the cusp-zero section with tangentC have the same paired Tate extension at every odd coefficient, including5. Their actual geometric pro2 images agree by A.49 and the unique2-divisibility of C/5. Thus the product conjugator belongs to the full geometric H, not merely GL2. The finite etale cover z^5=1-t lifts the cusp through sheet1 but does not lift point5, since -4=21mod25 is not a fifth power. Its geometric quotient cannot factor H because H^ab=(Z/8)^2+Z/3 has no quotient5. This is explicitly a local statement, with no global Selmer lift asserted.

## A.70: explicit finite Kummer isolation for every rational realization

The proof is in `work/sections/finite_noncongruence_isolation.tex`.
Write lambda=a/c,1-lambda=b/c with coprimea+b=c andc>0. Let e_p=vp(abc). Take N=product_(oddp|abc)p^e_p, times2^(e2-1) only whene2>=5. A section with labeled integral realization E_lambda and Kummer congruences A=lambda,B=1-lambda moduloN is exactly the pointlambda.

At each potentially multiplicativep, the three cusp-regular units1-t,t,t/(t-1) have atlambda one unit entry of exact principal-unit depthe_p and two entries of valuations+-e_p. None is an N_p-th power: N_p=p^e_p foroddp andN2=2^(e2-1) fordyadicbadp. Their respective cusp packets make one of these units equal1, so the congruences exclude every local cusp. The pointed cover is lambda u^N+(1-lambda)v^N=1 withuv nonzero andpoint(1,1). The exact topological enlargement is E/(C_H intersect M_N)=E_H fibreproduct E_ab,N over(H^ab/NH^ab) semidirect G_Q. This isolates the point in its full-H fibre by finite noncongruence data, but does not derive those extra finite characters from H alone.

## Independent higher-quotient audits completed

A.59 coefficient-prime analytic lemma, A.61 full class-four lift, A.62 cubic recursion, A.65 all-fixed-depth lift, A.66 general fixed-product recursion, and A.68 generalized-Jacobian/metabelian comparison were independently checked. No unresolved gap was found in the versions sent to the root. The A.66 finite certificate is `work/code/general_exponent_certificate.py` with retained output: 3500 exact normalized-series coefficient checks; 2065 exponential-denominator checks;105 literal local-image quotient balls with14490inputs;433 LTE/gcd/common-image cases;21 fresh exact gcd identities;254698 primitive-preimage targets;1438 factorial precision inequalities. It does not claim to have run a giant prime-search stage.

The open several-label recognition system remains recorded exactly in A.63.12--17: a single global multiplier squareclass, independent local unit-square diagonal factors, the full coefficient-prime Tate logarithm equations, and the regular-coordinate Kummer equations at each assigned cusp. Two rational Kummer generators already span H1(Qp,Qp(1)) through the displayed valuation/logarithm map, so the one-line transcendence obstruction is not asserted to resolve an arbitrary larger support.


## A.74: all odd-prime analytic point-to-cusp maps

The complete source is `work/sections/odd_local_congruence_map.tex`; certificate and output are `work/code/odd_local_congruence_certificate.py` and `work/code/odd_local_congruence_certificate_output.txt`. The local agent independently audited the proof in full.

For every odd p, the normalized nome q(t)=t^2 F(t)/256 has F in1+tZ[1/2][[t]], F=1+t+O(t^2). The actual analytic map Theta_p(t)=t sqrt(F(t)) is an isometric bijection pZp->pZp. The point at x and the cusp-zero section with tangent Theta_p(x) are conjugate in the full H extension. The common splitting character is chi_(−1), and after paired Tate bases the explicit matrix U_l=[[1,h_l],[0,1]] intertwines the two integral cocycles with difference(chi_l−1)h_l. This includes l=p. At2 the formal ring Zp[[t]][1/(pt)] and A49's exact tame comparison give an H2 conjugator; the ratio Theta_p(x)/x is uniquely2-divisible. No p-power formal root is evaluated at x.

If vp(x)=e, both Theta_p(x)/x−1 and(1−x)−1 have exact valuatione. Thus the abelian p-power images agree below p^e and separate at p^e. The explicit cover z^(p^e)=1−t lifts the cusp but not the point, and fails the H^ab criterion even whenp3. For rationalx the tangent is transcendental by the proved Mahler–Manin theorem. The scope is local.

The certificate checks7 bijective finite discs,129564 isometry pairs,25 exact unit-power images,136 Tate cases(60split/76nonsplit), and476 separating levels. All checks passed.

## A.78: exact ordinary bad-place values and support only at actual cusps

The complete source is `work/sections/legendre_ordinary_support.tex`; both root and birational independent audits passed. Certificate/output are `work/code/legendre_ordinary_support_certificate.py` and `work/code/legendre_ordinary_support_certificate_output.txt`.

With any labeled full integral realization E_lambda, an ordinary local point at a potentially multiplicative bad prime equals lambda exactly. Over a common splitting field, the saturated Tate-line comparison gives N_x=(a_l/d_l)N_0 with integral units for every coefficient. The positive rational ratio is a unit everywhere, hence1. Therefore all Kummer classes q_x/q_0 vanish and full local Kummer injectivity gives q_x=q_0. The resulting actual curve isomorphism differs from the given 2-adic intertwiner by a scalar: commutation forces equal diagonal entries because the extension class is nonzero, and then zero off-diagonal because chi2 is nontrivial. The scalar is a Z2-unit, preserving the ordered2torsion, so the affine x-coordinate map fixes0,1,lambda.

Under full H conjugacy, every unknown relative valuation exponent is supported only on the actual cuspidal primes C. At potentially-good2 the twelve possible valuation pairs(k,0),(0,k),(−k,−k),1<=k<=4 are distinctmod8 and H^ab fixes the exact pair. H^ab also fixes both global signs. The dyadic Tate series proves the same labeled cyclotomic line as at odd primes: forq=r^2, v X(−1)=−2v2, v(X(r)−X(−r))=2v2+vr, and both other differences have valuation−2v2. Thus every cusp label is the point's contact label.

Writing C0,C1,Cinfty for these label classes gives the exact products
A=lambda prod_(C0 unionCinfty) p^delta_p,
B=(1−lambda) prod_(C1 unionCinfty) p^delta_p.
Eachdelta_p is24-divisible. More precisely delta_p=sigma_p m_p(u_p^2−1), with m_p=e_p foroddp ande2−4at2, sigma+for0/1and−forinfinity, and separateunits u_p inZhat^×. No common unit across local places is asserted. The final table A78.14 retains all regular-coordinate local Kummer equations, and A78.15 gives the resulting exact inhomogeneous quadratic equation in coefficient-p units. These equations supplement the full Tate-logarithm equations of A63; their general inconsistency has not been proved.

Direct primary source opened for the coordinate series: John Tate, *A Review of Non-Archimedean Elliptic Functions*, equations(1)–(4), manuscriptp2, Theorem1p6, https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf . Bib keyLegTate1995 added. The certificate checks48 exact dyadic Tate cases including q*j(lambda)=q*J(q) modulo2^14, all12 valuation pairs, and144 label-vector kernel conditions; allpassed.

## Further independent audits

A72 finite-Q plus full-abelian ghosts with actual local matching passed a complete independent audit, including distinguished component maps, local analytic continuation whenp divides the quotient exponent, entire new-prime boundary fibres, good-reduction counting bound, and the inverse-limit compact conjugator argument. A73's uniform finite-level higher-character obstruction passed, including the exact primitive cyclotomic element in every fibre factor, all Q2 power conditions, local invariant1/2 and global invariant-sum contradiction. Its certificate was rerun. A76's density-one completed Kummer injectivity also passed: a local2m-power condition gives globalm-power via the relative Kummer subgroup and real radical argument; the doubled exponent is essential, as the16/eighth-power example verifies. No completed old-coordinate tuple is inferred from A73.


## A.79: a fixed valuation minimum excludes an entire cusp label

The proof is `work/sections/legendre_log_minimum.tex`; root and local_preprint independently audited it successfully. Code/output are `work/code/legendre_log_minimum_certificate.py` and `work/code/legendre_log_minimum_certificate_output.txt`.

Let lambda>1 be even, with lambda−1=product q^e_q and k=v2(lambda). The possible cusp0 primes are the odd divisors oflambda and2 onlywhenk>=5. At an odd q dividinglambda−1, the arbitrary labeled integral Tate comparison gives beta_q,l=e_q times a Z_l-unit, including coefficientl=q; no square multiplier assumption is needed. Whenknotin{2,4}, the B coordinate has dyadic valuationzero by parity(k1or3), or by A78's exact ordinary value/dyadic label(k>=5). For k2or4 the same conclusion uses the full-H mod8 characters. Thus B=−product q^beta_q.

At a proposed cusp0 primep, localregularityB_p=1 gives sum beta_q,p log_p(q)=0. Every summand has exact valuation w_pq=vp(e_q)+vp(q^(p−1)−1) foroddp, andw_2q=v2(e_q)+v2(q²−1)−1. A unique minimum cannot cancel. If that minimum is unique at every candidatep, allcusp0 places are excluded; A78 already excludesinfinityforintegerlambda, soA37 recognizes the section. This proves the exact criterion withoutH whenknotin{2,4}, and withH whenk2or4.

The explicit infinite family lambda=191^(2j+1)+1,j>=0, hask6 and is recognized with arbitrary labeled integral GL comparison. The family lambda=3^(2j+1)+1,j>=2, hask2 and is recognized withH. Each has a singleodd-neighbourprime, so every minimumisunique; the exact constant dyadic valuations follow from the odd alternating quotient ofq^(odd)+1 byq+1. These families lie outside A41's odd-dyadic-valuation hypothesis, A45's finite list, and A63's dyadic-coordinate family, as verified through the actual sixS3coordinatefunctions.

Composite-neighbour examples outside those earlier criteria arelambda88 and120, both withoutH. For88, weightsat11 are2forq3 and1forq29. For120, weightsat3 are1,2forq7,17, andat5 theyare2,1. The certificate tests the criterion on evenlambda<=5000:714pass; relative toA41/A45/A63,17additionalparameters have arbitraryGLscope and217requireH; afteralsoexcludingA64 thereare199additionalHparameters. It retains exactmodular certificates for all computed logarithmvaluations. This finite enumeration illustrates the provedcriterion and is not a classification of allrealizations.

## A.82: the common multiplier gives an exact finite quadratic test

Complete proof: `work/sections/legendre_square_form.tex`. Certificate and output: `work/code/legendre_square_form_certificate.py`, `work/code/legendre_square_form_certificate_output.txt`. Birational's independent audit passed.

Fix one global paired integral intertwiner g_l and Delta_l=det(g_l). Every geometric representative change and every paired local Tate basis change has determinant one. At each odd contact-one prime q, the exact ratio is beta_(q,l)/e_q=a_(q,l)^2/Delta_l, including ordinary q where the ratio is one. At a proposed cusp-zero prime p, multiplication of the regular-coordinate equation by the SAME Delta_p gives sum e_q log_p(q) a_(q,p)^2=0, with every variable a unit. No individual ratio is asserted square before Delta is controlled.

After dividing coefficients by their smallest valuation, at odd p the exact criterion is existence of a unit zero of the reduced diagonal form over F_p. A pivot derivative is a unit, so every such zero lifts; the equivalence is proved. At2 all unit squares are1mod8, and Hensel with derivative valuation1 proves the exact criterion k>=d_2+3. Lambda34 has normalized Fermat quotients10,9 at17 for its neighbour primes3,11; the required ratio14 is nonsquare, so it is recognized without H. A separate coefficient3 calculation excludes its cusp1 there, fixes ordinary3, and then excludes cusp11; the dyadic alternatives are checked through the full squareclasses.

The certificate checks584 odd normalized forms,12256 explicit lifts modulo p^2,500 dyadic forms,52 lifts modulo2^10,880 binary equivalences, and every displayed34 residue. All pass.

## A.84: the full Tate extension recognizes lambda35

Complete proof: `work/sections/legendre_parameter_35.tex`; certificate and output: `work/code/legendre_parameter_35_certificate.py`, `work/code/legendre_parameter_35_certificate_output.txt`. Local agent's full independent audit passed.

The exact dyadic pair is(0,1), giving A=5^beta7^gamma, B=-2*17^alpha with all exponents profinite units. Under the nonpoint supposition, label1 must occur at17. Its full coefficient17 Tate comparison uses q17=17^2 F(-34)/64 and gives alpha17=14mod17, a nonsquare. A34 then forces every bad place to be cuspidal. At5, regular B=1 gives alpha5=3mod5, while the full Tate equation q5=35^2 F(35)/256 gives beta5=4mod5 because log5(7)=0mod25. Their ratio2 is nonsquare, contradicting the SAME global multiplier at5. No H hypothesis is used. The simpler regular-coordinate square form at17 has a genuine local unit solution (its required ratio13 is square); the retained computation distinguishes the extra full Tate equation from that weaker projection.

## A.87: contact-two dyadic inertia fixes every odd multiplier

Complete proof: `work/sections/legendre_dyadic_symplectic.tex`. Certificate and output: `work/code/legendre_dyadic_symplectic_certificate.py`, `work/code/legendre_dyadic_symplectic_certificate_output.txt`.

At each of the three dyadic contact-order-two labels, an explicit integral Legendre equation has invariant valuations(4,6,8) and normalized discriminant1mod8. The finite inertia action onT3 is faithful modulo3 because1+3M2(Z3) is torsion-free, and the Weil pairing embeds it inSL2(F3). The good-reduction discriminant forces3 to divide its order. The two elementary order-three generators exclude an index-two subgroup, hence order12. Freitas–Kraus Table5 and Section14.3 exclude orders3 and6 because they require normalized discriminant-1mod4. Thus the group isSL2(F3), order24.

At contact order4, the exact negative twist y^2=x(x+1)(x+16u), under x=4X,y=8Y+4X, is Y^2+XY=X^3+4uX^2+uX with unit discriminant u^2(1-16u)^2. The explicit maps E_t to E_(1-t)^(-1) by(x,y)->(x-1,y), and E_t=E_(1/t)^(t), cover the other labels; all contact4 inertia has order at most2. For a realized contact2 curve, the actual dyadic point has even valuation parities, so only contact2 or4 is possible; equality of the actual inertia representations forces contact2.

The actual odd-coefficient intertwiners identify the inertial fields of the realized and point curves, both with minimal discriminant valuation8. Freitas–Kraus Theorem7 then forces every odd multiplier to be square, and its uniqueness clause applies to the actual intertwiner. Geometric local representative changes have determinant1, so these are the original global Delta_l. No claim onDelta2 is made. For lambda=4u, u=1or3mod8, its labeled unit squareclasses exclude contact1 andinfinity, fixing dyadic pair(2,0). Thus A79/A82's full-H proviso at k2 can be dropped on this exact subset.

Forlambda36 this gives A=4*3^alpha, B=-5^beta7^gamma, with X=alpha/2,beta,gamma profinite units and all their odd components square units. Cusp1 at5 would force X5=-log5(2)/log5(3)=2mod5, impossible. Ordinary5 fixes beta=1. The full Tate equation at7 then gives gamma7=(2log7(5)-8log7(2))/(2log7(5)-8log7(2)+log7F(-35))=4/6=3mod7, also nonsquare. Only cusp label0 can remain, so A37 gives the exact point36.

Primary text opened: Nuno Freitas and Alain Kraus, arXiv:1607.01218v5, 1June2022, https://arxiv.org/pdf/1607.01218v5 . Exact passages: Section4.1 inertial field and coefficient independence; Proposition6/Table5 caseC3iii; complete order6 list inSection14.3; Theorem7 and its no-both-types clause. Bib keyLegFreitasKraus2022 records the arXiv version because theorem numbers differ from publication. The certificate checks768 invariant triples, the finiteSL2(F3) generation and derived subgroup, the symbolic good twist, all contact2 squareclass alternatives, and the exact inverse-nome/logarithm residues at7. All pass.

### A.87 completed scope extension

The appended (A87.2a--g), independently audited by the local agent, also forces dyadic pair(2,0) for every integerlambda withv2lambda2 andlambda0or1mod9. At coefficient3, automatic square multipliers give alpha_p-f_p in3f_pZ3 andbeta_q-e_q in3e_qZ3. Multiplying by the local logarithms gives exact weighted congruences modulo9, including weights divisible3. For each alternate dyadic pair, the cusp's regular coordinate at the bad prime3 would be a nonzero multiple oflog3(2)=6mod9. Thus3 is ordinary. A34 makes the whole multiplier square, A17 gives the actual H adjustment, and A56's two separate mod8 characters rule out the alternate pair. Hence the H proviso in A79/A82 at dyadic valuation2 is unnecessary on this additional infinite congruence class.

In particular everylambda=3^n+1,n>=1 is now recognized with arbitrary labeled integral GL comparison: oddn>=3 use the modulo9 extension; n1is4 andusesu1mod8; evenn have dyadic valuation1 anduseA41. The certificate includes378 weightedmod9 checks and the family arithmetic for n1..120, while the proof is uniform.

## A.91: contact-four inertia fixes its exact label without H

Complete proof: `work/sections/legendre_dyadic_four.tex`. Certificate/output: `work/code/legendre_dyadic_four_certificate.py`, `work/code/legendre_dyadic_four_certificate_output.txt`. Local agent's full independent audit passed.

The explicit good curve G_v:Y²+XY=X³+4vX²+vX has discriminantv²(1−16v)². The three contact4 parameter types have, respectively, squareclass pairs/inertia characters (v,1)/chi_−1 for16v, (1,v)/1 for1−16v, and(v,−v)/chi_−v forv/16. The exact maps are the negative twist model fromA87, translation(x,y)->(x−1,y), andE_t=E_(1/t)^(t). Chi_−1 is ramified since(1+i)²=2i. The actual integral comparison excludes contact2 by its e24inertia. At contact4, every change of label compatible with the prescribed two squareclasses would change the inertia character between trivial andchi_−1. Hence the actual dyadic valuation pair equals the realized pair at each of the three labels.

This removes A79/A82's H proviso at k4 entirely. It also upgrades A64: everylambda=±16p^n,p odd,n>=1 is recognized under arbitrary labeled integral GL comparison. The exact support isA=±16p^beta. A cusp atp would have Tate classp^(2beta), on the rational Kummerline excluded byA63; ordinaryp has exactparameterlambda byA78, so beta=n inZhat andA is rational. Finite-value recognition gives the point. Both negative units and allsixS3 transforms are covered by the actual curve maps(x,y)->(1−x,iy) and(x,y)->(x/t,y/(t sqrt(t))); the second twisting character agrees on sectionandpoint byA16.

The certificate verifies144 comparisons ofallcontact4unit-class/inertiarows,256signedoddunits, thesymbolicgoodmodelanddiscriminant, andthetwoS3coordinateidentities. It makes no claim to infer the full-section conclusion from finite arithmetic alone.

## A.90 independent audit: completed old coordinates with a new-coordinate obstruction

The full proof in `work/sections/completed_old_obstruction_agent.tex` passed independent audit. The mixed-exponent common-field lemma is exact for all4|n_j, including odd factors: withN=lcm n_j, the actual root action gives simultaneous stabilizer equations modulo2n_j. For cyclotomicu3mod4, choose every prime-radical rotation with its prescribed parity and divisible by the lcm of all odd gcdparts. This gives an actual common fixed tuple. The elementtau actingnontriviallyoni then generates the entire subgroup fixing the quadraticfield, andA57's maximalabelianfield computation proves the claimed commonfield.

The refinement compatibility uses the stronger individual local invariant(X_i,chi)=0 for every boundary quadraticcharacter, not an inference from(T−ci,chi). A88 proves these zeros at the initialdyadicpoint andP0 elsewhere. The principalidele/rayclass calculation uses the oldrootsX_i themselves. The exact mapX_i=uY_i^h givesY_i near1 atcontrolledprimes, henceasquare, includingp|h. Otherroots stayfixed. Newcoefficientprimes and allremaininggoodprimes haveunitroots againstunramifiedboundarycharacters, so the invariant persists.

The mixed-cover genusandboundarybound includes the wholefibre atnewc, allfreshprimesavoidc−ci, andeveryprimeeventuallyenters thecontrolledset. ItsT-coordinate is thenfixedforever. The exponents4h! arecofinalforallintegers, whileeachcoefficientupdate isanold-exponentpower. Thus thelocalfinitepowerclasses identify thefullcompletedAi withtheordinaryt_p−ci atallmoduli. Noordinaryp-adicconvergence oftherationalcoefficients isclaimedorneeded. Eachcoordinategetsinfinitelymanyfreshpositivevaluations, whichremainfixedbytheunitrootinvariant.

The outside-S_* Brauer evaluation iszeroforeveryC0point, through theunit/pole/fibreexhaustion. Thecontrolleddyadicpoint retainsinvariant1/2. Aputativenewglobalcompletedcoordinate would giveaglobalsquareclasswiththatimpossiblelocalinvariantsum. Allthese stepspassed; thefinitecertificatewasrerun separately.

## A.92 independent audit

The full proof in `work/sections/norm_split_generation_agent.tex` passed independent audit. The primary Hilbert class-field compositum is an unramified abelian ell-extension of the Galois closureL. For split rationalprimes, the exact Artin values arepsi(g^−1sigma g), so annihilating allprime differences is equivalent to invariance ofpsi onV. The holomorph H² with Q_ell/Z_ell vanishes: bothcyclicdegree2terms vanish bydivisibility, and thedegree(1,1)termvanishes because theinverseprimitiveunitaction minusone is invertible. Thefive-termsequence andtheexplicitprojection toU extendthecharacterexactly fromH toG.

For every unramified rationalprime, theactualFrobenius cyclesgivecharactervaluesf_i chi(sigma), soeverylocal weightednormkernel isannihilated. The finiteclassgroup therefore placesallunramifiedR_q inthesplit-prime subgroup. Thecompletedc0tail divisiblebyell^a remainsacompleteddivisor afterdivision; thisjustifies reducingtheclass targettoanalgebraicsumoflocalimages. Ramifiedqnotell arealreadystableatleveln andliftthroughthelocalinversemodules; finitelymanysuchlifts satisfytheglobalc0condition. Atell3thecoefficient-placekernel iszero byEisenstein. Theconclusionisafixed-levelgenerationequality, withnocompatiblesplit-prime correctionasserted.

## A.93 independent audit

The full proof in `work/sections/completed_old_section_obstruction.tex` passed independent audit. The normalized Brauerclass has a μ2 lift on the propercurve whose value atP0 iszero, because H²(Q,μ2)→Br(Q)[2] isanisomorphism. Restrictionto theaffinecover andtheétale K(pi,1)comparison identifyit withacentralprofiniteextension ofH⋊GQ. Thetwoactualsplittings overfreeH andoverGQ produce thepreciseone-cocycleeta andcross-two-cocycle eta(g1)(g1h2). EverycharacterofH killsK=H²[H,H], so theclass factorsonthecoversubgroup(H/K)⋊GQ; noextension tothewholelargerquotient ispresumed.

Themod4Kummercondition isexactly thevanishingofthepointedcover'storsorclass, andageometricconjugationliftsthesectionintothecoversubgroup. Atordinarylocalpoints, thefixedsheet isarationalpoint oftheactualquarticcover andthecoversectionisconjugatebyH/K tothatpoint. Theμ2pullback thereforeequalstheBrauer evaluation. Atarealcusp, inertiaorbitsonthefinitecoversheets indextheboundarypoints; afixedsheetgivesarealboundarypoint, andthemaptothepropercurvekillsitsinertia. Theproperμ2liftthereforehastherequiredzerorealpullback. Thefinitequotientstatementretainstheordinaryrealpointcondition, avoidinganincorrectinferencefromBrR alone.

The geometricquotient hasorder2^135 fromSchreier rank129, andPi''liesinK. Thethirdquarticcharacter remainsnonzero, givingtheexactreasonthisquotientdoesnotfactor throughthetripodmapwhichkillsc3inertia. Thus thecompletedthree-coordinate tuplehasnofullSelmersectiononthefour-puncturedline andnolocallymatchingsection oftheindicatedfinite/metabelianquotients, withoutanassertionaboutatripodsectionusingonlyitsfirsttwocoordinates.

## A.94: all odd multipliers at dyadic contacts one through three

The proof is `work/sections/legendre_dyadic_multiplier_range.tex`; its exact certificate and output are `work/code/legendre_dyadic_multiplier_range_certificate.py` and `work/code/legendre_dyadic_multiplier_range_certificate_output.txt`. Local agent's full independent audit passed after reopening the primary conductor criteria.

The explicit minimal invariant rows are(4,>=7,6)/(6,>=10,12) atcontact1, and(4,6,10)/(6,9,16) atcontact3, with the second row ineachpair belongingtoinfinity. Theinfinitymodelscome fromactualrationalchangesofvariables. Theyareminimal becausean integralWeierstrass c4 is eitherodd ordivisibleby16, excludingthevalue2thatnonminimal scalingwould produce. Atcontact1theexactA39cubicresolvent4t(1−t) isacubeinQ2, so theinertiaimage lies intheorder8quaternionkernel oftheactualpair-partitionmapSL2(F3)→C3. Freitas–Kraus'sorder2/4lists excludethoseorders. Contact3good-reductiondiscriminantsforce3intheorder, theindex2group argumentexcludes12, andtheexactorder3/6invariantlists leave24. Thetwoorders distinguishactualcontact1from3afterA16hasfixedthelabelbyparity.

Forcontact1atlabels0/1themodelhasnormalizedc4=3mod4 andtriple(4,>=7,6). FKProp6/Table5givesconductor32 exceptpossibly64. Inthat64case, Thm9appliedtotheself-pair forcesits2twistintoconductor32or256. Thetwist'sminimaltriple(6,>=10,12)stillhasnormalizedc4=3, contradictingTable5Db'srequiredresidue1. HencebothcomparedcurvesarepreciselyThm9/Table3casea. Atinfinitythesame2twistonbothsidesisliterally y²=x(x−2)(x−u), againcasea. Thms8/9thereforeforceeveryoddmultiplier tobesquare. Forcontact3, Thm7appliestobothminimaldiscriminantvaluations10or16. Contact2wasA87. Alltheactualglobalmultipliersareretained; noDelta2claimismade.

Atcontact4A91givesexactlabels. TheequalquadraticuntwistsyieldG_u,G_v (orG_(1/u),G_(1/v)atinfinity), withtheactualsameF2reduction y²+xy=x³+x. It has4points, soFrobeniustrace−1,det2,discriminant−7. Mod7itcannotbescalar, sinceascalarliftwouldmakeitsdiscriminantdivisible49. Itsnon-scalarJordancentralizerhasmatrices(a,b;0,a), thereforeonlysquaredeterminants. Thesymplecticspecializationmaps proveDelta7square. Noall-oddassertionismadeatcontact4.

Thecertificatechecks1536minimal-invariantrows,256exacttwo-twist/conductorresiduecases,256integralWeierstrassdivisibilitycases,768resolventvaluations,theactualorder8kernel,andall42invertibleFrobeniuscentralizermatricesmod7. Allchecks pass.


## A.97: own-coefficient and fixed-coefficient rigidity

The complete proof is `work/sections/own_coefficient_rigidity.tex`. Root and local-preprint independent audits passed. For an ordinary completed pair, equality with a rational pair in the local coefficient-p components at one physical prime p already forces the actual ordinary coordinate to be that rational number. The exact odd-p local kernel is μ_(p−1); the two root-of-unity ratios lie in a cyclotomic number field, and a complex embedding gives |1−λζ|²=(1−λ)², forcing ζ=η=1 for every rational λ≠0,1. At p=2 the own-coefficient local map is injective. A76 then gives density-one rigidity and a positive-density Chebotarev set of failures for any nonrational pair.

A single fixed global coefficient equality also suffices when the pair is ordinary at every finite place: its global valuations are ordinary integers, and equality in Z_ell fixes all of them. The exact kernel of the global valuation map is ±1 by rational prime factorization at each exponent. The unit equation forces both remaining signs. Chinese remainder gives the continuous product of the primary completions without any compactness claim. Therefore an ordinary pair cannot be a nontrivial patch of a rational pair supported at any proper subset of coefficient primes.

The density-one part requires ordinary points only at the density-one primes under comparison. Applied to a Selmer section in A14, whose possible finite cusp places are confined to the finite potentially multiplicative set by A37, it excludes finite-primary or density-zero-primary Kummer patches of the realized point. The three actual regular cusp functions 1−t,t,t/(t−1) exclude every finite cusp once the global pair is rational. Every different section in this realization range must change the global coefficient pair on a positive-density Chebotarev class. The fixed-single-global-coefficient argument retains its stronger all-place ordinariness hypothesis. No coefficient equality is inferred from the A56 map T→H^ab=(a mod8,b mod8,a+b mod3); full-H recognition remains unresolved.

## A.96 independent audit

The complete saved proof `work/sections/quartic_tripod_initialization_agent.tex` passed independent audit. The actual stabilizer equations divide to the stated F2 system; its dual relation characters give all common quartic fibre characters, and the negative-relation generators exhaust the field after the exact positive-relation elimination identity. The explicit map ((1−ι)z)^2=2r works for every root choice. The singleton norms and two-coordinate norm have the stated constants; in the pair calculation u k²=bc and (2k)/(2r)=D0/r² give the precise squareclass comparison. The affine coordinate change and A85 reciprocity/sufficiency use the actual pointed forgetful map. The statement concerns one prescribed point at each selected place.


## A.102: full H with every bad-place comparison, and a good-prime obstruction

The proof is `work/sections/legendre_bad_place_fibre.tex`; the exact certificate and retained output are `work/code/legendre_bad_place_fibre_certificate.py` and `work/code/legendre_bad_place_fibre_certificate_output.txt`. Root and local-preprint audited the base construction. The additional recognition proof has also been independently checked in argument and is saved in the same statement.

For lambda254=2*127 and1-lambda=-11*23, define completed exponents alpha,beta with all components1 except coefficient23/127. At127 set alpha=-6log(2)/log(q127/127^2), beta=-log(11)/log(23); at23 set alpha=-log(2)/log(127), beta=(2log(11)-8log(2))/log(q23/23^2). Their respective residues are31,49 mod127 and8,4 mod23, all nonzero squares, with roots44,7 and10,2. The exact nomes satisfy q127/127²=2^-6 F(254) and q23/23²=11²*2^-8 F(-253), F(w)=1+w+O(w²). The four defining ratios are actual p-adic units; the certificate checks them modulo p^6 with the nomes/logarithms retained modulo p^9/p^7.

Set A=2*127^alpha,B=-11*23^beta. Their relative cocycle from point254 has only coefficient23/127 components, so maps literally to zero in H^ab. A56's compact fibre-product isomorphism constructs an actual continuous global section of E/(kerH intersect Gamma2Pi), with full H image exactly point254 and those finite-support Kummer classes. At127 B=1 and cusp0's Tate class A²/256 equals alpha times the realized nome class in the full completion. At23 A=1 and cusp1's B²/256 equals beta times its nome class. Root-of-unity components match because23 does not divide126 and127 does not divide22. Every paired Tate intertwiner has determinant1. At2 and11 the whole local pair remains the honest point254; the changed coefficient primes occur in none of their relevant unit factors. These are exactly all bad primes.

Simultaneous local conjugacy is proved in the actual quotient, not inferred from independent classes. Its geometric group is Q23 times the product over ell>=5 of(Hell times Tell), where Q23=(H2 times H3) fibre(T2 times T3) over the common abelian factors. The global quotient section is literally the point in Q23. A49's same normalization/Abhyankar proof works for geometric covers of order2^a3^b at residue23/127, giving one actual disc conjugator for the entire Q23 factor. The tangent2/3 classes are unchanged. The other factors have no common quotient, so the paired H intertwiner and abelian coboundary can be combined independently.

At good47, exponents modulo46 are31,27, yielding both residues A=B=33, whose sum is19. The three cusp regular-coordinate residues are33,33,-1, so every cusp is excluded. The finite exponent46 quotient also excludes nonintegral ordinary points: near0/1/infinity one of those regular coordinates has residue1. Thus the global quotient section matches every bad place but has no local point/cusp image at47, and cannot lift to a Selmer section. No full-section existence is asserted.

The same calculation recognizes every actual noncuspidal Selmer section with arbitrary labeled integral realization E254. A94 fixes dyadic pair(1,0) and makes all odd multipliers square. A16 fixes signs and the odd-prime valuation parities, giving A=2*127^u,B=-11^v*23^w with unit exponents and with only labels0at127 and1at11/23 available. At11 a cusp1 would force u11=-log11(2)/log11(127)=10mod11, a nonsquare, since both normalized logs equal6. Hence11 is ordinary and A78 gives v=1 globally. A37 forces both remaining labels for any nonpoint. The actual coefficient23 regular/Tate equations then force u23=8,w23=4mod23; their two-components are odd, so the same exponents31,27mod46 hold regardless every other coefficient choice. Good47 gives the contradiction. A78's ordinary value at11 identifies the rational point exactly as254. This is a cross-prime use of the fixed-H support equations: bad-place own-coefficient data are transported through an explicit finite-field reduction at a different good prime. The broader recognition problem remains unresolved.


## A.104: the simultaneous projection fibre and its relative signs

The complete proof is `work/sections/legendre_simultaneous_fibre.tex`, with certificate/output `work/code/legendre_simultaneous_fibre_certificate.py` and `work/code/legendre_simultaneous_fibre_certificate_output.txt`. Local-preprint independently audited the full proof and both finite strengthenings; all passed. Root is auditing for integration. No active paper input was added by this agent.

For J=H fibre_M T and K=ker(T→M), fixing the H point representative makes the remaining sections continuous K-cocycles. Requiring the full abelian point class gives exactly ker(H1(K)→H1(T))=δ(M^G), because T^G=0. Forgetting the H representative quotients by the actual H-centralizer image in M; the conjugation formula is z(g)↦z(g)+t−gt for(h,t)∈J. OverQ andQ3, M^G=(μ8)^2⊕μ3 consists of four elements(4epsilon0,4epsilon1,0). Explicit lifts aret=(12epsilon0,12epsilon1), with cocycle(chi−1)t. The abelian projection is point conjugated by−t, while the H projection remains literally the point; (1,−t) is not a simultaneous geometric element for a nonzero invariant.

The centralizer image is zero uniformly at physical3. In the potentially multiplicative case the full integral Tate extension has scalar rational commutant, so H2's centralizer isI. In the good case every Legendre parameter reduces to2mod3. The reduction has4points, soFrobeniusF hastrace0,det3; A16 givesFmod4=(3,2;2,1). B=(F−I)/2 hasB²+B+I=0 and is cyclic overZ2, so its integral commutant isZ2[B]. Forh=a+bB∈H2, a1mod4,b0mod4. Writinga1+4u,b4v anddet1 givesv2umod4. Thereforehmod16=I+4uF=c^u forA56's exactcommutatorc=(13,8;8,5). A56's full inverse-limit derived-group identity, including the entire level16kernel, makes its H2ab imagezero. There are no coefficient3 invariants, so this proves the entire centralizer imagezero locally and hence globally. Exactlyfour globalclassesremain, restriction mapsbijectivelytoexactlyfour Q3classes, andonlyzero ispoint/cuspidal.

For good3 the finite detector is(H2mod32) fibre_(Z8)^2 (Z16)^2, oforder8192. A finite centralizer mod32 reduces to the same commutant ofBmod16, hence mapszero toHab. Its abelian conjugator mustbe8-divisible, whoseFrob3coboundary iszero mod16; the nonzero relative-sign cocycle hasvalue8inaselectedcoordinate. The certificate checks65536 character-homomorphism products, all128allowedFrobenius matricesmod32, all4096commutingpairs,49152finiteframeconjugator exclusions and1024cocycle identities. The j1728 polynomial factorization identifieslambda=-1,2,1/2, allgoodat3, so no separateCMhypothesis remains. The same finite quotient excludes every local ordinary point and cusp. All ordinary good-reduction parameters lie in the residue disc t=lambda+z, z in3Z3. The actual scheme Spec Z3[[z]][1/3] has trivial geometric pro-two group by finite normalization, tame constant base change, purity, and the henselian local equivalence, so their point classes coincide. Potentially multiplicative ordinary points and cusp packets have quadratic Tate traces: ramified twists give inertia trace minus2 versus2, and unramified twists give Frobenius trace plus/minus4 versus0, already modulo32. These are exact finite point/cusp exclusions.

At bad three, put e=-v3(j)/2 and N=5+v2(e). The actual inverse nome is q3=3^(2e)u with u in1+3Z3, which has unique compatible two-power roots. The two actual tame Galois matrices, after cancelling the scalar quadratic twist, are U(2e) and diag(3,1). A commuting matrix modulo2^N has off-diagonal entries divisible2^(N-1) and diagonal difference divisible16, so is scalar modulo16 in every integral basis. The H2 conditions leave I or9I=c^2, hence zero abelian image. Thus the finite quotient (H2 mod2^N) fibre_(Z8)^2 (Z16)^2, of order2^(3N-2), distinguishes the four relative-sign classes. This last finite claim is only separation of these four classes; fullJ still gives the uniform exclusion of every local point/cusp source. The certificate verifies the bound for e=1..256 and3072 allowed linear centralizer residues.

### Additional main-A7 routes checked during this cycle

The fixed finite-S abelian closure route was compared with Harari–Voloch through root's opened source: their Conjecture2 remains the missing equality with rationalS-unit points, so it was not imported as a theorem. A search for “Chabauty--Kim and the Section Conjecture for locally geometric sections” found Betts–Kumpitsch–Luedtke, arXiv2305.09462, whose abstract gives a Kim-conjectural general implication and an unconditional Z[1/2]case; it did not supply a general finite-S recognition theorem. Searches for Serre–Tate local moduli found Katz's primary authorPDF https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf and its Theorem2.1 description, but no unproved deformation-to-full-section inference was used. The actual new full-H progress in this cycle is A102's bad-place-compatible quotient and cross-prime47 obstruction, followed by A104's exact simultaneous-fibre calculation.


## A.108 independent audit: exact harmonic Jacobian descent

The saved proof `work/sections/harmonic_jacobian_descent.tex` passed full independent audit. The etale degree-sixteen cover C4→D has pullback kernel the character line bundles generated by the four rational branch divisor differences, with group (Z/4)^2. The automorphism a:W→iW fixes these classes; its differential eigenvalues -1,i,i give degree16 for1-a. Hence the exact kernel equality supplies the closed immersion j with pi*=j(1-a), and complex conjugation gives bar(j)=-ja. The elliptic factor h=j q* is Q-defined. The degree-four etale map C2→E has precisely the full two-torsion translation kernel, giving the exact pointed isomorphism psi and h=(psi r)* by cancellation in Hom.

The uniform Galois sign calculation gives the negative-triple quaternion exactly as h applied to the quadratic twist cocycle g↦iQ on the nontrivial coset of Q(i). The source cocycle is trivial precisely for elliptic norms, by N(iS)=Q when bar(S)-S=iQ. The rational two-torsion pushforwards are actual coboundaries of -jLi. The explicit [1+i] division formula retains the possible (0,0) correction, which these branch primitives kill; both signs of rational-square x-coordinates therefore give zero after the actual Jacobian pushforward. The basepoint direction is killed by the displayed quartic norm. No injectivity on H1 is asserted.

The source norm quartic was independently expanded and its local source obstructions were retained in `work/code/harmonic_norm_source_certificate.py` and `_output.txt`. Sources (d,Q)=(138,(162,1080)), (154,(350,5880)), (210,(-90,1800)), and (210,(490,9800)) are all non-norms at2: the quartic has no integral solution modulo16, and negative m-valuation gives normalized unit7 modulo8. Additional odd obstructions occur modulo3^3,7^3,3^3,7^3 respectively. The exact soluble points at their other nonsplit bad primes are also retained. These source obstructions do not survive as a claim about the C4 pullback.

## A.111: universal dyadic harmonic quartic evaluation

The complete proof is `work/sections/harmonic_dyadic_norm.tex`; local-preprint independently audited it and passed all cases. The exact certificate/output are `work/code/harmonic_dyadic_norm_certificate.py` and `_output.txt`. They check426 actual old fourth-power local points and7009 locally soluble negative-triple sources, giving14018 zero Hilbert-symbol evaluations after both root-sign choices. All four D4 normalization paths and every proof branch occur, including576 nonsquare-first-entry cases. Two explicit remaining cases are R16,T256,c12,f61 and R32,T512,c56,f=-19; in both, v2(2r)=0 is even and the Hilbert symbol is zero.

The theorem is local over Q2: if the three ratios (T-ci)/(R-ci) are fourth powers for ci=0,1,1/2, and r²=-F(c)/F(R), then ((T-c)/(R-c),2r)=0. The actual coordinate maps1-T and1/(2T) preserve the cover and the quaternion: F(1-T)=-F(T), F(1/(2T))=F(T)/(4T^4), r changes by the square(R/c)^2 and the first entry by the fourth powerR/T. These maps put v2R>=1. The exact three valuation congruences and the non-fourth-power unit -1 modulo16 force T into the same residue disc.

For v2R<=3 the negative-square condition prevents c from approaching R closely enough to give a nonsquare normalized first entry; it lies in1+8Z2. When R and c both have valuation>=4, the ratio G(c)/G(R), G=(1-T)(1-2T), has a square root in1+8 which is itself square. This preserves the actual character and reduces to the exact norm X^4+a²=(X²+a)^2-2aX². In the remaining k=v2c=1,2,3 cases, parity forces f into1+4; its only nonsquare case has v2(f-1)=2 and forces v2(2r) even, so the actual unramified extension Q2(sqrt(f))=Q2(sqrt5) has2r in its norm group. The polynomialX²−X−1 identifies the extension; successive F4/F2 traces give every unit norm, and norm valuations are even. This is an unbounded proof, not an inference from the finite certificate.

The odd-place extension was independently derived with local-preprint. At p1mod4 the source extension splits. At p3mod4 with good reduction,1+Frobenius is onto the finite-field norm target, and formal2-division corrects any lift. After rescaling an odd-valuation d to p times a unit, every singular-reduction point is translated into E0 by a rational two-torsion point: x'=-d²/x for vx>=2, or x'=±d+2d²/(x∓d) for vx1. The latter denominator has valuation>=2 by the curve equation. E0 is uniquely2-divisible, since the smooth special cubic is additive and the formal kernel has2 invertible. Thus E(k)/2 is generated by rational E[2], whose pushed cocycles have the exact branch primitives above. Consequently the odd-local pushed cohomology classes vanish. The local agent owns the formal odd-place/all-place consequence; this agent has not inserted active inputs.


## A.114: quadratic-coset detection and the degree-three Belyi source

The complete proof is `work/sections/cubic_belyi_fibre.tex`; root and local-preprint independently audited it and passed every step. The exact certificate/output `work/code/cubic_belyi_fibre_certificate.py` and `_output.txt` passed: all six S3 subgroups,4946 Kummer translation derangements,1342 internal quadratic coset checks,13 exact Gauss-sum squares,16 prime-power unit square quotients and4872 exceptional local-power checks. Parent explicitly authorized the integration script `work/code/integrate_a114.py`; it was run and verified byte-idempotent, then the register builder passed148 statements. No PDF build was run by this agent.

The completed Kummer lemma localizes at every unramified nonsplit prime of a fixed nontrivial quadratic field K_D. For each coefficient ell with K_D outside its primary cyclotomic tower, the actual compositum L K_D of L=Q(mu_m,a^(1/m)) gives a derangement in the nonsplit coset whenever Gal(L/Q(mu_m)) is nontrivial. If K_D is not in L, pair any nonzero translation with its independent quadratic involution. If K_D lies in L but not the cyclotomic base, restriction of the translation subgroup onto its quadratic quotient is surjective, so choose a translation in that coset. Chebotarev contradicts the assumed local root at such primes. The resulting cyclotomic radical is a rational power at odd ell; doubling the2-power exponent gives coherent global signs, and any nonsplit local prime kills the negative sign. Thus the original class has only the at-most-one exceptional primary component left. The actual exceptions are K=Q(i),Q(sqrt2),Q(sqrt(-2)) at2, or Q(sqrt((-1)^((ell-1)/2)ell)) at an odd ell. The explicit classes2^(2e2),2^(4e2),ell^eell show this exception is necessary.

For f(T)=27T²(1-T)/4, the actual source is P1 minus0,1,2/3,-1/3,infinity. The completed coordinate map is A=-27A0²A1/4, B=27A_(2/3)²A_(-1/3)/4. The monic fibre cubic Z³-Z²+4t/27 has discriminant(4/9)²3t(1-t), so its sign class is D=3AB=-3A1A_(-1/3) modulo squares. For any full Selmer tripod section with the displayed ordinary local pair, all its local cubic sheet actions have a fixed letter. Chebotarev excludes three-cycles globally; D nontrivial then makes the image a single transposition subgroup with a unique global fixed sheet. This gives a unique full source-section lift, preserving ordinary local sections and the real point-or-cusp condition through the actual cover and boundary maps.

At nonsplit D primes, that lift's ordinary centre must equal the prescribed T_p. Hence each old Kummer ratio is supported at most at the one exceptional coefficient prime by the coset lemma. If there is no exception, the old tuple is already recovered. With an exception, requiring each frozen T_p to be rational lets A97's own-coefficient theorem at every other physical prime force the same actual centre. A76 then identifies all four old global classes. This proves the exact Selmer-fibre bijection in the named range; D=1 is explicitly excluded, since it leaves three fixed sheets. The remaining main task is to construct an A90-type obstructed completed tuple on this particular four-finite-puncture source; no such tuple has yet been asserted.

## A.118: arbitrary quartic subsets at every odd place

The complete proof is `work/sections/odd_quartic_subset_norm.tex`. Root and local-preprint independently passed the saved proof. The actual norm-reciprocity statement was reopened at the primary author text https://kskedlaya.org/cft/sec_localrecip.html, Theorem 4.1.2; the proof uses only its finite abelian norm isomorphism and the literal restriction from a cyclic quartic extension to its quadratic subfield. The exact certificate and output are `work/code/odd_quartic_subset_certificate.py` and `_output.txt`. They pass five symbolic identities, 2,913 rational x values, 6,661 input quartic classes, 11,440 generated product states and 7,350 actual local-root/Hilbert checks at thirteen odd primes.

For any number of equations w_i^4=x+(1−x)d_i and product d_i=−r², the quaternion (x,2r) vanishes over every odd Q_p and R. At p congruent to one modulo four, each d_i is the literal norm of (w_i−alpha)/(1−alpha), alpha^4=x. Thus (ir)² is a norm from the cyclic quartic field. Its reciprocity image has order at most two and restricts trivially to the quadratic subfield, while (2r)/(ir)=−2i=(1−i)². At p congruent to three modulo four, the exact inversion of all data makes v(x) nonnegative. When v(x) is not divisible by four, the negative-product unit equation forces a square unit and odd number of leading x terms; the valuation equation then forces x square. In the remaining nonsquare case all d_i have valuations divisible by four, hence r has even valuation and 2r is a norm from the unramified quadratic extension. The real assertion follows from positivity.

The old-point map x=(T−c)/(R−c), w_i=eta_i/xi_i and d_i=(c−c_i)/(R−c_i) is exact. Every A96 negative-subset root changes by the square product of the xi_i, and the individual symbols have explicit quadratic norms. Thus all quartic common characters have constant odd and real evaluation on arbitrary old covers. With a rational old base point, global reciprocity reduces the complete A85 finite-character test to its dyadic value. The proof makes no dyadic or completed-initialization assertion. Parent authorized `integrate_a118.py`; integration and the register build were performed, and a rerun was byte-idempotent. No PDF build was run here.

## A.120: finite quartic initialization on the exact cubic source

The complete proof is `work/sections/cubic_source_quartic_initialization.tex`, with exact certificate/output `work/code/cubic_source_quartic_certificate.py` and `_output.txt`. Root and local-preprint independently passed the full proof. The certificate uses actual Q2 fourth-power classes, rather than requiring the local roots to be small rational numbers. It checks 1,118 sampled rational centres in 288 quartic fibres, every one of 2,416 old-point pairs, all fifteen nonempty subset transport identities, and 193,024 Hilbert evaluations from 96,512 local negative-square relations, including both root signs.

Two general local lemmas supply the mechanism. Equal old valuation coordinates force v(T−R) at least four above the largest old distance; a negative-subset relation prevents c from approaching R within two additional powers, so the normalized first entry is square. In a single boundary disc, normalize the boundary to zero and every other old puncture to valuation at most zero. For R,T of depth at least four, subsets omitting zero either have square first entry or cannot have negative-square product. Subsets containing zero have r²=−(c/R)G(c)/G(R). Deep c makes the G quotient have a square root which is itself square, reducing to X^4+a²=(X²+a)²−2aX². The remaining shallow cases have either square first entry or the unramified quadratic norm with even v(2r).

For the four finite punctures 0,1,2/3,−1/3, the six exact valuation rows exclude changes between different residue clusters. A change between 0 and 2/3 would force depths at least five but gives the unit ratio 1/3=11 modulo sixteen at the old puncture one. A change between one and −1/3 requires depths at least six but gives −1/3=5 modulo sixteen at zero. Both contradict fourth powers. A distinct-depth pair in one finite row is four powers deeper than its nearest neighbour, so the affine coefficient map reaches the general boundary-disc lemma. At infinity, u=1/T sends the four root coordinates to Y0=1/X0 and Y_(1/b)=Xb/X0, with the explicit inverse retained. For an old subset of size j, its transformed negative-square root is r D0^(−ceil(j/2)); the remaining character correction is the individual zero symbol (f,D0). This proves every dyadic negative-subset evaluation on the actual A114 source.

A118 handles all other places and A96 supplies every common quartic character. The exact A85 criterion therefore initializes one new rational coefficient at exponent four for every rational old base and every new rational puncture, preserving any finite set of prescribed ordinary old local points. The c=R fibre has a rational root tuple and is handled separately. This result concerns the same five-punctured source as the cubic Belyi comparison; it does not construct a completed tuple or a compatible higher-exponent lift. Parent authorized `integrate_a120.py`; integration and the register build were performed, and the script is byte-idempotent. The register then had 154 statements, of which 136 were Proved, 13 Refuted, one Known and four Open.

## A.121 independent audit

The complete saved proof `work/sections/eighth_common_field.tex` passed independent review. The parity-constrained actual lifts give the literal root-stabilizer equations. If i is absent from the individual quadratic field, the coset with cyclotomic parity three generates its full stabilizer kernel. If i is present but square root two is absent from B4, the u=5 modulo eight slice is exactly the quartic solution subgroup, and its coset products generate the same field. When mu8 lies in B4, the remaining equations are the exact Z/4 image condition for the valuation matrix. Its annihilator gives all positive fourth-power relation characters and all negative characters chi16+chi_r. The direct product-root maps verify every field inclusion, and both degree-sixteen examples have the claimed full fields. This audit makes no extra local-evaluation claim beyond the authored theorem.


## A125 and A128, 16 November 2026, 08:57 UTC

A125 is integrated after A124 and before A126, with root and local-preprint audits passing. Its retained certificate checks 2,900 odd local entries, 1,548 active norm/field cases, 10,940 generated finite states, 17,616 mixed character evaluations at twelve odd primes, 2,800 old dyadic pairs, and 2,568 actual common-field evaluations. The prime-three cross-disc example is retained. This is finite exponent-eight initialization on the actual cubic Belyi source.

A128 is saved for independent audit in `work/sections/arbitrary_twist_local_constancy.tex`. It proves all odd-place common-character local constancy for arbitrary rational old punctures and coefficients at every exponent divisible by four. The new induction uses A126's full relation list, with an explicit local-square correction of each global relation root. The same constancy at two follows for harmonic and cubic source punctures by exact coefficient/affine/inverse-root maps and the dyadic depth induction.

For every common character the actual cyclic class `(T-c,chi)` extends to the proper curve: all finite residues vanish by the boundary-factor maps, and the pole order at infinity is exactly N. Its choice-independent global sum beta defines gamma in Gal(B_N/K), where K is the individual squareclass field; individual classes are explicitly global constants. A85 gives initialization if and only if gamma is trivial. A128 does not assert that gamma vanishes for arbitrary twists, and does not assert that finite vanishing supplies compatible new coefficients. Actual compatible coefficient power maps give restriction-compatible gamma elements for completed old data.

The A128 certificate passed 91 symbolic identities; 9,484 actual odd local equations; 282,786 literal d_i computations; 606,450 generated finite power-class states; 40,408 mixed-character evaluations (23,438 positive and 16,970 negative); and 3,006 exact Frobenius-order checks for n=4 through128 at thirteen odd primes. Dyadic checks passed 312 depth cases, 1,632 positive-sign implications, twelve literal power images and eight signed cyclotomic norm kernels. Code and full output are retained under `work/code/arbitrary_twist_constancy_certificate*`.

Primary source reopened for A128: Colliot-Thelene--Skorobogatov, author version 31 October2019, https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf. Corollary3.7.3 gives the unramified Brauer exact sequence; Proposition9.5.2 gives local continuity, including the real case; Proposition12.3.1(iii) gives uniform finite support for proper Brauer evaluation; Theorem12.1.8 supplies reciprocity. Existing bibliography key AgentCTSkoro2019 is used; parent bibliography was not mutated.

## A134: an executed harmonic twist with nonzero global obstruction

The complete proof is work/sections/harmonic_twist_completed_obstruction.tex.
Root and local-preprint independently passed its saved source, including the
signed first refinement, and reran the exact finite certificate. The search,
repair, retained rational local points, and independent standard-library
certificate are under work/code/harmonic_square_twist_search*,
harmonic_twist_repair_search*, harmonic_twist_repair_data.json and
harmonic_twist_repair_certificate*. Local-preprint independently checked
all root-symbol inputs in harmonic_root_symbol_independent_audit*.

The exact constants are R=529/382, c=-338/191, q=139, r=1119169,
s=qr=155564491, and (a0,a1,ah)=(529/382,147/382,(13s)^2/191).
On T-i=ai Xi^4 for i=0,1,1/2, the proper Brauer class is
(T-c,d), d=7*17s=18512174429. Its invariant is1/2 at two and zero
everywhere else. This is an actual nonzero A128 global sum.
All611 finite rational centres are retained: every prime at most4500
and the extra repair prime r. The independent certificate checks1833
literal local fourth-power conditions. Beyond4500, the connected
genus33 cover has64 old boundary points, and the exact Weil bound
supplies a smooth ordinary residue point. If a lift initially has
T=c, varying T in its unramified residue disc avoids c.
The exact support is {2,3,7,13,17,23,139,191,1119169}.

The fibre at c has common field Q(i,sqrt6,sqrt299,sqrt d), of degree16.
The product root z=Z0Z1Zh satisfies z^4=-rho^2, rho=34/(7s);
(7s/2)(1-z^2/rho)z is an explicit square root of d in every factor.
The nonzero global character gives the actual A85 obstruction.

The infinite completed old triple is also proved. At two choose
fourth roots congruent to (5,3,5) modulo8. The two coordinate-zero
boundary symbols are both1/2, and every other root symbol is zero.
Choose the real coordinate-zero root negative and the others positive;
its two real symbols cancel the dyadic values in the global sums.
The signed first refinement chooses u<0 with u/X0,p arbitrarily
deep principal at controlled finite places. Subtracting reciprocity
for d0=-prod(p^v_p(X0,p)) makes its unit CRT class fix the actual
common boundary field B0. The finite stabilizer-word construction
supplies u=d0 times positive fresh primes. The map X0=uY0^2 makes
the new root positive at infinity and a principal square at controlled
finite places. The other two coordinates already have pointwise-zero
symbols. The later A90 mixed refinements retain the exact T-values,
use the actual maps Xi=uYi^m, and have cofinal exponents4m!.
The resulting completed old triple has infinite support in all
coordinates and cannot admit a new completed coordinate at c,
already at the squareclass level. Effective least-choice conventions
are stated; only the finite input, not the infinite recursion, was
executed.

## A132/A133 independent audits

Both saved sources fixed_local_completion_image.tex and
harmonic_escaping_support.tex passed full independent audit.
A132 proves all-place finite Kummer injectivity from ordinary
rational valuations and the dyadic sign exclusion. Thus all-place
finite representatives of the same fixed tuple are unique and
automatically compatible.

A133 constructs completed harmonic old data at R=1/4 with every
finite A85 obstruction zero, while the new coordinate at c=2 has
valuation one at infinitely many fresh primes. Its actual stages
freeze T_p=2+p there, preserve the old root-symbol invariant and
avoid T=-1 as well. The restricted-product condition fails at
exponent two. The genus bound includes both extra fibres2,-1.
All maps and finite-point/all-place scopes passed audit.

## Exact class17 for A137's actual quotient

The proof fragment harmonic_quotient_class_fragment.tex was passed
to root for integration. Root, local-preprint and birational
independently passed the construction and certificate.
All bases and literal provenance are retained in
work/code/harmonic_quotient_class_data.json.
The index128 deck group is P=(C4^2) semidirect C8, with the C8
generator swapping the two C4 coordinates. The exact graph has128
vertices,256 directed edges and129 independent cycles.
Its path-chain kernel is H^2[H,H], giving quotient order2^136.
Lower-central dimensions from weight4 through18 are
124,121,115,107,97,85,71,55,41,29,19,11,5,2,0.
Starting with [[[X,Y],X],X] and bracketing successively with
XXYXYXYYYYYYY gives all128 X-edges at weight17.
Thus the actual map is Pi/Gamma18→Q, with exact class17.
Local independently proved I^17=0 in the actual augmentation
module and derived the path-chain weight bound directly.
An independent196606-letter walk gave the same nonzero cycle.

## A139: a metabelian quotient of order4096

The source harmonic_cyclic_finite_obstruction.tex has passed the
full local-preprint audit and certificate rerun; root is auditing.
Its certificate and output are work/code/harmonic_cyclic_detector_certificate*;
detailed data are harmonic_cyclic_detector_data.json.

The actual map W=X0X1Xh sends the old cover to D:W^4=F(T)/a,
a=a0a1ah. Its degree-eight map to the tripod is
W^8=t^2(1-t)/(64a^2), with inverse T=1/2-4aW^4/t.
It is geometrically cyclic, genus3, with four boundary points.
The same class (T-c,d) is proper on D: at c,
(1-W^2/rho)W is sqrt(2rho), d/(2rho) is a rational square,
and the infinity pole order is four.

For a local sheet over x_p, the only T-values are T_p and1-T_p;
the latter exists exactly when-1 is a local fourth power.
At two it is impossible. Outside the explicit support S, every
D-point has zero evaluation by the exact valuation/root-field
argument. Within S the only flips are17 and r: the first entries
have square residues9 and8 at17, and the same square residue
867/382 at r. Every allowed local sheet therefore has invariant
1/2 at two and zero elsewhere.

The index-eight subgroup H_D is the kernel of
2kappa(t)+kappa(1-t) modulo8. The explicit Nielsen basis
u=xy^-2, v=y gives Schreier basis u_j=v^juv^-j (j=0..7), z=v^8.
The quotient by H_D^2[H_D,H_D] is exactly (C2)^8 semidirect C16,
where v cyclically shifts the eight lamps. Its lower-central series
is tau^(k-1)F2[tau]/tau^8, so its exact class is eight.
Since Pi' lies in H_D, it is an actual metabelian quotient.

The A134/A137 pair satisfies [A^2B]_8=[64a^2], forcing the
degree-eight cover lift. The nonsplit central-extension descent
from A137 then gives a rational Brauer class with impossible local
sum1/2. This excludes a locally matching section already in the
4096-element quotient, and hence in the full metabelian quotient.
The certificate checks all611 input centres and flips, all4096
graph-group elements, explicit semidirect normal forms and8192
generator products, and the nonzero all-eight-X-edge commutator
at weight8.
# A143 and A146: positive-rank elliptic factor and primary classes

The actual quotient Dbar -> E -> F is saved in
sections/harmonic_elliptic_positive_rank.tex.  Here E is
y^2=x^3-1146^2 x and F is v^2=u^3+573^2 u.  The literal
degree-two maps, inverse field equations, dual isogenies, and four
boundary fibres are proved.  An elementary two-isogeny descent gives
rank exactly two on both curves, using the independent points
(2028,75348) and (5202,365976) on E.  The opened Tunnell original
Theorem 1 and Theorem 3 give L(E,1)=L(F,1)=0 from the exhaustively
computed signed coefficient b(573)=0; no exact positive analytic rank
or Tate--Shafarevich assertion is made.

The finite-primary exclusion applies to every non-torsion element of
the completed Mordell--Weil group of F, not only scalar multiples,
when its coefficient support is finite.  Surjectivity of E(Q)->F(Q)
and the exact full two-primary group at p=3 mod 8 handle coefficient
two without a coprimality omission.  A143 source, literal finite
certificate, and scanned-primary formula all passed the independent
local_preprint audit.

A146, sections/harmonic_infinite_primary_obstruction.tex, strengthens
this by using boundary reduction rather than an exact local cusp.
For an odd-prime set S with counting function O(X^delta), delta<1/2,
every non-torsion completed F-class whose odd components outside S
are divisible by their coefficient primes has no full Selmer lift to
D^circ.  This includes sparse infinite support and the full-support
scalar z_2=1, z_ell=ell for all odd ell.  The exact positive-density
set is p=3 mod 8, no ell in S dividing p+1, and no ell outside S
with ell^2 dividing p+1.  Its Euler product and uniform tails are
proved using the opened Montgomery--Vaughan original Theorem 2,
equation (1.10), printed p.121, and explicit integer-divisor tails.

The integral comparison is the explicit smooth projective quartic
aW^4=T(T-Z)(T-Z/2)Z over Z with a finite prime set inverted.
Its map to F has exactly the four marked boundary sections above
O_F and (0,0)_F in every good geometric fibre, all with multiplicity
two.  The physical p-primary formal component need not vanish; its
reduction does vanish because p does not divide p+1.  Positive-density
nonintegrality then contradicts AP-D25 in the Selmer range unless the
full section is globally cuspidal, which would give a torsion compact
class.  Every comparison map and this exact scope are retained.

A146 certificate passed 161280 literal CRT residues in eight mixed
patterns, 5776 actual quartic points in 47 good special fibres, and
111648 full elliptic finite-group points at 82 detecting primes.
The full saved-source audit and independent rerun by local_preprint
passed, with no correction, on 2026-11-16 at about 10:24 UTC.

The full primary classification in A10 remains open.  In particular,
this density criterion does not exclude profinite units multiplying a
fixed non-torsion rational point: such a scalar preserves its finite
reduction order, and the rational point reduces into the fixed
elliptic boundary only at finitely many primes.  The next direct
test is the actual cyclic-four D->F image on such unit multiples,
retaining both the proper integral map and all local constraints.

