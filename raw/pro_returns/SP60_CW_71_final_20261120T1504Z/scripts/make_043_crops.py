from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
im=Image.open('source/SP60_CW_71_scans/J71-06_71_scan043.jpg')
boxes={'y':(1180,170,1315,252),'existe':(1140,245,1280,324),'fai':(1385,325,1520,402),'A_subscripts':(1280,395,1425,490),'black_cancel':(716,515,805,608),'v_y':(1190,520,1310,603),'arrow':(1285,1045,1374,1125),'dee':(305,1225,407,1310),'U_formula':(908,1360,1640,1460),'x_member':(581,1887,686,1976),'deleted_z':(574,2020,724,2110),'q_clair':(1225,2030,1287,2114),'quen':(1368,2030,1500,2110),'zz_zy':(579,2132,710,2222),'final_punct':(1568,2260,1650,2351),'cqsd':(1436,2295,1600,2356),'x_dot':(671,1631,742,1725)}
for n,b in boxes.items():
 c=ImageOps.autocontrast(im.crop(b));c=c.resize((2400,round(c.height*2400/c.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3));c.save('work_crops/043_'+n+'.png')
print(boxes)
