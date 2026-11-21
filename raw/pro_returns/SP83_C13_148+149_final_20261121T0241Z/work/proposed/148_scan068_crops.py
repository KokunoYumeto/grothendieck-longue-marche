from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops
import json
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan068'
boxes={
'loop':(1680,115,2015,435),
'small_edges':(2047,109,2522,196),
'chord_circle':(2430,174,2868,535),
'long_edge':(1665,337,2394,657),
'short_edge':(1910,586,2414,874),
'holes':(2410,574,2827,959),
'job_records':(220,934,2880,1143),
'banner_p':(2387,1197,2672,1610),
'banner_r':(2110,1197,2390,1610),
'banner_e':(1830,1197,2105,1610),
'banner_d':(1553,1197,1830,1610),
'banner_o':(1275,1197,1552,1610),
'banner_n':(996,1197,1275,1610),
'banner_t':(718,1197,996,1610),
'banner_a':(438,1197,718,1610),
'zero_fields':(1458,1680,2737,2113),
'folio':(145,2095,262,2176)
}
(root/'transport').mkdir(exist_ok=True)
paths={}
im=Image.open(root/f'source/SP83_C13_148+149_scans/{page}.jpg')
for name,box in boxes.items():
 out=ImageOps.autocontrast(im.crop(box))
 if name.startswith('banner_') or name in ('job_records','zero_fields'):
  out=out.transpose(Image.Transpose.ROTATE_180)
 width=2200
 if name=='small_edges':width=2600
 if name=='long_edge':width=2800
 if name=='short_edge':width=2400
 if name=='job_records':width=5200
 if name.startswith('banner_'):width=1300
 if name=='zero_fields':width=3600
 if name=='folio':width=1200
 out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
 canonical=root/f'result/crops/{page}_{name}.png'
 out.save(canonical)
 viewed=canonical
 if canonical.stat().st_size>6000000:
  viewed=root/f'transport/{page}_{name}.webp'
  out.save(viewed,format='WEBP',lossless=True,quality=100,method=4)
  with Image.open(viewed) as check:
   assert check.size==out.size and check.mode==out.mode
   assert ImageChops.difference(check,out).getbbox() is None
 paths[name]=str(viewed)
 print(name,canonical.stat().st_size,viewed.name,flush=True)
(root/f'proposed/{page}_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
(root/f'proposed/{page}_view_paths.json').write_text(json.dumps(paths,indent=2)+'\n')
print('17 canonical crops complete; transport copies are pixel-identical and excluded from archival evidence.',flush=True)
