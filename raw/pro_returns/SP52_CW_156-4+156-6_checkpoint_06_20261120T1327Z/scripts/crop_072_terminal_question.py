from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json
O=Path(__file__).resolve().parents[1];s=O.parent/'source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan072.jpg';out=O/'crops/156-4_072';p=out/'a05_terminal_question.jpg'
if p.exists():raise SystemExit('Existing crop; do not recrop')
box=[410,890,710,1150]
im=ImageOps.autocontrast(Image.open(s).crop(box));im=im.rotate(-45,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white');sc=2500/im.width;im=im.resize((2500,round(im.height*sc)),Image.Resampling.LANCZOS);im=ImageEnhance.Sharpness(im).enhance(1.15);im.save(p,quality=94)
f=out/'manifest.json';m=json.loads(f.read_text());m.append(dict(path=str(p.relative_to(O)),source=str(s),bbox=box,rotation=-45,scale=sc,transforms=['autocontrast','rotation -45','LANCZOS to 2500 pixels','sharpness 1.15'],reason='Only the still-open terminal lge/large and closing parenthesis: all reader crops clip its continuation; R1 located missing extent at x550–660 y970–1100. Earlier words are not recropped.'));f.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
