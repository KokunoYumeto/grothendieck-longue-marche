from pathlib import Path
import json
from PIL import Image, ImageOps
root=Path(__file__).parent
items=[('13_faint_lower_strokes', '/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan007_b.jpg', [1207, 732, 1283, 786], 2400, 'Faint short strokes immediately below pi-zero equality'), ('14_middle_vertical_tip', '/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan007_a.jpg', [1040, 1147, 1100, 1222], 2400, 'Lower tip of vertical connector under boundary Sigma')]
log=json.loads((root/"crop_log.json").read_text(encoding="utf-8"))
for name,source,box,width,place in items:
    im=ImageOps.autocontrast(Image.open(source).convert("L").crop(box))
    scale=width/im.width
    im=im.resize((width,round(im.height*scale)),Image.Resampling.LANCZOS)
    target=root/(name+".jpg")
    im.save(target,format="JPEG",quality=97)
    log.append({"file":str(target),"source":source,"box":box,"rotation":0,"output_width":width,"scale":scale,"processing":"grayscale; autocontrast; LANCZOS enlargement; JPEG quality 97; no sharpening","place":place,"observed":"PENDING VIEW"})
(root/"crop_log.json").write_text(json.dumps(log,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
