"""Preserve the complete c5be edition before a literal missing-factor repair."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT/'records/checkpoint37_before_A127_Bu_correction'
DEST.mkdir(exist_ok=False)
names = ['LM4_SUCCESSOR_paper'+ext for ext in ('.tex','.pdf','.log','.aux','.toc','.out','.bbl','.blg')]
names += ['records/checkpoint37_build_driver.out','records/checkpoint37_build_driver.err',
          'sections/a_elliptic_brunnian_cyclic_involution.tex',
          'work_DE/A127_elliptic_brunnian_cyclic_involution_proposed.tex',
          'records/checkpoint37_formal_source_copies.json',
          'records/checkpoint37_root_formal_reviews.json',
          'records/checkpoint37_independent_review_manifest.json',
          'records/checkpoint37_metrics.json','records/checkpoint37_metrics_run.out',
          'records/checkpoint37_metrics_run.err',
          'records/checkpoint37_render_run.out','records/checkpoint37_render_run.err',
          'records/checkpoint37_final_pdf_audit.json',
          'records/checkpoint37_final_pdf_audit_run.out',
          'records/checkpoint37_final_pdf_audit_run.err',
          'work_A/checkpoint37_final_page_review.json',
          'work_CE/checkpoint37_final_page_review.json',
          'work_DE/checkpoint37_page_review_c5be64cd_before_Bu_correction.json',
          'records/thirty_seventh_hour_research_report.md']
names += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'records/pdf_qa/checkpoint37_final').rglob('*')) if p.is_file()]
rows = []
for rel in names:
    src = ROOT/rel
    assert src.is_file(), rel
    raw = src.read_bytes()
    dst = DEST/rel
    if dst.suffix in {'.aux','.toc','.bbl','.blg'}:
        dst = dst.with_name(dst.name+'.retained.txt')
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('xb') as stream:
        stream.write(raw)
    rows.append({'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                 'retained_as':str(dst.relative_to(ROOT))})
record = {'recorded_at':datetime.now(timezone.utc).isoformat(),
          'result':'RETAINED_BEFORE_A127_Bu_MISSING_FACTOR_CORRECTION',
          'reason':'On page234 the prose following A.127.27 omitted B_u in Theta(Pi_u)=L D W B_u F_b^-1; the Br-membership argument is unchanged after literal repair.',
          'prior_final_pdf_sha256':'c5be64cdf00bf3a384a3328de004453b3e3496f969822af26fbf6df88af0c8a2',
          'prior_actual_operations':[
              {'role':'build','session_id':70791,'exit_code':0,'tool_chunk_id':'20b7cb','full_driver_read':'71b90e'},
              {'role':'metrics','session_id':48509,'exit_code':0,'tool_chunk_id':'1e4569','full_output_read':'4e5cef'},
              {'role':'render','session_id':90930,'exit_code':0,'tool_chunk_id':'cca131','full_output_read':'d20e5e'},
              {'role':'audit','exit_code':0,'tool_chunk_id':'e95c13','full_output_read':'a30416'}],
          'root_old_rendered_images_observed':False,
          'old_root_image_output_truncated_and_not_counted':True,
          'running_old_size_estimate_session_id':12069,
          'size_estimate_completion_not_yet_observed':True,
          'retained_files':rows}
with (ROOT/'records/checkpoint37_before_A127_Bu_correction_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2)
    stream.write('\n')
print(json.dumps({'result':record['result'],'files':len(rows),'prior_pdf':record['prior_final_pdf_sha256']}))
