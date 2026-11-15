#!/usr/bin/env python3
"""Record a manually read page, its explicit element inventory, and reading notes.

This program performs no image processing, recognition, or transcription.
"""
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_72_035-081'
FIELDS = ['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def macros(s, name):
    pattern = re.compile(r'\\'+name+r'\{')
    for m in pattern.finditer(s):
        depth, i = 1, m.end()
        while i < len(s) and depth:
            if s[i] == '{' and (i == 0 or s[i-1] != '\\'): depth += 1
            if s[i] == '}' and (i == 0 or s[i-1] != '\\'): depth -= 1
            i += 1
        yield s[m.end():i-1], s[:m.start()].count('\n')+1

def require_unfrozen():
    log = ROOT / "progress.log"
    if log.exists() and any(line.startswith("transcription frozen ") for line in log.read_text().splitlines()):
        raise RuntimeError("Transcription is frozen; record later reading questions in research notes only")

def rebuild():
    require_unfrozen()
    records = [json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
    with (ROOT/(PREFIX+'_inventory.csv')).open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=FIELDS); w.writeheader()
        for r in records:
            for i,e in enumerate(r['elements'],1):
                w.writerow(dict(cote='72',scan=f"{r['scan']:03d}",sheet_kind=r.get('sheet_kind','text'),element=f"{r['scan']:03d}.{i:02d}",kind=e[0],position=e[1],first_words_or_objects=e[2],transcribed='yes'))
    header=(ROOT/'records/notation.md').read_text()
    parts=[header, '\n## Reading doubts\n\nLocations are approximate; `TeX line` identifies a line in the individual page fragment. Every uncertainty remains marked in the transcription.\n\n| File | Scan | Approximate location | Reading | Alternatives | Confidence |\n|---|---:|---|---|---|---|\n']
    for r in records:
        tex=(ROOT/'pages'/f"{PREFIX}_72_scan{r['scan']:03d}.tex").read_text()
        for value,line in macros(tex,'unsure'):
            reads=value.split('|',1)
            esc=lambda x:x.replace('|','\\|').replace('\n',' ')
            parts.append(f"| 72 | {r['scan']:03d} | TeX line {line} | `{esc(reads[0])}` | `{esc(reads[1])}` | {r.get('confidence','medium')} |\n" if len(reads)>1 else f"| 72 | {r['scan']:03d} | TeX line {line} | `{esc(reads[0])}` | — | {r.get('confidence','medium')} |\n")
        for value,line in macros(tex,'illegible'):
            parts.append(f"| 72 | {r['scan']:03d} | TeX line {line} | Physically unreadable, estimated {value} words | — | low |\n")
    parts.append('\n## Page-specific reading observations\n\n')
    for r in records:
        if r.get('reading_notes'): parts.append(f"### Scan {r['scan']:03d}\n\n{r['reading_notes']}\n\n")
    tail=ROOT/'records/abbreviations_legibility.md'
    if tail.exists(): parts.append(tail.read_text())
    (ROOT/(PREFIX+'_doubts.md')).write_text(''.join(parts))
    (ROOT/(PREFIX+'_transcription.tex')).write_text(''.join((ROOT/'pages'/f"{PREFIX}_72_scan{r['scan']:03d}.tex").read_text() for r in records))

def main():
    require_unfrozen()
    data=json.load(sys.stdin); n=int(data['scan'])
    target=ROOT/'pages'/f'{PREFIX}_72_scan{n:03d}.tex'
    existed=target.exists()
    assert 35<=n<=81
    assert f'\\scanpage{{{n}}}' in data['tex']
    assert data['elements']
    if not existed and n>35:
        assert (ROOT/'pages'/f'{PREFIX}_72_scan{n-1:03d}.tex').exists(), 'Pages must be recorded in scan order'
    tex=data.pop('tex').rstrip()+'\n\n'
    target.write_text(tex)
    data['recorded_utc']=utc()
    (ROOT/'records'/f'scan{n:03d}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    rebuild()
    with (ROOT/'progress.log').open('a') as f:
        f.write(f"72 scan {n:03d} {'revised before freeze' if existed else 'done'} {utc()}\n")
    print(f'Scan {n:03d}: page, {len(data["elements"])} inventory elements, doubts and combined fragment saved.')

if __name__=='__main__': main()
