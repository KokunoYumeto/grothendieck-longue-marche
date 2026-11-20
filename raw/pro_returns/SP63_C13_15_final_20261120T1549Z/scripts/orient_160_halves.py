"""Orient the already-created native halves; no second half-crop is made."""
from pathlib import Path
from PIL import Image
p=Path(__file__).resolve().parents[2]/'views'
a=Image.open(p/'160_top.png').copy().rotate(180)
b=Image.open(p/'160_bottom.png').copy().rotate(180)
b.save(p/'160_top.png');a.save(p/'160_bottom.png')
