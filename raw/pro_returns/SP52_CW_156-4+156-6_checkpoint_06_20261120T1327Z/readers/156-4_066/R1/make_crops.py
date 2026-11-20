from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R1')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066.jpg'
items=[
('01_lemma_insertion',[1250,122,1635,285],'Raised parenthesis, fini/finie, insertion extent, and capitalization of following il.'),
('02_lemma_abbreviation',[238,277,715,391],'Literal first f et s abbreviation and its punctuation.'),
('03_lemma_nb',[966,360,1628,493],'C doubt nb; following fini sont and slashed empty set.'),
('04_notations_cancelled_parenthesis',[560,628,950,735],'Cancelled loop after pi_0(G), preceding comma and following et.'),
('05_first_superscript',[495,737,775,860],'Cancelled superscript cat/act and live ! above pi_0(cal F).'),
('06_attention',[905,732,1335,849],'C doubt Attention and comma.'),
('07_second_superscript',[1355,699,1545,846],'Looped upright d/! above second pi_0(cal F).'),
('08_quotation',[288,945,1460,1047],'Article du/des, Sup, quotation marks, punctuation and unclosed Attention parenthesis.'),
('09_tuple_left_gloss',[196,1064,563,1295],'First C alphabet and lower contrée/contrie gloss with connector.'),
('10_tuple_relation_gloss',[565,1073,820,1310],'Retraced third relation, cancelled predecessor, entire right gloss, and upward pointer.'),
('11_tuple_right',[822,1045,1580,1165],'on pose aussi and final C alphabet in pi_0(C).'),
('12_axiom_right_deletion',[1425,1388,1620,1531],'Cancelled rightmost material after product: exists F/cal F.'),
('13_axiom_corrected_fi',[1009,1515,1390,1670],'Overwritten final F_i in restriction equation and possible prior cal F.'),
('14_axiom_terminal_relation',[1400,1520,1660,1645],'Terminal i vdash/in I and punctuation.'),
('15_residual_heading',[335,1735,945,1880],'Contrée/Contrie and résiduelle/réssiduelle spelling and accents.'),
('16_bottom_initial_deletion',[480,1876,845,2090],'Cancelled indexed family, inserted H_i, and placement connector to figures.'),
('17_cosupp_deletion',[309,2070,760,2175],'Cancelled Cosupp./Compl. Phi before que.'),
('18_disjointe',[936,2072,1630,2215],'Final e of disjointe/disjoint and clause continuation.'),
('19_final_posons',[1010,2272,1495,2345],'Cancelled final Posons/Poser and live replacement.')]
im=Image.open(source)
manifest=[]
for name,bbox,reason in items:
 cr=im.crop(bbox)
 cr=ImageOps.autocontrast(cr)
 scale=2400/cr.width
 cr=cr.resize((2400,round(cr.height*scale)),Image.Resampling.LANCZOS)
 cr=cr.filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
 path=root/'crops'/(name+'.jpg')
 cr.save(path,quality=94)
 manifest.append(dict(path=str(path),source=source,bbox=bbox,scale=scale,rotation=0,reason=reason,transformations=['crop','autocontrast','LANCZOS resize to 2400px width','UnsharpMask radius=1 percent=110 threshold=3','JPEG quality=94']))
(root/'crop_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
log='''# Inspection log — 156-4 scan 066, R1\n\nStarted: 2026-11-20T09:23:41Z (assignment and packet reading).\n\nOnly the assigned metadata, C.tex, H.tex, conventions, preamble, C_context.md and notation snapshot were read. No other reader, page, OCR, or outside source was consulted.\n\n## Required image views, in order\n\n1. Whole page: /workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066.jpg — once, native view, for layout.\n2. Upper half: /workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066_a.jpg — once, native view, every line compared to both witnesses.\n3. Lower half: /workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066_b.jpg — once, native view, every line compared to both witnesses.\n\nWhole size: 1680 × 2361; half a: 1680 × 1260; half b: 1680 × 1261. Half b starts at whole y=1100.\n\n## Open loci fixed before crops\n\n'''
for n,b,r in items:
 log+=f'- {n}: {r} Original whole-page bbox {b}.\n'
log+='\n## Crop creation\n\nCreated each locus exactly once with make_crops.py. All use the whole-page original, the recorded bbox, no rotation, autocontrast, LANCZOS to 2400 px wide, mild UnsharpMask (radius 1, 110%, threshold 3), JPEG quality 94. Exact scales are in crop_manifest.json and report.json. Each will be viewed once in the numbered order; no decided place will be recropped.\n\n## Crop inspection evidence\n\n'
(root/'inspection_log.md').write_text(log)
print(f'Created {len(manifest)} crops and inspection log.')
