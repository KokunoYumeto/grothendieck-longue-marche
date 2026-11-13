"""Prepare current-PDF evidence for the final visual-finding ledger.

No command grants visual clearance. ``prepare`` reads immutable sources only;
``queue --final`` is used after the complete build is declared stable. Reviewers
view the generated pages, make native crops, and supply their own observations.
``validate`` checks those observations without editing the central finding ledger.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work/data'
BUILD = ROOT / 'work/build'
LEDGER = DATA / 'final_visual_issue_closure.json'
INVENTORY = DATA / 'final_native_closure_inventory.json'
QUEUES = DATA / 'final_native_closure_queues'
EVIDENCE = ROOT / 'work/visual_repair_proofs/native_final_closure'
BOOKS = {
    'LM_FR_diplomatique': ('fr', 0),
    'LM_FR_corrige_apparat': ('fr', 1),
    'LM_FR_texte_de_lecture': ('fr', 2),
    'LM_EN_corrected_apparatus': ('en', 1),
    'LM_EN_reading': ('en', 2),
    'LM_FR_master_annotated': ('fr', 1),
    'LM_EN_master_annotated': ('en', 1),
}
GEOMETRY_IDS = {
    'VIS-140-3-441-117', 'VIS-140-3-449-137-138',
    'VIS-140-3-443-121', 'VIS-140-3-520-81',
    'VIS-140-3-637-BLUE-NOTE', 'VIS-140-3-055-3',
    'VIS-140-3-408-44', 'VIS-140-3-649-59',
    'VIS-140-4-065-EPILABELS', 'VIS-140-4-75-E144-MASK',
}


def sha_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def relative(path):
    return path.resolve().relative_to(ROOT).as_posix()


def resolve(path):
    value = Path(path)
    value = value if value.is_absolute() else ROOT / value
    value.resolve().relative_to(ROOT)
    return value


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def definitions(findings):
    keys = ('id', 'cote', 'scan', 'equations', 'affected_books')
    return [{key: row.get(key) for key in keys} for row in findings]


def definition_hash(findings):
    return sha_bytes(json.dumps(definitions(findings), sort_keys=True,
                               ensure_ascii=False).encode())


def inspection_kind(row):
    if row['id'] in GEOMETRY_IDS:
        return 'geometry', 8, 'Inspect the full diagram, then the repaired label or route at native8x or higher; verify visible clearance, unchanged endpoints, readable uncertainty and neighboring labels.'
    if 'CANCELLEDTAG' in row['id']:
        return 'cancelled-tag', 3, 'Inspect the complete source-local cancelled tag location at native3x or higher; generated empty parentheses must be absent and any surviving uncertainty anchor must remain visible and linked.'
    if row['id'] == 'VIS-140-2-252-OPTIONS':
        return 'literal-options', 3, 'Inspect both affected diagram rows at native3x or higher; option syntax must not print as cell content, and objects, arrows and labels must remain intact.'
    return 'heading-or-tag-binding', 3, 'Inspect the source heading or introduction with its first substantive opening block at native3x or higher; check both page boundaries when needed. A generated rule must stay with its heading and first entry. Long following text must remain breakable.'


def source_index():
    manifest = read_json(ROOT / 'sources/en/MANIFEST.json')
    out = {}
    for unit in manifest['units']:
        for scan in unit['scans']:
            key = (unit['cote'], int(scan))
            assert key not in out or out[key] == unit['package'], key
            out[key] = unit['package']
    return out


def raw_anchor(package, language, scan):
    if language == 'fr':
        path = ROOT / 'sources/fr/texts' / (package + '.tex')
    else:
        path = ROOT / 'sources/en/packages' / (package + '_en.tex')
    text = path.read_text()
    matches = list(re.finditer(r'\\scanpage\{(\d+)\}', text))
    matched = [(i, m) for i, m in enumerate(matches) if int(m[1]) == scan]
    assert len(matched) == 1, (relative(path), scan, len(matched))
    i, match = matched[0]
    end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
    return dict(source_path=relative(path), source_file_sha256=sha_file(path),
                source_line=text.count('\n', 0, match.start()) + 1,
                source_scan_sha256=sha_bytes(text[match.start():end].encode()))


def prepare():
    ledger = read_json(LEDGER)
    index = source_index()
    rows = []
    counts = collections.Counter()
    for finding in ledger['findings']:
        cote, scan = finding['cote'], int(finding['scan'])
        package = index[(cote, scan)]
        kind, scale, instruction = inspection_kind(finding)
        anchors = {lang: raw_anchor(package, lang, scan) for lang in ('fr', 'en')}
        counts.update(finding['affected_books'])
        rows.append(dict(id=finding['id'], cote=cote, scan=scan, package=package,
                         equations=finding.get('equations'),
                         affected_books=finding['affected_books'],
                         inspection_kind=kind, minimum_native_scale=scale,
                         required_inspection=instruction, source_anchors=anchors,
                         historical_finding=finding.get('detected_in', {}),
                         status='PENDING_FINAL_BUILD'))
    result = dict(schema='final-native-closure-inventory-v1',
                  status='SOURCE_QUALIFIED_PENDING_FINAL_BUILD', generated_at_utc=now(),
                  ledger=relative(LEDGER), ledger_sha256=sha_file(LEDGER),
                  finding_definition_sha256=definition_hash(ledger['findings']),
                  observations_generated_by_script=False,
                  findings=len(rows), required_book_confirmations=sum(counts.values()),
                  per_book_counts=dict(counts), items=rows)
    write_json(INVENTORY, result)
    print(json.dumps({key: result[key] for key in ('status', 'findings',
          'required_book_confirmations', 'per_book_counts')}, ensure_ascii=False))


def current_queue(path):
    queue = read_json(path)
    reader = queue['reader']
    for name, expected in ((reader + '.pdf', queue['pdf_sha256']),
                           (reader + '.tex', queue['tex_sha256']),
                           (reader + '.lm-scans.tsv', queue['scan_map_sha256']),
                           (queue['language'] + '_source_marks.json', queue['source_marks_sha256'])):
        assert sha_file(BUILD / name) == expected, 'Current build changed: ' + name
    current = read_json(LEDGER)
    assert definition_hash(current['findings']) == queue['finding_definition_sha256'], 'Finding definitions changed; regenerate the inventory and queue.'
    for row in queue['items']:
        assert sha_file(ROOT / row['source_path']) == row['source_file_sha256'], row['source_path']
    return queue


def queue_book(reader, final):
    if not final:
        raise SystemExit('queue requires --final after the complete build is declared stable.')
    import pymupdf as fitz
    inventory = read_json(INVENTORY)
    ledger = read_json(LEDGER)
    assert definition_hash(ledger['findings']) == inventory['finding_definition_sha256'], 'Rerun prepare: finding definitions changed.'
    language, form = BOOKS[reader]
    path = BUILD / (reader + '.pdf')
    tex = path.with_suffix('.tex')
    scanmap = path.with_suffix('.lm-scans.tsv')
    markfile = BUILD / (language + '_source_marks.json')
    pdf_hash = sha_file(path)
    tex_text = tex.read_text()
    header = re.search(r'^% COMMON MASTER BODY SHA256 ([0-9a-f]{64})\n', tex_text, re.M)
    assert header, 'Missing common-body hash'
    body = tex_text[header.end():tex_text.rfind(r'\end{document}')]
    assert sha_bytes(body.encode()) == header[1], 'Common-body hash mismatch'
    with scanmap.open() as stream:
        scans = {(r['cote'], int(r['scan'])): [int(p) for p in r['physical_pages'].split(',') if p]
                 for r in csv.DictReader(stream, delimiter='\t')}
    marks = read_json(markfile)
    final_rows = {f['id']: f for f in ledger['findings']}
    directory = EVIDENCE / pdf_hash[:16] / reader
    directory.mkdir(parents=True, exist_ok=True)
    items, page_numbers = [], set()
    with fitz.open(path) as pdf:
        for spec in inventory['items']:
            if reader not in spec['affected_books']:
                continue
            anchor = spec['source_anchors'][language]
            assert sha_file(ROOT / anchor['source_path']) == anchor['source_file_sha256']
            matches = [m for m in marks if m['kind'] == 'scanpage' and
                       m['cote'] == spec['cote'] and int(m['scan']) == spec['scan'] and
                       m['package'] == spec['package']]
            assert len(matches) == 1, (spec['id'], len(matches))
            source_pages = scans[(spec['cote'], spec['scan'])]
            # The next page may carry apparatus or an opening block. The previous
            # page is included for an introduced heading at a scan boundary.
            candidates = sorted({q for p in source_pages for q in (p - 1, p, p + 1)
                                 if 1 <= q <= len(pdf)})
            page_numbers.update(candidates)
            items.append(dict(id=spec['id'], reader=reader, cote=spec['cote'],
                              scan=spec['scan'], package=spec['package'],
                              equations=spec['equations'], **anchor,
                              source_id=matches[0]['id'], source_scan_pages=source_pages,
                              candidate_pages=candidates, inspection_kind=spec['inspection_kind'],
                              minimum_native_scale=spec['minimum_native_scale'],
                              required_inspection=spec['required_inspection'],
                              repair_record_ids=final_rows[spec['id']].get('repair_record_ids', []),
                              historical_finding=spec['historical_finding'],
                              status='PENDING_ACTUAL_VISUAL_REVIEW'))
        images = []
        for number in sorted(page_numbers):
            page = pdf[number - 1]
            image_path = directory / ('page_' + str(number).zfill(4) + '_900.png')
            scale = 900 / page.rect.width
            page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False).save(image_path)
            images.append(dict(path=relative(image_path), sha256=sha_file(image_path),
                               page=number, scale=scale, basis='Full page at900px',
                               pdf_sha256=pdf_hash))
        result = dict(schema='final-native-closure-queue-v1', status='PENDING_ACTUAL_VISUAL_REVIEW',
                      generated_at_utc=now(), reader=reader, language=language, form=form,
                      pdf_sha256=pdf_hash, tex_sha256=sha_file(tex), pages=len(pdf),
                      actual_body_sha256=header[1], scan_map_sha256=sha_file(scanmap),
                      source_marks_sha256=sha_file(markfile),
                      finding_definition_sha256=inventory['finding_definition_sha256'],
                      evidence_directory=relative(directory), observations_generated_by_script=False,
                      required_findings=len(items), items=items, evidence_candidates=images,
                      observation_schema=dict(id='Exact finding ID', reader=reader,
                          pdf_sha256=pdf_hash, status='RESOLVED or ISSUE',
                          reviewer='Actual reviewer', observation='Specific actual visual observation',
                          images=[dict(path='Viewed current full/native image', sha256='Image SHA256')]))
    assert sha_file(path) == pdf_hash, 'PDF changed during queue rendering'
    output = QUEUES / (reader + '.json')
    write_json(output, result)
    current_queue(output)
    print(json.dumps(dict(queue=relative(output), findings=len(items), rendered_pages=len(images),
                          pdf_sha256=pdf_hash), ensure_ascii=False))


def crop(args):
    import pymupdf as fitz
    queue_path = resolve(args.queue)
    queue = current_queue(queue_path)
    item = next(r for r in queue['items'] if r['id'] == args.finding)
    assert args.page in item['candidate_pages'], 'Page is not in the source-qualified candidate neighborhood'
    with fitz.open(BUILD / (queue['reader'] + '.pdf')) as pdf:
        page = pdf[args.page - 1]
        clip = fitz.Rect(args.clip) if args.clip else page.rect
        assert clip.is_valid and not clip.is_empty and page.rect.contains(clip), 'Invalid page crop'
        suffix = sha_bytes(json.dumps([args.page, list(clip), args.scale]).encode())[:10]
        filename = item['id'] + '_p' + str(args.page).zfill(4) + '_' + suffix + '.png'
        image_path = ROOT / queue['evidence_directory'] / filename
        page.get_pixmap(matrix=fitz.Matrix(args.scale, args.scale), clip=clip, alpha=False).save(image_path)
    evidence = dict(path=relative(image_path), sha256=sha_file(image_path), page=args.page,
                    clip=list(clip), scale=args.scale, basis='Native PDF crop',
                    finding_id=args.finding, pdf_sha256=queue['pdf_sha256'])
    current_queue(queue_path)
    queue['evidence_candidates'] = [r for r in queue['evidence_candidates'] if r['path'] != evidence['path']] + [evidence]
    write_json(queue_path, queue)
    print(json.dumps(evidence, ensure_ascii=False))


def validate(args):
    queue_path = resolve(args.queue)
    queue = current_queue(queue_path)
    raw = read_json(resolve(args.observations))
    observations = raw['observations'] if isinstance(raw, dict) else raw
    ids = [r['id'] for r in observations]
    expected = {r['id'] for r in queue['items']}
    assert len(ids) == len(set(ids)), 'Duplicate finding observations'
    assert set(ids) <= expected, 'Unknown finding observations'
    if not args.partial:
        assert set(ids) == expected, 'Missing finding observations: ' + ', '.join(sorted(expected - set(ids)))
    candidates = {r['path']: r for r in queue['evidence_candidates']}
    specs = {r['id']: r for r in queue['items']}
    output = []
    for supplied in observations:
        row = dict(supplied)
        spec = specs[row['id']]
        assert row.get('reader') == queue['reader'] and row.get('pdf_sha256') == queue['pdf_sha256'], row['id']
        assert row.get('status') in ('RESOLVED', 'ISSUE'), row['id']
        assert row.get('reviewer') and len(row.get('observation', '').strip()) >= 40, row['id']
        images = row.get('images', [])
        assert images, 'No actually viewed image for ' + row['id']
        checked = []
        for image in images:
            info = candidates[image['path']]
            assert info['pdf_sha256'] == queue['pdf_sha256']
            assert info['sha256'] == image['sha256'] == sha_file(ROOT / image['path'])
            assert info['page'] in spec['candidate_pages']
            assert not info.get('finding_id') or info['finding_id'] == row['id']
            checked.append(info)
        assert any(r['scale'] >= spec['minimum_native_scale'] for r in checked), 'Native enlargement missing for ' + row['id']
        row.update(tex_sha256=queue['tex_sha256'], source_id=spec['source_id'],
                   source_path=spec['source_path'], source_file_sha256=spec['source_file_sha256'],
                   source_line=spec['source_line'], source_scan_sha256=spec['source_scan_sha256'],
                   cote=spec['cote'], scan=spec['scan'], package=spec['package'],
                   pages=sorted({r['page'] for r in checked}), images=checked)
        output.append(row)
    result = dict(schema='final-native-observations-v1',
                  status='PARTIAL_VALIDATED' if args.partial else 'VALIDATED_OBSERVATIONS',
                  reader=queue['reader'], pdf_sha256=queue['pdf_sha256'],
                  tex_sha256=queue['tex_sha256'], generated_at_utc=now(),
                  observations_generated_by_script=False,
                  queue=relative(queue_path), queue_sha256=sha_file(queue_path),
                  supplied_observations=relative(resolve(args.observations)),
                  supplied_observations_sha256=sha_file(resolve(args.observations)),
                  required_findings=len(expected), observed_findings=len(output),
                  resolved=sum(r['status'] == 'RESOLVED' for r in output),
                  issues=sum(r['status'] == 'ISSUE' for r in output), observations=output)
    destination = DATA / 'final_native_closure_validated' / (queue['reader'] + '.json')
    write_json(destination, result)
    print(json.dumps({key: result[key] for key in ('status', 'reader', 'required_findings',
          'observed_findings', 'resolved', 'issues')}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('prepare')
    q = sub.add_parser('queue')
    q.add_argument('--reader', required=True, choices=BOOKS)
    q.add_argument('--final', action='store_true')
    c = sub.add_parser('crop')
    c.add_argument('--queue', required=True)
    c.add_argument('--finding', required=True)
    c.add_argument('--page', type=int, required=True)
    c.add_argument('--clip', type=float, nargs=4)
    c.add_argument('--scale', type=float, default=8)
    v = sub.add_parser('validate')
    v.add_argument('--queue', required=True)
    v.add_argument('--observations', required=True)
    v.add_argument('--partial', action='store_true')
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare()
    elif args.command == 'queue':
        queue_book(args.reader, args.final)
    elif args.command == 'crop':
        crop(args)
    elif args.command == 'validate':
        validate(args)


if __name__ == '__main__':
    main()
