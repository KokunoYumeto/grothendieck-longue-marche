from PIL import Image, ImageOps, ImageFilter
im=Image.open('source/SP60_CW_71_scans/J71-06_71_scan046.jpg')
b=(1195,2193,1585,2268)
c=im.crop(b).rotate(180,expand=True);c=c.resize((2600,round(c.height*2600/c.width)),Image.Resampling.LANCZOS);c=ImageOps.autocontrast(c).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3));c.save('work_crops/046_note.png')
print(b)
