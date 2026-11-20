from pathlib import Path
import csv,json,re,shutil

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'source/SP53_CW_156-6_witnesses'
OUT=ROOT/'out'
rows=list(csv.DictReader((SRC/'page_map.tsv').open(),delimiter='\t'))
srows=list(csv.DictReader((ROOT/'source/SP53_CW_156-6_sweep3/readings/156-6_CORRECTIONS.tsv').open(),delimiter='\t'))
for row in rows:
    n=int(row['our_scan']); folder=row['folder']; p=ROOT/'packets'/f'scan{n:03}'
    p.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(SRC/row['codex_file'],p/'C.tex')
    h=(SRC/row['hua_file']).read_text()
    m=re.search(r'\\page\{'+row['their_page']+r'\}',h)
    tail=h[m.end():]; nxt=re.search(r'\\page\{\d+\}|\\end\{document\}',tail)
    (p/'H.tex').write_text(h[m.start():m.end()]+tail[:nxt.start() if nxt else len(tail)])
    context=[]
    for typ in ['doubts','notes']:
        txt=(SRC/f'codex/{folder}/{folder}_{typ}.md').read_text()
        # Page sections where the file has those, plus matching table entries.
        matches=list(re.finditer(r'(?im)^#{2,4}\s+.*?(?:scan\s*0*'+str(n)+r'\b).*$',txt))
        if matches:
            for mt in matches:
                rest=txt[mt.end():]; nx=re.search(r'(?m)^#{1,4}\s',rest)
                context.append(txt[mt.start():mt.end()]+rest[:nx.start() if nx else len(rest)])
        lines=[l for l in txt.splitlines() if re.match(r'^\|\s*0*'+str(n)+r'\s*\|',l)]
        context.extend(l for l in lines if not any(l in section for section in context))
    (p/'C_context.md').write_text('\n\n'.join(context))
    relevant=[]
    for sr in srows:
        vals=re.findall(r'156-6/(\d+)(?:-(\d+))?',sr['where'])
        if any(int(a)<=n<=int(b or a) for a,b in vals): relevant.append(sr)
    (p/'S.json').write_text(json.dumps(relevant,ensure_ascii=False,indent=2))
    img=ROOT/'source/SP53_CW_156-6_scans'/f'{folder}_156-6_scan{n:03}'
    info={**row,'whole':str(img)+'.jpg','half_a':str(img)+'_a.jpg','half_b':str(img)+'_b.jpg','preamble':str(OUT/'PREAMBLE.tex'),'h_preamble':str(SRC/'hua/transcripts/preamble/grothendieck.sty')}
    (p/'inputs.json').write_text(json.dumps(info,ensure_ascii=False,indent=2))
print('Prepared 28 page-specific witness packets; no image recognition used.')
