from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_068/R3')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan068.jpg'
items=[
('01_first_cancel',[290,65,1245,210],'Cancelled opening line, final quoted glyph and deletion extent'),
('02_minimale',[320,215,690,375],'Minimale compressed middle; context immediately above'),
('03_celles',[700,210,1610,373],'Celles/telles initial and all of parenthesis, with preceding line'),
('04_cancel_sappelle',[490,300,935,470],'Cancelled s\'appelle and last small word, with line above'),
('05_operator',[320,735,1300,920],'Isolated point, cosup/p descenders and operator, with preceding line'),
('06_bijection',[325,820,805,1070],'Raised e and possible leader in bijection, with preceding line'),
('07_ens_saturees',[820,810,1665,1028],'Ens punctuation and final saturée/s letters, with preceding line'),
('08_sur_elles',[325,1015,1655,1218],'Sur and literal equals mark after elles, with following line'),
('09_m0_ou_f0',[200,1300,1275,1525],'Inserted M0 and leader; ou accent; cancelled de; final M after F0, with preceding line'),
('10_cancel_on_definit',[1280,1300,1665,1520],'Cancelled On définit at line end, with preceding line'),
('11_cancel_lapplication',[315,1500,1370,1670],'Entire cancelled L\'application ... phrase, with following line'),
('12_desidentifie',[330,1515,900,1680],'Verb before Sigma, with cancelled line above'),
('13_sigma_deleted_f',[910,1510,1580,1675],'De/a after Sigma, crossed family sign, ses/un deux group; with preceding line'),
('14_realisations_partie',[325,1590,1265,1760],'Realisations and partie/s compressed endings, with preceding line'),
('15_premier_p',[1200,1590,1585,1738],'First power-set letter and its M, with preceding line'),
('16_second_p',[325,1640,635,1830],'Second power-set letter and family symbol, with preceding line'),
('17_anti_correction',[945,1890,1545,2132],'Worked anti compound, exact cancellation and surviving strokes, with preceding line')]
im=Image.open(source)
manifest=[]
for name,bbox,reason in items:
 crop=im.crop(bbox)
 width=2600 if bbox[2]-bbox[0]>1000 else 2400
 scale=width/crop.width
 crop=ImageOps.autocontrast(crop)
 crop=crop.resize((width,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
 path=out/'crops'/(name+'.jpg')
 crop.save(path,quality=94)
 manifest.append({'path':str(path),'source':source,'bbox':bbox,'scale':scale,'rotation':0,'reason':reason,'transformations':['autocontrast','LANCZOS enlargement','unsharp mask radius 1 percent 110 threshold 3','JPEG quality 94']})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(out/'inspection_log.md').write_text('# R3 inspection log — 156-4 scan 068\n\nStarted image inspection 2026-11-20T10:19:08Z.\n\n1. Viewed whole page once: '+source+' — layout, text blocks, states, page number.\n2. Viewed supplied upper half once: '+source.replace('.jpg','_a.jpg')+' — every line compared against C and H.\n3. Viewed supplied lower half once: '+source.replace('.jpg','_b.jpg')+' — every line compared against C and H.\n\nAll subsequent images are R3 crops from the whole image. Each crop was created once; original coordinates, scale, rotation, and reasons are in crop_manifest.json. No OCR, research, compiler, or other reader files were used.\n')
print('Created',len(manifest),'own crops.')
