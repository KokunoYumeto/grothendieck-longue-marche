# finish_20261111.py -- work file (Claude, Fable 5.2; 11 Nov 2026). Assembles LM3b_TEICHMULLER_PUSH/PROMPT.md,
# writes its BACKGROUND.md, appends the attachment lists to the BACKGROUND.md of LM4-LM8, and adds a section to the stack README.
import io, os, re, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
STACK = os.path.join(HERE, "..", "pro_prompts_draft_20261111")
rd = lambda p: io.open(p, encoding="utf-8").read()
def wr(p, s): io.open(p, "w", encoding="utf-8", newline="\n").write(s)

# ---- LM3b prompt
d = os.path.join(HERE, "LM3b_TEICHMULLER_PUSH")
head = rd(os.path.join(d, "PROMPT_head.md")).rstrip() + "\n"
common = rd(os.path.join(STACK, "_COMMON_BLOCK.md"))
wr(os.path.join(d, "PROMPT.md"), head + "\n---\n\n" + common)
parts = head[head.index("\n## Parts\n"):]
VERBS = r"\b(prove|proves|proved|refute|decide|construct|compute|classify|determine|derive|exhibit|enumerate|tabulate|attack|carry out|write a program|by program|find)\b"
w = len(re.findall(r"\S+", parts)); v = len(re.findall(VERBS, parts, flags=re.I))

RET = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_returns_20261111\LM3_TEICHMULLER_TOWER"
REV = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_reviews_20261111\LM3_TEICHMULLER_TOWER"
BIS = r"C:\Users\user\Documents\derivateurs_companion_20261109\pro_returns_20261110\7_BISITE"
BISR = r"C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\7_BISITE"

wr(os.path.join(d, "BACKGROUND.md"), f"""# LM3b_TEICHMULLER_PUSH: background to put in the zip (draft list; no zip built)

Written by Claude (Fable 5.2), 11 November 2026. Root and the rule for the current text of a package: as in `LM4_FINITE_GROUP_ACTIONS\\BACKGROUND.md`. "(m)" = from memory: resolve by exact title first.

## Start from the LM3 package
Everything in `pro_prompts_draft_20261111\\LM3_TEICHMULLER_TOWER\\LM3_TEICHMULLER_TOWER_background.zip` (manuscript packages for cote 140-2 scans 201–550 with their scans and notes, the table of contents, `OVERVIEW.md`, the papers, the three proof packs 008, 019, 031, the STRATA and GALOIS files), per its `MANIFEST.tsv` in `pro_prompts_draft_20261111_work\\LM3_TEICHMULLER_TOWER\\`. Add the prompt LM3 answered as `LM3_prompt/PROMPT.md`.

## The LM3 answer and its review
- `{RET}\\LM3_TEICHMULLER_TOWER_paper.pdf`, `_paper.tex`, `sections\\*.tex`, `_results.csv`, `_readings.csv`, `_report.md`, `_references.bib` -> `LM3_return/`. Nothing from its `code\\` or `audit\\` folders.
- `{REV}\\REVIEW_author.md`, `checks_author\\check_lm3.py`, `checks_author\\check_lm3.out` -> `LM3_review/` (the reviewer's own program; the prompt tells the model to recompute and not to rely on it).

## Papers to add (not in the LM3 zip, or to check there)
- M. Boggi, *Congruence topologies on the mapping class group* (2020) and the 2026 papers LM3 cites as Boggi2026BC and Boggi2026Automorphisms (v6, 22 April 2026): take the exact titles and arXiv numbers from `LM3_return/LM3_TEICHMULLER_TOWER_references.bib`.
- M. Boggi, L. Funar, the 2023 paper on the profinite curve complex and automorphisms (bib key AF_BoggiFunar2023); M. Boggi, P. Zalesskii (2019; key BoggiZalesskii2019BC).
- A. Minamide, H. Nakamura, *The automorphism groups of the profinite braid groups* (2022).
- H. Nakamura, L. Schneps, *On a subgroup of the Grothendieck–Teichmüller group acting on the tower of profinite Teichmüller modular groups*, Invent. Math. 141 (2000); A. Hatcher, P. Lochak, L. Schneps, *On the Teichmüller tower of mapping class groups*, J. reine angew. Math. 521 (2000).
- F. Pop, the 2018 paper on the tripod and `G_Q` (key Pop2018Tripod); Y. Hoshi, S. Mochizuki, S. Tsujimura (2025; key HoshiMochizukiTsujimura2025).
- H. Nakamura, *Galois rigidity of pure sphere braid groups and profinite calculus* (1994; in the LM3 zip) and *Galois rigidity of the étale fundamental groups of punctured projective lines* (1990) (m).
- Y. Ihara, *Braids, Galois groups, and some arithmetic functions*, Proc. ICM 1990; *On the stable derivation algebra associated with some braid groups*, Israel J. Math. 80 (1992) (m): for Leads 1–4 (special derivations, their lifting, the stable derivation algebra).
- P. Lochak, L. Schneps, *A cohomological interpretation of the Grothendieck–Teichmüller group*, Invent. Math. 127 (1997) (m): torsion and complex conjugation in `GT̂`.
- V. Dolgushev and coauthors, the papers on GT-shadows (m): for Part F (b).
- T. Willwacher, arXiv:2610.15592 (reported by LM3 E.28; NOT opened by us: fetch, check that it exists and what it proves, before attaching).
- D. Kent, C. Leininger, S. Schleimer (in the LM3 zip via STRATA); R. Hain, M. Matsumoto, *Weighted completion of Galois groups and Galois actions on the fundamental group of P^1 − {{0,1,∞}}* (in the LM3 zip).

## Status
Draft. Not ready to send: the user has not seen it; the leads rest on one program and one reader. No zip.
""")

# ---- BACKGROUND.md of LM4-LM8: attachments for the two new sections
ATT = {
 "LM4_FINITE_GROUP_ACTIONS": ("sections `A.tex`, `B.tex`, `C.tex`, `D.tex` (D.14, D.15), `F.tex` (F.11)", "`sections/A.tex`, `B.tex`, `E.tex`, `F.tex`, `G.tex`"),
 "LM5_MULTI_GALOIS_TOPOI": ("sections `C.tex`, `F.tex`, `F_continuation.tex`", "`sections/B.tex`, `D.tex`, `E.tex`"),
 "LM6_POINTS_AS_SECTIONS": ("sections `C.tex`, `D.tex`, `E.tex`; with the proof pack `019_…` and, for Part A, `031_…` (from `recent_results_20261110\\proof_packs\\`)", "`sections/B.tex`; and PATHS `sections/E.tex` (from `pro_returns_20261110\\6_PATHS\\`)"),
 "LM7_FERMAT_TOWER": ("sections `A.tex`, `E.tex`; with the proof pack `008_…`", "`sections/B.tex`"),
 "LM8_LIE_APPROXIMATIONS": ("sections `A.tex`, `E.tex`, `F_continuation.tex`; with the proof packs `008_…` and `019_…`", "`sections/B.tex`"),
}
MARK = "## Added 11 November 2026: after LM3 and after BISITE (push rewrite)"
for name, (lm3s, biss) in ATT.items():
    p = os.path.join(HERE, name, "BACKGROUND.md"); s = rd(p)
    if MARK in s: s = s[:s.index(MARK)].rstrip() + "\n"
    s = s.rstrip() + f"""

{MARK}

The prompt now has the sections "After LM3" and "After BISITE and the seven Dérivateurs returns". When the zip is built, add:
- `LM3_return/`: from `{RET}\\`: `LM3_TEICHMULLER_TOWER_report.md`, `_results.csv`, `_paper.pdf`, and {lm3s}. Nothing from its `code\\` or `audit\\` folders.
- `LM3_review/`: `{REV}\\REVIEW_author.md` and `checks_author\\check_lm3.py`, `check_lm3.out`.
- `BISITE_return/`: from `{BIS}\\` (check the folder layout there): the report, the register of statements, and {biss}. Nothing from its code folder.
- `BISITE_review/`: `{BISR}\\REVIEW_author.md` and `COMBINED_REVIEW.md`.
- If `LM3b_TEICHMULLER_PUSH` has been answered and reviewed by then: its report, register and review, under `LM3b_return/`, `LM3b_review/`.
The previous prompt is `PROMPT_before_push_20261111.md` in this folder. No zip was built.
"""
    wr(p, s)

# ---- stack README
p = os.path.join(STACK, "README.md"); s = rd(p)
MARK2 = "## 11 November 2026: after the LM3 answer; the push rewrite of LM4–LM8; LM3b"
if MARK2 in s: s = s[:s.index(MARK2)].rstrip() + "\n"
rec = rd(os.path.join(HERE, "PUSH_REWRITE_RECORD_20261111.md"))
table = rec[rec.index("| Prompt | Parts words before"):rec.index("For comparison")].strip()
s = s.rstrip() + f"""

{MARK2}

`LM3_TEICHMULLER_TOWER` has been answered (GPT-6 Astra, ChatGPT Pro mode; 110 statements: 57 Proved, 30 Known, 11 Refuted, 12 Open) and reviewed by Claude (Fable 5.2): `..\\pro_reviews_20261111\\LM3_TEICHMULLER_TOWER\\REVIEW_author.md`, with `checks_author\\`. No statement labelled Proved, Known or Refuted was found false. Its main result: `𝕀Γ_{{g,ν}}` has two definitions (§26: normalizer of the geometric subgroup; §29: arithmetic image); for the second the "conjecture fondamentale" is a theorem (Hoshi–Mochizuki 2011, Corollary 6.4), for the first the group is `GT̂_0` at `(0,3)` and `GT̂` at `(0,n)`, `n ≥ 4`, and `(1,1)`. Leads 1 and 4 of the LM3 prompt and two sentences of `OVERVIEW.md` (§2 on the conjecture fondamentale, §3 on the faithfulness he doubted and on the centre of `Gal`) are corrected in the review; `OVERVIEW.md` itself is in the sent stack and was not edited.

The audit of 11 November (`..\\pro_prompts_draft_20261111_work\\PUSH_STANDARD_AND_AUDIT_20261111.md`) found that the task lists of the LM prompts asked for status more than for mathematics. The unsent prompts LM4–LM8 were rewritten to its push standard in the work tree (`..\\pro_prompts_draft_20261111_work\\<name>\\PROMPT.md`; before-copies `PROMPT_before_push_20261111.md`; record `PUSH_REWRITE_RECORD_20261111.md`; the texts are generated by `push_rewrite_20261111.py` and `followups_block.py` there):

{table}

Each got: a demand at the end of every item of "What is to be settled"; a section "After LM3"; a section "After BISITE and the seven Dérivateurs returns" with the follow-ups L1–L6 of `derivateurs_companion_20261109\\pro_reviews_20261110\\7_BISITE\\FOLLOW_UPS.md` (L1, L2 in LM5; L3, L6 in LM4; L4 in LM6; L5 in LM7 and LM8); and new Parts. The leads, the earlier "After …" sections and the common block are unchanged. The run-now-or-wait table is unchanged: all five still wait for their second passes, and no zip was built. Still not done for LM6–LM8: the fold of the recent-results brief (the list in the section "recent results" above); the "After LM3" sections of LM6, LM7, LM8 carry what LM3 established about the manuscripts 008, 019, 031, which covers part of it.

New draft: `LM3b_TEICHMULLER_PUSH` (work tree only; `PROMPT.md`, `BACKGROUND.md`; Parts: {w} words, {v} demanding verbs by the same count). It attacks the twelve Open rows of LM3 and derives his statements from the theorems LM3 cited without using. Its first three leads are results of the review (pro-ℓ analogues of LM3 B.7 and C.8, by a computation with special derivations): unverified by anyone else. It can run on the LM3 package (all second-passed) once the user has seen it.
"""
wr(p, s)
print("LM3b parts:", w, "words,", v, "verbs")
