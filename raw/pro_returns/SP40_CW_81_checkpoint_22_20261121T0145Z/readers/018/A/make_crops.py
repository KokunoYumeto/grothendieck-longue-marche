from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/018/A'
src=root/'source/SP40_CW_81_scans/J81-02_81_scan018.jpg'
items=[
('01_opening',(225,65,785,165),'Opening dernière and nearby si'),
('02_recurrence',(440,165,1060,285),'Parenthetical récurrence with accents and ending'),
('03_ens',(230,280,1150,370),'ens, possible abbreviation stop, adjoining de/des/classes/est'),
('04_unique',(805,390,1515,615),'unique insertion guide and de/des ces n, full nearby que descender'),
('05_considerons',(765,880,1455,1005),'considérons accent and ending'),
('06_lemma',(225,1145,1645,1395),'Lemma ring and cancelled subscript; underline and vertical rule endpoints; terminal punctuation'),
('07_dire',(1175,1375,1565,1505),'Worked-over Dire and preceding colon'),
('08_quune',(220,1475,750,1620),'qu’une, cancelled la, complete insertion guide and adjoining classe donnée'),
('09_insert_u',(710,1445,1140,1605),'Inserted U_alpha/de/Pi ring with guide, baseline ne, punctuation'),
('10_bar_e',(1155,1465,1620,1605),'Corrected E_i and independent possible upper bar with pas and i.e. est'),
('11_formula',(800,1695,1605,1860),'le, Sigma_j+, corrected E_j index and cancelled choisi'),
('12_quoted',(215,1840,810,1985),'Quoted composant(e) ending and quote strokes'),
('13_double_est',(1165,1825,1515,1950),'Cancelled est and live est/soit'),
('14_soit',(240,2080,1055,2280),'Inserted soit Sigma_i- with complete curved guide and adjoining éléments de pi expression'),
('15_card',(245,2240,600,2363),'Cancelled deux with raised card I=2, comma and bottom boundary'),
('16_bottom',(620,2235,1120,2363),'Cancelled OK/cela and accent before fortiori'),
('17_final_u',(1130,2230,1645,2363),'Final U subscript, inclusion, Sigma_i- and final OK punctuation')]
manifest=[]
for name,box,purpose in items:
 im=ImageOps.autocontrast(Image.open(src).crop(box))
 im=im.resize((2600,round(im.height*2600/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 dest=out/(name+'.png');im.save(dest)
 manifest.append({'path':dest.name,'bbox':list(box),'rotation':0,'purpose':purpose,'size':list(im.size)})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'created':len(manifest),'source_size':[1683,2363],'source_coordinate_convention':'full-scan top-left origin, x right, y down; half a origin (0,0); supplied half b bottom anchored, origin (0,1101) from heights 2363 and1262; no pixel comparison performed'},indent=2))
