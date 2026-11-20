from pathlib import Path
from PIL import Image,ImageEnhance
import json
src='SP02_CW_10+12_scans/B10-09_10_scan128.jpg'; im=Image.open(Path('source')/src)
items=[('comoduleclose',[665,298,752,369],0,26),('arrowclose',[735,373,810,422],0,28),('cancelAsub',[970,323,1020,368],0,30),('marginSub',[204,705,243,748],0,32),('bottomwide',[20,1905,365,2139],-22,9),('formclose',[943,1967,1048,2018],-2,25),('projo1',[579,1800,608,1844],0,32),('projo2',[604,1800,632,1844],0,32)]
rs=[]
for name,box,rot,scale in items:
 assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height,(name,box)
 rs.append(dict(id=name,source=src,box=box,rotation=rot,scale=scale))
 c=im.crop(box).resize(((box[2]-box[0])*scale,(box[3]-box[1])*scale))
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c.save('work/crops/10-128-'+name+'.png')
old=json.loads(Path('work/crops128.json').read_text());ids={x['id'] for x in rs}
Path('work/crops128.json').write_text(json.dumps([x for x in old if x['id'] not in ids]+rs,ensure_ascii=False,indent=2)+'\n')
print(len(rs),'new recipes, not yet seen')
