"""Save immutable numbered research checkpoints; upload is performed separately."""
from pathlib import Path
import hashlib, json, sys, zipfile
from package_files import distribution_files, exclusion_reason

root = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
milestone = sys.argv[2]
destination = root.parent / 'checkpoints' / f'LM8_LIE_APPROXIMATIONS_checkpoint_{number:02d}.zip'
if destination.exists():
    raise SystemExit(f'Refusing to overwrite {destination}')
destination.parent.mkdir(exist_ok=True)
files = distribution_files(root)
source_only='--source-only' in sys.argv[3:]
if source_only:
    files=[p for p in files if p.name!='LM8_LIE_APPROXIMATIONS_paper.pdf']
excluded = [p for p in sorted(root.rglob('*')) if p.is_file()
            and exclusion_reason(root,p) is not None
            and p.suffix in {'.pdf','.png','.txt'}]
# Hash and archive the same captured bytes, including any running experiment log.
captured = {str(p.relative_to(root)):p.read_bytes() for p in files}
manifest = {'milestone': milestone,
            'source_only':source_only,
            'pdf_omission_reason':('Final document layout and visual audit are in progress.'
                                   if source_only else None),
            'files': [{'path':rel,
                       'sha256':hashlib.sha256(data).hexdigest()} for rel,data in captured.items()],
            'reading_material_not_packaged': [str(p.relative_to(root)) for p in excluded]}
manifest_path = root/'audit'/f'checkpoint_{number:02d}.json'
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
captured[str(manifest_path.relative_to(root))]=manifest_path.read_bytes()
with zipfile.ZipFile(destination,'x',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for rel,data in captured.items():
        z.writestr(root.name+'/'+rel,data)
print(json.dumps({'path':str(destination),'files':len(captured),'bytes':destination.stat().st_size}))
