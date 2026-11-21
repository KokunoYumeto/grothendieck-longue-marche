"""Read-only method/documentation audit; writes only reader_a QA artifacts.

Does not assemble, adjudicate, change accepted records/pages, or modify frozen TSVs.
No OCR, image recognition, research or TeX compilation.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
from PIL import Image
import csv
import hashlib
import io
import json
import re
import stat
import zipfile

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
OUT = ROOT / 'result'
QA = OUT / 'qa'
ID = 'SP83_C13_148+149'
EXPECTED_PENDING = {'148_scan068', '148_scan069', '148_scan071', '148_scan072', '149_scan003', '149_scan004'}
csv.field_size_limit(16 * 1024 * 1024)
START = datetime.now(timezone.utc).isoformat()
findings = []
checks = []
snapshots = {}

def relative(path):
    path = Path(path)
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)

def raw(path):
    path = Path(path)
    data = path.read_bytes()
    snapshots[relative(path)] = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data), 'mtime_ns': path.stat().st_mtime_ns}
    return data

def doc(path):
    return json.loads(raw(path))

def rows(path, delimiter='\t'):
    data = raw(path).decode('utf-8-sig')
    reader = csv.DictReader(io.StringIO(data), delimiter=delimiter)
    result = list(reader)
    return reader.fieldnames, result

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def add(code, severity, summary, evidence=None, action=None, pages=None, status='open'):
    findings.append({'id': code, 'severity': severity, 'status': status, 'summary': summary,
                     'pages': pages or [], 'evidence': evidence or [], 'action': action or ''})

def check(name, passed, detail):
    checks.append({'check': name, 'passed': bool(passed), 'detail': detail})

def norm_reader(value):
    return str(value).rstrip('/').split('/')[-1] if value else None

def walk(value, location=''):
    if isinstance(value, dict):
        yield location, value
        for key, child in value.items():
            yield from walk(child, location + '/' + str(key))
    elif isinstance(value, list):
        for n, child in enumerate(value):
            yield from walk(child, location + '/' + str(n))

def resolve(value):
    if not isinstance(value, str) or not value:
        return None
    value = value.split(' (', 1)[0]
    p = Path(value)
    if p.is_absolute():
        return p
    if value.startswith(('crops/', 'second/', 'pages/', 'records/', 'scripts/')):
        return OUT / value
    if value.startswith(('result/', 'source/', 'proposed/', 'halves/', 'transport/')):
        return ROOT / value
    return None

def resolve_image(value):
    if not isinstance(value, str) or len(value) > 400 or not re.fullmatch(r'[\w/+.:-]+\.(?:png|webp|jpg|jpeg)', value, re.I):
        return None
    p = resolve(value)
    if p is not None:
        return p
    for base in (OUT / 'crops', OUT / 'second', ROOT / 'proposed'):
        if (base / value).is_file():
            return base / value
    return None

def image_bounds(page, bounds):
    if not isinstance(bounds, (list, tuple)) or len(bounds) != 4:
        return False
    if not all(isinstance(v, (int, float)) for v in bounds):
        return False
    w, h = sizes[page]
    return 0 <= bounds[0] < bounds[2] <= w and 0 <= bounds[1] < bounds[3] <= h

order = raw(OUT / 'page_order.txt').decode().splitlines()
records = {page: doc(OUT / 'records' / (page + '.json')) for page in order}
proposals = {page: doc(ROOT / 'proposed' / (page + '.json')) for page in order}
source_images = {p.stem: p for p in (ROOT / 'source' / (ID + '_scans')).glob('*.jpg')}
sizes = {page: Image.open(source_images[page]).size for page in order}
check('23-page ordered scope', len(order) == len(set(order)) == 23 and set(order) == set(source_images),
      {'ordered_pages': order, 'original_scan_count': len(source_images)})

assignment_header, assignments = rows(OUT / 'second/assignments.tsv')
assignment_by_page = {row['page']: row for row in assignments}
check('Assignment rows cover all pages once', len(assignments) == 23 and set(assignment_by_page) == set(order),
      {'rows': len(assignments), 'unique_pages': len(assignment_by_page), 'columns': assignment_header})

page_results = []
second_docs = {}
all_crop_references = []
manifest_crops = []
frozen_hash_mismatches = []
first_snapshot_mismatches = []
comparison_mismatches = []
manifest_issues = []
assignment_issues = []
adjudication_issues = []
record_crop_issues = []
stale_decision_rows = []
boundary_notes = []

for page in order:
    record = records[page]
    files = {kind: OUT / 'second' / f'{page}_{kind}.tsv' for kind in ('boxes', 'first', 'second')}
    table = {}
    issues = []
    for kind, path in files.items():
        header, items = rows(path)
        table[kind] = items
        expected_header = ['box', 'kind', 'x0', 'y0', 'x1', 'y1'] if kind == 'boxes' else ['box', 'reading']
        if header != expected_header:
            issues.append({'file': relative(path), 'issue': 'Wrong columns', 'actual': header})
        if len({r['box'] for r in items}) != len(items):
            issues.append({'file': relative(path), 'issue': 'Duplicate box IDs'})
        if kind != 'boxes' and any(not r.get('reading', '').strip() for r in items):
            issues.append({'file': relative(path), 'issue': 'Empty reading'})
    ids = [r['box'] for r in table['boxes']]
    if any([r['box'] for r in table[k]] != ids for k in ('first', 'second')):
        issues.append({'issue': 'Box/first/second rows differ in membership or order'})
    if ids != [f'B{n:02}' for n in range(1, len(ids) + 1)]:
        issues.append({'issue': 'Unexpected box ID sequence', 'ids': ids})
    bounds_by_box = {r['box']: [int(r[k]) for k in ('x0', 'y0', 'x1', 'y1')] for r in table['boxes']}
    for box, bounds in bounds_by_box.items():
        if not image_bounds(page, bounds):
            issues.append({'issue': 'Invalid/out-of-image original box', 'box': box, 'bounds': bounds})
    if len(set(tuple(v) for v in bounds_by_box.values())) != len(ids):
        issues.append({'issue': 'Duplicate exact rectangles in prescribed boxes'})
    first_by_box = {r['box']: r['reading'] for r in table['first']}
    second_by_box = {r['box']: r['reading'] for r in table['second']}
    record_first = {r['box']: r.get('reading', '') for r in record.get('second_boxes', [])}
    if record_first != first_by_box:
        first_snapshot_mismatches.append({'page': page, 'boxes': sorted(k for k in set(record_first) | set(first_by_box) if record_first.get(k) != first_by_box.get(k))})

    docs = {}
    for p in (OUT / 'second').glob(page + '*.json'):
        if any(token in p.name for token in ('comparison', 'main_decisions', 'main_detail')):
            continue
        docs[p.name] = doc(p)
    second_docs[page] = docs
    note_readers = set()
    stored_hashes = []
    for filename, data in docs.items():
        if isinstance(data, dict):
            for key in ('reader', 'second_reader', 'independent_reader'):
                if data.get(key):
                    note_readers.add(norm_reader(data[key]))
        for loc, item in walk(data):
            for key, value in item.items():
                if not isinstance(value, str) or not re.fullmatch(r'[a-fA-F0-9]{64}', value):
                    continue
                low = key.lower()
                if loc == '' and ('tsv' in low or 'second' in low or 'frozen' in low or low in ('sha256', 'sha')):
                    stored_hashes.append({'source': 'result/second/' + filename, 'field': key, 'sha256': value.lower()})
            if loc == '' and any('boundary' in str(k).lower() or 'clipp' in str(k).lower() for k in item):
                boundary_notes.append({'page': page, 'file': 'result/second/' + filename,
                                       'fields': {k: v for k, v in item.items() if 'boundary' in k.lower() or 'clipp' in k.lower()}})
    hash_file = OUT / 'second' / (page + '_second.sha256')
    if hash_file.exists():
        stored_hashes.append({'source': relative(hash_file), 'field': 'checksum file', 'sha256': raw(hash_file).decode().split()[0].lower()})
    audit = record.get('audit', {})
    if audit.get('second_reading_sha256'):
        stored_hashes.append({'source': f'result/records/{page}.json', 'field': 'audit.second_reading_sha256', 'sha256': audit['second_reading_sha256']})
    current_hash = snapshots[relative(files['second'])]['sha256']
    for item in stored_hashes:
        if item['sha256'] != current_hash:
            frozen_hash_mismatches.append({'page': page, 'actual': current_hash, **item})
    actual_reader = norm_reader(audit.get('reader')) or (next(iter(note_readers)) if len(note_readers) == 1 else None)
    first_reader = norm_reader(record.get('reader'))
    assignment = assignment_by_page.get(page, {})
    for key, expected in [('first_reader', first_reader), ('second_reader', actual_reader)]:
        if assignment.get(key) != expected:
            assignment_issues.append({'page': page, 'field': key, 'ledger': assignment.get(key), 'recorded_actual': expected})
    if first_reader == actual_reader or not actual_reader or (note_readers and note_readers != {actual_reader}):
        assignment_issues.append({'page': page, 'issue': 'Reader independence or identity evidence conflict', 'first': first_reader, 'audit': audit.get('reader'), 'notes_readers': sorted(note_readers)})
    if norm_reader(proposals[page].get('reader')) != first_reader:
        assignment_issues.append({'page': page, 'issue': 'Accepted first-reader identity differs from proposal'})

    manifest_path = OUT / 'second' / (page + '_second_crop_manifest.json')
    manifest = docs.get(manifest_path.name)
    entries = manifest if isinstance(manifest, list) else manifest.get('crops', []) if isinstance(manifest, dict) else []
    manifest_by_box = {entry['box']: entry for entry in entries if isinstance(entry, dict) and 'box' in entry}
    if set(manifest_by_box) != set(ids) or len(entries) != len(ids):
        manifest_issues.append({'page': page, 'issue': 'Canonical manifest does not exactly cover box list', 'entry_count': len(entries), 'box_count': len(ids)})
    view_claim = False
    view_claim_sources = []
    for filename, data in docs.items():
        if not isinstance(data, dict):
            continue
        encoded = json.dumps(data, ensure_ascii=False).lower()
        if (any(data.get(k) is True for k in ('all_canonical_crops_directly_viewed', 'all_prescribed_crops_directly_viewed',
                                             'all_fresh_exact_box_crops_viewed', 'canonical_crops_all_directly_viewed',
                                             'all_prescribed_fields_directly_viewed'))
                or data.get('canonical_crops_directly_viewed') == len(ids)
                or re.search(r'all (?:\w+ )?(?:exact-box |prescribed |canonical )?crops.{0,70}(?:directly|successfully).{0,50}view', encoded)
                or re.search(r'view.{0,25}(?:all|every) (?:canonical |prescribed )?crop', encoded)):
            view_claim = True
            view_claim_sources.append('result/second/' + filename)
    unasserted = []
    for box in ids:
        canonical = OUT / 'crops' / f'{page}_second_{box}.png'
        entry = manifest_by_box.get(box, {})
        if not canonical.is_file():
            manifest_issues.append({'page': page, 'box': box, 'issue': 'Missing canonical crop', 'path': relative(canonical)})
        else:
            with Image.open(canonical) as im:
                im.verify()
        declared_bounds = entry.get('original_box', entry.get('rect', entry.get('source_rect')))
        if declared_bounds != bounds_by_box[box]:
            manifest_issues.append({'page': page, 'box': box, 'issue': 'Manifest original coordinates differ from prescribed box', 'manifest': declared_bounds, 'prescribed': bounds_by_box[box]})
        declared_path = resolve(entry.get('path'))
        if declared_path and declared_path != canonical:
            manifest_issues.append({'page': page, 'box': box, 'issue': 'Manifest canonical path differs from required path', 'declared': str(declared_path)})
        for key in ('sha256', 'canonical_sha256'):
            if entry.get(key) and canonical.exists() and sha(canonical) != entry[key]:
                manifest_issues.append({'page': page, 'box': box, 'issue': 'Canonical crop hash mismatch', 'field': key})
        if not (entry.get('viewed') is True or entry.get('directly_viewed') is True or entry.get('actual_view', {}).get('success') is True or view_claim):
            unasserted.append(box)
        manifest_crops.append({'page': page, 'box': box, 'path': relative(canonical), 'original_box': bounds_by_box[box], 'view_flag': entry.get('viewed'), 'page_view_claim': view_claim})
    if unasserted:
        manifest_issues.append({'page': page, 'issue': 'No machine-detected per-crop/page-wide successful view statement', 'boxes': unasserted, 'manual_documentation_review_needed': True})

    comparison_path = OUT / 'second' / (page + '_comparison.json')
    comparison = doc(comparison_path) if comparison_path.exists() else None
    differing = set()
    if comparison is not None:
        if [r['box'] for r in comparison] != ids:
            comparison_mismatches.append({'page': page, 'issue': 'Comparison row order/membership differs'})
        for item in comparison:
            box = item['box']
            if item.get('first') != first_by_box.get(box) or item.get('second') != second_by_box.get(box):
                comparison_mismatches.append({'page': page, 'box': box, 'issue': 'Comparison does not preserve exact frozen inputs'})
            if not item.get('same_tokens'):
                differing.add(box)
    adjudication_path = OUT / 'second' / (page + '_adjudication.tsv')
    adjudications = rows(adjudication_path)[1] if adjudication_path.exists() else None
    if audit:
        if comparison is None or adjudications is None:
            adjudication_issues.append({'page': page, 'issue': 'Finalized audit lacks comparison/adjudication'})
        else:
            if len(adjudications) != len(differing) or {r['box'] for r in adjudications} != differing:
                adjudication_issues.append({'page': page, 'issue': 'Adjudication does not cover exactly all differing boxes'})
            for item in adjudications:
                box = item['box']
                if item.get('first') != first_by_box.get(box) or item.get('second') != second_by_box.get(box):
                    adjudication_issues.append({'page': page, 'box': box, 'issue': 'Adjudication snapshots differ from frozen TSVs'})
                if item.get('main_reader_reviewed') != 'yes' or not item.get('evidence', '').strip():
                    adjudication_issues.append({'page': page, 'box': box, 'issue': 'Missing visual review/evidence assertion'})
                crop = resolve(item.get('crop'))
                if not crop or not crop.is_file():
                    adjudication_issues.append({'page': page, 'box': box, 'issue': 'Adjudication crop is missing', 'crop': item.get('crop')})
    elif page not in EXPECTED_PENDING:
        adjudication_issues.append({'page': page, 'issue': 'Unexpected unfinished audit'})

    reviewed = set(record.get('main_reader_crops', []))
    for group in ('changes', 'decisions', 'implicit_decisions'):
        for item in record.get(group, []):
            mandatory = bool(item.get('diff_c') or item.get('diff_h') or item.get('decision') in ('first', 'alternative', 'other'))
            crop_value = item.get('crop')
            crop = resolve(crop_value)
            location = item.get('id') or item.get('place', '')
            if mandatory and (not crop_value or crop_value == 'page'):
                record_crop_issues.append({'page': page, 'group': group, 'id': location, 'issue': 'Mandatory crop not supplied'})
            if crop_value and crop_value != 'page':
                all_crop_references.append({'page': page, 'group': group, 'id': location, 'crop': crop_value, 'box': item.get('box')})
                if crop is None or not crop.is_file():
                    record_crop_issues.append({'page': page, 'group': group, 'id': location, 'issue': 'Referenced crop missing', 'crop': crop_value})
                if not image_bounds(page, item.get('box')):
                    record_crop_issues.append({'page': page, 'group': group, 'id': location, 'issue': 'Missing or invalid original pixel box', 'box': item.get('box'), 'crop': crop_value})
                if mandatory and crop_value not in reviewed:
                    record_crop_issues.append({'page': page, 'group': group, 'id': location, 'issue': 'Mandatory crop absent from accepted main-reader review registry', 'crop': crop_value})

    page_results.append({'page': page, 'first_reader': first_reader, 'second_reader': actual_reader,
                         'assignment': assignment, 'box_count': len(ids), 'row_issues': issues,
                         'first_sha256': snapshots[relative(files['first'])]['sha256'],
                         'second_sha256': current_hash, 'second_recorded_hash_count': len(stored_hashes),
                         'second_recorded_hashes': stored_hashes,
                         'first_snapshot_matches_record': record_first == first_by_box,
                         'comparison_present': comparison is not None, 'different_boxes': len(differing) if comparison is not None else None,
                         'adjudication_present': adjudications is not None, 'audit_finalized': bool(audit),
                         'expected_pending_at_assignment': page in EXPECTED_PENDING,
                         'second_file_mode': oct(files['second'].stat().st_mode & 0o777),
                         'first_file_mode': oct(files['first'].stat().st_mode & 0o777)})

row_issues = [{'page': r['page'], **i} for r in page_results for i in r['row_issues']]
check('Exact first/second box coverage, order and nonempty readings', not row_issues,
      {'pages': len(page_results), 'boxes': sum(r['box_count'] for r in page_results), 'issues': row_issues})
check('First reading snapshots preserved in accepted metadata', not first_snapshot_mismatches, first_snapshot_mismatches)
check('Recorded second-reading hashes match frozen TSVs', not frozen_hash_mismatches,
      {'hash_references_checked': sum(r['second_recorded_hash_count'] for r in page_results), 'mismatches': frozen_hash_mismatches,
       'pages_without_a_separate_recorded_hash': [r['page'] for r in page_results if not r['second_recorded_hash_count']]})
check('Comparison preserves complete frozen readings', not comparison_mismatches, comparison_mismatches)
check('Finalized visual adjudication records complete', not adjudication_issues, adjudication_issues)
check('Different first and second readers, consistent assignments', not assignment_issues, assignment_issues)
check('Canonical crop existence, coordinates, hash and view documentation', not manifest_issues, manifest_issues)
check('First-reading decision/change crops exist with boxes and review registration', not record_crop_issues,
      {'references_checked': len(all_crop_references), 'issues': record_crop_issues})

if assignment_issues:
    add('A01', 'action_required', 'Assignment ledger identity mismatch', assignment_issues,
        'Correct only the assignment metadata to match the accepted first-reader record and frozen independent reader; leave both TSVs unchanged.',
        sorted({i['page'] for i in assignment_issues}))
elif assignment_by_page.get('149_scan004', {}).get('first_reader') == 'reader_b' and assignment_by_page.get('149_scan004', {}).get('second_reader') == 'reader_a':
    add('R01', 'resolved_during_audit', 'Reversed 149_scan004 assignment row corrected during audit',
        {'initial_observation': 'The first read of assignments.tsv listed first_reader=reader_a and second_reader=reader_b for 149_scan004. The accepted record and proposal named reader_b, and the frozen second notes named reader_a.',
         'current_assignment': assignment_by_page['149_scan004'],
         'audit_action': 'Reader_a notified root; reader_a did not edit the ledger.'},
        'No further action: the current ledger matches both reader records.', ['149_scan004'], status='resolved')
for code, title, items, action in [
    ('A02', 'Box/TSV structure or order mismatch', row_issues, 'Review the listed structural mismatch without changing a frozen reading after comparison.'),
    ('A03', 'First snapshot metadata differs from frozen first.tsv', first_snapshot_mismatches, 'Preserve frozen first.tsv; explain or repair only mistaken metadata.'),
    ('A04', 'Stored frozen second-reading hash mismatch', frozen_hash_mismatches, 'Stop final packaging until the unchanged independent snapshot is identified and the discrepancy explained.'),
    ('A05', 'Comparison snapshots differ from frozen readings', comparison_mismatches, 'Regenerate comparison only from unchanged frozen TSVs, then recheck adjudication associations.'),
    ('A06', 'Finalized audit documentation incomplete', adjudication_issues, 'Complete or correct the listed audit documentation.'),
    ('A07', 'Canonical crop documentation needs review', manifest_issues, 'Review the listed manifest/view documentation issue; do not infer a successful view from a generated file alone.'),
    ('A08', 'Required evidence crop reference or provenance gap', record_crop_issues, 'Repair evidence metadata or retain a justified uncertainty; do not silently assert an unperformed crop view.'),
]:
    if items:
        add(code, 'action_required', title, items, action, sorted({i['page'] for i in items if 'page' in i}))

# Exact MARKS coverage, order and per-page ownership.
marks_header, marks = rows(ROOT / 'source' / (ID + '_texts') / 'MARKS.tsv')
decision_header, decisions = rows(OUT / 'decisions.tsv')
mark_ids = [r['id'] for r in marks]
decision_ids = [r['id'] for r in decisions]
mark_map = {r['id']: r for r in marks}
decision_map = {r['id']: r for r in decisions}
record_decisions = [(page, d) for page in order for d in records[page].get('decisions', [])]
record_ids = [d['id'] for page, d in record_decisions]
mark_issues = []
expected_decision_header = ['id', 'cote', 'scan', 'decision', 'reading', 'what the ink shows', 'crop', 'confidence']
if len(marks) != 261 or len(decisions) != 261 or decision_ids != mark_ids or len(set(decision_ids)) != 261:
    mark_issues.append({'issue': 'Global decisions do not exactly cover all 261 supplied marks once in original order'})
if decision_header != expected_decision_header:
    mark_issues.append({'issue': 'Decision columns differ', 'actual': decision_header})
if Counter(record_ids) != Counter(mark_ids):
    mark_issues.append({'issue': 'Page records do not exactly own all supplied mark IDs once',
                        'extra': list((Counter(record_ids) - Counter(mark_ids)).elements()),
                        'missing': list((Counter(mark_ids) - Counter(record_ids)).elements())})
for page, d in record_decisions:
    expected_page = None
    m = mark_map.get(d['id'])
    if m:
        expected_page = f"{m['cote']}_scan{int(m['scan']):03}"
    if expected_page != page:
        mark_issues.append({'page': page, 'id': d['id'], 'issue': 'Mark assigned to wrong page', 'expected_page': expected_page})
    exported = decision_map.get(d['id'], {})
    if any(exported.get(k) != str(d.get(k, '')) for k in ('decision', 'reading', 'confidence')):
        stale_decision_rows.append({'page': page, 'id': d['id'], 'fields': [k for k in ('decision', 'reading', 'confidence') if exported.get(k) != str(d.get(k, ''))]})
    if d.get('decision') not in ('first', 'alternative', 'other', 'undecided'):
        mark_issues.append({'page': page, 'id': d['id'], 'issue': 'Invalid decision value', 'value': d.get('decision')})
    if d.get('confidence') not in ('high', 'medium', 'low'):
        mark_issues.append({'page': page, 'id': d['id'], 'issue': 'Invalid confidence'})
    if not d.get('reading') or not d.get('evidence'):
        mark_issues.append({'page': page, 'id': d['id'], 'issue': 'Missing reading or ink evidence'})
check('All 261 supplied C mark IDs occur once in original order', not mark_issues,
      {'source_marks': len(marks), 'exported_decisions': len(decisions), 'record_decisions': len(record_decisions), 'issues': mark_issues})
if mark_issues:
    add('A09', 'action_required', 'Supplied C mark decision coverage issue', mark_issues, 'Repair decision metadata while retaining original MARKS order and IDs.')
if stale_decision_rows:
    add('P01', 'expected_pending', 'Aggregate decision export awaits final refresh', stale_decision_rows,
        'After all adjudications, run the root-controlled assembly and repeat exact MARKS coverage checks.', sorted({r['page'] for r in stale_decision_rows}))

# Deliverable presence and mandatory table schemas/values.
required_files = [ID + suffix for suffix in ('_transcription.tex', '_changes.md', '_collation.tsv', '_doubts.md', '_inventory.csv', '_notes.md', '_sheet_feedback.md', '_hand_log.md')]
required_files += ['decisions.tsv', 'CHECK_EVENTS.tsv', 'progress.log', 'page_order.txt']
missing_required = [name for name in required_files if not (OUT / name).is_file() or not (OUT / name).stat().st_size]
accepted_pages = {p.stem for p in (OUT / 'pages').glob('*.tex')}
check('Required aggregate files and 23 accepted page files exist', not missing_required and accepted_pages == set(order),
      {'missing_or_empty': missing_required, 'page_files': len(accepted_pages), 'extra_pages': sorted(accepted_pages - set(order))})
schema_issues = []
inventory_header, inventory = rows(OUT / (ID + '_inventory.csv'), ',')
expected_inventory_header = ['scan', 'sheet_kind', 'hand', 'element', 'kind', 'position', 'first_words_or_objects', 'transcribed']
if inventory_header != expected_inventory_header:
    schema_issues.append({'file': ID + '_inventory.csv', 'issue': 'Wrong inventory columns'})
if set(r['scan'] for r in inventory) != set(order):
    schema_issues.append({'file': ID + '_inventory.csv', 'issue': 'Inventory does not cover all 23 pages'})
for row in inventory:
    if row.get('transcribed') != 'yes' or row.get('kind') not in ('text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'):
        schema_issues.append({'file': ID + '_inventory.csv', 'page': row.get('scan'), 'element': row.get('element'), 'issue': 'Invalid/unconfirmed inventory row'})
    if row.get('sheet_kind') not in ('text', 'reused_typed', 'typescript', 'letter', 'list', 'cancelled_draft', 'cover') or not row.get('hand'):
        schema_issues.append({'file': ID + '_inventory.csv', 'page': row.get('scan'), 'element': row.get('element'), 'issue': 'Invalid sheet kind or absent hand attribution'})
collation_header, collation = rows(OUT / (ID + '_collation.tsv'))
expected_collation_header = ['folder', 'their_page', 'our_scan', 'line', 'their_reading', 'codex_reading', 'final_reading', 'scan_shows', 'kind', 'marked_in_H', 'confidence']
if collation_header != expected_collation_header:
    schema_issues.append({'file': ID + '_collation.tsv', 'issue': 'Wrong collation columns'})
events_header, events = rows(OUT / 'CHECK_EVENTS.tsv')
if events_header != ['statement_id', 'date', 'who', 'type', 'outcome']:
    schema_issues.append({'file': 'CHECK_EVENTS.tsv', 'issue': 'Wrong event columns'})
for index, event in enumerate(events, 2):
    if any(not event.get(k, '').strip() for k in events_header):
        schema_issues.append({'file': 'CHECK_EVENTS.tsv', 'row': index, 'issue': 'Empty required check-event field'})
for name in (ID + '_changes.md', ID + '_notes.md'):
    text = raw(OUT / name).decode()
    headers = re.findall(r'^## ((?:148|149)_scan\d{3})\s*$', text, re.M)
    if headers != order:
        schema_issues.append({'file': name, 'issue': 'Per-page sections missing, duplicated or out of page order', 'headers': headers})
check('Required table schemas, inventory confirmations and per-page sections', not schema_issues,
      {'inventory_rows': len(inventory), 'collation_rows': len(collation), 'check_events': len(events), 'issues': schema_issues})
if missing_required or schema_issues:
    add('A10', 'action_required', 'Required deliverable/documentation structure gap', missing_required + schema_issues,
        'Complete the listed required structure during final root assembly; preserve frozen readings.')

# Progress chronology and expected unfinished work.
progress = raw(OUT / 'progress.log').decode()
done = re.findall(r'^scan (\d+) done ([0-9:-]+ [0-9:]+ UTC) cote (\d+):.*?first reader (reader_[abc])$', progress, re.M)
done_map = {f'{cote}_scan{int(scan):03}': {'time': time, 'reader': reader} for scan, time, cote, reader in done}
audited = re.findall(r'^scan (\d+) audited ([0-9:-]+ [0-9:]+ UTC):.*?cote (\d+); independent reader (reader_[abc])$', progress, re.M)
audit_map = {f'{cote}_scan{int(scan):03}': {'time': time, 'reader': reader} for scan, time, cote, reader in audited}
chronology_issues = []
if len(done) != 23 or set(done_map) != set(order):
    chronology_issues.append({'issue': 'Progress log does not contain exactly one accepted first-reading line per page', 'count': len(done)})
for page, record in records.items():
    if done_map.get(page, {}).get('reader') != record.get('reader'):
        chronology_issues.append({'page': page, 'issue': 'First-reader identity differs between accepted record and progress'})
    if bool(record.get('audit')) != (page in audit_map):
        chronology_issues.append({'page': page, 'issue': 'Audit record/progress mismatch'})
def utc(s):
    return datetime.strptime(s, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
last_done = max(utc(r['time']) for r in done_map.values())
first_assignment = min(utc(r['assigned_utc']) for r in assignments)
if first_assignment < last_done:
    chronology_issues.append({'issue': 'Blind assignment preceded acceptance of all first readings', 'first_assignment': first_assignment.isoformat(), 'last_first_acceptance': last_done.isoformat()})
check('Progress and first/second phase chronology', not chronology_issues,
      {'done_lines': len(done), 'audited_lines': len(audited), 'last_first_acceptance': last_done.isoformat(), 'first_blind_assignment': first_assignment.isoformat(), 'issues': chronology_issues})
if chronology_issues:
    add('A11', 'action_required', 'Progress/phase documentation mismatch', chronology_issues, 'Correct only inaccurate process metadata; do not invent missing events.')
pending_now = [r['page'] for r in page_results if not r['audit_finalized']]
add('P02', 'expected_pending', 'Root adjudication and final transcription freeze remain in progress',
    {'pending_at_snapshot': pending_now, 'expected_pending_from_assignment': sorted(EXPECTED_PENDING),
     'transcription_hashes_present': (OUT / 'transcription_hashes.tsv').exists(),
     'transcription_frozen_log_line_present': bool(re.search(r'^transcription frozen ', progress, re.M))},
    'Finish the outstanding visual adjudications, refresh aggregate deliverables, freeze all 24 transcription hashes, verify them unchanged, then create the final ZIP.', pending_now)

# Packaging simulation: package.py includes result/ (minus pycache/ZIPs), then proposed/ as work/proposed/.
package_files = [p for p in OUT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() != '.zip']
package_files += [p for p in (ROOT / 'proposed').glob('*') if p.is_file() and p.suffix.lower() != '.zip']
input_files = [p for p in (ROOT / 'source').rglob('*') if p.is_file()]
input_files += [p for p in (ROOT / 'halves').rglob('*') if p.is_file()]
input_by_size = defaultdict(list)
for p in input_files:
    input_by_size[p.stat().st_size].append(p)
byte_matches = []
for p in package_files:
    matches = input_by_size.get(p.stat().st_size, [])
    if not matches:
        continue
    h = sha(p)
    for source in matches:
        if sha(source) == h:
            byte_matches.append({'packaged_path': relative(p), 'input_path': relative(source), 'sha256': h})
input_images = [p for p in input_files if p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp')]
input_dimensions = defaultdict(list)
for p in input_images:
    try:
        with Image.open(p) as im:
            input_dimensions[im.size].append(p)
    except Exception:
        pass
pixel_matches = []
pixel_cache = {}
for p in package_files:
    if p.suffix.lower() not in ('.jpg', '.jpeg', '.png', '.webp'):
        continue
    with Image.open(p) as im:
        same_size = input_dimensions.get(im.size, [])
        if not same_size:
            continue
        h = hashlib.sha256(im.convert('RGB').tobytes()).hexdigest()
    for source in same_size:
        if source not in pixel_cache:
            with Image.open(source) as im:
                pixel_cache[source] = hashlib.sha256(im.convert('RGB').tobytes()).hexdigest()
        if pixel_cache[source] == h:
            pixel_matches.append({'packaged_path': relative(p), 'input_image': relative(source), 'pixel_sha256': h})
suspicious_names = []
for p in package_files:
    rel = relative(p)
    if p.name in ('C.tex', 'H.tex', 'MARKS.tsv', 'PREAMBLE.tex', 'images.json') or re.fullmatch(r'(148|149)_scan\d{3}\.jpe?g', p.name, re.I):
        suspicious_names.append(rel)
    if p.is_symlink() and any(parent.name in ('source', 'halves', 'packets') for parent in p.resolve().parents):
        suspicious_names.append(rel + ' -> ' + str(p.resolve()))
packaging_clean = not byte_matches and not pixel_matches and not suspicious_names
check('Packaged result/work trees exclude attached texts, originals and prepared halves', packaging_clean,
      {'candidate_files': len(package_files), 'input_files': len(input_files), 'input_images': len(input_images),
       'byte_identical_input_copies': byte_matches, 'pixel_identical_original_or_half_images': pixel_matches,
       'suspicious_input_names_or_symlinks': suspicious_names, 'root_work_directory_exists': (ROOT / 'work').exists(),
       'archive_work_proposed_source': 'proposed/ -> work/proposed/'})
if not packaging_clean:
    add('A12', 'action_required', 'Attached input or prepared half found in packaging tree',
        {'byte_matches': byte_matches, 'pixel_matches': pixel_matches, 'suspicious_names': suspicious_names},
        'Exclude attached source scans/texts and prepared halves from the final archive; do not delete source evidence from its source directory.')

# Retained crop provenance, including helpers whose coordinates are in a parent crop.
crop_files = [p for p in (OUT / 'crops').rglob('*') if p.is_file() and p.suffix.lower() in ('.png', '.webp')]
crop_files += list((OUT / 'second').glob('*.png'))
crop_documents = defaultdict(list)
crop_provenance = defaultdict(list)
declared_image_hashes = []
metadata_files = list((OUT / 'records').glob('*.json')) + list((OUT / 'second').glob('*.json')) + list((ROOT / 'proposed').glob('*.json'))
for path in metadata_files:
    if 'comparison' in path.name:
        continue
    data = doc(path)
    page_match = re.match(r'((?:148|149)_scan\d{3})_crop_boxes\.json$', path.name)
    if page_match and isinstance(data, dict):
        for name, bounds in data.items():
            if isinstance(bounds, list) and len(bounds) == 4 and all(isinstance(n, (int, float)) for n in bounds):
                image_path = OUT / 'crops' / f'{page_match[1]}_{name}.png'
                crop_provenance[image_path].append({'file': relative(path), 'location': '/' + name, 'coordinates': {'original_box': bounds}})
    for loc, item in walk(data):
        coordinate_fields = {k: v for k, v in item.items() if k in (
            'original_box', 'source_rect', 'rect', 'box', 'original_bbox', 'bounds',
            'canonical_pixel_subrect', 'rect_in_origin_pixels', 'rect_in_canonical_pixels', 'box_in_canonical',
            'canonical_crop_pixel_box'
        ) and isinstance(v, list) and len(v) == 4 and all(isinstance(n, (int, float)) for n in v)}
        derived = bool(coordinate_fields or item.get('within_canonical_box') or item.get('same_original_box') or item.get('source_canonical_crop') or item.get('origin'))
        for key, value in item.items():
            image_path = resolve_image(value)
            if image_path is None:
                continue
            evidence = {'file': relative(path), 'location': loc + '/' + key}
            crop_documents[image_path].append(evidence)
            if derived:
                crop_provenance[image_path].append(dict(evidence, coordinates=coordinate_fields,
                    origin=item.get('origin', item.get('source_canonical_crop')), within_canonical_box=item.get('within_canonical_box')))
            if key == 'path' and isinstance(item.get('sha256'), str) and re.fullmatch(r'[a-f0-9]{64}', item['sha256']):
                declared_image_hashes.append({'path': image_path, 'sha256': item['sha256'], 'file': relative(path), 'location': loc})
script_files = list((ROOT / 'proposed').glob('*.py')) + list((OUT / 'scripts').glob('*.py')) + list((OUT / 'second').glob('*.py'))
script_texts = {p: p.read_text() for p in script_files}
# These four dynamic filenames were inspected directly in the retained generator.
# The source is a canonical audit crop; rectangles are in that crop's pixels.
for name, parent, bounds in [('upper', 'B24', [350, 600, 2480, 1450]),
                             ('middle', 'B24', [0, 1200, 2400, 2100]),
                             ('lower', 'B25', [0, 600, 2350, 1850]),
                             ('end', 'B25', [0, 1400, 2300, 2700])]:
    path = OUT / 'crops' / ('148_scan053_second_detail_' + name + '.png')
    crop_provenance[path].append({'file': 'result/scripts/148_scan053_second_details.py',
        'source': 'crops/148_scan053_second_' + parent + '.png', 'canonical_pixel_subrect': bounds,
        'additional_scale': 1.5, 'audit_note': 'Read directly from retained parts list and save pattern; no generator rerun.'})
generator_only = []
unlocated_crop_provenance = []
for p in crop_files:
    if p in crop_provenance:
        continue
    page_match = re.match(r'((?:148|149)_scan\d{3})_(.+)', p.stem)
    matches = []
    if page_match:
        page, suffix = page_match.groups()
        for script, text in script_texts.items():
            if page not in script.name and page not in text:
                continue
            if p.name in text or repr(suffix) in text or ('"' + suffix + '"') in text:
                matches.append(relative(script))
    if matches:
        generator_only.append({'crop': relative(p), 'generator_references': matches})
    else:
        page = re.match(r'((?:148|149)_scan\d{3})_', p.name)
        page = page[1] if page else None
        registered = bool(page and 'crops/' + p.name in records[page].get('main_reader_crops', []))
        mandatory_reference = any(r['crop'] == 'crops/' + p.name for r in all_crop_references)
        unlocated_crop_provenance.append({'crop': relative(p), 'json_references': crop_documents.get(p, []),
            'main_reader_view_registry_contains_crop': registered,
            'used_by_accepted_change_or_mark_evidence': mandatory_reference})
image_hash_issues = []
seen_image_hashes = set()
for item in declared_image_hashes:
    identity = (str(item['path']), item['sha256'])
    if identity in seen_image_hashes:
        continue
    seen_image_hashes.add(identity)
    if not item['path'].is_file() or sha(item['path']) != item['sha256']:
        image_hash_issues.append({**item, 'path': relative(item['path'])})
check('Retained crop/helper provenance and stored image hashes', not unlocated_crop_provenance and not image_hash_issues,
      {'retained_crop_images': len(crop_files), 'metadata_provenance_count': sum(p in crop_provenance for p in crop_files),
       'generator_provenance_count': len(generator_only), 'generator_only': generator_only,
       'unlocated_provenance': unlocated_crop_provenance, 'unique_declared_image_hashes_checked': len(seen_image_hashes),
       'image_hash_issues': image_hash_issues})
if unlocated_crop_provenance or image_hash_issues:
    add('A15', 'action_required', 'Four legacy retained intermediates lack locatable original-coordinate provenance' if len(unlocated_crop_provenance) == 4 and not image_hash_issues else 'Retained crop/helper provenance needs a documented source',
        {'unlocated_provenance': unlocated_crop_provenance, 'image_hash_issues': image_hash_issues},
        'This is a provenance annotation gap for retained intermediates, not a missing mandatory citation or an ink-reading failure. Locate an existing original/parent box or generator if recoverable; otherwise document honestly that the historical coordinates were not retained. Preserve the images and existing view registry. Do not invent coordinates or change frozen readings.',
        sorted({re.search(r'(148|149)_scan\d{3}', r['crop'])[0] for r in unlocated_crop_provenance}))

archive_checks = []
archive_continuity_issues = []
current_archive_names = {str(p.relative_to(OUT)) for p in package_files if p.is_relative_to(OUT)}
current_archive_names |= {'work/proposed/' + p.name for p in package_files if p.parent == ROOT / 'proposed'}
injected_archive_names = {'ARCHIVE_CONTENTS.txt', 'CROP_COMPRESSION_MANIFEST.json', 'CROPS_README.md', 'scripts/restore_crops.py'}
for archive in sorted((ROOT / 'deliverables').rglob('*.zip')):
    try:
        with zipfile.ZipFile(archive) as z:
            names = z.namelist()
            bad = [n for n in names if n.lower().endswith('.zip') or n.startswith(('source/', 'halves/', 'packets/'))
                   or Path(n).name in ('C.tex', 'H.tex', 'MARKS.tsv', 'PREAMBLE.tex', 'images.json')
                   or re.fullmatch(r'(148|149)_scan\d{3}\.jpe?g', Path(n).name, re.I)]
            duplicate_names = [n for n, count in Counter(names).items() if count > 1]
            archive_checks.append({'archive': relative(archive), 'entry_count': len(names), 'prohibited_input_or_nested_zip_names': bad, 'duplicate_member_names': duplicate_names})
            documented_names = set(z.read('ARCHIVE_CONTENTS.txt').decode().splitlines()) if 'ARCHIVE_CONTENTS.txt' in names else set(names)
            if 'CROP_COMPRESSION_MANIFEST.json' in names:
                compression_manifest = json.loads(z.read('CROP_COMPRESSION_MANIFEST.json'))
                documented_names |= {r['original_path'] for r in compression_manifest.get('crops', [])}
                documented_names -= {r['archived_path'] for r in compression_manifest.get('crops', []) if r['archived_path'] != r['original_path']}
            missing = sorted(documented_names - current_archive_names - injected_archive_names)
            if missing:
                archive_continuity_issues.append({'archive': relative(archive), 'earlier_documented_files_absent_from_current_packaging_tree': missing})
    except zipfile.BadZipFile as exc:
        archive_checks.append({'archive': relative(archive), 'error': str(exc)})
check('Existing checkpoint ZIP central directories exclude inputs and nested ZIPs',
      all(not a.get('error') and not a.get('prohibited_input_or_nested_zip_names') and not a.get('duplicate_member_names') for a in archive_checks), archive_checks)
if any(a.get('error') or a.get('prohibited_input_or_nested_zip_names') or a.get('duplicate_member_names') for a in archive_checks):
    add('A13', 'action_required', 'Checkpoint archive member issue', archive_checks,
        'Keep earlier checkpoints immutable; document the issue and ensure the final archive corrects it.')
check('Current package tree retains files documented by earlier checkpoints', not archive_continuity_issues,
      {'archives_checked': len(archive_checks), 'missing_files': archive_continuity_issues,
       'exception': 'Archive-generated contents/compression manifests, crop README and restore script are regenerated for the final transport archive.'})
if archive_continuity_issues:
    add('A16', 'action_required', 'Earlier checkpoint documentation absent from current package tree', archive_continuity_issues,
        'Restore the missing retained work files from the immutable checkpoint before final packaging, or document why an archive-generated transport artifact will be regenerated.')
receipts = doc(OUT / 'checkpoint_receipts.json')
receipt_issues = []
receipt_rows = []
for receipt in receipts:
    location = receipt.get('local_path') or receipt.get('path')
    p = Path(location) if location else ROOT / 'deliverables' / receipt['file_name']
    if not p.is_file():
        p = ROOT / 'deliverables' / receipt['file_name']
    ok = bool(p.is_file() and receipt.get('status') == 'succeeded' and receipt.get('library_file_id') and receipt.get('sha256'))
    receipt_rows.append({'file_name': receipt.get('file_name'), 'local_archive': relative(p), 'durable_receipt_complete': ok,
                         'saved_at': receipt.get('saved_utc', receipt.get('saved_at')), 'note': receipt.get('note', '')})
    if not ok:
        receipt_issues.append(receipt_rows[-1])
check('Checkpoint durable-save receipts retained', not receipt_issues, receipt_rows)
if receipt_issues:
    add('A17', 'action_required', 'Checkpoint receipt incomplete', receipt_issues, 'Retain truthful archive/save receipts; do not rewrite immutable checkpoints.')

# Prove this audit did not alter any frozen TSV, even while root edits other files.
changed_frozen = []
for page in order:
    for kind in ('first', 'second'):
        p = OUT / 'second' / f'{page}_{kind}.tsv'
        before = snapshots[relative(p)]['sha256']
        after = sha(p)
        if before != after:
            changed_frozen.append({'path': relative(p), 'before': before, 'after': after})
check('All 46 frozen TSV files unchanged during this audit', not changed_frozen, changed_frozen)
if changed_frozen:
    add('A14', 'action_required', 'Frozen TSV changed during audit interval', changed_frozen,
        'Investigate concurrent alteration; this audit script never writes these files.')

summary = {
    'pages': len(order), 'independent_boxes': sum(r['box_count'] for r in page_results),
    'first_readers': dict(Counter(r['first_reader'] for r in page_results)),
    'second_readers': dict(Counter(r['second_reader'] for r in page_results)),
    'supplied_C_marks': len(marks), 'exported_decisions': len(decisions),
    'accepted_records': len(records), 'finalized_audits': sum(r['audit_finalized'] for r in page_results),
    'expected_pending_audits': pending_now, 'canonical_independent_crops': len(manifest_crops),
    'record_crop_references': len(all_crop_references),
    'actionable_findings': sum(f['severity'] == 'action_required' and f['status'] == 'open' for f in findings),
    'expected_pending_findings': sum(f['severity'] == 'expected_pending' for f in findings),
}
report = {'audit': 'reader_a read-only method/documentation completeness audit', 'started_utc': START,
          'completed_utc': datetime.now(timezone.utc).isoformat(), 'scope': 'Process structure, metadata, frozen row/hash preservation, crop references/provenance and packaging exclusions; no new ink adjudication.',
          'write_scope': 'Only result/qa/reader_a_method_audit.py and reader_a_method_findings.md/.json.',
          'summary': summary, 'findings': findings, 'checks': checks, 'pages': page_results,
          'boundary_documentation': boundary_notes,
          'limitations': [
              'This is a metadata/process audit, not a fresh visual reading. View claims are checked against retained documentation; they are not re-enacted.',
              'Geometric box coverage alone cannot establish that every ink word or revision lies in an audit box; that semantic coverage belongs to the main reader and accepted inventories.',
              'Read-only checks are a timed snapshot while the root reader continues adjudication. Expected pending pages were supplied explicitly in the assignment.',
              'Filesystem write permission is not used as the definition of a frozen reading; unchanged content hashes and preserved comparison snapshots are the evidence.',
          ], 'snapshots': snapshots}
QA.mkdir(exist_ok=True)
(QA / 'reader_a_method_findings.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
md = ['# Method and documentation audit', '', f"Snapshot: {report['completed_utc']}", '',
      'Read-only audit by reader_a. Accepted pages, records, assignments, first/second TSVs and aggregates were not edited or assembled.', '',
      '## Coverage', '',
      f"- {summary['pages']} page sets; {summary['independent_boxes']} prescribed boxes; all first/second reading rows checked in order.",
      f"- {summary['supplied_C_marks']} supplied C marks and {summary['exported_decisions']} exported decisions checked.",
      f"- {summary['canonical_independent_crops']} canonical independent crop entries; {summary['record_crop_references']} accepted evidence references checked.",
      f"- {summary['finalized_audits']} finalized audits at this snapshot; expected pending: {', '.join(pending_now) or 'none'}.", '',
      '## Actionable findings', '']
actions = [f for f in findings if f['severity'] == 'action_required']
if not actions:
    md += ['No open structural defect found in the checks below.', '']
for f in actions:
    md += [f"### {f['id']}: {f['summary']}", '', f['action'], '', 'Evidence:', '', '```json', json.dumps(f['evidence'], ensure_ascii=False, indent=2), '```', '']
md += ['## Expected pending work', '']
for f in findings:
    if f['severity'] == 'expected_pending':
        md += [f"### {f['id']}: {f['summary']}", '', f['action'], '', '```json', json.dumps(f['evidence'], ensure_ascii=False, indent=2), '```', '']
resolved = [f for f in findings if f['status'] == 'resolved']
if resolved:
    md += ['## Resolved during this audit', '']
    for f in resolved:
        md += [f"- **{f['id']}: {f['summary']}.** {f['action']}"]
    md += ['']
md += ['## Check results', '', '| Check | Result |', '|---|---|']
md += [f"| {c['check']} | {'Pass' if c['passed'] else 'Review finding'} |" for c in checks]
md += ['', '## Page ledger', '', '| Page | First reader | Independent reader | Boxes | Audit state |', '|---|---|---|---:|---|']
md += [f"| {r['page']} | {r['first_reader']} | {r['second_reader']} | {r['box_count']} | {'Finalized' if r['audit_finalized'] else 'Expected pending'} |" for r in page_results]
md += ['', '## Limits', ''] + ['- ' + line for line in report['limitations']]
md += ['', 'The JSON companion retains per-page TSV hashes, all checked hash references, evidence for every check, and the timed input snapshot hashes.', '']
(QA / 'reader_a_method_findings.md').write_text('\n'.join(md))
print(json.dumps({'summary': summary, 'findings': [{k: f[k] for k in ('id', 'severity', 'summary', 'pages')} for f in findings],
                  'report_md': str(QA / 'reader_a_method_findings.md'), 'report_json': str(QA / 'reader_a_method_findings.json')}, ensure_ascii=False, indent=2))
