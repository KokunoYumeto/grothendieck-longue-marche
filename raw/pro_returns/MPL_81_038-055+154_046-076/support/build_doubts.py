#!/usr/bin/env python3
"""Assemble root-reviewed doubts without reading or changing manuscript sources."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_81_038-055+154_046-076'
DATA = ROOT / 'support/validation/uncertainties_for_doubts.json'

# Root's qualitative judgments after direct scan reading and review of every
# extracted occurrence. These are editorial inputs, not inferred by this script.
LOW = {
46:[1,2,3,4,5,9,10,13,14,16,21,22,24,29,30,31,32,35,38,39,40,41,46,47,48,49,50,51,52,53,54,55],
47:[1,6,7,8,9,11,12,13,14,15,17,18,20,22,25,26,27,29],
48:[1,2,6,10,13,14,16,17,23,26,27,28],
49:[1,2,3,4,5,8,9,13,15,16],
50:[5,8,9,10,12,13,14,15,16,17,18,20,22],
51:[1,5,6,8,10,11,12,13,14],
52:[4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,23,24,26,27,28,31,32],
53:[1],
54:[1,2,5,6,8,12,13,14,15,16,17,19,20,21],
55:[1,2,4,5,7,9,10],
56:[1,2,3,7,8,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],
57:list(range(1,14)),
58:[1,2,4,5,7,8,10,12,13,14,15],
59:[1,2,4,5,6,7,8,9,11,12,13],
60:[2,3,5,7,8,9,10,11,12,14,15,16,17,18,19,20,21],
61:[3,4,5,6,7,8,9,10,11,12,13,14,15],
62:[1,2,3],
63:[1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,21],
64:[1,3,4,6,7],
65:[3,6,8,9,10,11,12,13,14,16],
66:[2,5,7,9,10,11,13,14],
67:[1,2,3,5],
68:list(range(1,15)),
69:[1,3,4,5,6,7,8,9,10,11],
70:[1,2,3,4,5,6,7,8,9,11],
71:list(range(1,7)),
72:[1,2,3,4,5,10,11,12,13,14,15,16,17],
73:[1,2],
74:[2,4,5,6,7,8,9],
75:[1,3,5,6,7,8,10,13,14],
76:[1,2,3,4,7,8,9,10,11,12,13,14],
}

def cell(value):
    return str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n',' ')

def code(value):
    return '<code>' + cell(value) + '</code>' if value else '—'

def main():
    data = json.loads(DATA.read_text())
    assert not data['errors']
    rows = data['occurrences']
    counts = Counter()
    out = [(ROOT/'support/doubts_frontmatter.md').read_text()]
    out.append(f"The final literal register contains **{len(rows)} doubt occurrences**. Every occurrence is retained separately; no repeated uncertainty has been deduplicated.\n\n")
    previous = None
    for o in rows:
        n = o['scan']
        if n != previous:
            out.append(f"### Cote 154, scan {n:03d}\n\n")
            out.append('| ID | File | Cote | Scan | Approximate manuscript position / source line | Reading | Alternatives | Confidence |\n|---|---|---:|---:|---|---|---|---|\n')
            previous=n
        conf = 'low' if o['page_ordinal'] in LOW.get(n,[]) else 'medium'
        counts[conf]+=1
        pos=(o.get('element') or {}).get('position','unassigned position')
        ident=f"154-{n:03d}-U{o['page_ordinal']:02d}"
        out.append('| '+ ' | '.join([
            ident,code(o['source_file']),'154',str(n),
            cell(pos)+f"; TeX line {o['source_line']}, column {o['source_column']}",
            code(o['reading']),'<br>'.join(code(a) for a in o['alternatives']) or '—',conf])+' |\n')
        o['doubt_id']=ident;o['confidence']=conf
        if o is rows[-1] or rows[rows.index(o)+1]['scan'] != n:
            out.append('\n')
    out.append((ROOT/'support/doubts_afterword.md').read_text())
    target=ROOT/'deliver'/f'{PREFIX}_doubts.md'
    target.write_text(''.join(out))
    (ROOT/'deliver/records/doubt_occurrences.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'doubt_count':len(rows),'confidence_counts':counts,'output':str(target)},ensure_ascii=False))

if __name__=='__main__': main()
