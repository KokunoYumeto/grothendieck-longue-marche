from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(root/'packets/145_scan009/page.jpg')
boxes={
 'pair_separator':[1070,70,1310,190],
 'ca_semble':[820,270,1130,375],
 'comme_and_respectant_insertion':[225,640,1310,805],
 's3_plus':[320,785,490,925],
 's3_entier':[780,780,930,920],
 'exterieurs':[210,1008,570,1125],
 'margin_note':[18,755,465,1300],
 'commutation_struck_u':[485,1205,1015,1315],
 'arguments_emphasis':[1195,1280,1585,1390],
 'first_condition_and_parameter':[375,1495,1590,1735],
 'second_condition_annotation':[320,1760,1060,1925],
 'cancelled_condition':[500,2130,1645,2268],
 'existential_condition':[295,2250,1075,2348],
 'manuscript_number_eight':[25,2250,145,2348]
}
for name,box in boxes.items():
 c=ImageOps.autocontrast(im.crop(box).convert('RGB'),cutoff=.5)
 if name=='margin_note':c=c.rotate(-26,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
 c=c.resize((2600,round(c.height*2600/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 c.save(root/f'edition/crops/145_scan009_{name}.png')
(root/'edition/reader_reports/145_scan009_crop_boxes.json').write_text(json.dumps(boxes,indent=2))
