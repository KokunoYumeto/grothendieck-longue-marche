#!/usr/bin/env python3
"""Exclude the unresolved first (88) relation from substantive witness counts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'reviewed' / '147_scan072.json'
ROW_ID = '072-02'
FINAL = r'\widehat M_{D_1}\unsure{=|\simeq}\widehat M_{G_1}\simeq\widehat M_{1,1}'
NOTE = ('The unresolved relation 072-02 remains in the page, doubts and B04 '
        'adjudication, and is excluded from the 20 substantive changes.')


def main():
    source = PATH.read_text()
    record = json.loads(source)
    matches = [row for row in record['changes'] if row.get('id') == ROW_ID]
    if not matches:
        if NOTE not in record['root_review_notes']:
            raise SystemExit('Row already absent but classification note differs; review required')
        print('147_scan072.json unresolved relation already excluded')
        return
    if len(matches) != 1 or len(record['changes']) != 21:
        raise SystemExit('Unexpected change-list state; refusing an unrelated edit')
    row = matches[0]
    if (row['final'] != FINAL or row['against_C'] is not False
            or row['against_H'] is not True
            or 'the H comparison remains unresolved' not in row['evidence']):
        raise SystemExit('Unexpected 072-02 classification or reading')
    adjudications = json.loads((ROOT / 'second' / '147_scan072_adjudications.json').read_text())
    b04 = next(a for a in adjudications if a['box'] == 'B04')
    if FINAL not in b04['final'] or b04['changed'] is not False:
        raise SystemExit('B04 authority changed; review this repair before applying')
    if record['doubts'][0]['reading'] != r'\unsure{=|\simeq}':
        raise SystemExit('Expected retained first-relation doubt is missing')
    old_note = record['root_review_notes']
    old_phrase = "Accepted the reader's 21 logged places"
    if old_note.count(old_phrase) != 1:
        raise SystemExit('Unexpected root-review count description')
    new_note = old_note.replace(old_phrase, "Reviewed the reader's 21 originally logged places", 1)
    new_note += ' ' + NOTE
    # Remove only this serialized list entry and replace the one narrative field.
    row_token = '\n'.join('    ' + line for line in json.dumps(row, ensure_ascii=False, indent=2).splitlines()) + ',\n'
    note_token = json.dumps(old_note, ensure_ascii=False)
    if source.count(row_token) != 1 or source.count(note_token) != 1:
        raise SystemExit('Unexpected JSON formatting; refusing a broader rewrite')
    updated = source.replace(row_token, '', 1).replace(note_token, json.dumps(new_note, ensure_ascii=False), 1)
    record['changes'].remove(row)
    record['root_review_notes'] = new_note
    if json.loads(updated) != record:
        raise SystemExit('Repair would change an unexpected JSON field')
    PATH.write_text(updated)
    print('Removed 072-02 from substantive changes (21 -> 20); clarified root_review_notes only')


if __name__ == '__main__':
    main()
