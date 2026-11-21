from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/012/A'
source=root/'source/SP40_CW_81_scans/J81-02_81_scan012.jpg'
plans=[
 ('01_top_right_OK',(1438,26,1540,111),'C doubtful-readings row 1: fourth top label, K/k and final branch.'),
 ('02_miniature_ou',(145,807,259,902),'C doubtful-readings row 2: word between the two lower-left miniature ovals.'),
 ('03_overlaid_oval',(140,548,408,840),'C doubtful-readings row 3: large lower-left oval and complete overlaid zigzags; cancellation role.'),
 ('04_right_group',(803,343,1661,1188),'Complete right group: repeated corner lines, all extended curves and their endpoints; H cancellation claim and arrowheads.'),
 ('05_lower_pale_trace',(363,1268,435,1347),'Detached pale curved trace in lower blank field, including both ends.'),
 ('06_lower_single_point',(770,1412,811,1453),'Detached dark point in lower blank field.'),
 ('07_lower_paired_points',(1505,1686,1548,1730),'Two detached dark points in lower-right blank field.'),
 ('08_triangle_gap_marks',(195,429,316,526),'Small detached marks over and to the right of the first lower triangle, with triangle/solid point context.'),
 ('09_gap_point',(430,470,479,527),'Detached dark point between first lower dot and looping mark.'),
 ('10_upper_looping_mark',(512,398,570,523),'Complete narrow looping mark to left of heavy tripod; inspect supported shape without supplied letter.'),
 ('11_lower_zigzag',(388,885,459,1031),'Complete lower narrow zigzag between quadrilateral and spoked triangle.'),
]
manifest=[]
with Image.open(source) as im:
 for stem,box,purpose in plans:
  crop=im.crop(box)
  crop=ImageOps.autocontrast(crop,cutoff=0)
  w=2400 if box[2]-box[0]>=500 else 2000
  h=round(crop.height*w/crop.width)
  crop=crop.resize((w,h),Image.Resampling.LANCZOS)
  crop=crop.filter(ImageFilter.UnsharpMask(radius=1.0,percent=80,threshold=3))
  target=out/'crops'/f'{stem}.png'
  crop.save(target)
  manifest.append({'path':f'crops/{stem}.png','bbox':list(box),'coordinate_system':'original full scan, upper-left origin; right/bottom exclusive','rotation':0,'purpose':purpose,'output_size':[w,h]})
(out/'crops_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'single-enlargement crops.')
