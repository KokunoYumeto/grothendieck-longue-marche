#!/usr/bin/env python3
"""Record main-reader cross-locations established by direct page/crop inspection.
This script records editorial conclusions; it does not read handwriting.
No transcription bytes are changed.
"""
from pathlib import Path
import json
from review import D, now, rebuild

ADDITIONS = [
    ('6_scan033', 'L709', 'Main-reader cross-location check: the supplied elliptic-curve material is visible on other reviewed leaves. Scan 035 contains the semisimplicity/open-image discussion; scan 037 contains the multiplicative-group and Tate-module factors discussed by L703 and L704. These are verified subject locations, not a proof of the supplied refinements or a reconstruction of the full leaf order.'),
    ('6_scan038', 'L718', 'Main-reader cross-location check: the relevant mathematical questions and conjectures occur on the reviewed cote 6 scans 041, 043 and 045; their evidence crops and separate L718 placements identify those actual loci. Scan 038 remains a title sheet.'),
    ('6_scan038', 'L719', 'Main-reader cross-location check: the reviewed cote 6 scan 042 visibly carries the printed page number 15 and draft number 357, as documented in its header crop and L1319 placement. That is the verified local typescript locus among the supplied pages; the title sheet at scan 038 does not carry those labels.'),
    ('7_scan006', 'L739', 'Main-reader cross-location check: the closing Remarque was directly inspected on cote 7 scan 016; scans 017–019 contain the reviewed p-adic-cohomology commentary and Tests décisifs, and scan 021 begins the reviewed de Rham discussion. This identifies those supplied leaves without claiming to have checked every scan in the proposed editorial range.'),
    ('7_scan016', 'L1320', 'Main-reader cross-location check: the wording « C’est faux malheureusement » occurs on the directly inspected cote 7 scan 017 in the p-adic-cohomology discussion, before the ordinary abelian example. The margin on scan 016 instead says « C’est en effet faux ! ». The quotations are not interchangeable, and neither introduces a catalogue label into the TeX.'),
]

for page, statement, addition in ADDITIONS:
    path = D / 'reviews' / (page + '.json')
    report = json.loads(path.read_text())
    row = next(r for r in report['rows'] if r['id'] == statement)
    if addition in row['note']:
        continue
    row['note'] += ' ' + addition
    row.setdefault('events', []).append({
        'date': now(),
        'who': 'GPT-6 Astra Pro; effort not exposed; main reader; run IM02_6-9_20261120',
        'type': 'used and rechecked in this run',
        'outcome': f'Cote {row["cote"]}, scan {int(row["scan"]):03d}: ' + addition,
    })
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(rebuild())
