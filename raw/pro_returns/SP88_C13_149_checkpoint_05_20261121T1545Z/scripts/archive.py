"""Package this run's deliverables; checkpoint creation is time-gated.

Source attachments and reproducible image halves are outside edition/ and
therefore excluded. Archives are always written outside edition/.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, time, zipfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('kind', choices=['checkpoint', 'final'])
    args = ap.parse_args()
    run_path = ROOT / 'review/run.json'
    run = json.loads(run_path.read_text())
    now = time.time()
    if args.kind == 'checkpoint':
        elapsed = now - run['last_checkpoint_epoch']
        if elapsed < 45 * 60:
            print(json.dumps({'due': False, 'seconds_until_due': round(2700-elapsed)}))
            return
        seq = run.get('checkpoint_count', 0) + 1
        filename = f'SP88_C13_149_checkpoint_{seq:02d}.zip'
        run['checkpoint_count'] = seq
        run['last_checkpoint_epoch'] = now
        run.setdefault('checkpoints', []).append({'name':filename, 'created_utc':utc()})
        run_path.write_text(json.dumps(run, ensure_ascii=False, indent=2)+'\n')
        with (ROOT/'progress.log').open('a') as out:
            out.write(f'checkpoint {seq:02d} packaged {utc()}: {filename}\n')
    else:
        filename = 'SP88_C13_149.zip'
    destination = WORK / 'deliveries' / filename
    destination.parent.mkdir(exist_ok=True)
    if destination.exists():
        raise FileExistsError(f'Refusing to overwrite {destination}')
    files = sorted(p for p in ROOT.rglob('*') if p.is_file()
                   and '__pycache__' not in p.parts and p.suffix not in {'.zip','.pyc'})
    manifest=[]
    with zipfile.ZipFile(destination, 'x', zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
        for p in files:
            data=p.read_bytes()
            rel=p.relative_to(ROOT).as_posix()
            z.writestr(rel,data)
            manifest.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        z.writestr('ARCHIVE_MANIFEST.json',json.dumps({'created_utc':utc(),'kind':args.kind,'files':manifest},indent=2)+'\n')
    print(json.dumps({'due':True,'kind':args.kind,'path':str(destination),'bytes':destination.stat().st_size,'files':len(files),'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()}))

if __name__=='__main__':
    main()
