INCOMPLETE

# Part B: proof and computation record

| Task | Statements | State reached |
|---|---|---|
| B.a | B.1–B.2 | Proved finite-group plane and simultaneous stabilizer local models from Kolev, with the exact compactification/lifting maps; refuted the orientation-free isolated lemma and supplied the annulus-quotient proof. |
| B.b | B.3–B.5 | Proved sections/fixed points, reflection components and both centralizer values, including real punctures and the incidence graph recovering cyclic order. Sphere and trivial-operator comparisons are explicit. |
| B.c | B.6–B.11 | Proved the positive loop lemma via punctured cyclic realization; classified fixed subgroups and proved finiteness; refuted reflection uniqueness of maximal overgroups already in type (0,3); proved the valid positive normalizer equality; refuted the two stronger withdrawn assertions with topological and integral-matrix examples. |
| B.d | B.12–B.15 | Proved discrete intrinsic multiplier formula and the need for peripheral data, simultaneous affine/annulus normal forms, explicit multiplier formulas, and the strongest homotopically trivial classification. Profinite continuation is assigned to Part D. |
| B.e, anti-involution list and corollaries | B.16–B.18 | Proved quotient classification and puncture decorations, real moduli-stack component formula in hyperbolic types with unlabelled punctures, low-type failures of mapping-class injectivity, and both centralizer corollaries for both quotient families. The different conventions for labelled/coarse moduli are not silently identified. |
| B.e, H and normalizer | B.19–B.20 | Proved the twist identification and exact cut-surface normalizer, refuted maximal-free-abelian claim and corrected presentation (52) by explicit mutually inverse homomorphisms and an S3 certificate. |
| B.e, numbered task 1 | B.19, B.21, B.24 | Tube twist words computed; full words for the manuscript's dihedral generators in its particular common-pole marking remain unwritten. Exact missing comparison: transport the chosen base paths through the 2g-holed sphere under each geometric generator. |
| B.e, numbered task 2 | B.21, B.24 | Proved the actual B3 central extension of SL2Z, its lack of section, braid and disjoint-support relations, and failure of generation for disjoint chosen strips. All unspecified overlapping-strip relations are not computed. |
| B.f | B.22–B.24 | Refuted the assumption that a subgroup of the mapping class group determines the requested invariants in all abelian types; retained extension class is necessary. Completed and checked the entire type (0,3) table. No exhaustive extension-indexed catalogue for every other type with 2g+nu≤6 is claimed. |

## Sources actually read

- `longue_marche/LM_P014` through `LM_P021`: the relevant section and multiplier passages, especially all of scans 141–160, 179–181, 193–203.
- `longue_marche/LM_P044` through `LM_P047`: anti-involutions, their centralizers, the tube construction and presentation (52).
- Actual manuscript images inspected: scans 147, 179, 198, 439, 440, 469. The cancellation scope on 198–200 remains provisional.
- Constantin–Kolev, complete supplied TeX source: Proposition 2.4, Lemma 2.5, Theorems 3.1 and 4.1, Corollary 4.2, and their proofs.
- Kolev, complete supplied TeX source: Theorem 1.2, invariant-disc discussion, and finite-group part of the proof.
- Kerckhoff original 1983 paper, opened through the author's Harvard-hosted copy; the shared Part C source audit checked the extended group convention and Section IV cusp case. No reliance on the announcement's silence about cusps remains.
- Mochizuki, *Topics surrounding the anabelian geometry of hyperbolic curves*: supplied PDF extracted and Theorem 3.6, Corollaries 3.7–3.8, and Example 3.3 read. The real moduli statement is about a stack and the full punctured-surface modular group.
- Gross–Harris, supplied PDF, Proposition 3.1 and quotient Euler characteristic argument.
- Harvey, supplied PDF, Theorem 7 and its sign convention on pages 393–394.
- No Part B proof uses a companion return as an authority. Shared A/C lemmas are cited by their precise role.

## Computations run

`code/check_part_b.py` uses only Python's standard library and exact integers/rationals. It ran successfully after a closure-loop implementation error was corrected before any result was accepted. Final outputs are `check_part_b_stdout.txt` and `check_part_b_output.json`.

1. Enumerated all subgroups of S3×C2 by exhaustive iterative adjoining and closure: 16 subgroups, 10 conjugacy classes.
2. Computed every full and nontrivial partial section for every representative in type (0,3), their inclusions, maximal classes, group orbits and local multipliers, from the explicit sphere fixed-set geometry. Complete outputs are `type_0_3_finite_subgroups.csv` and `type_0_3_partial_sections.json`.
3. Checked the finite quotient of the (2,3,infinity) NEC group: vertex images of orders 4 and 6, intersection order 2, cusp image order 4, total order 12. Kernel Euler characteristic −1, three cusps, genus zero.
4. Checked all nine relators of presentation (52) at g=2 in S3; the two claimed commuting twist generators do not commute.
5. Checked S and TST⁻¹ have common square −I and order four; their product has trace −6, proving infinite order by its characteristic polynomial.
6. Checked the two C3*C3 monodromies produce respectively genus one/one cusp and genus zero/three cusps.
7. Enumerated the real quotient-type counts for 2g+nu≤6, output in `real_type_counts.csv`; checked the closed formula through genus 20. The proof establishes it generally; the finite checks are consistency checks.

`code/free_words.py` verifies by literal free reduction the braid identity for the two chosen handle automorphisms and the identity (AB)^6=conjugation by [a,b]⁻¹. Its exact output is attached in JSON and text.

## Corrections carrying consequences for other parts

- The unique maximal-section assertion requires a nontrivial positive part. Reflections already violate it in the smallest hyperbolic type (0,3). The same concrete discrete subgroups survive in the completion.
- The valid positive discrete normalizer equality N=C does not make the torsion in C into a group. The explicit punctured-torus example separates these claims by their actual inclusion and product maps.
- The scan-179 uniqueness expectation fails for a free glide involution as well as for C_n×C2 of arbitrary order.
- An outer subgroup in an abelian type does not determine its lift extension. The same order-two subgroup in GL2Z has a two-section realization and a zero-section realization.
- Formula (52) presents a group with a free F_g factor. The quotient F_g→Z^g, with its explicit equivariant abelianization map, is the correction needed to obtain the stated geometric semidirect product.

## Exact unfinished work and attempted approaches

For B.e(1), the abstract dihedral permutation action and every tube-twist word have been obtained. A naive permutation of the ordered commutator pairs changes the surface relator and does not determine the required base-path conjugations. The next concrete step is a cellular path calculation on the manuscript's sphere-with-2g-boundaries model, followed by free reduction of the transported paths. We have not replaced those words by their homological matrices.

For B.e(2), disjoint strip choices have been constructed and all their supported-group comparisons proved. These give a proper subgroup. Strips which overlap require their actual geometric intersections; braid relations for intersection one and commutation for disjoint supports are established, but no full relation list for every unspecified overlapping configuration has been derived.

For B.f, the first attempt to index all results only by a finite mapping-class subgroup fails by B.22. After repairing the index, the exact remaining task is to enumerate finite orbifold epimorphisms with each required kernel type, modulo orbifold mapping classes and target-group automorphisms, carrying the H² extension data in the abelian types. The finite-group enumeration for (0,3) is complete; extending that code without this orbifold completeness argument would not establish a complete table. The smallest next hyperbolic types are (0,4) and (1,1). This return does not label their missing tables as theorems or as unknown literature results.
