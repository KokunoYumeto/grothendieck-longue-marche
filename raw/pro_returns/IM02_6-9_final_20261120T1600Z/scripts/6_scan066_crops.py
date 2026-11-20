from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
BASE=Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE=BASE/'assignments/6_scan066/scan.jpg'
DEST=BASE/'deliverables/crops'
DEST.mkdir(parents=True,exist_ok=True)
CROPS={
 '6_scan066_L717_lemma_context.jpg':(170,35,1585,220),
 '6_scan066_L717_deleted_inserted.jpg':(935,110,1280,210),
}
with Image.open(SOURCE) as source:
    print('Source dimensions:',source.size)
    for name,box in CROPS.items():
        crop=ImageOps.autocontrast(source.crop(box).convert('RGB'),cutoff=0.5)
        crop=ImageEnhance.Contrast(crop).enhance(1.45)
        crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
        crop.save(DEST/name,quality=96)
        print(name,box,crop.size)
