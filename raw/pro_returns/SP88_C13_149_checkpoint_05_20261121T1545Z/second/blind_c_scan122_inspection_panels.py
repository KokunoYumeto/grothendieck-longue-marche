from PIL import Image
from pathlib import Path
import json
root=Path('/workspace/scratch/0cab6a548abb')
records=[]
for box in ['b01','b02']:
    p=root/f'edition/crops/149_scan122_second_{box}.png'
    im=Image.open(p);mid=im.width//2
    panel=Image.new(im.mode,(im.width-mid,2*im.height+40),'white')
    panel.paste(im.crop((0,0,mid,im.height)),(0,0))
    panel.paste(im.crop((mid,0,im.width,im.height)),(0,im.height+40))
    q=root/f'edition/crops/149_scan122_second_{box}_halves.png';panel.save(q)
    records.append({'box':box,'file':str(q),'derived_from':str(p),'layout':'left half above right half with 40px gap; no overlap','split_x_pixels':mid,'rotation_degrees':0})
p=root/'edition/crops/149_scan122_second_b03.png'
im=Image.open(p)
q=root/'edition/crops/149_scan122_second_b03_overview.png'
im.resize((1650,1795),Image.Resampling.LANCZOS).save(q)
records.append({'box':'b03','file':str(q),'derived_from':str(p),'layout':'complete saved crop reduced to 1650x1795 for overview','rotation_degrees':0})
for row,y0 in enumerate([0,900,1800,2700,3600,4500],1):
    y1=min(y0+1000,im.height)
    for col,(x0,x1) in enumerate([(0,2550),(2400,4950)],1):
        q=root/f'edition/crops/149_scan122_second_b03_tile_{row}_{col}.png'
        im.crop((x0,y0,x1,y1)).save(q)
        records.append({'box':'b03','file':str(q),'derived_from':str(p),'layout':'detail tile; 150px horizontal and 100px vertical overlaps','derivative_pixel_bbox':[x0,y0,x1,y1],'rotation_degrees':0})
(root/'edition/second/blind_c_scan122_inspection_records.json').write_text(json.dumps(records,indent=2),encoding='utf8')
print('Created',len(records),'inspection panels.')
