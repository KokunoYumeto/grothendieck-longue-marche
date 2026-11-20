from PIL import Image,ImageEnhance
from pathlib import Path
import json
src='SP02_CW_10+12_scans/B10-09_10_scan124.jpg';im=Image.open(Path('source')/src)
items=[('upper-abbr',[1398,789,1507,828],32,-1),('overlap-note',[1156,802,1308,854],28,-1),('Aexponents',[1490,797,1605,844],30,-1),('longguide',[1093,822,1538,888],12,-1),('Cela-guide',[432,836,744,967],10,0),('impairs-end',[1599,897,1669,950],28,0),('decomp-over',[779,920,843,969],32,0),('resp-over',[1002,987,1053,1033],32,0),('grad-end',[355,1192,387,1246],36,0),('ten-under',[236,1402,290,1473],34,0),('semi-over',[324,1448,378,1493],32,0),('necess-over',[1473,1982,1542,2031],30,0),('ce-wide',[698,708,785,753],24,0),('fets',[784,238,1100,300],18,1),('topguide',[966,269,1600,318],10,1),('suffit-guide',[1239,864,1450,921],18,0)]
rs=json.loads(Path('work/crops124.json').read_text());ids={r['id'] for r in rs}
for ident,box,scale,rot in items:
 if ident not in ids:rs.append(dict(id=ident,source=src,box=box,rotation=rot,scale=scale))
 o=im.crop(box)
 if rot:o=o.rotate(rot,expand=True,fillcolor='white')
 o.resize((o.width*scale,o.height*scale)).save(f'work/crops/10-124-{ident}.png')
Path('work/crops124.json').write_text(json.dumps(rs,indent=2));print(len(rs))
