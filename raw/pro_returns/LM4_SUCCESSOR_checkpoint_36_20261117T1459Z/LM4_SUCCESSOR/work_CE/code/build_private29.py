#!/usr/bin/env python3
"""Preserving three-pass private build in the agreed clean TeX environment."""
from pathlib import Path
import json, os, subprocess, sys
ROOT = Path(__file__).resolve().parents[2]
label = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
assert label in ('B139', 'B140')
qa = ROOT/'work_CE'/('qa_'+label)
env = os.environ.copy()
env.update(json.loads((ROOT/'records/checkpoint25_tex_env.json').read_text()))
for n in range(start, start+3):
    out, err = qa/('build%d.out'%n), qa/('build%d.err'%n)
    assert not out.exists() and not err.exists()
    with out.open('w') as stdout, err.open('w') as stderr:
        result = subprocess.run(
            ['lualatex', '-interaction=nonstopmode', '-halt-on-error',
             '-output-directory='+str(qa), str(qa/(label+'_check.tex'))],
            cwd=ROOT, env=env, stdout=stdout, stderr=stderr)
    log = qa/(label+'_check.log')
    if log.exists(): (qa/('build%d.log'%n)).write_bytes(log.read_bytes())
    print(label, 'pass', n, 'exit', result.returncode, flush=True)
    if result.returncode: sys.exit(result.returncode)
