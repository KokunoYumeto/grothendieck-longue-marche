from pathlib import Path
import re, shutil, csv

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'source/SP48_CW_104_witnesses'
OUT=ROOT/'SP48_CW_104'
PACK=ROOT/'reader_inputs'
PACK.mkdir(exist_ok=True)
batch=(SRC/'hua/transcripts/104/batch-01.fr.tex').read_text()
markers=list(re.finditer(r'\\page\{(\d+)\}',batch))
drawing_by_scan={}
for drawing in sorted((SRC/'hua/transcripts/104/drawings').glob('*.tex')):
    with drawing.open() as f: header=f.readline()
    page_match=re.search(r'PDF page (\d+)',header)
    if page_match:
        scan=int(page_match.group(1))
        if scan in drawing_by_scan:raise RuntimeError('Multiple drawings need explicit packet names')
        drawing_by_scan[scan]=drawing
for row in csv.DictReader((SRC/'page_map.tsv').open(),delimiter='\t'):
    n=int(row['our_scan']); p=int(row['their_page']); folder=row['folder']
    dest=PACK/f'scan{n:03d}'; dest.mkdir(exist_ok=True)
    shutil.copy2(SRC/row['codex_file'],dest/'C.tex')
    m=next(x for x in markers if int(x.group(1))==p)
    k=markers.index(m)
    h=batch[m.start():markers[k+1].start() if k+1<len(markers) else len(batch)]
    (dest/'H.tex').write_text(h)
    # Drawing suffixes enumerate drawings, not manuscript page numbers.
    drawing=drawing_by_scan.get(n)
    if drawing: shutil.copy2(drawing,dest/'H_drawing.tex')
    elif (dest/'H_drawing.tex').exists(): (dest/'H_drawing.tex').unlink()
    ctxt=[]
    for suffix in ['doubts','audit','notes']:
        text=(SRC/f'codex/{folder}/{folder}_{suffix}.md').read_text()
        if suffix=='audit':
            found=re.search(rf'## Scan {n}\s*\n(.*?)(?=\n## Scan |\Z)',text,re.S)
            lines=found.group(0) if found else ''
        else:
            selected=[]
            for line in text.splitlines():
                mentions={int(v) for v in re.findall(r'\b[Ss]cans?\s+(\d+)',line)}
                leading_scan=re.match(r'\|\s*(\d+)(?=\D|$)',line)
                if (leading_scan and int(leading_scan.group(1))==n) or (not leading_scan and mentions=={n}): selected.append(line)
            lines='\n'.join(selected)
        ctxt.append(f'# Witness C {suffix}: scan {n}\n{lines}')
    (dest/'C_context.md').write_text('\n\n'.join(ctxt))
    (dest/'page.json').write_text(__import__('json').dumps(row,indent=2))
shutil.copy2(SRC/'codex/H104-01/PREAMBLE.tex',OUT/'PREAMBLE.tex')
print('Prepared text packets for scans 002–017. Images were not opened by this script.')
