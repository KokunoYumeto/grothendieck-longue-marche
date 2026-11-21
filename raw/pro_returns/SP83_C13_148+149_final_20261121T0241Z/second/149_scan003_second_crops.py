from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops
import csv,json

ROOT=Path('/workspace/scratch/f28c4f52d3ec')
PAGE='149_scan003'
im=Image.open(ROOT/'source/SP83_C13_148+149_scans'/f'{PAGE}.jpg').convert('RGB')
with (ROOT/'result/second'/f'{PAGE}_boxes.tsv').open(newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
manifest=[]
for row in boxes:
    coords=[int(row[k]) for k in ['x0','y0','x1','y1']]
    crop=ImageOps.autocontrast(im.crop(coords))
    scale=min(8,max(2,3000/crop.width))
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
    p=ROOT/'result/crops'/f'{PAGE}_second_{row["box"]}.png'
    crop.save(p)
    item={'box':row['box'],'kind':row['kind'],'original_box':coords,'path':str(p),'relative_path':'crops/'+p.name,'scale':scale,'bytes':p.stat().st_size,'viewed':False}
    if p.stat().st_size>6290000:
        t=ROOT/'result/crops/transport'/f'{PAGE}_second_{row["box"]}.webp'
        t.parent.mkdir(exist_ok=True)
        crop.save(t,lossless=True,method=4)
        assert ImageChops.difference(crop,Image.open(t).convert('RGB')).getbbox() is None
        item['transport_path']=str(t)
        item['transport_pixels_identical']=True
    manifest.append(item)
(ROOT/'result/second'/f'{PAGE}_second_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
