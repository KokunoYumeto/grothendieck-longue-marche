# Cartan comparison and actual compact projective duality

Root source and proof audit, 2026-11-16, for the proposed A84.

## Sources opened at the exact step

Webb, P. (2016). *A course in finite group representation theory*.
Cambridge University Press. https://doi.org/10.1017/CBO9781316677216

The author-hosted prepublication PDF was retrieved through its indexed
source and opened at Proposition10.2.1, Theorem10.2.2 and Corollary10.2.4,
with their full proofs (printed174--178). We also read the complete
projective-character vanishing proof in Lemma9.6.2 and the dual-projectivity
proof in Proposition8.5.2. Direct URL opens initially returned502; the
subsequent find and line-specific open calls supplied the actual text.
We do not describe the failed direct calls as successful reads.

Primary source:
https://www-users.cse.umn.edu/~webb/RepBook/RepBookLatex.pdf

Successful retrievals: turn770view2, turn772view0, turn772view1,
turn772view2, turn774view0, turn774view1. Official publisher metadata
and the matching chapter theorem number were checked at turn767search0
and turn767search2. The date of the online prepublication file was not
used as the book's publication year.

The precise imported result is the injectivity comparison for finite
projectives with equal composition factors. The character pairing in
the read proof makes projective-cover characters independent, which
gives this result. We use no integral surjectivity of the Cartan map.

As a cross-check we opened Schneider's author-hosted notes,
Theorem15.4 and its proof, printed84--85, at turn772view3:
https://www.uni-muenster.de/FB10/u/pschnei/publ/lectnotes/modular-rep.pdf
Its stronger cokernel statement is not needed in A84; we do not import
the induction-theorem dependencies of that stronger argument. The new
formal bibliography entry is therefore Webb alone.

## The additional arguments are explicit in A84

The actual coefficient field is Fp, which need not split Q. We descend
from a finite splitting extension by restricting scalars and cancelling
the resulting equal finite multiples with Krull--Schmidt. This step
does not require a silent change of the coefficient field.

For the inverse-limit passage we use the completed-ring projective
dual Hom_Lambda(P,Lambda), made into a left module by group inversion.
Finite idempotent matrices give its base-change compatibility. The
coefficient-of-identity formula identifies each mod-p finite reduction
with the ordinary contragredient dual. At higher coefficient powers,
projectivity lifts an isomorphism and finite Nakayama proves the lift
is invertible. Common refinements give the finite intersection property
for the finite isomorphism sets, and hence one compatible full system.

The resulting isomorphism is over the actual full Zp[[E]]. It is not
obtained by taking an inverse limit of ordinary vector-space duals.
The final multiplicity argument uses projective covers at modular
heads; it does not confuse their multiplicity with a composition-factor
multiplicity. The projective cover of S dualizes to that of S*, as
verified directly with a primitive idempotent and the group-inversion
anti-involution.

This closes the modular-head isomorphism and compact-duality limits
left in A83. It does not prove untwisted odd-prime freeness, rule out
nonselfdual imbalances, realize a tree, or make a selected incidence
map surjective. The main involution conjugacy decisions remain Open.

The complete proposed proof is work_A/A84_root_proposed.tex. It was sent
to A for a full independent review and to CE when the priority B review
permits. No final review result is claimed in this initial source log.

## Final review and integration

Both complete independent reviews passed. Their records are
work_A/review_A84_independent.md and
work_CE/review_A84_projective_duality_15h.txt. The reviewers each flagged
the same potential notational confusion in the finite base-change
identity. The accepted A84 now writes(P^#)_(a,K)=(P_(a,K))^# and explicitly
defines the symbol on the right over the finite group ring. There is no
second dualization. The statement, proof, verified Webb bibliography
record, register row, and report entry are integrated into the paper.
The combined first build is clean; no further mathematical qualification
was required by either review. The main full conjugacy problem remains
Open for the exact incidence reason already stated above.
