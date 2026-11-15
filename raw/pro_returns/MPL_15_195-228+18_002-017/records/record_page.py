from pathlib import Path
from datetime import datetime, timezone
import csv,re,json
ROOT=Path(__file__).resolve().parents[1]
PREFIX=ROOT.name
HEADER=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
def stamp(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def macro_args(text,name):
    start=0
    while True:
        m=re.search(r'\\'+name+r'\{',text[start:])
        if not m:break
        a=start+m.end();i=a;depth=1
        while i<len(text) and depth:
            if text[i]=='{' and (i==0 or text[i-1]!='\\'):depth+=1
            elif text[i]=='}' and (i==0 or text[i-1]!='\\'):depth-=1
            i+=1
        yield start+m.start(),text[a:i-1]
        start=a

def save(cote,scan,kind,body,blocks,remark=''):
    p=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03}.tex'
    if p.exists():raise RuntimeError('Already exists: '+str(p))
    prefix=(f'\\cotefile{{{cote}}}\n' if (cote,scan) in [(15,195),(18,2)] else '')+f'\\scanpage{{{scan}}}\n'
    content=prefix+body.strip()+'\n'
    p.write_text(content,encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    rows=[]
    for i,(k,pos,words) in enumerate(blocks,1):rows.append([cote,scan,kind,f'{i:03}',k,pos,words,'yes'])
    for name,k in [('deleted','deletion'),('inserted','insertion'),('margin','margin note')]:
        for pos,arg in macro_args(content,name):
            rows.append([cote,scan,kind,f'{len(rows)+1:03}',k,'TeX line '+str(content[:pos].count('\n')+1),arg.replace('\n',' ')[:350],'yes'])
    new=not inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if new:w.writerow(HEADER)
        w.writerows(rows)
    doubts=ROOT/'records/doubt_rows.jsonl'
    with doubts.open('a',encoding='utf-8') as f:
        for name in ['unsure','illegible']:
            for pos,arg in macro_args(content,name):
                f.write(json.dumps({'cote':cote,'scan':scan,'line':content[:pos].count('\n')+1,'macro':name,'reading':arg,'confidence':'low' if name=='illegible' else 'medium'},ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'{cote} scan {scan:03} done {stamp()}\n')
        if remark:f.write('  '+remark+'\n')
    (ROOT/'records'/f'{cote}_{scan:03}_inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Saved {p.name}: {len(content)} characters, {len(rows)} inventory elements.')
