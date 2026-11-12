r"""The pages to transcribe, with their draft passages and the alignment table (12 Nov 2026).

Pursuing Stacks (draft: arXiv 2111.01000 v2 LaTeX):
  134-2 sites 1-2 (folder cover, "The Modelizing Story" title page), 3-12 (provisional contents), 13 (dedication):
        no draft (the edition does not contain them);
  134-2 sites 14-36 (letter to Quillen), 37-77 (appendix: letters to Breen), 78-81 (notes to chapter I and appendix),
        134-3 sites 89-93 (notes for chapter II): passage(s) found by the OCR aligner (align.py);
  134-3 sites 1-88 = pp. 1-88; 134-4 sites 1-82 = pp. 89-170, 84-100 = pp. 171-187 (site 83 is a Recoltes et
        Semailles verso, left out); 134-5 sites 1-132 = pp. 188-319; 134-6 sites 1-26 = pp. 320-345, site 27 = a
        struck-through version of p. 345, sites 28-124 = pp. 346-442; 134-7 sites 1-112 = pp. 443-554; 134-8 sites
        1-39 = pp. 555-593. The site-to-page offsets were read from the aligner's votes (ALIGNMENT_raw.tsv,
        ts_page_by_vote) and are constant within each run of pages; the passage is the draft between the \pspage
        markers of page n and page n+1 (for 279, 289 and 370, which have no marker, from n-1 to n+1), widened by
        about 400 characters on each side and cut at whole lines.
  Not sent: 134-1 (handwritten letter), 134-2 sites 82-183 (separator, duplicate copies, Recoltes et Semailles versos,
        R. Brown's documents, handwritten letter copies), 134-8 sites 40-86 (folder cover, blank, handwritten notes on
        listing paper). See the report.
Esquisse (draft: Grothendieck Circle EsquisseFr.pdf, text layer): 119 sites 2-59 = sommaire and typescript pp. 1-57
  (copy 1), passage(s) by the OCR aligner.
EGA V: cote 25 sites 1-184 and cote 24 sites 1-76, no draft.

Writes PAGES.json, alignment/ALIGNMENT.tsv and alignment/drafts/<key>.txt.
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
AL = BASE / "alignment"
PS_SRC = pathlib.Path(r"C:\Users\user\Documents\pursuing_stacks_expert_20261110\src")
MARK = re.compile(r"\\(?:named)?pspage\{([^}]*)\}(?:\{([^}]*)\})?")

PS_RUNS = [("134-3", 1, 88, 0), ("134-4", 1, 82, 88), ("134-4", 84, 100, 87), ("134-5", 1, 132, 187),
           ("134-6", 1, 26, 319), ("134-6", 28, 124, 318), ("134-7", 1, 112, 442), ("134-8", 1, 39, 554)]
TEXT_NAMES = {"ps": "Pursuing Stacks", "esq": "Esquisse d'un programme", "ega25": "Nouveau EGA V (cote 25)",
              "ega24": "EGA V, English translation by P. Blass (cote 24)"}


def marker_table():
    """label -> (file, offset)"""
    t = {}
    for k in range(1, 8):
        name = f"ps{k}.tex"
        text = (PS_SRC / name).read_text(encoding="utf-8")
        for m in MARK.finditer(text):
            t[m.group(2) or m.group(1)] = (name, m.start())
    return t


def ps_passage(n, marks, cache={}):
    lo = str(n) if str(n) in marks else str(n - 1)
    hi = n + 1
    while str(hi) not in marks and hi < 600:
        hi += 1
    fname, a = marks[lo]
    if fname not in cache:
        cache[fname] = (PS_SRC / fname).read_text(encoding="utf-8")
    text = cache[fname]
    if str(hi) in marks and marks[str(hi)][0] == fname:
        b = marks[str(hi)][1]
    else:
        b = len(text)
    a = max(0, a - 400)
    b = min(len(text), b + 400)
    a = text.rfind("\n", 0, a) + 1
    e = text.find("\n", b)
    b = len(text) if e < 0 else e
    l0 = text.count("\n", 0, a) + 1
    l1 = text.count("\n", 0, b) + 1
    return f"{fname}:{l0}-{l1}", f"%%% draft: {fname}, lines {l0}-{l1}\n" + text[a:b]


def main():
    raw = {r["key"]: r for r in json.load(open(AL / "alignment_raw.json", encoding="utf-8"))}
    marks = marker_table()
    (AL / "drafts").mkdir(exist_ok=True)
    pages = []

    def add(text, cote, site, kind, ts_page="", draft=None, loc="", method=""):
        key = f"{text}_{cote}_{site:03d}"
        r = raw.get(f"{'ps' if text == 'ps' else 'esq'}_{cote}_{site:03d}", {})
        if draft:
            (AL / "drafts" / f"{key}.txt").write_text(draft, encoding="utf-8")
        pages.append({"key": key, "text": text, "cote": cote, "site": site, "pdf_page": site + 1, "kind": kind,
                      "ts_page": ts_page, "draft": bool(draft), "draft_location": loc, "align_method": method,
                      "ocr_score": r.get("score", ""), "ocr_vote_page": r.get("ts_page_by_vote", "")})

    def ocr_draft(prefix, cote, site):
        k = f"{prefix}_{cote}_{site:03d}"
        p = AL / "drafts_by_ocr" / f"{k}.txt"
        if p.exists():
            return p.read_text(encoding="utf-8"), raw[k]["draft_location"]
        return None, ""

    # ---- Pursuing Stacks
    for s in (1, 2):
        add("ps", "134-2", s, "front matter", method="no draft")
    for s in range(3, 13):
        add("ps", "134-2", s, "provisional contents", method="no draft")
    add("ps", "134-2", 13, "dedication", method="no draft")
    for s in range(14, 82):
        kind = "letter to Quillen" if s <= 36 else "appendix (letters to Breen)" if s <= 77 else "notes to ch. I"
        d, loc = ocr_draft("ps", "134-2", s)
        add("ps", "134-2", s, kind, draft=d, loc=loc, method="OCR aligner" if d else "no draft found")
    runs = {(c, s): s + off for c, a, b, off in PS_RUNS for s in range(a, b + 1)}
    for cote in ["134-3", "134-4", "134-5", "134-6", "134-7", "134-8"]:
        sites = sorted(s for (c, s) in runs if c == cote)
        if cote == "134-6":
            sites = sorted(sites + [27])
        for s in sites:
            if (cote, s) == ("134-6", 27):
                loc, d = ps_passage(345, marks)
                add("ps", cote, s, "typescript (struck-through version of p. 345)", "345 (struck version)", d, loc,
                    "pspage markers, page 345")
                continue
            n = runs[(cote, s)]
            loc, d = ps_passage(n, marks)
            add("ps", cote, s, "typescript", str(n), d, loc, "pspage markers" + (
                "" if str(n) in marks else f" (no marker for {n}: from {n - 1} to {n + 1})"))
        if cote == "134-3":
            for s in range(89, 94):
                d, loc = ocr_draft("ps", cote, s)
                add("ps", cote, s, "notes for ch. II", draft=d, loc=loc, method="OCR aligner")
    # ---- Esquisse
    for s in range(2, 60):
        d, loc = ocr_draft("esq", "119", s)
        add("esq", "119", s, "sommaire" if s == 2 else "typescript", "" if s == 2 else str(s - 2), d, loc,
            "OCR aligner")
    # ---- EGA V
    for s in range(1, 185):
        add("ega25", "25", s, "typescript", method="no draft")
    for s in range(1, 77):
        add("ega24", "24", s, "typescript", method="no draft")

    json.dump(pages, open(BASE / "PAGES.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    cols = ["key", "text", "cote", "site", "pdf_page", "kind", "ts_page", "draft", "draft_location", "align_method",
            "ocr_score", "ocr_vote_page"]
    with open(AL / "ALIGNMENT.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(cols) + "\n")
        for p in pages:
            f.write("\t".join(str(p[c]) for c in cols) + "\n")
    from collections import Counter
    print(Counter(p["text"] for p in pages), Counter(p["align_method"].split(" (")[0] for p in pages))


if __name__ == "__main__":
    main()
