from pathlib import Path
from datetime import datetime, timezone
import csv, json
ROOT=Path(__file__).resolve().parent.parent
PREFIX='MPL_136_282-327'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def record(scan,body,elements,doubts=(),observations=(),kind='text'):
    p=ROOT/'pages'/f'{PREFIX}_136_scan{scan:03}.tex'
    if p.exists(): raise FileExistsError(p)
    head=('\\cotefile{136}\n' if scan==282 else '')+f'\\scanpage{{{scan}}}\n'
    p.write_text(head+body.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if inv.stat().st_size==0:w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(typ,pos,start) in enumerate(elements,1):w.writerow([136,scan,kind,f'{scan}.{i:02}',typ,pos,start,'yes'])
    with (ROOT/'reading_doubts.jsonl').open('a',encoding='utf-8') as f:
        for row in doubts:f.write(json.dumps({'cote':136,'scan':scan,'line':row[0],'reading':row[1],'alternatives':row[2],'confidence':row[3]},ensure_ascii=False)+'\n')
    with (ROOT/'reading_observations.jsonl').open('a',encoding='utf-8') as f:
        for obs in observations:f.write(json.dumps({'scan':scan,'observation':obs},ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'136 scan {scan:03} done {utc()}\n')
    print(p.name, 'saved;',len(elements),'inventory elements')
