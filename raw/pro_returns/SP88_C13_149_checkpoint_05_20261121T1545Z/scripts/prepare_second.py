"""Freeze first readings and box coordinates before blind image-only reading."""
from pathlib import Path
import csv, hashlib, json
from assemble import SCANS

ROOT=Path(__file__).resolve().parents[1]

def write(path,headers,rows):
    if path.exists():
        raise FileExistsError(f'Refusing to replace frozen audit input: {path}')
    with path.open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(headers);w.writerows(rows)

def main():
    accepted=ROOT/'review/accepted'
    if not all((accepted/f'149_scan{n:03d}.json').exists() for n in SCANS):
        raise RuntimeError('Blind second reading begins only after all 25 first readings are accepted.')
    frozen=[]
    for n in SCANS:
        stem=f'149_scan{n:03d}'
        data=json.loads((accepted/f'{stem}.json').read_text())
        boxes=data['audit_boxes']
        if len({r['box'] for r in boxes}) != len(boxes):
            raise ValueError(f'{stem}: duplicate box identifiers')
        bp=ROOT/'second'/f'{stem}_boxes.tsv';fp=ROOT/'second'/f'{stem}_first.tsv'
        write(bp,['box','kind','x0','y0','x1','y1'],[[r['box'],r['kind'],*r['bbox']] for r in boxes])
        write(fp,['box','reading'],[[r['box'],r['reading']] for r in boxes])
        for p in [bp,fp]:
            frozen.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (ROOT/'second/FIRST_READINGS_SHA256.json').write_text(json.dumps(frozen,indent=2)+'\n')
    print(json.dumps({'pages':len(SCANS),'frozen_files':len(frozen)}))

if __name__=='__main__':main()
