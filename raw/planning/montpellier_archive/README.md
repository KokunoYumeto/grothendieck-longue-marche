# Planning files of the Montpellier archive work

These are the working plans of the work on the open part of Grothendieck's mathematical archive at Montpellier
(178 cotes, 16,074 scan pages): what each section contains, how the whole is organized into books and chapters, in
which order it is transcribed, how the second pass and the readings are run, and what they cost. They are plans and
methodology, not results: the mathematics and the transcriptions are in the other folders of `raw/` and in the
edition. They are filed in this repository, with the archive returns, until the archive has its own repository.

All files are AI-produced. Figures marked as estimates are estimates; the files were written on the dates given and are
not updated here.

| File | What it is | Written by | Date |
|---|---|---|---|
| `PLAN_EVERYTHING.md` | The plan for the whole archive as the user set it: download everything, organize it by topic, transcribe in Pro mode in packages, second pass, editions; with the adopted shape and order and the page counts by route | Claude Opus 5.5 (the coordinating session; effort setting not recorded in the file), recording the user's instructions | 10 Nov 2026, additions 11 Nov |
| `SECTIONS_STATE.md` | What each of the 178 cotes contains, how far Grothendieck took it, and who has edited or studied it, with sources | Claude Opus 5.5, effort max | 10 Nov 2026 |
| `ORGANIZATION_RECOMMENDATION.md` | How to organize the archive as one body of mathematics: a front door, six books and a workshop, and the transcription order that follows | Claude Fable 5.2, effort medium | 10 Nov 2026 |
| `PLACEMENT_EVERYTHING.md`, `PLACEMENT_EVERYTHING.csv` | Every cote placed in a book and chapter, with its reading position, transcription rank, route and package; the CSV has one row per cote | Claude Fable 5.2, effort medium | 11 Nov 2026 |
| `EXISTING_EDITIONS_CHECK_20261112.md`, `.html` | Whether the outside editions of *Pursuing Stacks*, the *Esquisse d'un programme* and "Nouveau EGA V" are complete and faithful to the archive's typescripts, checked against the scans | Claude Opus 5.5, effort max | 12 Nov 2026 |
| `ARCHIVE_PLAN_20261112.html` | Report on the state of the work: what has been transcribed and returned, the works it goes into, the quality of the first pass, the cost of the second pass, the plan for the Fable readers, and the decisions open on that day | Claude Opus 5.5, effort max | 12 Nov 2026 |
| `PROGRAM_WARGAME_20261112.md`, `.html` | War game, round 1: a planning and simulation pass over the plan made at effort medium; how the programme develops from what has been found, what has to change for it to be a coherent whole, and what mathematics follows from the totality | Claude Fable 5.2, effort max | 12 Nov 2026 |
| `PROGRAM_WARGAME_ROUND2_20261112.md`, `.html` | War game, round 2: corrects and extends round 1 and replaces its summary; to be read first | Claude Fable 5.2, effort max | 12 Nov 2026 |
| `ROUND2_STATE_20261112.md` | State note written at the end of round 2: what was finished, what was not checked, the lookups that failed | Claude Fable 5.2, effort max | 12 Nov 2026 |
| `WARGAME_MATH_HUNCHES_20261112.md` | Nine mathematical hunches drawn from the war game (H1–H9), each with its statement, the reason for it, the smallest test, what would refute it, the cotes and results it bears on, and a prompt specification; unchecked when written | Claude Fable 5.2, effort max (the round-2 war-game agent, consulted) | 12 Nov 2026 |
| `H8_CHECK_20261112.py`, `H8_CHECK_20261112_output.txt` | Machine check of hunch H8: the cokernel of the divided-power Lefschetz map Λ^i(Z^2g) → Λ^(2g−i)(Z^2g) by Smith normal form, for g ≤ 5 and for g = 6 with i ≤ 3, against the prediction from Wilson's diagonal form for inclusion matrices; all 22 cases agree | Claude Opus 5.5, effort max | 12 Nov 2026 |
| `AGENT_USAGE_20261112.csv` | Raw usage metadata, one row per agent run on 12 Nov 2026 | Extracted from the session records | 12 Nov 2026 |

Columns of `AGENT_USAGE_20261112.csv`: `agent` (short agent id), `description` (the agent's task), `model`,
`first_turn_utc` and `last_turn_utc`, `turns`, `input_tokens`, `cache_write_tokens`, `cache_read_tokens`,
`output_tokens`, and `cost_units`, which weights the tokens by their price ratios: 1 × input + 1.25 × cache writes +
0.1 × cache reads + 5 × output, per million tokens.

The HTML files are renderings of the Markdown files of the same name, except `ARCHIVE_PLAN_20261112.html`, which
exists only as HTML. "GPT-6 Astra (ChatGPT Pro mode)" is the model that makes the first-pass transcriptions; "points"
are shares of the weekly usage meters of the subscriptions the work runs on.

In these copies the user who runs the project is called "user". In `ARCHIVE_PLAN_20261112.html` the label of the user's
API account is replaced by a description. Nothing else in the files is changed.

To the extent that we hold any rights in these AI-produced texts, they are dedicated to the public domain under CC0 1.0.
