# Proved extension of C62 to the actual principal operator fibers

This note applies the already proved word triangle to another explicitly constructed foliation. It does not assert a lift of a moving base contraction or an ambient extension of the intrinsic C33 contraction.

Let O be an original open orbit of the loop-generated group G, and let C_O be the full local centralizer of G restricted to O with its actual compact-open topology. Suppose its dimension is one, and put A=C_O^0. C30 and C33 prove that C_O is a free proper Lie transformation group and construct a principal bundle

\[
\pi_0:O\longrightarrow B=O/A.
\]

Here A is the additive line or circle, B is a line or circle, and the pair of circles is excluded because O is noncompact. C33 supplies an actual section and the homeomorphism

\[
\Theta:A\times B\longrightarrow O,\qquad
\Theta(a,b)=a\,s(b),\qquad \pi_0\Theta(a,b)=b.
\]

## The original universal cover and its exact labels

Write η_A:R→A and η_B:R→B for the identity in a line factor and the specified quotient by Z in a circle factor. The displayed map

\[
p_*(u,v)=\Theta(\eta_A(u),\eta_B(v))
\]

is a covering from the simply connected plane, hence a universal covering. If p_O:X_O→O is the previously chosen universal covering, choose the point above Θ(0,0) in each cover. The unique based covering isomorphism χ:X_O→R² satisfies

\[
p_O=p_*\chi.
\]

It is a homeomorphism: the inverse is the unique based lift of p_* through p_O, and the two compositions are identity lifts with the same basepoint. Define the actual real quotient

\[
F=\operatorname{pr}_2\chi.
\]

Its connected proper fibers are horizontal lines in this explicit chart. The original deck labels are retained by

\[
\chi\delta\chi^{-1}(u,v)
 =(u+m_A(\delta),v+m_B(\delta)),
\]

where m_A or m_B is identically zero in each line factor, and the circle factor has its integer label determined by the original deck transformation. There is at most one circle factor. In particular

\[
F\delta=F+m_B(\delta).
\]

This is an equation for each original δ, not a replacement of its label by an unchosen covering generator.

## The original loop and all local operator components

Every f_t|O commutes with A. In the actual product chart its exact form is therefore

\[
(a,b)\longmapsto(a+\varphi_t(b),\psi_t(b)),
\]

as in C33.11. Its based source lift has the form

\[
\chi\widetilde f_t^O\chi^{-1}(u,v)
 =(u+\widetilde\varphi_t(v),\beta_t(v)),
\]

where β_t is the actual based real lift of ψ_t and is increasing. The fiber translation lift is fixed by the based source lift, including any nonzero integer accumulated in a circle fiber. No endpoint closure is needed for the C62 triangle argument. Every original deck map commutes with the source lift, by the same deck-valued commutator path used in C62.

Every q∈C_O normalizes its characteristic identity component A and hence preserves the A-orbit partition. Its induced map on B is the actual map of the quotient group C_O/A. C33 proves that this group acts freely and properly on B. A decreasing line or circle homeomorphism has a fixed point, so no decreasing element occurs in this induced group. Its source lifts consequently preserve F-fibers with increasing induced real base maps. The full affine fiber component equations in C33, including a negative conjugation coefficient on A, are retained; no such coefficient is discarded by the base orientation observation.

The original stabilizer H_O maps into C_O by restriction, with the precise kernel of C30.4. No identification of H_O with C_O is made. For an operator h transporting O to O', conjugation by h gives an actual topological group isomorphism C_O→C_O' and carries A-orbits to A'-orbits. Thus the principal partitions are transported along all original operator orbits. The projected global word comparison is automatically natural under h because h commutes with every f_t.

## Exact containment and uniform consequence

The source hypotheses used in the C62 proof are now all verified: the original cover, one actual product homeomorphism, a real quotient with connected proper fibers, the increasing induced base maps of the original lifted path, and the original deck equations. For any x∈O and two original prefix times whose values have exactly the same F-level, the compact interval I in that real fiber satisfies

\[
I\subset
\{\widetilde f_u^O(\widetilde f_v^O)^{-1}
  \widetilde f_a^O\widetilde x:0\le a\le v\le u\le1\}.
\]

Projection gives exactly

\[
p_O(I)\subset
\{f_u f_v^{-1}f_a(x):0\le a\le v\le u\le1\}.
\]

The inverse-path version is the projected word f_u^(-1)f_vf_a^(-1). For arbitrary varying dimension-one principal orbits with x_n→x, the one compact global word map gives the same uniform compact containment and same-G-orbit accumulation as C62, and complete shrinking when x is fixed by G.

This application does not require any actual global quotient to a nonopen orbit. In particular it applies when the full nonopen-target family is empty. It concerns the already established principal orbit fibers, and does not assume that this foliation extends across the frontier. The remaining moving-base lift and its prescribed nonfixed boundary values are unchanged.
