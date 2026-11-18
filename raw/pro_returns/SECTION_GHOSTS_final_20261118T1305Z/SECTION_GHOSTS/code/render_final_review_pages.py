#!/usr/bin/env python3
"""Render specified final PDF pages for actual visual inspection."""
from pathlib import Path
import fitz,json,hashlib
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/"SECTION_GHOSTS_paper.pdf"
assert hashlib.sha256(pdf.read_bytes()).hexdigest()=="fed1f30941dbbe05d50da29e95bc9d236b571e0ef449912bbcc4805fabcd3563"
out=ROOT/"qa/root";out.mkdir(parents=True,exist_ok=True)
pages=[1,2,3,4,5,9,17,54,100,200,300]+list(range(338,344))+list(range(359,365))
doc=fitz.open(pdf)
images=[]
for n in pages:
    pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
    p=out/f"page_{n:03d}.png";pix.save(str(p))
    im=Image.open(p).convert("RGB")
    panel=Image.new("RGB",(im.width,im.height+32),"#eeeeee")
    panel.paste(im,(0,32));ImageDraw.Draw(panel).text((12,9),f"PDF PAGE {n}",fill="black")
    images.append((n,panel))
montages=[]
for i in range(0,len(images),4):
    group=images[i:i+4];w=max(im.width for _,im in group);h=max(im.height for _,im in group)
    canvas=Image.new("RGB",(2*w,2*h),"#cccccc")
    for j,(n,im) in enumerate(group):canvas.paste(im,((j%2)*w,(j//2)*h))
    p=out/f"montage_{i//4+1:02d}.png";canvas.save(p)
    montages.append({"file":str(p),"pages":[n for n,_ in group]})
(out/"render_manifest.json").write_text(json.dumps({"pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),"pages_rendered":pages,"montages":montages,"viewed":False},indent=2)+"\n")
print(json.dumps(montages,indent=2))
