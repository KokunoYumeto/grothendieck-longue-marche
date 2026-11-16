from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / 'records'
REC.mkdir(exist_ok=True)

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def macro_arguments(text, name):
    marker = '\\' + name + '{'
    start = 0
    while (p := text.find(marker, start)) >= 0:
        i, depth = p + len(marker), 1
        j = i
        while j < len(text) and depth:
            if text[j] == '{' and (j == 0 or text[j-1] != '\\'): depth += 1
            if text[j] == '}' and (j == 0 or text[j-1] != '\\'): depth -= 1
            j += 1
        yield text[i:j-1], text.count('\n', 0, p) + 1
        start = j

def refresh():
    notation = (REC/'notation.md').read_text(encoding='utf-8')
    s = '# MPL 133 — notation and doubts\n\n' + notation + '\n\n## Doubt register\n\n'
    s += 'Locations use the approximate line in the page fragment; retained line breaks follow the handwriting where practicable. An entire marked phrase means its uncertain letters or endings could not be separated securely. The first alternative is the visual reading, without grammatical correction.\n\n'
    s += '| Cote | Scan | Approx. fragment line | Reading | Alternative / qualification | Confidence |\n|---|---:|---:|---|---|---|\n'
    for p in sorted(REC.glob('scan*.json')):
        d = json.loads(p.read_text())
        for arg,line in macro_arguments(d['tex'], 'unsure'):
            parts=arg.split('|',1)
            read=parts[0].replace('|','\\|').replace('\n',' ')
            alt=(parts[1] if len(parts)>1 else 'Uncertain ink; no secure alternative').replace('|','\\|').replace('\n',' ')
            confidence='low' if '?' in arg else 'medium'
            s += f'| 133 | {d["scan"]:03} | {line} | `{read}` | {alt} | {confidence} |\n'
        for arg,line in macro_arguments(d['tex'], 'illegible'):
            s += f'| 133 | {d["scan"]:03} | {line} | `\\illegible{{{arg}}}` | Estimated word count; ink not resolved after enlargement | low |\n'
        for row in d.get('doubts',[]):
            loc,read,alt,conf=row
            s+=f'| 133 | {d["scan"]:03} | {loc} | {read.replace("|"," / ")} | {alt.replace("|"," / ")} | {conf} |\n'
    s+='\n## Abbreviations\n\n'+(REC/'abbreviations.md').read_text()+'\n\n## Legibility and limitations\n\n'+(REC/'legibility.md').read_text()+'\n'
    (ROOT/'MPL_133_doubts.md').write_text(s,encoding='utf-8')
    pages=sorted((ROOT/'pages').glob('MPL_133_133_scan*.tex'))
    (ROOT/'MPL_133_transcription.tex').write_text(''.join(p.read_text() for p in pages),encoding='utf-8')

def save(scan, tex, kind, elements, doubts=None, observations=''):
    path=ROOT/'pages'/f'MPL_133_133_scan{scan:03}.tex'
    if path.exists(): raise RuntimeError(f'Page already exists: {path}')
    if not tex.endswith('\n'): tex+='\n'
    path.write_text(tex,encoding='utf-8')
    data=dict(scan=scan,tex=tex,sheet_kind=kind,elements=elements,doubts=doubts or [],observations=observations)
    (REC/f'scan{scan:03}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    with (ROOT/'MPL_133_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for n,(typ,pos,first) in enumerate(elements,1): w.writerow(['133',str(scan),kind,f'{scan:03}-{n:02}',typ,pos,first,'yes'])
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'133 scan {scan:03} done {utc()}\n')
    if observations:
        with (REC/'observations.md').open('a',encoding='utf-8') as f: f.write(f'\n## Scan {scan:03}\n\n{observations}\n')
    refresh()
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements; {len(tex)} characters; {utc()}')
