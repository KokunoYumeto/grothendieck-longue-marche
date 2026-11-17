from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit_record(scan, changes='', doubts=(), elements=()):
    dp=ROOT/'MPL_64_040-077_doubts.md'
    d=dp.read_text()
    esc=lambda x:str(x).replace('|',r'\|').replace('\n',' ')
    rows=''.join('| 64 | %03d | %s | `%s` | %s | %s |\n'%(scan,esc(pos),esc(read),esc(alt),conf) for pos,read,alt,conf in doubts)
    d=d.replace('\n# Abbreviations','\n'+rows+'\n# Abbreviations')
    dp.write_text(d)
    ip=ROOT/'MPL_64_040-077_inventory.csv'
    with ip.open(newline='') as f: inv=list(csv.DictReader(f))
    n=sum(r['scan']==f'{scan:03d}' for r in inv)
    with ip.open('a',newline='') as f:
        w=csv.writer(f)
        for i,(kind,pos,words) in enumerate(elements,n+1): w.writerow(['64',f'{scan:03d}','text',f'{scan:03d}.{i:02d}',kind,pos,words,'yes'])
    (ROOT/'MPL_64_040-077_transcription.tex').write_text('\n'.join(p.read_text().rstrip() for p in sorted((ROOT/'pages').glob('*.tex')))+'\n')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:
        if changes:f.write(f'audit correction scan {scan:03d}: {changes}\n')
        f.write(f'scan {scan:03d} audited {now}\n')
    print(f'scan {scan:03d} audited {now}')
