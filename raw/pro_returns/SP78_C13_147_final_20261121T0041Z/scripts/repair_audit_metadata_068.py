#!/usr/bin/env python3
"""Update only scan068's stale hand-log delimiter claim after B19 adjudication."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'reviewed' / '147_scan068.json'
OLD = ('Checked at the opening M infinity, inserted adjective, lieu de mettre, '
       'Aut phrase, and two lower gauche insertions; the real parenthesis after '
       'the lower ellipsis and the final unmatched closing parenthesis remain.')
NEW = ('Checked at the opening M infinity, inserted adjective, lieu de mettre, '
       'Aut phrase, and two lower gauche insertions; the closing parenthesis '
       'after the lower ellipsis is secure. The final unmatched closing delimiter '
       'after combinatoire remains uncertain between ) and ], transcribed as '
       '\\unsure{)|]}.')


def main():
    source = PATH.read_text()
    record = json.loads(source)
    current = record['hand_log'][2]['all_occurrences']
    if current == NEW:
        print('147_scan068.json hand_log[2].all_occurrences already current')
        return
    if current != OLD:
        raise SystemExit('Unexpected hand-log value; refusing an unrelated edit')
    decisions = json.loads((ROOT / 'second' / '147_scan068_root_decisions.json').read_text())
    if not decisions['B19']['final'].endswith('\\unsure{)|]}'):
        raise SystemExit('B19 authority changed; review this repair before applying')
    old_token = json.dumps(OLD, ensure_ascii=False)
    if source.count(old_token) != 1:
        raise SystemExit('Expected exactly one serialized target string')
    updated = source.replace(old_token, json.dumps(NEW, ensure_ascii=False), 1)
    record['hand_log'][2]['all_occurrences'] = NEW
    if json.loads(updated) != record:
        raise SystemExit('Repair would change an unexpected JSON field')
    PATH.write_text(updated)
    print('Updated 147_scan068.json hand_log[2].all_occurrences only')


if __name__ == '__main__':
    main()
