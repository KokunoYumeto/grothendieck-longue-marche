#!/usr/bin/env python3
"""Record actual final build diagnostics and bind them to frozen sources."""
from pathlib import Path
import hashlib
import json
import re
import fitz

ROOT = Path(__file__).resolve().parents[1]
state_path = ROOT / 'notes/checkpoint16_frozen_state.json'
state = json.loads(state_path.read_text())
frozen = json.loads((ROOT / 'notes/checkpoint16_frozen_source_hashes.json').read_text())
for path, digest in frozen.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
pdf = (ROOT/'LM8_PUSH_paper.pdf').read_bytes()
assert pdf == (ROOT/'build/LM8_PUSH_paper.pdf').read_bytes()
log = (ROOT/'build/LM8_PUSH_paper.log').read_text()
console = (ROOT/'build/build_console.out').read_text()
blg = (ROOT/'build/LM8_PUSH_paper.blg').read_text()
with fitz.open(stream=pdf, filetype='pdf') as doc:
    pages = len(doc)
record = {
    'paper_pages': pages, 'pdf_bytes': len(pdf), 'pdf_sha256': hashlib.sha256(pdf).hexdigest(),
    'all_pass_overfull': re.findall(r'Overfull \\hbox \((\d+(?:\.\d+)?)pt',console),
    'final_overfull': re.findall(r'Overfull \\hbox \((\d+(?:\.\d+)?)pt',log),
    'final_warnings': log.count('Warning'), 'final_undefined': log.count('undefined'),
    'final_missing_characters': log.count('Missing character'),
    'bibtex_warnings': [line for line in blg.splitlines() if line.startswith('Warning--')],
    'used_bibliography_entries': (ROOT/'build/LM8_PUSH_paper.bbl').read_text().count(r'\bibitem'),
}
record['status'] = 'PASS' if not (record['final_overfull'] or record['final_warnings'] or record['final_undefined'] or record['final_missing_characters']) else 'NEEDS_REVIEW'
(ROOT/'notes/checkpoint16_final_build.json').write_text(json.dumps(record,indent=2)+'\n')
state.update({k:record[k] for k in ['paper_pages','pdf_bytes','pdf_sha256']})
state_path.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps(record,indent=2))
