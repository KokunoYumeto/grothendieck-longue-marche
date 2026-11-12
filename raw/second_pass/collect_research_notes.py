"""Collect the research notes of every package into one file, in the manuscript's order (cote 140-2, 140-3, 140-4,
then the draft 140-1): for a package with a second pass, its checked notes (second_pass/<KEY>_notes_checked.md);
otherwise the research-notes section of Pro's notes file (from the heading that names research notes to the next
heading of the same level). Writes second_pass/ALL_RESEARCH_NOTES.md and prints sizes. Reads only."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
L = pathlib.Path(__file__).parent.parent
SP = L / "second_pass"
U = L / "answers" / "unzipped"
rows = []
for m in re.finditer(r"^\| (LM_[A-Z0-9-]+) \| cote (140-\d)[^|]*\| (\d+)[–-](\d+) \|", (L / "PACKAGES.md").read_text(
        encoding="utf-8"), re.M):
    rows.append((m.group(1), m.group(2), int(m.group(3)), int(m.group(4))))
keys = {r[0] for r in rows}
pilot = [(f"LM_P{n:02d}", "140-2", 10 * (n - 1) + 1, 10 * n) for n in range(1, 11)]
trial = [("LM_P068-069", "140-3", 91, 110), ("LM_P070-071", "140-3", 111, 130)]
order = {"140-2": 0, "140-3": 1, "140-4": 2, "140-1": 3}
allrows = [r for r in pilot if r[0] not in keys] + rows + [t for t in trial if t[0] not in keys]
allrows = [r for r in allrows if r[0] not in ("LM_P068", "LM_P069", "LM_P070", "LM_P071")]
allrows.sort(key=lambda r: (order[r[1]], r[2]))
HEAD = re.compile(r"^(#{2,3}) .*(research notes|notes de recherche|research note|implications|conjectures)", re.I | re.M)


def section(text):
    m = HEAD.search(text)
    if not m:
        return None
    level = len(m.group(1))
    nxt = re.compile(r"^#{2,%d} " % level, re.M)
    n = nxt.search(text, m.end())
    return text[m.start(): n.start() if n else len(text)]


out, total = [], 0
for k, cote, a, b in allrows:
    src, body = None, None
    chk = SP / f"{k}_notes_checked.md"
    if chk.exists():
        src, body = chk, chk.read_text(encoding="utf-8")
    else:
        cands = list((U / k).glob("*notes*.md")) if (U / k).exists() else []
        cands += [p for p in (L / "answers").glob(f"{k}_*.md")]
        for p in cands:
            s = section(p.read_text(encoding="utf-8"))
            if s:
                src, body = p, s
                break
    head = f"\n\n# {k} — cote {cote}, scans {a}–{b}"
    if body is None:
        out.append(head + "\n\n(no research notes found)")
        print(k, "none")
        continue
    out.append(head + f"  [source: {src.relative_to(L)}]\n\n" + body.strip())
    total += len(body)
    print(k, src.name, len(body))
(SP / "ALL_RESEARCH_NOTES.md").write_text("# La Longue Marche: all research notes, in manuscript order" + "".join(out) + "\n",
                                          encoding="utf-8")
print("total chars", total)
