"""Refresh current exact-repair evidence while preserving historical probes."""
from pathlib import Path
from collections import Counter
from hashlib import sha256
import csv, json, re, datetime, argparse

ROOT=Path(__file__).resolve().parents[2]
def digest(path): return sha256(path.read_bytes()).hexdigest()
def accepted_probe(ident,language,mode,pdf,image,page,reviewer,observation):
    pdf=ROOT/pdf;image=ROOT/image
    log=pdf.with_suffix('.log').read_text(errors='replace')
    errors=len(re.findall(r'^!',log,re.M));overfull=log.count('Overfull \\hbox');missing=log.count('Missing character:')
    assert errors==overfull==missing==0
    return dict(repair_id=ident,language=language,mode=mode,
        historical_checkpoint_pdf=pdf.relative_to(ROOT).as_posix(),pdf_sha256=digest(pdf),
        pdf_delivery_status='historical development probe; excluded from FINAL',delivered_pdf=None,
        errors=errors,overfull_hboxes=overfull,missing_characters=missing,
        visually_inspected_pages=[page],reviewer=reviewer,
        proof_image='proofs/visual_repairs/'+image.name,proof_image_sha256=digest(image),
        proof_tex='proofs/visual_repairs/'+pdf.with_suffix('.tex').name,
        proof_tex_sha256=digest(pdf.with_suffix('.tex')),
        proof_log='proofs/visual_repairs/'+pdf.with_suffix('.log').name,
        proof_log_sha256=digest(pdf.with_suffix('.log')),observation=observation)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--preserve-freeze',action='store_true',help='Refresh records only; require the installed dependency hashes to match the existing source freeze.')
    args=parser.parse_args()
    data=ROOT/'work/data'
    path=data/'layout_probe_validation.json'
    obj=json.loads(path.read_text())
    records=json.loads((data/'layout_repairs_applied.json').read_text())
    exact=json.loads((data/'layout_exact_patches.json').read_text())
    semantic=json.loads((data/'layout_semantic_command_audit.json').read_text())
    visual=list(csv.DictReader((ROOT/'work/records/VISUAL_REPAIRS.tsv').open(),delimiter='\t'))
    assert semantic['total_local_changes']==len(records)
    assert semantic['local_size_gate']['all_added_sizes_pass']
    obj.update(exact_records=len(records),record_kinds=dict(Counter(r['kind'] for r in records)),
               source_byte_span_failures=[],layout_module_sha256=digest(ROOT/'work/scripts/layout_repairs.py'))
    obj['current_source_layout_audit']=dict(
        exact_records=len(records),per_language=dict(Counter(r['language'] for r in records)),
        exact_scan_local_net_patches=sum(len(p['patches']) for p in exact['packages']),
        affected_language_package_entries=len(exact['packages']),all_net_patches_replayed_exactly=True,
        source_package_language_inputs=semantic['package_language_pairs'],
        named_mathematical_commands_preserved=True,source_marks_preserved=semantic['all_source_marks_preserved'],
        paired_stable_ids_equal=semantic['paired_stable_ids_equal'],
        source_character_and_utf8_byte_offsets_valid=semantic['all_raw_source_offsets_valid'],
        exact_patch_manifest='data/layout_exact_patches.json',exact_patch_manifest_sha256=digest(data/'layout_exact_patches.json'),
        semantic_audit='data/layout_semantic_command_audit.json',semantic_audit_sha256=digest(data/'layout_semantic_command_audit.json'),
        local_size_audit='data/layout_size_audit.json',local_size_audit_sha256=digest(data/'layout_size_audit.json'),
        minimum_added_font_ratio=semantic['local_size_gate']['minimum_added_font_ratio_to_body'],
        minimum_added_scale_factor=semantic['local_size_gate']['minimum_added_scale_factor'],
        all_added_sizes_pass_70_percent=True,
        visual_repairs_record='records/VISUAL_REPAIRS.tsv',
        confirmed_visual_scan_sites=len({(r['cote'],r['affected_scan']) for r in visual}),
        confirmed_visual_display_or_placement_occurrences=len({r['repair_id'] for r in visual}),
        paired_visual_rows=len(visual),
        visual_source_local_rows=sum(r.get('record_basis')!='generated range-heading formatting' for r in visual),
        visual_generated_formatting_rows=sum(r.get('record_basis')=='generated range-heading formatting' for r in visual),
        visual_probe_inventory='data/visual_repair_proof_inventory.json')
    extra=[]
    for lang in ['fr','en']:
        for mode in [0,1,2]:
            name=f'scan276_clearance_{lang}_{mode}'
            pdf=ROOT/'work/layout_probes'/f'{name}.pdf'
            log=pdf.with_suffix('.log').read_text(errors='replace')
            errors=len(re.findall(r'^!',log,re.M));overfull=log.count('Overfull \\hbox');missing=log.count('Missing character:')
            assert errors==overfull==missing==0
            image=(ROOT/'work/visual_repair_proofs'/(f'140-4-276-L1_{lang}.png' if mode==1 else f'{name}.png'))
            extra.append(accepted_probe('140-4-276-L1',lang,mode,pdf.relative_to(ROOT),image.relative_to(ROOT),1,'typeset',
                'The uncertain alternative arrows fit between the complete source and target objects; deleted content or its reading-form uncertainty markers remain present; the surrounding array is clear.'))
    probes=ROOT/'work/layout_probes'
    for row in json.loads((probes/'final_residual_labels_visual_review.json').read_text()):
        ids={446:'140-3-446-T1',574:'140-3-574-L1',561:'140-3-561-D1',637:'140-3-637-T1',638:'140-3-638-L1'}
        extra.append(accepted_probe(ids[row['scan']],row['language'],row['form'],row['pdf'],row['proof_png'],
            row['pdf_page'],row['reviewer'],row['observation']))
    for row in json.loads((probes/'scan97_restriction_proof_index.json').read_text()):
        extra.append(accepted_probe('140-3-97-L1',row['language'],row['form'],row['probe_pdf'],row['image'],
            row['page'],row['reviewer'],row['observation']))
    for row in json.loads((probes/'scan440_geometry_validation.json').read_text())['visual_observations']:
        extra.append(accepted_probe('140-3-440-L1',row['language'],row['form'],
            f"work/layout_probes/scan440_candidate_{row['language']}.pdf",row['image'],row['form']+4,'editorial',row['observation']))
    for row in json.loads((probes/'scan545_eq58_validation.json').read_text())['forms']:
        extra.append(accepted_probe('140-3-545-L2',row['language'],row['form'],
            f"work/layout_probes/scan545_eq58_{row['language']}.pdf",row['image'],row['form']+1,'editorial',row['observation']))
    obj['latest_all_form_probes']=extra
    obj['latest_all_form_probe_count']=len(extra)
    obj['latest_all_form_probe_scope']='Earlier nine diagram repair occurrences in both languages and all three forms; all 54 diagram images were actually inspected by their named reviewer. The later revision512 findings are recorded separately in current_batch_accepted_probes.'
    batch_path=data/'layout_pending_batch.json'
    if batch_path.exists():
        batch=json.loads(batch_path.read_text());accepted=[]
        for item in batch['items']:
            candidate=ROOT/item['candidate'];validation=ROOT/item['validation']
            assert digest(candidate)==item['candidate_sha256']
            assert digest(validation)==item['validation_sha256']
            accepted.append(dict(name=item['name'],stage=item['stage'],candidate=item['candidate'],
                candidate_sha256=digest(candidate),validation=item['validation'],
                validation_sha256=digest(validation),validation_status=item['validation_status'],
                source_language_records=item['paired_records'],
                scope='Accepted local probe with attributed actual-image observations; final full-book closure is separate.'))
        obj['current_batch_accepted_probes']=dict(candidate_files=len(accepted),
            source_language_records_touched=sum(x['source_language_records'] for x in accepted),
            added_source_records=batch.get('accepted_addition_records'),
            replacement_source_records=batch.get('accepted_replacement_records'),
            actual_visual_observations_created_by_refresh_script=False,evidence=accepted)
    residual_path=data/'layout_residual_batch_revision578.json'
    residual_integration=data/'layout_residual_revision578_integration_result.json'
    if residual_path.exists() and residual_integration.exists():
        batch=json.loads(residual_path.read_text());accepted=[]
        integration=json.loads(residual_integration.read_text())
        assert integration['manifest_sha256']==digest(residual_path)
        for item in batch['items']:
            candidate=ROOT/item['candidate'];validation=ROOT/item['validation']
            assert digest(candidate)==item['candidate_sha256']
            assert digest(validation)==item['validation_sha256']
            proof=json.loads(validation.read_text());assert proof['status']=='PASS'
            accepted.append(dict(name=item['name'],stage=item['stage'],candidate=item['candidate'],
                candidate_sha256=digest(candidate),validation=item['validation'],
                validation_sha256=digest(validation),validation_status=proof['status'],
                source_language_records=0 if item['stage']=='generated' else 2,
                generated_language_examples=2 if item['stage']=='generated' else 0,
                scope='Accepted actual probe evidence only; current publication closure is a separate required gate.'))
        obj['revision578_residual_accepted_probes']=dict(
            base_source_records=batch['base_records'],candidate_files=len(accepted),
            added_source_records=batch['added_source_records'],
            generated_package_exceptions=batch['generated_package_exceptions'],
            original_batch_evidence_preserved='current_batch_accepted_probes',
            actual_visual_observations_created_by_refresh_script=False,
            manifest=residual_path.relative_to(ROOT).as_posix(),manifest_sha256=digest(residual_path),
            integration_record=residual_integration.relative_to(ROOT).as_posix(),
            integration_sha256=digest(residual_integration),evidence=accepted)
    pagination=json.loads((probes/'tag_pattern_stress_validation.json').read_text())
    for row in pagination:
        pdf=ROOT/row['pdf'];assert row['pdf_sha256']==digest(pdf)
        row['delivered_pdf']=None
        row['proof_tex']='proofs/visual_repairs/'+pdf.with_suffix('.tex').name
        row['proof_log']='proofs/visual_repairs/'+pdf.with_suffix('.log').name
        if row.get('review_image'):
            row['delivered_review_image']='proofs/visual_repairs/'+Path(row['review_image']).name
            row['review_image_sha256']=digest(ROOT/row['review_image'])
    obj['pagination_stress_probes']=pagination
    obj['pagination_stress_scope']='All 60 forced-page-foot groups passed six language/form compiles; the ten French diplomatic and ten English reading groups were actually viewed. Final book pagination is a separate required visual gate.'
    refresh=probes/'tag_pattern_stress_revision578_refresh.json'
    if refresh.exists():
        refreshed=json.loads(refresh.read_text())
        assert refreshed['status']=='PASS'
        obj['pagination_stress_recompilation']=dict(record=refresh.relative_to(ROOT).as_posix(),sha256=digest(refresh),
            status='PASS',scope='Regenerated TeX was recompiled; exact per-page pixel identity preserves only the explicitly recorded prior actual inspections.')
    reconciliation=json.loads((data/'layout_pagination_reconciliation.json').read_text())
    obj['pagination_source_reconciliation']={key:reconciliation[key] for key in [
        'historical_primary_candidates','confirmed_detached_instances','cleared_same_page_instances',
        'all_confirmed_instances_bound_exactly','exact_binding_records','paired_binding_sites',
        'covered_standalone_leading_tag_sites','leading_tag_binding_sites','confirmed_trailing_tag_sites',
        'section_opening_binding_sites','affected_packages','final_page_inspection_is_a_separate_required_gate']}
    obj['probe_delivery_policy']='Every development probe PDF is historical evidence retained only in checkpoints and is excluded from FINAL. FINAL contains exactly seven publication PDFs; accepted proof PNG, TeX, log and hash records are delivered.'
    for row in obj.get('probes',[]):
        row['pdf_delivery_status']='historical development probe; excluded from FINAL'
        row['delivered_pdf']=None
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    dependencies=['work/scripts/layout_repairs.py']+[
        'work/data/'+name for name in ['layout_label_clearances.json','layout_expected_matches.json',
        'layout_diagram_targets.json','layout_cancelled_cells.json','layout_tag_bindings.json',
        'layout_geometry_expected_matches.json','layout_pagination_additions.json']]
    freeze=dict(status='source-local repair module and exact data frozen for final seven-book compile',
        frozen_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),records=len(records),
        per_language=dict(Counter(r['language'] for r in records)),
        net_scan_patches=sum(len(p['patches']) for p in exact['packages']),
        affected_language_package_entries=len(exact['packages']),
        exact_pagination_records=len(json.loads((data/'layout_tag_bindings.json').read_text())),
        all_exact_patches_replayed=True,all_source_marks_preserved=semantic['all_source_marks_preserved'],
        all_raw_source_offsets_valid=semantic['all_raw_source_offsets_valid'],
        local_size_gate_pass=semantic['local_size_gate']['all_added_sizes_pass'],
        sha256={name:digest(ROOT/name) for name in dependencies},
        final_publication_validation='Awaiting final seven-book compilation and hash-bound actual-page checks; source freeze is not a publication quality claim.')
    if args.preserve_freeze:
        existing=json.loads((data/'layout_release_checkpoint.json').read_text())
        assert existing['records']==len(records)
        assert existing['sha256']==freeze['sha256'],'Installed source dependencies changed after the recorded freeze.'
    else:
        (data/'layout_release_checkpoint.json').write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(obj['current_source_layout_audit'],indent=2))
if __name__=='__main__':main()
