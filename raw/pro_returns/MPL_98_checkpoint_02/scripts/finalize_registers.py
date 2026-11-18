"""Synchronize final pre-freeze registers; never infer or edit manuscript readings."""
from pathlib import Path
import csv
import json

BASE = Path(__file__).resolve().parents[1]
if (BASE / 'research/frozen_sha256.json').exists():
    raise SystemExit('Transcription is frozen: register finalizer must not rewrite the combined fragment.')
rp = BASE / 'research/page_records.jsonl'
records = [json.loads(x) for x in rp.read_text().splitlines() if x.strip()]

drop = {
    4: {'running family index throughout typescript'},
    7: {'recurring norm label', 'recurring norm labels'},
    14: {'middle noun'},
    19: {'series word'},
    38: {'insertion above commençant'},
    42: {'left lower formula'},
}
for r in records:
    r['tex'] = (BASE / 'pages' / f"MPL_98_98_scan{r['scan']:03d}.tex").read_text()
    if r['scan'] in drop:
        r['doubts'] = [d for d in r['doubts'] if d[0] not in drop[r['scan']]]
    for d in r['doubts']:
        if r['scan'] == 3 and d[0] == 'arrow before T_A^n':
            d[1:4] = ['thick single left arrow', 'weight of retraced stroke', 'medium']
        if r['scan'] == 22 and d[0] == 'first object of large sequence':
            d[1:4] = ['bullet', '0', 'medium']
        if r['scan'] == 30 and d[0] == 'class-set notation':
            d[1:4] = ['Phi(X/k)', 'Cl(X/k)', 'low']
        if r['scan'] == 31 and d[0] == 'class notation':
            d[1:4] = ['Phi', 'Cl; comparison with scans030–033 does not settle the glyph', 'low']
        if r['scan'] == 43 and d[0] == 'cancelled bracket':
            d[1] = 'il suffit [en fait?] que N soit; 7 words unreadable'
    if r['scan'] == 7:
        r['doubts'].append(['recurring norm labels', 'Cor', 'Cn', 'low'])
    if r['scan'] == 38:
        r['doubts'].append(['insertion above commençant', 'ab. = le dernier,', 'ab. le dernier,', 'low'])
rp.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records))

# Added grouping marks belong beside the relevant text, not at the end of a sheet.
reposition = {14: [(15, 12)], 16: [(15, 4)], 20: [(20, 7)],
              35: [(21, 2)], 37: [(18, 15)], 39: [(17, 1), (18, 11)],
              40: [(20, 19)], 41: [(15, 9)], 42: [(30, 3)]}
marker = BASE / 'research/registers_reconciled.json'
if marker.exists():
    reposition = {}
ip = BASE / 'MPL_98_inventory.csv'
with ip.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
ordered = []
for scan in range(2, 45):
    group = sorted([r for r in rows if int(r['scan']) == scan], key=lambda r: int(r['element']))
    moved = {src for src, _ in reposition.get(scan, [])}
    by_id = {int(r['element']): r for r in group}
    seq = []
    for row in group:
        n = int(row['element'])
        for src, dest in reposition.get(scan, []):
            if n == dest:
                seq.append(by_id[src])
        if n not in moved:
            seq.append(row)
    for i, row in enumerate(seq, 1):
        row['element'] = str(i)
        if scan == 14 and row['first_words_or_objects'].startswith('le couple'):
            row['first_words_or_objects'] = "l'objet [or le couple] X/H′ avec groupe à opérateurs fini"
        if scan == 37 and row['kind'] == 'diagram':
            row['first_words_or_objects'] = 'K_i d_i K_i+1 d_i+1 K_i+2; H_i+1 [or B_i+1]'
        if scan == 42 and row['kind'] == 'display' and row['position'] == 'left lower':
            row['first_words_or_objects'] = 'Coker Hom(underlined L_N,G) dash Hom(underlined L_N+1,G)'
    ordered.extend(seq)
with ip.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(ordered)

combined = '\n'.join((BASE / 'pages' / f'MPL_98_98_scan{s:03d}.tex').read_text().rstrip() for s in range(2, 45)) + '\n'
assert combined.startswith('\\cotefile{98}\n\\scanpage{2}')
(BASE / 'MPL_98_transcription.tex').write_text(combined)
marker.write_text(json.dumps({'pages': len(records), 'inventory_elements': len(ordered),
                              'phase': 'pre-freeze register reconciliation'}, indent=2) + '\n')
print(f'Synchronized {len(records)} page records; ordered {len(ordered)} inventory elements; combined fragment written.')
