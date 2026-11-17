# The entire mirrored free neck survives the complete first-family filling

Cycle30 addendum to one_sided_family_centralizer_extension30.md (frozen predecessor SHA811fd46c). This is an actual all-retained-word survival and retraction statement before the opposite family is imposed. It does not assert survival through both families or of the larger E1 group.

## 1. Exact setup and the preserved character

Use the proved exact first-family quotient

    V_i=F(disjoint_union_j B_i/S_ji) semidirect B_i,
    B_i=(L_L *_K R_R)/normal(P0,...,P4),

with the four actual family letters lambda_alpha=alpha1, lambda_beta=beta0, lambda_delta=delta1, lambda_epsilon=epsilon1. Its defining presentation is

    <B_i,lambda_j | [lambda_j,S_ji]=1>,
    S_ji=image(<k,Q_j>).

The original retained retraction V->K kills every P_i and therefore gives a well-defined B_i->K. Let chi:B_i->Z be its f-exponent. It has

    chi(h)=1, chi(k)=chi(a)=chi(d)=chi(e)=chi(V)=0.

Every displayed generator of each Q_j has h-height zero, so chi(S_ji)=0 for all four j. This remains true after every first-family ambient conjugate; it is a character of the actual quotient, not an approximate height.

## 2. The complete marked mirrored neck

The full actual map in B141 satisfies

    theta(d(K))=a C K C a^-1=:J_*.

This is equality of based subgroups, since d(u)=p(a C(a^-1 eta(u)a)C a^-1), theta p=id, and a^-1 eta(K)a=K. No independent conjugating choice is made. Use the following five actual generators in V_i:

    z_a=a C a C a^-1=(a h^-1)lambda_alpha(a h^-1)^-1,
    z_B=a C B C a^-1=a lambda_beta a^-1,
    z_d=a C d C a^-1=(a h^-1)lambda_delta(a h^-1)^-1,
    z_e=a C e C a^-1=(a h^-1)lambda_epsilon(a h^-1)^-1,
    g=a C f C a^-1=a k^-1 h a^-1.

The last equality is the exact actual CfC=k^-1h identity from the previous note; it is an identity before filling. In particular g belongs to B_i and chi(g)=1.

## 3. A literal arbitrary-target retraction

Let F5=F(A,B,D,E,G) be an abstract free group. Define a homomorphism from the ACTUAL quotient V_i to F5 by

    b in B_i  -> G^{chi(b)},
    lambda_alpha -> G A G^-1,
    lambda_beta -> B,
    lambda_delta -> G D G^-1,
    lambda_epsilon -> G E G^-1.

Every defining stabilizer subgroup S_ji maps to1, so every [lambda_j,S_ji] relation holds. Thus this is a homomorphism of the complete quotient V_i, with no need to guess a presentation of B_i or truncate its relation closure.

It sends the five complete marked words above to A,B,D,E,G, respectively: the three (a h^-1) conjugators have chi=-1; a has chi0; g has chi1. Conversely the assignment (A,B,D,E,G)->(z_a,z_B,z_d,z_e,g) defines a homomorphism from the free group. Their composite on F5 is the identity. Consequently the actual image of J_* in V_i is a free group on exactly these five generators, the original map on J_* is injective, and composing the two maps gives an actual retraction

    V_i -> J_*.

In particular, for M_i=normal_V(P0,...,P4),

    J_* intersect M_i=1.                                   (1)

Every finite quotient of J_* extends by this actual retraction. Therefore J_* has full induced profinite topology in V_i, its actual closure in hat(V_i) is canonically hat(F5), and the continuous completion of the retraction fixes it. This compact consequence uses a genuine finitely generated free target retraction, not the discontinuous infinite-coordinate projection of B145. No whole completion of the family kernel is used.

## 4. Exact free-factor position inside the ordinary family kernel

For completeness the same survival can be seen in the actual coset basis. Put b_alpha=b_delta=b_epsilon=a h^-1 and b_beta=a. The kernel of J_*-><g> has all the usual free basis letters

    g^n z_j g^-n = X_(g^n b_j S_ji,j),  n in Z.

For each fixed j, these cosets are all distinct: equality for n,n' would give chi(g^{n-n'})=0, since every S_ji has chi0, hence n=n'. Different j belong to different components of the disjoint union. Thus the entire kernel is a coordinate free factor of F(disjoint_union B_i/S_ji), not merely a set of individually primitive words. This includes all positive and negative levels.

## 5. Exact scope of the surviving edge

This proves survival and full topology of the complete actual mirrored free neck theta(d(K)) under the WHOLE first-family normal closure, including all K translates and ambient conjugates. Applying theta gives the corresponding swapped statement for d(K) under the whole opposite-family filling.

It does not prove injectivity of the larger local E1 group containing its extra k generator. It also does not prove that this free neck survives the final quotient by both families: the second family lies partly in its generated free kernel and retains the coupled square word. The exact final carrier restriction (D intersect N_*)/R_cyc and the original fixed-source/icosahedral comparisons remain open.
