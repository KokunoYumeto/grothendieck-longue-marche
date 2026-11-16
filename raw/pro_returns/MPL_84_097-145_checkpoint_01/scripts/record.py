"""Root reader's page recording helper. No OCR or text inference."""
from pathlib import Path
from datetime import datetime, timezone
import csv, re

ROOT = Path(__file__).resolve().parents[1]
def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def draft(scan, text):
    p=ROOT/'pages'/f'MPL_84_097-145_84_scan{scan:03d}.tex'
    p.write_text(text.strip()+'\n',encoding='utf-8')

def finish(scan, elements, notes='', sheet_kind='text'):
    p=ROOT/'pages'/f'MPL_84_097-145_84_scan{scan:03d}.tex'
    assert p.exists()
    with (ROOT/'MPL_84_097-145_inventory.csv').open('a',newline='') as f:
        w=csv.writer(f)
        for i,(kind,position,first) in enumerate(elements,1):
            w.writerow([84,scan,sheet_kind,f'{scan:03d}-{i:02d}',kind,position,first,'yes'])
    doubts=[]
    text=p.read_text()
    for m in re.finditer(r'\\(unsure|illegible)\{',text):
        j=m.end(); depth=1
        while j<len(text) and depth:
            if text[j]=='{': depth+=1
            elif text[j]=='}': depth-=1
            j+=1
        val=text[m.end():j-1]
        line=text.count('\n',0,m.start())+1
        if m.group(1)=='illegible':
            reading=f'{val} unreadable word(s)'; alt='No secure reading after enlargement'; conf='low'
        else:
            parts=val.split('|',1); reading=parts[0]; alt=parts[1] if len(parts)>1 else 'No secure alternative'; conf='low' if len(parts)>1 else 'medium'
        doubts.append(f'| 84 | {scan} | TeX line {line} | `{reading.replace(chr(10)," ").replace("|","&#124;")}` | {alt.replace(chr(10)," ").replace("|","&#124;")} | {conf} |\n')
    d=ROOT/'MPL_84_097-145_doubts.md'
    s=d.read_text(); s=s.replace('\n# Abbreviations',''.join(doubts)+'\n# Abbreviations'); d.write_text(s)
    if notes:
        with (ROOT/'research_leads.md').open('a') as f: f.write(f'\n## Scan {scan}\n\n{notes}\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'84 scan {scan:03d} done {now()}\n')
    print(f'Scan {scan:03d} recorded, {len(elements)} inventory elements, {len(doubts)} doubt marks.')

def audit(scan, note=''):
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} audited {now()}'+(f' — {note}' if note else '')+'\n')
