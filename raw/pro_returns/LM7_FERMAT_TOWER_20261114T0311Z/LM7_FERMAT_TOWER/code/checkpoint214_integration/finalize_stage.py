"""Finalize214 staging and preserve the complete prior209 rendered review."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys
B=Path(__file__).resolve().parents[2];R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for ext in ['.py','.out']:
 p=R/('root_integrate214'+ext);q=Path(__file__).resolve().parent/p.name
 shutil.copy2(p,q)
q=B/'qa';assert sha(B/'LM7_FERMAT_TOWER_paper.pdf')=='0197634cad8fd1609f08450038762904db6f219357cfefa9fdafc0a28bfb1c29'
h=q/'history/checkpoint209_before214';assert not h.exists();h.mkdir(parents=True)
files=list(q.glob('contact_*.jpg'))+list(q.glob('detail209*.jpg'))
files+=[q/n for n in ['pdf_qa.json','visual_review.md','visual209_a.json','visual209_d.json','visual209_root.json','detail209_manifest.json']]
assert len(list(q.glob('contact_*.jpg')))==39 and len(list(q.glob('detail209*.jpg')))==25
rows=[]
for p in files:
 if p.exists():
  shutil.copy2(p,h/p.name);rows.append(dict(file=p.name,bytes=p.stat().st_size,sha256=sha(p)))
(h/'archive_manifest.json').write_text(json.dumps(dict(checkpoint=209,pdf_sha256='0197634cad8fd1609f08450038762904db6f219357cfefa9fdafc0a28bfb1c29',files=rows),indent=2)+'\n')
p=B/'ledger/d_stabilizer_projective_lift_results.json';d=json.loads(p.read_text());old=d[0]['where_proved']
d[0]['where_proved']=old.replace('audit/d60_author_rebuild/','code/d60_bundle/audit/d60_author_rebuild/')
assert d[0]['where_proved']!=old
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
with (B/'code/assemble.out').open('wb') as out:run=subprocess.run([sys.executable,str(B/'code/assemble.py')],stdout=out,stderr=subprocess.STDOUT)
assert run.returncode==0
summary=json.loads((B/'code/assemble.out').read_text())
assert summary['statements']==214 and summary['tasks']==33 and summary['all_identity_and_coverage_checks']
record=dict(status='PASS',prior_qa_files_preserved=len(rows),metadata_path_amendment=dict(before=old,after=d[0]['where_proved']),assembly=summary)
(B/'ledger/checkpoint214_stage_finalize.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(record,indent=2,ensure_ascii=False))

