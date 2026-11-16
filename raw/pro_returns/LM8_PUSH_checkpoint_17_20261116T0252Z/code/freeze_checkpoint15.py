#!/usr/bin/env python3
"""Freeze the audited manuscript and compare every active statement to CSV."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import re
import zipfile

root = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((root / 'LM8_PUSH_results.csv').open()))
assert len(rows) == len({r['id'] for r in rows})
active = []
seen = set()
statements = []

def visit(path):
    path = path.resolve()
    assert path.is_relative_to(root)
    assert path not in seen, 'Duplicate active input: ' + str(path)
    seen.add(path)
    active.append(path.relative_to(root).as_posix())
    source = re.sub(r'(?m)(?<!\\)%.*$', '', path.read_text())
    controls = [(i, ord(c)) for i, c in enumerate(source)
                if ord(c) < 32 and c not in '\n\t']
    assert not controls, (path, controls)
    for m in re.finditer(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}', source):
        statements.append({'id': m[1], 'status': m[2],
                           'source': path.relative_to(root).as_posix()})
    for name in re.findall(r'\\input\{([^}]+)\}', source):
        target = root / name
        if not target.suffix:
            target = target.with_suffix('.tex')
        visit(target)

visit(root / 'LM8_PUSH_paper.tex')
assert len(statements) == len({s['id'] for s in statements})
assert {s['id']: s['status'] for s in statements} == {
    r['id']: r['status'] for r in rows}
with zipfile.ZipFile(root.parent / 'LM8_PUSH_checkpoint_14.zip') as old:
    previous = list(csv.DictReader(io.StringIO(old.read('LM8_PUSH_results.csv').decode())))
new_ids = sorted({r['id'] for r in rows} - {r['id'] for r in previous},
                 key=lambda s: (s.split('.')[0], int(s.split('.')[1])))
assert new_ids == ['A.70', 'A.71', 'A.72', 'A.73', 'A.74', 'C.44', 'D.86', 'D.87', 'D.88', 'D.89']
paths = [root / 'LM8_PUSH_paper.tex', root / 'LM8_PUSH_references.bib']
paths += sorted((root / 'sections').rglob('*.tex'))
hashes = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in paths}
state = {
    'frozen_utc': datetime.now(timezone.utc).isoformat(),
    'paper_statements': len(rows),
    'status_counts': {s: sum(r['status'] == s for r in rows)
                      for s in ['Proved', 'Refuted', 'Known', 'Open']},
    'new_ids': new_ids,
    'frozen_source_count': len(hashes),
    'notes_only_after_freeze': 'Further modular-two-group geometry, nonunit five-valuation cusp calculations and later iterated-character research stays unregistered in notes; no subsequent candidate enters this frozen paper.',
}
comparison = {'status': 'PASS', 'active_tex_files': active,
              'source_statement_count': len(statements), 'csv_rows': len(rows),
              'every_id_and_status_equal': True, 'statements': statements}
(root / 'notes/checkpoint15_frozen_state.json').write_text(json.dumps(state, indent=2) + '\n')
(root / 'notes/checkpoint15_frozen_source_hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')
(root / 'notes/checkpoint15_statement_source_comparison.json').write_text(json.dumps(comparison, indent=2) + '\n')
print(json.dumps(state, indent=2))
