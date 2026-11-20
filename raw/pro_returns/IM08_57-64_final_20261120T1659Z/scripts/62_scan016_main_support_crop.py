from pathlib import Path
from PIL import Image, ImageEnhance
b=Path(__file__).resolve().parents[1]
im=Image.open(b/'source/IM08_57-64_scans/62_scan017.jpg');w,h=im.size
box=(int(w*.21),int(h*.933),int(w*.94),int(h*.99))
c=ImageEnhance.Contrast(im.crop(box)).enhance(1.45)
c.resize((3800,round(c.height*3800/c.width)),Image.Resampling.LANCZOS).save(b/'crops/62_scan016_L798_scan017_question.png')
