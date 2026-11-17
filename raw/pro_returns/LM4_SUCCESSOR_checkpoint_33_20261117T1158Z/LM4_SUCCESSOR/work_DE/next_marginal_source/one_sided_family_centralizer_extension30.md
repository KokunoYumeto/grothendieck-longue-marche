# The complete one-sided filling has a free family kernel; the theta family remains coupled

Cycle30 research. Actual ordinary groups and all retained words. This is a larger exact comparison than the cyclic carrier, not a conclusion about the complete two-family quotient or any compact kernel.

## 1. Exact regional centralizer extensions

Use the actual L=<K,k> and auxiliary section T_h of B145:

    L=<h,k,a,d,e,V | [h^2,k],[k,a],[k,d],[k,e],[k,V]>,
    T_h=F(h,a,d,e,V), Q0=<h^2,a,d,e,V>.

Use the four complete family representatives alpha1,beta0,delta1,epsilon1 and their entire stabilizers from B147:

    Qalpha=<hah^-1,h^2 Vh^-2,hdh^-1,heh^-1>,
    Qbeta=<a,hVh^-1,hdh^-1,heh^-1>,
    Qdelta=Qepsilon=h<a,d,e,V>h^-1.

Write lambda_j for the corresponding actual family letter, and S_j=<k,Q_j> as an actual subgroup of L. Then the exact entire regional presentation is

    R0=<L,lambda_alpha,lambda_beta,lambda_delta,lambda_epsilon |
             [lambda_j,s]=1 for every s in S_j>.             (1)

This is a finite presentation over L: it is enough to use k and the four displayed generators of each Q_j. Here is a proof accounting for every graph edge. In B141 the family vertices of type j are exactly T_h/Q_j, so every one is t lambda_j t^-1. The stabilizer equations are precisely [lambda_j,Q_j]=1. All center/family edges arise by translating the representative edge [k,lambda_j]=1 by T_h. The entire neighborhood of lambda_j consists of the Q_j-translates of k, and commuting with k and Q_j implies commuting with that entire neighborhood. Conversely all those translated edge equations and stabilizers occur in the original expanded graph and its T_h action. There are no family/family edges. Eliminating all translated family names in the actual A(Sigma) semidirect T_h presentation therefore gives exactly (1), with inverse substitution lambda_(tQ_j)=t lambda_j t^-1. This proves both presentation maps; it does not infer (1) merely from bipartiteness.

The subgroup S_j itself has the exact embedded description

    S_j=F(X_(qQ0):q in Q_j) semidirect Q_j,

where its center basis is indexed by Q_j/(Q_j intersect Q0). This follows inside the full coset-basis presentation of L. No claim that Q_j commutes with k is made; only the newly adjoined family letter centralizes their generated subgroup.

## 2. Retain the entire opposite region in the base

Put

    V=R_L *_K R_R,
    B=L_L *_K R_R.

The actual color retraction R_L->L_L fixes every element of K, so B embeds in V by ordinary normal form and the induced map rho:V->B is a retraction. Substituting (1) into this actual amalgam gives the complete presentation

    V=<B,lambda_j | [lambda_j,S_j]=1 for all four j>.         (2)

The edge subgroups S_j are the actual left-region subgroups in B. In particular all right families are retained in B; no right-family relation is dropped.

For an arbitrary group B and specified subgroups S_j, the group in (2) is exactly

    F(Omega) semidirect B,   Omega=disjoint_union_j B/S_j.    (3)

The B action is left coset translation. One inverse map sends the free basis letter X_(bS_j,j) to b lambda_j b^-1, which is representative-independent by the stabilizer relations. The other sends B to its section and lambda_j to the root basis letter of its type. They are inverse on every generator. Thus the actual full kernel of rho is free on ALL these cosets, including every retained direction and every right-region word. This is not an abstract completion assertion.

## 3. The entire first-family normal closure is evaluated on this base

Keep the actual five B141 words

    P0=[(gamma k)^2,k],   Pi=[k,x_i] (i=1..4),
    gamma=d(f), x_i=d(V_i), d(K)<=R_R.

All five lie in B. Let

    R_i=normal_B(P0,P1,P2,P3,P4),
    M_i=normal_V(P0,P1,P2,P3,P4),
    B_i=B/R_i, S_ji=image(S_j in B_i).

These are the ENTIRE ordinary normal closures; in particular every K translate is present because K<=B. The presentations (2)--(3) give the exact filled group

    V_i=V/M_i
       =<B_i,lambda_j | [lambda_j,S_ji]=1>
       =F(Omega_i) semidirect B_i,
    Omega_i=disjoint_union_j B_i/S_ji.                       (4)

Both inverse maps are the same coset maps as above, now in the actual quotient B_i. This proves in particular

    M_i intersect B=R_i.                                    (5)

No injectivity of an abstract presentation for an S_ji is assumed: S_ji is its actual image subgroup in B_i. Alternatively (5) follows by the retraction rho, which fixes all five P_i and therefore descends to a retraction V_i->B_i.

More precisely the restriction of M_i to the free family kernel F(Omega) is exactly the kernel of the basis-identification epimorphism

    F(Omega)->F(R_i\Omega)=F(Omega_i).

It is the free-group normal closure of all X_omega X_(r omega)^-1 for r in R_i and omega in Omega. Thus the one-sided filling introduces exactly the induced family-coset identifications and no additional relation in the base quotient. This statement includes every ambient conjugate of the first family; no bounded translate family or partial cyclic orbit is substituted.

The original cyclic carrier D of B146 lies in B. Consequently

    D intersect M_i = D intersect R_i,

so its remaining first-family restriction is an actual all-retained-direction problem entirely inside B. Equation (5) does NOT say R_i restricts on D as R_cyc; the latter is a separate, still unproved intersection.

## 4. The opposite family supplies four free-kernel relators and one coupled base word

Let pi_L:R_L->L_L be the actual color deletion used above. It kills the four opposite family cores, so on the conjugate neck group it satisfies

    pi_L(CaC)=pi_L(CBC)=pi_L(CdC)=pi_L(CeC)=1.

The actual identities [C,h]=1, CkC=hkh^-1 and [h^2,k]=1 give

    pi_L(CfC)=h(CkC)^-1=k^-1h.

For the actual mirror theta and the full marked d-map,

    theta(d(u))=a C(a^-1 eta(u)a) C a^-1.

The reflection eta reverses the f-exponent, while the other four K letters have exponent zero. Therefore the exact color image is

    rho(theta(d(u)))=a(k^-1h)^(-chi_f(u))a^-1.              (6)

In particular rho(theta(x_i))=1 for all four leaves and

    rho(theta(gamma))=A0:=a h^-1 k a^-1.

Write k'=p(k) in the right region. Before passing to B_i the complete opposite-family projections are consequently

    rho(theta(P_i))=1 (i=1..4),
    rho(theta(P0))=[(A0 k')^2,k']=:b0.                     (7)

After the exact quotient (4), decompose each of the five actual theta words uniquely in F(Omega_i) semidirect B_i. They have the forms

    theta(P0)=omega0 * image(b0),
    theta(P_i)=omega_i (i=1..4),                           (8)

where all omega_i are the literal free-kernel rewrites using the full coset map in (4). No claim that omega0 or any leaf omega_i is trivial is made. The complete initial quotient is exactly

    V_*=(F(Omega_i) semidirect B_i) /
         normal(omega0 image(b0),omega1,omega2,omega3,omega4). (9)

All K translates and all ambient conjugations of BOTH original families are contained in this normal closure. Equations (6)--(9) are an exact typed reduction of the full comparison: four opposite relations lie in the actual free kernel, and one remains coupled to an actual base word. They do not give a base section after that last filling.

For the cyclic carrier, its entire extra restriction is still (D intersect N_*)/R_cyc. The preceding construction separates an exact first step, D intersect R_i, from the genuine second-family restriction in (9). It does not replace their sum by pairwise subgroup intersections, does not deduce survival from a local proper amalgam, and does not remove any changed family edge. The nonsplitting obstruction for the whole coarse quotient is compatible with the proper one-sided semidirect description here.

No compact version of (3)--(9) is asserted; the free family kernels are infinite and their ambient induced topology has not been identified with their abstract completions. Every checkpoint29 file and every frozen B145--147 source remains unchanged.
