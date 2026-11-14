# Independent post-freeze checks of three segment examples

This memo reconstructs the complete preserved mathematical analysis after the execution environment reset. These are our own constructions, checked against the frozen transcription after context access; they are not manuscript readings and change no transcription file. Confidence is **high for the explicit examples and the limited conclusions stated**, with no claim of novelty.

Relevant frozen axioms: F1–F2 at 156-1/006; F3 and its strengthening at 007 and 013; F4 at 008; F5/F5′ at 009; restriction at 010; local/global directedness at 021–022; both formulations of F6 at 023. Inclusion in the filtering conditions permits equality, as required by “filtrant croissant”; demanding proper inclusion would be a different statement. Branch equivalence is understood by **common initial subsegments**, as stated in the F3 dichotomy and explicitly in the F6 hypothesis at scan 023; the separate doubtful equivalence-relation display at scan 007 is not silently resolved.

## 1. Ambient order intervals: reusable verification

For a partially ordered set \(P\), put

\[
S(P)=\{[a,b]_P:a<b\},\qquad
[a,b]_P=\{t\in P:a\le t\le b\},\qquad
\delta[a,b]_P=\{a,b\}.
\]

Supports have unique least and greatest elements, so regarding them as the segments introduces no duplicate boundary ambiguity. If the order is dense, every nondegenerate segment has nonempty interior. F1 follows because the unique subsegment from endpoint \(a\) to \(z\in[a,b]\setminus\{a\}\) is \([a,z]\), and dually at \(b\). For F2, \([a,z]\cap[z,b]=\{z\}\), and a subsegment with endpoint \(z\) lies on the appropriate side according to whether its other endpoint is below or above \(z\).

**Important scope:** F2 does not require \([a,b]=[a,z]\cup[z,b]\); points incomparable with \(z\) can be missing from the union. F4 expressly says “on n'affirme pas égalité!” (156-1/008), so a glued support cannot be assumed to equal the union of its inputs.

In the examples below, each point is in a rational chain block with no immediate neighbor on each available side. Same-direction endpoint segments share a sufficiently short interval in that block, whereas opposite directions meet only at the endpoint. This verifies F3, identifies the available branch germs, and proves F5 at regular points. It also proves F4: segments meeting only in a regular common endpoint must have opposite directions, so their other endpoints satisfy \(a<z<b\), and the unique gluing is \([a,b]\), containing their union.

The strengthened local filtering condition is checked within each interval by choosing a point sufficiently near the pertinent endpoint in its rational block. In the first example, if two interior points belong to different middle chains, a common upper point can be chosen in the upper rational block and a common lower point in the lower rational block. This verifies the strengthened F3 at 156-1/007 and 013, as well as its original form.

## 2. An arbitrary retained-support restriction can destroy F4

### Construction

Let

\[
P=A\amalg M_0\amalg M_1\amalg B,
\]

with

\[
A=\mathbb Q\cap[0,1),\quad
M_\sigma=(\mathbb Q\cap(1,2))\times\{\sigma\},\quad
B=\mathbb Q\cap(2,3].
\]

Within each block use the rational order; every element of \(A\) is below both middle blocks and every element of either middle block is below \(B\); the middle blocks are mutually incomparable. The potential branching and merging levels \(1,2\) are absent. Take all nondegenerate order intervals as segments.

### Ambient axioms

- **Density and F1–F2:** Rational density works within blocks. Between comparable blocks, choose a point closer to the omitted endpoint in the source or target block. The general interval argument proves F1–F2.
- **F3, its strengthening, and F5:** Every point other than \(0,3\) lies between points of its own rational block and is regular. Positive endpoint segments share a short positive interval in that block, negative ones share a short negative interval, and the two germs differ. Thus every regular point has exactly two branches; \(0,3\) are singular one-branch points. Common local bounds inside a larger interval exist near its endpoints, including when the interior contains both middle chains.
- **F4:** Same-direction endpoint intervals have nontrivial overlap; hence the premise of intersection only at a regular endpoint forces opposite directions. The unique full order interval between the outer endpoints is the required gluing.
- **F5′ directly:** Choose two sufficiently close rational-block points around a regular point lying in two interval interiors. Their interval gives a smaller interior contained in both.
- **Both F6 formulations:** The global extrema supply bounds. At \(x<3\), all positive endpoint segments lie in \([x,3]\) and all their interiors lie in \([x,3]^\circ\). At \(x>0\), use \([0,x]\) for negative endpoint segments. Thus ambient F6 holds even in its whole-support version.

### Restriction failure

Choose \(z=(3/2,0)\), \(I=[0,z]_P\), \(J=[z,3]_P\), and

\[
P'=I\cup J=A\amalg M_0\amalg B,
\qquad S'=\{K\in S(P):K\subseteq P'\}.
\]

This is exactly the rule of 156-1/010: keep original segments whose whole supports are contained in the new set; do not replace every original support by its intersection with that set. Both \(I,J\) survive and meet only at \(z\), with their endpoint sets meeting only there. The point \(z\) remains regular in the restricted model because \([(7/5,0),(8/5,0)]\) survives and contains it in its interior.

The only original segment with endpoints \(0,3\) is \([0,3]_P=P\), which contains the omitted middle chain \(M_1\). It is absent from \(S'\). Hence the restricted model fails the existence part of F4. The failure does not depend on losing divisibility, making the gluing point singular, or omitting ambient F6.

### Conclusion and bounded repair

The unrestricted preservation assertion at 156-1/010 fails for the interval-support specification with the explicit branch convention above; even ambient F6 does not rescue it. Closure of \(P'\) under the original F4 gluing supports is a sufficient additional requirement for that step; order-convexity is a stronger convenient sufficient condition in these interval examples. Defining new supports by intersections is a different operation requiring its own checks, notably of divisibility.

Suggested note: quote “les axiomes F1–F5 sont satisfaits” (010), alongside “on n'affirme pas égalité!” (008). The fork-and-rejoin interval model satisfies F1–F6, but \(P'=[0,z]\cup[z,3]\) loses the only original segment with endpoints \(0,3\). This is a counterexample to the retained-support closure claim, not a proposed transcription correction.

## 3. A clean locally bifiltered connected fork which fails interior-F6

Let

\[
Q_* = Q_0\oplus(Q_1\amalg Q_2),
\]

where each \(Q_i\) is a copy of \(\mathbb Q\), every point of \(Q_0\) is below each point in \(Q_1,Q_2\), and the two upper blocks are incomparable. Take all nondegenerate order intervals.

### Order-theoretic checks

The order is dense and has no extremal points, since every point has smaller and larger points within its block. It is locally filtered in both directions. If \(x<y_1,y_2\) and \(x\in Q_0\), choose \(x<y\in Q_0\) below those \(y_i\) that also lie in \(Q_0\); if neither lies there, any larger point of \(Q_0\) works. If \(x\) is in an upper block, all larger points are in that same rational chain. The dual condition follows by choosing a point in the block of the specified upper bound.

Every point is regular with two branch germs; the interval argument verifies F1–F5 and strengthened F3. The model is connected in the precise segment-generated equivalence-relation sense of 156-1/015: every point shares an interval with a point of \(Q_0\), connecting any two points through at most two such relations. It is globally downward directed, using a sufficiently small point of \(Q_0\). It is not globally upward directed, since a point of \(Q_1\) and one of \(Q_2\) have no common upper bound.

### Interior-F6 fails

Choose \(x\in Q_0\), \(a\in Q_1\), \(b\in Q_2\), and set \(I=[x,a]\), \(J=[x,b]\). They have the same positive branch at \(x\): any \(y\in Q_0\) larger than \(x\) lies in both interiors and gives the same initial interval \([x,y]\). But each interior contains points of its own upper block, and any positive endpoint interval at \(x\) can reach at most one upper block. No negative endpoint interval contains even their positive initial interval. Thus there is no \(K\) satisfying the displayed interior-F6, independently of any demand to include the other endpoints.

### Scope relative to 156-1/021–022

This fully specified example realizes the live ordinal-sum idea on 022. It explicitly uses two nonempty upper pieces and ensures that every point has smaller and larger neighbors, rather than relying on the existential quantifier written in the scan. It therefore proves the local-versus-global warning without silently changing that quantifier or transferring the cancelled draft's cardinality condition to the live passage. It also shows exactly what F6 excludes.

## 4. Interior-F6 is weaker than the unqualified whole-support restatement

Let

\[
R=(\mathbb Q\cap[0,1))\amalg\{u,v\},
\]

with the usual rational order, every rational below both incomparable maxima \(u,v\), and all nondegenerate order intervals as segments.

### Verification

Every interval is a dense chain; one ending at a formal maximum is a rational tail with that maximum attached. F1–F2 follow from the interval argument. Rational points in \((0,1)\) are regular with two germs, while \(0,u,v\) are singular with one germ. Same-direction segments share a short rational interval, opposite directions meet only at the endpoint, so F3–F4 hold; small rational intervals verify F5/F5′. Rational density below either maximum proves strengthened F3.

Interior-F6 holds globally. At rational \(x\), every positive interior contains only rational points above \(x\), all of which lie in \([x,u]^\circ\), including when the original endpoint is \(v\). Negative intervals at rational \(x>0\) are bounded by \([0,x]\). At endpoint \(u\), all negative interiors are bounded by \([0,u]\), and likewise for \(v\). These cases cover every branch.

Now let \(I=[0,u]\), \(J=[0,v]\). Then

\[
I^\circ=J^\circ=\mathbb Q\cap(0,1).
\]

The segments define the same branch at \(0\), and interior-F6 is witnessed by \(K=I\). Yet no segment contains both \(u,v\), since they are incomparable maximal points. Hence no segment contains \(I\cup J\).

### Conclusion

The unqualified whole-support assertion following “Ou encore” on 156-1/023 is not equivalent to the displayed interior-F6 when singular other endpoints are allowed. This leaves the initial interior axiom intact and agrees exactly with the margin's exemption of the other endpoints from membership in \(K\). Both omitted endpoints in this example are singular. A stronger full-support claim requires an additional hypothesis.

## 5. Positive repair: regular other endpoints suffice

Suppose F1–F5 and interior-F6 hold, and \(I,J\) share endpoint \(x\) and a branch there. Suppose their respective other endpoints \(y,z\) are regular. F4 Corollary 1 at 156-1/008 permits extending \(I\) past \(y\) while preserving endpoint \(x\), producing \(I^+\) with \(I\setminus\{x\}\subset(I^+)^\circ\); likewise extend \(J\) past \(z\) to \(J^+\). The extensions retain their common initial subsegment, so they still share the same branch at \(x\).

Apply interior-F6 to \(I^+,J^+\). The resulting \(K\) has \(x\in\delta K\) and contains \((I^+)^\circ\cup(J^+)^\circ\) in its interior. Therefore \(I\cup J\subseteq K\), since every original point except \(x\) lies in those enlarged interiors and \(x\) itself is retained as an endpoint. Regularity of \(x\) is unnecessary. This establishes a precise sufficient repair of the stronger implication, whereas the singular-end example proves that no unqualified equivalence follows.

## Context comparison and provenance

Actual context searches under `F1`, `F6`, `filtrant`, `restriction`, and `branch` locate no established result concerning these particular segment-axiom issues; the isolated `F1` hit is part of unrelated note identifiers. Related **STRATA A.12**, **STRATA A.4**, and **BISITE G.10** concern poset realizations and exits, not these axioms, and are neither re-derived nor contradicted. These examples add checks relevant to the unchecked **WG2 B15 (§1.2)** / README refinement proposal and distinguish local compatibility from global gluing or directedness. No register status is changed.

All mathematical checks are self-contained. The frozen transcription's uncertain symbols and exceptional statements remain untouched, including the existential quantifier on scan 022 and the interior/full-support distinction on 023.
