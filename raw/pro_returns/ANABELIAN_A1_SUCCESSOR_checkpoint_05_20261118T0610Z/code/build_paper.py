"""Reproducible LuaLaTeX/BibTeX build with local LuaTeX support libraries."""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess

W = Path(__file__).resolve().parents[1]
B = W / "build"
R = W / "code/tex_runtime"
B.mkdir(exist_ok=True)
env = dict(os.environ)
env.update({
    "TEXMF": "{" + str(R / "vendor") + ",/usr/share/texlive/texmf-dist,/usr/share/texmf}",
    "TEXMFVAR": str(B / "runtime/var"),
    "TEXMFCONFIG": str(B / "runtime/config"),
    "TEXMFCACHE": "tex_cache",
    "LUAOTFLOAD_CACHE": "tex_cache",
    "TEXFORMATS": str(B) + "//:",
    "TEXINPUTS": ".:" + str(R / "vendor") + "//:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:",
    "LUAINPUTS": ".:" + str(R / "vendor") + "//:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:",
    "TEXFONTMAPS": str(R / "maps") + "//:/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:",
    "BIBINPUTS": str(W) + ":",
    "BSTINPUTS": "/usr/share/texlive/texmf-dist/bibtex/bst//:",
})
for p in [B / "runtime/var", B / "runtime/config", W / "tex_cache"]:
    p.mkdir(parents=True, exist_ok=True)

def run(args, name, cwd=W):
    with (B / name).open("w") as out:
        result = subprocess.run(args, cwd=cwd, env=env, stdout=out, stderr=subprocess.STDOUT)
    if result.returncode:
        print((B / name).read_text()[-6000:])
        raise SystemExit(result.returncode)

if not (B / "lualatex.fmt").exists():
    run(["luahbtex", "--ini", "--jobname=lualatex", "--progname=lualatex", "lualatex.ini"], "format_build.out", B)
stem = "ANABELIAN_A1_SUCCESSOR_paper"
args = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", stem + ".tex"]
run(args, "latex_pass1.out")
run(["bibtex", stem], "bibtex.out", B)
run(args, "latex_pass2.out")
run(args, "latex_pass3.out")
log = (B / (stem + ".log")).read_text()
over = [float(x) for x in re.findall(r"Overfull \\hbox \(([0-9.]+)pt", log)]
report = {
    "engine": "LuaHBTeX 1.18.0; LaTeX2e 2024-11-01",
    "passes": 3,
    "undefined_citations": "There were undefined citations" in log,
    "undefined_references": "There were undefined references" in log,
    "missing_characters": re.findall(r"Missing character:[^\n]*", log),
    "overfull_hboxes_pt": over,
    "overfull_above_2pt": [x for x in over if x > 2],
    "pdf_bytes": (B / (stem + ".pdf")).stat().st_size,
}
(B / "BUILD_STATUS.json").write_text(json.dumps(report, indent=2) + "\n")
shutil.copy2(B / (stem + ".pdf"), W / (stem + ".pdf"))
print(json.dumps(report))
