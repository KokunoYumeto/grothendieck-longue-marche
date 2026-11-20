"""Prepare non-leading image-only boxes and compare independent transcriptions by tokens."""
from pathlib import Path
import csv, json, re, difflib, sys, shutil, hashlib
from datetime import datetime, timezone
E=Path(__file__).resolve().parents[1];ROOT=E.parent

def read_tsv(p):
 with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def write_tsv(p,fields,rows):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
def blind_kind(s):
 s=s.lower();out=[]
 for key,label in [('insert','insertion'),('margin','margin note'),('delet','deletion'),('struck','deletion'),('cancel','deletion'),('formula','formula'),('display','formula'),('numeric','handwritten number'),('number','handwritten number'),('numeral','handwritten number'),('header','header'),('word','text'),('lexical','text'),('prose','text'),('punctuation','text')]:
  if key in s and label not in out:out.append(label)
 return '; '.join(out) or 'manuscript text or notation'
def tokens(s):
 return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]',s)
mode=sys.argv[1]
if mode=='sanitize':
 for p in sorted((E/'second').glob('*_boxes.tsv')):
  if p.with_name(p.name.replace('_boxes','_second')).exists():raise SystemExit('Do not alter an already read box list')
  rows=read_tsv(p)
  for r in rows:r['kind']=blind_kind(r['kind'])
  write_tsv(p,['box','kind','x0','y0','x1','y1'],rows)
 print('All current box descriptions reduced to structural categories, without candidate readings.')
elif mode=='prepare':
 expected=[3]+list(range(5,28))
 completed={json.loads(p.read_text())['scan'] for p in (E/'reader_reports').glob('*_reviewed.json')}
 assert completed==set(expected),'All 24 first-pass pages must be finalized before blind reading'
 assert all((E/'pages'/f'145_scan{n:03d}.tex').is_file() for n in expected)
 scan=int(sys.argv[2]);reader=sys.argv[3];stem=f'145_scan{scan:03d}'
 first_report=json.loads((E/'reader_reports'/(stem+'_reviewed.json')).read_text())
 assert reader.split('/')[-1]!=first_report['reader'].split('/')[-1],'Second reader has read the page before'
 assert not (reader.split('/')[-1]=='reader_b' and scan in [25,26,27]),'Excluded by documented accidental difference-list exposure'
 dest=ROOT/'audit_packets'/stem;dest.mkdir(parents=True,exist_ok=True)
 src=E/'second'/(stem+'_boxes.tsv');rows=read_tsv(src)
 for r in rows:r['kind']=blind_kind(r['kind'])
 write_tsv(src,['box','kind','x0','y0','x1','y1'],rows)
 shutil.copyfile(src,dest/'boxes.tsv');shutil.copyfile(ROOT/'source/SP75_C13_145_scans'/(stem+'.jpg'),dest/'page.jpg')
 (E/'second'/(stem+'_audit_assignment.json')).write_text(json.dumps({'reader':reader,'assigned_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'supplied_evidence':['page.jpg','boxes.tsv'],'first_reader':first_report['reader'],'exposure_exclusions_checked':True},indent=2))
 print(dest)
elif mode=='compare':
 scan=int(sys.argv[2]);stem=f'145_scan{scan:03d}';d=E/'second'
 sealed={x['file']:x['sha256'] for x in read_tsv(d/'FIRST_READINGS_SHA256.tsv')}
 first_hash=hashlib.sha256((d/(stem+'_first.tsv')).read_bytes()).hexdigest()
 second_hash=hashlib.sha256((d/(stem+'_second.tsv')).read_bytes()).hexdigest()
 assert first_hash==sealed[stem+'_first.tsv'],'Pre-comparison reading changed after sealing'
 receipt=d/(stem+'_reading_receipt.json')
 if receipt.exists():
  old=json.loads(receipt.read_text())
  assert old['first_sha256']==first_hash and old['second_sha256']==second_hash,'Submitted reading changed'
 else:
  receipt.write_text(json.dumps({'first_sha256':first_hash,'second_sha256':second_hash,'boxes_sha256':hashlib.sha256((d/(stem+'_boxes.tsv')).read_bytes()).hexdigest(),'comparison_started_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'method':'Exact LaTeX-command, word, number and non-space-character token comparison; both readings existed before this receipt and comparison.'},indent=2))
 boxes=read_tsv(d/(stem+'_boxes.tsv'));first=read_tsv(d/(stem+'_first.tsv'));second=read_tsv(d/(stem+'_second.tsv'))
 ids=[r['box'] for r in boxes]
 assert [r['box'] for r in first]==ids, 'first-reading box order mismatch'
 assert [r['box'] for r in second]==ids, 'second-reading box order mismatch'
 rows=[];details=[]
 for b,a,z in zip(boxes,first,second):
  x=tokens(a['reading']);y=tokens(z['reading']);ops=[(tag,i,j,k,l) for tag,i,j,k,l in difflib.SequenceMatcher(a=x,b=y,autojunk=False).get_opcodes() if tag!='equal']
  if ops:
   rows.append({'box':b['box'],'kind':b['kind'],'first':a['reading'],'second':z['reading'],'differing_token_spans':len(ops),'adjudication':'PENDING','final':'','ink':''})
   details.append({'box':b['box'],'first_tokens':x,'second_tokens':y,'differences':[{'operation':tag,'first_range':[i,j],'second_range':[k,l],'first':x[i:j],'second':y[k:l]} for tag,i,j,k,l in ops]})
 write_tsv(d/(stem+'_comparison.tsv'),['box','kind','first','second','differing_token_spans','adjudication','final','ink'],rows)
 (d/(stem+'_token_differences.json')).write_text(json.dumps(details,ensure_ascii=False,indent=2))
 print(json.dumps({'scan':scan,'boxes':len(boxes),'boxes_with_differences':len(rows),'token_difference_spans':sum(r['differing_token_spans'] for r in rows)}))
else:raise SystemExit(mode)
