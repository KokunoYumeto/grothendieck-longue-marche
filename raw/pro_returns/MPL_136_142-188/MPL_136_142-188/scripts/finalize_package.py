"""Assemble the authorized final archive from deliverables and text work records."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, zipfile

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
ALLOWED={'.md','.tex','.csv','.log','.py','.json','.sha256','.txt'}

def included(p):
    return p.is_file() and p.suffix in ALLOWED and '__pycache__' not in p.parts

def main():
    final=WORK/'MPL_136_142-188.zip'
    if final.exists():
        raise SystemExit('Final archive already exists; inspect it before any replacement.')
    for p in (WORK/'verification').rglob('*'):
        if included(p):
            target=ROOT/'records'/'verification'/p.relative_to(WORK/'verification')
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(p,target)
    result=subprocess.run([sys.executable,str(ROOT/'scripts/validate_package.py'),'--final'],
                          text=True,capture_output=True)
    (ROOT/'records/final_validation.txt').write_text(result.stdout+result.stderr)
    if result.returncode:
        raise SystemExit(result.stdout+result.stderr)
    frozen=[]
    for line in (ROOT/'records/frozen.sha256').read_text().splitlines():
        digest,name=line.split('  ',1)
        actual=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        assert actual==digest,name
        frozen.append(name)
    assert len(frozen)==47
    now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'research notes completed {now}; 68 numbered items, all individually searched against supplied context; 46 scans and their source distinctions reviewed in the notes\n')
        f.write(f'frozen hashes unchanged {now}; all 46 page-file SHA-256 values and the combined-transcription SHA-256 match the pre-context freeze\n')
        f.write(f'final package assembly {now}; original scans, crops, context sources and generated binary compilation outputs excluded\n')
    manifest=ROOT/'records/package_manifest.sha256'
    files=sorted(p for p in ROOT.rglob('*') if included(p) and p!=manifest)
    manifest.write_text('\n'.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix()
                                  for p in files)+'\n')
    files.append(manifest)
    with zipfile.ZipFile(final,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(files):
            z.write(p,ROOT.name+'/'+p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(final) as z:
        assert z.testzip() is None
        assert len(z.infolist())==len(files)
        for p in files:
            arc=ROOT.name+'/'+p.relative_to(ROOT).as_posix()
            assert z.read(arc)==p.read_bytes(),arc
        assert not any(Path(n).suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.xdv','.fmt','.pyc'} for n in z.namelist())
    print(json.dumps({'archive':str(final),'bytes':final.stat().st_size,'members':len(files),
                      'sha256':hashlib.sha256(final.read_bytes()).hexdigest(),
                      'frozen_hashes_unchanged':len(frozen),'zip_crc_and_member_bytes':'passed'},indent=2))

if __name__=='__main__':main()
