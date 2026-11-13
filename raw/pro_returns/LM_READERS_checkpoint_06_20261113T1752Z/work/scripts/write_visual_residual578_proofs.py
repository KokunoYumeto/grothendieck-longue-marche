"""Curate the separately accepted revision578 pagination evidence.

The original revision512 batch remains unchanged.  These records cover two
paired literal source bindings and one generated range-heading exception.
They copy attributed probe observations and never create publication closure.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work/data'
BATCH = 'revision578_residual_pagination'
FINDINGS = {
    'scan573_tag76': ('VIS-140-2-573-76', 'work/data/scan573_tag76_root_merge_finding.json'),
    'scan695_tag15': ('VIS-140-3-695-15', 'work/data/scan695_tag15_root_merge_finding.json'),
    'range134_heading': ('VIS-140-4-134-RANGEHEADING', 'work/data/range134_heading_root_merge_finding.json'),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def selected_after_view(name, validation, language):
    """Select an explicitly accepted after view, never the before control."""
    assert validation['status'] == 'PASS'
    if name == 'range134_heading':
        jobs = [r for r in validation['proofs']
                if r['language'] == language and r['variant'] == 'after']
        assert len(jobs) == 1
        job = jobs[0]
        fixtures = [r for r in job['fixtures']
                    if r['form'] == 1 and r['spare_points'] == 400]
        assert len(fixtures) == 1
        view = fixtures[0]
        assert view['status'] == 'PASS' and view['reviewer']
        assert view['heading_with_first_complete_source_item']
        assert len(view['images']) == 1
        return job, view, view['images'][0]
    jobs = [r for r in validation['forms']
            if r['language'] == language and r['form'] == 1]
    assert len(jobs) == 1
    job = jobs[0]
    assert job['status'] == 'PASS' and job['reviewer']
    path_key = ('curved_picture_paths_on_tag_page' if name == 'scan573_tag76'
                else 'path_objects_on_tag_page')
    after = [r for r in job['images'] if r.get(path_key, 0) > 0]
    before = [r for r in job['images'] if r.get(path_key) == 0]
    assert len(after) == len(before) == 1
    assert after[0]['page'] == 4 and before[0]['page'] == 1
    return job, job, after[0]


def referenced_probe_paths(value):
    """Retain evidence files; their own status records explain their scope."""
    if isinstance(value, dict):
        for child in value.values():
            yield from referenced_probe_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from referenced_probe_paths(child)
    elif isinstance(value, str) and value.startswith('work/layout_probes/'):
        path = ROOT / value
        if path.is_file() and path.suffix in ('.png', '.pdf', '.tex', '.log', '.json'):
            yield value


def separate_closure_inventory(item, candidate):
    """Locate additive witnesses without changing the original36 native scope."""
    generated = item['stage'] == 'generated'
    path = DATA / ('generated_heading_known_witnesses.json' if generated
                   else 'pagination_known_extensions.json')
    inventory = json.loads(path.read_text())
    if generated:
        witnesses = [r for r in inventory['witnesses']
                     if r['package'] == candidate['package']
                     and r['cote'] == candidate['cote']
                     and int(r['scan']) == int(candidate['scan'])
                     and r.get('discovered_revision') == '578']
        assert len(witnesses) == 3
    else:
        ids = {r['id'] for r in candidate}
        witnesses = [r for r in inventory['primary_witnesses'] if r['binding_id'] in ids]
        assert len(witnesses) == (2 if item['name'] == 'scan573_tag76' else 1)
    return dict(
        inventory=path.relative_to(ROOT).as_posix(), inventory_sha256=sha(path),
        witness_ids=[r['id'] for r in witnesses],
        required_final_gate=('work/data/generated_heading_audit_final.json' if generated
                             else 'work/data/pagination_verification_final.json'),
        publication_status='REFER_TO_SEPARATE_CANONICAL_GATE',
        original36_native_finding_scope_changed=False)


def extend_revision578():
    integration_path = DATA / 'layout_residual_revision578_integration_result.json'
    if not integration_path.exists():
        return
    from write_visual_batch_proofs import copy
    from write_visual_repairs import publication_evidence

    manifest_path = DATA / 'layout_residual_batch_revision578.json'
    manifest = json.loads(manifest_path.read_text())
    integration = json.loads(integration_path.read_text())
    assert integration['manifest_sha256'] == sha(manifest_path)
    assert integration['actual_records'] >= 582
    applied = {(r['id'], r['language']): r for r in json.loads(
        (DATA / 'layout_repairs_applied.json').read_text())}
    ledger = ROOT / 'work/records/VISUAL_REPAIRS.tsv'
    with ledger.open(newline='') as stream:
        prior_rows = list(csv.DictReader(stream, delimiter='\t'))
    inventory_path = DATA / 'visual_repair_proof_inventory.json'
    prior_inventory = json.loads(inventory_path.read_text())
    rows, inventory = [], []
    for item in manifest['items']:
        assert item['name'] in FINDINGS
        for field in ('candidate', 'validation'):
            assert sha(ROOT / item[field]) == item[field + '_sha256']
        candidate = json.loads((ROOT / item['candidate']).read_text())
        validation = json.loads((ROOT / item['validation']).read_text())
        issue_id, issue_path = FINDINGS[item['name']]
        issue = json.loads((ROOT / issue_path).read_text())
        assert issue['id'] == issue_id
        closure = separate_closure_inventory(item, candidate)
        candidate_copy, candidate_sha = copy(item['candidate'])
        validation_copy, validation_sha = copy(item['validation'])
        generated = item['stage'] == 'generated'
        sources = candidate['source_qualification'] if generated else candidate
        for source in sources:
            language = source['language']
            ident = candidate['id'] if generated else source['id']
            record = source if generated else applied[(ident, language)]
            job, view, image = selected_after_view(item['name'], validation, language)
            assert sha(ROOT / image['path']) == image['sha256']
            pdf = ROOT / job['pdf']
            assert sha(pdf) == job['pdf_sha256']
            tex, log = pdf.with_suffix('.tex'), pdf.with_suffix('.log')
            log_text = log.read_text(errors='replace')
            gate = dict(errors=len(re.findall(r'^!', log_text, re.M)),
                        overfull_hboxes=log_text.count('Overfull \\hbox'),
                        missing_glyphs=log_text.count('Missing character:'))
            assert not any(gate.values()), (pdf, gate)
            proof_image, image_sha = copy(image['path'], ident + '_' + language + '.png')
            proof_tex, tex_sha = copy(tex.relative_to(ROOT).as_posix())
            proof_log, log_sha = copy(log.relative_to(ROOT).as_posix())
            before = issue['detected_in']['images'][0]
            assert sha(ROOT / before['path']) == before['sha256']
            before_copy, before_sha = copy(before['path'], ident + '_before.png')
            cote, scan = issue['cote'], int(issue['scan'])
            publications = publication_evidence(language, cote, scan)
            if generated:
                publications = [r for r in publications if r['file'].removesuffix('.pdf')
                                in issue['affected_books']]
            basis = 'generated range-heading formatting' if generated else 'source-local pagination'
            record_ref = ('work/data/generated_heading_repairs.json: ' + ident if generated
                          else 'LAYOUT_REPAIR_DETAILS.tsv: ' + ident + ' / ' + language)
            row = dict(
                repair_id=ident, language=language, cote=cote, affected_scan=scan,
                source_scan=scan if generated else record['scan'],
                package=issue['package'], source_path=record['source_path'].removeprefix('sources/'),
                source_line=record['source_line'], source_byte_start=record['source_byte_start'],
                source_byte_end=record['source_byte_end'], before_issue=issue['detected_in']['observation'],
                exact_action=candidate['reason'] if generated else record['reason'],
                exact_tex_record=record_ref, probe_pdf=job['pdf'],
                probe_pdf_status='historical development probe; not delivered in FINAL',
                probe_pdf_delivered_in_final=False, probe_page=image['page'],
                probe_image=proof_image, probe_tex=proof_tex, probe_log=proof_log,
                probe_errors=gate['errors'], probe_overfull_hboxes=gate['overfull_hboxes'],
                probe_missing_glyphs=gate['missing_glyphs'], probe_pdf_sha256=sha(pdf),
                probe_image_sha256=image_sha, probe_tex_sha256=tex_sha, probe_log_sha256=log_sha,
                before_image=before_copy, before_image_sha256=before_sha,
                publication_evidence_json=json.dumps(publications, ensure_ascii=False, separators=(',', ':')),
                proof_scope='Accepted revision578 local probe, recorded separately from the original29 candidate files. Publication closure requires current full-book actual observations; probe PDFs remain historical and excluded from FINAL.',
                finding_id=issue['id'], candidate_json=candidate_copy, candidate_sha256=candidate_sha,
                probe_validation_json=validation_copy, probe_validation_sha256=validation_sha,
                publication_closure_status=closure['publication_status'],
                publication_closure_inventory_json=json.dumps(closure, ensure_ascii=False, separators=(',', ':')),
                original_finding_record=issue_path, original_finding_sha256=sha(ROOT / issue_path),
                actual_probe_observation=view['observation'],
                actual_probe_reviewer=view['reviewer'],
                additional_before_evidence_json=json.dumps(issue['detected_in']['images'], ensure_ascii=False, separators=(',', ':')),
                evidence_batch=BATCH, record_basis=basis, manuscript_reading_changed=False)
            rows.append(row)
            inventory.append(dict(
                repair_id=ident, language=language, original_pdf=job['pdf'], original_image=image['path'],
                historical_checkpoint_pdf=job['pdf'], delivered_pdf=None,
                pdf_status='historical_not_delivered_in_final', delivered_image=proof_image,
                delivered_tex=proof_tex, delivered_log=proof_log, pdf_sha256=sha(pdf),
                image_sha256=image_sha, tex_sha256=tex_sha, log_sha256=log_sha,
                candidate=candidate_copy, validation=validation_copy,
                publication_evidence=publications, finding_id=issue['id'],
                publication_closure_status=closure['publication_status'],
                publication_closure_inventory=closure,
                original_finding_record=issue_path, original_finding_sha256=sha(ROOT / issue_path),
                evidence_batch=BATCH, record_basis=basis))
        for path in sorted(set(referenced_probe_paths(validation))):
            copy(path)
            if Path(path).suffix == '.pdf':
                for suffix in ('.tex', '.log'):
                    extra = Path(path).with_suffix(suffix).as_posix()
                    if (ROOT / extra).is_file():
                        copy(extra)
    assert len(rows) == 6
    keys = {(r['repair_id'], r['language']) for r in rows}
    combined = [r for r in prior_rows if (r['repair_id'], r['language']) not in keys] + rows
    fields = list(prior_rows[0])
    for row in combined:
        for field in row:
            if field not in fields:
                fields.append(field)
    assert len({(r['repair_id'], r['language']) for r in combined}) == len(combined)
    with ledger.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(combined)
    all_inventory = [r for r in prior_inventory if (r['repair_id'], r['language']) not in keys] + inventory
    inventory_path.write_text(json.dumps(all_inventory, ensure_ascii=False, indent=2) + '\n')
    print('Revision578 residual proof ledger:4 paired source rows +2 generated-formatting rows;',
          len(combined), 'total visual-evidence rows')


if __name__ == '__main__':
    extend_revision578()
