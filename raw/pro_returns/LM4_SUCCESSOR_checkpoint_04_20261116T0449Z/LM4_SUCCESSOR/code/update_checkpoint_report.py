"""Refresh the outcome table from task_coverage.csv; preserve report prose."""
import csv
from pathlib import Path
P=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((P/'task_coverage.csv').open()))
p=P/'LM4_SUCCESSOR_report.md';s=p.read_text()
body=s[s.index('## Scope and principal decisions'):]
table='INCOMPLETE\n\n| Task or lead | Statements | Outcome and exact state |\n|---|---|---|\n'
for r in rows:
 table+=f"| {r['task']} | {r['statement_ids']} | **{r['outcome']}** — {r['state']} |\n"
p.write_text(table+'\n'+body)
print('Refreshed',len(rows),'rows; historical report text preserved')
