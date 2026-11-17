"""Record actual final front-page views and reviewed identical mathematical images."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((root/rel).read_text())
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
m=read('records/checkpoint33_metrics.json')
render=read('records/pdf_qa/checkpoint33_final/render_manifest.json')
audit=read('records/checkpoint33_corrected_pdf_audit.json')
initial=read('records/checkpoint33_initial_root_visual_observations.json')
assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==render['pdf_sha256']==audit['final_pdf_sha256']
assert audit['changed_pngs']==['contact-01.png','page-001.png','page-002.png']
comparisons={r['file']:r for r in audit['all_png_comparisons']}
for n in [4,615,626]:
    name=f'page-{n:03d}.png'
    assert comparisons[name]['byte_identical']
    assert initial['image_sha256'][name]==comparisons[name]['new_sha256']
for n in range(2,6):
    name=f'contact-{n:02d}.png'
    assert comparisons[name]['byte_identical']
    assert initial['image_sha256'][name]==comparisons[name]['new_sha256']
root_receipt=dict(recorded_at=datetime.now(timezone.utc).isoformat(),reviewer='/root',pdf_sha256=m['pdf_sha256'],
    freshly_individually_viewed_final_pages=[1,2],freshly_viewed_final_contacts=[1],
    prior_individual_page_observations_carried_by_exact_png_identity=[4,615,626],
    prior_contact_observations_carried_by_exact_png_identity=[2,3,4,5],
    individual_pages=[1,2,4,615,626],
    each_actual_image_view_was_separate=True,truncated_outputs_counted=False,
    final_image_sha256={f'records/pdf_qa/checkpoint33_final/{name}':r['new_sha256'] for name,r in comparisons.items()},
    observations='Corrected final abstract pages1 and2 and contact1 individually opened and read: explicit full-GT and residue-ring wording; no clipping, overlap or missing glyphs. All other contact and root individual observations transfer only through exact byte equality to the already viewed images. The final reference continuation is unchanged.',issues=[])
path=root/'records/checkpoint33_root_visual_observations.json';assert not path.exists()
path.write_text(json.dumps(root_receipt,indent=2)+'\n')
receipts=list(audit['initial_review_receipts'])+['records/checkpoint33_initial_root_visual_observations.json','records/checkpoint33_root_visual_observations.json','records/checkpoint33_corrected_pdf_audit.json']
individual=sorted(set(render['required_new_mathematical_pages'])|{1,2,4,615,626})
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),visual_review='PASS',pdf_sha256=m['pdf_sha256'],
    rendered_pages=render['rendered_pages'],required_math_pages=render['required_new_mathematical_pages'],individually_inspected_pages=individual,
    individual_page_review_receipts={rel:sha(rel) for rel in receipts},contact_sheets_inspected=5,
    each_contact_sheet_opened_separately=True,truncated_outputs_counted=False,
    final_log_and_stdout_case_insensitive='PASS',final_log_and_stdout_audits=audit['final_log_and_stdout_audits'],
    underfull_scope='Exactly19 final underfull notices; identical as a multiset to checkpoint32 and to the final stabilized stdout. No new underfull paragraph. Zero overfull boxes in the original33 build, the corrected first pass, and the final pass.',
    corrected_edition_scope='Final626-page PDF SHA80e44d3c. All17 required mathematical pages freshly rendered and proven byte-identical to the exact individually inspected first-pass PNGs; initial review receipts retain their original PDF hash honestly. Changed final pages1 and2 and contact1 freshly viewed. All40 rendered pages covered by actual image observations and exact final-byte bindings.')
target=root/'records/checkpoint33_visual_review.json';assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n')
text=('Visual review: PASS\nFinal PDF SHA256: '+m['pdf_sha256']+'\n'
      '626 pages;17 new mathematical pages individually inspected with exact unchanged final PNG identity;22 individual pages overall;40 rendered pages on5 separately viewed contact images.\n'
      'Changed final abstract pages1 and2 and contact1 freshly inspected. Final engine log and stabilized stdout:0 overfull,0 warnings,0 errors;19 unchanged underfull notices.\n'
      'Overflow counts: before integration0; first33 build0; corrected first pass0; final0. No overflow>2pt.\n')
(root/'records/checkpoint33_typesetting.txt').write_text(text)
append='\n### Observed final33 typesetting verification\n\n'+text.replace('\n','  \n')+'\n'
for rel in ['records/thirty_third_hour_research_report.md','LM4_SUCCESSOR_report.md']:
    path=root/rel;path.write_text(path.read_text()+append)
print(json.dumps(dict(status='PASS',pdf_sha256=m['pdf_sha256'],pages=626,required_math_pages=17,individual_pages=len(individual),rendered_pages=40,contacts=5,underfull_notices=19),indent=2))
