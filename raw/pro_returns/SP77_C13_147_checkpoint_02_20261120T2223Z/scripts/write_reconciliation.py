"""Copy an explicit root-authored plan into a reconciliation TSV.

Usage: python scripts/write_reconciliation.py SCAN PLAN_JSON

The JSON object maps every token-different box ID to an object containing
decision, evidence, final_reading, changed ("yes" or "no"), crop, and
viewed_by ("root").  These are supplied statements, not observations made
by this helper.  The helper neither chooses readings nor inspects images,
changes page/record files, or closes an audit.
"""

import argparse
import csv
import io
import json
from pathlib import Path


W = Path(__file__).resolve().parents[1]
FIELDS = [
    'box', 'first', 'second', 'decision', 'final_reading', 'changed',
    'evidence', 'crop', 'viewed_by',
]
PLAN_FIELDS = (
    'decision', 'evidence', 'final_reading', 'changed', 'crop', 'viewed_by',
)


def unique_object(pairs):
    """Reject duplicate JSON keys instead of silently losing a decision."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key!r}')
        result[key] = value
    return result


def read_comparison(path):
    with path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        required = {'box', 'first', 'second', 'equal_tokens'}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError('Comparison is missing required columns')
        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError('Comparison contains duplicate columns')
        rows = list(reader)

    seen = set()
    differences = []
    for row in rows:
        if None in row or any(row.get(key) is None for key in required):
            raise ValueError('Comparison contains a malformed row')
        box = row['box']
        if not box.strip() or box in seen:
            raise ValueError(f'Comparison contains an empty or duplicate box ID: {box!r}')
        seen.add(box)
        if row['equal_tokens'] not in ('yes', 'no'):
            raise ValueError(f'{box}: equal_tokens must be yes or no')
        if row['equal_tokens'] == 'no':
            differences.append(row)
    return differences


def write_reconciliation(scan, plan_path):
    if scan < 1:
        raise ValueError('SCAN must be a positive integer')
    base = W / 'second' / f'147_scan{scan:03d}'
    output = Path(str(base) + '_reconciliation.tsv')
    if output.exists() or output.is_symlink():
        raise FileExistsError(f'Refusing to overwrite {output}')

    differences = read_comparison(Path(str(base) + '_comparison.tsv'))
    with Path(plan_path).open(encoding='utf-8') as stream:
        plan = json.load(stream, object_pairs_hook=unique_object)
    if not isinstance(plan, dict):
        raise ValueError('The plan must be a JSON object keyed by box ID')

    expected = {row['box'] for row in differences}
    missing = expected - set(plan)
    extra = set(plan) - expected
    if missing or extra:
        raise ValueError(
            f'Plan must cover exactly the token-different boxes; '
            f'missing={sorted(missing)}, extra={sorted(extra)}'
        )

    output_rows = []
    for comparison in differences:
        box = comparison['box']
        entry = plan[box]
        if not isinstance(entry, dict):
            raise ValueError(f'{box}: plan entry must be an object')
        for field in PLAN_FIELDS:
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f'{box}: {field} must be a nonblank string')
        if entry['changed'] not in ('yes', 'no'):
            raise ValueError(f'{box}: changed must be yes or no')
        if entry['viewed_by'] != 'root':
            raise ValueError(f'{box}: viewed_by must be root')
        if not (W / entry['crop']).is_file():
            raise ValueError(f'{box}: missing crop file {entry["crop"]!r}')

        # Source values are copied as parsed, with no trimming or normalization.
        row = {key: comparison[key] for key in ('box', 'first', 'second')}
        row.update({key: entry[key] for key in PLAN_FIELDS})
        output_rows.append(row)

    # Serialize before exclusive creation; never replace an existing file.
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, delimiter='\t')
    writer.writeheader()
    writer.writerows(output_rows)
    with output.open('x', encoding='utf-8', newline='') as stream:
        stream.write(buffer.getvalue())
    return output, len(output_rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scan', metavar='SCAN', type=int)
    parser.add_argument('plan', metavar='PLAN_JSON', type=Path)
    args = parser.parse_args()
    try:
        output, count = write_reconciliation(args.scan, args.plan)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f'Error: {error}\n')
    print(json.dumps({
        'reconciliation': str(output),
        'rows': count,
        'status': 'Copied root-supplied plan; no visual inspection or audit closure performed.',
    }))


if __name__ == '__main__':
    main()
