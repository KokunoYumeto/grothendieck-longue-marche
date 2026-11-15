# Part E work log

This file records the work of the completion/Galois agent. All claims from attached AI returns were treated as claims to check.

## Main advances saved

- E.1–E.3: strict finite-congruence completion and finite constructible-sheaf comparison in all stable types. Finite stack isotropy is handled by finite étale atlas descent; the asserted dependence on the nonsolvable finite-subgroup centralizer equality is refuted by the explicit descent construction. No CSP is needed for this comparison.
- E.4: coherent arithmetic action on the completed system and faithfulness via the open four-point stratum, with the cyclotomic action on normal inertia.
- E.5–E.6: all chain stabilizers for the boundary stratification of Mbar0,5, their goodness and full induced profinite topology; a retraction is constructed for each multicurve stabilizer. All 15 compatible boundary pairs are checked by integer matrices. This supplies the proposed H.9 proof; root is reviewing the cofinal categorical quotient argument.
- E.7: checked Hoshi–Mochizuki–Tsujimura Theorem 5.17(ii), Definition 5.12 and its proof dependencies, and Lochak–Schneps Proposition 4(ii). Derived uniqueness of the maximal AA subgroup containing a selected complex conjugation.
- E.8–E.10: explicit center-free-extension kernel theorem, genuine mixed-braid GT lift to full PΓhat1,3, and automatic nonseparating inertia for the precise group in LM3b E.9. The proof identifies the extension by its explicit pullback Q ×_Out(K) Aut(K), not solely its endpoints. The GT action preserves every quotient relation because it acts on the ambient mixed braid group and sends both the full twist and the peripheral product to their λ-powers.

## Primary sources opened at exact steps

The bibliography records URLs and theorem numbers. Particularly important reads: Jansen Construction 3.18 and Corollary 6.6; BGH Proposition 12.6.4 and proof and spatial décollage reconstruction; Hoshi–Mochizuki Topics I Theorem 6.13(ii), its reduction to Theorem 6.12(i), and Lemmas 6.8 and 6.10; Minamide–Nakamura Theorem 4.3(i) and proof; Harbater–Schneps formula (1) and Appendix pp. 34–35; Boggi 2011.15075v6 Sections 6.6–6.17; Iijima RIMS1761 Theorem 2.5 and proof.

## Corrections under active development

1. Boggi Proposition 6.9 uses the incorrect identification of the full closed hyperelliptic group with B_(2g+1)/<z²>. The latter is the stabilizer of a Weierstrass point. In genus two the abelianizations have orders 10 and 40, respectively. A correct full presentation via B_(2g+2) is checked in Catanese–Wajnryb Example 4.1. Conjugating the standard GT action by braid reversal preserves W, W², the full twist and centrality of W, and repairs the required GT existence step.
2. Boggi Lemma 6.16's claimed uniqueness of a genuine extension is false: conjugation by the removed twist is identity on the smaller oriented multicurve stabilizer and nonidentity on the larger one. The finite symplectic image modulo 3 certifies nonidentity. The exact ambiguity and whether it suffices for the subsequent outer gluing are being attacked.
3. Hoshi–Mochizuki Topics I Lemma 6.8, printed p. 132, writes 3g−3+r>1 where the induction needs >0. The missing complexity-one cases can be included by the same one-node degeneration: (1,1) normalizes to a tripod and (0,4) to two tripods. Their moving-node pieces reduce to the already proved tripod base case. This is an inequality typo with a specified repair, not a reason to abandon the centralizer theorem.
4. Cote 143's bar denotes geometric base change, as proved by the exact sequences of scans 30–31. The universal-curve exact sequence of scan 33 relates the surface group πhat0,3 to Γhat0,4, while Γhat0,3 is trivial. The prompt's (0,3) comparison involving the mapping-class group and its comparison involving the tripod surface group require these exact maps and cannot use the same target without a label shift.

## Computations

- `code/E_meridian_pairs.py`, `.out`, `.json`: all 15 disjoint labelled boundary pairs of Mbar0,5 have primitive rank-two meridian spans; explicit integral left inverses supplied.
- `code/E_braid_models.py`, `.out`, `.json`: reduced-word Artin full-twist identity for three and four strands, central-quotient abelianizations for genus 2–6, and a finite matrix witness for the failed genuine uniqueness assertion.

## Outstanding work

Elliptic boundary clutching coherence and the complete same-pair orbifold comparisons; correction of the full procongruence outer-tower proof at genuine/outer extension ambiguity; a self-contained verification of ANABELIAN E.13; LM6 C.15/C.17 audit; manuscript type-by-type arithmetic/topos answers. The equality G_Q=GT and the restriction of the attached Δ character are not asserted. Root continues the overall task and handles final compilation and delivery.

## Added E.11–E.13
- E.11 gives all relevant elliptic braid boundary maps and exact genuine GT commutation with elliptic forgetting. The branch character is explicitly different from the ordinary A3 strand character; no same-pair normalization assertion is hidden.
- E.12 settles the orbifold normalizer comparison using the mixed-braid parity model and parameter detection on B3/B4; HMM2022 Cor2.8(i) now opened with its proof.
- E.13 reproduces the entire mathematical proof of ANABELIAN E.13 independently: point pushing, chosen-sheet equations, finite-deck cancellation, labelled ramification, and a direct smooth connected-fiber Hurwitz construction. Parent review requested.
- LNS2026 introduction explicitly warns that their GT action on genus-one two-point groups need not respect Lego absent the extra relation; E.11 has therefore not been promoted to a full boundary-coherence result.
