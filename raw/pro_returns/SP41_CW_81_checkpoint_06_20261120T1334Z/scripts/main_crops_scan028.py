from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json,datetime
root=Path('/workspace/scratch/811dda00717a')
p=json.loads((root/'runtime_inputs/scan028/packet.json').read_text())
im=Image.open(p['images'][0]);out=root/'work/crops/scan028';out.mkdir(exist_ok=True)
# Each box identifies an unresolved witness comparison absent from reader crops.
boxes={
 'F02_ens':(250,195,420,275),
 'F12_comp':(250,1045,660,1145),
 'F25_ens':(1180,170,1400,270),
 'F26_X_end':(1200,735,1450,920),
 'F27_Xprime_end':(930,1380,1140,1510),
 'F28_Xdouble_end':(970,1505,1160,1650),
 'F29_note_gap':(220,1650,1560,1710),
 'F30_avec':(210,1695,390,1800),
 'F31_intersection_end':(860,1700,1080,1820),
 'F32_cette':(210,1810,420,1930)
}
for name,box in boxes.items():
 f=out/('main_'+name+'.png')
 if f.exists():continue
 a=ImageOps.autocontrast(im.crop(box));a=a.resize((2500,round(a.height*2500/a.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3));a.save(f)
 with (out/'crop_manifest.jsonl').open('a') as h:h.write(json.dumps({'source':p['images'][0],'target':str(f),'bbox':box,'rotation_degrees':0,'width':2500,'UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
print(len(boxes),'new main-reader crops')
