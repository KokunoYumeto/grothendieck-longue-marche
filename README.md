# Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981): transcription

A diplomatic LaTeX transcription of Grothendieck's manuscript *La Longue Marche à travers la théorie de Galois*,
made from the scans of the Université de Montpellier archive (cotes 140-1 to 140-4, 1,588 scan pages), with
research notes on the mathematics. This is an initial edition: the whole manuscript is transcribed in a first pass,
and the transcription is being checked page by page against the scans.

[Version française](README.fr.md)

## What is here

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
  mode) to research prompts on the Teichmüller tower, first-pass transcriptions of the archive's cotes 146, 147 and
  149, their reviews, the prompts with everything attached, and the scripts.

The transcription is diplomatic: Grothendieck's French, spelling, abbreviations, numbering, deletions, insertions and
margin notes as written, with doubt marked (`\unsure{a|b}`, `\illegible{n}`). Mathematics keeps his letters, indices
and arrows; diagrams are typeset with tikz-cd.

## Status (9 November 2026)

- First pass: all 1,588 scans.
- Second pass, in which every line is checked against the archive images at full resolution and collated with the
  earlier transcriptions listed below where they cover the text: cote 140-2, scans 21–30 and 101–575; cote 140-3,
  scans 1–130. The other scans (cote 140-2, scans 1–20 and 31–100; cote 140-3, scans 131–696; cotes 140-4 and 140-1)
  have the first pass only.
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
- Second pass: Claude Opus 5.5 (Anthropic), against the archive images and the earlier transcriptions.

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

## Errors

Please report errors as [issues](../../issues), with the cote and the scan number.

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights,
in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain
under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.

---

[Sponsor this work](https://github.com/sponsors/KokunoYumeto)
