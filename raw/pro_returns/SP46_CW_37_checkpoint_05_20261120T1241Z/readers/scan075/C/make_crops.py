from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/C')
source=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075.jpg')
items=[
 {'id':'note','bbox':[35,48,242,248],'rotation':-24,'reason':'C doubt in the first word of the slanted pencil note; inspect the word and adjacent ruled references in their own orientation.'},
 {'id':'introduced_K','bbox':[1125,956,1230,1025],'rotation':0,'reason':'C explicit K versus blackboard K doubt; distinguish independent stem from retracing.'},
 {'id':'schema','bbox':[935,1110,1072,1185],'rotation':0,'reason':'C explicit doubt at the overwritten terminal letter of schéma before lisse.'},
 {'id':'marginal_points','bbox':[1518,1342,1576,1395],'rotation':0,'reason':'C colon doubt; inspect the geometry and material of the detached pair right of diagram (2).'},
 {'id':'sentence_il','bbox':[1042,1035,1246,1106],'rotation':0,'reason':'Open upper/lower-case reading of il following the full stop after dérivée.'},
 {'id':'ext_detached_trace','bbox':[960,1195,1205,1278],'rotation':0,'reason':'New detached trace below the Ext expression in (1); inspect whether there is a recoverable ink mark.'},
 {'id':'extensions_ending','bbox':[294,963,485,1024],'rotation':0,'reason':'Check unresolved singular/plural ending of d’extensions in the group-definition paragraph.'}
]
im=Image.open(source)
for item in items:
 crop=im.crop(item['bbox'])
 if item['rotation']:
  crop=crop.rotate(item['rotation'],resample=Image.Resampling.BICUBIC,expand=True,fillcolor=(250,250,242))
 crop=ImageOps.autocontrast(crop,cutoff=0.4)
 scale=2400/crop.width
 crop=crop.resize((2400,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.5,percent=115,threshold=3))
 filename='crop_C_075_'+item['id']+'.jpg'
 crop.save(root/'crops'/filename,quality=96,subsampling=0)
 item['file']='crops/'+filename
 item['processing']='RGB autocontrast cutoff 0.4%; rotation with bicubic where specified; LANCZOS resize to 2400 px width; UnsharpMask radius 1.5, percent 115, threshold 3; JPEG quality 96, no subsampling.'
json.dump(items,open(root/'crop_log.json','w'),ensure_ascii=False,indent=2)
print(json.dumps(items,ensure_ascii=False,indent=2))
