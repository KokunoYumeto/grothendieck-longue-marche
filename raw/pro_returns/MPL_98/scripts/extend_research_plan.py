"""Append genuinely performed note-specific context searches after new findings."""
from pathlib import Path
import datetime, json, subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / 'context'
plan_path = ROOT / 'research/note_plan.json'
plan = json.loads(plan_path.read_text())
new = [
 ('MPL98.N15','013–014','The explicit request to relate the examples','Expliquer|galoisiennes|galoisien|cas général|pages 12'),
 ('MPL98.G12','024','Cohomology action is not only component permutation','pi_0|composantes|système local|H.q.Y'),
 ('MPL98.B31','027','Generic length one does not give a global embedding','longueur|Chow général|Chow raffiné|mathcal.O._.Z|cas.*l'),
 ('MPL98.R09','039–040','Input flatness is present in the frozen lemma','omis|manque|plats|platitude|F_.*alpha'),
 ('MPL98.T11','019,021','Additional literal typescript formula anomalies','imprimées|retapées|dactylo|page 18|coefficient'),
]
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
existing = {n['id'] for n in plan}
for ident,scans,title,query in new:
 if ident in existing: continue
 r = subprocess.run(['rg','-n','--no-heading',query,str(CONTEXT)],capture_output=True,text=True)
 if r.returncode not in (0,1): raise RuntimeError(r.stderr)
 matches=[]
 for line in r.stdout.splitlines():
  path,number,_ = line.split(':',2)
  matches.append({'file':str(Path(path).relative_to(CONTEXT)),'line':int(number)})
 item={'id':ident,'scans':scans,'title':title,'query':query,'searched_utc':now,'exit_status':r.returncode,'matches':matches}
 plan.append(item)
 with (ROOT/'research/context_searches.jsonl').open('a') as f: f.write(json.dumps(item,ensure_ascii=False)+'\n')
for n in plan:
 if n['id']=='MPL98.B19': n['title']='Input flatness is necessary and is present in the lemma'
 if n['id']=='MPL98.B02': n['title']='Fixed quotient and cycle degree do not bound even pure sheaves'
plan_path.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(f'{len(plan)} note-specific context searches recorded')
