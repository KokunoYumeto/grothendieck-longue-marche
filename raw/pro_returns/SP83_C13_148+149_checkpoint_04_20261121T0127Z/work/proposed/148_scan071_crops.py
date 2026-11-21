from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops
import json
base=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan071'
im=Image.open(base/'source/SP83_C13_148+149_scans/148_scan071.jpg').convert('RGB')
boxes={
 'heading':(175,55,920,140),
 'first_heading':(172,140,1650,255),
 'isomorphismes_end':(1360,398,1678,468),
 'first_case':(438,444,1670,556),
 'variants':(228,494,1618,646),
 'signature_functor':(638,762,1548,954),
 'fibre':(330,958,1380,1050),
 'isolated_mark':(1125,1057,1188,1105),
 'triple_definition':(305,1094,1596,1338),
 'homeom_tail':(1125,1325,1625,1420),
 'notation_old_d':(700,1414,1616,1524),
 'definition_words':(330,1505,1605,1745),
 'nb':(460,1668,1625,1950),
 'third':(300,1946,1580,2155),
 'background_drawing':(460,1035,1470,2030),
 'folio':(40,2245,135,2318),
}
widths={'heading':2500,'first_heading':4000,'isomorphismes_end':1900,'first_case':3600,'variants':3600,'signature_functor':3600,'fibre':3300,'isolated_mark':900,'triple_definition':3400,'homeom_tail':2300,'notation_old_d':3000,'definition_words':3600,'nb':3400,'third':3400,'background_drawing':2600,'folio':1100}
views={}
for name,box in boxes.items():
 out=ImageOps.autocontrast(im.crop(box))
 w=widths[name]
 out=out.resize((w,round(out.height*w/out.width)),Image.Resampling.LANCZOS)
 out=out.filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
 p=base/'result/crops'/f'{page}_{name}.png';out.save(p)
 view=p
 if p.stat().st_size>6000000:
  view=base/'transport'/f'{page}_{name}.webp'
  out.save(view,format='WEBP',lossless=True,quality=100,method=4)
  check=Image.open(view).convert('RGB')
  assert out.size==check.size and ImageChops.difference(out,check).getbbox() is None
 views[name]=str(view)
 print(name,p.stat().st_size,view.name,flush=True)
(base/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
(base/'proposed'/f'{page}_view_paths.json').write_text(json.dumps(views,indent=2)+'\n')
print('16 canonical crops complete',flush=True)
