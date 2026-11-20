from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
BASE=Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE=BASE/'assignments/7_scan019/scan.jpg'
DEST=BASE/'deliverables/crops'
DEST.mkdir(parents=True,exist_ok=True)
CROPS={
 '7_scan019_L740_tests_decisifs.jpg':(250,35,1665,495),
 '7_scan019_L740_concluding_paragraph.jpg':(280,535,1665,1155),
}
with Image.open(SOURCE) as source:
    print('Source dimensions:',source.size)
    for name,box in CROPS.items():
        crop=ImageOps.autocontrast(source.crop(box).convert('RGB'),cutoff=0.5)
        crop=ImageEnhance.Contrast(crop).enhance(1.6)
        crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
        crop.save(DEST/name,quality=96)
        print(name,box,crop.size)
