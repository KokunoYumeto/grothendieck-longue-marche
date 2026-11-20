from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(root/'packets/145_scan006/page.jpg')
boxes={
 's3_opening':[690,65,1100,165],
 'top_insert_and_strike':[310,140,1285,300],
 'aut_struck_words':[590,310,1010,405],
 'linfty_formula':[380,540,1658,655],
 'de_meme_abbreviation':[235,743,510,820],
 's3_representation':[985,1020,1260,1145],
 'du_moins':[1070,1380,1645,1495],
 's3_operant':[1110,1490,1360,1625],
 'sur_pi_insertion':[1235,1670,1658,1825],
 'et_meme_abbreviation':[345,1960,805,2060],
 'fixed_point_insertion_and_cancellation':[960,1900,1658,2060],
 'a_inclus':[745,2135,1270,2230],
 'teichmuller_insertion':[235,2195,880,2330],
 'conjugaison_quotes':[835,2245,1635,2335]
}
for name,box in boxes.items():
 c=ImageOps.autocontrast(im.crop(box).convert('RGB'),cutoff=0.5)
 c=c.resize((2600,round(c.height*2600/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 c.save(root/f'edition/crops/145_scan006_{name}.png')
(root/'edition/reader_reports/145_scan006_crop_boxes.json').write_text(json.dumps(boxes,indent=2))
name='manuscript_number'
box=[25,2245,150,2340]
c=ImageOps.autocontrast(im.crop(box).convert('RGB'),cutoff=0.5)
c=c.resize((2200,round(c.height*2200/c.width)),Image.Resampling.LANCZOS)
c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
c.save(root/f'edition/crops/145_scan006_{name}.png')
boxes[name]=box
(root/'edition/reader_reports/145_scan006_crop_boxes.json').write_text(json.dumps(boxes,indent=2))
