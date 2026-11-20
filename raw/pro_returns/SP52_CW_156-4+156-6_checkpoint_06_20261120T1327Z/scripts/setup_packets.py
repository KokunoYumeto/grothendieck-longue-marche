from pathlib import Path
import csv,re,shutil,json,sys

BASE=Path(__file__).resolve().parents[2]
SRC=BASE/'source/SP52_CW_156-4+156-6_witnesses'
OUT=BASE/'SP52_work'
PACKETS=BASE/'page_packets'
PACKETS.mkdir(exist_ok=True)
rows=list(csv.DictReader((SRC/'page_map.tsv').open(),delimiter='\t'))
for row in rows:
    key=f"{row['cote']}_{int(row['our_scan']):03d}"
    if len(sys.argv)>1 and key!=sys.argv[1]:continue
    p=PACKETS/key;p.mkdir(exist_ok=True)
    shutil.copy(SRC/row['codex_file'],p/'C.tex')
    h=(SRC/row['hua_file']).read_text()
    m=re.search(r'\\page\{'+row['their_page']+r'\}',h)
    tail=h[m.end():]
    stop=re.search(r'\\page\{|\\end\{document\}',tail)
    (p/'H.tex').write_text(h[m.start():m.end()]+(tail[:stop.start()] if stop else tail))
    cd=SRC/'codex'/row['folder']
    d=(cd/(row['folder']+'_doubts.md')).read_text()
    n=int(row['our_scan'])
    dl=[]
    for line in d.splitlines():
        # A comparison to this scan inside another scan's row is not this page's context.
        if re.match(r'\|\s*0?'+str(n)+r'\s*[|,]',line) or (not line.lstrip().startswith('|') and re.search(r'\bScan\s+0?'+str(n)+r'\b',line,re.I)): dl.append(line)
    notes=(cd/(row['folder']+'_notes.md')).read_text()
    nl=[s for s in notes.splitlines() if re.search(r'\bScan\s+0?'+str(n)+r'\b',s,re.I)]
    audit=(cd/(row['folder']+'_audit.md')).read_text()
    a=re.search(r'^## Scan\s+0?'+str(n)+r'\b',audit,re.M)
    at=''
    if a:
        # A batch's final page may be followed by a cross-page audit section.
        # Isolated readers receive only the requested page's audit.
        t=audit[a.start():];e=re.search(r'^##\s+',t[3:],re.M)
        at=t[:e.start()+3] if e else t
    (p/'C_context.md').write_text('# C doubts for this page\n\n'+'\n'.join(dl)+'\n\n# C notes\n\n'+'\n'.join(nl)+'\n\n# C prior audit (draft evidence only)\n\n'+at)
    shutil.copy(cd/'PREAMBLE.tex',p/'PREAMBLE.tex')
    prompt=(cd/'PROMPT.md').read_text()
    rules=prompt[prompt.index('## Absolute rules'):prompt.index('## The attached draft')]
    (p/'CONVENTIONS.md').write_text(rules+'\n\nH macro meanings: \\uncertain{...} marks doubt, not manuscript underlining; \\struck{...} is deletion; \\add{...} insertion; \\ill{} unread; \\note{...} editorial; \\marginal{...} margin. H \\emph often represents manuscript underlining. Differences only of equivalent macros do not count.\n')
    image_stem=f"{row['folder']}_{row['cote']}_scan{n:03d}"
    metadata=dict(row,key=key,images=[str(BASE/'source/SP52_CW_156-4+156-6_scans'/(image_stem+s+'.jpg')) for s in ['','_a','_b']])
    (p/'metadata.json').write_text(json.dumps(metadata,indent=2))
shutil.copy(SRC/'codex/J156-4-08/PREAMBLE.tex',OUT/'PREAMBLE.tex')
(OUT/'page_order.json').write_text(json.dumps(rows,indent=2))
print(f'Prepared isolated page packet {sys.argv[1]}.' if len(sys.argv)>1 else f'Prepared {len(rows)} isolated page packets.')
