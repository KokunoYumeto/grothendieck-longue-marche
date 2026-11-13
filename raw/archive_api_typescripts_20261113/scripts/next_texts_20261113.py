r"""The next typescripts for the API (13 Nov 2026): typed-page inventory, new PAGES.json entries and drafts.

Written by Claude Opus 5.5 (effort high), 13 Nov 2026. No API call.

The classification below was made by eye from contact sheets of every scan (thumbnails about 200 px wide, larger
crops where a page was unclear) and checked against MANIFEST.csv, PLACEMENT_EVERYTHING.csv, SECTIONS_STATE.md, the
12 Nov blank-scan list (packages_work/RECUT_20261113/BLANKS_20261112.json) and the Pro package plan
(packages_work/full_archive_20261112/PLAN.json). "site" = PyMuPDF page index = PDF page - 1 (PDF page 1 is the IMAG
cover of the digitization).

New texts (key prefix = text key; the prefix before the first "_" must be the text key, see batch.py):
  brown   134-2 sites 115-143: R. Brown's translations of two letters to L. Breen, his cover note and comments
  mtl129  129 sites 1-75: typed notes of the Montreal seminar (1970); sites 76-114 are in Pro package 249
          (MPL_129_077-115; package 178 before the 13 Nov re-cut)
  t162    162-5: the two typed copies of "Tapis de Quillen", Quillen's offprint and preprint; sites 18-31 (PDF 19-32,
          the handwritten notes) are in Pro package 76
  esq119  119 sites 78-135: second copy of the Esquisse; draft = the copy 1 transcription of the same page
  r119    119: the rest of the typed and printed pages (offprints 1971, reports, courses, CV, letters)
Drafts: esq119 from esquisse/pages/esq_119_<site-76>.tex (copy 2 site = copy 1 site + 76, checked on all 58 pages by
the row-ink profiles and by the typed page numbers); brown sites 128-143 (Brown's translation of the letter of 17-19
July 1975) from the arXiv text of Pursuing Stacks, appendix, ps1.tex lines 1380-1647, where Grothendieck reprinted that
translation with his corrections; the passage of each page is found by word 3-grams of its Tesseract OCR
(work/ocr/134-2/<site>.txt), as in align.py.

Writes: TYPED_INVENTORY_20261113.tsv, PAGES.json (new entries appended; backup first), alignment/drafts/<key>.txt,
alignment/ALIGNMENT_next_texts_20261113.tsv.
usage: python -I -B scripts/next_texts_20261113.py
"""
import json
import pathlib
import re
import shutil
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
AL = BASE / "alignment"
PS1 = pathlib.Path(r"C:\Users\user\Documents\pursuing_stacks_expert_20261110\src\ps1.tex")
TAG = "_before_next_texts_20261113"

# ------------------------------------------------------------------ inventory: (cote, first, last, class, what, route)
T, H, B, P, C = "typed", "handwritten", "blank", "printed", "cover"
INV = [
    # 134-2, around R. Brown's documents (sites 82-114 and 144-183 are listed in the 12 Nov report)
    ("134-2", 115, 115, T, "R. Brown, cover note of the translation", "API brown"),
    ("134-2", 116, 116, B, "blank sheet", "none"),
    ("134-2", 117, 120, T, "R. Brown, 'Comments' (4 pp., references)", "API brown"),
    ("134-2", 121, 121, B, "blank sheet", "none"),
    ("134-2", 122, 126, T, "R. Brown, translation of the letter to L. Breen of 17/2/1975 (5 pp.)", "API brown"),
    ("134-2", 127, 127, B, "back of a sheet of computer listing paper (show-through only)", "none"),
    ("134-2", 128, 143, T, "R. Brown, translation of an extract from the letter to L. Breen of 17-19 July 1975 (16 pp.)",
     "API brown"),
    ("134-2", 144, 144, B, "blank sheet", "none"),
    # 129
    ("129", 1, 13, T, "Montreal seminar notes, chapter I 'Preliminaires sur Witt' (title page and pp.)", "API mtl129"),
    ("129", 14, 14, B, "blank sheet", "none"),
    ("129", 15, 27, T, "chapter I again: a second copy (or retyping) of the same chapter", "API mtl129"),
    ("129", 28, 54, T, "chapter II (title page at site 28), annotated copy", "API mtl129"),
    ("129", 55, 75, T, "chapter III (title page at site 55), annotated copy", "API mtl129"),
    ("129", 76, 76, C, "folder cover with handwritten titles", "Pro 249"),
    ("129", 77, 114, H, "handwritten notes (sites 78 and 88 blank)", "Pro 249"),
    # 162-5
    ("162-5", 1, 1, C, "folder cover, handwritten title 'Le Tapis de Quillen ... (1968)'", "none (see report)"),
    ("162-5", 2, 17, T, "'Tapis de Quillen', typescript, first copy, 'notes du 10.9.68' (pp. 1-16), annotated",
     "API t162"),
    ("162-5", 18, 18, B, "blank sheet", "Pro 76"),
    ("162-5", 19, 19, T, "typed list 'Publications of Daniel Quillen'", "Pro 76"),
    ("162-5", 20, 20, B, "blank sheet", "Pro 76"),
    ("162-5", 21, 30, H, "handwritten notes (1968)", "Pro 76"),
    ("162-5", 31, 31, B, "blank sheet", "Pro 76"),
    ("162-5", 32, 48, T, "'Tapis de Quillen', second copy (17 pp.), annotated", "API t162"),
    ("162-5", 49, 49, B, "blank sheet", "none"),
    ("162-5", 50, 55, P, "offprint: D. Quillen, Inventiones math. 5 (1968) 237-242", "API t162"),
    ("162-5", 56, 56, B, "blank sheet", "none"),
    ("162-5", 57, 68, T, "D. G. Quillen, 'On a conjecture of Adams', typed preprint (MIT), blue duplicate, 12 pp.",
     "API t162"),
    # 119 (copy 1 of the Esquisse, sites 2-59, was done on 12 Nov)
    ("119", 1, 1, B, "blank sheet (pencil '1' at the foot)", "none"),
    ("119", 2, 59, T, "Esquisse d'un programme, copy 1 (sommaire and pp. 1-57)", "API esq (done 12 Nov)"),
    ("119", 60, 60, B, "blank sheet", "none"),
    ("119", 61, 76, P, "four C. R. Acad. Sc. Paris offprints of N. Saavedra Rivano (1971), 4 scans each", "API r119"),
    ("119", 77, 77, B, "blank sheet", "none"),
    ("119", 78, 135, T, "Esquisse d'un programme, copy 2 (sommaire and pp. 1-57), annotated", "API esq119"),
    ("119", 136, 136, B, "blank sheet", "none"),
    ("119", 137, 139, T, "Rapport d'activite (1.10.1984 - 15.12.1984), 3 pp.", "API r119"),
    ("119", 140, 140, B, "blank sheet", "none"),
    ("119", 141, 142, T, "a second 'Rapport d'activite' (title by hand): teaching since 1978, theses (2 pp.)",
     "API r119"),
    ("119", 143, 160, H, "handwritten notes (sites 146 and 153 blank)", "Pro 250"),
    ("119", 161, 161, B, "blank sheet", "none"),
    ("119", 162, 180, T, "'Fonctions holomorphes I', course text, USTL Montpellier 1973-74", "API r119"),
    ("119", 181, 181, B, "blank sheet", "none"),
    ("119", 182, 191, T, "'Fonctions holomorphes II', course text, 1973-74", "API r119"),
    ("119", 192, 192, B, "blank sheet", "none"),
    ("119", 193, 194, T, "programme of the C4 course, USTL 1978-79", "API r119"),
    ("119", 195, 195, B, "blank sheet", "none"),
    ("119", 196, 212, T, "'Esquisse thematique des principaux travaux mathematiques de A. Grothendieck' (1972), copy 1, "
     "with bibliography complement and list of works citing him (pp. 1-17)", "API r119"),
    ("119", 213, 213, B, "blank sheet", "none"),
    ("119", 214, 239, T, "Esquisse thematique, copy 2 (another typing, 26 pp.), with 'Principales publications'",
     "API r119"),
    ("119", 240, 240, B, "blank sheet", "none"),
    ("119", 241, 250, T, "'Le maitre-enseignant et le maitre-chercheur dans l'Universite d'aujourd'hui et de demain' "
     "(1968), copy 1 (10 pp.), annotated", "API r119"),
    ("119", 251, 252, T, "letter of A. Grothendieck to H. Beuve-Mery (Le Monde), Massy, 4 June 1968 (2 pp.)",
     "API r119"),
    ("119", 253, 253, B, "blank sheet", "none"),
    ("119", 254, 270, T, "'Le maitre-enseignant et le maitre-chercheur', copy 2 (17 pp.)", "API r119"),
    ("119", 271, 271, B, "blank sheet", "none"),
    ("119", 272, 273, T, "typed proposal on the doctorat d'Etat in mathematics (2 pp.), with handwriting",
     "API r119"),
    ("119", 274, 274, B, "blank sheet", "none"),
    ("119", 275, 279, H, "handwritten 'Rapport de la Commission relative au recrutement des enseignants'", "Pro 250"),
    ("119", 280, 280, T, "a few faint typed lines at the head (probable)", "Pro 250"),
    ("119", 281, 281, B, "blank sheet", "none"),
    ("119", 282, 286, T, "typed letter in English 'Dear Alexander', signed by hand 'Ronnie' (5 pp.)", "API r119"),
    ("119", 287, 287, B, "blank sheet", "none"),
    ("119", 288, 301, T, "J.-P. Serre, College de France, resume des cours 1990-1991, seminar, publications, missions",
     "API r119"),
    ("119", 302, 302, B, "blank sheet", "none"),
    ("119", 303, 306, T, "Curriculum vitae de Alexandre Grothendieck, copy 1, with 'Principales publications'",
     "API r119"),
    ("119", 307, 307, B, "blank sheet", "none"),
    ("119", 308, 308, T, "CNRS form letter of 26.1.72 to Grothendieck, address by hand", "API r119"),
    ("119", 309, 309, B, "blank sheet", "none"),
    ("119", 310, 313, T, "Curriculum vitae, copy 2, handwritten addition on the last page", "API r119"),
]

# Inventory only (not prepared): cotes 10, 12, 15, 37. From thumbnails; "probable" where the thumbnail could not
# settle it. These cotes are whole in Pro packages 134-137 (10), 85-88 (12), 88-92 (15), 241-243 (37).
INV_ONLY = {
    "10": [(1, 2, C, "folder covers with handwritten titles"), (3, 16, H, ""), (17, 17, B, ""), (18, 18, H, ""),
           (19, 19, B, "blank or nearly blank"), (20, 30, H, "(21: one struck line only)"), (31, 31, B, ""),
           (32, 57, T, "typescript (Tannakian categories), heavily annotated; 55 has a long handwritten passage"),
           (58, 58, B, ""), (59, 83, T, "typescript, annotated"), (84, 84, B, ""),
           (85, 86, T, "typescript (86 sparse, probable)"), (87, 87, C, "cover with handwritten title"),
           (88, 98, H, "notes, some on IHES letterhead (91, 93 nearly blank)"), (99, 100, B, ""),
           (101, 108, T, "typescript, faint copy"), (109, 109, B, ""), (110, 112, H, ""), (113, 113, B, ""),
           (114, 136, T, "typescript (114: table of contents), annotated"), (137, 137, B, ""), (138, 139, H, ""),
           (140, 140, C, "cover with handwritten title"), (141, 141, B, ""), (142, 154, H, ""), (155, 155, B, ""),
           (156, 197, H, "")],
    "12": [(1, 9, H, ""), (10, 10, H, "IHES letterhead, nearly blank"), (11, 18, H, ""), (19, 19, B, ""),
           (20, 20, H, "list 'Motifs'"), (21, 21, T, "typescript page"), (22, 64, H, ""),
           (65, 65, T, "typescript, struck through by hand"), (66, 66, H, ""), (67, 69, T, "typescript, annotated"),
           (70, 70, H, ""), (71, 71, T, "typed page upside down (reused sheet)"), (72, 79, H, ""),
           (80, 80, T, ""), (81, 81, H, ""), (82, 82, T, ""), (83, 83, H, ""), (84, 84, T, ""), (85, 94, H, ""),
           (95, 95, C, "cover with handwritten note"), (96, 97, T, "typescript, annotated"),
           (98, 98, H, "plan with a list of references"), (99, 99, T, "typed with handwritten formulas (probable)"),
           (100, 100, H, ""), (101, 101, T, "faint typescript"), (102, 102, B, ""), (103, 108, H, ""),
           (109, 109, B, ""), (110, 115, H, ""), (116, 116, T, "typed letter, signed by hand"), (117, 117, H, ""),
           (118, 118, P, "printed cover of LNM 41, Local Cohomology (1967)"), (119, 119, H, ""),
           (120, 120, T, ""), (121, 121, H, ""), (122, 122, T, ""), (123, 123, B, ""), (124, 124, H, ""),
           (125, 137, "alternating", "odd sites typed (purple duplicated Bourbaki-style redaction, numbered pages), "
            "even sites handwritten"), (138, 138, C, "cover with handwritten note"), (139, 158, H, ""),
           (159, 167, "alternating", "odd sites typed upside down (English typescript, reused versos), even sites "
            "handwritten")],
    "15": [(1, 1, C, "cover with handwritten note"), (2, 2, H, ""), (3, 3, T, "typed upside down (reused, English)"),
           (4, 4, H, ""), (5, 5, T, "typed upside down (probable)"), (6, 6, H, ""), (7, 7, T, "typed upside down"),
           (8, 10, H, ""), (11, 11, T, "typed upside down"), (12, 13, H, ""), (14, 14, B, ""), (15, 23, H, ""),
           (24, 24, B, ""),
           (25, 56, "alternating", "faint purple typed pages with his handwriting (even sites, probable) alternate "
            "with handwritten pages (odd sites)"), (57, 57, B, ""), (58, 58, T, "typescript, annotated"),
           (59, 60, H, ""), (61, 63, T, "faint typed, annotated (probable)"), (64, 64, B, ""),
           (65, 78, "alternating", "handwritten pages and faint typed pages, mixed (probable)"), (79, 79, B, ""),
           (80, 81, T, "typescript"), (82, 82, B, ""),
           (83, 99, "alternating", "handwritten pages on the backs of an upside-down typescript (probable)"),
           (100, 125, "alternating", "English typescript in blue ('Some applications of the criterion of "
            "projectivity ...', numbered pages) interleaved with handwritten pages"),
           (126, 126, B, ""), (127, 132, H, ""), (133, 133, B, ""), (134, 134, H, ""),
           (135, 135, T, "typed list (Bourbaki-type circular)"), (136, 136, H, ""),
           (137, 137, T, "typed upside down (blue)"), (138, 138, H, ""), (139, 139, B, "orange sheet"),
           (140, 144, H, ""), (145, 145, B, ""), (146, 151, H, ""), (152, 152, B, ""), (153, 154, H, ""),
           (155, 155, B, ""), (156, 156, C, "sheet with a handwritten note"), (157, 157, B, ""),
           (158, 165, "alternating", "handwritten pages and blue typed pages upside down"), (166, 166, B, ""),
           (167, 167, H, "on graph paper"), (168, 168, B, ""), (169, 170, T, "typed (Bourbaki-type redaction), "
            "annotated"), (171, 171, C, "sheet with a handwritten note"), (172, 178, H, ""),
           (179, 179, H, "a few handwritten lines"), (180, 180, T, "typed list"), (181, 181, C, "handwritten note"),
           (182, 186, "alternating", "handwritten pages and the blue English typescript (183, 185)"),
           (187, 187, T, "blue English typescript"), (188, 188, C, "cover with handwritten title"),
           (189, 190, H, ""),
           (191, 227, "alternating", "handwritten pages and typed redaction pages ('Redaction n.', blue or purple, "
            "many upside down); typed: about 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, "
            "219, 221, 223, 225, 227 (probable)")],
    "37": [(1, 1, B, ""), (2, 2, T, "typed plan of the re-editions"), (3, 4, T, "typed letters of 3.11.1970"),
           (5, 5, B, ""), (6, 6, T, "typed letter (probable)"), (7, 7, B, "nearly blank"),
           (8, 12, T, "typed letters and lists (12: letter in blue, 23.6.1971)"),
           (13, 13, H, "handwritten letter on Brandeis University paper"), (14, 15, T, "typed letters (1971)"),
           (16, 16, H, "IHES paper"), (17, 17, T, "typed list"), (18, 21, H, ""),
           (22, 24, T, "typescript, heavily annotated"), (25, 25, H, ""), (26, 26, T, "typescript, annotated"),
           (27, 27, H, "slip"), (28, 28, B, ""), (29, 30, T, "typescript"), (31, 31, B, ""), (32, 32, H, ""),
           (33, 34, T, "typed lists"), (35, 35, H, ""), (36, 36, B, "IHES letterhead upside down"), (37, 37, H, ""),
           (38, 44, T, "typescript and typed index lists"), (45, 45, B, ""), (46, 46, H, "diagram"),
           (47, 47, T, "typed upside down"), (48, 48, H, ""), (49, 49, T, "typed upside down"), (50, 50, B, ""),
           (51, 54, H, "notes and handwritten letters (53 on Harvard paper)"), (55, 55, B, ""), (56, 63, H, ""),
           (64, 64, B, ""), (65, 71, T, "typed list of corrections"), (72, 72, B, "nearly blank"),
           (73, 73, T, "typed letter of 3.11.1970"), (74, 82, H, "(74: handwritten letter on graph paper)"),
           (83, 83, B, "nearly blank"), (84, 91, T, "typed table of contents"), (92, 93, T, "typed letter"),
           (94, 94, H, ""), (95, 97, T, "typed letters (95: 21 September 1967)"), (98, 98, B, "nearly blank"),
           (99, 99, H, "")],
}

# ------------------------------------------------------------------ the pages sent: (text, cote, first, last, doc, kind)
SEND = [
    ("brown", "134-2", 115, 115, "brown_note", "cover note"),
    ("brown", "134-2", 117, 120, "brown_comments", "comments"),
    ("brown", "134-2", 122, 126, "brown_feb", "translation of the letter of 17/2/1975"),
    ("brown", "134-2", 128, 143, "brown_july", "translation of the letter of 17-19 July 1975"),
    ("mtl129", "129", 1, 13, "mtl_ch1a", "typescript"),
    ("mtl129", "129", 15, 27, "mtl_ch1b", "typescript"),
    ("mtl129", "129", 28, 54, "mtl_ch2", "typescript"),
    ("mtl129", "129", 55, 75, "mtl_ch3", "typescript"),
    ("t162", "162-5", 2, 17, "tq1", "typescript"),
    ("t162", "162-5", 32, 48, "tq2", "typescript"),
    ("t162", "162-5", 50, 55, "quillen_inv", "offprint"),
    ("t162", "162-5", 57, 68, "quillen_adams", "preprint"),
    ("esq119", "119", 78, 135, "esq_copy2", "typescript"),
    ("r119", "119", 61, 64, "cr_homogene", "offprint"),
    ("r119", "119", 65, 68, "cr_gradue", "offprint"),
    ("r119", "119", 69, 72, "cr_representations", "offprint"),
    ("r119", "119", 73, 76, "cr_tannaka", "offprint"),
    ("r119", "119", 137, 139, "rapport84", "typescript"),
    ("r119", "119", 141, 142, "rapport_c4", "typescript"),
    ("r119", "119", 162, 180, "fh1", "typescript"),
    ("r119", "119", 182, 191, "fh2", "typescript"),
    ("r119", "119", 193, 194, "c4_7879", "typescript"),
    ("r119", "119", 196, 212, "et1", "typescript"),
    ("r119", "119", 214, 239, "et2", "typescript"),
    ("r119", "119", 241, 250, "me1", "typescript"),
    ("r119", "119", 251, 252, "lettre_monde", "typed letter"),
    ("r119", "119", 254, 270, "me2", "typescript"),
    ("r119", "119", 272, 273, "doctorat", "typescript"),
    ("r119", "119", 282, 286, "lettre_ronnie", "typed letter"),
    ("r119", "119", 288, 301, "serre", "typescript"),
    ("r119", "119", 303, 306, "cv1", "typescript"),
    ("r119", "119", 308, 308, "cnrs72", "typed form letter"),
    ("r119", "119", 310, 313, "cv2", "typescript"),
]


# ------------------------------------------------------------------ OCR alignment for brown_july (as in align.py)
def norm_words(t):
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.findall(r"[a-z]{2,}", t)


def july_drafts():
    lines = PS1.read_text(encoding="utf-8").splitlines()
    lo, hi = 1380, len(lines)  # 1-based line numbers: the letter of 17/19 July 1975 to the end of ps1.tex
    tok = []  # (word, line number)
    for n in range(lo, hi + 1):
        tok += [(w, n) for w in norm_words(lines[n - 1])]
    words = [w for w, _ in tok]
    grams = {}
    for i in range(len(words) - 2):
        grams.setdefault(tuple(words[i:i + 3]), []).append(i)
    out, prev_end = {}, lo
    for s in range(128, 144):
        ow = norm_words((BASE / "work" / "ocr" / "134-2" / f"{s}.txt").read_text(encoding="utf-8", errors="replace"))
        votes = []
        for i in range(len(ow) - 2):
            pos = grams.get(tuple(ow[i:i + 3]), [])
            if 1 <= len(pos) <= 3:
                votes += pos
        if len(votes) < 5:
            out[s] = None
            continue
        votes.sort()
        # densest window of 700 draft words (a typed page holds about 250-450 words)
        best, bi = 0, 0
        j = 0
        for i in range(len(votes)):
            while votes[i] - votes[j] > 700:
                j += 1
            if i - j + 1 > best:
                best, bi = i - j + 1, (j, i)
        a, b = votes[bi[0]], votes[bi[1]]
        la, lb = tok[max(0, a - 60)][1], tok[min(len(tok) - 1, b + 60)][1]
        text = "\n".join(lines[la - 1:lb])
        out[s] = (la, lb, best, len(ow), text)
        prev_end = lb
    return out


def main():
    # inventory
    rows = []
    for c, a, b, cls, what, route in INV:
        for s in range(a, b + 1):
            rows.append((c, s, s + 1, cls, what, route, "eye (contact sheet, crops where unclear)"))
    for c, spec in INV_ONLY.items():
        for a, b, cls, what in spec:
            for s in range(a, b + 1):
                cl = cls
                if cls == "alternating":
                    cl = "mixed run (typed and handwritten sheets alternate)"
                rows.append((c, s, s + 1, cl, what, "Pro (whole cote); inventory only", "eye (thumbnails)"))
    with open(BASE / "TYPED_INVENTORY_20261113.tsv", "w", encoding="utf-8", newline="\n") as f:
        f.write("cote\tscan_site\tpdf_page\ttyped_or_handwritten\twhat_it_is\troute\tread_from\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")

    # pages
    pj = BASE / "PAGES.json"
    bak = BASE / "work" / f"PAGES{TAG}.json"
    if not bak.exists():
        shutil.copy2(pj, bak)
    pages = [p for p in json.load(open(bak, encoding="utf-8"))]  # always start from the backup (rerunnable)
    old = {p["key"] for p in pages}
    july = july_drafts()
    al_rows = []
    new = []
    for text, cote, a, b, doc, kind in SEND:
        for s in range(a, b + 1):
            key = f"{text}_{cote}_{s:03d}"
            assert key not in old, key
            draft, loc, method, ts = None, "", "no draft", ""
            if text == "esq119":
                c1 = s - 76
                src = BASE / "esquisse" / "pages" / f"esq_119_{c1:03d}.tex"
                body = [l for l in src.read_text(encoding="utf-8").splitlines()
                        if not (l.startswith("% ") or l.startswith("\\scanpage"))]
                loc = f"esquisse/pages/esq_119_{c1:03d}.tex (copy 1, site {c1})"
                draft = f"%%% draft: {loc}\n" + "\n".join(body).strip("\n") + "\n"
                method = "copy 1 page = copy 2 site - 76"
                ts = "" if s == 78 else str(s - 78)
                kind = "sommaire" if s == 78 else "typescript"
            elif doc == "brown_july" and july.get(s):
                la, lb, nv, nw, t = july[s]
                loc = f"ps1.tex, lines {la}-{lb}"
                draft = f"%%% draft: arXiv 2111.01000 v2, ps1.tex, lines {la}-{lb}\n" + t + "\n"
                method = f"OCR 3-gram aligner ({nv} votes, {nw} OCR words)"
            if draft:
                (AL / "drafts" / f"{key}.txt").write_text(draft, encoding="utf-8")
            new.append({"key": key, "text": text, "cote": cote, "site": s, "pdf_page": s + 1, "kind": kind,
                        "ts_page": ts, "draft": bool(draft), "draft_location": loc, "align_method": method,
                        "ocr_score": "", "ocr_vote_page": "", "doc": doc})
            al_rows.append((key, doc, loc, method))
    json.dump(pages + new, open(pj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(AL / "ALIGNMENT_next_texts_20261113.tsv", "w", encoding="utf-8", newline="\n") as f:
        f.write("key\tdoc\tdraft_location\tmethod\n" + "".join("\t".join(r) + "\n" for r in al_rows))
    from collections import Counter
    print("inventory rows", len(rows), Counter(r[0] for r in rows))
    print("new pages", len(new), Counter(p["text"] for p in new), "with draft",
          Counter(p["text"] for p in new if p["draft"]))
    for s in range(128, 144):
        v = july.get(s)
        print("brown july", s, v[:4] if v else None)


if __name__ == "__main__":
    main()
