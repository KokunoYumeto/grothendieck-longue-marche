# Four actual outer contact factors and the inner section centralizer

DE, checkpoint23. Exact complete-vertex calculation, limited to the four prescribed factors. No inference is made about survival after the actual two cross relations.

## 1. Exact centralizer of the geometric section in B112

Use B112's actual unfolded presentation R=A(Gamma_infinity) semidirect (Z_h x C2(c)). Write k=k0 and bar k=k1. The shift h swaps k0,k1, as does c. The two vertices are not adjacent and have distinct images in the free abelianization of the graph group.

For g h^n c^epsilon to centralize k0, its graph conjugation must take k_(n+epsilon mod2) to k0. Abelianization makes this impossible if n+epsilon is odd. If n+epsilon is even, the condition is exactly g in C_A(Gamma)(k0).

The latter centralizer is the star subgroup <k0> x A(link(k0)). Indeed isolate k0 by the actual graph-product amalgam

  A(Gamma) = A(Gamma\{k0}) *_{A(link k0)}
               (A(link k0) x <k0>).

The k0 winding character is zero on every conjugate edge group and nonzero on k0. Thus k0 fixes only the star vertex of its ordinary amalgam tree, and its centralizer lies in that vertex; there it is exactly the entire star group. This proves the assertion without a new graph-group centralizer theorem.

Consequently

  C_R(k0) = (<k0> x A(link k0)) semidirect <hc>.

For ordinary elements the h-height must be even. At height zero, membership is exactly membership of the reduced graph word in the star subgroup. A graph word belongs to a full-subgraph subgroup precisely when its reduced support lies there, by graph-product normal form and the coordinate retraction.

## 2. Four prescribed marked factors

Use the actual common K basis (a,B=bar b,d,e,f), with the fully certified eta. The four factors requested for the natural outer source diagonals are

  eta(a B a^{-1}), eta(a), eta(a d a^{-1}), eta(a e a^{-1}).

The B112 actual source basis changes are retained separately: the beta22 positive peripheral is a SOURCE conjugate of the natural e diagonal, rather than being identified with it without that conjugation. This calculation concerns these exact factors; it does not remove any of those source conjugators.

All four factors have h-height zero. In graph-followed-by-height normal form,

  f=bar(k)^{-1} h,       f^{-1}=k h^{-1}.

Reading the complete actual eta words with these identities gives the exact graph words saved in annular_four_contact_factors23.json. The checker uses all four B112 edge families, their barred images, and their shifts; it does not truncate the defining relations.

Every cancellation is certified by the full intervening commuting suffix, and the final graph words have no cancellable inverse pair. Their support outside star(k0) is:

| Factor | Outside-star vertices |
|---|---|
| eta(a B a^{-1}) | bar b_0 |
| eta(a) | bar b_0 |
| eta(a d a^{-1}) | bar b_0, d_1, e_1 |
| eta(a e a^{-1}) | bar b_0, d_1, e_1, bar k |

The corresponding reduced lengths are3,5,13,15. A separate reduction of each complete commutator [k0,V] is nonempty. Thus none of these four factors is already centralized by the inner geometric section in the COMPLETE bad annular vertex.

## 3. Scope

The actual one-neck quotient adds both cross commutators and may change these memberships. The calculation only rules out obtaining a source commutation by combining [k_-,c_+]=1 with an already valid vertex commutation [k_-,V]=1 for one of these four prescribed factors. It neither refutes a relation after the quotient nor determines its source image or centralizer.

No further factor/depth census is intended. The exact producer is check_annular_four_contact_factors23.py, with genuine .out/.err and full word/cancellation JSON. The input eta hash is retained.
