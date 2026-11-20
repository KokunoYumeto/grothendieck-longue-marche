#!/usr/bin/env python3
"""Recreate single-page textual packets from the supplied unpacked witnesses.

No OCR. Source images are referenced in place, never converted to text.
Usage: prepare_packets.py SOURCE_DIRECTORY PACKET_DIRECTORY
"""
from pathlib import Path
import csv,json,re,shutil,sys
from PIL import Image
source=Path(sys.argv[1]).resolve();packets=Path(sys.argv[2]).resolve()
w=source/'SP45_CW_37_witnesses';packets.mkdir(parents=True,exist_ok=True)
for r in csv.DictReader((w/'page_map.tsv').open(),delimiter='\t'):
    n=int(r['our_scan']);p=packets/f'scan{n:03d}';p.mkdir(exist_ok=True)
    shutil.copyfile(w/r['codex_file'],p/'C.tex')
    hs=(w/r['hua_file']).read_text();matches=list(re.finditer(r'\\page\{(\d+)\}',hs))
    i=next(i for i,m in enumerate(matches) if int(m[1])==int(r['their_page']))
    end=matches[i+1].start() if i+1<len(matches) else hs.find(r'\end{document}',matches[i].end())
    if end<0:end=len(hs)
    ht=hs[matches[i].start():end]
    # These batches use section* for intervening unnumbered cover sheets.
    sec=ht.find(r'\section*')
    if sec>=0:ht=ht[:sec]
    (p/'H.tex').write_text(ht)
    ds=(w/f"codex/{r['folder']}/{r['folder']}_doubts.md").read_text()
    dl=[x for x in ds.splitlines() if re.match(r'^\|\s*'+str(n)+r'\s*\|',x)]
    ns=(w/f"codex/{r['folder']}/{r['folder']}_notes.md").read_text()
    nl=[];scan_table=False
    for x in ns.splitlines():
        if not x.startswith('|'):
            scan_table=False
            continue
        first=x.split('|')[1].strip()
        if first.lower().startswith('scan'):scan_table=True
        elif first=='SGA':scan_table=False
        if scan_table and re.match(r'^\|\s*'+str(n)+r'(?:\s|\||,|–|-)',x):nl.append(x)
    for x in ns.splitlines():
        m=re.match(r'- \*\*(\d+)(?:[–-](\d+))?:\*\*',x)
        if m and int(m[1])<=n<=int(m[2] or m[1]):nl.append(x)
    (p/'C_prior_questions.md').write_text('# Earlier C doubt rows for this scan\n\n'+'\n'.join(dl)+'\n\n# Earlier C note rows for this scan\n\n'+'\n'.join(nl)+'\n')
    inv=list(csv.DictReader((w/f"codex/{r['folder']}/{r['folder']}_inventory.csv").open()))
    (p/'C_inventory.json').write_text(json.dumps([x for x in inv if int(x['scan'])==n],ensure_ascii=False,indent=2))
    imgs={k:str(source/'SP45_CW_37_scans'/f"{r['folder']}_37_scan{n:03d}{k}.jpg") for k in ['','_a','_b']}
    (p/'metadata.json').write_text(json.dumps(dict(r,images=imgs,image_sizes={k:Image.open(v).size for k,v in imgs.items()}),ensure_ascii=False,indent=2))
print('Single-page packets prepared.')
