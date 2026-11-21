from pathlib import Path
from PIL import Image
import numpy as np,json
ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
helpers=[]
for box in ['B03','B06']:
    im=Image.open(ROOT/'crops'/f'148_scan068_second_{box}.png').convert('RGB')
    a=np.asarray(im,dtype=np.float32)
    neutral=1-np.clip((a[:,:,0]-a[:,:,2]-5)/20,0,1)
    luminance=a.mean(axis=2)
    ink=np.clip((255-luminance)*2.2,0,255)*neutral
    out=Image.fromarray(np.uint8(np.clip(255-ink,0,255)))
    p=ROOT/'crops'/f'148_scan068_second_{box}_neutral.png'
    out.save(p)
    helpers.append({'box':box,'path':str(p),'within_canonical_box':True,'transform':'Neutral-colour weighting suppresses yellow/brown printed hatching, followed by 2.2-fold ink contrast; enhancement is supplemental and no absent line is inferred from it.','viewed':False})
(ROOT/'second'/'148_scan068_second_helper_manifest.json').write_text(json.dumps(helpers,ensure_ascii=False,indent=2)+'\n')
