# Independent full audit of D91

Status: **PASS**, 2026-11-16. The complete written proof, owner certificate,
PBC's affine-stabilizer derivation and stabilizer certificate were read.
The final literal `+in` typo was corrected by the owner before this record.
No mathematical correction is required.

## Actual arithmetic and module comparisons

The degeneracies and previously proved ranges are separately imported at
their stated scope. In the new range `r < m < N`, the common valuation
graph is retained, the actual difference ideal is `(P,q_m)`, and the source
keeps its `q_r` generator weight. Its scalar relation is `5^(N-m) F`, not
an unjustified replacement by a uniform coefficient quotient. The target
is the actual torsion-free local invariant module from D77.

I checked the annihilator calculation in the original power-series domain:
evaluation at `u=0` forces the required factor of `u`, cancellation gives
the norm generator, and cancellation of `F` identifies its exact coefficient
order. The extra axis-intersection line has tame weight three; the
remaining comparison kernels have weights two and one. Thus all the
discarded pieces are killed by an actual tame unit, including their
homology, rather than merely having zero rational rank.

The zero-snake proof works over every coefficient reduction: invariants
of the boundary quotient lie in `uQ`, and `uT -> uQ` is an equivariant
isomorphism because `(u) intersect (vw) = (uvw)`. This injects the entire
infinite layer, including its torsion, into the actual source coinvariants.

## Exact boundary calculation and natural map

The affine semidirect group is the actual finite translation group with
the full unit action. Continuous Shapiro is applied to the discrete dual
of a finite permutation module. Pullback of functions restricts stabilizer
characters; after duality the map is stabilizer inclusion, not transfer.
For a nonzero shell the inclusion has coordinates `(unit,5^h)`, giving
one cyclic group of order `5^(h+min(b,k))`. The lower zero orbit contributes
nothing. This retains the nonsplit `C25` in the first middle example.

Multiplication by `u q_r` on the source and by `u` on the target identifies
the actual inclusion with the literal reduction to the orbit module.
Both diagonal half-gauges commute with `q_r`. The free orbit-kernel part
embeds and precisely the finite homology cokernel is killed. I found no
replacement of this natural map by an abstract-corank comparison.

## Finite and infinite depth

At finite depth the kernel is exactly the source torsion subgroup. Actual
restriction followed by corestriction kills the *whole* extension by
`5^e`, before exact-order lifts split its finite cyclic quotient. Only
factors of the same maximal exponent are absorbed into the infinite
product; smaller cyclic factors remain in the statement.

At infinity the operator image is compact and closed, so the stated
compact-intersection argument identifies coinvariants with the inverse
limit. The stabilized transition maps are onto, are the identity on the
free orbit quotient, and have equal finite torsion orders, hence are
isomorphisms. The coefficientwise zero-snake argument gives the actual
purity identity `E intersect 5^H M = 5^H E`. For `H >= m` this yields
`5^H M0 = 5^H E`, and exact torsion lifts follow by integral adjustment.
The map kills the layer by the literal identity
`q_r v w = P (q_r/u)` and kills its finite complement in the torsion-free
target; the free boundary part still embeds. Thus the full kernel at
infinity is identified by actual maps, with its finite torsion retained.

The zero-axis map, the separate free boundary factor, all three actual
cusp markings, the completed infinite-support parameters and the stated
rational examples agree with their imported hypotheses. No claim about
arbitrary noncuspidal abelian pairs or higher section obstructions is made.

## Executed evidence and primary check

`code/fgh_D91_certificate_rerun.py` independently reran all twelve literal
middle source matrices, two target matrices, exact norm and intertwining
identities, half-gauges, integral Smith factors and the tangent example.
Every mathematical and source-hash field equals the owner's JSON. Only
the author's elapsed-time metadata is excluded from equality. Original
outputs were not overwritten. Independent output is retained in
`notes/fgh_D91_certificate_rerun.json` and `.out`.

verified: Milne, *Class Field Theory*, II Proposition 1.11, Example 1.27(a)
and Proposition 1.30, printed pages 62, 69 and 70, respectively.
Primary URL: https://www.jmilne.org/math/CourseNotes/CFT.pdf . Freshly
opened references `turn1209view0`, `turn1209view1`, `turn1209view2`,
`turn1210view0`, `turn1210view1`. The finite-coset continuous argument is
also explicitly retained in D88. No arbitrary inverse-limit commutation
for cohomology is assumed.
