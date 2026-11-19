#!/usr/bin/env python3
"""Rebuild page-only witness excerpts from the supplied unpacked source package."""
from pathlib import Path
import csv,re,json,shutil,argparse
p=argparse.ArgumentParser();p.add_argument('workspace');a=p.parse_args()
root=Path(a.workspace).resolve();src=root/'source/SP37_CW_71_witnesses'
for row in csv.DictReader((src/'page_map.tsv').open(),delimiter='\t'):
    n=int(row['our_scan']);d=root/f'inputs/scan{n:03d}';d.mkdir(parents=True,exist_ok=True)
    shutil.copy(src/row['codex_file'],d/'C.tex')
    h=(src/row['hua_file']).read_text();m=re.search(r'\\page\{'+row['their_page']+r'\}',h)
    if m:
        h=h[m.start():];ends=[x for x in [h.find('\\page{',6),h.find('\\end{document}')] if x>=0];h=h[:min(ends)] if ends else h
    else:h='% Witness H has no page text.\n'
    (d/'H.tex').write_text(h)
    folder=src/'codex'/row['folder']
    ds=(folder/(row['folder']+'_doubts.md')).read_text().splitlines()
    ns=(folder/(row['folder']+'_notes.md')).read_text().splitlines()
    selected=[l for l in ds if re.match(r'\|\s*'+str(n)+r'\s*\|',l)]
    selected += [l for l in ns if l.startswith('- Scan '+str(n)+'.')]
    (d/'C_doubts_notes.md').write_text('\n'.join(selected)+'\n')
    s=(root/'source/SP37_CW_71_sweep3/readings/cotes71_75_CORRECTIONS.tsv').read_text().splitlines()
    (d/'S.tsv').write_text(s[0]+'\n'+'\n'.join(l for l in s[1:] if f'71/{n},' in l)+'\n')
    (d/'meta.json').write_text(json.dumps(row,indent=2)+'\n')
print('Prepared page-specific excerpts for scans 036–048')
