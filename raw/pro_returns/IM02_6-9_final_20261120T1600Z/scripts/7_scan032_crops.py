from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
BASE=Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE=BASE/'assignments/7_scan032/scan.jpg'
DEST=BASE/'deliverables/crops'
DEST.mkdir(parents=True,exist_ok=True)
CROPS={
 '7_scan032_L736_handwritten_upper.jpg':(10,85,1665,650),
 '7_scan032_L735_cohomology_functor.jpg':(220,635,1665,1335),
 '7_scan032_L735_serre_and_coefficients.jpg':(220,1295,1665,2090),
}
with Image.open(SOURCE) as source:
    print('Source dimensions:',source.size)
    for name,box in CROPS.items():
        crop=ImageOps.autocontrast(source.crop(box).convert('RGB'),cutoff=0.5)
        crop=ImageEnhance.Contrast(crop).enhance(1.55)
        crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
        crop.save(DEST/name,quality=96)
        print(name,box,crop.size)
