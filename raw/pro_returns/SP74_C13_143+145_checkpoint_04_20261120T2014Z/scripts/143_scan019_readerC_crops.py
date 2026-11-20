from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
src = Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan019.jpg')
boxes = {
'beta-formula': (245,195,1335,350),
'pair-where': (1000,340,1615,535),
'pi-identity': (330,475,1050,612),
'upper-extension': (565,737,1240,869),
'section-deletion': (1015,1345,1620,1474),
'lower-extension': (325,1485,1000,1617),
'lower-tuple': (555,1690,1230,1840),
'triple-insertions': (590,1868,1538,2065),
'group-question': (803,2037,1635,2178),
'chi-parenthesis-map': (300,2125,1415,2290),
}
for name, box in boxes.items():
    im = ImageOps.autocontrast(src.crop(box).convert('RGB'))
    im = im.resize((3000,round(im.height*3000/im.width)),Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.6,percent=155,threshold=3))
    path = root/'crops'/('143_scan019_readerC_'+name+'.png')
    im.save(path)
    print(name, list(box))
