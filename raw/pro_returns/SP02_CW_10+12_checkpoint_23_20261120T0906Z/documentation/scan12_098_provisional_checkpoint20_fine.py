from PIL import Image
from pathlib import Path
import json
spec=[('cependantcomma','a',(885,166,925,211),28,0),('lesfine','a',(629,651,707,693),30,0),('recentcell','a',(1063,650,1117,694),28,0),('algebleft','a',(1278,1068,1365,1129),28,0),('algebright','a',(1350,1075,1420,1137),28,0),('algebmain','a',(1225,1064,1455,1141),20,0),('econtrol','a',(1078,727,1113,767),30,0),('signalend','b',(599,360,652,411),28,0),('dontcell','b',(1441,569,1476,617),30,0),('adiqleft','b',(646,812,704,870),28,0),('adiqright','b',(691,812,754,870),28,0),('smotifsfirst','b',(939,851,997,912),28,0),('dejacomma','b',(1168,849,1238,911),28,0),('cequifirst','b',(452,926,549,979),28,0),('Dans','b',(628,930,719,979),28,0),('Rhamlow','a',(1626,877,1667,925),30,0),('resacute','b',(603,211,656,251),30,0),('algebearlier','a',(1424,438,1646,488),22,0),('bcontrol','a',(973,369,1042,412),28,0),('Parcell','a',(809,123,852,163),30,0)]
p=Path('work/crops12_098.json');rows=json.loads(p.read_text());old={x['id'] for x in rows}
for ident,half,box,scale,rotation in spec:
 fn=f'B12-01_12_scan098_{half}.jpg';im=Image.open(Path('source/SP02_CW_10+12_scans')/fn).crop(box)
 if rotation: im=im.rotate(rotation,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
 im=im.resize((im.width*scale,im.height*scale),Image.Resampling.LANCZOS);im.save(f'work/crops/12-098-{ident}.png');im.thumbnail((1850,1250));im.save(f'work/view12_098/12-098-{ident}.png')
 if ident not in old:rows.append(dict(id=ident,source=f'SP02_CW_10+12_scans/{fn}',box=list(box),scale=scale,rotation=rotation))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');print({'crops':len(rows)})
