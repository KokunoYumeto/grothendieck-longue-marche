from pathlib import Path
from PIL import Image,ImageOps
import json
root=Path('/workspace/scratch/98070f078628')
out=root/'SP116_CW_75_work/readers/scan011'
out.mkdir(parents=True,exist_ok=True)
crops=root/'SP116_CW_75_work/crops'
boxes={
'heading':[307,59,1170,136],
'struck_attempt':[292,142,877,254],
'diagram_one':[350,257,1336,399],
'splitting':[627,428,1436,513],
'conditions':[624,552,995,696],
'avaient':[423,814,558,875],
'relation_formula':[681,899,1658,980],
'verify_formula':[687,1079,1325,1220],
'or':[346,1204,669,1252],
'deleted_one':[525,1252,1253,1311],
'deleted_two':[547,1321,989,1382],
'live_prelim':[576,1371,1515,1446],
'live_final':[610,1438,1613,1518],
'Itou':[103,1425,609,1616],
'example':[353,1575,1313,1720],
'NB':[1356,1627,1664,1753],
'deleted_Gamma':[494,1711,598,1757],
'aff_rows':[430,1763,1038,1978],
'half_product':[973,1771,1444,1840],
'dihedral':[1158,1888,1600,2049],
'n_ge_3':[1505,2064,1653,2116],
'family':[862,2113,1223,2177],
'insert_deleted':[1242,2094,1648,2174],
'autre':[320,2210,466,2257],
'diagram_two':[502,2211,1240,2346],
'archive_10':[42,2269,119,2337]
}
im=Image.open(root/'source/SP116_CW_75_scans/J75-02_75_scan011.jpg')
for key,b in boxes.items():
    x=ImageOps.autocontrast(im.crop(tuple(b)).convert('RGB'))
    if key in ['deleted_one','deleted_two','live_prelim','live_final']: x=x.rotate(-2,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
    target=3000 if key in ['struck_attempt','diagram_one','relation_formula','verify_formula','deleted_one','live_prelim','live_final','example','aff_rows','insert_deleted','diagram_two'] else 2200
    w,h=x.size
    x=x.resize((round(w*target/max(w,h)),round(h*target/max(w,h))),Image.Resampling.LANCZOS)
    x.save(crops/f'scan011_{key}.jpg',quality=94)
(out/'crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(f'{len(boxes)} crops created; no recognition performed.')
