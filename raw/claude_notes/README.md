# La Longue Marche: packages for ChatGPT Pro

160 packages of ten scan pages each cover the whole manuscript from the Montpellier archive: cote 140-2 (manuscript
pages 1–292, 575 scans), cote 140-3 (pages 293–650, 696 scans), cote 140-4 (pages 650bis–787, 280 scans) and the
draft cote 140-1 (37 scans). [PACKAGES.md](PACKAGES.md) lists each package with its archive file and scan range.

- LM_P01–LM_P10 (cote 140-2, scans 1–100): the pilot, prompt version 1.
- LM_P011–LM_P160: prompt version 2 ([PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md)), which adds a section on the typical
  misreadings found in the pilot and names the archive file. A landscape spread, if any, comes as two images
  (left and right sheet).

The images are contrast-enhanced and sharpened; the archive's header band is cut off.

## Running a package

1. Open a new ChatGPT Pro chat.
2. Open the package folder (e.g. `LM_P011`), select everything in it (the prompt and the page images), drag it into
   the chat, and write "Follow the attached prompt."
3. Pro returns one zip, `LM_P011.zip` (the transcription and the notes). Save it in `answers`.
4. Next package.

## What happens after

Every answer gets a second pass by Claude: each line is checked against the archive's own images at full resolution,
and each scan is collated with the partial transcriptions by others (the CSG draft, Carmona's edition,
Carmona–Künzer's typeset 207 pages, the Grothendieck Circle's table of contents). The prompts never give Pro those
transcriptions, so its reading stays blind. See [METHODOLOGY.md](METHODOLOGY.md).

Each answer also ends with research notes: Grothendieck's own conjectures and questions, claims he leaves without
proof, implications he does not pursue on those pages, and Pro's own ideas (labelled as such). They are collected in
`NOTES_LEDGER.md` and checked against the later pages of the manuscript and the literature; the ones still worth
pursuing go on.
