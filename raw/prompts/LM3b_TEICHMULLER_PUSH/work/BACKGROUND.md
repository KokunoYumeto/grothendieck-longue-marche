# LM3b_TEICHMULLER_PUSH: background to put in the zip (draft list; no zip built)

Written by Claude (Fable 5.2), 11 November 2026. Root and the rule for the current text of a package: as in `LM4_FINITE_GROUP_ACTIONS\BACKGROUND.md`. "(m)" = from memory: resolve by exact title first.

## Start from the LM3 package
Everything in `pro_prompts_draft_20261111\LM3_TEICHMULLER_TOWER\LM3_TEICHMULLER_TOWER_background.zip` (manuscript packages for cote 140-2 scans 201–550 with their scans and notes, the table of contents, `OVERVIEW.md`, the papers, the three proof packs 008, 019, 031, the STRATA and GALOIS files), per its `MANIFEST.tsv` in `pro_prompts_draft_20261111_work\LM3_TEICHMULLER_TOWER\`. Add the prompt LM3 answered as `LM3_prompt/PROMPT.md`.

## The LM3 answer and its review
- `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_returns_20261111\LM3_TEICHMULLER_TOWER\LM3_TEICHMULLER_TOWER_paper.pdf`, `_paper.tex`, `sections\*.tex`, `_results.csv`, `_readings.csv`, `_report.md`, `_references.bib` -> `LM3_return/`. Nothing from its `code\` or `audit\` folders.
- `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_reviews_20261111\LM3_TEICHMULLER_TOWER\REVIEW_author.md`, `checks_author\check_lm3.py`, `checks_author\check_lm3.out` -> `LM3_review/` (the reviewer's own program; the prompt tells the model to recompute and not to rely on it).

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
- D. Kent, C. Leininger, S. Schleimer (in the LM3 zip via STRATA); R. Hain, M. Matsumoto, *Weighted completion of Galois groups and Galois actions on the fundamental group of P^1 − {0,1,∞}* (in the LM3 zip).

## Status
Draft. Not ready to send: the user has not seen it; the leads rest on one program and one reader. No zip.

## Packaged, 11 November 2026 (about 14:10 UTC)

Built by build_zip_20261111.py: upload folder pro_prompts_draft_20261111/LM3b_TEICHMULLER_PUSH/ holds PROMPT.md and LM3b_TEICHMULLER_PUSH_background.zip (297 files with MANIFEST.tsv, 92,771,874 bytes); MANIFEST.tsv is also here. This replaces the Status section above. Included beyond the LM3 zip: LM3_prompt/, LM3_return/ (paper, sections, registers, report, bib, README, SHA256SUMS; no code/, no audit/), LM3_review/, and eleven papers (_downloads/). NOT included: Boggi, A congruence subgroup property for symmetric mapping class groups (2026; Springer, not fetched); Ihara, On the stable derivation algebra (Israel J. Math. 1992; not free); Lochak-Schneps, A cohomological interpretation of GT (1997; not located); Nakamura 1990 (from memory, not resolved). Already in the LM3 zip: Nakamura-Schneps (papers/schneps_newGT), Hatcher-Lochak-Schneps (papers/schneps_HLS), Pop (papers/pop_IOM), Ihara ICM 1990, Nakamura 1994, Hain-Matsumoto. The downloaded papers were checked by first page only and were not read.
