"""Split ALL_RESEARCH_NOTES.md into note blocks (a heading of level 3-5 or a bold-led bullet, with the text up to the next
one), classify each by the kind it states, and write three reading files in manuscript order:
  NOTES_A_conjectures.md  Grothendieck's conjectures, questions, expectations, announced programme (full block, cut at 1200)
  NOTES_B_implications.md unpursued implications (cut at 500)
  NOTES_C_claims_ideas.md unproved claims and the model's own ideas (cut at 300)
Notes marked dropped by a second pass are left out of A and B. Reads only; prints counts and sizes."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).parent
t = (SP / "ALL_RESEARCH_NOTES.md").read_text(encoding="utf-8")
parts = re.split(r"\n(?=# LM_)", t)
START = re.compile(r"^(#{3,5} |- \*\*|\d+\. \*\*|\*\*[A-Z]{0,3}[ -]?\d)")
A, B, C, other = [], [], [], 0


def kind_of(s):
    h = s[:400].lower()
    if re.search(r"own idea|second pass[^.]{0,40}own|claude, second pass", h):
        return "C"
    if re.search(r"conjectur|question|expect|programme|program|research plan|work announced|announced next", h):
        return "A"
    if re.search(r"implication", h):
        return "B"
    if re.search(r"claim|without proof", h):
        return "C"
    return None


for p in parts[1:]:
    head, _, body = p.partition("\n")
    if "(no research notes found)" in body[:200]:
        continue
    pkg = head.lstrip("# ").split("  [source")[0]
    blocks, cur = [], None
    for line in body.split("\n"):
        if START.match(line.strip()):
            if cur:
                blocks.append(cur)
            cur = [line.strip()]
        elif cur is not None:
            cur.append(line.strip())
    if cur:
        blocks.append(cur)
    for b in blocks:
        s = re.sub(r"\s+", " ", " ".join(x for x in b if x)).strip()
        k = kind_of(s)
        if k is None:
            other += 1
            continue
        dropped = bool(re.search(r"\bdrop(ped)?\b", s[:200].lower()))
        if k == "A" and not dropped:
            A.append((pkg, s[:1200]))
        elif k == "B" and not dropped:
            B.append((pkg, s[:500]))
        elif k == "C":
            C.append((pkg, s[:300]))


def write(name, items, title):
    out, last = [f"# {title}"], None
    for pkg, s in items:
        if pkg != last:
            out.append(f"\n## {pkg}")
            last = pkg
        out.append("- " + s)
    (SP / name).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(name, len(items), "notes,", sum(len(s) for _, s in items), "chars")


write("NOTES_A_conjectures.md", A, "La Longue Marche: Grothendieck's conjectures, questions, expectations and programme")
write("NOTES_B_implications.md", B, "La Longue Marche: unpursued implications")
write("NOTES_C_claims_ideas.md", C, "La Longue Marche: unproved claims and the model's own ideas")
print("unclassified blocks:", other)
