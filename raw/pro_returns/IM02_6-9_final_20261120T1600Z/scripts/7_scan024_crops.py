from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
BASE=Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE=BASE/'assignments/7_scan024/scan.jpg'
DEST=BASE/'deliverables/crops'
DEST.mkdir(parents=True,exist_ok=True)
CROPS={
 '7_scan024_L723_example_context.jpg':(220,915,1665,1485),
 '7_scan024_L723_inserted_example.jpg':(455,1115,1665,1245),
 '7_scan024_L723_cancelled_qualification.jpg':(240,1205,1235,1320),
}
with Image.open(SOURCE) as source:
    print('Source dimensions:',source.size)
    for name,box in CROPS.items():
        crop=ImageOps.autocontrast(source.crop(box).convert('RGB'),cutoff=0.5)
        crop=ImageEnhance.Contrast(crop).enhance(1.55)
        crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
        crop.save(DEST/name,quality=96)
        print(name,box,crop.size)
