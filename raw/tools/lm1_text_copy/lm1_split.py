"""Split the text copy of the LM1_GROUP_SCHEMES chat (11 Nov 2026, 21:03 UTC) into the files it delivers.

Usage: python -I lm1_split.py <text copy> <output folder> <log.json>
Each file starts at the line that names it. Its content is the line range given below (1-based, inclusive). The
lines outside the ranges are the chat around the files: the lines naming each file, the ChatGPT status lines
("Checked ...", "Prepared ...", "Searching ..."), and Pro's short messages between files (with mathematics copied
as rendered text). Two files open with one sentence of Pro's message before the code (build_reconstruction.py,
integrate_and_build_recovery.py); those sentences are left out of the files too. The ranges were set by reading
every boundary. Every line from 401 to the end is accounted for: name line, content, or left out (listed in the log).
Files are written in UTF-8 with LF line ends and a final newline. Nothing else is changed.
"""
import hashlib
import json
import os
import sys

FILES = [  # (relative path, line naming it, first content line, last content line)
    ("LM1_GROUP_SCHEMES_paper.tex", 401, 402, 511),
    ("sections/00_conventions.tex", 512, 513, 620),
    ("sections/A.tex", 625, 626, 1047),
    ("sections/B.tex", 1076, 1077, 1861),
    ("sections/F.tex", 1917, 1918, 2100),
    ("code/ab_reconstructed.js", 2105, 2106, 2203),
    ("code/ab_reconstructed.out", 2204, 2205, 2218),
    ("sections/C.tex", 2219, 2220, 2793),
    ("sections/D.tex", 2800, 2801, 3706),
    ("sections/E.tex", 3715, 3716, 4823),
    ("code/c_replacement.js", 4830, 4831, 4883),
    ("code/c_replacement.out", 4884, 4885, 4885),
    ("code/d_reconstructed.js", 4886, 4887, 5028),
    ("code/d_reconstructed.out", 5029, 5030, 5030),
    ("code/e_arithmetic_replacement.js", 5036, 5037, 5204),
    ("code/e_arithmetic_replacement.out", 5205, 5206, 5206),
    ("code/e_groups_replacement.js", 5207, 5208, 5245),
    ("code/e_groups_replacement.out", 5246, 5247, 5247),
    ("code/e_fermat.js", 5248, 5249, 5310),
    ("code/e_fermat.out", 5311, 5312, 5325),
    ("code/e_additional.py", 5328, 5329, 5439),
    ("results.csv", 5450, 5451, 5548),
    ("readings.csv", 5551, 5552, 5609),
    ("LM1_GROUP_SCHEMES_references.bib", 5616, 5617, 5805),
    ("report.md", 5812, 5813, 5959),
    ("build_reconstruction.py", 5970, 5973, 6135),
    ("code/e_additional.out", 6190, 6191, 6216),
    ("sections/C12_addendum.tex", 6304, 6305, 6513),
    ("evidence/C12_references.bib", 6514, 6515, 6562),
    ("evidence/C12_result.json", 6563, 6564, 6573),
    ("RECOVERY_UPDATE.md", 6576, 6577, 6708),
    ("integrate_and_build_recovery.py", 6709, 6712, 7193),
]

src, out_dir, log_path = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(src, encoding="utf-8").read().split("\n")
n_lines = len(lines)
used = {}
record = {"source": src, "source_lines": n_lines,
          "source_sha256": hashlib.sha256(open(src, "rb").read()).hexdigest(), "files": [], "left_out": []}
for rel, name_line, a, b in FILES:
    assert lines[name_line - 1].strip() == rel, (name_line, lines[name_line - 1], rel)
    assert name_line < a <= b, rel
    for n in [name_line] + list(range(a, b + 1)):
        assert n not in used, (n, rel, used.get(n))
        used[n] = rel
    text = "\n".join(lines[a - 1:b]) + "\n"
    data = text.encode("utf-8")
    p = os.path.join(out_dir, rel)
    os.makedirs(os.path.dirname(p) or out_dir, exist_ok=True)
    assert not os.path.exists(p), "exists: " + p
    open(p, "wb").write(data)
    record["files"].append({"file": rel, "name_line": name_line, "lines": [a, b], "n_lines": b - a + 1,
                            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
# every line from the first name line to the end is a name line, content, or left out
run = None
for n in range(FILES[0][1], n_lines + 1):
    if n in used:
        if run:
            record["left_out"].append(run)
            run = None
        continue
    if run is None:
        run = {"lines": [n, n], "text": []}
    run["lines"][1] = n
    run["text"].append(lines[n - 1])
if run:
    record["left_out"].append(run)
record["left_out_lines"] = sum(r["lines"][1] - r["lines"][0] + 1 for r in record["left_out"])
json.dump(record, open(log_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("files written:", len(record["files"]), " content lines:", sum(f["n_lines"] for f in record["files"]),
      " left out:", record["left_out_lines"], "lines in", len(record["left_out"]), "runs;",
      " lines before the first file (chat, kept only in the text copy):", FILES[0][1] - 1)
