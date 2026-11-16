"""Inventory every retained Python program and its available actual output."""
import ast
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
rows = []
for path in sorted(root.rglob('*.py')):
    if '__pycache__' in path.parts:
        continue
    rel = str(path.relative_to(root))
    outputs = [p for p in (path.with_suffix('.out'), path.with_suffix('.stdout'), path.with_name(path.name+'.out')) if p.exists()]
    try:
        purpose = ' '.join((ast.get_docstring(ast.parse(path.read_text())) or '').split())
    except (SyntaxError, UnicodeDecodeError):
        purpose = 'See the program and its associated component records.'
    rows.append(dict(program=rel,
                     output='; '.join(str(p.relative_to(root)) for p in outputs) or 'See named research/build records or generated data; helper if no standalone output',
                     command='python3 '+rel,
                     purpose=purpose))
target = root/'records/computation_inventory.csv'
with target.open('w') as f:
    writer = csv.DictWriter(f, fieldnames=['program','output','command','purpose'])
    writer.writeheader()
    writer.writerows(rows)
print('Inventoried',len(rows),'programs')
