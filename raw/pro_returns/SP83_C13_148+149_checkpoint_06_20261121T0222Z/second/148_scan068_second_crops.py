from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import csv,json
ROOT=Path('/workspace/scratch/f28c4f52d3ec')
PAGE='148_scan068'
im=Image.open(ROOT/'source'/'SP83_C13_148+149_scans'/f'{PAGE}.jpg').convert('RGB')
with (ROOT/'result'/'second'/f'{PAGE}_boxes.tsv').open(newline='') as f:boxes=list(csv.DictReader(f,delimiter='\t'))
manifest=[]
for b in boxes:
    rect=tuple(int(b[k]) for k in ('x0','y0','x1','y1'))
    crop=ImageOps.autocontrast(im.crop(rect))
    scale=min(8,max(2,3000/crop.width))
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
    path=ROOT/'result'/'crops'/f'{PAGE}_second_{b["box"]}.png'
    crop.save(path)
    manifest.append({'box':b['box'],'kind':b['kind'],'original_box':rect,'path':str(path),'relative_path':f'crops/{path.name}','scale':scale,'bytes':path.stat().st_size,'viewed':False,'needs_transport':path.stat().st_size>6290000})
(ROOT/'result'/'second'/f'{PAGE}_second_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'dimensions':im.size,'boxes':len(boxes),'sizes':[(e['box'],e['bytes'],e['needs_transport']) for e in manifest]}))
