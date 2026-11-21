from PIL import Image,ImageEnhance,ImageFilter
from pathlib import Path
import json
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');src=Image.open(w.parent/'source/SP87_C13_149_scans/149_scan095.jpg')
rows=[]
for name,box,reason in [('regarder_full',(1205,55,1535,180),'B003 stops inside regarder; verify the excluded end rather than interpret clipping as source loss.'),('parenthesis_opening',(865,1100,1100,1240),'B021 reports si versus où in the small opening of the full parenthesis.')]:
 im=src.crop(box);im=im.resize((1600,round(im.height*1600/im.width)),Image.Resampling.LANCZOS);im=ImageEnhance.Contrast(im).enhance(1.25);im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=115,threshold=3));target=w/'crops'/f'audit_149_scan095_{name}.png';im.save(target);rows.append({'source':'149_scan095.jpg','coordinates':box,'crop':str(target.relative_to(w)),'reason':reason,'stage':'root adjudication after independent TSV saved'})
(w/'review/149_scan095_additional_crop_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
