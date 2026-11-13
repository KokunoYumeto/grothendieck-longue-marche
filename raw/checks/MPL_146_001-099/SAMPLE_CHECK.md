# Sample check of the first pass MPL_146_001-099 (cote 146, scans 1–99)

Checked 13 Nov 2026 by Claude Fable 5.2 (effort max). The transcription is by GPT-6 Astra (ChatGPT Pro mode).

## Summary

- **Errors:** 0.21 per 100 words on four pages: one error in 482 words (package 9, MPL_142_001-093: 1.56; package
  3: 2.15; package 2: 0.73; package 1: 1.90). Misread words and symbols: 0.21 (package 9: 1.01; 3: 1.70; 2: 0.55; 1:
  0.92). Unmarked errors: 0.21 (package 9: 1.46; 3: 1.52; 2: 0.27; 1: 1.25).
- **This figure is weak, and weaker than those of the other two packages checked today.** One error in 482 words is
  compatible with a true rate anywhere from near 0 to about 1.2 per 100 words. The sample is four pages of a
  90-page package, where the earlier checks took eight. Disputed places were enlarged from the package's own page
  images (1,685 pixels wide), not from the archive's PDF, and only three places were enlarged. One diagonal margin
  note (051, about 44 words) and the struck blocks of 051 were not read word by word and are left out of the word
  count. What the sample shows: four pages without a wrong formula, equation number or dropped line.
- **Minutes per page:** four parallel streams (001–024, 025–049, 050–073, 074–099). Within a stream: 1.24 minutes
  per page and 0.92 per 100 words, the fastest so far (package 9: 1.83 and 1.16; package 3: 1.61 and 1.12; package
  2: 1.32 and 1.06; package 1: 2.55 and 1.28). On the clock: 32.7 minutes for the 90 pages, 0.36 per page. The log
  has no audit pass: the transcription was frozen 4.4 minutes after the last page, the notes took 25.4 minutes, and
  the run 62.5 minutes in all.
- **Completeness:** all 90 supplied scans are transcribed; 89 carry their pencil number, and the one without is the
  printed cover. The inventory has 1,844 rows, all `yes`. Nothing is summarized or skipped. The pages with few
  counted words that were viewed (056, 069, 072) are complete. Nine scans (26, 35, 42, 57, 70, 76, 79, 80, 88) are
  not in the scans zip and could not be looked at.
- **Research notes:** 127 notes. One was read and recomputed (on φ_ω and p_ω, scans 048–049); it is right. The notes
  of this package are close to unchecked.
- **Verdict:** complete; no sign of trouble on four pages; the accuracy figure cannot rank this package. It is the
  fastest run and the only one of today's three without an audit pass, so it is the one that most needs the full
  eight-page check.

## Method

`progress.log` shows four streams (the "done" times of 001–024, 025–049, 050–073 and 074–099 interleave). One page
per stream was taken, by a rule fixed before any page was opened: the second page of text of streams 1 and 3 (004,
051; scans 001 and 002 are the cover and a title sheet), the second-to-last page of streams 2 and 4 (048, 098).
Every line of the first-pass page was compared with the page halves from `MPL_146_001-099_scans.zip` (unzipped to
`scans_unzipped/`, the sampled pages copied to `img/`); 098, a short page, was read from the whole page image.
Three places were enlarged (`img/c048_definir_faisant.jpg`, `img/c051_insertion_entre.jpg`). The ink decided. Scans
056, 069 and 072 were viewed for completeness (`img/c_sheet_056_069_072.jpg`).

Scoring and word count as in `MPL_142_094-122_check/SAMPLE_CHECK.md`. `pages_checked/` holds the four pages; only
051 differs from the first pass.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 048 | *permet de définir un autom* | `\unsure{d}` | the last token is a struck letter | DI | yes (the letter, not the deletion) | low |
| 048 | *en faisant opérer* | `opérer` | the ending of the word is written over | DI | no | low |
| 048 | *V ⟶ V_ω* | `V_\omega` | perhaps `V_{(ω)}`, as in the insertion above | MS | no | low |
| 051 | l. 3, insertion above the line | `\inserted{de $(P\Sigma)_x$ et $(F\wedge\omega)^*$}` | *entre (PΣ)_x et (F∧ω)\**: the word has a crossed t (`c051_insertion_entre.jpg`) | MW | no | medium |
| 051 | same insertion | placed after *l'action de ℂ\** | its guide line ends after *isom (20)*, before the struck word | PL | no | low |
| 051 | struck line before the struck diagram | `\unsure{transposant}` | begins with a dotted i, perhaps *induisant* | MW | yes | low |
| 098 | *une structure de ℰ-groupoïde* | `$\unsure{\mathcal E}$-groupoïde` | ℰ is written above a struck letter | DI | no | low |
| 098 | *Ob C′ ≝ E′* | `\unsure{E'}` | a struck token stands before E′ | DI | yes | low |

Checked and found right: *définir* on 048 (enlarged; the sense needs it); the two displays numbered (21) on 051;
the numbers (5₀), (5_I), (6), (16), (17), (20), (22).

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 004 | 1, early | 1.08 | 147 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 048 | 2, late | 1.22 | 104 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| 051 | 3, early | 1.22 | 167 (+44 not scored) | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.60 | 1 | 2 |
| 098 | 4, late | 0.72 | 64 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| **All** | | | **482** | **1** | **0** | **0** | **0** | **0** | **0** | **1** | **0.21** | **1** | **7** |

Pace by stream, from `progress.log`:

| Stream | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| 1 (001–024) | 24 | 27.5 | 1.15 | 1.01 |
| 2 (025–049) | 22 | 28.7 | 1.30 | 0.79 |
| 3 (050–073) | 22 | 32.7 | 1.48 | 1.12 |
| 4 (074–099) | 22 | 22.7 | 1.03 | 0.80 |
| All, within a stream | 90 | 111.6 | 1.24 | 0.92 |
| All, on the clock | 90 | 32.7 | 0.36 | 0.27 |

## Doubt marks and notation across streams

Package: 828 `\unsure` and 13 `\illegible` marks on 90 pages, 9.3 per page and 6.96 per 100 words (package 3: 6.9
and 4.82). Only 119 of the 828 carry an alternative (14 %; package 3: 42 %).

On the four pages the marks the ink decides are right: 𝔖_I and *ss-groupoïde* (004), *pour* and *vect.* (048),
ℰ and *discussion* (098). The marks of 051 sit in struck text and in the margin note and were not decided.

The streams differ in how they write the pencil number: `\mspage{N}` at the foot in streams 1 and 3, `\margin{N}` in
stream 2 (047–049) and elsewhere in the page file, `\mspage{N}` at the head of the file in stream 4 (098). All of it
is there; the second pass should make it one form. This run predates the shared notation table of the template.

## Completeness

- 90 page files; the main file is their concatenation. Scans 26, 35, 42, 57, 70, 76, 79, 80 and 88 are not in the
  scans zip. Package 9's check found that scans left out as blank there carried pencil numbers and short notes;
  these nine should be looked at in `146.pdf`.
- Every page except the cover (001) has a page-number marker in its file.
- The inventory has 1,844 rows, all `yes`, 2 to 60 per scan: 761 text blocks, 307 displays, 330 deletions, 145
  insertions, 108 margin notes, 70 diagrams, 123 drawings. No "[...]", no summary or omission notes; 52 diagrams in
  tikz-cd, 74 TikZ pictures.
- On the four pages nothing is missing: every block, display, margin note, insertion and deletion is present.
- Words against ink (ink: the fraction of dark pixels of each scan, measured for this check; index: words per unit
  of ink divided by the package average):

| Part | Pages | Words per page | Ink per page | Index |
|---|---|---|---|---|
| First third (001–032) | 30 | 124.9 | 0.0610 | 0.94 |
| Middle third (033–066) | 30 | 160.2 | 0.0641 | 1.15 |
| Last third (067–099) | 30 | 117.6 | 0.0606 | 0.90 |
| First third of each stream | 29 | 144.1 | 0.0649 | 1.02 |
| Middle of each stream | 32 | 144.3 | 0.0623 | 1.07 |
| Last third of each stream | 29 | 113.3 | 0.0584 | 0.89 |

  The measure is poor for this package (r = 0.53 between words and ink): cote 146 mixes handwriting with printed
  and typed sheets, and the first pass sets several typed sheets inside a rotated figure, which the word count takes
  as one object. Scans 069 and 072, at the end of stream 3, count 16 and 10 words and are in fact a typed letter and
  an examination sheet, scanned upside down and transcribed in full (their texts are in the page files). 056 is a
  title sheet of one line. So the lower index of the last thirds (0.90 and 0.89) is not evidence of thinner pages;
  with only these three low pages viewed, it is not excluded either. 058 (23 words) and 071 (50 words) were not
  viewed.

## Research notes

127 notes (numbered R001 onwards) in 25.4 minutes, with 189 context references and 11 literature references by the
log's count. The notes file opens with a section on the reliability of the supplied context, which was not read.

Read and recomputed: the note on φ_ω and p_ω (line 636 of the notes file, scans 048–049). With J = u_ω, J² = −1 and
p_ω the ℂ-linear extension of the identity V → V_(ω), as scan 048 defines it: p_ω(x − iJx) = x − J²x = 2x; the
vectors x − iJx form the +i eigenline of J; the inverse of p_ω on that line is x ↦ ½(x − iJx); and x + iJx lies in
the kernel of p_ω. All four statements of the note hold, and its quotation of 048 agrees with the ink.

One note is not a sample of 127. The notes of this package still need the check that the earlier reports gave
theirs (about 30 notes read, the mathematics recomputed).

## Verdict

1. Complete for the 90 supplied scans; the nine scans left out of the package remain to be looked at.
2. Accuracy: one error in 482 words on four pages. Nothing on these pages points to a problem, and the figure does
   not carry more than that.
3. This package ran fastest (1.24 minutes per page within a stream) and has no audit pass in its log. A full check
   of eight pages with enlargements from `146.pdf`, and of the notes, should precede any use of its rate.
