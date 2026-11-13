# Sample check of the first pass MPL_147_138-190 (cote 147, scans 138–190)

Checked on 13 Nov 2026 by Claude Fable 5.2 (effort max), in one run with packages 5 and 6 (MPL_149_001-090,
MPL_149_091-136). This is package 4 (`packages_done/04_MPL_147_138-190`).

## Summary

- **Errors:** 0.38 per 100 words (2 in 524 words, one in 262). Misread words and symbols: 0.38. Unmarked errors: 0.38.
  Both errors are a plausible word in place of the ink, without a doubt mark: *entièrement* for *essentiellement*
  (139) and *implique* for *indique* (162). Earlier packages: 2.15, 1.70 and 1.52 for package 3; 1.56, 1.01 and 1.46
  for package 9; 0.73, 0.55 and 0.27 for package 2; 1.90, 0.92 and 1.25 for package 1.
- **The sample is four pages, half of the earlier samples of eight.** With 2 errors the 95 % range of the rate is
  0.05 to 1.4 per 100 words: the package is not worse than packages 3 and 9, and it may be as good as package 2;
  four pages cannot say more.
- **Minutes per page:** GPT-6 Astra (ChatGPT Pro mode) split the 53 scans into four parallel streams of 13–14 scans
  (138–150, 151–163, 164–176, 177–190). Within a stream: 1.41 minutes per page and 0.99 per 100 words, against 1.61
  and 1.12 for package 3 and 1.83 and 1.16 for package 9. On the clock: 26.8 minutes for the 53 pages, 0.51 minutes
  per page. A second reader audited every page, the transcription was frozen 13.3 minutes after the last page, and
  the notes took 30.4 minutes: 70.7 minutes in all.
- **Completeness:** every scan is transcribed in full. All 53 pages start with their scan marker and end with the
  pencil number at the foot of the page, the inventory has 904 rows, all `yes`, and nothing is summarized or
  skipped. Words per unit of writing fall from 1.17 of the package average in the first third to 0.89 in the last.
  The fall follows the content: the two pages with the fewest words for their writing (176 and 188) were read against
  the ink and are complete to the last line, and the inventory has the same number of elements per page in every
  third (16.7, 17.8, 16.6).
- **Research notes:** 136 notes, each compared with the earlier scans of cote 147 or with La Longue Marche by file
  and scan. Ten were read: their quotations agree with the ink, all five context locations tested are at the stated
  file and scan, and the one calculation recomputed holds. None rests on the two errors found.
- **Verdict:** complete, and on this sample more accurate than packages 3 and 9. The two errors carry no doubt mark,
  so the second pass still has to read every line against the scan.

## Method

Four pages were checked against the scans, one from each stream, alternating the second and the second-to-last page
of the stream (the positions of the earlier samples): 139 (stream 1, second page), 162 (stream 2, second-to-last),
165 (stream 3, second page), 189 (stream 4, second-to-last). The earlier checks took both positions in every stream;
this check covers three packages within one compute bound and takes half of that.

Every line of the first-pass page was compared with the two page halves from `MPL_147_138-190_scans.zip`
(`img/`); disputed places were cropped and enlarged from the same images (`img/c*.jpg`; margins rotated). The
earlier checks enlarged from the archive's own page images in `147.pdf`, which lie outside the folders this check
could read; the package images are 1,691 pixels wide, enough for words and signs, less for small marks. The ink
decided. Scans 176 and 188 were read whole for completeness (`img/whole_176_188.jpg`).

Scoring rule, as for packages 1–3 and 9: the error rates count discrepancies of high and medium confidence; low ones
are listed in the same table and counted separately. Words: prose words, struck text included, plus one word per
formula and one more per relation sign or comma in it. The script of the earlier checks is not in their folders;
the rule was written out again (`tools/wc_tex.py`). On the checked pages of the earlier packages it gives 1,066
words against 1,116 (package 3), 1,121 against 1,091 (package 2) and 1,222 against 1,093 (package 9), so word
counts here can differ from the earlier ones by a few per cent. `pages_checked/` holds the four pages with the two
errors corrected.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 139 | last paragraph, after (233) | `est de nature entièrement trivial` | `essentiellemt trivial`: after the crossed t a dotted i and two tall loops (ll), no accent (`c139_nature_trivial.jpg`) | MW | no | high |
| 139 | "On donnera la … construction" | `la` | *la* or *le*, one written over the other | DI | no | low |
| 162 | l. 7, "(ce qui … qu'on se borne" | `ce qui implique qu'on` | `ce qui indique qu'on`: no p below the line before the tall letter; *implicitement* and *simpliciales* on this page and *implique* on 189 have it (`c162_indique_zoom.jpg`, `c162_implicitement_compare.jpg`, `c189_implique_donc.jpg`) | MW | no | medium |
| 162 | end of l. 13 | `Avec` | *Avec* stands on a horizontal stroke: struck, or written over a dash (`c162_avec.jpg`) | DI | no | low |
| 162 | margin, before *à l'inclusion* | — | a short token before *l'inclusion* (`c162_margin_rot.jpg`) | OM | no | low |
| 162 | foot of the page | `\deleted{\unsure{indépendamment}}` | a mark (⊥ or L) after the struck word (`c162_bottom_struck.jpg`) | OM | no | low |
| 165 | (268), under I'_1 | `aux facteurs $\mathbb C^*$` | the letter is written over another, probably ℂ over 𝔻 (`c165_factors.jpg`) | DI | no | low |
| 165 | margin | ``` ``partition'' \unsure{sens généralisé} ``` | a short token (*au* or *en*) after "partition" (`c165_margin_rot.jpg`) | OM | no | low |
| 165 | (267) | `\prod_{i\in I}` | ∏ written over another sign (`c165_267.jpg`) | DI | no | low |
| 189 | before "une application finie étale" | `\unsure{est}` | *est* with a stroke through the whole word, probably struck (`c189_est.jpg`) | DI | yes (the reading, not the deletion) | low |
| 189 | "le fait que les … strates" | `les \deleted{\unsure{diff.}}` | *les* also carries a stroke (`c189_les_strates.jpg`) | DI | no | low |
| 189 | chain of arrows under "suite de flèches" | first segment a dash without head | the first segment has a small head like the others (`c189_arrows.jpg`) | MS | no | low |

Not errors: (233) has `\Pi_1P_{D'^{*}}` with one prime in the ink too (`c139_233_essentiellement.jpg`), although the
composite of (231) and (232) starts from D''*; note 138-03 records it. `\unsure{donc|bien}` on 189 is not decidable:
his *donc* two lines above has the same tall first stroke (`c189_bien.jpg`).

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 139 | 1, early | 0.68 | 97 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1.03 | 1 | 1 |
| 162 | 2, late | 0.83 | 183 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.55 | 1 | 3 |
| 165 | 3, early | 1.20 | 110 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| 189 | 4, late | 3.37 | 134 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| **All** | | | **524** | **2** | **0** | **0** | **0** | **0** | **0** | **2** | **0.38** | **2** | **10** |

Streams: 1 = scans 138–150, 2 = 151–163, 3 = 164–176, 4 = 177–190. Minutes on page: the gap between this page's
"done" line in `progress.log` and the previous page's in the same stream.

Overall: 0.38 errors per 100 words (one in 262), all of them misread words, all unmarked. Early pages (139, 165):
1 error in 207 words; late pages (162, 189): 1 in 317. The two errors stand on the two pages done fastest (0.68 and
0.83 minutes); the two slower pages have none. One page per stream cannot separate stream, position and pace.

Pace by stream, from `progress.log`:

| Stream | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| 1 (138–150) | 13 | 13.1 | 1.01 | 0.54 |
| 2 (151–163) | 13 | 15.8 | 1.21 | 0.81 |
| 3 (164–176) | 13 | 19.0 | 1.46 | 1.33 |
| 4 (177–190) | 14 | 26.8 | 1.92 | 1.50 |
| All, within a stream | 53 | 74.7 | 1.41 | 0.99 |
| All, on the clock | 53 | 26.8 | 0.51 | 0.35 |

Run: start 14:19:56 UTC; last page 14:46:46; independent audit of every page until the freeze at 15:00:04; context
opened 15:00:13; notes finished 15:30:35 (11 Nov 2026).

## Doubt marks

Density: 390 `\unsure` and 1 `\illegible` in 53 pages, 7.4 per page and 5.17 per 100 words (package 3: 6.9 and 4.82).
72 carry an alternative. The doubts register has 392 rows, each with a confidence of its own (238 medium, 154 low).

The four pages carry 22 `\unsure` marks (6 with an alternative). The ink decides eight, and in all eight the first
reading is right (*correspondraient* 162; *correspondre*, *sens généralisé* 165; *ordonné*, *est*, *rev.*, *soient*,
*donc* 189). Fourteen are not decidable from these images, seven of them in struck text. Neither error carries a
mark: as in package 9, the marks are right where the ink decides them and absent where the errors are.

## Completeness

- 53 page files, each beginning with its `\scanpage` marker; the main file is their concatenation (identical up to
  white space, 86,130 against 86,078 characters). All 53 pages end with the pencil number at the foot (`\margin{N}`,
  scan − 1); 27 carry his own sheet number (`\mspage`).
- The inventory has 904 rows, all `yes`, 8 to 31 per scan: 303 text blocks, 226 deletions, 112 insertions,
  103 displays, 96 margin notes, 55 diagrams, 9 drawings. The transcription has no "[...]", no summary or omission
  note, and no « ».
- On the four pages nothing larger than a token is missing: every block, display, margin note, insertion and
  deletion is present and in the order of the page.
- Words against writing. The earlier checks used the ink fraction in `packages_work/…/MANIFEST.json`, outside the
  folders of this check; here "writing" is the share of pixels at least 22 grey levels darker than their blurred
  surroundings (`tools/ink2.py`), which does not depend on how dark the pen is. Index = words per unit of writing
  divided by the package average.

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First third (138–154) | 17 | 182.1 | 1.17 |
| Middle third (155–172) | 18 | 125.2 | 0.92 |
| Last third (173–190) | 18 | 123.1 | 0.89 |
| First third of each stream | 16 | 169.9 | 1.15 |
| Middle of each stream | 17 | 135.9 | 0.98 |
| Last third of each stream | 20 | 126.8 | 0.89 |

  The later pages have fewer words for their writing, in the run and within a stream, and words follow the writing
  only loosely (r = 0.38). The pages with the lowest index are 176 (0.53), 188 (0.59), 178 (0.65), 149 (0.66) and
  183 (0.68). Scans 176 and 188 were read against the ink: both are complete to the last line ("Retenons cependant
  la" on 176; "définis de façon évidente" on 188) and consist of large displays, the boxed (294) and the bracketed
  (303). The inventory has 16.7, 17.8 and 16.6 elements per page in the three thirds. The fall is the content
  (scans 138–154 are dense prose), not thinning. Scans 178, 149 and 183 were not viewed.

## Research notes

136 notes, written in 30.4 minutes after the freeze, in two header formats (kind in the header up to scan 176, in a
"Kind" line from 177 on). Each note says what the page adds to, restates from or differs from a named context file
and scan.

Read: 138-01, 138-02, 138-03, 151-30, 151-31, 164-03, 164-04, 164-29, 188-02, 189-01 (ten notes, covering the four
sampled pages and scans 176 and 188).

- **Quotations agree with the ink** in the eight notes on viewed pages: "morphisme canonique (dit 'de
  générisation')" (139), "les op. … de dégénérescence sont des iso" and "compléter implicitement" (162), "On
  s'attend" and "partitions possibles" (165), "homéomorphie (heuristique !)" (176), "premier sommet" and the finite
  étale claims (189). Note 138-03 records exactly what the ink has in (233): one prime on the source, and
  P_{D'} → P_{D''} in the prose.
- **Context locations:** five tested, all at the stated file and scan: "non-formel" (`ARCH_147_003-137_text.tex`,
  scan 133; 138-02); the torsor and H(J) (scans 109–110; 164-04); the branches through x (scan 106; 164-03, where
  "Boolean lattice" is the note's word, not the page's); "image inverse" (scan 129; 189-01); "topos mixte"
  (`LM_140-2_text.tex`, scan 163; 188-02).
- **Mathematics:** 188-02 (own idea) recomputed and right: for P¹ with strata C and {∞} the space of non-strict
  local flags of length 0 is S² ⨿ {∞}, with one non-identity arrow at ∞; its nerve is S² with an interval attached
  and retracts to S², while the two-object incidence category gives an interval.
- **Not checked:** the 15 literature references (for instance Lurie 2009, Theorem 4.1.3.1; Deligne 1989,
  §§ 15.3–15.7), and the other 126 notes.
- **Wrong claims:** none found. No note read rests on *entièrement* or *implique*.

## Comparison

| Package | Scans | Streams | Pages, words checked | Errors per 100 words | Misread words and symbols | Unmarked | Minutes per page within a stream |
|---|---|---|---|---|---|---|---|
| 1, MPL_1_002-050 | 3–50 | 4 | 8, 1,526 | 1.90 | 0.92 | 1.25 | 2.55 |
| 2, MPL_147_003-047 | 3–47 (45) | 1 | 8, 1,091 | 0.73 | 0.55 | 0.27 | 1.32 |
| 3, MPL_147_048-137 | 48–137 (90) | 4 | 8, 1,116 | 2.15 | 1.70 | 1.52 | 1.61 |
| 9, MPL_142_001-093 | 1–93 (90) | 4 | 8, 1,093 | 1.56 | 1.01 | 1.46 | 1.83 |
| **4, MPL_147_138-190** | 138–190 (53) | 4 | 4, 524 | **0.38** | **0.38** | **0.38** | 1.41 |
| 5, MPL_149_001-090 | 1–90 (90) | 4 | 4, 574 | 0.52 | 0.17 | 0.52 | 1.71 |
| 6, MPL_149_091-136 | 91–136 (46) | 1 | 4, 583 | 1.03 | 1.03 | 0.00 | 1.84 |

Packages 4, 5 and 6 were checked on four pages each, from the package images; packages 1–3 and 9 on eight, with
crops from the archive's PDF. The lists of low items are shorter here for that reason and should not be compared.
No recurring sign is written differently by different streams on the pages viewed, and the package has no « »;
the exclamation-mark exponent of scans 048–128 does not occur on the six pages viewed and is nowhere written `^!` in
this package, which the second pass should confirm against the ink.

## Verdict

1. Complete: every scan in full, nothing summarized or skipped. Fewer words per unit of writing on the later pages
   come from large displays, checked on the two thinnest pages.
2. Accuracy on the sample: 0.38 errors per 100 words, all misread words without a mark (95 % range 0.05–1.4, from
   four pages). Not worse than packages 3 and 9; possibly as good as package 2.
3. For the second pass: correct *essentiellement* (139) and *indique* (162); decide the ten low items, most of them
   overwritten letters and strokes through *est*, *les* and *Avec*; and read every line, since the errors carry no
   mark.
