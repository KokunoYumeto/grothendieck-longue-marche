# Actual extreme derivations after A.25

This is a working proof record for the remaining fixed-subgroup problem. The arithmetic occurrence of the two extreme derivations is justified below. The all-degree common-kernel assertion is still open in this return; finite ranks are not a proof of it.

**Subsequent resolution of the arithmetic D3 problem:** A.27, in sections/A_D3_fixed_all.tex, proves the full odd-prime fixed-subgroup assertion using the full separating monodromy and one actual CM Frobenius conjugate. Its all-degree prefix normal form handles the arbitrary based correction lambda ad(Omega). The separate two-extreme-derivation kernel assertion below remains unproved and is not used as an input to A.27.

## Normal arithmetic span

Given an open subgroup Delta0 of Delta, choose a finite number field L/K so that Delta intersect G_L is contained in Delta0 and all maps, cusps, and CM isogenies are defined over L. It is enough to use the smaller normal group Gamma=closure([G_L,G_L]). The actual cusp-packet action of Gamma is IA on the rank-four free pro-l group of D minus its cusp. Its ordinary first Johnson degree is zero by hyperelliptic equivariance. Thus its ordinary degree-two Johnson image is an additive subgroup of special derivations. Its rational span is stable under conjugation by the actual packet image of G_L, because Gamma is normal.

The action on that graded derivation space depends only on the action on H1. After splitting the CM field in the coefficient field, H1 has the characters psi and psi-bar, each twice. An ordinary Frobenius at a split good prime, taken to a suitable positive residue power, has eigenvalues alpha and alpha-bar with disjoint prime-ideal support. They are multiplicatively independent. Its cyclic Zariski closure is therefore the full two-dimensional CM torus. In particular the actual degree-two span is stable under the character projectors. One can alternatively write these projectors as polynomials in a Frobenius on this finite-dimensional space; the ratio of its two eigenvalues has infinite order.

At the place above two of A.25, the local commutator [Frob,tame] lies in Gamma and has nonzero separating monodromy, with scalar (q-1)m. Thus the proper outer degree-two image contains a nonzero multiple of the separating derivation T1 described below.

## Exact comparison of the global CM and local component decompositions

Let the stable components E1,E2 have map degrees 1,2 to the good reduction of the original E, as proved in A.25. Choose a symplectic basis a,b,c,d of their rational homology such that

    f_* a = x,  f_* b = y,  f_* c = x,  f_* d = 2y.

Here x,y is a symplectic CM eigenbasis on E, after the coefficient extension. The degree-two isogeny has symplectic similitude factor two, so this normalization is compatible with the component polarizations.

Adjointness gives f^*x=a+2c and f^*y=b+d. The global original elliptic subspace is therefore spanned by a+2c,b+d; its complementary elliptic subspace, ker f_*, is spanned by a-c,2b-d.

The automorphism rho(t,z)=(-t,-iz) satisfies f rho=[-i] f. The original elliptic differential is dt/z and has rho eigenvalue -i. The complementary differential t dt/z has eigenvalue +i, so rho acts by [i] on the complementary elliptic factor. The component degrees are different, hence rho preserves each component. The two maps f_i intertwine its action with [-i] on the target.

Consequently a global CM symplectic eigenbasis is

    p1 = a+2c,           p2 = (2b-d)/3,
    q1 = (b+d)/3,        q2 = c-a.

The p's have character psi, the q's have character psi-bar, and

    Omega=[a,b]+[c,d]=[p1,q1]+[p2,q2].

The inverse formulas are a=(p1-2q2)/3, c=(p1+q2)/3, b=p2+q1, d=2q1-p2. All formulas are rational; division by three is legitimate even when l=3 because this is a rational graded obstruction, not a proposed integral change of generators.

## Extreme projections and the based ambiguity

Let T1 act by ad([a,b]) on a,b and by zero on c,d. Let T2 act by ad([c,d]) on c,d and by zero on a,b. In the proper surface Lie algebra, T1 and T2 have the same outer class. Direct expansion in the displayed CM basis gives the SAME extreme projections for each:

    weight psi^3 / psi-bar:      (1/9) Dplus,
    weight psi-bar^3 / psi:      (-4/9) Dminus,

where

    Dplus(p1)=Dplus(p2)=0,
    Dplus(q1)=[[p1,p2],p2],
    Dplus(q2)=-[[p1,p2],p1],

and

    Dminus(q1)=Dminus(q2)=0,
    Dminus(p1)=[[q1,q2],q2],
    Dminus(p2)=-[[q1,q2],q1].

Both derivations kill Omega.

There is no silent identification of outer and based derivations here. Every degree-two inner derivation is ad(w) with w in L2(V), whose possible CM characters are psi^2, psi psi-bar, and psi-bar^2. Neither extreme character occurs.

There is also no silent identification of proper and punctured derivations. The kernel of the degree-two map from derivations of the free Lie algebra to derivations of the proper surface Lie algebra has generator values in

    (Omega)_3 = [Omega,V].

It is therefore a submodule of Hom(V, chi V)=End(V) tensor chi, where chi=psi psi-bar. This again has only psi^2, psi psi-bar, and psi-bar^2. Thus the two extreme components lift uniquely from the proper outer derivation to the actual based punctured derivation. Packet changes add a multiple of ad(Omega), of the middle character chi, and do not change either extreme.

It follows that the rational degree-two span of the ACTUAL Gamma action contains both Dplus and Dminus, up to nonzero scalars. No unknown arithmetic coefficient has been assigned.

## Remaining all-degree algebra

The desired statement is

    ker(Dplus) intersect ker(Dminus) = Q_l Omega

in the free Lie algebra on p1,p2,q1,q2. If proved, the first nonzero class of a fixed actual pro-l element is an integral multiple of Omega, by primitivity. Subtracting the corresponding actual cusp power then excludes every remainder and gives the full fixed subgroup I.

Code a_D3_extreme_graded.py checks degrees 1 through 6. In the free Lie algebra its joint kernel dimensions are 0,1,0,0,0,0; in the proper surface Lie quotient they are 0,0,0,0,0,0. Free dimensions are 4,6,20,60,204,670; proper dimensions are 4,5,16,45,144,440. The proper associative reduction uses the one non-overlapping rule p1 q1 = q1 p1 - p2 q2 + q2 p2.

Each individual derivation has many constants; for instance [q1,Dplus(q1)] is killed by Dplus. Thus the incorrect simplification ker Dplus = Lie(p1,p2,Omega) must not be used.
