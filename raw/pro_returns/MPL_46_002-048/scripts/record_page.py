from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_46_002-048'

def require_unfrozen():
    log = ROOT/'progress.log'
    if log.exists() and '\ntranscription frozen ' in log.read_text():
        raise RuntimeError('Transcription is frozen; record reading questions in research notes.')

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def arguments(text, macro):
    token='\\'+macro+'{'
    start=0
    while (pos:=text.find(token,start)) >= 0:
        begin=pos+len(token); depth=1; end=begin
        while end<len(text) and depth:
            if text[end]=='{' and (end==0 or text[end-1]!='\\'): depth+=1
            elif text[end]=='}' and (end==0 or text[end-1]!='\\'): depth-=1
            end+=1
        yield pos,text[begin:end-1]
        start=end

def cell(s):
    return str(s).replace('|','\\|').replace('\n',' ')

def rebuild():
    require_unfrozen()
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
    with (ROOT/(PREFIX+'_inventory.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for r in records:
            for k,row in enumerate(r['inventory'],1):
                w.writerow([46,r['scan'],r['sheet_kind'],f"{r['scan']:03d}.{k:02d}",*row,'yes'])
    parts=['# Notation table (maintained from the first page)\n', '| Visible form / use | LaTeX | Reading policy |', '|---|---|---|']
    seen=set()
    for r in records:
        for row in r.get('notation',[]):
            if tuple(row) not in seen:
                parts.append('| '+' | '.join(cell(s) for s in row)+' |');seen.add(tuple(row))
    parts+=['\n# Doubts\n','Confidence describes the proposed reading, not a mathematical reconstruction. Locations refer to the page block or to a LaTeX line in the page fragment (which preserves reading order, but is not a facsimile line count).','', '| File | Scan | Approximate line / position | Reading | Alternatives / reason | Confidence |','|---|---:|---|---|---|---|']
    for r in records:
        for row in r.get('doubts',[]): parts.append('| 46 | '+str(r['scan'])+' | '+' | '.join(cell(s) for s in row)+' |')
        for pos,arg in arguments(r['tex'],'unsure'):
            reading,sep,alt=arg.partition('|')
            row=[46,r['scan'],f"LaTeX line {r['tex'][:pos].count(chr(10))+1}",reading,alt if sep else 'Stroke / ending remains uncertain','medium']
            parts.append('| '+' | '.join(cell(s) for s in row)+' |')
        for pos,arg in arguments(r['tex'],'illegible'):
            row=[46,r['scan'],f"LaTeX line {r['tex'][:pos].count(chr(10))+1}",'\\illegible{'+arg+'}','Unreadable after visual inspection; estimated word count','low']
            parts.append('| '+' | '.join(cell(s) for s in row)+' |')
    parts+=['\n# Abbreviations\n','Expansions below are editorial aids only and are never substituted into the transcription.','', '| Abbreviation | Possible expansion |','|---|---|']
    seen=set()
    for r in records:
        for row in r.get('abbreviations',[]):
            if tuple(row) not in seen:
                parts.append('| '+' | '.join(cell(s) for s in row)+' |');seen.add(tuple(row))
    parts+=['\n# Legibility and reading record\n']
    for r in records:
        if r.get('observation'):parts.append(f"- Scan {r['scan']:03d}: {r['observation']}")
    assessment=ROOT/'records'/'legibility_assessment.md'
    if assessment.exists(): parts.append('\n'+assessment.read_text())
    (ROOT/(PREFIX+'_doubts.md')).write_text('\n'.join(parts)+'\n',encoding='utf-8')
    (ROOT/(PREFIX+'_transcription.tex')).write_text('\n'.join(r['tex'].rstrip() for r in records)+'\n',encoding='utf-8')

def save(scan, tex, inventory, sheet_kind='text', doubts=(), notation=(), abbreviations=(), observation=''):
    require_unfrozen()
    dest=ROOT/'pages'/f'{PREFIX}_46_scan{scan:03d}.tex'
    if dest.exists():raise FileExistsError(dest)
    tex=tex.strip()+'\n'
    if f'\\scanpage{{{scan}}}' not in tex:raise ValueError('Missing scan marker')
    dest.write_text(tex,encoding='utf-8')
    rec=dict(scan=scan,tex=tex,inventory=inventory,sheet_kind=sheet_kind,doubts=doubts,notation=notation,abbreviations=abbreviations,observation=observation)
    (ROOT/'records'/f'scan{scan:03d}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rebuild()
    with (ROOT/'progress.log').open('a') as f:f.write(f'46 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(tex)} characters; {len(inventory)} inventory elements')

def amend(scan, old, new, reason):
    require_unfrozen()
    p=ROOT/'records'/f'scan{scan:03d}.json'
    rec=json.loads(p.read_text())
    if old not in rec['tex']:raise ValueError('Old reading absent')
    rec['tex']=rec['tex'].replace(old,new)
    p.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'pages'/f'{PREFIX}_46_scan{scan:03d}.tex').write_text(rec['tex'],encoding='utf-8')
    with (ROOT/'progress.log').open('a') as f:f.write(f'46 scan {scan:03d} revised {utc()} {reason}\n')
    rebuild()
