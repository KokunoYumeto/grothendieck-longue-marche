"""Record and verify the frozen transcription without compiling LaTeX."""
from pathlib import Path
import argparse, datetime, hashlib, json

ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/'reference/transcription_hashes.json'

def utc():return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');a=p.parse_args()
    paths=sorted((ROOT/'pages').glob('150_scan*.tex'))+[ROOT/'SP90_C13_150_transcription.tex']
    current={str(p.relative_to(ROOT)):digest(p) for p in paths}
    if a.verify:
        frozen=json.loads(STATE.read_text())
        if current!=frozen['sha256']:raise RuntimeError('Frozen transcription hash mismatch')
        with (ROOT/'progress.log').open('a') as f:f.write(f'transcription hashes verified unchanged {utc()}: {len(current)} files\n')
        print(json.dumps({'verified':len(current),'unchanged':True}))
        return
    if STATE.exists():raise FileExistsError('A transcription freeze already exists')
    if len(paths)!=26:raise RuntimeError(f'Expected 25 pages plus combined fragment; got {len(paths)} files')
    stamp=utc();STATE.write_text(json.dumps({'frozen_at':stamp,'sha256':current},indent=2)+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'transcription frozen {stamp}\n')
        for name,sha in current.items():f.write(f'sha256 {sha} {name}\n')
    print(json.dumps({'frozen':len(current),'time':stamp}))

if __name__=='__main__':main()
