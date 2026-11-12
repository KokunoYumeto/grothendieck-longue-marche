"""Stack crops found by word (findcrop.py logic) into one image with labels: python montage.py OUT.png KEY:REGEX[:nth] ..."""
import json, pathlib, re, subprocess, sys
from PIL import Image, ImageDraw
BASE = pathlib.Path(__file__).resolve().parent.parent
outs = []
for i, spec in enumerate(sys.argv[2:]):
    parts = spec.split("::")
    key, rx = parts[0], parts[1]
    nth = parts[2] if len(parts) > 2 else "0"
    tmp = BASE / "pilot" / "crops" / f"_m{i}.png"
    r = subprocess.run([sys.executable, str(BASE / "scripts" / "findcrop.py"), key, rx, str(tmp), nth, "1.0", "1.0"], capture_output=True, text=True)
    if not tmp.exists() or "not found" in r.stdout + r.stderr:
        print("NOT FOUND", spec); continue
    im = Image.open(tmp); im = im.resize((int(im.width * 0.75), int(im.height * 0.75)))
    lab = Image.new("RGB", (im.width, 26), "yellow"); ImageDraw.Draw(lab).text((5, 5), f"[{i}] {key} / {rx}", fill="black")
    outs += [lab, im]; tmp.unlink()
W = max(o.width for o in outs); H = sum(o.height for o in outs)
m = Image.new("RGB", (W, H), "white"); y = 0
for o in outs: m.paste(o, (0, y)); y += o.height
m.save(sys.argv[1]); print("ok", W, H)
