#!/usr/bin/env python3
"""Rerender after the A.23 status-prose correction and compare inspected pixels.

This records which previously viewed sample pages changed. It does not
perform or certify visual inspection.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
renders = root / 'build' / 'renders'
before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
          for p in renders.glob('page_*.png')}
with (root/'build'/'rerender_checkpoint03.log').open('w') as stream:
    subprocess.run([sys.executable, str(root/'code'/'render_pdf_qa.py')],
                   cwd=root, stdout=stream, stderr=subprocess.STDOUT,
                   check=True)
after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
         for p in renders.glob('page_*.png')}
result = {
    'old_rendered_pages': len(before),
    'new_rendered_pages': len(after),
    'changed_or_new_pages': [p for p in sorted(after)
                             if before.get(p) != after[p]],
    'unchanged_pages': [p for p in sorted(after)
                        if before.get(p) == after[p]],
    'visual_approval_recorded': False,
}
(root/'research'/'checkpoint03_rerender_comparison.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
