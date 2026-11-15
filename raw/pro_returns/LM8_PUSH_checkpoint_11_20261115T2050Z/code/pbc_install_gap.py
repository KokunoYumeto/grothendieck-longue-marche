#!/usr/bin/env python3
"""Reproduce the scratch GAP installation used for the finite Hopf test."""
from pathlib import Path
import hashlib,json,os,subprocess,tarfile,urllib.request
import re

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'gap-runtime'
VERSION='4.16.1'
CORE=DEST/f'gap-{VERSION}-core.tar.gz'
URL=f'https://github.com/gap-system/gap/releases/download/v{VERSION}/gap-{VERSION}-core.tar.gz'
SHA='b4433a540a2f746d14b1645a0e95b3d499afb180aa421ebfd62b427f2b0cf74f'
DEST.mkdir(exist_ok=True)
if not CORE.exists():
    with urllib.request.urlopen(URL,timeout=60) as r:CORE.write_bytes(r.read())
assert hashlib.sha256(CORE.read_bytes()).hexdigest()==SHA
GAP=DEST/f'gap-{VERSION}'
if not GAP.exists():
    with tarfile.open(CORE) as t:t.extractall(DEST,filter='data')
tmp=DEST/'tmp';tmp.mkdir(exist_ok=True)
env=dict(os.environ,TMPDIR=str(tmp))
commands=[['./configure','--without-readline','--build=x86_64-pc-linux-gnu'],['make','-j4']]
if not (GAP/'gap').exists():
    for i,cmd in enumerate(commands):
        with (DEST/('configure.out' if i==0 else 'make.out')).open('w') as out:
            subprocess.run(cmd,cwd=GAP,env=env,stdout=out,stderr=subprocess.STDOUT,check=True)
pkg=GAP/'pkg';pkg.mkdir(exist_ok=True)
def package(name,version,url,expected):
    file=DEST/url.rsplit('/',1)[1]
    if not file.exists():
        with urllib.request.urlopen(url,timeout=60) as r:file.write_bytes(r.read())
    sha=hashlib.sha256(file.read_bytes()).hexdigest()
    assert sha==expected
    with tarfile.open(file) as t:t.extractall(pkg,filter='data')
    row=dict(package=name,version=version,url=url,sha256=sha)
    print(json.dumps(row),flush=True)
    return row
packages=[
 package('primgrp','4.0.3','https://github.com/gap-packages/primgrp/releases/download/v4.0.3/primgrp-4.0.3.tar.gz','2e733c10dbe7a904aac8eb8dd2c2cf1de2ecf7476b7d0fbf763866f22f489979'),
 package('smallgrp','1.7.0','https://github.com/gap-packages/smallgrp/releases/download/v1.7.0/SmallGrp-1.7.0.tar.gz','1bac5dd020d6ce38ec0879495424c964491437991961a5bb82b97f28dd734442'),
 package('polycyclic','2.18','https://github.com/gap-packages/polycyclic/releases/download/v2.18/polycyclic-2.18.tar.gz','334416c8aeb8bcd0a2b58b16cba590ea26fa8d54d275a0bdcf5999b889c13317')
]
# Four required packages have no matching GitHub "latest release" API.
# Use the authenticated official GAP distribution instead of guessing URLs.
full_url='https://github.com/gap-system/gap/releases/download/v4.16.1/gap-4.16.1.tar.gz'
full_sha='df7d116f03c426dac24bf7c76ea11416b29c5a48eac12f97811d80ec215f7f69'
full=DEST/'gap-4.16.1.tar.gz'
if not full.exists():
    with urllib.request.urlopen(full_url,timeout=60) as src,full.open('wb') as out:
        while block:=src.read(4*1024*1024):out.write(block)
digest=hashlib.sha256()
with full.open('rb') as src:
    while block:=src.read(4*1024*1024):digest.update(block)
assert digest.hexdigest()==full_sha
wanted=('gapdoc','transgrp','alnuth','autpgrp')
with tarfile.open(full) as archive:
    for member in archive:
        parts=Path(member.name).parts
        if len(parts)>=3 and parts[1]=='pkg' and any(parts[2].lower().startswith(x) for x in wanted):
            archive.extract(member,DEST,filter='data')
for name in wanted:
    info=next(p for p in pkg.glob('*/PackageInfo.g') if p.parent.name.lower().startswith(name))
    version=re.search(r'Version\s*:=\s*"([^"]+)"',info.read_text()).group(1)
    row=dict(package=name,version=version,url=full_url,distribution_sha256=full_sha)
    packages.append(row);print(json.dumps(row),flush=True)
record=dict(core=dict(version=VERSION,url=URL,sha256=SHA),build_commands=commands,packages=packages)
(DEST/'installation.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'LM8_PUSH/code/pbc_gap_installation.json').write_text(json.dumps(record,indent=2)+'\n')
