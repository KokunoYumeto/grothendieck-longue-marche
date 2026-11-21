from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan059'
boxes={
'old_traduire':(454,86,666,154),
'groupoid_name':(925,85,1666,203),
'cancelled_groupoid':(228,386,1664,632),
'forgetting':(272,620,1663,833),
'heading':(330,895,1312,1044),
'crucial':(274,1048,738,1170),
'tautologique':(770,1035,1572,1178),
'toutes':(605,1180,1565,1285),
'passons_revue':(272,1300,1589,1406),
'pratiquer':(279,1415,1668,1620),
'partie_old':(421,1620,1080,1712),
'sigma_old':(1184,1750,1560,1857),
'cancel_etles':(277,1718,766,1830),
'b_old_formula':(709,1818,1015,1935),
'toute_orbite':(1044,1818,1515,1942),
'un_isom':(607,1924,1065,2022),
'inverse_lun':(273,2160,891,2249),
'final_isom':(1081,2244,1632,2338),
'lower_number':(37,2267,132,2340)
}
im=Image.open(root/f'source/SP83_C13_148+149_scans/{page}.jpg')
for name,box in boxes.items():
    out=ImageOps.autocontrast(im.crop(box))
    width=2400 if out.width>700 else 2000
    if name=='lower_number':width=1000
    out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS)
    out=out.filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
    out.save(root/f'result/crops/{page}_{name}.png')
(root/f'proposed/{page}_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(f'Created {len(boxes)} crops for {page}.')
