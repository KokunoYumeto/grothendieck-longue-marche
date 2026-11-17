from pathlib import Path
from datetime import datetime, timezone
import csv, re, sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_58_020-067'
HEADERS = ['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def finish(scan, sheet_kind, elements):
    page = ROOT/'pages'/f'{PREFIX}_58_scan{scan:03d}.tex'
    assert page.exists()
    inv = ROOT/f'{PREFIX}_inventory.csv'
    rows = []
    if inv.exists():
        with inv.open(newline='',encoding='utf-8') as f:
            rows = [r for r in csv.DictReader(f) if int(r['scan']) != scan]
    for i, (kind, position, first) in enumerate(elements,1):
        rows.append(dict(zip(HEADERS,['58',str(scan),sheet_kind,str(i),kind,position,first,'yes'])))
    rows.sort(key=lambda r:(int(r['scan']),int(r['element'])))
    with inv.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=HEADERS); w.writeheader(); w.writerows(rows)
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'58 scan {scan:03d} done {now()}\n')
    rebuild_doubts()
    print(f'Saved scan {scan:03d}: {len(elements)} inventory elements')

def macro_args(text, macro):
    token='\\'+macro+'{'
    start=0
    while True:
        a=text.find(token,start)
        if a<0: return
        b=a+len(token); depth=1; j=b
        while j<len(text) and depth:
            if text[j]=='{' and (j==0 or text[j-1]!='\\'): depth+=1
            if text[j]=='}' and (j==0 or text[j-1]!='\\'): depth-=1
            j+=1
        yield a,text[b:j-1]
        start=a+len(token)

def split_alternatives(value):
    depth=0
    for i,ch in enumerate(value):
        if ch=='{' and (i==0 or value[i-1]!='\\'): depth+=1
        elif ch=='}' and (i==0 or value[i-1]!='\\'): depth-=1
        elif ch=='|' and depth==0: return value[:i],value[i+1:]
    return value,None

LOW_CONFIDENCE_SCANS={30,31,38,41,44,46,50,58,65,67}

def rebuild_doubts():
    out=(ROOT/'records'/'notation.md').read_text(encoding='utf-8')
    out+='\n## Doubt register\n\nLine numbers below refer to the per-page LaTeX source; they are approximate locations on the image. Confidence is confidence in the proposed reading, not in its mathematical plausibility. The particularly overwritten or compressed scans 30, 31, 38, 41, 44, 46, 50, 58, 65 and 67 are conservatively rated low wherever a doubt mark occurs. Nested doubt marks are listed individually; alternatives are separated only at the outermost brace level.\n\n| File | Scan | Approximate line | Reading | Alternatives | Confidence |\n|---|---:|---:|---|---|---|\n'
    for p in sorted((ROOT/'pages').glob('*.tex')):
        scan=int(re.search(r'scan(\d+)',p.name)[1]); s=p.read_text(encoding='utf-8')
        marks=sorted([(a,'unsure',v) for a,v in macro_args(s,'unsure')]+[(a,'illegible',v) for a,v in macro_args(s,'illegible')])
        for a,kind,v in marks:
            line=s.count('\n',0,a)+1
            if kind=='illegible': reading=f'[unreadable: estimated {v} words]'; alt='No secure reading'; conf='low'
            else:
                reading,alternative=split_alternatives(v); alt=alternative if alternative is not None else 'Undetermined'; conf='low' if alternative is not None or scan in LOW_CONFIDENCE_SCANS else 'medium'
            reading=reading.replace('|','&#124;').replace('\n',' '); alt=alt.replace('|','&#124;').replace('\n',' ')
            out+=f'| 58.pdf | {scan} | {line} | `{reading}` | `{alt}` | {conf} |\n'
    tail=ROOT/'records'/'doubts_tail.md'
    if tail.exists(): out+='\n'+tail.read_text(encoding='utf-8')
    (ROOT/f'{PREFIX}_doubts.md').write_text(out,encoding='utf-8')

if __name__=='__main__': rebuild_doubts()
