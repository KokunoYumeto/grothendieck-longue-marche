"""Create a complete checkpoint or final ZIP, excluding reproducible inputs/halves."""
from pathlib import Path
import zipfile, argparse, hashlib

p=argparse.ArgumentParser()
p.add_argument('name')
a=p.parse_args()
out=Path(__file__).resolve().parents[1]
dest=out.parent/'deliveries'/a.name
dest.parent.mkdir(exist_ok=True)
if dest.exists():raise SystemExit('Refusing to overwrite an existing delivery.')
source_copies={'documentation/task_prompt.md','documentation/PREAMBLE_reference.tex'}
paths=sorted(x for x in out.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.suffix!='.zip' and str(x.relative_to(out)) not in source_copies)
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in paths:z.write(f,str(f.relative_to(out)))
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
print(str(dest))
print('files',len(paths),'bytes',dest.stat().st_size,'SHA-256',hashlib.sha256(dest.read_bytes()).hexdigest())
