# Sample check of the first pass MPL_8_079-081+9+4+100 (cotes 8, 9, 4 and 100)

Checked on 13 Nov 2026 by Claude Fable 5.2 (effort max). This is package 33
(`packages/33_MPL_8_079-081+9+4+100`): cote 8 scans 79–81, cote 9 scans 1–29, cote 4 scans 1–12, cote 100 scans
1–53 without scan 47; 96 pages.

## Summary

- **Errors:** 0.10 per 100 words (2 in 1,916 words, one in 958). Misread words and symbols: 0.05. Unmarked errors:
  0.10. Both errors stand on one handwritten page (cote 100, scan 7) and carry no doubt mark: *dépt de base* for
  *chgt de base*, and the double quotes around "est" left out. On the five handwritten pages alone (1,007 words)
  the rates are 0.20, 0.10 and 0.20; the three typed pages (909 words) have no error. Earlier packages: 0.38 to
  1.03 for packages 4–6 (four pages each), 1.56 for package 9, 2.15 for package 3, 0.73 for package 2.
- **Range:** with 2 errors on eight pages the 95 % range is 0.01 to 0.38 per 100 words for the package and 0.02 to
  0.72 for its handwriting. This is the most accurate package checked so far, also on handwriting alone.
- **Time: 226.1 minutes, of which 151.5 for the first reading of the 96 pages in one stream.** Per page the run was
  not slow: 1.58 minutes per page and 0.76 per 100 words, the fastest per word of all packages checked. Package 5
  spent the same work, 154.0 stream-minutes for 90 pages, in four parallel streams and 40.4 minutes of clock. The
  rest: a second reading of every page (45.3 minutes), the comparison of recurring signs and the freeze (8.7), and
  closing work (20.2). The notes were written along with the pages and have no phase of their own.
- **Completeness:** every supplied scan is transcribed in full. The 96 page files are in order and the main file is
  their concatenation; every page except the three printed covers records the pencil number at its foot; the
  inventory has 1,914 rows, all `yes`; nothing is summarized or skipped. The later pages are not thinner: words
  per unit of writing are 0.85, 0.99 and 1.14 of the package average over the thirds of the run.
- **Research notes:** 349 notes of 36 to 96 words. Those read quote the page correctly and name what it leaves
  unproved; they carry no calculation, no literature and no comparison with other manuscripts (the package has no
  context zip). They are thinner than the notes of packages 4–6.
- **Verdict:** complete and accurate; the one-stream run with a second reading of every page costs clock time and
  gives the lowest error rate so far.

## Method

Eight pages were checked against the scans. `progress.log` shows one stream (the "done" times follow the page
order), so the pages were taken by position in the run of 96, as for package 2: the second page, the
second-to-last, and six in between at steps of about twelve: cote 8 scan 080 (position 2), cote 9 scans 011 and
023 (14, 26), cote 4 scan 006 (38), cote 100 scans 007, 018, 031 and 052 (51, 62, 75, 95). They were fixed before the
pages were seen. Five are handwritten; three are typed: 9/011 and 4/006 are his typescript with handwritten
corrections, 100/018 is a reused typed sheet (a list of corrections to the proofs of EGA IV, struck through). Typed
sheets are about a third of the package (22 reused sheets, the 11 pages of cote 4, a few pages of cote 9).

Every line of the first-pass page was compared with the two page halves from the scans zip (`img/`); places in doubt
were enlarged from the same images (`img/c*.jpg`; the margins rotated), and four further passages of the handwritten
pages were enlarged for a second look without finding anything. The archive's own page images lie outside the folders
of this check. The ink decided. Scan 9/005 was read whole for completeness (`img/whole_9_005.jpg`).

Scoring rule, kinds and word estimate as in `MPL_147_138-190_check/SAMPLE_CHECK.md` (scripts in that folder's
`tools/`, and `tools/stats33.py` here). `pages_checked/` holds the eight pages; 100/007 has the two corrections.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 100/007 | "Elle devient effective après …" | `après dépt de base $S_0\hookrightarrow S$` | `après chgt de base`: c and h joined, g below the line, t; no accent (`c100_007_chgt_zoom.jpg`). Note 170 of the return itself says "after base change" | MW | no | medium |
| 100/007 | "Son image inverse sur S'_0 …" | `est un vrai schéma abélien` | `"est" un vrai`: double quotes before and after *est* (`c100_007_est_quotes_zoom.jpg`) | OM | no | medium |
| 100/007 | inserted line "On peut supposer … affine" | `On peut supposer $S$ affine` | a struck A before *affine* (`c100_007_on_peut_supposer.jpg`) | DI | no | low |
| 8/080 | "si S est de car. p>0" | `$S$` | S written over another letter | DI | no | low |
| 8/080 | second display, first line | `(M\otimes_{\mathbb Z}\mathbb F_p)` | this F has no double stroke; the F in the subscripts has | MS | no | low |
| 9/011 | struck typed lines 2–4 | — | a dashed line drawn under the struck words "algébriquement clos …" | OM | no | low |
| 9/011 | "de monodromie s'il admet" | `s'il` | one typed letter is struck over | DI | no | low |
| 9/023 | first exact sequence | last connector a dash | the last connector has a head | MS | no | low |
| 4/006 | "… de sorte qu'on trouve (oubli dans 8.3 !)" | `\margin{\uline{(oubli dans 8.3!)}}` | typed in the running line, at the end of the struck passage | PL | no | low |
| 4/006 | "En admettant lesingrédients" | `lesingrédients` | a stroke by hand separates *les* and *ingrédients* | OM | no | low |
| 4/006 | margin note | `(\unsure{utilis.}$\to$8.1?)` | the end may be `8.1.7)` (`c4_006_margin_rot.jpg`) | MS | partly | low |
| 100/018 | "une suite O_X-régulirère" | `régulirère` | one typed letter is struck over; which letters remain is a guess | MW | no | low |
| 100/031 | (i), "complété formel le long de A_s" | `le` | *le* written over another word (`c100_031_le_long.jpg`) | DI | no | low |
| 100/031 | "un trait T_1" | `un trait` | a short struck token before *trait* (`c100_031_dem_1.jpg`) | OM | no | low |
| 100/031 | margin NB | `se borner \uline{aux} $x\in S$` | x seems written at the end of one line and again at the start of the next (`c100_031_margin_NB.jpg`) | OM | no | low |
| 100/052 | "Soit Z_n = …" | `\operatorname{Cent}` | perhaps `Centr.` | MW | no | low |

Not errors: the label `\unsure{(2.1)|(2.2)}` on 8/080 is not decidable from the ink (`c8_080_label_22.jpg`); (2.2')
follows, so the alternative is the likely one. Pages 8/080, 9/011, 9/023, 4/006, 100/018, 100/031 and 100/052 have
no counted discrepancy.

## Per page

| Scan | Position, kind | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8/080 | 2, handwritten | 0.97 | 140 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| 9/011 | 14, typed with corrections | 0.98 | 331 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| 9/023 | 26, handwritten | 0.62 | 114 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| 4/006 | 38, typed with corrections | 2.18 | 292 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| 100/007 | 51, handwritten | 1.70 | 288 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 0.69 | 2 | 1 |
| 100/018 | 62, typed, reused sheet | 0.92 | 286 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| 100/031 | 75, handwritten | 4.33 | 257 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| 100/052 | 95, handwritten | 1.72 | 208 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| **All** | | | **1,916** | **1** | **0** | **1** | **0** | **0** | **0** | **2** | **0.10** | **2** | **14** |
| Handwritten | 5 pages | | 1,007 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 0.20 | 2 | 8 |
| Typed | 3 pages | | 909 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 6 |

Minutes on page: the gap between this page's "done" line in `progress.log` and the previous page's.

First half of the run (positions 2–38): no error in 877 words; second half (51–95): 2 in 1,039, both on 100/007.
The page that took longest (100/031, 4.33 minutes, 26 doubt marks) has no error. Accuracy does not fall towards the
end of the run.

## Time

| Phase | UTC, 13 Nov 2026 | Minutes | Share |
|---|---|---|---|
| First reading, 96 pages in one stream, notes written alongside | 00:45:58 – 03:17:29 | 151.5 | 67 % |
| Second reading of every page ("audited") | 03:17:53 – 04:03:14 | 45.3 | 20 % |
| Recurring signs compared against the ink, LaTeX compiled, freeze | – 04:11:55 | 8.7 | 4 % |
| Notes reviewed against the frozen pages, ten research questions added | – 04:18:30 | 6.6 | 3 % |
| Inventory put in source order, sheet kinds reviewed | – 04:28:31 | 10.0 | 4 % |
| Final verification, hashes, ZIP | – 04:32:05 | 3.6 | 2 % |
| **All** | | **226.1** | |

First reading by cote and by kind of sheet:

| Part | Pages | Words per page | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|---|
| Cote 8 | 3 | 149.3 | 3.9 | 1.29 | 0.87 |
| Cote 9 | 29 | 146.6 | 38.5 | 1.33 | 0.91 |
| Cote 4 | 12 | 280.7 | 23.4 | 1.95 | 0.69 |
| Cote 100 | 52 | 229.8 | 85.7 | 1.65 | 0.72 |
| All | 96 | 208.5 | 151.5 | 1.58 | 0.76 |
| of which his notes (`text`) | 64 | 226.2 | 115.0 | 1.80 | 0.79 |
| reused typed sheets | 22 | 224.1 | 27.9 | 1.27 | 0.57 |
| covers | 8 | 46.1 | 3.3 | 0.41 | |
| cancelled drafts | 2 | 122.0 | 5.3 | 2.65 | |

What took the time:

- **One stream.** The 151.5 minutes of the first reading are the sum that other packages spread over four streams:
  package 5 needed 154.0 stream-minutes for 90 pages and 40.4 minutes on the clock. Run the same way, this package's
  first reading would have taken about 40 minutes and the whole run about 115.
- **More text per page.** 208 words per page against 143 to 156 in packages 4–6; 20,018 words in all against 14,028
  for package 5. Per 100 words the first reading took 0.76 minutes, against 0.99 to 1.27 for packages 4–6.
- **A full second reading.** 45.3 minutes, 0.47 per page, in page order, with four pauses of about three minutes (at
  9/005, 4/009, 100/022 and 100/043). Package 5's audit took 41.8 minutes for 90 pages with several readers.
- **Reused sheets.** 27.9 minutes of the first reading (18 %) and a quarter of the words went to the 22 typed sheets
  whose backs he reused: unrelated typescript, here for instance corrections to the proofs of EGA IV.
- **No separate notes phase.** The notes file already had 117,900 of its 128,615 bytes at the checkpoint taken
  during the second reading; after the freeze the notes took 6.6 minutes.

## Checkpoint 053

`MPL_8_079-081+9+4+100_checkpoint_053_unzipped` was saved at 03:49:59 UTC, 184 minutes into the run, while the
second reading had reached cote 100 scan 021. It holds all 96 pages. 29 are identical to the final return; 67 were
changed later, in 1 to 23 places each. On the sampled pages: 100/018 and 100/052 are unchanged; 8/080
(`\mathbf F_p` to `\mathbb F_p`), 9/011, 9/023, 4/006 and 100/007 (the `&` of diagrams) changed in notation only,
after their second reading; 100/031, read a second time after the checkpoint, changed in nine places (the margin notes
rebuilt as figures, *aux* underlined, a struck *des* recorded, two `\illegible` replaced by doubtful readings).
Notes, doubts register and inventory were still growing (55,054 against 59,898 bytes for the doubts; 143,385
against 174,507 for the inventory). The log records eleven checkpoints saved to the Library.

## Doubt marks

Density: 821 `\unsure` and 28 `\illegible` in 96 pages, 8.8 per page and 4.24 per 100 words (package 6: 8.8 and
6.08; package 5: 5.8 and 3.74). 158 carry an alternative; the register has 849 entries. The eight pages carry 83
`\unsure` marks (15 with an alternative), 46 of them on 100/007 and 100/031. Where the ink decides a mark on these
pages the first reading is right (for instance *églt*, the *même* sign, *algébrique*, *montre*, the struck typed
words on 9/011); most of the others sit in struck text or are his ξ-or-ζ (seven marks on 8/080), which these images
do not decide. Neither error carries a mark.

## Completeness

- 96 page files in the order of the prompt; four begin with a `\cotefile` line, all carry their `\scanpage` marker;
  the main file is their concatenation (identical up to white space, 193,551 against 193,456 characters).
- **Page numbers.** Every page except the three printed covers (scan 001 of cotes 9, 4 and 100) records the pencil
  number at its foot (scan − 1), 90 of them as the last line. This package writes it `\mspage{N}`, the macro the
  prompt reserves for his own page or sheet number, and uses the same macro for his own numbers (the circled 3 on
  100/007); packages 3–6 wrote the pencil number `\margin{N}`. The second pass should separate the two.
- The inventory has 1,914 rows, all `yes`, 2 to 43 per scan: 676 text blocks, 510 deletions, 282 insertions,
  165 displays, 97 margin notes, 95 drawings, 89 diagrams; by kind of sheet 1,543 rows on his notes, 296 on reused
  typed sheets, 44 on cancelled drafts, 31 on covers. The transcription has no "[...]", no summary or omission note
  and no « ».
- On the eight pages nothing larger than a pair of quotation marks is missing.
- Words against writing ("writing" as defined in `MPL_147_138-190_check/SAMPLE_CHECK.md`):

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First third (8/079 – 9/029) | 32 | 146.9 | 0.85 |
| Middle third (4/001 – 100/020) | 32 | 242.2 | 0.99 |
| Last third (100/021 – 100/053) | 32 | 236.5 | 1.14 |
| His notes only, first third | 21 | 175.3 | 0.87 |
| His notes only, middle | 21 | 262.2 | 0.96 |
| His notes only, last third | 22 | 240.3 | 1.18 |

  The index rises through the run. The lowest values belong to the covers; the lowest page of notes is 9/005
  (0.33), a landscape sheet of formulas, which was read against the ink and is complete, down to the last line
  "φ_n(Fz) = φ_n(zF) =".
- **Scan 47 of cote 100** was left out of the package as blank. The archive's PDF lies outside the folders of this
  check, so this was not verified; in package 9 three scans left out as blank carried pencil numbers and short notes.

## Research notes

349 notes: 136 unproved claims, 78 reading questions, 61 own ideas, 46 conjectures, 28 unpursued implications;
36 to 96 words each, 55 at the median. The file states that no outside mathematics or literature was used; it has
no references and, the package having no context zip, no comparison with La Longue Marche or other cotes.

Read: the notes on 8/080 (3–5), 9/023 (70–73), 100/007 (168–172) and 100/052 (339–343), seventeen notes.

- **Quotations agree with the ink:** the struck hypothesis "si … O_S est plat sur Λ (p.ex. n=p)" (4); "cette
  dualité est compatible avec filtrations", "il y aurait lieu d'expliciter la structure d'extension", the cancelled
  *fonctoriel* (70–72); "Foncteur ess. surjectif", "(réf … !!!)", "le critère de Raynaud" (168–170); "à dégager un
  lemme", the cancelled second case and "K parfait" (341–342).
- **None rests on an error found here.** Note 170 reads the passage of 100/007 as "after base change to S_0", the
  sense of the ink, where the page file has *dépt*.
- **Descriptive, not mathematical.** Each note says what the page asserts and what would have to be proved; the
  "own ideas" are questions for later work (for instance 5 and 73, which link 8/080 and 9/023 to cote 100 scans 37
  and 3). None of the seventeen carries out a calculation, a test or a construction, and none cites a source. The
  notes of packages 4–6 did (context locations by file and scan, literature, recomputed examples).

## Comparison

| Package | Scans | Streams | Pages, words checked | Errors per 100 words | Misread words and symbols | Unmarked | Minutes per page within a stream | Run, minutes |
|---|---|---|---|---|---|---|---|---|
| 1, MPL_1_002-050 | 3–50 | 4 | 8, 1,526 | 1.90 | 0.92 | 1.25 | 2.55 | |
| 2, MPL_147_003-047 | 45 | 1 | 8, 1,091 | 0.73 | 0.55 | 0.27 | 1.32 | 98 |
| 3, MPL_147_048-137 | 90 | 4 | 8, 1,116 | 2.15 | 1.70 | 1.52 | 1.61 | 101.5 |
| 9, MPL_142_001-093 | 90 | 4 | 8, 1,093 | 1.56 | 1.01 | 1.46 | 1.83 | 130.8 |
| 4, MPL_147_138-190 | 53 | 4 | 4, 524 | 0.38 | 0.38 | 0.38 | 1.41 | 70.7 |
| 5, MPL_149_001-090 | 90 | 4 | 4, 574 | 0.52 | 0.17 | 0.52 | 1.71 | 129.2 |
| 6, MPL_149_091-136 | 46 | 1 | 4, 583 | 1.03 | 1.03 | 0.00 | 1.84 | not on record |
| **33, MPL_8_079-081+9+4+100** | 96 | 1 | 8, 1,916 | **0.10** | **0.05** | **0.10** | 1.58 | 226.1 |
| 33, handwriting only | | | 5, 1,007 | 0.20 | 0.10 | 0.20 | | |

Packages 4–6 and 33 were checked from the package images; packages 1–3 and 9 with crops from the archive's PDF.
The lists of low items are shorter here for that reason and should not be compared. Two things differ from the
earlier packages and both favour accuracy: the hand of these cotes (ink, dated by the archive from 1958 to about
1971) is easier than the faint writing of cote 149, and the run was one stream followed by a second reading of every page and a comparison of recurring signs.
This sample cannot separate the two.

## Verdict

1. Complete: every supplied scan in full, nothing summarized or skipped, no thinning towards the end of the run.
2. Accuracy on the sample: 0.10 errors per 100 words, 0.20 on the handwritten pages, both errors unmarked and on
   one page (95 % range 0.01–0.38, and 0.02–0.72 for handwriting).
3. Time: 226.1 minutes, two thirds of it a single-stream first reading at an ordinary pace per page and the fastest
   pace per word; a fifth the second reading.
4. For the second pass: on 100/007 read *chgt de base* and put *est* in quotes; decide the fourteen low items;
   separate the pencil numbers from his own page numbers; check scan 47 of cote 100 in the PDF. The research notes
   are an index of open points, not yet mathematics.
