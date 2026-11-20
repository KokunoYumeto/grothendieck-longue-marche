from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
im=Image.open('source/SP60_CW_71_scans/J71-06_71_scan048.jpg')
boxes={
 'toutes':((130,61,239,120),0,2400),
 'so_dot':((297,70,377,115),0,2200),
 'first_A':((147,149,197,201),0,2200),
 'bien':((1427,247,1513,296),0,2200),
 'second_A':((620,356,677,411),0,2200),
 'recurrence':((1199,336,1368,397),0,2600),
 'focon':((1384,332,1485,394),0,2400),
 'b_lambda':((852,668,907,737),0,2200),
 'inserted_end':((976,876,1630,984),0,3600),
 'existe':((981,1235,1073,1293),0,2400),
 'exterieur':((772,1320,950,1395),0,2600),
 'numero':((206,1422,350,1485),0,2600),
 'faux_margin':((15,1390,173,1745),-46,3200),
 'co':((278,1590,324,1647),0,2200),
 'precedent':((1257,1532,1437,1605),0,2600),
 'trian':((953,1632,1062,1693),0,2400),
 'corespondent':((367,1737,645,1809),0,2800),
 'douteux':((17,1852,180,1980),-31,2600),
 'Le':((151,1931,240,1999),0,2200),
 'montent':((1136,1957,1307,2020),0,2600),
 'juillet':((1114,2070,1250,2155),0,2600),
 'signature':((1166,2140,1366,2240),0,3000)}
for name,(b,rot,w) in boxes.items():
 c=im.crop(b)
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c=c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS)
 c=ImageOps.autocontrast(c).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 c.save(Path('work_crops')/f'048_{name}.png')
print(im.size,len(boxes),'crops')
