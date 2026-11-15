"""Log reproducible searches of supplied textual context for a research note."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,re,subprocess
ROOT=Path(__file__).resolve().parents[1];CONTEXT=ROOT.parent/'context_sources'
a=argparse.ArgumentParser();a.add_argument('--id',required=True);a.add_argument('--pattern',required=True);a.add_argument('--limit',type=int,default=20);args=a.parse_args()
files=sorted([*CONTEXT.glob('*.tex'),*CONTEXT.glob('*.md'),*CONTEXT.glob('notes/*.md')])
hits=[];counts={}
for p in files:
 lines=p.read_text().splitlines();locs=[];cote=None;scan=None;section=''
 for line in lines:
  m=re.search(r'\\cotefile\{(\d+)\}',line)
  if m:cote=int(m.group(1))
  m=re.search(r'\\scanpage\{(\d+)\}',line)
  if m:scan=int(m.group(1))
  if line.startswith('#'):section=line
  locs.append({'cote':cote,'scan':scan} if p.suffix=='.tex' else {'section':section})
 proc=subprocess.run(['rg','-n','-i','--',args.pattern,str(p)],capture_output=True,text=True)
 assert proc.returncode in (0,1),proc.stderr
 fh=[]
 for line in proc.stdout.splitlines():
  num,body=line.split(':',1);ln=int(num);fh.append({'file':str(p.relative_to(CONTEXT)),'line':ln,**locs[ln-1],'text':body})
 counts[str(p.relative_to(CONTEXT))]=len(fh);hits.extend(fh)
record={'note_id':args.id,'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'pattern':args.pattern,'source_root':'context_sources','counts':counts,'hits':hits,'source_status':'Prior transcription and notes are first-pass leads; RESULTS_STATE statuses remain as stated.'}
with (ROOT/'records/context_searches.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
print(json.dumps({'note_id':args.id,'pattern':args.pattern,'counts':counts,'shown_hits':hits[:args.limit],'total_hits':len(hits)},ensure_ascii=False,indent=2))
