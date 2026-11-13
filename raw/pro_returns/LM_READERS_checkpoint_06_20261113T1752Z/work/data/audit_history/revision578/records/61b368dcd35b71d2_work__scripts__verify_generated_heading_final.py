#!/usr/bin/env python3
"""Prepare and finalize actual, hash-bound generated-heading review.

Preparation is a localization/rendering aid, never an inspection. Finalization
requires reviewer-supplied observations for every primary candidate and every
historically confirmed witness. Master duplicates require current all-page RGB
identity with the actually reviewed apparatus book.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import fitz

from audit_equation_pagination import BOOKS, ignored, lines, page_scans, sha
from audit_generated_heading_endings import HEADINGS, canonical
from verify_pagination_final import (COMPARISONS, MASTER_SOURCE, now, observations,
                                     read, rel, render_full, write)

ROOT = Path(__file__).resolve().parents[2]
SCANNER = 'work/scripts/audit_generated_heading_endings.py'
WITNESSES = 'work/data/generated_heading_known_witnesses.json'
INVENTORY = 'work/data/generated_heading_final_candidates.json'
QUEUE = 'work/data/generated_heading_verification_queue.json'
OUTPUT = 'work/data/generated_heading_audit_final.json'
PROOFS = 'work/visual_repair_proofs/generated_heading_final'
ORIGINAL_WITNESSES = 'work/data/generated_heading_known_witnesses_revision512.json'


def reference(path, **extra):
    return dict(path=path, sha256=sha(ROOT / path), **extra)


def verify_reference(record):
    path = ROOT / record.get('path', '__missing__')
    return path.is_file() and sha(path) == record.get('sha256')


def frozen_witnesses(path):
    data = read(path)
    rows = data.get('witnesses', [])
    ids = [row.get('id') for row in rows]
    count = data.get('count')
    if (data.get('schema') != 'generated-heading-known-witnesses-v1' or
            data.get('status') != 'FROZEN_ACTUAL_BEFORE_WITNESSES' or
            not isinstance(count, int) or isinstance(count, bool) or count <= 0 or len(rows) != count or
            len(set(ids)) != count or any(not key for key in ids)):
        raise ValueError('The frozen inventory count must match its nonempty unique actual historical witnesses.')
    original_reference = data.get('original_inventory', {})
    if original_reference.get('path') != ORIGINAL_WITNESSES or not verify_reference(original_reference):
        raise ValueError('The immutable original witness inventory is absent or changed.')
    original = read(ORIGINAL_WITNESSES)
    original_rows = original.get('witnesses', [])
    by_id = {row['id']: row for row in rows}
    if (len(original_rows) != 48 or original.get('count') != 48 or
            original_reference.get('count') != 48 or
            len({r['id'] for r in original_rows}) != len(original_rows) or
            any(by_id.get(row['id']) != row for row in original_rows)):
        raise ValueError('An original actual witness was dropped, duplicated or modified during extension.')
    for row in rows:
        for record in row['before_images'] + [row['source'], row['observation_source']]:
            if not verify_reference(record):
                raise ValueError('A historical witness input or evidence image changed: ' + row['id'])
    return data


def source_references():
    paths = ['work/scripts/book_preamble.tex', 'work/scripts/build_readers.py',
             'work/scripts/verify_generated_heading_final.py',
             'work/scripts/audit_equation_pagination.py',
             'work/scripts/verify_pagination_final.py',
             'work/scripts/compare_pdf_pixels.py', 'work/scripts/verify_pdf.py']
    paths += ['work/build/' + book + '.tex' for book in BOOKS]
    # All shared source bodies are inline in the seven TeX drivers. Preserve
    # the generator metadata as additional dependencies when it is present.
    paths += [path for path in (
        'work/scripts/book_links.lua',
        'work/build/fr_source_marks.json', 'work/build/en_source_marks.json',
        'work/data/generated_heading_repairs.json',
        'work/data/shared_heading_guard_integration.json',
        'work/data/layout_repairs_applied.json',
        'sources/fr/records/CURRENT_TEXT_INDEX.tsv') if (ROOT / path).is_file()]
    return [reference(path) for path in paths]


def heading_matches(text, kind, scan_range=None):
    if kind == 'scan_range':
        match = re.fullmatch(r'scans\s*(\d+)\s*[–—-]\s*(\d+)',
                             unicodedata.normalize('NFKC', text).strip(), re.I)
        return bool(match and '-'.join(match.groups()) == scan_range)
    base = kind.removesuffix('_rule_only')
    return any(value == base and canonical(text) == canonical(title)
               for title, value in HEADINGS.items())


def localize_witnesses(book, rows, digest, directory):
    """Locate by source entry identifier; retain alternatives for actual review."""
    result = []
    with fitz.open(ROOT / 'work/build' / (book + '.pdf')) as doc:
        tables = {page.number + 1: lines(page) for page in doc}
        scans = page_scans(book, doc) if any(r['heading_kind'] == 'scan_range' for r in rows) else {}
        cache = {}

        def evidence(page_number):
            if page_number not in cache:
                cache[page_number] = render_full(doc, book, page_number, directory)
            return cache[page_number]

        for original in rows:
            row = dict(original, pdf_sha256=digest, status='PENDING_ACTUAL_VISUAL_REVIEW')
            anchor = original.get('first_entry_anchor')
            anchor_hits = []
            if anchor and original['heading_kind'] != 'scan_range':
                for number, body in tables.items():
                    for item in body:
                        text = re.sub(r'\s+', '', unicodedata.normalize('NFKC', item['text']))
                        if anchor in text:
                            anchor_hits.append(dict(page=number, **item))
            titles = []
            if original['heading_kind'] == 'scan_range':
                context = (original['cote'], int(original['scan']))
                for number, body in tables.items():
                    neighboring = {(s['cote'], int(s['scan'])) for p in (number - 1, number, number + 1)
                                   for s in scans.get(p, [])}
                    for item in body:
                        if heading_matches(item['text'], 'scan_range', original['scan_range']) and context in neighboring:
                            titles.append(dict(page=number, **item))
            else:
                for hit in anchor_hits:
                    choices = []
                    for number in (hit['page'] - 1, hit['page']):
                        for item in tables.get(number, []):
                            if (heading_matches(item['text'], original['heading_kind']) and
                                    (number < hit['page'] or item['bbox'][3] <= hit['bbox'][1] + 1)):
                                choices.append(dict(page=number, **item))
                    if choices:
                        titles.append(max(choices, key=lambda t: (t['page'], t['bbox'][1])))
            # A failed localization stays visibly unresolved. Never use an old
            # physical page number as an inferred final closure.
            title_unique = {(r['page'], tuple(r['bbox'])): r for r in titles}
            titles = list(title_unique.values())
            pages = {r['page'] for r in titles + anchor_hits}
            if original['heading_kind'] == 'scan_range':
                pages |= {r['page'] + 1 for r in titles if r['page'] < len(doc)}
            # Include the preceding physical page for known separator defects:
            # this permits actual confirmation that no rule remains behind.
            if original['heading_kind'].endswith('_rule_only'):
                pages |= {r['page'] - 1 for r in titles if r['page'] > 1}
            row.update(anchor_hits=anchor_hits, heading_hits=titles,
                       localization_status=('LOCALIZED_FOR_ACTUAL_REVIEW' if len(titles) == 1 and
                           (original['heading_kind'] == 'scan_range' or len(anchor_hits) == 1)
                           else 'AMBIGUOUS_OR_MISSING_LOCALIZATION'),
                       candidate_pages=sorted(pages), images=[evidence(p) for p in sorted(pages)])
            result.append(row)
    return result


def pending_report(queue_path, queue):
    return {'schema': 'generated-heading-audit-v1', 'status': 'PENDING_ACTUAL_REVIEW',
            'generated_at_utc': now(), 'queue': reference(queue_path),
            'files': queue['files'], 'scanner': queue['scanner'],
            'source_inputs': queue['source_inputs'], 'candidate_inventory': queue['candidate_inventory'],
            'witness_inventory': queue['witness_inventory'], 'review_inputs': [], 'comparisons': [],
            'primary_candidates': [r for r in queue['final_candidates'] if r['reader'] not in MASTER_SOURCE],
            'master_candidates': [r for r in queue['final_candidates'] if r['reader'] in MASTER_SOURCE],
            'witnesses': queue['known_witnesses'],
            'counts': {'files': 7, 'primary_candidates': queue['counts']['primary_candidates'],
                       'primary_cleared': 0, 'master_candidates': queue['counts']['master_candidates'],
                       'master_cleared': 0, 'expected_witnesses': queue['witness_inventory']['count'],
                       'witnesses_resolved': 0, 'unresolved': 1},
            'unresolved': [{'scope': 'actual final review', 'reason': 'Prepared evidence awaits attributed actual observations and current master pixel comparisons.'}],
            'observations_generated_by_script': False}


def prepare(args):
    if not args.final:
        raise ValueError('Preparation requires --final after the complete seven-PDF build is stable.')
    historical = frozen_witnesses(args.witnesses)
    expected_count = len(historical['witnesses'])
    frozen = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    sources = source_references()
    revision = hashlib.sha256(json.dumps(frozen, sort_keys=True).encode()).hexdigest()[:16]
    directory = ROOT / args.proof_dir / revision
    pair_dir = directory / 'candidate_pairs'
    scanner_hash = sha(ROOT / SCANNER)
    subprocess.run([sys.executable, str(ROOT / SCANNER), '--output', args.scanner_output,
                    '--proof-dir', rel(pair_dir)], cwd=ROOT, check=True)
    inventory = read(args.scanner_output)
    if len(inventory['files']) != 7 or {r['reader']: r['sha256'] for r in inventory['files']} != frozen:
        raise RuntimeError('The scanner did not cover exactly the seven frozen PDFs.')
    files = [dict(r, path='work/build/' + r['reader'] + '.pdf') for r in inventory['files']]
    candidates = []
    for item in inventory['candidates']:
        row = dict(item)
        if row['reader'] not in MASTER_SOURCE:
            path = row['native_pair_image']
            row['images'] = [reference(path, pages=[row['page'], row['adjacent_page']],
                                       render_basis='Native 2.5x end/start page pair from the frozen final PDF.')]
        candidates.append(row)
    known = []
    for book in BOOKS:
        if book in MASTER_SOURCE:
            continue
        selected = [r for r in historical['witnesses'] if r['reader'] == book]
        if selected:
            known.extend(localize_witnesses(book, selected, frozen[book], directory / 'known'))
    after = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    if after != frozen or scanner_hash != sha(ROOT / SCANNER) or any(not verify_reference(r) for r in sources):
        raise RuntimeError('A PDF, scanner or source input changed during preparation.')
    schema = {'id': 'Exact prepared item ID', 'reader': 'Exact book basename',
              'pdf_sha256': 'Prepared current PDF SHA256',
              'status': 'RESOLVED_ON_FINAL_PDF for known witnesses; CLEARED_ON_FINAL_PDF for primary candidates; DETACHMENT_REMAINS for an observed defect.',
              'reviewer': 'Actual reviewer attribution', 'observation': 'Specific actual image observation identifying heading, rule and first substantive content.',
              'heading_page': 'Actual physical page containing the intact heading',
              'first_content_page': 'Actual physical page of its first substantive entry or source content',
              'rule_page': 'Actual separator page, mandatory for a rule-only historical witness or candidate',
              'images': 'Nonempty array of prepared {path,sha256} image records actually viewed.'}
    queue = {'schema': 'generated-heading-queue-v1', 'status': 'PENDING_ACTUAL_REVIEW',
             'generated_at_utc': now(), 'files': files, 'scanner': reference(SCANNER),
             'source_inputs': sources, 'candidate_inventory': reference(args.scanner_output),
             'witness_inventory': reference(args.witnesses, count=expected_count),
             'known_witnesses': known, 'final_candidates': candidates,
             'counts': {'expected_witnesses': expected_count, 'known_witnesses': len(known),
                        'primary_candidates': sum(r['reader'] not in MASTER_SOURCE for r in candidates),
                        'master_candidates': sum(r['reader'] in MASTER_SOURCE for r in candidates),
                        'ambiguous_localizations': sum(r['localization_status'] != 'LOCALIZED_FOR_ACTUAL_REVIEW' for r in known)},
             'observation_schema': schema, 'observations_generated_by_script': False}
    write(args.output, queue)
    for book in BOOKS:
        if book in MASTER_SOURCE:
            continue
        split = {'schema': 'generated-heading-review-queue-v1', 'status': 'PENDING_ACTUAL_REVIEW',
                 'reader': book, 'pdf_sha256': frozen[book], 'queue': reference(args.output),
                 'known_witnesses': [r for r in known if r['reader'] == book],
                 'final_candidates': [r for r in candidates if r['reader'] == book],
                 'observation_schema': schema, 'observations_generated_by_script': False}
        write('work/data/generated_heading_final_queues/' + book + '.json', split)
    write(args.report, pending_report(args.output, queue))
    return queue


def check_observation(item, ob, expected_status, page_count):
    errors = []
    if not ob:
        return ['No actual final-image observation supplied.']
    for key in ('id', 'reader', 'pdf_sha256'):
        if ob.get(key) != item.get(key):
            errors.append('Observation differs from prepared ' + key + '.')
    if ob.get('status') != expected_status:
        errors.append('Required actual closure status is absent: ' + expected_status)
    if any(not str(ob.get(key, '')).strip() for key in ('reviewer', 'observation')):
        errors.append('Nonempty actual reviewer and observation are required.')
    expected = {r['path']: r for r in item.get('images', [])}
    viewed = ob.get('images', [])
    pages = set()
    if not viewed:
        errors.append('No actually viewed image evidence supplied.')
    for image in viewed:
        evidence = expected.get(image.get('path'))
        if not evidence:
            errors.append('An observation image is outside this prepared item.')
            continue
        if image.get('sha256') != evidence.get('sha256') or not verify_reference(image):
            errors.append('An actual image hash differs from its prepared evidence.')
        pages.update(evidence.get('pages', [evidence.get('page')]))
    heading = ob.get('heading_page')
    content = ob.get('first_content_page')
    if not isinstance(heading, int) or isinstance(heading, bool) or not 1 <= heading <= page_count:
        errors.append('A valid actual physical heading page is required.')
    if heading != content:
        errors.append('The first substantive entry/content is not on the heading page.')
    if item.get('heading_kind', '').endswith('_rule_only') and 'rule_page' not in ob:
        errors.append('A rule-only case requires the actual separator page.')
    if 'rule_page' in ob and ob['rule_page'] != heading:
        errors.append('The separator is not on the heading page.')
    if heading not in pages:
        errors.append('The actual heading/content page is absent from the viewed image evidence.')
    if expected_status == 'RESOLVED_ON_FINAL_PDF':
        if heading not in {hit['page'] for hit in item.get('heading_hits', [])}:
            errors.append('The claimed heading page does not contain a prepared source-qualified title hit.')
        if item.get('heading_kind') != 'scan_range':
            if (not item.get('first_entry_anchor') or
                    content not in {hit['page'] for hit in item.get('anchor_hits', [])}):
                errors.append('The claimed first-content page does not contain the exact prepared entry anchor.')
    elif expected_status == 'CLEARED_ON_FINAL_PDF':
        expected_heading = (item['adjacent_page'] if item.get('heading_kind', '').endswith('_rule_only')
                            else item['page'])
        if heading != expected_heading:
            errors.append('The claimed heading page differs from the title side of the prepared candidate boundary.')
    return errors


def compare_gate(master, frozen, page_counts):
    path = COMPARISONS[master]
    errors = []
    if not (ROOT / path).is_file():
        return {}, None, ['Current all-page apparatus/master pixel comparison is missing.']
    data = read(path)
    source = MASTER_SOURCE[master]
    if data.get('source_pdf_sha256') != frozen[source] or data.get('target_pdf_sha256') != frozen[master]:
        errors.append('Pixel comparison does not name the current source/master PDF hashes.')
    if (not data.get('every_corresponding_page_compared') or not data.get('page_counts_equal') or
            data.get('source_pages') != page_counts[source] or data.get('target_pages') != page_counts[master]):
        errors.append('Pixel comparison does not cover the actual complete current page counts.')
    rows = data.get('pages', [])
    if (len(rows) != page_counts[source] or
            {r.get('page') for r in rows} != set(range(1, page_counts[source] + 1))):
        errors.append('Per-page comparison is incomplete or duplicated.')
    if any(p != 1 for p in data.get('different_or_missing_pages', [])):
        errors.append('A source/master page beyond the title differs.')
    for row in rows:
        if row.get('page') == 1:
            continue
        a, b = row.get('source', {}), row.get('target', {})
        if (not row.get('identical_pixels') or not a or a != b or
                not re.fullmatch(r'[0-9a-f]{64}', a.get('pixel_sha256', ''))):
            errors.append('A per-page RGB identity record is missing or inconsistent.')
            break
    return data, reference(path, master=master, status='FAIL' if errors else 'PASS'), errors


def finalize(args):
    queue = read(args.queue)
    historical = frozen_witnesses(queue['witness_inventory']['path'])
    expected_count = len(historical['witnesses'])
    supplied, reviews = observations(args.observations or [])
    frozen = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    page_counts = {}
    for book in BOOKS:
        with fitz.open(ROOT / 'work/build' / (book + '.pdf')) as doc:
            page_counts[book] = len(doc)
    unresolved = []

    def issue(scope, reason):
        unresolved.append({'scope': scope, 'reason': reason})

    files = queue.get('files', [])
    if (len(files) != 7 or {r.get('reader'): r.get('sha256') for r in files} != frozen or
            any(r.get('pages') != page_counts.get(r.get('reader')) for r in files)):
        issue('PDF inventory', 'The prepared queue does not match exactly the seven current hashes and page counts.')
    required_sources = {'work/scripts/book_preamble.tex', 'work/scripts/build_readers.py'} | {
        'work/build/' + book + '.tex' for book in BOOKS}
    if not required_sources <= {r.get('path') for r in queue.get('source_inputs', [])}:
        issue('source inputs', 'The generator, preamble and all seven inline-body TeX drivers are required.')
    for key in ('scanner', 'candidate_inventory', 'witness_inventory'):
        if not verify_reference(queue[key]):
            issue(key, 'A prepared input hash changed or the referenced file is absent.')
    for record in queue.get('source_inputs', []):
        if not verify_reference(record):
            issue('source inputs', 'A prepared source dependency changed: ' + record['path'])
    inventory = read(queue['candidate_inventory']['path'])
    candidates = queue.get('final_candidates', [])
    expected_candidates = {r['id']: r for r in inventory['candidates']}
    if (len(expected_candidates) != len(inventory['candidates']) or len(candidates) != len(expected_candidates) or
            {r['id'] for r in candidates} != set(expected_candidates)):
        issue('candidate inventory', 'Exact unique all-page scanner candidate coverage differs from the prepared queue.')
    for row in candidates:
        original = expected_candidates.get(row['id'], {})
        for key in ('reader', 'pdf_sha256', 'page', 'adjacent_page', 'heading_kind', 'bbox'):
            if row.get(key) != original.get(key):
                issue(row['id'], 'Prepared candidate changed from the scanner output: ' + key)
    if (len(inventory['files']) != 7 or {r['reader']: r['sha256'] for r in inventory['files']} != frozen or
            any(r.get('pages') != page_counts.get(r.get('reader')) for r in inventory['files'])):
        issue('scanner inventory', 'The all-page scanner belongs to different PDFs or page counts.')
    known = queue.get('known_witnesses', [])
    expected_known = {r['id']: r for r in historical['witnesses']}
    if (len(known) != expected_count or len({r['id'] for r in known}) != expected_count or
            {r['id'] for r in known} != set(expected_known)):
        issue('known witness inventory', 'The prepared queue does not contain every frozen historical ID exactly once.')
    primary, witnesses = [], []
    for items, output, required in ((known, witnesses, 'RESOLVED_ON_FINAL_PDF'),
            ([r for r in candidates if r['reader'] not in MASTER_SOURCE], primary, 'CLEARED_ON_FINAL_PDF')):
        for item in items:
            ob = supplied.get(item['id'])
            errors = check_observation(item, ob, required, page_counts.get(item['reader'], 0))
            if item['pdf_sha256'] != frozen.get(item['reader']):
                errors.append('Prepared item belongs to a different current PDF hash.')
            if required == 'RESOLVED_ON_FINAL_PDF':
                original = expected_known.get(item['id'], {})
                for key in ('reader', 'heading_kind', 'cote', 'scan', 'package', 'first_entry_anchor',
                            'source', 'before_pdf_sha256', 'before_images', 'observation_source'):
                    if item.get(key) != original.get(key):
                        errors.append('Historical source-qualified witness changed: ' + key)
            out = dict(item)
            out['prepared_images'] = item.get('images', [])
            if ob:
                # Reviewer fields cannot overwrite the frozen source identity,
                # prepared title/anchor localization or historical evidence.
                for key in ('reviewer', 'observation', 'heading_page', 'first_content_page',
                            'rule_page', 'images', 'observation_record', 'observation_record_sha256'):
                    if key in ob:
                        out[key] = ob[key]
            out['status'] = 'UNRESOLVED' if errors else required
            out['validation_errors'] = errors
            output.append(out)
            for error in errors:
                issue(item['id'], error)
    comparisons, comparison_records = {}, []
    for master in MASTER_SOURCE:
        data, record, errors = compare_gate(master, frozen, page_counts)
        comparisons[master] = data, errors
        if record:
            comparison_records.append(record)
        for error in errors:
            issue(master, error)
    primary_by_key = {(r['reader'], r['page'], r['heading_kind']): r for r in primary}
    masters = []
    for item in candidates:
        master = item['reader']
        if master not in MASTER_SOURCE:
            continue
        data, failures = comparisons[master]
        errors = list(failures)
        source = primary_by_key.get((MASTER_SOURCE[master], item['page'], item['heading_kind']))
        if not source or source.get('status') != 'CLEARED_ON_FINAL_PDF':
            errors.append('The corresponding primary candidate lacks an actual current clearance.')
        pixels = {r['page']: r for r in data.get('pages', [])}
        if any(not pixels.get(p, {}).get('identical_pixels') for p in (item['page'], item['adjacent_page'])):
            errors.append('Both candidate boundary pages require current identical RGB pixels.')
        out = dict(item, status='UNRESOLVED' if errors else 'CLEARED_BY_IDENTICAL_RENDER',
                   source_candidate_id=source['id'] if source else None,
                   comparison=reference(COMPARISONS[master]) if (ROOT / COMPARISONS[master]).is_file() else None,
                   validation_errors=errors)
        if source and not errors:
            out.update(reviewer=source['reviewer'],
                       observation='Transferred through complete current apparatus/master RGB identity. Actual apparatus observation: ' + source['observation'],
                       heading_page=source['heading_page'], first_content_page=source['first_content_page'],
                       images=source['images'], source_pdf_sha256=frozen[MASTER_SOURCE[master]])
            if 'rule_page' in source:
                out['rule_page'] = source['rule_page']
        masters.append(out)
        for error in errors:
            issue(item['id'], error)
    expected_observations = set(expected_known) | {r['id'] for r in candidates if r['reader'] not in MASTER_SOURCE}
    for key in set(supplied) - expected_observations:
        issue(key, 'Supplied observation is outside the prepared final inventory.')
    after = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    if after != frozen:
        issue('PDF inventory', 'A PDF changed while finalizing.')
    for record in queue['source_inputs'] + reviews + comparison_records:
        if not verify_reference(record):
            issue('final evidence stability', 'A dependency or review record changed during finalization: ' + record['path'])
    result = {'schema': 'generated-heading-audit-v1', 'status': 'FAIL' if unresolved else 'PASS',
              'generated_at_utc': now(),
              'scope': f'Every physical page of all seven current publication PDFs; actual closure of {expected_count} historical generated-heading, rule-only and range-heading detachments; actual clearance of every final primary scanner candidate; current all-page pixel identity for master duplicates.',
              'queue': reference(args.queue),
              'files': [dict(r, stable_during_audit=(frozen == after and r['sha256'] == frozen.get(r['reader']))) for r in files],
              'scanner': queue['scanner'], 'source_inputs': queue['source_inputs'],
              'candidate_inventory': queue['candidate_inventory'], 'witness_inventory': queue['witness_inventory'],
              'review_inputs': reviews, 'comparisons': comparison_records,
              'primary_candidates': primary, 'master_candidates': masters, 'witnesses': witnesses,
              'counts': {'files': len(files), 'primary_candidates': len(primary),
                         'primary_cleared': sum(r['status'] == 'CLEARED_ON_FINAL_PDF' for r in primary),
                         'master_candidates': len(masters),
                         'master_cleared': sum(r['status'] == 'CLEARED_BY_IDENTICAL_RENDER' for r in masters),
                         'expected_witnesses': expected_count,
                         'witnesses_resolved': sum(r['status'] == 'RESOLVED_ON_FINAL_PDF' for r in witnesses),
                         'unresolved': len(unresolved)},
              'unresolved': unresolved, 'observations_generated_by_script': False}
    write(args.output, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    command = commands.add_parser('prepare')
    command.add_argument('--final', action='store_true')
    command.add_argument('--witnesses', default=WITNESSES)
    command.add_argument('--scanner-output', default=INVENTORY)
    command.add_argument('--proof-dir', default=PROOFS)
    command.add_argument('--output', default=QUEUE)
    command.add_argument('--report', default=OUTPUT)
    command = commands.add_parser('finalize')
    command.add_argument('--queue', default=QUEUE)
    command.add_argument('--observations', action='append')
    command.add_argument('--output', default=OUTPUT)
    args = parser.parse_args()
    if Path.cwd().resolve() != ROOT:
        parser.error('Run from the project root.')
    try:
        result = prepare(args) if args.command == 'prepare' else finalize(args)
    except Exception as error:
        destination = args.report if args.command == 'prepare' else args.output
        write(destination, {'schema': 'generated-heading-audit-v1', 'status': 'FAIL',
                            'generated_at_utc': now(), 'files': [], 'primary_candidates': [],
                            'master_candidates': [], 'witnesses': [],
                            'unresolved': [{'scope': 'audit execution', 'reason': 'The audit did not complete (' + type(error).__name__ + '); no PASS is issued.'}],
                            'observations_generated_by_script': False})
        raise
    print(json.dumps({'status': result['status'], 'output': args.output, 'counts': result['counts']}))
    if result['status'] == 'FAIL':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
