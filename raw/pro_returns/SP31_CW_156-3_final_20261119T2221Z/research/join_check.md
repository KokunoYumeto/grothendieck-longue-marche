# Narrow check of the join and moderate difference

Worker: `/root/context_links`, GPT-6 Astra Pro; reasoning effort not exposed. Check completed 2026-11-19. Source: frozen `out/SP31_CW_156-3_transcription.tex`, especially scans 007–010 and 018–022. No images or witness C notes were read; no TeX was edited. This is a mathematical check of the intended order axioms in the frozen text, not a repair of uncertain literal symbols in the transcription. No broad RESULTS_STATE theorem is used or re-proved.

## Verdict

**The general join in scan 020 has a complete order-theoretic proof.** Sorting the chain-ordered endpoints and merging overlapping pieces gives the construction, but that algorithm alone does not establish leastness against an arbitrary moderate upper bound. The missing ingredient is a short convexity-and-divisibility lemma. It proves the required component uniqueness as well, without treating the pieces as topological connected components. Rays require the global directedness hypotheses when identifying a merged hull.

The marked-boundary inclusion is valid **under an explicit, consistent relative-endpoint convention**. The frozen definitions have an endpoint-presentation ambiguity when the ambient tronçon has extrema; this is isolated below as **SP31-N018-04**. No claim is made that the original boundary definition is already well-defined.

**The unrestricted least-set assertion for moderate difference in scan 021 is false under the intended tronçon axioms.** The doubled-rational example below is **SP31-N021-04**. Restricting the competing upper sets to those in moderate position with Y avoids this particular counterexample, but no general theorem with that restriction is proved here. The additional scan 022 assertions are consequently not certified as general statements.

## 1. Setting and endpoint convention

Write P for the ordered tronçon. The intended scan 009 assumptions include upward and downward global directedness, divisibility (between a<b there is z with a<z<b), and the local strict-cone filtering axioms. The proof of the join below needs only the global directedness and divisibility, in addition to the displayed definitions of the pieces. It does not assume P is totally ordered.

A nonempty closed wide piece is a set of one of the forms

- [a,b] = {x : a≤x≤b}, with a≤b;
- P_{≤b} or P_{≥a};
- P itself.

A singleton is included by a=b. Every such set is order-convex. A closed moderate set is a finite disjoint union of these pieces whose finite marked endpoints form a chain. Mutual moderation of two such sets puts all their finite endpoints into a common chain. Formal bounds −∞ and +∞ may be used to encode rays and P.

### SP31-N018-04 — Endpoint-presentation ambiguity

If P has a least element m, then the nondegenerate set [m,b] is also P_{≤b}; if it has both extrema m,M, then [m,M]=P. The literal formulas on scan 018 assign {m,b} to the first interval presentation, {b} to the ray presentation, and the empty set to P. Therefore a boundary operation on sets needs a convention before the scan 020 boundary assertion can have an unambiguous meaning.

For the conditional boundary proof here, use the relative-endpoint convention: for a **nondegenerate** piece, suppress an endpoint that is an ambient extremity, normalize [m,b] to a lower ray, [a,M] to an upper ray, and [m,M] to P. **A wide singleton {m} or {M} still has its one marked endpoint**, as the manuscript says; the suppression rule does not apply to a singleton. This convention only removes redundant endpoints from nondegenerate representations. It does not identify marked endpoints with ordinary topological frontier.

The construction and leastness of the join as a subset do not depend on this boundary convention. The convention is needed to speak of its intrinsic marked boundary and mutual moderation independently of presentations.

## 2. Separated-component lemma

**Lemma.** Suppose W is a finite disjoint union of nonempty closed wide pieces W_1,…,W_k with chain-ordered endpoints. Any nonempty order-convex set A⊆W lies in one W_i.

**Proof.** Sorting the endpoint bounds orders the disjoint pieces. Between consecutive pieces there are finite endpoints r_i<l_{i+1}, with

W_i⊆P_{≤r_i},  W_{i+1}⊆P_{≥l_{i+1}}.

The bounds defining an internal gap are genuine points of P, even if the first or last piece is a ray. If A met two different pieces, take x in its earlier piece W_i and y in a later piece W_j. Divisibility supplies

r_i<z<l_{i+1}.

Then x<z<y, so convexity gives z∈A. But z lies in the gap and hence outside every W_h, a contradiction. Thus A lies in one piece. ∎

The lemma does **not** require A's endpoints to be comparable with the endpoints of W. This is exactly why it applies to an arbitrary moderate upper bound of the proposed join.

### Consequence: combinatorial component uniqueness

Suppose a set has two admissible finite disjoint decompositions into closed wide pieces, A_i and B_j. The lemma puts each A_i in one B_j and that B_j in one A_h. Since A_i is nonempty and the A-family is disjoint, h=i; therefore A_i=B_j. Interchanging the families proves equality of the decompositions as families of subsets.

This proves the combinatorial uniqueness used by scan 019 and the join argument. It supplies no proof that these are topological connected components. In particular, neither order completeness nor topological connectedness was used.

## 3. Construction and leastness of the general join

Take all component pieces of X and Y. The assumption of mutual moderation makes their finite endpoints a common chain; append the two formal bounds for rays.

**Construction.** Sort by lower bound. Merge overlapping pieces into their full order hull, and repeat until consecutive output pieces are separated. Equivalently, take the connected components of the finite graph whose vertices are the input pieces and whose edges indicate nonempty intersection. The hull of each graph component has lower bound the least of its lower bounds and upper bound the greatest of its upper bounds. Call the union of these hulls H.

The familiar test “next lower bound ≤ current upper bound” is justified here because the relevant bounds lie in a chain. If it succeeds, the next piece actually meets an earlier input piece having the current greatest upper bound; it does not merely meet a point artificially added by an earlier hull. Common rays and the whole set P cause no exception.

The output hulls are disjoint closed wide pieces with chain-ordered endpoints. Thus H is closed moderate and contains X∪Y. Although the endpoint list is totally ordered, **the elements inside a piece need not form a chain**. Merging takes the whole order interval: [a,b] and [b,c] produce [a,c], which can contain points incomparable with b. This is the distinction explicitly illustrated at the bottom of scan 020.

**Leastness.** Let W be any closed moderate set containing X∪Y. Do not assume that W is in moderate position with X or Y. Each input piece is order-convex, so the separated-component lemma puts it wholly in one component of W. Two intersecting input pieces must lie in the same component of W. Hence every graph component of inputs lies in one component K of W.

It remains to check that K contains the corresponding hull:

1. If both outer bounds l,u are finite, they belong to input pieces and hence to K. Convexity gives [l,u]⊆K.
2. If the hull is P_{≤u}, the cluster contains a lower ray P_{≤v} and also the outer endpoint u. For x≤u, global downward directedness gives z≤x,v. Then z∈K and z≤x≤u, so x∈K by convexity.
3. The upper-ray case is dual.
4. If the hull is P, either P was an input piece, or the cluster contains a lower ray P_{≤v} and an upper ray P_{≥w}. For arbitrary x∈P choose z≤x,v and t≥x,w by global directedness. Then z,t∈K, so x∈K.

Thus H⊆W for every moderate upper bound W, proving that H is the least upper bound X∪_mod Y.

**Boundary inclusion.** Every finite outer endpoint selected by a merge came from an input endpoint; normalization can only remove redundant ambient endpoints from nondegenerate pieces. A singleton output is already a singleton input piece, so its marked endpoint is also inherited. Under the explicit convention in §1,

B(X∪_mod Y) ⊆ B(X)∪B(Y).

The same construction handles every finite mutually moderate family, including empty inputs. It also proves the stated compatibility consequence: a set whose marked endpoints are comparable with those of every input remains compatible with the resulting subset of marked endpoints.

## 4. SP31-N021-04 — The general moderate difference can have no least closed moderate envelope

Let

P = Q×{0,1},

ordered by (r,i)<(s,j) exactly when r<s; equality is the only comparison between equal rational coordinates. This is the doubled rational line. It satisfies the intended tronçon axioms: rational numbers above or below any finite list give global directions; choosing a rational strictly between the base level and the minimum (or maximum) of two given levels gives local cone filtering; choosing an intermediate rational proves divisibility.

Put

c=(-1,0), a=(0,0), a'=(0,1), b=(1,0), b'=(1,1), d=(2,0),

and take X=[c,d], Y=[a,b]. These are closed moderate sets with Y⊆X and mutually comparable endpoint sets. Points a,a' are incomparable, as are b,b'.

The moderate complement C=C_mod(Y,X) consists exactly of those points of X whose rational coordinate is below 0 or above 1. The omitted twins a',b' are outside Y but are not in moderate position with the relevant endpoint of Y. In formulas, C has a left part including c and all doubled levels −1<r<0, and a right part consisting of all levels 1<r<2 and d.

Consider

Z_0=[c,a] ∪ [b,d],

Z_1=[c,a'] ∪ [b',d].

Each is a closed moderate set: its two components are disjoint and its own four endpoints form a chain. Each contains C. Directly from the equal-level incomparability,

Z_0 ∩ Z_1 = C.

However, C is not closed moderate. Its left part A is nonempty and order-convex. If C had an admissible finite closed-piece decomposition, the separated-component lemma would put A in one closed wide piece K⊆C. Such a piece cannot be an upper ray or P. A finite upper endpoint of K cannot have level below 0, since A contains levels arbitrarily close to 0 from below. An upper endpoint at level 0 is not in C; one at a higher level would, by convexity with c, force forbidden points of Y into K. All possibilities are excluded.

If a least closed moderate set Z containing C existed, then

C ⊆ Z ⊆ Z_0∩Z_1 = C,

so Z=C, contradicting the preceding paragraph. This refutes the scan 021 unrestricted minimum claim under the displayed intended order hypotheses.

**Refinement and limit.** Z_1 is not in moderate position with Y, because a' is incomparable with a and b' with b. Therefore this example does not refute a theorem that asks for a least upper set only **among closed moderate upper sets compatible with Y**. That restriction is a possible refined statement, not a generally proved result in this check. It also must be stated before taking a minimum; the later assertion that the unrestricted minimum is compatible with Y does not restrict its competitors retroactively.

## 5. What remains unchecked on scan 022

The general assertions about a finite relative frontier F, F⊆Z, absence of isolated points of Z in F, and C_mod(Y,X)=C_mod(F,Z) are not proved here. The unrestricted Z used on scan 021 need not exist. Even after a compatible-envelope reformulation, one would have to specify whether F is a marked endpoint set or ordinary topological frontier, and prove the asserted identity under that choice. The already checked total-order example is not promoted to a general result.
