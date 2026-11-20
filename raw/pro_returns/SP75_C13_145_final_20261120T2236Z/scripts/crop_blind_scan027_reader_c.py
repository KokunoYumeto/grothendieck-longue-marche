from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageFilter
root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
packet=root/"audit_packets/145_scan027"
edition=root/"edition"
im=Image.open(packet/"page.jpg")
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    boxes=list(csv.DictReader(f,delimiter="\t"))
manifest=[]
for b in boxes:
    coords=[int(b[k]) for k in ("x0","y0","x1","y1")]
    p=edition/"crops"/("second_145_scan027_"+b["box"]+".png")
    assert not p.exists(), "Only one original crop per box"
    c=ImageOps.autocontrast(im.crop(tuple(coords)),cutoff=0.5)
    scale=min(3,2800/c.width)
    c=c.resize((round(c.width*scale),round(c.height*scale)),Image.Resampling.LANCZOS)
    c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    c.save(p)
    manifest.append({"box":b["box"],"crop":str(p.relative_to(edition)),"coords":coords,"rotation_degrees":0,"inspected":False,"observations":"","submission_status":"PROVISIONAL"})
out=edition/"second/145_scan027_crop_manifest.provisional.json"
assert not out.exists()
out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Saved",len(manifest),"original crops; page size",im.size)
print(out)

