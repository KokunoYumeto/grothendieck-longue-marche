# Rejected relaxation of the whole-subgroup propagation lemma

This is a correction to a proposed proof, not a statement about the actual
icosahedral source image. The stronger stage-by-stage argument used in B.82
remains valid.

Suppose an operator satisfies `gamma^{-1}(b)=k b k^{-1}`. The correct identity is

\[
b^n\gamma(w)b^{-n}
=\gamma\bigl(kb^n(k^{-1}wk)b^{-n}k^{-1}\bigr).
\]

The middle conjugation cannot be omitted. If `k` merely belongs to a known
normalizer of the eventual orbit subgroup, the new word `k^{-1}wk` need not
belong to a shorter induction stage. For an inner source operator this is
exactly the assertion one was trying to prove.

There is an explicit free-group counterexample. Let

\[
F=F(b,h,u),\qquad \beta(b)=b,\quad\beta(h)=h,\quad
\beta(u)=bub^{-1},\qquad
\Gamma=\langle\beta,\operatorname{Inn}(h)\rangle.
\]

The two operators commute. Consequently

\[
J=\langle\Gamma\cdot u\rangle
=\langle h^k b^n u b^{-n}h^{-k}:k,n\in\mathbb Z\rangle.
\]

All conjugates `b^n u b^{-n}` are in `J`. Put `H=<h,J>`; then `H` normalizes
`J`. For the generators of `Gamma` and their inverses, the conjugator in
`gamma^{-1}(b)=k_gamma b k_gamma^{-1}` is either `1`, `h`, or `h^{-1}`, hence
lies in `H`. These are all the hypotheses of the rejected relaxation.

Nevertheless `b h u h^{-1} b^{-1}` is outside `J`. The normal closure of `u`
in `F(b,h)*<u>` is free on the elements `g u g^{-1}`, indexed by
`g in F(b,h)`. The displayed subgroup `J` uses precisely the subset of
indices `{h^k b^n}`. The reduced word `bh` is not in that subset. Thus `b`
does not normalize `J`.

There is also an elementary finite separation. Take `Q=S3`,
`b=(12)`, `h=(23)`, and the regular permutation module `A=(C2)^Q`.
In `A semidirect Q`, let `u` be the basis vector at the identity. The
automorphism `beta` acts on `A` by right translation by `b` and fixes `Q`;
this commutes with the left `Q` action, so it is an actual automorphism.
The orbit subgroup is the coordinate subspace supported on
`<h><b>={1,b,h,hb}`, whereas `b h u h^{-1} b^{-1}` is the coordinate vector
at `bh`, outside that set. This gives a finite separating quotient of
order `2^6*6=384`, so the same counterexample persists for the actual
closures in the full completion of the free group.

The exact positive statement still available is the one used in B.82:
the conjugating corrections must lie in a specified earlier subgroup
that is already normal under the retained direction. Membership in a
normalizer of the eventual source subgroup is insufficient.
