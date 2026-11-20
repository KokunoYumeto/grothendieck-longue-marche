from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/94548b74fbe0')
out=base/'out/readers/012/B'
src=Image.open(base/'source/SP40_CW_81_scans/J81-02_81_scan012.jpg').convert('RGB')
plans=[
 ('c01_upper_right_label.png',[1425,22,1540,113],'C doubt row 1: OK/Ok; retain full letter height and upper-right oval context'),
 ('c02_marked_left_assembly.png',[145,547,412,927],'C doubt row 3: overlaid strokes and oval state; connected lower miniature and C doubt row 2 between-miniature ou'),
 ('c03_upper_loop.png',[510,400,573,521],'Detached upright loop/zigzag between triangle-dot and heavy Y; graphical or letter-shaped reading'),
 ('c04_lower_loop.png',[390,882,458,1029],'Detached upright zigzag right of lower quadrilateral; full upper and lower endpoints'),
 ('c05_right_group.png',[801,335,1687,1197],'Right group: connected border rules, crossing strokes, arrowheads, curves, oval boundaries; H cancellation assertion and faint endpoints; includes independent side-edge mark'),
 ('c06_triangle_dots.png',[151,432,472,534],'Small triangle, detached filled point, upper-apex tick and two detached tiny marks'),
 ('c07_top_gap_traces.png',[552,26,629,92],'Two detached narrow traces between upper small oval and OK oval'),
 ('c08_pale_lower_hook.png',[347,1259,439,1354],'Pale curved trace in otherwise empty lower area; possible glyph versus unassigned graphical shape'),
 ('c09_lower_paired_spots.png',[1437,1642,1551,1737],'Lower-right detached paired dark spots and nearby pale short trace; role and surface origin unresolved'),
 ('c10_foot_right_traces.png',[1398,2071,1672,2303],'Lower-right faint upright and detached dark spots in empty field; no character assigned from texture')
]
manifest=[]
for name,bbox,purpose in plans:
 im=src.crop(bbox)
 im=ImageOps.autocontrast(im,cutoff=0)
 factor=max(3,round(2400/im.width))
 im=im.resize((im.width*factor,im.height*factor),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
 im.save(out/'crops'/name)
 manifest.append({'path':'crops/'+name,'bbox':bbox,'rotation':0,'purpose':purpose,'original_size':[bbox[2]-bbox[0],bbox[3]-bbox[1]],'enlargement':factor,'processed':'PIL autocontrast cutoff 0; LANCZOS; UnsharpMask(radius=1.3,percent=110,threshold=3)'})
(out/'crops/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False))
