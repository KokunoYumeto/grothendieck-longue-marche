from pathlib import Path
import csv,hashlib,json,re,sys
from datetime import datetime,timezone
from PIL import Image

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
ORDER=json.loads((ROOT/'scripts/page_order.json').read_text())
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def table(path,sep='\t'):
    with path.open() as f:return list(csv.DictReader(f,delimiter=sep))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def uncomment(t):return re.sub(r'(?<!\\)%[^\n]*','',t)
def check_tex(p):
    t=uncomment(p.read_text());depth=0
    for m in re.finditer(r'\\.|[{}]',t):
        a=m.group()
        if a=='{':depth+=1
        elif a=='}':depth-=1
        assert depth>=0,(p.name,'unmatched closing brace',m.start())
    assert depth==0,(p.name,'unbalanced braces',depth)
    assert len(re.findall(r'(?<!\\)\$',t))%2==0,(p.name,'odd dollar count')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
        if m[1]=='begin':stack.append(m[2])
        else:assert stack and stack.pop()==m[2],(p.name,'environment mismatch',m.group())
    assert not stack,(p.name,stack)

mode=sys.argv[1] if len(sys.argv)>1 else 'validate'
paths=[ROOT/'pages'/f'150_scan{s}.tex' for s in ORDER]+[ROOT/'SP91_C13_150_transcription.tex']
if mode=='verify-frozen':
    stored=table(ROOT/'transcription_hashes.tsv')
    for x in stored:assert digest(ROOT/x['file'])==x['sha256'],x['file']
    with (ROOT/'progress.log').open('a') as f:f.write(f'Frozen transcription hashes checked unchanged {now()}: {len(stored)} files\n')
    print('Frozen hashes unchanged:',len(stored));raise SystemExit

assert len(list((ROOT/'pages').glob('*.tex')))==len(ORDER)
for p in paths:assert p.exists(),p;check_tex(p)
with (BASE/'input/SP91_C13_150_texts/MARKS.tsv').open() as f:marks=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
decisions=table(ROOT/'decisions.tsv')
assert [x['id'] for x in marks]==[x['id'] for x in decisions], 'Decision IDs/order differ'
first_hashes=table(ROOT/'second/first_reading_hashes.tsv')
assert len(first_hashes)==2*len(ORDER), 'Every box list and first reading needs its pre-audit hash'
for x in first_hashes:
    assert digest(ROOT/x['file'])==x['sha256'], ('Pre-audit file changed',x['file'])
audits=0;changes=0;crop_refs=set()
for s in ORDER:
    r=json.loads((ROOT/'records'/f'150_scan{s}.json').read_text());assert r.get('main_reviewed')
    assert r.get('audited'),('Missing audit adjudication',s)
    dims=Image.open(BASE/'input/SP91_C13_150_scans'/f'150_scan{s}.jpg').size
    bb=table(ROOT/'second'/f'150_scan{s}_boxes.tsv');ff=table(ROOT/'second'/f'150_scan{s}_first.tsv');ss=table(ROOT/'second'/f'150_scan{s}_second.tsv')
    ids=[b['box'] for b in bb]
    assert len(ids)==len(set(ids)),s
    assert ids==[b['box'] for b in ff]==[b['box'] for b in ss],s
    for b in bb:
        x0,y0,x1,y1=(int(b[k]) for k in ['x0','y0','x1','y1'])
        assert 0<=x0<x1<=dims[0] and 0<=y0<y1<=dims[1],(s,b)
        assert (ROOT/'crops'/f"150_scan{s}_second_{b['box']}.png").exists(),(s,b['box'])
    audits+=len(bb);changes+=len(r['changes'])
    for c in r.get('crops',[]):
        assert (ROOT/c['file']).exists(),c;crop_refs.add(c['file'])
    for d in r['decisions']:
        assert d['decision'] in ['first','alternative','other','undecided'],d
        if d['decision']!='undecided':assert d['crop']!='page' and (ROOT/d['crop']).exists(),d
    cmp=json.loads((ROOT/'second'/f'150_scan{s}_comparison.json').read_text())
    adjud=table(ROOT/'second'/f'150_scan{s}_adjudication.tsv')
    assert [x['box'] for x in cmp if x['different']]==[x['box'] for x in adjud],('Every token difference must be adjudicated',s)
required=['SP91_C13_150_changes.md','SP91_C13_150_collation.tsv','decisions.tsv','SP91_C13_150_doubts.md','SP91_C13_150_inventory.csv','SP91_C13_150_notes.md','CHECK_EVENTS.tsv','progress.log','SP91_C13_150_sheet_feedback.md','SP91_C13_150_hand_log.md']
for name in required:assert (ROOT/name).exists()
inventory=table(ROOT/'SP91_C13_150_inventory.csv',',')
assert {int(x['scan']) for x in inventory}=={int(s) for s in ORDER}
assert all(x['transcribed']=='yes' for x in inventory)
report={'pages':len(ORDER),'decisions':len(decisions),'audit_boxes':audits,'change_rows_including_certainty_records':changes,'inventory_elements':len(inventory),'first_pass_crop_refs':len(crop_refs),'png_files':len(list((ROOT/'crops').glob('*.png'))),'checked_at':now(),'checks':'File/ID/order/crop coverage, TeX brace/dollar/environment syntax, all blind differences adjudicated; no TeX compilation.'}
(ROOT/'validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if mode=='freeze':
    assert not (ROOT/'transcription_hashes.tsv').exists(), 'Already frozen'
    with (ROOT/'transcription_hashes.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['file','sha256']);w.writerows([[p.relative_to(ROOT).as_posix(),digest(p)] for p in paths])
    with (ROOT/'progress.log').open('a') as f:
        f.write('transcription frozen '+now()+'\n')
        for p in paths:f.write(digest(p)+'  '+p.relative_to(ROOT).as_posix()+'\n')
