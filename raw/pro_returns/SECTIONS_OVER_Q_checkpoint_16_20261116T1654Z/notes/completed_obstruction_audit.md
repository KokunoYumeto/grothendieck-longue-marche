# A.90 and A.93: completed old-coordinate obstruction

The mathematical sources are:

- work/sections/completed_old_obstruction_agent.tex — A.90, the fully profinite completed tuple and its new-puncture obstruction.
- work/sections/completed_old_section_obstruction.tex — A.93, the finite geometric quotient, its cochain, and the locally matching section obstruction.
- work/notes/local_agent_references.bib — updated verified entries AgentMilneLEC and AgentCTSkoro2019.

## Primary source checks

Opened the complete author PDF of J. S. Milne, *Lectures on Étale Cohomology*, version 2.21 (22 March 2013), at:

https://www.jmilne.org/math/CourseNotes/LEC.pdf

The passages used in A.93 were checked on 16 November 2026:

- Remark 3.3(c), printed p. 27: finite-cover invariance under extension of algebraically closed fields of characteristic zero.
- Theorem 21.3, printed p. 130, and its proof: the finite-cover comparison with the complex analytic variety.
- Theorems 21.1 and 21.5, printed pp. 130 and 132: cohomology comparison for finite constant and finite locally constant coefficients.
- Propositions 14.2 and 14.3, printed pp. 90–91: proper-curve cohomology and point-support groups. Localization gives the geometric higher-cohomology vanishing used in the arithmetic comparison.

The previous AgentCTSkoro2019 note now also records Remark 4.5.2, opened and checked by the parent agent, for the split Brauer/Jacobian sequence in A.88. Its author PDF is:

https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf

## Independent proof audits

A.90 has passed complete independent audits by the parent, Legendre agent, and birational agent. The mixed-exponent stabilizer argument handles every exponent divisible by four, and the refinement schedule is cofinal for every positive integer. The maintained condition is the individual vanishing of the root symbols (X_i, χ), not an inferred condition on roots from the even-power equation. Exact local T values are retained once a prime is controlled.

A.93 has passed complete independent audits by the parent and both other agents. Its class is inflated from (H/K) ⋊ G_Q, the actual cover subgroup, and no extension of that class to the whole (Π/K) ⋊ G_Q is assumed. The modulo-four torsor condition moves a section into the cover subgroup. Its geometric quotient has order 2^135.

The finite-quotient assertion includes ordinary real-point matching. Real splitness of the Brauer class alone is not used to infer vanishing of a chosen μ₂ lift along an arbitrary finite-quotient section. For the full Selmer consequence, the μ₂ lift is chosen on the proper curve first; real ordinary and tangential evaluation therefore give the required zero invariant.

The augmentation-ideal calculation gives the actual map Π/Γ_12 Π → Π/K: Γ_(2+k)(Π/K)=I^k(Π/K)' and I^10=0 in F₂[(Z/4)^3]. Thus this finite obstruction factors through class eleven. This is a four-punctured-line statement. The third modulo-four inertia coordinate proves that this quotient does not factor through the tripod map.

## Retained finite certificates

- work/code/completed_old_obstruction_certificate.py
- work/code/completed_old_obstruction_certificate_output.txt
- work/code/completed_old_section_certificate.py
- work/code/completed_old_section_certificate_output.txt

All have been executed and pass. A.90's script checks finite stabilizers, local images, rational refinement identities, the cofinal exponent schedule, and uniform genus bounds. A.93's script checks the actual 64-sheet graph, the group order, the augmentation-degree bound, the cross cocycle, its edge, and splitting changes. Neither script claims to execute the unbounded Chebotarev construction.

These results do not rule out every completed tuple for all rational punctures and do not rule out a tripod section with only the first two coordinates.
