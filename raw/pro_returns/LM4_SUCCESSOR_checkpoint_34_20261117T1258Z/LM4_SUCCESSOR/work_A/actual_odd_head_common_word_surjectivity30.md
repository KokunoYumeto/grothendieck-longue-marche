# Actual common words and exact duality at every odd Alexander head

Cycle30 research. This is an exact statement about the same full free profinite source and its three marked cyclic-cover quotients. It is not a construction of a canonical GT0 parameter or a pentagon solution. All previously frozen sources remain unchanged.

## 1. The three actual maps

Let F be the free profinite group on x,y, let z=(xy)^(-1), and let c=[x,y]=xyx^(-1)y^(-1). For an odd positive integer n put A_n=F_2[C_n], write T for its specified generator, and let I_n be its augmentation ideal. Use additive module coordinates followed by the head, with multiplication

    (P,T^a)(Q,T^b)=(P+T^a Q,T^(a+b)).

The universal property of F gives the following three genuine continuous maps to A_n semidirect C_n:

    kappa_x: x -> (1,1),       y -> (0,T);
    kappa_y: x -> (0,T),       y -> (1,1);
    kappa_z: x -> (0,T),       y -> (T^(-1),T^(-1)).

In the last map z goes to (1,1). They are exactly the finite quotients of the x-, y-, and z-cyclic-cover modules, with retained generators y,x,x respectively. Every element of F' has head1 in all three, and its module coordinates lie in I_n. Write pi_n:F'->I_n^3 for those coordinates. The commutator maps to

    pi_n(c)=(1-T, T-1, 1-T^(-1)).                         (1)

All signs in (1) are in characteristic two. For example the third coordinate follows from x=(0,T), y=(T^(-1),T^(-1)) and the affine commutator formula. No independent choice of three source words is made.

## 2. Exact image and explicit interpolation

Let R_n=F_2[C_n x C_n], with generators X,Y recording the original x,y conjugations. Conjugating c by x^a y^b multiplies its three coordinates by T^b,T^a,T^(a-b). Since F' is the closed normal closure of c, and the target coordinates commute, its exact image is

    { ((1-T)P(1,T), (T-1)P(T,1),
                     (1-T^(-1))P(T,T^(-1))): P in R_n }. (2)

For the inclusion from right to left, each monomial of P is realized by the actual corresponding conjugate of c, and their finite product realizes the sum. The reverse inclusion follows from normal generation. The normal-generation assertion itself follows by imposing c=1: the resulting universal two-generated profinite abelian group is the abelianization of F.

For any one of X,Y,XY, let N denote the sum of all n powers. As n is odd, N^2=N and its augmentation is1. In A_n the kernel of multiplication by T-1 is exactly F_2 N_T: comparison of adjacent coefficients proves this directly. Its intersection with I_n is zero, so multiplication by T-1, and also by1-T^(-1), is an automorphism of I_n.

Define the following three explicit elements of R_n:

    E_x=N_X(1-N_Y),
    E_y=N_Y(1-N_X),
    E_z=N_(XY)(1-N_X).

Their respective evaluations on the three lines (X,Y)=(1,T),(T,1),(T,T^(-1)) are

    E_x -> (1-N_T, 0,       0),
    E_y -> (0,       1-N_T, 0),
    E_z -> (0,       0,       1-N_T).                     (3)

For example N_X(T)N_Y(T^(-1))=N_T^2=N_T, and N_(XY) evaluates to1 on the third line because n is odd. On I_n,1-N_T acts as the identity.

Given any (A_x,A_y,A_z) in I_n^3, choose the unique Q_x,Q_y,Q_z in I_n satisfying

    (1-T)Q_x=A_x, (T-1)Q_y=A_y,
    (1-T^(-1))Q_z=A_z.

Then

    P=E_x Q_x(Y)+E_y Q_y(X)+E_z Q_z(X)

has exactly the required coordinates in (2). Consequently

    pi_n(F')=I_n x I_n x I_n                             (4)

for EVERY odd n, including the trivial n=1 case. This is a symbolic all-head proof, not a finite-head test or census.

## 3. Exact swap-duality words realize every permitted pair

Let iota exchange x and y. On the three module coordinates of a word in F' its action is

    (A_x,A_y,A_z) -> (A_y,A_x, T^(-1) bar(A_z)),          (5)

where bar sends T to T^(-1). The third factor is essential: iota(z)=x^(-1)zx, while the retained x-head is inverted. These two actual identities give (5) on the full cyclic-cover module.

Let j(P)=T^(-1)bar(P) on A_n. Its action on the coefficient basis is the involution r -> -r-1 of Z/n. For odd n there is one fixed index, r0=(n-1)/2; every other orbit has size two. Therefore an invariant element of I_n has zero coefficient at that fixed index and is a sum of two-element orbit sums. It is a norm P+j(P). Moreover P can be chosen in I_n: if a first choice has augmentation1, add T^r0, whose norm is zero and whose augmentation is1. Thus

    (1+j)(I_n)=I_n^j.                                    (6)

For any U in I_n and W in I_n with bar(W)=T W, choose P_z in I_n with P_z+j(P_z)=W. By (4) choose an ACTUAL w in F' with pi_n(w)=(U,0,P_z). Put

    u=w iota(w)^(-1).

Then u lies in F', satisfies the exact nonlinear identity iota(u)=u^(-1), and has

    pi_n(u)=(U,U,W).                                    (7)

Finally the first cyclic-cover coordinate of u(y,z) is exactly the third coordinate of u(x,y): kappa_x(y)=(0,T) and kappa_x(z)=(T^(-1),T^(-1)), which are the defining kappa_z images. Hence (7) says, in A89's literal original marking,

    [u(x,y)]_x=U,       [u(y,z)]_x=W,
    bar(W)=T W.                                         (8)

Every U and weighted-invariant W allowed by augmentation and the displayed duality is realized by one exact full-source duality word. The realization has not discarded a conjugator or replaced u(x,y),u(y,z) by unrelated words.

## 4. Simultaneous all-odd-head version

Let A_odd=lim_(n odd) A_n=F_2[[product_(p odd) Z_p]] and I_odd=ker(augmentation). The quotient maps above are compatible as n varies by divisibility. Given any compatible triple in I_odd^3, its finite-coordinate preimages in the compact group F' are nonempty by (4). Any finite collection of coordinates is controlled by their odd least common multiple. These closed preimage sets have the finite-intersection property, so compactness supplies one full w realizing the entire triple.

The same argument applies to (7)--(8), using w as the compact variable and u=w iota(w)^(-1). For every compatible U in I_odd and W in I_odd with bar(W)=T W there is one full duality word u realizing them simultaneously at all odd heads. This argument does not require choosing compatible norm preimages P_z by hand.

## 5. Exact consequence and remaining gate

The common-word constraint across the three original cyclic-cover modules, by itself, adds no further odd-head linear condition: (4) is onto. Even imposing exact swap duality on the source word adds no further condition beyond the already used equality of the first two coordinates and bar(W)=T W, by (7)--(8).

This narrows the limitation recorded in A91. Any additional argument forcing the A89 weighted symmetry of the ACTUAL canonical hexagon class must use information not captured by this common-word/duality realization, such as the actual canonical involution equation, the full marked pentagon, or further nonlinear/relative compatibility. In particular the present u is NOT asserted to equal the canonical parameter of any GT0 involution, to satisfy the pentagon, or to have a prescribed dihedral d. It is not a counterexample to a_reg=d. No arbitrary ring example is substituted for those missing hypotheses.

The exact odd-head coefficient question for an actual full-GT involution remains the A90 condition. The nonlinear Omega or cubic cusp relation also remains open. No prospective modular homomorphism has been used before proving its cubic relation, and no pro-p statement has been transferred to a relative odd-head quotient.
