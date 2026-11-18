from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
changes=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
    scan=int(p.stem[-3:]); s=p.read_text(); old=s
    for letter in ('C','P','E','A','G'):
        s=s.replace('\\mathbf '+letter,'\\mathbb '+letter)
    if scan in (108,112,113):
        s=s.replace(r'\unsure{\mathbb E^1_S|\mathbb A^1_S}',r'\mathbb E^1_S')
        s=s.replace(r'\unsure{\mathbb E^1|\mathbb A^1}',r'\mathbb E^1')
    if scan in (126,129,130,132):
        s=s.replace('E^1',r'\mathbb E^1')
    if scan==129:
        s=s.replace('P^1',r'\mathbb P^1')
    if scan==134:
        s=s.replace(r'\unsure{\mathcal H|\mathfrak g}',r'\unsure{\mathcal H}')
    if scan in (114,115):
        s=s.replace(r'\unsure{\ldots}',r'\ldots')
    if s!=old:
        p.write_text(s); changes.append(scan)
with (ROOT/'documentation/doubts_rows.tsv').open('a') as f:
    for scan,reading,alt,conf in [
        (108,r'\mathbb E^1','A alternative resolved by visible E strokes in the inserted morphism','high'),
        (112,r'\mathbb E^1','A alternative resolved by the doubled E and three bars','high'),
        (113,r'\mathbb E^1','A alternative resolved by comparison of both E forms on this page and scan 108','high'),
        (134,r'\mathcal H','matches the recurring cursive H on scan 092; exact script font remains uncertain','medium')]:
        f.write('\t'.join(['93',str(scan),'recurring notation, final comparison',reading,alt,conf])+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write('notation reconciled '+stamp+'; root visual comparison; affected scans '+','.join(map(str,changes))+'; details documentation/notation_reconciliation.md\n')
print('Notation reconciliation written for scans:', changes)
