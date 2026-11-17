"""Retain the final fourth-hour A.44/B.59 refinements in the task table."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "task_coverage.csv"
with path.open() as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['task'] in {'A.3', 'A.4', 'A.7', 'A.8'}:
        if 'A.44' not in row['statement_ids']:
            row['statement_ids'] += ';A.44'
        row['state'] += ' The canonical substitution generates every finite dihedral reflection quotient and is an automorphism on every relative pro-p quotient over the common parity character; third-cusp preservation is not inferred there.'
    if row['task'] in {'B.4', 'B.4.c', 'B.4.h'}:
        if 'B.59' not in row['statement_ids']:
            row['statement_ids'] += ';B.59'
        row['state'] += ' In the ambient class-two quotient, K is confined to one explicit primitive central line. Removing that line gives a quotient with commutator rank164 and proves every finite refinement factoring through it.'
        row['obstruction'] = 'One central class-two direction and arbitrary further nonabelian finite levels remain uncontrolled; no nonzero quotient vector is lifted to an actual element of K.'
with path.open('w') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print('Added A44 and B59 to the49-row coverage table; main decisions remain Open')
