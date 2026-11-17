# Maps and moduli: proof and computation record

Run: MPL_138_090-133/maps_moduli_research. Author: GPT-6 Astra Pro; inherited effort unspecified. Research began after the transcription freeze of 2026-11-17 23:02:39 UTC. No source image was read and no frozen page was changed for these checks.

This record supplies the longer arguments behind MM01–MM17 in maps_moduli_research.md. The torus counterexample, genus-zero qualification, weighted-count warning, catalogue symmetry interpretation and elementary impossibility bound were already present in **Hua, modernised reading of cote 138, §§13–14**; they are credited there and tested here, not presented as new discoveries. The elliptic twist witness makes the failure of the raw isomorphism-class functor explicit.

## P1. Exact data and permutation convention

Frozen scan 98, lines 6–11 and 42–48, defines a precarte as three degree-labelled sets S,A,F, with q taking values 1 or 2, and an épinglage as an isomorphism C0 → Fac(C). It does not mark a dart, a tangent vector, an incident flag, or a parametrisation of a cell. The distinction is essential.

Use left-acting permutations on a finite dart set E, and compose ab as a after b. Put r = ρ_s, s = σ, and t = r^(-1)s = ρ_f, so rts = 1 and s² = 1. The cycles of r,s,t give S,A,F. Fixed points of s are allowed: these are the q=1 folded or half edges in the source. The oriented automorphism group is the common centralizer of r and s in Sym(E). Its kernel on Fac(C) consists of the centralizing permutations preserving every individual cycle of all three permutations setwise.

The Python certificate uses zero-based images of permutations; the displays in this document use one-based cycle notation. It enumerates only the explicit examples and two specified passports, not the whole catalogue.

## P2. The already-known torus counterexample, checked exactly

Take E={1,2,3,4}, r=(1234), s=(13)(24)=r², t=r. The action is transitive; the cycle counts are 1,2,1, giving Euler characteristic 1+2+1−4=0. Thus this is a connected oriented genus-one map with one vertex, two edges and one face.

The common centralizer is ⟨r⟩≅C4, because every permutation commuting with a full 4-cycle is its power. The element r² fixes the vertex cycle, the face cycle, and each of the two edge cycles {1,3},{2,4}. The odd powers exchange those two edge cycles. Consequently the kernel on Fac(C) is precisely ⟨r²⟩≅C2.

This proves MM02R: complete pinning in the literal sense of scan 98 does not imply rigidity. It also refutes faithfulness on isomorphisms for Fac, while saying nothing against the separate conservativity assertion. A conservative functor need only reflect isomorphisms; it need not distinguish automorphisms.

Hua §13.I, lines 1525–1533, already describes the same square-torus half-turn. The calculation here checks that it survives the actual definition, including the inserted orientation requirement. This finite kernel is unrelated to the different infinite-operator comparison left open in RESULTS_STATE **LM4 C.12**.

## P3. Ordinary counts, groupoid mass and stabilizers

For a fixed oriented map C with Fac(C)≅C0, let γ=Aut(C0), A_C=Aut(C), and K_C=ker(A_C→Aut(Fac(C))). The set of labellings Iso(C0,Fac(C)) is a γ-torsor. The A_C-orbits are exactly the pinned isomorphism classes with underlying map C, and each orbit has |A_C|/|K_C| elements. Therefore

\[
\#\{\text{pinned classes}\}
=\sum_{[C]}\frac{|\gamma|}{|\operatorname{im}(A_C\to\gamma)|}
=\sum_{[C]}\frac{|\gamma|\,|K_C|}{|A_C|}.
\]

Every object in such an orbit has pinned automorphism group K_C. Dividing each isomorphism class by the order of its own automorphism group gives groupoid mass

\[
\sum_{[C]}\frac{|\gamma|}{|A_C|}.
\]

When K_C=1, the latter is also the ordinary number of pinned classes. It is still not in general the unweighted number of underlying map classes multiplied by |γ|.

For the cubic star, r=(123), s=1, t=(132). There is one underlying oriented map, |γ|=3!=6, |A_C|=3, and K_C=1. The number of pinned classes is 2, not 6. This is the example already cited by Hua §13.I, lines 1541–1546; the current arithmetic agent handles its occurrence on frozen scan 104.

For the torus, |γ|=2, |A_C|=4 and |K_C|=2. There is one pinned class over this underlying map, with automorphism group C2; the weighted contribution is 1/2. Thus blindly using the weighted expression as an ordinary count beyond the rigid locus also fails.

The same orbit calculation gives

\[
\operatorname{Stab}_{\gamma}([C,u])
\simeq\operatorname{im}(A_C\to\operatorname{Aut}(\mathrm{Fac}(C)))
\simeq A_C/K_C.
\]

This is MM06R. It is the full automorphism group only if the pinning action is faithful. The torus is a regular C4 cover but the γ-stabilizer has order 2, not 4. The statement is made here for geometric objects; relative sections over a non-algebraically-closed base require additional descent qualifications.

## P4. The genus-zero qualification

Over an algebraically closed field of characteristic zero, a genus-zero cover is a map f:P1→P1. A pinned automorphism fixes each point in each of the three reduced fibres over 0,1,∞. Since a nonconstant finite cover is surjective, choose one point in each fibre: these are three distinct points. An automorphism of P1 fixing three distinct points is the identity, as follows directly from the fractional-linear formula.

Thus genus-zero geometric rigidity is valid. This verifies the qualification in Hua §13.I without relying on its abbreviated inequality V+F=E+2≥3: q=1 edges are allowed, and the star example has V+F=2. The marked points above 1 supply the missing fixed point. Geometric rigidity alone does not establish every representability and base-change assertion in scan 100.

## P5. A concrete failure of the raw fine moduli functor

For d=1 or 2, let E_d be the smooth projective curve with affine equation

\[
d y^2=x^3-x,
\qquad f_d=x^2:E_d\longrightarrow\mathbb P^1_{\mathbb Q}.
\]

The roots of x³−x are distinct. The map to the x-line has degree two and f_d has degree four. At (0,0), x has order 2, so f_d has zero order 4. At each of (1,0),(-1,0), x∓1 has order 2, so f_d−1 has zero order 2. At the unique point O at infinity, x has pole order 2 and f_d has pole order 4. The ramification passport is consequently (4)|(2,2)|(4), and there is no other ramification: the degree-two x map is branched only at x=0,±1,∞, and x↦x² is branched only at 0,∞.

Pin the reduced fibres by labelling (0,0), the ordered pair ((1,0),(-1,0)), and O. All these points are rational. The involution (x,y)↦(x,−y) preserves the pins. Over C the automorphism (x,y)↦(−x,iy) has order four and preserves f; since f has degree four, the cover is Galois with group C4, and its square is this pinned involution.

Over L=Q(√2), the map E_2→E_1 given by (x,y)↦(x,√2 y) is a pinned isomorphism of covers. Over Q, a cover isomorphism would have to send the function x to x or −x, since its square is f. Preservation of the two individual labels over 1 excludes −x. An isomorphism over Q(x) would then identify the quadratic extensions obtained by adjoining √(x³−x) and √((x³−x)/2). They are distinct because their square-class ratio is 2, which is not a square in Q(x): a rational function whose square is constant is constant, and 2 is not a square in Q.

Thus two different elements of the raw set P_C0(Q) become equal in P_C0(L). Since Spec L→Spec Q is finite étale and surjective, this raw isomorphism-class presheaf is not even separated for the étale topology. Every functor represented by a scheme is an étale sheaf. This proves MM05R and disproves the literal universal representability assertion of scan 100 already over Q; no assertion about a coarse moduli sheaf is refuted.

The argument was independently checked by /root/arithmetic_research in this run. That check stressed exactly the necessary qualification: the pins here are reduced fibre points, not tangent vectors or local parameters.

Context connections are unusually close: LM_140-2_text.tex, scan 547, line 15778, distinguishes the level-2 elliptic moduli object from a scheme and describes a C2-gerbe; LM_140-3_text.tex, scans 180–181, lines 7891–7898, identifies quadratic-twist ambiguity and writes y²=x(x−1)(x−1/2). The latter becomes E_2 after X=x−1/2, u=2X, v=2y, because 2v²=u³−u. Its supplied note C3 already discusses this twist; the application to f=x² is the explicit witness added here.

## P6. What survives of the arithmetic moduli discussion

For a connected degree-δ cover, its faithful monodromy group embeds in S_δ, so |G| divides δ! and every p>δ is prime to |G|. This is an elementary implication, not a complete proof of the asserted integral moduli construction.

The appropriate primary reference is SGA 1, Exposé XIII, Corollary 2.9: for a smooth proper family with a relative normal-crossing boundary, prime-to-residue-characteristic finite-group torsor classes form a locally constant constructible R¹ sheaf. The following specialization construction and Lemma 2.11 track inertia. Apply this to the pair (P1,{0,1,∞}) and groups of order dividing δ! over Z[1/δ!]. It explains the prime bound and supports an unramified finite geometric-class formulation; it does not turn the raw presheaf refuted in P5 into a fine scheme.

For this run, the numerical prime bound and the match of the smooth pair with the cited hypotheses were checked. No all-characteristic representability theorem, extension theorem for every pinned family, or proof of the full scheme M_C0 over Z is claimed. Hua's citation to Fulton's 1969 Hurwitz paper was checked bibliographically only; that article's theorem was not used as a proof of this exact moduli problem.

Once a finite continuous Γ_Q-set of geometric isomorphism classes is given, it corresponds to a finite étale Q-scheme regardless of whether the raw isomorphism-class presheaf is represented. Explicitly, an orbit Γ_Q/H corresponds to the fixed field Qbar^H and the disjoint union over the finitely many orbits gives the scheme. Conversely, a finite étale algebra is a product of finite separable extensions. Every Q-algebra map R→C lands in Qbar, since each image element is algebraic over Q. This verifies the first displayed bijection in scan 103 conditionally on finite étaleness.

An operation of γ=Aut(C0) on the labelling set is defined over Q, so it commutes with Γ_Q. If finite étaleness and the unramified condition are established, the corresponding finite étale model over Z[1/δ!] is recovered by integral closure; the claim requires that unramified condition, not merely an arbitrary finite Γ_Q-set.

## P7. Core-free subgroups, the connectedness condition, and generators

For a transitive G-set E, choose e∈E and let H be its stabilizer. The map gH↦g·e identifies E with G/H, and the kernel of the action is

\[
\operatorname{core}_G(H)=\bigcap_{g\in G}gHg^{-1}.
\]

Thus faithfulness is equivalent to core-freeness. Conversely a finite group G generated by r,s, with s²=1, together with a core-free H yields a faithful transitive action on G/H; putting t=r^(-1)s supplies rts=1. Requiring the three cycle partitions to equal the degrees in C0 gives exactly the connected combinatorial criterion in scan 102.

Here δ=[G:H], so δ divides |G|. The length of each r-,s-,t-cycle divides the order of the corresponding group element, hence divides |G|. A G-equivariant self-map of G/H is determined by the image of H; this image must be nH for n∈N_G(H), and the resulting automorphism group is N_G(H)/H (with the opposite multiplication if right translations are used without inversion). In the regular case H=1 its order is |G|=δ.

Transitivity is indispensable for δ=[G:H]. For disconnected covers one needs a disjoint union of coset actions; a degree-two trivial disconnected cover already has trivial monodromy group, so its degree need not divide the group order. These notes do not decide whether connectedness was an ambient convention on earlier pages; they state the hypothesis actually used.

For a fixed complex cover f:X→P1_C, the embedded graph f^(-1)([0,1]) and complex orientation determine the oriented dessin, including the q=1 convention after the usual suppression at degree-two white vertices. Equivalently, after fixing a basepoint and standard loops in the punctured target, the monodromy representation is determined up to simultaneous conjugacy. Actual elements in a separately chosen abstract group require those choices, but that does not imply that the oriented map's isomorphism type is undetermined. This is the precise issue with the negative sentence at the end of scan 102, already flagged by Hua §13.II–III; no conjectural alternative reading is inserted into the frozen text.

## P8. Catalogue groups, chirality, and the two targeted enumerations

For the orientation-preserving symmetry group, the certificate enumerates permutations commuting with r,s. An orientation-reversing symmetry is represented by a permutation a with ara^(-1)=r^(-1) and asa^(-1)=s, together with the reversing orientation sign. The sign is part of the symmetry even when its dart permutation coincides with an orientation-preserving permutation (notably degree one).

All automorphism orders in this section concern finite combinatorial symmetries, with isotopies forgotten. The full group of homeomorphisms or holomorphic automorphisms preserving the embedded graph can also contain an identity component, as illustrated by the separate operations_proofs.md P4.

| Example | Monodromy | Oriented automorphism order | Full automorphism order |
|---|---:|---:|---:|
| Degree-one folded segment | trivial | 1 | 2 |
| Cubic star | C3 | 3 | 6 |
| Cubic loop-tail | S3 | 1 | 2 |
| Torus example P2 | C4 | 4 | 8 |

The degree-one label C2 already excludes a monodromy interpretation for the catalogue. The star's S3 and loop-tail's C2 agree with full symmetry, respectively D3 and a single reflection, not their monodromy groups. This confirms Hua §14's interpretation in these diagnostic examples; it does not certify every handwritten group label.

For the degree-five passport (4,1)|(2,2,1)|(4,1), fix r=(1234)(5). Enumerate all involutions s of type (2,2,1), retain transitive pairs for which r^(-1)s has type (4,1), and quotient by the centralizer of r. There are exactly two classes. Both have oriented and full automorphism group 1 and monodromy order 20; reflection exchanges them. This gives an exact finite check of the group-1 and “rigide” example on frozen scans 116 and 118, and an example where complex conjugation can exchange the two oriented classes after forgetting the pins. It is not a classification of torsion in any profinite Grothendieck–Teichmüller group.

For the repeated degree-six passport (6)|(2,2,1,1)|(3,2,1), take r=(123456). The three representatives from the certificate are

\[
s_1=(36)(45),\quad s_2=(23)(46),\quad s_3=(24)(56).
\]

All three have monodromy S6 and trivial oriented automorphism group. The first has a reflection and full automorphism order 2; the last two form a chiral pair, each with full automorphism group 1. Thus there are three oriented classes but two classes after forgetting orientation. Repetition of the passport in scan 117 is mathematically compatible with two distinct unoriented maps; it does not by itself prove a scribal duplication.

The arithmetic agent's separate computation for the dual passport (3,2,1)|(2,2,1,1)|(6) gives the same three-class phenomenon; see arithmetic_certificate.py and its JSON, and arithmetic_research.md AR13–AR14. Its primary literature lead was opened and checked here: Gareth A. Jones, “Regular dessins with a given automorphism group,” Example 7.7, printed page 12, explicitly records the dual triple, one reflexible map and a chiral pair, each with monodromy S6. This is therefore a targeted recheck of a known example, not a new classification. The present calculation does not identify every drawn representative, and no complete enumeration of scans 114–120 was attempted.

## P9. Elementary impossibilities and internal numerical checks

A connected map with V vertices has at least V−1 full edges joining vertices in a spanning tree. Each such edge consumes two darts, while q=1 half edges cannot connect two distinct vertices. Hence δ≥2(V−1).

The degree-five case V=4 with degrees (2,1,1,1) violates 5≥6; the degree-six case V=5 with degrees (2,1,1,1,1) violates 6≥8. This confirms both “impossible” annotations, already explained by Hua §14.

Frozen scan 120, line 3, literally lists (3,2,2), whose sum is 7, while its marginal passports at line 5 list (3,2,1), of sum 6. That is a numerical incompatibility inside the frozen reading, not authorization to silently replace the last 2 by 1. Likewise the degree-four “rigide” on frozen scan 114 lies inside the deleted block at lines 74–80; its textual status differs from the live boxed “rigide” on scan 118.

## Reproduction and evidence boundaries

Run from the work directory:

~~~sh
python3 records/check_maps_moduli.py
~~~

The script verifies all 44 frozen source hashes before and after the calculation and writes maps_moduli_certificate.json. The successful run was at 2026-11-17 23:07:24 UTC. It uses Python's standard library only; no approximate arithmetic or external group database is involved. The JSON contains every automorphism and representative used above, with the explicit permutation convention.

### External primary references actually consulted

1. **Stacks Project, Lemma 58.2.2, tag 03QR**, equivalence of étale K-schemes and continuous Galois sets: https://stacks.math.columbia.edu/tag/03QR .
2. **Stacks Project, §58.7, tag 03SF**, finite Galois covers and normal subgroups: https://stacks.math.columbia.edu/tag/03SF .
3. **SGA 1**, Exposé XIII, Corollary 2.9, construction 2.10 and Lemma 2.11, printed pages 288–290 (PDF pages 303–305, zero-based): https://arxiv.org/pdf/math/0206203 . The displayed application in P6 is an inference using this theorem, not a claim that the source states the manuscript's full moduli assertion.
4. **William Fulton, “Hurwitz schemes and irreducibility of moduli of algebraic curves,” Annals of Mathematics 90 (1969), 542–575**, DOI 10.2307/1970748: https://annals.math.princeton.edu/1969/91-3/p06 . Bibliographic check only; no theorem from this paper is treated as verified here.
5. **Gareth A. Jones, “Regular dessins with a given automorphism group,” Example 7.7, printed page 12**, https://arxiv.org/pdf/1309.5219 . The known degree-six triple was checked against the present dual-passport computation.

All longer source interpretations remain in the concise research notes; the actual check events are recorded separately in maps_moduli_check_events.tsv.
