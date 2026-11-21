from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan063'
boxes={
'opening_est_donc':(1090,125,1650,223),
'graph_old_colon':(995,242,1601,361),
'repere_replacement':(263,354,866,471),
'groupoide':(266,518,551,617),
'plus_avec':(1007,469,1262,576),
'foncteurs':(843,579,1484,736),
'margin_nb':(20,455,407,856),
'auto_comma':(270,1046,904,1168),
'same_temps':(1168,1103,1608,1191),
'same_facon':(268,1231,1039,1349),
'first_groupoid':(1266,1174,1459,1284),
'second_connus':(280,1340,917,1471),
'bouchage':(953,1289,1576,1394),
'pourrait':(272,1410,952,1564),
'cas_operations':(1270,1362,1655,1488),
'analogs_deleted':(265,1571,806,1677),
'structures_deleted':(693,1679,1223,1829),
'elementaires_diminution':(267,1687,1643,1975),
'lower_diagram':(414,1832,1375,2046),
'right_note':(1412,1817,1667,2220),
'footer_annotation':(701,2013,1250,2318),
'lower_number':(43,2268,129,2340)
}
im=Image.open(root/f'source/SP83_C13_148+149_scans/{page}.jpg')
for name,box in boxes.items():
    out=ImageOps.autocontrast(im.crop(box))
    if name=='margin_nb':
        out=out.rotate(-32,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    width=2600 if out.width>700 else 2100
    if name=='right_note':width=1000
    if name=='lower_number':width=1000
    out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
    out.save(root/f'result/crops/{page}_{name}.png')
(root/f'proposed/{page}_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(f'Created {len(boxes)} first-reading crops; source boxes and generator retained.')
