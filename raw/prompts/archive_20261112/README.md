# Research prompts of the Montpellier archive programme, 12 November 2026

Research prompts for GPT-6 Astra (ChatGPT Pro mode) on Grothendieck's manuscript notes in the Montpellier archive
(cotes 142, 146, 147 and 149, with *La Longue Marche*), as packaged on 12 November 2026. All were written by Claude Fable 5.2
(effort max); the war game they draw on is in `../../planning/montpellier_archive/`.

Each folder holds the prompt (`PROMPT.md`) and the list of its background zip, not the zip itself: `ZIP_LIST.tsv` (or
`ZIP_LIST.md`) is the list of files the zip was built from, with the reason for each, and `ZIP_CONTENTS.tsv` lists every
member of the zip as packaged (name, bytes, CRC-32). The archive's scans and the papers by other authors that the zips
carry are not re-published here.

| Folder | Subject | State |
|---|---|---|
| `CYCLOTOMIC_KERNEL/` | The kernel of the cyclotomic character sees the cusps; centralizers of sections restricted to `Γ°` (cote 149, scans 44–66 and 126–127; *La Longue Marche* §§32–34; the PS of the letter to Faltings) | sent and returned (`../../pro_returns/CYCLOTOMIC_KERNEL/`, reviewed in `../../reviews_max_20261112/CYCLOTOMIC_REVIEW_OPUS/`) |
| `EXIT_ONE_TYPE/` | When the reconstruction by fundamental groupoids is exact: normal crossings pairs and their exit paths, the dependence on the compactification, minimal models, the boundary complex, the levels (cote 147, scans 106–190; cote 149) | sent 12 Nov, returned 13 Nov 2026 (`../../pro_returns/EXIT_ONE_TYPE/`; the three checkpoints taken during the run are in `../../pro_returns/EXIT_ONE_TYPE_checkpoints/`); four excerpts of the model's working trace, below |
| `EXIT_TOWER/` | The MDT-structure as the exit category of the stable moduli stacks; finite models; forgetting at infinity; the levels; completion and the Galois action (cote 147, §§7–10, scans 60–105, 152, 179; cote 146, scan 100) | packaged; the prompt stands as revised on 13 Nov (typesetting check added) |
| `FLAGGED_149/` | Every step that cote 149 and the opening of cote 142 mark as unverified, proved or refuted; its zip has a second part, `FLAGGED_149_new_results.zip` | sent and returned 12 Nov 2026 (`../../pro_returns/FLAGGED_149/`; intake in `../../reviews_max_20261112/FLAGGED_149_REVIEW_FABLE/`, check of the sources cited for F17.6 and F17.7 in `../../reviews_max_20261112/FLAGGED_149_SOURCE_CHECK_OPUS/`) |
| `GOOD_REDUCTION/` | The limit action at a place of bad reduction, and Grothendieck's "Conjecture-à-tout-hasard" (cote 149, scans 99–104) | packaged 12 Nov; not sent; superseded 13 Nov (next row) |
| `GOOD_REDUCTION_SUPERSEDED_20261113/` | The same prompt in its last version, set aside on 13 Nov 2026 and not sent: its items went into `ANABELIAN_149_PUSH` (`SUPERSEDED.md` there) | superseded; do not send |
| `ANABELIAN_149_PUSH/` | Every statement that the returns FLAGGED_149 and CYCLOTOMIC_KERNEL left undecided on cote 149 and on the opening of cote 142, with what GOOD_REDUCTION still asked (written 13 Nov 2026 by Claude Fable 5.2, effort max; `ZIP_LIST.md`, and the two scripts that fetched the sources and built the zip) | packaged 13 Nov 2026 |

Other files:

- `GLOBAL_SHAPE_AFTER_CYCLOTOMIC_20261112.md`: the shape of cote 149 and the order of the next prompts after the review of
  the CYCLOTOMIC_KERNEL return (reader R-149, Claude Fable 5.2, effort max; its own marks say which parts are unchecked).
- `EXIT_ONE_TYPE/TRACE_20261112_part1_untitled1955.md`, `_part2_paste.md`, `_part3_paste.md`: the working trace of the
  EXIT_ONE_TYPE run as GPT-6 Astra (ChatGPT Pro mode) displayed it in the chat on 12 November 2026, copied by the user
  while the run was going and its execution environment was disconnected. They are the model's own trace text, not a
  return; part 1 is a raw copy of the page (it opens with the app's menu and ends mid-sentence), and parts 2 and 3 have a
  short header saying where they come from.

Added 13 November 2026: `EXIT_ONE_TYPE/TRACE_20261112_part4_paste.md` (a fourth excerpt of the trace, like the
others); `EXIT_ONE_TYPE_EARLY_SHAPE_20261112.md` (a note written from the trace while the run was going; unchecked);
`PACKAGING_REPORT_20261112.md` (how the zips of 12 November were built). `ZIP_CONTENTS.tsv` of every folder was
regenerated from the zips as they stand.

In these copies the first name of the user is replaced by "user", local paths included. Nothing else in the files is
changed.

To the extent that we hold any rights in these AI-produced texts, they are dedicated to the public domain under CC0 1.0.
