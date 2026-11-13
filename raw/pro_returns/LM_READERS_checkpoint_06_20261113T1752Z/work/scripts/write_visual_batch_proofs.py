"""Extend the visual-repair ledger with the accepted revision512 findings.

This script records already inspected probe evidence.  It does not manufacture
visual observations or close publication issues.  Its publication references
are refreshed only from the current seven-book verifier outputs.
"""
from pathlib import Path
import csv, hashlib, json, re, shutil

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'work/visual_repair_proofs'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def copy(path, name=None):
    source = ROOT/path
    assert source.is_file(), path
    destination = OUT/(name or source.name)
    if source.resolve() != destination.resolve():
        shutil.copyfile(source, destination)
    return 'proofs/visual_repairs/'+destination.name, sha(destination)


def accepted_view(validation, language, scan):
    rows = validation.get('forms', validation.get('probes', []))
    rows = [r for r in rows if r.get('language') == language
            and r.get('variant',r.get('version',r.get('phase','after'))) != 'before'
            and ('scan' not in r or int(r['scan']) == int(scan))]
    assert rows, (language,scan,validation.keys())
    rows.sort(key=lambda r:(r.get('form',1)!=1,r.get('spare',r.get('remaining_page_height_pt',0))))
    outer = rows[0]
    if isinstance(outer.get('pages'), list):
        inner = [p for p in outer['pages'] if p.get('image') and p.get('heading',True) and p.get('opening',True)]
        assert inner
        inner.sort(key=lambda r:(r.get('form',1)!=1,r.get('remaining_page_height_pt',0)))
        return outer, inner[0]
    for key in ['tag_pages','definition_pages']:
        if key in outer:
            selected = [r for r in outer[key] if r['page']==outer['after_page']]
            assert len(selected)==1
            return outer, selected[0]
    return outer, outer


def probe_pdf(name, language, scan, outer):
    if outer.get('pdf'):
        return outer['pdf']
    if name == 'scan443_520_labels':
        stem = 'scan443_eq121' if int(scan)==443 else 'scan520_eq81'
        return f'work/layout_probes/{stem}_{language}.pdf'
    direct = {'scan441_eq117','scan449_labels','scan637_blue_note'}
    if name in direct:
        return f'work/layout_probes/{name}_{language}.pdf'
    after = {'scan408_eq44','section12','sectionII','remarque221','section565',
             'scan419_circled3','cancelled_tags','section495'}
    if name in after:
        return f'work/layout_probes/{name}_after_{language}.pdf'
    raise ValueError(('Explicit historical PDF path needed',name,language))


def extend():
    integration = ROOT/'work/data/layout_batch_integration_result.json'
    if not integration.exists():
        return
    from integrate_layout_pending import identifier
    from write_visual_repairs import publication_evidence
    manifest = json.loads((ROOT/'work/data/layout_pending_batch.json').read_text())
    issues = json.loads((ROOT/'work/data/final_visual_issue_closure.json').read_text())['findings']
    applied = json.loads((ROOT/'work/data/layout_repairs_applied.json').read_text())
    lookup = {(r['id'],r['language']):r for r in applied}
    ledger = ROOT/'work/records/VISUAL_REPAIRS.tsv'
    with ledger.open(newline='') as f:
        old_rows = list(csv.DictReader(f,delimiter='\t'))
    prior = {(r['repair_id'],r['language']):r for r in old_rows}
    inventory_path = ROOT/'work/data/visual_repair_proof_inventory.json'
    old_inventory = json.loads(inventory_path.read_text())
    added_rows = []; added_inventory = []; replaced_keys = set()
    for item in manifest['items']:
        candidate = json.loads((ROOT/item['candidate']).read_text())
        candidate_rows = candidate['records'] if isinstance(candidate,dict) else candidate
        validation = json.loads((ROOT/item['validation']).read_text())
        validation_copy, validation_sha = copy(item['validation'])
        candidate_copy, candidate_sha = copy(item['candidate'])
        for source in candidate_rows:
            ident = identifier(source,item['name']);lang = source['language'];key = ident,lang
            record = lookup[key]
            matching = [x for x in issues if ident in x.get('repair_record_ids',[])]
            assert len(matching)==1,(ident,matching)
            issue = matching[0];affected = int(issue['scan'])
            outer, view = accepted_view(validation,lang,source['scan'])
            image = view.get('image'); expected_image_hash = view.get('image_sha256')
            if not image:
                images = view.get('viewed_images',view.get('images',[]));assert images
                image = images[0]['path'];expected_image_hash = images[0].get('sha256')
            assert expected_image_hash and sha(ROOT/image)==expected_image_hash,(ident,image)
            pdf = probe_pdf(item['name'],lang,source['scan'],outer)
            pdf_path = ROOT/pdf; assert pdf_path.exists(),pdf
            tex = pdf_path.with_suffix('.tex');log = pdf_path.with_suffix('.log')
            log_text = log.read_text(errors='replace')
            gate = dict(errors=len(re.findall(r'^!',log_text,re.M)),
                        overfull_hboxes=log_text.count('Overfull \\hbox'),
                        missing_glyphs=log_text.count('Missing character:'))
            assert not any(gate.values()),(pdf,gate)
            proof_image,image_sha = copy(image,ident+'_'+lang+'.png')
            proof_tex,tex_sha = copy(tex.relative_to(ROOT).as_posix())
            proof_log,log_sha = copy(log.relative_to(ROOT).as_posix())
            before_images = issue['detected_in']['images'];assert before_images
            before = before_images[0]
            assert sha(ROOT/before['path'])==before['sha256']
            before_copy,before_sha = copy(before['path'],ident+'_before.png')
            issue_text = issue['detected_in']['observation']
            if key in prior:
                issue_text = prior[key]['before_issue']+' Later native/page-boundary review: '+issue_text
            publications = publication_evidence(lang,record['cote'],affected)
            page = view.get('page',view.get('physical_page',view.get('tag_page',view.get('heading_page',''))))
            row = dict(repair_id=ident,language=lang,cote=record['cote'],affected_scan=affected,
                source_scan=record['scan'],package=record['package'],source_path=record['source_path'],
                source_line=record['source_line'],source_byte_start=record['source_byte_start'],source_byte_end=record['source_byte_end'],
                before_issue=issue_text,exact_action=record['reason'],exact_tex_record='LAYOUT_REPAIR_DETAILS.tsv: '+ident+' / '+lang,
                probe_pdf=pdf,probe_pdf_status='historical development probe; not delivered in FINAL',probe_pdf_delivered_in_final=False,
                probe_page=page,probe_image=proof_image,probe_tex=proof_tex,probe_log=proof_log,
                probe_errors=gate['errors'],probe_overfull_hboxes=gate['overfull_hboxes'],probe_missing_glyphs=gate['missing_glyphs'],
                probe_pdf_sha256=sha(pdf_path),probe_image_sha256=image_sha,probe_tex_sha256=tex_sha,probe_log_sha256=log_sha,
                before_image=before_copy,before_image_sha256=before_sha,
                publication_evidence_json=json.dumps(publications,ensure_ascii=False,separators=(',',':')),
                proof_scope='Accepted native probe evidence supports this local change. The probe PDF is historical and excluded from FINAL; publication confirmation requires the current hash-bound full-book findings ledger.',
                finding_id=issue['id'],candidate_json=candidate_copy,candidate_sha256=candidate_sha,
                probe_validation_json=validation_copy,probe_validation_sha256=validation_sha,
                publication_closure_status=issue['status'],
                actual_probe_observation=view.get('observation',view.get('visual_observation',outer.get('observation',validation.get('observation','See the attributed actual-image observations in the probe validation JSON.')))),
                additional_before_evidence_json=json.dumps(before_images,ensure_ascii=False,separators=(',',':')),
                historical_prior_proof_json=json.dumps(prior[key],ensure_ascii=False,separators=(',',':')) if key in prior else '')
            added_rows.append(row);replaced_keys.add(key)
            added_inventory.append(dict(repair_id=ident,language=lang,original_pdf=pdf,original_image=image,
                historical_checkpoint_pdf=pdf,delivered_pdf=None,pdf_status='historical_not_delivered_in_final',
                delivered_image=proof_image,delivered_tex=proof_tex,delivered_log=proof_log,
                pdf_sha256=row['probe_pdf_sha256'],image_sha256=image_sha,tex_sha256=tex_sha,log_sha256=log_sha,
                candidate=candidate_copy,validation=validation_copy,publication_evidence=publications,
                finding_id=issue['id'],publication_closure_status=issue['status']))
    rows = [r for r in old_rows if (r['repair_id'],r['language']) not in replaced_keys]+added_rows
    assert len({(r['repair_id'],r['language']) for r in rows})==len(rows)
    keys = list(old_rows[0])
    for row in rows:
        for key in row:
            if key not in keys:keys.append(key)
    with ledger.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=keys,delimiter='\t');writer.writeheader();writer.writerows(rows)
    inventory = [r for r in old_inventory if (r['repair_id'],r['language']) not in replaced_keys]+added_inventory
    inventory_path.write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    print('Reviewed batch proof ledger:',len(added_rows),'source/language rows;',len(rows),'total visual-repair rows')


if __name__ == '__main__':
    extend()
