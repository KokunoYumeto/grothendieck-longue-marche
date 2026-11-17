"""Print line-numbered excerpts from supplied context, with preceding scan marker.

Usage: python3 context_excerpt.py context/file.tex 100:130 200:205
Reads text only.  The supplied context itself is not copied into the deliverable.
"""
from pathlib import Path
import re
import sys

p = Path(sys.argv[1])
lines = p.read_text().splitlines()
for spec in sys.argv[2:]:
    start, stop = map(int, spec.split(':'))
    scan = 'not supplied'
    for line in lines[:start-1]:
        match = re.search(r'\\scanpage\{([^}]+)\}', line)
        if match:
            scan = match.group(1)
    print(f'FILE {p}; LINES {start}–{stop}; preceding scan {scan}')
    for i in range(start-1, min(stop, len(lines))):
        print(f'{i+1}: {lines[i]}')
