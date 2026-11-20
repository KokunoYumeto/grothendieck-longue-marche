#!/usr/bin/env python3
"""Record ONLY readings and inventory confirmations explicitly supplied by root.

No OCR, semantic alignment, interpretation, or image verification occurs here.
The caller is responsible for every assertion in its page record.  --finalize
is an explicit declaration by the caller that the page has been read and its
inventory checked.  Without it this tool validates and previews, without writes.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import shutil
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from crop_metadata import validate_crop_metadata

BASE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = Path(__file__).resolve().parents[1]
DEFAULT_WITNESSES = BASE / 'source' / 'SP02_CW_10+12_witnesses'
PREFIX = 'SP02_CW_10+12'
KINDS = {'misread word', 'misread symbol or index', 'omission', 'text not on the page',
         'deletion state', 'deletion state (struck given live or live given struck)', 'insertion or placement',
         'abbreviation expanded or spelling modernised', 'readable ink left as \\ill{}',
         'drawing or diagram', 'other'}
INVENTORY_KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
SHEET_KINDS = {'text', 'reused_typed', 'typescript', 'letter', 'list', 'cancelled_draft', 'cover'}
INV_FIELDS = ['scan', 'sheet_kind', 'hand', 'element', 'kind', 'position', 'first_words_or_objects', 'transcribed']
COLL_FIELDS = ['folder', 'their_page', 'our_scan', 'line', 'their_reading', 'codex_reading',
               'final_reading', 'scan_shows', 'kind', 'marked_in_H', 'confidence']
CROP_REFERENCE_ALIASES = frozenset({'whole', 'both halves'})


def utc() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def md(value) -> str:
    if isinstance(value, (list, tuple)):
        value = '; '.join(map(str, value))
    if isinstance(value, dict):
        value = json.dumps(value, ensure_ascii=False)
    return str(value if value is not None else '').replace('|', '\\|').replace('\n', '<br>')


def table(headers, rows) -> str:
    return '| ' + ' | '.join(headers) + ' |\n|' + '|'.join('---' for _ in headers) + '|\n' + ''.join(
        '| ' + ' | '.join(md(x) for x in row) + ' |\n' for row in rows)


def write_csv(path: Path, fields: list[str], rows: list[dict], delimiter=',') -> None:
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=delimiter, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def read_map(witness_root: Path) -> list[dict]:
    with (witness_root / 'page_map.tsv').open(encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def page_key(record: dict) -> str:
    return f"{record['folder']}_{record['cote']}_scan{int(record['scan']):03d}"


def require_string(value, label: str, nonempty=False) -> None:
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ValueError(f'{label} must be ' + ('a nonempty string.' if nonempty else 'a string.'))


def require_attestations(value, label: str) -> None:
    if isinstance(value, str):
        return
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
        raise ValueError(f'{label} must be a string or a list of strings.')


def inventory_scan_label(record: dict) -> str:
    """Return the immutable inventory identity for this page record."""
    return str(record.get('scan_label', f"{record['cote']}:{int(record['scan']):03d}"))


def resolve_crop_references(reference: str, crop_ids: set[str]) -> list[str]:
    """Resolve explicit recipe IDs or established whole-image aliases, without IO.

    An exact complete ID wins before separator parsing, because '+' and even
    separator words may occur in recorded IDs. Commas, semicolons and 'and'
    separate groups before '+' is considered within each group. Thus an ID
    containing '+' can also be combined unambiguously with another ID using a
    comma. The aliases identify existing whole-image evidence conventions; this
    function does not open or verify any image.
    """
    require_string(reference, 'Crop reference', True)
    allowed = set(crop_ids) | CROP_REFERENCE_ALIASES

    def resolve(value: str) -> list[str]:
        if value in allowed:
            return [value]
        value = value.strip()
        if value in allowed:
            return [value]
        parts = re.split(r'\s*(?:[,;]|\band\b)\s*', value)
        if len(parts) == 1:
            parts = re.split(r'\s*\+\s*', value)
        if len(parts) == 1:
            raise ValueError(f'Unknown crop reference: {value!r}.')
        return [item for part in parts for item in resolve(part)]

    return resolve(reference)


def validate_record_metadata(record: dict) -> None:
    """Validate render-consumed metadata only; never read files or decide readings."""
    if not isinstance(record, dict):
        raise ValueError('A page record must be an object.')
    for field in ['edits', 'changes', 'remaining_doubts', 'notation_updates', 'abbreviations', 'crops']:
        values = record.get(field, [])
        if not isinstance(values, list) or not all(isinstance(v, dict) for v in values):
            raise ValueError(f'{field} must be a list of objects.')
    for n, edit in enumerate(record.get('edits', []), 1):
        require_string(edit.get('old'), f'Edit {n} old', True)
        require_string(edit.get('new'), f'Edit {n} new')
        count = edit.get('count', 1)
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            raise ValueError(f'Edit {n} count must be a positive integer.')
    for n, change in enumerate(record.get('changes', []), 1):
        for field in ['place', 'C', 'H', 'final', 'shows', 'crop']:
            require_string(change.get(field), f'Change {n} {field}', field in {'place', 'shows', 'crop'})
        if change.get('confidence') not in {'high', 'medium', 'low'}:
            raise ValueError(f'Change {n} requires a valid confidence.')
        for field in ['against_C', 'against_H']:
            if not isinstance(change.get(field), bool):
                raise ValueError(f'Change {n} {field} must be Boolean.')
        if change['against_H']:
            if change.get('kind') not in KINDS:
                raise ValueError(f'Change {n} requires an allowed H kind.')
            marked = change.get('marked_in_H')
            if not isinstance(marked, (bool, str)) or (isinstance(marked, str) and not marked.strip()):
                raise ValueError(f'Change {n} marked_in_H must be Boolean or a nonempty explicit answer.')
            if record.get('map', {}).get('hua_has') != 'text':
                raise ValueError('An H difference requires mapped H text.')
        if 'consequential' in change and not isinstance(change['consequential'], (bool, str)):
            raise ValueError(f'Change {n} consequential must be Boolean or an explanation string.')
    for n, doubt in enumerate(record.get('remaining_doubts', []), 1):
        require_string(doubt.get('line', doubt.get('place')), f'Doubt {n} place', True)
        require_string(doubt.get('reading'), f'Doubt {n} reading', True)
        if doubt.get('confidence') not in {'high', 'medium', 'low'}:
            raise ValueError(f'Doubt {n} requires a valid confidence.')
        alternatives = doubt.get('alternatives', '')
        if not isinstance(alternatives, str) and not (isinstance(alternatives, list) and all(isinstance(v, str) for v in alternatives)):
            raise ValueError(f'Doubt {n} alternatives must be a string or list of strings.')
        require_string(doubt.get('comment', doubt.get('reason', '')), f'Doubt {n} comment')
    for n, notation in enumerate(record.get('notation_updates', []), 1):
        require_string(notation.get('sign', notation.get('notation', notation.get('key'))), f'Notation {n} sign', True)
        require_string(notation.get('form', notation.get('reading', notation.get('description'))), f'Notation {n} form', True)
        require_string(notation.get('status', ''), f'Notation {n} status')
        require_attestations(notation.get('attestations', notation.get('attestation', '')), f'Notation {n} attestations')
    for n, abbreviation in enumerate(record.get('abbreviations', []), 1):
        require_string(abbreviation.get('abbreviation', abbreviation.get('abbr')), f'Abbreviation {n} form', True)
        require_string(abbreviation.get('expansion', abbreviation.get('meaning')), f'Abbreviation {n} expansion', True)
        require_attestations(abbreviation.get('attestations', ''), f'Abbreviation {n} attestations')
    crop_ids, crop_names = set(), set()
    for crop in record.get('crops', []):
        validate_crop_metadata(crop)
        require_string(crop['source'], 'Recorded crop source', True)
        normalized_name = re.sub(r'[^A-Za-z0-9_.+-]+', '_', crop['id'])
        if crop['id'] in crop_ids or normalized_name in crop_names:
            raise ValueError('Crop ids must be unique and must not collide after filename normalization.')
        crop_ids.add(crop['id']); crop_names.add(normalized_name)
    for n, change in enumerate(record.get('changes', []), 1):
        try:
            resolve_crop_references(change['crop'], crop_ids)
        except ValueError as exc:
            raise ValueError(f'Change {n}: {exc}') from exc
    if 'inventory_resolved' in record:
        inventory = record['inventory_resolved']
        if not isinstance(inventory, list) or not inventory or not all(isinstance(r, dict) for r in inventory):
            raise ValueError('Resolved inventory must be a nonempty list of objects.')
        element_ids = set()
        for row in inventory:
            if set(row) - set(INV_FIELDS):
                raise ValueError('Resolved inventory has unsupported row fields.')
            for field in INV_FIELDS:
                if field not in row:
                    raise ValueError(f'Resolved inventory lacks {field}.')
            if str(row['scan']) != inventory_scan_label(record):
                raise ValueError('Resolved inventory scan identity differs from its page record.')
            element_id = str(row['element'])
            if row['element'] is None or not element_id.strip() or element_id in element_ids:
                raise ValueError('Resolved inventory element IDs must be nonempty and unique.')
            element_ids.add(element_id)
            if row['transcribed'] != 'yes' or row['kind'] not in INVENTORY_KINDS or row['sheet_kind'] not in SHEET_KINDS:
                raise ValueError('Resolved inventory has an invalid kind, sheet kind, or incomplete state.')


def editorial_table_rows(records: list[dict]) -> tuple[list[list], list[list]]:
    """Preserve each exact supplied form/meaning with its own attestations."""
    notation = {}; abbreviations = {}
    for record in records:
        scan = f"{record['cote']}:{int(record['scan']):03d}"
        for item in record.get('notation_updates', []):
            sign = item.get('sign', item.get('notation', item.get('key')))
            form = item.get('form', item.get('reading', item.get('description')))
            status = item.get('status', '')
            key = (sign, form, status)
            att = item.get('attestations', item.get('attestation', scan))
            notation.setdefault(key, []).extend(att if isinstance(att, list) else [att])
        for item in record.get('abbreviations', []):
            form = item.get('abbreviation', item.get('abbr'))
            expansion = item.get('expansion', item.get('meaning'))
            att = item.get('attestations', scan)
            abbreviations.setdefault((form, expansion), []).extend(att if isinstance(att, list) else [att])
    notation_rows = [[sign, form, list(dict.fromkeys(att)), status] for (sign, form, status), att in notation.items()]
    abbreviation_rows = [[form, meaning, list(dict.fromkeys(att))] for (form, meaning), att in abbreviations.items()]
    return notation_rows, abbreviation_rows


def normalize_inventory(record: dict, witness_root: Path) -> list[dict]:
    if record.get('inventory_confirmed') is not True:
        raise ValueError('inventory_confirmed must explicitly be true after root checks all elements.')
    if record.get('inventory_from_C') is True or record.get('inventory_source') == 'witness_C':
        candidates = list((witness_root / 'codex' / record['folder']).glob('*_inventory.csv'))
        if len(candidates) != 1:
            raise ValueError(f'Expected one C inventory, found {len(candidates)}')
        with candidates[0].open(encoding='utf-8') as f:
            rows = [dict(r) for r in csv.DictReader(f)
                    if int(r['scan']) == int(record['scan']) and str(r.get('cote', record['cote'])) == str(record['cote'])]
    else:
        rows = copy.deepcopy(record.get('inventory_rows', record.get('inventory', [])))
    if not isinstance(rows, list) or not rows or not all(isinstance(r, dict) for r in rows):
        raise ValueError('A nonempty inventory is required, from explicit rows or confirmed witness C inventory.')
    overrides = record.get('inventory_overrides', {})
    if isinstance(overrides, list):
        converted = {}
        for override in overrides:
            if not isinstance(override, dict) or 'element' not in override:
                raise ValueError('Each list-form inventory override needs an element.')
            key = str(override['element'])
            if key in converted:
                raise ValueError('Duplicate list-form inventory override id.')
            converted[key] = override.get('fields', {k: v for k, v in override.items() if k != 'element'})
        overrides = converted
    if not isinstance(overrides, dict):
        raise ValueError('inventory_overrides must be an object or a list of explicit element overrides.')
    if len({str(k) for k in overrides}) != len(overrides):
        raise ValueError('Inventory override keys collide after string conversion.')
    overrides = {str(k): v for k, v in overrides.items()}
    removal_list = record.get('inventory_remove_elements', [])
    if not isinstance(removal_list, list):
        raise ValueError('inventory_remove_elements must be a list.')
    removed = set(map(str, removal_list))
    if len(removed) != len(removal_list):
        raise ValueError('Duplicate inventory removal id.')
    element_counts = Counter(str(row.get('element')) for row in rows)
    for key in set(overrides) | removed:
        if element_counts[key] != 1:
            raise ValueError(f'Inventory operation must identify exactly one existing element: {key!r}')
    if set(overrides) & removed:
        raise ValueError('An inventory element cannot be both overridden and removed in one record.')
    for patch in overrides.values():
        if not isinstance(patch, dict) or set(patch) - set(INV_FIELDS):
            raise ValueError('Inventory override has non-object or unsupported row fields.')
    kept = []
    for row in rows:
        if str(row.get('element')) in removed:
            continue
        if 'sheet_kind' in record:
            row['sheet_kind'] = record['sheet_kind']
        row.update(overrides.get(str(row.get('element')), {}))
        kept.append(row)
    additions = record.get('inventory_extra', record.get('inventory_additions', []))
    if not isinstance(additions, list) or not all(isinstance(r, dict) for r in additions):
        raise ValueError('Inventory additions must be a list of row objects.')
    kept.extend(copy.deepcopy(additions))
    for row in kept:
        allowed_scan_values = {str(record['scan']), f"{record['cote']}:{int(record['scan']):03d}",
                               str(record.get('scan_label', f"{record['cote']}:{int(record['scan']):03d}"))}
        if 'scan' in row and str(row['scan']) not in allowed_scan_values:
            raise ValueError('An inventory row has a scan identity different from its page record.')
        row['scan'] = record.get('scan_label', f"{record['cote']}:{int(record['scan']):03d}")
        if 'sheet_kind' not in row and 'sheet_kind' in record:
            row['sheet_kind'] = record['sheet_kind']
        row['hand'] = {'typed': 'typewriter', 'Grothendieck': 'his hand',
                       'other hand': 'another unnamed hand'}.get(row.get('hand'), row.get('hand', 'unknown'))
        row['kind'] = {'handwritten': 'text', 'letter part': 'text'}.get(row.get('kind'), row.get('kind'))
        if 'transcribed' in row and row['transcribed'] != 'yes':
            raise ValueError('An explicitly incomplete inventory row cannot be converted to yes; root must correct it explicitly.')
        row['transcribed'] = 'yes'
        if row.get('kind') not in INVENTORY_KINDS:
            raise ValueError(f"Unsupported inventory kind: {row.get('kind')!r}; supply an explicit override.")
        if row.get('sheet_kind') not in SHEET_KINDS:
            raise ValueError(f"Unsupported sheet kind: {row.get('sheet_kind')!r}")
        for field in INV_FIELDS:
            if field not in row:
                raise ValueError(f'Missing inventory field {field}: {row}')
    return [{k: r[k] for k in INV_FIELDS} for r in kept]


def prepare(record: dict, witness_root: Path) -> tuple[dict, str]:
    record = copy.deepcopy(record)
    for k in ['folder', 'cote', 'scan']:
        if k not in record:
            raise ValueError(f'Missing {k}')
    record['cote'] = str(record['cote'])
    record['scan'] = int(record['scan'])
    rows = read_map(witness_root)
    matches = [r for r in rows if r['folder'] == record['folder'] and r['cote'] == record['cote'] and int(r['our_scan']) == record['scan']]
    if len(matches) != 1:
        raise ValueError('Page identity must match exactly one page_map row.')
    mapped = matches[0]
    record['map'] = mapped
    record['key'] = page_key(record)
    validate_record_metadata(record)
    source_raw = (witness_root / mapped['codex_file']).read_bytes()
    record['source_C_sha256'] = hashlib.sha256(source_raw).hexdigest()
    # Keep the existing universal-newline edit workflow, but hash actual source bytes.
    source = source_raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
    text = source
    for n, edit in enumerate(record.get('edits', []), 1):
        old, new = edit['old'], edit['new']
        if not old:
            raise ValueError(f'Edit {n}: empty old string is prohibited.')
        expected = edit.get('count', 1)
        actual = text.count(old)
        if actual != expected:
            raise ValueError(f'Edit {n}: expected {expected} occurrences, found {actual}: {old!r}')
        text = text.replace(old, new)
    for n, ch in enumerate(record.get('changes', []), 1):
        for field in ['place', 'C', 'H', 'final', 'shows', 'confidence', 'against_C', 'against_H']:
            if field not in ch:
                raise ValueError(f'Change {n}: missing {field}')
        if ch['confidence'] not in {'high', 'medium', 'low'}:
            raise ValueError(f'Change {n}: invalid confidence')
        if not isinstance(ch['against_C'], bool) or not isinstance(ch['against_H'], bool):
            raise ValueError(f'Change {n}: against_C and against_H must be booleans')
        if ch['against_H']:
            if mapped['hua_has'] != 'text':
                raise ValueError('No H collation rows may be recorded for a page without H text.')
            if ch.get('kind') not in KINDS:
                raise ValueError(f"Change {n}: invalid H kind {ch.get('kind')!r}")
            if 'marked_in_H' not in ch:
                raise ValueError(f'Change {n}: marked_in_H required for an H difference')
    record['inventory_resolved'] = normalize_inventory(record, witness_root)
    for n in record.get('notation_updates', []):
        if not any(n.get(k) for k in ('sign', 'notation', 'key')):
            raise ValueError('Notation update needs sign, notation, or key.')
    record['page_sha256'] = hashlib.sha256(text.encode()).hexdigest()
    validate_record_metadata(record)
    return record, text


def render(output_root: Path) -> None:
    registry = output_root / 'documentation' / 'page_records'
    records = [json.loads(p.read_text(encoding='utf-8')) for p in registry.glob('*.json')]
    records.sort(key=lambda r: (int(r['cote']), int(r['scan'])))
    for record in records:
        validate_record_metadata(record)
    global_file = output_root / 'documentation' / 'editorial_metadata.json'
    global_meta = json.loads(global_file.read_text(encoding='utf-8')) if global_file.exists() else {}
    if not isinstance(global_meta, dict):
        raise ValueError('Editorial metadata must be an object.')
    for field in ['legibility', 'additional_doubts_text']:
        if field in global_meta:
            require_string(global_meta[field], f'Editorial metadata {field}')
    changes = ['# Changes against witnesses C and H\n',
               'Counts refer to recorded loci, not individual letters or words. A locus differing from both witnesses is counted once against each. Macro syntax alone is excluded by the reader.\n']
    counts, consequential, collation, inventory = [], [], [], []
    total_c = total_h = 0
    total_conf = Counter()
    for r in records:
        cc = sum(c['against_C'] for c in r.get('changes', []))
        hh = sum(c['against_H'] for c in r.get('changes', []))
        conf = Counter(c['confidence'] for c in r.get('changes', []) if c['against_C'] or c['against_H'])
        total_c += cc; total_h += hh; total_conf.update(conf)
        counts.append([f"{r['cote']}:{r['scan']:03d}", cc, hh, conf['high'], conf['medium'], conf['low']])
        for c in r.get('changes', []):
            if c.get('consequential'):
                explanation = c['consequential'] if isinstance(c['consequential'], str) else c['final']
                consequential.append(f"- {r['cote']}:{r['scan']:03d}, {c['place']}: {explanation}\n")
            if c['against_H']:
                collation.append(dict(zip(COLL_FIELDS, [r['folder'], r['map']['their_page'], r['scan'],
                    c['place'], c['H'], c['C'], c['final'], c['shows'] + (f" [crop: {c['crop']}]" if c.get('crop') else ''),
                    c['kind'], c['marked_in_H'], c['confidence']])))
        inventory.extend(r['inventory_resolved'])
    counts.append(['ALL', total_c, total_h, total_conf['high'], total_conf['medium'], total_conf['low']])
    changes.append(table(['Scan (cote:scan)', 'Against C', 'Against H', 'High', 'Medium', 'Low'], counts))
    changes.append('\n## Consequential corrections\n\n' + (''.join(consequential) or 'None recorded so far.\n'))
    notation_rows, abbreviation_rows = editorial_table_rows(records)
    doubts = []
    for r in records:
        scan = f"{r['cote']}:{r['scan']:03d}"
        changes.append(f'\n## {r["folder"]} — cote {r["cote"]}, scan {r["scan"]:03d}\n\n')
        if r.get('changes'):
            changes.append(table(['Place', 'C', 'H', 'Final', 'What the scan shows', 'Crop', 'Confidence', 'Differs from'],
                                 [[c['place'], c['C'], c['H'], c['final'], c['shows'], c.get('crop', ''), c['confidence'],
                                   ', '.join(w for w in ['C', 'H'] if c['against_' + w])] for c in r['changes']]))
        else:
            changes.append('No reading differences recorded.\n')
        changes.append('\n### Unresolved places\n\n')
        remaining = r.get('remaining_doubts', [])
        if remaining:
            changes.append(table(['Place', 'Reading', 'Alternatives', 'Confidence', 'Comment'],
                                 [[d.get('line', d.get('place', '')), d.get('reading', ''), d.get('alternatives', ''),
                                   d.get('confidence', ''), d.get('comment', d.get('reason', ''))] for d in remaining]))
            doubts.extend([[scan, d.get('line', d.get('place', '')), d.get('reading', ''), d.get('alternatives', ''),
                            d.get('confidence', ''), d.get('comment', d.get('reason', ''))] for d in remaining])
        else:
            changes.append('None recorded.\n')
    changes_text = '\n'.join(changes)
    (output_root / f'{PREFIX}_changes.md').write_text(changes_text, encoding='utf-8')
    write_csv(output_root / f'{PREFIX}_collation.tsv', COLL_FIELDS, collation, delimiter='\t')
    write_csv(output_root / f'{PREFIX}_inventory.csv', INV_FIELDS, inventory)
    doubt_text = '# Notation table\n\n'
    doubt_text += table(['Sign or usage', 'Form in the ink and transcription', 'Attestations', 'Status'],
                        notation_rows)
    doubt_text += '\n# Remaining doubts\n\n' + table(['Scan (cote:scan)', 'Place', 'Reading', 'Alternatives', 'Confidence', 'Comment'], doubts)
    doubt_text += '\n# Abbreviations\n\n' + table(['Abbreviation', 'Possible expansion (editorial only)', 'Attestations'],
                                               abbreviation_rows)
    doubt_text += '\n# Legibility and witnesses\n\n' + global_meta.get('legibility', 'Work in progress. Only the completed pages recorded above have been assessed.') + '\n'
    if global_meta.get('additional_doubts_text'):
        doubt_text += '\n' + global_meta['additional_doubts_text'] + '\n'
    (output_root / f'{PREFIX}_doubts.md').write_text(doubt_text, encoding='utf-8')


def record_page(record: dict, witness_root=DEFAULT_WITNESSES, output_root=DEFAULT_OUT,
                finalize=False, allow_update=False) -> dict:
    witness_root, output_root = Path(witness_root), Path(output_root)
    prepared, text = prepare(record, witness_root)
    result = {'key': prepared['key'], 'bytes': len(text.encode()), 'changes': len(prepared.get('changes', [])),
              'inventory_rows': len(prepared['inventory_resolved']), 'finalized': False}
    if not finalize:
        return result
    log_path = output_root / 'progress.log'
    log_text = log_path.read_text(encoding='utf-8') if log_path.exists() else ''
    if 'transcription frozen ' in log_text or 'context opened ' in log_text:
        raise ValueError('Transcription is frozen or context has opened; page mutation is prohibited.')
    registry = output_root / 'documentation' / 'page_records'
    target_record = registry / f"{prepared['key']}.json"
    if target_record.exists() and not allow_update:
        raise FileExistsError(f'{prepared["key"]} already recorded; use allow_update for an explicit correction.')
    if target_record.exists() and allow_update:
        prior = json.loads(target_record.read_text(encoding='utf-8'))
        if prior.get('audits'):
            raise ValueError('Use record_audit.py for an audited page; C-based replacement would discard audit history.')
        sessions = output_root / 'documentation' / 'audit_sessions'
        for p in sessions.glob('*.json'):
            session = json.loads(p.read_text(encoding='utf-8'))
            if session.get('key') == prepared['key'] and session.get('status') in {'started', 'commit_pending'}:
                raise ValueError('Page has an active audit; revise only through record_audit.py.')
    ordered = read_map(witness_root)
    done_keys = set()
    for line in log_text.splitlines():
        match = re.fullmatch(r'scan (\d+) done .+ cote=(\d+) folder=(\S+)', line)
        if match:
            done_keys.add(f'{match[3]}_{match[2]}_scan{int(match[1]):03d}')
    previous = []
    for m in ordered:
        k = f"{m['folder']}_{m['cote']}_scan{int(m['our_scan']):03d}"
        if k == prepared['key']:
            break
        if not (registry / f'{k}.json').exists() or k not in done_keys:
            previous.append(k)
    if previous:
        raise ValueError('Earlier pages have not been finalized: ' + ', '.join(previous))
    registry.mkdir(parents=True, exist_ok=True)
    (output_root / 'pages').mkdir(parents=True, exist_ok=True)
    prepared['recorded_utc'] = utc()
    staging_parent = output_root.parent / 'work' / 'record_staging'
    staging_parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=staging_parent) as temporary:
        stage = Path(temporary)
        staged_registry = stage / 'documentation/page_records'
        staged_registry.mkdir(parents=True)
        originals = {}
        for path in registry.glob('*.json'):
            raw = path.read_bytes(); originals[path.name] = hashlib.sha256(raw).hexdigest()
            (staged_registry / path.name).write_bytes(raw)
        staged_record = staged_registry / target_record.name
        staged_record.write_text(json.dumps(prepared, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        editorial = output_root / 'documentation/editorial_metadata.json'
        editorial_raw = editorial.read_bytes() if editorial.exists() else None
        if editorial_raw is not None:
            (stage / 'documentation/editorial_metadata.json').write_bytes(editorial_raw)
        # All report validation and generation must succeed before page/record publication.
        render(stage)
        staged_page = stage / 'page.tex'; staged_page.write_text(text, encoding='utf-8')
        current_log = log_path.read_text(encoding='utf-8') if log_path.exists() else ''
        if 'transcription frozen ' in current_log or 'context opened ' in current_log:
            raise ValueError('Transcription froze or context opened while staging; no page committed.')
        current_records = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in registry.glob('*.json')}
        if current_records != originals:
            raise ValueError('Page-record state changed while staging; no page committed.')
        if (editorial.read_bytes() if editorial.exists() else None) != editorial_raw:
            raise ValueError('Editorial metadata changed while staging; no page committed.')
        os.replace(staged_page, output_root / 'pages' / f"{prepared['key']}.tex")
        os.replace(staged_record, target_record)
        for filename in [f'{PREFIX}_changes.md', f'{PREFIX}_collation.tsv', f'{PREFIX}_inventory.csv', f'{PREFIX}_doubts.md']:
            os.replace(stage / filename, output_root / filename)
    state = 'corrected' if allow_update and prepared['key'] in done_keys else 'done'
    with log_path.open('a', encoding='utf-8') as f:
        f.write(f"scan {prepared['scan']:03d} {state} {utc()} cote={prepared['cote']} folder={prepared['folder']}\n")
    result['finalized'] = True
    result['page'] = str(output_root / 'pages' / f"{prepared['key']}.tex")
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('record', nargs='?', type=Path, help='Root-authored JSON page record')
    ap.add_argument('--witness-root', type=Path, default=DEFAULT_WITNESSES)
    ap.add_argument('--output', type=Path, default=DEFAULT_OUT)
    ap.add_argument('--finalize', action='store_true')
    ap.add_argument('--allow-update', action='store_true')
    ap.add_argument('--render', action='store_true', help='Regenerate derived logs only; do not change pages')
    args = ap.parse_args()
    if args.render:
        render(args.output)
        print('Rendered logs from existing explicit page records; no page or progress-log change.')
        return
    if args.record is None:
        ap.error('record is required unless --render is given')
    record = json.loads(args.record.read_text(encoding='utf-8'))
    print(json.dumps(record_page(record, args.witness_root, args.output, args.finalize, args.allow_update), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
