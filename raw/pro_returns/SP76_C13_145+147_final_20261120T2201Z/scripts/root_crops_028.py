from pathlib import Path
from PIL import Image,ImageOps
W=Path(__file__).resolve().parents[1]
im=Image.open(W.parent/'source/SP76_C13_145+147_scans/145_scan028.jpg')
boxes={'semicolon':(705,365,1090,470),'isotropy_comma':(1180,1685,1545,1808),'pageno':(25,2278,115,2340)}
for name,box in boxes.items():
    p=W/'crops'/f'145_scan028_root_{name}.png'
    if p.exists():raise SystemExit('Refusing to recrop '+str(p))
    c=ImageOps.autocontrast(im.crop(box).convert('L'))
    c.resize((2200,round(c.height*2200/c.width)),Image.Resampling.LANCZOS).save(p)
    print(p.name,box)
