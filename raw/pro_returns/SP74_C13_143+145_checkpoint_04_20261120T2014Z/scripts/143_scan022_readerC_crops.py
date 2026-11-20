from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
src=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan022.jpg')
boxes={
'iso-abbreviation':(917,40,1151,123),
'common-identification':(283,241,912,343),
'ie-abbreviation':(1136,354,1388,474),
'grpes-abbreviation':(266,625,1045,746),
'pi-space':(318,1196,1067,1324),
'autom-abbreviation':(1372,1311,1642,1422),
'inner-automorphisms':(302,1443,680,1563),
'restriction':(1109,1552,1641,1694),
'supposing-abelian':(480,1728,1638,1933),
'family-insertion':(847,1860,1627,2021),
'quotient-label':(631,2014,963,2123),
'donne-ending':(476,2204,805,2304),
'parameter-glyph':(289,130,657,237),
}
for name,box in boxes.items():
 im=ImageOps.autocontrast(src.crop(box).convert('RGB'))
 im=im.resize((3000,round(im.height*3000/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.6,percent=155,threshold=3))
 path=root/'crops'/('143_scan022_readerC_'+name+'.png')
 im.save(path)
 print(name,list(box))
