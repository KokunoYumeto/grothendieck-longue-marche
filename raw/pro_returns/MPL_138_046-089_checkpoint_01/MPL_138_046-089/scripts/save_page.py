from pathlib import Path
import csv, json, datetime, re, sys
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_138_046-089'
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(scan, text, elements, sheet_kind='text', observations=''):
    p=ROOT/'pages'/f'{PREFIX}_138_scan{scan:03}.tex'
    if p.exists(): raise ValueError(f'Already saved: {p.name}')
    p.write_text(text.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    new=not inv.exists()
    with inv.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if new:w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,position,words) in enumerate(elements,1):w.writerow([138,scan,sheet_kind,i,kind,position,words,'yes'])
    if observations:
        with (ROOT/'precontext_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## Scan {scan:03}\n\n{observations}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'138 scan {scan:03} done {now()}\n')
    combine()
    refresh_doubts()
    print(f'Saved scan {scan:03}: {len(text)} characters; {len(elements)} inventory elements; {now()}')
def combine():
    ps=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text() for p in ps),encoding='utf-8')
def braced(s,start):
    depth=1;i=start
    while i<len(s) and depth:
        if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
        if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
        i+=1
    return s[start:i-1]
def refresh_doubts():
    head=(ROOT/'notation_table.md').read_text(encoding='utf-8')
    rows=['\n## Readings requiring review\n','The location is the approximate manuscript-line group in the page file; source line numbers are also given for unambiguous retrieval. Confidence is medium for a single proposed reading and low when alternatives or physically unreadable words remain. These grades concern the reading, not the mathematical assertion.\n','| File | Scan | Approximate line / location | Reading | Alternative(s) | Confidence |','|---|---:|---|---|---|---|']
    for p in sorted((ROOT/'pages').glob('*.tex')):
        s=p.read_text(encoding='utf-8');scan=int(re.search(r'scan(\d+)',p.name)[1])
        for m in re.finditer(r'\\(unsure|illegible)\{',s):
            value=braced(s,m.end());sl=s[:m.start()].count('\n')+1
            locs=list(re.finditer(r'% lines? ([^\n]+)',s[:m.start()]));loc=locs[-1][1] if locs else 'unspecified'
            if m[1]=='illegible':reading=f'physically unreadable, estimated {value} word(s)';alt='—';conf='low'
            else:
                parts=value.split('|');reading=parts[0];alt=' / '.join(parts[1:]) or '—';conf='low' if len(parts)>1 else 'medium'
            esc=lambda x:x.replace('|','\\|').replace('\n',' ')
            rows.append(f'| 138 | {scan:03} | {esc(loc)}; TeX L{sl} | `{esc(reading)}` | `{esc(alt)}` | {conf} |')
    tail=(ROOT/'legibility.md').read_text(encoding='utf-8')
    (ROOT/f'{PREFIX}_doubts.md').write_text(head+'\n'+'\n'.join(rows)+'\n\n'+tail,encoding='utf-8')
if __name__=='__main__':
    combine();refresh_doubts()
