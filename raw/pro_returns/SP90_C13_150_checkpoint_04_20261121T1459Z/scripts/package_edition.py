"""Package the cumulative deliverables and audit records, excluding inputs.

The caller enforces the user's 45-minute checkpoint schedule and saves the
result persistently. This script neither schedules nor uploads anything.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('output',type=Path);a=p.parse_args()
    out=a.output.resolve()
    if out.exists():raise FileExistsError(out)
    if ROOT==out or ROOT in out.parents:raise ValueError('Archive must be outside edition tree')
    files=[f for f in sorted(ROOT.rglob('*')) if f.is_file()
           and f.suffix.lower()!='.zip' and '__pycache__' not in f.parts
           and f.relative_to(ROOT).as_posix()!='reference/controlling_prompt.md']
    out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for f in files:z.write(f,f.relative_to(ROOT))
    with zipfile.ZipFile(out) as z:
        bad=z.testzip()
        if bad:raise RuntimeError('ZIP CRC failed: '+bad)
        names=z.namelist()
        if len(names)!=len(files):raise RuntimeError('Archive entry count mismatch')
    sha=hashlib.file_digest(out.open('rb'),'sha256').hexdigest()
    print(json.dumps({'path':str(out),'files':len(files),'bytes':out.stat().st_size,'sha256':sha},indent=2))

if __name__=='__main__':main()
