# Exact compatibility gate for gluing the two regional filling kernels

DE, checkpoint23. Research only. The regional graph-kernel theorem is accepted; a global graph-kernel conclusion is not yet established.

## 1. The regional theorem does not omit translates

A's complete regional presentation is

  R = A(Omega) semidirect ((C2(C)*Z(k)) x Z(z)).

Its coordinate vertices are (g<k>,U,n), U=a,b,d,e. The actual common neck kernel K0=ker(K->Z_f) is the full coordinate subgroup with Schreier basis f^n a f^-n, f^n B f^-n, f^n d f^-n, f^n e f^-n, where B=bar b. All regional coarse-deck and height translates occur. This is a sound starting point.

The ACTUAL global coarse quotient is the retained bundle described in coarse_annular_height_kernel23.md. Its height kernel includes the full free base F2 action on the infinite free product of cone factors. Replacing that base by only the two zero-level loops without their translates would change the problem.

## 2. The literal edge map is not a coordinate graph map

The actual common K map is eta, with the completely marked prefix formula. In the regional free Schreier coordinate system,

  eta(a)=a B a^{-1} B^{-1} a^{-1}.

This is a freely reduced word of length5 in two distinct height-zero coordinate generators. It is not a signed single coordinate vertex. Coarse-deck action in the regional Omega model permutes the coordinate vertices, so it is not repaired merely by relabeling their coarse cosets. The map is a basis-conjugating map of the common free subgroup, not the literal graph map needed by the simplest coordinate-graph amalgamation.

This statement does not say eta cannot extend after a nontrivial change of regional graph basis. Such a change would have to be proved simultaneously compatible with EVERY regional edge and every coarse translate. A separate conjugation of each peripheral or the fact that each word is primitive is insufficient.

## 3. The two regional split sections also disagree on the retained edge

The inner regional split section uses the retained branch f. In local mirrored coordinates the outer split section uses f_+, whose actual common-K image is eta(f). In the filled coarse quotient the branch identification is f_+ -> f^{-1}. The difference is the literal common-kernel word

  d_f=eta(f) f in K0.

The exact eta dictionary shows d_f is freely reduced and nonempty (length18); the full word is retained in regional_graph_gluing_obstruction23.json. Since K injects in both regional vertices and in the prequotient amalgam, this discrepancy is real there. The actual cross quotient may impose further relations, so its survival there is not asserted.

Thus the two existing regional SPLIT extensions cannot simply be glued as though their coarse edge sections already agreed. One needs an actual kernel-valued section correction, compatible with the whole coarse action. A choice correcting the branch alone may change the cone and mapping equations.

## 4. The coarse cross two-cells retain kernel corrections

In the actual group the two cross relations are

  [eta(a) C_+ eta(a)^{-1}, k_-]=1,
  [a C_- a^{-1}, k_+]=1.

After filling the added families they become [C_+,k_-]=[C_-,k_+]=1. The displayed bare cone lifts therefore need not satisfy the coarse relations before filling. This is another section-coherence condition, now at the coarse two-cells.

Using the selected conjugated cones instead makes those two relations literal, but changes the compatible regional branch/source lift: for example a h a^{-1} commutes with a C a^{-1}, and its branch part is a f a^{-1}, not the original f. Consequently the edge and the two-cell corrections must be solved together. They cannot be erased independently.

## 5. Sufficient next comparison and present limit

A genuine graph-kernel proof would need explicit simultaneous data: regional kernel basis changes whose common edge map is coordinate (possibly after signs), compatible coarse-section corrections on the retained edge, and the exact correction around BOTH coarse cross relations. It must then show that the complete coarse-group action preserves the resulting graph presentation and that all translates of all regional relations are accounted for.

Alternatively a non-split graph-of-groups/graph-product construction could retain the cocycle, but its developability and normal-form comparison would have to be proved for these actual based maps. The current regional RAAG presentations, transverse geometry, and coordinate abelianizations do not themselves give that comparison.

No impossibility assertion is made. This note isolates the actual non-coordinate edge word, retained-branch defect and cross-two-cell corrections that a successful construction must handle. It neither asserts a global RAAG nor transfers prequotient nonmembership to the actual annular quotient.

## 6. One exact simultaneous formula for the entire common edge kernel

The actual edge map can nevertheless be written uniformly, without sampling retained heights. Put tau(w)=f w f^{-1}, d_f=eta(f)f, and for every integer n set psi_n=eta(f)^n f^n in K0. Thus psi_0=1 and the ordered recurrence is

  psi_(n+1)=psi_n tau^(-n)(d_f).

For U in {a,B,d,e}, every free Schreier coordinate r_(n,U)=f^n U f^{-n} has the exact image

  eta(r_(n,U))=psi_n tau^(-n)(eta(U)) psi_n^{-1}.

These are literal free-group identities obtained by inserting eta(f)^n=psi_n f^{-n}. The finite actual eta dictionary and d_f therefore specify ALL edge maps, including negative n. For n>0, psi_n is the ordered product of tau^(-j)(d_f), j=0,...,n-1. For n=-m<0 it is the ordered product tau^j(d_f^{-1}), j=1,...,m. No commutations or quotient relations are used. This is a complete simultaneous word map; it is not a coordinate-vertex map.

A Reidemeister-Schreier or graph-of-groups construction can retain this exact nonlinear edge map and its coarse conjugates. The remaining question is whether it admits a compatible graph presentation after the two actual coarse cross two-cells are attached. The formula does not discard their kernel corrections.

## 7. Exact edge-only simplification by the prefix basis

CE identified a useful further exact change, already justified by the actual reflection certificate. Put P_i=O1...Oi. These five words are a free basis of K because O1=P1 and O_i=P_(i-1)^{-1}P_i for i>1. The first four have branch height zero, P5 has height one, and eta(P_i)=P_i^{-1} for all five. Consequently

  { P5^n P_i P5^{-n} : 1<=i<=4, n in Z }

is a free Schreier basis of K0 on which eta is literally the signed permutation (i,n)->(i,-n), with inversion. Thus the common edge itself admits a completely compatible basis and height section P5; the cocycle of Section6 belongs to the original regional f-coordinate choice, not an intrinsic obstruction within K.

What remains is simultaneous EXTENSION of this prefix/height change to each entire regional Omega graph presentation and its complete coarse action, together with the actual two cross cells. The prefix kernel generators are not the original regional coordinate vertices. In the same basis the selected cone coefficients are a=P1^{-1}P2 and eta(a)=P1 P2^{-1}, so the actual cross relations still carry their specified kernel conjugations. No theorem that an arbitrary basis change of the coordinate free subgroup extends to the whole regional graph group is being assumed. This is the sharper current compatibility gate.
