# D.31: a unit criterion for the remaining finite cusps

## Proved scope

Let a continuous noncuspidal section of a smooth hyperbolic curve over Q have ordinary or cuspidal localizations at every finite place and ordinary integral localizations outside a finite set. If a nonconstant global unit is regular and nonzero at every boundary centre used by those cuspidal localizations, the section is a rational point section.

The proof uses an actual local value at every place. At a cusp, Kummer covers of a regular nonzero unit are unramified in the horizontal direction, so every splitting of the cusp decomposition group evaluates the unit at its ordinary leading value. This includes completed tangential classes. D.3 then makes the global completed Kummer class rational. The finite fibre of the unit contains the whole finite-place support, and the finite-support comparison already checked in D.5 and D.22 concludes.

A connected finite étale neighbourhood with unit-lattice rank greater than the number of cuspidal finite places supplies such a unit by the kernel of the boundary-order map. Existence of that neighbourhood is an additional hypothesis. The proof retains transfer of noncuspidality and cofinite integrality to the lifted section.

For the tripod, if at most one cusp label occurs, one may use respectively 1−t, t, or t/(t−1). Each has value one at that cusp and never takes that value at an ordinary point of the tripod. Rationalization therefore excludes every remaining cusp. Combined with D.30, finite ramification and at most one local cusp label imply a rational point section.

## Exact remaining obstruction

If several labels occur, the global classes of t and 1−t lie in the profinite completion of the finitely generated S-unit group. Their outside-S local tuple lies in the closure of that group squared and satisfies x+y=1. Cusps impose the additional exact relations B_p=1, A_p=1, or A_p/B_p=−1, with the corresponding profinite valuation pairs displayed in the section. No assertion forces the remaining profinite coordinates to be ordinary integers.

Harari–Voloch Theorem 1 compares the outside-S closure condition with finite abelian descent; Conjecture 2 is the stronger diagonal integral-point assertion that would finish this route. If that conclusion held for the section's tuple, D.26 would recover the two global Kummer classes from their almost-everywhere localizations, excluding all cusp labels. This is a conditional route, not a proof of that conjecture.

Helm–Voloch Theorem 4 assumes the common finite ramification set and the good local elliptic realizations outside it. Its modular-curve result asserts existence, not identity with the section's tuple. Liu–Xu's projected all-place Brauer–Manin statement needs ordinary local components at the omitted places; their stronger outside-S conclusion over Q has S archimedean. These precise hypotheses leave the multiple-label case open here.

## Review, integration, and validation

Root independently checked the complete single-label and general-unit arguments against D.3, D.5 and D.22, and opened the primary Harari–Voloch and Helm–Voloch statements. The root approval explicitly retains the conditional existence of a neighbourhood with enough units. The earlier candidate remains in audit/D_finite_cusp_candidate.tex and .md as the review history.

Integrated files are sections/D_finite_cusp_extension.tex, audit/D_finite_cusp_results.json, this report, sources/D_finite_cusp_refs.bib and sources/D_finite_cusp_sources.md. The new section is input after D.30 in sections/D.tex under the parent's express authorization. Root owns assembly and the combined build.

The argument is symbolic and contains no proposed computable counterexample. Validation checks the result-row schema, claim label, citation-key resolution, TeX delimiter balance and single reachable input. No theorem is inferred from these formatting checks. D1–D4 remain unresolved.
