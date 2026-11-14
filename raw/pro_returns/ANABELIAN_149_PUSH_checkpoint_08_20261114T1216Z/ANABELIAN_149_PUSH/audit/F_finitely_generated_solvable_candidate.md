# Reconstruction over subfields of finitely generated extensions of Qsolv

Status: independently reviewed and approved by root and the finite-field agent; integrated as F.33–F.37 in sections/F.tex and its result ledger. The constant-case finite-extension clarification and original Jannsen Theorem 4.3(ii) numbering are included. The earlier checkpoint04 freeze has ended.

Throughout, k=Qsolv inside a chosen algebraic closure of Q. The claim is that every subfield of a finitely generated extension of k satisfies closed-point-preserving étale reconstruction. This enlarges F.31 and contains the corrected LM5-F.50 field class. It does not give a necessary condition or settle the intrinsic classification in F.9.

## Lemma A. Divisibility kernel, algebraic constants and finite models

For every finitely generated field extension L/k,

    D(L*) = intersection_n (L*)^n = k*.

Indeed, let k' be the algebraic closure of k in L. It is finite over k (Stacks Lemma 9.26.11). Choose a normal projective model Z of L over k; normalization of a projective model is finite in characteristic zero. Its global regular functions form k': normality and properness identify them with the algebraic constants. If a in L* is divisible by every positive integer, its valuation at each prime divisor of Z is divisible by every positive integer, hence zero. Normality implies that a and its inverse are global regular functions, so a belongs to k'*. Moreover every root z in L of z^n=a has zero prime-divisor valuations and thus belongs to k'*. Therefore a belongs to D(k'*)=k* by F.16. Conversely k* is divisible. This argument applies to every finite extension of L, since it too is finitely generated over k.

There are algebraic numbers outside L. Otherwise Qbar would lie in k', which is finite over k, contradicting F.18's unbounded finite extensions of k. Thus one can choose a finite Galois number field N/Q not contained in L.

Any finite collection of schemes, morphisms, points and coefficients over L descends to a finitely generated field F/Q inside L with L=Fk: start with generators for L/k, adjoin the finitely many coefficients, and include the finitely many algebraic constants from k needed for all defining relations. The extension L/F is algebraic Galois and prosolvable. It is a scalar extension of k/Q; its automorphisms restrict to a closed subgroup of the prosolvable group Gal(k/Q). In particular the finite quotient of L/F appearing as the intersection with any finite Galois extension of F is solvable.

## Lemma B. Finite arithmetic quotient detection

F.24 remains valid when L/k is finitely generated rather than finite. Thus for every smooth separated geometrically connected curve U/L and every finite quotient G of pi1(U), there are closed points of arbitrarily large degrees whose entire arithmetic decomposition groups surject onto G. Consequently F.29 remains valid for every smooth geometrically connected quasiprojective variety over such L.

Here are all changes in the proof, including the arithmetic predicates. Descend the curve, completion, connected G-torsor, full action and torsor identity to a finitely generated F/Q with L=Fk. The algebraic constant field M/F of the descended G-cover is finite Galois; write N=Gal(cover/M), P=Gal(M/F). Connectedness after the original base change implies M intersect L=F. The degree-n pencil over F is constructed by the same length-at-most-four jet evaluation and incidence counts as in F.24. All fields involved embed in C, so the same SGA1 comparison and topological branch-loop proof yield the common-constant wreath embedding

    H subset (G x_P ... x_P G) semidirect S_n

and show that H^infinity contains literal A_n and that H^infinity intersect N^n projects onto every coordinate N. This proof uses neither the number-field hypothesis nor a claim of unrestricted wreath monodromy. In particular possible additional constants of the Galois closure remain harmless.

The field F is Hilbertian. To see the precise deduction from the opened Serre source, Q is Hilbertian by Theorem 3.4.1, including its affine-space formulation. A rational-function field Q(t_1,...,t_d) is Hilbertian: clear denominators in a finite family of monic irreducible polynomials over Q(t)(T), and apply Hilbert irreducibility over Q with the variables t and T simultaneously. A specialization irreducible over Q at one t-value makes the corresponding polynomial at that T-value irreducible over Q(t), since a monic factorization over the integrally closed localized polynomial ring would specialize to a factorization. Nonzero denominator conditions are included in the avoided closed sets. Finally F is finite over such a rational-function field, and Serre Corollary 3.2.2 preserves Hilbertianity under finite extension.

Hence Serre Proposition 3.3.1 specializes the Galois closure with full group H over F. Put J=Gal(Omega L/L). The prosolvability of L/F gives H^infinity subset J. The equality M intersect L=F gives J -> P surjective. For a coordinate i, literal A_n corrects the block image of an element of J with any prescribed P-image, and the support-at-most-two commutators supply the full kernel N in that coordinate. Therefore J intersect Stab(i) surjects onto G. Literal A_n also makes the degree-n fibre a single closed point. The permissible n are unbounded, as in F.24. No perfectness of P or J is assumed.

For a higher-dimensional source, the Poonen–Slavov hyperplane slicing argument of F.29 is unchanged: apply it to every geometric component of the prescribed finite connected cover; each map to the ambient projective space is quasi-finite, so its nonempty fibres have dimension zero. Choose rational hyperplanes over the infinite field L in the simultaneous good open. The geometric components remain irreducible and the arithmetic Galois action remains transitive. The resulting smooth curve retains the entire finite quotient, and the curve case detects it.

## Lemma C. Gauss valuations and fixed-model integrality on punctured lines

Let L/k be finitely generated, U a nonempty open of Gm_L, and xi in lim_n H1(U,mu_n). Suppose every evaluation at a point over every finite extension E/L is the compatible Kummer class of an actual b_x in E*. Then xi is the class of an actual regular unit h on U, and b_x/h(x) belongs to k*.

As in F.18, write P_0=T and P_1,...,P_r for the other monic irreducible puncture polynomials. The localized polynomial ring is a PID, so its Picard group vanishes and its units modulo L* have basis P_j. Choose x_0 in U(L), take its actual value b_0, and write

    xi = kappa(b_0) + sum_j lambda_j ([P_j(T)]-[P_j(x_0)]),
    lambda_j in Zhat.

Choose F0/Q finitely generated inside L, with L=F0 k, containing every coefficient of every P_j and x_0,b_0. Let t_1,...,t_d be a transcendence basis of F0/Q; hence F0/Q(t) is finite. Choose a finite Galois number field N/Q not contained in L, as in Lemma A. In one algebraic closure of F0, take a finite Galois extension M/Q(t) containing F0, N and all roots of every P_j. This is possible by taking a finite Galois closure of their compositum.

The extension Mk/L is finite Galois, and LN/L is a nontrivial Galois subextension. Choose sigma in Gal(Mk/L) acting nontrivially on N. Since M/Q(t) is normal and Q(t) subset F0 subset L, sigma preserves M. It fixes k and all coefficients of the P_j. Let C=M intersect Qbar. This is a finite Galois number field: a Q-embedding of C extends while fixing the transcendental t-variables, and normality of M/Q(t) preserves M and hence C. The restriction sigma|C is nontrivial because N subset C.

If d=0, M is a number field and F.18's completely split prime argument applies verbatim. Suppose d>0. We construct the needed valuations in detail. Choose one root r_i of each P_i. A finite étale model of M/C(t) exists over

    A = O_C[S^(-1)][t_1,...,t_d,1/f]

for some finite set S of rational primes and nonzero f in Z[t_1,...,t_d]. To construct it, use a primitive element for M/C(t), clear its polynomial denominators, and invert its nonzero discriminant. Its monogenic algebra is then finite étale and normal. Further invert the norms of the finitely many nonzero elements whose inverses are required. Taking products of the conjugate denominators under Gal(C/Q), and enlarging S, allows f to have rational, then integral, coefficients. The resulting normal finite étale algebra B is the integral closure of A in M and is stable under sigma. It can be chosen so that all P_j coefficients and all their roots are integral in B, and every nonzero derivative P_i'(r_i) and cross-value P_j(r_i), j distinct from i, is a unit. Separability and distinctness of the puncture polynomials make those elements nonzero.

There are infinitely many rational primes splitting completely in C, by the elementary polynomial-value proof given in F.18. Exclude S and the finitely many primes for which f becomes the zero polynomial. For each remaining p and every prime pfrak of C above p, the ideal pfrak A is a height-one prime. Its local ring is the Gauss DVR of C(t) extending that place of C, with uniformizer p and residue field F_p(t_1,...,t_d). Choose a height-one prime of B over it. The corresponding DVR v of M is unramified over the Gauss DVR because B/A is étale; hence v(p)=1. Its residue field is a finite separable extension of F_p(t), and in particular is infinite. The listed units and integral elements have the required valuations there.

Choose pairwise distinct such rational primes p_i and prolongations v_i. Complete splitting in C and sigma|C nontrivial imply v_i != sigma^(-1)v_i: their restrictions to C are different primes, since a nonidentity automorphism cannot fix a prime above a completely split rational prime. Distinct i give different rational residue characteristics, so all these pairs of valuations are disjoint.

Localize B at the complement of the union of these finitely many height-one primes. This is a normal noetherian one-dimensional semilocal ring, hence a semilocal Dedekind ring R, with precisely the selected DVRs as its local rings. Its distinct maximal ideals are comaximal. The Chinese remainder theorem therefore supplies alpha in R satisfying

    alpha = r_i+p_i modulo p_{v_i}^2,
    alpha = c_i modulo p_{sigma^(-1)v_i},

where c_i avoids every root of every reduced P_j. Such c_i exist because these residue fields are infinite. In the number-field case d=0, choose p_i greater than the sum of the degrees, as in F.18. Integrality and the derivative/cross-value units give

    v_i(P_j(alpha)) = delta_ij,
    v_i(P_j(sigma alpha)) = v_{sigma^(-1)v_i}(P_j(alpha)) = 0.

The second equality uses that sigma fixes every polynomial coefficient; it does not assume that sigma fixes individual roots. In particular alpha lies in U(Mk). For R_j=P_j(sigma alpha)/P_j(alpha) we have v_i(R_j)=-delta_ij.

Let b_alpha in Mk realize the actual value at this point. Choose a finite number field S0 subset k containing all the finitely many constants needed to express b_alpha using M, and put F=M S0. This F is finitely generated over Q and is fixed before any radical level is chosen. It is sigma-stable, since sigma fixes k and preserves M.

The radical descent of F.16 works over this F without change. If z in Mk satisfies z^n=a in F*, then for tau in Gal(Mk/F), the ratio tau(z)/z is in mu_n subset k. The automorphisms tau and sigma commute: check their compositions on the generating subfields M and k; tau fixes M, sigma preserves M, sigma fixes k and tau preserves k. Thus

    tau(sigma(z)/z) = sigma(z)/z.

The extension Mk/F is Galois, being obtained from k/S0 by scalar extension; its fixed field is F. Therefore sigma(z)/z belongs to F, and sigma(a)/a belongs to (F*)^n. No number-field restriction has entered this argument.

Take integers a_{j,n} representing lambda_j modulo n. Applying the descent calculation to

    (b_alpha/b_0) product_j (P_j(alpha)/P_j(x_0))^(-a_{j,n}) = z_n^n

gives

    (sigma b_alpha/b_alpha) product_j R_j^(-a_{j,n}) in (F*)^n.

For h_i=v_i composed with N_{F/M}, h_i(R_j)=-[F:M]delta_ij. Hence

    [F:M] lambda_i = -h_i(sigma b_alpha/b_alpha) in Z

inside Zhat. The elementary equality Q intersect Zhat=Z proves every lambda_i is an ordinary integer. Thus xi=kappa(h) for

    h(T)=b_0 product_j (P_j(T)/P_j(x_0))^(lambda_j).

The residual point ratio belongs to D(E*)=k* by Lemma A. This completes the actual-unit assertion.

## Lemma D. Point-theoretic classes on all curves and smooth affine sources

The proofs F.26–F.30 extend to every finitely generated L/k. We give all arithmetic changes rather than citing an unspecified stability assertion.

First take a smooth geometrically connected pointed curve U/L. Split the finitely many boundary points by finite constants and descend U, its completion, boundary, point and generalized Jacobian A to a finitely generated F/Q with L=Fk. Set H=G_L, normal in G_F, and W=(V_l A)_H. The cyclotomic character is trivial on H because mu_infinity subset k. Point Kummer homomorphisms into the coinvariant lattice span W: otherwise a nonzero normalized integral functional gives a finite quotient of pi1(U) killed by every closed-point decomposition group, contrary to Lemma B. Choose finitely many point images spanning W.

For the finitely many chosen points, their coordinates and the actual multiplicative Kummer values lie in one finite extension M/F after first adjoining the finite number of constants from k needed to write their algebraic equations. Put L'=Mk. Restricting to the finite-index subgroup G_L' does not change the rational spans of the Kummer images. Conjugating by G_M gives the same two identities as F.26, for every chosen point i:

    c_i(ghg^(-1))=g c_i(h),
    kappa(beta_i/b_0)(ghg^(-1))=chi(g) kappa(beta_i/b_0)(h).

It follows that the functional attached to the point-theoretic class is G_M-equivariant on all V_l A, not merely on G_L coinvariants.

The needed integral Tate-Hom theorem is available over precisely this finitely generated M/Q. Jossen, On the Mumford–Tate conjecture for 1-motives, §1.4 p.6, explicitly states

    Hom_M(M1,M2) tensor Z_l = Hom_{G_M}(T_l M1,T_l M2)

for 1-motives over any field finitely generated over its prime field. We apply it only to [0->A] and [0->Gm]. The original primary statement has also been opened: Jannsen, Mixed Motives, Motivic Cohomology, and Ext-Groups, ICM1994 proceedings (published 1995), Theorem 4.3(ii), printed p.676. It explicitly gives this integral isomorphism over a finitely generated field. The displayed proof reduces by Ext sequences to the abelian Tate theorem and the Mordell–Weil injection for the dual abelian variety. Jossen cites it as Theorem 4.6, but the opened original has numbering 4.3(ii). This is the additional primary input; the 2009 dissertation alone was only used over number fields and is not silently enlarged.

After splitting the boundary and normalizing at the rational point, the geometric unit lattice is fixed over F: divisors are fixed, and evaluation 1 removes the scalar ambiguity. Therefore the same integral conclusion as F.26 holds, xi=kappa(b_0)+sum lambda_j kappa(u_j) in one fixed unit basis. The Picard Tate component of this particular class vanishes; the whole Picard Tate module need not vanish.

For each boundary component of a curve, the Riemann–Roch finite map with one simple zero and no other boundary zero from F.27 remains available. Norm the restricted class to a punctured rational line. Actual point values are preserved by field norms. Lemma C proves its residue is an ordinary integer. Norm residues use residue degrees, not ramification indices, and the selected simple rational boundary point contributes degree one. The integral divisor matrix then forces every lambda_j in Z. This gives an actual unit on every curve.

For higher-dimensional smooth pointed affine X, use the same generalized Albanese and the integral comparison of Spieß–Szamuely Propositions 4.1–4.3 as F.30. Its assumptions concern smooth quasiprojective geometry and a smooth projective compactification, available in characteristic zero, and do not require L algebraic over Q. Lemma B replaces F.29 in the spanning step. The finite-data G_M-equivariance argument and the just-stated finitely generated-field Tate-Hom theorem again give a completed normalized unit lattice. Transverse complete-intersection curves at smooth boundary points make every residue integral by the curve assertion; the same divisor matrix proves the class is an actual unit h. Normalize h(x_0)=the actual value at x_0.

## Lemma E. Algebraic point functions and the full reconstruction theorem

For a pinned curve morphism phi:U_et->Gm_et, Lemma D gives an actual unit h and ratios phi(x)/h(x) in k*. The proof F.28 works word for word over finitely generated L/k, with Lemma A supplying the kernel and Lemma B supplying closed points of arbitrarily high degrees. In detail, if h is constant, pass to a finite extension of L containing beta with beta/h not in k; such an element exists because finite extensions of k have unbounded degrees. All previous lemmas hold after this finite extension. The point values avoid beta, so pull back T-beta on the whole source; the eventual unique point-function unit descends to the original L. Its actual unit must be constant, since a nonconstant rational function cannot take values in L at closed points of degrees exceeding its degree. Comparing the two constant classes forces the point function constant. If h is nonconstant, pulling back T-1 gives a second actual unit h_1. A point of degree greater than the fixed total pole degree forces the identity c_x h-d_x h_1-1=0, with c_x,d_x in k*. Thus h_1=A h+B, A,B in k*, and high-degree values determine the single scalar c=-A/B. For every b in k*, the same argument with T-b yields h_b=e_b(ch-b). The zeros force phi(x)=ch(x) also at points where h(x) is in k. The inverse images of these omitted points are closed; nonconstant point maps make the needed opens nonempty. Finite-quotient detection kills a residual Kummer class with zero values at every closed point, as in F.28.

For a smooth affine pointed X of higher dimension, Lemma D supplies the normalized actual unit h. Given a geometric point x, pass to finite constants making x rational and use a smooth geometrically connected curve through x and x_0. The curve's algebraic point-function unit and h on that curve have equal Kummer class; their ratio has zero divisor on its proper completion, hence is constant. Its value at x_0 is 1, so equality holds at x. This proves that every geometric point value of phi equals h(x). This is exactly CHW Theorem 4.18(5), hence yields the full all-scheme reconstruction theorem over every finitely generated L/k. It does not infer full-topos equality directly from this one point calculation.

Finally let k0 be any subfield of a finitely generated extension L/k. The compositum k0 k is an intermediate field between k and L and is finitely generated over k. Here is the precise elementary justification: choose a finite transcendence basis t of k0 k/k; the field k0 k is algebraic over k(t), and lies in L. By Stacks Lemma 9.26.11 the algebraic closure of k(t) in the finitely generated extension L/k(t) is finite, so k0 k/k(t) is finite. The extension k0 k/k0 is algebraic. Apply the algebraic-descent theorem F.32 to conclude reconstruction over k0.

This positive field range contains every subfield of a finitely generated extension of Qab: form its compositum with Qsolv in an algebraic closure, which is a finitely generated extension of Qsolv, and apply the just-proved subfield result. No necessary-and-sufficient intrinsic arithmetic classification follows.

## Sources actually opened

- Serre (2007), Topics in Galois Theory, Corollary 3.2.2 p.22, Proposition 3.3.1 p.23, Theorem 3.4.1 p.25. Reopened primary CNRS-hosted PDF. These prove the exact Hilbert specialization predicates; the rational-function extension argument is supplied above.
- Jossen, On the Mumford–Tate conjecture for 1-motives, arXiv:1107.5259v2, §1.4 p.6. Opened both the author PDF https://jossenpeter.ch/PdfDvi/MTConj.pdf and https://arxiv.org/pdf/1107.5259. The displayed integral Tate-Hom statement explicitly assumes a field finitely generated over its prime field.
- The Stacks Project, §9.26, Lemma 9.26.11, https://stacks.math.columbia.edu/tag/030D, opened: finiteness of the algebraic constant field in a finitely generated field extension. It is used twice, with the exact base field identified each time.
- Jannsen (1995), Mixed Motives, Motivic Cohomology, and Ext-Groups, in Proceedings of the ICM1994, pp.667–679, Theorem 4.3(ii) p.676. Official IMU volume https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1994.1/ICM1994.1.ocr.pdf downloaded; actual relevant pages extracted to tmp/F_Jannsen_ICM1994_excerpt.pdf and .txt. The web reader rejected the 80 MB volume as too large; direct download and local text opening succeeded. Jossen's reference to Theorem4.6 is recorded as a numbering mismatch rather than repeated.
- SGA1, Spieß–Szamuely, Poonen–Slavov, and CHW are the previously opened primary sources specified in F.24–F.31; their relevant hypotheses are rechecked above. No unpublished claim about the full wreath monodromy, arbitrary-field Tate-Hom, or transcendental small-topos base change is used.
