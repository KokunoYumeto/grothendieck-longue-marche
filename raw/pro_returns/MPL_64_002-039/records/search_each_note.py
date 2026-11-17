from pathlib import Path
from collections import Counter,defaultdict
import subprocess,json,re,datetime
root=Path(__file__).resolve().parents[1]
ctx=root.parent/'context'
files=['root_note_items.json','question_note_items.json','apparatus_note_items.json']
notes=[x for f in files for x in json.loads((root/'records'/f).read_text())]
records=[]
for note in notes:
 pattern=note['query']
 cmd=['rg','-n','-i','--no-heading','--color=never','--',pattern,str(ctx)]
 p=subprocess.run(cmd,text=True,capture_output=True)
 attempts=[{'argv':cmd,'exit_code':p.returncode,'stderr':p.stderr.strip()}]
 if p.returncode==2:
  pattern=pattern.replace('{',r'\{').replace('}',r'\}')
  cmd=['rg','-n','-i','--no-heading','--color=never','--',pattern,str(ctx)]
  p=subprocess.run(cmd,text=True,capture_output=True)
  attempts.append({'argv':cmd,'exit_code':p.returncode,'stderr':p.stderr.strip()})
 if p.returncode not in (0,1):
  raise RuntimeError((note['id'],p.stderr))
 counts=Counter(); excerpts=defaultdict(list)
 for line in p.stdout.splitlines():
  if not line.strip():
   continue
  path,ln,hit=line.split(':',2)
  path=str(Path(path).relative_to(ctx))
  counts[path]+=1
  if len(excerpts[path])<3:
   excerpts[path].append({'line':int(ln),'excerpt':hit[:260],'excerpt_truncated':len(hit)>260})
 records.append({'note_id':note['id'],'query':note['query'],'actual_pattern':pattern,'attempts':attempts,'matched_lines':sum(counts.values()),'file_counts':dict(sorted(counts.items())),'sample_hits_by_file':dict(sorted(excerpts.items())),'comparison_cited_in_note':note['context'],'scope':'Search hits are navigation evidence, not proof verification; excerpts are limited to three per file,260 characters each'})
out={'run':'MPL_64_002-039','search_time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'context_opened_only_after_freeze':True,'note_count':len(notes),'records':records}
(root/'records/root_context_searches.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
zero=[x['note_id'] for x in records if x['matched_lines']==0]
retries=[x['note_id'] for x in records if len(x['attempts'])>1]
print(json.dumps({'notes_searched':len(notes),'zero_hit_queries':zero,'regex_literal_brace_retries':retries,'log_bytes':(root/'records/root_context_searches.json').stat().st_size},ensure_ascii=False))
