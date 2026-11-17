"""Read-only checks of the genuinely built and reviewed checkpoint34 snapshot."""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re

def main():
    root=Path(__file__).resolve().parents[1]
    read=lambda rel:json.loads((root/rel).read_text())
    sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
    m=read('records/checkpoint34_metrics.json')
    assert m['statements']==362 and m['task_rows']==49 and m['bibliography_entries']==116
    assert m['statuses']=={'Known':6,'Proved':318,'Refuted':19,'Open':19}
    assert m['pages']>0 and not m['overfull'] and not m['warnings'] and not m['errors']
    assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']
    assert (root/'LM4_SUCCESSOR_paper.pdf').stat().st_size==m['pdf_bytes']
    review=read('records/checkpoint34_root_formal_reviews.json')
    assert review['status']=='PASS_COMPLETE_SOURCE_REVIEW'
    assert [r['statement'] for r in review['copies']]==['A.'+str(n) for n in range(106,112)]+['B.'+str(n) for n in range(165,167)]
    for row in review['copies']:
        assert (root/row['source']).read_bytes()==(root/row['target']).read_bytes()
        assert sha(row['target'])==row['sha256']
    assert read('records/checkpoint34_formal_source_copies.json')['copies']==review['copies']
    for rel,digest in review['independent_reviews'].items():
        assert sha(rel)==digest,rel
    assert sha(review['bibliography']['path'])==review['bibliography']['sha256']
    rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
    assert len(rows)==362 and dict(Counter(r['status'] for r in rows))==m['statuses']
    tasks=list(csv.DictReader((root/'task_coverage.csv').open()))
    assert len(tasks)==49
    for task in ('A.8','B.4'):
        assert next(r for r in tasks if r['task']==task)['outcome']=='Open'
    assert (root/'LM4_SUCCESSOR_report.md').read_text().splitlines()[0]=='INCOMPLETE'
    assert len(re.findall(r'\\bibitem',(root/'LM4_SUCCESSOR_paper.bbl').read_text()))==116
    for entry in re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]:
        assert re.search(r'\b(?:verified|unverified)\b',entry,re.I)
    visual=read('records/checkpoint34_visual_review.json')
    render=read('records/pdf_qa/checkpoint34_final/render_manifest.json')
    assert visual['visual_review']=='PASS'
    assert visual['pdf_sha256']==render['pdf_sha256']==m['pdf_sha256']
    assert render['page_count']==m['pages'] and render['dpi']==144
    assert visual['rendered_pages']==render['rendered_pages']
    assert visual['required_math_pages']==render['required_new_mathematical_pages']
    assert set(visual['required_math_pages'])<=set(visual['individually_inspected_pages'])
    assert set(visual['individually_inspected_pages'])<=set(visual['rendered_pages'])
    assert visual['contact_sheets_inspected']==render['contact_sheets']>0
    assert visual['each_contact_sheet_opened_separately'] and not visual['truncated_outputs_counted']
    assert visual['underfull_scope']
    for audit in visual['final_log_and_stdout_audits']:
        assert sha(audit['path'])==audit['sha256']
        assert not audit['warnings'] and not audit['issues']
    for rel,digest in visual['individual_page_review_receipts'].items():
        assert sha(rel)==digest
    anchor=read('records/checkpoint34_retention_parent_anchor.json')
    assert anchor['parent_number']==33 and anchor['child_number']==34
    assert anchor['archive']=='LM4_SUCCESSOR_checkpoint_33.zip'
    assert anchor['archive_bytes']==508499680
    assert anchor['archive_sha256']=='5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96'
    assert anchor['logical_entries']==10053 and anchor['inherited_rows']==142600
    assert anchor['inherited_archives']==32
    assert sum(anchor['inherited_counts'].values())==142600
    for evidence in anchor['trusted_coverage']['verification_records'].values():
        assert evidence['actual_exit_code_observed']==0
        assert sha(evidence['path'])==evidence['sha256']
        assert (root/evidence['path']).stat().st_size==evidence['bytes']
    estimate=read('records/checkpoint34_size_estimate.json')
    assert estimate['baseline_archive']=='LM4_SUCCESSOR_checkpoint_33.zip'
    assert estimate['baseline_bytes']==508499680
    assert estimate['baseline_sha256']=='5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96'
    assert estimate['estimated_total_with_allowance']<estimate['delivery_cap_bytes']==536870912
    assert not estimate['creates_zip'] and not estimate['writes_authored_input_files']
    assert estimate['current_main_pdf_sha256']==m['pdf_sha256']
    for kind,expected in [('images',67108864),('documents',8388608),('data',67108864)]:
        assert estimate['prospective_bundles'][kind]['dictionary_bytes']==expected
        assert estimate['prospective_bundles'][kind]['zip_method']=='ZIP_LZMA'
    freeze=read('records/checkpoint34_writer_pause.json')
    assert freeze['all_writers_paused'] and len(freeze['agents'])==3 and not freeze['live_producers']
    ready=read('records/checkpoint34_capture_ready.json')
    assert ready['ready'] and ready['main_A']==ready['main_B']==ready['actual_CM_parity']=='Open'
    assert ready['pdf_sha256']==m['pdf_sha256']
    for item in ready['observed_producer_completions']:
        assert item['exit_code']==0
    for rel in ['records/thirty_fourth_hour_research_report.md','records/checkpoint34_computation_audit_state.md',
                'code/verify_checkpoint34_system_tars.py','code/verify_checkpoint34_inductive_retention.py']:
        assert (root/rel).is_file(),rel
    assert not (root.parent/'LM4_SUCCESSOR_checkpoint_34.zip').exists()
    print('PASS:362 statements,116 references,49 tasks; current PDF and every new page reviewed; exact closed33 anchor and current size evidence; actual mains/CM Open.',flush=True)

if __name__=='__main__':
    main()
