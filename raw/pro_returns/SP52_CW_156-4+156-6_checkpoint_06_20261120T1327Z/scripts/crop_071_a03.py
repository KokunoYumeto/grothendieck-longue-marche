from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json
O=Path(__file__).resolve().parents[1];d=O/'crops/156-4_071';s=O.parent/'source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan071.jpg';b=[270,585,920,850];p=d/'a03_de_family_F.jpg'
if p.exists():raise SystemExit('Existing crop; do not recrop')
im=ImageOps.autocontrast(Image.open(s).crop(b));scale=2500/im.width;im=im.resize((2500,round(im.height*scale)),Image.Resampling.LANCZOS);im=ImageEnhance.Sharpness(im).enhance(1.2);im.save(p,quality=94)
m=json.loads((d/'manifest.json').read_text());m.append(dict(path=str(p.relative_to(O)),source=str(s),bbox=b,rotation=0,scale=scale,transforms=['autocontrast','LANCZOS to 2500 pixels','sharpness 1.2'],reason='Family F in de F after objet G, not covered by any existing reader crop'));(d/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
