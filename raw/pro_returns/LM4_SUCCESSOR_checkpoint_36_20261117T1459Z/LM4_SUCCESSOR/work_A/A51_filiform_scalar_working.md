# A genuine second scalar layer over an odd filiform head

Status: the parent and CE independently reviewed the exact proof and certificate; incorporated as formal A.51. This is a concrete failure of immediate scalar stabilization, not a norm obstruction and not a counterexample to the full involution question.

Let Pi=C2 amalg C3, let R be the pronilpotent residual of the congruence kernel as in A.31–A.34, and put C=Pi/R. All commutator subgroups below are closed. The same initial base is used; no claim of compatibility with all previously enlarged bases is needed for this obstruction.

## 1. An actual odd nilpotent head

Work over F7. On A=F7^4 with coordinates (y,z,w,t), put D(y,z,w,t)=(0,y,z,w), E(x)=exp(xD), and

    N = A semidirect C7,
    (x,v)(u,w)=(x+u,v+E(x)w).

The C6 generator acts on x by3 and on A by B=diag(5,1,3,2). Since BDB^{-1}=3D this is an honest action. Put H=N:C6. The coordinate convention is A(v)X^x followed by the C6 element. Thus |H|=6*7^5=100842. Take s=(0,0,0,0,0,3), r0=(0,0,0,0,0,2), n=(1,1,0,0,0,0), and r=n r0 n^{-1}=(6,4,4,5,3,2).

The pair has orders2,3 and generates H. Indeed its image in N/[N,N]=F7^2 has nonzero components in both distinct C6 characters3 and5. A complement cannot contain pure s and this r: fixing the s-translation forces the conjugating vector to vanish, whereas the r-translation is nonzero in both components. Consequently the generated subgroup meets N in a subgroup surjecting its Frattini quotient, hence in N itself. The exact certificate independently enumerates all100842 elements.

The image of K_cong is N, using the same fact as A.49 that a solvable congruence quotient has no7 composition factor and H/N=C6 is congruence. Since N is a7-group, H is a quotient of C. The retained positive h_C acts identically on H. The kernel of this particular head need not be c-stable; this result does not assert an involution on the single head.

## 2. Two irreducible modules and different odd/full coinvariants

Let k=F8 and zeta its specified primitive seventh root. Let ell=(1,0,0,1) on A. On U=k^7, indexed by j in F7, set

    rho_U(x,v)e_j = zeta^{ell E(-(j+x))v} e_{j+x}.

The pure r0 acts by R(e_j a)=e_(2j) a^4. The identity ell B^2=4ell proves compatibility. This is an F2 representation of the odd subgroup J=N:C3.

For the involution s, let U^s be the N-twist by (x,y,z,w,t)->(-x,-y,z,-w,t), with the same r0 action. Put V=U direct-sum U^s and let s swap the two summands. This defines a42-dimensional F2 representation of H. The dual V^vee is obtained by replacing ell with -ell.

Here are elementary proofs of the required representation facts. The central element T acts on U by the scalar zeta. Any F2 endomorphism commuting with it is k-linear. The seven A characters ell E(-j) are distinct, so the A-action gives all diagonal matrix units over k; X cyclically permutes them. Hence U is irreducible over F2 as an N-module and End_N(U)=k. The additional r0 semilinearity reduces its endomorphism field to F2. The s-twist is distinct: the central T character would force any Frobenius multiplier to be1, and the zero W-coordinate forces the X-orbit translation to be0, after which the Y-coefficients1 and-1 differ. Thus V is irreducible over H and End_H(V)=F2; End_J(V)=F2 direct-sum F2. The negative central-character Frobenius orbit is disjoint from the positive orbit, so V and V^vee are distinct and no self-pairing on either exists.

Put Vbar=V direct-sum V^vee. The two trace pairings between matching U/U^vee and U^s/(U^s)^vee summands span all J-invariant alternating forms. The involution s exchanges them. Therefore

    dim_F2 (wedge^2 Vbar)_J = 2,
    dim_F2 (wedge^2 Vbar)_H = 1.

In particular the first space is the free F2[C2] module of rank1, not a trivial two-dimensional module. The exact84-dimensional calculation gives ranks3484 and3485 in the3486-dimensional exterior square.

## 3. Actual affine Pi quotients and H1(C,V)=0

For each sign, the s norm kernel on V has dimension21, the r norm kernel has dimension28, and coboundaries have dimension42. Thus H1(Pi,V) and H1(Pi,V^vee) have dimension7 over F2. Normalize the s-value to0. The r-values recorded by the certificate are, in the first seven-dimensional k block,

    d_+(r)=zeta^3 e_1,
    d_-(r)=e_1,

and0 in the other block. They satisfy the r norm equation and are not coboundaries; the certificate gives the exact matrices and rank21 versus22 test. Here k is F2[a]/(a^3+a+1), zeta=a, so zeta^3 is the integer bit representation3.

Every nonzero cohomology class gives a full affine quotient V:H. Indeed H1(H,V)=0 since its normal odd N has no invariant vectors. By irreducibility, a subgroup mapping onto H is either the whole affine group or a complement; the latter would make the cocycle a coboundary. The same holds for V^vee. Since the two modules are distinct, the paired map has full image G=Vbar:H.

The image of K_cong in G is Vbar:N: its normality and projection onto N force all of Vbar because [Vbar,N]=Vbar. The pronilpotent residual of Vbar:N is precisely Vbar. Hence the image of R is Vbar.

This also proves H1(C,V)=H1(C,V^vee)=0 without a dimension-one assumption. Any nonzero Pi cohomology class gives a full affine quotient by the preceding paragraph and has nonzero restriction to R. Therefore the inflation subspace is0. The same conclusion applies to the dual of Vbar.

Let W=R intersect ker(Pi->G). Then Pi/W=G times_H C, because the joint image contains its entire Vbar kernel over C.

## 4. Two explicit central covers

Let P=P1 times P2 have elements (v,w,t1,t2), v in V, w in V^vee, ti in F2, with multiplication

    (v,w,t)(v',w',t')=(v+v',w+w', t_i+t'_i+B_i(v,w')).

Here B_i is the trace pairing on the i-th matching summand. Each P_i is an extraspecial hyperbolic2-group; all that is needed is the displayed multiplication. The odd J acts on each center trivially, and s swaps the two central coordinates, so H acts honestly on P. Let Z=<z1,z2> be its center and z=z1 z2. Put

    G2=P:H,
    G1=G2/<z>.

The two normalized affine cocycles lift to an actual map Pi->G2. Take S=(0,s), so S^2=1. Choose the central coordinates of the r-lift to cancel its cube; because r has order3, adding that cube in the elementary central group cancels it. The exact certificate gives correction(1,0). Thus Rlift^3=1.

The map onto G=Vbar:H is full. Its intersection with P surjects Vbar, and commutators of that intersection generate both central coordinates, so it contains all of P. Consequently Pi->G2 is surjective. The image of R is P, because it surjects Vbar and its commutators generate Z. The image of W is Z.

Now [Z,H]=<z> is nontrivial and central in G2. Therefore the map to G2 kills [[W,Pi],Pi] but does not kill [W,Pi]. This alone proves a genuine strict inclusion

    [[W,Pi],Pi] < [W,Pi].

It is not merely a permitted module extension: it occurs in an actual quotient generated by order2 and order3 elements with the actual R and W.

## 5. Identification of the first and second actual refinements

Write W1=[W,Pi], W2=[W1,Pi], W3=[W2,Pi]. The finite Pontryagin-duality argument of A.49, using H1(C,Vbar^vee)=0, makes the abelianization of the R-preimage in Pi/W1 equal to Vbar. Its central kernel is consequently a quotient of (wedge^2 Vbar)_H, of dimension at most1. The explicit G1 cover attains it. Hence

    Pi/W1 = G1 times_H C.

For Pi/W2, the same duality argument first gives R-preimage abelianization Vbar. Its preimage of the old center centralizes that R-preimage: the central commutator pairing from the old trivial central module tensor Vbar vanishes, since (Vbar)_C=0. The whole center of the R-preimage is therefore an elementary-abelian wedge quotient. Its action factors through H. The odd J is trivial on its two central subquotients and so on their extension by odd-order semisimplicity. Its dimension is at most2, attained by G2. Thus

    Pi/W2 = G2 times_H C,
    W1/W2 = C2.

For the next refinement, the old center Z is no longer a trivial H-module. Nevertheless N acts trivially on Z and has no invariants on Vbar. The possible central pairing Z tensor Vbar -> W2/W3 therefore vanishes by N-coinvariants. The next center is again a wedge quotient on which J acts trivially, of dimension at most2; the old center already has dimension2. Thus W3=W2. This last argument must be run over all finite quotients retaining G2, as in A.49; it does not assume an infinite central kernel is finite before deriving the bound.

## Scope

The immediate stabilization used in A.43, A.49 and A.50 is not a general consequence of relative perfectness or odd sensitivity of the chief module. This exact example requires two scalar steps. It still supplies no obstruction to the negative norm equation: the chosen head is not itself c-stable, and neither a compatible negative action on its paired characteristic family nor a nontrivial norm class has been asserted. In particular the full parity-one involution and full cofinality questions remain Open.

Certificate: check_filiform7_scalar.py and check_filiform7_scalar.out.
