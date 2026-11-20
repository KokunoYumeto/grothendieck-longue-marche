"""Apparatus helpers. Reading decisions are supplied by the main reader, never inferred."""
from pathlib import Path
import json,re,copy
W=Path(__file__).resolve().parents[1]

def load_page(n):
    return {r:json.loads((W/f'readers/{n:03}/{r}/report.json').read_text()) for r in 'ABC'}

def normalized(text):
    text=re.sub(r'\\cotefile\{109\}\s*','',text)
    return re.sub(r'\s+',' ',text).strip()

def crop_counts(n,viewed):
    out={r:sum(p.suffix.lower() in ['.jpg','.jpeg','.png'] for p in (W/f'readers/{n:03}/{r}/crops').glob('*')) for r in 'ABC'}
    out['main_new']=sum(p.suffix.lower() in ['.jpg','.jpeg','.png'] for p in (W/f'crops/{n:03}').glob('*'))
    out['main_reused']=len({p for p in viewed if p.startswith('readers/')})
    return out

def doubt_decisions(report,n,reader):
    out=[]
    for x in report['c_doubts']:
        d=copy.deepcopy(x)
        d['decision']=('Resolved/confirmed: ' if d.get('resolved') else 'Retained: ')+d.get('reading','')
        if d.get('crop'):
            p=Path(d['crop'])
            loc=str(p.relative_to(W)) if p.is_absolute() else f'readers/{n:03}/{reader}/'+str(p)
            d['evidence']+=' Crop: '+loc
        out.append(d)
    return out

def append_notation(n,entries):
    with (W/'notation.md').open('a') as f:
        for x in entries:
            cells=[x['sign'],f'{n:03}, '+x['location'],x['reading'],x['evidence']]
            f.write('| '+' | '.join(s.replace('|','&#124;').replace('\n',' ') for s in cells)+' |\n')

def write_record(n,reader,brief,text,decisions,cd,doubts,notes,coverage,viewed=None,events=None,equivalences=None,inventory=None,notation=None):
    rp=W/f'records/scan{n:03}.json'
    assert not rp.exists(),'An adjudicated page needs an explicit logged revision, not silent replacement.'
    R=load_page(n);base=R[reader];meta=json.loads((W/f'inputs/{n:03}/metadata.json').read_text())
    filename=Path(meta['codex_file']).name
    if not text.lstrip().startswith('\\cotefile'):text='\\cotefile{109}\n'+text
    (W/'pages'/filename).write_text(text)
    viewed=viewed or []
    rec={'scan':n,'folder':meta['folder'],'hua_has':meta['hua_has'],'filename':filename,
        'readers':[f'/root/scan{n:03}_{r}' for r in 'abc'],'brief':brief,
        'decisions':decisions,'c_doubts':cd,'doubts':doubts,'inventory':inventory if inventory is not None else base['inventory'],
        'notes':notes,'check_events':events or [],'abbreviations':base['abbreviations'],
        'coverage':coverage,'equivalences':equivalences or [],'crop_counts':crop_counts(n,viewed),'main_viewed_crops':viewed}
    rp.write_text(json.dumps(rec,ensure_ascii=False,indent=2))
    append_notation(n,notation if notation is not None else base['notation'])
    return rec
