from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R3')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-08_156-4_scan065.jpg'
places=[
('01_opening_deletion',(1275,125,1635,425),'Opening deleted formula and possible opening parenthesis, with line below.'),
('02_question_final_F',(750,320,1130,525),'Overwritten final F and possible subscript, with preceding line.'),
('03_le_les_cas',(1140,510,1640,715),'le or les before cas, with next line.'),
('04_c4_letters_des',(640,824,1575,1040),'C4 variable/family letters and des/deux, with following line.'),
('05_inserted_necessity',(510,1035,1460,1260),'Interlined necessity sentence, abbreviation and deletion, with preceding line.'),
('06_cor1_pres',(275,1355,1100,1575),'Corollary 1 crossed start of presque, with preceding line and final punctuation.'),
('07_cor1_sauf',(1280,1250,1640,1435),'Corollary 1 crossed sauf and equality, with map above.'),
('08_cor2_heading',(860,1380,1645,1640),'Added Cor. 2 heading, connector, and canceled word, with following line.'),
('09_cor2_les',(910,1460,1645,1660),'Corollary 2 les/le deletion and deux, with preceding map line.'),
('10_cor2_fini',(275,1535,960,1775),'Inserted I est fini and canceled suivants/f, with adjacent lines.'),
('11_canceled_b_dash',(1020,1715,1645,1930),'Canceled case b ending and possible dash before alors, with next line.'),
('12_cor3_first_de',(1080,1780,1645,2020),'Canceled group after figures in Cor. 3, with preceding/following lines.'),
('13_cor3_parenthesis',(560,1870,1235,2040),'Inserted resp. finies and canceled Alors il with surrounding line.'),
('14_cor3_meme_de',(280,1980,1265,2150),'Two-stroke repetition mark and deleted de, with preceding line.'),
('15_cor3_last_map',(275,2080,810,2305),'Final map stroke, with following tuple line.'),
('16_cor3_pres_que',(1000,2110,1645,2320),'Final pres que spacing and ens punctuation, with preceding line.')
]
im=Image.open(source)
manifest=[]
for stem,bbox,reason in places:
 c=im.crop(bbox)
 c=ImageOps.autocontrast(c.convert('L'))
 scale=2400/c.width
 c=c.resize((2400,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=125,threshold=3))
 p=out/'crops'/f'{stem}.png'
 c.save(p)
 manifest.append({'path':str(p),'source':source,'bbox':list(bbox),'scale':scale,'rotation':0,'reason':reason,'transforms':'PIL grayscale, autocontrast (cutoff 0), LANCZOS to 2400 px width, UnsharpMask radius 1.2 / percent 125 / threshold 3'})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(out/'inspection_log.md').write_text('# R3 inspection log — scan 065\n\n1. Whole page: '+source+' — viewed once, no transform, for layout.\n2. Upper half: '+source.replace('.jpg','_a.jpg')+' — viewed once, no transform; all lines compared with C and H.\n3. Lower half: '+source.replace('.jpg','_b.jpg')+' — viewed once, no transform; all lines compared with C and H.\n\nNo OCR, text recognition, other scans, reader files, or outside sources.\n')
print('Created',len(manifest),'own crops; source size',im.size)
