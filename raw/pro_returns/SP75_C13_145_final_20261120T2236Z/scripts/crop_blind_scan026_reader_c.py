from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageFilter
root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
packet=root/"audit_packets/145_scan026"
edition=root/"edition"
im=Image.open(packet/"page.jpg")
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    boxes=list(csv.DictReader(f,delimiter="\t"))
manifest=[]
for b in boxes:
    coords=[int(b[k]) for k in ("x0","y0","x1","y1")]
    p=edition/"crops"/("second_145_scan026_"+b["box"]+".png")
    assert not p.exists(), "Each original crop is made once"
    c=ImageOps.autocontrast(im.crop(tuple(coords)),cutoff=0.5)
    rot=-35 if b["box"]=="B07" else 0
    if rot:
        c=c.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor="white")
    factor=min(3,2800/c.width)
    c=c.resize((round(c.width*factor),round(c.height*factor)),Image.Resampling.LANCZOS)
    c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    c.save(p)
    manifest.append({"box":b["box"],"crop":str(p.relative_to(edition)),"coords":coords,"rotation_degrees":rot,"inspected":False,"observations":"","submission_status":"PROVISIONAL"})
p=edition/"second/145_scan026_crop_manifest.provisional.json"
assert not p.exists()
p.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Saved",len(manifest),"original crops; page size",im.size)
print(p)

