"""One original-coordinate crop per assigned scan120 box; no OCR."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import csv, json, math

base=Path('/workspace/scratch/0cab6a548abb')
second=base/'edition/second'
crops=base/'edition/crops'
diag=second/'diagnostics'
diag.mkdir(exist_ok=True)
with (second/'149_scan120_boxes.tsv').open(encoding='utf-8',newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
source=Image.open(base/'source/SP88_C13_149_scans/149_scan120.jpg').convert('RGB')
records=[]
def starts(length,maximum=1800,overlap=240):
    if length<=maximum:return [0]
    count=math.ceil((length-maximum)/(maximum-overlap))+1
    return [round(n*(length-maximum)/(count-1)) for n in range(count)]
for b in boxes:
    bbox=tuple(int(b[k]) for k in ['x0','y0','x1','y1'])
    part=source.crop(bbox)
    part=ImageOps.autocontrast(part,cutoff=0)
    part=part.resize((part.width*3,part.height*3),Image.Resampling.LANCZOS)
    target=crops/f"149_scan120_second_{b['box']}.png"
    part.save(target)
    panels=[]
    for row,y in enumerate(starts(part.height,1500),1):
        for col,x in enumerate(starts(part.width),1):
            rect=(x,y,min(x+1800,part.width),min(y+1500,part.height))
            tile=part.crop(rect)
            canvas=Image.new('RGB',(tile.width,tile.height+28),'white')
            canvas.paste(tile,(0,28))
            ImageDraw.Draw(canvas).text((8,5),f"{b['box']} panel r{row} c{col}; saved-crop bbox {rect}; overlap retained",fill='black')
            path=diag/f"149_scan120_{b['box']}_r{row}_c{col}.png"
            canvas.save(path)
            panels.append({'file':str(path),'saved_crop_bbox':rect,'row':row,'col':col,'rotation_degrees':0})
    records.append({'box':b['box'],'original_bbox':bbox,'canonical_crop':str(target),'scale':3,'rotation_degrees':0,'source_crop_count':1,'panels':panels})
(diag/'149_scan120_crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(records),'canonical crops;',sum(len(r['panels']) for r in records),'saved-crop panels')
