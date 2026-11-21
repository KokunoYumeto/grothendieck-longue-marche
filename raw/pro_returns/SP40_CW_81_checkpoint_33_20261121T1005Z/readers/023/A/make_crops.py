from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/023/A')
src=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan023.jpg')
plans=[
('01_opening_a',[225,165,935,305],0,'Reduced opening a and complete adjacent first formula'),
('02_replacement',[245,270,785,395],0,'Complete cancelled contient, raised rencontre and adjoining aucun'),
('03_first_union',[390,375,1025,550],0,'First union old/live strokes, hatted Sigma predecessor and decorations; full index and comma'),
('04_cancelled_lead',[1020,390,1575,530],0,'Complete cancelled words before je dis, including full descenders and endpoint'),
('05_continuation',[615,535,1455,680],0,'Beta membership and reduced on a en fait, with isolated high brown fleck'),
('06_margin',[25,630,585,980],-24,'Complete slanted note: all three lines, cancellation and final parenthesis'),
('07_first_display',[615,665,1658,800],0,'Complete first displayed inclusion, Sigma body/head/index/plus and parenthetical endpoint'),
('08_cequi',[245,780,1645,950],0,'Complete ce qui prouvera l assertion and mieux, with full descenders'),
('09_cela_revient',[285,1010,1270,1175],0,'Complete last top inclusion and Cela revient au, including Sigma decorations'),
('10_lemma_intro',[250,1170,1515,1405],0,'Complete two-line lemma lead, cancelled tel que les and et, S04, tels and que'),
('11_lemma_condition',[285,1378,1445,1505],0,'Complete duplicate relation display including both Sigmas, indices, signs and endpoint'),
('12_lemma_conclusion',[280,1480,1635,1700],0,'Complete two-line lemma conclusion, old/live insertion cluster, both Sigmas and punctuation'),
('13_unfinished',[240,1660,1645,1848],0,'Complete Cela line, crossed signifie que, live verb and final short word, all descenders and detached flank marks'),
('14_corollary_heading',[275,1785,1645,1960],0,'Complete corollary lead, abbreviation and indexed family with punctuation'),
('15_corollary_body',[245,1900,1645,2148],0,'Complete marked corollary statement: Pi, ring, formée with full descender, S10, V union and S11, vertical rule and all endpoints'),
('16_final_line',[290,2115,1655,2325],0,'Complete final two-line assertion with accents, card K and comparison sign'),
('17_left_mark',[70,400,380,540],0,'Detached tiny mark left of first union, with adjoining E beta as location context'),
('18_opening_line',[275,60,1648,235],0,'Complete opening prose including reduced maintenant and prouvons, all descenders and endpoint')]
im=Image.open(src)
records=[]
for name,box,rotation,purpose in plans:
    crop=im.crop(box)
    crop=ImageOps.autocontrast(crop)
    if rotation: crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    target=3600 if crop.width>850 else 2800
    crop=crop.resize((target,round(crop.height*target/crop.width)),Image.Resampling.LANCZOS)
    p=out/(name+'.png')
    crop.save(p)
    records.append({'path':p.name,'bbox':box,'coordinate_system':'full scan, top-left origin, pixels; right/bottom exclusive','rotation':rotation,'purpose':purpose,'viewed':False})
(out/'crop_plan.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
with (out/'progress.log').open('a') as f:
    f.write('Whole image, half a and half b each successfully delivered once. Half b origin is (0,1101), derived from full height 2362 minus half height 1261.\n')
    f.write('Eighteen unresolved-target crops planned before inspection; one transformation per target, PIL autocontrast and LANCZOS enlargement, margin rotated -24 degrees.\n')
print('Created 18 planned crops; none yet viewed.')
