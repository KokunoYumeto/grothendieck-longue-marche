"""Package current deliverables; never include source attachments or older ZIPs.

Run at the prescribed 45-minute boundaries with --checkpoint NN, or after the
completed audit and freeze with --final. Existing archives are never replaced.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse
import hashlib
import json
import zipfile

ROOT = Path('/workspace/scratch/b8c6ff258063')
WORK = ROOT / 'SP87_C13_149_work'
PREFIX = 'SP87_C13_149'

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def eligible(path):
    rel = path.relative_to(WORK)
    return (path.is_file() and '__pycache__' not in rel.parts
            and path.name != 'input.json'
            and path.suffix not in {'.zip', '.pyc'}
            and rel.parts[0] not in {'halves', 'source', 'upload'})

def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--checkpoint', type=int)
    g.add_argument('--final', action='store_true')
    args = p.parse_args()
    now = datetime.now(timezone.utc)
    stamp = now.strftime('%Y-%m-%d %H:%M:%S UTC')
    if args.checkpoint:
        first = (WORK/'progress.log').read_text().splitlines()[0]
        started = datetime.strptime(first, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
        due = started + timedelta(minutes=45*args.checkpoint)
        if now < due:
            raise SystemExit(f'Checkpoint {args.checkpoint} is not due until {due.isoformat()}')
        name = f'{PREFIX}_checkpoint_{args.checkpoint:02d}.zip'
        label = f'checkpoint {args.checkpoint:02d} packaged {stamp}'
    else:
        name = f'{PREFIX}.zip'
        label = f'final archive packaged {stamp}'
        if 'transcription frozen ' not in (WORK/'progress.log').read_text():
            raise SystemExit('Freeze the audited transcription before final packaging.')
    target = ROOT/name
    if target.exists():
        raise SystemExit(f'Refusing to overwrite {target}')
    with (WORK/'progress.log').open('a') as f:
        f.write(label+'\n')
    manifest = WORK/'review/archive_manifest.tsv'
    files = sorted(x for x in WORK.rglob('*') if eligible(x) and x != manifest)
    # Capture each file once so the manifest matches the archived bytes even
    # while independent readers continue writing provisional reports.
    snapshots = {x: x.read_bytes() for x in files}
    manifest.write_text('path\tbytes\tsha256\n'+''.join(
        f'{x.relative_to(WORK).as_posix()}\t{len(snapshots[x])}\t{hashlib.sha256(snapshots[x]).hexdigest()}\n' for x in files))
    files.append(manifest)
    snapshots[manifest] = manifest.read_bytes()
    with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for x in files:
            z.writestr(x.relative_to(WORK).as_posix(), snapshots[x])
    with zipfile.ZipFile(target) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f'ZIP CRC verification failed: {bad}')
    receipt = {'path':str(target), 'files':len(files), 'bytes':target.stat().st_size,
               'sha256':digest(target), 'created_utc':stamp}
    (WORK/'review'/f'{name}.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
