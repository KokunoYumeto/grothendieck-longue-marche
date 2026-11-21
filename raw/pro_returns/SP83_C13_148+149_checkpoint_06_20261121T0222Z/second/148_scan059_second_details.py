"""Retained generator for the three same-box display details already viewed."""
from pathlib import Path
from PIL import Image
BASE=Path('/workspace/scratch/f28c4f52d3ec')
for bid,name,bounds in [('B10','right',[1980,0,3000,306]),
                        ('B10','left',[0,0,1200,306]),
                        ('B11','formula',[700,0,1650,279])]:
    im=Image.open(BASE/'result/crops'/f'148_scan059_second_{bid}.png')
    bounds[3]=min(bounds[3],im.height)
    det=im.crop(tuple(bounds))
    det=det.resize((det.width*2,det.height*2),Image.Resampling.LANCZOS)
    det.save(BASE/'result/second'/f'148_scan059_second_{bid}_{name}_detail.png')
