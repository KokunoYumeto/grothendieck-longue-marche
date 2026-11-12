"""Close of the second pass (12 Nov 2026): coverage, compile check and the index of current texts.
For every package of PACKAGES.md that is not superseded (P068-P071 by P068-069 and P070-071; P072-P160 by the C3/C4/C1
packages of 19 images), find the current text (second_pass/PKG_checked_fixed.tex, else PKG_checked.tex; LM_P057 has
only the second pass of its API first pass, LM_P057api), compile it in the check wrapper (answers/fixed/build/wrap.tex,
LuaLaTeX) unless --nocompile, and count the changes and unresolved places of its _changes.md.
Writes second_pass/CURRENT_TEXT_INDEX.tsv and work_close_20261112/coverage.tsv.
Counting: changes = data rows of the tables before the unresolved section; unresolved = top-level items (list items,
numbered items, table data rows) in the section whose level-2 heading mentions "unresolved", or the number the heading
states when it states one. usage: python -I build_index.py [--nocompile | --reuselogs]"""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
SP = W.parent
L = SP.parent
COMPILE = "--nocompile" not in sys.argv
REUSE = "--reuselogs" in sys.argv
RETRY = {}
for _f in sorted(W.glob("retry_failed_run*.tsv")):
    for _l in _f.read_text(encoding="utf-8").splitlines()[1:]:
        _k, _cur, _alt, _rep = _l.split("\t")
        RETRY[_k] = _rep
rows = re.findall(r"^\| (LM_[A-Z0-9-]+) \| (cote 140-\d)[^|]*\| (\d+)[–-](\d+) \| (\d+) \|",
                  (L / "PACKAGES.md").read_text(encoding="utf-8"), re.M)
pk = {}
for key, cote, a, b, n in rows:
    m = re.match(r"LM_P(\d+)$", key)
    if m and len(m.group(1)) == 3 and 68 <= int(m.group(1)) <= 160:
        continue  # superseded
    pk[key] = (cote, int(a), int(b), int(n))
pk["LM_P068-069"] = ("cote 140-3", 91, 110, 20)
pk["LM_P070-071"] = ("cote 140-3", 111, 130, 20)


def order(k):
    c = {"cote 140-1": 1, "cote 140-2": 2, "cote 140-3": 3, "cote 140-4": 4}[pk[k][0]]
    return (c, pk[k][1])


def counts(md):
    """changes, unresolved, basis"""
    lines = md.read_text(encoding="utf-8").splitlines()
    ch, sec, stated, sub, items, intro = 0, "pre", None, 0, [], []
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            if re.search(r"unresolved", ln, re.I):
                sec = "unres"
                m = re.search(r"\((\d+)(?: places?)?\)", ln)
                stated = int(m.group(1)) if m else None
            elif sec == "unres":
                sec = "post"
            continue
        if sec == "unres" and ln.startswith("### "):
            m = re.search(r"\((\d+)\)", ln)
            sub += int(m.group(1)) if m else 0
            continue
        if ln.startswith("|"):
            if re.match(r"^\|\s*:?-{3,}", ln):
                continue
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if re.match(r"^\|\s*:?-{3,}", nxt):
                continue  # header row
            if sec == "pre":
                ch += 1
            elif sec == "unres":
                items.append(("row", ln))
            continue
        if sec == "unres":
            if re.match(r"^(?:[-*] |\d+[.)] )", ln):
                items.append(("item", ln))
            elif ln.strip() and items and items[-1][0] == "item" and ln.startswith((" ", "\t")):
                items[-1] = ("item", items[-1][1] + " " + ln.strip())
            elif ln.strip() and not items:
                intro.append(ln)
    if stated is None:
        m = re.search(r"\((\d+) places?\)|(\d+) places", " ".join(intro))
        if m:
            stated = int(m.group(1) or m.group(2))
    if stated is not None:
        return ch, stated, "stated in the file"
    if sub:
        return ch, sub, "stated in the file (subsections)"
    n, per = 0, False
    for kind, txt in items:
        m = re.match(r"^(?:[-*]|\d+[.)])\s+(?:\*\*)?(?:[Ss]cans?\s*)?\d+(?:\*\*)?\s*\((\d+)\)\s*(?:\*\*)?:", txt)
        if m and int(m.group(1)) <= 30:
            n += int(m.group(1))
            per = True
        elif kind == "row" or re.match(r"^\d+[.)] ", txt):
            n += 1
        else:
            n += 1 + txt.count(";")
    return ch, n, "per-scan counts in the file" if per else "counted (numbered items or rows; bullet items split at ;)"

def compile_ok(key, body):
    bd = W / "build"
    if REUSE and (bd / f"{key}.log").exists():
        log = (bd / f"{key}.log").read_text(encoding="utf-8", errors="replace")
        m = re.search(r"Output written on .*?\((\d+) page", log)
        return ("OK", m.group(1)) if m else ("FAIL " + (re.findall(r"^! .*", log, re.M) or [""])[0], "")
    bd.mkdir(exist_ok=True)
    wrap = (L / "answers" / "fixed" / "build" / "wrap.tex").read_text(encoding="utf-8")
    (bd / f"{key}.tex").write_text(wrap.replace("BODYFILE", body.as_posix()), encoding="utf-8")
    subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", f"{key}.tex"], cwd=bd,
                   capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
    log = (bd / f"{key}.log").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"Output written on .*?\((\d+) page", log)
    err = (re.findall(r"^! .*", log, re.M) or [""])[0]
    for ext in (".aux", ".pdf"):
        (bd / f"{key}{ext}").unlink(missing_ok=True)
    return ("OK", m.group(1)) if m else ("FAIL " + err, "")


out = ["package\tcote\tscans\timages\tcurrent_text\tfixed\tchanges\tunresolved\tunresolved_basis\tunsure_marks\tillegible_marks\tchanges_file\tnotes_file\tcompile\tpages"]
cov = []
for k in sorted(pk, key=order):
    cote, a, b, n = pk[k]
    base = "LM_P057api" if k == "LM_P057" else k
    f = SP / f"{base}_checked_fixed.tex"
    fixed = f.exists()
    if not fixed:
        f = SP / f"{base}_checked.tex"
    if not f.exists():
        cov.append(f"{k}\tMISSING")
        out.append(f"{k}\t{cote[5:]}\t{a}-{b}\t{n}\tMISSING" + "\t" * 11)
        print(k, "MISSING")
        continue
    md, nt = SP / f"{base}_changes.md", SP / f"{base}_notes_checked.md"
    ch, unv, basis = counts(md) if md.exists() else ("", "", "no changes file")
    t = f.read_text(encoding="utf-8")
    nus, nil = t.count("\\unsure{"), t.count("\\illegible{")
    scans_in = sorted({int(x) for x in re.findall(r"\\scanpage\{(\d+)", t)})
    gap = [s for s in range(a, b + 1) if s not in scans_in]
    st, pages = compile_ok(k, f) if COMPILE else ("not compiled", "")
    if st.startswith("FAIL") and k in RETRY and RETRY[k].startswith("OK"):
        st, pages = "OK after the reader build's mechanical LaTeX repairs", RETRY[k].split()[1]
    out.append(f"{k}\t{cote[5:]}\t{a}-{b}\t{n}\tsecond_pass/{f.name}\t{'yes' if fixed else 'no'}\t{ch}\t{unv}\t{basis}\t{nus}\t{nil}\t"
               f"second_pass/{md.name if md.exists() else ''}\tsecond_pass/{nt.name if nt.exists() else ''}\t{st}\t{pages}")
    cov.append(f"{k}\t{f.name}\t{st}\t{pages}\tscanpages missing: {gap if gap else 'none'}\tunresolved {unv} ({basis})")
    print(k, f.name, st, pages, "missing scanpages:", gap, "| ch", ch, "un", unv, basis, flush=True)
(SP / "CURRENT_TEXT_INDEX.tsv").write_text("\n".join(out) + "\n", encoding="utf-8")
(W / "coverage.tsv").write_text("\n".join(cov) + "\n", encoding="utf-8")
print("packages:", len(pk))




