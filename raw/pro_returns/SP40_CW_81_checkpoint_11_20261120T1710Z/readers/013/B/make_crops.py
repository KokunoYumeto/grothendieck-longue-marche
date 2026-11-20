from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/013/B')
src=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan013.jpg')
im=Image.open(src)
items=[
('01_under_A',(160,482,248,594),0,'C doubt row 1: pale predecessor under dark A'),
('02_meditation',(91,748,370,865),0,'C doubt row 2: entire first title ending with preceding line'),
('03_cascades',(476,680,710,858),0,'C doubt row 3 and adjoining initial Réveil flourish'),
('04_cancel_A_and_question',(100,872,251,1020),0,'C doubt rows 4 and 10: cancelled A subdivision; lower question and arrow'),
('05_cancel_B_and_arrow',(492,873,649,1065),0,'C doubt row 5: cancelled B subdivision and descending arrow'),
('06_cancel_C',(909,872,1041,967),0,'C doubt row 6: cancelled C subdivision'),
('07_cancel_D',(1276,873,1409,964),0,'C doubt row 7: cancelled D subdivision'),
('08_cancel_E20',(1680,872,1804,964),0,'C doubt row 8: cancelled Notes20 subdivision'),
('09_cancel_E23',(2086,873,2229,970),0,'C doubt row 9: cancelled Notes23 subdivision'),
('10_live_A',(137,1029,244,1148),0,'C doubt row13 sublocus A: pale precursor below live (i)'),
('11_live_C',(907,1020,1022,1122),0,'C doubt row13 sublocus C: pale offset opening parenthesis'),
('12_live_D',(1286,1016,1400,1120),0,'C doubt row11: overwritten live subdivision'),
('13_plus',(418,1133,763,1255),0,'C doubt row12: plus in full second title'),
('14_margin',(23,387,139,860),0,'Left margin barred up arrow, brace, question, opposed arrows and detached point'),
('15_bent_arrows',(230,623,345,753),0,'Bent arrows between first date and first title: full connected strokes'),
('16_date_hook',(350,583,462,663),0,'Detached hook and rule near first column right edge in date row'),
('17_E20_titles',(1575,678,1955,872),0,'Baumeister dot and Bâtisseur accent'),
('18_E20_lower_titles',(1572,1140,1958,1334),0,'Spiel- und Sucht and Jeu - et Fringale punctuation'),
('19_E23_maitre',(2012,1140,2301,1239),0,'Paired quote ticks and Maître accent'),
('20_lower_A_trace',(193,1368,280,1467),0,'Detached short trace below Envol'),
('21_lower_A_foot_trace',(294,1556,378,1639),0,'Detached oblique trace under M1976 row'),
('22_lower_E23_dash',(2196,1268,2313,1385),0,'Detached dash below last title and nearby rule'),
('23_lower_E20_spot',(1870,1297,1974,1409),0,'Gray compact spot below Fringale'),
('24_lower_D_point',(1442,1477,1554,1585),0,'Tiny point in blank near Sch I'),
('25_A_lower_slant',(344,995,418,1065),0,'Pale slant near first column right boundary below crossed row'),
]
manifest=[]
for name,bbox,rot,purpose in items:
 crop=im.crop(bbox)
 if rot: crop=crop.rotate(rot,expand=True)
 scale=min(14,2400/crop.width,3200/crop.height)
 size=(round(crop.width*scale),round(crop.height*scale))
 crop=ImageOps.autocontrast(crop.resize(size,Image.Resampling.LANCZOS),cutoff=0.3)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=90,threshold=3))
 path=name+'.png'
 crop.save(root/path)
 manifest.append({'path':path,'bbox':list(bbox),'coordinate_system':'original full scan, upper-left origin, right/bottom exclusive','rotation':rot,'purpose':purpose,'size':list(size),'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'planned tight crops.')
