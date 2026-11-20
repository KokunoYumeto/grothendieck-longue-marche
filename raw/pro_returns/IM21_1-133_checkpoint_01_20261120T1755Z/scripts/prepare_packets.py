#!/usr/bin/env python3
"""Regenerate per-page working packets from the unchanged supplied inputs.

The source ZIP must already have been unpacked into ../../source.
No scan recognition or source modification is performed.
"""
from pathlib import Path
import collections,csv,json

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source'
with (SOURCE/'IM21_1-133_corrections.tsv').open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
groups=collections.OrderedDict()
for row in rows:
    key=f"{row['cote']}_scan{int(row['scan']):03d}"
    groups.setdefault(key,[]).append(row)
(ROOT/'page_packets').mkdir(exist_ok=True)
for index,(key,items) in enumerate(groups.items(),1):
    tex=SOURCE/'IM21_1-133_pages'/f'{key}.tex'
    scan=SOURCE/'IM21_1-133_scans'/f'{key}.jpg'
    assert tex.is_file() and scan.is_file()
    packet=dict(page_index=index,page_key=key,source_tex_path=str(tex),scan_path=str(scan),
                latex=tex.read_text(encoding='utf-8'),rows=items)
    (ROOT/'page_packets'/f'{key}.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'page_order.txt').write_text('\n'.join(groups)+'\n',encoding='utf-8')
print(f'Prepared {len(groups)} page packets with {len(rows)} correction rows.')
