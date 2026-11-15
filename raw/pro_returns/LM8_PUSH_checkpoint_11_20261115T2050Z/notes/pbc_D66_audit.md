# Independent audit of D.66

Verdict: **PASS**, 2026-11-15. I read `notes/de_alexander_baire_draft.tex` in full and checked the actual finite-action and integral local-vanishing dependencies in D.35, D.42, D.43 and D.47, together with the completed cusp construction of D.60.

## Parameter topology and finite data

Kummer theory gives the stated intrinsic completion `c0(primes,Z5)`: modulo each power of five the support is finite, and the compatible finite-support residues are exactly the c0 families. Fixed compatible prime-root cocycles give a uniformly convergent continuous representative for every such family, since each Kummer cocycle is integral and each coefficient tends to zero. Completeness and separability in the uniform five-adic topology are correct.

Both the support set `S_r` and the actual action on `W_r` are constant on a coset of `5^r K^2`. The draft's support set is slightly larger than the sharp D.47 set; this is harmless and makes the local constancy immediate. D.47 proves the stronger needed assertion for **actual reduced cocycles**, not only their cohomology classes. The binomial estimate makes all inertia values vanish at this precision, uniformly for every integral cocycle.

The set `E_r` is finite because it consists of cocycles with a fixed finite coefficient action and finite ramification set. No transition maps between arbitrary `E_r` sets are assumed.

## Open dense witness conditions

An exceptional cocycle has a nonzero translation in the kernel of its finite linear action. Conjugation preserves the identity linear part and nonzero translation, so the requested Frobenius tests are genuinely conjugacy-class conditions in the actual finite affine image.

At each precision there are only finitely many exceptional cocycles. On the fixed finite-data coset, a chosen witness is stable on a smaller open parameter neighborhood because its nonzero coefficient is an open condition. Thus `U_r` is open.

The density argument works with **every fixed second coordinate**. Choose `M >= max(N,r)`, use Chebotarev to pick distinct witness primes outside the finite support set and outside the finite set where the old first-coordinate coefficient is not divisible by `5^(M+1)`, and add `5^M` at each chosen prime. This preserves all finite data and avoids cancellation exactly. There is no circular requirement that the prime have already been ramified: the finite Frobenius test is selected first, and the deeper parameter coefficient is added afterward.

The first nonzero-inertia condition is also open and dense in each fixed-second-coordinate slice. Baire therefore applies globally and separately in every slice; it does not require intersecting an uncountable family of dense open sets indexed by the second coordinate.

## From the witnesses to zero integral cohomology

For an integral cocycle, an exceptional reduced cocycle would have a witnessing prime with nonzero abelian inertia. D.43 makes its integral local restriction an actual coboundary. The witnessing Frobenius has identity reduced action, so its reduced cocycle value must be zero, contradicting its selection.

Hence every reduced cocycle kills the corresponding reduced action kernel. The integral cocycle kills the full kernel and descends continuously to the compact actual operator image. This uses the compact quotient map, not an abstract image identification.

At a nonzero-inertia prime, the monomial multiplication subgroup `N` is closed and normal under every actual semilinear Alexander operator. It has zero invariants because the module is rank one over the integral domain `Z5[[u,v]]` and the monomial is nontrivial, including for nonprimitive exponent vectors. Subtracting the integral local coboundary kills the cocycle on `N`; comparing the cocycle identities on `ng = g(g^-1ng)` then forces every value to be `N`-invariant, hence zero. This proves actual cohomological vanishing without replacing an integral obstruction by rational vanishing.

## Refinements and section scope

Finite-support parameters form a countable union of closed nowhere-dense submodules, so the infinite-ramification refinement is valid both globally and in each fixed-second-coordinate slice.

For the zero cusp packet, every `(a,0)` already has a full completed cusp section. D.35's exact fibre torsor has no additional abelian stabilizer quotient, so zero H1 gives the stated singleton. The puncture permutations transport the conclusion to the other two packet parameter spaces.

The local condition at the single prime two is the union of three closed lines in `Z5^2`. The coordinate projection from `K^2` is open and continuous. Its preimage is therefore closed and nowhere dense. The draft correctly distinguishes generic vanishing of the homogeneous cohomology from existence of an arbitrary section lift; singleton existence is asserted only in cusp packets.

## Opened primary source

I independently reopened J. S. Milne, *Class Field Theory*, version 4.03, Chapter V, Theorem 3.23 (printed page 164, PDF page index 172), which gives positive density for each conjugacy class in a finite Galois group. This is exactly the source needed for the fresh-prime selection in the actual affine representation.

URL: https://www.jmilne.org/math/CourseNotes/CFT.pdf

Verified browser references: `turn796view0`, `turn797view0`.

No mathematical gap or necessary correction found. No new computation is required for this category argument.
