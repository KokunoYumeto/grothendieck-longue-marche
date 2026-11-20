from pathlib import Path
import csv, re, json, sys

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'source'
OUT = ROOT / 'SP44_CW_36_work'
W = SRC / 'SP44_CW_36_witnesses'

def make(scan):
    rows=list(csv.DictReader((W/'page_map.tsv').open(), delimiter='\t'))
    row=next(r for r in rows if int(r['our_scan'])==scan)
    folder=row['folder']; their=int(row['their_page'])
    h=(W/row['hua_file']).read_text()
    m=re.search(r'\\page\{'+str(their)+r'\}',h)
    if not m: raise ValueError('H page not found')
    n=re.search(r'\\page\{\d+\}|\\end\{document\}',h[m.end():])
    hp=h[m.start():m.end()+n.start() if n else len(h)]
    cp=(W/row['codex_file']).read_text()
    d=(W/f'codex/{folder}/{folder}_doubts.md').read_text().splitlines()
    doubts='\n'.join(l for l in d if (lambda m: m and int(m.group())==scan)(re.search(r'\b0[12][0-9]\b',l)))
    notes=(W/f'codex/{folder}/{folder}_notes.md').read_text().splitlines()
    notes='\n'.join(l for l in notes if re.match(r'\| 0?'+str(scan)+r' \|',l))
    packet=OUT/'packets'/f'scan{scan:03d}'
    packet.mkdir(exist_ok=True)
    (packet/'C.tex').write_text(cp)
    (packet/'H.tex').write_text(hp)
    (packet/'notation.tsv').write_text((OUT/'notation.tsv').read_text())
    ims=[SRC/'SP44_CW_36_scans'/f'{folder}_36_scan{scan:03d}{s}.jpg' for s in ('','_a','_b')]
    info={'scan':scan,'their_page':their,'folder':folder,'C_source':row['codex_file'],'H_source':row['hua_file'],'images':list(map(str,ims))}
    (packet/'metadata.json').write_text(json.dumps(info,indent=2))
    text=f'# Scan {scan:03d} — page-local packet\n\nWhole, top half a, bottom half b:\n'+''.join(f'- `{p}`\n' for p in ims)
    text+='\n## Witness C\n```latex\n'+cp+'\n```\n\n## Witness H (their page '+str(their)+')\n```latex\n'+hp+'\n```\n'
    text+='\n## C earlier doubts and notation entries mentioning this page\n'+doubts+'\n\n## C earlier notes mentioning this page\n'+notes+'\n'
    text+='\n## Notation as decided before this page\n```tsv\n'+(OUT/'notation.tsv').read_text()+'\n```\n'
    text+='\n## Cropping\nUse `python '+str(OUT/'scripts/crop.py')+' --scan '+str(scan)+' --reader Rx --label locus --box x0 y0 x1 y1 [--rotate degrees]`. Coordinates refer to the whole image. This saves one JPG and records dimensions/operations. Then view the returned path. The original whole image dimensions are available through PIL without reopening its pixels.\n'
    (packet/'packet.md').write_text(text)
    print(packet/'packet.md')

if __name__=='__main__': make(int(sys.argv[1]))
