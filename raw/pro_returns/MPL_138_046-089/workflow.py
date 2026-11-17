from pathlib import Path
from datetime import datetime, timezone
import csv, re, hashlib, zipfile

ROOT = Path(__file__).resolve().parent
PREFIX = 'MPL_138_046-089'

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def log(s):
    with (ROOT/'progress.log').open('a') as f:
        f.write(s+'\n')

def macro_arguments(s, macro):
    pattern = '\\'+macro+'{'
    start = 0
    while True:
        i = s.find(pattern, start)
        if i < 0: break
        j = i+len(pattern)
        depth = 1
        k = j
        while k < len(s) and depth:
            if s[k] == '{' and (k == 0 or s[k-1] != '\\'): depth += 1
            if s[k] == '}' and (k == 0 or s[k-1] != '\\'): depth -= 1
            k += 1
        yield s.count('\n',0,i)+1, s[j:k-1]
        start = k

def refresh_doubts():
    p=ROOT/(PREFIX+'_doubts.md')
    s=p.read_text()
    a=s.index('# Doubts')
    b=s.index('# Abbreviations')
    rows=['# Doubts\n\nApproximate line numbers refer to the per-page TeX source. A single marked reading has no positively identified alternative. Confidence concerns the reading, not its mathematical plausibility.\n\n| Cote | Scan | Approx. line / place | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n']
    for page in sorted((ROOT/'pages').glob('*.tex')):
        scan=re.search(r'scan(\d+)',page.name).group(1)
        t=page.read_text()
        for line,arg in macro_arguments(t,'unsure'):
            first,*alts=arg.split('|')
            first=first.replace('\n',' ')
            alt=' / '.join(alts).replace('\n',' ') if alts else '—'
            rows.append(f'| 138 | {scan} | TeX line {line} | `{first}` | `{alt}` | medium |\n')
        for line,arg in macro_arguments(t,'illegible'):
            rows.append(f'| 138 | {scan} | TeX line {line} | physically unreadable: {arg} word(s) | — | low |\n')
    p.write_text(s[:a]+''.join(rows)+'\n'+s[b:])

def save_page(scan, text, elements, sheet_kind='text'):
    p=ROOT/'pages'/f'{PREFIX}_138_scan{scan:03}.tex'
    if p.exists(): raise RuntimeError(f'Page already exists: {p}')
    p.write_text(text.strip()+'\n')
    with (ROOT/(PREFIX+'_inventory.csv')).open('a',newline='') as f:
        w=csv.writer(f)
        for i,(kind,position,words) in enumerate(elements,1):
            w.writerow(['138',str(scan),sheet_kind,f'{scan:03}-{i:02}',kind,position,words,'yes'])
    refresh_doubts()
    log(f'138 scan {scan:03} done {now()}')
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements')

def combine():
    pages=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/(PREFIX+'_transcription.tex')).write_text('\n'.join(p.read_text() for p in pages))

def checkpoint(n):
    target=ROOT.parent/f'{PREFIX}_checkpoint_{n:02}.zip'
    if target.exists(): raise RuntimeError('Checkpoints must not be overwritten')
    log(f'hourly checkpoint {n:02} assembled {now()}')
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                z.write(p,p.relative_to(ROOT))
    print(target)
