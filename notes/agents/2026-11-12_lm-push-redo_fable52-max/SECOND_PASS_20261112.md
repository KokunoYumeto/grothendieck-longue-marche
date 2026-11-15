# Second pass of the Parts of LM4, LM5, LM6 (literature-driven): change log

Author: Claude Fable 5.2, effort max (fork D of the LM expert successor, taken 12 Nov 2026, 13:55 UTC, before the
reread of sections 19-36 and before the LM3/LM3b reviews). Written 12 Nov 2026, 14:08 UTC (clock read). This file is
`SECOND_PASS_head.md` followed by `SECOND_PASS_generated.md`; the second is written by `second_pass_20261112.py`,
which builds the v2 Parts from the v1 Parts by the edit list it contains (rerun it, then `cat` the two again).

Scope. Edits that follow from the literature read by forks A, B1, B2 (`LM_EXPERT\work\lit\LIT_*.md`), from fork C's
`assembly\NOTES.md`, and from the texts read by the main agent before the fork point (Drinfeld 1990 section 4,
Harbater-Schneps, Hoshi-Minamide-Mochizuki, Minamide-Nakamura, Boggi's two preprints, 008). NOT in scope and not
done: edits that follow from the LM3/LM3b reviews; the After-blocks; `--install`. No `PROMPT.md` was changed.

Files. `LM4_PARTS_redo_20261112_v2.md` (5,134 words; v1 2,821), `LM5_PARTS_redo_20261112_v2.md` (1,985; v1 1,847),
`LM6_PARTS_redo_20261112_v2.md` (4,715; v1 2,092; now with Part E). The v1 files are untouched. `assemble_20261112.py`
now reads the v2 files (one line changed); run without `--install` it gives three assembled prompts (9,466, 7,162 and
6,978 words) with no problem reported, 0 occurrences of "Asked:", "After LM3", "After BISITE", "After LM2" and of
placeholder words, and the three work-tree `PROMPT.md` unchanged (same sha256 as in NOTES.md section 9). The only
warnings are the three empty `after_blocks.md`.

## 1. Decisions

### 1.1 Proposals of the forks' closing lists

`LIT_LM6_sections.md` (ii), 17 proposals: all accepted. 1-3 are in the new intro of the LM6 Parts (tool (1) with its
external inputs; the two consequences (T1), (T2) to be derived and used; the limits). 4, 5: B (a). 6: B (b). 7, 8:
B (c) (8 modified: "list which of the axioms are now theorems" became "determine which are theorems, each with its
proof"). 9: B (d). 10: B (e). 11: B (f). 12: C (a). 13: C (c). 14: D (a). 15: D (b), modified: the ask goes on to
other curves meeting Stoll's criterion. 16: D (c). 17: Part E (c) of LM6; its half for LM7 is not this fork's.

`LIT_LM6_anabelian.md` (ii), 8 proposals: all accepted. 1, 2: LM6 A (e) (2 extended to the m-step solvable
quotients). 3: A (a). 4, 5: A (b). 6: LM4 A (c). 7: LM6 B (f) and C (b); its half for LM3 belongs to the main agent.
8: nothing to change (009 is named in no Part).

`LIT_LM4_surfaces.md` has no list of proposals; its table was applied: the lemma of 2:sc146-147 is false as written
(LM4 B (a)); F1 is classical and its step (i) needed an amendment (C (b)); 1-fidelity is MacLachlan-Harvey and
0-fidelity Hamstrom/Scott (C (b)); Kerckhoff's theorem was read only in the announcement for closed surfaces
(B (c), C (b)); F9 (b) is not in Bridson-Conder-Reid (D (a)); the count of anti-involutions and the rank of abelian
subgroups (B (e)); Harvey's formula for the rotation angles (B (d)); his (III) (C (d)).

Rejected: none of the forks' proposals. Not adopted, with reasons: see 1.3.

### 1.2 Fork C's open decisions (NOTES.md section 7)

- 3 (proposals LM5-P1..P4, LM6-P1): accepted (`"apply": true` in `proposed_edits.json`): P1-P3 correct scan numbers
  and a title that fork C checked in the transcription; P4 and LM6-P1 bring the DRAFT line up to date. The main agent
  can set them back.
- 4 (Parts without lettered tasks): LM4 F, LM5 E and LM6 E are lettered and have a done sentence. LM6 Part E moved
  from `tail.md` into the Parts file (the old frame is kept as `tail_before_second_pass_20261112.md`; a rerun of
  `build_frames_20261112.py --force` would put Part E back into the tail and the assembler would then refuse the
  doubled Part E). Its (a), (b) are the base text, lettered; the passages of cote 140-4 behind them were not read by
  this line.
- 5 (elements of the items that no Part asked), each checked in `work\reading2\`: scan 179 "seul contre-exemple"
  (LM4 B (d)); scan 281 "homotopisme" (LM4 C (a)); scan 413 "relèvements pathologiques" (LM6 B (c)); scan 480
  "conditions ... faisant intervenir les Frobenius" and the description of admissible exterior actions (LM6 B (f));
  scan 470, the `SL(2,Z)_j` of the "lanières" (LM4 B (e)).
- 6 (section 12 in LM5 Part C (d) and nowhere else): one sentence in the intro of the LM5 Parts. Left for the main
  agent: "12" in the title, a fourth item (then "3 items" in `mid.md`), and package LM_P011 in `BACKGROUND.md`.
- 7 (leads against Parts): LM6 Lead 3: Part C now asks one numbered statement for each of its two outer clauses and
  keeps the Part for the middle one. LM6 Lead 2: the intro says how to read its "Open in general". LM5 Lead 2: Part
  B (a) now decides between the two descriptions of `B_{X,U}` instead of presupposing one.
- 8 (range of section 16): 160-179, in the heading of LM5 Part C and, for the head, as the new proposal LM5-P5
  (`"apply": true`).
- 11 (second-pass readings that lived only in the void Parts): E9a in LM4 A (a) (scans 82, 86, 91-92, 97), E9b in
  LM4 A (b) (scan 98), E11 in LM5 C (a) (scan 166).

### 1.3 Left as they are, with the reason

- Decisions 1, 2, 9, 10 of NOTES.md (After-blocks; LM4-P1..P5 "attached"; rule 11; the reviews cited in the base
  blocks): the main agent's, after the reviews.
- Wording inside the base blocks After CATHOT / GALOIS / STRATA / PATHS (NOTES.md R6, R7, R10, R12, R14 and the
  "say" sentences of 1.5 and 2.5): the recipe keeps these blocks as in the base.
- LM6 item 3 in the head still lists points now asked in LM4 (R16): head text; the Parts say where they are asked.

### 1.4 What in the v2 Parts is this line's own reasoning, not a quotation

Each is worded in the Part as an expectation "to prove or refute" or as a derivation "to check": LM4 E (b) (one class
of lifts of order 2, two of order 3, hence a subgroup of index at most 2 containing the image of
`Gal(Q̄/Q(√−3))`); LM4 D (b) (the non-solvable finite subgroups in genus at most 2 are icosahedral groups on the
sphere); LM4 B (e) (the property proposed to characterize `H`); LM4 C (c) (vanishing of both groups); LM6 B (a) (the
abelianized packets in genus 0: fork B1's computation); LM6 A (b) (the absolute Hom-form: fork B2's derivation);
LM6 B (c) (iii) (the start through finiteness of torsion over the cyclotomic field: fork B1's).

Named in the Parts without having been read by this line (said so in the Parts where it matters): Kerckhoff 1983
(announcement read), MacLachlan-Harvey 1975 and Birman-Hilden 1973 (through Margalit-Winarski), Hamstrom and Scott
(through Yagasaki), Birman-Lubotzky-McCarthy (through Behrstock-Minsky), Stallings, Boggi-Zalesskii 2025 (title
only), Betts-Stix, Hoshi 2010 (through Hoshi-Tsujimura), Saïdi (abstracts), Porowski (abstract and Theorem 1.5).
The six preprints of 2025-2026 added by this fork were read in their abstracts and main theorem statements only
(arXiv:2610.24986 main theorem; 2608.21232 Theorem A; 2611.09080 Theorem A; 2605.02577 Theorems 1.1-1.3, 2.4;
2604.26131 Theorems 1.3, 1.7; 2510.13325 Theorems A, B); every ask that uses one names it as unrefereed and asks for
the check.

### 1.5 For the main agent

1. Write the three `after_blocks.md`; then `python -I assemble_20261112.py`, then `--install` when decided.
2. LM6: the Parts name as attached the 2026 paper on the p-adic section conjecture, and use *Open homomorphisms of
   global solvably closed Galois groups* (A (b)): both PDFs must be on the list of `BACKGROUND.md` (NOTES.md R20).
3. LM4 Part E (b) and D (b) speak of `GT_0` in the sense of Harbater-Schneps; if the LM3/LM3b reviews fix another
   convention, align them.
4. LM7 (not written): proposal 17 of `LIT_LM6_sections.md` (Steklov with the 2026 theorem) belongs there too.

### 1.6 Downloads and hosts (deliverable 6)

All 68 files logged in `work\lit\downloads_{A,B1,B2,main,D}.jsonl` were entered in
`Free or receipted\free\CLAUDE_FREE_SHELF.json` (4,448 → 4,516 entries; sha256 of every file verified; backup
`CLAUDE_FREE_SHELF.before_lm_expert_20261112.json`). Hosts: arxiv.org 34, kurims.kyoto-u.ac.jp 12 (authors' pages
and RIMS preprints), ams.org 8 (open archive), gdz.sub.uni-goettingen.de 3, mathnet.ru 2, numdam.org 1,
publications.ias.edu 1, ms.u-tokyo.ac.jp 1 (journal archive), cambridge.org 1 (Compositio open archive),
archive.mpim-bonn.mpg.de 1, and authors' own pages: Harari (imo.universite-paris-saclay.fr), Stoll
(mathe2.uni-bayreuth.de), Schneps's survey (webusers.imj-prg.fr). One file does not meet the README rule of that
library as written: `grothendieck-faltings-1983\grothendieck_brief_an_faltings_GanF.pdf`, from the Grothendieck
Circle page of L. Schneps (an editor's page, not the author's; the shelf already holds EGA and FGA from the same
host). Nothing was deleted. Codex has not been told of the new entries.

## 2. Every edit (generated by `second_pass_20261112.py` from its edit list)

### LM4, intro: introappend

Reason and source: The asks now name the theorems that settle parts of them, so that the run derives his statements from them and spends itself on what is not settled. Sources and locations: LIT_LM4_surfaces.md sections 1-11; LIT_LM6_anabelian.md Part 0; Harbater-Schneps and Boggi read by the main agent.

Old wording:

> Every lettered ask below is one or more rows of the results register. A row is done only in one of the three ways of "What the outcome must be": proved in his form or in its strongest correct form; refuted by a complete counterexample with the strongest true statement proved in its place; or partly settled, with the cases proved, the computations run and the obstruction as an exact statement with the smallest undecided instance. Theorems of the literature are tools here, not answers: each time one is used, state it with its hypotheses and theorem number and then derive Grothendieck's statement from it in the form he gives, with the proof of the reduction.

Appended:

> Tools named in the asks (statements read for this prompt in freely accessible copies; "through X" means that only X, which quotes the theorem, was read, so state the theorem you use from its source). Periodic maps and finite groups of homeomorphisms of the disc, the plane and the sphere: Constantin–Kolev, Enseign. Math. 40 (1994), Lemma 2.5, Theorems 3.1 and 4.1, Corollary 4.2; Kolev, Enseign. Math. 52 (2006) (a compact group of homeomorphisms of `S²` is conjugate to a closed subgroup of `O(3)`). Realization: Kerckhoff, Ann. of Math. 117 (1983), read in the announcement Bull. AMS 2 (1980) (closed surfaces of genus ≥ 2, orientation-reversing classes allowed; the announcement says that the method covers geodesic boundary and cone points and does not name punctures). Teichmüller's theorem for type `(p, n)`: Bers, Bull. AMS 5 (1981), §3 (D). Fixed sets of finite groups in Teichmüller space and rotation angles: Harvey, Trans. AMS 153 (1971), Theorem 2, Corollary 3, Theorem 7. The Birman–Hilden property: Margalit–Winarski, arXiv:1703.03448, Theorem 2.1 (Birman–Hilden: unbranched or solvable covers), Theorem 2.2 (MacLachlan–Harvey: all finite regular branched covers of hyperbolic surfaces), Proposition 3.1. Homeomorphism groups: Hamstrom and Scott through Yagasaki, arXiv:math/0010223, Lemma 2.1 and Theorem 1.1; Earle–Eells, Bull. AMS 73 (1967), Theorem 1 (diffeomorphisms, closed surfaces). Torsion-free finite extensions: Eckmann–Müller, Comment. Math. Helv. 55 (1980), Theorem 2 and Corollary 2; Eckmann–Linnell, ibid. 58 (1983). Anti-involutions: Gross–Harris, Ann. Sci. ENS 14 (1981), Proposition 3.1; Mochizuki, *Topics surrounding the anabelian geometry of hyperbolic curves* (2003), Theorem 3.6, Corollaries 3.7, 3.8, 3.13, 3.15. Abelian subgroups: Birman–Lubotzky–McCarthy, Duke Math. J. 50 (1983), through Behrstock–Minsky, arXiv:math/0512352. Profinite completions: Bridson–Conder–Reid, arXiv:1401.3645, Theorem 5.1, Corollaries 5.2 and 5.3; Minasyan–Zalesskii, arXiv:1504.00613, Theorem 1.1 and Corollary 3.5, with Minasyan, arXiv:0905.1282, Proposition 3.2; Boggi, arXiv:2408.12486v2 (January 2026, unrefereed), Theorem C; Boggi–Zalesskii, *Finite subgroups of the profinite completion of good groups*, Bull. London Math. Soc. 57 (2025) 236–255 (known to this prompt by its title only). Profinite groups with loops: Nakamura, J. Math. Sci. Univ. Tokyo 1 (1994), Corollary (1.3.4), Lemma (2.1.2), Theorem (2.1.1); Mochizuki, *The absolute anabelian geometry of hyperbolic curves* (2004), Lemmas 1.3.1 and 1.3.7; Mochizuki, Tohoku Math. J. 59 (2007), Proposition 1.2; Mochizuki–Tamagawa, Hokkaido Math. J. 37 (2008), Proposition 1.4 and Remark 1.2.2. The groups `GT_0` and `GT`: Harbater–Schneps, Trans. AMS 352 (2000), Main Theorem and Theorem A.

### LM4, Part A (a): changed inside

Reason and source: Second-pass reading E9a of 12 Nov (Claude Opus 5.5, effort max), which lived only in the void Parts (NOTES.md 1.2); scans 82, 86 seen in reading2.

Old wording:

> and prove the corrected list.

New wording:

> and prove the corrected list. State for which types each of his formulas holds: the rank `2g + ν − 1` of `π_ab` (scan 86) is for `ν ≥ 1` only (`I = ∅` is allowed, scan 82), and `(S², pt)` is admitted with `π = 0` (scans 91–92), the one admitted type in which `κ_i` is not injective (scans 92, 97).

### LM4, Part A (b): changed inside

Reason and source: Second-pass reading E9b (NOTES.md 1.2, R2): scan 98 excepts only "le cas de la couronne" (seen in reading2); item 1 of the head points to Part A for the torus.

Old wording:

> For each excluded type give the element that makes the statement fail.

New wording:

> For each excluded type give the element that makes the statement fail. Prove his statement of scan 98 (since the centre of `π` is trivial, an extension of `Σ` by `π` is the same, up to unique isomorphism, as a homomorphism `Σ → Autext(π)`), which he excepts only for the annulus: determine what classifies the extensions for the annulus and for the torus, which he omits there (`π = Z²` has non-trivial centre too), and correct the statement.

### LM4, Part A (c): rewritten

Reason and source: Proposal (ii) 6 of LIT_LM6_anabelian.md, accepted: every statement of the profinite list except (4) for ν = 0 has a named theorem (its section 0.2), and Lemme 5 follows from slimness (section 0.3); v1 asked to prove the whole list from nothing.

Old wording:

> (c) Prove the same list for the profinite completions `π̂_{g,ν}` (his margin on scan 118: "Ce n'est démontré pour le moment dans aucun cas anabélien profini"), and prove (2) and (4) of scan 500–501 (`L_i = Centr_π(L_i^n)`; `Centr_π(Λ_i^n) = Λ_i` for the procyclic subgroups generated by the elements `x_i, y_i` of a base), which he marks "pas prouvé". Then decide whether these statements follow from his axioms for an abstract profinite group with loops (the presentation of scan 318, relation (4)) alone: a proof, or a profinite group satisfying the axioms in which one of them fails.

New wording:

> (c) The same list for the profinite completions `π̂_{g,ν}` (his margin on scan 118: "Ce n'est démontré pour le moment dans aucun cas anabélien profini"), with (2) and (4) of scans 500–501 (`L_i = Centr_π(L_i^n)`; `Centr_π(Λ_i^n) = Λ_i` for the procyclic subgroups generated by the elements `x_i, y_i` of a base), which he marks "pas prouvé". Most of it is now in the literature: derive each of his statements, in his form and for every anabelian type, from the theorem that gives it (trivial centre: Nakamura 1994, Corollary (1.3.4); trivial centralizer of every open subgroup: Mochizuki 2004, Lemma 1.3.1, or Mochizuki–Tamagawa, Proposition 1.4; no torsion: Mochizuki–Tamagawa, Remark 1.2.2; `Norm_π(L_i) = L_i`, hence `Centr_π(L_i^n) = L_i`, and distinct classes not commensurable: Mochizuki 2004, Lemma 1.3.7, and Mochizuki 2007, Proposition 1.2; (2) and (4) for `ν ≥ 1`: Nakamura 1994, Lemma (2.1.2)), writing out each reduction, and prove his Lemme 5 and Corollaire 2 of scans 498–501 from the trivial centralizers of open subgroups alone, so that (2) and (4) are not needed for them. Then prove what the literature named here does not give: (4) for `ν = 0`, that is `Centr_π(⟨x_i⟩^n) = ⟨x_i⟩` for a base element of the profinite completion of a closed surface group of genus ≥ 2 (a proof, for instance from the centralizer condition for surface groups, or a counterexample); decide whether the statements of the list follow from his axioms for an abstract profinite group with loops (the presentation of scan 318, relation (4)) alone: a proof, or a profinite group satisfying the axioms in which one of them fails; and decide which statements of the list survive in the maximal `m`-step solvable quotients of `π̂_{g,ν}`, `m ≥ 2` (centre- and torsion-freeness are claimed in arXiv:2601.07112v4, 2026, unrefereed: check the step you use; the loop-subgroup statements are yours to prove or refute, with the smallest `m` for each).

### LM4, Part B (a): rewritten

Reason and source: LIT_LM4_surfaces.md section 1 (Constantin-Kolev, arXiv:math/0303256; Kolev, arXiv:math/0304106): the lemma of 2:sc146-147 is false without "orientation preserving" (u = complex conjugation); local linearity is needed for stabilizer groups, not only single maps.

Old wording:

> (a) Prove the "lemme fondamental" of scans 141–148 completely, closing the two gaps he leaves: the lemma of scan 146–147 (a homeomorphism of finite order of `C` commuting with `z ↦ z+1` and fixing `0` is the identity; "On doit pouvoir terminer par la suite spectrale d'Adams") and the local form of an anti-involution at a fixed point (scan 148, margin; scan 440, the admitted lemma). Do it for topological actions, with no smoothness assumed.

New wording:

> (a) Prove the "lemme fondamental" of scans 141–148 completely, for topological actions with no smoothness assumed, closing the two gaps he leaves. The first is the lemma of scans 146–147 (a homeomorphism of finite order of `C` commuting with `z ↦ z+1` and fixing `0` is the identity; "On doit pouvoir terminer par la suite spectrale d'Adams"): as written it is false, since `z ↦ z̄` has order 2, commutes with `z ↦ z+1` and fixes `0`; state it with the hypothesis it needs (he is in the case `Γ = Γ⁰`), prove it, and show where his own argument uses the hypothesis. The second is the local form of an anti-involution at a fixed point (scan 148, margin; scan 440, the admitted lemma). Tools: Constantin–Kolev (Lemma 2.5, Theorems 3.1 and 4.1, Corollary 4.2) for one periodic map; Kolev's theorem for finite groups. Derive parts (a) and (b) of the lemma from them, with the invariant disc around a fixed point constructed for a finite group and not only for one map; then give a proof of the lemma of scans 146–147 along his own line (the action induced on `C/Z`, which he hopes to finish by a spectral sequence), or prove that this line cannot be completed.

### LM4, Part B (b): changed inside

Reason and source: LIT_LM6_sections.md Part 2 item 5 (Mochizuki 2003, Thm 3.6, Cor. 3.7, read on the author page): his section 33 theorem is in the literature since 2003; the picture with real punctures corrected.

Old wording:

> as his margin of scan 437 asks).

New wording:

> as his margin of scan 437 asks). His theorem with the centralizers is Mochizuki 2003, Theorem 3.6 and Corollary 3.7 (hyperbolic real Riemann surfaces, compact or not): derive it in his form, and prove what he could not, the local form at a fixed point with no smoothness (Part B (a)). With punctures on the real locus each real puncture is adjacent to two half-branches: prove that the classes of splittings recover which punctures are real, on which component of `X^σ` each lies and their cyclic order on it up to reversal, and nothing more.

### LM4, Part B (c): changed inside

Reason and source: LIT_LM4_surfaces.md section 2: Kerckhoff 1983 was not obtained; the 1980 announcement states closed surfaces; realization with punctures stays "from memory" in this line, so the prompt must not present it as read.

Old wording:

> (state the theorem you use, with punctures, and prove the reduction he sketches on scans 194–196)

New wording:

> (state the theorem you use with its source: the announcement of Kerckhoff's theorem is for closed surfaces; for punctured surfaces either cite the statement that covers them or prove that case, for instance from the theorem that convergence groups are Fuchsian (Gabai, Bull. AMS 25 (1991), Theorem 1) or, for torsion-free extensions, from Eckmann–Müller, Theorem 2; and prove the reduction he sketches on scans 194–196)

### LM4, Part B (d): changed inside

Reason and source: NOTES.md R4 (scan 179 margin, seen in reading2: no v1 Part asked it); LIT_LM4_surfaces.md section 11 (Harvey 1971, Thm 7 gives the formula he asks for, closed surfaces only).

Old wording:

> up to conjugacy, or refute it).

New wording:

> up to conjugacy, or refute it). Prove or refute his margin of scan 179 ("Ça doit être le seul contre-exemple (dans le cas renvers. d'une orientation ...)"): that, up to conjugacy, `z ↦ 1/z̄` on `C*` generates the only faithful action of a finite group on a surface of abelian type that is homotopically trivial without being an action by translations, and that any such action is by an anti-involution. For closed surfaces Harvey 1971, Theorem 7, reads the rotation angles from the epimorphism onto `Z_n`: derive your formula for `μ` from it, extend it to punctured surfaces and to groups with reflections, and define `μ` on the torsion of the profinite completion `Ê` (Part D (a)).

### LM4, Part B (e): rewritten

Reason and source: LIT_LM4_surfaces.md sections 9, 10 (count confirmed by Gross-Harris Prop. 3.1; H is not maximal for g >= 2 by the rank 3g-3); LIT_LM6_sections.md (iii) (Mochizuki 2003 Cor. 3.8); NOTES.md R16 (the question on the "lanieres" of scan 470, seen in reading2, was asked by no Part).

Old wording:

> (e) §33. Classify the conjugacy classes of anti-involutions of `X_g` and of `U_{g,ν}` in `A_{g,ν}` and in `𝒯_{g,ν}`: his proposition of scan 439 with its two marginal corrections gives two families (quotient non-orientable, `g = γ + μ`; quotient orientable, `g = 2γ + μ − 1`); prove the complete list with the count for every `g`, extend it to `ν > 0`, and prove that distinct classes in `A_g` stay distinct in `𝒯_g` (he hopes so on scan 440). Prove Corollaries 1 and 2 of scans 445–448 in both families (he proves them only when `X_g/σ` is non-orientable). For his group `G = H ⋊ {1, τ}`, `H = ⟨ρ_j⟩ ≅ Z^g` (scans 449–470): identify the `ρ_j` as mapping classes, compute the exterior action of `D̃_{2g}·H` on `π_g` on explicit generators (his task 1 of scan 467), prove or correct the presentation (52) of scan 469, and decide his three questions of scan 470 (is `H` characterized intrinsically in `𝒯_g`, is it a maximal free abelian subgroup, what is its normalizer), with proofs.

New wording:

> (e) §33. Classify the conjugacy classes of anti-involutions of `X_g` and of `U_{g,ν}` in `A_{g,ν}` and in `𝒯_{g,ν}`: his proposition of scan 439 with its two marginal corrections gives two families (quotient non-orientable, `g = γ + μ`; quotient orientable, `g = 2γ + μ − 1`); prove the complete list with the count for every `g` (expected `(g+1) + ⌊(g+2)/2⌋ = ⌊(3g+4)/2⌋`, the classification of real curves of Weichold and Klein: Gross–Harris, Proposition 3.1), extend it to `ν > 0` with the position of the punctures as part of the invariant, and prove that distinct classes in `A_g` stay distinct in `𝒯_g` (he hopes so on scan 440; derive it from the uniqueness of realization of Part C (b)). Prove Corollaries 1 and 2 of scans 445–448 in both families (he proves them only when `X_g/σ` is non-orientable), and derive from them and from Mochizuki 2003, Corollary 3.8 (the components of `M_{g,r}(R)` correspond to the classes of involutions over complex conjugation in the extended mapping class group, with their centralizers) the number of components of `M_{g,ν}(R)` for every `(g, ν)`. For his group `G = H ⋊ {1, τ}`, `H = ⟨ρ_j⟩ ≅ Z^g` (scans 449–470): identify the `ρ_j` as mapping classes, compute the exterior action of `D̃_{2g}·H` on `π_g` on explicit generators (his task 1 of scan 467), prove or correct the presentation (52) of scan 469, and settle his questions of scan 470 with proofs: is `H` a maximal free abelian subgroup (the maximal rank is `3g − 3`, Birman–Lubotzky–McCarthy, so for `g ≥ 2` exhibit the larger subgroup, and then find and prove the property that does characterize `H`, for instance among subgroups generated by Dehn twists about curves whose union does not disconnect `X_g`); what is its normalizer and how does it act on `H`; and do the groups `SL(2, Z)_j` attached to the "lanières" through the tubes `T_j` (his task 2 of scans 467–469: the one-holed torus made of `T_j` and a strip, with its special Teichmüller group) play the part of the rank-one subgroups of a reductive group: construct them in `𝒯_g`, compute their commutation relations with `H` and with each other, decide whether `H` and these subgroups generate `𝒯_g⁺`, and state and prove the analogy in the strongest form that is true.

### LM4, Part C (a): changed inside

Reason and source: NOTES.md R5 (scan 281, seen in reading2): item 5 of the head quotes the sentence and no v1 Part asked what it says.

Old wording:

> à reprendre avec soin").

New wording:

> à reprendre avec soin"). On the same scan he adds "Le plus agréable serait que ce soit un homotopisme ... qui exprimerait qu'on a une ∞-équivalence": identify the map he means, state it as the comparison between the fixed points of `Γ` in `A` (for the action by conjugation through `u`) and the homotopy fixed points, and prove that it is a homotopy equivalence for finite `Γ` in the anabelian types; decide each abelian type.

### LM4, Part C (b): rewritten

Reason and source: LIT_LM4_surfaces.md sections 1, 3, 4, 5: the uniqueness statement (FINDINGS F1) is classical (Harvey 1971 Thm 2, Cor. 3, read; MacLachlan-Harvey through Margalit-Winarski), so the ask is the proof in his generality; step (i) corrected (Kolev); 1-fidelity is MacLachlan-Harvey, not Birman-Hilden; 0-fidelity is Hamstrom/Scott through Yagasaki.

Old wording:

> (b) Prove his conjecture of scans 270–271 for every anabelian type and every finite `Γ`, orientation-reversing elements allowed, in the topological category: each of the four levels with a complete proof. The following chain is proposed and is not authority; check every link, with exact hypotheses (punctures, orientation reversal, homeomorphisms against diffeomorphisms), and replace any link that fails. Existence of lifts: the realization theorem for finite subgroups of the mapping class group. Uniqueness up to `A⁰`: if `ρ_1, ρ_2: Γ → A` have the same image in `π_0(A)`, choose invariant conformal structures `c_1, c_2`; the extremal quasiconformal map `h: (S, c_1) → (S, c_2)` isotopic to the identity is unique, and `ρ_2(g)^{-1} h ρ_1(g)` is extremal in the same class, hence equal to `h`. Connectedness of `(A⁰)^u`: fibre-preserving homeomorphisms isotopic to the identity are so through fibre-preserving ones. `π_1((A⁰)^u) = 0`: the identity component of `A^u` is the identity component of the homeomorphism group of the quotient surface with its branch points removed. State the final theorem as an equivalence of 2-categories and say what fails for each abelian type and for infinite `Γ` (give an infinite `Γ` for which each level fails).

New wording:

> (b) Prove his conjecture of scans 270–271 for every anabelian type and every finite `Γ`, orientation-reversing elements allowed, in the topological category: each of the four levels with a complete proof. The statement is classical for closed surfaces and orientation-preserving groups (Harvey 1971, Theorem 2 and Corollary 3: the fixed set of a finite group in Teichmüller space is the image of one Teichmüller space; MacLachlan–Harvey 1975): what is asked is the proof in his generality, with punctures, orientation-reversing elements and actions by homeomorphisms with no smoothness. The following chain is proposed and is not authority; check every link with its exact hypotheses and replace any link that fails. Existence of lifts: the realization theorem for finite subgroups of the extended mapping class group (for punctured surfaces state the theorem you use with its source, or prove that case from the closed one). Uniqueness up to `A⁰`: if `ρ_1, ρ_2: Γ → A` have the same image in `π_0(A)`, choose invariant conformal structures `c_1, c_2` of finite type (this needs the quotient to be a surface with boundary, cone points and corner points, hence local linearity of the finite stabilizer groups and not only of single periodic maps: Kolev's theorem; prove this step); the extremal quasiconformal map `h: (S, c_1) → (S, c_2)` isotopic to the identity is unique (Bers, §3 (D), for type `(p, n)`), and `ρ_2(g)^{-1} h ρ_1(g)` is orientation preserving, has the same maximal dilatation and is isotopic to the identity, hence equals `h`. Connectedness of `(A⁰)^u`: fibre-preserving homeomorphisms isotopic to the identity are so through fibre-preserving ones (Margalit–Winarski, Theorem 2.2; the quoted statements are for orientation-preserving deck groups: prove the case with reflections). `π_1((A⁰)^u) = 0`: the identity component of `A^u` is the identity component of the homeomorphism group of the quotient surface with its branch points and punctures marked and its mirror boundary (Yagasaki, Lemma 2.1; prove that no exceptional pair of that lemma occurs for hyperbolic `U`). State the final theorem as an equivalence of 2-categories, and prove for each abelian type and for infinite `Γ` which levels fail (give an infinite `Γ` for which each level fails).

### LM4, Part C (c): changed inside

Reason and source: LIT_LM4_surfaces.md section 4 ("What it gives"): a derivation exists for orientation-preserving groups; it is given as an expectation to prove, not as settled.

Old wording:

> and deduce the exact value of `π_0(A^{0Γ})`.

New wording:

> and deduce the exact value of `π_0(A^{0Γ})` (expected for hyperbolic `U`: both vanish and `A^{0Γ}` is connected, by the Birman–Hilden property for `U → U/Γ` and the uniqueness of realization applied to `V = U ∖ S^!`; write the proof, groups with reflections included, where the quoted Birman–Hilden statements do not apply).

### LM4, Part C (d): changed inside

Reason and source: LIT_LM4_surfaces.md section 7 (Eckmann-Mueller 1980 Thm 2, Cor. 2 read; Stallings and Bieri-Eckmann from memory, so the step is asked).

Old wording:

> (also scan 353).

New wording:

> (also scan 353; for `ν = 0` this is Eckmann–Müller 1980, Corollary 2, and the extension can be a non-orientable surface group when the finite group reverses the orientation, so his statement has to be corrected to allow it; for `ν ≥ 1` derive it from Stallings's theorem on torsion-free virtually free groups and Eckmann–Müller, Theorem 2, on pairs, proving the step that makes `(E; centralizers of the L_i)` a duality pair).

### LM4, Part D (a): rewritten

Reason and source: LIT_LM4_surfaces.md section 8: FINDINGS F9 (a) is Bridson-Conder-Reid Thm 5.1 plus a short argument; F9 (b) is not in that paper (centralizer condition: Minasyan-Zalesskii Thm 1.1 with Minasyan Prop. 3.2, cocompact case read; free case from memory); reflections and dihedral subgroups are open in the texts read.

Old wording:

> (a) For a finite `G ⊂ 𝒯(π_0)` (an exterior action stabilizing a discretization `π_0 ⊂ π = π̂_0`), with discrete extension `E` and completion `Ê`: prove or refute his two "conjectures sans vergogne" of scan 393: the map from `π_0`-classes of splittings of `E → G` to `π`-classes of splittings of `Ê → G` is bijective, and `π^G = 1` for `G ≠ 1`. Prove the profinite forms of the theorem of scans 148–149 (every finite subgroup of `Ê` meeting `π` trivially is cyclic or dihedral; finitely many classes; unique maximal section subgroups) and of c), d), e) of scans 197–198. Use the theorems on torsion in profinite completions of Fuchsian groups if they apply, state them exactly, and prove what they do not give (dihedral subgroups, the centralizer statement, the loop structure).

New wording:

> (a) For a finite `G ⊂ 𝒯(π_0)` (an exterior action stabilizing a discretization `π_0 ⊂ π = π̂_0`), with discrete extension `E` and completion `Ê`: prove his two "conjectures sans vergogne" of scan 393 for orientation-preserving `G` from the named theorems, writing each reduction: the bijection of classes of splittings from Bridson–Conder–Reid, Theorem 5.1 (every finite subgroup of `Ê` is conjugate into `E`; maximal finite subgroups conjugate in `Ê` are conjugate in `E`), by the passage from `Ê`-conjugacy to `π`-conjugacy; and `π^G = 1`, which is not in that paper, from the centralizer condition `C_Ê(k) = closure of C_E(k)` (for cocompact `E`: Minasyan–Zalesskii, Theorem 1.1, with Minasyan, Proposition 3.2; for `ν > 0`, where `E` is a free product of cyclic groups, prove it, stating the theorem on centralizers of torsion in free profinite products that you use). Then prove what these do not give: both statements when `G` contains orientation-reversing elements (`E` is then a group with reflections; for anti-involutions the bijection of classes of elements of order 2 follows from Minasyan–Zalesskii, Corollary 3.5; decide the dihedral subgroups, and compute `π^G` for them: expected `Ẑ` for the reflection in an oval and `1` for a line, as in his theorem of scans 440–445); the profinite forms of the theorem of scans 148–149 (every finite subgroup of `Ê` meeting `π` trivially is cyclic or dihedral; finitely many classes; unique maximal section subgroups) and of c), d), e) of scans 197–198; and the profinite `μ`: prove that the multiplier of Part B (d) extends to the torsion of `Ê` with values in `T̂ ⊗ Q/Z` and is invariant under the automorphisms of `Ê` that preserve the loop structure.

### LM4, Part D (b): rewritten

Reason and source: Boggi, arXiv:2408.12486v2, Theorem C and section 1.1 (read by the main agent: congruence subgroup property known for genus at most 2; Theorem C quoted): finite subgroups of the completion are largely settled there (unrefereed), so the ask is split and the weight goes to the non-solvable case and to the full Autext_lac. Boggi-Zalesskii is named by title only.

Old wording:

> (b) Without the hypothesis that `G` stabilizes a discretization (his remark on scan 384: "ce n'est sans doute pas automatique"): decide, for the types `(0,3)`, `(0,4)`, `(1,1)`, whether every finite subgroup of `𝒯̂̂_{g,ν} = Autext_lac(π̂_{g,ν})` is conjugate to a subgroup of `𝒯_{g,ν}`. Either prove it, or construct a finite subgroup that is not (for instance of order 2 or 3 in `Autext_lac` of the free profinite group of rank 2, by a program working in finite quotients and a proof that the examples lift), or prove the pro-`ℓ` form and state exactly what is missing.

New wording:

> (b) Without the hypothesis that `G` stabilizes a discretization (his remark on scan 384: "ce n'est sans doute pas automatique"): decide, for the types `(0,3)`, `(0,4)`, `(1,1)`, whether every finite subgroup of `𝒯̂̂_{g,ν} = Autext_lac(π̂_{g,ν})` is conjugate to a subgroup of `𝒯_{g,ν}`. The question has two layers. For finite subgroups of the completion `𝒯̂_{g,ν}` (it embeds in `𝒯̂̂_{g,ν}` for `g ≤ 2`, where the congruence subgroup property is known) Boggi, arXiv:2408.12486v2, Theorem C, states for genus ≤ 2: the classes of solvable finite subgroups of the mapping class group and of its profinite completion correspond bijectively, torsion elements are conjugacy distinguished, and the centralizer of a finite subgroup `G` in the completion is the closure of its centralizer in the discrete group (unrefereed: check the step you use; state also what Boggi–Zalesskii give). Derive from it the answer for this layer, extend it to orientation-reversing elements, and settle the finite subgroups that are not solvable (in genus ≤ 2 these are icosahedral groups acting on the sphere with marked points: prove that this is the list). For finite subgroups of `𝒯̂̂_{g,ν}` outside `𝒯̂_{g,ν}` nothing is known to this prompt: either prove that every finite subgroup is conjugate into `𝒯̂_{g,ν}`, or construct one that is not (for instance of order 2 or 3 in `Autext_lac` of the free profinite group of rank 2, by a program working in finite quotients and a proof that the examples lift), or prove the pro-`ℓ` form and state exactly what is missing. For `(0,3)` this is a statement about torsion in the centralizer of `S_3`, the group `GT_0` of Part E (b): decide whether its elements of finite order are the conjugates of the element `(−1, 1)`.

### LM4, Part D (d): changed inside

Reason and source: arXiv:2605.02577 (abstract and Theorems 1.1-1.3, 2.4 seen by this fork in the PDF text): a 2026 claim on torsion in profinite Fuchsian-type groups, to be used and checked.

Old wording:

> with what you tried.

New wording:

> with what you tried. Collas–Philip–Yamaguchi (arXiv:2605.02577, May 2026, unrefereed) study the profinite analogues of Fuchsian groups (their Theorems 1.3 and 2.4: such a group has a torsion-free open normal subgroup, with a bound on the derived length of the quotient): state exactly what they give for this question, check the step you use, and prove the rest.

### LM4, Part E (b): changed inside

Reason and source: Harbater-Schneps, Trans. AMS 352 (2000), Main Theorem and Theorem A (read by the main agent; quoted in the shared context): the centralizer of S_3 in the loop-preserving outer automorphisms of the free profinite group of rank 2 is their GT_0. The expectation in brackets is this fork's reasoning, marked to prove or refute.

Old wording:

> and decide whether it is the whole centralizer.

New wording:

> and decide whether it is the whole centralizer. The centralizer itself is the group `GT_0` of Harbater–Schneps (Main Theorem (a)): pairs `(λ, f) ∈ Ẑ* × F̂_2'` satisfying (I) and (II), which by their Theorem A are the conditions `[θ, F] = inn(f)` and `[ω, F] = inn(y^m f)`, `m = (λ − 1)/2`, on the lift `F: x ↦ x^λ, y ↦ f^{-1} y^λ f`, with `θ, ω` lifts of a transposition and of a 3-cycle. So his condition asks whether these inner automorphisms can be removed by changing the lift within its class: write it as a statement about the classes of lifts of order 2 and of order 3 and settle it (expected, to prove or refute: the transposition `z ↦ 1 − z` has one fixed point in `U`, hence one `π̂`-class of lifts of order 2 by Bridson–Conder–Reid, Theorem 5.1, so the first condition holds for every element of the centralizer; the 3-cycle has the two fixed points `e^{±iπ/3}`, hence two classes of lifts of order 3, which an element of the centralizer preserves or exchanges, so the second condition cuts out a subgroup of index at most 2 that contains the image of `Gal(Q̄/Q(√−3))`: determine it in terms of `(λ, f)`).

### LM4, Part F: Part rewritten

Reason and source: NOTES.md R3: Part F had numbered lemmas and no lettered tasks, so the outcome section gave it no table line and no bar. Boggi Theorem C (iii) added as a tool for (b).

Old wording:

> **F. What the later sections use (§§26–32; scans 318–436).** State as numbered lemmas, with proofs, exactly what §§26–32 take from this part, in the form they use: (1) the action of a finite group on the set of discretizations and prediscretizations of `π̂` and its fixed points (scans 352–358); (2) for a finite `G ⊂ 𝒯⁺` the statements (c), (d) of scans 383–387 (finiteness of `Z`, open image of `N_a ∩ Z(G) → Γ_a`) translated into statements about `Centr_{𝒯̂̂}(G)` that do not mention `N_a`, proved or refuted in that form; (3) the lifting statement of scans 390–393 (the stabilizer of a point `P` of `[U^!]` in `𝒯(π_0)^G` lifts canonically to `𝔖(π_0)^G`) and its profinite form. LM3_TEICHMULLER_TOWER and LM6_POINTS_AS_SECTIONS cite these lemmas: give each a stable label.

New wording:

> **F. What the later sections use (§§26–32; scans 318–436).** Each of the following is a numbered lemma with a stable label (LM4-F.a, LM4-F.b, LM4-F.c), stated in the form in which §§26–32 use it and proved; LM3_TEICHMULLER_TOWER and LM6_POINTS_AS_SECTIONS cite these labels.
> (a) The action of a finite group on the sets of discretizations and of prediscretizations of `π̂` and its fixed points (scans 352–358): determine the fixed sets and prove the answer.
> (b) For a finite `G ⊂ 𝒯⁺`, the statements (c), (d) of scans 383–387 (finiteness of `Z`; open image of `N_a ∩ Z(G) → Γ_a`), translated into statements about `Centr_{𝒯̂̂}(G)` and `Centr_{𝒯̂}(G)` that do not mention `N_a`: prove or refute each in that form. For genus ≤ 2, Boggi's Theorem C gives the centralizer of `G` in the completion `𝒯̂⁺` as the closure of the discrete centralizer: derive what follows for (c) and (d), and prove or refute the same equality for the centralizer in `𝒯̂̂`, in the smallest type where it is not clear.
> (c) The lifting statement of scans 390–393 (the stabilizer of a point `P` of `[U^!]` in `𝒯(π_0)^G` lifts canonically to `𝔖(π_0)^G`), and its profinite form: prove both, with the exact group to which the stabilizer lifts.

### LM4, Part F done sentence: changed

Reason and source: Follows the lettering.

Old wording:

> Done for Part F: each lemma is proved or refuted; none is only stated.

New wording:

> Done for Part F: each of (a), (b), (c) is a labelled lemma, proved or refuted; none is only stated.

### LM4, Part A (d): changed inside

Reason and source: Push standard rule 1: "say" on its own replaced by a producing verb.

Old wording:

> say exactly which subgroups

New wording:

> determine exactly which subgroups

### LM4, Part B (b): changed inside

Reason and source: Push standard rule 1.

Old wording:

> and say what the classes of splittings see

New wording:

> and prove what the classes of splittings see

### LM4, Part C (d): changed inside

Reason and source: Push standard rule 1.

Old wording:

> say exactly which step uses the geometry.

New wording:

> isolate the step that uses the geometry as an exact statement.

### LM5, intro: introappend

Reason and source: NOTES.md R8: section 12 is asked in Part C (d) and named nowhere else in the prompt.

Old wording:

> Every lettered ask is one or more rows of the results register, done only as "What the outcome must be" says: proved in his form or its strongest correct form; refuted by a complete counterexample with the strongest true statement proved in its place; or partly settled with the cases proved and the obstruction as an exact statement with the smallest undecided instance. SGA 1, SGA 4 and the later Galois theory of topoi are tools: when one of them gives a statement of his, cite the theorem and write the derivation of his statement in his generality and his form (no base points, no connectedness, groupoids and not groups).

Appended:

>  Part C (d) concerns §12 (scans 103–109), which the title and the items of this prompt do not name: it is part of the task and has its own rows.

### LM5, Part B (a): rewritten

Reason and source: NOTES.md 2.5: Lead 2 and the base block After STRATA ask to decide between two descriptions of B_{X,U}; v1 Part B (a) presupposed one of them. The ask now decides it with proof, so that Lead 2 gets its numbered statement.

Old wording:

> (a) Define `B_{X,U}` (later `B_{X;S}`) exactly as on scans 123–127, prove that `B_{π_1,U} → B_{X,U}` is an open induction morphism with closed complement `B_{π_1,D}` and gluing functor `σ_* ρ^*`, and prove his formula `π_1(X) = π_1(U)/⟨⟨ρ_i(Π_i)⟩⟩` (scan 123).

New wording:

> (a) Define `B_{X,U}` (later `B_{X;S}`) exactly as on scans 123–127, and decide between the two candidates named in Lead 2 and in the block After STRATA: the gluing of `B_{π_1,U}` and `B_{π_1,D}` along the functor `σ_* ρ^*` (sheaves on `X` locally constant on `U`), or the Kummer-étale (logarithmic) topos of `(X, S)`. Prove from his definition that it is the first: `B_{π_1,U} → B_{X,U}` is an open induction morphism with closed complement `B_{π_1,D}` and gluing functor `σ_* ρ^*`; construct the comparison morphism with the second and prove exactly how they differ (objects, points, cohomology with torsion coefficients). Prove his formula `π_1(X) = π_1(U)/⟨⟨ρ_i(Π_i)⟩⟩` (scan 123).

### LM5, Part C (head): changed inside

Reason and source: NOTES.md section 5 item 6 and decision 8: the last sentence of section 16 runs onto the first lines of scan 179.

Old wording:

> (scans 103–109, 160–178)

New wording:

> (scans 103–109, 160–179)

### LM5, Part C (a): changed inside

Reason and source: Second-pass reading E11 of 12 Nov (fix 01-030), which lived only in the void Parts (NOTES.md 1.2); scan 166 seen in reading2.

Old wording:

> of scans 163–168:

New wording:

> of scans 163–168 (on scan 166 the lower object of the diagram is `B_X`: the `Π_1` in its subscript is struck out):

### LM5, Part E: Part rewritten

Reason and source: NOTES.md R9: Part E had no lettered tasks. Same mathematics, lettered.

Old wording:

> **E. Relation to the higher theory.** The companion work on *Les Dérivateurs* has a package (GALOIS) on locally constant coefficients for an arbitrary coefficient theory. Construct the common generalization (the shape, or fundamental pro-∞-groupoid, of a topos and its truncations); prove that his `E_[1]` is its 1-truncation and that the tower of Part A (c) is its Postnikov tower; and for each statement of Parts A–C decide, with proof or counterexample, whether it extends to all levels or is special to level 1 (in particular 1.1, 2.1, the van Kampen statement of Part C (a), and the acyclicity of Part C (b)). The coefficient-relative theory itself is in GALOIS: use it, do not redo it.

New wording:

> **E. Relation to the higher theory.** The companion work on *Les Dérivateurs* has a package (GALOIS) on locally constant coefficients for an arbitrary coefficient theory. The coefficient-relative theory itself is in GALOIS: use it, do not redo it.
> (a) Construct the common generalization: the shape, or fundamental pro-∞-groupoid, of a topos and its truncations, under his hypotheses of §2 (locally connected, locally simply connected) and under the weaker ones decided in Part A.
> (b) Prove that his `E_[1]` is its 1-truncation and that the tower of Part A (c) is its Postnikov tower.
> (c) For each statement of Parts A–C decide, with proof or counterexample, whether it extends to all levels or is special to level 1 (in particular 1.1, 2.1, the van Kampen statement of Part C (a), and the acyclicity of Part C (b)).

### LM5, Part E done sentence: changed

Reason and source: Follows the lettering.

Old wording:

> Done for Part E: a theorem for the comparison, and a decided list.

New wording:

> Done for Part E: (a) is a construction, (b) a theorem, (c) a decided list with a proof or a counterexample for each entry.

### LM5, Part B (b): changed inside

Reason and source: Push standard rule 1.

Old wording:

> and say what changes for `p`-torsion.

New wording:

> and prove what changes for `p`-torsion (the exact statement that replaces the comparison, with an example where it fails).

### LM5, Part D (c): changed inside

Reason and source: Push standard rule 1.

Old wording:

> and say which of his two computations is right.

New wording:

> and decide which of his two computations is right.

### LM6, intro: intro

Reason and source: Proposals (ii) 1-3 of LIT_LM6_sections.md and (ii) 4 of LIT_LM6_anabelian.md, accepted: the external inputs of the 2026 theorem are named so that "check the step" has a target; the two consequences (local affine statement; global equivalence) and the known limits become tools; exact theorem numbers; the 2025-2026 preprints named as unrefereed claims. Resolves NOTES.md R18 (Lead 2 stale).

Old wording:

> Every lettered ask is one or more rows of the results register, done only as "What the outcome must be" says: proved in his form or its strongest correct form; refuted with the strongest true statement proved in its place; or partly settled with the cases proved, the computations run and the obstruction as an exact statement with the smallest undecided instance. Two recent claims are to be used and not re-proved: the local `p`-adic section conjecture for smooth proper geometrically connected curves of genus ≥ 2 over finite extensions of `Q_p` (OpenAI, *The p-adic section conjecture*, 6 October 2026, Theorem 1.1; attached), and the theorems of Tamagawa and Mochizuki on the Isom- and Hom-forms. Both kinds are tools: state what you use with its hypotheses, check the step of the 2026 paper you rely on (it is unrefereed), and derive his statement in his form. Do not spend the run re-deriving them.

New wording:

> Every lettered ask is one or more rows of the results register, done only as "What the outcome must be" says: proved in his form or its strongest correct form; refuted with the strongest true statement proved in its place; or partly settled with the cases proved, the computations run and the obstruction as an exact statement with the smallest undecided instance. Theorems and recent claims are tools here: state what you use with its hypotheses and its number, check the step you rely on when the source is unrefereed, and derive his statement in his form. Do not spend the run re-deriving them.
> 
> Tools. (1) The local `p`-adic section conjecture for smooth proper geometrically connected curves of genus ≥ 2 over finite extensions of `Q_p` (OpenAI, *The p-adic section conjecture*, 6 October 2026, Theorem 1.1; attached; unrefereed, no formal proof). Its external inputs of weight are Mochizuki–Tsujimura's resolution of nonsingularities (RIMS-1974, Theorem A and Proposition 2.4 (iv); itself a recent preprint), the lifting theorem of Amini–Baker–Brugallé–Rabinoff (arXiv:1303.4812, Theorem 7.7), Pop–Stix (arXiv:1111.1354, Theorem 26) and Koenigsmann (arXiv:math/0305226, Proposition 2.4 (2)). (2) Two consequences, to be derived in a few lines and then used: (T1) for a finite extension `k` of `Q_p` and every hyperbolic curve `U = X ∖ S` over `k`, every section of `π_1(U) → G_k` is the section of a point of `U(k)` or is cuspidal at a point of `S(k)`, the packets at distinct cusps are disjoint, and each is a torsor under `H¹(k, Ẑ(1))`, the profinite completion of `k^×` (neighbourhood argument: Stix, arXiv:1203.3236, 2.1.2 and Corollary 5; packets: Stix, arXiv:0809.0017, Proposition 8 and Theorem 14); (T2) for a smooth proper curve `C` of genus ≥ 2 over a number field `K`, the section conjecture for `C` holds if and only if `C(A_K)_•^{f-cov} = C(K)` (Proposition 8.1 and Theorem 8.2 of the 2026 paper, with Harari–Stix, Theorem 2.1, and Stix, arXiv:1203.3236, Corollary 5). (3) Limits: non-geometric sections exist for the geometrically pro-`p` quotient (Hoshi, Publ. RIMS 46 (2010); Hoshi–Tsujimura, RIMS-1950) and for the geometrically metabelian and nilpotent-by-abelian quotients over `p`-adic fields (Saïdi, arXiv:1510.06864, arXiv:2109.14882); for an elliptic curve over a `p`-adic field the section map is not surjective; so no fallback to a quotient may assume geometricity. (4) Isom- and Hom-forms: Tamagawa, Compositio Math. 109 (1997), Theorem (0.3) and Remark (7.3)(i); Mochizuki, Invent. Math. 138 (1999), Theorem A (dominant morphisms and open homomorphisms, sub-`p`-adic fields) and Theorem C = 19.1 (injectivity); Mochizuki, *The absolute anabelian geometry of hyperbolic curves* (2004), Lemma 1.3.1, Corollary 1.3.3, Theorem 1.3.4, Lemmas 1.3.7 and 1.3.9; Nakamura, J. Math. Sci. Univ. Tokyo 1 (1994), Theorem (2.1.1); Hoshi–Mochizuki, Hiroshima Math. J. 41 (2011), Theorem C and Corollaries 6.4, 6.5. (5) Sections: Grothendieck's letter to Faltings of 27 June 1983 (conjecture (7), the correction on packets, the PS on the kernel of the cyclotomic character); Stix, arXiv:0809.0017 (Proposition 8, Corollary 12, Theorems 14, 17, 20, Corollary 22, Theorem 45); Esnault–Hai, arXiv:math/0703877 (Theorem 5.1, Proposition 5.3, Theorems 5.5, 6.5, Corollary 6.9); Deligne, *Le groupe fondamental de la droite projective moins trois points* (1989), §15; Koenigsmann, Lemma 1.7; Mochizuki–Tsujimura, Theorem F; over `R`: Mochizuki 2003 (*Topics surrounding the anabelian geometry of hyperbolic curves*), Theorem 3.6, Corollaries 3.7, 3.8, 3.13, 3.15; Stix, arXiv:0802.4125, Theorem 26; Bresciani–Vistoli, arXiv:2012.06278. (6) Preprints of 2025–2026, all unrefereed, to be used as claims and checked where used: Luo–Watanabe, arXiv:2610.24986 (the sections of the universal complete curve over `M_{g,n}`, `g ≥ 3`, `n ≥ 1`, over fields finitely generated over `Q`, are the `n` tautological ones); Holzschuh–Schmidt–Stix, arXiv:2608.21232 (families of hyperbolic curves over a normal base of finite type over a sub-`p`-adic field are anabelian for dominant morphisms); Carlson–Corwin, arXiv:2611.09080 (cuspidal sections in any dimension, relative to a normal crossings compactification); Collas–Philip–Yamaguchi, arXiv:2605.02577, and Steklov, arXiv:2602.17746 (hyperbolic Deligne–Mumford curves; Selmer sections of the Fermat curves); Porowski, arXiv:2509.15660 and arXiv:2607.27746 (reductions of Selmer sections); Pop, arXiv:2604.26131 (birational sections for small quotients); Holzschuh, arXiv:2510.13325 (the real section conjecture in étale homotopy theory). Lead 2 of this prompt was written before (1): read its "Open in general" with (1), (T1) and (T2).

### LM6, Part A (a): changed inside

Reason and source: Proposal (ii) 3 of LIT_LM6_anabelian.md, accepted; the case of positive characteristic added as the part not covered by the named theorem.

Old wording:

> (scan 54, margin).

New wording:

> (scan 54, margin): this is the statement that `G_K` is slim (Mochizuki 1999, Lemma 15.8; Mochizuki 2004, Corollary 1.3.3, for sub-`p`-adic `K`): give a proof for `K` of finite type over `Q` from what he had (Galois theory and number fields), and decide the statement for `K` of finite type over `F_p`, which he mentions on scan 109.

### LM6, Part A (b): rewritten

Reason and source: Proposals (ii) 4 and 5 of LIT_LM6_anabelian.md, accepted: exact tool theorems; the absolute Hom-form from family 031 with Mochizuki Thm A (its section 1.2 (c), a derivation of fork B2, unchecked, hence asked as a proof with the step of 031 to check); section 35 named as settled.

Old wording:

> (b) Prove the "conjecture bordélique" 7.1 (scan 35) in each of his cases I, II, III, IV a)–d) of §8 (scans 55–67), in the following precise sense: for each case say which theorem gives it over which fields (number fields, finitely generated extensions of `Q`, sub-`p`-adic fields), and write the proof of the reduction from his groupoid formulation, with Kummer data and degrees, to that theorem. Case IV b) (scan 66: every homomorphism of extensions `E' → E`, `E'` from a complete curve, `E` from `X ∖ S` with `S ≠ ∅`, is trivial on `π'`; "Il faudrait essayer de vérifier ce point directement") is to be proved directly as he asks, or derived, or refuted. Case III is Part B.

New wording:

> (b) Prove the "conjecture bordélique" 7.1 (scan 35) in each of his cases I, II, III, IV a)–d) of §8 (scans 55–67), in the following precise sense: for each case name the theorem that gives it and the fields over which it does (Tamagawa 1997, Theorem (0.3): isomorphisms, affine hyperbolic curves, fields finitely generated over `Q`; Mochizuki 1999, Theorem A: open homomorphisms against dominant morphisms, hyperbolic curves over sub-`p`-adic fields, profinite and pro-`p`), and write the proof of the reduction from his groupoid formulation, with Kummer data and degrees, to that theorem. Case IV b) (scan 66: every homomorphism of extensions `E' → E`, `E'` from a complete curve, `E` from `X ∖ S` with `S ≠ ∅`, is trivial on `π'`; "Il faudrait essayer de vérifier ce point directement") is to be proved directly as he asks, or derived, or refuted. Case III is Part B. Then go beyond the relative statements: prove the absolute Hom-form over number fields (for hyperbolic curves `X/K`, `Y/L` over number fields, every continuous homomorphism `π_1(X) → π_1(Y)` with open image comes from a unique dominant morphism of schemes `X → Y`, up to inner automorphisms) from Theorem A and the claimed Hom-form of the Neukirch–Uchida theorem (OpenAI, *Open homomorphisms of global solvably closed Galois groups*, 5 October 2026, Theorem 1.1; unrefereed: the step to check is its use of Uchida's local correspondence for open homomorphisms that are not surjective), proving that the image of the geometric subgroup is geometric; and decide the same over finite extensions of `Q_p`, where the absolute statement fails already in dimension 0. His §35 is settled and is a tool: the outer Galois action is faithful for every hyperbolic curve over a number field or a `p`-adic field (Hoshi–Mochizuki 2011, Theorem C), and his Lemme 5 follows from the trivial centralizers of open subgroups alone. Prove instead what the literature named here does not give: the kernel of `G_K → Out π_1(U_K̄)` for `K` finitely generated over `Q` of positive transcendence degree (it lies in the kernel of `G_K → G_Q`: determine it), and the kernels for the pro-`ℓ` completions.

### LM6, Part A (e): rewritten

Reason and source: Proposals (ii) 1 and 2 of LIT_LM6_anabelian.md and remark (iii) of LIT_LM6_sections.md, accepted: 2:sc483 is false as written; the true statement is Nakamura 1994 Thm (2.1.1) (read by fork B2); the commutant statement is Tamagawa 1997 Remark (7.3)(i).

Old wording:

> (e) §34, scan 483: prove his conjecture that the loop structure is determined by the exterior Galois action (the `L_i` are the maximal subgroups of `π` whose normalizer in `E` has open image in `Γ`, and every non-trivial subgroup with that property lies in a unique `L_i`), over number fields, and decide it over finite extensions of `Q_p`. Prove the full faithfulness of scan 484 for dominant morphisms from the Hom-form, and prove his statement of scan 485 that the commutant of the Galois image in `Autext_lac(π̂_{0,3})` is `S_3`.

New wording:

> (e) §34, scan 483. His conjecture as written (the `L_i` are the maximal subgroups of `π` whose normalizer in `E` has open image in `Γ`, and every non-trivial subgroup with that property lies in a unique `L_i`) is false as it stands: `π` itself, every open subgroup of `π` normal in `E`, and the closure of the commutator subgroup have the property. Prove the correct statements. (1) Nakamura's theorem in his language (Nakamura 1994, Theorem (2.1.1); Stix, Theorem 20 and Corollary 22): over a number field a non-trivial procyclic subgroup of `π` lies in a loop subgroup if and only if its normalizer in `E` has open image in `Γ` and acts on it through the cyclotomic character; derive it, and from it the description of the `L_i` as the maximal such subgroups and of the `E_i` as their normalizers. (2) Decide whether the cyclotomic condition can be dropped: classify the closed procyclic subgroups `A ≠ 1` of `π` whose normalizer in `E` has open image in `Γ` (a Galois-stable line of weight −1 in the homology of a cover exists when its Jacobian has a factor with complex multiplication: prove that no such line lifts to a procyclic subgroup with open normalizer image, or construct one). (3) Prove that the loop structure is the only one on `π` invariant under an open subgroup of `Γ` with the cyclotomic compatibility (c) of §11 (scan 84). (4) Over finite extensions of `Q_p`, where a Tate curve puts `Z_ℓ(1)` inside a Tate module so that the proof of (1) is not available, prove what replaces it (Mochizuki 2004, Lemma 1.3.9, recovers the cusps by Frobenius weights) or give a counterexample to (1). Prove the full faithfulness of scan 484 for dominant morphisms from Theorem A. His statement of scan 485, that the commutant of the Galois image in `Autext_lac(π̂_{0,3})` is `S_3`, is Tamagawa 1997, Remark (7.3)(i): derive it in his form, then prove or refute the same for the pro-`ℓ` completions (known for odd `ℓ`: Nakamura 1994, Theorem A; decide `ℓ = 2`) and for the maximal `m`-step solvable quotients, with the smallest `m` for which the commutant is `S_3`.

### LM6, Part B (a): rewritten

Reason and source: Proposals (ii) 4 and 5 of LIT_LM6_sections.md, accepted: the abelianized form of 2:sc79 fails in genus 0 (its Part 2 item 2: computed by fork B1, hence asked as "refute", to be confirmed by the run); recognition of tangential sections is the point Stix lists as missing.

Old wording:

> (a) Cuspidal sections. Carry out §9 completely: the construction of scans 75–77 (a uniformizer `t` gives a section of `Gal(L̄/L) → Gal(k̄/k)`; `t` and `tu`, `u ∈ 1 + m`, give the same class), the torsor of classes of sections under `H¹(k, T(G_m))`, the `Θ(k*)`-subtorsor of tangential sections indexed by `(m/m²)*`. Prove his assertion of scan 79 that the classes obtained at distinct points of `S` are distinct from each other and from those of rational points of `X ∖ S`, already in the extension by `π_ab` (he omits the verification). Do what he postpones on scan 78: the behaviour of the tangential subtorsor under a morphism (with ramification index `d`) and its relation to the norm of 1-forms.

New wording:

> (a) Cuspidal sections. Carry out §9 completely: the construction of scans 75–77 (a uniformizer `t` gives a section of `Gal(L̄/L) → Gal(k̄/k)`; `t` and `tu`, `u ∈ 1 + m`, give the same class), the torsor of classes of sections under `H¹(k, T(G_m))`, the `Θ(k*)`-subtorsor of tangential sections indexed by `(m/m²)*`; prove that his construction is the tangential base point of Deligne (§15.13–15.26) and that his torsor is the packet of the letter of 1983 (Stix, Proposition 8; Esnault–Hai, Theorem 6.5). His assertion of scan 79, that the classes obtained at distinct points of `S` are distinct from each other and from those of rational points of `X ∖ S` already in the extension by `π_ab`, is true in the full group (Stix, Theorem 14) and is to be decided in the extension by `π_ab`: prove it for `g ≥ 1`, refute it for `g = 0` (on `P¹ ∖ {0,1,∞}` the tangential classes at `0` towards `1` and at `1` towards `0` coincide there), and compute for every `(g, ν)` the fibres of the map from points and packets to classes of splittings of the extension by `π_ab`. Do what he postpones on scan 78: the behaviour of the tangential subtorsor under a morphism (with ramification index `d`) and its relation to the norm of 1-forms. Then prove what the literature leaves open (Stix lists it as missing): a group-theoretic characterization of the `K*`-subtorsor of tangential sections inside the packet, and of its closure (which members of a packet are limits of sections of points `x → y`).

### LM6, Part B (b): rewritten

Reason and source: Proposal (ii) 6 of LIT_LM6_sections.md, accepted: his reason for injectivity is false when the torus is non-trivial; his excluded case is g = 0 with at most one hole, not two (v1 had "nu = 2").

Old wording:

> (b) Injectivity (scan 64) in his generality: for `U` embedded in an extension of an abelian variety by a torus, over `K` of finite type over `Q`, prove that a rational point is determined by the class of its splitting in the extension by `π_ab`; treat the case `g = 0`, `ν = 2` he excludes, and say what fails there.

New wording:

> (b) Injectivity (scan 64) in his generality: for `U` embedded in an extension `G` of an abelian variety by a torus, over `K` of finite type over `Q`, prove that a rational point is determined by the class of its splitting in the extension by `π_ab`. He derives it from "`G(K)` de type fini" (also in the letter of 1983), which is false as soon as the torus is non-trivial: give the proof from the true input, that `G(K)` has no non-trivial divisible element (Esnault–Hai, Proposition 5.3; Stix, Theorem 45), and prove that property for semi-abelian `G` over `K` finitely generated over `Q`. He excludes `g = 0` with `ν ≤ 1` (the projective and the affine line; `G_m` is included): prove what fails there, and give the fields over which injectivity fails for hyperbolic curves (`R`; a `p`-adically closed field that is not sub-`p`-adic), with an explicit pair of points for each.

### LM6, Part B (c): rewritten

Reason and source: Proposals (ii) 7 and 8 of LIT_LM6_sections.md, accepted (the "transcendental" sections have a definite answer; the condition that excludes cusps is the fixed group of Ker chi, his 1983 PS); NOTES.md R15 (scan 413, seen in reading2, asked by no v1 Part).

Old wording:

> (c) His corrected conjecture of scan 79 and the "conjecture provisoire profinie" of scans 431–433 with its axioms ① to ⑥ (scans 412–421) and (a)–(d): state each exactly, then prove the implications among them and with the section conjecture in its standard forms (for the proper curve; for the affine curve with cuspidal sections; birational). In particular prove: his ⑤ (scan 418: a), b), c)) for a hole `i` fixed by `Γ` is equivalent to the section conjecture for the affine curve given the one for the curve with the hole plugged, together with (a); his ⑥ (scans 420–421) follows from `L^{Γ'} = 1`, which you prove or refute for the kernel `L` he names; his injectivity claim (25) of scans 409–410 ("Je dis que cette application est injective") holds unconditionally. For the "transcendental" sections of scan 78–79 (classes in the `H¹(K, T(G_m))`-torsor outside the `K*`-subtorsor): decide whether they are admissible in his sense (they normalize a loop subgroup), so that his final formulation "no other splittings than those" (scan 79) and the 1983 form agree, and say exactly how the two differ.

New wording:

> (c) His corrected conjecture of scan 79 and the "conjecture provisoire profinie" of scans 431–433 with its axioms ① to ⑥ (scans 412–421) and (a)–(d): state each exactly, then prove the implications among them and with the section conjecture in its standard forms (for the proper curve; for the affine curve with cuspidal sections; birational). In particular prove: his ⑤ (scan 418: a), b), c)) for a hole `i` fixed by `Γ` is equivalent to the section conjecture for the affine curve given the one for the curve with the hole plugged (the neighbourhood argument of tool (T1), written in his terms), together with (a); his ⑥ (scans 420–421) follows from `L^{Γ'} = 1`, which you prove or refute for the kernel `L` he names; his injectivity claim (25) of scans 409–410 ("Je dis que cette application est injective") holds unconditionally. Then determine which of ①–⑥ are theorems for `Γ = G_k`, `k` a finite extension of `Q_p` (granted tool (1)), and over a number field for the curves with `C(A_K)_•^{f-cov} = C(K)`, each with its proof. The "transcendental" sections of scans 78–79: prove that every member of a packet has its image in the normalizer of a loop subgroup (Stix, Corollary 12), so that none is admissible in his sense and his formulation of scan 79 is that of the letter of 1983, which also takes the whole packet. His condition `π^{Γ'} = 1` (scan 431 (a)) does not separate points from cusps: prove (i) `π^{Γ'} = 1` for every section of a point and for every cuspidal section, `Γ'` open; (ii) the kernel of `χ` centralizes the loop subgroup of a cuspidal section; (iii) prove or refute his stronger guess "peut-être même `π^{Γ⁺} = 1`" (scan 433; the PS of the letter of 1983): for the section of a point, the fixed group of `Ker χ` in `π` is trivial (a start to check: for proper `X`, by the finiteness of the torsion of abelian varieties over the cyclotomic field, the fixed group maps to zero in the abelianization of every open subgroup containing it and the image of the section; what remains is to exclude a non-trivial perfect closed subgroup). Prove his remark of scan 413, that an effective action can lift an admissible exterior action without being admissible ("relèvements pathologiques"): construct such a lift (a cuspidal section is the candidate) and classify all lifts of a given admissible exterior action.

### LM6, Part B (d): rewritten

Reason and source: Proposal (ii) 9 of LIT_LM6_sections.md, accepted: v1 said "Theta is no longer injective", which is false over finite extensions of Q_p; the dichotomy is tool (T1), so the weight moves to the subtorsor, genus 0 and 1, the axioms, and finitely generated extensions of Q_p.

Old wording:

> (d) The `p`-adic counterpart, using the 2026 theorem for proper curves: for `k/Q_p` finite and `U = X ∖ S` hyperbolic with `S ≠ ∅`, determine the set of conjugacy classes of sections of `π_1(U) → G_k`: prove that every section is either cuspidal or comes from a `k`-point of `U`, or find the obstruction; describe the cuspidal packets at each `s ∈ S(k)` as he does over `K` (now `H¹(k, Ẑ(1))` is the profinite completion of `k*`, and `Θ` is no longer injective: say what replaces his subtorsor). Then decide which of his axioms ①–⑥ hold for `Γ = G_k`, in particular `π^{Γ'} = 1` for open `Γ' ⊂ Γ` acting through a section (his ③), for proper and affine curves.

New wording:

> (d) The `p`-adic counterpart. For `k/Q_p` finite and `U = X ∖ S` hyperbolic, tool (T1) gives the set of classes of sections: derive it with every step written, including the cases where `X` has genus 0 or 1. Here `Θ: k^× → H¹(k, Ẑ(1))` is injective with cokernel `Ẑ/Z` (over `R` it is not injective): describe the packet at `s ∈ S(k)`, its tangential subtorsor and the closure of the latter, with proofs. Compute the section sets of complete curves of genus 0 and 1 over `k` (for an elliptic curve the cokernel of `E(k) → H¹(k, T E)` is the Tate module of `H¹(k, E)`) and determine which classes are limits of points. Then decide which of his axioms ①–⑥ hold for `Γ = G_k`, in particular `π^{Γ'} = 1` for open `Γ' ⊂ Γ` acting through a section (his ③), for proper and affine curves; and attack the first case where nothing is claimed: `k` a finitely generated extension of `Q_p` of positive transcendence degree (prove the dichotomy "point or cuspidal" there, or isolate the step of the 2026 proof that fails).

### LM6, Part B (e): rewritten

Reason and source: Proposal (ii) 10 of LIT_LM6_sections.md, accepted; arXiv:2608.21232 and arXiv:2610.24986 (abstracts and main theorems seen by this fork and the main agent) claim the relative Hom-form and the sections of the universal curve: his margin on scan 432 becomes "derive and go beyond".

Old wording:

> (e) The relative version (scans 433–436). He withdraws surjectivity because two sections of a family `U → S` can meet. Formulate the corrected statement for `Γ = π_1(S)`, `S` a smooth curve over a number field (sections of `π_1(U) → π_1(S)` against sections of `U → S`, with his "strictement distinctes"), prove what the Hom-form gives (sections of `U → S` are among the `π_1(S)`-sections; which group-theoretic sections come from morphisms `S → U`), and prove or refute the surjectivity statement for the constant family `U_0 × S → S`.

New wording:

> (e) The relative version (scans 433–436). He withdraws surjectivity because two sections of a family `U → S` can meet. Formulate the corrected statement for `Γ = π_1(S)`, `S` a smooth curve over a number field (sections of `π_1(U) → π_1(S)` against sections of `U → S`, with his "strictement distinctes"), and prove what the theorems give: from the Hom-form and its version in families (Holzschuh–Schmidt–Stix, arXiv:2608.21232: dominant `S`-morphisms into a family of hyperbolic curves; unrefereed), which group-theoretic sections come from morphisms `S → U` (a section is not a dominant morphism, so this needs an argument: give it); from Mochizuki–Tsujimura, Theorem F (ii), the functoriality of geometricity along dominant morphisms of hyperbolic curves. Prove or refute the surjectivity statement for the constant family `U_0 × S → S`. For the universal family, Luo–Watanabe (arXiv:2610.24986, unrefereed) claim that for `g ≥ 3`, `n ≥ 1` the sections of `π_1` of the universal complete curve over `M_{g,n}` are the `n` tautological ones: derive from it his margin of scan 432 (the family `𝒰_{g,ν} → M_{g,ν}` has no admissible sections, the tautological ones being cuspidal for `𝒰_{g,ν}`), stating the step of that paper you rely on, and go beyond it: the sections over open subgroups of `π_1(M_{g,n})` (his "multisections étales"), and the cases `g ≤ 2` and `n = 0`.

### LM6, Part B (f): rewritten

Reason and source: Proposal (ii) 11 of LIT_LM6_sections.md and (ii) 7 of LIT_LM6_anabelian.md, accepted (Theta injective for all types: Hoshi-Mochizuki 2011 Cor. 6.4, read by fork B2; (6) is a congruence-kernel statement); NOTES.md R15 (scan 480, seen in reading2); arXiv:2611.09080, 2602.17746, 2605.02577 as unrefereed claims.

Old wording:

> (f) Scans 487–488: his direct criteria for admissibility (for `g ≥ 1`: after plugging all holes, the points defined by the holes are distinct; for `g = 0`, `ν > 3`: the same after plugging all but three) and the interpretation of admissible germs of splittings of `1 → 𝒯̂_{g,ν} → N_{g,ν} → Γ_{g,ν} → 1` as algebraic points of `M_{g,ν}`. Prove that the criteria are necessary; decide whether they are sufficient for `(0,4)` (where `M_{0,4} = P¹ ∖ {0,1,∞}` and the question is the section conjecture for it, cuspidal sections removed) by reducing to an exact statement; state and prove the precise relation between sections of `π_1(M_{g,ν}) → G_K` and curves of type `(g,ν)` over `K` that the Isom-form gives.

New wording:

> (f) Scans 480 and 487–488: his direct criteria for admissibility (lifts that normalize no loop subgroup, or with `π̂_{0,3}^{Γ''⁺} = 1`; for `g ≥ 1`: after plugging all holes, the points defined by the holes are distinct; for `g = 0`, `ν > 3`: the same after plugging all but three) and the interpretation of admissible germs of splittings of `1 → 𝒯̂_{g,ν} → N_{g,ν} → Γ_{g,ν} → 1` as algebraic points of `M_{g,ν}`. Here `Γ_{g,ν} = Γ_Q`: the maps `Θ_{g,ν}` are injective for all types (Hoshi–Mochizuki 2011, Corollary 6.4), so (f) of scan 396 holds in that form, and what remains of his isomorphism (6) is a statement about congruence kernels, known for `g ≤ 2`. Prove that the criteria are necessary; decide whether they are sufficient for `(0,4)` (where `M_{0,4} = P¹ ∖ {0,1,∞}`; the local statement is tool (T1), so the question is the global one: reduce it to an exact statement); state and prove the precise relation between sections of `π_1(M_{g,ν}) → G_K` and curves of type `(g,ν)` over `K` that the Isom-form gives, with the cuspidal sections of `M_{g,ν}` relative to its boundary defined (Carlson–Corwin, arXiv:2611.09080, Theorem A, unrefereed) and proved to be non-admissible in his sense. For the stacks among them (`M_{1,1}`; the quotient of `P¹ ∖ {0,1,∞}` by `S_3` of §§36–37) Steklov's Theorems B and C (arXiv:2602.17746) and Collas–Philip–Yamaguchi (arXiv:2605.02577) claim the reduction of the section conjecture to curves and the Isom-form: derive the statement for `M_{1,1}` over a number field and over `Q_p`, checking the steps used. Finally his remark of scan 480 ("il est concevable qu'il faille y apporter des conditions plus subtiles, faisant intervenir les Frobenius"): decide it over finite extensions of `Q_p` and over number fields, by proving that the condition "normalizes no loop subgroup" characterizes the sections of points among all sections (given the section conjecture), or by producing the Frobenius condition that is needed; and construct the description of admissible exterior actions that does not pass through effective ones, which he asks for on the same scan.

### LM6, Part C: Part rewritten

Reason and source: Proposals (ii) 12 and 13 of LIT_LM6_sections.md, accepted: v1 C (a) asked to prove a false statement (over R all classes come from components; a real packet has two elements; Mochizuki 2003 Cor. 3.13, Bresciani-Vistoli, read by fork B1); "six packets" corrected to three. NOTES.md R17 resolved (Lead 3 gets its rows without redoing LM4). (d) added from Mochizuki 2003 Cor. 3.8, 3.15 and arXiv:2510.13325 (Theorems A, B seen in the PDF text).

Old wording:

> **C. Real structures (scans 139, 148, 437–448; with scan 377–378).**
> The topological classification of anti-involutions and the groups `H ≅ Z^g` are treated in LM4_FINITE_GROUP_ACTIONS, Part B (e); do not redo them here. Here: (a) prove the profinite real section statement in his form: for a smooth curve `U` over `R` (affine or proper, hyperbolic), `π_0(U(R)) →` conjugacy classes of sections of `π_1(U) → Gal(C/R)` that are not cuspidal is bijective, with the cuspidal packets at the real points at infinity described (his margin of scan 437: recover "la disposition des points à l'infini sur les composantes connexes de `X^σ`" from the group theory: prove exactly what is recovered: which cusps are real, on which component each lies, and their cyclic order on it); compute the fixed groups `π̂^{σ_i}` (his (7) and (14) of scans 441–445 give `1` for a line and `Z` for an oval in the discrete case: prove the profinite values). (b) Prove (29)–(30) of scans 377–378 as far as they are unconditional: the map from prediscretizations to elements of order 2 of `Γ_a`, and its bijectivity onto the conjugates of complex conjugation in the image of `Γ_Q`; state precisely what the conjectural identification of `Γ_a` adds. (c) For a number field `K` with a real place and a curve over `K`: prove that the real sections at that place and the `K`-sections are compatible in the sense his §29 suggests (a `K`-section restricted to the decomposition group at the real place is a real section), and compute, for `P¹ ∖ {0,1,∞}` over `Q`, the six real cuspidal packets and the three components of `U(R)` in terms of explicit elements of `π̂_{0,3}`.

New wording:

> **C. Real structures (scans 139, 148, 437–448; with scans 377–378).**
> Lead 3 has three clauses. The classification of anti-involutions and the statement on maximal free abelian subgroups are proved in LM4_FINITE_GROUP_ACTIONS, Part B (e): give each here one numbered statement with its proof in a few lines from the named theorems (Gross–Harris, Ann. Sci. ENS 14 (1981), Proposition 3.1; Birman–Lubotzky–McCarthy, Duke Math. J. 50 (1983)), so that the lead has its row, and spend the Part on the middle clause.
> (a) Over `R` every class of sections comes from a component: for every hyperbolic curve `U` over `R`, affine or proper, `π_0(U(R)) →` classes of sections of `π_1(U) → Gal(C/R)` is bijective (Mochizuki 2003, Corollary 3.13; Bresciani–Vistoli), and his theorem of scans 440–445 is the discrete form with centralizers (Mochizuki 2003, Theorem 3.6, Corollary 3.7). Derive both in his language. The packet at a real cusp has two elements, the classes of the two adjacent components (`H¹(R, Ẑ(1)) = Z/2`): prove it, and prove exactly what the classes recover of the position of the points at infinity (his margin of scan 437): which cusps are real, on which component of `X(R)` each lies, and their cyclic order on it up to reversal. Prove the profinite fixed groups `π̂^{σ_i}` (his (7) and (14) of scans 441–445 give `1` for a line and `Z` for an oval in the discrete case; expected `1` and `Ẑ`), which the literature named here states only for moduli in genus ≤ 2.
> (b) Prove (29)–(30) of scans 377–378 as far as they are unconditional: the map from prediscretizations to elements of order 2 of `Γ_a`, and its bijectivity onto the conjugates of complex conjugation in the image of `Γ_Q`; then prove what the identification `Γ_a = Γ_Q` (injectivity of `Θ_{g,ν}`: Hoshi–Mochizuki 2011, Corollary 6.4) adds: the bijection of `P_a/±1` with the archimedean places of `Q̄`.
> (c) For a number field `K` with a real place and a curve over `K`: prove that the real sections at that place and the `K`-sections are compatible in the sense his §29 suggests (a `K`-section restricted to the decomposition group at the real place is a real section), and compute, for `P¹ ∖ {0,1,∞}` over `Q`, the three components of `U(R)`, the three classes of involutions and the three real packets of two classes each, with the six identifications of tangential classes with components (the class at `0` towards `1` and the class at `1` towards `0` are both the class of the interval `(0,1)`), in terms of explicit elements of `π̂_{0,3}`.
> (d) The moduli stacks. `π_0(M_{g,ν}(R))` corresponds to the classes of involutions over complex conjugation in the extended mapping class group, with centralizers (Mochizuki 2003, Corollary 3.8; profinite, for `g ≤ 2`: Corollary 3.15; in étale homotopy theory: Holzschuh, arXiv:2510.13325, Theorems A and B, unrefereed). Derive from it his counts of scans 445–448 as the number of components of `M_{g,ν}(R)`, and prove the profinite statement with centralizers for `g ≥ 3`, or reduce it to an exact statement about the mapping class group (goodness) with the smallest undecided case.

### LM6, Part C done sentence: changed

Reason and source: Follows the new ask (d) and the Lead 3 rows.

Old wording:

> Done for Part C: (a)–(c) are theorems with proofs; the computation in (c) is explicit.

New wording:

> Done for Part C: (a)–(d) are theorems with proofs; the computation in (c) is explicit; the two statements for Lead 3 are given.

### LM6, Part D (a): rewritten

Reason and source: Proposal (ii) 14 of LIT_LM6_sections.md, accepted: the equivalence with the finite-descent equality is tool (T2); the abelianized set is not finite in general, so "decide whether it is finite" became "compute it".

Old wording:

> (a) State his finiteness statement exactly: for `g ≥ 2` and `K` a number field, the set of `π`-conjugacy classes of splittings of `E → Γ` is finite. Prove the exact logical relations between: this statement; the section conjecture; Faltings's theorem; finiteness of the set of sections of the extension by `π_ab` modulo the Mordell–Weil group (compute this last set: it is a torsor-like object under `H¹(K, T(J))`; decide whether it is finite).

New wording:

> (a) State his finiteness statement exactly: for `g ≥ 2` and `K` a number field, the set of `π`-conjugacy classes of splittings of `E → Γ` is finite. Prove the exact logical relations between: this statement; the section conjecture; Faltings's theorem; the equality `C(A_K)_•^{f-cov} = C(K)` (equivalent to the section conjecture by tool (T2); compare Stoll's Remark 8.9); and the set of classes of splittings of the extension by `π_ab`, a torsor under `H¹(K, T J)`, which contains the completion of `J(K)` with quotient the Tate module of `H¹(K, J)`: compute it and its Selmer part, and prove that it is infinite in general.

### LM6, Part D (b): rewritten

Reason and source: Proposal (ii) 15 of LIT_LM6_sections.md, accepted: the statement is Cor. 8.5 of the paper, the four links were compared with their sources by fork B1; the ask now goes beyond the modular curves.

Old wording:

> (b) Prove the finiteness of his set of classes for the curves where the section conjecture is now claimed (`X_0(N)`, `X_1(N)` of genus ≥ 2 over `Q`), stating which step of the 2026 paper is used.

New wording:

> (b) The finiteness of his set of classes for `X_0(N)`, `X_1(N)` of genus ≥ 2 over `Q` is Corollary 8.5 of the 2026 paper: check the chain it rests on (its Theorem 1.1; Harari–Stix, Theorem 2.1; Stix, arXiv:1203.3236, Corollary 5; Stoll, Corollary 8.8) and write the proof in his terms; then prove the same for every curve to which Stoll's criterion applies that you can exhibit (a non-constant map to an abelian variety with finite Mordell–Weil group and trivial divisible part of the Tate–Shafarevich group), with a list of explicit curves of genus 2 and 3.

### LM6, Part D (c): rewritten

Reason and source: Proposal (ii) 16 of LIT_LM6_sections.md, accepted: v1 D (c) asked for what is Prop. 8.1 of the paper; the ask now starts beyond it. arXiv:2604.26131 (Theorems 1.3, 1.7 seen in the PDF text) added for the quotient question.

Old wording:

> (c) For a general curve of genus ≥ 2 over a number field prove the strongest finiteness you can for sections: finiteness of Selmer sections with prescribed local behaviour, finiteness modulo a fixed nilpotent or metabelian quotient, or the exact statement that would be needed; with the 2026 local theorem, prove that every section is locally geometric at every finite place and derive what this gives globally (the finite-descent set), with the smallest example where the global conclusion is not known.

New wording:

> (c) For a general curve of genus ≥ 2 over a number field: that every section is locally geometric and that the image of the localization map is the finite-descent set is Proposition 8.1 of the 2026 paper. Go beyond it: prove the finiteness of `loc_v(Sec(C/K))` for `K` without CM subfield (Betts–Stix with Theorem 1.1) and the rigidity of sections under reduction (Porowski, arXiv:2509.15660 and arXiv:2607.27746, Theorem 1.5, unrefereed), checking the steps used; then prove or refute the finiteness of `Sec(C/K)` itself, naming the missing statement exactly (finite fibres of `loc_v` at one place) with the smallest curve for which it is not known. For quotients of `π_1`: non-geometric sections exist for the geometrically pro-`p` and the geometrically metabelian quotients over `p`-adic fields (tool (3)), while birational statements hold for very small quotients (Pop, arXiv:2604.26131, Theorems 1.3 and 1.7, unrefereed): determine, with proofs, the smallest quotient of `π_1(C)` for which every section over a number field is locally geometric at every place.

### LM6, Part E: new Part

Reason and source: NOTES.md R19: the base Part E had no letters, no done sentence and a status-shaped last clause. (a) and (b) are the base text, lettered, with producing verbs; its passages in cote 140-4 were NOT re-read by this line (RECORD.md: Part E is to be redone after sections 50-52 are read). (c) is proposal (ii) 17 of LIT_LM6_sections.md (Steklov Thm A with the 2026 theorem).

Old wording:

> (in the base prompt, in the tail frame, unlettered)

New wording:

> **E. Fermat (item 4; scan 65 of cote 140-2 and §51.16).**
> (a) Write his proposal exactly: the extensions (371), (372), (373), the groups involved, what "scindages provenant des points à l'infini" are, with every definition he uses, and prove each assertion he makes about them, or refute it.
> (b) Carry it out as far as it goes: compute the sections of the metabelian (his first Lie) approximation for the Fermat curves `U_n` and decide whether that level can exclude non-cuspidal sections (non-geometric sections of metabelian quotients exist over `p`-adic fields: tool (3)); determine the first nilpotent level at which an obstruction to a rational point on the affine Fermat curve appears, for small `n` by explicit computation (with code), and in general as far as it can be proved; prove how this compares with Kim's method for the same curves.
> (c) The section-conjecture form of Fermat's theorem. Steklov (arXiv:2602.17746, Theorem A, unrefereed) claims that all Selmer sections over `Q` of the affine Fermat curve `V_ℓ` are cuspidal for `ℓ ≥ 7`; with tool (T1) and the real case every section of `π_1(V_ℓ) → G_Q` would be Selmer, hence cuspidal: prove this chain, checking in particular that "Selmer" in Steklov's sense is what tool (1) delivers at every place, `2` and `ℓ` included; then treat `ℓ = 5` and `ℓ = 3`, where his method stops, and prove the exact statement that a proof of Fermat's theorem along Grothendieck's lines (through the extension of scan 65) still requires.

### LM6, Part E done sentence: changed

Reason and source: New: the base Part E had none.

Old wording:

> Done for Part E: .

New wording:

> Done for Part E: (a) is an exact statement of his proposal with its assertions proved; (b) and (c) are theorems, computations with code, or exact obstructions with the smallest undecided exponent.

## 3. Push check of every lettered ask of the v2 files (generated)

Per ask: the producing verbs found in it (from: prove, refute, decide, construct, compute, classify, derive, determine, settle, carry out, write out, write, define, formulate, exhibit, state, check, extend, identify, attack), flagged words (briefly, a table of, status, survey, cite or prove, say what remains, need not, at most a), words. A Part passes if every ask has at least one of prove / refute / decide / construct / compute / classify / derive / determine / settle and the Part has its "Done for Part X" line.

**LM4_PARTS_redo_20261112_v2.md** (5086 words, comment header excluded)

| Part | Ask | Producing verbs | Flagged | Words |
|---|---|---|---|---|
| A | (a) | prove, write, state |  | 160 |
| A | (b) | prove, refute, determine |  | 191 |
| A | (c) | prove, refute, decide, derive, check |  | 313 |
| A | (d) | prove, decide, determine |  | 83 |
| B | (a) | prove, derive, state |  | 208 |
| B | (b) | prove, derive |  | 205 |
| B | (c) | prove, refute, settle, write out, write, state |  | 218 |
| B | (d) | prove, refute, decide, compute, derive, define |  | 241 |
| B | (e) | prove, decide, construct, compute, classify, derive |  | 380 |
| B | (f) | compute, check |  | 68 |
| C | (a) | prove, decide, write, define, state, identify |  | 183 |
| C | (b) | prove, state, check |  | 354 |
| C | (c) | prove, refute, write |  | 92 |
| C | (d) | prove, derive, carry out |  | 252 |
| C | (e) | prove, compute, identify |  | 62 |
| D | (a) | prove, decide, compute |  | 277 |
| D | (b) | prove, decide, construct, derive, settle, state |  | 282 |
| D | (c) | prove, refute, construct |  | 68 |
| D | (d) | prove, state, check |  | 110 |
| E | (a) | prove, construct |  | 70 |
| E | (b) | prove, refute, decide, determine, settle, write |  | 339 |
| F | (a) | prove, determine |  | 31 |
| F | (b) | prove, refute, derive |  | 95 |
| F | (c) | prove |  | 36 |

Done sentences present for Parts: A, B, C, D, E, F. Parts with asks and no done sentence: none. Asks without a strong verb: none.

**LM5_PARTS_redo_20261112_v2.md** (1938 words, comment header excluded)

| Part | Ask | Producing verbs | Flagged | Words |
|---|---|---|---|---|
| A | (a) | prove, decide |  | 124 |
| A | (b) | prove, write out, write |  | 52 |
| A | (c) | prove, decide, construct, define, state |  | 108 |
| A | (d) | prove, construct, determine |  | 62 |
| A | (e) | prove, write, define |  | 58 |
| A | (f) | prove, identify |  | 92 |
| B | (a) | prove, decide, construct, define |  | 105 |
| B | (b) | prove, decide |  | 150 |
| B | (c) | prove, construct, carry out |  | 103 |
| B | (d) | prove, construct |  | 62 |
| C | (a) | prove, decide |  | 106 |
| C | (b) | prove, refute |  | 35 |
| C | (c) | prove |  | 65 |
| C | (d) | construct |  | 72 |
| D | (a) | prove, decide, construct |  | 74 |
| D | (b) | prove, compute, classify |  | 107 |
| D | (c) | prove, decide, state |  | 52 |
| D | (d) | prove, define |  | 80 |
| E | (a) | construct |  | 35 |
| E | (b) | prove |  | 20 |
| E | (c) | decide |  | 43 |

Done sentences present for Parts: A, B, C, D, E. Parts with asks and no done sentence: none. Asks without a strong verb: none.

**LM6_PARTS_redo_20261112_v2.md** (4669 words, comment header excluded)

| Part | Ask | Producing verbs | Flagged | Words |
|---|---|---|---|---|
| A | (a) | prove, decide, construct |  | 141 |
| A | (b) | prove, decide, determine, write, check |  | 352 |
| A | (c) | prove, compute |  | 137 |
| A | (d) | prove, decide |  | 86 |
| A | (e) | prove, refute, decide, construct, classify, derive |  | 358 |
| B | (a) | prove, refute, compute, carry out |  | 259 |
| B | (b) | prove |  | 153 |
| B | (c) | prove, refute, construct, classify, determine, state |  | 404 |
| B | (d) | prove, decide, compute, derive, determine, attack |  | 185 |
| B | (e) | prove, refute, derive, formulate |  | 218 |
| B | (f) | prove, decide, construct, derive, state |  | 340 |
| B | (g) | prove, construct, compute, determine |  | 75 |
| C | (a) | prove, derive |  | 166 |
| C | (b) | prove |  | 63 |
| C | (c) | prove, compute |  | 113 |
| C | (d) | prove, derive |  | 88 |
| D | (a) | prove, compute, state |  | 104 |
| D | (b) | prove, write, exhibit, check |  | 96 |
| D | (c) | prove, refute, determine |  | 162 |
| E | (a) | prove, refute, write |  | 37 |
| E | (b) | prove, decide, compute, determine |  | 92 |
| E | (c) | prove |  | 107 |

Done sentences present for Parts: A, B, C, D, E. Parts with asks and no done sentence: none. Asks without a strong verb: none.

