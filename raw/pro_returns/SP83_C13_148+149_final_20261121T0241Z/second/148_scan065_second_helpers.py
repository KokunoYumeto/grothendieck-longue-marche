from pathlib import Path
from PIL import Image
import json
ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
helpers=[]
def helper(box,name,rect,width):
    im=Image.open(ROOT/'crops'/f'148_scan065_second_{box}.png').convert('RGB').crop(rect)
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    p=ROOT/'crops'/f'148_scan065_second_{box}_{name}.png'
    im.save(p)
    helpers.append({'box':box,'path':str(p),'within_canonical_box':True,'canonical_pixel_subrect':rect,'display_width':width,'viewed':False})
helper('B04','parenthetical',(0,75,2650,380),4000)
helper('B06','upper_right',(1650,15,2900,300),3000)
helper('B06','lower_words',(0,615,1600,929),3200)
(ROOT/'second'/'148_scan065_second_helper_manifest.json').write_text(json.dumps(helpers,ensure_ascii=False,indent=2)+'\n')
