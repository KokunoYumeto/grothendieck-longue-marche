from pathlib import Path
from PIL import Image
import json
src='SP02_CW_10+12_scans/B10-09_10_scan130.jpg'
im=Image.open(Path('source')/src)
items=[('margin_rot',[1131,1161,1656,1266],2,10),('mono_initial',[1021,298,1054,339],0,30),('cat_initial',[1599,868,1631,911],0,30),('firstg',[1152,1354,1199,1409],0,26),('inlineaster1',[678,1340,761,1405],0,24),('inlineaster2',[520,1410,600,1473],0,24),('two_header',[256,278,309,328],0,24),('p2_close',[1256,1833,1305,1875],0,28),('bottom1',[49,2003,549,2081],1,10),('bottom2',[539,2017,1068,2095],1,10),('bottom3',[1060,2039,1651,2113],1,10),('bottom4',[236,2072,815,2129],-1,10),('bottom5',[795,2077,1105,2135],-1,12),('bottom6',[1080,2076,1548,2136],-1,12)]
rs=json.loads(Path('work/crops130.json').read_text())
for name,b,rot,s in items:
 assert 0<=b[0]<b[2]<=im.width and 0<=b[1]<b[3]<=im.height,(name,b,im.size)
 rs.append(dict(id=name,source=src,box=b,rotation=rot,scale=s))
 c=im.crop(b).resize(((b[2]-b[0])*s,(b[3]-b[1])*s))
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c.save('work/crops/10-130-'+name+'.png')
 c.thumbnail((2200,1200));c.save('work/view130/10-130-'+name+'.png')
Path('work/crops130.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n')
print(len(rs),'recipes; 14 newly generated crops remain unviewed')
