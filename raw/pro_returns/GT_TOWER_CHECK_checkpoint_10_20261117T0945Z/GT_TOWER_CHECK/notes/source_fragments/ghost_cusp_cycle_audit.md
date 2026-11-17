# Independent audit: the finite cusp-cycle detector

The exact source is
\[
R=\langle a,d\mid a^2=1\rangle=C_2*\mathbf Z.
\]
Let \(q:R\twoheadrightarrow Q\) be a finite quotient in which \(q(a)\) has order two, put \(K=\ker q\), and put
\[
Q^+=R/[K,K]K^2.
\]
The following construction and proof verify the cusp-centralizer step used by the pending finite E.44 compiler. They do not assert the later compiler conclusion.

## Exact graph and homology map

Use the HNN tree for the presentation above: vertices are \(R/\langle a\rangle\), oriented edges are \(R\), and the edge indexed by \(r\) runs from \(r\langle a\rangle\) to \(rd\langle a\rangle\). Left multiplication preserves the chosen orientation. The reduced-word normal form in \(C_2*\mathbf Z\) proves that this connected graph is a tree. Since \(q\) is injective on \(\langle a\rangle\), \(K\) acts freely on its vertices and edges.

Thus the finite quotient graph has vertices \(Q/\langle q(a)\rangle\), oriented edges \(Q\), and the same incidence formula. Its fundamental group, with base vertex \(\langle q(a)\rangle\), is literally \(K\). In particular the conjugation action of \(R\) on
\(K/[K,K]K^2\) is its left deck action on
\[
H_1(K,\mathbf F_2)=\ker\bigl(\mathbf F_2[Q]\longrightarrow
\mathbf F_2[Q/\langle q(a)\rangle]\bigr).
\]
There are no two-cells, so the displayed map from homology into oriented edge chains is injective.

## The cusp cycle and its exact stabilizer

Write \(\delta=q(d)\) and \(m=\operatorname{ord}(\delta)\). The actual element \(d^m\in K\) is represented by the closed path with consecutive oriented edges
\(1,\delta,\ldots,\delta^{m-1}\). Its homology class has edge chain
\[
c_d=\sum_{i=0}^{m-1}[\delta^i].
\]
Every edge occurs once, including when \(m=1\). Hence \(c_d\neq0\) and its support is exactly the subset \(\langle\delta\rangle\subset Q\). An element \(x\in Q\) fixes this chain precisely when
\(x\langle\delta\rangle=\langle\delta\rangle\), which is precisely \(x\in\langle\delta\rangle\).

An element of \(C_{Q^+}(d)\) fixes \(d^m\) by conjugation. Under the exact homology map, its image in \(Q\) therefore fixes \(c_d\), and belongs to \(\langle\delta\rangle\). Conversely each \(\delta^i\) is the image of \(d^i\in C_{Q^+}(d)\). This proves the exact equality
\[
\operatorname{im}\bigl(C_{Q^+}(d)\longrightarrow Q\bigr)
=\langle q(d)\rangle.
\]
The same support argument applies to an equality \(z d z^{-1}=d^\lambda\) in \(Q^+\) for an odd integer \(\lambda\): it sends \(c_d\) to \(\lambda c_d=c_d\). This statement uses the equality in the refined quotient itself.

## Size and the second cusp

For \(n=|Q|\), the graph has \(n\) edges and \(n/2\) vertices, so \(K\) is free of rank \(1+n/2\), and
\[
|Q^+|=n\,2^{1+n/2}.
\]
For the actual cusp-swap involution \(S\), with \(S(d)=v\), replace \(q\) by the image of \((q,q\circ S)\). Its kernel is \(S\)-stable, as is \([K,K]K^2\). The same construction consequently detects both \(d\) and \(v\) in the same actual finite quotient, with their respective projection maps.

Audit conclusion: the graph, chain, stabilizer, converse, and finite-size arguments all check. No numerical calculation is needed for this lemma. In particular no completion, finite centralizer equality in a previous quotient, or assertion about the later pentagon compiler is being inferred.
