"""Validate deliverable structure and evidence coverage; never judge manuscript ink."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, sys
from PIL import Image

W = Path(__file__).resolve().parents[1]
S = W.parent/'source'
PREFIX = 'SP76_C13_145+147'
final = '--final' in sys.argv
order = (W/'page_order.txt').read_text().splitlines()
errors = []
def require(condition, message):
    if not condition: errors.append(message)
def read_tsv(path):
    with path.open() as f: return list(csv.DictReader(f, delimiter='\t'))
def check_box(box, size, label):
    require(isinstance(box, (list, tuple)) and len(box)==4, label+': missing original box')
    if not isinstance(box, (list, tuple)) or len(box)!=4: return
    x0,y0,x1,y1=box
    require(0<=x0<x1<=size[0] and 0<=y0<y1<=size[1], label+': invalid original box')
def brace_check(text):
    level=0
    for line in text.splitlines():
        line=re.split(r'(?<!\\)%', line, maxsplit=1)[0]
        for m in re.finditer(r'(?<!\\)[{}]', line):
            level+=1 if m.group()=='{' else -1
            if level<0: return False
    return level==0

kinds={'misread word','misread symbol or index','omission','text not on the page',
       'deletion state','insertion or placement','abbreviation expanded or spelling modernised',
       'readable ink left as \\ill{}','drawing or diagram','other'}
inventory_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
sheet_kinds={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
confidences={'high','medium','low'}
viewed={Path(x.strip()).name for x in (W/'reports/root_viewed_crops.txt').read_text().splitlines() if x.strip()}
assignments=json.loads((W/'reports/assignments.json').read_text())
marks=read_tsv(S/(PREFIX+'_texts')/'MARKS.tsv')
require(len(order)==24 and len(set(order))==24, 'Expected exactly 24 unique pages')
reports=[]
for page in order:
    rp=W/'reports'/f'{page}.json'
    if not rp.exists():
        require(not final, page+': missing report')
        continue
    r=json.loads(rp.read_text())
    if not r.get('adjudicated'):
        require(not final, page+': first reading not committed')
        continue
    reports.append(r)
    require(r['page']==page, page+': report identity mismatch')
    with Image.open(S/(PREFIX+'_scans')/(page+'.jpg')) as im: size=im.size
    pp=W/'pages'/(page+'.tex')
    require(pp.is_file(), page+': missing page file')
    if pp.is_file():
        tex=pp.read_text()
        require(brace_check(tex), page+': unbalanced unescaped TeX braces')
        require('\\scanpage{'+str(int(r['scan']))+'}' in tex, page+': missing correct scan marker')
    for x in r['changes']:
        label=page+' '+x['place']
        require(x['kind'] in kinds, label+': invalid collation kind')
        require(x['confidence'] in confidences, label+': invalid confidence')
        require(x.get('against_C') or x.get('against_H') or x.get('certainty_resolution_C'), label+': certainty-only row belongs in doubts')
        require(bool(x.get('crop')), label+': missing evidence crop')
        if x.get('crop'):
            require((W/x['crop']).is_file(), label+': nonexistent crop')
            require(Path(x['crop']).name in viewed, label+': crop not in root viewing ledger')
            check_box(x.get('box'), size, label)
    page_marks=[m for m in marks if m['cote']==str(r['cote']) and int(m['scan'])==int(r['scan'])]
    for x in r.get('additional_crop_checks',[]):
        label=page+' unchanged inspection '+x['place']
        require((W/x['crop']).is_file(),label+': nonexistent crop')
        require(Path(x['crop']).name in viewed,label+': crop not in root viewing ledger')
        check_box(x.get('box'),size,label)
    require([d['id'] for d in r['decisions']]==[m['id'] for m in page_marks], page+': mark IDs/order do not match input')
    for d in r['decisions']:
        label=page+' '+d['id']
        require(d['decision'] in {'first','alternative','other','undecided'}, label+': invalid decision')
        require(d['confidence'] in confidences, label+': invalid confidence')
        if d['decision']!='undecided':
            require(bool(d.get('crop')) and d['crop']!='page', label+': resolved mark lacks crop')
            if d.get('crop') and d['crop']!='page':
                require((W/d['crop']).is_file(), label+': nonexistent resolved-mark crop')
                require(Path(d['crop']).name in viewed, label+': mark crop not in root viewing ledger')
            check_box(d.get('box'), size, label)
    require(len({x['element'] for x in r['inventory']})==len(r['inventory']), page+': duplicate inventory element')
    for x in r['inventory']:
        require(x['kind'] in inventory_kinds and x['sheet_kind'] in sheet_kinds, page+': invalid inventory classification')
        require(x['transcribed']=='yes', page+': untranscribed inventory element')
    boxes=read_tsv(W/'second'/f'{page}_boxes.tsv')
    first=read_tsv(W/'second'/f'{page}_first.tsv')
    require([x['box'] for x in boxes]==[x['box'] for x in first], page+': first readings differ from box list')
    require(len({x['box'] for x in boxes})==len(boxes), page+': duplicate second box')
    for x in boxes: check_box([int(x[k]) for k in ['x0','y0','x1','y1']],size,page+' '+x['box'])
    require(not final or r.get('audited'), page+': second reading not adjudicated' if final else '')
    if r.get('audited'):
        require(assignments['first'][page]!=assignments['second'][page], page+': second reader is first reader')
        second=read_tsv(W/'second'/f'{page}_second.tsv')
        comparison=read_tsv(W/'second'/f'{page}_comparison.tsv')
        require([x['box'] for x in second]==[x['box'] for x in boxes], page+': second readings differ from box list')
        mismatches={x['box'] for x in comparison if x['exact_token_match']=='no'}
        adjudications=r['audit']['adjudications']
        require({x['box'] for x in adjudications}==mismatches, page+': unadjudicated token mismatch')
        for x in adjudications:
            require((W/x['crop']).is_file(), page+' '+x['box']+': missing second evidence crop')
            require(Path(x['crop']).name in viewed, page+' '+x['box']+': second crop not in root viewing ledger')

present={r['page'] for r in reports}
require({p.stem for p in (W/'pages').glob('*.tex')}==present, 'Page files do not equal committed report set')
expected_ids=[m['id'] for m in marks if f"{m['cote']}_scan{int(m['scan']):03d}" in present]
require([x['id'] for x in read_tsv(W/'decisions.tsv')]==expected_ids, 'Combined decisions missing, duplicated, or out of order')
combined=[];prev=None
for r in reports:
    if r['cote']!=prev: combined.append('\\cotefile{'+str(r['cote'])+'}\n');prev=r['cote']
    combined.append((W/'pages'/f"{r['page']}.tex").read_text().rstrip()+'\n')
require((W/(PREFIX+'_transcription.tex')).read_text()=='\n'.join(combined), 'Combined transcription differs from ordered page files')
first_manifest=W/'second/first_readings_manifest.json'
if first_manifest.exists():
    first_hashes=json.loads(first_manifest.read_text())['files']
    require(len(first_hashes)==48,'Expected 24 immutable first readings and 24 box lists')
    for name,digest in first_hashes.items():
        p=W/name
        require(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest,'First reading or box list changed after blind-reading start: '+name)
if final:
    require(len(reports)==24, 'Final requires 24 committed pages')
    require(len(expected_ids)==len(marks), 'Not all original marks covered')
    for name in ['changes.md','doubts.md','inventory.csv','notes.md','collation.tsv','hand_log.md','sheet_feedback.md']:
        require((W/(PREFIX+'_'+name)).is_file(), 'Missing deliverable '+name)
    require((W/'reports/legibility.md').is_file(), 'Missing final legibility assessment')
    require((W/'reports/frozen_hashes.json').is_file(), 'Transcription not frozen')
    require(first_manifest.is_file(),'Missing pre-audit first-reading hash record')
result={'date':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'mode':'final' if final else 'partial','committed_pages':len(reports),'errors':errors}
(W/'reports'/('validation_final.json' if final else 'validation_partial.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
if errors: raise SystemExit(1)
