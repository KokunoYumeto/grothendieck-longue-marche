"""Close a visually reconciled blind reading; this script does not read the ink."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, sys
from manage import assemble

W = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
base = W / 'second' / f'147_scan{n:03d}'
def rows(suffix):
    with Path(str(base) + suffix).open() as f:
        return list(csv.DictReader(f, delimiter='\t'))
comparison = rows('_comparison.tsv')
reconciliation = rows('_reconciliation.tsv')
comparison_meta = json.loads(Path(str(base) + '_comparison_metadata.json').read_text())
verified_hashes = {}
for suffix, key in [('_first.tsv', 'first_sha256'), ('_second.tsv', 'second_sha256')]:
    current_hash = hashlib.sha256(Path(str(base) + suffix).read_bytes()).hexdigest()
    if comparison_meta.get(key) != current_hash:
        raise ValueError(f'{suffix} changed after comparison, or comparison metadata hash is missing')
    verified_hashes[key] = current_hash
differences = [x for x in comparison if x['equal_tokens'] == 'no']
if [x['box'] for x in reconciliation] != [x['box'] for x in differences]:
    raise ValueError('Every token-different box needs an ordered visual decision')
for r, expected in zip(reconciliation, differences):
    if r['first'] != expected['first'] or r['second'] != expected['second']:
        raise ValueError(f"{r['box']}: reconciliation first/second do not exactly match comparison")
    assert r['decision'] and r['evidence'] and r['final_reading']
    assert r['changed'] in ('yes', 'no')
    assert r['viewed_by'] == 'root'
    assert (W / r['crop']).is_file()
record_path = W / 'records' / f'147_scan{n:03d}.json'
record = json.loads(record_path.read_text())
reader_meta = json.loads(Path(str(base) + '_second_reader.json').read_text())
reader = reader_meta['reader'].split('/')[-1]
assert reader != record['reader'].split('/')[-1], 'Blind reader must differ'
assert reader_meta['no_previous_reading'] is True
changed = sum(x['changed'] == 'yes' for x in reconciliation)
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
record['audit'] = {
    'reader': reader, 'main_reader': 'root', 'completed': stamp,
    'boxes': len(comparison), 'differences': len(differences),
    'changed': changed, 'count_unit': 'boxes whose consolidated reading changed, including explicit uncertainty changes',
    'second_sha256': verified_hashes['second_sha256'],
    'reconciliation': str(Path(str(base) + '_reconciliation.tsv').relative_to(W))
}
record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
assemble()
with (W / 'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {stamp}: {len(comparison)} boxes read, {len(differences)} differences, {changed} changed\n')
print(json.dumps(record['audit']))
