from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
base=Path('/workspace/scratch/94548b74fbe0/out/readers/004/B')
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan004.jpg')
items=[
('01_top_eta_brace.png',(690,205,997,348),0,'First descended Greek letter and mark after d-1'),
('02_xf_relation.png',(145,947,780,1064),0,'Equals or equivalence beneath box, with complete local line'),
('03_struck_xf.png',(155,1055,282,1177),0,'Locally struck fragment beneath xf1 line'),
('04_expansion_factors.png',(328,1103,902,1241),0,'Independent first-factor indices in left expansion'),
('05_expansion_annotations.png',(490,1212,1251,1447),0,'Expansion terms, local cancellations, and lower annotations'),
('06_upside_down_note.png',(444,1414,1117,1739),180,'Complete upside-down note, all three lines and range'),
('07_struck_delta_end.png',(67,1579,376,1728),0,'Final character of locally cancelled delta formula'),
('08_upper_cancelled_coefficient.png',(1572,421,1830,523),0,'Locally cancelled character before eta in right first case'),
('09_upper_second_coefficient.png',(1926,500,2164,610),0,'Sign between 1 and alpha in right second case'),
('10_underlined_struck_factor.png',(1354,667,1643,813),0,'Locally cancelled factor after f1e1'),
('11_lower_cancelled_lead.png',(1516,851,1764,961),0,'Cancelled material immediately after lower left-hand member equals'),
('12_lower_second_case.png',(1710,921,2050,1021),0,'Eta subscript sign, following factor, and local crossed term'),
('13_lower_struck_tail.png',(1608,1036,2168,1153),0,'Crossed expansion after ei(f1e1), including final tall symbol'),
('14_bottom_initials.png',(2020,1453,2342,1598),0,'Three small initials after signed delta result'),
('15_box_detached_ticks.png',(1027,754,1111,860),0,'Detached two tiny marks inside right edge of left box')
]
out=[]
for name, box, rot, purpose in items:
 c=im.crop(box)
 if rot: c=c.rotate(rot,expand=True)
 c=ImageOps.autocontrast(c,cutoff=.3)
 target=2600 if c.width>350 else 1900
 c=c.resize((target,round(c.height*target/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
 c.save(base/name)
 out.append({'path':name,'bbox':list(box),'rotation':rot,'purpose':purpose})
(base/'crop_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(out),'one-pass local crops.')
