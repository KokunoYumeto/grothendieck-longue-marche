from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
base=Path('out/readers/022/B')
src=Path('source/SP40_CW_81_scans/J81-03_81_scan022.jpg')
items=[
('01_opening',[250,60,835,270],2600,'Opening On/Un and procède/procédé; insertion and preceding deletion wording'),
('02_parenthesis_ending',[1390,140,1685,315],2300,'C doubts R01 opening curve and R02 disjoints/disjointes; complete right edge'),
('03_top_formula_insert',[995,135,1335,390],2500,'Complete opening V formula, Sigma head/hat, underbrace and descending equality/intersection'),
('04_brace_old_relation',[390,265,1020,495],3000,'Brace geometry, marginal trivial arrow and C R03 cancelled relation plus empty-set glyph'),
('05_main_equality_annotations',[575,630,1673,855],3200,'Main equality bars and Sigma head; both lower annotations and C R04 right connector/state'),
('06_comme',[240,775,1670,1010],3200,'Cancelled Comme line including all symbols, final punctuation and prouvons continuation'),
('07_inverse',[535,1000,1160,1130],2800,'Cancelled inverse inclusion, complete retraced Sigma and formula endpoint'),
('08_soit_neighbourhood',[245,1120,1660,1340],3200,'Cancelled Soit and neighbourhood lines, bars, small memberships, i.e. punctuation and right continuation'),
('09_or_corrected_noun',[245,1250,1665,1540],3400,'C R05 on and R06 predecessor noun; peut considérer cette, inserted égalité and full adjoining wording'),
('10_old_variable',[275,1525,1380,1655],3000,'C R07 old variable after l’espace, equality and complete cancellation continuation'),
('11_dans_lequel',[270,1645,1550,1860],3200,'Cancelled dans lequel/laquelle and complete disjointes, local frame endpoint and live Or restart'),
('12_lower_sigma_mark',[595,1815,1345,2095],3000,'Detached slash above bottom Y/Z display, Sigma heads/hats, beta and union subscript delimiters')
]
im=Image.open(src)
records=[]
for name,bbox,width,purpose in items:
 cr=ImageOps.autocontrast(im.crop(bbox).convert('RGB'))
 h=round(cr.height*width/cr.width)
 cr=cr.resize((width,h),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
 path=base/'crops'/f'{name}.png'
 cr.save(path)
 records.append({'path':str(path.relative_to(base)),'bbox':bbox,'coordinate_space':'original full scan; top-left origin; x right, y down','rotation':0,'width':width,'height':h,'purpose':purpose,'viewed':False})
(base/'crop_plan.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
