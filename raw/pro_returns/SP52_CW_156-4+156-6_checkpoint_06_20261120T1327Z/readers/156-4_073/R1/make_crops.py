from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R1')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan073.jpg'
items=[
('01_margin',[20,20,320,460],-55,'Complete slanted upper-left note, including isolated low de and high final continuation.'),
('02_first_cancellation',[680,55,1000,270],0,'Cancelled primed capital after de, with continuation line below.'),
('03_overwritten_g',[1210,65,1555,275],0,'Overwritten capital before de F in opening continuation.'),
('04_c7_ending',[1110,415,1670,640],0,'Ending induise/induit and C-prime/G-prime, including preceding line and right blank.'),
('05_role_and_orders',[840,625,1555,835],0,'rôle/rôles, crossed upright before straight order and bowed order, with symétrique above.'),
('06_faux_mark',[285,745,795,970],0,'Crossed curled sign after faux and colon, with preceding line.'),
('07_donnes',[285,865,820,1065],0,'donnés/données and terminal comma, with preceding line.'),
('08_sous_figure',[780,840,1670,1050],0,'tte and singular sous figure with possible hyphen, plus G-prime and preceding line.'),
('09_soit_induite',[285,965,840,1145],0,'soit/sont/est and singular induite, with preceding line.'),
('10_last_overprint',[1315,935,1668,1145],0,'Overwritten final F and closing punctuation, with preceding G-prime line.'),
('11_strengthening',[430,1135,1670,1345],0,'Worked verb, par la suite, and small stroke before C7 on following line.'),
('12_crossed_heading',[280,1450,750,1710],0,'Scribbled lower heading and possible numeral, with inserted phrase below.'),
('13_draft_capital',[805,1345,1665,1605],0,'Overwritten G after Soient F comma and surrounding line.'),
('14_insertion',[280,1565,1050,1780],0,'Full inserted Considérons les, connecting enclosure, Conditions and cancelled adjective.'),
('15_conclusion',[970,1975,1665,2160],0,'Mais pas phrase, uncertain middle word, comma and closing stop; preceding formula line.'),
('16_diagram',[1270,2035,1560,2300],0,'Entire four-node diagram, worked top relation, cup, dots and arrow endpoint, with upper surrounding line.'),
('17_final_arrow',[340,2145,1125,2335],0,'Separately struck proof line, final implication and terminal punctuation.'),
]
im=Image.open(source)
records=[]
for name,bbox,rot,reason in items:
 c=im.crop(bbox)
 if rot: c=c.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 scale=2400/c.width
 c=c.resize((2400,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageOps.autocontrast(c).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 path=root/'crops'/f'{name}.jpg'
 c.save(path,quality=94,subsampling=0)
 records.append(dict(path=str(path),source=source,bbox=bbox,scale=scale,rotation=rot,reason=reason,resize='PIL LANCZOS',autocontrast=True,sharpen='UnsharpMask radius 1.1, percent 120, threshold 3'))
(root/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(root/'inspection_log.md').write_text('''# R1 inspection log — scan 156-4_073

Started UTC: 2026-11-20T12:58:41Z.

Read assignment, complete brief v09, metadata, C.tex, H.tex, CONVENTIONS.md, PREAMBLE.tex, C_context.md and supplied notation snapshot. Combined textual read truncated; C_context and notation snapshot were read separately in full. No OCR, external sources, other reader files or compilation.

## Successful image views, in order

1. Whole `/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan073.jpg`, alone, original orientation. Layout: folio 72; two-line continuation with two corrections; slanted upper-left note; C7₀ statement; parenthetical paragraph; strengthening paragraph; lower cancelled draft, raised phrase, two displays, right diagram and two concluding proof lines. Three long diagonal cancellation strokes in lower draft.
2. Half a `/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan073_a.jpg`, alone, full supplied resolution. Read every visible text/sign once. Upper coordinates coincide with whole.
3. Half b `/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan073_b.jpg`, alone, full supplied resolution. Read every visible text/sign once. Whole-image y = half-b y + 1098.

## Crop plan

Seventeen unresolved local places were identified after the halves. `crop_manifest.json` records exact source rectangles, rotations, enlargement scales and reasons. All were created once by `make_crops.py`; all are 2400 pixels wide, LANCZOS enlarged, autocontrasted and lightly sharpened, JPEG quality 94. No crop was made from another reader’s image. Crop inspections and ink decisions are appended below.
''')
print('Created',len(records),'own crops and initial inspection log.')
