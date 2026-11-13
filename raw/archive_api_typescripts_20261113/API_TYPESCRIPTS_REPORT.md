# Three typescripts transcribed over the API by collation: report

12 November 2026. The run used Claude Opus 5.5 (`claude-opus-5-5`, adaptive thinking, effort high) through the Message
Batches API, one request per page, with one batch at a time. The basis for the work is
`grothendieck_archive_montpellier/EXISTING_EDITIONS_CHECK_20261112.md`. Published raw on 12 Nov 2026, 18:57 UTC, in
grothendieck-longue-marche under `raw/archive_api_typescripts_20261112/` (commit 9eb13d1); additions of 13 Nov in
commit 2325f05.

> **Status note, 13 Nov 2026 (main session, from the user's review):** the user never confirmed this run and learned
> of it on 13 Nov; the user calls it an honest misunderstanding, not against their wishes. Each page was transcribed
> from its scan images, with the existing edition's passage given to the model as a draft for the comparison, so the
> transcriptions are not independent of the edition (the pilot shows two places where the model followed the edition
> against the ink). Only the 28 pilot pages were checked by eye. Since then: every paid run is confirmed with the user
> first and reported when done.

## Outcome in brief

- **The pilot passed.**
  - Recall was 178 of the check's 184 differences (96.7 %).
  - The new findings looked at on the crops were all real: 29 of them.
  - No error that the API itself introduced was found on the crops.
  - The cost was $0.066 a page on average, and $0.094 for Pursuing Stacks pages.
- **Pages done:**
  - *Pursuing Stacks*: all 680 pages in scope (typescript pp. 1–593 and the 134-2 front matter, letters and notes).
  - *Esquisse*: all 58 pages of copy 1.
  - Cote 25: the 3 pilot pages of 184.
  - Cote 24: the 3 pilot pages of 76.
- **Cost:** $63.55 billed at batch price over 6 batches. All 6 have rows in the ledger.
- **Why it stopped:** the API refused the first cote 25 batch (95 pages) with *"Your credit balance is too low to access
  the Anthropic API"*. That happened at $63.55 spent, not at the $70 cap. The account therefore held less than the
  assumed $118; the console balance should be checked. Cotes 25 and 24 remain to be done.

## Method

- **Drafts and alignment** (`scripts/align.py`, `scripts/inventory.py`; table in `alignment/ALIGNMENT.tsv`):
  - **Pursuing Stacks.** The draft is the arXiv 2111.01000 v2 LaTeX (CC0).
    - In 134-3 to 134-8, the page is matched by the `\pspage` markers. The draft passage runs from marker n to marker
      n+1, widened by about 400 characters on each side.
    - The site-to-page offsets were read from an OCR aligner, which matches word 3-grams of the Tesseract OCR against
      the draft. Within each run of pages the offset is constant:
      - 134-3: site = page;
      - 134-4: +88 (sites 1–82) and +87 (sites 84–100; site 83 is a Récoltes et Semailles verso);
      - 134-5: +187;
      - 134-6: +319 (sites 1–26) and +318 (sites 28–124). Site 27 is a struck-through version of p. 345;
      - 134-7: +442;
      - 134-8: +554 (sites 1–39).
    - Pages 279, 289 and 370 have no marker; their passage runs from n−1 to n+1.
    - The 134-2 pages and the notes for chapter II (134-3 sites 89–93) have no usable markers. The edition's L-numbers
      of the Quillen letter do not follow the sheets. Their passages come from the OCR aligner.
  - **Esquisse.** The draft is the text layer of the Grothendieck Circle's `EsquisseFr.pdf`. Its accents, which the
    text layer splits off, were recomposed by script. The passages come from the OCR aligner. The faint pages were
    OCRed again for alignment only (`scripts/reocr.py`).
  - **Cotes 24 and 25** have no draft.
- **Images** (`scripts/prep_images.py`): each page goes as two colour JPEGs at native resolution, the upper and lower
  parts, overlapping by 6 % of the height. Autocontrast with the same curve on all three channels keeps the hue of the
  inks.
- **Prompt** (`scripts/prompt_system.txt`, built from `ARCHIVE_PROMPT_TEMPLATE.md`): a diplomatic LaTeX transcription,
  with these rules:
  - no correction or normalization;
  - the handwritten layer marked with `\hand`, `\over{typed}{written}`, `\inserted`, `\margin` and `\deleted`;
  - typewriter strike-outs marked `\xout`;
  - doubt marked `\unsure` and `\illegible`.
  The model transcribes first and only then compares with the draft. It then lists every difference as JSON lines,
  with a class, the draft's text, the page's text and a note. It also writes notes on what needs a check by eye.
- **Outputs** (`scripts/parse.py`):
  - `pages/<key>.tex`: the model's transcription, unchanged, under a comment header;
  - `<dir>_combined.tex`;
  - `DIFFERENCES.tsv`;
  - `NOTES.tsv`.
  The folder guide is `README_FOLDER.md`.

## Pilot

The pilot covered the 28 pages that the check compared: 11 of Pursuing Stacks, 11 of the Esquisse, and the 6 of
EGA V (cote 24 sites 4, 18 and 37; cote 25 sites 2, 4 and 140). It ran as batch `msgbatch_0189Nhf1xB615YWnztubtLfc`.

**Recall.** Every difference the check lists was written down as an item before the results were read
(`scripts/pilot_eval.py`), 184 items in all. For EGA V the items are the check's readings, since there is no draft.
Each item was then matched by script and reviewed by hand (`pilot/pilot_review.tsv`).

| Text | Items | Caught (reported, or the page's reading in the transcription) |
|---|---|---|
| Pursuing Stacks | 137 | 133 |
| Esquisse | 13 | 12 |
| EGA V (cotes 24 and 25) | 34 | 33 |
| **Total** | **184** | **178 (96.7 %)** |

The six misses:

- **"stablilise" (134-2 site 44).** The API transcribed "stabilise", which is the draft's reading. The crop shows the
  misspelling.
- **Struck "pouvoir" (same page).** It is transcribed as live text, as in the draft. On the crop the word is plainly
  struck.
- **The handwritten 1 and 7 of the Esquisse N.B.** They are transcribed as superscripts without the handwriting mark.
- **Commas after "(non-ordered simplices)" and "boundary maps)" (p. 337).** Not reported.
- **"roman s, t, k" (L.2).** Not reported. The prompt excludes font conventions.
- **k′ in "à valeurs dans k′" (cote 25 site 140).** The API reads "k" followed by a handwritten comma. The stroke on
  the crop looks like a comma, so this one is disputed.

The first two follow the draft against the ink. A transcription made after seeing the draft can be pulled towards it.

**Where the check was wrong.** "nothing on" (p. 81) is typed above the line, not handwritten; the crop
`m_typed.png` shows it. The API marks it `\inserted[typed]`, and does the same for "handy criterion for", "one or the
other of", "but only" and "cases".

**New differences.** The API reported 110 differences on the pilot pages that the check did not have
(`pilot/pilot_new_findings.tsv`). 29 of them were looked at on crops (`pilot/crops/m_*.png`): 27 are confirmed, and
the other 2 are plausible. Most of the remaining 81 are spacing before "!" or ":", commas, and handwritten symbols
merged unmarked; these were spot-checked only. Among the confirmed findings:

- Pursuing Stacks:
  - "this" is struck by hand on p. 24, and "just" on p. 170. The arXiv text prints both.
  - The typed "he" for "be" (p. 24), "ih loc. cit." (p. 337) and "do'nt" (p. 506) are silently corrected in the
    arXiv text.
  - §25 has no title on the page. The arXiv title "A tentative equivalence relation for topologists" is not in the
    typescript.
- Esquisse: the check found the Circle text close to the typescript, but on the same pages the API found more
  departures, all confirmed:
  - "est connu" → "connue", and "correspondants" → "correspondant" (p. 17);
  - "restreint" → "restreints", and "les caractéristique 2 et 5" → "caractéristiques" (p. 23);
  - "d'une notion de" omitted, and "s'est agit" → "agi" (p. 40);
  - "chapître" → "chapitre", and "van Kampen" → "Van Kampen" (p. 45);
  - "convenanble" corrected (p. 7);
  - commas added or dropped.

On the crops, no reading was found that the API introduced wrongly. The one doubtful case, "interval\xout{s}" on
p. 132, turned out to be right: the s is overtyped with x. The visible errors are the two places where it followed the
draft, plus the unmarked N.B. numbers.

**Cost of the pilot.** 275,074 input and 130,709 output tokens came to $1.86, or $0.066 a page. By text:

| Text | Cost per page |
|---|---|
| Pursuing Stacks | $0.094 |
| Esquisse | $0.052 |
| Cote 25 | $0.049 |
| Cote 24 | $0.036 |

**Verdict: passes.** Recall is above 90 %, no introduced error was seen on the crops, and the cost is at or under
$0.10 a page.

## Pages done and cost

| Batch | Batch id | Pages | Input tokens | Output tokens | Billed (batch price) |
|---|---|---|---|---|---|
| pilot | msgbatch_0189Nhf1xB615YWnztubtLfc | 28 | 275,074 | 130,709 | $1.86 |
| ps1 | msgbatch_01Rv5hCaNTtUt4JHx1yqoHPL | 190 | 1,969,085 | 1,350,890 | $17.45 |
| ps2 | msgbatch_01NVwr1Yuo8qJf5rykeGBXPK | 190 | 1,954,293 | 1,275,723 | $16.67 |
| ps3 | msgbatch_01XdFmuVVBAcgc7EFxdtCqsj | 190 | 1,953,928 | 1,240,112 | $16.31 |
| ps4 | msgbatch_012Aoc1NuskATPsyBeKSYK7J | 99 | 1,010,565 | 676,681 | $8.79 |
| esq1 | msgbatch_01LNsogFyF3y6KSp9UbtJtBk | 47 | 474,983 | 153,086 | $2.48 |
| **Total** | | **744** | | | **$63.55** (list price about $127) |

- Every request finished with `end_turn`. No page had to be sent again.
- The ledger rows in `compute_cost_ledger/LEDGER.jsonl` are `typescripts-api-pilot`, `-ps1`, `-ps2`, `-ps3`, `-ps4`
  and `-esq1`.
- The refused batch `ega25a` was not billed. It is recorded in `RUNS.jsonl`, and its unsent request file is in
  `batches/ega25a_refused_credit/`.

| Text | Pages done | Cost | Per page |
|---|---|---|---|
| Pursuing Stacks | 680 of 680 in scope | $60.24 | $0.089 |
| Esquisse (copy 1) | 58 of 58 | $3.05 | $0.053 |
| Nouveau EGA V (cote 25) | 3 of 184 | $0.15 | $0.049 |
| EGA V, Blass (cote 24) | 3 of 76 | $0.11 | $0.036 |

### Differences found

- **Pursuing Stacks:** 12,140 rows in `pursuing_stacks/DIFFERENCES.tsv`:

  | Class | Rows |
  |---|---|
  | handwriting merged unmarked | 5,419 |
  | normalization | 2,925 |
  | silent correction | 1,191 |
  | wording | 627 |
  | formula | 486 |
  | handwriting absent from the arXiv text | 463 |
  | addition | 367 |
  | omission | 334 |
  | handwriting rewritten | 144 |
  | other | 130 |
  | struck text printed | 53 |
  | unparsed | 1 |

- **`PS_ARXIV_DIFF.tsv`** (`scripts/ps_arxiv_diff.py`), as the coordinator asked: the same 12,140 rows keyed to the
  arXiv source.
  - **Columns:**
    - the arXiv file, line, end line, section (§N and its title) and paragraph within the section;
    - the arXiv text as quoted and the source text at the match;
    - the reading on the page;
    - the kind;
    - the typescript page, the page number written on the scan, and the last arXiv page marker;
    - the cote, site and PDF page;
    - how the row was located.
  - **How the rows were located:**

    | Located | Rows | Note |
    |---|---|---|
    | verbatim | 10,457 | 785 of them occur more than once in the passage; the occurrence in page order is taken, and the row says so |
    | ignoring whitespace | 1,094 | 1 of them occurs more than once; handled the same way |
    | fuzzy | 199 | |
    | by the page's reading | 49 | no arXiv text to quote |
    | not located | 341 | only the passage's line range is given; mostly handwritten margin notes absent from the arXiv text |

  - **Status:** these are the model's rows, checked by hand only on the pilot pages.
- **Esquisse:** 327 rows in `esquisse/DIFFERENCES.tsv`:

  | Class | Rows |
  |---|---|
  | normalization | 152 |
  | silent correction | 95 |
  | wording | 27 |
  | handwriting unmarked | 17 |
  | omission | 13 |
  | addition | 10 |
  | other | 8 |
  | formula | 4 |
  | handwriting missing | 1 |

  Examples:
  - "thèmes de réflexion" → "réflexions";
  - "en toutes dimensions" → "en toute dimension";
  - "pendant quelque temps" → "quelques temps";
  - "sur les corps premiers F_p" → "le corps premier";
  - "F_4 et F_5" → "F2 et F5";
  - "beaucoup plus rigides", "donc aussi" and "bien" omitted;
  - "géométrie algébrique" with "algébrique" added;
  - "Histoire de Modèles" → "Histoires";
  - "sibyllin" → "sybillin".

  The Circle text departs from the typescript far more often than the check's sample suggested.

### Combined files

- **Esquisse, cote 25, cote 24:** `<dir>_combined.tex` compiles. The Esquisse has 35 LaTeX errors where
  `$...$` is nested inside the handwriting macros in math; pdflatex recovers and writes the PDF.
- **Pursuing Stacks:** `pursuing_stacks_combined.tex` stops at scan 134-2/53, where one paragraph runs into TeX's
  limit of 100 errors from the same nesting. The per-page files are complete.
- **Unbalanced braces:** five pages of Pursuing Stacks leave braces unbalanced; the other texts have none
  (`pursuing_stacks/COMPILE_FIXES.tsv`). The combined file balances them at the edge of the page, with a comment;
  the page files are unchanged.
- **Next step:** a mechanical LaTeX clean-up is needed before the Pursuing Stacks combined file can be typeset.

## Pages for the in-app route or Pro

- **Not sent: handwritten documents.**
  - 134-1 sites 3–6: the letter "Cher Deligne".
  - 134-8 sites 42–86: about 40 pages of notes on computer listing paper, with versos.
  - 134-2 sites 145–183: handwritten letter copies, among them the French letter to Breen of 17/19 July 1975.
- **Sent, and flagged by the model as having long handwritten passages:** 18 pages, in `*/NOTES.tsv`, column
  `long_handwriting`:
  - 134-2 sites 7, 8, 10, 13, 15, 81;
  - 134-3 sites 4, 24, 81, 88;
  - 134-4 sites 44, 61, 71, 77, 79, 86;
  - 134-5 sites 2, 75.

  Sites 8, 10 and 13 of 134-2 (two contents pages and the dedication) are entirely handwritten.
- **Sent, with many doubt marks** (4 or more `\illegible`, or 12 or more `\unsure`): 53 pages of Pursuing Stacks, listed
  by `scripts/summary.py`. Most are in the letter to Quillen (134-2 sites 22–29), in faint carbon pages of 134-3 and
  134-4, and in pages with dense handwritten formulas. They should be read by eye on the scan.
- **Known errors.** Every page is AI-transcribed and not yet checked by eye. The pilot shows the residual risk: a
  struck word left live, or a misspelling normalized, where the draft does the same.

## Not done

- **Cote 25:** 181 pages, about $9 at the measured rate. **Cote 24:** 73 pages, about $3. Both stopped because the API
  credit ran out.
- **134-2 sites 115–143**, R. Brown's translation, cover note and comments: typed, not sent. Their pages can go over the
  API, at about $0.05 each.
- **Duplicates and versos** in 134-2, the Récoltes et Semailles versos, and the 134-8 folder cover (site 40): not sent.
- **p. 556:** a white box on the Montpellier scan hides most of the upper half of the page. The transcription marks
  this with a `% NOTE` and transcribes only what is visible. The hidden text needs another copy.
- **Esquisse copy 2:** its annotations (sites 78–136) were not transcribed.
- **Review:** no review by eye beyond the pilot. The `DIFFERENCES.tsv` and `PS_ARXIV_DIFF.tsv` rows outside the pilot
  are the model's.
