r"""Align the drafts to the archive pages, by script (12 Nov 2026).

Drafts:
  ps   arXiv 2111.01000 v2 LaTeX (CC0), pursuing_stacks_expert_20261110\src\ps1.tex ... ps7.tex
  esq  Grothendieck Circle, EsquisseFr.pdf, text layer (work\EsquisseFr.txt; accents recomposed here, words unchanged)
Pages: the Tesseract (eng) OCR of every site page made by the existing-editions check (work\ocr\<cote>\<site>.txt).

Method: words of the OCR and of the draft are normalized (lower case, accents and LaTeX commands removed); every
word 3-gram of the page that occurs at most 3 times in the draft votes for its draft positions; the votes are
clustered (gap > 150 draft words starts a new cluster) and the clusters with >= 3 votes give the page's passage(s),
each widened by 60 words on either side and snapped to whole lines. For Pursuing Stacks the \pspage / \namedpspage
markers that fall in the passage give the typescript page label(s), as a cross-check.

Writes alignment\ALIGNMENT.tsv and alignment\drafts_by_ocr\<text>_<cote>_<site>.txt (inventory.py chooses the passage sent).
usage: python align.py
"""
import collections
import json
import os
import pathlib
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
OCR = BASE / "work" / "ocr"
PS_SRC = pathlib.Path(r"C:\Users\user\Documents\pursuing_stacks_expert_20261110\src")
OUT = BASE / "alignment"
(OUT / "drafts_by_ocr").mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- the pages in scope

def ps_pages():
    """(cote, site, kind) for the Pursuing Stacks pages sent over the API with the arXiv draft."""
    pages = []
    # 134-2: provisional contents (3-12), dedication (13), letter to Quillen (14-36), appendix (37-77),
    # notes to chapter I and appendix (78-81)
    for s in range(3, 82):
        kind = ("contents" if s <= 12 else "dedication" if s == 13 else "quillen" if s <= 36
                else "appendix" if s <= 77 else "notes")
        pages.append(("134-2", s, kind))
    for cote in ["134-3", "134-4", "134-5", "134-6", "134-7", "134-8"]:
        n = len(list((OCR / cote).glob("*.txt")))
        for s in range(0, n + 1):
            if (OCR / cote / f"{s}.txt").exists():
                pages.append((cote, s, "typescript"))
    return pages


def esq_pages():
    return [("119", s, "sommaire" if s == 2 else "esquisse") for s in range(2, 60)]


# ---------------------------------------------------------------- normalization

ACC = {"´": "\u0301", "`": "\u0300", "ˆ": "\u0302", "¨": "\u0308", "¸": "\u0327", "˜": "\u0303"}
LIG = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"}


def recompose_circle(t):
    """The Circle PDF's text layer writes accents as a spacing accent before the letter ("´e", "`a", "¸c" after);
    recompose them. Nothing else is changed."""
    for k, v in LIG.items():
        t = t.replace(k, v)
    t = re.sub(r"([´`ˆ¨˜])\s?([A-Za-zıI])", lambda m: unicodedata.normalize(
        "NFC", ("i" if m.group(2) == "ı" else m.group(2)) + ACC[m.group(1)]), t)
    t = re.sub(r"([cC])¸", lambda m: unicodedata.normalize("NFC", m.group(1) + "\u0327"), t)
    t = re.sub(r"¸([cC])", lambda m: unicodedata.normalize("NFC", m.group(1) + "\u0327"), t)
    return t


def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


WORD = re.compile(r"[A-Za-z]+")


def tokens_plain(t):
    """[(word, start_offset)] of a plain text."""
    out = []
    for m in re.finditer(r"[^\W\d_]+", t):
        w = strip_acc(m.group(0)).lower()
        if w:
            out.append((w, m.start()))
    return out


def tokens_latex(t):
    """[(word, start_offset)] of LaTeX: comments and control words are skipped."""
    out = []
    i = 0
    for m in re.finditer(r"%[^\n]*|\\[A-Za-z@]+|\\.|[^\W\d_]+", t):
        g = m.group(0)
        if g[0] in "%\\":
            continue
        out.append((strip_acc(g).lower(), m.start()))
    return out


def ocr_words(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    return [w for w, _ in tokens_plain(t)], t


# ---------------------------------------------------------------- aligner

class Draft:
    def __init__(self, name, files):
        self.name = name
        self.files = files  # [(label, text)]
        self.tok = []  # (word, file_index, offset)
        for fi, (_, text) in enumerate(files):
            toks = tokens_latex(text) if name == "ps" else tokens_plain(text)
            self.tok += [(w, fi, o) for w, o in toks]
        self.words = [w for w, _, _ in self.tok]
        # page markers (Pursuing Stacks) in token space: (token index of the first word after the marker, label)
        self.marks = []
        if name == "ps":
            import bisect
            keys = [(fi, o) for _, fi, o in self.tok]
            for fi, (_, text) in enumerate(files):
                for m in MARK.finditer(text):
                    self.marks.append((bisect.bisect_left(keys, (fi, m.start())), m.group(2) or m.group(1)))
            self.marks.sort()
        self.idx = collections.defaultdict(list)
        for i in range(len(self.words) - 2):
            self.idx[tuple(self.words[i:i + 3])].append(i)

    def align(self, pw):
        votes = []
        for j in range(len(pw) - 2):
            g = tuple(pw[j:j + 3])
            if any(len(x) < 2 for x in g):
                continue
            hits = self.idx.get(g, [])
            if 0 < len(hits) <= 3:
                votes += hits
        votes.sort()
        clusters, cur = [], []
        for v in votes:
            if cur and v - cur[-1] > 150:
                clusters.append(cur)
                cur = []
            cur.append(v)
        if cur:
            clusters.append(cur)
        clusters = [c for c in clusters if len(c) >= 3]
        return clusters, len(votes)

    def passage(self, c, widen=60):
        a = max(0, c[0] - widen)
        b = min(len(self.tok) - 1, c[-1] + 2 + widen)
        fa, oa = self.tok[a][1], self.tok[a][2]
        fb, ob = self.tok[b][1], self.tok[b][2]
        if fa != fb:  # passage crosses a file boundary: cut at the end of the first file
            text = self.files[fa][1]
            ob = len(text)
            fb = fa
        text = self.files[fa][1]
        oa = text.rfind("\n", 0, oa) + 1
        e = text.find("\n", ob)
        ob = len(text) if e < 0 else e
        l0 = text.count("\n", 0, oa) + 1
        l1 = text.count("\n", 0, ob) + 1
        return self.files[fa][0], l0, l1, text[oa:ob]


MARK = re.compile(r"\\(?:named)?pspage\{([^}]*)\}(?:\{([^}]*)\})?")


def main():
    ps_files = [(f"ps{k}.tex", (PS_SRC / f"ps{k}.tex").read_text(encoding="utf-8")) for k in range(1, 8)]
    circle = recompose_circle((BASE / "work" / "EsquisseFr.txt").read_text(encoding="utf-8"))
    (BASE / "work" / "EsquisseFr_recomposed.txt").write_text(circle, encoding="utf-8")
    drafts = {"ps": Draft("ps", ps_files), "esq": Draft("esq", [("EsquisseFr.pdf (text layer)", circle)])}
    rows = []
    for text, pages in (("ps", ps_pages()), ("esq", esq_pages())):
        D = drafts[text]
        for cote, site, kind in pages:
            p = OCR / cote / f"{site}.txt"
            if not p.exists():
                continue
            pw, raw = ocr_words(p)
            clusters, nv = D.align(pw)
            parts, labels, locs = [], [], []
            total = sum(len(c) for c in clusters)
            # keep clusters carrying at least 8 % of the votes (the main text, footnotes elsewhere in the draft)
            keep = [c for c in clusters if len(c) >= max(3, 0.08 * total)]
            for c in keep:
                fname, l0, l1, ptxt = D.passage(c)
                parts.append(f"%%% draft: {fname}, lines {l0}-{l1}\n{ptxt}")
                locs.append(f"{fname}:{l0}-{l1}")
                if text == "ps":
                    labels += [(m.group(2) or m.group(1)) for m in MARK.finditer(ptxt)]
            ts_vote = ""
            if text == "ps" and keep:
                big = max(keep, key=len)
                med = big[len(big) // 2]
                prev = [lab for ti, lab in D.marks if ti <= med]
                ts_vote = prev[-1] if prev else ""
            ngr = max(1, len(pw) - 2)
            score = round(total / ngr, 3)
            key = f"{text}_{cote}_{site:03d}"
            if parts:
                (OUT / "drafts_by_ocr" / f"{key}.txt").write_text("\n\n".join(parts), encoding="utf-8")
            rows.append({"key": key, "text": text, "cote": cote, "site": site, "pdf_page": site + 1, "kind": kind,
                         "ocr_words": len(pw), "votes": total, "score": score, "clusters": len(keep),
                         "draft_location": " ; ".join(locs), "pspage_markers_in_passage": " ".join(labels),
                         "ts_page_by_vote": ts_vote})
    with open(OUT / "ALIGNMENT_raw.tsv", "w", encoding="utf-8") as f:
        cols = list(rows[0])
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r[c]) for c in cols) + "\n")
    json.dump(rows, open(OUT / "alignment_raw.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(len(rows), "pages aligned")


if __name__ == "__main__":
    main()
