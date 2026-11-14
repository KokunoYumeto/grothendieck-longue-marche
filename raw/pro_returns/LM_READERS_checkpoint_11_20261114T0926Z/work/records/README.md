# La Longue Marche: readers, annotated masters and audit records

Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981). Edition prepared 13 November 2026 from the supplied checked French transcription and English translation.

This release contains five readers and two annotated masters. Each book is supplied as a single LuaLaTeX source and its PDF. The sources of record are the 116 French package texts in `fr/texts/` and the 116 English package texts in `en/packages/`. No archive image was reinterpreted and no conjectural manuscript reading was introduced.

## Files and forms

| Archive | Source and matching PDF | Form |
|---|---|---|
| `LM_READERS_FR.zip` | `LM_FR_diplomatique.tex` | Checked diplomatic transcription: authorial cancellations in grey, insertions in teal, original notation and manuscript page numbers, doubtful readings in blue, illegibility in red. |
| `LM_READERS_FR.zip` | `LM_FR_corrige_apparat.tex` | French final authorial state, with integrated insertions and a scan-end apparatus giving each original reading, resulting state, kind and reason. |
| `LM_READERS_FR.zip` | `LM_FR_texte_de_lecture.tex` | French corrected running text without the variant apparatus. Scan and manuscript page numbers appear in the margin. Original uncertainty in cancelled material remains visible in explicitly labelled residual-doubt blocks. |
| `LM_READERS_FR.zip` | `LM_FR_master_annotated.tex` | Complete French annotated master, compiled in the corrected-with-apparatus form. |
| `LM_READERS_EN.zip` | `LM_EN_corrected_apparatus.tex` | Checked English translation of the same corrected authorial state, with the corresponding English apparatus and the one recorded glossary correction. |
| `LM_READERS_EN.zip` | `LM_EN_reading.tex` | English corrected reading form, with the same treatment of page numbers and residual uncertainty as the French reading form. |
| `LM_READERS_EN.zip` | `LM_EN_master_annotated.tex` | Complete English annotated master, compiled in the corrected-with-apparatus form. |
| `LM_READERS_RECORDS.zip` | Records, scripts, provenance and verification outputs | Source coverage, change logs, exact typesetting changes, glossary audit, footer inventory, build evidence and attributed visual inspection records. |

The annotated masters are usable single-file books. Their body is also the body of every reader in the same language. A form selector changes which branches print; independently edited reader bodies are not maintained. Every source declares its common-body SHA-256 immediately before that body. `MASTER_INTEGRITY.md` verifies the declared hash against the actual text and independently reconstructs that text from the checked packages and recorded transformations.

## Coverage and source identity

| Cote | Manuscript extent | Scan count |
|---|---|---:|
| 140-1 | Draft | 37 |
| 140-2 | Manuscript pages 1–292 | 575 |
| 140-3 | Manuscript pages 293–650 | 696 |
| 140-4 | Manuscript pages 650bis–787 | 280 |
| **Total** | **116 packages** | **1,588** |

The English unit manifest contains **245 translation units**. Exact unit reassembly is checked against both the French package texts and the checked English package texts. The source hashes are checked against the supplied ZIP manifests before processing. Processing normalizes line endings from CRLF to LF where necessary; the immutable byte hashes and the text-stage hashes are reported separately.

Each language contains **1,588 source scan marks, 17,117 source `\unsure` occurrences and 1,261 source `\illegible` occurrences**. These are logical source counts. They are not the number of literal macro calls in an annotated master or the number of PDF annotations: alternate branches, apparatus copies, inherited uncertainty and passages occupying several lines produce different quantities. The audit keeps source marks, literal master occurrences, selected executed source IDs, TeX measurement expansions and PDF link rectangles separate.

`SOURCE_INTEGRITY.md`, `SOURCE_SCAN_MARKS.tsv`, `SOURCE_UNIT_ASSEMBLY.tsv` and `MASTER_INTEGRITY.md` give the detailed coverage and reconstruction evidence. All French and English authorial variant IDs agree in sequence.

## Editorial construction

Each effective authorial revision is encoded in the common body as:

```tex
\var{manuscript reading}{corrected reading}{kind}{stable source id}
```

Identifiers combine cote, scan, kind and ordinal, for example `140-2-s314-D001`. The original branch retains the complete cancellation or insertion, including nested marks; recorded mechanical and layout changes may occur inside it. The change logs and inverse patches preserve the exact raw-source reading. The corrected branch omits cancelled wording or integrates inserted wording. The apparatus prints at the end of the corresponding scan; it does not use TeX footnotes.

There are **10,888 effective authorial variants per language: 6,702 deletions and 4,186 insertions**. A further **380 source revisions per language occur wholly inside an enclosing cancellation**. Their original text and nested marks remain in that cancellation's manuscript reading; they are not printed again as separate effective changes. No unsupported slip correction has been added.

| Cote | Deletions | Insertions | Authorial variants |
|---|---:|---:|---:|
| 140-1 | 144 | 31 | 175 |
| 140-2 | 2,239 | 1,755 | 3,994 |
| 140-3 | 3,134 | 1,755 | 4,889 |
| 140-4 | 1,185 | 645 | 1,830 |
| **Total** | **6,702** | **4,186** | **10,888** |

The English has one additional, explicitly identified glossary variant, for **10,889 total textual entries**. `CHANGES_FR.tsv` and `CHANGES_EN.tsv` retain source-reading strings from the checked package texts before layout wrappers are added. Every row has a kind and reason. Exact staged reversal verifies that editorial annotation and link instrumentation can recover their input texts.

### Doubt and illegibility in cancellations

Removing a cancellation must not erase the transcriber's uncertainty. In apparatus forms the original cancellation, including its doubts and illegibility, is printed in the apparatus. The reading forms preserve the exact doubtful fragments in residual-doubt blocks associated with their stable variant IDs. There are **4,969 such cancellation rows per language**. These retained source fragments are the declared exception to omitting the apparatus; they do not add a new reading or commentary.

Some deletions occur entirely inside an enclosing `\unsure`. There are **110 such cases per language**, including 12 that also contain explicit internal doubt marks. The full inherited uncertain fragment is preserved once, with nested uncertainty retained, and a linked dagger anchors the cancellation. Nonprinting metadata prevents the inherited and internal structures from generating duplicate visible daggers.

The marginal-note policy measures each note at the specified margin width. Notes of at most three lines that fit stay in the margin. Longer notes use a ruled, labelled, breakable text block. Notes encountered inside mathematics or a box are queued with a visible source reference, preserving the original mathematical or textual mode. Measurement repetitions reuse stable source IDs rather than creating duplicate notes. `MARGINAL_NOTE_CONTEXTS.tsv` records the source-context audit.

### Glossary

`GLOSSARY_INCONSISTENCIES.md` and `GLOSSARY_CONCORDANCE.tsv` record the audit against the supplied translation glossary. The sole unambiguous correction is in `en/packages/LM_P030_en.tex`, cote 140-2, scan 296: **“structure with loops” → “loop structure”**, matching the unmarked French abbreviation and the supplied glossary. Its stable ID is `EN-GLOSS-140-2-296-001`. Mathematical notation, authorial changes and uncertainty marks are unaffected. Variations not supported as clear slips are documented without imposing a new interpretation.

## Archive footers

**237 paired source footer occurrences** are inventoried: 129 in cote 140-3 and 108 in cote 140-4. Of these, 180 were active source text and 57 were already commented out. The institutional archive URL and postal-address line are omitted uniformly from every printed form. The author's manuscript page number is retained. At all inventoried places that number was already independently marked immediately before the footer, so it prints once from that marker. The exact original footer remains recoverable from the annotated source metadata. `ARCHIVE_FOOTERS.tsv` lists each occurrence and what each reader prints.

## Typesetting and fonts

The build applies mechanical TeX repairs only to the 21 packages identified by the supplied `en/COMPILE.tsv`. These yield 2,055 recorded mechanical replacements per language. The repairs reproduce the supplied repair logic and are exactly reversible; they do not reinterpret mathematics. `MECHANICAL_FIXES.tsv` records them.

Further layout repairs are attached to identified source sites and applied to the corresponding French and English constructions. The records distinguish changes to diagram spacing, labels, line breaks, cancelled empty cells, boxed text and source-local placement. There is no blanket diagram-scaling pass. Three diagrams are placed on landscape pages, with a notice at their original positions; one overlong running-text formula is displayed with a location mark. The apparatus forms include the four separately identified layout notices requested in the brief. Those notices are typographic explanations, not extra manuscript readings.

`TYPESETTING_FIXES.tsv`, `LAYOUT_REPAIR_DETAILS.tsv`, the exact-patch JSON files and `TYPESETTING_REPORT.md` record the source locations, reasons, before/after changes and verification. Exact raw UTF-8 byte spans are checked against the original attached source bytes, including their original line endings.

The books use Latin Modern Roman, Latin Modern Math and the standard TeX Live STIX Two fonts. STIX Two Math supplies the two diagonal mathematical glyphs selected in the preamble, and STIX Two Text covers the Cyrillic characters occurring in the source. The source `\boldsymbol{\Gamma}` command appears 65 times per language. The legacy bold-math route selected an ordinary Gamma because no matching bold Unicode math version existed. A consistent macro definition using `\symbf` restores the intended bold upright Gamma while leaving every source command unchanged. A compiled glyph comparison verifies the regular U+0393 versus bold U+1D6AA distinction; all 130 sites are listed in `FONT_REPAIRS.tsv`.

A remaining `OMS/LatinModernRoman(0)/m/n` substitution warning can arise from the legacy circle component used by source `\textcircled`. The standard fallback circle glyph is present. This warning is distinguished from missing characters and from the corrected loss of bold Gamma. Actual warning messages and counts, including moved-margin and underfull-box diagnostics, belong to each book's final log summary below and in `TYPESETTING_REPORT.md`; they are not silently suppressed. The preamble sets `\hfuzz=0pt` and `\vfuzz=0pt`.

## Scan links

Every printed doubtful reading, illegibility marker and scan mark links to its cote and scan using:

```text
https://grothendieck.umontpellier.fr/web/viewer.html?file=../<cote>.pdf#page=<scan>
```

The source instrumentation assigns each literal marked occurrence a stable `M` identifier. A macro expanded repeatedly during mathematical measurement retains one identity. The PDF annotations record their covered marker IDs, including nested marks. Verification reconstructs every marker's link runs, target and physical-page set independently from the PDF and compares them with the LuaLaTeX trace. It also checks that the exact set of executed IDs matches the selected edition branches. A proof of scan coverage alone is not substituted for this per-marker check.

## Compiling a delivered book

Use a standard, fully installed TeX Live with LuaLaTeX and its ordinary packages/fonts. No source fragments, images, external Lua files or attached archives are needed to compile an individual delivered `.tex` file. The Lua code is embedded. Shell escape is unnecessary.

From the directory containing the source, run LuaLaTeX twice, replacing the filename for another form:

```bash
lualatex --no-shell-escape -interaction=nonstopmode -halt-on-error LM_FR_corrige_apparat.tex
lualatex --no-shell-escape -interaction=nonstopmode -halt-on-error LM_FR_corrige_apparat.tex
```

The first pass establishes the contents data; the second resolves its page references. Compilation also writes the normal log and auxiliary files, plus `.lm-links.tsv` and `.lm-scans.tsv` audit sidecars. Those sidecars are outputs, not input dependencies.

The preamble uses the standard packages `geometry`, `fontspec`, `amsmath`, `amssymb`, `mathtools`, `unicode-math`, `ulem`, `graphicx`, `xcolor`, `tikz`, `tikz-cd`, `pdflscape`, `needspace`, `newunicodechar`, `luacode`, `xurl` and `hyperref`.

## Rebuilding from the supplied archives

Extract `LM_READERS_RECORDS.zip` into a working directory. Extract the TeX and PDF files from both language ZIPs into its `work/build/` directory when rerunning verification without a rebuild. Run `python work/scripts/restore_image_aliases.py` to recreate any selected-page image duplicates represented by the digest-backed alias inventory. The full-page PNGs contain the visual evidence; `verify_pdf.py --render` regenerates contact and overview sheets. Curated repair evidence is included at both `proofs/visual_repairs/` and `work/visual_repair_proofs/`, preserving the historical archive links and the original project paths with byte-identical copies.

The project scripts use the relative `sources/` and `work/` structure. Keep that structure when using the reproducibility bundle. The original `LM_FR.zip`, `LM_EN.zip` and `LM_TYPESET.zip` are the inputs; no reconstructed package is substituted for a source of record.

```bash
python work/scripts/restore_inputs.py LM_FR.zip LM_EN.zip LM_TYPESET.zip
python work/scripts/source_integrity.py
python work/scripts/build_frozen_release.py --jobs 2
python work/scripts/verify_sources.py --stage build
python work/scripts/record_generated_heading_repairs.py
python work/scripts/assemble_records.py
python work/scripts/verify_pdf.py work/build/LM_FR_corrige_apparat.pdf --render
```

Run the last command for each of the seven PDFs. The source and layout data shipped with the scripts supply the recorded decisions. `editorial.py`, `mechanical_repairs.py`, `layout_repairs.py` and `instrument_marks.py` implement the stages; `book_preamble.tex` and `book_links.lua` supply the common rendering and link implementation before being embedded in each generated book. `texenv.py` uses a normal TeX installation when the optional local recovery runtime is absent. `bootstrap_tex.py` documents recovery of incomplete TeX environments; a normal full TeX Live installation does not require it.

`verify_sources.py` verifies immutable source hashes, unit reconstruction, every mechanical/layout stage, exact editorial projection, raw-source change-log readings, shared bodies, instrumentation and per-form executed marker IDs. `verify_pdf.py` checks logs, every page's painted ink bounds and every scan-link annotation. `audit_margin_collisions.py` adds a targeted search for overlapping separate text lines in the marginal-note column; candidates are inspected visually. This additional check found the duplicated short-note collision at scan 140-2:344 and prompted the recorded source-local repair preserving both notes.

The visual workflow is deliberately separate from rendering. `review_pages.py` records supplied observations only after inspection of the corresponding image. Every row is bound to the PDF SHA-256, PNG-file SHA-256 and decoded RGB-pixel SHA-256. A rebuilt page retains an existing review only if its pixels and image file are identical. `compare_pdf_pixels.py` can transfer a completed review from an apparatus reader to its master only after comparing the actual page images; different title pages are inspected separately. `VERIFICATION_METHOD.md` explains the bounds, links, page selection and evidence rules.

## Final build and inspection status

**PROVISIONAL — NOT A FINISHED RELEASE.**

| PDF | Pages | LaTeX errors | Warnings | Overfull boxes / widest pt | Missing characters | Outside sheet / permitted area | Archive links | Scans linked | Reviewed / required pages |
|---|---|---|---|---|---|---|---|---|---|
| LM_FR_diplomatique.pdf | 865 | 0 | 40 | 0 / 0 | 0 | 0 / 0 | 20113 | 1588 | 477 / 477 |
| LM_FR_corrige_apparat.pdf | 1533 | 0 | 50 | 0 / 0 | 0 | 0 / 0 | 21449 | 1588 | 676 / 676 |
| LM_FR_texte_de_lecture.pdf | 949 | 0 | 910 | 0 / 0 | 0 | 0 / 0 | 25087 | 1588 | 494 / 494 |
| LM_EN_corrected_apparatus.pdf | 1540 | 0 | 48 | 0 / 0 | 0 | 0 / 0 | 21484 | 1588 | 684 / 684 |
| LM_EN_reading.pdf | 956 | 0 | 904 | 0 / 0 | 0 | 0 / 0 | 25137 | 1588 | 499 / 499 |
| LM_FR_master_annotated.pdf | 1533 | 0 | 50 | 0 / 0 | 0 | 0 / 0 | 21449 | 1588 | 1 / 676 |
| LM_EN_master_annotated.pdf | 1540 | 0 | 48 | 0 / 0 | 0 | 0 / 0 | 21484 | 1588 | 1 / 684 |

`TYPESETTING_REPORT.md` gives before/after measurements, complete page-specific visual observations and warning interpretation. `LATEX_WARNINGS.tsv` and `logs/` retain the complete warnings and sanitized logs. `CHECKPOINT_RETENTION.tsv` explains every checkpoint entry retained or superseded.

Unfinished conditions are listed explicitly in the report; this checkpoint is not a final publication.

## Credits, sources and rights

The archive scans are held by the Université de Montpellier, Institut Montpelliérain Alexander Grothendieck, cotes 140-1 through 140-4. The front matter retains every human contribution named in `records/README_published.md`: Mateo Carmona's edition of the first part from the typescript; the deciphered and transcribed typeset text by Mateo Carmona with Matthias Künzer; the Centre for Grothendieckian Studies (Grothendieck Institute, Mondovì) draft edition of February 2026; and Grothendieck's own table of contents published by the Grothendieck Circle. Those earlier transcriptions were consulted as witnesses during the checked transcription's second pass and are not reproduced here.

The required credit lines are retained:

- AI-transcribed by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checked against the scans by Claude Opus 5.5 (Anthropic).
- AI-translated by GPT-6.1 Sol (OpenAI, reasoning effort max, API Flex tier); prompts, checks and fixes by Claude (Anthropic).
- this edition built by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

The English translation credit appears in the English books. Earlier glossary contributions by Claude Opus 5.5 and Claude Fable 5.2 are also credited. `CREDITS_AUDIT.md` records the provenance of these statements.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.

The full rights statement appears in each book's language. This build does not itself publish a GitHub repository. All source references in the delivered records are archive-relative or project-relative; no private machine path or email address is part of the edition.
