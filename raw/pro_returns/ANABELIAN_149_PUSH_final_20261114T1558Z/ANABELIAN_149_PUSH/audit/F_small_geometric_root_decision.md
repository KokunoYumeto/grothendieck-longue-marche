# Root acceptance of F.49

**Decision: integrate the complete sufficient theorem, with both strict
examples and all limits retained.** Root authored the nine-section
candidate, then read both complete independent reviews:
`audit/F_small_geometric_topos_review.md` and
`audit/F_small_geometric_finite_field_review.md`. Both accept the theorem.
The optional explicitness corrections concerning roots in the relative
constant field and the dense product tail were inserted in the candidate
before integration. The separate universal-tripod example was also read
in full and accepted by both reviewers.

The exact approved conclusion is as follows. Let D/Q be finitely
generated of positive transcendence degree, and k/D algebraic Galois with
Qbar contained in k. If k is Hilbertian, every finitely generated L/k
satisfies the actual closed-point-preserving reconstruction convention.
If Gal(k/DQbar) is small, Hilbertianity follows and every
positive-transcendence subfield of every such L reconstructs. The core
claim alone does not assert this arbitrary-subfield conclusion without
the additional smallness argument.

The proof checks the precise additional inputs rather than replacing the
full étale topos by its fundamental group. The normal model L=Fk gives
G_L normal in G_F. Commuting automorphisms and all roots of unity give
D(E*) contained in k*, which is the only scalar control required; k*
is not asserted divisible. Hilbert specialization keeps the entire
arithmetic finite-cover degree. Integral residues are obtained with a
single finite norm field chosen before the Kummer modulus. The
generalized Albanese and Tate-Hom steps use finitely generated Q-fields
only. Unit reconstruction is followed by the translated-function
argument proving equality of actual geometric point functions. The
previously opened CHW reduction is then applied to the full topos.

In the small case, the relevant geometric group after finite-type base
change is an open subgroup. The bounded-degree subextension compositum is
finite, allowing full-degree Hilbert specialization disjoint from the
whole normal extension. For arbitrary positive-transcendence subfields,
regularity identifies the geometric normal-closure group as a quotient,
so the proof does not use the false assertion that every closed subgroup
of a small group is small.

The polynomial example has geometric group product_(m>=2) A_(2m+1).
The universal-tripod example has group Fhat2. Both are small, and every
open subgroup in either example has alternating quotients of unbounded
degree. The changed-algebraic-model argument therefore excludes the
entire previous F.46 formation class, not just one preferred model. The
tripod example has all roots of t and1-t but does not contain a square
root of t-2, illustrating why the weaker divisible-kernel inclusion is
the appropriate hypothesis.

Root independently opened the exact primary Hilbertian statements and
the SGA1 comparison passages, recorded in
`audit/F_small_geometric_literature.md`. Preservation of Hilbertianity
under small Galois extension is explicitly credited as known. The
focused reconstruction searches found no exact prior statement, which
does not establish novelty or priority.

The theorem supplies no necessary condition of Hilbertianity or
smallness, no converse to F.48, and no intrinsic classification of all
characteristic-zero reconstruction fields. F.9 remains unresolved.
Combined-source readback, compilation and visual QA are separate from
this mathematical acceptance and will be recorded when completed.

## Integrated-source readback

Root read the entire integrated `sections/F_small_geometric_extension.tex`
after integration, including all eighteen displayed equation tags and
both strict examples. The text includes the relative-constant root
clarification and the continuity argument for the product tail, credits
the known small-extension Hilbertian input, and retains the stronger
subfield conclusion only under its separately proved smallness
hypothesis. The readback passes against both accepted independent
reviews. The final combined build and visual approval are recorded
separately.
