#!/usr/bin/env python3
"""One-time root visual correction from the reflected scan143 print crop."""
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
p = root / 'pages/MPL_154_127-176_154_scan143.tex'
s = p.read_text()
zero = [
    '           00000000', '         0000000000',
    '       00      0000', '      00     00 00',
    '     00    00  00', '    00   00   00',
    '   00  00    00', '  00 00     00',
    ' 0000      00', '000       00',
    '0000000000', '00000000',
]
rows = []
for shape in zero:
    canvas = [' '] * 70
    for offset in (0,14,28,42):
        for j,ch in enumerate(shape):
            if ch != ' ': canvas[offset+j] = ch
    rows.append(''.join(canvas).rstrip())
rows += ['',
 ' CCCCCCCCCC   RRRRRRRRRRR    AAAAAAAAAA   YY        YY   2222222222',
 'CCCCCCCCCCCC  RRRRRRRRRRRR  AAAAAAAAAAAA  YY        YY  222222222222',
 'CC        CC  RR        RR  AA        AA   YY      YY  22        22',
 'CC            RR        RR  AA        AA    YY    YY            22',
 'CC            RR        RR  AA        AA     YY  YY             22',
 'CC            RRRRRRRRRRRR  AAAAAAAAAAAA      YYYY              22',
 'CC            RRRRRRRRRRR   AAAAAAAAAAAA       YY             22',
 'CC            RR    RR      AA        AA       YY           22',
 'CC            RR     RR     AA        AA       YY         22',
 'CC        CC  RR      RR    AA        AA       YY       22',
 'CCCCCCCCCCCC  RR       RR   AA        AA       YY      222222222222',
 ' CCCCCCCCCC   RR        RR  AA        AA       YY      222222222222',
]
start=s.index('\\begin{tabular}{l}')+len('\\begin{tabular}{l}')
end=s.index('\\end{tabular}',start)
s=s[:start]+'\n'+'\n'.join('\\texttt{'+r.replace(' ',r'\ ')+'}\\\\' for r in rows)+'\n'+s[end:]
p.write_text(s)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'records/visual_audit.md').open('a') as f:
    f.write('\n## Additional pre-freeze comparison: 141 and 143 — '+now+'\n\n'
            'Root again viewed the upright faint-print crop of 141: existing tentative fragments remain plausible but low confidence; no change. Root again viewed the reflected full print crop of 143 and corrected the positions of the eighth–tenth numeric-banner rows, restored the two right-hand CC groups in CRAY2 rows 3 and 10, and corrected the visible R row lengths. The entire faint/overdrawn banner remains under a local uncertainty marker. No context used.\n')
with (root/'progress.log').open('a') as f:
    f.write('additional pre-freeze visual recheck scans 141 and 143 '+now+'\n')
print('scan143 banner corrected from own reflected crop')
