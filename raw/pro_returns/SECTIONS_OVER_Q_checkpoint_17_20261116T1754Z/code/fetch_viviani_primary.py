#!/usr/bin/env python3
"""Retrieve and render the primary radical-extension ramification source."""
from pathlib import Path
import hashlib
import urllib.request
import fitz

w = Path(__file__).resolve().parents[1]
url = 'https://www.numdam.org/item/JTNB_2004__16_3_779_0.pdf'
out = w / 'notes/primary_sources'
out.mkdir(exist_ok=True, parents=True)
data = urllib.request.urlopen(url, timeout=30).read()
assert data.startswith(b'%PDF-')
p = out / 'viviani2004.pdf'; p.write_bytes(data)
doc = fitz.open(p)
for page in [31, 32, 33]:
    doc[page].get_pixmap(matrix=fitz.Matrix(1.4, 1.4)).save(out / f'viviani2004_p{779+page}.png')
print('Primary source:', url)
print('Bytes:', len(data), 'SHA256:', hashlib.sha256(data).hexdigest())
print('Pages:', len(doc), 'Rendered printed pages:', [810, 811, 812])
print('An initial inline retrieval attempt used the unavailable requests package and stopped with ModuleNotFoundError before any retrieval; this executable uses the standard-library urllib instead.')
