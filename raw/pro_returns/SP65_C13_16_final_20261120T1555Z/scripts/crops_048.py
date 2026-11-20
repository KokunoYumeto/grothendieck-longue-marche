from PIL import Image,ImageOps,ImageEnhance,ImageFilter
from pathlib import Path
r=Path(__file__).resolve().parents[2];im=Image.open(r/'source/SP65_C13_16_scans/16_scan048.jpg')
boxes={'motive':(1055,515,1170,570),'subscript':(770,650,850,725),'coefficients':(210,1145,480,1205),'v_degree_article':(665,1645,900,1720),'formula':(1170,1780,1682,1875)}
for name,box in boxes.items():
 t=r/f'views/048_{name}.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));
 if name=='coefficients':a=ImageEnhance.Contrast(a).enhance(1.7).filter(ImageFilter.UnsharpMask(radius=1,percent=150,threshold=2))
 w=2500 if a.width>450 else 1800;a.resize((w,round(a.height*w/a.width)),Image.Resampling.LANCZOS).save(t)
print(boxes)
