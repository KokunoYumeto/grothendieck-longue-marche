"""Download official public PARI source and build a local computation runtime.
Only a public release URL is requested; no task data leaves the workspace.
"""
from pathlib import Path
import urllib.request, hashlib, tarfile, subprocess, os
base=Path('/tmp/birational-pari-runtime');base.mkdir(exist_ok=True)
url='https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.19.1.tar.gz'
archive=base/'pari-2.19.1.tar.gz'
if not archive.exists():
    archive.write_bytes(urllib.request.urlopen(url, timeout=60).read())
sha=hashlib.sha256(archive.read_bytes()).hexdigest()
assert sha=='419553b11ff8c3ecb8e9031b7d91d7cee003a5d721e685fcb499565c96fe2943',sha
print('Official public release',url,'SHA256',sha,flush=True)
source=base/'pari-2.19.1'
if not source.exists():
    with tarfile.open(archive) as t:t.extractall(base,filter='data')
for args in [['./Configure','--without-readline'],['make','-j4','gp']]:
    print('Local command',args,flush=True)
    subprocess.run(args,cwd=source,check=True)
print('LOCAL GP',source/'gp',flush=True)
