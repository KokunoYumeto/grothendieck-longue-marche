from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan065'
boxes={
'quoted_modele':(1188,88,1450,177),
'first_formula':(288,197,435,310),
'parenthesis_cordes':(235,280,842,450),
'la':(1412,530,1518,614),
'foulee_avec':(288,675,691,813),
'model_clause_insertion_pi':(695,633,1635,886),
'second_formula':(492,794,767,913),
'lower_number':(44,2250,132,2322)
}
im=Image.open(root/f'source/SP83_C13_148+149_scans/{page}.jpg')
for name,box in boxes.items():
 out=ImageOps.autocontrast(im.crop(box))
 width=2800 if out.width>700 else 2200
 if name=='lower_number':width=1000
 out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
 out.save(root/f'result/crops/{page}_{name}.png')
(root/f'proposed/{page}_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(f'Created {len(boxes)} first-reading crops.')
