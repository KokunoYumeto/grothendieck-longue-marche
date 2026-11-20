#!/usr/bin/env python3
"""Make transient, smaller viewing copies of proposal crop references; no OCR.

The enlarged archival crops remain unchanged. Output paths live under /tmp.
Run after reading the proposal, then view the returned images explicitly.
"""
from pathlib import Path
from PIL import Image
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
seen=set()
for key in sys.argv[1:]:
    p=json.loads((ROOT/'proposals'/f'{key}.json').read_text())
    for row in p['rows']:
        for name in re.findall(r'crops/[A-Za-z0-9_.-]+\.(?:jpg|jpeg|png)',row['what_the_ink_shows']):
            if name in seen:continue
            seen.add(name)
            im=Image.open(ROOT/name)
            im.thumbnail((1400,1100))
            out=Path('/tmp')/('review_'+Path(name).name)
            im.save(out)
            print(str(out))
