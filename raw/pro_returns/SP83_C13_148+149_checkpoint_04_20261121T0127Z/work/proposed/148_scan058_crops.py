from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan058'
boxes={
'folio14':[780,35,861,96],
'opening_de':[890,143,1005,229],
'liees':[1442,472,1655,609],
'fois_ci':[591,613,1007,713],
'quotes':[527,717,1454,938],
'marquage_cancel':[389,1249,1249,1425],
'anodine_enC':[929,1438,1374,1624],
'replacement':[379,1587,1635,1832],
'qui_choses':[900,1714,1604,1842],
'finite_close':[1302,1808,1642,1954],
'enplus':[335,1937,628,2074],
'reverse':[620,1928,1145,2071],
'aide_du':[1155,1907,1569,2041],
'produit':[325,2046,1134,2187],
'marque_comma':[714,2136,1052,2302],
'folio57':[35,2269,121,2344]
}
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan058.jpg').convert('RGB')
for name,box in boxes.items():
 out=ImageOps.autocontrast(im.crop(box));factor=max(3,min(8,3000/out.width));out=out.resize((round(out.width*factor),round(out.height*factor)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,105,3));out.save(root/'result/crops'/f'{page}_{name}.png')
(root/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(json.dumps(boxes))
