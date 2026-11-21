from PIL import Image
from pathlib import Path
root=Path('/workspace/scratch/0cab6a548abb/edition/crops')
for box in ('b13','b17'):
    im=Image.open(root/f'149_scan107_second_{box}.png')
    mid=(im.width+1)//2
    out=Image.new(im.mode,(mid,2*im.height+40),'white')
    out.paste(im.crop((0,0,mid,im.height)),(0,0))
    out.paste(im.crop((mid,0,im.width,im.height)),(0,im.height+40))
    out.save(root/f'149_scan107_second_{box}_inspect_panels.png')
print('Two inspection layouts saved from already-created crops.')
