#!/usr/bin/env python3
"""Historical A.116 report-edit script executed at 08:11 UTC.

Retained verbatim for the audit trail; DO NOT rerun.
This first version matched later two-column state rows as well as the
early outcome table. Parent repaired those table rows afterward.
Future table edits must be confined to the parsed outcome-table section.
The manuscript input and JSON metadata were added by the accompanying
apply_patch call recorded in A116_integration_output.txt.
"""
from pathlib import Path
p=Path('work/SECTIONS_OVER_Q_report.md')
s=p.read_text()
lines=s.splitlines()
for j,line in enumerate(lines):
    if any(line.startswith('| '+item+' |') for item in ['A9','A12','A15','L14','L20']):
        parts=line.split('|')
        if 'A.116' not in parts[2]:
            parts[2]=parts[2].rstrip()+', A.116 '
            parts[3]=parts[3].rstrip()+' A.116 proves zero evaluation at every place for the explicit order-four negative-fourth-power triple character on the harmonic eighth-power cover. Its full common-character group remains under investigation. '
            lines[j]='|'.join(parts)
lines += ['', '08:11 UTC: A.116 extends the harmonic calculation to the order-four character chi16+chi_r when the three boundary radicands have product −r^4. The product of the three eighth roots gives the literal finite etale map to Z^8+r^4; the character field is contained in every factor by an explicit root-stabilizer equation. The proof gives zero cyclic-algebra evaluation at every place, using actual norm identities, exact coordinate changes and old-point exchange, complete odd-prime reduction cases, the dyadic depth argument and real positivity. Root and Legendre independently audited the proof. The retained finite certificates and searches supplement those maps. The additional common characters for general octic fibres remain unclassified here; no full exponent-eight initialization or completed lift is inferred.', '']
p.write_text('\n'.join(lines))

