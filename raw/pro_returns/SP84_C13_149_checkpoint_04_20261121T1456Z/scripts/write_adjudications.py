"""Serialize explicit main-reader crop decisions; never infer a reading."""
from pathlib import Path
import csv
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def write(n, choices_path):
    stem = f'149_scan{n:03d}'
    first = {r['box']: r['reading'] for r in rows(ROOT / f'second/{stem}_first.tsv')}
    second = {r['box']: r['reading'] for r in rows(ROOT / f'second/{stem}_second.tsv')}
    boxes = rows(ROOT / f'second/{stem}_boxes.tsv')
    different = {r['box'] for r in rows(ROOT / f'second/{stem}_token_differences.tsv')}
    choices = json.loads(Path(choices_path).read_text())
    assert set(choices) == different, (set(choices), different)
    output = []
    for b in boxes:
        key = b['box']
        if key not in different:
            continue
        c = choices[key]
        assert c.get('personally_inspected') is True, key
        assert c['selection'] in ('first', 'second', 'custom'), key
        assert c['evidence'].strip(), key
        assert c['changed'] in ('yes', 'no'), key
        final = (first[key] if c['selection'] == 'first' else
                 second[key] if c['selection'] == 'second' else c['final'])
        crop = c.get('crop', f'crops/{stem}_second_{key}.png')
        assert (ROOT / crop).is_file(), crop
        output.append({
            'box': key, 'first_reading': first[key], 'second_reading': second[key],
            'final_reading': final, 'evidence': c['evidence'],
            'changed': c['changed'], 'crop': crop,
            'pixel_box': str(tuple(int(b[k]) for k in ('x0','y0','x1','y1'))),
        })
    dest = ROOT / f'second/{stem}_adjudications.tsv'
    assert not dest.exists(), 'Do not overwrite a recorded adjudication silently.'
    fields = ['box','first_reading','second_reading','final_reading','evidence',
              'changed','crop','pixel_box']
    with dest.open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(output)
    print(json.dumps({'scan': n, 'adjudications': len(output),
                      'changed': sum(r['changed'] == 'yes' for r in output)}))


if __name__ == '__main__':
    write(int(sys.argv[1]), sys.argv[2])
