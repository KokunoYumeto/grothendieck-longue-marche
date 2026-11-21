"""Record a completed visual adjudication; this script never chooses a reading."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def finish(n, reader):
    stem = f'149_scan{n:03d}'
    report_path = ROOT / f'reviews/{stem}.json'
    report = json.loads(report_path.read_text())
    assert report.get('root_approved'), 'First reading must have been finalized.'
    assert not report.get('audited'), 'Do not duplicate an audit completion.'
    assert reader != report['reader'], 'The independent reader must be different.'
    first = rows(ROOT / f'second/{stem}_first.tsv')
    second = rows(ROOT / f'second/{stem}_second.tsv')
    provenance = json.loads((ROOT / f'second/{stem}_comparison_provenance.json').read_text())
    for kind, expected in provenance['sha256'].items():
        actual = hashlib.sha256((ROOT / f'second/{stem}_{kind}.tsv').read_bytes()).hexdigest()
        assert actual == expected, 'A frozen independent-comparison input changed'
    assert [x['box'] for x in first] == [x['box'] for x in second]
    diffs = rows(ROOT / f'second/{stem}_token_differences.tsv')
    adj = rows(ROOT / f'second/{stem}_adjudications.tsv')
    different = {x['box'] for x in diffs}
    decided = {x['box'] for x in adj}
    assert different == decided, (different, decided)
    assert len(adj) == len(decided), 'One adjudication per differing box.'
    a = {x['box']: x['reading'] for x in first}
    b = {x['box']: x['reading'] for x in second}
    for item in adj:
        assert item['first_reading'] == a[item['box']]
        assert item['second_reading'] == b[item['box']]
        assert item['evidence'].strip() and item['final_reading'].strip()
        assert item['changed'] in ('yes', 'no')
        assert (ROOT / item['crop']).is_file()
    changed = sum(x['changed'] == 'yes' for x in adj)
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    report.update(audited=True, second_reader=reader,
                  audit_boxes_read=len(first), audit_differing_boxes=len(different),
                  audit_token_spans=len(diffs), audit_changed_boxes=changed,
                  audit_completed_utc=now)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    with (ROOT / 'progress.log').open('a') as stream:
        stream.write(f'scan {n:03d} audited {now}: {len(first)} boxes read, '
                     f'{len(different)} differences, {changed} changed\n')
        stream.write(f'scan {n:03d} audit accounting: differences counts boxes; '
                     f'{len(diffs)} token-difference spans were adjudicated within them.\n')
    print(json.dumps({'scan': n, 'boxes': len(first), 'different_boxes': len(different),
                      'token_spans': len(diffs), 'changed_boxes': changed}))


if __name__ == '__main__':
    finish(int(sys.argv[1]), sys.argv[2])
