from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
root = Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R1')
source = Path('/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013.jpg')
items = [
 ('01_vertical_label',[527,72,614,257], 'C01: small label beside the left upward arrow; the two Z objects provide context.'),
 ('02_splitte',[694,317,987,393], 'C02: compressed ending and possible acute after splitte, with the preceding (E).'),
 ('03_cancelled_une',[939,522,1242,621], 'C04: canceled letters between d apostrophe and live l ext.'),
 ('04_torseur_preposition',[1246,1052,1637,1164], 'C05 and H plural: end of torseur and contracted sur/sous before Z2.'),
 ('05_cancelled_sous',[839,1175,1105,1283], 'C06: letters and cancellation state after underlined affine.'),
 ('06_overwritten_f2',[1091,1170,1190,1268], 'C07: underform below the first overwritten F2, with underline and nearby opening curve.'),
 ('07_cancelled_word',[1195,1175,1563,1280], 'C08: one canceled word after the second ou encore; context includes that phrase.'),
 ('08_s_subscript',[1061,1576,1288,1690], 'C09/C10: alphabet and small subscript of the boxed S, with preceding relation and box edges.'),
 ('09_a_alphabet',[890,1696,1201,1794], 'C11: A alphabet in the parenthetical statement below the box.'),
 ('10_lower_relations',[704,1989,890,2141], 'C12: overwritten left vertical comparison and its F3-plus / Z3 endpoints; adjacent equality supplies context.'),
 ('11_overwritten_f3',[548,2139,1005,2240], 'C13: canceled Z-like underform in the final A3 statement.'),
 ('12_detached_mark',[1118,539,1246,709], 'New open locus: short detached dark mark below ext.; nearby prose provides context.'),
 ('13_detached_point',[988,744,1347,833], 'New open locus: detached point to right of the divider, with divider endpoint as context.')
]
with Image.open(source) as im:
    for name,bbox,reason in items:
        crop=im.crop(tuple(bbox)).convert('RGB')
        size=(round(crop.width*2600/max(crop.size)),round(crop.height*2600/max(crop.size)))
        crop=crop.resize(size,Image.Resampling.LANCZOS)
        crop=ImageOps.autocontrast(crop)
        crop=crop.filter(ImageFilter.UnsharpMask(radius=1.6,percent=150,threshold=2))
        crop.save(root/(name+'.png'))
manifest={'scan':'013','reader':'R1','source':str(source),'source_dimensions':[1687,2362], 'halves': [{'path':'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_a.jpg','origin':[0,0],'dimensions':[1687,1261]},{'path':'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_b.jpg','origin':[0,1101],'dimensions':[1687,1261]}], 'whole_viewings':1,'half_viewings':[1,1], 'crop_count':len(items), 'crops':[{'file':name+'.png','bbox':box,'rotation_degrees':0,'enhancement':'LANCZOS to 2600 pixels on longest edge, autocontrast, UnsharpMask radius 1.6 percent 150 threshold 2','reason':reason,'visually_inspected':False} for name,box,reason in items]}
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(items),'tight crops; no original image was altered.')
