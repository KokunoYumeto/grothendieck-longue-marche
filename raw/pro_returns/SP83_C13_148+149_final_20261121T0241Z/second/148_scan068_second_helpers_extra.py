"""Retained generator for same-box supplemental views used by reader_a.

These derive only from this page's independent canonical second crops.
The canonical crops remain unchanged. No OCR or recognition is performed.
"""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
for box in ['B03','B06']:
    im=Image.open(ROOT/'crops'/f'148_scan068_second_{box}.png')
    im.resize((1200,round(im.height*1200/im.width)),Image.Resampling.LANCZOS).save(ROOT/'crops'/f'148_scan068_second_{box}_overview.png')

im=Image.open(ROOT/'crops/148_scan068_second_B16.png')
for idx,(y0,y1) in enumerate([(0,270),(240,520),(490,770),(740,1016)],1):
    strip=ImageOps.autocontrast(im.crop((0,y0,im.width,min(y1,im.height))).getchannel('R'),cutoff=.1)
    strip=strip.resize((6000,strip.height*2),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=80,threshold=2))
    strip.save(ROOT/'crops'/f'148_scan068_second_B16_strip{idx}.png')

for idx,(x0,x1) in enumerate([(0,1000),(530,1650),(1180,2300),(1830,3000)],1):
    detail=ImageOps.autocontrast(im.crop((x0,0,x1,im.height)).getchannel('R'),cutoff=.1)
    detail.resize((detail.width*2,detail.height*2),Image.Resampling.LANCZOS).save(ROOT/'crops'/f'148_scan068_second_B16_group{idx}.png')

im=Image.open(ROOT/'crops/148_scan068_second_B16_group1.png').convert('RGB')
out=Image.new('RGB',(im.width+100,im.height+70),'white')
out.paste(im,(100,70))
draw=ImageDraw.Draw(out)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',30)
for j in range(20):
    x=100+185+94*j
    draw.text((x-10,15),str(j+1),fill='red',font=font)
    draw.line((x-47,70,x-47,out.height),fill=(220,140,140),width=1)
for j in range(12):
    y=70+100+157*j
    draw.text((15,y-15),str(j+1),fill='red',font=font)
    draw.line((100,y+78,out.width,y+78),fill=(220,140,140),width=1)
out.save(ROOT/'crops/148_scan068_second_B16_grid.png')
out.crop((700,0,2050,920)).save(ROOT/'crops/148_scan068_second_B16_grid_upper.png')
