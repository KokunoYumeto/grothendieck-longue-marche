#!/usr/bin/env python3
"""A compact parity witness for the already certified cross-sheet rows."""
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent/'odd_G_overlap.json'
raw=p.read_bytes();d=json.loads(raw)
rows=d['columns'];assert len(rows)==128
for i in range(64):
    x,y=rows[i],rows[i+64]
    assert x['node']==y['node']
    a,b=x['augmented_row'],y['augmented_row']
    assert a[:2]==b[:2]
    diff=tuple((sum(abs(t)==j for t in a[2])-sum(abs(t)==j for t in b[2]))%2 for j in range(1,6))
    assert diff==(1,0,0,0,0)
print('PASS all64 same-physical-pair relative heads differ by parity(1,0,0,0,0).')
print('This is a bounded128-column incidence certificate,not arbitrary-orbit separation.')
print('Input SHA256',hashlib.sha256(raw).hexdigest())
