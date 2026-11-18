#!/usr/bin/env python3
"""Reconcile final authoring records and inventory; never write page transcriptions.

Prepared for the root reader's approved inventory placements. This script reads
the live page .tex files and per-page JSON at invocation time, not preparation
time. It never opens scans, crops, context archives, or research sources.

Default invocation prints a plan and makes no changes. To apply the plan:
    python records/reconcile_metadata.py --apply

The per-page JSON is authoritative for metadata, while pages/*.tex is
authoritative for transcription text. Existing CSV rows provide the old IDs.
The script refuses a second reconciliation against already-renumbered IDs.
"""
from __future__ import annotations

import argparse
import ast
import copy
import csv
import datetime
import hashlib
import io
import json
import os
import pprint
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / 'records'
PREFIX = 'MPL_29_095-140'
EXPECTED = [95, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108,
            109, 110, 111, 112, 117, 118, 124, 126, 129, 130, 131, 132,
            133, 135, 137, 138, 139, 140]
FIELDS = ['cote', 'scan', 'sheet_kind', 'element', 'kind', 'position',
          'first_words_or_objects', 'transcribed']
INVENTORY = ROOT / f'{PREFIX}_inventory.csv'
MAPPING = RECORDS / 'inventory_id_mapping.tsv'
RECEIPT = RECORDS / 'metadata_reconciliation.json'

# These are old IDs, before this reconciliation. Ordering is explicitly approved
# by the root visual reader; no spatial order is inferred from manuscript text.
PLACEMENTS = [
    {'scan': 100, 'where': 'after', 'anchor': '100-07', 'items': ['100-44']},
    {'scan': 100, 'where': 'after', 'anchor': '100-21', 'items': ['100-45']},
    {'scan': 106, 'where': 'after', 'anchor': '106-16', 'items': ['106-28']},
    {'scan': 106, 'where': 'after', 'anchor': '106-19', 'items': ['106-27']},
    {'scan': 137, 'where': 'before', 'anchor': '137-11', 'items': ['137-20']},
    {'scan': 139, 'where': 'after', 'anchor': '139-02', 'items': ['139-19', '139-20']},
    {'scan': 139, 'where': 'after', 'anchor': '139-03', 'items': ['139-21']},
]
EXPECTED_ROLES = {
    '100-44': 'drawing', '100-45': 'drawing',
    '106-28': 'drawing', '106-27': 'drawing',
    '137-20': 'drawing', '137-11': 'text',
    '139-19': 'deletion', '139-20': 'insertion', '139-21': 'deletion',
    '139-02': 'text', '139-03': 'text',
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def canonical(value):
    """Treat Python tuples and the corresponding JSON arrays identically."""
    return json.loads(json.dumps(value, ensure_ascii=False))


def authoring_source(scan: int, tex: str, metadata: dict) -> bytes:
    # save_page() normalizes only outer whitespace. Refuse rather than silently
    # claim exact reproducibility if a page uses a different outer convention.
    if tex != tex.strip() + '\n':
        raise ValueError(f'Scan {scan}: page outer whitespace is not save_page-normalized; no files written.')
    fmt = lambda value: pprint.pformat(value, width=100, sort_dicts=False)
    source = (
        '"""Mechanically regenerated from the saved page and authoritative JSON.\n'
        'No scan reading or mathematical correction is performed by this script.\n'
        '"""\n'
        'from save_page import save_page\n\n'
        f'save_page({scan},\n'
        f'    {tex!r},\n'
        f'    elements={fmt(metadata["elements"])},\n'
        f'    doubts={fmt(metadata.get("doubts", []))},\n'
        f'    leads={fmt(metadata.get("leads", []))},\n'
        f'    sheet_kind={metadata["sheet_kind"]!r},\n'
        ')\n'
    )
    tree = ast.parse(source, filename=f'page{scan:03}.py')
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Name) and node.func.id == 'save_page']
    if len(calls) != 1:
        raise ValueError(f'Scan {scan}: regenerated source lacks a unique save_page call.')
    call = calls[0]
    if ast.literal_eval(call.args[0]) != scan or ast.literal_eval(call.args[1]) != tex:
        raise ValueError(f'Scan {scan}: regenerated source does not preserve the exact page text.')
    values = {item.arg: canonical(ast.literal_eval(item.value)) for item in call.keywords}
    for field, default in [('elements', []), ('doubts', []), ('leads', []), ('sheet_kind', 'text')]:
        if values[field] != canonical(metadata.get(field, default)):
            raise ValueError(f'Scan {scan}: regenerated {field} does not match JSON.')
    return source.encode('utf-8')


def build_plan():
    if MAPPING.exists() or RECEIPT.exists():
        raise ValueError('A reconciliation mapping/receipt already exists. Do not reapply old-ID placements to renumbered rows.')
    originals = {}

    def remember(path: Path, required=True):
        if path not in originals:
            if path.exists():
                originals[path] = path.read_bytes()
            elif required:
                raise FileNotFoundError(path)
            else:
                originals[path] = None
        return originals[path]

    reader = csv.DictReader(io.StringIO(remember(INVENTORY).decode('utf-8')))
    if reader.fieldnames != FIELDS:
        raise ValueError('Inventory columns do not match the required schema.')
    rows = list(reader)
    ids = [row['element'] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError('Inventory contains duplicate element IDs.')
    groups = {scan: [] for scan in EXPECTED}
    for row in rows:
        scan = int(row['scan'])
        if scan not in groups or row['cote'] != '29' or row['transcribed'] != 'yes':
            raise ValueError(f'Unexpected or incomplete inventory row: {row["element"]}')
        groups[scan].append(row)
    by_id = {row['element']: row for row in rows}
    for element, kind in EXPECTED_ROLES.items():
        if element not in by_id or by_id[element]['kind'] != kind:
            raise ValueError(f'Old-ID role guard failed for {element}; no automatic reassignment is safe.')

    metadata, texts, page_hashes = {}, {}, {}
    for scan in EXPECTED:
        record_path = RECORDS / f'{scan:03}.json'
        data = json.loads(remember(record_path))
        if data.get('scan') != scan:
            raise ValueError(f'{record_path.name}: scan identity mismatch.')
        actual = [[row['kind'], row['position'], row['first_words_or_objects']] for row in groups[scan]]
        if actual != data.get('elements'):
            raise ValueError(f'Scan {scan}: CSV elements/order differ from authoritative JSON; resolve before applying.')
        if any(row['sheet_kind'] != data['sheet_kind'] for row in groups[scan]):
            raise ValueError(f'Scan {scan}: CSV sheet_kind differs from authoritative JSON.')
        expected_ids = [f'{scan:03}-{n:02}' for n in range(1, len(actual) + 1)]
        if [row['element'] for row in groups[scan]] != expected_ids:
            raise ValueError(f'Scan {scan}: old ID sequence already changed or is incomplete.')
        metadata[scan] = data
        page_path = ROOT / 'pages' / f'{PREFIX}_29_scan{scan:03}.tex'
        page_bytes = remember(page_path)
        texts[scan] = page_bytes.decode('utf-8')
        page_hashes[str(page_path.relative_to(ROOT))] = sha(page_bytes)
        remember(RECORDS / f'page{scan:03}.py', required=False)

    reasons = {}
    for move in PLACEMENTS:
        scan = move['scan']
        current = groups[scan]
        current_ids = {row['element'] for row in current}
        if move['anchor'] not in current_ids or not set(move['items']).issubset(current_ids):
            raise ValueError(f'Missing old-ID anchor or moved element: {move}')
        moved = [by_id[element] for element in move['items']]
        current = [row for row in current if row['element'] not in move['items']]
        index = next(i for i, row in enumerate(current) if row['element'] == move['anchor'])
        if move['where'] == 'after':
            index += 1
        current[index:index] = moved
        groups[scan] = current
        for element in move['items']:
            reasons[element] = f'root-approved placement {move["where"]} old {move["anchor"]}'

    plan, final_rows, map_rows = {}, [], []
    for scan in EXPECTED:
        data = copy.deepcopy(metadata[scan])
        data['elements'] = []
        for n, old in enumerate(groups[scan], 1):
            row = dict(old)
            new_id = f'{scan:03}-{n:02}'
            row['element'] = new_id
            row['scan'] = str(scan)
            final_rows.append(row)
            data['elements'].append([row['kind'], row['position'], row['first_words_or_objects']])
            reason = reasons.get(old['element'], 'unchanged' if old['element'] == new_id else 'renumbered after approved placement')
            map_rows.append([29, scan, old['element'], new_id, row['kind'], row['position'], reason])
        if len(data['elements']) != len(metadata[scan]['elements']):
            raise ValueError(f'Scan {scan}: reconciliation would change element count.')
        plan[RECORDS / f'{scan:03}.json'] = json_bytes(data)
        plan[RECORDS / f'page{scan:03}.py'] = authoring_source(scan, texts[scan], data)

    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(final_rows)
    plan[INVENTORY] = output.getvalue().encode('utf-8')
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter='\t', lineterminator='\n')
    writer.writerow(['cote', 'scan', 'old_element', 'new_element', 'kind', 'position', 'reason'])
    writer.writerows(map_rows)
    plan[MAPPING] = output.getvalue().encode('utf-8')
    originals[MAPPING] = originals[RECEIPT] = None

    # Receipt has no self-hash. It records every other emitted metadata file and
    # the untouched page bytes used to generate the authoring sources.
    receipt = {
        'created_at_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scope': 'Metadata reconciliation only; no page .tex files written; no source images/context opened.',
        'page_count': len(EXPECTED), 'inventory_count': len(final_rows),
        'approved_placements': PLACEMENTS,
        'page_sha256': page_hashes,
        'output_sha256': {str(path.relative_to(ROOT)): sha(content) for path, content in plan.items()},
    }
    plan[RECEIPT] = json_bytes(receipt)
    for path in plan:
        if path != INVENTORY and path.parent != RECORDS:
            raise ValueError(f'Forbidden reconciliation destination: {path}')
        if path.parent == ROOT / 'pages' or path.suffix == '.tex':
            raise ValueError('Transcription mutation is forbidden.')
    return plan, originals, page_hashes, map_rows


def apply_plan(plan, originals, page_hashes):
    # Stage every output before replacing anything, and reject a stale snapshot.
    with tempfile.TemporaryDirectory(prefix='.metadata-stage-', dir=ROOT) as directory:
        staged = {}
        for n, (path, content) in enumerate(plan.items()):
            stage = Path(directory) / f'{n:03}.stage'
            stage.write_bytes(content)
            staged[path] = stage
        for path, before in originals.items():
            current = path.read_bytes() if path.exists() else None
            if current != before:
                raise RuntimeError(f'Input changed during staging: {path.relative_to(ROOT)}. Nothing was committed.')
        changed = []
        try:
            for path in plan:
                os.replace(staged[path], path)
                changed.append(path)
            for relative, expected in page_hashes.items():
                if sha((ROOT / relative).read_bytes()) != expected:
                    raise RuntimeError(f'Page changed concurrently: {relative}. Reconciliation will be rolled back.')
        except BaseException:
            for n, path in enumerate(reversed(changed)):
                previous = originals.get(path)
                if previous is None:
                    path.unlink(missing_ok=True)
                else:
                    rollback = Path(directory) / f'rollback-{n:03}'
                    rollback.write_bytes(previous)
                    os.replace(rollback, path)
            raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Commit validated metadata and regenerated authoring scripts.')
    args = parser.parse_args()
    plan, originals, page_hashes, mapping = build_plan()
    print(f'Validated live inputs: {len(EXPECTED)} pages, {len(mapping)} inventory rows.')
    print(f'AST-validated {len(EXPECTED)} regenerated authoring scripts against exact current page text and JSON.')
    for move in PLACEMENTS:
        print(f'Placement: {", ".join(move["items"])} {move["where"]} old {move["anchor"]}')
    print(f'Complete ID map: {MAPPING}')
    if not args.apply:
        print('Plan only: no files written. Invoke --apply when the final live inputs are ready.')
        return 0
    apply_plan(plan, originals, page_hashes)
    print(f'Applied {len(plan)} metadata/script outputs; all {len(page_hashes)} page SHA-256 values are unchanged.')
    print('The reconciliation receipt prevents accidental reapplication of the old-ID placements.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
