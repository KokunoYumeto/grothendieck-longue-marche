#!/usr/bin/env python3
"""Repair extra columns introduced by older outcome-table append operations."""
from pathlib import Path

w=Path(__file__).resolve().parents[1]
p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
inside=False
fixed=[]
for index,line in enumerate(lines):
    if line.startswith('### State and attempts for every undecided outcome row'):
        inside=True
        continue
    if inside and line.startswith('## '):
        inside=False
    if not inside or not line.startswith('| '):
        continue
    cells=[cell.strip() for cell in line.strip().strip('|').split('|')]
    if len(cells)>2 or not line.rstrip().endswith('|'):
        key=cells[0]
        body=' '.join(cells[1:]).replace(', A.116 A.116', ' A.116')
        body=body.replace(', A. A.87', ' A.87')
        lines[index]='| '+key+' | '+body+' |'
        fixed.append(key)
    assert len(lines[index].split('|'))==4, (index+1,lines[index])
p.write_text('\n'.join(lines)+'\n')
output='Repaired two-column state-table rows: '+', '.join(fixed)+'. All state-table rows now have exactly two cells.\n'
Path(__file__).with_name('repair_report_state_table_hour8_output.txt').write_text(output)
with(w/'notes/hour8_root_audits.md').open('a')as f:
    f.write('\nReport formatting audit: '+output)
print(output,end='')
