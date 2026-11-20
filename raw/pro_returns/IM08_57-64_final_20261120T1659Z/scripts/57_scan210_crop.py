from PIL import Image, ImageEnhance, ImageOps
from pathlib import Path
root = Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im = Image.open(root / 'source/IM08_57-64_scans/57_scan210.jpg')
print(im.size)
crop = im.crop((375, 145, 1480, 255))
crop = ImageEnhance.Contrast(crop).enhance(1.65)
crop.resize((3315, 330), Image.Resampling.LANCZOS).save(root / 'crops/57_scan210_L659_equation.png')
