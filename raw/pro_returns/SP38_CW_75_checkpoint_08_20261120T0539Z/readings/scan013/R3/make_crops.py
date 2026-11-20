from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R3')
src=Path('/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013.jpg')
im=Image.open(src)
specs=[
('01_vertical_label',[528,76,617,258],'C01: tiny label beside the upward arrow between Z objects remains unresolved after the halves.'),
('02_upper_shaft',[617,70,760,132],'Arrowhead versus short terminal turn on the upper Z to G shaft; witnesses differ.'),
('03_lower_shaft',[421,201,542,264],'Arrowhead versus blunt downward turn on the lower 1 to Z shaft; witnesses differ.'),
('04_splitte',[784,313,982,391],'C02: ending and possible accent of the first splitte/splittée occurrence.'),
('05_canceled_une',[962,530,1221,607],'C04: canceled material and its boundary before the live l\u2019ext.'),
('06_torseur_sur',[1251,1060,1632,1150],'C05 and H plural: noun ending and following compressed preposition.'),
('07_canceled_sous',[992,1174,1109,1267],'C06: letters and cancellation state of the short word after espace affine.'),
('08_overwritten_field',[1096,1172,1185,1265],'C07: underform and final alphabet of the first overwritten field letter.'),
('09_canceled_word',[1187,1177,1556,1264],'C08: heavily canceled word after the second ou encore; opening punctuation and placement context.'),
('10_box_S',[1071,1588,1288,1696],'C09 and C10: decorative alphabet and small subscript at the end of the boxed comparison.'),
('11_A2',[889,1705,1193,1802],'C11: alphabet of A in the parenthesized condition below the box.'),
('12_lower_signs',[723,1988,875,2143],'C12: first lower vertical correspondence sign, with neighboring second sign and its objects for context.'),
('13_last_field',[644,2132,860,2231],'C13: overwritten field underform and superscript at the foot.'),
('14_upper_detached',[1128,627,1184,687],'Two detached dark traces beside the remark: writing versus surface/ink debris is unresolved.'),
('15_box_detached',[1477,1616,1546,1688],'Two detached dark traces to the right of the box: writing versus surface/ink debris is unresolved.')]
manifest={'scan':13,'reader':'R3','original_image':str(src),'original_dimensions':[1687,2362],'half_a_box':[0,0,1687,1261],'half_b_box':[0,1101,1687,2362],'processing':'Pillow RGB crop, LANCZOS enlargement to long edge 2400, autocontrast cutoff 0.5, UnsharpMask(radius=1.2,percent=135,threshold=3); no rotation','crops':[]}
for name,box,why in specs:
    crop=im.crop(box).convert('RGB')
    scale=2400/max(crop.size)
    crop=crop.resize(tuple(round(v*scale) for v in crop.size),Image.Resampling.LANCZOS)
    crop=ImageOps.autocontrast(crop,cutoff=.5)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=135,threshold=3))
    filename=f'{name}.png'
    crop.save(root/filename)
    manifest['crops'].append({'id':name,'file':filename,'bbox':box,'rotation_degrees':0,'reason':why,'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Saved 15 distinct tight crops, manifest, and creation script.')
