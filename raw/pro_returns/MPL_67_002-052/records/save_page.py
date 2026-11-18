from pathlib import Path
from datetime import datetime,timezone
import csv,re
ROOT=Path(__file__).resolve().parents[1]
EXPECTED=[n for n in range(2,53) if n not in {15,22,23,47,52}]
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def macro_args(text,name):
    result=[]
    token='\\'+name+'{'
    start=0
    while (p:=text.find(token,start))>=0:
        a=p+len(token); depth=1; q=a
        while q<len(text) and depth:
            if text[q]=='{' and (q==0 or text[q-1]!='\\'): depth+=1
            if text[q]=='}' and (q==0 or text[q-1]!='\\'): depth-=1
            q+=1
        result.append((text.count('\n',0,p)+1,text[a:q-1]))
        start=a
    return result
def save(n,text,elements,sheet='text',leads='',doubts=None):
    existing=sorted(int(p.stem[-3:]) for p in (ROOT/'pages').glob('*.tex'))
    if n in existing: raise ValueError('Page already saved; use explicit audited correction')
    if n!=EXPECTED[len(existing)]: raise ValueError('Pages must be saved in order')
    header=('\\cotefile{67}\n' if n==2 else '')+f'\\scanpage{{{n}}}\n'
    full=header+text.strip()+'\n'
    (ROOT/'pages'/f'MPL_67_002-052_67_scan{n:03d}.tex').write_text(full,encoding='utf-8')
    with (ROOT/'MPL_67_002-052_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,pos,excerpt) in enumerate(elements,1):w.writerow([67,n,sheet,f'{n:03d}.{i:02d}',kind,pos,excerpt,'yes'])
    if doubts is None:
        doubts=[(f'TeX line {line}',s.split('|')[0],' / '.join(s.split('|')[1:]) or 'Not resolved from ink','medium') for line,s in macro_args(full,'unsure')]
        doubts += [(f'TeX line {line}',f'illegible: {s} word(s)','No secure reading','low') for line,s in macro_args(full,'illegible')]
    with (ROOT/'MPL_67_002-052_doubts.md').open('a',encoding='utf-8') as f:
        for pos,r,a,c in doubts:
            f.write('| 67 | '+str(n)+' | '+' | '.join(str(v).replace('|','&#124;').replace('\n',' ') for v in [pos,r,a,c])+' |\n')
    if leads:
        with (ROOT/'records/research_leads.md').open('a',encoding='utf-8') as f:f.write(f'\n## Scan {n:03d}\n\n'+leads.strip()+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'67 scan {n:03d} done {now()}\n')
    print(f'Saved scan {n:03d}: {len(elements)} inventory elements; {len(doubts)} doubt records.')
