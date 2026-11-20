from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
source=Image.open(root/'source/SP74_C13_143+145_scans/143_scan028.jpg')
boxes={
 'bound-three':[1043,188,1250,274],
 'topos-type':[238,323,531,411],
 'first-correction':[827,272,1576,407],
 'punctured-line':[807,505,1587,597],
 'en-tant':[1295,739,1645,846],
 'interval-indices':[949,1005,1142,1109],
 'interlinear-du':[622,1138,1508,1328],
 'final-topos-index':[299,1462,531,1578]
}
for name,box in boxes.items():
 img=ImageOps.autocontrast(source.crop(box))
 width=3000
 img=img.resize((width,round(img.height*width/img.width)),Image.Resampling.LANCZOS)
 img=img.filter(ImageFilter.UnsharpMask(radius=1.6,percent=155,threshold=3))
 img.save(work/'crops'/f'143_scan028_readerC_{name}.png')
print(boxes)
