from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
im=Image.open('source/SP60_CW_71_scans/J71-06_71_scan047.jpg')
boxes={'annotation':((820,378,1650,485),-3,3600),'telque':((28,743,220,861),-35,2600),'example':((817,895,973,954),0,2400),'faux':((39,1277,147,1394),-30,2400),'notsubset':((1191,1235,1252,1314),0,2200),'bracket':((225,1363,273,1431),0,2200),'interieur_middle':((1214,1335,1430,1407),0,2600),'lambda_point':((1276,1401,1363,1481),0,2400),'black_token':((626,1538,673,1593),0,2200),'mais':((1248,1716,1345,1770),0,2200),'so_what':((22,1945,153,2052),-32,2400),'interieur_final':((548,2073,779,2153),0,2600)}
for name,(b,rot,w) in boxes.items():
 c=im.crop(b)
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c=c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS);c=ImageOps.autocontrast(c).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3));c.save(Path('work_crops')/f'047_{name}.png')
print(im.size,boxes)
