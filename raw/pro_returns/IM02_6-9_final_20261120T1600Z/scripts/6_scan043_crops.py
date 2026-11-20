from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/6_scan043/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("6_scan043_L711_matrix.jpg", (265, 1740, 440, 1920), 2600),
    ("6_scan043_L718_relations_question.jpg", (180, 905, 1010, 1065), 2800),
    ("6_scan043_L718_group.jpg", (215, 1490, 1630, 1925), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
