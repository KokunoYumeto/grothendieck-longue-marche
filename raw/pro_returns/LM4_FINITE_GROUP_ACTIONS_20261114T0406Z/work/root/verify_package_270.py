#!/usr/bin/env python3
"""Independent ZIP member, registry, certificate-route and PDF audit."""
from pathlib import Path
import collections
import csv
import hashlib
import io
import json
import re
import zipfile
import fitz

ROOT = Path(__file__).resolve().parents[2]
archive = ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS.zip'
prefix = 'LM4_FINITE_GROUP_ACTIONS'
digest = lambda data:hashlib.sha256(data).hexdigest()

with zipfile.ZipFile(archive) as z:
    names = z.namelist()
    assert len(names) == len(set(names))
    assert z.testzip() is None
    manifest = list(csv.DictReader(io.StringIO(z.read('manifest.csv').decode())))
    assert set(names) == {'manifest.csv'} | {r['path'] for r in manifest}
    for entry in manifest:
        data = z.read(entry['path'])
        assert len(data) == int(entry['bytes']), entry['path']
        assert digest(data) == entry['sha256'], entry['path']
    claims = list(csv.DictReader(io.StringIO(z.read(prefix+'_results.csv').decode())))
    counts = dict(collections.Counter(r['status'] for r in claims))
    assert len(claims) == len({r['id'] for r in claims}) == 270
    assert counts == {'Proved':239,'Known':3,'Refuted':25,'Open':3}
    readings = list(csv.DictReader(io.StringIO(z.read(prefix+'_readings.csv').decode())))
    assert len(readings) == 36
    bib = z.read(prefix+'_references.bib').decode()
    bib_count = len(re.findall(r'(?m)^@\w+\s*\{',bib))
    assert bib_count == 88
    report = z.read(prefix+'_report.md').decode()
    lines = report.splitlines()
    assert lines[0] == 'INCOMPLETE'
    assert lines[1] == '' and lines[2].startswith('| Obligation |')
    table = []
    for line in lines[4:]:
        if not line.startswith('|'):break
        table.append(line)
    assert len(table) == 39
    assert 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.' in report
    for phrase in ['### C.92:', '### F.29:', '## Continuation through F.31:', '**96 selected pages**', 'Accepted original transporter continuation']:
        assert phrase in report, phrase
    assert 'FINAL_VERIFICATION_270_PENDING' not in report
    assert all(r['status']=='Proved' for r in claims if r['id'] in ('C.92','F.27','F.28','F.29','F.30','F.31'))
    pdf_bytes = z.read(prefix+'_paper.pdf')
    pdf_hash = digest(pdf_bytes)
    assert pdf_hash == '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
    pdf = fitz.open(stream=pdf_bytes,filetype='pdf')
    assert len(pdf) == 619
    qa = json.loads(z.read('verification/pdf_qa.json'))
    review = json.loads(z.read('verification/render_review.json'))
    build = json.loads(z.read('verification/build_artifact.json'))
    assert qa['sha256'] == review['sha256'] == build['pdf_sha256'] == pdf_hash
    for name,h in build['source_sha256'].items():assert digest(z.read(name)) == h
    assert review['actually_viewed_count'] == len(review['rendered_images']) == 96
    assert len(set(review['actually_viewed_pages'])) == 96
    for im in review['rendered_images']:
        path = str(Path(im['path']).relative_to(ROOT))
        data = z.read(path)
        assert digest(data) == im['sha256'] and len(data) == im['bytes'], path
    assert not qa['overfull_widths_pt'] and not review['issues']
    assert len(review['root_images_opened_this_final_review']) == 4
    assert len(review['peer_images_opened_this_final_review']) == 10
    assert len(review['byte_identical_prior_review_images']) == 82
    prior = review['prior_pdf']
    prior_bytes = z.read(prior['path'])
    assert len(prior_bytes) == prior['bytes'] and digest(prior_bytes) == prior['sha256']
    prior_doc = fitz.open(stream=prior_bytes, filetype='pdf')
    assert len(prior_doc) == 611
    current_images = {x['page']:x for x in review['rendered_images']}
    for page in review['byte_identical_prior_review_images']:
        reproduced = prior_doc[page-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).tobytes('png')
        entry = current_images[page]
        current_path = str(Path(entry['path']).relative_to(ROOT))
        assert reproduced == z.read(current_path), page
    transporter = json.loads(z.read('work/root/actual_transporter_acceptance_269.json'))
    assert transporter['status'] == 'PASS_ROOT_AND_PEER'
    assert transporter['named_checks_each'] == 24
    assert transporter['raw_output_and_stdout_byte_identical_each']
    for gate in review['current_document_gates']:
        raw = z.read(gate['path'])
        assert len(raw) == gate['bytes'] and digest(raw) == gate['sha256']
    assert 'FINAL_VERIFICATION_268_PENDING' not in report
    routes = {}
    for label,expected in [('f23',64),('f24',23),('f25',10),('f26',27),('f27',32),('f28',31),('f29',63),('f30',37),('f31',54)]:
        data = json.loads(z.read('verification/'+label+'_evidence_archive_routes.json'))
        assert data['all_entries_resolve'] and len(data['entries']) == expected
        for entry in data['entries']:
            raw = z.read(entry['archive_path'])
            assert len(raw) == entry['bytes'] and digest(raw) == entry['sha256']
        routes[label] = expected
    f31_gate = json.loads(z.read('work/root/final_new_claim_acceptance_270.json'))
    assert f31_gate['status'] == 'PASS_ROOT_AND_PEER' and f31_gate['manifest_entry_count'] == 54
    assert f31_gate['root_independent_checks'] == f31_gate['peer_independent_checks'] == 1603
    for gate_name in ['actual_class_two_acceptance_270.json','filled_carriers_acceptance_270.json','norm_branch_acceptance_270.json']:
        gate = json.loads(z.read('work/root/'+gate_name))
        assert gate['status'] == 'PASS_ROOT_AND_PEER' and not gate['numbered_claim_added']
    for basename in ['actual_transporter_class_two','actual_odd_local_midpoint']:
        for suffix in ['.py','_output.json','_stdout.txt']:
            a='code/part_d_attack/'+basename+suffix
            b='work/part_d_attack/code/'+basename+suffix
            assert z.read(a) == z.read(b), a
    assert sum(routes.values()) == 341
    historical_routes=json.loads(z.read('work/root/checkpoint_270_historical_binding_routes.json'))
    assert historical_routes['status']=='PASS_EXACT_HISTORICAL_BYTES'
    assert len(historical_routes['entries'])==1
    for entry in historical_routes['entries']:
        raw=z.read(entry['archive_path'])
        assert len(raw)==entry['bytes'] and digest(raw)==entry['sha256']
        assert entry['sha256']=='6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
    required = json.loads(z.read('code/part_b/low_complexity_catalogue_required_paths.json'))
    assert len(required['required_for_assembler']) == 44
    assert len(required['generated_outputs']) == 8
    assert all(p in names for p in required['required_for_assembler'])
    assert all(p in names for p in required['generated_outputs'])
    summary = json.loads(z.read('verification/package_manifest_summary.json'))
    assert summary['catalogue_outputs_byte_identical'] and not summary['missing_catalogue_inputs']
    result = {
        'zip':str(archive), 'zip_sha256':digest(archive.read_bytes()),
        'zip_bytes':archive.stat().st_size, 'entries':len(names),
        'manifest_entries_size_and_hash_checked':len(manifest), 'crc_error':None,
        'claims':len(claims), 'statuses':counts, 'obligations':len(table),
        'readings':len(readings), 'bibliography_entries':bib_count,
        'pdf_pages':len(pdf), 'pdf_sha256':pdf_hash,
        'render_reviewed_pages':96, 'final_review_images_hash_verified_in_archive':96,
        'f23_evidence_routes_verified':routes['f23'],
        'f24_evidence_routes_verified':routes['f24'],
        'f25_evidence_routes_verified':routes['f25'],
        'f26_evidence_routes_verified':routes['f26'],
        'f27_evidence_routes_verified':routes['f27'],
        'f28_evidence_routes_verified':routes['f28'],
        'f29_evidence_routes_verified':routes['f29'],
        'f30_evidence_routes_verified':routes['f30'],
        'f31_evidence_routes_verified':routes['f31'],
        'total_evidence_routes_verified':sum(routes.values()),
        'catalogue_inputs':44, 'catalogue_outputs':8, 'report_immediate_table':True}
    (ROOT/'work/root/package_270_independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
