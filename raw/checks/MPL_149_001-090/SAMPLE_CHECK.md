# Sample check of the first pass MPL_149_001-090 (cote 149, scans 1–90)

Checked on 13 Nov 2026 by Claude Fable 5.2 (effort max), in one run with packages 4 and 6 (MPL_147_138-190,
MPL_149_091-136). This is package 5 (`packages_done/05_MPL_149_001-090`).

## Summary

- **Errors:** 0.52 per 100 words (3 in 574 words, one in 191). Misread words and symbols: 0.17. Unmarked errors:
  0.52. All three stand on one page, 045, and none carries a doubt mark: a circle he blotted out, given as live
  (`E_{K'}^\circ` at the head of the composite that defines E°_{K'}); *ainsi corrigée* for *revue et corrigée*, which
  is one misread word and one omitted word. Earlier packages: 2.15, 1.70 and 1.52 for package 3; 1.56, 1.01 and 1.46
  for package 9; 0.73, 0.55 and 0.27 for package 2.
- **The sample is four pages, half of the earlier samples of eight.** With 3 errors the 95 % range of the rate is
  0.11 to 1.5 per 100 words. The writing of cote 149 is faint on the scans, and the check used the package images, not the
  archive's PDF: small marks and faint strokes are less well covered than in the earlier checks.
- **A research note rests on one of the errors.** Note B045.4 calls the kernel definition on scan 045
  "self-referential as written", because the composite begins with E°_{K'}. In the ink the circle is blotted out:
  he corrected it himself, and the composite begins with E_{K'}.
- **Minutes per page:** GPT-6 Astra (ChatGPT Pro mode) split the 90 scans into four parallel streams of 22–23 scans
  (001–023, 024–046, 047–068, 069–090). Within a stream: 1.71 minutes per page and 1.10 per 100 words, against 1.61
  and 1.12 for package 3 and 1.83 and 1.16 for package 9. On the clock: 40.4 minutes for the 90 pages, 0.45 minutes
  per page. A different reader then audited every page; the transcription was frozen 41.8 minutes after the last
  page, and the notes took 46.7 minutes: 129.2 minutes in all (package 9: 130.8).
- **Completeness:** every scan is transcribed in full. All 90 pages start with their scan marker, the 89 pages after
  the printed cover end with the pencil number, the inventory has 1,691 rows, all `yes`, and nothing is summarized
  or skipped. The later scans are not thinner: words per unit of writing are 0.92, 1.12 and 0.97 of the package
  average over the thirds of the run, and 0.94, 1.07 and 1.00 over the thirds of each stream.
- **Checkpoints:** the checkpoint after 10 pages (`checkpoint_048`) and the fully audited one
  (`checkpoint_090`) are both consistent with the final return; the second has the same 90 pages, combined file,
  doubts register and inventory, byte for byte.
- **Verdict:** complete, and on this sample more accurate than packages 3 and 9. The errors sit on the page done
  fastest, carry no mark, and one of them changed the mathematics that a note then discussed.

## Method

Four pages were checked against the scans, one from each stream, alternating the second and the second-to-last
page of the stream: 004 (stream 1; scans 001 and 002 are the printed cover and a title sheet, so 004 is the second
page of text), 045 (stream 2, second-to-last), 048 (stream 3, second page), 089 (stream 4, second-to-last). The
earlier checks took both positions in every stream; this check covers three packages within one compute bound.

Every line of the first-pass page was compared with the two page halves from `MPL_149_001-090_scans.zip` (`img/`);
disputed places were cropped and enlarged from the same images (`img/c*.jpg`). The archive's own page images lie
outside the folders this check could read. The ink decided.

Scoring rule, kinds and word estimate as in `MPL_147_138-190_check/SAMPLE_CHECK.md` (scripts in that folder's
`tools/`; the word estimate can differ from the earlier checks' by a few per cent). `pages_checked/` holds the four
pages; 045 has the three corrections.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 045 | display after "le noyau de l'hom. composé" | `E_{K'}^\circ\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}` | the circle on this E is blotted out; the circles on the two E°_{K'} above it are open (`c045_circle_struck_vs_open.jpg`). The composite starts from E_{K'}, as the sentence requires | DI | no | medium |
| 045 | "Donc, la conjecture initiale …" | `ainsi corrigée` | `revue … corrigée`: a word of five low letters without the two dots of *ainsi* (`c045_revue_et.jpg`) | MW | no | medium |
| 045 | same place | — | `et` before *corrigée*, at the end of the line: "revue et corrigée" (`c045_revue_et.jpg`) | OM | no | high |
| 045 | "section de E_K sur …", struck | `\deleted{$\Gamma_{\mathbb Q}$, \unsure{soit}}` | a second struck word after *soit* (`c045_last_lines.jpg`) | OM | no | low |
| 048 | "Conditions équivalentes" | `Conditions` | the first letters are written over another beginning | DI | no | low |
| 048 | a), second line | `homomorphisme` | written over a shorter word | DI | no | low |
| 089 | "Une section rationnelle" | `\inserted{$f_{\unsure{K}}$}` | the subscript of the inserted f looks struck | DI | yes (the reading) | low |
| 089 | "de U_Õ sur S̃" | `sur $\widetilde S$` | a small mark before S̃ | OM | no | low |
| 089 | (28) | `E_{U_s}` | E written over another letter | DI | no | low |

Not errors: on 048 the three connectors B_V — B_U, E_V = π₁(V) — E_U = π₁(U) and V — U are written `\longrightarrow`
without a mark; the ink has dashes with a very reduced head (`c048_BV_BU.jpg`, `c048_f_EV_EU.jpg`, `c048_V_U.jpg`).
Page 004 has no discrepancy.

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 004 | 1, early | 2.45 | 113 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 045 | 2, late | 1.43 | 172 | 1 | 0 | 1 | 0 | 1 | 0 | 3 | 1.74 | 3 | 1 |
| 048 | 3, early | 1.77 | 143 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| 089 | 4, late | 3.62 | 146 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| **All** | | | **574** | **1** | **0** | **1** | **0** | **1** | **0** | **3** | **0.52** | **3** | **6** |

Streams: 1 = scans 001–023, 2 = 024–046, 3 = 047–068, 4 = 069–090. Minutes on page: the gap between this page's
"done" line in `progress.log` and the previous page's in the same stream.

Overall: 0.52 errors per 100 words (one in 191); 0.52 unmarked; misread words and symbols alone, 0.17. Early pages
(004, 048): no error in 256 words; late pages (045, 089): 3 in 318, all on 045, the page done fastest of the four
(1.43 minutes). One page per stream cannot separate stream, position and pace.

Pace by stream, from `progress.log`:

| Stream | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| 1 (001–023) | 23 | 40.4 | 1.76 | 1.20 |
| 2 (024–046) | 23 | 36.3 | 1.58 | 0.87 |
| 3 (047–068) | 22 | 37.9 | 1.72 | 1.15 |
| 4 (069–090) | 22 | 39.5 | 1.80 | 1.23 |
| All, within a stream | 90 | 154.0 | 1.71 | 1.10 |
| All, on the clock | 90 | 40.4 | 0.45 | 0.29 |

Run: start 21:56:36 UTC on 11 Nov 2026; last page 22:37:00; audits and notation reconciliation until the freeze
at 23:18:49; context opened 23:19:07; notes finished 00:05:47 on 12 Nov.

## Checkpoints

- `MPL_149_001-090_checkpoint_048_unzipped`: saved after 10 pages (001–003, 024, 025, 047, 048, 069–071; status file
  created 22:01:49 UTC, no page audited). Three of the ten pages are identical to the final return; seven were
  changed by the later audit. On 048 the audit changed one place (*lui-même* to the sign `\unsure{=|\overline m}`);
  on 025 six (among them *la* to *une*, `\xrightarrow{\sim}` to `\simeq`, and a new doubt mark `\psi|\varphi`).
- `MPL_149_001-090_checkpoint_090_unzipped`: the "fully audited frozen checkpoint" of 23:19:01 UTC. Its 90 pages,
  combined transcription, doubts register and inventory are byte-identical to the final return; its notes file is
  the state before the research phase (76,140 bytes against 196,093) and its log stops earlier.
- The log records nine checkpoints saved to the Library between 22:03 and 22:37 (`checkpoint_048` is the first of
  them) and the SHA-256 of every page at the freeze; the final return states that all 91 hashes are unchanged.

## Doubt marks and the rules added after package 3

Density: 521 `\unsure` and 4 `\illegible` in 90 pages, 5.8 per page and 3.74 per 100 words (package 3: 6.9 and
4.82). 253 carry an alternative. The doubts file opens with the shared notation table and gives every row a
confidence of its own (44 high, 270 medium, 194 low by count of the table rows).

- The four pages carry 28 `\unsure` marks (10 with an alternative). The ink decides nine, all with the first reading
  right (*rev.* and the struck primes on K on 004; the *même* sign twice on 045 and once on 048; *réguliers* on 048;
  (26), the underlined O and the *même* sign on 089). None of the three errors carries a mark.
- **Quotation marks:** ``…'' throughout, no « ».
- **One recurring sign is still handled stream by stream.** His dash-or-arrow carries a doubt mark 19 times in
  stream 1 and once in streams 2–4 together, which write the dash or the arrow without a mark (48, 38, 23 and 57
  arrow commands in the four streams). On the pages viewed the unmarked choices agree with the ink.

## Completeness

- 90 page files, each beginning with its `\scanpage` marker; the main file is their concatenation (identical up to
  white space). The 89 pages after the printed cover end with the pencil number (`\margin{N}`); 44 carry his sheet
  number (`\mspage`).
- The inventory has 1,691 rows, all `yes`, 2 to 44 per scan: 773 text blocks, 280 deletions, 276 insertions,
  156 displays, 154 margin notes, 47 diagrams, 5 drawings. The transcription has no "[...]" and no summary or
  omission note.
- On the four pages nothing larger than a token is missing; the one omission is *et* on 045.
- Words against writing ("writing" as defined in `MPL_147_138-190_check/SAMPLE_CHECK.md`; index = words per unit of
  writing divided by the package average):

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First third (001–030) | 30 | 159.3 | 0.92 |
| Middle third (031–060) | 30 | 166.7 | 1.12 |
| Last third (061–090) | 30 | 141.5 | 0.97 |
| First third of each stream | 28 | 155.0 | 0.94 |
| Middle of each stream | 30 | 165.1 | 1.07 |
| Last third of each stream | 32 | 148.0 | 1.00 |

  No thinning in the run or within a stream (r = 0.44 between words and writing over the 90 pages). The lowest
  indices belong to the printed cover (001, 0.21) and the title sheet (002, three words); after them come 065
  (0.72), 077 (0.73) and 069 (0.74), which were not viewed.

## Research notes

247 notes in 46.7 minutes, in one numbering scheme (A003.1 … D…, one letter per stream): 102 unproved claims, 45 unpursued implications, 39 own
ideas, 34 reading questions, 27 conjectures (the log's count). Each compares with a context file and scan.

Read: B045.2, B045.3, B045.4, C048.1 (four notes, on the two sampled pages with the most mathematics).

- **B045.4 rests on a first-pass error.** It reports that the composite defining E°_{K'} "itself begins with
  E°_{K'}" and asks that "the frozen display … retain its visible circle". The ink has the circle blotted out. The
  note's own comparison (`LM_140-4_text.tex`, scan 169, I_ℓ⁺ = Ker(χ_ℓ : I_ℓ → Z_ℓ*), found there as quoted) gives
  the form that he in fact wrote.
- **The other three agree with the ink:** "* à vérifier!" on the centralizer of Γ'° (B045.2); the "Conséquence
  (conjecturale)" π_K^{Γ'°} ≠ (1) (B045.3); "a un centralisateur réduit à 1" in condition b) of the "Conjecture
  fondamentale" (C048.1).
- **Context locations:** two tested, both at the stated file and scan with the stated content: `LM_140-2_text.tex`,
  scan 118 (the centralizer of every open subgroup of π reduced to 1, with his margin that it is not yet proved;
  B045.2, C048.1), and `LM_140-4_text.tex`, scan 169 (B045.4).
- **Not checked:** the mathematics of the notes, the 30 literature references (for instance Mochizuki 2004,
  Corollary 1.3.3; Mochizuki 1999, Theorem A; Stix 2012, § 5), and the other 243 notes.

## Comparison

| Package | Scans | Streams | Pages, words checked | Errors per 100 words | Misread words and symbols | Unmarked | Minutes per page within a stream |
|---|---|---|---|---|---|---|---|
| 1, MPL_1_002-050 | 3–50 | 4 | 8, 1,526 | 1.90 | 0.92 | 1.25 | 2.55 |
| 2, MPL_147_003-047 | 3–47 (45) | 1 | 8, 1,091 | 0.73 | 0.55 | 0.27 | 1.32 |
| 3, MPL_147_048-137 | 48–137 (90) | 4 | 8, 1,116 | 2.15 | 1.70 | 1.52 | 1.61 |
| 9, MPL_142_001-093 | 1–93 (90) | 4 | 8, 1,093 | 1.56 | 1.01 | 1.46 | 1.83 |
| 4, MPL_147_138-190 | 138–190 (53) | 4 | 4, 524 | 0.38 | 0.38 | 0.38 | 1.41 |
| **5, MPL_149_001-090** | 1–90 (90) | 4 | 4, 574 | **0.52** | **0.17** | **0.52** | 1.71 |
| 6, MPL_149_091-136 | 91–136 (46) | 1 | 4, 583 | 1.03 | 1.03 | 0.00 | 1.84 |

Packages 4, 5 and 6 were checked on four pages each, from the package images; packages 1–3 and 9 on eight, with
crops from the archive's PDF. The lists of low items are shorter here for that reason and should not be compared.
This package is the first of 90 scans in four streams that ran with the shared notation table and a different
auditor for every page: its audit took 41.8 minutes against 25.1 for package 9, and its sampled rate is a third of
package 9's. Four pages do not prove that the audit is the cause.

## Verdict

1. Complete: every scan in full, nothing summarized or skipped, no thinning towards the end of the run or of a
   stream. The two checkpoints agree with the final return.
2. Accuracy on the sample: 0.52 errors per 100 words, 0.17 for misread words and symbols, 0.52 unmarked (95 % range
   0.11–1.5, from four pages). All three errors stand on the page done fastest.
3. For the second pass: on 045 strike the circle in the composite and read *revue et corrigée*; withdraw or rewrite
   note B045.4; decide the six low items; and read every line, since no error carries a mark.
