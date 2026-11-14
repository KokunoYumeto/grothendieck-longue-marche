# Audit of the supplied local p-adic section-conjecture proof

## Scope and conclusion

The local argument of the supplied OpenAI manuscript dated 6 October 2026 has now been read in full through Section 7 and independently checked in three pieces. The resulting mathematical derivation is written out as D.15–D.19. The earlier checkpoints' conditional treatment of the proper local assertion is superseded by that derivation in the current assembled manuscript. No claim of external peer review or priority is made.

The decision concerns the proper local assertion and its specific completion theorem. It does not certify every global application in Section 8, the separate companion Selmer-converse manuscript, or the global section conjecture. D1–D4 remain unresolved. The already checked finite-descent implications in D.5 retain their exact additional hypotheses.

## The precise completion statement

For a finite extension k/Qp and a smooth proper geometrically connected curve X/k of genus≥2, put K=k(X). Fix a real rank-one prolongation of the p-adic norm to Ksep, let E be its completion, and let Ktilde be the function field of the full arithmetic universal étale cover. If H is the closure of Ktilde in E, the statement is the **specified containment Ksep⊂H inside E**. An unrelated abstract embedding is not substituted for that assertion.

Write K0=kbar(X) and Omega=completion(kbar)⊂H. The K0-embedding in H and the Omega-embedding together define a complete-field-valued point of X_Omega. Its image xi can be Omega-rational while its projection to X_kbar remains generic. Every evaluation in the proof retains the complete-field-valued point, not merely its underlying Berkovich point.

## Independent checks and decisions

| Stage | Exact issue checked | Decision and location |
|---|---|---|
| Local analytic coordinates | The local expression t=z^e is valid after shrinking even for p dividing e; the whole inverse disk is captured by properness. | Checked by root and the first-stage reviewer; D.15. |
| Patching | Roots on the entire inverse collar split every local branch, including all sheets. Finite locally free algebras glue on an open cover with disjoint branch-disk pieces. | Checked by root and both reviewers; D.15. |
| Field evaluation | A descended proper étale cover with its field in H supplies the correct H-point; exterior analytic evaluation gives a K0-embedding. Normality then identifies the chosen subfield. | Checked independently by all three; D.15 and D.18. |
| Horizontal ramification | Indices are for residue-characteristic-zero closed-point valuations. They divide ell after subextensions, composita, normal closure, normalized pullback and an upper étale cover. No arbitrary ramified-tower assertion is used. | Checked independently; D.15. |
| Stable-node roots | For a nonseparating edge, residue Kummer covers have matching full marked fibres and zero augmented-graph ramification. For a bridge, two connected side covers produce ell bridges, all nonseparating. | First-stage independent pass and root; D.16. |
| Whole-collar control | RNS gives a stable model mapping to the chosen blowup model. An irrational coordinate level avoids every source model vertex and smooth disk tube; compactness upgrades that level to a whole collar. | First-stage independent pass, root, and second-stage interface check; D.16. |
| Period lattice | Division by m on a torically uniformized Jacobian partitions the full pullback by Lambda/Lambda^m. Adjusted local lifts glue because Lambda is torsion-free. | Root and independent second-stage pass; D.17. |
| Integral slope | The character lattice is H1 of the graph. The cycle e_j−e_j' evaluates to slope1 on e_j; no inverse period matrix or hidden factor ell enters. | Exact Baker–Rabinoff conventions reopened by root and second-stage reviewer; D.17. |
| Arbitrary m, including p-powers | Laurent coefficient bounds at both open-annulus endpoints give the strict middle-collar bound needed for log/exp. The threshold includes p=2. | Root and independent second-stage pass; D.17. |
| Completion | Every auxiliary normalized cover has horizontal indices dividing ell; its upper étale cover descends over the proper base. First-stage containment and normality finish the specified-copy assertion. | Root and independent second-stage pass; D.18. |
| Local sections | Rank-one decomposition restriction is an isomorphism. Birational localization would give two inequivalent henselian rank-one valuations on the section field; an explicit square-root contradiction excludes this. Rank-two coarsening gives a rational horizontal point. | Root and independent finite-field-agent pass; D.19. |

The independent records are `R24_first_stage_review.md` and `F_R24_independent_review.md`. The third review concerned D.19 with D.18 as hypothesis, and independently confirmed the decomposition-group comparison, two-valuation computation, rank-two reduction and Jacobian injectivity proof.

## External inputs opened and matched

1. **Amini, Baker, Brugallé and Rabinoff(2015), Theorem7.7.** The target triangulated curve is fixed. A tame covering of its metrized complex lifts to a tame covering of that curve. Definitions2.19,2.21,4.25,4.31 and Section 7's lifting convention retain the full inverse skeleton; with an empty puncture set the lift is finite étale. Lemma6.10 gives the monomial form on entire tame annuli. The first-stage proof verifies the covering data and Riemann–Hurwitz condition instead of merely asserting liftability.

2. **Mochizuki and Tsujimura(2024), TheoremA and Proposition2.4(iv).** For a finite p-adic local field, the all-prime RNS hypothesis is satisfied. The proposition gives a finite étale cover, after finite extension of the local field, whose stable model maps to the specified compactified model. The argument uses no unsupported finiteness of the model morphism.

3. **Baker and Rabinoff(2015), Sections4 and6, Proposition6.1 and Corollary6.6.** The toric uniformization and the Abel–Jacobi tropical comparison use the integral graph-homology character lattice and edge-length pairing. These exact conventions are sufficient for the slope-one calculation in the explicitly constructed two-vertex graph.

4. **Poineau(2010), AppendixA, TheoremA.1(ii).** Proper analytic GAGA gives the coherent-sheaf equivalence. Applied to the finite locally free algebra, its unit and multiplication, it algebraizes the glued finite cover. **Temkin(2010), Facts4.2.2,4.3.4,5.1.3,5.1.5–5.1.6 and Exercise5.1.7** supply the good-space sheaf comparison, local contractibility, complete-field-valued points, and detection of étaleness.

5. **SGA1, ExposéX, Corollary1.8.** The supplied primary TeX was reopened at the exact statement: extension of an algebraically closed field preserves the fundamental group of a proper connected scheme. Thus the finite étale cover over Omega descends over kbar. The exterior analytic map is not asserted to descend.

6. **Pop and Stix(2017), author-preprint Theorem26 and Section6.1.** Every continuous section for a hyperbolic curve over a finite extension of Qp lies in a decomposition group of a valuation extending the p-adic valuation. The type2h conclusion identifies the point section after rationality is forced by surjection onto G_k.

7. **Koenigsmann(2005), Proposition2.4(2), Definition1.4, Observation1.3 and Lemma1.7.** The full birational section over a finite extension of Qp lies in a decomposition group of a rational point of the smooth complete curve. The theorem is used only after the proved rank-one comparison has produced an actual continuous birational lift.

The bibliography records the opened versions and URLs. The new proof does not import the desired local section theorem as a premise. The two nontrivial geometric stages establish the completion statement first, and only then do the opened localization theorems give the local section conclusion.
