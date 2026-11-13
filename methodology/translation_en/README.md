# La Longue Marche in English: the translation over the API of 12 November 2026

Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981; cotes 140-1 to 140-4 of the
Grothendieck archive, Université de Montpellier, 1,588 scans), AI-translated by GPT-6.1 Sol (OpenAI, effort max) from
the AI-transcribed text checked by Claude Opus 5.5. The user decided on 12 Nov 2026: "The translation should go over
the API, because then immediately you have it". Prompts, runs, checks, fixes and build by Claude Opus 5.5 (Claude Code,
a subagent). Not published: the coordinator publishes after a look.

**Status (12 Nov 2026, 22:07 UTC): 173 of 245 units translated (1,175 of 1,588 scans), $23.1802 billed of the $40
limit; projection for the whole translation $32.43.** All 173 English units pass the checks (38 fixes in
`checks/FIXES.jsonl`, 25 waivers in `checks/WAIVERS.jsonl`); the 93 complete packages compile with the same status as
their French (83 as they are, 10 after the mechanical repairs; `build/COMPILE.tsv`). 72 units (413 scans) remain; the
main session runs them from b06 on ("To continue"). The reader is built when all packages are in.

**Status at the pilot (12 Nov 2026, 19:20 UTC): stopped after the pilot, as the brief requires.** The pilot (3 packages, 7 units,
48 scans) cost $0.9364 at the Flex price. Extrapolated by French characters to all 245 units, the whole translation
comes to **$35.41**, over the $35 limit, so no further batch was submitted. The 7 pilot units pass every check (after
one fix); the 3 pilot packages compile as their French does; a test reader of the 3 packages compiles (29 pages, no
LaTeX errors). Everything is ready to continue in one command once a higher limit is set ("To continue" below).

**Run record.**
- 12 Nov 2026, 19:01-19:16 UTC: b01-pilot, 7 units, $0.9364; projection $35.41, over the brief's $35: stopped.
- 12 Nov 2026, 19:43 UTC: the user approved raising the limit to **$40** (relayed by the coordinator); `CAP = 40.0` in
  `scripts/run.py` ("the user's limit, raised from 35 on 12 Nov 2026 after the pilot's projection of $35.41"). The
  guard is unchanged: the amount billed so far plus each batch's worst case, and the projection, must stay within the
  cap; one batch at a time.
- b02, 19:45-20:32 UTC: 50 units, 397 scans, $7.4441 (in 321,397, out 1,424,544 tokens, 1,183,385 reasoning), with
  the prompt's explicit diagram line. Raw checks (with the checks as refined after it): 26 pass, 24 fail.
- The faithfulness review of the 7 pilot units (`checks/FAITHFULNESS_REVIEW_PILOT_20261112.md`, Claude Opus 5.5 at
  max; 17 findings, 6 medium) and the coordinator's approval of its five prompt changes: made exactly as given for the
  units not yet sent (`prompt/PROMPT_PARTS_LM.txt`: the m-bar line, "soit" is "i.e." and Latin stays Latin, a mark
  holds exactly what it holds; `scripts/terms_LM.txt`: "hom" between schemes, pairs, spaces, topoi, sheaves of sets
  is a morphism, the new entry "automorphisme à lacets" → loop automorphism, also entered in the glossary's
  `entries_LM.txt` (the files before: `glossary_before_20261112/`); `scripts/common_lm.py`: the `MBAR` pattern for
  the two-reading and plural forms). The parts as b02 had them: `prompt/PROMPT_PARTS_LM_b02.txt`; the 57 prompts sent
  before the change are kept as sent. The review's 17 pilot corrections: 19 rows of `checks/FIXES.jsonl`; its waivers
  for scans 116 (a formula) and 148 (the negation across the illegible gap left open: \unsure{does not occur|only
  occurs}).
- b02's search for the review's patterns (`scripts/b02_patterns.py`): his m with a bar 1 place changed (LM_P037,
  \unsure{same|$=$} to \unsure{same|=}); "homomorphism" for maps of topoi or spaces 3 changed (LM_P011, LM_P014,
  LM_P021); "soit" rendered "or" 0 (16 candidates read: all render "ou" or "soit ... soit", or "soit" is "let"/"say");
  Latin put into English 0; "autom. à lacets" 3 changed to "loop automorphism", 5 kept where his "à lacets" stands
  inside his insertion (waived), 2 were the review pattern catching "hom. de groupes à lacets" (pattern widened). No
  unit had more than three such places, so none was re-run. Also LM_P04 (\hbox{et}, \hbox{si}) and LM_P018 ("ou"
  inside a formula, one of the review's places) fixed.
- b03, 20:37-21:15 UTC: 48 units, 348 scans, $7.0026 (in 316,677, out 1,337,191; 1,113,084 reasoning), the first with
  the reviewed prompt. Raw: 35 pass, 13 fail; 1 fix ("loop group"), 11 waivers (his marks kept where they stand,
  "lacets de souliers" is shoelaces, two m-bar readings), 3 patterns widened; the review's places LM_P040 (negation
  left open: \unsure{cannot|can only}) and LM_P056 (m with a bar in a display: \text{same grain of salt}) fixed; the
  package compile found one LaTeX slip (LM_P054, "\S\)"), fixed.
- b04, 21:18-21:50 UTC: 38 units, 234 scans, $4.6413 (in 229,849, out 882,290; 716,732 reasoning). Raw: 30 pass, 8
  fail, mostly French words inside marks within formulas translated ("\deleted{\unsure{par}}" to "by") and raised
  endings of abbreviations ($^{\mathrm t}$) written out: the formula check now lists both for review (docstring of
  `scripts/check_units.py`); 1 waiver, 2 patterns widened; the review's place LM_C3-207-225 (negation left open:
  \unsure{does not cover|covers only}) fixed.
- b05, launched by the main session at 21:50 UTC, 21:50-22:06: 30 units, 148 scans, $3.1557 (in 185,503, out 594,045;
  456,468 reasoning). Raw: 28 pass, 2 fail; 1 fix ("loop groups"), 1 waiver; the review's places in b05: LM_C3-454-472_s467-472 ("\inserted{et}" in a formula came back "\inserted{and}"), and his m with a bar in the displays of LM_C3-454-472_s454-458 and LM_C3-492-510_s497-501, written out (\text{likewise}, \text{and likewise}; 2 fixes, 2 formula waivers).
- All five batches: no Flex refusal, no failed request, no re-run; one ledger row each (`lmtr-b01-pilot` to `lmtr-b05`).

## The pilot

| | |
|---|---|
| Packages | LM_P012 (cote 140-2, scans 111-120, a `_checked_fixed` text), LM_C3-131-149 (140-3), LM_C4-001-019 (140-4; m-bar shorthand, the archive's printed footers, quotation marks, a text that compiles only after the mechanical repairs) |
| Units | 7 (5 to 10 scans, 9,813 to 14,198 characters), 48 scans, 79,380 French characters |
| Requests | 7, all completed on Flex at the first submission (no refusals); 14.5 minutes for the batch |
| Tokens | 39,328 in; 179,421 out, of which 149,974 reasoning |
| Billed | **$0.9364** at the Flex price ($1.00 / $5.00 per million); $1.8729 at list price; $0.0195 a scan, $0.0000118 a French character; per unit $0.0997 to $0.1803 |
| Ledger | one row, `lmtr-b01-pilot`, in `C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl` (key "OpenAI project key (Untitled 1936.md)") |

**Projection for the whole translation (245 units, 1,588 scans, 3,001,419 French characters):**
- by French characters (the basis `scripts/run.py` uses; cost follows the length of text): **$35.41** in all
  (including the pilot's $0.94);
- weighted by cote (the pilot's rate for 140-2, 140-3 and 140-4 applied to each cote's characters): $35.68;
- by scans: $30.98; by units: $32.77 (the pilot's scans and units are shorter than the average: 1,654 characters a
  scan against 1,890);
- the seven units' rates per character spread from $9.2 to $14.9 per million characters (mean $11.7, standard error
  about 7 %), so the true total lies roughly between $33 and $38.

For comparison, Les Dérivateurs cost $0.0000068 a character with the same model and settings; the Longue Marche costs
about 1.7 times as much a character. Its reasoning is 84 % of the output tokens (77 % for Les Dérivateurs): the
deletions, insertions, doubt marks with two readings, and his abbreviations make each unit harder.

## Model and method

The method of the Dérivateurs translation (`C:\Users\user\Documents\derivateurs_translation_20261111`), applied to the
transcription of the Longue Marche.

- **Model**: GPT-6.1 Sol (`gpt-6.1-sol`), reasoning effort max, OpenAI Responses API, **Flex tier**
  (`service_tier: "flex"`), background mode, `max_output_tokens` 128,000, no tools. No Batch API job (another batch
  job runs on the second account). The key of the user's first OpenAI account is read only by
  `enriques_api_pilot_20261106\enr_pilot.py` (`call`), from the user's note, at each request; never printed, copied,
  logged or stored.
- **Input (source of record)**: `second_pass\CURRENT_TEXT_INDEX.tsv`, the closed second pass: 116 packages, each with
  its current text (32 `_checked_fixed`). The sha256 of each current text is in `source/MANIFEST.json` and is checked
  again before every batch (and each unit must still be the same slice of it). Compared with the repository
  KokunoYumeto/grothendieck-longue-marche after `git fetch` (origin/main 671d2cf): 22 texts are the same blob in
  `raw/second_pass/`, 18 the same text up to line endings, 50 the same blob elsewhere in the tree (`transcription/`,
  the prompts' attachments), 26 not found as an identical blob (`source/SOURCE_OF_RECORD.json`; logged in
  `Documents\LOGBOOK_20261112.md`).
- **Units** (`scripts/prepare.py`): each package's current text cut at `\scanpage` lines into runs of consecutive
  scans of about 12,000 characters (the Dérivateurs units had about 15,000): **245 units** of 3 to 12 scans (median
  12,137 characters). Every `\scanpage` line of the 116 texts is at brace depth 0; a cut that would leave a formula,
  group or environment open moves on; the units of a package joined give the package byte for byte.
- **Prompt**: the comparison's template `prompt/PROMPT_TEMPLATE.txt`, byte for byte (the Dérivateurs used the same),
  with the comparison's La Longue Marche parts, extended for the whole manuscript in `prompt/PROMPT_PARTS_LM.txt`
  (the cote; his "même" written m with a bar; the archive's printed footers copied as they are; the unit's other
  text-carrying macros; diagrams and drawings; quotation marks ``...''). A faithful English in his voice, his own
  English of *Pursuing Stacks* as the model, American spelling; formulas, macros, `\scanpage`, `\mspage` and
  comment lines copied; the marks `\deleted`, `\inserted`, `\margin`, `\unsure` (with both readings of A|B),
  `\illegible`, `\uline` kept where they stand, their words translated, deletions included; his abbreviations written
  out. The user message: the request line (cote, scans, his page numbers) and the unit's text. Every request's
  prompts: `prompt/system/`, `prompt/user/`.
- **Glossary and notation** (`C:\Users\user\Documents\translation_glossary_20261110`): every request carries the
  term lines (`scripts/terms_LM.txt`, all 116 entries) of the entries whose French occurs on its scans.
  NOTATION_LM's decisions that act on the prose are applied (abbreviations written out, "ssi" iff, the m-bar
  written out, underlining kept, ``...''). Listed rather than applied: the two PENDING entries (script S/G; natural
  or sharp exponent) and the decisions that would change formulas (SL/GL, `\GQ`, `\tag` and the like), since the
  formulas stay the French's character for character: `checks/GLOSSARY_APPLIED_AND_FLAGGED.md`.
- **Spend rules** (`scripts/run.py`): one batch at a time; before a batch, the dollars billed so far plus the batch's
  worst case (128,000 output tokens a request) must stay within the cap ($35), and after the pilot the projection
  (billed so far plus the characters left at the measured rate) must too; Flex refusals ("server_is_overloaded",
  nothing billed) resubmitted after 4, 8, 16 and 30 minutes, up to 8 times; exhausted credit stops the run. One ledger
  row per batch.
- **Checks** (`scripts/check_units.py`; the Dérivateurs checks, loaded from byte-identical copies in `scripts/der/`,
  with the comparison's `checks.py`): formulas identical to the French (the wording of text-mode boxes masked); his
  standalone m-bar formulas left out on both sides (they become words); `\scanpage` and `\mspage` in order; comment
  lines unchanged; **the apparatus marks counted scan by scan** (`\deleted`, `\inserted`, `\unsure`, `\illegible`,
  `\margin`, `\uline`, `\uuline`, and the bars of `\unsure{A|B}`: must be equal); **completeness**: paragraphs paired
  one for one (blank lines kept), each paragraph's length (fails below 0.7 or above 1.8 of its French, 80 characters
  and more), each scan's length (fails below 0.7, 300 characters and more); no French left (function words, flagged
  sentences, elisions, French in the text-mode wording of formulas); the glossary's English on the scan where its
  French occurs (100 entries fail when missing, 16 are listed for review); British spellings; no new control
  sequence that acts outside the page. A failing unit is fixed (`checks/FIXES.jsonl`, applied by
  `scripts/assemble.py`) or re-run; a misfire on a correct translation is waived with its reason
  (`checks/WAIVERS.jsonl`).
- **Build** (`scripts/build.py`): each English package in the transcription's check wrapper
  (`answers/fixed/build/wrap.tex`, byte for byte), LuaLaTeX, as it is and, if that fails, after the reader build's
  mechanical LaTeX repairs (`fix_tikzcd_in_macros.py`, `unwrap_gathered_diagrams.py`, `normalize_reader_text.py`), as
  the second pass compiled the French; the reader: one LaTeX file, title page, a note on the text, how to read it
  and how it was made, credits and rights, the contents by cote and package, then the packages.

## Results of the pilot

- **Checks of the output as it came back**: 4 of 7 pass as first checked (6 of 7 with the widened pattern below,
  `checks/CHECKS_raw.json`). 3 fail: in two units the glossary entry "commutant" (his
  noun for the centralizer) fired on the participle "commutant à ρ", "commutant extérieurement", which the model
  rightly translated "commuting" (the English pattern now accepts it; the file as first used is
  `checks/terms_LM_as_first_used.txt`); in LM_P012 the transcription's description of a drawing, in French in square
  brackets inside `\diagram{...}`, was copied untranslated. Fixed (`checks/FIXES.jsonl`, 1 fix), and the prompt's
  diagram line now asks for such descriptions to be translated (21 places in 14 units; the parts as the pilot had
  them: `prompt/PROMPT_PARTS_LM_pilot.txt`; the seven prompts sent are unchanged).
- **Checks of the English units: 7 of 7 pass.** Formulas: 1,119 of 1,119 identical to the French (and 7 m-bar
  formulas written out as words, 7 of 7); 72 page anchors in order; 257 paragraphs paired one for one; every
  apparatus mark and every bar of `\unsure{A|B}` the same on every scan; glossary: 221 of 222 entry-scans carry the
  English form (the one other is "extérieurement", of level review, rendered by a phrase). Points to review, one in
  each of 3 units: that "extérieurement"; "dévissages" (the glossary keeps the word in French); two terms found fewer
  times than in the French on their scans (LM_P012, "profini" and "topos étale").
- **Compile**: LM_P012 OK (4 pages), LM_C3-131-149 OK (10 pages), LM_C4-001-019 OK after the mechanical repairs (11
  pages): the same status as each French text (`build/COMPILE.tsv`).
- **Reader** (`reader/LaLongueMarche_English.tex`, `.pdf`): a test build with the three pilot packages, 29 pages,
  no LaTeX errors, no undefined references, no missing characters, 8 overfull lines. The full reader is built by the
  same command when all packages are translated.

## To continue

State at 22:07 UTC, 12 Nov 2026: 173 of 245 units translated (b01-pilot to b05), $23.1802 billed of the $40 limit
(`CAP = 40.0` in `scripts/run.py`), projection $32.43; 72 units to do (413 scans, 856,012 characters); no batch in
flight; 26 units fit under the guard now. Next: `python -I -B run.py batch b06 --next 26`, then the next batches as
`run.py plan` allows (the worst case of a unit is $0.646, so they shrink as the total nears $40). After each batch:
the raw checks, repairs as for b02-b05 (fixes and waivers with their reasons), `assemble.py`, the checks of the English
units, the compile of the new packages. The review's places still to look at when their units come back:
LM_C3-587-605_s591-595, LM_C4-134-152_s134-139 (his m with a bar inside a display beside \text), LM_C3-663-681_s672-675
(`$\unsure{\underset{=}{\mathrm m}|\overline{\mathrm m}}$`). From `scripts/`:

```
python -I -B run.py plan                          # billed so far, projection, how many units fit now
python -I -B run.py batch b06 --next 26           # then b07 ... as many as run.py plan allows
python -I -B check_units.py --raw                 # checks of the output as it came back
python -I -B assemble.py                          # English units and packages (with checks/FIXES.jsonl)
python -I -B check_units.py                       # checks of the English units
python -I -B build.py packages                    # compile each English package
python -I -B build.py reader                      # the reader
python -I -B report.py                            # checks/REPORT.md
```

Each batch writes a ledger row (`lmtr-<batch>`) and refuses to start if the billed amount plus its worst case, or the
projection, would pass `CAP`.

## Files

| Path | What |
|---|---|
| `source/units/<unit>.tex`, `source/MANIFEST.json` | the French units (exact slices of the current texts), the packages and units with sha256 |
| `source/SOURCE_OF_RECORD.json` | the comparison of the 116 current texts with the repository (`scripts/source_of_record.py`) |
| `prompt/PROMPT_TEMPLATE.txt`, `PROMPT_PARTS_LM.txt`, `PROMPT_PARTS_LM_pilot.txt` | the template (byte for byte the comparison's), the parts, the parts as the pilot had them |
| `prompt/system/<unit>.txt`, `prompt/user/<unit>.txt` | every request's prompt (245 units; the 7 of the pilot as sent) |
| `runs/out/<unit>.tex`, `<unit>_result.json` | each translation as it came back, its figures (tokens, cost, response id, prompt hashes) |
| `runs/RUNS.jsonl`, `runs/b01-pilot.log`, `runs/state_b01-pilot.json` | the batches |
| `checks/raw/`, `checks/CHECKS_raw.json` | the checks of the output as it came back |
| `checks/units/`, `checks/CHECKS.json`, `checks/SUMMARY.md` | the checks of the English units |
| `checks/FIXES.jsonl`, `checks/WAIVERS.jsonl` | fixes applied (38), waivers (25), each with its reason, by whom and when |
| `checks/REPORT.md` | batches, tokens, costs, check and fix counts |
| `checks/GLOSSARY_APPLIED_AND_FLAGGED.md` | which glossary and notation decisions are applied, which are listed and why |
| `checks/terms_LM_as_first_used.txt` | the glossary check patterns as the pilot was first checked |
| `translation/units/<package>/<unit>.tex` | the English units (output plus fixes) |
| `translation/packages/<package>_en.tex` | the English of each complete package (93 at 22:07 UTC), bodies like the French current texts |
| `build/COMPILE.tsv`, `build/packages/<package>/` | the compile of each English package (wrapper, log) |
| `reader/LaLongueMarche_English.tex`, `.pdf`, `.log` | the reader (now: the test build of the pilot's 3 packages) |
| `scripts/` | `common_lm.py`, `prepare.py`, `run.py`, `check_units.py`, `assemble.py`, `build.py`, `report.py`, `source_of_record.py`, `terms_LM.txt`; `der/`: the Dérivateurs `check_units.py` and `common_dt.py` and the comparison's `cmp/`, byte for byte |

## Credits

- **Author**: Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981).
- **Scans**: Université de Montpellier, Institut Montpelliérain Alexander Grothendieck, archives Grothendieck,
  <https://grothendieck.umontpellier.fr/archives-grothendieck/>, cotes 140-1 to 140-4.
- **Transcription** (the French translated here): AI-transcribed; first pass GPT-6 Astra (OpenAI, ChatGPT Pro mode;
  one package through the OpenAI API), second pass Claude Opus 5.5 (Anthropic), against the archive images and the
  earlier transcriptions consulted as witnesses and not reproduced: Mateo Carmona's edition of the first part and the
  typeset text deciphered and transcribed by Mateo Carmona with the collaboration of Matthias Künzer
  (agrothendieck.github.io); the draft edition of the Centre for Grothendieckian Studies (Grothendieck Institute,
  Mondovì), February 2026; the table of contents compiled by Grothendieck himself, as published by the Grothendieck
  Circle.
- **Translation**: AI-translated by GPT-6.1 Sol (OpenAI; Responses API, reasoning effort max, Flex tier).
- **Glossary, prompt, checks, fixes, build**: Claude Opus 5.5 (Anthropic) and, for the glossary, Claude Fable 5.2
  (Anthropic) (`translation_glossary_20261110`).

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights,
in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain
under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.

## Status, 13 Nov 2026 (00:4x UTC)

- All 245 units translated (1,588 scans; $31.25 of the $40 cap). Checks of the English units (output + 41 fixes, 34 waivers): 245 pass.
- 116 of 116 packages compile (95 as they are, 21 after the reader build's mechanical repairs).
- Reader reader/LaLongueMarche_English.pdf: 796 pages, 0 LaTeX errors, 0 undefined references, 4 missing glyphs left (pages 94, 605, 606: one math-italic Gamma and three U+2243 set in the text font), 382 overfull boxes. Since 13 Nov the repairs apply only to the 21 packages that need them (they had broken LM_P07), and the preamble maps his Cyrillic to DejaVu Serif and U+27CB/U+27CD to STIX Two Math.
- To continue: the four missing glyphs; the user looks at the reader before anything is published.
