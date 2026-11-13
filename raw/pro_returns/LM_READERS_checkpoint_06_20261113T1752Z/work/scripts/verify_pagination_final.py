#!/usr/bin/env python3
"""Prepare and finalize hash-bound review of repaired equation pagination.

Preparation renders evidence but makes no visual-inspection claim. Finalization
accepts only explicitly supplied observations whose PDF and image hashes match
the prepared evidence. Exact source bindings alone cannot close a defect.
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
import re
from pathlib import Path

import fitz

from audit_equation_pagination import BOOKS, normalize, render_pair, scan_book, sha
from verify_pdf import URI_RE

ROOT = Path(__file__).resolve().parents[2]
BASELINE = 'work/data/pagination_review_before_repairs.json'
BINDINGS = 'work/data/layout_tag_bindings.json'
APPLIED = 'work/data/layout_repairs_applied.json'
RECONCILIATION = 'work/data/layout_pagination_reconciliation.json'
HEADING_AUDIT = 'work/data/heading_closure_final.json'
QUEUE = 'work/data/pagination_verification_queue.json'
SCANNER = 'work/data/equation_tag_pagination_final_candidates.json'
OUTPUT = 'work/data/pagination_verification_final.json'
PROOFS = 'work/visual_repair_proofs/pagination_final'
MASTER_SOURCE = {
    'LM_FR_master_annotated': 'LM_FR_corrige_apparat',
    'LM_EN_master_annotated': 'LM_EN_corrected_apparatus',
}
COMPARISONS = {
    'LM_FR_master_annotated': 'work/verification/FR_MASTER_PIXEL_IDENTITY.json',
    'LM_EN_master_annotated': 'work/verification/EN_MASTER_PIXEL_IDENTITY.json',
}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def rel(path):
    path = Path(path)
    return path.resolve().relative_to(ROOT).as_posix()


def read(path):
    return json.loads((ROOT / path).read_text())


def write(path, data):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def safe(value):
    return re.sub(r'[^A-Za-z0-9]+', '-', str(value)).strip('-')


def known_id(row):
    return f"KNOWN-{row['reader']}-p{int(row['page']):04d}-{safe(row['tag'])}"


def candidate_id(row):
    direction = 'forward' if row['direction'].startswith('number_before') else 'reverse'
    return f"FINAL-{row['reader']}-p{int(row['page']):04d}-{safe(row['tag'])}-{direction}"


def baseline_check(data):
    rows = data['candidates']
    counts = collections.Counter(r['decision'] for r in rows)
    if len(rows) != 106 or counts != {'confirmed detached tag': 80, 'visually cleared': 26}:
        raise ValueError('The baseline must contain exactly the 106 supplied inspections: 80 true, 26 clear.')
    if len({known_id(r) for r in rows}) != len(rows):
        raise ValueError('Duplicate baseline instance ID.')


def source_contexts(row):
    source = row.get('source', row.get('confirmed_source', {}))
    cote = row.get('source_cote') or source.get('cote')
    scan = row.get('source_scan') or source.get('scan')
    if cote and scan:
        return {(str(cote), int(scan))}
    return {(str(r['cote']), int(r['scan'])) for r in
            row.get('scan_context', []) + row.get('adjacent_scan_context', [])}


def binding_has_tag(binding, tag):
    tag = normalize(tag)
    declared = binding.get('tag', binding.get('equation_tag'))
    if declared is not None:
        return normalize(str(declared)) == tag or '(' + normalize(str(declared)) + ')' == tag
    if binding.get('tags'):
        return any(normalize(str(t)) == tag for t in binding['tags'])
    # Fallback only selects candidates. Uniqueness, source context, an applied
    # exact-replacement record, and final visual inspection remain mandatory.
    variants = binding.get('variants', [])
    return any(tag in normalize(v['old']) for v in variants)


def resolve_sources(baseline, bindings, applied, overrides=None, reconciliation=None):
    by_id = collections.defaultdict(list)
    for row in applied:
        by_id[row.get('id', '')].append(row)
    manifest = {r['package']: r for r in read('sources/en/MANIFEST.json')['packages']}
    overrides = overrides or {}
    canonical = {}
    if reconciliation is not None:
        canonical = {(r['reader'], int(r['historical_page']), normalize(r['tag'])): r
                     for r in reconciliation['confirmed_instances']}
        expected = {(r['reader'], int(r['page']), normalize(r['tag']))
                    for r in baseline['candidates'] if r['decision'] == 'confirmed detached tag'}
        if set(canonical) != expected or not reconciliation.get('all_confirmed_instances_bound_exactly'):
            raise ValueError('Canonical source reconciliation does not cover all 80 baseline instances exactly.')
    resolved = []
    for row in baseline['candidates']:
        if row['decision'] != 'confirmed detached tag':
            continue
        item_id = known_id(row)
        language = 'en' if row['reader'].startswith('LM_EN') else 'fr'
        contexts = source_contexts(row)
        canonical_row = canonical.get((row['reader'], int(row['page']), normalize(row['tag'])))
        if canonical_row:
            if (canonical_row['historical_pdf_sha256'] != row['historical_pdf_sha256'] or
                    canonical_row['before_image_sha256'] != row['native_pair_image_sha256']):
                raise ValueError('Canonical source reconciliation names different historical evidence: ' + item_id)
            contexts = {(canonical_row['cote'], int(canonical_row['scan']))}
        choices = [b for b in bindings if b['language'] == language and
                   (str(b.get('cote', manifest[b['package']]['cote'])), int(b['scan'])) in contexts and
                   binding_has_tag(b, row['tag'])]
        if canonical_row:
            choices = [b for b in choices if b['id'] == canonical_row['repair_id'] and
                       b['package'] == canonical_row['package']]
        if item_id in overrides:
            choices = [b for b in choices if b['id'] == overrides[item_id]['binding_id']]
        out = {'id': item_id, 'reader': row['reader'], 'tag': row['tag'],
               'before_page': row['page'], 'before_adjacent_page': row['adjacent_page'],
               'before_direction': row['direction'],
               'before_pdf_sha256': row['historical_pdf_sha256'],
               'before_image': row['native_pair_image'],
               'before_image_sha256': row['native_pair_image_sha256'],
               'before_observation': row['observation'],
               'source_context_candidates': [dict(cote=c, scan=s) for c, s in sorted(contexts)],
               'binding_candidates': [b['id'] for b in choices],
               'source_resolution_status': 'UNRESOLVED'}
        if len(choices) == 1:
            b = choices[0]
            witnesses = [a for a in by_id[b['id']] if a.get('language') == language and
                         a.get('package') == b['package'] and int(a.get('scan', -1)) == int(b['scan'])]
            if len(witnesses) == 1 and any(witnesses[0].get('new') == v['new'] for v in b['variants']):
                a = witnesses[0]
                source_path = a.get('source_path') or (
                    ('en/packages/' if language == 'en' else 'fr/texts/') + b['package'] +
                    ('_en' if language == 'en' else '') + '.tex')
                disk_source = ROOT / 'sources' / source_path
                out.update(source_resolution_status='EXACT_APPLIED_SOURCE_BINDING',
                           binding_id=b['id'], binding_kind=b['kind'], binding_reason=b['reason'],
                           source={'cote': str(b.get('cote', manifest[b['package']]['cote'])),
                                   'scan': int(b['scan']), 'package': b['package'], 'language': language,
                                   'path': 'sources/' + source_path,
                                   'line': a.get('source_line'),
                                   'sha256': sha(disk_source) if disk_source.is_file() else None},
                           applied_old_sha256=hashlib.sha256(a['old'].encode()).hexdigest(),
                           applied_new_sha256=hashlib.sha256(a['new'].encode()).hexdigest(),
                           associated_display_source=a.get('source_old', a['old']))
                if canonical_row:
                    out['source'].update({key: canonical_row[key] for key in
                        ('source_offset_start', 'source_offset_end', 'source_byte_start', 'source_byte_end')})
                    out['source']['line'] = canonical_row['source_line']
                    out['source_resolution_basis'] = canonical_row['source_resolution_basis']
            else:
                out['source_resolution_error'] = 'Expected one matching applied exact-replacement witness.'
        else:
            out['source_resolution_error'] = 'Expected one source-qualified binding; manual qualification is required.'
        resolved.append(out)
    return resolved


def source_preflight(args):
    baseline = read(args.baseline)
    baseline_check(baseline)
    reconciliation = read(args.reconciliation)
    if reconciliation['layout_tag_bindings_sha256'] != sha(ROOT / args.bindings):
        raise ValueError('Canonical reconciliation refers to a different tag-binding inventory.')
    sources = resolve_sources(baseline, read(args.bindings), read(args.applied),
                              read(args.source_overrides) if args.source_overrides else None, reconciliation)
    result = {'status': 'SOURCE_PREFLIGHT_ONLY_NO_FINAL_PDF_INSPECTION',
              'baseline': {'path': args.baseline, 'sha256': sha(ROOT / args.baseline)},
              'bindings': {'path': args.bindings, 'sha256': sha(ROOT / args.bindings)},
              'applied': {'path': args.applied, 'sha256': sha(ROOT / args.applied)},
              'source_reconciliation': {'path': args.reconciliation, 'sha256': sha(ROOT / args.reconciliation)},
              'known_detachments': sources,
              'resolved_source_count': sum(r['source_resolution_status'] == 'EXACT_APPLIED_SOURCE_BINDING' for r in sources),
              'observations_generated_by_script': False}
    write(args.output, result)
    return result


def scan_links(doc):
    by_scan = collections.defaultdict(set)
    for page in doc:
        for link in page.get_links():
            match = URI_RE.match(link.get('uri', ''))
            if match:
                by_scan[(match[1], int(match[2]))].add(page.number + 1)
    return by_scan


def tag_hits(page, tag):
    hits = []
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            text = ''.join(s['text'] for s in line['spans'])
            if normalize(tag) in normalize(text):
                box = fitz.Rect(line['bbox']) * page.rotation_matrix
                hits.append({'page': page.number + 1, 'bbox': list(box), 'line_text': text})
    return hits


def render_full(doc, reader, page_number, directory):
    target = directory / reader / f'page_{page_number:04d}_native2x.png'
    target.parent.mkdir(parents=True, exist_ok=True)
    page = doc[page_number - 1]
    page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB, alpha=False).save(target)
    return {'path': rel(target), 'sha256': sha(target), 'page': page_number,
            'render_basis': 'Full physical page rendered from the hash-bound final PDF at 2x MuPDF resolution.'}


def prepare(args):
    baseline = read(args.baseline)
    baseline_check(baseline)
    reconciliation = read(args.reconciliation)
    if reconciliation['layout_tag_bindings_sha256'] != sha(ROOT / args.bindings):
        raise ValueError('Canonical reconciliation refers to a different tag-binding inventory.')
    sources = resolve_sources(baseline, read(args.bindings), read(args.applied),
                              read(args.source_overrides) if args.source_overrides else None, reconciliation)
    if any(r['source_resolution_status'] != 'EXACT_APPLIED_SOURCE_BINDING' for r in sources):
        write(args.output, {'status': 'BLOCKED_SOURCE_QUALIFICATION', 'known_detachments': sources})
        raise ValueError('All 80 old detachment instances require exact source bindings before final preparation.')
    frozen = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    files, candidates = [], []
    directory = ROOT / args.proof_dir
    # Keep each revision in a hash-keyed directory; earlier inspected evidence
    # is never overwritten when pagination or glyphs change.
    revision = hashlib.sha256(json.dumps(frozen, sort_keys=True).encode()).hexdigest()[:16]
    directory = directory / revision
    directory.mkdir(parents=True, exist_ok=True)
    for book in BOOKS:
        info, rows = scan_book(ROOT / 'work/build' / (book + '.pdf'), set())
        if info['sha256'] != frozen[book]:
            raise RuntimeError('Input PDF changed while preparing final audit: ' + book)
        files.append(info)
        for row in rows:
            row['id'] = candidate_id(row)
            row['pdf_sha256'] = frozen[book]
            row['status'] = 'PENDING_MASTER_PIXEL_IDENTITY' if book in MASTER_SOURCE else 'PENDING_VISUAL_REVIEW'
            if book not in MASTER_SOURCE:
                render_pair(row, directory)
                row['native_pair_image'] = rel(row['native_pair_image'])
                row['images'] = [{'path': row['native_pair_image'],
                                  'sha256': row['native_pair_image_sha256'],
                                  'pages': [row['page'], row['adjacent_page']]}]
            candidates.append(row)
        print(book + ': ' + str(len(rows)) + ' final candidates rendered or assigned to master comparison.', flush=True)
    scanner = {'status': 'FINAL_CANDIDATES_REQUIRE_REVIEW', 'generated_at_utc': now(),
               'files': files, 'candidate_count': len(candidates), 'candidates': candidates,
               'observations_generated_by_script': False}
    write(args.scanner_output, scanner)
    for book in BOOKS:
        local = [r for r in sources if r['reader'] == book]
        if not local:
            continue
        with fitz.open(ROOT / 'work/build' / (book + '.pdf')) as doc:
            links = scan_links(doc)
            for item in local:
                source = item['source']
                linked_pages = sorted(links[(source['cote'], source['scan'])])
                # Always include immediate neighbors. An unmarked display can
                # move to the next page while a prose reference to its tag
                # remains on the page containing the scan-link annotation.
                neighbors = sorted({q for p in linked_pages for q in (p - 1, p, p + 1) if 1 <= q <= len(doc)})
                hits = [dict(h, page_has_source_scan_link=p in linked_pages)
                        for p in neighbors for h in tag_hits(doc[p - 1], item['tag'])]
                expanded = any(h['page'] not in linked_pages for h in hits)
                pages = sorted({h['page'] for h in hits}) or linked_pages
                item.update(pdf_sha256=frozen[book], status='PENDING_VISUAL_REVIEW',
                            scan_linked_pages=linked_pages, final_tag_candidates=hits,
                            tag_search_expanded_to_neighbor_pages=expanded,
                            final_pages=pages,
                            images=[render_full(doc, book, p, directory) for p in pages])
                if not hits:
                    item['localization_warning'] = 'No exact extracted tag located. Reviewer must qualify the actual tag and display.'
        print(book + ': ' + str(len(local)) + ' known detachment closure instances prepared.', flush=True)
    after = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    if after != frozen:
        raise RuntimeError('A PDF changed during final evidence preparation. Queue not saved.')
    result = {'status': 'PENDING_VISUAL_REVIEW', 'generated_at_utc': now(), 'files': files,
              'baseline': {'path': args.baseline, 'sha256': sha(ROOT / args.baseline),
                           'candidates': 106, 'true_detachments': 80, 'cleared': 26},
              'source_bindings': {'path': args.bindings, 'sha256': sha(ROOT / args.bindings)},
              'applied_repairs': {'path': args.applied, 'sha256': sha(ROOT / args.applied)},
              'source_reconciliation': {'path': args.reconciliation, 'sha256': sha(ROOT / args.reconciliation)},
              'scanner': {'path': args.scanner_output, 'sha256': sha(ROOT / args.scanner_output)},
              'known_detachments': sources, 'final_candidates': candidates,
              'counts': {'known_detachments': len(sources),
                         'unique_known_source_sites': len({(r['source']['cote'], r['source']['scan'], normalize(r['tag'])) for r in sources}),
                         'unique_known_source_binding_ids': len({r['binding_id'] for r in sources}),
                         'final_primary_candidates': sum(r['reader'] not in MASTER_SOURCE for r in candidates),
                         'final_master_candidates': sum(r['reader'] in MASTER_SOURCE for r in candidates)},
              'observation_schema': {
                  'id': 'Exact queue item ID',
                  'status': 'RESOLVED_ON_FINAL_PDF for a known defect; CLEARED_ON_FINAL_PDF for a final primary candidate; DETACHMENT_REMAINS if defective.',
                  'pdf_sha256': 'Exact prepared PDF SHA256', 'reviewer': 'Actual reviewer',
                  'observation': 'What was actually seen, with tag and associated display identified.',
                  'tag_page': 'Actual physical page containing the tag',
                  'display_pages': 'List of actual physical pages containing the associated complete display',
                  'images': 'List of {path,sha256} for the prepared images actually viewed.'},
              'observations_generated_by_script': False}
    write(args.output, result)
    for book in BOOKS:
        if book in MASTER_SOURCE:
            continue
        split = {'status': 'PENDING_VISUAL_REVIEW', 'reader': book, 'pdf_sha256': frozen[book],
                 'queue': {'path': args.output, 'sha256': sha(ROOT / args.output)},
                 'known_detachments': [r for r in sources if r['reader'] == book],
                 'final_candidates': [r for r in candidates if r['reader'] == book],
                 'observation_schema': result['observation_schema'],
                 'observations_generated_by_script': False}
        write('work/data/pagination_final_queues/' + book + '.json', split)
    return result


def observations(paths):
    result = {}
    records = []
    for path in paths:
        data = read(path)
        if isinstance(data, list):
            rows = data
        elif isinstance(data.get('observations'), list):
            rows = data['observations']
        else:
            rows = [dict(value, id=key) for key, value in data.items()]
        for row in rows:
            if row['id'] in result:
                raise ValueError('Duplicate supplied observation: ' + row['id'])
            result[row['id']] = dict(row, observation_record=path,
                                     observation_record_sha256=sha(ROOT / path))
        records.append({'path': path, 'sha256': sha(ROOT / path), 'observations': len(rows)})
    return result, records


def retained_tag_source_errors(item, observation):
    """Validate the narrow source case of an uncancelled tag on a deleted display.

    This permits an honest empty visible-display list. It does not infer a
    visual clearance: the ordinary actual-image and tag-page checks still run.
    """
    errors = []
    if observation.get('classification') != 'RETAINED_TAG_AFTER_FULLY_CANCELLED_DISPLAY':
        return ['An empty visible-display list lacks the exact retained-tag source classification.']
    if item.get('reader') not in {'LM_FR_corrige_apparat', 'LM_FR_texte_de_lecture',
                                  'LM_EN_corrected_apparatus', 'LM_EN_reading'}:
        errors.append('A retained tag after a fully cancelled display is only applicable to a corrected primary form.')
    source = observation.get('source_assessment', {})
    path = source.get('path', '')
    language = 'en' if item.get('reader', '').startswith('LM_EN') else 'fr'
    prefix = 'sources/en/packages/' if language == 'en' else 'sources/fr/texts/'
    if not path.startswith(prefix) or Path(path).name != path.removeprefix(prefix) or not path.endswith('.tex'):
        return errors + ['The cancelled-display witness must be an immutable source package for this language.']
    disk = ROOT / path
    if not disk.is_file() or sha(disk) != source.get('sha256'):
        return errors + ['The cancelled-display source file is missing or has a different hash.']
    text = disk.read_text()
    fragment = source.get('fragment', '')
    if (not fragment or text.count(fragment) != 1 or
            hashlib.sha256(fragment.encode()).hexdigest() != source.get('fragment_sha256')):
        return errors + ['The exact cancelled-display fragment is absent, ambiguous or has a different hash.']
    start = text.index(fragment)
    if source.get('source_line') != text.count('\n', 0, start) + 1:
        errors.append('The cancelled-display source line differs from its immutable fragment.')
    scans = list(re.finditer(r'\\scanpage\{(\d+)\}', text[:start]))
    if not scans or int(scans[-1][1]) != source.get('scan'):
        errors.append('The cancelled-display fragment is not in the asserted source scan.')
    if (str(source.get('cote')), source.get('scan')) not in source_contexts(item):
        errors.append('The cancelled-display source is outside the candidate scan context.')
    manifest = read('sources/en/MANIFEST.json')['packages']
    package = Path(path).stem.removesuffix('_en')
    record = next((row for row in manifest if row['package'] == package), None)
    if not record or str(record['cote']) != str(source.get('cote')):
        errors.append('The cancelled-display cote differs from the immutable package manifest.')
    body = fragment.strip()
    opening = re.match(r'^\\\[\s*\\deleted\s*\{', body)
    if not opening:
        return errors + ['The source display does not begin with one complete deleted group.']
    group_start = opening.end() - 1
    depth, position = 1, group_start + 1
    while position < len(body) and depth:
        char = body[position]
        if char == '\\':
            position += 2
            continue
        if char == '%':
            newline = body.find('\n', position)
            position = len(body) if newline < 0 else newline + 1
            continue
        depth += (char == '{') - (char == '}')
        position += 1
    if depth or not body[group_start + 1:position - 1].strip():
        return errors + ['The cancelled source group is unbalanced or empty.']
    tail = re.fullmatch(r'\s*\\tag\{([^{}]+)\}\s*\\\]', body[position:])
    if not tail or normalize('(' + tail[1] + ')') != normalize(item.get('tag', '')):
        errors.append('The only uncancelled display content must be the exact matching tag after the deleted group.')
    if not str(source.get('observation', '')).strip():
        errors.append('The source-qualified explanation of the retained empty tag is missing.')
    return errors


def check_observation(item, observation, required_status):
    errors = []
    if not observation:
        return ['Actual final-image observation has not been supplied.']
    if observation.get('status') != required_status:
        errors.append('Required closure status was not supplied: ' + required_status)
    if observation.get('pdf_sha256') != item['pdf_sha256']:
        errors.append('Observation PDF hash differs from the prepared PDF.')
    for field in ('reviewer', 'observation'):
        if not str(observation.get(field, '')).strip():
            errors.append('Missing ' + field + '.')
    expected = {r['path']: r for r in item.get('images', [])}
    viewed = observation.get('images', [])
    if not viewed:
        errors.append('No actual viewed-image evidence supplied.')
    viewed_pages = set()
    for image in viewed:
        path = image.get('path')
        if path not in expected:
            errors.append('Observation image is outside this prepared item.')
            continue
        evidence = expected[path]
        if image.get('sha256') != evidence['sha256'] or not (ROOT / path).is_file() or sha(ROOT / path) != evidence['sha256']:
            errors.append('Observation image hash differs from the prepared or actual image.')
        viewed_pages.update(evidence.get('pages', [evidence.get('page')]))
    tag_page = observation.get('tag_page')
    display_pages = observation.get('display_pages')
    empty_retained = (required_status == 'CLEARED_ON_FINAL_PDF' and display_pages == [] and
                      observation.get('classification') == 'RETAINED_TAG_AFTER_FULLY_CANCELLED_DISPLAY')
    if empty_retained:
        errors.extend(retained_tag_source_errors(item, observation))
    if not isinstance(tag_page, int) or not isinstance(display_pages, list) or (not display_pages and not empty_retained):
        errors.append('The actual tag page and complete-display page list are required.')
    elif not empty_retained and set(display_pages) != {tag_page}:
        errors.append('The supplied observation does not place the complete display with its tag.')
    if tag_page not in viewed_pages:
        errors.append('The final tag/display page lacks actually viewed image evidence.')
    if required_status == 'CLEARED_ON_FINAL_PDF' and tag_page != item['page']:
        errors.append('Candidate observation names a different tag page.')
    return errors


def final_report(args):
    queue = read(args.queue)
    baseline = read(queue['baseline']['path'])
    baseline_check(baseline)
    supplied, observation_records = observations(args.observations or [])
    unresolved = []
    frozen = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    actual_page_counts = {}
    for book in BOOKS:
        with fitz.open(ROOT / 'work/build' / (book + '.pdf')) as document:
            actual_page_counts[book] = len(document)
    prepared = {r['reader']: r['sha256'] for r in queue['files']}
    if prepared != frozen or len(queue['files']) != len(BOOKS):
        unresolved.append({'scope': 'PDF inventory', 'reason': 'The prepared queue does not match all seven current PDF hashes.'})
    if any(r.get('pages') != actual_page_counts.get(r['reader']) for r in queue['files']):
        unresolved.append({'scope': 'PDF inventory', 'reason': 'Prepared page counts differ from the actual current PDFs.'})
    for name in ('baseline', 'source_bindings', 'applied_repairs', 'source_reconciliation', 'scanner'):
        evidence = queue[name]
        if sha(ROOT / evidence['path']) != evidence['sha256']:
            unresolved.append({'scope': name, 'reason': 'Supporting input hash changed after preparation.'})
    scanner = read(queue['scanner']['path'])
    scanner_keys = {(r['reader'], r['page'], r['tag'], r['direction']) for r in scanner['candidates']}
    queue_keys = {(r['reader'], r['page'], r['tag'], r['direction']) for r in queue['final_candidates']}
    if scanner_keys != queue_keys or len(queue_keys) != len(queue['final_candidates']):
        unresolved.append({'scope': 'final scanner inventory', 'reason': 'Prepared final candidate coverage differs from the complete scanner output.'})
    if {r['reader']: r['sha256'] for r in scanner['files']} != frozen:
        unresolved.append({'scope': 'final scanner inventory', 'reason': 'Final scanner PDF hashes differ from the current publication PDFs.'})
    if any(r.get('pages') != actual_page_counts.get(r['reader']) for r in scanner['files']):
        unresolved.append({'scope': 'final scanner inventory', 'reason': 'Final scanner page counts differ from the actual current PDFs.'})
    expected_known = {known_id(r) for r in baseline['candidates'] if r['decision'] == 'confirmed detached tag'}
    if (len(queue['known_detachments']) != 80 or
            len({r['id'] for r in queue['known_detachments']}) != 80 or
            {r['id'] for r in queue['known_detachments']} != expected_known):
        unresolved.append({'scope': 'known detachment inventory', 'reason': 'Prepared known-instance coverage differs from the 80 baseline defects.'})
    known, final_candidates = [], []
    for item in queue['known_detachments']:
        ob = supplied.get(item['id'])
        issues = check_observation(item, ob, 'RESOLVED_ON_FINAL_PDF')
        if item['source_resolution_status'] != 'EXACT_APPLIED_SOURCE_BINDING':
            issues.append('Exact applied source binding is not qualified.')
        source = item.get('source', {})
        if not source.get('sha256') or sha(ROOT / source['path']) != source['sha256']:
            issues.append('Immutable source witness is absent or changed.')
        if not (ROOT / item['before_image']).is_file() or sha(ROOT / item['before_image']) != item['before_image_sha256']:
            issues.append('Historical before-image evidence is absent or changed.')
        out = dict(item, status='UNRESOLVED' if issues else 'RESOLVED_ON_FINAL_PDF',
                   final_observation=ob, validation_errors=issues,
                   prepared_candidate_pages=item.get('final_pages', []),
                   final_pages=sorted(set(ob['display_pages'] + [ob['tag_page']])) if not issues else [],
                   prepared_images=item.get('images', []), images=ob['images'] if not issues else [])
        known.append(out)
        for reason in issues:
            unresolved.append({'id': item['id'], 'reason': reason})
    primary_by_key = {}
    for item in queue['final_candidates']:
        if item['reader'] in MASTER_SOURCE:
            continue
        ob = supplied.get(item['id'])
        issues = check_observation(item, ob, 'CLEARED_ON_FINAL_PDF')
        out = dict(item, status='UNRESOLVED' if issues else 'CLEARED_ON_FINAL_PDF',
                   final_observation=ob, validation_errors=issues)
        final_candidates.append(out)
        primary_by_key[(item['reader'], item['page'], item['tag'], item['direction'])] = out
        for reason in issues:
            unresolved.append({'id': item['id'], 'reason': reason})
    comparison_results = []
    comparisons = {}
    for master, path in COMPARISONS.items():
        issues = []
        if not (ROOT / path).is_file():
            issues.append('Required all-page master comparison is absent.')
            data = {}
        else:
            data = read(path)
            if data.get('source_pdf_sha256') != frozen[MASTER_SOURCE[master]] or data.get('target_pdf_sha256') != frozen[master]:
                issues.append('Master comparison belongs to different PDF hashes.')
            if not data.get('every_corresponding_page_compared') or not data.get('page_counts_equal'):
                issues.append('All corresponding master pages have not been compared.')
            if (data.get('source_pages') != actual_page_counts[MASTER_SOURCE[master]] or
                    data.get('target_pages') != actual_page_counts[master]):
                issues.append('Master comparison page counts differ from the actual current source/master PDFs.')
            if any(p != 1 for p in data.get('different_or_missing_pages', [])):
                issues.append('An apparatus/master page beyond the separately reviewed title differs.')
            if len(data.get('pages', [])) != data.get('source_pages'):
                issues.append('Per-page master comparison inventory is incomplete.')
            if {r['page'] for r in data.get('pages', [])} != set(range(1, data.get('source_pages', 0) + 1)):
                issues.append('Master comparison page sequence is incomplete or duplicated.')
            if any(not r.get('identical_pixels') and r['page'] != 1 for r in data.get('pages', [])):
                issues.append('A per-page pixel comparison differs beyond the title page.')
        comparisons[master] = (data, issues)
        comparison_results.append({'master': master, 'path': path,
                                   'sha256': sha(ROOT / path) if (ROOT / path).is_file() else None,
                                   'source_pdf_sha256': data.get('source_pdf_sha256'),
                                   'target_pdf_sha256': data.get('target_pdf_sha256'),
                                   'status': 'FAIL' if issues else 'PASS', 'validation_errors': issues})
        for reason in issues:
            unresolved.append({'scope': master, 'reason': reason})
    for item in queue['final_candidates']:
        if item['reader'] not in MASTER_SOURCE:
            continue
        master = item['reader']
        data, comparison_issues = comparisons[master]
        issues = list(comparison_issues)
        primary = primary_by_key.get((MASTER_SOURCE[master], item['page'], item['tag'], item['direction']))
        if not primary or primary['status'] != 'CLEARED_ON_FINAL_PDF':
            issues.append('Corresponding primary candidate lacks an actual cleared review.')
        pixels = {r['page']: r for r in data.get('pages', [])}
        if any(not pixels.get(p, {}).get('identical_pixels') for p in (item['page'], item['adjacent_page'])):
            issues.append('Candidate end/start master pages lack exact pixel identity.')
        out = dict(item, status='UNRESOLVED' if issues else 'CLEARED_BY_MASTER_PIXEL_IDENTITY',
                   source_candidate_id=primary['id'] if primary else None,
                   master_comparison=COMPARISONS[master], validation_errors=issues)
        final_candidates.append(out)
        for reason in issues:
            unresolved.append({'id': item['id'], 'reason': reason})
    expected_observation_ids = expected_known | {r['id'] for r in queue['final_candidates'] if r['reader'] not in MASTER_SOURCE}
    for unknown in set(supplied) - expected_observation_ids:
        unresolved.append({'id': unknown, 'reason': 'Observation is outside the prepared final review inventory.'})
    after = {book: sha(ROOT / 'work/build' / (book + '.pdf')) for book in BOOKS}
    if frozen != after:
        unresolved.append({'scope': 'PDF inventory', 'reason': 'A PDF changed while finalizing the audit.'})
    heading_reference = {'path': HEADING_AUDIT, 'status': 'NOT_YET_AVAILABLE',
                         'scope': 'Separate heading closure gate, including the C3:548 V/Preliminary opening; not counted as an equation-tag instance.'}
    if (ROOT / HEADING_AUDIT).is_file():
        heading = read(HEADING_AUDIT)
        heading_readers = heading.get('readers', [])
        heading_reference.update(sha256=sha(ROOT / HEADING_AUDIT), status=heading.get('status'),
                                 readers=heading_readers,
                                 current_pdf_hashes_match=bool(heading_readers) and all(
                                     r.get('sha256') == frozen.get(Path(r.get('file', '')).stem)
                                     for r in heading_readers))
    result = {'schema': 'pagination-verification-v1', 'status': 'FAIL' if unresolved else 'PASS', 'generated_at_utc': now(),
              'scope': 'All seven publication PDFs; actual final-image closure of 80 previously confirmed detachment instances, actual inspection of every final primary scanner candidate, and exact all-page apparatus/master pixel identity for master duplicate coverage.',
              'queue': {'path': args.queue, 'sha256': sha(ROOT / args.queue)},
              'files': [dict(r, stable_during_audit=(prepared == frozen == after),
                             sha256_after=after[r['reader']]) for r in queue['files']],
              'baseline': queue['baseline'], 'source_bindings': queue['source_bindings'],
              'applied_repairs': queue['applied_repairs'], 'scanner': queue['scanner'],
              'source_reconciliation': queue['source_reconciliation'],
              'known_detachments': known, 'final_candidates': final_candidates,
              'master_comparisons': comparison_results, 'observation_records': observation_records,
              'related_heading_verification': heading_reference,
              'counts': {'known_detachments': len(known),
                         'resolved_known_detachments': sum(r['status'] == 'RESOLVED_ON_FINAL_PDF' for r in known),
                         'final_primary_candidates': len(primary_by_key),
                         'cleared_primary_candidates': sum(r['status'] == 'CLEARED_ON_FINAL_PDF' for r in final_candidates),
                         'final_master_candidates': sum(r['reader'] in MASTER_SOURCE for r in final_candidates),
                         'cleared_master_candidates': sum(r['status'] == 'CLEARED_BY_MASTER_PIXEL_IDENTITY' for r in final_candidates),
                         'unresolved': len(unresolved)},
              'unresolved': unresolved, 'observations_generated_by_script': False}
    write(args.output, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('source-preflight', 'prepare'):
        command = commands.add_parser(name)
        command.add_argument('--baseline', default=BASELINE)
        command.add_argument('--bindings', default=BINDINGS)
        command.add_argument('--applied', default=APPLIED)
        command.add_argument('--reconciliation', default=RECONCILIATION)
        command.add_argument('--source-overrides')
        command.add_argument('--output', default=QUEUE if name == 'prepare' else 'work/data/pagination_source_preflight.json')
        if name == 'prepare':
            command.add_argument('--scanner-output', default=SCANNER)
            command.add_argument('--proof-dir', default=PROOFS)
    command = commands.add_parser('finalize')
    command.add_argument('--queue', default=QUEUE)
    command.add_argument('--observations', action='append')
    command.add_argument('--output', default=OUTPUT)
    args = parser.parse_args()
    # Imports share project-relative paths with the existing verified tools.
    # This tool therefore requires the project root as its working directory.
    if Path.cwd().resolve() != ROOT:
        parser.error('Run this tool from the project root.')
    try:
        result = {'source-preflight': source_preflight, 'prepare': prepare, 'finalize': final_report}[args.command](args)
    except Exception as error:
        if args.command == 'finalize':
            # Never leave an older PASS artifact in place after an incomplete
            # finalization. Detailed diagnostics remain in the local execution
            # result; the delivered failure record contains no private paths.
            write(args.output, {'schema': 'pagination-verification-v1', 'status': 'FAIL',
                                'generated_at_utc': now(), 'files': [], 'known_detachments': [],
                                'final_candidates': [], 'counts': {'resolved_known_detachments': 0},
                                'unresolved': [{'scope': 'audit execution',
                                    'reason': 'Finalization could not complete (' + type(error).__name__ + '); no PASS is issued.'}],
                                'observations_generated_by_script': False})
        raise
    print(json.dumps({'status': result['status'], 'output': args.output,
                      'counts': result.get('counts', {'source_resolved': result.get('resolved_source_count')})}))
    if result['status'] == 'FAIL':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
