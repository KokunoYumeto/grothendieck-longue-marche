"""Static source/evidence checks only. No OCR or TeX compilation."""
from pathlib import Path
import csv,json,re,hashlib,sys,collections
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
SCANS=list(range(108,118))+list(range(119,132))
errors=[];warnings=[]
def require(ok,msg):
    if not ok:errors.append(msg)
def braces(s):
    level=0
    for line in s.splitlines():
        line=re.split(r'(?<!\\)%',line)[0]
        for m in re.finditer(r'(?<!\\)[{}]',line):
            level+=1 if m.group()=='{' else -1
            if level<0:return False
    return level==0
pages=list((ROOT/'pages').glob('147_scan*.tex'))
require({p.stem for p in pages}=={f'147_scan{s}' for s in SCANS},'Page set is not exactly the 23 supplied scans.')
for p in pages:
    s=p.read_text()
    require(braces(s),'Unbalanced braces: '+p.name)
    require(not re.search(r'\\(?:documentclass|begin\{document\}|end\{document\}|note|struck|marginal|uncertain|ill|add)\b',s),'Foreign/preamble macro: '+p.name)
    require(bool(re.search(r'\\scanpage\{[0-9]+\}',s)),'Missing scanpage: '+p.name)
combined=ROOT/'SP80_C13_147_transcription.tex'
expected='\\cotefile{147}\n\n'+'\n\n'.join((ROOT/'pages'/f'147_scan{s}.tex').read_text().rstrip() for s in SCANS if (ROOT/'pages'/f'147_scan{s}.tex').exists())+'\n'
require(combined.exists() and combined.read_text()==expected,'Combined fragment differs from ordered individual pages.')
marks=list(csv.DictReader((BASE/'source/SP80_C13_147_texts/MARKS.tsv').open(),delimiter='\t'))
decisions=list(csv.DictReader((ROOT/'decisions.tsv').open(),delimiter='\t'))
require([r['id'] for r in decisions]==[r['id'] for r in marks],'Decisions do not match all supplied MARKS in order.')
for r in decisions:
    require(r['decision'] in {'first','alternative','other','undecided'},'Invalid decision '+r['id'])
    if r['decision']!='undecided':require('crops/' in r['crop'],'Resolved doubt without crop '+r['id'])
for scan in SCANS:
    stem=f'147_scan{scan}';report=ROOT/'review'/f'{stem}_reviewed.json'
    require(report.exists(),'Missing root review '+stem)
    if not report.exists():continue
    d=json.loads(report.read_text())
    for i,r in enumerate(d['rows']):
        require(r.get('against_C') or r.get('against_H'),f'Row against neither witness: {scan} #{i}')
        require(bool(r.get('crop')) and (ROOT/r['crop']).is_file(),f'Missing evidence crop: {scan} #{i} {r.get("crop")}')
    for phase in ['boxes','first','second','comparison','adjudications']:
        require((ROOT/'second'/f'{stem}_{phase}.tsv').exists(),f'Missing {phase}: {stem}')
inv=list(csv.DictReader((ROOT/'SP80_C13_147_inventory.csv').open()))
require(all(r['transcribed']=='yes' for r in inv),'Inventory has untranscribed elements.')
require(all(r['sheet_kind'] in {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'} for r in inv),'Inventory has an unsupported sheet kind.')
require(all(r['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for r in inv),'Inventory has an unsupported element kind.')
assignments=json.loads((ROOT/'review/assignments.json').read_text())
for scan in SCANS:
    require(str(scan) in assignments['second'],f'Missing independent-reader assignment {scan}')
    if str(scan) in assignments['second']:
        require(assignments['second'][str(scan)]!=assignments['first'][str(scan)],f'Same reader in both passes {scan}')
    stem=f'147_scan{scan}'
    paths={suffix:ROOT/'second'/f'{stem}_{suffix}.tsv' for suffix in ('boxes','first','second','comparison','adjudications')}
    if not all(p.exists() for p in paths.values()):continue
    records={suffix:list(csv.DictReader(p.open(),delimiter='\t')) for suffix,p in paths.items()}
    ids={suffix:[r['box'] for r in rows] for suffix,rows in records.items()}
    for suffix in ('first','second','comparison'):
        require(ids[suffix]==ids['boxes'],f'Box order/coverage mismatch {stem} {suffix}')
    meta_path=ROOT/'second'/f'{stem}_comparison_meta.json'
    require(meta_path.exists(),f'Missing pre-comparison reading hashes {stem}')
    if meta_path.exists():
        meta=json.loads(meta_path.read_text())
        require(all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in meta['sha256'].items()),f'A first or second reading changed after comparison {stem}')
    require(len(ids['adjudications'])==len(set(ids['adjudications'])),f'Duplicate adjudications {stem}')
    differing={r['box'] for r in records['comparison'] if r['equal']=='no'}
    require(differing<=set(ids['adjudications']),f'Unadjudicated differing boxes {stem}')
frozen_first=ROOT/'second/first_readings_frozen.json'
require(frozen_first.exists(),'First-reading baseline was not frozen before blind reading.')
if frozen_first.exists():
    record=json.loads(frozen_first.read_text())
    require(all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in record['sha256'].items()),'Frozen first readings or box lists were altered.')
for p in (ROOT/'reports').glob('*_crops.jsonl'):
    for line in p.read_text().splitlines():
        r=json.loads(line);require((ROOT/r['crop']).is_file(),'Missing crop from manifest '+r['crop'])
log=(ROOT/'progress.log').read_text()
for scan in SCANS:
    require(f'scan {scan} done ' in log,f'Missing completion log {scan}')
    require(f'scan {scan} audited ' in log,f'Missing audit log {scan}')
print(json.dumps({'errors':errors,'warnings':warnings,'page_count':len(pages),'decisions':len(decisions),'inventory_elements':len(inv),'crops':len(list((ROOT/'crops').glob('*.jpg')))},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
