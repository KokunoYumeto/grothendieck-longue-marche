from PIL import Image,ImageOps
from pathlib import Path
import json,os
root=Path('/workspace/scratch/b12af914b284')
im=Image.open(root/'input/SP91_C13_150_scans/150_scan073.jpg').convert('RGB')
items=[
('p00_heading',[32,18,1215,153],'Author32, item14, title and underline scope',0),
('p01_dans',[734,131,1105,211],'M0637 ds/dans, first parenthesis',0),
('p02_insert_ferme',[461,278,1088,399],'Inserted quoted standart T_<i and cancelled ferme',0),
('p03_first_union',[1114,289,1476,421],'Whole dotted reworked X/Sigma union formula M0638',0),
('p04_formula42',[402,476,1072,575],'Formula42 and its handwritten number',0),
('p05_definition',[374,585,844,691],'Ring/dot tubular notation and def label',0),
('p06_nb_phrase',[947,574,1640,681],'Il aurait suffit versus Il suffirait en fait',0),
('p07_nb_standart',[1255,683,1524,761],'Literal standart in main NB',0),
('p08_lui',[237,769,1655,879],'lui abbreviation M0639 and full final Sigma formula',0),
('p09_margin',[14,465,391,869],'Complete slanted margin NB and its formulas',-40),
('p10_ambient',[1176,969,1565,1086],'Whole ambient formula with overwritten X and doubtful T index M0640',0),
('p11_prendre',[908,1068,1604,1157],'Cancelled prendre and live d abord prendre',0),
('p12_standart_ds',[726,1156,1590,1244],'standart, underlined ds/dans and ou sinon',0),
('p13_ds',[236,1266,590,1361],'Second ds/dans before Xj',0),
('p14_dot_cancel',[564,1414,1075,1531],'First dotted T prime and cancelled trailing s',0),
('p15_union',[1068,1403,1549,1536],'la trace de/des and full union with indices M0641 M0642',0),
('p16_donc',[568,1531,1656,1612],'M0643 donc c est and successeur phrase',0),
('p17_singular',[570,1599,1657,1703],'soit S dot T prime and singular part wording',0),
('p18_alors',[241,1705,1134,1815],'Undotted T prime and period; On prend alors/donc',0),
('p19_drawing',[116,1557,404,1698],'Oval, filled point and three outgoing strokes',0),
('p20_insert_formula',[235,1768,1086,1909],'standart, inserted T(S dot T prime), leader and de strike state',0),
('p21_insert_union',[474,1875,1621,2005],'Inserted union Tk above reunion and all attachment strokes',0),
('p22_standart',[235,2012,805,2121],'Final standart des Xk',0),
('p23_final_ambient',[881,1997,1577,2124],'Whole parenthesized index and X---Xj formula M0644',0),
('p24_insert_de',[234,2163,732,2324],'Inserted de before final T prime and its leader',0),
('p25_aura',[738,2191,1261,2294],'Cancelled prendra and inserted aura',0),
('p26_formula43',[332,2267,1254,2359],'Whole final formula43 and handwritten number',0),
('p27_folio',[18,2288,93,2346],'Other-hand foliation72',0)
]
manifest={'scan':'073','size':list(im.size),'crops':[]}
for name,box,purpose,rotation in items:
 c=ImageOps.autocontrast(im.crop(box))
 if rotation: c=c.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 c=c.resize((2400,round(2400*c.height/c.width)),Image.Resampling.LANCZOS)
 file='crops/150_scan073_'+name+'.png'
 c.save(root/'edition'/file)
 manifest['crops'].append({'file':file,'box':box,'purpose':purpose,'rotation':rotation})
path=root/'edition/scripts/150_scan073_crop_index.json'
tmp=path.with_suffix('.json.tmp');tmp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');os.replace(tmp,path)
print(path)
print('crops',len(items))
