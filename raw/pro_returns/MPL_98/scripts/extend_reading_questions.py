from pathlib import Path
import json, subprocess, datetime
root=Path('MPL_98_work'); ctx=Path('context').resolve()
p=root/'research/note_plan.json'; plan=json.loads(p.read_text())
new=[
('MPL98.R10','031','Corollary 3 versus the modernized Corollary 5','Corollaire 5|Un corps universel|transcendance infini'),
('MPL98.R11','016','The second argument of the sheaf Hom formula','Hom_G|E pour A|Les G-ensembles'),
('MPL98.R12','043','A-flat versus A-free in the Hom complex','A-libres|A-plats|termes'),
('MPL98.T12','021','Function versus divisor in the typed equality','imprimées|retapées|page 20|dactylo'),
('MPL98.R13','028','The conclusion about extensions is already in the frozen text','inverse|noyaux|extensions|ligne.*e'),
]
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ids={n['id'] for n in plan}
for ident,scans,title,query in new:
 if ident in ids: continue
 r=subprocess.run(['rg','-n','--no-heading',query,str(ctx)],capture_output=True,text=True)
 if r.returncode not in [0,1]: raise RuntimeError(r.stderr)
 matches=[]
 for line in r.stdout.splitlines():
  f,num,_=line.split(':',2)
  matches.append({'file':str(Path(f).relative_to(ctx)),'line':int(num)})
 item={'id':ident,'scans':scans,'title':title,'query':query,'searched_utc':now,'exit_status':r.returncode,'matches':matches}
 plan.append(item)
 with (root/'research/context_searches.jsonl').open('a') as out: out.write(json.dumps(item,ensure_ascii=False)+'\n')
for n in plan:
 if n['id']=='MPL98.R04': n.update(scans='030',title='Composed or common extension versus universal extension')
 if n['id']=='MPL98.R05': n.update(scans='014',title='The unfinished final contracted-product assertion')
 if n['id']=='MPL98.R07': n.update(scans='039,041–043',title='Coefficient rings in the base-change formulas')
 if n['id']=='MPL98.T11': n.update(scans='019',title='The omitted index-zero term in the typescript expansion')
p.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(len(plan))

