from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/011/C')
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan011.jpg')
regions=[
 ('01_edge.png',(575,0,683,65),'Detached paired strokes at upper edge'),
 ('02_left_first.png',(61,129,290,286),'Upper-left heavy P and detached short stroke at X'),
 ('03_top_product.png',(628,21,936,155),'First product Z or 2 and questioned relation'),
 ('04_top_right.png',(940,33,1391,156),'Overwritten first argument, final looped letter, endpoint'),
 ('05_crossed_cluster.png',(908,145,1463,348),'Cancelled Hom and three raised shapes; following Hom and little first argument'),
 ('06_left_second.png',(53,306,348,431),'O or 0 and double-stem P with closing expression boundary'),
 ('07_upper_drawing.png',(306,150,524,602),'Overlapping disk, rays, petals and detached traces'),
 ('08_middle_hom.png',(559,323,1026,445),'Small first argument, underlined inner Hom and closing parentheses'),
 ('09_last_hom.png',(371,773,765,889),'Predecessor beneath Z in last Hom line and underline state'),
 ('10_diagram_top.png',(1191,377,1565,581),'Crossed upper object, arch, overwritten product and final object'),
 ('11_diagram_vertical.png',(1236,567,1408,743),'Crossed letter beside vertical arrow and PxX destination'),
 ('12_diagram_lower_right.png',(1316,649,1582,1023),'U product subscript, V or W, left arrow and lower branches'),
 ('13_diagram_left_bar.png',(1060,731,1250,958),'Detached parallel uprights beside lower left P and formula endpoint'),
]
manifest=[]
with Image.open(source) as im:
 for name,bbox,purpose in regions:
  crop=ImageOps.autocontrast(im.crop(bbox))
  w=2600
  crop=crop.resize((w,round(crop.height*w/crop.width)),Image.Resampling.LANCZOS)
  crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
  crop.save(root/name)
  manifest.append(dict(path=name,bbox=list(bbox),rotation=0,purpose=purpose))
(root/'crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
