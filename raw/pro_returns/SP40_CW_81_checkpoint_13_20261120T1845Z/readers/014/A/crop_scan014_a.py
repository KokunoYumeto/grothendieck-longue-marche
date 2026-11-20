from pathlib import Path
from PIL import Image, ImageOps
BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/readers/014/A'
SOURCE=BASE/'source/SP40_CW_81_scans/J81-02_81_scan014.jpg'
CROPS=[
 ('01_first_line.png',(860,30,1560,192),'first C doubt, insertion, n-aires, detached adjacent marks'),
 ('02_second_line.png',(930,182,1570,306),'second C doubt, apostrophe, terminal punctuation and detached mark at left'),
 ('03_mid_right_trace.png',(1400,700,1455,760),'isolated dark trace in upper blank field'),
 ('04_mid_trace.png',(1045,885,1110,945),'isolated dark trace below title'),
 ('05_lower_left_trace.png',(210,1355,275,1420),'isolated dark short trace in lower-left field'),
 ('06_lower_right_pair.png',(1535,1760,1610,1835),'two dark separated spots in lower-right field'),
 ('07_lower_left_faint.png',(205,1865,265,1925),'faint isolated vertical mark in lower-left field'),
 ('08_bottom_right_trace.png',(1675,2250,1730,2308),'isolated mark near lower-right edge'),
 ('09_bottom_middle_trace.png',(710,2395,770,2445),'isolated faint mark near foot'),
]
im=Image.open(SOURCE)
for name,bbox,purpose in CROPS:
 crop=ImageOps.autocontrast(im.crop(bbox))
 w=2800 if name.startswith(('01','02')) else 2000
 crop=crop.resize((w,round(crop.height*w/crop.width)),Image.Resampling.LANCZOS)
 crop.save(OUT/name)
 print(name,bbox,purpose)
