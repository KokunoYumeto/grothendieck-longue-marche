from pathlib import Path
import sys, zipfile, hashlib, json
root=Path(__file__).resolve().parents[2]
number=int(sys.argv[1])
target=root/f"02_SECTIONS_OVER_Q_checkpoint_{number:02d}.zip"
assert not target.exists(), f"Refusing to overwrite {target}"
files=sorted(p for p in (root/"work").rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".zip")
manifest={str(p.relative_to(root/"work")): {"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
with zipfile.ZipFile(target,"x",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,str(p.relative_to(root/"work")))
    z.writestr("checkpoint_manifest.json",json.dumps(manifest,indent=2)+"\n")
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    assert all(not n.startswith(("background/","runtime/")) and not n.endswith(".zip") for n in z.namelist())
print(json.dumps({"archive":str(target),"files":len(files)+1,"bytes":target.stat().st_size,"sha256":hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
