from pathlib import Path
import csv,json,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
FIELDS=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(cote,scan,tex,elements,doubts=(),observations=(),sheet_kind='text'):
    path=ROOT/'pages'/f'MPL_116+117_{cote}_scan{scan:03}.tex'
    if path.exists(): raise RuntimeError(f'Page exists: {path}')
    path.write_text(tex.strip()+'\n',encoding='utf-8')
    inv=ROOT/'MPL_116+117_inventory.csv'
    fresh=not inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS)
        if fresh:w.writeheader()
        for n,(kind,position,first) in enumerate(elements,1):
            w.writerow(dict(cote=cote,scan=scan,sheet_kind=sheet_kind,element=f'{cote}-{scan:03}-{n:02}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
    with (ROOT/'working'/'doubts.jsonl').open('a',encoding='utf-8') as f:
        for line,reading,alternatives,confidence in doubts:
            f.write(json.dumps(dict(cote=cote,scan=scan,line=line,reading=reading,alternatives=alternatives,confidence=confidence),ensure_ascii=False)+'\n')
    with (ROOT/'working'/'observations.md').open('a',encoding='utf-8') as f:
        for obs in observations:f.write(f'- {cote} scan {scan:03}: {obs}\n')
    files=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/'MPL_116+117_transcription.tex').write_text(''.join(p.read_text(encoding='utf-8') for p in files),encoding='utf-8')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'{cote} scan {scan:03} done {utc()}\n')
    print(f'Saved {cote} scan {scan:03}; {len(files)}/34 page files')
