from PIL import Image
from pathlib import Path
root=Path('/workspace/scratch/0cab6a548abb/edition/crops')
def stack_halves(im):
    mid=(im.width+1)//2
    out=Image.new(im.mode,(mid,im.height*2+40),'white')
    out.paste(im.crop((0,0,mid,im.height)),(0,0))
    out.paste(im.crop((mid,0,im.width,im.height)),(0,im.height+40))
    return out
for box in ('b04','b05','b09','b10','b11','b12'):
    im=Image.open(root/f'149_scan113_second_{box}.png')
    stack_halves(im).save(root/f'149_scan113_second_{box}_inspect_panels.png')
im=Image.open(root/'149_scan113_second_b08.png')
print('b08 dimensions:',im.size)
for i,(y0,y1) in enumerate(((0,430),(390,830),(800,1250),(1230,1614)),1):
    stack_halves(im.crop((0,y0,im.width,y1))).save(root/f'149_scan113_second_b08_inspect_line{i}.png')
