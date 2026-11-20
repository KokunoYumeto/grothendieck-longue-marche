"""Audit delivered records and freeze/verify the fully adjudicated transcription.
This performs structural checks only; it is not OCR or mathematical certification.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,hashlib,json,re
O=Path(__file__).resolve().parents[1];R=O.parent;PREFIX='SP43_CW_29+32'
p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');p.add_argument('--verify',action='store_true');a=p.parse_args()
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
if a.verify:
 rows=list(csv.DictReader((O/'FREEZE_SHA256.tsv').open(),delimiter='\t'))
 bad=[x['file'] for x in rows if digest(O/x['file'])!=x['sha256']]
 if bad:raise RuntimeError('Frozen files changed: '+str(bad))
 with (O/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+now()+'; '+str(len(rows))+' files verified\n')
 print(json.dumps({'hashes_unchanged':True,'files':len(rows)}));raise SystemExit
mapping=json.loads((R/'work/page_map.json').read_text());expected=[Path(x['codex_file']).name for x in mapping]
pages=sorted([json.loads(x.read_text()) for x in (O/'decisions').glob('*.json')],key=lambda x:x['order'])
errors=[];warnings=[];agents=[]
if [x['filename'] for x in pages]!=expected:errors.append('Page decisions do not cover all 28 pages in archive order.')
if sorted(x.name for x in (O/'pages').glob('*.tex'))!=sorted(expected):errors.append('Page file set differs from source mapping.')
for d in pages:
 stem=d['stem'];tex=(O/'pages'/d['filename']).read_text()
 # Remove unescaped comments and escaped braces; count actual structural delimiters.
 clean=re.sub(r'(?<!\\)%[^\n]*','',tex)
 depth=0
 for j,c in enumerate(clean):
  if c not in '{}':continue
  slashes=0;k=j-1
  while k>=0 and clean[k]=='\\':slashes+=1;k-=1
  if slashes%2:continue
  depth+=1 if c=='{' else -1
  if depth<0:errors.append(stem+': unmatched closing brace');break
 if depth:errors.append(stem+': unbalanced brace count '+str(depth))
 if re.search(r'\\(?:newcommand|renewcommand|def|usepackage|documentclass)\b',tex):errors.append(stem+': fragment defines new commands/packages')
 begins=re.findall(r'\\begin\{([^}]+)\}',clean);ends=re.findall(r'\\end\{([^}]+)\}',clean)
 if sorted(begins)!=sorted(ends):errors.append(stem+': environment mismatch')
 if any(x.get('transcribed')!='yes' for x in d['inventory']):errors.append(stem+': incomplete inventory item')
 for u in d.get('unresolved',[]):
  if not u.get('reading'):errors.append(stem+': unresolved item missing reading at '+u.get('place',''))
 for rid in ['r1','r2','r3']:
  agent=d.get('agents',{}).get(rid);agents.append(agent)
  q=O/'readers'/stem/rid/'report.json';t=q.with_name('reading.tex')
  if not q.exists() or not t.exists():errors.append(stem+': missing '+rid+' return');continue
  rr=json.loads(q.read_text())
  if not rr.get('finished_utc'):errors.append(stem+': no finish time '+rid)
  for c in rr.get('crops',[]):
   name=c.get('path',c.get('file',''))
   if not name:warnings.append(stem+'/'+rid+': crop path field varies');continue
   path=Path(name)
   if not path.is_absolute():path=q.parent/path
   if not path.exists():warnings.append(stem+'/'+rid+': inspect relative crop path '+name)
 for d2 in d['differences']:
  if len(d2.get('readers',{}))!=3:errors.append(stem+': missing three reader fields '+d2.get('id',''))
  src=d2.get('source','')
  if src.startswith(('crops/','readers/')) and not (O/src).is_file():errors.append(stem+': missing adjudication evidence '+src)
 if d['our_scan'] in ['134','136'] and d['scan'].startswith('29/') and any(x.get('diff_H') for x in d['differences']):errors.append(stem+': H rows on absent-H page')
if len(agents)!=len(set(agents)) or None in agents:errors.append('Reader agents not fresh and unique for every page.')
combined='\n\n'.join((O/'pages'/d['filename']).read_text().rstrip() for d in pages)+'\n'
if (O/(PREFIX+'_transcription.tex')).read_text()!=combined:errors.append('Combined transcription differs from page concatenation.')
rows=list(csv.DictReader((O/(PREFIX+'_collation.tsv')).open(),delimiter='\t'))
if len(rows)!=sum(x.get('diff_H',False) for d in pages for x in d['differences']):errors.append('Collation count mismatch')
for x in rows:
 if x['marked_in_H'] not in ['yes','no']:errors.append('Invalid H doubt marker')
checks=list(csv.DictReader((O/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
for x in checks:
 if not all(x.get(k) for k in ['statement_id','date','who','type','outcome']):errors.append('Incomplete check event '+x.get('statement_id',''))
report={'UTC':now(),'pages':len(pages),'independent_reader_runs':len(agents),'H_collation_rows':len(rows),'check_events':len(checks),'errors':errors,'warnings':warnings,'scope':'Structural record and LaTeX-fragment checks; no compilation, OCR, or further mathematical certification.'}
(O/'FINAL_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
if errors:raise SystemExit(1)
if a.freeze:
 if (O/'FREEZE_SHA256.tsv').exists():raise RuntimeError('Transcription already frozen')
 paths=[O/'pages'/x for x in expected]+[O/(PREFIX+'_transcription.tex')]
 rows=[{'file':str(x.relative_to(O)),'sha256':digest(x)} for x in paths]
 with (O/'FREEZE_SHA256.tsv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['file','sha256'],delimiter='\t');w.writeheader();w.writerows(rows)
 with (O/'progress.log').open('a') as f:
  for x in rows:f.write('sha256 '+x['sha256']+' '+x['file']+'\n')
  f.write('transcription frozen '+now()+'\n')
 print('Frozen',len(rows),'transcription files')
