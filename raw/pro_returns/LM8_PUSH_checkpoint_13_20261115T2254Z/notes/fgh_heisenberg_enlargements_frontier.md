# Further Heisenberg covers: exact consequences and remaining gates

Notes only, not a new registered statement. The canonical A61–A62 sources are frozen for checkpoint11. The following even-enlargement argument is an application of their conclusion and the already audited tame model argument; it has not received a separate complete independent audit.

## Every even torsion enlargement

Let p be odd, let C_p be the actual curve z^p=psi_p(x), and take m=2^a m_0 with a≥1 and m_0 odd. Consider the actual finite etale cover

`C_p minus q^{-1}(E[pm]) -> E minus O`, with map `[pm]q`.

At residue2 the elliptic curve has potential good supersingular reduction. Its p-torsion sections remain disjoint. The degree-p cyclic map q is tame, branched only along those sections, so after a finite extension its actual normalization has a smooth proper model and retains q. Write n=pm_0. All generic E[2^a n] points over one reduced E[n] point form a group of size4^a.

At a target reduction outside E[p], the special q-fibre has p distinct etale points. Each receives exactly4^a marked sections, by the actual local etale sections. At a target reduction in E[p], its one ramified source point receives exactly `1+p(4^a−1)` marks: one from the original ramified p-torsion target, and p from each of the other4^a−1 targets. Every cluster therefore has at least two marks. Marked separation puts each cluster on a rational tree attached to the smooth proper source. The hypotheses of A42 hold at every chosen mark, for every coefficient prime and packet.

Normalizer recognition passes from the original affine C_p to this further puncturing by A11: a proposed noncuspidal normalized pro-prime cyclic subgroup has nonzero proper homology. The open immersion has the same proper compactification, so the image remains nonzero and infinite in the original curve, where A61–A62 force it peripheral, contradicting its nonzero proper homology. This argument does not require the enlarged cover's Galois closure itself to be nilpotent.

This gives a concrete extension beyond the original marked sets, but A53 already supplies infinitely many enlargements on every compactification. It is not currently being registered as a separate main-task advance.

## Odd enlargements require a separate critical-centre check

The residue-p models of A61–A62 have positive-genus tails over the zeros of the actual critical function. Extra odd-order torsion marks can only be treated by the same rational-cluster argument after verifying that their reduced images avoid these critical centres, or after analyzing the marks on the tails. The special support cannot be inferred just from the original p-torsion case. No all-m enlargement theorem for every p is asserted here.

## Higher prime-power Heisenberg level

The exact characteristic-zero division identity is

`psi_{mn}(P)=psi_m([n]P) psi_n(P)^{m^2}`.

Its divisor and leading Laurent coefficient both give this equality. For n=p^r it supplies actual maps between intermediate Kummer function fields, for example

`w=z^{p^{r−1}}/psi_{p^{r−1}}(P)^p`,

with `w^p=psi_p([p^{r−1}]P)` on `z^{p^r}=psi_{p^r}(P)`.

This identity alone does not give the stable model of the higher-level curve. The upper cyclic extension remains wildly ramified, and neither compact type nor the required rational cusp paths follow from the degree-p model by a fixed-point or quotient argument. A59 supplies the normalizers whenever the actual finite geometric Galois closure is nilpotent, but the all-coefficient fixed subgroup still needs its own geometric comparison. No higher-level fixed-group theorem is promoted from these identities.
