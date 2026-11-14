from pathlib import Path
from datetime import datetime, timezone
import csv,re
ROOT=Path(__file__).resolve().parents[1]
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save_page(cote, scan, content, elements, kind='text', observations=''):
    name=f'MPL_152+120_{cote}_scan{scan:03}.tex'
    path=ROOT/'pages'/name
    if path.exists(): raise RuntimeError('Page already exists: '+name)
    prefix=(f'\\cotefile{{{cote}}}\n' if scan==1 else '')+f'\\scanpage{{{scan}}}\n'
    text=prefix+content.strip()+'\n'
    path.write_text(text)
    with (ROOT/'MPL_152+120_inventory.csv').open('a',newline='') as f:
        w=csv.writer(f)
        for j,(typ,pos,first) in enumerate(elements,1):
            w.writerow([cote,scan,kind,f'{cote}-{scan:03}-{j:02}',typ,pos,first,'yes'])
    rows=[]
    for m in re.finditer(r'\\unsure\{',text):
        start=m.end(); i=start; depth=1
        while i<len(text) and depth:
            if text[i]=='{': depth+=1
            elif text[i]=='}': depth-=1
            i+=1
        reading=text[start:i-1]
        parts=reading.split('|',1)
        context=re.sub(r'\s+',' ',text[max(0,m.start()-65):m.start()]).replace('|','\\|')
        rd=parts[0].replace('|','\\|')
        alt=parts[1].replace('|','\\|') if len(parts)>1 else '—'
        confidence='low' if len(parts)>1 else 'medium'
        rows.append(f'| {cote} | {scan} | After `{context}` | `{rd}` | `{alt}` | {confidence} |\n')
    if rows:
        p=ROOT/'MPL_152+120_doubts.md'; d=p.read_text(); d=d.replace('\n# Abbreviations\n','\n'+''.join(rows)+'\n# Abbreviations\n'); p.write_text(d)
    if observations:
        with (ROOT/'reading_observations.md').open('a') as f:f.write(f'\n## Cote {cote}, scan {scan}\n\n{observations}\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03} done {now()}\n')
    print(name, 'saved;',len(elements),'inventory elements;',len(rows),'doubt marks.')
