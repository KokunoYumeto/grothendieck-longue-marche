# Codex-web folders of the Montpellier archive, 13 Nov 2026

Five drag-and-drop folders, 52 scans, for the second ChatGPT account's remaining Codex allowance for the week. Each
folder is one transcription task for GPT-6 Astra at reasoning effort high, of about an hour. They hold the
easiest-to-read scans of the archive: typescripts with Grothendieck's handwritten corrections, and letters. Built by
Claude Opus 5.5 at effort high, 13 Nov 2026, ~17:40 UTC.

| Folder | Cote | Scans | Count | What the scans are | Zip |
|---|---|---|---:|---|---:|
| `drag\A57-01` | 57 (Picard) | 3-13 | 11 | typescript in English, "Local Picard schemes", with handwritten corrections | 19.2 MB |
| `drag\A57-02` | 57 (Picard) | 20-23, 73-79 | 11 | typed letters in English: one to Murre; two letter texts dated July 18, 1962, one of them with the typed signature A. GROTHENDIECK | 21.5 MB |
| `drag\A29-01` | 29 (Groupe fondamental) | 3-6, 8-12, 79-81 | 12 | letters in English, "Dear Grothendieck" / "Dear Murre" (scan 3 is dated May 10 1967): typed, one written by hand (5-6), typed comments (80-81) | 17.0 MB |
| `drag\A36-01` | 36 (SGA 7, ma part) | 10-18 | 9 | typescript in French with many handwritten corrections, insertions and typed-over words | 14.8 MB |
| `drag\A36-02` | 36 (SGA 7, ma part) | 19-27 | 9 | the same typescript, continued | 13.9 MB |

`ASSIGNMENTS.tsv` lists every folder with its cote and scans, and the Pro package of the 12 Nov packaging report that
holds them (the Pro packages are being re-cut today, so the package names will change). When a return proves good,
the Pro packaging leaves these scans out.

## Why these scans

- **Easy to read.** Grothendieck's handwritten notes in these cotes are fast and dense on nearly every page we sampled
  (contact sheets of 12 cotes: 2, 29, 31, 36, 37, 57, 62, 63, 122, 126, 130, 131). The typed and letter pages are
  the clear exception. To find them, every scan of eleven cotes with typescripts (27, 29, 32, 35, 36, 37, 45, 46, 57,
  63, 123) got a typed-text score from Tesseract word confidences, used only to choose pages, never to transcribe.
  The high-scoring runs were then looked at in contact sheets, and the coherent ones kept:
  - consecutive pages of one typescript (57 scans 3-13, opening with its title; 36 scans 10-27, opening with its
    title on scan 10, split in two);
  - the letters together (57; 29).
  Every page is upright; scan 7 of cote 29 is blank and was left out. A full-size third of 36 scan 14 was checked:
  typewriter text, sharp, with handwritten corrections legible.
- **Late in order W.** The scans belong to packages 159 (36), 164 (57), 170 and 171 (29) of the 12 Nov packaging
  report: ranks 21, 23 and 24, near the end of the send order. None is in a package sent or returned (01-35,
  `packages_done\`, `returns\`). `packages\` and `packages_work\` were not touched.
- **Left out on purpose:** copies of other authors' printed articles (63), his handwritten calculation drafts, and
  the typed French text of 29 (scans 13-38), which is legible but dense in indices and would need smaller folders.

## How the folders were sized: about an hour at Astra high

The Deligne drag returns record their times in `progress.log` (deligne_codex_packets_20261112\returns\). Over the 20
returns of 12-13 Nov (GPT-6 Astra at reasoning effort high), start to frozen transcription took 12-76 minutes for
6-12 pages: median 4.3 minutes per page, of which about 1.5 for the first pass and the rest for the second reading.
The one typescript graded (D002-01) took 5.1 minutes per page.

- **The two typescripts of 36:** 9 scans each. The pages are full, and nearly every line has a correction or a
  typed-over word; they will run slower than D002.
- **The typed letters (57, 29):** 11-12 scans each. The letters run at about the D002 rate.

The rate for handwriting does not enter: the only handwritten pages are the two of one letter (29 scans 5-6),
written in a clear hand.

## How to run them

On the second ChatGPT account, open a work session (Codex) with **GPT-6 Astra, reasoning effort high**, one session
per folder, as for the Deligne drag folders. Drag in the three files of the folder: `PROMPT.md`, `PREAMBLE.tex` and
`<ID>_scans.zip`. The first line of `PROMPT.md` says that the file is the task. To check the method on one return
before the rest, start with A57-01: look at its final message, `out\progress.log` (minutes per page) and
`out\A57-01_audit.md`, whose second reading must list what it checked. The four other folders can run while you
check.

## What comes back, and where it goes

Each session offers `<ID>_out.zip`. It holds:
- `pages\<ID>_<cote>_scanNNN.tex`;
- `<ID>_transcription.tex` and `<ID>_standalone.tex`;
- `<ID>_doubts.md`: the notation table, the doubts, the slips kept as written and the abbreviations;
- `<ID>_inventory.csv`, with the columns `sheet_kind` and `hand`;
- `<ID>_audit.md`;
- `<ID>_notes.md`: the steps the pages mark as unverified, and their titles, dates and page counts;
- `progress.log`.

Drop the zip into `C:\Users\user\Documents\grothendieck_archive_transcription_20261110\codex_web_20261113\returns\`.

## How a return is graded

One return is graded before the scans are taken out of the Pro packages, the way D002-01 was
(`deligne_codex_packets_20261112\returns\GRADE_D002-01_20261113.md`). The grade is an in-app check by Claude Opus 5.5
at effort max.
- **Pages.** Two of the return's pages, read line by line against the images: the one densest in formulas and
  corrections, and an ordinary one.
- **What is counted:**
  - omissions;
  - text errors, mathematics errors and font errors;
  - doubt marks missing where the page is unclear, and marks put where it is clear;
  - handwritten corrections left out or put in the wrong place.
- **Also checked:**
  - the counts in the final message against the files;
  - the first and last lines of the other pages against the images;
  - a LuaLaTeX build of the standalone file here, with the overfull boxes counted (the sandbox does not compile).

Verdict: good enough as is, good enough with a second pass, or not usable. If the grade is good, the ASSIGNMENTS.tsv
rows are dropped from the Pro packages.

## The prompt

`tools\PROMPT_TEMPLATE_CODEX_WEB.md` takes these parts from the archive's Pro template (`ARCHIVE_PROMPT_TEMPLATE.md`):
- the macros (`\cotefile`, `\scanpage`, `\mspage`, `\deleted`, `\inserted`, `\margin`, `\uline`, `\uuline`,
  `\diagram`, `\figure`, `\unsure`, `\illegible`) and its doubt rules;
- one stream, and the notation table;
- the inventory with `sheet_kind`;
- the two standing questions.

It is laid out like the Deligne drag prompt:
- the whole page and three thirds per scan, with MANIFEST.tsv;
- a page file and progress line per page as the checkpoint;
- a full second reading with a per-page audit;
- frozen hashes, and a zip offered as a download.

Without the context zip and the research notes, which are the Pro runs' part. New for this material:
- `\handwritten` for his hand on a typed page;
- typed-over words as `\deleted`;
- letters, letterheads and the archive's sheet numbers;
- a `hand` column in the inventory.

The four prompt changes from the D002-01 grade are applied:
1. **Overstruck letters.** Every capital in a heading or a functor name is checked for double striking on its own
   crop; a notation entry for the body does not cover a heading. A typescript has no bold.
2. **Second reading from a fresh crop.** The accents and the odd-looking words of each line are written down from
   the crop before the page file is opened.
3. **Recurring ambiguous glyphs.** The doubt is recorded once in the notation table, with every candidate, and
   marked at its first occurrence on each page.
4. **No compilation in the sandbox.** LuaLaTeX does not work there; only the balance check is run, and we compile
   the return here.

Also added: `\diagram` with tikz-cd needs `ampersand replacement=\&`, as the Pro returns write it. Every PROMPT.md
passes `push_rule_pro_prompts.py --lint`. `tools\PREAMBLE.tex` was test-compiled with every macro under LuaLaTeX and
pdfLaTeX, with no errors.

## Files

- `drag\<ID>\`: the five folders, flat, as dragged.
- `ASSIGNMENTS.tsv`.
- `returns\`: for the returned zips.
- `tools\`:
  - `build_codex_web.py`, which builds the folders; it reads the archive PDFs only and skips folders that exist;
  - `PROMPT_TEMPLATE_CODEX_WEB.md`;
  - `PREAMBLE.tex`;
  - `BUILD_LOG.jsonl`: per folder its scans, ink values, zip size and SHA-256.

Images are taken as in the Pro packages, then converted to grayscale:
- the largest image of each PDF page (about 1700 x 2150 px, 228 ppi);
- autocontrast with cutoff 1, and an unsharp mask (r2 p120 t3);
- JPEG at quality 88;
- thirds overlapping by 60 px.

SECTIONS_STATE.md lists a CSG transcription (L12d) of a letter from cote 29; which letter it is was not checked.


## Batch B, 13 Nov 2026 ~19:1x UTC: 20 more folders, 181 scans (user: every easy-to-read run, Codex web at GPT-6 Astra max)

Effort: the user runs these folders at GPT-6 Astra **max** (A57-01 ran at max and took about 2 hours for 11 scans; checked on scans 003 and 008 by Claude Opus 5.5 at effort max: no misreadings, markup correct).

Source of the pages: the typed-page inventory `api_typescripts_20261112/TYPED_INVENTORY_20261113.tsv` (made by eye from contact sheets), the typed scans of cotes 10 (typescript on Tannakian categories, 84 scans), 37 (typed letters, lists, typescripts, tables of contents, 48 scans), 12 (22 scans) and 15 (27 scans, some faint or probable). None of these was sent over the API or to Pro. Upside-down typed versos are left out. Scan numbers are PDF pages (the inventory's site number + 1); a first build that used the site numbers was set aside in `_wrong_pages_20261113_not_for_use/`. Folders: B10-01 to B10-10, B37-01 to B37-05, B12-01, B12-02, B15-01 to B15-03; each 5-11 scans. Rows in `ASSIGNMENTS.tsv`.

## Batch C, 13 Nov 2026 ~19:5x UTC: 12 folders, 70 pages

Every page of cotes 27, 29, 32, 35, 36, 45, 46 and 123 was scored by `tools/score_typed_C.py` (Tesseract, words of 3+ letters read at confidence >= 80; `scoring_C/scores.tsv`). Pages scoring 60 or more and not already in a folder were kept (`scoring_C/selected.json`) and all 70 were checked by eye on one contact sheet: all typescript, many with handwritten corrections and formulas. Folders of 4-8 pages (cote 29's French text is dense, so its folders are small): C29-01 to C29-07, C32-01, C45-01, C46-01, C123-01, C123-02. Single typed pages of cotes 35 and 36 were left out. A57-01 is in `done/`; the builder now skips folders found there.
