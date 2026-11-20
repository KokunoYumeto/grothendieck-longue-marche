"""Explicit, versioned amendments to already committed visual decisions.

No image inspection or reading inference occurs here. The supplied independent
report and a full expected-before row for every target are required authorities.
"""
from __future__ import annotations
import copy
from collections import Counter
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

from reconcile import FIELDS, EVENT_FIELDS, atomic, fail, tsv_bytes, tsv_read, utcnow


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def digest(content):
    return hashlib.sha256(content).hexdigest()


def file_digest(path):
    return digest(path.read_bytes()) if path.exists() else None


def immutable(path, content):
    if path.exists():
        if path.read_bytes() != content:
            fail(f'Immutable amendment archive conflicts: {path}')
    else:
        atomic(path, content)


def instant(value):
    value = str(value)
    if value.endswith(' UTC'):
        return dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=dt.timezone.utc)
    parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        fail('Amendment report timestamps must include a timezone')
    return parsed


def verify_amendments(project, receipts, events):
    """Check immutable archives, version links, and effective evidence rows."""
    current = {row['id']: row for receipt in receipts for row in receipt['rows']}
    versions_path = project.out / 'audit/STATEMENT_VERSIONS.json'
    versions = json.loads(versions_path.read_text()) if versions_path.exists() else {}
    manifests = {}
    for path in sorted((project.out / 'audit/amendments').glob('*/manifest.json')):
        manifest = json.loads(path.read_text())
        manifests[manifest['amendment_id']] = manifest
        base = path.parent
        for relative, expected_hash in manifest['archive_sha256'].items():
            if file_digest(base / relative) != expected_hash:
                fail(f'Amendment archive altered or missing: {base / relative}')
        for event in manifest['events']:
            if event not in events:
                fail(f'Amendment {manifest["amendment_id"]}: missing version-linked event')
        for relative, expected_hash in manifest['source_sha256'].items():
            if file_digest(project.workspace / relative) != expected_hash:
                fail(f'Amendment source changed: {relative}')
        for link in manifest['version_links']:
            latest = versions.get(link['id'])
            if not latest or latest['version'] < link['version']:
                fail(f'Missing current version for {link["id"]}')
    for mark_id, version in versions.items():
        manifest = manifests.get(version['amendment_id'])
        if not manifest:
            fail(f'{mark_id}: version has no amendment manifest')
        if current.get(mark_id) != version['row']:
            fail(f'{mark_id}: current decision differs from its current version')
        link = next((v for v in manifest['version_links'] if v['id'] == mark_id), None)
        if not link or link['statement_id'] != version['statement_id']:
            fail(f'{mark_id}: invalid current version linkage')
        event = next((e for e in manifest['events'] if e['statement id'] == version['statement_id']), None)
        if not event or event not in events:
            fail(f'{mark_id}: current refined statement lacks its actual ink-check event')
    for receipt in receipts:
        if receipt.get('amendment_history'):
            if 'initial_rows' not in receipt or 'initial_submission_rows' not in receipt:
                fail(f'scan {receipt["scan"]}: amendment lost initial primary statements')
            initial, _ = project.validate_rows(int(receipt['scan']), receipt['initial_submission_rows'])
            if initial != receipt['initial_rows']:
                fail(f'scan {receipt["scan"]}: initial rows do not match preserved submission')
            for history in receipt['amendment_history']:
                if history['amendment_id'] not in manifests:
                    fail('Receipt names an absent amendment')


def finish_transaction(project, base, manifest):
    # Check every destination before writing anything. An interrupted transaction
    # may have any mixture of the exact saved before/after bytes, but no third state.
    for relative, state in manifest['writes'].items():
        actual = file_digest(project.workspace / relative)
        if actual not in {state['before_sha256'], state['after_sha256']}:
            fail(f'Amendment destination has unrelated edits: {relative}')
    for relative, expected_hash in manifest['unchanged_sha256'].items():
        if file_digest(project.workspace / relative) != expected_hash:
            fail(f'Untouched amendment invariant changed: {relative}')
    for relative, state in manifest['writes'].items():
        content = (base / state['staged_path']).read_bytes()
        if digest(content) != state['after_sha256']:
            fail(f'Corrupt staged amendment file: {relative}')
        if file_digest(project.workspace / relative) != state['after_sha256']:
            atomic(project.workspace / relative, content)
    project.verify(False)
    for relative, expected_hash in manifest['unchanged_sha256'].items():
        if file_digest(project.workspace / relative) != expected_hash:
            fail(f'Amendment changed protected file: {relative}')
    manifest['status'] = 'applied'
    manifest['applied_utc'] = utcnow()
    atomic(base / 'manifest.json', encoded(manifest))
    print(json.dumps({'amendment': manifest['amendment_id'], 'status': 'applied',
                      'ids': manifest['ids'], 'before_counts': manifest['before_counts'],
                      'after_counts': manifest['after_counts'],
                      'applied_utc': manifest['applied_utc'],
                      'archive': str(base.relative_to(project.workspace))}, ensure_ascii=False))


def amend(project, plan_path: Path, apply: bool):
    if not plan_path.is_absolute():
        plan_path = project.workspace / plan_path
    plan_bytes = plan_path.read_bytes()
    plan = json.loads(plan_bytes)
    amendment_id = plan['amendment_id']
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{2,79}', amendment_id):
        fail('Use a unique, safe amendment_id (letters, digits, underscore, hyphen)')
    if not str(plan.get('reason', '')).strip() or not str(plan.get('accepted_by', '')).strip():
        fail('Amendment plan needs its concrete reason and accepting coordinator')
    report_path = Path(plan['report'])
    if not report_path.is_absolute():
        report_path = project.workspace / report_path
    report_bytes = report_path.read_bytes()
    report = json.loads(report_bytes)
    base = project.out / 'audit/amendments' / amendment_id
    manifest_path = base / 'manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        if manifest['plan_sha256'] != digest(plan_bytes) or manifest['report_sha256'] != digest(report_bytes):
            fail('Amendment ID already refers to a different plan or independent report')
        if manifest['status'] == 'applied':
            project.verify(False)
            print(json.dumps({'amendment': amendment_id, 'status': 'already applied', 'ids': manifest['ids']}))
        elif apply:
            finish_transaction(project, base, manifest)
        else:
            print(json.dumps({'amendment': amendment_id, 'status': 'prepared; --apply resumes saved transaction'}))
        return

    project.verify(False)
    receipts = project.receipts()
    all_before = [row for receipt in receipts for row in receipt['rows']]
    current = {row['id']: row for row in all_before}
    expected = plan.get('expected', [])
    ids = [row['id'] for row in expected]
    if not ids or len(ids) != len(set(ids)):
        fail('Amendment expected rows must identify each target exactly once')
    if ids != [row['id'] for row in all_before if row['id'] in ids]:
        fail('Amendment targets must be committed IDs in original source order')
    if any(current.get(row['id']) != row for row in expected):
        fail('Amendment expected-before rows do not match current complete decisions')
    if [row.get('id') for row in report.get('rows', [])] != ids:
        fail('Independent report rows must exactly match the explicit amendment targets')
    who = report.get('reader') or report.get('who')
    checked_at = report.get('checked_at') or report.get('finished_utc') or report.get('date')
    if not who or not checked_at:
        fail('Independent report requires its actual reader and checking timestamp')
    instant(checked_at)
    replacements = {}
    for raw in report['rows']:
        observed = raw.get('observed strokes') or raw.get('what the ink shows')
        if not observed:
            fail(f'{raw["id"]}: missing independent ink evidence')
        row = {key: raw[key] for key in FIELDS if key != 'what the ink shows'}
        row['what the ink shows'] = observed
        if int(row['scan']) != int(current[row['id']]['scan']):
            fail(f'{row["id"]}: amendment report changes the source scan')
        replacements[row['id']] = row
    affected = sorted({int(current[mark_id]['scan']) for mark_id in ids})
    after_receipts = copy.deepcopy(receipts)
    normalized_new = {}
    for receipt in after_receipts:
        scan = int(receipt['scan'])
        if scan not in affected:
            continue
        old_raw = receipt.get('submission_rows', receipt['rows'])
        raw_rows = copy.deepcopy(old_raw)
        for raw in raw_rows:
            if raw['id'] in replacements:
                raw.update(replacements[raw['id']])
        normalized_rows, _ = project.validate_rows(scan, raw_rows)
        for old, new in zip(receipt['rows'], normalized_rows):
            if old['id'] not in ids and old != new:
                fail(f'Amendment would also change {old["id"]}; include its own accepted report explicitly')
            if old['id'] in ids:
                if old == new:
                    fail(f'{old["id"]}: amendment makes no change')
                normalized_new[old['id']] = new
        receipt.setdefault('initial_rows', copy.deepcopy(receipt['rows']))
        receipt.setdefault('initial_submission_rows', copy.deepcopy(old_raw))
        receipt['rows'] = normalized_rows
        receipt['submission_rows'] = raw_rows
    all_after = [row for receipt in after_receipts for row in receipt['rows']]
    if len(all_after) != len(all_before) or [r['id'] for r in all_after] != [r['id'] for r in all_before]:
        fail('Amendment changed global decision order or count')
    before_counts, after_counts = dict(Counter(r['decision'] for r in all_before)), dict(Counter(r['decision'] for r in all_after))
    if not apply:
        print(json.dumps({'valid_amendment': amendment_id, 'ids': ids, 'scans': affected,
                          'before_counts': before_counts, 'after_counts': after_counts,
                          'total_marks': len(all_after), 'changes': [{'before': current[i], 'after': normalized_new[i]} for i in ids]}, ensure_ascii=False, indent=2))
        return

    # An intent fixes preparation time before any archive writes. Retrying an
    # interrupted preparation uses exactly that timestamp and immutable inputs.
    intent_path = base / 'intent.json'
    if intent_path.exists():
        intent = json.loads(intent_path.read_text())
        if intent['plan_sha256'] != digest(plan_bytes) or intent['report_sha256'] != digest(report_bytes):
            fail('Incomplete amendment preparation has conflicting inputs')
    else:
        intent = {'prepared_utc': utcnow(), 'plan_sha256': digest(plan_bytes), 'report_sha256': digest(report_bytes)}
        immutable(intent_path, encoded(intent))
    prepared = intent['prepared_utc']
    versions_path = project.out / 'audit/STATEMENT_VERSIONS.json'
    versions = json.loads(versions_path.read_text()) if versions_path.exists() else {}
    events = []
    links = []
    for mark_id in ids:
        prior = versions.get(mark_id, {'version': 1, 'statement_id': mark_id})
        number = int(prior['version']) + 1
        statement_id = f'{mark_id}@v{number}'
        row = normalized_new[mark_id]
        link = {'id': mark_id, 'version': number, 'statement_id': statement_id, 'refutes': prior['statement_id'],
                'amendment_id': amendment_id, 'checked_at': checked_at, 'reader': who, 'row': row}
        links.append(link)
        versions[mark_id] = link
        events.extend([
            {'statement id': prior['statement_id'], 'date': checked_at, 'who (model, effort, run)': who,
             'type': 'refuted', 'outcome': f'Refined statement {statement_id}; amendment={amendment_id}; old reading={current[mark_id]["reading"]}; refined reading={row["reading"]}; {row["what the ink shows"]}'},
            {'statement id': statement_id, 'date': checked_at, 'who (model, effort, run)': who,
             'type': 'independent re-proof', 'outcome': f'Refines and replaces {prior["statement_id"]}; stable mark={mark_id}; amendment={amendment_id}; {row["decision"]}; reading={row["reading"]}; confidence={row["confidence"]}; crop={row["crop"]}; {row["what the ink shows"]}'}
        ])
    archive_relative = str(base.relative_to(project.workspace))
    writes = {}
    def put(path, content):
        writes[str(path.relative_to(project.workspace))] = content
    history = {'amendment_id': amendment_id, 'prepared_utc': prepared, 'checked_at': checked_at,
               'reader': who, 'archive': archive_relative, 'report': f'{archive_relative}/independent_report.json',
               'timing_scope': 'Original primary timestamps and views remain unchanged; this re-proof is separate.'}
    for receipt in after_receipts:
        scan = int(receipt['scan'])
        if scan not in affected:
            continue
        page_ids = [i for i in ids if int(current[i]['scan']) == scan]
        page_history = {**history, 'ids': page_ids,
                        'versions': {i: versions[i]['statement_id'] for i in page_ids}}
        receipt.setdefault('amendment_history', []).append(page_history)
        receipt.setdefault('current_row_readers', {}).update({i: who for i in page_ids})
        put(project.out / f'audit/receipts/scan{scan:03}.json', encoded(receipt))
        put(project.out / f'pages/1_scan{scan:03}.tex', project.apply(scan, receipt['rows']))
        submission_path = project.out / f'audit/scan{scan:03}.json'
        submission = json.loads(submission_path.read_text())
        if isinstance(submission, list):
            submission = {'rows': submission}
        submission['rows'] = receipt['submission_rows']
        submission.setdefault('amendment_history', []).append(page_history)
        submission.setdefault('row_readers', {}).update({i: who for i in page_ids})
        put(submission_path, encoded(submission))
    put(project.out / 'decisions.tsv', tsv_bytes(FIELDS, all_after))
    old_events = (project.out / 'CHECK_EVENTS.tsv').read_bytes()
    if not old_events.endswith(b'\n'):
        fail('CHECK_EVENTS.tsv must end with a newline before exact-prefix append')
    addition = tsv_bytes(EVENT_FIELDS, events)
    put(project.out / 'CHECK_EVENTS.tsv', old_events + addition[addition.index(b'\n')+1:])
    put(versions_path, encoded(versions))

    views = report.get('views', [])
    page_views = crop_views = 0
    for scan in affected:
        grouped = [view for view in views if int(view.get('scan', scan if len(affected) == 1 else -1)) == scan]
        pages, crops = project.view_counts(scan, {'views': grouped})
        page_views += pages
        crop_views += crops
    if page_views + crop_views != len(views):
        fail('Every multi-page report view must declare its actual scan')
    duration = None
    if report.get('started_utc') and report.get('finished_utc'):
        duration = (instant(report['finished_utc']) - instant(report['started_utc'])).total_seconds()
        if duration < 0:
            fail('Independent review finish precedes start')
    time_note = (f"The separate re-proof interval was {report['started_utc']} to {report['finished_utc']} "
                 f"({duration:g} seconds). " if duration is not None else '')
    workflow = (f'\n### {prepared} — audited amendment {amendment_id}\n\n'
                f"{plan['reason']} Accepted by {plan['accepted_by']}. The authoritative independent report is preserved unchanged at "
                f"audit/amendments/{amendment_id}/independent_report.json.\n\n"
                f'{time_note}It covered {len(ids)} marks in {len(views)} actual views: {page_views} whole-page view(s) and {crop_views} crops. '
                f"These are recorded review intervals, not a claim of uninterrupted viewing. The original primary timing and view metrics remain intact.\n\n"
                f"Only {', '.join(ids)} were amended. Original statements and all prior check events remain in the before archive; "
                f"the refined statements are {', '.join(link['statement_id'] for link in links)}. Separate refutation and independent re-proof events use the actual reader and check time. "
                f"The amendment regenerates affected pages from original source, preserves every unmarked byte, and leaves page completion order unchanged.\n")
    put(project.out / 'WORKFLOW.md', (project.out / 'WORKFLOW.md').read_bytes() + workflow.encode('utf-8'))
    patterns = f'\n<!-- amendment-{amendment_id} -->\n## Accepted re-proof: {amendment_id}\n\n'
    for pattern in report.get('patterns', []):
        pattern_ids = pattern.get('marks', ids)
        if not set(pattern_ids) <= set(ids):
            fail('Amendment pattern refers to an unamended mark')
        patterns += f"### {pattern.get('name', 'Independent comparison')}\n\nMarks: {', '.join(pattern_ids)}.\n\n{pattern.get('description', '')}\n\n"
    patterns += (f"This accepted comparison refines the previous readings of {', '.join(ids)} only. "
                 'Each later occurrence still requires inspection of its own surviving ink; similarity alone does not settle it. '
                 f'Actual check: {checked_at}; {who}. Full original and refined records are linked in audit/amendments/{amendment_id}/manifest.json.\n')
    put(project.out / 'PATTERNS.md', (project.out / 'PATTERNS.md').read_bytes() + patterns.encode('utf-8'))
    if plan.get('reading_guide_addition'):
        guide = project.out / 'audit/READING_GUIDE.md'
        put(guide, guide.read_bytes() + ('\n' + plan['reading_guide_addition'].strip() + '\n').encode('utf-8'))

    # Preserve complete original target receipts/pages, consolidated and raw
    # submissions, original review revisions, and the full global event/decision logs.
    snapshot = {project.workspace / relative for relative in writes if (project.workspace / relative).exists()}
    snapshot.update([project.out / 'progress.log', project.out / 'audit/METRICS.tsv'])
    for receipt in receipts:
        scan = int(receipt['scan'])
        if scan not in affected:
            continue
        for relative in [receipt.get('submission_path', '')] + receipt['metadata'].get('source_submission_paths', []):
            if relative:
                path = Path(relative)
                path = path if path.is_absolute() else project.workspace / path
                if not path.is_relative_to(project.workspace):
                    fail('Amendment source submissions must be within the workspace for archival')
                snapshot.add(path)
        snapshot.update((project.workspace / 'work').glob(f'scan{scan:03}*.json'))
        snapshot.update((project.out / 'audit').glob(f'scan{scan:03}*.json'))
        snapshot.update((project.out / 'audit/parts').glob(f'scan{scan:03}*.json'))
        snapshot.update((project.out / 'audit/revisions').glob(f'scan{scan:03}*.json'))
    archive_hashes = {}
    def archive(relative, content):
        immutable(base / relative, content)
        archive_hashes[relative] = digest(content)
    archive('plan.json', plan_bytes)
    archive('independent_report.json', report_bytes)
    for path in sorted(snapshot):
        archive('before/' + str(path.relative_to(project.workspace)), path.read_bytes())
    write_manifest = {}
    for relative, content in writes.items():
        staged = 'after/' + relative
        archive(staged, content)
        write_manifest[relative] = {'before_sha256': file_digest(project.workspace / relative),
                                    'after_sha256': digest(content), 'staged_path': staged}
    unchanged = {str(path.relative_to(project.workspace)): file_digest(path) for path in
                 [project.out / 'progress.log', project.out / 'audit/METRICS.tsv']}
    manifest = {'amendment_id': amendment_id, 'status': 'prepared', **intent,
                'ids': ids, 'scans': affected, 'reason': plan['reason'], 'accepted_by': plan['accepted_by'],
                'old_rows': expected, 'new_rows': [normalized_new[i] for i in ids],
                'before_counts': before_counts, 'after_counts': after_counts,
                'version_links': links, 'events': events, 'writes': write_manifest,
                'archive_sha256': archive_hashes, 'unchanged_sha256': unchanged,
                'source_sha256': {str((project.source / f'pages/1_scan{scan:03}.tex').relative_to(project.workspace)):
                                  file_digest(project.source / f'pages/1_scan{scan:03}.tex') for scan in affected},
                'independent_metrics': {'started_utc': report.get('started_utc'), 'finished_utc': report.get('finished_utc'),
                                        'seconds': duration, 'marks': len(ids), 'views': len(views),
                                        'page_views': page_views, 'crop_views': crop_views}}
    atomic(manifest_path, encoded(manifest))
    finish_transaction(project, base, manifest)
