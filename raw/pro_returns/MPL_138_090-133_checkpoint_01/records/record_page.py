from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, fcntl
ROOT=Path(__file__).resolve().parent.parent
PREFIX='MPL_138_090-133'
INVENTORY_KINDS={'text','display','diagram','drawing','margin note','insertion','deletion'}
INVENTORY_KIND_ALIASES={
    'formula':'display', 'number':'display',
    'heading':'text', 'title':'text', 'subtitle':'text',
    'annotation':'margin note', 'figure':'drawing', 'margin':'margin note',
}
def normalize_inventory_kind(kind):
    if kind.startswith(('cancelled','deleted')):
        return 'deletion'
    normalized=INVENTORY_KIND_ALIASES.get(kind,kind)
    if normalized not in INVENTORY_KINDS:
        raise ValueError(f'Unrecognized inventory kind: {kind!r}')
    return normalized
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(scan, tex, elements, doubts=(), notation=(), abbreviations=(), leads='', sheet_kind='text'):
    elements=[(normalize_inventory_kind(kind),position,first) for kind,position,first in elements]
    path=ROOT/'pages'/f'{PREFIX}_138_scan{scan:03d}.tex'
    if path.exists(): raise ValueError('Page exists; audit/edit explicitly')
    tex=tex.strip()+'\n'
    assert f'\\scanpage{{{scan}}}' in tex
    path.write_text(tex)
    with (ROOT/f'{PREFIX}_inventory.csv').open('a',newline='') as f:
        fcntl.flock(f,fcntl.LOCK_EX)
        w=csv.writer(f)
        for i,(kind,position,first) in enumerate(elements,1):
            w.writerow([138,scan,sheet_kind,f'{scan:03d}.{i:02d}',kind,position,first,'yes'])
        f.flush()
        fcntl.flock(f,fcntl.LOCK_UN)
    record={'scan':scan,'doubts':list(doubts),'notation':list(notation),'abbreviations':list(abbreviations)}
    (ROOT/'records'/f'page{scan:03d}_reading.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    if leads:
        with (ROOT/'records/research_leads.md').open('a') as f:f.write(f'\n## Scan {scan}\n\n{leads}\n')
    rebuild_doubts()
    with (ROOT/'progress.log').open('a') as f:f.write(f'138 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(tex)} characters, {len(elements)} inventory elements, {len(doubts)} doubt entries; {utc()}')
def rebuild_doubts():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('page*_reading.json'))]
    s='# Notation table and reading doubts\n\n## Package notation table\n\n| Manuscript sign | LaTeX | Scans / visual evidence |\n|---|---|---|\n'
    for r in records:
        for a,b,c in r['notation']: s+=f'| {a} | `{b}` | {r["scan"]}: {c} |\n'
    s+='\n## Reading doubts\n\n| File | Scan | Approximate line | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n'
    for r in records:
        for line,reading,alternatives,confidence in r['doubts']:
            s+=f'| 138 | {r["scan"]} | {line} | {reading.replace("|"," / ")} | {alternatives.replace("|"," / ")} | {confidence} |\n'
    s+='\n## Abbreviations\n\n| Written form | Possible expansion (only here) | Scan |\n|---|---|---|\n'
    seen=set()
    for r in records:
        for a,b in r['abbreviations']:
            if (a,b) not in seen:s+=f'| {a} | {b} | {r["scan"]} |\n';seen.add((a,b))
    s+='\n## Legibility assessment\n\nThe ink is often clear at stroke level, but rapid cursive, overwritten symbols and abbreviated words create reading uncertainty. Explicit doubt marks record these limits; a plausible mathematical interpretation has not been used to remove a visual doubt. The final assessment follows the full audit.\n'
    (ROOT/f'{PREFIX}_doubts.md').write_text(s)
