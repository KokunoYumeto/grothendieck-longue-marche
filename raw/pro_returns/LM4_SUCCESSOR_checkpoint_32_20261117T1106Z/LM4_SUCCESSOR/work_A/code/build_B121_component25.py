#!/usr/bin/env python3
"""Build the isolated B121 proposal and preserve all actual pass outputs."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
stage = sys.argv[1] if len(sys.argv) > 1 else "initial"
qa = Path("/tmp/LM4_B121_QA")
qa.mkdir(parents=True, exist_ok=True)
wrapper = (ROOT / "work_A/qa_templates/component_article.tex").read_text().replace("B102", "B121")
wrapper = wrapper.replace("\\bibliographystyle{plainnat}\n", "")
wrapper = wrapper.replace("\\bibliography{B121_reference}\n", "")
(qa / "B121_qa.tex").write_text(wrapper)
shutil.copy2(ROOT / "work_A/B121_final_neck_retraction_proposed.tex",
             qa / "B121.tex")
env = os.environ.copy()
env.update(json.loads((ROOT.parent / "tex_runtime/env.json").read_text()))
for number in range(3):
    output = ROOT / f"work_A/B121_component_{stage}_pass{number}.out"
    with output.open("wb") as handle:
        result = subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "B121_qa.tex"],
            cwd=qa, env=env, stdout=handle, stderr=subprocess.STDOUT)
    print(f"pass {number}: exit {result.returncode}; {output.relative_to(ROOT)}", flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
shutil.copy2(qa / "B121_qa.pdf", ROOT / "work_A/B121_component.pdf")
print("PASS isolated B121 PDF copied.", flush=True)
