from PIL import Image,ImageOps
from pathlib import Path
im=Image.open('source/SP65_C13_16_scans/16_scan038.jpg')
boxes={'firstP':(1025,165,1245,250),'kernel_old':(850,340,1010,455),'parent_old':(1190,515,1395,590),'lambda_range':(1170,730,1310,810),'injectivity':(920,800,1645,900),'kernel_bounds':(265,935,1035,1045),'conjunction':(1170,910,1350,988),'rest_bound':(1160,1100,1330,1170),'cancel_block':(280,1230,1650,1720),'final_sum':(1230,1740,1540,1865),'final_cancel':(865,1890,1145,1980)}
for name,box in boxes.items():
 out=Path('views')/('038_'+name+'.png'); assert not out.exists()
 c=ImageOps.autocontrast(im.crop(box));w=2600 if c.width>500 else 1400;c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS).save(out)
print(boxes)
