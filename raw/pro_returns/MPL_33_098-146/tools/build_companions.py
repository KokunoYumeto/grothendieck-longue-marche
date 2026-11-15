#!/usr/bin/env python3
"""Rebuild the pre-freeze combined fragment and its doubt register, without OCR."""
from pathlib import Path
import json
from save_page import extract_doubts
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_33_098-146'
if (ROOT/'records/frozen_sha256.json').exists():
    raise SystemExit('Transcription frozen: this builder is disabled.')
low_lines={98:{10,18,25},106:{7,19,20,26,40,48},112:{15,16,22,23,27,28,38,40},122:{15,16,17,21},124:{16},128:{2},136:{13,21},138:{9,20,21,22,25,27},142:{3},144:{30,34},146:{21,35}}
high_readings={(100,12,'-'),(100,16,'-'),(140,12,r'\text{---}'),(140,23,r'\text{---}')}
def cell(x):
    return str(x).replace('|',r'\|').replace('\n',' ')
pages=sorted((ROOT/'pages').glob('*.tex'))
assert len(pages)==49
combined='\n'.join(p.read_text().rstrip() for p in pages)+'\n'
(ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
rows=[]
for p in pages:
    scan=int(p.stem[-3:]); ds=extract_doubts(p.read_text())
    for d in ds:
        if d['line'] in low_lines.get(scan,set()): d['confidence']='low'
        if (scan,d['line'],d['reading']) in high_readings: d['confidence']='high'
        rows.append((scan,d))
    (ROOT/'records'/f'doubts_{scan:03}.json').write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
content=(ROOT/'records/notation.md').read_text().rstrip()+'\n\n## Doubts register\n\n'
content+='| File (cote) | Scan | Approx. source line | First reading | Alternative(s) / limitation | Confidence |\n|---|---|---|---|---|---|\n'
for scan,d in rows:
    content+=f"| 33 | {scan:03} | {d['line']} | `{cell(d['reading'])}` | {cell(d['alternative'])} | {d['confidence']} |\n"
content+='\n'+(ROOT/'records/abbreviations.md').read_text()
(ROOT/f'{PREFIX}_doubts.md').write_text(content)
print(f'Rebuilt 49-page combined fragment; {len(rows)} doubt entries.')
