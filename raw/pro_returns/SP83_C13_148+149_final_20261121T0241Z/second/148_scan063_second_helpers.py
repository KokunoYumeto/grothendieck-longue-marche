from pathlib import Path
from PIL import Image
import json
ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
helpers=[]
def helper(box,name,rect=None,angle=None,width=None):
    im=Image.open(ROOT/'crops'/f'148_scan063_second_{box}.png').convert('RGB')
    if rect: im=im.crop(rect)
    if angle: im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    if width: im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    p=ROOT/'crops'/f'148_scan063_second_{box}_{name}.png'
    im.save(p)
    helpers.append({'box':box,'path':str(p),'within_canonical_box':True,'canonical_pixel_subrect':rect,'angle':angle,'display_width':width,'viewed':False})
helper('B02','right',(1600,0,3000,232),width=2800)
helper('B03','overwritten',(2000,0,2460,255),width=2300)
helper('B09','rotated',angle=-32,width=3000)
(ROOT/'second'/'148_scan063_second_helper_manifest.json').write_text(json.dumps(helpers,ensure_ascii=False,indent=2)+'\n')
helper('B22','formula',(900,50,3000,600),width=3600)
helper('B22','annotation',(1170,510,2650,1290),width=2960)
(ROOT/'second'/'148_scan063_second_helper_manifest.json').write_text(json.dumps(helpers,ensure_ascii=False,indent=2)+'\n')
helper('B17','leader',(0,90,1800,679),width=3000)
helper('B20','cancelled',(0,380,3000,849),width=3600)
(ROOT/'second'/'148_scan063_second_helper_manifest.json').write_text(json.dumps(helpers,ensure_ascii=False,indent=2)+'\n')
