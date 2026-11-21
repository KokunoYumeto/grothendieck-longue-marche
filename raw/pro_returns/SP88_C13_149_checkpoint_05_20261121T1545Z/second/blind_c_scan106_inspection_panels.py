from pathlib import Path
from PIL import Image
root=Path('/workspace/scratch/0cab6a548abb/edition/crops')
for box in ('b04','b05','b06','b07','b13'):
    path=root/f'149_scan106_second_{box}.png'
    im=Image.open(path)
    mid=(im.width+1)//2
    out=Image.new(im.mode,(mid,im.height*2+40),'white')
    out.paste(im.crop((0,0,mid,im.height)),(0,0))
    out.paste(im.crop((mid,0,im.width,im.height)),(0,im.height+40))
    out.save(root/f'149_scan106_second_{box}_inspect_panels.png')
print('Created five inspection layouts from existing crops; no source was recropped.')
