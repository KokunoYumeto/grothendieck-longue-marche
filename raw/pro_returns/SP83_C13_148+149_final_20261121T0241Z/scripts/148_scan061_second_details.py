from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan061'
original=Image.open(root/'source/SP83_C13_148+149_scans'/f'{page}.jpg').convert('RGB')
specs=[
('D01','original',(310,135,755,222),6),
('D02','original',(735,135,1370,222),5),
('D03','original',(380,240,1070,385),5),
('D04','original',(1050,245,1645,389),5),
('D05','original',(900,560,1663,1040),4),
('D06','original',(290,540,950,1040),4),
('D07','original',(410,1035,920,1110),6),
('D08','original',(1420,1010,1640,1105),8),
('D09','B14',(1300,990,2640,1570),1.8),
('D10','B16',(260,1420,2640,1780),1.5),
('D11','B15',(700,450,2200,740),1.7),
('D12','B15',(350,810,1300,1080),1.8),
('D13','B11',(1500,0,3750,440),1.4),
]
manifest=[]
for name,origin,rect,scale in specs:
 im=original if origin=='original' else Image.open(root/'result/crops'/f'{page}_second_{origin}.png').convert('RGB')
 crop=im.crop(rect)
 if origin=='original':crop=ImageOps.autocontrast(crop)
 crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
 if origin=='original':crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
 out=root/'result/crops'/f'{page}_second_{name}.png';crop.save(out)
 manifest.append({'detail':name,'origin':origin,'rect_in_origin_pixels':rect,'scale':scale,'path':str(out.relative_to(root)),'dimensions':crop.size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False})
 print(name,crop.size)
(root/'result/second'/f'{page}_second_detail_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
