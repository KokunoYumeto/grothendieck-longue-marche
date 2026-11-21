#!/usr/bin/env python3
"""Propagate B13's uncertain I-prime into two existing scan073 descriptions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'reviewed' / '147_scan073.json'
REPAIRS = [
    ('doubts', 6, 'reading',
     r"\deleted{2g'+\operatorname{card}I'\geq\unsure{2}}",
     r"\deleted{2g'+\operatorname{card}I^{\unsure{\prime}}\geq\unsure{2}}"),
    ('inventory', 18, 'first_words_or_objects',
     "2g'+card I'>=doubtful2",
     r"2g'+card I^{\unsure{\prime}}>=doubtful2"),
]


def main():
    source = PATH.read_text()
    record = json.loads(source)
    adjudications = json.loads((ROOT / 'second' / '147_scan073_adjudications.json').read_text())
    b13 = next(a for a in adjudications if a['box'] == 'B13')
    if REPAIRS[0][4] not in b13['final']:
        raise SystemExit('B13 authority changed; review this repair before applying')
    updated = source
    changed = []
    for key, index, field, old, new in REPAIRS:
        current = record[key][index][field]
        if current == new:
            continue
        if current != old:
            raise SystemExit(f'Unexpected {key}[{index}].{field}; refusing an unrelated edit')
        token = json.dumps(old, ensure_ascii=False)
        if updated.count(token) != 1:
            raise SystemExit(f'Expected one serialized target for {key}[{index}].{field}')
        updated = updated.replace(token, json.dumps(new, ensure_ascii=False), 1)
        record[key][index][field] = new
        changed.append(f'{key}[{index}].{field}')
    if json.loads(updated) != record:
        raise SystemExit('Repair would change an unexpected JSON field')
    if changed:
        PATH.write_text(updated)
    print(json.dumps({'scan': 73, 'changed_fields': changed}, ensure_ascii=False))


if __name__ == '__main__':
    main()
