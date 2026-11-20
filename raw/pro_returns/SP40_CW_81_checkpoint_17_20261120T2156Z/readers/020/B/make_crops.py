from pathlib import Path
from PIL import Image, ImageOps
import json
base=Path('out/readers/020/B')
source=Path('source/SP40_CW_81_scans/J81-03_81_scan020.jpg')
items=[
 ('01_opening_ring.png',[1065,65,1260,180],'C R01a: first Pi-I superscript'),
 ('02_second_ring.png',[630,165,815,285],'C R01b: Pi-J superscript'),
 ('03_opening_overwritten_U.png',[1270,145,1545,300],'Opening overwritten U/Pi group, indices and comma'),
 ('04_les_word_parmi.png',[735,275,1270,382],'C R02: complete word after les, its endpoint and parmi'),
 ('05_first_intersection_index.png',[575,365,990,520],'C R03: full positive intersection with overwritten or descending subscript'),
 ('06_cancelled_sigma_before_U.png',[280,757,615,915],'C R04: cancelled Sigma and index before live U'),
 ('07_voisinage_E.png',[1190,740,1555,890],'C R05 and overwritten base: complete de E group, comma and et'),
 ('08_barred_intersections.png',[270,895,1135,1035],'Three overwritten base loci, closure rules, indices and endpoint punctuation'),
 ('09_On_verb_donc.png',[1190,875,1650,995],'C R10: complete On verb donc line, accents and word strokes'),
 ('10_en_cancelled_word.png',[945,1010,1635,1140],'C R06: classes est en and whole cancelled endpoint word'),
 ('11_ce_qui_acheve.png',[1130,1138,1645,1318],'Complete ce qui achève group, accents and q descender'),
 ('12_aussi_dem.png',[270,1290,975,1445],'C R11 and R07: aussi/ainsi, la, dém./dem., and par'),
 ('13_lemma_formula_insert.png',[870,1530,1535,1930],'C R01c/R08: lemma ring, complete union/brace/hat/index group and crossed non vide insertion with guide'),
 ('14_membership_correction.png',[575,1895,1110,2050],'C R09: cancelled on a, positive Sigma and complete reworked membership/arrow group')
]
im=Image.open(source)
manifest=[]
for name,box,purpose in items:
 crop=ImageOps.autocontrast(im.crop(box).convert('L'))
 width=2600 if box[2]-box[0] < 600 else 3000
 height=round(crop.height*width/crop.width)
 crop=crop.resize((width,height),Image.Resampling.LANCZOS)
 crop.save(base/name)
 manifest.append({'path':name,'bbox':box,'coordinate_system':'original full scan, x right and y down, origin upper left; PIL right/bottom exclusive','rotation':0,'purpose':purpose,'source':str(source),'operations':['grayscale','autocontrast','LANCZOS enlargement'],'output_size':[width,height]})
(base/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(base/'image_audit.json').write_text(json.dumps({'start_utc':'2026-11-20 20:45:44 UTC','source_dimensions':{'full':[1683,2362],'a':[1683,1261],'b':[1683,1261]},'coordinate_note':'Local crops use original full-scan coordinates. Half b lower-edge offset is 2362-1261=1101; half a origin is the full top. No pixel comparisons performed.','whole':{'path':str(source),'successful_views':1},'halves':[{'path':'source/SP40_CW_81_scans/J81-03_81_scan020_a.jpg','successful_views':1},{'path':'source/SP40_CW_81_scans/J81-03_81_scan020_b.jpg','successful_views':1}],'local_views':[],'failed_unseen_deliveries':[],'processing_note':'One whole and each supplied half were delivered successfully once. Local crops prepared once from full source, without OCR, rendering, or compilation.'},ensure_ascii=False,indent=2)+'\n')
print('Prepared',len(manifest),'local crops and image audit.')
