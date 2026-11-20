from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/006c0e32b2af')
out=root/'out/readers/scan085/B'
source=root/'source/SP46_CW_37_scans/B37-04_37_scan085.jpg'
specs=[
 ('B01_chapter_round_character.jpg',[239,257,653,381],0,'Unresolved C doubt: O versus 0 in chapter heading; includes adjacent typed O context.'),
 ('B02_left_marginal_mark.jpg',[233,1100,310,1200],0,'Identity and exact strokes of the marginal mark beside the two cancelled rows.'),
 ('B03_two_row_cancellation.jpg',[320,1091,1510,1199],0,'Exact course and material of the cancellation crossing old 2.4 and 2.5 and extending over dotted leaders.'),
 ('B04_live_2_5_mark.jpg',[319,1239,531,1299],0,'Character and writing operation of the terminal mark in the live 2.5 reference.'),
 ('B05_reciproques_overtype.jpg',[569,1829,839,1888],0,'Explicit C doubt and linked overtyped letter pair inside réciproques in entry 3.5.')
]
im=Image.open(source)
rows=[]
for fn,bbox,rotation,reason in specs:
 crop=im.crop(tuple(bbox))
 before=crop.size
 crop=ImageOps.autocontrast(crop,cutoff=0.3)
 width=2600
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 crop.save(out/fn,quality=95)
 rows.append({'file':str(out/fn),'source':str(source),'bbox':bbox,'rotation':rotation,'reason':reason,'processing':{'crop_source_size':list(before),'autocontrast_cutoff':0.3,'resize_filter':'LANCZOS','output_size':list(crop.size),'unsharp_mask':{'radius':1.2,'percent':120,'threshold':3},'jpeg_quality':95},'requested_visual_deliveries':0,'actual_visual_views':0})
manifest={'source_image':str(source),'source_size':list(im.size),'half_a_origin':[0,0],'half_b_origin':[0,997],'source_views':[str(source),str(source.with_name(source.stem+'_a.jpg')),str(source.with_name(source.stem+'_b.jpg'))],'source_actual_visual_views':[1,1,1],'crops':rows}
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'crops_created':len(rows),'files':[x['file'] for x in rows]},ensure_ascii=False))
