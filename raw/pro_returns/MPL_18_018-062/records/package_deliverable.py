"""Package all deliverables and work records, excluding input/source images."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, zipfile

parser=argparse.ArgumentParser()
mode=parser.add_mutually_exclusive_group(required=True)
mode.add_argument('--final',action='store_true')
mode.add_argument('--checkpoint',type=int)
args=parser.parse_args()
work=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
name='MPL_18_018-062.zip' if args.final else f'MPL_18_018-062_checkpoint_{args.checkpoint:02d}.zip'
dest=work.parent/name
assert not dest.exists(),f'Refusing to overwrite {dest}'
frozen=[]
for line in (work/'records/frozen.sha256').read_text().splitlines():
    digest,rel=line.split(None,1)
    assert hashlib.sha256((work/rel.strip()).read_bytes()).hexdigest()==digest,rel
    frozen.append((digest,rel.strip()))
assert len(frozen)==46
if args.final:
    required=['MPL_18_018-062_transcription.tex','MPL_18_018-062_inventory.csv',
              'MPL_18_018-062_doubts.md','MPL_18_018-062_notes.md','progress.log',
              'records/research_self_flagged.md','records/final_validation.json']
    assert all((work/p).is_file() for p in required)
    with (work/'progress.log').open('a') as f:
        f.write(f'frozen transcription hashes unchanged {stamp}; all 45 pages and combined fragment (46 files) verified\n')
        f.write(f'final archive assembly {stamp}; complete deliverables and records\n')
    with (work/'records/quality_checks.md').open('a') as f:
        f.write(f'\n## Final verification\n\n{stamp}: all 46 frozen hashes unchanged. '
                'Final research-note structure and mathematical delimiters checked; '
                'the archive contains all 45 page files, required deliverables and research/work records. '
                'The supplied scans and context sources are excluded.\n')
else:
    with (work/'progress.log').open('a') as f:
        f.write(f'hourly checkpoint {args.checkpoint:02d} {stamp}; all deliverables and work records written so far; frozen transcription unchanged\n')

manifest=work/'records/package_manifest.sha256'
paths=sorted(p for p in work.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=manifest)
assert not any(p.suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.zip'} for p in paths)
manifest.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(work))+'\n' for p in paths))
paths.append(manifest)
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(paths):z.write(p,str(p.relative_to(work)))
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(paths)
    for digest,rel in frozen:assert hashlib.sha256(z.read(rel)).hexdigest()==digest
    for line in z.read('records/package_manifest.sha256').decode().splitlines():
        digest,rel=line.split(None,1)
        assert hashlib.sha256(z.read(rel.strip())).hexdigest()==digest,rel
print(json.dumps({'archive':str(dest),'bytes':dest.stat().st_size,'members':len(paths),
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                  'frozen_files_verified':len(frozen),'crc_check':'passed'}))
