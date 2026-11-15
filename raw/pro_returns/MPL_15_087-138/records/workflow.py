from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, hashlib, zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_15_087-138'
def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def record(scan, sheet, elements, doubts=(), notation=(), abbreviations=()):
    page = ROOT/'pages'/f'{PREFIX}_15_scan{scan:03d}.tex'
    assert page.exists() and f'\\scanpage{{{scan}}}' in page.read_text()
    with (ROOT/f'{PREFIX}_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,position,words) in enumerate(elements,1):
            w.writerow([15,scan,sheet,f'{scan:03d}.{i:02d}',kind,position,words,'yes'])
    with (ROOT/'records/readings.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps(dict(scan=scan,sheet=sheet,doubts=doubts,notation=notation,abbreviations=abbreviations),ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'15 scan {scan:03d} done {now()}\n')
    rebuild_doubts()
    print(f'15 scan {scan:03d} saved and inventoried {now()}')
def rebuild_doubts():
    data=[json.loads(l) for l in (ROOT/'records/readings.jsonl').read_text().splitlines()]
    lines=['# Notation table','','| Manuscript sign | LaTeX | Scans | Reading observations |','|---|---|---|---|']
    for d in data:
        for n in d['notation']:
            lines.append('| '+' | '.join(str(x).replace('|','&#124;') for x in [n[0],n[1],d['scan'],n[2]])+' |')
    lines+=['','# Doubt register','','| File | Scan | Approximate line / position | Reading | Alternatives | Confidence |','|---|---|---|---|---|---|']
    for d in data:
        for q in d['doubts']:
            lines.append('| '+' | '.join(str(x).replace('|','&#124;') for x in [15,d['scan'],*q])+' |')
    lines+=['','# Abbreviations','','| Written form | Proposed expansion (not inserted in transcription) | Scans |','|---|---|---|']
    for d in data:
        for a in d['abbreviations']:
            lines.append('| '+' | '.join(str(x).replace('|','&#124;') for x in [a[0],a[1],d['scan']])+' |')
    lines+=['','# Legibility and limits','','Reading and audit in progress. Doubt marks follow the ink, including grammatically or mathematically surprising forms. No OCR has been used.']
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
def combined():
    files=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text() for p in files),encoding='utf-8')
def checkpoint(number):
    combined()
    dest=ROOT.parent/f'{PREFIX}_checkpoint_{number:02d}.zip'
    assert not dest.exists()
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                z.write(p,p.relative_to(ROOT))
    print(dest)

def audit(scan, observations, doubts=(), notation=()):
    data=[json.loads(l) for l in (ROOT/'records/readings.jsonl').read_text().splitlines()]
    entry=next(d for d in data if d['scan']==scan)
    entry['doubts'].extend(doubts)
    entry['notation'].extend(notation)
    (ROOT/'records/readings.jsonl').write_text(''.join(json.dumps(d,ensure_ascii=False)+'\n' for d in data))
    with (ROOT/'records/visual_audit.jsonl').open('a') as f:
        f.write(json.dumps({'scan':scan,'time':now(),'observations':observations},ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} audited {now()}\n')
    rebuild_doubts()
    print(f'scan {scan:03d} audited {now()}')
