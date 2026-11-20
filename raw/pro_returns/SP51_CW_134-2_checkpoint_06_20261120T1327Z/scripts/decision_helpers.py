"""Helpers for recording explicit main-reader decisions; never infer readings."""
from pathlib import Path
from datetime import datetime,timezone
import json,copy
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent

def load_reports(n):
    reports={r:json.loads((ROOT/f'records/scan{n}/{r}/report.json').read_text()) for r in 'ABC'}
    if not all(d.get('complete') for d in reports.values()):raise RuntimeError('Three completed readers are required.')
    return reports

def row(reports, reader, index, **overrides):
    d=copy.deepcopy(reports[reader]['differences'][index]);d.update(overrides)
    if d.get('crop','') and d['crop'].startswith('result/'):d['crop']=d['crop'][7:]
    if d.get('marked_in_H') in [True,'true','yes']:d['marked_in_H']='yes'
    else:d['marked_in_H']='no'
    return d

def write_decision(n, reader, replacements, differences, comparisons, unresolved,
                   inventory, notes, abbreviations, doubt_review, viewed_crops,
                   brief='briefs/brief_v02_scan171.md', workflow_note='',
                   extra_events=None, text_override=None):
    reports=load_reports(n)
    folder='H134-05' if n<178 else 'H134-06'
    name=f'{folder}_134-2_scan{n}.tex'
    text=(ROOT/f'records/scan{n}/{reader}/reading.tex').read_text() if text_override is None else text_override
    for old,new in replacements:
        if old not in text:raise ValueError(f'Absent old text for scan {n}: {old!r}')
        text=text.replace(old,new)
    if n!=170:text=text.replace('\\cotefile{134-2}\n','')
    for prefix in ['% C page filename:','% source page filename:']:
        text='\n'.join(l for l in text.split('\n') if not l.startswith(prefix))
    import re
    text=re.sub(r'(\\scanpage\{\d+\}\\mspage\{[^}]+\})(?!%)(\n)',r'\1%\2',text)
    if not text.endswith('\n'):text+='\n'
    (ROOT/'pages'/name).write_text(text)
    inv=copy.deepcopy(inventory)
    for x in inv:
        x['sheet_kind']='letter'
        if x.get('hand','').lower() in {'author', 'author hand', "author's hand", 'authorial main hand'}:x['hand']='his hand'
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    events=[]
    for r,rep in reports.items():
        for e in rep.get('check_events',[]):
            if not isinstance(e,dict):continue
            events.append({'statement_id':e.get('statement_id',f'S{n}-{r}-local-check'),'date':now,'who':f'GPT-6 Astra Pro; inherited effort not separately exposed; /root/scan{n}_{r.lower()}','type':e.get('type','carried as background without fault found'),'outcome':e.get('outcome','')+(' Method: '+e['method'] if e.get('method') else '')})
    events.append({'statement_id':f'S{n}-notes','date':now,'who':'GPT-6 Astra Pro; inherited effort not separately exposed; /root','type':'carried as background without fault found','outcome':'The source statements reported in this page’s notes were transcribed, not thereby proved. No external research was used. Any actual local mathematical check has its own narrowly scoped event; visual reading decisions remain in the changes log.'})
    events+=extra_events or []
    abbr=[]
    for x in abbreviations:
        if isinstance(x,dict):abbr.append({'written':x.get('written',x.get('written_form',x.get('form',''))),'expansion':x.get('expansion',x.get('possible_expansion',x.get('meaning','')))})
    crop_counts={r:len(reports[r].get('crops',[])) for r in 'ABC'}
    crop_counts['main']=len([p for p in (ROOT/f'crops/scan{n}/main').glob('*') if p.suffix.lower() in ['.jpg','.png']])
    d={'scan':n,'folder':folder,'filename':name,'brief':brief,'differences':differences,'reader_comparisons':comparisons,'doubt_review':doubt_review,'unresolved':unresolved,'inventory':inv,'notes':notes,'abbreviations':abbr,'check_events':events,'crop_counts':crop_counts,'workflow_note':workflow_note}
    dest=ROOT/f'records/scan{n}';dest.mkdir(exist_ok=True)
    (dest/'decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    (dest/'main_viewed_crops.txt').write_text('\n'.join(viewed_crops)+'\n')
    return d

def complete(n,next_n=None):
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    log=ROOT/'progress.log'
    if f'scan {n} done ' in log.read_text():raise RuntimeError(f'Scan {n} already logged done')
    with log.open('a') as f:f.write(f'scan {n} done {now}\n')
    if next_n is not None:
        d=ROOT/f'records/scan{next_n}';d.mkdir(exist_ok=True)
        (d/'notation_input.md').write_text((ROOT/'notation.md').read_text())
    print(f'scan {n} done {now}')

def register(n):
    now=datetime.now(timezone.utc).isoformat()
    with (ROOT/'records/assignments.tsv').open('a') as f:
        for r in 'ABC':f.write(f'{n}\t{r}\t/root/scan{n}_{r.lower()}\tGPT-6 Astra Pro\tinherited; not separately exposed\t{now}\n')

def add_notation(rows):
    with (ROOT/'notation.md').open('a') as f:
        for cells in rows:f.write('| '+' | '.join(str(x).replace('|','\\|') for x in cells)+' |\n')


def register_note_statements(n, statements):
    p=ROOT/'records/note_statements.json'
    registry=json.loads(p.read_text()) if p.exists() else {}
    for i,s in enumerate(statements,1):
        s.setdefault('id',f'S{n}-N{i}')
        s.setdefault('status','source assertion recorded without independent proof')
    registry[str(n)]=statements
    p.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
