from PIL import Image,ImageOps,ImageFilter
im=Image.open('source/SP60_CW_71_scans/J71-06_71_scan044.jpg')
b=(1465,2150,1648,2256)
c=ImageOps.autocontrast(im.crop(b));c=c.resize((2300,round(c.height*2300/c.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3));c.save('work_crops/044_audit_autrement.png')
print(b)
