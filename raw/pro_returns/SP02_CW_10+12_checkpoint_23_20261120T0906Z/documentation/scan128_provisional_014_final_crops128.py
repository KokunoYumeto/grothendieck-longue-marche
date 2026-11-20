from pathlib import Path
from PIL import Image
import json
src='SP02_CW_10+12_scans/B10-09_10_scan128.jpg';im=Image.open(Path('source')/src)
items=[('arrowfull',[705,375,766,431],0,28),('cancelAfull',[933,299,1071,378],0,22),('formcontext',[930,1906,1075,2020],0,14),('bottomletters',[91,1985,313,2136],-22,18)]
rs=[]
for name,box,rot,scale in items:
 assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
 rs.append(dict(id=name,source=src,box=box,rotation=rot,scale=scale))
 c=im.crop(box).resize(((box[2]-box[0])*scale,(box[3]-box[1])*scale))
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c.save('work/crops/10-128-'+name+'.png')
a=json.loads(Path('work/crops128.json').read_text());ids={x['id'] for x in rs}
Path('work/crops128.json').write_text(json.dumps([x for x in a if x['id'] not in ids]+rs,ensure_ascii=False,indent=2)+'\n')
print(len(rs),'new crops, not yet viewed')
