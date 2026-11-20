from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import csv,json
root=Path('/workspace/scratch/ddf8babdc42e')
source=root/'source/SP115_CW_156-7_scans/H156-01_156-7_scan006.jpg'
boxfile=root/'out/second/H156-01_156-7_scan006_boxes.tsv'
rotations={'B023':-45,'B027':-43,'B029':-40,'B035':-33,'B036':-40,'B037':-38,'B038':-35,'B041':-45}
with boxfile.open(encoding='utf-8',newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
im=Image.open(source).convert('RGB')
manifest={'source':str(source),'source_size':list(im.size),'coordinate_convention':'original whole-image pixels; right and lower coordinates exclusive','transform_order':['exact_box_crop','rotation','autocontrast','light_sharpening','resize'],'rotation':{'resample':'BICUBIC','expand':True,'fillcolor':'white'},'contrast':{'method':'ImageOps.autocontrast','cutoff':0},'sharpen':{'method':'UnsharpMask','radius':1,'percent':110,'threshold':3},'resize':{'width':2800,'aspect_ratio':'preserved','resample':'LANCZOS'},'crops':[]}
for row in boxes:
    name=row['box']
    coords=[int(row[k]) for k in ['x0','y0','x1','y1']]
    crop=im.crop(tuple(coords))
    rotation=rotations.get(name,0)
    if rotation:
        crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=ImageOps.autocontrast(crop)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
    crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
    output=root/f'out/crops/second_scan006_{name}.png'
    if output.exists():
        raise RuntimeError(f'Fresh-crop destination already exists: {output.name}')
    crop.save(output)
    manifest['crops'].append({'box':name,'kind':row['kind'],'coordinates':coords,'rotation_degrees':rotation,'file':str(output.relative_to(root)),'output_size':list(crop.size)})
(root/'out/second/H156-01_156-7_scan006_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Saved {len(boxes)} fresh exact-coordinate crops and manifest.')
