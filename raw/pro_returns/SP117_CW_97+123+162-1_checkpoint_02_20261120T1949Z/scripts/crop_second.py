"""Create the neutral crops for a blind reader after all first passes finish.

Run by the blind reader. No witness or first reading is read by this script.
"""
from pathlib import Path
import csv
import sys
from PIL import Image, ImageOps, ImageFilter

packet = Path(sys.argv[1]).resolve()
destination = Path(sys.argv[2]).resolve()
destination.mkdir(parents=True, exist_ok=True)
image = Image.open(packet / "image.jpg")
with (packet / "boxes.tsv").open(newline="") as stream:
    boxes = list(csv.DictReader(stream, delimiter="\t"))
for box in boxes:
    bounds = tuple(int(box[key]) for key in ("x0", "y0", "x1", "y1"))
    crop = ImageOps.autocontrast(image.crop(bounds))
    ratio = 2500 / max(crop.size)
    crop = crop.resize(tuple(max(1, round(value * ratio)) for value in crop.size), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.0, percent=110, threshold=3))
    crop.save(destination / f"{box['box']}.png")
print(f"Saved {len(boxes)} neutral image crops to {destination}")
