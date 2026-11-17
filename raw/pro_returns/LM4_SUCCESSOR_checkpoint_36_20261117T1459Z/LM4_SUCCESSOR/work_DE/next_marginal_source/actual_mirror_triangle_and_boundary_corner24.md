# The actual mirror triangle and the isolated full-boundary corner

DE, checkpoint24. Complete discrete algebraic comparison. Every injection and centralizer below is asserted in its explicitly named auxiliary group; none is transferred through the remaining relations of the actual annular quotient.

## 1. The exact marked mirror presentation

Let R be the actual regional B112 group, K the actual common free neck, and c=a C a^{-1} the selected upper-gap cone. Let k be the actual far/base loop. The exact mirror is eta on K, and its external based involution is j. B114 and the independently certified mirror marking give the presentation

 X = < R,j | j²=1, j x j=eta(x) (x in a basis of K), [j c j,k]=1 >.

This is the mirror extension of the actual two-region annular group. The second cross relation is the j-conjugate of the displayed one; it has not been dropped. All regional relators remain in R.

The subgroup S=<c,k> is an actual embedded C2*Z in R. This follows from the regional split quotient and [a,k]=1: S=a<C,k>a^{-1}, and the split quotient is injective on it. Also S intersect K=1, by the previously proved full regional edge-avoidance result.

## 2. The original exact triangle and its short alternating relations

The presentation can be viewed as the colimit of three groups

  R,  J=K semidirect_eta C2(j),
  W=<S,j | j²=1,[j c j,k]=1>.

Their edges are K, S, and C2(j); the face group is trivial. Set D=j c j, so c=j D j. Then

  W=(C2(D) times Z(k)) * C2(j).

In particular S embeds in W: a reduced word in k and c expands, after replacing c by jDj, to a reduced free-product word. The first nonidentity factor lies either in <k> inside the first vertex group, or begins j followed by D. No cancellation erases such a reduced word. The C2(j) edge is also embedded. The two other corner embeddings are the actual K,S embeddings in R and the defining K,C2 embeddings in J.

There are exact minimal cyclically reduced alternating relation lengths 4,4,8 at R,J,W, respectively.

At J, the relation j x j eta(x)^{-1} has length4 for any nonidentity x in K. Since K and C2(j) intersect trivially, no length2 relation occurs.

At R, put t=a f a^{-1}. It belongs to K and normalizes S by the inner element c k^{-1}. Hence for nonidentity s in S,

  t s t^{-1} ((c k^{-1})s(c k^{-1})^{-1})^{-1}=1

is a nontrivial alternating length4 relation in K*S. The trivial K/S intersection excludes length2.

At W, the subgroup jSj=<D,j k j> has trivial intersection with S. To see this directly, expand both reduced subgroup normal forms in the free product A*C2(j), A=C2(D) times Z(k). A nonidentity S word begins with an A-syllable k^n, n nonzero, or with j followed by D. A nonidentity jSj word begins with D, or with j followed by k^n. These first A-syllables cannot agree, since <k> intersect <D>=1 in A. Thus no length4 alternating S/j relation exists. A relation involving an odd number of j letters is excluded by the homomorphism W->C2 sending S to0 and j to1. This also excludes cyclically reduced alternating length2 and6. The displayed cross commutator has length8, so8 is minimal.

The corresponding numerical corner angles 2pi/length are pi/2, pi/2, pi/4, with sum5pi/4. This calculation does not prove either developability or nondevelopability. In particular no sufficient criterion requiring angle sum at most pi can be invoked from these data.

## 3. The actual full boundary and the exact regrouping

Let P=P5=O1...O5. The literal ordinary-cut table gives

  P=a B f d_R e_R,

where d_R,e_R are the original regional deleted generators (distinct from the reflected cone D below). Put T=cP. Using B=CbC, f=C z k^{-1}, z=C h and the actual generic commutations,

  T=a b z d_R e_R k^{-1},   [k,T]=1.

This is also the actual full orbifold-disk boundary, preserved by the far braid. It is not the branch normalizer t=a f a^{-1}.

Define D=j c j and u=T D. Then

  T=uD,  c=jDj,  P=j D j u D.

The complete prefix mirror relation jPj=P^{-1} is exactly equivalent to juj=u^{-1}. At the relator level,

  (jPj)P = D (j u j u) D.

Also [k,T]=1 together with the actual cross relation [k,D]=1 is equivalent to [k,u]=[k,D]=1. The exact free-word identity is

  [k,uD]=[k,u] u[k,D]u^{-1}.

All these equalities are independently checked by check_boundary_corner24.py, using the actual eta(P5)=P5^{-1} dictionary and the two involution relations only.

## 4. The isolated boundary corner is a proper cyclic amalgam

Keep precisely these relations for the moment. The resulting group is

  C_corner = <D,u,k,j | D²=j²=1, [k,D]=[k,u]=1, juj=u^{-1}>
           = A *_<u> B,

  A=(C2(D)*Z(u)) times Z(k),
  B=Z(u) semidirect C2(j), with j acting by inversion.

Both copies of <u> are infinite cyclic and visibly embedded. Thus this is an ordinary proper amalgam with its usual reduced-word normal form. There is a canonical homomorphism from this corner to the actual mirror group, defined by the indicated words. Its injectivity after the OTHER regional and four remaining prefix mirror relations is not established here.

The kernel of the j-parity character of C_corner is the index-two amalgam

  A *_<u> jAj,

where the outer copy identifies its u with u^{-1}. Equivalently it is the graph product on the path

  D -- k -- u -- k' -- c,

with k'=j k j, c=j D j, endpoint vertex groups C2(D), C2(c), and all three interior vertex groups infinite cyclic. Explicitly its only relations, besides D²=c²=1, are

  [D,k]=[k,u]=[u,k']=[k',c]=1.

This follows either by the two-sheet graph-of-groups covering or direct Reidemeister-Schreier rewriting. It is a graph product with two order-two vertices, not an assertion that the fine actual annular group is a right-angled Artin group.

## 5. Exact discrete corner centralizers and a common-subgroup gate

In the Bass-Serre tree of A *_<u> B, k fixes the A vertex and no incident edge: every conjugate of <u> inside A has k-coordinate zero. If k fixed another vertex it would fix the path and hence an incident edge. Thus its fixed vertex is unique, and every centralizer element lies in A. Since k is central in A,

  C_C_corner(k)=A.

The involution D also fixes only that A vertex, because each edge stabilizer is torsion-free. Its centralizer is therefore its centralizer in A, namely <D> times Z(k), by the free-product normal form in C2(D)*Z(u). Conjugating by j gives

  C_C_corner(c)=<c> times <k'>.

These are exact DISCRETE corner statements; no additional profinite amalgam theorem is asserted.

There is also a useful precise common subgroup. In A, T=uD has infinite order, and <k,T> is Z². It meets <u> trivially: a nonzero power of uD has a D syllable, while the k-coordinate detects any nonzero k power. The subgroup <c> in jAj also meets <u> trivially. Amalgam normal form therefore proves

  <c,k,T> in C_corner is C2(c) * Z²(k,T).

Whether this same marked subgroup injects with that presentation in R is a separate actual regional comparison. Its common quotient R after filling all deleted families is smaller, so the coarse quotient alone cannot certify that injection.

## 6. Remaining relations are substantive even after coarse filling

The corner is not yet the whole coarse retained bundle. In the coarse filling P=f and the two generic source/cone relations become

  [c,P k]=1,   [D,P^{-1}k']=1.

With P=c u D these are respectively

  [c,u D k]=1,   [D,u^{-1}c k']=1.

Neither is a consequence of the isolated path graph product. These next maps are maps of the embedded j-even subgroup: for the first, kill D,k,k' and retain c,u; its image is [c,u] in C2(c)*Z(u), nontrivial, while the second relator dies. For the second, kill c,k,k' and retain D,u; its image is [D,u^{-1}] in C2(D)*Z(u), nontrivial, while the first dies. Thus both are nontrivial in the entire corner, and each survives after killing the other inside the j-even subgroup. In the ENTIRE mirror corner they are j-conjugate, so they form one mirror orbit, not two independent normal generators there. This distinction matches the two actual annular equations and their one folded orbit.

Before coarse filling, their actual source/fiber corrections and all other regional relations must be retained in A's full transformed presentation. No auxiliary centralizer or graph-product normal form can be passed through those additions without a new proof.

## 7. Why merely adjoining the branch normalizer is insufficient

The regional subgroup P_reg=<S,t> is a(C2(C)*Z(k) times Z(z))a^{-1}. Its projection to the split coarse group is injective, and K intersect P_reg=<t>; the same statement holds for actual compact images, by the primitive branch coordinate and the retractions. Meanwhile eta(t) is not in <t>: both are conjugates of primitive branch meridians, their branch exponents are opposite, but the literal words eta(t) and t^{-1} differ. The independent certificate also checks their nonzero free commutator.

Thus adjoining the original branch normalizer to the S corner does not automatically supply its mirror mate. An enlarged edge carrying both t and j would also carry jtj=eta(t), which is outside the original regional P_reg intersection with K. A further simultaneous enlargement/comparison would be needed. The full-boundary regrouping above is useful precisely because it records another exact compatibility relation without pretending this normalizer problem has disappeared.

All main source/centralizer decisions remain Open.
