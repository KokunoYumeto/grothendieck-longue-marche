# Supplemental notes SR01–SR02: revised precarte morphisms

Author: GPT-6 Astra Pro; inherited effort unspecified. Run MPL_138_090-133/maps_moduli_research. Date: 2026-11-17. These checks use frozen TeX only, with no source-image reading or transcription change.

## SR01 — The fibre-cardinality law does not describe the standard cartographic quotient

**Source:** frozen scan98, lines24–32, “p'(s')=ν(φ,s)p(s)” and “ν(φ,s)=Card(φ_s^(-1)(s)),” with the parallel q,r equations; lines34–36, the asserted functor C↦Fac(C).  
**Kind:** own targeted counterexample, conditional on the usual cartographic-set / branched-cover morphism category; confidence high because the equivariant map and all cycle counts are explicit.  
**Context:** Hua, modernised reading of cote138, §13.I “Précartes, et la catégorie des cartes co-épinglées,” lines1513–1518, records the same ν definition but proceeds only with isomorphisms; RESULTS_STATE: no direct entry located by searches for precarte, Cartcomb and morphisme.

The equivariant quotient from E={1,2,3}, ρ_s=(123), σ=1 to the singleton is the standard morphism of the cubic star to the identity map, analytically z↦z³. Its vertex and face fibres each contain one cell although their degrees change from3 to1, while the edge fibre contains three cells each of unchanged degree1, so every displayed family of equations fails. **SR01R:** for the usual branched-cover morphisms the multiplier is the local ramification index at the source cell, rather than the number of cells above the target cell; alternatively a narrower morphism category must be stated (supplementary checks P1).

## SR02 — The literal precarte morphism laws fail closure under composition

**Source:** frozen scan98, line13, “forment une catégorie … morphismes,” and lines24–32, the revised equations and ν definition.  
**Kind:** own elementary counterexample to the category assertion under ordinary composition of the three set maps; confidence high because all objects and fibre sizes are finite and displayed.  
**Context:** Hua §13.I, lines1508–1518, retains the object definition and the ν footnote; RESULTS_STATE: no direct entry; equality of the three degree sums occurs only later as a necessary condition for a precarte to admit a pinned map (frozen scan99, lines3–5), not in the precarte definition itself.

Let S0 have one point of weight1, let S1 have two points each of weight2 mapping to S0, and let S2 have one point of weight2 over the first S1 point and two points of weight4 over the second. Both maps satisfy p_source=(fibre cardinality)·p_target, but their composite has fibre cardinality3 and would require all source weights to be3, contradicting2,4,4; choose singleton A and F of degree1 and identity maps at every level to obtain complete precartes. **SR02R:** these literal equations do not define a category under ordinary composition; replacing the multiplier by the local degree ratio restores multiplicativity, while the isomorphism-only case ν=1 is unaffected (supplementary checks P2).
