import csv, json
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
base = Path('/workspace/scratch/ddf8babdc42e')
source = base / 'source/SP115_CW_156-7_scans/H156-01_156-7_scan007.jpg'
boxlist = base / 'out/second/H156-01_156-7_scan007_boxes.tsv'
outdir = base / 'out/crops'
with boxlist.open(encoding='utf-8', newline='') as f:
    boxes = list(csv.DictReader(f, delimiter='\t'))
im = Image.open(source).convert('RGB')
manifest = {'source':str(source), 'source_size':list(im.size), 'box_list':str(boxlist), 'crops':[]}
for item in boxes:
    box_id = item['box']
    bounds = tuple(int(item[k]) for k in ('x0','y0','x1','y1'))
    rotation = -30 if box_id == 'B014' else 0
    crop = im.crop(bounds)
    crop = ImageOps.autocontrast(crop, cutoff=.4)
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    size = (2800, round(crop.height * 2800 / crop.width))
    crop = crop.resize(size, Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=100, threshold=3))
    path = outdir / ('second_scan007_' + box_id + '.png')
    crop.save(path)
    manifest['crops'].append({'box':box_id,'kind':item['kind'],'original_box':list(bounds),'rotation_degrees_pillow':rotation,'rotation_resampling':'BICUBIC' if rotation else None,'rotation_expand':bool(rotation),'rotation_fill':'white' if rotation else None,'resize_resampling':'LANCZOS','output_size':list(size),'autocontrast_cutoff':.4,'unsharp_mask':{'radius':1.1,'percent':100,'threshold':3},'operations':['crop','autocontrast']+(['rotate'] if rotation else [])+['resize','unsharp_mask'],'crop_path':str(path)})
mp = base / 'out/second/H156-01_156-7_scan007_crop_manifest.json'
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_size':im.size,'crops':len(boxes),'manifest':str(mp),'rotated_boxes':['B014']}))
