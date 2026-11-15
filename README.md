# Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981): transcription

A diplomatic LaTeX transcription of Grothendieck's manuscript *La Longue Marche à travers la théorie de Galois*,
made from the scans of the Université de Montpellier archive (cotes 140-1 to 140-4, 1,588 scan pages), with
research notes on the mathematics. This is an initial edition: the whole manuscript is transcribed in a first pass,
and the transcription is being checked page by page against the scans.

[Version française](README.fr.md)

## Which book to read (typeset readers, working draft)

*La Longue Marche* comes here in seven books, all made from one checked French transcription and one checked English translation. **Start with the English reading text** (`LM_EN_reading.pdf`), or the French one (`LM_FR_texte_de_lecture.pdf`) if you read French.

- **Reading texts** (`LM_EN_reading.pdf`, `LM_FR_texte_de_lecture.pdf`): Grothendieck's final text, in English or in French, for reading the mathematics.
- **French diplomatic** (`LM_FR_diplomatique.pdf`): the manuscript as it is, scan by scan, with his deletions, insertions, doubtful readings and illegible marks shown as they stand, for checking against the archive.
- **Corrected text with apparatus** (`LM_FR_corrige_apparat.pdf`, `LM_EN_corrected_apparatus.pdf`): his final text with every change he made to it listed at the end of each scan, for anyone who wants to see how the text was revised. An apparatus entry records one change: what stood first and what replaced it.
- **Annotated masters** (`LM_FR_master_annotated.pdf`, `LM_EN_master_annotated.pdf`): the editors' copies from which each language's books are printed. As PDFs they show the corrected text with the apparatus, so most readers do not need them.

## What is here

- **Typeset readers, working draft (14 November 2026)**: five readers and two annotated masters, French and English
  (diplomatic, corrected with apparatus, reading text), under
  [Releases](../../releases/tag/lm-readers-working-draft-2026-11-14). The text is settled; the typesetting is still
  being finished, and a finished edition will replace them.
- **Draft readers**, one PDF per archive file, under [Releases](../../releases): cote 140-2 (manuscript pages 1–292),
  140-3 (pages 293–650), 140-4 (pages 650bis–787) and 140-1 (a draft). Each part uses the best text available;
  [reader/READER_SOURCES.md](reader/READER_SOURCES.md) says which.
- `transcription/`: the LaTeX of each package of scans (10, 19 or 20 scans), by cote.
  - `*_first_pass.tex`: the first pass as returned.
  - `*_first_pass_fixed.tex`: the first pass after targeted repairs (diagrams and illegible marks redone, or LaTeX
    markup repaired so that it compiles).
  - `*_checked.tex` and `*_changes.md`: the text after the second pass, and the table of every change with the
    evidence and a confidence.
- `notes/`: for each package, the first pass's apparatus (doubts, abbreviations, legibility) and its research notes:
  Grothendieck's own conjectures and questions, claims he leaves without proof, implications he does not pursue,
  and the models' own ideas, labelled as such. `*_notes_checked.md`: the same notes checked against the corrected
  text (kept, corrected or dropped, with reasons).
- [notes/RESEARCH_TOPICS.md](notes/RESEARCH_TOPICS.md): an initial map of the manuscript's topics and of the
  questions Grothendieck leaves open, with scan references.
- `methodology/`: how the transcription is made, the prompts used, the list of packages and the coverage.
- [`raw/`](raw/README.md): raw research outputs, not edited for publication: answers of GPT-6 Astra (ChatGPT Pro
  mode) to research prompts on *La Longue Marche* (its group schemes, the equation of loops, the Teichmüller tower),
  first-pass transcriptions of the archive's cotes 146, 147 and
  149, their reviews, the prompts with everything attached, and the scripts.
- [`raw/planning/montpellier_archive/`](raw/planning/montpellier_archive/README.md): the working plans of the Montpellier archive work (plans, war games, cost and usage records), not results.

The transcription is diplomatic: Grothendieck's French, spelling, abbreviations, numbering, deletions, insertions and
margin notes as written, with doubt marked (`\unsure{a|b}`, `\illegible{n}`). Mathematics keeps his letters, indices
and arrows; diagrams are typeset with tikz-cd.

## English translation

An English translation of the whole manuscript: all 245 units of the transcription, 1,588 scans.

- **A draft reader**, one PDF: `La_Longue_Marche_English.pdf`, under [Releases](../../releases)
  (English translation, 13 November 2026). Its LaTeX source is
  [reader/LaLongueMarche_English.tex](reader/LaLongueMarche_English.tex). It is a draft: the packages set one
  after another, with provisional typesetting (a wide formula or diagram is reduced or turned on its side, a long
  marginal note is set in the text block). A typeset reader will replace it.
- `translation/en/`: the English of each package of scans, as LaTeX (116 files).
- [methodology/translation_en/](methodology/translation_en/README.md): how it was translated and checked, with the
  prompts, the scripts, the checks (every fix and every waiver) and the run reports.

It translates the checked transcription with its marks: deletions, insertions, marginal notes, underlining, doubtful
and illegible readings. The formulas are the transcription's, character for character. Terms follow one glossary for
the whole manuscript, built on Grothendieck's own English (*Pursuing Stacks*) and on the English *Sketch of a
Programme*.

In the draft readers (the English one and the four French ones), every doubtful reading (blue), every `[illeg. n]` and
every `[scan n]` is a link: it opens that scan in the viewer of the Grothendieck archive of the Université de
Montpellier, so that you can look at the handwriting yourself.

AI-translated by GPT-6.1 Sol (OpenAI, reasoning effort max, API Flex tier) from the AI-transcribed French text (transcription by GPT-6 Astra, ChatGPT Pro mode, checked by Claude Opus 5.5 (effort not recorded)); prompts, checks, fixes and build by Claude (Anthropic).

The rights in the original work belong to its author or the author's representatives or heirs. Our transcription, translation, corrections and typesetting were produced by AI. They have no human author and, in our understanding, are not protected by copyright; where any right of ours exists nonetheless, it is dedicated to the public domain under CC0 1.0. All of this work reproduces or translates Grothendieck's text, whose rights belong to his heirs, so nothing here licenses or authorizes any reproduction, translation or other use of his work. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.

## Status (12 November 2026)

- First pass: all 1,588 scans.
- Second pass, in which every line is checked against the archive images at full resolution and collated with the
  earlier transcriptions listed below where they cover the text: all 1,588 scans (116 packages, cotes 140-1 to
  140-4), with 4,890 changes to the first pass and 3,636 places left unresolved and marked. The draft readers of
  13 November hold it for all four cotes. The edition's `transcription/` and `notes/` hold it for cote 140-2, scans
  21–30 and 101–575, and cote 140-3, scans 1–130; the rest is under [`raw/`](raw/README.md) (section "Second passes") until the next
  release.
- The earlier transcriptions cover the first part of the manuscript (§§ 1–37, cote 140-2). For cote 140-3 they offer
  only the section titles of the table of contents, so the images alone decide the reading.
- In the checked packages, the second pass changed the first pass's reading at about 2 places in every 100 words
  (counting the changes made with high or medium confidence), and about half of those places carried no doubt mark.
  Expect errors of that kind in the packages not yet checked. Places that the images do not settle stay marked.

## How it was made

The transcription, corrections, typesetting and notes are AI-produced.

- First pass: ChatGPT Pro (OpenAI), one package of scans at a time, from contrast-enhanced images, with no access to
  any other transcription. Package 57 (cote 140-2, scans 561–570) was transcribed through the OpenAI API (GPT-6
  Astra) as a test.
- Second pass: Claude Opus 5.5 (Anthropic, effort not recorded), against the archive images and the earlier transcriptions.

Details, measured error rates and costs are in [methodology/METHODOLOGY.md](methodology/METHODOLOGY.md).

## Sources and earlier work

- The scans: Université de Montpellier, Institut Montpelliérain Alexander Grothendieck,
  [archives Grothendieck](https://grothendieck.umontpellier.fr/archives-grothendieck/), cotes 140-1 (37 scans), 140-2
  (575), 140-3 (696) and 140-4 (280).
- Earlier transcriptions, consulted in the second pass as witnesses and not reproduced here:
  - Mateo Carmona's edition of the first part, transcribed from the typescript, and the typeset text deciphered and
    transcribed by Mateo Carmona with the collaboration of Matthias Künzer
    ([agrothendieck.github.io](https://agrothendieck.github.io/));
  - the draft edition of the Centre for Grothendieckian Studies (Grothendieck Institute, Mondovì), February 2026;
  - the table of contents compiled by Grothendieck himself, as published by the Grothendieck Circle.

  These texts read many passages differently from the ink here and there, and so do we; each disagreement is decided
  on the scan. The `*_changes.md` tables record where a witness agrees or differs.

## Weigh in

AI models are following up the mathematical leads in this material. Claude Fable 5.2 and Claude Opus 5.5 (effort max)
read the texts, check the results and write the next questions; GPT-6 Astra (ChatGPT Pro mode) proves and computes.
The results are published here as they come in.

If you work on these topics and want something taken into account (a reference, a known result, an error, an
objection, a direction worth pursuing or one to drop), please open an [issue](../../issues). Issues are read and go
into the next round of work, with credit to you.

## Errors

Please report errors as [issues](../../issues), with the cote and the scan number.

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Our transcription, translation, corrections and typesetting were produced by AI. They have no human author and, in our understanding, are not protected by copyright; where any right of ours exists nonetheless, it is dedicated to the public domain under CC0 1.0. All of this work reproduces or translates Grothendieck's text, whose rights belong to his heirs, so nothing here licenses or authorizes any reproduction, translation or other use of his work. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.

**Prompts and method.** The prompts, templates, scripts and working method published here are dedicated to the public domain under CC0 1.0. If you want to do similar work, use them freely; we claim no rights in them.

## Rights considerations

**Grothendieck's texts.** The rights belong to his heirs; his texts are protected until the end of 2084. The University
of Montpellier publishes the scans of his mathematical papers (https://grothendieck.umontpellier.fr/archives-grothendieck/) with his heirs' agreement. We hold no licence
from his heirs and claim no rights in his texts.

**Earlier editions and transcriptions.** Others have edited or transcribed parts of these papers before us:
- *Les Dérivateurs*: the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis (https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html);
- *La Longue Marche à travers la théorie de Galois*: tome 1, edited by J. Malgoire (Université Montpellier II, 1995),
  and the transcriptions by M. Carmona with M. Künzer (https://agrothendieck.github.io/);
- *Pursuing Stacks*: M. Carmona's transcription (https://arxiv.org/abs/2111.01000), which he dedicated to the public domain under CC0, and
  G. Maltsiniotis's edition *À la poursuite des champs*, vol. I (SMF, 2022);
- the transcriptions of the Centre for Grothendieckian Studies (https://csg.igrothendieck.org/), which states that it publishes them with the
  consent of the rights holders.

Apart from that statement, none of these says it holds a licence from the heirs, and a transcription gives its maker no
rights in the author's text. We do the same work with AI for the whole archive: to make all of it available as editable
LaTeX, with translations, and as a second reading beside the existing ones. This is no claim of priority or
superiority, and no claim to rights we do not hold. If the editors of an earlier edition would rather we took down what
we based on their work, so that theirs stands alone, we will do so as a courtesy.

**Works with an authorized edition.** Where a work has an edition published with the rights holders' authorization, as
*Récoltes et Semailles* has (Gallimard, 2022), we do not reproduce or translate it; at most we write our own commentary
on its mathematics.

**Texts by others.** We transcribe or translate other people's texts only where the rights holders, or the institution
that holds the texts, have made them publicly available for study. Examples are Daniel Quillen's notebooks, which the
Clay Mathematics Institute has digitized and made available to the mathematical community (https://www.claymath.org/online-resources/quillen-notebooks/), and the Séminaire
Bourbaki exposés and Bourbaki drafts that Grothendieck reused or kept among his own notes, which the University
publishes as part of his papers. This is our good-faith reading, not a claim of rights. If you hold rights in any of
this and object, please open a GitHub issue and we will take it down.

---

[Sponsor this work](https://github.com/sponsors/KokunoYumeto)
