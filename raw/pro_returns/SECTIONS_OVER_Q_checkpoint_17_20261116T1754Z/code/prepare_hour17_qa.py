#!/usr/bin/env python3
"""Prepare the seventeenth-hour renderer, retaining all historical repair anchors."""
from pathlib import Path
import re

w = Path(__file__).resolve().parents[1]
source = (w / 'code/render_hour16_qa.py').read_text()
source = source.replace('CP16', 'CP17').replace('hour16', 'hour17')
source = source.replace('range(8, 17)', 'range(8, 18)')
source = source.replace('range(193, 205)', 'range(205, 211)')
source = source.replace('range(193,205)', 'range(205,211)')
source = source.replace('start = starts[193]', 'start = starts[205]')
source = source.replace('i+1 >= starts[204]', 'i+1 >= starts[210]')
source = source.replace("saved = W/'qa/visual_review_hour15.json'", "saved = W/'qa/visual_review_hour16.json'")
source = source.replace('263,283,299,305,317,325,347,351,365,377,395,410,422,',
                        '263,283,299,305,317,325,347,351,365,377,395,410,422,')
source = source.replace('437,447,465,470,488,504,525,540,555]',
                        '437,447,465,470,488,504,525,540,555,579,586,600,609,614]')
source, n = re.subn(r"    new_full_tags = \[.*?\]\n    # Optional", "    new_full_tags = ['A.205.2','A.205.4','A.205.7','A.205.13',\n                     'A.206.14','A.206.16','A.206.22','A.207.4',\n                     'A.207.10','A.207.15','A.208.1','A.208.13',\n                     'A.208.18','A.208.22','A.209.2','A.209.9',\n                     'A.209.14','A.210.1']\n    # Optional", source, flags=re.S)
assert n == 1
source, n = re.subn(r"    required_full = sorted\(set\(toc \+ historical \+ \[starts\[n\] for n in range\(205,211\)\]\n\s*\+ \[p for ps in equation_locations.values\(\) for p in ps\]\)\)",
                     '    required_full = sorted(set(toc + historical + new_pages))', source)
assert n == 1
(w / 'code/render_hour17_qa.py').write_text(source)
corrections = w / 'notes/hour17_typesetting_corrections.json'
if not corrections.exists():
    corrections.write_text('[]\n')
out = 'Prepared CP17 renderer: activeA205–A210; every new proof page and every historical repaired page is a full-resolution target.\n'
(w / 'code/prepare_hour17_qa_output.txt').write_text(out)
print(out, end='')
