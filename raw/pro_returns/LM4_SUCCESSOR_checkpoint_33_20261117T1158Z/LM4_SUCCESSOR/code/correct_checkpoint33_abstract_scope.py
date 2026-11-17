"""Preserve first33 build artifacts before the accepted abstract-only scope correction."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
root=Path(__file__).resolve().parents[1]
backup=root/'records/pdf_qa/checkpoint33_abstract_firstpass'
assert not backup.exists();backup.mkdir(parents=True)
paths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
paths+=['records/checkpoint33_metrics.json','records/checkpoint33_build_audit.json','code/audit_checkpoint33_build.py']
for stem in ['build','metrics','render','build_audit','size_estimate']:
    paths += ['records/checkpoint33_'+stem+'_run.'+e for e in ('out','err')]
for path in (root/'records').glob('build_*.log'):paths.append(str(path.relative_to(root)))
for rel in paths:
    src=root/rel
    if src.is_file():
        suffix='.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
        dst=backup/(rel+suffix);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
paper=root/'LM4_SUCCESSOR_paper.tex'
before=paper.read_text()
old='A uniform affine sphere-pentagon calculation over every finite ring\nproves that the original hexagon word vanishes in the entire signed'
new='For actual full-GT data, a uniform affine sphere-pentagon calculation\nover every residue ring $\\mathbb Z/m\\mathbb Z$ proves that the original\nhexagon word vanishes in the entire signed'
assert before.count(old)==1
paper.write_text(before.replace(old,new))
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),reason='Independent CE scope review: explicit full-GT hypothesis and exact residue rings in the abstract.',
    old=old,new=new,before_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(paper.read_bytes()).hexdigest(),
    mathematical_section_sources_changed=False,
    stopped_estimator=dict(session_id=88588,actual_exit_code=130,tool_chunk='216a87',reason='Its PDF binding would become stale after the abstract correction; no ZIP created.'),
    first_build=dict(session_id=58868,actual_exit_code=0),first_render=dict(session_id=82555,actual_exit_code=0),
    first_pdf_sha256='f4eaebbf1ecadb549772cefcade0a2e4aea7f1b9cb0c6c4c44bbf2c88614c002',
    first_visual_scope='Actual first-pass individual observations retained separately. They may transfer only if freshly rendered final PNG bytes are identical.')
(root/'records/checkpoint33_abstract_scope_correction.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
