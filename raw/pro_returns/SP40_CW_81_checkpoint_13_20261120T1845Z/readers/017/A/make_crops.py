from pathlib import Path
from PIL import Image, ImageOps
import json
root = Path('/workspace/scratch/94548b74fbe0')
out = root / 'out/readers/017/A'
specs = [
 ('01_upper_correction',(1020,165,1680,335),0,'C row01: deleted subject, verb and adjective; on ait insertion and si/où witness difference'),
 ('02_struck_sentence',(265,286,1030,438),0,'C row02: cancelled trouve; entire cancelled sentence and descender context'),
 ('03_equation_endpoints',(785,410,1200,602),0,'Top two RHS endpoints and detached point: punctuation and indices'),
 ('04_first_join',(793,738,1235,846),0,'C row03: first join in Sigma12 formula'),
 ('05_margin_note',(20,925,322,1338),-40,'C row04a/b: marginal wording, Pi/pi, cancelled predecessor and complete formula'),
 ('06_cancelled_definie',(315,1250,915,1395),0,'C row05: cancelled wording after de X and live following word'),
 ('07_first_E_predecessor',(1075,1245,1590,1395),0,'C row07a: predecessor beneath first E_j and following quantifier'),
 ('08_intersection_start',(312,1393,813,1502),0,'C row06a/b: cancellation and live intersection'),
 ('09_later_cancelled_sign',(1074,1495,1455,1625),0,'C row07b: isolated cancelled sign after later E_j'),
 ('10_partition_display',(625,1598,1252,1755),0,'Display coproduct limits, pi_0, alpha and terminal index'),
 ('11_first_union_dot',(515,1825,1030,1992),0,'First indexed union and detached point to its left'),
 ('12_inserted_partition_ring',(735,1950,930,2080),0,'C row08a: inserted Pi_J upper ring and insertion guide'),
 ('13_middle_union',(1000,1970,1290,2120),0,'C row11: transverse stroke on middle union'),
 ('14_binary_partition_guide',(1085,2048,1570,2220),0,'C row08b: binary partition ring; added quantifier guide; H parentheses'),
 ('15_U_subscript',(305,2138,575,2310),0,'C row12: U subscript predecessor, replacement, equals and complete insertion guide'),
 ('16_final_words',(1105,2205,1655,2343),0,'C rows09 and10: final parenthetical variable and Pour/Puis; full endpoints')
]
manifest=[]
with Image.open(root/'source/SP40_CW_81_scans/J81-02_81_scan017.jpg') as src:
 for name,box,rotation,purpose in specs:
  im=ImageOps.autocontrast(src.crop(box).convert('RGB'))
  if rotation:
   im=im.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  pre=im.size
  target=(2600,round(im.height*2600/im.width))
  im=im.resize(target,resample=Image.Resampling.LANCZOS)
  path=name+'.png'
  im.save(out/path)
  manifest.append({'path':path,'bbox':list(box),'rotation':rotation,'purpose':purpose,'source':'full scan, upper-left origin','pre_enlargement_size':list(pre),'output_size':list(target),'processing':'RGB autocontrast; optional BICUBIC rotation on expanded white canvas; width 2600 with proportional rounded height; LANCZOS enlargement; no sharpening'})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created 16 distinct tight crops and crop_manifest.json; source size 1685 x 2363. No OCR or image comparison performed.')
