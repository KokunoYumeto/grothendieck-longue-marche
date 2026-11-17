"""Finite column diagnostic; no assertion about the full old-base orbit."""
from pathlib import Path
from collections import Counter
import hashlib
import json

root = Path(__file__).resolve().parents[1]
directory = root / 'work_CE/next_symmetric_nodes'
records = []
for name, status in (
    ('symmetric_node_words_fox_columns.json', 'superseded transport convention'),
    ('symmetric_node_words_pullback_corrected_fox_columns.json', 'corrected geometric pullback'),
):
    path = directory / name
    raw = path.read_bytes()
    data = json.loads(raw)
    counts = Counter(tuple(row['component_basis_pair']) for row in data['node_columns'])
    row = dict(input=name, status=status, sha256=hashlib.sha256(raw).hexdigest(),
               columns=len(data['node_columns']), distinct_pairs=len(counts),
               multiplicity_counts=dict(Counter(counts.values())),
               repeated_pairs=[dict(pair=pair, count=n) for pair, n in counts.items() if n>1])
    records.append(row)
    print(status + ':', row['columns'], 'columns;', row['distinct_pairs'],
          'distinct augmented pairs;', row['multiplicity_counts'])
print('Scope: only the64 initial columns; all old-base/deck translates and their dependencies remain separate.')
(root / 'records/symmetric_incidence_pairs17.json').write_text(json.dumps(records, indent=2)+'\n')
