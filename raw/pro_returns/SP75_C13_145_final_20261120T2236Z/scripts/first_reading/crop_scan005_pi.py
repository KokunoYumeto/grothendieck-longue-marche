from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(root/'packets/145_scan005/page.jpg')
b=[740,2015,890,2100]
im=ImageOps.autocontrast(im.crop(b))
im=im.resize((2400,round(im.height*2400/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=90,threshold=3))
im.save(root/'edition/crops/145_scan005_14_pi_adjacent_marks.png')
print(b)
