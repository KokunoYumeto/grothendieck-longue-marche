# Auxiliary mathematical checks

These checks were requested only after the transcription had been frozen.
The auxiliary reviewer received self-contained mathematical questions and did
not read manuscript scans, page transcriptions, or the contextual archive.
The primary reader retained responsibility for the manuscript interpretation.

## Conditional facet-set counterexample (research note R22)

Let $T^2=\mathbb R^2/\mathbb Z^2$, and let the graph consist of the two
coordinate circles. This cellular graph has one vertex, two open edges, and
one open two-dimensional face. The two maps

$$
D_1(t)=(t,t+1/3),\qquad D_2(t)=(t,2t+1/3),\qquad t\in\mathbb R/\mathbb Z
$$

are embedded circles because projection to the first coordinate is the
identity. Both avoid the graph vertex: when the first coordinate is zero,
the second is $1/3$. Their tangent vectors $(1,1)$ and $(1,2)$ are transverse
to both coordinate edges at every intersection.

Both meet the open vertical edge at $(0,1/3)$. The first meets the open
horizontal edge at parameter $2/3$; the second meets it at parameters $1/3$
and $5/6$. Both also meet the unique open two-dimensional face and avoid the
vertex. Consequently they meet exactly the same set of three open facets,
although their intersection multiplicities differ.

Their homology classes in $H_1(T^2;\mathbb Z)$ are $(1,1)$ and $(1,2)$.
An ambient isotopy from the identity induces the identity on homology;
forgetting the orientation of the circles permits a sign change, but these
two classes are not equal up to sign. Hence such an isotopy cannot carry one
circle to the other. An arbitrary ambient homeomorphism can change the
homology class, so that stronger distinction must not be claimed.

This validates the example against a literal unrestricted facet-*set*
criterion. It does not establish that the manuscript intended that full
generality, or refute a pseudoline-only statement or a convention in omitted
earlier pages. Those applicability limits remain explicit in R22.

## Five involutions and two different relation patterns (research note R35)

If $s_1,\ldots,s_5$ are involutions and every pair commutes, every word reduces
to $s_1^{e_1}\cdots s_5^{e_5}$ with each $e_i\in\{0,1\}$. Thus the generated
group is a quotient of $(\mathbb Z/2)^5$, has order at most 32, and every orbit
under any action has at most 32 elements. Additional relations can make the
group and its orbits smaller.

If the only stipulated commutations are between neighboring vertices of a
five-cycle, the universal presentation is instead

$$
\left\langle s_1,\ldots,s_5\;\middle|\;s_i^2=1,\;
s_i s_{i+1}=s_{i+1}s_i\;(i\bmod 5)\right\rangle.
$$

It is infinite: sending two nonadjacent generators to the two generators of
$C_2*C_2$ and the other three to the identity defines a surjection onto that
infinite group. A particular action or additional quotient may nevertheless
be finite. Circular indexing by itself imposes **no** commutation relation.

The distinction is algebraically secure. It is only a proposed diagnostic
for the intended five operators; it does not authorize replacing the frozen
wording or choosing a different manuscript reading.
