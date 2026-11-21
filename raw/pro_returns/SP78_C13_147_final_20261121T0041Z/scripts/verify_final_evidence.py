"""Verify preserved readings and complete root decision coverage; no new ink reading."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,re
w=Path(__file__).resolve().parents[1]
start=json.loads((w/'workflow/blind_audit_start.json').read_text())
views=json.loads((w/'workflow/root_audit_views.json').read_text())
state=json.loads((w/'run_state.json').read_text());rows=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def tokens(s):return re.findall(r'\\[A-Za-z]+|\\.|[\wÀ-ÿ]+|[^\s]',s)
def utc(s):
 if s.endswith(' UTC'):return datetime.strptime(s,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
 return datetime.fromisoformat(s.replace('Z','+00:00'))
for x in start['pages']:
 n=x['scan'];p=f'147_scan{n:03}';base=w/'second'
 assert sha(base/f'{p}_first.tsv')==x['first_sha256'],p
 assert sha(base/f'{p}_boxes.tsv')==x['boxes_sha256'],p
 meta=json.loads((base/f'{p}_comparison_metadata.json').read_text())
 for which in ['first','second']:assert sha(base/f'{p}_{which}.tsv')==meta['files'][which]['sha256'],(p,which)
 first=read(base/f'{p}_first.tsv');second=read(base/f'{p}_second.tsv');boxes=read(base/f'{p}_boxes.tsv')
 assert [r['box'] for r in first]==[r['box'] for r in second]==[r['box'] for r in boxes]
 assert len(first)==x['boxes']
 differences=[a['box'] for a,b in zip(first,second) if tokens(a['reading'])!=tokens(b['reading'])]
 a=json.loads((base/f'{p}_adjudications.json').read_text());comp=json.loads((base/f'{p}_comparison.json').read_text())
 assert differences==[r['box'] for r in a]==[r['box'] for r in comp]
 for r,c in zip(a,comp):
  assert r['root_viewed'] and r['evidence'] and r['first']==c['first'] and r['second']==c['second']
  assert r['changed']==(r['final']!=r['first'])
  assert (w/'crops'/r['crop']).is_file()
 assert set(differences)<=set(views[str(n)]['observations'])
 report=json.loads((w/'reviewed'/f'{p}.json').read_text())
 assert report['audit_complete'] and report['root_review_complete']
 assert report['audit_changes']==[r for r in a if r['changed']]
 auditor=json.loads((w/'audit_returns'/f'{p}.json').read_text())
 assert set(auditor['boxes_read'])=={r['box'] for r in boxes}
 assert meta['second_reader_completed_utc']==auditor['completed_utc']
 assert utc(meta['second_reader_completed_utc'])<=utc(meta['compared_utc'])
 assert state['first_assignments'][str(n)]!=state['audit_assignments'][str(n)]
 rows.append({'scan':n,'boxes':len(boxes),'differing_boxes':len(a),'changed_boxes':sum(r['changed'] for r in a),'first_and_boxes_match_start_manifest':True,'both_readings_match_comparison_hashes':True,'root_coverage_complete':True})
assert [r['scan'] for r in rows]==state['scope']
result={'recorded_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'scope':'Deterministic evidence integrity; no new source reading, mathematical proof, OCR, compilation or rendering.','pages':rows,'totals':{k:sum(r[k] for r in rows) for k in ['boxes','differing_boxes','changed_boxes']},'issues':[]}
(w/'workflow/final_evidence_integrity.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':len(rows),**result['totals'],'issues':[]}))
