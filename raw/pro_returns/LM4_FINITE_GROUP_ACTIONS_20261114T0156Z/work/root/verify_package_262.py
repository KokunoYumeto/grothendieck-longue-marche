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
    assert len(claims) == len({r['id'] for r in claims}) == 262
    assert counts == {'Proved':231,'Known':3,'Refuted':25,'Open':3}
    readings = list(csv.DictReader(io.StringIO(z.read(prefix+'_readings.csv').decode())))
    assert len(readings) == 36
    bib = z.read(prefix+'_references.bib').decode()
    bib_count = len(re.findall(r'(?m)^@\w+\s*\{',bib))
    assert bib_count == 81
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
    for phrase in ['### F.25:', '**104 selected pages**', '**231 Proved, 3 Known, 25 Refuted and 3 Open**']:
        assert phrase in report, phrase
    pdf_bytes = z.read(prefix+'_paper.pdf')
    pdf_hash = digest(pdf_bytes)
    assert pdf_hash == '7b32432e84921f17f1a8635e03621a30370b4f5254a1ea5656f0b8a0b1aa65ee'
    pdf = fitz.open(stream=pdf_bytes,filetype='pdf')
    assert len(pdf) == 578
    qa = json.loads(z.read('verification/pdf_qa.json'))
    review = json.loads(z.read('verification/render_review.json'))
    build = json.loads(z.read('verification/build_artifact.json'))
    assert qa['sha256'] == review['sha256'] == build['pdf_sha256'] == pdf_hash
    for name,h in build['source_sha256'].items():assert digest(z.read(name)) == h
    assert review['actually_viewed_count'] == len(review['rendered_images']) == 104
    assert len(set(review['actually_viewed_pages'])) == 104
    for im in review['rendered_images']:
        path = str(Path(im['path']).relative_to(ROOT))
        data = z.read(path)
        assert digest(data) == im['sha256'] and len(data) == im['bytes'], path
    assert not qa['overfull_widths_pt'] and not review['issues']
    routes = {}
    for label,expected in [('f23',64),('f24',23),('f25',10)]:
        data = json.loads(z.read('verification/'+label+'_evidence_archive_routes.json'))
        assert data['all_entries_resolve'] and len(data['entries']) == expected
        for entry in data['entries']:
            raw = z.read(entry['archive_path'])
            assert len(raw) == entry['bytes'] and digest(raw) == entry['sha256']
        routes[label] = expected
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
        'render_reviewed_pages':104, 'final_review_images_hash_verified_in_archive':104,
        'f23_evidence_routes_verified':routes['f23'],
        'f24_evidence_routes_verified':routes['f24'],
        'f25_evidence_routes_verified':routes['f25'],
        'catalogue_inputs':44, 'catalogue_outputs':8, 'report_immediate_table':True}
    (ROOT/'work/root/package_262_independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
