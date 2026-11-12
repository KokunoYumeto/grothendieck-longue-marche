r"""PS_ARXIV_DIFF.tsv: every difference between the arXiv source of Pursuing Stacks (arXiv 2111.01000 v2,
pursuing_stacks_expert_20261110/src) and the faithful page transcription, keyed to the arXiv source, so that the
fixes can be carried into the translations made from the arXiv text (coordinator's request, 12 Nov 2026).

Source of the rows: pursuing_stacks/DIFFERENCES.tsv (the model's list per page, written after collating its own
transcription with the draft passage). For each row the arXiv text quoted by the model is located in the page's draft
passage (alignment/drafts/<key>.txt, which records file and line range) and so in the arXiv file:
  exact            the quoted arXiv text occurs verbatim in the passage; where it occurs more than once, the
                   occurrence at or after the previous row of the same page (rows come in page order, starting
                   300 characters before the page's \pspage marker) is taken, and the column says so;
  whitespace       it occurs once line breaks and runs of spaces are ignored;
  fuzzy:0.NN       best approximate match (difflib ratio >= 0.6); the quoted text may differ slightly from the source;
  context:0.NN     the row has no arXiv text (an omission or a handwritten note absent from the arXiv text): the
                   place is found by matching the page's reading, with its markup stripped, against the passage;
  not located      only the passage's line range is known.
Columns: arxiv_file, arxiv_line (first line of the match), arxiv_line_end, arxiv_section (nearest preceding
\label{sec:..} or sectioning title), paragraph (paragraph number within that section, counting blank-line-separated
blocks from the section start), arxiv_text (as quoted; the exact source text at the match is in arxiv_source_text),
page_reading, kind, kind_detail (the model's class), note, typescript_page (from the alignment),
page_number_on_scan (the \mspage{} of the transcription), last_arxiv_page_marker (the last \pspage or

amedpspage label before the line in the arXiv file, e.g. L.2 in the letter to Quillen), cote, site (scan page),
pdf_page, page_key, locate.
usage: python ps_arxiv_diff.py
"""
import bisect
import csv
import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(r"C:\Users\user\Documents\pursuing_stacks_expert_20261110\src")
KIND = {"wording": "wording", "formula": "formula", "omission": "omission", "addition": "addition",
        "silent-correction": "silent correction", "normalization": "normalization",
        "hand-unmarked": "handwritten note merged (unmarked in arXiv)",
        "hand-altered": "handwritten note rewritten in arXiv",
        "hand-missing": "handwritten note added on the page, absent from arXiv (or handwritten deletion not applied)",
        "struck-printed": "struck text printed in arXiv (handwritten deletion not applied)",
        "other": "other", "UNPARSED": "unparsed"}

_files = {}


def src(name):
    if name not in _files:
        t = (SRC / name).read_text(encoding="utf-8")
        lines = t.split("\n")
        starts = [0]
        for l in lines[:-1]:
            starts.append(starts[-1] + len(l) + 1)
        secs = []  # (line, section)
        for i, l in enumerate(lines, 1):
            m = re.search(r"\\label\{sec:([^}]*)\}", l)
            if m:
                secs.append((i, "§" + m.group(1)))
                continue
            m = re.search(r"\\(chapter|section|subsection|hangsection|subsubsection)\*?(?:\[[^\]]*\])?\{([^}]{0,60})", l)
            if m:
                secs.append((i, m.group(2).strip()))
        merged = []  # a sectioning title followed within 3 lines by its \label{sec:N} becomes "§N Title"
        for ln, s in secs:
            if merged and s.startswith("§") and not merged[-1][1].startswith("§") and ln - merged[-1][0] <= 3:
                merged[-1] = (merged[-1][0], s + " " + merged[-1][1])
            else:
                merged.append((ln, s))
        _files[name] = (t, lines, starts, merged)
    return _files[name]


def section_para(name, line):
    t, lines, starts, secs = src(name)
    k = bisect.bisect_right([s[0] for s in secs], line) - 1
    if k < 0:
        return "", ""
    s0 = secs[k][0]
    para, blank = 1, False
    for l in lines[s0:line - 1]:
        if not l.strip():
            blank = True
        elif blank:
            para += 1
            blank = False
    return secs[k][1], str(para)


def blocks(key):
    p = BASE / "alignment" / "drafts" / f"{key}.txt"
    if not p.exists():
        return []
    out = []
    for m in re.finditer(r"%%% draft: (\S+), lines (\d+)-(\d+)\n(.*?)(?=\n\n%%% draft: |\Z)", p.read_text(encoding="utf-8"), re.S):
        out.append((m.group(1), int(m.group(2)), m.group(4)))
    return out


def collapse(s):
    idx, out, prev_sp = [], [], False
    for i, c in enumerate(s):
        if c.isspace():
            if not prev_sp:
                out.append(" ")
                idx.append(i)
            prev_sp = True
        else:
            out.append(c)
            idx.append(i)
            prev_sp = False
    return "".join(out), idx


def strip_markup(s):
    s = re.sub(r"\\(deleted|xout)\{[^{}]*\}", "", s)
    s = re.sub(r"\\over\{[^{}]*\}\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\(hand|inserted|margin|uline|unsure)(\[[^\]]*\])?\{", "", s)
    s = re.sub(r"\\illegible\{\d+\}", "", s)
    return s.replace("}", "").replace("{", "")


def locate(query, bl, mode, cursor=None):
    """return (file, start_offset_in_file, end_offset_in_file, how). cursor = (block index, offset in block): the
    rows of a page come in page order, so an exact match at or after the previous row's place is preferred."""
    q = query.strip()
    if not q or not bl:
        return None
    ci, co = cursor if cursor else (0, 0)
    for bi, (fname, l0, text) in enumerate(bl):
        n = text.count(q)
        if n and mode == "draft":
            k = text.find(q, co) if bi == ci else -1
            if k < 0:
                k = text.find(q)
            base = src(fname)[2][l0 - 1]
            return fname, base + k, base + k + len(q), "exact" + ("" if n == 1 else f" ({n} occurrences in the passage; taken in page order)")
    qc, _ = collapse(q)
    for bi, (fname, l0, text) in enumerate(bl):
        tc, idx = collapse(text)
        n = tc.count(qc)
        if n and mode == "draft":
            k = -1
            if bi == ci:
                cc = next((j for j, x in enumerate(idx) if x >= co), len(idx))
                k = tc.find(qc, cc)
            if k < 0:
                k = tc.find(qc)
            base = src(fname)[2][l0 - 1]
            return fname, base + idx[k], base + idx[min(len(idx) - 1, k + len(qc) - 1)] + 1, "whitespace" + ("" if n == 1 else f" ({n} occurrences; taken in page order)")
    best = None
    for fname, l0, text in bl:
        tc, idx = collapse(text)
        sm = difflib.SequenceMatcher(None, tc, qc, autojunk=False)
        a, b, n = sm.find_longest_match(0, len(tc), 0, len(qc))
        if n < 3:
            continue
        st = max(0, a - b)
        win = tc[st:st + len(qc)]
        r = difflib.SequenceMatcher(None, win, qc, autojunk=False).ratio()
        if best is None or r > best[0]:
            base = src(fname)[2][l0 - 1]
            best = (r, fname, base + idx[st], base + idx[min(len(idx) - 1, st + max(1, len(win)) - 1)] + 1)
    if best and best[0] >= 0.6:
        return best[1], best[2], best[3], ("fuzzy" if mode == "draft" else "context") + ":%.2f" % best[0]
    return None


def line_of(fname, off):
    return bisect.bisect_right(src(fname)[2], off)


def main():
    rows = list(csv.DictReader(open(BASE / "pursuing_stacks" / "DIFFERENCES.tsv", encoding="utf-8"), delimiter="\t"))
    import json
    P = {p["key"]: p for p in json.load(open(BASE / "PAGES.json", encoding="utf-8"))}
    out = []
    stats = {}
    cur_key, cursor = None, None
    mspage = {}
    for r in rows:
        bl = blocks(r["key"])
        if r["key"] != cur_key:
            cur_key = r["key"]
            cursor = (0, 0)
            ts = P[r["key"]]["ts_page"]
            for bi, (fname, l0, text) in enumerate(bl):
                m = re.search(r"\\pspage\{%s\}" % re.escape(ts), text) if ts else None
                if m:
                    cursor = (bi, max(0, m.start() - 300))
        hit = locate(r["draft"], bl, "draft", cursor) if r["draft"].strip() else None
        if hit is None and r["page"].strip():
            pq = strip_markup(r["page"])
            if len(pq.strip()) >= 4:
                hit = locate(pq, bl, "context")
        if hit:
            fname, a, b, how = hit
            for bi, (bf, bl0, btext) in enumerate(bl):
                bbase = src(bf)[2][bl0 - 1]
                if bf == fname and bbase <= a <= bbase + len(btext):
                    cursor = (bi, a - bbase)
            l0, l1 = line_of(fname, a), line_of(fname, max(a, b - 1))
            sec, para = section_para(fname, l0)
            srctext = src(fname)[0][a:b]
        else:
            how = "not located"
            fname = bl[0][0] if bl else ""
            l0 = bl[0][1] if bl else ""
            l1 = (bl[0][1] + bl[0][2].count("\n")) if bl else ""
            sec, para = section_para(fname, l0) if bl else ("", "")
            srctext = ""
        stats[how.split(":")[0]] = stats.get(how.split(":")[0], 0) + 1
        p = P[r["key"]]
        if r["key"] not in mspage:
            tf = BASE / "pursuing_stacks" / "pages" / f"{r['key']}.tex"
            mm = re.findall(r"\\mspage\{([^}]*)\}", tf.read_text(encoding="utf-8")) if tf.exists() else []
            mspage[r["key"]] = " ; ".join(mm)
        marker = ""
        if fname and l0 != "":
            ft = src(fname)[0]
            ms = [m for m in re.finditer(r"\\(?:named)?pspage\{([^}]*)\}(?:\{([^}]*)\})?", ft)
                  if line_of(fname, m.start()) <= int(l0)]
            marker = (ms[-1].group(2) or ms[-1].group(1)) if ms else ""
        out.append({"arxiv_file": fname, "arxiv_line": l0, "arxiv_line_end": l1, "arxiv_section": sec,
                    "paragraph": para, "arxiv_text": r["draft"], "arxiv_source_text": srctext,
                    "page_reading": r["page"], "kind": KIND.get(r["class"], r["class"]), "kind_detail": r["class"],
                    "note": r["note"], "typescript_page": p["ts_page"], "page_number_on_scan": mspage[r["key"]],
                    "last_arxiv_page_marker": marker, "cote": p["cote"], "site": p["site"],
                    "pdf_page": p["pdf_page"], "page_key": r["key"], "locate": how})
    cols = list(out[0])
    with open(BASE / "PS_ARXIV_DIFF.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for o in out:
            w.writerow({k: (str(v).replace("\t", " ").replace("\r", " ").replace("\n", "\\n")) for k, v in o.items()})
    print(len(out), "rows;", stats)


if __name__ == "__main__":
    main()
