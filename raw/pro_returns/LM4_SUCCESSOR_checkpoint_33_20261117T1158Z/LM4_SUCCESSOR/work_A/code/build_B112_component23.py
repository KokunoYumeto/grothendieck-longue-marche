#!/usr/bin/env python3
"""Private B112 component build; preserve each real pass output."""
from pathlib import Path
import os
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
stage = sys.argv[1] if len(sys.argv) > 1 else 'initial'
qa = Path('/tmp/LM4_B112_QA')
qa.mkdir(parents=True, exist_ok=True)
wrapper = Path('/tmp/LM4_B102_QA/B102_qa.tex').read_text().replace('B102', 'B112')
(qa / 'B112_qa.tex').write_text(wrapper)
shutil.copy2(ROOT / 'work_A/B112_annular_centralizer.tex', qa / 'B112.tex')
shutil.copy2(ROOT / 'sections/b_sources.bib', qa / 'B112_reference.bib')
commands = [
    ['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'B112_qa.tex'],
    ['bibtex', 'B112_qa'],
    ['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'B112_qa.tex'],
    ['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'B112_qa.tex'],
]
env = os.environ.copy()
env.update(json.loads((ROOT.parent / 'tex_runtime/env.json').read_text()))
for i, command in enumerate(commands):
    output = ROOT / f'work_A/B112_component_{stage}_pass{i}.out'
    with output.open('wb') as handle:
        completed = subprocess.run(command, cwd=qa, env=env, stdout=handle,
                                   stderr=subprocess.STDOUT)
    print(f'pass {i}: exit {completed.returncode}; {output.relative_to(ROOT)}', flush=True)
    if completed.returncode:
        raise SystemExit(completed.returncode)
shutil.copy2(qa / 'B112_qa.pdf', ROOT / 'work_A/B112_component.pdf')
print('PASS private component PDF copied.', flush=True)
