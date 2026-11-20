from pathlib import Path
from PIL import Image
import json
src='SP02_CW_10+12_scans/B10-09_10_scan128.jpg';im=Image.open(Path('source')/src)
items=[
('topindices',[244,161,522,228],0,8),('lesB',[1433,161,1564,215],0,16),
('Bsecond',[480,239,530,296],0,20),('Asecond',[868,238,949,296],0,18),
('cinsert',[1176,203,1340,301],0,12),('comodule',[658,299,860,365],0,13),
('cancelA',[934,306,1028,367],0,22),('firstdisplay',[598,374,927,441],0,11),
('firstlabel',[247,380,319,432],0,18),('De',[947,379,1017,425],0,24),
('Utilisant',[248,448,287,497],0,24),('Aaugment',[964,449,1029,496],0,18),
('seconddisplay',[617,521,862,581],0,12),('secondlabel',[248,522,358,580],0,16),
('homunderline',[486,590,1028,641],0,7),('textAprimes',[438,662,1142,714],0,6),
('AL',[875,797,945,854],0,22),('quoteleft',[234,805,289,854],0,20),('quoteright',[1073,801,1136,856],0,20),
('marginNB',[44,538,264,821],0,8),('Cette',[112,579,228,621],0,20),
('marginformula',[138,682,264,747],0,18),('preciser',[33,814,286,912],0,10),
('rightnote',[1123,777,1667,887],0,7),('verticalrule',[181,270,250,1059],0,4),
('delta1',[392,875,441,921],0,24),('tensorX',[1353,873,1507,926],0,15),
('cancelEst',[1503,869,1680,928],0,18),('cancelNext',[251,947,329,992],0,24),
('delparen',[1030,1086,1100,1136],0,22),('cancelL',[803,1155,903,1221],0,22),
('liveL',[917,1154,1136,1221],0,14),('element',[1055,1223,1326,1285],0,12),
('etre',[1156,1281,1639,1348],0,10),('estspace',[1370,1365,1470,1421],0,18),
('ceci',[249,1403,1387,1498],0,7),('delta2',[714,1440,763,1497],0,24),
('si',[1153,1427,1223,1492],0,20),('tensor2',[1365,1435,1408,1491],0,24),
('dxonnee',[1484,1432,1649,1493],0,15),('associatilite',[250,1506,603,1560],0,10),
('phi',[572,1510,609,1562],0,24),('cancelQuand',[1039,1578,1657,1633],0,9),
('verifi',[251,1644,410,1697],0,18),('delta3',[675,1644,721,1699],0,24),
('Cpsi',[1115,1641,1302,1710],0,16),('Projf',[556,1789,765,1850],0,16),
('asso',[1473,1789,1566,1840],0,22),('bracket',[411,1850,464,1930],0,20),
('H',[1235,1845,1287,1911],0,24),('Pinsert',[1351,1897,1447,1980],0,17),
('Hk',[467,1991,533,2064],0,24),('princhom',[807,1961,1258,2046],-2,10),
('bottommargin',[38,1939,284,2134],-22,12),('archive',[25,2074,108,2129],0,20),
('finaledge',[1408,1991,1680,2051],0,10)
]
rs=[]
for name,box,rot,scale in items:
 assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height,(name,im.size,box)
 rs.append(dict(id=name,source=src,box=box,rotation=rot,scale=scale))
 c=im.crop(box).resize(((box[2]-box[0])*scale,(box[3]-box[1])*scale))
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c.save('work/crops/10-128-'+name+'.png')
Path('work/crops128.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n')
print(im.size,len(rs),'recipes, all require root viewing.')
