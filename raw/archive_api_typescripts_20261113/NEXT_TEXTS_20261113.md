# The next typescripts for the API: ready to submit

13 November 2026. Prepared by Claude Opus 5.5 at effort high (sub-agent of the main session; no sub-agents of its own).
No API call was made, no key was read and nothing was submitted. The main session submits.

## What was done

- Every scan of the cotes in scope was looked at on contact sheets, with larger crops where a page was unclear:
  - 134-2, sites 108–147;
  - 129, 162-5 and 119, every scan;
  - 10, 12, 15 and 37, every scan.
  
  Each scan's class was checked against `MANIFEST.csv`, `PLACEMENT_EVERYTHING.csv`, `SECTIONS_STATE.md`, the blank-scan
  list of 12 Nov and the Pro package plan. The result is in `TYPED_INVENTORY_20261113.tsv`, with one row per scan
  (1,215 rows). Its columns are:
  - cote;
  - site;
  - PDF page;
  - typed / handwritten / printed / blank / cover;
  - what the scan is;
  - route;
  - how it was read.
- `scripts/next_texts_20261113.py` writes the inventory, appends the new pages to `PAGES.json` (363 pages, each with a
  `doc` field), and writes the drafts to `alignment/drafts/`. Its alignment table is
  `alignment/ALIGNMENT_next_texts_20261113.tsv`. The script starts from the backup, so it can be run again.
- `scripts/batch.py` has new material:
  - TEXT_CONTEXT paragraphs for the five texts;
  - DOC_CONTEXT, one paragraph per document, which gives each offprint's bibliographic data and the instruction on
    annotations;
  - DRAFT_CONTEXT for `esq119` and `brown`;
  - the sommaire and typescript-page phrase for copy 2.

  When a batch mixes in the new texts, its ledger row names the new project.
- `scripts/parse.py`: output folders and names for the new texts; DIFFERENCES.tsv for `brown` and `esq119`.
- `scripts/prep_images.py`: the PDF paths of 129 and 162-5. The images (`work/img/<key>_a.jpg`, `_b.jpg`, 726 files)
  were made in the same form as before. Log: `work/prep_images_next_texts_20261113.log`.
- Backups:
  - `work/PAGES_before_next_texts_20261113.json`;
  - `work/batch_before_next_texts_20261113.py`;
  - `work/parse_before_next_texts_20261113.py`;
  - `work/prep_images_before_next_texts_20261113.py`.
- Pilot pages: `PILOT_NEXT_20261113.json` (15 pages).

## The texts

Site = PDF page − 1. Blank sheets are left out everywhere.

### `brown`: R. Brown's documents in 134-2 (26 pages)

Typed pages:
- site 115: Brown's cover note;
- sites 117–120: his "Comments", with references;
- sites 122–126: his translation of the letter to L. Breen of 17/2/1975;
- sites 128–143: his translation of an extract from the letter of 17–19 July 1975.

Left out:
- the blank sheets at sites 116, 121 and 144;
- site 127, the back of a sheet of listing paper.

**Draft for sites 128–143.** Grothendieck reprinted Brown's July translation in the appendix of Pursuing Stacks
(arXiv 2111.01000 v2, `ps1.tex` lines 1380–1647). He wrote there that he "correct[ed] some inaccuracies" and added the
subtitles 9–18 and his notes. That text is given as the draft. Each page's passage was found from its Tesseract OCR by
word 3-grams, as align.py does it (6.4k characters a page on average). The DIFFERENCES will therefore list
Grothendieck's 1983 corrections together with the editors' normalizations.

Sites 115–126 have no draft. The French original of the February letter is in the appendix, but not in English.

Context paragraph (with the July document's paragraph):
> This page is from archive cote 134-2 (the folder of chapter I of Pursuing Stacks, 1983), site page {site} (PDF page
> {pdf}): typed English documents of R. Brown (Bangor) that Grothendieck kept with the typescript. It is from Brown's
> English translation, "prepared with assistance from L. Breen and J.-L. Loday", of an extract from Grothendieck's
> handwritten letter to L. Breen of 17-19 July 1975. Grothendieck reprinted this translation in the appendix of
> Pursuing Stacks (1983), "correcting some inaccuracies" and adding subtitles and notes. The handwriting on the page may
> be Grothendieck's or another hand's.

The other documents end with "No draft is given for this text: transcribe the page." The draft paragraph is in
`batch.py`, DRAFT_CONTEXT["brown"].

Pilot pages:
- `brown_134-2_118`: the Comments, with a diagram;
- `brown_134-2_124`: the February letter, dense formulas;
- `brown_134-2_130`: the July letter, formulas, with the draft.

### `mtl129`: the Montréal seminar notes, cote 129 (74 pages)

Typed pages, sites 1–75 except the blank site 14. All are annotated typescript copies:
- 1–13: chapter I, "Préliminaires sur Witt";
- 15–27: chapter I again, a second copy or retyping;
- 28–54: chapter II;
- 55–75: chapter III.

Site 76, the folder cover, and sites 77–114, the handwritten notes, are in Pro package 249 (`MPL_129_077-115`; it was
package 178 before the re-cut of 13 Nov).

Context paragraph:
> This page is from archive cote 129: notes of the seminar Grothendieck gave at Montréal in 1970 on Barsotti-Tate groups
> and Dieudonné theory, written up by Delale, Labute, Hakim and Messing; copies of annotated typescripts, in French;
> site page {site} (PDF page {pdf}). {chapter} The handwriting may be Grothendieck's or the note-takers'. The notation is
> that of the period (W_n, F, V, \underline{Z}_p, Spec, script letters); write it as typed or written. The printed
> version (Groupes de Barsotti-Tate et cristaux de Dieudonné, Presses de l'Université de Montréal, 1974) differs from
> these notes and is not given. No draft is given for this text: transcribe the page.

Pilot pages:
- `mtl129_129_031`: margin marks and formulas;
- `mtl129_129_046`: the large diagram of equivalences;
- `mtl129_129_065`: handwritten insertion and formulas.

### `t162`: Tapis de Quillen, cote 162-5 (51 pages)

Typed and printed pages:
- sites 2–17: "Tapis de Quillen", first copy, pp. 1–16, headed by hand "notes du 10.9.68", annotated;
- sites 32–48: second copy, 17 pp., with annotations of its own;
- sites 50–55: offprint, D. Quillen, "On the Representation of Hermitian Forms as Sums of Squares", *Inventiones math.*
  5, 237–242 (1968);
- sites 57–68: D. G. Quillen, "On a conjecture of Adams", a typed MIT preprint in a blue duplicated copy, 12 pp.
  - Probably the version printed as "Some remarks on etale homotopy theory and a conjecture of Adams", *Topology* 7
    (1968). This rests on the title only, has not been checked, and is not in the prompt.

Pro package 76 holds sites 18–31 (PDF 19–32): the handwritten notes of 1968 and the typed list "Publications of Daniel
Quillen" (site 19).

Not routed anywhere: site 1, the folder cover with the handwritten title "Le Tapis de Quillen … (1968)". It is one
sheet with two lines. Add it to a Pro package, or send it with this text, as you decide.

Context paragraph:
> This page is from archive cote 162-5, "Tapis de Quillen", a dossier Grothendieck assembled in 1968; site page {site}
> (PDF page {pdf}). {document}

Documents:
- **First copy:** "It is Grothendieck's typescript "Tapis de Quillen" (French; headed by hand "notes du 10.9.68"),
  first copy (sites 2-17), with handwritten corrections and annotations. The notation is his of 1968 ((Cat), (Ss), Hom,
  nerve, topos, Gr-catégories). No draft is given for this text: transcribe the page."
- **Second copy:** the same, saying that the annotations of this copy are the point.
- **Offprint:** the bibliographic data above, then: "This page is printed, not typed. The point of the page is the
  handwriting on it (annotations, marks, underlinings, corrections, a dedication or a name): mark every one with the
  macros, at its place. Transcribe the printed text plainly as the context of those marks … If the page carries no
  handwriting at all, write "NO HANDWRITING" as the first line of NOTES. No draft is given for this text: transcribe
  the page."

No full edition exists. Carmona's partial transcription covers part I only. The second copy could be sent after the
first, with the first copy's transcription as its draft (as for the Esquisse), if the pilot shows that the two copies'
annotations differ enough to need it. It is prepared without a draft now.

Pilot pages:
- `t162_162-5_008`: copy 1, heavy margins;
- `t162_162-5_041`: copy 2, handwritten paragraph;
- `t162_162-5_048`: copy 2, dense annotations.

### `esq119`: Esquisse d'un programme, copy 2, cote 119 (58 pages)

Sites 78–135: the sommaire (78) and typescript pp. 1–57 (79–135). Copy 2 site = copy 1 site + 76. This was checked for
all 58 pages by the ink profile of each page against copy 1 at offsets 75, 76 and 77 (best at 76 on 57 pages). The one
page where the profile was not decisive was checked by its typed page number (site 112 = p. 34 = copy 1 site 36).

**Draft:** copy 1's transcription of 12 Nov (`esquisse/pages/esq_119_<site−76>.tex`, without its comment header), as for
the `esq` text. The DRAFT_CONTEXT says this:
- the typed text should agree;
- a handwritten mark of copy 2 that is missing from the draft is hand-missing, and is the main thing to find;
- a mark only in copy 1 is addition, with the note "only in copy 1";
- a typed difference is either a misreading in copy 1 (to be marked so) or a real difference between the copies.

Context paragraph:
> This page is from the second copy of the typescript of Esquisse d'un programme by A. Grothendieck (1984, French) in
> archive cote 119, site page {site} (PDF page {pdf}); it is typescript page {n}. It is a copy of the same typescript as
> the first copy in the same folder, but it carries handwriting of its own (on page 1, for instance, the title and the
> author's name are struck through by hand): that handwriting is the point of this page, so look for every mark,
> however small, in the text, between the lines and in the margins.

Pilot pages:
- `esq119_119_078`: the sommaire with handwritten numbers;
- `esq119_119_079`: p. 1, with the title struck;
- `esq119_119_134`: p. 56, with the diagram.

### `r119`: the rest of cote 119 (154 pages)

Typed and printed pages, by document:

| Sites | Pages | Document |
|---|---|---|
| 61–64 | 4 | Offprint: N. Saavedra Rivano, "Polarisations des catégories tannakiennes : cas homogène", note transmise par M. Henri Cartan, *C. R. Acad. Sc. Paris* t. 273, Série A, p. 1144–1147 (8 décembre 1971) |
| 65–68 | 4 | Offprint: the same, "… cas gradué", t. 273, p. 1246–1248 (20 décembre 1971) |
| 69–72 | 4 | Offprint: the same, "Représentations linéaires de schémas en groupes affines", t. 272, p. 258–261 (18 janvier 1971) |
| 73–76 | 4 | Offprint: the same, "⊗-catégories et dualité de Tannaka", t. 272, p. 389–392 (1er février 1971) |
| 137–139 | 3 | Rapport d'activité (1.10.1984 – 15.12.1984) |
| 141–142 | 2 | A second "Rapport d'activité" (title by hand): teaching since 1978, theses |
| 162–180 | 19 | "Fonctions holomorphes I", USTL Montpellier, 1973–74 |
| 182–191 | 10 | "Fonctions holomorphes II", 1973–74 |
| 193–194 | 2 | Programme of a C4 course, 1978–79 |
| 196–212 | 17 | "Esquisse thématique des principaux travaux mathématiques de A. Grothendieck" (1972), copy 1, with the bibliography complement and the list of works citing him |
| 214–239 | 26 | Esquisse thématique, copy 2 (another typing), with "Principales publications" |
| 241–250 | 10 | "Le maître-enseignant et le maître-chercheur dans l'Université d'aujourd'hui et de demain" (1968), copy 1, annotated |
| 251–252 | 2 | Letter of Grothendieck to H. Beuve-Méry (Le Monde), Massy, 4 June 1968 |
| 254–270 | 17 | "Le maître-enseignant …", copy 2 |
| 272–273 | 2 | Typed proposal on the doctorat d'État in mathematics, with handwriting |
| 282–286 | 5 | Typed letter in English, "Dear Alexander", signed by hand "Ronnie" |
| 288–301 | 14 | J.-P. Serre, Collège de France, résumé des cours 1990–1991, with seminar, publications, missions |
| 303–306 | 4 | Curriculum vitae de Alexandre Grothendieck, copy 1 |
| 308 | 1 | CNRS form letter of 26.1.72 |
| 310–313 | 4 | Curriculum vitae, copy 2, with a handwritten addition |

Handwritten material in Pro package 250:
- sites 143–160;
- sites 275–279, the handwritten "Rapport de la Commission relative au recrutement des enseignants";
- site 280, a few faint typed lines.

Blank: 1, 60, 77, 136, 140, 161, 181, 192, 195, 213, 240, 253, 271, 274, 281, 287, 302, 307, 309.

The 154 pages plus copy 2 (58) make 212 sent pages. With the 18 blank sheets that is 230, the figure in the brief.

Context paragraph:
> This page is from archive cote 119, the dossier Grothendieck put together for his application to the CNRS in 1984,
> which also holds older documents (1968-1991); site page {site} (PDF page {pdf}). {document}

Each document's sentence (in `batch.py`, DOC_CONTEXT) names it, gives its language, and ends with "No draft is given
for this text: transcribe the page." The four offprints carry their bibliographic data and the annotation instruction
quoted under `t162`.

**Draft possible later.** The Circle's typeset "Esquisse thématique" (EsquisseThem.pdf, 13 pp.) could be a draft for
the 43 pages of the two Esquisse thématique copies. It was not downloaded or aligned here.

Pilot pages:
- `r119_119_061`: offprint, to test the annotation instruction;
- `r119_119_170`: Fonctions holomorphes, formulas;
- `r119_119_249`: Le maître-enseignant, handwritten insertions and strike-outs.

## Dry runs and estimate

The runs were `python -I -B scripts/batch.py dry <name> <text>`, with no key, on 13 Nov 2026.

| Text | Pages | Request body | Dry-run estimate |
|---|---|---|---|
| brown | 26 | 23.8 MB | $2.03 |
| mtl129 | 74 | 51.2 MB | $5.77 |
| t162 | 51 | 40.7 MB | $3.98 |
| esq119 | 58 | 51.4 MB | $4.52 |
| r119 | 154 | 140.7 MB | $12.01 |
| **Total** | **363** | | **$28.31** |
| Pilot (`PILOT_NEXT_20261113.json`) | 15 | 12.8 MB | $1.17 |

- **What the estimate rests on.** None of these texts has been measured yet, so `measured_means` falls back to the
  guard's constants: 9,000 input and 6,000 output tokens a page, or $0.078 a page at batch price. The measured rates of
  12–13 Nov were:

  | Text | Per page |
  |---|---|
  | ps | $0.089 |
  | ega25 | $0.065 |
  | esq | $0.053 |
  | ega24 | $0.035 |

  At those rates the 363 pages would cost about $13–32. The likely figure is about $20–25: dense French course text and
  formulas in 129, 162-5 and the Fonctions holomorphes; drafts on 74 pages. After the pilot, `measured_means` uses the
  pilot's own figures per text.
- **Size.** Every text fits in one batch, under the script's 200 MB body limit. r119 is the largest at 140.7 MB.
- **Guard.** The dry runs used the guard's defaults, so they print "job cap left −$7.96" and "credit left about $40".
  For the submit the main session sets JOB_SINCE, JOB_CAP_USD, CREDIT_LEFT_START and KEY_LABEL for the key it uses.
- **Suggested order:**
  1. the pilot ($1.17);
  2. a check of the 15 pages against the scans;
  3. the five texts, one batch at a time.

## Inventory only: cotes 10, 12, 15 and 37

From thumbnails, with larger crops for ten pages of 12. The class of each scan is in `TYPED_INVENTORY_20261113.tsv`;
"probable" there marks the scans the thumbnail did not settle. All four cotes are whole in Pro packages:
- 10: 134–137;
- 12: 85–88;
- 15: 88–92;
- 37: 241–243.

| Cote | Scans | Typed or printed (sites) | Mixed runs | Handwritten | Blank / cover |
|---|---|---|---|---|---|
| 10 | 197 | 84: 32–57, 59–83, 85–86, 101–108, 114–136 (annotated typescripts; 114 is a table of contents) | – | 97 | 12 / 4 |
| 12 | 167 | 17: 21, 65, 67–69, 71, 80, 82, 84, 96–97, 99, 101, 116 (letter), 118 (printed LNM 41 cover), 120, 122 | 22: 125–137 (odd sites purple duplicated redactions), 159–167 (odd sites an English typescript upside down, reused) | 122 | 4 / 2 |
| 15 | 227 | 16: 3, 5, 7, 11, 58, 61–63, 80–81, 135, 137, 169–170, 180, 187 | 139: 25–56, 65–78, 83–125, 158–165, 182–186, 191–227 | 52 | 15 / 5 |
| 37 | 99 | 50: 2–4, 6, 8–12, 14–15, 17, 22–24, 26, 29–30, 33–34, 38–44, 47, 49, 65–71, 73, 84–93, 95–97 | – | 36 | 13 / 0 |

**Cote 15** is mostly his handwriting on reused typed sheets: purple or blue duplicated redactions with numbered pages,
and an English typescript in blue ("Some applications of the … criterion of projectivity …", as far as the thumbnail
shows), often upside down. Typed and handwritten
sheets alternate through most of the cote. A typed-only API pass makes little sense there: the typed side is someone
else's text, and the notes are on the other side.

**Cote 37** has the most clearly typed material: the re-edition plans, the letters of 1967–71, the lists of corrections,
and the table of contents at 84–91.

**Cote 10** has long annotated typescripts. It would be the next API candidate after these texts.
