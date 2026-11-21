from PIL import Image
from pathlib import Path
root=Path('/workspace/scratch/0cab6a548abb/edition/crops')
im=Image.open(root/'149_scan109_second_b11_inspect_rotated.png')
print('Rotated dimensions:',im.size)
for name,bbox in [('upper',(700,600,2400,1480)),('lower',(100,1150,2250,1980))]:
    im.crop(bbox).save(root/f'149_scan109_second_b11_inspect_{name}.png')
