"""Static source/evidence checks only. No OCR or TeX compilation."""
from pathlib import Path
from datetime import datetime
import argparse,csv,json,re,hashlib,sys,collections
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
SCANS=list(range(108,118))+list(range(119,132))
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--final',action='store_true',help='Also require the final 24-file freeze and logged unchanged-hash verification.')
args=parser.parse_args()
errors=[];warnings=[]
COLLATION_KINDS={'misread word','misread symbol or index','omission','text not on the page',
    'deletion state (struck given live or live given struck)','insertion or placement',
    'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}',
    'drawing or diagram','other'}
ERROR_CATEGORIES={'Symbols and indices','Words','Omissions','Drawings and diagrams',
    'Readable ink left as illegible','Insertions put in the wrong place','Struck text',
    'Abbreviations expanded, spelling modernised','Text that is not on the page','Other'}
REQUIRED_ARTIFACTS=[
    'SP80_C13_147_transcription.tex','SP80_C13_147_changes.md',
    'SP80_C13_147_collation.tsv','decisions.tsv','SP80_C13_147_doubts.md',
    'SP80_C13_147_inventory.csv','SP80_C13_147_notes.md','CHECK_EVENTS.tsv',
    'progress.log','SP80_C13_147_sheet_feedback.md','SP80_C13_147_hand_log.md']
TABLE_SCHEMAS={
    'SP80_C13_147_collation.tsv':('\t',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']),
    'decisions.tsv':('\t',['id','cote','scan','decision','reading','what the ink shows','crop','confidence']),
    'CHECK_EVENTS.tsv':('\t',['statement_id','date','who','type','outcome']),
    'SP80_C13_147_inventory.csv':(',',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'])}
SECOND_SCHEMAS={
    'boxes':['box','kind','x0','y0','x1','y1'],
    'first':['box','reading'],'second':['box','reading'],
    'comparison':['box','equal','first','second','token_differences'],
    'adjudications':['box','first','second','final','evidence','changed','crop']}
CHECK_EVENT_TYPES={'targeted proof check','independent re-proof',
    'computation or formal certificate','used and rechecked in this run',
    'carried as background without fault found','refuted, with refined statement id'}
FORBIDDEN_MACROS=re.compile(
    r'\\(?:documentclass|note|struck|marginal|uncertain|ill|add)\b'
    r'|\\(?:begin|end)\s*\{\s*document\s*\}')
def require(ok,msg):
    if not ok:errors.append(msg)
def read_table(path,columns,delimiter='\t'):
    # The caller checks existence, so a missing required artifact stays a
    # validation error rather than becoming an unhandled open() exception.
    if not path.is_file():return []
    try:
        with path.open(newline='') as f:
            reader=csv.DictReader(f,delimiter=delimiter)
            require(reader.fieldnames==columns,f'Incorrect header: {path.relative_to(ROOT)}; expected {columns}, found {reader.fieldnames}')
            if reader.fieldnames!=columns:return []
            rows=[]
            for line,row in enumerate(reader,2):
                valid=None not in row and all(row.get(k) is not None for k in columns)
                require(valid,f'Incorrect field count: {path.relative_to(ROOT)} row {line}')
                if valid:rows.append(row)
            return rows
    except (OSError,UnicodeError,csv.Error) as exc:
        require(False,f'Cannot read table {path.relative_to(ROOT)}: {exc}')
        return []
def validate_check_events(events):
    require(bool(events),'CHECK_EVENTS.tsv contains no check events.')
    for line,event in enumerate(events,2):
        label=f'CHECK_EVENTS.tsv row {line} ({event.get("statement_id","")})'
        for field in TABLE_SCHEMAS['CHECK_EVENTS.tsv'][1]:
            require(bool(event.get(field,'').strip()),f'Empty {field}: {label}')
        event_date=event.get('date','')
        valid_date=bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}',event_date))
        if valid_date:
            try:datetime.strptime(event_date,'%Y-%m-%d')
            except ValueError:valid_date=False
        require(valid_date,f'Invalid ISO calendar date: {label}')
        require(event.get('type') in CHECK_EVENT_TYPES,f'Unsupported check-event type: {label}')
        who=event.get('who','')
        provenance_parts=[p.strip() for p in who.split(';') if p.strip()]
        require(len(provenance_parts)>=3 and re.search(r'\beffort\b',who,re.I) and re.search(r'\brun\b',who,re.I),
                f'Provenance must identify model, effort and run: {label}')
def check_final_freeze(log):
    record_path=ROOT/'review/frozen_hashes.json'
    require(record_path.is_file(),'Final gate: missing review/frozen_hashes.json.')
    if not record_path.is_file():return
    try:record=json.loads(record_path.read_text())
    except (OSError,UnicodeError,ValueError) as exc:
        require(False,f'Final gate: cannot read freeze record: {exc}')
        return
    require(isinstance(record,dict),'Final gate: freeze record must be an object.')
    if not isinstance(record,dict):return
    hashes=record.get('sha256')
    require(isinstance(hashes,dict),'Final gate: missing SHA-256 mapping.')
    if not isinstance(hashes,dict):return
    expected={f'pages/147_scan{s}.tex' for s in SCANS}|{'SP80_C13_147_transcription.tex'}
    require(set(hashes)==expected and len(hashes)==24,
            'Final gate: frozen hash record must contain exactly the 23 supplied page files and combined transcription.')
    for name in sorted(expected):
        digest=hashes.get(name)
        valid_digest=isinstance(digest,str) and bool(re.fullmatch(r'[0-9a-f]{64}',digest))
        require(valid_digest,f'Final gate: invalid or missing SHA-256 for {name}.')
        path=ROOT/name
        require(path.is_file(),f'Final gate: missing frozen file {name}.')
        if valid_digest and path.is_file():
            require(hashlib.sha256(path.read_bytes()).hexdigest()==digest,f'Final gate: frozen bytes changed: {name}.')
    frozen_at=record.get('frozen_at','')
    try:
        frozen_time=datetime.strptime(frozen_at,'%Y-%m-%d %H:%M:%S UTC')
        valid_time=frozen_time.strftime('%Y-%m-%d %H:%M:%S UTC')==frozen_at
    except (TypeError,ValueError):valid_time=False
    require(valid_time,'Final gate: missing or invalid frozen_at UTC timestamp.')
    if not valid_time:return
    lines=log.splitlines()
    freeze_lines=[i for i,line in enumerate(lines) if line.startswith('transcription frozen ')]
    require(len(freeze_lines)==1 and lines[freeze_lines[0]]=='transcription frozen '+frozen_at,
            'Final gate: progress.log must contain the single matching transcription-frozen entry.')
    if len(freeze_lines)!=1 or lines[freeze_lines[0]]!='transcription frozen '+frozen_at:return
    freeze_index=freeze_lines[0]
    recheck_pattern=re.compile(r'frozen SHA-256 hashes rechecked (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC): all 23 page files and combined transcription unchanged')
    rechecks=[]
    for i,line in enumerate(lines):
        match=recheck_pattern.fullmatch(line)
        if match and i>freeze_index:
            try:recheck_time=datetime.strptime(match.group(1),'%Y-%m-%d %H:%M:%S UTC')
            except ValueError:continue
            if recheck_time>=frozen_time:rechecks.append(i)
    require(bool(rechecks),'Final gate: no dated unchanged-hash verification is logged after the freeze.')
    if rechecks:
        freeze_block=lines[freeze_index+1:rechecks[-1]]
        for name in sorted(expected):
            require(f'SHA-256 {name} {hashes.get(name)}' in freeze_block,
                    f'Final gate: missing matching logged SHA-256 for {name}.')
def braces(s):
    level=0
    for line in s.splitlines():
        line=re.split(r'(?<!\\)%',line)[0]
        for m in re.finditer(r'(?<!\\)[{}]',line):
            level+=1 if m.group()=='{' else -1
            if level<0:return False
    return level==0
for name in REQUIRED_ARTIFACTS:
    require((ROOT/name).is_file(),'Missing mandatory artifact: '+name)
tables={name:read_table(ROOT/name,columns,delimiter) for name,(delimiter,columns) in TABLE_SCHEMAS.items()}
check_events=tables['CHECK_EVENTS.tsv']
validate_check_events(check_events)
pages=list((ROOT/'pages').glob('147_scan*.tex'))
require({p.stem for p in pages}=={f'147_scan{s}' for s in SCANS},'Page set is not exactly the 23 supplied scans.')
for p in pages:
    s=p.read_text()
    require(braces(s),'Unbalanced braces: '+p.name)
    require(not FORBIDDEN_MACROS.search(s),'Foreign/preamble macro: '+p.name)
    require(bool(re.search(r'\\scanpage\{[0-9]+\}',s)),'Missing scanpage: '+p.name)
combined=ROOT/'SP80_C13_147_transcription.tex'
expected='\\cotefile{147}\n\n'+'\n\n'.join((ROOT/'pages'/f'147_scan{s}.tex').read_text().rstrip() for s in SCANS if (ROOT/'pages'/f'147_scan{s}.tex').exists())+'\n'
require(combined.exists() and combined.read_text()==expected,'Combined fragment differs from ordered individual pages.')
marks=list(csv.DictReader((BASE/'source/SP80_C13_147_texts/MARKS.tsv').open(),delimiter='\t'))
decisions=tables['decisions.tsv']
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
        require(r.get('crop','').startswith('crops/'),f'Evidence is outside retained crops: {scan} #{i}')
        require(r.get('kind') in COLLATION_KINDS,f'Unsupported collation kind: {scan} #{i} {r.get("kind")}')
        require(r.get('error_category') in ERROR_CATEGORIES,f'Unsupported error-sheet category: {scan} #{i} {r.get("error_category")}')
        require(r.get('confidence') in {'high','medium','low'},f'Unsupported confidence: {scan} #{i}')
    for phase in ['boxes','first','second','comparison','adjudications']:
        require((ROOT/'second'/f'{stem}_{phase}.tsv').exists(),f'Missing {phase}: {stem}')
inv=tables['SP80_C13_147_inventory.csv']
require(all(r['transcribed']=='yes' for r in inv),'Inventory has untranscribed elements.')
require(all(r['sheet_kind'] in {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'} for r in inv),'Inventory has an unsupported sheet kind.')
require(all(r['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for r in inv),'Inventory has an unsupported element kind.')
assignments=json.loads((ROOT/'review/assignments.json').read_text())
for scan in SCANS:
    require(str(scan) in assignments['second'],f'Missing independent-reader assignment {scan}')
    if str(scan) in assignments['second']:
        require(assignments['second'][str(scan)]!=assignments['first'][str(scan)],f'Same reader in both passes {scan}')
        require(scan not in assignments.get('blind_exclusions',{}).get(assignments['second'][str(scan)],[]),f'Blind reader exposed to witnesses {scan}')
    stem=f'147_scan{scan}'
    paths={suffix:ROOT/'second'/f'{stem}_{suffix}.tsv' for suffix in ('boxes','first','second','comparison','adjudications')}
    if not all(p.exists() for p in paths.values()):continue
    records={suffix:read_table(p,SECOND_SCHEMAS[suffix]) for suffix,p in paths.items()}
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
    manifest=ROOT/'reports'/f'{stem}_crops.jsonl'
    crop_records=[json.loads(line) for line in manifest.read_text().splitlines()]
    for box in records['boxes']:
        name=f'crops/{stem}_second_{box["box"]}.jpg'
        matches=[r for r in crop_records if r['crop']==name]
        require(len(matches)==1,f'Fresh crop not recorded exactly once: {name}')
        if len(matches)==1:
            require(matches[0]['box']==[int(box[k]) for k in ('x0','y0','x1','y1')],f'Fresh crop coordinates changed: {name}')
            require(matches[0]['stage']=='second',f'Wrong fresh-crop stage: {name}')
frozen_first=ROOT/'second/first_readings_frozen.json'
require(frozen_first.exists(),'First-reading baseline was not frozen before blind reading.')
if frozen_first.exists():
    record=json.loads(frozen_first.read_text())
    require(all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in record['sha256'].items()),'Frozen first readings or box lists were altered.')
for p in (ROOT/'reports').glob('*_crops.jsonl'):
    for line in p.read_text().splitlines():
        r=json.loads(line);require((ROOT/r['crop']).is_file(),'Missing crop from manifest '+r['crop'])
log=(ROOT/'progress.log').read_text() if (ROOT/'progress.log').is_file() else ''
for scan in SCANS:
    require(f'scan {scan} done ' in log,f'Missing completion log {scan}')
    require(f'scan {scan} audited ' in log,f'Missing audit log {scan}')
if args.final:check_final_freeze(log)
print(json.dumps({'errors':errors,'warnings':warnings,'final_mode':args.final,'page_count':len(pages),'decisions':len(decisions),'check_events':len(check_events),'inventory_elements':len(inv),'crops':len(list((ROOT/'crops').glob('*.jpg')))},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
