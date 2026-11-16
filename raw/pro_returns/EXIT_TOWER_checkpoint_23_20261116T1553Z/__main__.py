#!/usr/bin/env python3
"""Extract only pinned runtime; original members stream from this one ZIP."""
import hashlib,json,pathlib,subprocess,sys,tempfile,zipfile
sys.dont_write_bytecode=True
wrapper=pathlib.Path(sys.argv[0]).resolve()
with zipfile.ZipFile(wrapper) as archive,tempfile.TemporaryDirectory(prefix='mixed_checkpoint_runtime_') as directory:
    names=archive.namelist()
    if len(names)!=len(set(names)):raise ValueError('Duplicate portable ZIP entry')
    record=json.loads(archive.read('CHECKPOINT_RESUME.json'));root=pathlib.Path(directory)
    for name,expected in record['runtime_hashes'].items():
        p=pathlib.PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe portable runtime path')
        data=archive.read(name)
        if hashlib.sha256(data).hexdigest()!=expected:raise ValueError('Portable runtime differs')
        target=root/pathlib.Path(*p.parts);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    result=subprocess.run([sys.executable,'-B',str(root/'checkpoint_original_members.py'),str(wrapper),*sys.argv[1:]])
    raise SystemExit(result.returncode)
