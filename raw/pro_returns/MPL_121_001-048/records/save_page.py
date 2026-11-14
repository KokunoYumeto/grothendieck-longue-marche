from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys

ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_121_001-048'
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save(data):
    n=int(data['scan'])
    page=ROOT/'pages'/f'{PREFIX}_121_scan{n:03d}.tex'
    assert not page.exists(), f'Page {n} already exists'
    assert data['text'].startswith(('\\cotefile{121}\n' if n==1 else '')+f'\\scanpage{{{n}}}')
    page.write_text(data['text'].rstrip()+'\n',encoding='utf-8')
    (ROOT/'records'/f'scan{n:03d}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    refresh()
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'121 scan {n:03d} done {utc()}\n')
    print(f'Saved scan {n:03d}: {len(data["elements"])} inventory elements; {len(data.get("doubts",[]))} doubt entries.')

def refresh():
    records=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'records').glob('scan*.json'))]
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for d in records:
            for i,e in enumerate(d['elements'],1):
                w.writerow([121,d['scan'],d['sheet_kind'],i,*e,'yes'])
    combined='\n'.join(p.read_text(encoding='utf-8').rstrip()+'\n' for p in sorted((ROOT/'pages').glob('*.tex')))
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined,encoding='utf-8')
    head=ROOT/'records'/'doubts_header.md'
    text=head.read_text(encoding='utf-8') if head.exists() else '# Doubts and notation\n'
    text+='\n## Doubt register\n\n| Cote | Scan | Approximate line / position | Reading | Alternatives / reason | Confidence |\n|---|---:|---|---|---|---|\n'
    for d in records:
        for a in d.get('doubts',[]):
            cells=[str(x).replace('|','\\|').replace('\n',' ') for x in [121,d['scan'],*a]]
            text+='| '+' | '.join(cells)+' |\n'
    tail=ROOT/'records'/'doubts_tail.md'
    if tail.exists(): text+='\n'+tail.read_text(encoding='utf-8')
    (ROOT/f'{PREFIX}_doubts.md').write_text(text,encoding='utf-8')

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='refresh': refresh()
    else: save(json.load(sys.stdin))
