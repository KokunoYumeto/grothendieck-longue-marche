"""Assemble the independently audited F fragments; verify structural metadata."""
from pathlib import Path
import csv
import re

base = Path(__file__).resolve().parents[1]
source = (base / "F.tex").read_text()
source = source.replace(
    "The construction uses inversion of $2$ and $3$; nothing here asserts",
    (base / "F23_old_kernel.tex").read_text() + "\n\n"
    + "The construction uses inversion of $2$ and $3$; nothing here asserts",
    1,
)
source = source.replace(
    r"\subsection{Additional arithmetic tests and coherent limits}",
    (base / "F_local.tex").read_text() + "\n\n"
    + r"\subsection{Additional arithmetic tests and coherent limits}",
    1,
)
source = source.replace(
    r"\paragraph{F.43 (Proved).",
    (base / "F_invariance.tex").read_text() + "\n\n"
    + r"\paragraph{F.43 (Proved).",
    1,
)
point_map = base / "F44_point_map.tex"
if point_map.exists():
    source += "\n\n" + point_map.read_text()
general_reconstruction = base / "F47.tex"
if general_reconstruction.exists():
    source += "\n\n" + general_reconstruction.read_text()

rows = list(csv.DictReader((base / "results.csv").open()))
by_id = {row["id"]: row for row in rows}
pattern = re.compile(r"\\paragraph\{(F\.\d+) \(")
ids = [m.group(1) for m in pattern.finditer(source)]
assert ids == [f"F.{i}" for i in range(1, len(rows) + 1)], ids

def tex_escape(s):
    table = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
             "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
             "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(table.get(c, c) for c in s)

for match in reversed(list(pattern.finditer(source))):
    start = source.index("{", match.start())
    depth, end = 0, None
    for i in range(start, len(source)):
        if i and source[i - 1] == "\\":
            continue
        if source[i] == "{":
            depth += 1
        elif source[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    assert end is not None
    passage = by_id[match.group(1)]["manuscript_passages (section; folio; scan)"]
    marker = "\n\\textit{Manuscript: " + tex_escape(passage) + ".}\n"
    source = source[:end] + marker + source[end:]

begins = source.count(r"\begin{proof}")
ends = source.count(r"\end{proof}")
assert begins == ends, (begins, ends)
(base / "F_assembled.tex").write_text(source)

bib_sources = [base / name for name in
               ("references.bib", "local_refs.bib", "invariance_refs.bib",
                "F44_centralizer_refs.bib")]
bib_sources.append(base.parent / "foundations" / "cyclotomic_references.bib")
bib = "\n\n".join(p.read_text().rstrip() for p in bib_sources) + "\n"
keys = re.findall(r"(?m)^@\w+\{([^,]+),", bib)
assert len(keys) == len(set(keys)), keys
(base / "references_all.bib").write_text(bib)
print("Statements in numerical order:", len(ids))
print("Balanced proof environments:", begins)
print("One manuscript marker per statement:", len(ids))
print("Unique bibliography keys:", len(keys))
print("Assembly written to:", base / "F_assembled.tex")
