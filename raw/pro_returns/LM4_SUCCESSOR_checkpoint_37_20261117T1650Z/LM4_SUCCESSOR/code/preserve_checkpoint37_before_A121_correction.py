"""Retain the clean typesetting build before the newly found algebraic repair."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'records/checkpoint37_before_A121_correction'
DEST.mkdir(exist_ok=False)
names=['LM4_SUCCESSOR_paper'+ext for ext in ('.tex','.pdf','.log','.aux','.toc','.out','.bbl','.blg')]
names += ['records/checkpoint37_build_driver.out','records/checkpoint37_build_driver.err',
          'sections/a_elliptic_pentagon_cubic.tex','work_A/A121_elliptic_pentagon_cubic_proposed.tex',
          'LM4_SUCCESSOR_report.md','LM4_SUCCESSOR_references.bib',
          'records/checkpoint37_root_formal_reviews.json','records/checkpoint37_formal_source_copies.json',
          'records/checkpoint37_independent_review_manifest.json',
          'records/checkpoint37_operational_source_review.json',
          'code/render_checkpoint37_pdf.py','code/finalize_checkpoint37_visual_record.py',
          'code/bind_checkpoint37_operational_reviews.py']
rows=[]
for rel in names:
    src=ROOT/rel
    if not src.exists():
        rows.append({'path':rel,'exists':False})
        continue
    raw=src.read_bytes()
    dst=DEST/rel
    if dst.suffix in {'.aux','.toc','.bbl','.blg'}:
        dst=dst.with_name(dst.name+'.retained.txt')
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_bytes(raw)
    rows.append({'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                 'retained_as':str(dst.relative_to(ROOT))})
record={'recorded_at':datetime.now(timezone.utc).isoformat(),
        'actual_build_session_id':76904,'actual_launch_chunk_id':'e186a7',
        'actual_exit_code':0,'actual_exit_observed_chunk_id':'b07e37',
        'actual_full_driver_read_chunk_id':'66a575',
        'pass_directory':'records/build_passes/20261117T153617186723Z',
        'reason':'A.130 layout repair passed; before accepting dependent mathematics, a fresh A.121/primary Proposition2.20(2) literal-conjugation audit requires the separately checked algebraic correction.',
        'primary_fresh_read':{'url':'https://arxiv.org/pdf/1003.1012',
          'version':'1003.1012v3,26July2012',
          'scope':'Proposition2.20 statement/full-profinite continuation and part(2), especially author-version pp16–17.',
          'web_refs':['turn1267view0','turn1272view0','turn1272view1'],
          'screenshots_requested_but_not_counted_as_actual_visual_read':['turn1271view0','turn1271view1','turn1271view2']},
        'retained_files':rows}
with (ROOT/'records/checkpoint37_before_A121_correction_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2)
    stream.write('\n')
print(json.dumps({'result':'RETAINED_BEFORE_ALGEBRAIC_CORRECTION','files':len(rows),
                  'actual_prior_build_exit':0}))
