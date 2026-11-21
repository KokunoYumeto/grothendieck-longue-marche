from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import json

root=Path('/workspace/scratch/8759b8008681')
page='150_scan017'
boxes={
 'P00':[232,60,991,163],
 'P01':[590,266,988,497],
 'P02':[262,497,1498,613],
 'P03':[1022,817,1366,926],
 'P04':[735,1018,1060,1113],
 'P05':[753,1096,1305,1222],
 'P06':[440,1150,1290,1330],
 'P07':[574,1341,1509,1447],
 'P08':[276,1599,1264,1728],
 'P09':[20,1238,332,1479],
 'P10':[18,1578,628,2117],
 'P11':[1417,1688,1681,1839],
 'P12':[263,1834,1359,1959],
 'P13':[268,1915,1651,2048],
 'P14':[276,2010,780,2159],
 'P15':[768,1994,1660,2099],
 'P16':[774,2075,1681,2177],
 'P17':[263,2162,1645,2336],
 'P18':[22,2293,70,2345]
}
rotations={'P09':-40,'P10':-43}
original=Image.open(root/'source/SP89_C13_149+150_scans'/f'{page}.jpg')
for id,box in boxes.items():
    im=ImageOps.autocontrast(original.crop(box).convert('L'))
    if id in rotations:
        im=im.rotate(rotations[id],Image.Resampling.BICUBIC,expand=True,fillcolor=255)
    width=1800 if id=='P18' else 3000
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    im=ImageEnhance.Sharpness(im).enhance(1.12)
    im.save(root/'work/crops'/f'{page}_{id}.png')
out=root/'work/reports'/page
(out/'crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
(out/'crop_rotations.json').write_text(json.dumps(rotations,indent=2)+'\n')
print(f'{len(boxes)} crops saved; original {original.size}; half2 offset y1063.')
