# No injective extension of the prescribed center basis change

Cycle30. Ordinary, unfilled, actual regional group. Every checkpoint29 source remains unchanged. This strengthens the fixed-family obstruction from cycle29; it does not assert any compact conclusion or any collapse in an ambient filled group.

## 1. Actual graph and complete orbit marking

Use B141's actual regional retraction kernel N_reg=A(Sigma), its auxiliary retained section T_h=F(h,a,d,e,V), and the actual subgroup

    L=<h,k,a,d,e,V | [h^2,k], [k,a], [k,d], [k,e], [k,V]>.

Here V=f^{-1}Bf, h=fk, and the retained free section is the auxiliary h-section, not a newly asserted section compatible with the other source operator. The center vertices form the entire coset set T_h/Q_0, where

    Q_0=<h^2,a,d,e,V>,     X_{gQ_0}=gkg^{-1}.

There are four complete family orbits under T_h. Choose alpha_1, beta_0, delta_1, epsilon_1 as representatives, all adjacent to k=X_{Q_0}. The complete stabilizers, read from every row of B141's link table and its h-shift, are

    Q_alpha=<hah^{-1}, h^2 Vh^{-2}, hdh^{-1}, heh^{-1}>,
    Q_beta =<a, hVh^{-1}, hdh^{-1}, heh^{-1}>,
    Q_delta=Q_epsilon=h<a,d,e,V>h^{-1}.

A center gQ_0 and a family coset tQ_j are joined precisely when their cosets have a common representative. This accounts for all family vertices, including every h-translate and every retained-word translate. It is not a test on finitely many selected family rows. No two center vertices are adjacent, and no two family vertices are adjacent.

For clarity, the four stabilizers follow directly from the retained links of the chosen representatives. Alpha_1 has retained links a_1,B_1,d_1,e_1; beta_0 has a_0,B_0,d_1,e_1; delta_1 and epsilon_1 have a_1,d_1,e_1,B_0. Since B=hVh^{-1}, these are exactly the displayed subgroups. A family stabilizer has h-height zero, because h changes its index. The center has period two, producing the generator h^2 in Q_0.

## 2. The marked center line and a complementary neighbor

Retain the exact words from the cycle29 center proof:

    D=d e d^{-1},
    W=a h V h^{-1} a^{-1} h D h^{-1} d^{-1},
    r=W h W^{-1},
    Y_0=X_{WQ_0},  Y_1=X_{WhQ_0},
    Z_n=X_{r^nQ_0} (n in Z),
    q=Y_1^{-1}r.

The entire free-center basis change sends Z_n to u_n=q^n kq^{-n}=nu_n Z_n nu_n^{-1}, and fixes every center outside this pivot family; nu_n is a word only in Y_0,Y_1. In particular

    Z_1 -> Y_1^{-1} Z_1 Y_1.

Put l=hah^{-1} and X=X_{r l Q_0}. Because l belongs to Q_alpha, Q_delta and Q_epsilon, the families

    lambda_alpha=r(alpha_1),
    lambda_delta=r(delta_1),
    lambda_epsilon=r(epsilon_1)

are all adjacent to both Z_1 and X.

The center X is outside EVERY pivot coset. Equality r l Q_0=r^nQ_0 would imply r^{1-n}l in Q_0. For n=1, l=hah^{-1} exits the exact two-vertex Q_0 core at its a-letter after the first h. For n!=1,

    r^{1-n}l=W h^{1-n}W^{-1}h a h^{-1}

is reduced across the three displayed junctions: W ends in d^{-1}, W^{-1} begins in d and ends in a^{-1}, and l starts in h. Its initial segment a h V exits that same core at V. Thus the word is outside Q_0 for every nonzero 1-n, with no bounded exponent test. Consequently the prescribed center basis change fixes X.

## 3. The entire common link

Let E=ker(T_h -> Z/2), where h has value1 and the other four generators have value0. Its exact Schreier free basis is

    H=h^2,
    a_0=a, a_1=hah^{-1},
    d_0=d, d_1=hdh^{-1},
    e_0=e, e_1=heh^{-1},
    V_0=V, V_1=hVh^{-1}.

Thus E=Q_0*P, where

    Q_0=F(H,a_0,d_0,e_0,V_0),
    P=F(a_1,d_1,e_1,V_1).

In these factors the three distinct stabilizer types are

    Q_alpha=<H V_0 H^{-1}> * F(a_1,d_1,e_1),
    Q_beta =<a_0> * F(V_1,d_1,e_1),
    Q_delta=Q_epsilon=P.

Every common family neighbor of Q_0 and lQ_0 can be represented by gQ_j with g in Q_0. The second adjacency is equivalent to

    g^{-1}a_1 in Q_j Q_0.

Reduced Q_0*P normal forms now classify ALL solutions. For alpha, the a_1 syllable belongs to its P factor, and the Q_0 syllable g^{-1} must belong to <H V_0 H^{-1}>. Every such g lies in Q_alpha, hence gives the single identity coset Q_alpha. For beta, its P factor omits the free letter a_1, so there is no solution. For delta and epsilon, the Q_0 factor is trivial, forcing g=1. Therefore

    link(Q_0) intersect link(lQ_0)
       ={alpha_1,delta_1,epsilon_1}.

This argument includes all h^{2n}-translates: they are among the allowed representatives g in Q_0. Odd-height representatives cannot be adjacent to Q_0 in the first place, since all four Q_j have even h-height.

None of these three vertices is adjacent to Y_0=WQ_0. For alpha, adjacency would require W in Q_alpha Q_0. The V_1 exponent is zero on both factors of that product, whereas the complete word

    W=a_0 V_1 a_0^{-1}(d_1e_1d_1^{-1})d_0^{-1}

has V_1 exponent1. For delta and epsilon, adjacency would require W in P Q_0. Its displayed reduced Q_0*P normal form has five nontrivial alternating syllables, so this is impossible. Translating all vertices by r proves

    link(X) intersect link(Z_1)
       ={lambda_alpha,lambda_delta,lambda_epsilon},
    link(X) intersect link(Z_1) intersect link(Y_1)=empty.

An alternative verification of just the last equality avoids classification: W is outside Q_0 Q_alpha Q_0 by the same exponent, and outside Q_0 P Q_0 by its five syllables; the remaining beta type cannot also meet lQ_0 because its entire Q_0 Q_beta Q_0 double coset has a_1 exponent zero. Both arguments retain every coset.

## 4. The full centralizer intersection, not just a coordinate quotient

For any graph group A(Sigma) and three distinct pairwise nonadjacent vertices x,z,y,

    C(x) intersect y^{-1} C(z)y
      =A(link(x) intersect link(z) intersect link(y)).

Here is the ordinary normal-form proof, valid also for this countable graph. Delete y and put G_0=A(Sigma minus {y}). The whole graph group is the HNN extension of G_0 with stable letter y centralizing the embedded coordinate subgroup A(link(y)). Coordinate subgroups embed by their retractions and their defining graph presentations. The vertex centralizer C(x)=A(star(x)) and C(z)=A(star(z)) lie in G_0 because x,z are nonadjacent to y. If y^{-1}v y lies in G_0 for v in C(z), Britton's lemma forces v in A(link(y)); the stable letters then cancel by the defining commutations. Intersecting the three coordinate subgroups leaves precisely the displayed triple-link subgroup. The vertex-centralizer and coordinate-intersection statements follow from the ordinary graph reduced-word normal form; no completed graph-group theorem is used.

Apply this with x=X,z=Z_1,y=Y_1. The previous section therefore proves the full equality

    C_N_reg(X) intersect C_N_reg(Y_1^{-1}Z_1Y_1)=1.

This strengthens the earlier four-vertex quotient argument: there is no unexamined complementary family element in this full intersection.

## 5. Exact no-injective-extension conclusion

Let Phi:N_reg -> N_reg be any endomorphism whose restriction to the entire center free subgroup is the prescribed center basis change. It need not preserve any family name, family conjugacy class, family abelianization, or family subgroup. For each of the three actual common neighbors lambda_j, both [X,lambda_j]=1 and [Z_1,lambda_j]=1 hold before filling. Therefore Phi(lambda_j) must centralize both X and Y_1^{-1}Z_1Y_1. The full intersection just computed is trivial, so

    Phi(lambda_alpha)=Phi(lambda_delta)=Phi(lambda_epsilon)=1.

Each lambda_j is a nontrivial coordinate graph generator. Consequently no such Phi can be injective, and in particular there is NO automorphism or compatible basis extension with this prescribed center restriction, even if arbitrary family relabeling or mixing is allowed.

Noninjective extensions DO exist: delete every family generator, apply the free-center automorphism, and include the center subgroup again. Thus the conclusion is deliberately not a claim that every homomorphic extension is impossible.

The free-center substitution remains a legitimate Tietze generator change in the complete presentation. Its family-edge relations must all be rewritten. This result does not show that an actual family generator dies after either ambient filling, does not establish any restriction-kernel or fixed-source equality, and makes no compact assertion. A different center normalization is also not excluded.

## 6. Review provenance before writing

During the checkpoint29 writer pause, parent and A independently checked the entire argument in conversation, with no files or computations changed. A checked all-exponent coset exclusion, the complete four-family stabilizer table against B141, the Q_0*P classification, and the infinite-graph HNN/Britton intersection. Parent independently derived both the double-coset triple-link proof and the exact three-element common-link classification. Both explicitly approved the distinction between no injective extension and the existing family-deletion noninjective extension. These reviews will be bound separately to this saved cycle30 source; no execution of a new producer is claimed.
