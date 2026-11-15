#!/usr/bin/env python3
"""Prepare, but never apply, the required seven-label inventory conversion.

Only the live CSV and its existing metadata labels are read. No scan image,
transcription page, or context source is opened. The default output is a
separate CSV under records/. Provenance records the original kind and element
ID for every source row and supports exact reconstruction of all eight fields.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import io
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'MPL_134-8_043-087_inventory.csv'
RECORDS = ROOT / 'records'
FIELDS = ['cote', 'scan', 'sheet_kind', 'element', 'kind', 'position',
          'first_words_or_objects', 'transcribed']
ALLOWED = ['text', 'display', 'diagram', 'drawing', 'margin note',
           'insertion', 'deletion']

# Each tuple is the ordered sequence of output kinds for one source row.
# Qualifiers such as typed, faded, clipped, boxed, marginal, or underlined
# remain recoverable in the provenance; no original field value is discarded.
MAPPING = {
    'annotation': ('text',),
    'boxed_formula': ('display',),
    'bracketed_text': ('text',),
    'bracketed_text_formula': ('text', 'display'),
    'claim_formula': ('text', 'display'),
    'clipped_text': ('text',),
    'deletion': ('deletion',),
    'deletion_insertion': ('deletion', 'insertion'),
    'diagram': ('diagram',),
    'display': ('display',),
    'drawing': ('drawing',),
    'faded_typed_text': ('text',),
    'formula': ('display',),
    'insertion': ('insertion',),
    'margin note': ('margin note',),
    'marginal_formula': ('margin note',),
    'marginal_note': ('margin note',),
    'overtyping': ('text',),
    'page_number': ('text',),
    'question': ('display',),
    'question_formula': ('display',),
    'stray_typed_marks': ('text',),
    'symbol': ('display',),
    'symbols': ('display',),
    'text': ('text',),
    'text_formula': ('text', 'display'),
    'text_insertion': ('text', 'insertion'),
    'title': ('text',),
    'typed_section': ('text',),
    'typed_text': ('text',),
    'underbrace': ('display',),
    'underline': ('text',),
    'unfinished_formula': ('display',),
}

REASONS = {
    'annotation': 'The recorded annotation is the word OK.',
    'boxed_formula': 'The box qualifies a formula; its content is retained as a display.',
    'bracketed_text': 'The existing label identifies bracketed text.',
    'bracketed_text_formula': 'The existing composite identifies text and a formula; both kinds receive a row.',
    'claim_formula': 'The recorded incipit begins with prose (Je dis qu’alors) followed by a formula; both kinds receive a row.',
    'clipped_text': 'Clipping is retained in the original label and incipit; the content kind is text.',
    'deletion_insertion': 'The existing composite names both revision states; it is split in that order.',
    'faded_typed_text': 'Fading and typescript are retained in provenance; the content kind is text.',
    'formula': 'The existing label identifies a formula.',
    'marginal_formula': 'The whole recorded element is a margin note containing mathematics.',
    'marginal_note': 'This is the existing margin-note label with its required spelling.',
    'overtyping': 'The proposed broad category is text; cancellation/insertion states are not assigned from metadata alone. See the explicit ambiguity below.',
    'page_number': 'The original page-number text is retained verbatim.',
    'question': 'Both recorded incipits are mathematical expressions with an epi/mono property; their question role remains in provenance.',
    'question_formula': 'The recorded incipit is a formula with a question mark; no separate prose component is recorded.',
    'stray_typed_marks': 'The existing metadata identifies typescript marks; their descriptions remain unchanged.',
    'symbol': 'The existing label identifies a standalone mathematical symbol.',
    'symbols': 'The existing label identifies standalone mathematical symbols.',
    'text_formula': 'The existing composite identifies text and a formula; both kinds receive a row.',
    'text_insertion': 'The existing composite identifies text and an insertion; both kinds receive a row.',
    'title': 'The original title text is retained verbatim.',
    'typed_section': 'Section structure and typescript remain in provenance; the content kind is text.',
    'typed_text': 'The content kind is text; the typescript qualifier remains in provenance.',
    'underbrace': 'The recorded element is a mathematical underbrace and its formula label.',
    'underline': 'The recorded underlined words remain text; the underline qualifier remains in provenance.',
    'unfinished_formula': 'The unfinished state remains in provenance and in the unchanged incipit.',
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reconstruct(output_rows, provenance_rows):
    """Recover the original ordered row dictionaries from output and sidecar."""
    by_id = {row['element']: row for row in output_rows}
    reconstructed = []
    for entry in provenance_rows:
        restored = dict(by_id[entry['outputs'][0]['element']])
        restored['element'] = entry['original_element']
        restored['kind'] = entry['original_kind']
        reconstructed.append(restored)
    return reconstructed


def convert(rows):
    output, provenance = [], []
    used_ids = set()
    preserved_fields = [field for field in FIELDS if field not in ('kind', 'element')]
    for index, original in enumerate(rows, 1):
        kinds = MAPPING[original['kind']]
        destinations = []
        for part, kind in enumerate(kinds):
            converted = dict(original)
            converted['kind'] = kind
            # The first output retains the original ID. A second output has a
            # role suffix, while the sidecar also retains the exact parent ID.
            converted['element'] = original['element'] if part == 0 else (
                original['element'] + '.' + kind.replace(' ', '_'))
            assert converted['element'] not in used_ids, 'Output ID collision'
            used_ids.add(converted['element'])
            assert kind in ALLOWED
            assert all(converted[field] == original[field] for field in preserved_fields)
            output.append(converted)
            destinations.append({'element': converted['element'], 'kind': kind})
        provenance.append({
            'source_record_index': index,
            'source_scan': original['scan'],
            'original_element': original['element'],
            'original_kind': original['kind'],
            'outputs': destinations,
        })
    assert reconstruct(output, provenance) == rows, 'Exact row reconstruction failed'
    return output, provenance


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def markdown_code(value):
    return '`' + str(value).replace('|', '&#124;').replace('\n', ' ') + '`'


def make_report(source, output_path, rows, converted, provenance, metadata, ambiguity):
    by_kind = defaultdict(list)
    for row in rows:
        by_kind[row['kind']].append(row)
    old_counts = Counter(row['kind'] for row in rows)
    new_counts = Counter(row['kind'] for row in converted)
    split_entries = [entry for entry in provenance if len(entry['outputs']) > 1]
    changed_rows = sum(row['kind'] not in ALLOWED for row in rows)
    lines = [
        '# Proposed inventory kind conversion', '',
        '**Status: prepared for principal-reader review; the live inventory was not overwritten.**', '',
        f"The input contains {len(rows):,} rows, {len(by_kind)} distinct kind values, and {len(set(row['scan'] for row in rows))} scans. The proposed CSV contains {len(converted):,} rows using exactly the seven permitted kind labels. {changed_rows} source rows have labels outside the required vocabulary; {len(split_entries)} of those source rows produce two adjacent output rows.", '',
        'The conversion reads the live inventory and existing metadata labels only. No scan image, transcription page, or context source is read.', '',
        '## Complete mapping', '',
        '| Original kind | Input rows | Output kind or ordered pair | Scans | Reason |',
        '|---|---:|---|---|---|',
    ]
    for kind in sorted(by_kind):
        scans = ', '.join(sorted({row['scan'] for row in by_kind[kind]}))
        outputs = ' + '.join(markdown_code(x) for x in MAPPING[kind])
        reason = REASONS.get(kind, 'Already one of the permitted labels; retained unchanged.')
        lines.append(f'| {markdown_code(kind)} | {old_counts[kind]} | {outputs} | {scans} | {reason} |')
    lines += [
        '', '## Exact forward and inverse operations', '',
        'For each source row, the forward operation copies all eight fields. It substitutes the required kind label and retains the original element ID for the first output row. Each additional row receives the same original content, position, scan, sheet kind, cote, and transcribed status, with a unique role suffix on its element ID. The original incipit is copied in full into every split row; no fragment of it is inferred or discarded.', '',
        'The provenance sidecar records the original kind, original element ID, source record index, and ordered output IDs for every input row. The inverse reads the first output for each source record, restores the saved original kind and element ID, and places the recovered row at its original record index. This inverse reconstructed every original row dictionary in its original order; all eight field values matched the input exactly.', '',
        f"Verified: {metadata['checks']['all_other_fields_preserved']}; unique output element IDs: {metadata['checks']['unique_output_ids']}; exact ordered reconstruction: {metadata['checks']['exact_ordered_reconstruction']}; all source/output transcribed values are yes: {metadata['checks']['all_transcribed_yes']}.", '',
        '## Split-row provenance', '',
        '| Original element | Original kind | Output elements and kinds |',
        '|---|---|---|',
    ]
    for entry in split_entries:
        destinations = '; '.join(markdown_code(item['element']) + ' → ' + markdown_code(item['kind']) for item in entry['outputs'])
        lines.append(f"| {markdown_code(entry['original_element'])} | {markdown_code(entry['original_kind'])} | {destinations} |")
    lines += ['', '## Classification requiring principal-reader judgment', '']
    for item in ambiguity:
        lines += [
            f"**{item['kind']} — {len(item['elements'])} source rows.** {item['reason']}", '',
            f"Proposed category: {markdown_code(item['proposed_kind'])}. A cancellation/insertion split remains a principal-reader decision; the proposal preserves the existing detailed label in provenance and assigns no such states from metadata alone.", '',
            'Affected elements: ' + ', '.join(markdown_code(x) for x in item['elements']) + '.', '',
        ]
    lines += [
        'No other kind classification remained unresolved on the supplied label and incipit evidence. Qualifiers such as faded, clipped, typed, boxed, and underlined remain in the original-kind field of the sidecar.', '',
        '## Resulting kind counts', '',
        '| Required kind | Output rows |', '|---|---:|',
    ]
    lines += [f'| {markdown_code(kind)} | {new_counts[kind]} |' for kind in ALLOWED]
    lines += [
        '', '## Files and reproduction', '',
        f'- Input: {markdown_code(str(source))}',
        f'- Proposed CSV: {markdown_code(str(output_path))}',
        '- Full mapping: `records/inventory_kind_mapping.json`',
        '- Complete row provenance and verification: `records/inventory_conversion_provenance.json`',
        '- Explicit ambiguity record: `records/inventory_kind_ambiguities.json`',
        '- Conversion script: `scripts/propose_inventory_kinds.py`', '',
        'Run the script again after any inventory changes. It refuses to use the live input path as the output path and writes a separate proposal by default.', '',
        '```sh', 'python MPL_134-8_043-087/scripts/propose_inventory_kinds.py', '```', '',
        f"Generated UTC: {metadata['generated_utc']}", '',
        f"Source SHA-256: `{metadata['source_sha256']}`", '',
        f"Proposed CSV SHA-256: `{metadata['proposed_sha256']}`", '',
        'These hashes describe this preparation run. The script leaves the source CSV and all per-scan JSON records unchanged.', '',
    ]
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=SOURCE)
    parser.add_argument('--output', type=Path, default=RECORDS / 'inventory_proposed.csv')
    args = parser.parse_args()
    source, output_path = args.source.resolve(), args.output.resolve()
    if output_path in {source, SOURCE.resolve()}:
        parser.error('The output must differ from the live input; this script never applies the conversion.')
    source_bytes = source.read_bytes()
    reader = csv.DictReader(io.StringIO(source_bytes.decode('utf-8'), newline=''))
    if reader.fieldnames != FIELDS:
        parser.error('The source CSV does not have the exact required eight-column header.')
    rows = list(reader)
    unknown = sorted({row['kind'] for row in rows} - set(MAPPING))
    if unknown:
        parser.error('Unmapped kind values require review: ' + ', '.join(unknown))
    if len({row['element'] for row in rows}) != len(rows):
        parser.error('The source inventory has duplicate element IDs; conversion was not written.')
    converted, provenance = convert(rows)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator='\r\n')
    writer.writeheader()
    writer.writerows(converted)
    proposed_bytes = buffer.getvalue().encode('utf-8')
    output_path.write_bytes(proposed_bytes)
    ambiguity = [{
        'kind': 'overtyping',
        'proposed_kind': 'text',
        'elements': [row['element'] for row in rows if row['kind'] == 'overtyping'],
        'reason': ('The existing label and per-scan metadata identify superimposed typescript, '
                   'but do not assign old/new cancellation or insertion states to every overstruck character. '
                   'A text classification retains the printed marks without adding those states.'),
    }]
    metadata = {
        'generated_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'status': 'proposal only; live inventory not overwritten',
        'source_path': str(source),
        'proposed_path': str(output_path),
        'source_sha256': sha256(source_bytes),
        'proposed_sha256': sha256(proposed_bytes),
        'source_rows': len(rows),
        'proposed_rows': len(converted),
        'source_counts_by_scan': dict(sorted(Counter(row['scan'] for row in rows).items())),
        'proposed_counts_by_scan': dict(sorted(Counter(row['scan'] for row in converted).items())),
        'additional_rows_by_scan': dict(sorted(Counter(
            entry['source_scan'] for entry in provenance for item in entry['outputs'][1:]).items())),
        'checks': {
            'all_other_fields_preserved': True,
            'unique_output_ids': len({row['element'] for row in converted}) == len(converted),
            'exact_ordered_reconstruction': reconstruct(converted, provenance) == rows,
            'allowed_output_kinds': sorted({row['kind'] for row in converted}),
            'all_transcribed_yes': all(row['transcribed'] == 'yes' for row in rows + converted),
            'source_bytes_unchanged_at_completion': source.read_bytes() == source_bytes,
        },
        'rows': provenance,
    }
    mapping_record = {
        'allowed_kind_values': ALLOWED,
        'mapping': {kind: {'output_kinds': list(MAPPING[kind]),
                           'reason': REASONS.get(kind, 'Already permitted; retained unchanged.')}
                    for kind in sorted(MAPPING)},
    }
    RECORDS.mkdir(parents=True, exist_ok=True)
    write_json(RECORDS / 'inventory_kind_mapping.json', mapping_record)
    write_json(RECORDS / 'inventory_conversion_provenance.json', metadata)
    # Verify the serialized deliverables as well as the in-memory operation.
    with output_path.open(newline='', encoding='utf-8') as saved_file:
        saved_rows = list(csv.DictReader(saved_file))
    saved_provenance = json.loads((RECORDS / 'inventory_conversion_provenance.json').read_text(encoding='utf-8'))
    assert reconstruct(saved_rows, saved_provenance['rows']) == rows, 'Saved-file reconstruction failed'
    assert sha256(output_path.read_bytes()) == metadata['proposed_sha256']
    metadata['checks']['saved_file_exact_ordered_reconstruction'] = True
    write_json(RECORDS / 'inventory_conversion_provenance.json', metadata)
    write_json(RECORDS / 'inventory_kind_ambiguities.json', ambiguity)
    (RECORDS / 'inventory_kind_review.md').write_text(
        make_report(source, output_path, rows, converted, provenance, metadata, ambiguity), encoding='utf-8')
    assert source.read_bytes() == source_bytes, 'The source changed during this preparation run.'
    print(f'Prepared {len(converted)} proposed rows from {len(rows)} source rows.')
    print('Exact ordered reconstruction of all original fields: PASS')
    print('Live inventory unchanged: PASS')
    print('Ambiguous classification group retained for review: overtyping (' + str(len(ambiguity[0]['elements'])) + ' rows).')
    print('Proposal:', output_path)


if __name__ == '__main__':
    main()
