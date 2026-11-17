"""Preserve the failed first edition and apply two local line-break fixes."""
from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re, shutil

root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
backup=root/'records/pdf_qa/checkpoint35_first_layout'
assert not backup.exists()
specs=[
 ('A.112','work_DE/A112_actual_central_product_odd_cohomology_proposed.tex','sections/a_actual_central_product_odd_cohomology.tex',
  'aac45807a4751e1299b7980225d0ef4bdcf4729acc842d19a202fa1636b9f310',
  r''' N=\ker q,\quad N_1=\overline{[N,F]},\quad
 P=F^{(2)},\quad M_2=\ker(P\to\mathcal C_{(2)}),\quad
 M_{21}=\overline{[M_2,P]},\quad P_*=P/M_{21},''',
  r''' \begin{gathered}
 N=\ker q,\quad N_1=\overline{[N,F]},\quad P=F^{(2)},\\
 M_2=\ker(P\to\mathcal C_{(2)}),\quad
 M_{21}=\overline{[M_2,P]},\quad P_*=P/M_{21}.
 \end{gathered}'''),
 ('A.114','work_A/A114_next_modular_central_refinement_proposed.tex','sections/a_next_modular_central_refinement.tex',
  '28cf2329db608a2394dcdf84a588fd3d6d64fe716f2886b133e4a2246df48f22',
  'Equations (A.114.8),(A.114.13) imply','Equations (A.114.8) and (A.114.13) imply'),
]
overfull=re.findall(r'^.*Overfull.*$',(root/'LM4_SUCCESSOR_paper.log').read_text(),re.M)
assert len(overfull)==2 and '8.56215pt' in overfull[0] and '11.13672pt' in overfull[1]
assert sha(root/'LM4_SUCCESSOR_paper.pdf')=='16638a833567b0126358c233ce6e4cda41398ce23eea3527b7f0f4de4c90a4b7'
paths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
paths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','records/checkpoint35_build_driver.out',
        'records/checkpoint35_build_driver.err','records/checkpoint35_independent_review_manifest.json',
        'records/checkpoint35_root_formal_reviews.json','records/checkpoint35_formal_source_copies.json']
paths+=[str(p.relative_to(root)) for p in (root/'records').glob('build_*.log')]
paths+=[p for _,s,t,_,_,_ in specs for p in (s,t)]
for rel in paths:
    path=root/rel
    if path.is_file():
        suffix='.retained.txt' if path.suffix in {'.aux','.bbl','.blg','.toc'} else ''
        saved=backup/(rel+suffix);saved.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,saved)
changes=[]
for sid,source,target,before,old,new in specs:
    path=root/source
    assert sha(path)==sha(root/target)==before
    s=path.read_text();assert s.count(old)==1
    out=s.replace(old,new);path.write_text(out);(root/target).write_text(out)
    diff=''.join(difflib.unified_diff(s.splitlines(True),out.splitlines(True),fromfile=str((backup/source).relative_to(root)),tofile=source))
    dp='records/checkpoint35_'+sid.replace('.','')+'_layout.diff';(root/dp).write_text(diff)
    changes.append(dict(statement=sid,source=source,target=target,before_sha256=before,after_sha256=sha(path),diff=dp,diff_sha256=sha(root/dp)))
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),changes=changes,
 first_build_observed=dict(tool='write_stdin',session_id=76561,initial_chunk='7abbe4',exit_chunk='a661f2',exit_code=1,
   final_pdf_sha256='16638a833567b0126358c233ce6e4cda41398ce23eea3527b7f0f4de4c90a4b7',pages=671,
   bytes=4496930,overfull_notices=overfull,driver_stdout='records/checkpoint35_build_driver.out',driver_stderr='records/checkpoint35_build_driver.err',
   preserved_under=str(backup.relative_to(root))),
 scope='Only opening-definition line arrangement/punctuation and a breakable conjunction between identical equation references change. Complete mathematical content and order remain. Final source review binding is pending the independent exact-diff read.')
with (root/'records/checkpoint35_layout_correction.json').open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
