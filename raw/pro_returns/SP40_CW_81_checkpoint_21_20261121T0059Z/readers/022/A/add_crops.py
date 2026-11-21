from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
p=Path('out/readers/022/A')
records=json.loads((p/'crops.json').read_text())
for r in records: r.update(viewed=True,view_count=1)
new=[('14_live_fermees',[525,1810,815,1960],'independently unresolved acute/grave/absence in live fermées and its underline endpoints'),('15_precise',[245,515,1115,655],'independently unresolved accent in précise and complete introductory clause')]
with Image.open('source/SP40_CW_81_scans/J81-03_81_scan022.jpg') as im:
 for stem,bbox,purpose in new:
  a=ImageOps.autocontrast(im.crop(bbox).convert('RGB'))
  factor=3000/a.width
  a=a.resize((3000,round(a.height*factor)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=100,threshold=3))
  rel='crops/'+stem+'.png';a.save(p/rel)
  records.append({'path':rel,'bbox':bbox,'coordinate_system':'original full scan; origin upper left; x right, y down','rotation':0,'resample':'PIL LANCZOS','autocontrast':True,'sharpen':'UnsharpMask radius=1.1 percent=100 threshold=3','output_size':list(a.size),'purpose':purpose,'viewed':False,'view_count':0})
(p/'crops.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Thirteen crop views recorded; two new, independently unresolved word targets prepared.')
