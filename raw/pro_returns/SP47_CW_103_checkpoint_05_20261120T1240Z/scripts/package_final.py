from pathlib import Path
import zipfile,json,hashlib
R=Path(__file__).resolve().parents[1]
if not (R/'records/frozen_hashes.json').exists():raise SystemExit('Freeze first')
hashes=json.loads((R/'records/frozen_hashes.json').read_text())['sha256']
for path,h in hashes.items():
    if hashlib.sha256((R/path).read_bytes()).hexdigest()!=h:raise SystemExit('Frozen hash mismatch: '+path)
files=[p for p in sorted(R.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
manifest=R/'records/final_file_list.tsv'
manifest.write_text('path\tbytes\n'+'\n'.join(str(p.relative_to(R))+'\t'+str(p.stat().st_size) for p in files if p!=manifest)+'\n')
files=[p for p in sorted(R.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
dest=R.parent/'deliveries/SP47_CW_103.zip';dest.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(R))
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad:raise SystemExit('ZIP integrity failure: '+bad)
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'files':len(files),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
