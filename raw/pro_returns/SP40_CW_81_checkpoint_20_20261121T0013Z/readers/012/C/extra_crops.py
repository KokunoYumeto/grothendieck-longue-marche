from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/readers/012/C'
im=Image.open(B/'source/SP40_CW_81_scans/J81-02_81_scan012.jpg')
rows=[('13_lower_gray_spot',(1421,1630,1485,1686),'N19 pale small lower-right spot'),('14_lower_left_speck',(159,1770,212,1823),'N22 very small lower-left trace'),('15_lower_oblique',(672,1827,728,1879),'N23 faint oblique lower-field trace'),('16_lower_fold_spot',(1331,1909,1390,1961),'N24 pale spot at fold level'),('17_lower_central_point',(644,1978,701,2030),'N25 pale point in lower central field')]
manifest=json.loads((O/'crops/manifest.json').read_text())
for name,bbox,purpose in rows:
 out=ImageOps.autocontrast(im.crop(bbox),cutoff=0)
 ratio=2200/out.width
 out=out.resize((2200,round(out.height*ratio)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=70,threshold=3))
 rel='crops/'+name+'.png';out.save(O/rel)
 manifest.append(dict(path=rel,bbox=list(bbox),rotation=0,purpose=purpose,source_image='source/SP40_CW_81_scans/J81-02_81_scan012.jpg',processing='PIL autocontrast cutoff=0, LANCZOS resize, UnsharpMask radius=1 percent=70 threshold=3'))
(O/'crops/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created five additional first crops, without regenerating any prior crop.')
