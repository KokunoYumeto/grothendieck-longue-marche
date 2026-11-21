from pathlib import Path
from PIL import Image
root=Path('/workspace/scratch/0cab6a548abb/edition/crops')
for box in ('b05','b07','b08','b09','b10','b13','b14','b15'):
    im=Image.open(root/f'149_scan109_second_{box}.png')
    mid=(im.width+1)//2
    out=Image.new(im.mode,(mid,im.height*2+40),'white')
    out.paste(im.crop((0,0,mid,im.height)),(0,0))
    out.paste(im.crop((mid,0,im.width,im.height)),(0,im.height+40))
    out.save(root/f'149_scan109_second_{box}_inspect_panels.png')
im=Image.open(root/'149_scan109_second_b11.png')
im.rotate(-40,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white').save(root/'149_scan109_second_b11_inspect_rotated.png')
print('Inspection layouts saved from existing crops; no source recropping.')
