# Annular source-stable-letter presentation and periodic heads

**Checkpoint 22 research. Formal sources remain frozen.** The algebra below is a complete proposed proof structure, independently derived from the actual adapted ten-word table. The literal forward candidate check is complete in CE's records. The reverse derivation and periodic-head comparison are being independently reviewed; this note does not allocate a formal theorem or claim that an unreviewed stage has been accepted.

## 1. Actual adapted generic presentation

Use CE's exact change `Y_i=back(W0)(x_i)` and its inverse. Put

`a=Y1, b=Y2, c=Y3, f=Y4, d=Y5, e=Y6`.

The actual zero monodromy becomes the full twist of `(c,f)`. Let `g0` be its far-section generator, with `g0^-1 x g0=psi0(x)`, and put `h=g0 c f c`. Then, before any node relation is imposed,

`[h,c]=1, h^-1 f h=cfc, h^-1 U h=(cfc)^-1 U(cfc)` for `U=a,b,d,e`.

Equivalently `h U h^-1=f U f^-1` on those four outsiders. Set `k=f^-1 h`. Then

`[k,U]=1, h k h^-1=bar k, [h,c]=1`, with `bar x=cxc`.

In fact `k=g0`: the full-twist relation gives `f g0=g0 cfc`. This is relevant to the character below. The source-stable-letter height `h->1,k->0` is **not** the geometric zero-base winding, which takes both `g0` and `h` to one.

The generic group alone also has the actual algebraic amalgam

`((C2(c)*Z(f)) x Z(hc)) *_<g0> (Z(g0) x F(a,b,d,e))`,

where `g0=(hc) f^-1 c`. The amalgam statement is before the ten node relations; no post-filling edge injection follows from it.

## 2. Two-sided simplification of all ten filled relations

All words in this section refer to `work_CE/next_symmetric_nodes/inner_q0_adapted_basis22.json`. The first contact gives `[b,bar b]=1` (its printed word is `[b,bar b^-1]`); the two other immediate contacts give `[d,bar d]=1` and `[a,bar a]=1`, the latter up to its printed conjugator. The first shared node gives `[a,b]=1`, and beta34 gives `[bar a,d]=1`.

After using only the b-contact, put `A=f^-1 b f`, `X=d e d^-1`, and `t=d^-1 f^-1 c f d` (an involution). The two beta12/beta13 relations are

`[A,X^-1]=1, [X^-1 A X,d]=1`.

Their simultaneous normal closure equals that of `[A,d],[A,e]`: the first makes `X^-1 A X=A`; the second gives `[A,d]`; the first then gives `[A,e]`. Conversely these latter two imply the original pair. Conjugating by `f` and using `f U f^-1=h U h^-1` turns them into

`[b,h d h^-1]=1, [b,h e h^-1]=1`.

The other shared node is `[d,t e t]=1`. The beta22 contact is equivalent to `[e,t e t]=1`. These follow directly from the printed table after the b-contact: the long middle cone word reduces to `c`. Put

`E=f d e d^-1 f^-1=h(d e d^-1)h^-1`.

Conjugating the shared-node relation by `f d`, then by `h^-1`, gives `[d,bar d bar e bar d^-1]=1`. Because `[d,bar d]=1`, it is equivalent to `[d,bar e]=1`. Its c-conjugate gives `[bar d,e]=1`.

Under the same changes the beta22 contact becomes `[d e d^-1,bar d bar e bar d^-1]=1`. With the three already established commutations `[d,bar d]`, `[d,bar e]`, `[bar d,e]`, this commutator is the conjugate by `d bar d` of `[e,bar e]`. Thus the beta22 contact is equivalent to the missing diagonal `[e,bar e]=1`. Every use is reversible.

Finally beta24 is `[a,bar d bar e bar d^-1]=1`. Since `[bar a,d]=1` gives `[a,bar d]=1`, this is equivalent to `[a,bar e]=1`, or to its c-conjugate `[bar a,e]=1`.

Consequently the exact full ten relations, **in the generic annular group**, have the same normal closure as

- the four diagonals `[U,bar U]`, `U=a,b,d,e`;
- `[a,b]`, `[bar a,d]`, `[bar a,e]`, `[d,bar e]`;
- `[b,h d h^-1]`, `[b,h e h^-1]`.

This is a simultaneous two-sided reduction, not a claim that the zero monodromy acts on the slit quotient. CE's finite candidate HNN introduces `p=h d h^-1,q=h e h^-1`; all additional target-edge relations are h-images of the source-edge relations. The exact graph subgroup comparison then gives the proposed fourteen-vertex cone-bearing HNN.

## 3. Exact unfolded graph

For the new height `h->1`, use vertices `U_n=h^n U h^-n` and their bars for `U=a,b,d,e`, `n` in Z, together with `k0=k,k1=bar k`. The latter have period two because `h k h^-1=bar k` and `h` commutes with `c`.

The graph has precisely the following edges for each n, together with their barred images:

1. `(U_n,bar U_n)` for the four U.
2. `(a_n,b_n)`, `(bar a_n,d_n)`, `(bar a_n,e_n)`, `(d_n,bar e_n)`.
3. `(b_n,d_(n+1))`, `(b_n,e_(n+1))`.
4. `(k_(n mod2),U_n)` for the four U.

The bar involution exchanges each displayed vertex with its mate, including `k0,k1`. The shift moves n to n+1 and exchanges k0,k1. These automorphisms commute. Reidemeister–Schreier rewriting of the complete finite presentation gives exactly this graph group and no extra relations. Conversely its semidirect product by the shift and bar has the displayed finite presentation. Thus the claimed model, once Section 2's finite input comparison is accepted, is

`R_ann = A(Graph_infty) semidirect (Z_h x C2_c)`.

This is not the universal cover of the geometric annular base. It is the kernel of the explicitly different source-stable-letter character.

## 4. Discrete fixed subgroup

The piling argument from B110 applies to this countable graph: each finite word uses finitely many vertices, so the normal-form and first-letter proof is unchanged. The only bar-orbits whose two vertices commute are the four U-orbits at each n. In particular `k0,k1` are not adjacent and neither vertex is fixed by bar. Hence the fixed graph subgroup is generated by all `delta U_n=U_n bar U_n`.

These generators are free. Keep `a_n,d_n,e_n,bar b_n` at every n and kill the opposite four and k0,k1. The retained vertex set has no edges, including the shifted edges in item 3. The coordinate projection sends the diagonal generators to a free basis. This proves freeness without a rank inference. The shift permutes the four infinite families, so adjoining h gives the free group on `delta a_0,delta b_0,delta d_0,delta e_0,h`. Consequently the proposed discrete cone centralizer is this F5 times C2.

The actual source must be identified using DE's independently checked five-source detector. Its projection is a triangular free basis. Restricted to the natural fixed F5 just described, the same detector is an isomorphism. Actual source loops already centralize the cone, so equality follows from this isomorphism and the exact source images, not from equality of ranks.

## 5. Finite even-period heads and full completion

For even m at least four identify all indices modulo m. Keep k0,k1 distinct. This gives a finite graph with `8m+2` vertices and commuting shift/bar automorphisms, with the shift of order m. No ordinary U-vertex becomes its own barred mate. The only commuting bar-pairs remain the four diagonal pairs at each cyclic index: the other edge families never join a vertex with its own barred mate. The retained independent vertex set in Section 4 remains independent after wrapping indices.

Thus the discrete centralizer of c in

`R_m=A(Graph_m) semidirect (C_m x C2)`

is `F_(4m) semidirect C_m`, times C2, and is generated by the images of the four level-zero diagonal generators, h and c. It is therefore exactly the image of the proposed actual source F5 times C2.

Each head has a finite-graph RAAG of finite index. Its graph can have triangles, so no dimension-two bound is asserted. The general finite Salvetti model has finite dimension: induct on vertices, attaching a finite K(link,1) cylinder along the coordinate-injective link subgroup. This gives a finite projective resolution. Residual finiteness, Lorensen's full goodness, the filtered-colimit all-discrete-module passage and the finite-extension spectral sequence give exactly the finite virtual cohomological TYPE and comparison hypotheses required for the already-read prime-order Boggi–Zalesskii theorem. Hence the completed centralizer in each head is the closure of its discrete centralizer.

Every finite quotient of the original group factors through some even-period head: take m even, at least four and divisible by the order of its h image. The relation h^m=1 identifies the indexed generators precisely as in the cyclic graph presentation. This is a cofinality statement for **all** finite targets, not a selected tower assumption.

An element centralizing c in the full completion maps, in every such head, into the closure of the image of the source F5 times C2. Therefore its image in every finite quotient belongs to the source image; compact finite-quotient separation gives membership in the actual closed source. The reverse inclusion is immediate. DE's actual ordinary source retraction, followed by index-two cores, identifies this closure with the full completion F5-hat times C2.

## 6. Checkpoint status and remaining review

The exact generic adapted package and the forward fourteen-vertex HNN verification are complete and saved by CE. DE's actual source F5 retraction is independently executed. The reverse ten-relator proof and the unfolded/periodic group comparison above are mathematical proposals with the explicit review boundary retained. Root independently wrote the same route in `records/annular_reverse_relations_root22.md` and `records/annular_even_period_strategy_root22.md`. Their final comparison and adversarial reviews should be recorded before any formal annular theorem. No long computation is running, no formal source/register is changed, and no whole-surface/all-neck conclusion follows from this regional strategy.

**Final read at 22:45 UTC.** I read both root notes completely and compared them with the actual adapted ten-relation table already opened in this turn. The reverse derivation and exact four-family unfolded graph agree with the independent calculations above. The even-period presentation quotient, lack of new bar-fixed vertices or commuting mate pairs, independent free coordinate projection, finite-type/all-module comparison, and cofinal completed-centralizer argument all PASS as mathematical implications from this actual presentation. The exact source identification uses DE's actual detector and its restriction to the natural fixed F5, not ranks. I have not independently rerun DE's new detector producer in this turn; its established certificate remains the explicitly attributed input. These late results remain research-only for checkpoint22. Both full main decisions and the other-neck/global transfer remain Open. There is no live producer or background writer.
