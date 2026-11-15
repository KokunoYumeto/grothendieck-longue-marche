from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT = Path(__file__).resolve().parent
PREFIX = 'MPL_136_189-234'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save(scan, tex, rows, sheet_kind='text'):
    path = ROOT/'pages'/f'{PREFIX}_136_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError(f'Already saved: {path}')
    path.write_text(tex.strip()+'\n', encoding='utf-8')
    inv = ROOT/f'{PREFIX}_inventory.csv'
    new = not inv.exists()
    with inv.open('a', newline='', encoding='utf-8') as f:
        w=csv.writer(f)
        if new:
            w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i, (kind, position, first) in enumerate(rows, 1):
            w.writerow([136,scan,sheet_kind,i,kind,position,first,'yes'])
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'136 scan {scan:03d} done {utc()}\n')
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text() for p in sorted((ROOT/'pages').glob('*.tex'))),encoding='utf-8')
    print(f'Saved scan {scan}: {len(rows)} inventory elements; {len(tex)} characters')

def audit(scan):
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} audited {utc()}\n')

def macro_args(text, name):
    token='\\'+name+'{'
    pos=0
    while True:
        start=text.find(token,pos)
        if start<0: return
        i=start+len(token); depth=1; end=i
        while end<len(text) and depth:
            if text[end]=='{' and (end==0 or text[end-1]!='\\'): depth+=1
            elif text[end]=='}' and (end==0 or text[end-1]!='\\'): depth-=1
            end+=1
        yield start, text[i:end-1]
        pos=end

def update_doubts():
    intro=(ROOT/'notation.md').read_text()
    out=[intro,'\n## Doubt register\n\nLocations refer to line numbers in the per-page LaTeX source; they are approximate locators for the corresponding image. Confidence describes the proposed reading, not a mathematical claim.\n\n| File | Scan | Approximate line | Reading | Alternatives | Confidence |\n|---|---:|---:|---|---|---|']
    for p in sorted((ROOT/'pages').glob('*.tex')):
        scan=int(re.search(r'scan(\d+)',p.name).group(1)); t=p.read_text()
        for pos, val in macro_args(t,'unsure'):
            parts=val.split('|',1)
            reading=parts[0].replace('|','\\|').replace('\n',' ')
            alt=parts[1].replace('|','\\|').replace('\n',' ') if len(parts)>1 else 'Not resolved from the ink'
            line=t[:pos].count('\n')+1
            out.append(f'| 136 | {scan} | {line} | `{reading}` | `{alt}` | medium |')
        for pos,val in macro_args(t,'illegible'):
            line=t[:pos].count('\n')+1
            out.append(f'| 136 | {scan} | {line} | `\\illegible{{{val}}}` | No defensible reading at the inspected resolution | low |')
    tail=ROOT/'doubts_tail.md'
    if tail.exists(): out.append('\n'+tail.read_text())
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(out)+'\n')

if __name__=='__main__':
    update_doubts()
