from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageFilter

ROOT=Path('/workspace/scratch/ddf8babdc42e')
SOURCE=ROOT/'source/SP115_CW_156-7_scans/H156-01_156-7_scan002.jpg'
BOXES=ROOT/'out/second/H156-01_156-7_scan002_boxes.tsv'
rows=list(csv.DictReader(BOXES.open(),delimiter='\t'))
im=Image.open(SOURCE)
manifest={'source':str(SOURCE),'source_size':list(im.size),'box_list':str(BOXES),'crops':[]}
for r in rows:
    box=tuple(int(r[k]) for k in ('x0','y0','x1','y1'))
    angle=-27 if r['box']=='B004' else 0
    width=2200 if box[2]-box[0]<=200 else 2800
    crop=ImageOps.autocontrast(im.crop(box),cutoff=0.4)
    if angle:
        crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=100,threshold=3))
    out=ROOT/'out/crops'/f"second_scan002_{r['box']}.png"
    crop.save(out)
    manifest['crops'].append({'box':r['box'],'kind':r['kind'],'original_box':list(box),
        'rotation_degrees_Pillow':angle,'rotation_expand':True,'rotation_fillcolor':'white',
        'rotation_resample':'BICUBIC','output_width':width,'output_size':list(crop.size),
        'resample':'LANCZOS','autocontrast_cutoff':0.4,
        'unsharp_mask':{'radius':1.1,'percent':100,'threshold':3},
        'operation_order':['exact original crop','autocontrast','rotation if specified','resize','light unsharp mask'],
        'file':str(out)})
path=ROOT/'out/second/H156-01_156-7_scan002_crop_manifest.json'
path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'{len(rows)} crops written; source dimensions {im.size}')
