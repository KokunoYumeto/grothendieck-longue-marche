from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R2')
source=Path('/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013.jpg')
items=[
 ('01_vertical_label',[530,73,620,254],0,'C01: small label beside the first upward arrow; numeral, wavy sign, or letters.'),
 ('02_splitte',[704,306,980,400],0,'C02: first splitte/splittée ending and accent; include (E) and following comma.'),
 ('03_cancelled_une',[950,523,1223,622],0,'C04: cancellation state and letters between d apostrophe and l ext.'),
 ('04_torseur_sur',[1250,1057,1640,1155],0,'C05 and H plural: read singular/plural torseur and following compressed preposition.'),
 ('05_cancelled_sous',[967,1176,1100,1270],0,'C06: short crossed word after affine, with underline below.'),
 ('06_overwritten_field',[1086,1174,1180,1268],0,'C07: underlying and live letters at the first affine field symbol.'),
 ('07_deleted_word',[1184,1176,1570,1286],0,'C08: word canceled after the second ou encore and opening parenthesis.'),
 ('08_box_S_subscript',[1070,1564,1294,1720],0,'C09 and C10: decorative S alphabet and shallow following index in the box.'),
 ('09_A2',[888,1709,1209,1811],0,'C11: alphabet of the first A and placement beneath the boxed line.'),
 ('10_field_stack',[705,1943,901,2145],0,'C12: lower vertical relation and overinked plus; preserve both field/group correspondences.'),
 ('11_bottom_correction',[545,2144,1005,2246],0,'C13: visible canceled underform and final F at the last A3 identity.'),
 ('12_top_shafts',[612,72,971,130],0,'C/H arrow discrepancy: inspect small endpoint on the Z to G top shaft and following shafts.'),
 ('13_bottom_shafts',[413,191,1038,267],0,'C/H arrow discrepancy: inspect the four lower horizontal connectors and their endpoints.'),
 ('14_detached_pair_upper',[1119,616,1202,699],0,'New doubt: isolated dark pair below the extension paragraph; ink versus surface trace.'),
 ('15_detached_point_rule',[1273,755,1351,832],0,'New doubt: isolated dark point right of the divider; ink versus surface trace.'),
 ('16_detached_pair_box',[1472,1617,1549,1695],0,'New doubt: isolated pair right of the boxed identity; ink versus surface trace.'),
]
source_im=Image.open(source).convert('RGB')
manifest={
 'scan':'013','reader':'R2','whole_image':str(source),'whole_dimensions':[1687,2362],
 'halves':[{'path':'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_a.jpg','offset':[0,0],'dimensions':[1687,1261]}, {'path':'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_b.jpg','offset':[0,1101],'dimensions':[1687,1261]}],
 'crops':[]
}
for name,bbox,rotation,reason in items:
    im=source_im.crop(bbox)
    scale=min(12,max(4,2200/max(im.size)))
    im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
    im=ImageOps.autocontrast(im,cutoff=0.5)
    im=ImageEnhance.Sharpness(im).enhance(1.3)
    if rotation:
        im=im.rotate(rotation,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    filename=name+'.png'
    im.save(base/filename)
    manifest['crops'].append({'id':name,'bbox':bbox,'rotation_degrees':rotation,'reason':reason,'path':filename,'dimensions':list(im.size),'processing':'LANCZOS enlargement; autocontrast cutoff 0.5%; sharpness factor 1.3','visually_inspected':False})
(base/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(items),'distinct tight crops.')
