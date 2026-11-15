# Part D work log

Started 15 November 2026. Files read: attached EXIT_ONE_TYPE review §4 (Theorem R); original levels.tex results P5b2/P5b4/P5c1 and proofs; LM5 F.40–42; LAMBENCY_IN_AG_20261114.md. All are treated as claims.

## Current verified calculations

For a nonempty multicurve σ on S_(g,n), let v0 be the number of genus-zero components of the cut surface. The link is the join of the curve complexes of its components, and Harer's sphere dimensions give link sphere dimension 2g−3+n−v0. This exact formula warns that the proposed connectivity bound requires more than the rank deletion estimate asserted in the prompt.

The compactification-independent archimedean end system is established directly by N ↔ X\N: compact Hausdorffness identifies punctured neighborhoods with U\K for compact K⊂U. Oriented-blow-up collars identify a constant homotopy model for normal crossings pairs.

## Searches run

Web searches: curve complex rank selection / truncated pants complexes / Harer sphere dimensions. Primary sources to open next: Harer 1986; Hatcher pants decompositions; Boggi–Farb–Lochak procongruence curve complexes; Svaldi Mori hyperbolicity; toroidal factorization.

## Pending

Check Theorem R dependencies and low genus connectivity; derive exact boundary comparison; finite stable-graph/tropical map; run 23 modular dessins computation with primary CDH data; all unresolved claims remain unproved.

## Verified checkpoint

D.1--D.15 now written. The end comparison and low types, all four requested rank-selected cases, the corrected uniform link bound, projective Theorem R, finite-level completion, the complexity-two counterexample to the printed Kent range, all 23 lambencies, and the complete low-strata enumeration have been worked through. Primary sources and exact opened statements are recorded in D_references.bib. All listed computations were executed and their outputs saved under code/d_*.out and code/d_*.json.

The all-genus stronger rank-selected claim remains open in D.7: the first unresolved type is P_3 for (3,0). The exact boundary map between the rank-one and rank-two link Steinberg modules, rather than the incorrect dimension estimate, is the remaining issue. No general equality is inferred from a finite quotient.

A separate source audit found the finite-centralizer assertion in Boggi, Congruence topologies, Lemma 6.7 false for the characteristic mod-two homology subgroup. code/d_hyperelliptic_counterexample.py computes the resulting elementary-abelian centralizer. A different closed genus-two transfer through Proposition 2.4(ii) and Corollary 4.7 is being checked independently of that lemma.

Still being added: reconstruction from the complete face/collar diagram, five explicit depth-three complex-of-groups cases, graph/tropical comparison maps, and the source-audit correction just described.

## Reconstruction and comparison checkpoint

D.16 proves the given collar/face reconstruction by the actual angular quotient, including all four requested examples and both relevant fundamental-group filtrations. D.17 gives the five depth-three stratum tables, the node-normal bundles and Euler classes, flag stabilizers, and transport twisting words; it states the remaining five-/six-point finite word dictionary as open in B.8/B.15. D.18 constructs the graph-category homotopy-colimit map to the symmetric boundary complex and volume-one tropical space and computes its actual point fibres. Both CGP primary definitions and Theorem 6.1's proof have been opened.

Theorem R now explicitly proves the supporting-prime purity statement on a general transverse slice, contraction of every non-Rees exceptional subtree, intersection of monomial valuation ideals at a special triple point, and weak factorization relative to the endpoint Y.

The additional exact quotient-poset homology computation d_rank_quotients.py was executed. At (3,0), k=3, the finite type-poset has cells (34,148,208,93) and mod-two Betti numbers (1,0,0,0); it cannot detect the proposed actual rank-selected second-homology obstruction. The remaining genus-three map is being reduced to an incidence-system colimit of genus-two Steinberg modules.

## Independent low-genus completion proof

D.19 now proves the closed genus-two congruence transfer using HM2011 Theorem 6.1 (FC-admissible configuration restriction at n=1), the full configuration exact sequence, and Boggi2009 open CSP. The lift is adjusted by an element of the configuration group to centralize that group; its once-pointed image acts trivially on the punctured-surface group and is killed by open CSP. Agent E checked the exact morphisms. Neither Boggi2020 Corollary 4.3 nor Lemma 6.7 is used.

D.20 gives two exact counterexamples to those printed claims: the mod-two homology-cover finite centralizer, and the unequal-weight two-twist product whose handle swap changes its mod-three homology matrix. The program was rerun with both examples. D.21 transfers the profinite pentagon obstruction to (1,2) via Luo Lemma 2.1(a), whose map and proof were opened, and the explicit index24 pure-braid subgroup from B.9. All genus-at-most-two finite-level/procongruence comparisons and their connected one-type ranges are now settled. Higher profinite connectivity is not asserted.
