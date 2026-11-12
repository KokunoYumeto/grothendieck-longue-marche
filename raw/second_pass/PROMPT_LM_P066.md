# Second pass: check a first-pass transcription of *La Longue Marche à travers la théorie de Galois* against the scans

You check and correct a diplomatic LaTeX transcription of Grothendieck's manuscript (Montpellier archive, cote
140-3), made blind by another model from contrast-enhanced images. Its error rate is about 1.5 % of words, mostly
fluent misreadings that put a plausible mathematical word where the ink says something else ("fonctorielle" for
*tangentielle*, "propres" for *quasi-*), dropped conditions ("S ≠ ∅") and dropped symbols (an inclusion ∩ in a
display). Only about a third of its errors carry a doubt mark. Your pass must find them.

Package: LM_P066, scans 71–80.

This first pass already includes targeted fixes of described diagrams and illegible marks (redrawn in tikz-cd/TikZ); check them like everything else.

Inputs (all paths under `C:\Users\user\Documents\longue_marche_pro_pilot_20261104`):
- First pass: answers\fixed\LM_P066_transcription.tex (its `\scanpage{N}` lines mark the scans).
- Its notes: answers\unzipped\LM_P066\LM_P066_notes.md.
- Images at the archive's own resolution, in `second_pass\img_140-3`: `scanNNN.jpg` (the whole page) and `scanNNN_a.jpg`,
  `scanNNN_b.jpg` (top and bottom halves, or left and right pages of a spread). Read the two halves of every scan.
  Where a word is hard, crop and enlarge it (PIL, into `second_pass\work_LM_P066`), rotate margin notes.
- Other transcriptions, as text, in `second_pass\witness` (search them with Grep for a distinctive word of the
  passage): `CSG_G103d_draft_2026-02.txt` (the closest, a normalised reading edition), `IUT_galoisI_historical_witness.txt`,
  `Carmona_Kuenzer_207page_historical_witness.txt` (more errors, e.g. ≤ for ≥), `Grothendieck_Circle_tableLM.txt`
  (a later table of contents by the author). They come from one group and normalise: they expand abbreviations,
  regularise punctuation and drop deletions and insertions. They are evidence, never authority: the ink decides. They may not cover these scans (search before relying on them); where none does, the ink alone decides.

Method:
1. Go through the first pass scan by scan, line by line, with the image halves. Compare every word, abbreviation,
   symbol, index, sign, inequality, arrow, parenthesis, underline, deletion, insertion and margin note.
2. Collate each scan with the witnesses: find the passage in the CSG draft (and the IUT text where CSG lacks it) and
   look at every place where a witness differs from the first pass beyond normalisation. Settle each one on the image.
3. Also look for what both may have missed: words, conditions or symbols on the page that neither text has.
4. Correct the transcription where the image settles it. Keep the first pass's diplomatic conventions (its macros
   `\scanpage`, `\mspage`, `\margin`, `\deleted`, `\inserted`, `\uline`, `\unsure{a|b}`, `\illegible{n}`, `\diagram`),
   Grothendieck's spelling, accents, abbreviations and numbering. Never expand, modernise or complete. Where the ink
   does not settle a reading, keep or add `\unsure{...}` with the alternatives; do not guess.

Work economically: read each scan's two halves once and settle what you can from them; make an enlarged crop only
for a place where the first pass, a witness and your reading of the half still disagree, or a symbol decides the
mathematics. Aim at no more than about 120 tool calls for the package. Write each output file once, at the end.

Write:
- `second_pass\LM_P066_checked.tex`: the corrected transcription (the whole package).
- `second_pass\LM_P066_changes.md`: one table row per change: scan, place, first-pass reading, corrected reading,
  evidence (what the image shows; which witness agrees or differs), confidence (high/medium/low). Then a short list
  of places still unresolved, and the witnesses' own errors that you noticed (scan, witness, reading, ink).
- `second_pass\LM_P066_notes_checked.md`: the first pass's research notes (Grothendieck's conjectures and questions,
  claims without proof, implications not pursued, the model's own ideas), each checked against the corrected text:
  keep, correct or drop it, with a reason; add your own notes of the same kinds, labelled as yours. Give each note the
  scan number, its kind and one to four sentences.

Final message, short: counts (changes by confidence, unresolved places), and the consequential corrections (those that
change the mathematics) one per line. Nothing else.
