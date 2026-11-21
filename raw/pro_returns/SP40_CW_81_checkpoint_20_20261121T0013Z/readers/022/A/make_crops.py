from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/readers/022/A'
src=ROOT/'source/SP40_CW_81_scans/J81-03_81_scan022.jpg'
targets=[
('01_opening',[250,60,1615,245],'opening cancelled wording, accents, inserted clause, cancellation endpoints'),
('02_parenthetical_end',[1300,140,1681,310],'C R01 opener, C R02 disjoints ending, nearby hatted glyph, explicit parenthesis placement'),
('03_initial_formula',[860,125,1340,390],'initial V formula, hatted Sigma, separate head, brace, descending equality, intersection insertion'),
('04_first_brace',[375,260,1625,500],'two braced conditions, marginal arrow, C R03 cancelled relation/empty set, live terms and Sigma heads'),
('05_main_equality',[575,625,1670,830],'main equality and lower annotations; C R04 connector/state, heads, closure bars and hats'),
('06_comme',[245,770,1668,1010],'cancelled Comme argument, local spellings/accents, inclusion endpoint, Sigma groups'),
('07_inverse_soit',[265,1000,1540,1245],'cancelled inverse inclusion and Soit line, overlines/head runs, punctuation and i.e.'),
('08_neighbourhood',[240,1215,1668,1338],'full neighbourhood clause, W, x and montrons qu\'il endpoint'),
('09_or_and_noun',[250,1320,1668,1535],'rencontre endpoint and cancelled Or/on/peut considérer clause with corrected noun and égalité continuation; C R05/R06'),
('10_old_variable',[280,1525,1385,1650],'C R07 old variable after l\'espace, full cancelled equation, heads/hats/cancellation run'),
('11_dans_lequel',[280,1650,1550,1880],'cancelled dans lequel clause and disjointes continuation, live restart wording, crossing frame'),
('12_detached_slash',[815,1730,1270,1950],'detached short slash above/right of live disjointes with adjoining word/context'),
('13_YZ',[610,1910,1330,2095],'final Y/Z display, both hats and heads, equals, beta index and setminus braces')]
records=[]
with Image.open(src) as im:
 for stem,bbox,purpose in targets:
  crop=ImageOps.autocontrast(im.crop(tuple(bbox)).convert('RGB'))
  factor=3000/crop.width
  crop=crop.resize((3000,round(crop.height*factor)),Image.Resampling.LANCZOS)
  crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=100,threshold=3))
  rel='crops/'+stem+'.png'
  crop.save(OUT/rel)
  records.append({'path':rel,'bbox':bbox,'coordinate_system':'original full scan; origin upper left; x right, y down','rotation':0,'resample':'PIL LANCZOS','autocontrast':True,'sharpen':'UnsharpMask radius=1.1 percent=100 threshold=3','output_size':list(crop.size),'purpose':purpose,'viewed':False,'view_count':0})
(OUT/'crops.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created',len(records),'unique unresolved-target crops.')
