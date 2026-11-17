from pathlib import Path
import csv, datetime, re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_137_045-086'
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f: f.write(s+' '+now()+'\n')
def doubt_args(s):
    for m in re.finditer(r'\\(unsure|illegible)\{',s):
        start=m.end(); i=start; depth=1
        while i<len(s) and depth:
            if s[i]=='{' and (i==0 or s[i-1]!='\\'): depth+=1
            if s[i]=='}' and (i==0 or s[i-1]!='\\'): depth-=1
            i+=1
        yield m.group(1),s[start:i-1],s.count('\n',0,m.start())+1
def doubt_parts(v):
    """Split alternatives at a top-level bar, not inside a nested macro."""
    depth=0
    for i,c in enumerate(v):
        if c=='{' and (i==0 or v[i-1]!='\\'): depth+=1
        elif c=='}' and (i==0 or v[i-1]!='\\'): depth-=1
        elif c=='|' and depth==0: return [v[:i],v[i+1:]]
    return [v]
def rebuild():
    files=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/(PREFIX+'_transcription.tex')).write_bytes(b''.join(p.read_bytes() for p in files))
    header=(ROOT/'support/notation.md').read_text(encoding='utf-8')
    rows=['\n## Doubt register\n\nLocations below are approximate: numbered source lines within each page fragment follow the order of the manuscript. All explicitly uncertain readings, including those nested in deletions and diagrams, are included. No alternative is asserted where none is visible.\n\n| File | Scan | Approx. location | Reading | Alternatives | Confidence |\n|---|---:|---|---|---|---|']
    for p in files:
        n=int(re.search(r'scan(\d+)',p.name).group(1)); s=p.read_text(encoding='utf-8')
        for kind,v,l in doubt_args(s):
            parts=doubt_parts(v)
            reading=parts[0] if kind=='unsure' else 'Physically unreadable: '+v+' word(s)'
            alt=parts[1] if len(parts)>1 else '—'
            clean=lambda t:t.replace('|','&#124;').replace('\n',' ').replace('`','&#96;')
            low_pages={45,58,62,65,68,70,71,73,75,76,77,79,80,81,82,83}
            conf='low' if n in low_pages or len(parts)>1 or kind=='illegible' else 'medium'
            rows.append(f'| 137 | {n:03d} | source line {l} | `{clean(reading)}` | `{clean(alt)}` | {conf} |')
    tail=(ROOT/'support/doubts_tail.md').read_text(encoding='utf-8')
    (ROOT/(PREFIX+'_doubts.md')).write_text(header+'\n'+'\n'.join(rows)+'\n\n'+tail,encoding='utf-8')
def save(scan,text,elements,sheet_kind='text'):
    p=ROOT/'pages'/f'{PREFIX}_137_scan{scan:03d}.tex'
    if p.exists(): raise RuntimeError('Page already recorded; edit and rebuild explicitly.')
    p.write_text(text.strip()+'\n\n',encoding='utf-8')
    with (ROOT/(PREFIX+'_inventory.csv')).open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,e in enumerate(elements,1):
            kind,position,opening=e
            w.writerow(['137',f'{scan:03d}',sheet_kind,f'{scan:03d}-{i:02d}',kind,position,opening,'yes'])
    rebuild();log(f'137 scan {scan:03d} done')
    print(f'Saved scan {scan:03d}: {len(elements)} inventoried elements; {sum(1 for _ in doubt_args(text))} doubt marks.')
