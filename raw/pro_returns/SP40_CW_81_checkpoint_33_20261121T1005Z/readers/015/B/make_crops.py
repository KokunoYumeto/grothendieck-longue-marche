from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/015/B')
src=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan015.jpg')
specs=[
('01_heading',(40,15,281,122),0,'title word and overwritten predecessor'),
('02_first_family',(1120,116,1355,222),0,'earlier glyph beneath first E and family indices'),
('03_fermes',(195,169,558,285),0,'opening insertion ending and curved insertion guide'),
('04_upper_left_note',(20,386,432,1080),-45,'complete slanted marginal note, abbreviation, first Sigma index, non and arrow'),
('05_right_nb',(1242,322,1672,474),0,'right NB exponent, glyph after setminus, punctuation'),
('06_b_final',(1460,518,1670,603),0,'cancelled glyph under final E in b and endpoint punctuation'),
('07_automatiquement',(976,597,1670,720),0,'pale automatically word and preceding vérifiée'),
('08_case_heading',(507,995,963,1102),0,'overwritten heading letters and comparison sign'),
('09_cancelled_drawing_label',(145,1030,256,1133),0,'cancelled upper-left Sigma label'),
('10_drawing_exponent',(466,1180,575,1268),0,'overwritten exponent at right brace'),
('11_equivaut',(1088,1365,1412,1472),0,'equivaut after first equality and endpoint à'),
('12_car_si',(211,1427,431,1513),0,'cancelled car si and possible opening curve'),
('13_aussi_a',(226,1680,490,1759),0,'faint continuation aussi à'),
('14_et_symetrique',(215,1854,972,1955),0,'faint leading et, symétriquement and endpoint'),
('15_vois_ouvert',(416,2009,652,2092),0,'cancelled vois. ouvert above first lower Sigma'),
('16_lower_insertion',(750,2009,1667,2154),0,'inserted ie clause, struck il contient les, on a and punctuation'),
('17_lower_margin',(19,1996,427,2344),-45,'slanted closure note, à signaler and avant, archive numeral'),
('18_louvert',(1278,2080,1640,2244),0,'l’ouvert insertion and guide at final parenthesis'),
('19_un_ferme',(228,2245,606,2344),0,'inserted un or une over fermé, preceding serait'),
('20_donc_cancelled',(821,2234,1118,2344),0,'donc/puis and final cancelled Sigma phrase')]
records=[]
for name,bbox,rotation,purpose in specs:
 im=src.crop(bbox)
 im=ImageOps.autocontrast(im,cutoff=0.2)
 if rotation:
  im=im.rotate(rotation,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 target=2400 if not rotation else 2700
 scale=target/im.width
 im=im.resize((target,round(im.height*scale)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1,percent=65,threshold=3))
 fn=name+'.png'
 im.save(root/fn)
 records.append({'path':fn,'bbox':list(bbox),'coordinate_system':'full scan 1691×2360, origin top-left','rotation':rotation,'purpose':purpose})
(root/'crops.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created',len(records),'single-pass crops in assigned B directory.')
