# La Longue Marche à travers la théorie de Galois: the manuscript read as a whole

PROVISIONAL, 11 November 2026. Written by Claude (Fable 5.2, Anthropic) for the development prompts LM4_FINITE_GROUP_ACTIONS to LM5_MULTI_GALOIS_TOPOI in this folder. To be revised as second-pass results come in.

Tags: **[A]** the author's own statement, with section and scan; **[L]** established in the literature, from my knowledge and not re-checked here (each prompt asks for the check); **[I]** my inference; **[H]** a hunch.

## 0. What this rests on, and what it does not

Read: `PLAN_RECORD.md` (Q1–Q57 in full; Q58–Q117 through sections 2–5 and the addendum, where they are quoted; I did not read each of Q58–Q116 as a separate message); the author's table of contents (`second_pass\witness\Grothendieck_Circle_tableLM.txt`); `second_pass\GLOBAL_PASS.md` (the coordinator's pass over 624 notes on the author's conjectures and questions); `DEVELOPMENT_CANDIDATES_draft_20261108.md`; the board card with its line-by-line second-pass corrections for cote 140-3 scans 207–696 and cote 140-4 scans 1–114; the two open findings of the source audit. Read directly in the transcription: the openings of §19, §34 and §51, the passage on Fermat in §51.16 (first pass), and single sentences of §26 and §§28–30 found by search.

Not read: the 96 checked package texts line by line, and the notes files (`ALL_RESEARCH_NOTES.md`, `NOTES_B`, `NOTES_C`). The scan references below are those of the global pass and the card. So this overview is a reading of the manuscript's architecture and of its recorded questions, not a second check of the text.

## 1. The shape of the whole, as the author develops it

The table of contents is his own, in two parts.

**Première partie, §§1–37 (cote 140-2).** It moves from topoi to groups to arithmetic, by a sequence of reformulations:

1. §§1–4: multi-Galois topoi, coverings of a topos, pro-variants. The fundamental groupoid without base points.
2. §§5–11: "le contexte arithmétique" and the "conjecture anabélienne fondamentale" (Conjecture 5.5, scan 23, with his later margin "C'est un peu faux cf §9"); local analysis at the marked points; the reformulation he calls "bordélique" ("le purgatoire nécessaire"); a taxonomy of cases; tangential structures and "sections de deuxième type"; adjusted hypotheses; conditions on systems of groupoids coming from geometry.
3. §§12–13 bis: "L'analogie topologique", where he convinces himself that in the anabelian cases the whole "bordel groupoïdal" is expressed by exterior groups with loops; the Galois formulation.
4. §§14–18: filling and drilling holes, cohomologically and topologically; finite groups acting on surfaces and finite subgroups of `Autext_lac(π)`.
5. §§19–25 bis: the Teichmüller tower; a 2-isotopic description of the category of topological isomorphisms; Teichmüller spaces (§22 is missing, by his own margin); surfaces with finite groups of operators "mises en équations"; special Teichmüller groups.
6. §§26–33 bis: profinite Teichmüller groups, discretifications, the modular topos, a "conjecture hâtive" (§26) which "grince" (§28) and is criticized and adjusted (§29); properties of `N_{g,ν}` and `𝕀Γ_{g,ν}`; lifts of outer actions; the arithmetic of hole-filling, where "on reconstitue, sans le dire, tout le topos étale d'une courbe algébrique complète, à partir du π_1 d'un ouvert anabélien" (§32); anti-involutions (§33); coverings (§33 bis).
7. §§34–37: a "description heuristique profinie" of the category of algebraic curves over number fields; injectivity of `𝕀Γ_Q → Autext_lac(π̂_{0,3})`; `𝕀Γ_Q` and `𝕀Γ_{1,1}`, `SL(2, Z)^`; Legendre.

**Deuxième partie, §§38–53 (cotes 140-3, 140-4), "Variations sur l'équation des lacets"**, which the table's compilers call "d'un caractère encore plus exploratoire". It is one calculation pursued through four changes of method:

8. §§38–47: the image of Galois in type `(0,3)` and `(1,1)` by explicit equations in `π̂_{0,3}` and `SL(2, Ẑ)`; notation restarted at §44 and §46 ("Notations définitives (?)").
9. §§48–49: the same equations as a group scheme `M_{ρ,σ}` over `Z`, about 220 folios.
10. §50: schematic envelopes of discrete groups, metabelian case.
11. §51: the Fermat tower as the example, ending in "Réflexions sur le théorème de Fermat".
12. §§52–53: Lie approximations of "systèmes de Galois–Teichmüller"; the special Teichmüller group of type `(1,1)`.

**[I] The movement.** Each step replaces an object by a more algebraic one that should carry the same information: topos → system of groupoids → exterior group with loops → profinite group with outer Galois action → solutions of an equation in `SL(2, Ẑ)` → points of a group scheme over `Z` → Lie (unipotent or solvable) approximations of it. The first part goes outward to the general statement (all types `(g, ν)`, all curves); the second goes inward to the two smallest types and tries to compute. The 1984 *Esquisse d'un programme* summarizes the first movement; the second (the group schemes, the envelopes, the Lie approximations) is not in the Esquisse in this form and is the least known part.

## 2. Directions he points to

- **[A] Rational points as splittings.** "Ceci suggère une approche de la conjecture de Mordell … Idem pour une approche du th. de Fermat" (cote 140-2, scan 65); in §51.16: if one could prove that the extension (371) attached to the Fermat curve `U_n` has no splittings other than those from the points at infinity, "le th. de Fermat serait prouvé pour U_n, même sans avoir établi le yoga anabélien", by "approximations de plus en plus fines" of `π_1(U_n)` (cote 140-4, scans 173–174). [L] This is the route later taken by nilpotent methods (Kim; Ellenberg; Wickelgren).
- **[A] The "conjecture fondamentale":** the groups `𝕀Γ_{g,ν}` are all canonically `Gal(Q̄/Q)` (scans 341, 356, 371, 376), and "la question essentielle" is an algebraic description of `Γ_{0,3}` (479). [L] Belyi gives injectivity; the rest is the question of `GT̂` (Drinfeld, Ihara), open.
- **[A] The category of curves over number fields described by profinite groups** (§34), with the conjecture that the loop structure need not be given. [L] Largely theorems now (Nakamura, Tamagawa, Mochizuki).
- **[A] A 2-categorical classification of finite group actions on surfaces** ("3-fidèle", scans 270–271), by drilling holes. [L] Its core is Nielsen realization (Kerckhoff 1983); [I] the 2-categorical statement seems not to be written anywhere.
- **[A] Group schemes over `Z` presented by `ρ`, `σ` and `G_a`** ("vaudrait bien la peine de tirer cette question au clair", cote 140-3, scan 336) and "une construction systématique de représentations motiviques" (scan 489).
- **[A] Lie approximations of Galois–Teichmüller systems** (§52), with §51 as the "approximation minima". [I] The later relative and weighted completions (Hain, Hain–Matsumoto) and the pro-unipotent `GT` are the things to compare with.
- **[A] Arithmetic meaning of homotopy** for forms of `P^1` and Azumaya algebras (§20).

## 3. What he marks open or doubtful

Withdrawn or doubted in his own hand: Conjecture 5.5 ("un peu faux"); a conjecture on `T̂` in `T̂̂` ("ultra-faux", scans 322–323); the "conjecture hâtive" of §26; the faithfulness of `Γ → 𝚪_g`, `𝚪_{1,1}` ("peut-être est-ce tout à fait faux ?", 504–505); the lemma marked "faux !" and the abandoned theorem "Ultra fort" in §15; the genus-0 exception in §14 ("Non, à cause du genre 0 !!!"); the "lemme dubitatif" and the "Théorème (!)" of §50; the freeness claim struck out at cote 140-4, scan 98. Left open by him: whether the rotation invariant `μ` is intrinsic (155–160); the bijection "??" between fixed points and classes of sections (139, 148); centralizers in the profinite anabelian case ("pas prouvé pour le moment dans aucun cas", 118); the centre of `Gal` ("je cale", "Consulter Deligne", 496); a characterization of `Γ_Q` in `Γ̃` ("je n'ai pas de caractérisation bien plausible à proposer", cote 140-3, scans 170–185); only two explicit solutions of the loop equation (120); the conflicting fidelity bounds of §20 ("Au concours !").

**[I] Families.** (a) Profinite counterparts of discrete facts about surface groups (centralizers, normalizers, finite subgroups, torsion-free extensions): prompts LM4_FINITE_GROUP_ACTIONS, LM3_TEICHMULLER_TOWER. (b) "Is this the whole image of Galois?": LM3_TEICHMULLER_TOWER, LM2_LOOP_EQUATIONS. (c) Sections and points: LM6_POINTS_AS_SECTIONS. (d) Integrality at 2 and 3 in the group schemes: LM1_GROUP_SCHEMES, LM7_FERMAT_TOWER. (e) Statements whose proof he postponed because the notation was still moving (most of §§41–49): these need the corrected text before anything else.

## 4. What the transcription state still limits

- Second pass missing on 11 November: the pilot packages LM_P01, P02, P04–P10 (cote 140-2, scans 1–100, that is §§1–12, where the fundamental conjecture is stated); cote 140-4 from scan 115 (the end of §51, all of §§52–53); cote 140-1 (the draft). Everything said here about §§52–53 is from the first pass and the table of contents.
- LM_P060 (cote 140-3, scans 11–20, the start of §§38–39) has two first-pass returns and the checked notes belong to the earlier one. 33 fixes for 20 packages of P011–P040 are not yet merged into the current text (`second_pass\merge_fixes_open.md`): this touches §§13–31.
- The checked text still carries many open places: the card counts between 15 and 70 per package in cote 140-3. Several are in formulas the mathematics depends on (signs in the torus condition at scan 209; `ε` against `ε'`; which group a quotient is taken by). The exponent he writes as a zigzag (natural or sharp) is undecided for the whole series. No reading is final, and the prompts ask the model to report what the mathematics supports at each such place as evidence, not as a decision.
- §22 is missing in the manuscript itself.

## 5. Where this meets Les Dérivateurs

[I] Four contacts, each handled by one prompt on each side (README, "Overlaps"): the Teichmüller tower and the stratification of `M̄_{0,n}`; multi-Galois topoi and locally constant coefficients; gluing along an open and its closed complement (hole-filling here, collages and links there); levels of faithfulness ("3-fidèle" here, the three-level criterion for 1-types there). [H] The common root is that in both manuscripts he refuses a base point and a single invariant, and works with the whole system of objects and the operations between them; in 1981 the system is a tower of profinite groups with outer actions, in 1990 a family of categories of coefficients with Kan extensions. The 1981 text has the arithmetic and no homotopy theory above level 2; the 1990 text has all levels and no arithmetic. A statement that needs both is the Galois action on the profinite completion of the exit-path category of `M̄_{0,n}` (LM3_TEICHMULLER_TOWER, Part F).
