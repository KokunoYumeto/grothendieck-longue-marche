# INTAKE_B_TOWERS: the Pro intake prompt for six Longue Marche runs (1,358 register rows)

Built 19 Nov 2026 by Claude Opus 5.5 at effort max (an agent of the main session), for GPT-6 Astra (ChatGPT Pro mode). Builder scripts: `pro_intake_20261119/_work/` (`select_20261119.py`, `build_20261119.py`, `write_prompts_20261119.py`, this README's `write_readmes_20261119.py`).

**To send:** drag in `PROMPT.md` and the four zips, with no text, in a new chat in Pro mode. Lint: `push_rule_pro_prompts.py --lint` passes. Privacy scan (e-mail addresses, keys and tokens, the user's names and account name) over every text member of every zip and over PROMPT.md: no hits.

## Files

| File | Bytes | Members | SHA-256 |
|---|---:|---:|---|
| `INTAKE_B_1_returns.zip` | 10,278,929 | 1874 | `873d001290f99f992ffab02ce705467ef8eab241922ad544b54ad0042c999b1f` |
| `INTAKE_B_2_evidence_code.zip` | 11,790,252 | 200 | `6c4623e5212f47ce572807a0b1c33a310949b1e58de0ef581764e1d4fe0ac2bb` |
| `INTAKE_B_3_earlier_intakes.zip` | 735,272 | 51 | `de5f2bcd3ac2b91e304b0541ab01e64b1fdac144dab1cba86a19fdeb969da111` |
| `INTAKE_B_4_prompts_as_sent.zip` | 124,266 | 8 | `d01abcd19376f1c7d05e6cc459096fbcc987f3bb351f754c6434b1a6dbf90daa` |
| `PROMPT.md` | 19,397 |  | `fd371914b4be6444d546d38390be8e03d9185b10c4280d75d6dd8b171c274835` |

## Rows per run

| Run | Return | Rows | Return files attached (MB) | Evidence files (MB) |
|---|---|---:|---:|---:|
| LM7_FERMAT_TOWER | return | 229 | 509 (5.7) | 149 (1.3) |
| LM7_PUSH | cp09 | 218 | 268 (4.5) | 0 (0.0) |
| FERMAT_SUCCESSOR | cp06 | 144 | 48 (1.0) | 8 (0.0) |
| LM8_PUSH | cp17 | 304 | 699 (8.6) | 36 (85.4) |
| EXIT_TOWER | cp28 | 283 | 184 (4.2) | 6 (0.0) |
| GT_TOWER_CHECK | cp10 | 180 | 165 (2.1) | 0 (0.0) |
| **all** | | **1,358** | | |

## Estimated length of the run

About 21 to 36 hours: 1,358 rows at 40 to 70 rows an hour, plus about two hours for the sections across the runs and the gap work. The rate is set from S6_09_PAPERS (GPT-6 Astra, ChatGPT Pro mode), which re-derived the proofs of 1,184 statements and typeset them in under 12 hours (its inputs were built on 16 Nov at 18:20 UTC, its final came on 17 Nov at 06:01 UTC), slowed down here for checking another run's proofs, rerunning computations with new code and searching the literature. A night run, or more than one; two Pro runs per account.

## What is attached and what is left out

- Zip 1, per run: the register, the report, the paper's TeX and its sections, the notes TeX and records, the check-event files and the bibliography, and GT_TOWER_CHECK's saved chat. Left out: code, data, builds, PDFs, page renders and QA images, history copies, manifests, vendored TeX runtimes, nested checkpoint zips.
- Zip 2: only the code and data files that a register row names as its evidence.
- Zip 3: every document our intake ledger attributes to these runs (intakes, expert notes, referee reports, debate notes, main-session notes, prompt-item files), plus the reviews and checks the ledger does not scan (found for this build), the per-row coverage tables, the companion outline with its open items, the placement table of 3,929 Longue Marche statements, the check ledger and the mathematics to-do of 17 Nov.
- Zip 4: the prompts as sent, with their provenance.
- Privacy: home-folder paths in our notes are rewritten to `C:\Users\<user>\`; each zip's MANIFEST.tsv lists every member so changed. No other change.

## Not found or not attached

- LM7_FERMAT_TOWER and LM7_PUSH: no copy of the prompt marked as sent exists. Zip 4 holds the prompt as it stood on 14 Nov 12:53 UTC (the snapshot taken before the checkpoint rule was added); the chats show the uploads as `PROMPT(20261112-233006).md` and `PROMPT(20261113-043658).md`.
- EXIT_TOWER checkpoint 28 is a chunked archive that only its own program restores; we did not run it. The attached state is `extracted_20261116/` (register, readings, report, paper and its 175 sections), with the bibliography from checkpoint 19, the newest earlier checkpoint that holds it (MANIFEST.tsv names it). The agents' drafts that only checkpoint 06 holds are left out as superseded. One input of the paper, `sections/request_register`, is in neither.
- LM8_PUSH: one evidence file is a certificate of 84.9 MB (`code/pbc_quotient86_standard2_literal_original_identity.json`, named by its register rows); it is in zip 2.
