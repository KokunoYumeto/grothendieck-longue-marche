#!/usr/bin/env python3
"""Rebuild disposable page-specific input bundles from the supplied input archive."""
from pathlib import Path
import csv,json,re,shutil
b=Path(__file__).resolve().parent.parent.parent;w=b/'source/SP54_CW_57+63_witnesses';work=b/'work';work.mkdir(exist_ok=True)
rows=list(csv.DictReader((w/'page_map.tsv').open(),delimiter='\t'))
(work/'page_map.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
for row in rows:
    name=Path(row['codex_file']).stem;dest=work/'inputs'/name;dest.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(w/row['codex_file'],dest/'C.tex')
    text=(w/row['hua_file']).read_text();matches=list(re.finditer(r'\\page\{(\d+)\}',text))
    selected=next(m for m in matches if m.group(1)==row['their_page'])
    end=next((m.start() for m in matches if m.start()>selected.start()),len(text));h=text[selected.start():end]
    if row['our_scan']=='23':h=h[:h.index('\\section{Rigidité}')]
    (dest/'H.tex').write_text(h)
    prior=[];scan=int(row['our_scan'])
    for suffix in ['doubts.md','notes.md','inventory.csv','audit.md']:
        p=w/'codex'/row['folder']/(row['folder']+'_'+suffix);t=p.read_text()
        if suffix=='inventory.csv':
            rr=list(csv.DictReader(t.splitlines()));prior.append('## Prior inventory\n'+json.dumps([r for r in rr if str(r.get('scan'))==str(scan)],ensure_ascii=False,indent=2))
        elif suffix=='audit.md':
            headings=list(re.finditer(r'(?m)^#{1,4} .*$',t));found=[]
            for k,m in enumerate(headings):
                if re.search(r'(?:scan\s*0*|Scan\s*0*)'+str(scan)+r'\b',m.group()):found.append(t[m.start():headings[k+1].start() if k+1<len(headings) else len(t)])
            if found:prior.append('## Prior audit for this scan\n'+'\n'.join(found))
        else:
            found=[]
            for line in t.splitlines():
                if line.startswith('|'):
                    cells=line.split('|')
                    if len(cells)>2 and re.search(r'(?<!\d)'+str(scan)+r'(?!\d)',cells[1]):found.append(line)
            prior.append('## Prior '+suffix+' (scan-specific and cross-page notation rows)\n'+'\n'.join(found))
    (dest/'prior.md').write_text('\n\n'.join(prior))
    metadata=dict(row,page=name,whole=str(b/'source/SP54_CW_57+63_scans'/f'{name}.jpg'),half_a=str(b/'source/SP54_CW_57+63_scans'/f'{name}_a.jpg'),half_b=str(b/'source/SP54_CW_57+63_scans'/f'{name}_b.jpg'))
    (dest/'page.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2))
print('Rebuilt '+str(len(rows))+' disposable page-specific input directories; no deliverable was reset.')
