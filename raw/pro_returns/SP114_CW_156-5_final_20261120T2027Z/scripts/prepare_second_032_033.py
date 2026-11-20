"""Seal first readings for the last two pages after all first adjudications.
Reads edition text and first-reading metadata only; no image recognition.
"""
from pathlib import Path
import argparse,csv,json,hashlib
p=argparse.ArgumentParser();p.add_argument('--utc',required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1]
assert all((root/'review'/f'scan{n:03}_adjudicated.json').exists() for n in range(26,34))
out=root/'second';out.mkdir(exist_ok=True)
seals=[]
for n in (32,33):
    rec=json.loads((root/'review'/f'scan{n:03}_adjudicated.json').read_text())
    t=(root/'pages'/f'J156-5-04_156-5_scan{n:03}.tex').read_text()
    rows=rec['second_boxes']
    # Keep textual targets aligned with each saved crop. Enclosing state wrappers
    # may be repeated on excerpts because the parent scope begins outside a box.
    for z in rows:
        if n==33 and z['box']=='033-two_on_a':z['reading']=r"$A'\in F$. \deleted{On a} Soit $A$ le"
        if n==33 and z['box']=='033-jedis_mais':z['reading']=r'\deleted{Mais} Donc'
        if n==33 and z['box']=='033-jedis_et':z['reading']=r"$F'$, \deleted{et} Il en"
        if n==33 and z['box']=='033-jedis_insertion':z['reading']=r"\inserted{il suffirait $F'\ll F$}\deleted{)} cf lemme"
        if n==33 and z['box']=='033-cancel_underlined':z['reading']=r"\deleted{\uline{strate ouverte \deleted{dans \unsure{la}} de $F'$}. Soit}"
        if n==33 and z['box']=='033-cancel_de':z['reading']=r'\deleted{élément \deleted{de} tel que}'
        if n==33 and z['box']=='033-margin-rule':
            z.update(x0=65,y0=125,x1=285,y1=1755)
        if n==32 and z['box']=='032-b06':z['reading']=r'\[\deleted{A=\bigcup_{\substack{B\in F\\B\leq F}}B^\circ}\]'
    base=f'J156-5-04_156-5_scan{n:03}'
    targets=[out/(base+s+'.tsv') for s in ('_boxes','_first')]
    assert not any(p.exists() for p in targets),'Do not overwrite sealed readings'
    with targets[0].open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['box','kind','x0','y0','x1','y1'],delimiter='\t');w.writeheader()
        for z in rows:w.writerow({k:z[k] for k in w.fieldnames})
    with targets[1].open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t');w.writeheader()
        for z in rows:w.writerow({k:z[k] for k in w.fieldnames})
    seals.append({'scan':n,'utc':a.utc,'boxes':len(rows),'edition_sha256':hashlib.sha256(t.encode()).hexdigest(),'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in targets}})
(root/'review/second_seal_032_033.json').write_text(json.dumps(seals,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(seals,ensure_ascii=False))
