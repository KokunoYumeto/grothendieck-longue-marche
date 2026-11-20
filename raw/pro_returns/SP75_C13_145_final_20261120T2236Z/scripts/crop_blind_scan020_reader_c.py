from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import csv,json
root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition=root/"edition"
packet=root/"audit_packets/145_scan020"
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    boxes=list(csv.DictReader(f,delimiter="\t"))
source=Image.open(packet/"page.jpg")
rotations={f"B{i:02d}":-45 for i in range(6,12)}
rotations["B12"]=-20
manifest=[]
for row in boxes:
    coords=[int(row[k]) for k in ("x0","y0","x1","y1")]
    output=edition/"crops"/f"second_145_scan020_{row['box']}.png"
    assert not output.exists()
    crop=ImageOps.autocontrast(source.crop(coords),cutoff=.5)
    angle=rotations.get(row["box"],0)
    if angle:
        crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor="white")
    crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    crop.save(output)
    manifest.append({"box":row["box"],"crop":str(output.relative_to(edition)),"coords":coords,
        "rotation_degrees":angle,"inspected":False,"observations":"","submission_status":"PROVISIONAL"})
path=edition/"second/145_scan020_crop_manifest.provisional.json"
assert not path.exists()
path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Created {len(manifest)} crops once; provisional manifest saved. Left-margin crops rotate -45 degrees; right note -20 degrees.")

