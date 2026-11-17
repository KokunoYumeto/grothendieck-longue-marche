"""Record actually observed final35 page images and aggregate complete coverage."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,shutil

root=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((root/p).read_text())
sha=lambda p:hashlib.sha256((root/p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
parser=argparse.ArgumentParser();parser.add_argument('--agent-reviews',nargs=3,required=True);args=parser.parse_args()
m=read('records/checkpoint35_metrics.json');render=read('records/pdf_qa/checkpoint35_final/render_manifest.json')
audit=read('records/checkpoint35_final_pdf_audit.json');layout=read('records/checkpoint35_layout_correction.json')
expected='fc8b22184ee554e6586974df2e31a9b049622bdd700f58992cb0f4e74154b12f'
assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==render['pdf_sha256']==audit['final_pdf_sha256']==expected
assert m['pages']==render['page_count']==671
assert audit['final_overfull_count']==0 and audit['final_underfull_count']==19
assert audit['underfull_identical_to_checkpoint34']
assert len(layout['first_build_observed']['overfull_notices'])==2
assert not any(a['overfull'] for a in audit['all_final_build_pass_audits'])
render_path='records/pdf_qa/checkpoint35_final/render_manifest.json'
observations={
 1:'Title, author credit, INCOMPLETE status and opening abstract are clear; no clipping or collisions.',
 2:'New residual/tower/cohomology abstract scope and Part B continuation are clear and within the margins.',
 4:'New compact/mixed-contact scope, remaining-open paragraph and contents transition fit with legible page references.',
 205:'A116 residual nontriviality and A117 whole-cohomology statement, exact sequence and product displays fit; all equation tags remain distinct.',
 206:'Original coherent defect, explicit full cubic gate and beginning of its proof are legible; the long product and conjugator formulas fit.',
 207:'Specified-frame norm, original marking, full cubic proof and A118 opening render clearly; provenance paths and equation labels stay within margins.',
 208:'Full normalization, exact canonical norm and dihedral setup have intact formulas and no collisions or missing glyphs.',
 660:'Final Part E proof and References opening are legible and unclipped; the separate editorial spacing note below is retained.',
 671:'All final bibliography entries, source-verification scopes and final page number are legible; no clipping or overlap.'}
root_receipt='records/checkpoint35_root_visual_observations.json'
record=dict(recorded_at=now(),reviewer='/root',result='PASS',pdf_sha256=expected,
 render_manifest_sha256=sha(render_path),each_actual_image_view_was_separate=True,truncated_outputs_counted=False,
 pages=[dict(page=n,path=f'records/pdf_qa/checkpoint35_final/page-{n:03d}.png',sha256=sha(f'records/pdf_qa/checkpoint35_final/page-{n:03d}.png'),
    actually_viewed_individually=True,result='PASS',observation=obs,issues=[]) for n,obs in observations.items()],
 contacts=[dict(path=f'records/pdf_qa/checkpoint35_final/contact-{n:02d}.png',sha256=sha(f'records/pdf_qa/checkpoint35_final/contact-{n:02d}.png'),
    actually_viewed_separately=True,result='PASS',issues=[]) for n in range(1,7)],
 contact_observation='Each of all six complete contact images was opened in a separate tool output. All52 rendered pages have consistent margins and no clipped material, formula collisions or missing-glyph patterns. Individual mathematical-page inspections are separate.',
 nonblocking_notes=[dict(page=660,note='Inherited E52 citation is immediately adjacent to the preceding full stop (159.Herfort). It is legible, creates no overflow, and is queued with the A119 citation-spacing correction for the next typesetting pass.')],issues=[])
assert not (root/root_receipt).exists()
(root/root_receipt).write_text(json.dumps(record,indent=2)+'\n')
receipts=[*args.agent_reviews,root_receipt]
assert len(set(receipts))==4
individual=set();notes=[]
for rel in receipts:
    item=read(rel)
    assert item['pdf_sha256']==expected
    manifest=item.get('render_manifest_sha256')
    if manifest is None:manifest=item['render_manifest']['sha256']
    assert manifest==sha(render_path)
    assert not item.get('truncated_outputs_counted',False)
    for row in item['pages']:
        assert row.get('result',row.get('status'))=='PASS' and not row.get('issues',[])
        assert row.get('actually_viewed_individually',row.get('actually_viewed')) is True
        path=row.get('path',row.get('file'));assert sha(path)==row['sha256']
        individual.add(row['page'])
        notes.extend([dict(receipt=rel,page=row['page'],note=v) for v in row.get('nonblocking_notes',[])])
    notes.extend([dict(receipt=rel,observation=v) for v in item.get('nonblocking_notes',[])])
assert set(render['required_new_mathematical_pages'])<=individual<=set(render['rendered_pages'])
assert len(render['required_new_mathematical_pages'])==29 and len(individual)==34
assert len(render['rendered_pages'])==52 and render['contact_sheets']==6
for row in audit['final_log_and_stdout_audits']:
    assert sha(row['path'])==row['sha256'] and not row['warnings'] and not row['issues']
summary=dict(recorded_at=now(),visual_review='PASS',pdf_sha256=expected,
 rendered_pages=render['rendered_pages'],required_math_pages=render['required_new_mathematical_pages'],
 individually_inspected_pages=sorted(individual),individual_page_review_receipts={p:sha(p) for p in receipts},
 contact_sheets_inspected=6,each_contact_sheet_opened_separately=True,truncated_outputs_counted=False,
 final_log_and_stdout_case_insensitive='PASS',final_log_and_stdout_audits=audit['final_log_and_stdout_audits'],
 underfull_scope='Exactly19 final underfull notices, identical as a multiset to checkpoint34 and to the final stabilized stdout. No new underfull paragraph.',
 nonblocking_editorial_notes=notes,
 corrected_edition_scope='Final671-page PDF. All29 new mathematical pages individually viewed, plus5 individual front/reference samples; all52 rendered pages covered by6 separately opened contact sheets. First35 build had2 overflows8.56215pt and11.13672pt; every corrected pass and final log has0. Two local line-break changes preserved every mathematical assertion. Minor citation-spacing observations remain explicitly recorded for the next editorial pass.')
target=root/'records/checkpoint35_visual_review.json';assert not target.exists();target.write_text(json.dumps(summary,indent=2)+'\n')
text=('Visual review: PASS\nFinal PDF SHA256: '+expected+'\n'
 '671 pages;29 new mathematical pages individually inspected;34 individual pages overall;52 rendered pages on6 separately opened contact images.\n'
 'Final engine log and stabilized stdout:0 overfull,0 warnings,0 errors;19 unchanged underfull notices.\n'
 'Overflow counts: before integration0; first35 build2 (8.56215pt and11.13672pt); corrected first pass0; final0.\n'
 'The failed edition, every source change and its logs are preserved. Only definition-line layout and a breakable conjunction between identical references were changed.\n'
 'Minor citation-spacing observations on211 and660 are legible, do not overflow, and remain recorded for the next editorial pass; no clipping or missing-glyph defect was found.\n')
target=root/'records/checkpoint35_typesetting.txt';assert not target.exists();target.write_text(text)
backup=root/'records/checkpoint35_before_final_qa';backup.mkdir(exist_ok=False)
addition='\n### Observed final35 typesetting verification\n\n'+text.replace('\n','  \n')+'\n'
for rel in ['records/thirty_fifth_hour_research_report.md','LM4_SUCCESSOR_report.md']:
    path=root/rel;saved=backup/rel;saved.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(path,saved)
    path.write_text(path.read_text()+addition)
print(json.dumps(dict(status='PASS',pdf_sha256=expected,pages=671,required_math_pages=29,individual_pages=34,rendered_pages=52,contacts=6,nonblocking_editorial_notes=notes),indent=2))
