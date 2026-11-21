from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import csv,json

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan050'
source=ROOT/'source/SP83_C13_148+149_scans'/f'{PAGE}.jpg'
im=Image.open(source).convert('RGB')
boxes=list(csv.DictReader((ROOT/'result/second'/f'{PAGE}_boxes.tsv').open(),delimiter='\t'))
manifest=[]
for row in boxes:
    box=[int(row[k]) for k in ['x0','y0','x1','y1']]
    assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
    crop=ImageOps.autocontrast(im.crop(box))
    scale=min(8,max(2,3000/crop.width))
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
    path=ROOT/'result/crops'/f"{PAGE}_second_{row['box']}.png"
    crop.save(path)
    manifest.append(dict(box=row['box'],kind=row['kind'],original_box=box,path=str(path),
        relative_path=f"crops/{PAGE}_second_{row['box']}.png",scale=scale,bytes=path.stat().st_size,
        viewed=False,needs_transport=path.stat().st_size>6290000))
(ROOT/'result/second'/f'{PAGE}_second_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,source_size=im.size,boxes=len(boxes),crops=manifest)))
