"""Save immutable numbered research checkpoints; upload is performed separately."""
from pathlib import Path
import hashlib, json, sys, zipfile

root = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
milestone = sys.argv[2]
destination = root.parent / 'checkpoints' / f'LM8_LIE_APPROXIMATIONS_checkpoint_{number:02d}.zip'
if destination.exists():
    raise SystemExit(f'Refusing to overwrite {destination}')
destination.parent.mkdir(exist_ok=True)
files = [p for p in sorted(root.rglob('*')) if p.is_file()
         and '__pycache__' not in p.parts and p.suffix not in {'.aux', '.log', '.toc', '.out', '.bbl', '.blg'}]
# Printed computational outputs are deliverables, despite the shared .out suffix.
files += [p for p in sorted((root/'code').glob('*.out')) if p not in files]
# Full externally retrieved articles are reading material, not generated deliverables.
excluded = [p for p in files if p.parent == root/'notes' and p.suffix in {'.pdf', '.txt'}]
files = [p for p in files if p not in excluded]
manifest = {'milestone': milestone,
            'files': [{'path':str(p.relative_to(root)),
                       'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
            'reading_material_not_packaged': [str(p.relative_to(root)) for p in excluded]}
manifest_path = root/'audit'/f'checkpoint_{number:02d}.json'
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
files.append(manifest_path)
with zipfile.ZipFile(destination,'x',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for p in files:
        z.write(p,root.name+'/'+str(p.relative_to(root)))
print(json.dumps({'path':str(destination),'files':len(files),'bytes':destination.stat().st_size}))
