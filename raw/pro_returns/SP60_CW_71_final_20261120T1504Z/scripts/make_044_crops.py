from PIL import Image,ImageOps,ImageFilter
im=Image.open('source/SP60_CW_71_scans/J71-06_71_scan044.jpg')
boxes={'def1':(585,572,770,668),'def2':(1150,941,1357,1027),'XIV':(760,1010,868,1097),'s_pour':(704,1115,816,1190),'conjonction':(236,1310,422,1400),'J':(1271,1460,1322,1547),'s_card':(772,1592,826,1670),'Posons':(196,1850,307,1928),'egale':(632,1845,740,1934),'deux':(805,1851,880,1926),'larc':(874,2002,984,2077),'f_obtenu':(1464,1970,1620,2057),'recollement':(1090,2082,1325,2161)}
for n,b in boxes.items():
 c=ImageOps.autocontrast(im.crop(b));c=c.resize((2400,round(c.height*2400/c.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3));c.save('work_crops/044_'+n+'.png')
print(boxes)
