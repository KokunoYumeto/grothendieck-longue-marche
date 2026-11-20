from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/013/C')
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan013.jpg')
plan=[
('c01_faint_A',[164,482,246,594],'C doubt row 1: pale predecessor beneath dark A',1640),
('c02_meditation',[101,754,371,858],'C doubt row 2: ending and accents of Méditation',2700),
('c03_cascades',[476,763,713,855],'C doubt row 3: predecessor at Cascades',2370),
('c04_crossed_A',[160,874,248,951],'C doubt row 4: A crossed subdivision',1760),
('c05_crossed_B',[537,875,639,956],'C doubt row 5: B crossed subdivision',2040),
('c06_crossed_C',[927,875,1021,957],'C doubt row 6: C crossed subdivision',1880),
('c07_crossed_D',[1300,880,1393,955],'C doubt row 7: D crossed subdivision',1860),
('c08_crossed_E20',[1693,880,1786,954],'C doubt row 8: E Notes20 crossed subdivision',1860),
('c09_crossed_E23',[2103,878,2221,958],'C doubt row 9: E Notes23 crossed subdivision',2360),
('c10_lower_question_arrow',[102,913,181,1018],'C doubt row10: pale question and downward arrow',1422),
('c11_live_D',[1300,1033,1396,1112],'C doubt row11: live D subdivision with pale predecessor',1920),
('c12_vers_title',[423,1138,776,1260],'C doubt row12 plus; full title and detached marks below',2824),
('c13_live_A',[141,1039,226,1135],'C doubt row13a: pale predecessor below live A subdivision',1700),
('c14_live_C',[924,1032,1007,1114],'C doubt row13b: pale opening stroke at live C subdivision',1660),
('c15_left_margin',[25,393,143,862],'Complete connected left brace/arrow and question with opposed arrows',708),
('c16_bent_arrows',[229,629,344,749],'Two bent arrows between first date and title; line multiplicity',1610),
('c17_edge_top',[2302,87,2365,231],'First two cut-off right-edge strokes beside Notes and 23',756),
('c18_edge_blank',[2307,346,2365,447],'Third and fourth right-edge stroke clusters in blank upper row',928),
('c19_edge_dates',[2306,532,2365,672],'Fifth and sixth right-edge stroke clusters beside E and date',826),
('c20_edge_subdivisions',[2306,945,2365,1112],'Seventh and eighth right-edge clusters beside subdivision bands',708),
('c21_edge_lower_title',[2308,1174,2365,1225],'Ninth right-edge stroke beside lower title',1140),
('c22_edge_foot_archive',[2282,1538,2365,1680],'Tenth right-edge cluster and sideways archive number 12',996),
('c23_blank_A_stroke',[208,1383,265,1460],'Unrepresented small stroke in first blank lower cell',1140),
('c24_foot_A_stroke',[309,1569,368,1636],'Unrepresented pale stroke beneath first foot cell',1180),
('c25_blank_A_diagonals',[354,1002,399,1050],'Pale detached diagonal traces right of lower first arrow',900),
('c26_date_separator_tick',[386,604,429,650],'Small detached stroke at first/second date boundary',1032),
('c27_blank_E20_dot',[1902,1338,1959,1385],'Small detached pale mark below Fringale',1140),
('c28_baumeister_dot',[1683,682,1917,774],'Dot position above Baumeister and full letter forms',2574)
]
im=Image.open(source)
manifest=[]
for stem,bbox,purpose,width in plan:
 c=im.crop(tuple(bbox))
 c=ImageOps.autocontrast(c)
 scale=width/c.width
 c=c.resize((width,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.5,percent=110,threshold=3))
 target=root/(stem+'.png')
 c.save(target)
 manifest.append(dict(path=target.name,bbox=bbox,coordinate_system='original full scan; upper-left origin; pixels',rotation=0,purpose=purpose,output_size=list(c.size),viewed=False))
(root/'crops_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'local crops; source size',im.size)
