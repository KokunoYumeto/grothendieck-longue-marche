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
| `EXIT_ONE_TYPE/` | When the reconstruction by fundamental groupoids is exact: normal crossings pairs and their exit paths, the dependence on the compactification, minimal models, the boundary complex, the levels (cote 147, scans 106–190; cote 149) | sent; three excerpts of the model's working trace, below |
| `EXIT_TOWER/` | The MDT-structure as the exit category of the stable moduli stacks; finite models; forgetting at infinity; the levels; completion and the Galois action (cote 147, §§7–10, scans 60–105, 152, 179; cote 146, scan 100) | packaged |
| `FLAGGED_149/` | Every step that cote 149 and the opening of cote 142 mark as unverified, proved or refuted; its zip has a second part, `FLAGGED_149_new_results.zip` | packaged |
| `GOOD_REDUCTION/` | The limit action at a place of bad reduction, and Grothendieck's "Conjecture-à-tout-hasard" (cote 149, scans 99–104) | packaged |

Other files:

- `GLOBAL_SHAPE_AFTER_CYCLOTOMIC_20261112.md`: the shape of cote 149 and the order of the next prompts after the review of
  the CYCLOTOMIC_KERNEL return (reader R-149, Claude Fable 5.2, effort max; its own marks say which parts are unchecked).
- `EXIT_ONE_TYPE/TRACE_20261112_part1_untitled1955.md`, `_part2_paste.md`, `_part3_paste.md`: the working trace of the
  EXIT_ONE_TYPE run as GPT-6 Astra (ChatGPT Pro mode) displayed it in the chat on 12 November 2026, copied by the user
  while the run was going and its execution environment was disconnected. They are the model's own trace text, not a
  return; part 1 is a raw copy of the page (it opens with the app's menu and ends mid-sentence), and parts 2 and 3 have a
  short header saying where they come from.

In these copies the first name of the user is replaced by "user", local paths included. Nothing else in the files is
changed.

To the extent that we hold any rights in these AI-produced texts, they are dedicated to the public domain under CC0 1.0.
