# Knowledge handoff: the shape map

Written 13 November 2026, 03:41 UTC (machine clock), by Claude Fable 5.2 (effort medium, no sub-agents), the agent
that wrote the blind map and revisions 1, 1a, 1b and 2. For a successor who continues the work without my context.

## Where the work is

- `braindump_board/SHAPE_MAP_BLIND_FABLE_20261113.md`: the blind map (S1–S7, partial features, carry-overs 1–7). Do
  not change it.
- `braindump_board/SHAPE_MAP_REVISION_20261113.md`: revision 1 (NS from the LaTeX; the user's notes a–f), 1a (the
  vacuum-gravity lessons), 1b (later hunches, Grothendieck's own statements), 2 (open items pushed; eight new
  connections).
- `braindump_board/cards/shape-map-finite-to-limit.md`: the method, the user's words, the sources located.
- Scratch scripts of revision 2 (not preserved elsewhere):
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\rev2.py`
  and
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\rev2b.py`.
  Copy them next to the map if they are to be kept.

## Status of everything

No proof in any source was checked. "Proved here" in the revisions means a short argument or an exact computation
written or run by me, checked by nobody.

## What was read, and how far

| Source | Where | Read |
|---|---|---|
| OpenAI ETH paper | `openai/math`, `preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf` | abstract, Thm 1.1, §1.1, §2.1–2.4 |
| OpenAI local smoothing | `openai/math`, `preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf` | abstract, Thms 1.1–1.2, §1.3–1.4, §2.1 opening, Lemma 6.1, Remark 6.2 |
| Yang–Mills | kitp.ucsb.edu `YM_working_group.pdf` | in full; a custody statement, no mathematics; the proof is unreleased |
| Navier–Stokes | `KokunoYumeto/yang-mills-interacting-workbench`, `navier-stokes/` | reconstruction pp. 1–6, §3 outline, Thm 3.1, Props 9.3–9.6 (statements, 9.5 proof), Lemma 10.2; READMEs; `infinite_status.tex` in full |
| GR-VAC lessons | `KokunoYumeto/open-math-courses`, `courses/GR-VAC/` | A §§1–2, 7; B §§1, 6, 7, 8, 10, Ex. 5 |
| Andrews–Connes–La Gatta | `research_maps_20261112/CONNES_CONSANI_CFT/papers/2611.13129/src/prolate-weil-fine15.tex` | abstract, intro, Hypothesis LA, Fact and Table `tab:logbound`, Thm `thm:condpos` |
| Connes–Consani 2501.06560 | `Free or receipted/free/arxiv-eprints-shape-20261113/cc_2501.06560/arxiv-pisa.tex` | lines 404–418, `ramiprop`, `ramicor`, `archimedeanplace` |
| Perelman | same folder, `perelman_math0211159/src.tex` | §3, statement of 10.1 |
| S^6 | `s6_workbench_repo_20261112/README.md`, `survey_20261112/FINDINGS.md` (F1–F10), `s6_pro_prompts_20261112_work/reviews/` (FINDINGS, first half of ROUTES) | as listed |
| Returns | `longue_marche_pro_pilot_20261104/answers/` (LM7, EXIT_ONE_TYPE, FLAGGED_149, CYCLOTOMIC_KERNEL), TOTEX2 checkpoint | every CSV row; of the proofs only LM7 `sections/E_completed_pairs.tex` (E.32) |
| La Longue Marche | `KokunoYumeto/grothendieck-longue-marche`, `reader/LaLongueMarche_English.tex` | keyword search; passages at cote 140-4 scans 24, 172–175; cote 140-2 scans 72, 378; §19 opening |
| Archive returns | `grothendieck_archive_transcription_20261110/returns/` | keyword search; cote 147 scan 104 |
| Zeta workbench | `KokunoYumeto/zeta-function-research-reader`, `satellites/13_cue_mellin_complete_programme_audit.tex` | Thm `thm:cueM-U3-trace-descent` (statement), Prop. `prop:cueM-Psi2-not-SOS` |
| v35 | `Papors/Chatnotes/Soc/Arithmetic_Time_CPT_Spectral_Packets_v35_integrated_replacement.tex` | lines 7512–7572, 8008–8090 |
| Lehner–Pretorius 1006.5960 | arXiv PDF | abstract, Table I, the passages on generations |
| Abstract only | arXiv | 1807.04422, hep-th/0411114, 1909.10355, 2206.10780 |

Everything else cited in the revisions (Milne, Brown, Brown–Schnetz, Conway–Sloane, Cheng–Duncan–Harvey, Balaban,
Bost–Connes, Connes–Marcolli's book, Casini–Huerta–Myers, Kapustin–Sopenko, Myers–Sinha, Henningson–Skenderis,
Tseytlin, Penington, AEMM, Connes math/9811068, Connes–Consani 2004.08879, Grover–Mezzadri–Simm) was **not opened**;
what is said about it is from general knowledge and is marked so.

## What is established (at the level stated above)

1. S1: every item has a scale with a tractable end; the completed ones have a bound uniform in the scale, each open
   item lacks one. NS (OpenAI): residual order 1/5 + j/10 against a loss K_m independent of the stage. The user's
   continuation: explicit cost λ_q^{9/8} per layer for unchanged fields.
2. E.32 of LM7 is a lim¹ class (Jannsen's sequence), arising because v₃(q − 1) is unbounded; equivalently a telescope
   class one degree up. The tame relation is the scaling action; H² is the coinvariants of (q − 1) on restricted
   sequences.
3. Grothendieck states the layer-by-layer programme himself (cote 140-4, scans 172–175) and identifies a
   discretification with an archimedean valuation (cote 140-2, scan 378). Pentagon, hexagon and Lego are not in La
   Longue Marche.
4. E.25's class κ₂(−1) ∪ κ₂(−1) is the quaternion class (−1,−1) with non-zero invariant at ∞; κ₂(−1) is a
   Connes–Consani cover with one point over C_∞.
5. Ψ₂^♯ is negative at (u,v) = (4,0), (3,0), (0,−1), all outside the image of the cover (w < 0 or v < 0); exact values
   −217/24, −13/6, −97/24. The sum-of-squares obstruction is in degree zero and is not of E.32's kind.
6. Tate construction: Cone(M_{hG} → M^{hG}) is self-dual up to the shift [−1]; this is v35's boundary-defect duality
   with Z = {∞} and gives Tate duality Ĥ^r(G,M)^∨ ≅ Ĥ^{−r−1}(G,M^∨).
7. H₂(Δ₀,₆): f-vector (25,105,105); as a module over the standard S₅ (the stabilizer of a marked point) its character
   equals that of Ind from F₂₀ of the 4-dimensional module (24; −1 on 5-cycles; 0 elsewhere), exact check. Over the
   transitive PGL₂(5) ⊂ S₆ it does not (−8 on fixed-point-free involutions, 3 on type (3,3), 1 on 6-cycles). The
   cycle lattice in Z¹⁰⁵ has determinant 5⁸·11¹⁰·13⁵ (using EXIT P4d2's statement that the Smith form is trivial).
8. The driven energy identity for (S38): with zero initial data the total work at the wall equals the energy, so it
   is non-negative; the instantaneous work has no sign.
9. The Proj¹ formulation of the force budget is vacuous: restriction maps of smooth functions are surjective.
10. Table `tab:logbound` cannot test a lower bound (its entries are upper bounds), and its first column is not
    monotone.
11. E.32's witness z = (q_j − 1) lies in the 3-adic closure of the image of d and not in the image. So the class is a
    "closure of the image modulo the image" class: d = diag(q − 1) is injective with no gap (inf |q − 1|₃ = 0). This is
    the common form found in revision 2 for E.32, a gapless limit of gapped finite systems, the closing of ε_λ, and
    approximately inner automorphisms modulo inner ones.
12. Lehner–Pretorius Table I: string radii 0.148, 0.05, 0.02 at times 203.1, 223, 227: a roughly fixed ratio per
    generation, unlike the Alpöge–Buckmaster layers λ_q = λ_{q−1}^{Q_q}.

## Revision 3 (13 November 2026, 12:39 UTC): four new returns, none refereed

Read: TOTAL_EXACT_2's final message
(`derivateurs_companion_20261109/pro_prompts_max_20261112_work/TOTAL_EXACT_2/RETURN_TEXT_20261113.md`, §§1–2 and the
tables); the reports of LM8 checkpoint 16 (matrix head, sections E, F, G), LM7_PUSH checkpoint 04 (lead table,
"Derived limits") and LM4 (table head), all under `longue_marche_pro_pilot_20261104/answers/`. Reports only, no
proofs. `pro_intake_20261113/IMPLICATIONS.md` did not exist yet.

Claimed by the returns, and what the map takes from them:
- Total does not imply exact: the category C_δ, T₁(Q_R) ≅ R over every non-zero ring. The blind map's TOTEX2 row and
  carry-over 7 are superseded.
- The closure(im d)/im d form of revision 2, B2, appears again in LM8 F.21 (prime 5) and LM7_PUSH A.1–A.4, and
  LM7_PUSH states the criterion: the Milnor term vanishes exactly when the Smith valuations are bounded. The class is
  invisible to cardinalities, survives finite extensions, and cannot be evaluated from finite data.
- Compact towers have no lim¹ (LM8 F.15). So S7's wall (section surjectivity for P¹ minus three points) is not a lim¹
  phenomenon; the candidate is the kernel of the map to the product of the maximal pro-p quotients (LM8 A.22, G;
  LM4 D.29, D.30).
- Five frameworks: derived colimit; derived limit; the Galois part against the full topos; pro-p against profinite;
  integral against rational. The table is in Revision 3, (b).
- A discrepancy to settle: the brief said LM4's full profinite compatibility is open; the report's table says full
  profinite recognition is refuted.
- Tests proposed first: exactness as a Ramsey property (three small categories); the mixed-prime form of the section
  statement; the referee's check of the bounded-valuation criterion.

## What is open (the statements are in the revisions)

- A canonical map from the cosmic Galois group to the motivic Galois group of MT(Z); a coefficient version of
  Connes–Consani's covers for non-abelian Galois modules (E.18).
- A Perelman-type monotone for: Hypothesis LA; the all-stage force budget; TOTEX2 C.9; CYCLOTOMIC E3.
- A category in which E.32's residue complex has a determinant.
- "One class from a D+1 invertible theory" across the cases: holds in part for E.32 and for crossed products, fails
  for sums of squares, unformulated elsewhere.
- Whether H₂(Δ₀,₆) with any natural form is a step in a holy construction: no evidence; the determinant found is not
  that of a Niemeier lattice or of A₄⁶ (5⁶).
- The items of Revision 2, part B, marked open there.

## Not done, by instruction or by budget

- Aligning v35's Part on anomaly inflow with the literature (a separate run, waiting for the user's word).
- Lifting the Andrews–Connes–La Gatta uncertainty principle to each item (recorded for later).
- The proofs of the returns (only E.32's was read).
- NS reconstruction §§4–8 and appendices.

## Cautions for the successor

- The user asked that the hunches be treated as hunches; mark them known, new and proved, new and open, or wrong,
  case by case, and never mark something known because a special case is known.
- Say when a statement rests on an abstract or on a paper not opened.
- Two symbols collide: OpenAI's q (similarity parameter) and the lesson's q = kρ_c.

## Next round (user, 13 Nov 2026, P4082)
- B4 redirected. Compare the Landau–Widom plunge region with the spectral action: Tr f(D/Λ) and its cutoff transition
  (Chamseddine–Connes, The Spectral Action Principle, hep-th/9606001); the almost-commutative Standard Model spectrum
  (hep-th/0610241); the prolate operator and ζ (Connes–Moscovici 2112.05500); spectral triples and ζ-cycles
  (Connes–Consani 2106.01715). This replaces the islands comparison.
- The object is the closing gap of B2/B3, not positivity: E.32, the lattice gap, ε_λ (rate e^{−4πλ²}, Hypothesis LA),
  and the infinite-chain anomalies.
- Infinity points in a direction (user, P4087). Choosing a point at infinity breaks a symmetry spontaneously to the
  stabilizer of a direction, and the broken part acts by scaling. Instances: KMS states and boosts (Ojima 1986;
  Bisognano–Wichmann); Bost–Connes for β > 1 (extremal states ↔ embeddings Q^ab → C); tangential base points at a
  cusp, with Galois acting through the cyclotomic character (Grothendieck §9; Ker χ at cote 140-4); E.25 at the real
  place. To work out: is this the common reason the closing-gap obstructions live at ∞?
