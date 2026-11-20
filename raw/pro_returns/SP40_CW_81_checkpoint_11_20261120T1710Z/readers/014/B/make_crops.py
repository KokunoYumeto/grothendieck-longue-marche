from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan014.jpg')
out=Path('/workspace/scratch/94548b74fbe0/out/readers/014/B')
im=Image.open(source)
crops=[
 ('01_first_word.png',(860,83,1292,195),3000),
 ('02_second_line.png',(925,180,1565,305),3200),
 ('03_insertion_guide.png',(1138,28,1515,175),3000),
]
for name,bbox,width in crops:
 c=im.crop(bbox)
 c=ImageOps.autocontrast(c)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.1,percent=110,threshold=3))
 c.save(out/name)
 print(name, bbox, c.size)
