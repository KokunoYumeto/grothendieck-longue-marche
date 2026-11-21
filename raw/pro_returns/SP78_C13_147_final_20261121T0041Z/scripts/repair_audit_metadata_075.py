#!/usr/bin/env python3
"""Exclude three unresolved scan075 comparisons, retaining their complete history."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'reviewed' / '147_scan075.json'
# Original rows, including both witnesses, readings, evidence and classifications.
REMOVED = json.loads(r'''[
  {
    "id": "075-24",
    "place": "Letter below first left vertex",
    "C": "$C$",
    "H": "$c$",
    "final": "$\\unsure{C|c}$",
    "evidence": "The isolated curved letter is larger than some subscripts but does not decisively distinguish capital C from lower-case c. C is retained first, with H’s lower-case reading explicitly possible; this comparison row does not declare H wrong.",
    "crop": "147_scan075_place09.png",
    "box": [
      470,
      1308,
      1477,
      1506
    ],
    "confidence": "low",
    "against_C": false,
    "against_H": true,
    "kind": "misread symbol or index",
    "marked_in_H": false,
    "error_sheet_kind": "symbols and indices",
    "consequential": false
  },
  {
    "id": "075-27",
    "place": "Second drawing, fourth label",
    "C": "$c_{i+2}$",
    "H": "$c_{i+2}$",
    "final": "$\\unsure{c_{i-2}|c_{i+2}}$",
    "evidence": "The small operator is thickened into a horizontal wedge. Minus is preferred because no separate upright can be isolated, but the overwork prevents excluding a compact plus. Neither witness’s plus is treated as definitively disproved.",
    "crop": "147_scan075_place11.png",
    "box": [
      700,
      1557,
      1268,
      1680
    ],
    "confidence": "low",
    "against_C": true,
    "against_H": true,
    "kind": "misread symbol or index",
    "marked_in_H": false,
    "error_sheet_kind": "symbols and indices",
    "consequential": true
  },
  {
    "id": "075-31",
    "place": "Final prose, second c label",
    "C": "$c_{i+1}$",
    "H": "$c_{i+1}$",
    "final": "$\\unsure{c_{i-1}|c_{i+1}}$",
    "evidence": "The tiny operator after i is an overworked horizontal wedge without a securely separate upright. Minus is preferred, while plus remains possible. The complete c_i et c-label phrase is retained in the blind box; expected adjacency does not supply the sign.",
    "crop": "147_scan075_place13.png",
    "box": [
      305,
      1818,
      1676,
      1975
    ],
    "confidence": "low",
    "against_C": true,
    "against_H": true,
    "kind": "misread symbol or index",
    "marked_in_H": false,
    "error_sheet_kind": "symbols and indices",
    "consequential": true
  }
]''')
OLD_ROOT = 'all thirty-two comparison rows'
NEW_ROOT = 'all twenty-nine substantive comparison rows and the three uncounted unresolved comparisons'
OLD_NOTE = 'Every substantive comparison has an existing saved crop, including unresolved comparisons retaining C against H.'
NEW_NOTE = ('Every substantive comparison has an existing saved crop. The unresolved '
            'C/c and two minus/plus choices remain in the doubts and are excluded '
            'from the 29 substantive rows.')


def main():
    source = PATH.read_text()
    record = json.loads(source)
    ids = {row['id'] for row in REMOVED}
    found = [row for row in record['changes'] if row['id'] in ids]
    if not found:
        if (NEW_ROOT not in record['root_review_notes']
                or NEW_NOTE not in record['notes'][7]):
            raise SystemExit('Rows absent but summaries differ; review required')
        print('147_scan075.json uncertainty-only comparisons already excluded')
        return
    if found != REMOVED or len(record['changes']) != 32:
        raise SystemExit('Original row payload or count changed; refusing an unrelated edit')
    old_root_note = record['root_review_notes']
    old_note = record['notes'][7]
    if old_root_note.count(OLD_ROOT) != 1 or old_note.count(OLD_NOTE) != 1:
        raise SystemExit('Unexpected summary wording')
    new_root_note = old_root_note.replace(OLD_ROOT, NEW_ROOT, 1)
    new_note = old_note.replace(OLD_NOTE, NEW_NOTE, 1)
    updated = source
    for row in REMOVED:
        token = '\n'.join('    ' + line for line in json.dumps(row, ensure_ascii=False, indent=2).splitlines()) + ',\n'
        if updated.count(token) != 1:
            raise SystemExit('Unexpected row formatting; refusing a broader rewrite')
        updated = updated.replace(token, '', 1)
    for old, new in [(old_root_note, new_root_note), (old_note, new_note)]:
        token = json.dumps(old, ensure_ascii=False)
        if updated.count(token) != 1:
            raise SystemExit('Expected exactly one serialized summary')
        updated = updated.replace(token, json.dumps(new, ensure_ascii=False), 1)
    record['changes'] = [row for row in record['changes'] if row['id'] not in ids]
    record['root_review_notes'] = new_root_note
    record['notes'][7] = new_note
    if json.loads(updated) != record or len(record['changes']) != 29:
        raise SystemExit('Repair would change unexpected fields or counts')
    PATH.write_text(updated)
    print(json.dumps({'scan': 75, 'removed_ids': sorted(ids),
                      'substantive_rows': 29,
                      'summary_fields': ['root_review_notes', 'notes[7]']}))


if __name__ == '__main__':
    main()

