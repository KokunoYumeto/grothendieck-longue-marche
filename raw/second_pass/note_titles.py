"""From second_pass/ALL_RESEARCH_NOTES.md, write a compact map: for each package (in manuscript order) every note's
heading or bold label with the start of its text, one line per note, at most WIDTH characters. Writes
second_pass/ALL_NOTES_MAP.md and prints the number of notes and the size. Reads only."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).parent
WIDTH = 230
t = (SP / "ALL_RESEARCH_NOTES.md").read_text(encoding="utf-8")
parts = re.split(r"\n(?=# LM_)", t)
out, n = ["# La Longue Marche: map of all research notes (one line per note), manuscript order"], 0
for p in parts[1:]:
    head, _, body = p.partition("\n")
    if "(no research notes found)" in body[:200]:
        continue
    out.append("\n## " + head.lstrip("# ").split("  [source")[0])
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        item = None
        if re.match(r"^#{3,5} ", l):
            nxt = ""
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and not lines[j].lstrip().startswith("#"):
                nxt = lines[j].strip()
            item = re.sub(r"^#+ ", "", l) + " :: " + nxt
        elif re.match(r"^(- |\d+\. )\*\*", l):
            item = re.sub(r"^(- |\d+\. )", "", l)
        if item:
            item = re.sub(r"\s+", " ", item)
            out.append("- " + (item[:WIDTH] + ("…" if len(item) > WIDTH else "")))
            n += 1
        i += 1
(SP / "ALL_NOTES_MAP.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("notes:", n, "chars:", sum(len(x) for x in out))
