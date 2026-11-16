# Root complete proof and primary-source audit of A.78

**PASS; approved for canonical integration after the complete independent
PBC and DE audits.** Root read the full initial composite proof, the
complete amended model-comparison passage, and the exact diff to the
formal A.78 statement. The formal candidate SHA-256 is
`5cbddad1fa57b1e2176b77761bada8c31814e71e083b6d68deefef184106ad9b`.
The amended composite has SHA-256
`76f07253e404516127ff08ce569651318e136ff80f0c95a06a25213d6c1c6dfb`.
This is a structural geometric proof; no finite computation is claimed
to prove it. All earlier versions and the model-gate correction remain
retained.

## The single horizontal branch is killed at the correct valuation

The base has genus at least one and good reduction. Relative Serre
vanishing for a horizontal ample divisor disjoint from the chosen
section gives a global rational function whose first jet is a unit
local parameter at that section. Prescribing its value zero and its
first derivative a unit makes its local zero divisor exactly the
section. All other zeros and poles avoid the chosen special point.
The finite extension z^e=t is connected of degree e because the
valuation of t at the horizontal section is one. The inertia order
e is a power of p, and cyclicity is justified at this horizontal
discrete valuation, whose residue characteristic is zero.

The completed local algebra of the normalized new base is literally
R[[z]]. It is smooth over R and has a unique underlying point over
x. The other generic branch points cannot specialize to this new
point, once the actual proper map back to X is retained. At the
horizontal valuation the base-change ramification index equals e,
so the characteristic-zero case of Abhyankar's lemma removes the
original inertia. It does not remove vertical ramification or claim
that the two-dimensional source normalization is etale. That
distinction is essential to the proof.

Any connected component of the normalized generic pullback is
Galois over the new generic base with a subgroup of the original
p-group: it is the compositum field of one component, and the
decomposition subgroup acts as its full Galois group. It also
maps finitely and surjectively to the original generic source.
No new branch of this cover is created over a point where the
old cover was etale, by stability of etaleness under base change.

## The actual model map and the unique fibre are retained

This was the principal correction requested by root. The new
semistable base must have an actual map to X, with fibre over x
equal to the one smooth point x'. The generic function-field
diagram alone would not justify the later component comparison.

After any finite extension of the coefficient DVR, the local
ring R[[z]] remains smooth. The normalization can be resolved
away from this open neighbourhood. Its main residue field is
k(X_s)(tbar^(1/p^a)); since d(tbar) is nonzero, this is the
full purely inseparable extension of degree p^a. For a smooth
curve over the perfect residue field this is the corresponding
Frobenius inverse field, whose smooth model has the same genus.
Thus the component through x' has positive genus and cannot
be contracted as an exceptional rational curve.

After a finite extension giving semistable reduction, a proper
regular model contracts to the minimal regular model, which is
semistable. Each contracted exceptional curve is rational and
maps constantly to the smooth positive-genus X_s, by Luroth's
theorem. Consequently the actual map to X descends at each
contraction. The proof gives a precise graph argument: its
proper graph image over the contracted normal surface has
one-point fibres, hence is finite birational and therefore an
isomorphism. There is no unsupported descent of a rational map.

Initially no exceptional curve meets x', because its
neighbourhood is already smooth over R. Each contraction is
an isomorphism near x'; induction preserves this property.
The positive-genus main component remains, and the fibre over
x remains exactly x'. Separating the other branch or auxiliary
marks requires changes only away from this neighbourhood.
Equivalently, the additional rational unmarked blowup tree at
x' contracts back to the same smooth point. The required
proper map, unique fibre and completed local ring are all
explicit in equation SB.2a of the reviewed draft.

## Raynaud applies to the new nonmarked point

Choose the new branch marking away from x' and, if necessary,
auxiliary sections away from it. Yang's existence result is
for a cover over the specified pointed semistable base, not
an assertion of a finite map between arbitrary stable models.
It supplies the actual pointed semistable covering of X'.
The nonmarked smooth-point theorem then gives rank zero for
its entire vertical fibre over x', in particular for each
positive-genus component there. Adding or forgetting the
auxiliary markings changes only rational exceptional pieces.

For an old positive-genus component B over x, resolve the
rational map from the new semistable source to the old one.
After resolving nodal surface singularities, elimination of
indeterminacy uses point blowups of a regular surface. Their
exceptional curves are rational; the common resolving model
need not itself have reduced special fibre. The resulting
proper map is surjective because its generic map is finite
surjective. Some component therefore dominates B. It cannot
be an exceptional rational curve: no rational smooth curve
dominates a positive-genus smooth curve, even inseparably.
It is the strict transform of an existing positive-genus
component of the new semistable source.

Commutativity of the actual morphisms and the unique fibre
over x place this component above x'. Its rank is zero.
The induced map of smooth component normalizations forces
the rank of B to be at most that rank. Purely inseparable
maps preserve p-rank; for the separable part, the Jacobian
norm is surjective and the rank cannot increase on an
abelian quotient. This proves the local assertion for every
old positive-genus component, not merely for a terminal tail.

## Every main component has rank zero in the one-branch case

For the global conclusion, potential good reduction of the
source Jacobian follows separately from the nilpotent
ramified-cover theorem: the base is good, the branch divisor
is a single etale section, and generic characteristic zero
ensures the required generic tameness. Thus the stable graph
is a tree. The local theorem covers all components contracted
to the branch point, and the original nonmarked theorem
covers those contracted elsewhere.

For a main component, apply Raynaud's Proposition 1 only on
X minus the horizontal section. On this regular open
surface the ramification support, if nonempty, is the
single smooth irreducible vertical divisor. This verifies
the geometrically unibranch ramification hypothesis and
avoids the horizontal/vertical crossing. The inertia
quotient gives an actual connected etale D/I-cover of the
punctured special base; the original residue component is
radicial over it. After smooth compactification the quotient
is a connected p-group cover branched at most at the one
missing point. The unramified vertical case is included.

With d=|D/I| and r the number of points above the missing
point, Deuring--Shafarevich gives f(B_0)-1=-d+(d-r)=-r.
Since r>=1 and f(B_0)>=0, r=1 and f(B_0)=0. This includes
the unramified case, where r=d forces d=1. The radicial
comparison preserves rank, without needing its degree to
equal |I|. Hence every main component has rank zero. The
component ranks and graph Betti number are all zero, proving
the asserted potentially good rank-zero Jacobian.

## Primary passages actually opened and read

Root freshly read Yang's Definition 1.5, Proposition 1.6
and its model convention, Theorem 1.9, and the rank and
Deuring--Shafarevich formulas in the author's paper:
<https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/PSS.pdf>.
Retrievals include `turn1230view0`--`turn1230view2`,
`turn1231view2`, and `turn1235view0`. The marked-point warning
is respected by constructing a genuinely nonmarked point
on the new base. It is not silently extended across a mark.

Root freshly read the original Raynaud Proposition 1 on
printed pp.179--180, recovered as `turn1226view0` from the
previously opened primary publisher preview after a direct
URL request failed. The failure is recorded, not counted
as a successful source check. Root also freshly read
Lehr--Matignon Theorem 6.13 in `turn1236view1`, at
<https://arxiv.org/pdf/math/0411059>.

The exact Stacks lemmas were all freshly opened and read:
<https://stacks.math.columbia.edu/tag/0BRM> (horizontal
ramification removal), <https://stacks.math.columbia.edu/tag/0C5H>
(regular-surface indeterminacy), <https://stacks.math.columbia.edu/tag/0C5Q>
(common regular models), <https://stacks.math.columbia.edu/tag/0CD9>
(contraction to a minimal regular model), and
<https://stacks.math.columbia.edu/tag/0CDG> (semistability
of that model). Refs are `turn1234view0`--`turn1234view2`
and `turn1240view0`--`turn1240view1`. These exact primary
statements support the model argument independently of the
optional general textbook citation. PASS.

Root additionally opened and read Stacks Tag 0CDE, Lemma 55.14.3, as `turn1248view0`: nodal surface singularities resolve by closed-point blowups while retaining a nodal curve over the DVR. This confirms the precise preliminary source-resolution step.
