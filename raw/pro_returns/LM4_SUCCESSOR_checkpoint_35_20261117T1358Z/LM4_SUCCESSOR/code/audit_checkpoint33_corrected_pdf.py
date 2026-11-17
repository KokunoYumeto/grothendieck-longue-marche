"""Bind the corrected PDF logs and exact render comparison; do not infer fresh viewing."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda rel:json.loads((root/rel).read_text())
m=read('records/checkpoint33_metrics.json')
current=root/'records/pdf_qa/checkpoint33_final'
prior=root/'records/pdf_qa/checkpoint33_abstract_firstpass/render'
render=json.loads((current/'render_manifest.json').read_text())
old_render=json.loads((prior/'render_manifest.json').read_text())
assert sha(root/'LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==render['pdf_sha256']
assert m['pages']==render['page_count']==old_render['page_count']==626
assert render['rendered_pages']==old_render['rendered_pages']
assert render['required_new_mathematical_pages']==old_render['required_new_mathematical_pages']
comparisons=[]
for path in sorted(current.glob('*.png')):
    before=prior/path.name;assert before.is_file()
    old_sha=sha(before);new_sha=sha(path)
    comparisons.append(dict(file=path.name,old_path=str(before.relative_to(root)),new_path=str(path.relative_to(root)),
        old_sha256=old_sha,new_sha256=new_sha,byte_identical=before.read_bytes()==path.read_bytes()))
by_name={r['file']:r for r in comparisons}
receipts=['work_A/review_checkpoint33_initial_pages165_169.json','work_CE/checkpoint33_initial_visual_receipt_170_173.json','work_DE/checkpoint33_visual_review_pages529_536.json']
carried=[]
for rel in receipts:
    receipt=read(rel)
    assert receipt['pdf_sha256']==old_render['pdf_sha256']
    assert receipt['render_manifest_sha256']==sha(prior/'render_manifest.json')
    for row in receipt['pages']:
        assert row.get('result',row.get('status'))=='PASS' and not row.get('issues',[])
        assert row.get('actually_viewed_individually',row.get('actually_viewed')) is True
        name=f"page-{row['page']:03d}.png"
        compare=by_name[name]
        assert compare['old_sha256']==row['sha256']
        assert compare['byte_identical'],('New proof page requires fresh view',row['page'])
        carried.append(dict(page=row['page'],initial_receipt=rel,final_png_sha256=compare['new_sha256'],
            initial_individual_visual_observation='PASS',final_byte_identity=True))
assert sorted(r['page'] for r in carried)==render['required_new_mathematical_pages']
passes=root/'records/build_passes/20261117T113300822524Z'
audits=[]
for path in [root/'LM4_SUCCESSOR_paper.log',*sorted(passes.glob('build*.log'))]:
    content=path.read_text()
    warnings=[line for line in content.splitlines() if re.search(r'\bwarning\b',line,re.I) and not line.startswith(('Package:','File:'))]
    issues=[line for line in content.splitlines() if re.search(r'overfull|undefined|missing character|^!|fatal error|rerun to get',line,re.I)]
    notices=re.findall(r'^.*Underfull.*$',content,re.M)
    overfull=re.findall(r'^.*Overfull.*$',content,re.M)
    audits.append(dict(path=str(path.relative_to(root)),sha256=sha(path),warnings=warnings,issues=issues,underfull_notices=notices,overfull=overfull))
final=[audits[0],next(a for a in audits if a['path'].endswith('/build_stabilize_0.log'))]
assert all(not a['warnings'] and not a['issues'] for a in final)
assert Counter(final[0]['underfull_notices'])==Counter(final[1]['underfull_notices'])
old_notices=read('records/checkpoint32_visual_review.json')['final_log_and_stdout_audits'][0]['underfull_notices']
assert Counter(old_notices)==Counter(final[0]['underfull_notices']) and len(old_notices)==19
assert all(not a['overfull'] for a in audits)
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),result='PASS_RENDER_IDENTITY_AND_FINAL_LOGS',
    final_pdf_sha256=m['pdf_sha256'],initial_pdf_sha256=old_render['pdf_sha256'],
    old_render_manifest_sha256=sha(prior/'render_manifest.json'),final_render_manifest_sha256=sha(current/'render_manifest.json'),
    all_png_comparisons=comparisons,carried_individual_math_page_observations=carried,
    initial_review_receipts={p:sha(root/p) for p in receipts},
    changed_pngs=[r['file'] for r in comparisons if not r['byte_identical']],
    final_log_and_stdout_audits=final,all_final_build_pass_audits=audits,
    previous_overfull_count=0,first33_overfull_count=0,corrected_first_pass_overfull_count=0,final_overfull_count=0,
    unchanged_underfull_count=19,
    scope='All17 final new mathematical PNGs are byte-identical to the exact individually viewed initial PNGs. This transfers actual visual observations of identical images; it is not a fresh image-view claim. Changed front matter still requires actual final viewing.')
target=root/'records/checkpoint33_corrected_pdf_audit.json';assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(result=record['result'],final_pdf_sha256=m['pdf_sha256'],math_pages_carried=len(carried),
    changed_pngs=record['changed_pngs'],final_overfull=0,final_warnings=0,final_errors=0,unchanged_underfull=19),indent=2))
