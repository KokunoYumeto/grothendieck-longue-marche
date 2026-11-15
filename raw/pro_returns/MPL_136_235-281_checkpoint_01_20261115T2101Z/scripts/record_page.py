from pathlib import Path
from datetime import datetime, timezone
import csv, re

ROOT = Path(__file__).resolve().parents[1]

def record(scan, tex, elements, sheet_kind='text', notes=''):
    path = ROOT / 'pages' / f'MPL_136_235-281_136_scan{scan:03}.tex'
    if path.exists():
        raise RuntimeError(f'Page already recorded: {scan}')
    path.write_text(tex.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_136_235-281_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        w=csv.writer(f)
        for i,e in enumerate(elements,1):
            kind,position,start=e
            w.writerow([136,scan,sheet_kind,f'{scan}.{i:02}',kind,position,start,'yes'])
    with (ROOT/'MPL_136_235-281_doubts.md').open('a',encoding='utf-8') as f:
        for line_no,line in enumerate(tex.strip().splitlines(),1):
            for token in ['unsure','illegible']:
                for m in re.finditer(r'\\'+token+r'\{',line):
                    start=m.end(); p=start; depth=1
                    while p<len(line) and depth:
                        if line[p]=='{' and (p==0 or line[p-1]!='\\'): depth+=1
                        if line[p]=='}' and (p==0 or line[p-1]!='\\'): depth-=1
                        p+=1
                    s=line[start:p-1].replace('|',' / ')
                    reading=('unreadable words: '+s) if token=='illegible' else s
                    confidence='low' if token=='illegible' or ' / ' in s else 'medium'
                    f.write(f'| 136 | {scan} | transcription line {line_no} (page-local locator) | `{reading}` | alternatives within reading, where present | {confidence} |\n')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'136 scan {scan:03} done {now}\n')
        if notes: f.write(f'136 scan {scan:03} record: {notes}\n')
    print(f'Saved scan {scan}: {len(elements)} inventory elements, {len(tex)} characters; {now}')
