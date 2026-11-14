#!/usr/bin/env python3
"""Record the exact two escaped-TeX repairs to the first E119 preview."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent.parent
p=R/'sections/E_lower_fiftythree.tex'
b=p.read_bytes();before=hashlib.sha256(b).hexdigest()
assert b.count(bytes([13])+b'ight)')==1
assert b.count(b'|K_B|,qquad')==1
b=b.replace(bytes([13])+b'ight)',br'\right)')
b=b.replace(b'|K_B|,qquad',br'|K_B|,\qquad')
assert all(c>=32 or c in (9,10) for c in b)
p.write_bytes(b)
print(json.dumps({'status':'PASS','before':before,'after':hashlib.sha256(b).hexdigest(),
 'repairs':['one carriage-return plus ight changed to literal backslash-right',
            'one dropped backslash before qquad restored'],
 'mathematical_expressions_changed':False},indent=2))
