"""Final structural/evidence verification. No OCR, image reading or TeX compilation."""
from pathlib import Path
import csv,json,hashlib,re,collections,datetime,sys
W=Path(__file__).resolve().parents[1];ROOT=W.parent;P='SP89_C13_149+150'
order=(W/'scripts/page_order.txt').read_text().split();errors=[]
def require(ok,msg):
 if not ok:errors.append(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p,**kw):
 with p.open() as f:return list(csv.DictReader(f,delimiter='\t',**kw))
def clean(t):return re.sub(r'(?<!\\)%[^\n]*','',t)
rs=[];fixed=[];sum_a=collections.Counter();commands=collections.Counter();comb=[];last=None
originaldiff=rows(ROOT/'source'/f'{P}_C_H_differences.tsv',quoting=csv.QUOTE_NONE);diffcount=collections.Counter(x['page'].removesuffix('.tex') for x in originaldiff)
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
allowed_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
for page in order:
 r=json.loads((W/'reports'/page/'report.json').read_text());rs.append(r)
 require(bool(r.get('audited_utc')),page+' audit missing')
 c=json.loads((W/'second'/f'{page}_comparison.json').read_text());meta=json.loads((W/'second'/f'{page}_comparison_meta.json').read_text());assign=json.loads((W/'second'/f'{page}_assignment.json').read_text())
 require(assign['reader']!=assign['first_reader'],page+' readers not independent')
 bs=rows(W/'second'/f'{page}_boxes.tsv');fst=rows(W/'second'/f'{page}_first.tsv');snd=rows(W/'second'/f'{page}_second.tsv');adj=json.loads((W/'second'/f'{page}_adjudications.json').read_text());dec=json.loads((W/'second'/f'{page}_root_decisions.json').read_text())
 require([x['box'] for x in bs]==[x['box'] for x in fst]==[x['box'] for x in snd]==[x['box'] for x in c],page+' fixed box order mismatch')
 for suffix,key in [('first.tsv','first_sha256'),('second.tsv','second_sha256')]:
  f=W/'second'/f'{page}_{suffix}';h=sha(f);require(h==meta[key],page+' fixed '+suffix+' hash mismatch');fixed.append({'path':str(f.relative_to(W)),'sha256':h})
 differing=[x['box'] for x in c if not x['token_equal']]
 require([x['box'] for x in adj]==differing==[x['box'] for x in dec],page+' adjudication coverage mismatch')
 require(all(x.get('evidence') and (W/x['crop']).exists() for x in adj),page+' missing root crop evidence')
 require(sum(bool(x['changed']) for x in adj)==r['audit_counts']['changed_boxes'],page+' revised count mismatch')
 sum_a.update(r['audit_counts'])
 cov=r['diff_coverage'];require([int(x['row']) for x in cov]==list(range(1,diffcount[page]+1)),page+' supplied C/H difference coverage mismatch')
 require(all(x.get('disposition') for x in cov),page+' empty difference disposition')
 for x in r['changes']:require(x['kind'] in kinds,page+' invalid collation kind '+x['id'])
 for e in r['check_events']:
  require(e['type'] in allowed_events or e['type'].startswith('refuted, with refined'),page+' invalid mathematical event type '+e['type'])
  require(bool(e['statement_id']) and bool(e['outcome']),page+' empty mathematical event')
 text=(W/'pages'/f'{page}.tex').read_text();commands.update(re.findall(r'\\[A-Za-z]+',clean(text)))
 for m in re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',clean(text),re.S):
  require('ampersand replacement=\\&' in m.group(),page+' matrix lacks explicit ampersand replacement')
  require(not re.search(r'(?<!\\)&',m.group()),page+' raw matrix ampersand')
 require(not re.search(r'\\diagram\s*\{\s*(?:\\\[|\$)?\s*\\begin\{(?:tikzpicture|array)\}',clean(text)),page+' unconverted diagram body')
 cote=page.split('_')[0]
 if cote!=last:comb.append('\\cotefile{'+cote+'}\n');last=cote
 comb.append(text.rstrip()+'\n')
require('\n'.join(comb)==(W/f'{P}_transcription.tex').read_text(),'Combined fragment differs from ordered page sources')
allc=[c for r in rs for c in r['changes']];marks=[d for r in rs for d in r['decisions']]
require(len(rs)==25 and sum_a['boxes']==560 and len(marks)==195,'Required page/box/mark totals differ')
require(sum_a['differing_boxes']==472 and sum_a['changed_boxes']==194,'Final audit totals differ')
require(len(allc)==953 and sum(c['against_c'] for c in allc)==502 and sum(c['against_h'] for c in allc)==826,'Final witness totals differ')
require(len(list((W/'crops').glob('*.png')))==1110,'Crop inventory changed')
require(len(originaldiff)==1063,'Supplied differences parser count changed')
# Technical source hashes form a chain from audited source to final formatting.
fmt=json.loads((W/'reports/tex_integration_receipt.json').read_text());enc=json.loads((W/'reports/math_illegible_encoding_receipt.json').read_text())
expect={x['path']:x['after_sha256'] for x in fmt['files']}
for f in enc['files']:
 if f['path'].startswith('work/pages/'):
  require(expect.get(f['path'],f['before_sha256'])==f['before_sha256'],'Formatting/encoding hash chain broken '+f['path']);expect[f['path']]=f['after_sha256']
for p,h in expect.items():require(sha(ROOT/p)==h,'Final source differs from integration receipt '+p)
for p,h in enc['immutable_file_sha256'].items():require(sha(ROOT/p)==h,'Encoding altered historical record '+p)
for p in [W/'README.md',*(W/'reports'/n for n in ['legibility.txt','feedback_extra.md','notation_comparison.md','audit_box_scope_check.md'])]:
 require('{{' not in p.read_text(),'Unfilled documentation placeholder '+str(p))
require(not re.search(r'\\unsure\{\\overline j\|\\illegible\{1\}\}',(W/'pages/150_scan005.tex').read_text()),'Forbidden mathematical illegible alternative remains')
macro={'phase':'all25 audits and final source formatting complete','commands':dict(sorted(commands.items())),'review':'Commands are supplied editorial helpers, LaTeX/AMS, TikZ/tikz-cd, or local foreach variables. This inventory is source-only; no compilation or rendering.'}
(W/'reports/macro_inventory.json').write_text(json.dumps(macro,ensure_ascii=False,indent=2)+'\n')
summary={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':25,'audit_counts':dict(sum_a),'original_marks':len(marks),'inventory_elements':sum(len(r['inventory']) for r in rs),'changes':len(allc),'against_c':502,'against_h':826,'mathematical_check_events':sum(len(r['check_events']) for r in rs),'visual_events_retained_separately':sum(len(r.get('visual_audit_events',[])) for r in rs),'source_comparison_events_retained_separately':sum(len(r.get('source_comparison_events',[])) for r in rs),'supplied_difference_rows_covered':len(originaldiff),'crops':1110,'fixed_input_hashes':fixed,'source_sha256':{str(f.relative_to(W)):sha(f) for f in [*(W/'pages'/f'{p}.tex' for p in order),W/f'{P}_transcription.tex']},'errors':errors,'limitations':'Structural/source checks only. Pixel-equivalence and final archive entry/CRC checks have separate packaging receipts. No OCR, external textual research, TeX compilation or rendered-layout check.'}
(W/'reports/final_verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['fixed_input_hashes','source_sha256']},ensure_ascii=False));sys.exit(bool(errors))
