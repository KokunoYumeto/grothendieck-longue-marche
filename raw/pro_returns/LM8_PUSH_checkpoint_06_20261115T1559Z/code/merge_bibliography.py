#!/usr/bin/env python3
"""Merge individually maintained, checked bibliography fragments."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
entries={}
for path in sorted((root/'notes').glob('*refs.bib')):
    text=path.read_text()
    blocks=re.split(r'(?m)(?=^@)',text)
    for block in blocks:
        if not block.strip():continue
        match=re.match(r'@\w+\s*\{\s*([^,]+),',block)
        if not match:raise ValueError(f'Cannot parse entry in {path}')
        key=match[1]
        if key in entries and entries[key].strip()!=block.strip():
            raise ValueError('Conflicting bibliography key '+key)
        entries[key]=block.strip()
(root/'LM8_PUSH_references.bib').write_text('\n\n'.join(entries[k] for k in sorted(entries))+'\n')
print(json.dumps({'entries':len(entries)},indent=2))
