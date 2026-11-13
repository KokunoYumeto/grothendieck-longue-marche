r"""Parse the batch results into per-page LaTeX files, the differences TSV, the notes, and the combined transcription
of each text (12 Nov 2026).

Per page: <textdir>/pages/<key>.tex = a header of LaTeX comments (source, page, model, batch) + the TRANSCRIPTION
section exactly as the model wrote it.
Per text: <textdir>/DIFFERENCES.tsv (key, cote, site, typescript page, class, draft, page, note), NOTES.tsv,
<textdir>/<text>_combined.tex: a compilable file with the macro definitions (preamble.tex) and every page in
archive order. In the combined file only, each \diagram{...} is rewritten as \begin{diagramblock}...\end{diagramblock}
(tikz-cd cannot be read inside a macro argument); the per-page files are untouched.
usage: python parse.py
"""
import csv
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
DIRS = {"ps": "pursuing_stacks", "esq": "esquisse", "ega25": "ega_v_cote25", "ega24": "ega_v_cote24_blass",
        # 13 Nov 2026: next texts (scripts/next_texts_20261113.py)
        "brown": "brown_translations_134-2", "mtl129": "montreal_seminar_129", "t162": "tapis_de_quillen_162-5",
        "esq119": "esquisse_copy2", "r119": "cote119_rest"}
NAMES = {"ps": "Pursuing Stacks (cotes 134-2 to 134-8)", "esq": "Esquisse d'un programme (cote 119, copy 1)",
         "ega25": "Nouveau EGA V (cote 25)", "ega24": "EGA V, English translation by P. Blass, 1987 (cote 24)",
         "brown": "R. Brown's translations of two letters to L. Breen, with his note and comments (cote 134-2)",
         "mtl129": "Notes of the Montreal seminar, 1970 (cote 129, typed part)",
         "t162": "Tapis de Quillen, with Quillen's offprint and preprint (cote 162-5, typed part)",
         "esq119": "Esquisse d'un programme (cote 119, copy 2)",
         "r119": "Cote 119: offprints, reports, courses, CV and letters (typed and printed part)"}
DIFF_TEXTS = ("ps", "esq", "brown", "esq119")  # texts with drafts: DIFFERENCES.tsv is written


def sections(text):
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^\s*%%%\s*(TRANSCRIPTION|DIFFERENCES|NOTES)\s*$", line)
        if m:
            cur = m.group(1)
            out[cur] = []
            continue
        if cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip("\n") for k, v in out.items()}


def results():
    """key -> (text, batch name, batch id); later batches override earlier ones."""
    runs = [json.loads(l) for l in (BASE / "RUNS.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    out = {}
    for r in runs:
        if r["event"] != "done":
            continue
        sub = [s for s in runs if s["event"] == "submitted" and s["batch_id"] == r["batch_id"]][0]
        idmap = {k.replace("-", "_").replace(".", "_")[:64]: k for k in sub["keys"]}
        okk = {q["key"] for q in r["requests"] if q.get("ok")}
        for line in (BASE / "batches" / r["name"] / "results.jsonl").read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            x = json.loads(line)
            k = idmap[x["custom_id"]]
            if k in okk:
                m = x["result"]["message"]
                out[k] = ("".join(c.get("text", "") for c in m["content"] if c.get("type") == "text"), r["name"],
                          r["batch_id"], r["ended"][:10])
    return out


def match_brace(s, i):
    """s[i] == '{'; return index after the matching '}'."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return len(s)


def diagrams_to_env(t):
    out, i = [], 0
    while True:
        k = t.find("\\diagram{", i)
        if k < 0:
            out.append(t[i:])
            return "".join(out)
        e = match_brace(t, k + len("\\diagram"))
        out.append(t[i:k] + "\\begin{diagramblock}" + t[k + len("\\diagram{"):e - 1] + "\\end{diagramblock}")
        i = e


def brace_balance(t):
    """number of unclosed { in LaTeX text (comments and \\{ \\} ignored); negative if } are in excess"""
    t = re.sub(r"(?<!\\)%[^\n]*", "", t)
    t = t.replace("\\{", "").replace("\\}", "")
    return t.count("{") - t.count("}")


def header(p, model_note):
    ts = f", typescript page {p['ts_page']}" if p["ts_page"] else ""
    return (f"% {NAMES[p['text']]}: archive cote {p['cote']}, site page {p['site']} (PDF page {p['pdf_page']}){ts}.\n"
            f"% {p['kind']}. Draft compared: {p['draft_location'] or 'none'}.\n% {model_note}\n")


def main():
    P = {p["key"]: p for p in json.load(open(BASE / "PAGES.json", encoding="utf-8"))}
    order = list(P)
    res = results()
    pre = (BASE / "scripts" / "preamble.tex").read_text(encoding="utf-8")
    summary = {}
    for text, dname in DIRS.items():
        d = BASE / dname
        keys = [k for k in order if P[k]["text"] == text and k in res]
        if not keys:
            continue
        (d / "pages").mkdir(parents=True, exist_ok=True)
        diffs, notes, body = [], [], []
        for k in keys:
            p = P[k]
            txt, bname, bid, date = res[k]
            sec = sections(txt)
            note = (f"AI-transcribed by Claude Opus 5.5 (claude-opus-5-5, adaptive thinking, effort high), Message "
                    f"Batches API, batch {bname} ({bid}), {date}; not yet checked by eye.")
            tex = header(p, note) + f"\\scanpage{{{p['cote']}/{p['site']}}}\n" + sec.get("TRANSCRIPTION", "") + "\n"
            (d / "pages" / f"{k}.tex").write_text(tex, encoding="utf-8")
            body.append(tex)
            for line in sec.get("DIFFERENCES", "").splitlines():
                line = line.strip().rstrip(",")
                if not line or line.lower() == "none" or not line.startswith("{"):
                    continue
                try:
                    j = json.loads(line)
                except Exception:  # noqa: BLE001
                    j = {"class": "UNPARSED", "draft": "", "page": "", "note": line}
                diffs.append([k, p["cote"], p["site"], p["ts_page"], j.get("class", ""), j.get("draft", ""),
                              j.get("page", ""), j.get("note", "")])
            nt = sec.get("NOTES", "").strip()
            lh = "yes" if re.search(r"LONG-HANDWRITING:\s*yes", nt, re.I) else "no"
            stats = {k2: len(re.findall(v, sec.get("TRANSCRIPTION", ""))) for k2, v in
                     (("unsure", r"\\unsure\{"), ("illegible", r"\\illegible\{"), ("hand", r"\\(hand|over|inserted|margin)\b"),
                      ("deleted", r"\\deleted\{"))}
            notes.append([k, p["cote"], p["site"], p["ts_page"], lh, stats["unsure"], stats["illegible"],
                          stats["hand"], stats["deleted"], nt.replace("\t", " ").replace("\n", " | ")])
        if text in DIFF_TEXTS:
            with open(d / "DIFFERENCES.tsv", "w", encoding="utf-8", newline="") as f:
                w = csv.writer(f, delimiter="\t", lineterminator="\n")
                w.writerow(["key", "cote", "site", "typescript_page", "class", "draft", "page", "note"])
                w.writerows(diffs)
        with open(d / "NOTES.tsv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["key", "cote", "site", "typescript_page", "long_handwriting", "n_unsure", "n_illegible",
                        "n_hand_macros", "n_deleted", "notes"])
            w.writerows(notes)
        fixed, fixes = [], []
        for k, b in zip(keys, body):
            bal = brace_balance(b)
            if bal > 0:
                b = b + f"\n% COMPILE FIX (combined file only): {bal} closing brace(s) added; the page's LaTeX leaves them open\n" + "}" * bal + "\n"
            elif bal < 0:
                b = "{" * (-bal) + f"% COMPILE FIX (combined file only): {-bal} opening brace(s) added\n" + b
            if bal:
                fixes.append((k, bal))
            fixed.append(diagrams_to_env(b))
        with open(d / "COMPILE_FIXES.tsv", "w", encoding="utf-8") as f:
            f.write("key\tbrace_balance_of_page\n" + "".join(f"{k}\t{v}\n" for k, v in fixes))
        comb = (pre.replace("@TITLE@", NAMES[text]) + "\n\\begin{document}\n\\maketitle\n\n" +
                "\n\\clearpage\n".join(fixed) + "\n\\end{document}\n")
        (d / f"{dname}_combined.tex").write_text(comb, encoding="utf-8")
        summary[text] = {"pages": len(keys), "differences": len(diffs),
                         "long_handwriting_pages": sum(1 for n in notes if n[4] == "yes")}
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
