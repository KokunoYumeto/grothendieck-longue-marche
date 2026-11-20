#!/usr/bin/env python3
"""Rebuild missing isolated reader packets from the user-supplied source files.

Source files must already be in ../source; this script never unpacks an archive
and never overwrites a packet, page, placement, review, or completion log.
"""
from pathlib import Path
from collections import OrderedDict
import csv, json

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'source'
groups=OrderedDict()
with (SOURCE/'IM08_57-64_corrections.tsv').open(newline='') as f:
    for row in csv.DictReader(f,delimiter='\t'):
        page=f"{row['cote']}_scan{int(row['scan']):03d}"
        groups.setdefault(page,[]).append(row)
preamble=(SOURCE/'PREAMBLE.tex').read_text()
(BASE/'packets').mkdir(exist_ok=True)
created=0
for page,rows in groups.items():
    dest=BASE/'packets'/f'{page}.json'
    if dest.exists():
        continue
    tex=SOURCE/'IM08_57-64_pages'/f'{page}.tex'
    scan=SOURCE/'IM08_57-64_scans'/f'{page}.jpg'
    assert tex.is_file() and scan.is_file(),page
    packet={'page':page,'source_tex':str(tex),'scan_image':str(scan),
            'rows':rows,'latex':tex.read_text(),'preamble':preamble}
    dest.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
    created+=1
print(f'Created {created} missing packets; total page groups {len(groups)}.')
