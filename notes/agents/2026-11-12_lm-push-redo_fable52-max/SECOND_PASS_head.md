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

