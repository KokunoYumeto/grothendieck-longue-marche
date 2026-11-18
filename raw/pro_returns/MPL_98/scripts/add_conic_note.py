from pathlib import Path
import json,subprocess,datetime
root=Path('MPL_98_work'); ctx=Path('context').resolve(); p=root/'research/note_plan.json'; plan=json.loads(p.read_text())
ident='MPL98.G13'
if not any(n['id']==ident for n in plan):
 query='Pic|Brauer|G_m|d_2|page 21'
 r=subprocess.run(['rg','-n','--no-heading',query,str(ctx)],capture_output=True,text=True)
 if r.returncode not in (0,1): raise RuntimeError(r.stderr)
 matches=[]
 for line in r.stdout.splitlines():
  f,num,_=line.split(':',2); matches.append({'file':str(Path(f).relative_to(ctx)),'line':int(num)})
 n={'id':ident,'scans':'022','title':'The real conic tests an unrestricted fixed-cover injection','query':query,'searched_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'exit_status':r.returncode,'matches':matches}
 plan.append(n)
 with (root/'research/context_searches.jsonl').open('a') as f:f.write(json.dumps(n,ensure_ascii=False)+'\n')
for n in plan:
 if n['id']=='MPL98.G08':n['title']='The conditional Picard–Brauer edge sequence and the field setting'
p.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(len(plan))

