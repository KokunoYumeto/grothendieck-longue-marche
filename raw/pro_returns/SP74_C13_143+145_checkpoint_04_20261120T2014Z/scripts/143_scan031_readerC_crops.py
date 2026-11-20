from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
source=Image.open(root/'source/SP74_C13_143+145_scans/143_scan031.jpg')
boxes={
 'opening-on-a':[598,290,794,358],
 'first-link':[246,409,367,469],
 'aliases-upper':[640,358,1277,532],
 'aliases-lower':[640,487,1469,639],
 'equivalence-phrase':[667,831,1368,978],
 'first-basepoint':[602,1027,894,1152],
 'first-target':[1004,987,1676,1118],
 'quotient-expression':[721,1150,1656,1302],
 'last-operator':[608,1377,1258,1545],
 'last-x-exponent':[1263,1397,1673,1536],
 'nb-du':[913,1742,1576,1864],
 'nb-deletion':[858,1884,979,1964],
 'nb-equation-punctuation':[993,1833,1463,1968],
 'nb-exception':[498,2073,834,2168],
 'question-expression':[704,2197,1233,2361],
 'question-options':[1241,2191,1518,2361],
 'final-margin':[1263,2256,1677,2362]
}
for name,box in boxes.items():
 img=ImageOps.autocontrast(source.crop(box))
 img=img.resize((3000,round(img.height*3000/img.width)),Image.Resampling.LANCZOS)
 img=img.filter(ImageFilter.UnsharpMask(radius=1.6,percent=155,threshold=3))
 img.save(work/'crops'/f'143_scan031_readerC_{name}.png')
print(boxes)
