from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/016/B')
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan016.jpg')
plans=[
('01_first_sigma_verb.png',(810,65,1230,165),'Opening corrected subscript and verb cluster'),
('02_top_right_insertion.png',(1100,84,1685,275),'Connexe ending and both top insertion guides including clipped right wording'),
('03_opening_cancelled_equal.png',(230,268,920,373),'Cancelled c-est, live egal/e and following small sign'),
('04_opening_connective.png',(1050,276,1620,376),'Connective before final opening inclusion and its endpoint punctuation'),
('05_cqfd.png',(225,370,425,530),'Opening concluding abbreviation with complete descenders'),
('06_first_partition_overwrite.png',(499,582,1060,760),'Overwritten E before first partition Sigma, with second-row comparison'),
('07_brace_partition_overwrite.png',(920,866,1225,959),'Overwritten predecessor in central Sigma12'),
('08_definition.png',(615,1031,1225,1146),'Definition label accent, Sigma strokes and endpoint punctuation'),
('09_dans.png',(250,1180,595,1320),'Initial overdrawn D and possible predecessor'),
('10_ouverts_endpoint.png',(1340,1204,1685,1320),'Right-edge ouverts ending and punctuation'),
('11_lower_overwrites.png',(1020,2008,1465,2120),'Both overwritten letters in lower hypothesis'),
('12_conclurait_cancellation.png',(280,2113,1070,2225),'Inserted en conclurait and complete cancelled preceding expression'),
('13_bottom_unions.png',(300,2210,1100,2347),'Two crowded union signs under bar and bottom bracket opening'),
('14_bottom_rhs_closing.png',(1100,2195,1685,2348),'Final closure bars, underbrace label and clipped closing bracket'),
('15_right_pair_marks.png',(1540,1660,1685,1785),'Two detached dark points near right margin'),
('16_dot_above_closure.png',(810,1858,1010,1935),'Detached point above right lower closure'),
('17_dot_below_avec.png',(390,1089,480,1168),'Detached point below and right of avec')
]
im=Image.open(source)
records=[]
for filename,bbox,purpose in plans:
 c=ImageOps.autocontrast(im.crop(bbox))
 width=2600 if bbox[2]-bbox[0]>300 else 1800
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 c.save(root/filename)
 records.append(dict(path=filename,bbox=list(bbox),rotation=0,purpose=purpose,size=list(c.size)))
(root/'crop_plan.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
