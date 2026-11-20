from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/811dda00717a/work/readers/scan039/R1')
src=Image.open('/workspace/scratch/811dda00717a/source/SP41_CW_81_scans/J81-05_81_scan039.jpg').convert('RGB')
items=[
('01_rhs_annotation',[1240,90,1600,365],0,'First Pi case and deleted mark after i.e.'),
('02_upper_margin',[30,195,550,625],-25,'All four slanted lines; transitivité and final phrase'),
('03_formula27',[480,565,1050,765],0,'Arrow letter, angular target P and compressed subscript'),
('04_elles',[1140,760,1585,905],0,'Final strokes of elle(s)'),
('05_avec',[775,970,1510,1100],0,'Connector after de C and abbreviation punctuation'),
('06_panache',[225,1220,705,1338],0,'Non panaché ending and punctuation'),
('07_defined_term',[900,1360,1525,1525],0,'Maquette/moquette and overwritten beginning of ordonnée'),
('08_decompositions_fini',[240,1460,1650,1645],0,'Parenthetical décompositions n-aires; cancelled word and raised fini'),
('09_sigma_pt',[835,1565,1675,1745],0,'Sigma placement and point abbreviation'),
('10_propriete',[235,1695,1535,1970],0,'Clause wraps from ayant la/les to propriété(s) suivante(s)'),
('11_cancelled_text',[495,1880,1645,2100],0,'Three cancelled trial lines; comparison and congrus/mod wording'),
('12_live_conditions',[470,2040,1675,2320],0,'Black cancellation, revised comparability line and b) cancellation attachment'),
('13_labels',[270,1930,570,2295],0,'Cancelled branch labels and left formula number'),
('14_lower_margin',[25,1985,395,2345],-40,'Entire lower slanted NB, with source bottom edge kept'),
('15_last_nb',[260,2220,1692,2360],0,'Final NB verb and complete final line through physical edges')]
manifest=[]
for name,box,angle,targets in items:
 assert 0 <= box[0] < box[2] <= src.width and 0 <= box[1] < box[3] <= src.height
 im=src.crop(tuple(box))
 trim=None
 if angle:
  im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  mask=im.convert('L').point(lambda p:255 if p<215 else 0)
  bb=mask.getbbox()
  if bb:
   trim=[max(0,bb[0]-16),max(0,bb[1]-16),min(im.width,bb[2]+16),min(im.height,bb[3]+16)]
   im=im.crop(tuple(trim))
 im=ImageOps.autocontrast(im)
 im=im.resize((3000,round(im.height*3000/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=140,threshold=3))
 path=root/'crops'/f'{name}.png'
 im.save(path)
 manifest.append({'id':name,'bbox':box,'angle_degrees':angle,'rotated_trim':trim,'path':str(path),'size':list(im.size),'targets':targets,'view_count':0})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
