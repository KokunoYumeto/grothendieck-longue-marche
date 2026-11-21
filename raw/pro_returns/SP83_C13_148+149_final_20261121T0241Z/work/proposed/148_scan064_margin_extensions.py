from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan064'
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan064.jpg').convert('RGB')
side=root/'proposed'/f'{page}_crop_boxes.json'
records=json.loads(side.read_text())
for name,box in [('margin_middle',[30,1420,510,1740]),('margin_lower',[20,1660,500,1960])]:
    path=root/'result/crops'/f'{page}_{name}.png'
    region=ImageOps.autocontrast(im.crop(box)).rotate(-19,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    scale=max(3,min(8,3000/region.width))
    region=region.resize((round(region.width*scale),round(region.height*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,105,3))
    region.save(path)
    records.append(dict(name=name,path=str(path),crop=f'crops/{path.name}',box=box,rotation=-19,viewed=False,extends='margin',reason='Unresolved marginal words and overlap with main text; targeted first-reading strip.'))
side.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created two targeted unresolved marginal strips; 19 saved crops, 17 distinct places.')
