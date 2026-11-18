from pathlib import Path
import json, subprocess, datetime
root=Path('MPL_98_work'); ctx=Path('context').resolve()
p=root/'research/note_plan.json'; plan=json.loads(p.read_text())
ident='MPL98.B32'
if not any(x['id']==ident for x in plan):
 query='conditions.*isomorphisme|homomorphisme canonique|changement de base|pages 37'
 r=subprocess.run(['rg','-n','--no-heading',query,str(ctx)],capture_output=True,text=True)
 if r.returncode not in (0,1): raise RuntimeError(r.stderr)
 matches=[]
 for line in r.stdout.splitlines():
  f,num,_=line.split(':',2); matches.append({'file':str(Path(f).relative_to(ctx)),'line':int(num)})
 n={'id':ident,'scans':'038–040','title':'The explicit question about when Tor base change is an isomorphism','query':query,'searched_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'exit_status':r.returncode,'matches':matches}
 plan.append(n)
 p.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
 with (root/'research/context_searches.jsonl').open('a') as f:f.write(json.dumps(n,ensure_ascii=False)+'\n')
print(len(plan))

