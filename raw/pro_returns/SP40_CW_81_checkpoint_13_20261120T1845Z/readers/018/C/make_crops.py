from PIL import Image, ImageOps
from pathlib import Path
import json
base=Path('out/readers/018/C')
source=Path('source/SP40_CW_81_scans/J81-02_81_scan018.jpg')
items=[
('01_opening',(225,55,780,165),4,'Opening dernière and local accent'),
('02_recurrence',(435,160,1070,290),4,'Parenthesis par récurrence'),
('03_unique_de',(790,445,1510,615),4,'Whole unique insertion guide and de/des ces n'),
('04_considerons',(585,880,1255,1018),4,'Contains E_i, et considérons and accent'),
('05_lemma',(230,1135,1640,1405),2,'Complete lemma group, underline, left rule, Pi marks and endpoint'),
('06_dire',(1345,1365,1555,1490),6,'Worked Dire initial and complete word'),
('07_quune',(220,1480,550,1605),5,'Whole qu’une insertion, its guide, cancelled la and classe'),
('08_ualpha',(530,1445,1050,1605),4,'Whole U_alpha de Pi insertion and guide, donnée/ne, alleged struck un'),
('09_first_E',(1140,1470,1600,1600),4,'Corrected first E_i, upper strokes, pas and i.e. est'),
('10_second_E_choisi',(940,1700,1620,1855),4,'Sigma_j, pi_0(X setminus corrected E_j), cancelled choisi with full endpoints'),
('11_composant',(220,1840,615,2000),5,'Full quoted composant(e), all quote strokes'),
('12_est',(1185,1820,1495,1950),5,'Cancelled est and live est/soit'),
('13_du',(235,1965,790,2115),4,'l’élément du/de pi_0 and complete word ends'),
('14_soit',(245,2135,1040,2290),3,'Full elements/soit insertion guide, de and final pi_0 formula'),
('15_deux',(245,2240,615,2363),5,'cas, cancelled deux and raised card I=2'),
('16_OK_accent',(625,2230,1130,2363),4,'Cancelled OK/cela/et and accented a fortiori through paper edge'),
('17_final',(1140,2220,1630,2363),4,'Final U_alpha, subset, Sigma^- and OK punctuation')]
im=Image.open(source)
records=[]
for name,bbox,scale,purpose in items:
    out=base/'crops'/f'{name}.png'
    cut=im.crop(bbox)
    cut=ImageOps.autocontrast(cut.resize((cut.width*scale,cut.height*scale),Image.Resampling.LANCZOS))
    cut.save(out)
    records.append({'path':str(out.relative_to(base)),'bbox':list(bbox),'coordinate_system':'original full scan, origin upper-left','rotation':0,'scale':scale,'purpose':purpose,'viewed':False})
(base/'crops_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print('Created 17 single-target local crops; no image comparison, recognition, compilation or rendering.')
