from audit_work import *
n=3;p=OUT/'pages'/Path(mapping(n)['codex_file']).name;s=p.read_text();s=s.replace(r'\unsure{=|\Rightarrow}',r'\unsure{\Rightarrow|=}');p.write_text(s)
q=OUT/'records/scan003.json';r=json.loads(q.read_text());d=r['changes'][1];d['final']='2°) unsure implication|equal 3°)';d['c_changed']=True;d['evidence']+=' Second audit 003_audit_transition.jpg at 4×: joined pointed right end favors implication; equal sign remains alternative.'
for d in r['doubts']:
 if d['place']=='2⇒3':d['reading']='⇒';d['alternatives']='='
r['doubt_decisions'].append('Second audit reversed the first reading of the 2⇒3 connector to implication after examining the joined pointed end; uncertainty remains.')
q.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');regenerate()
audit(3,'Full-page rereading completed including proof cancellations and interline eta. Re-enlarged transition: implication now first, equal retained as alternative. Other live/old states unchanged.')
