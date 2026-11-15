#!/usr/bin/env python3
"""Preserve every changed prior-checkpoint member verbatim, without new ZIPs.

Usage: python code/preserve_checkpoint.py ../EXIT_TOWER_checkpoint_01.zip 01
Unchanged members already remain at their original paths. Changed or missing
members are copied under history/checkpoint_01; an exhaustive ledger records
both destinations. Existing history bytes are never overwritten.
"""
from pathlib import Path,PurePosixPath
import csv,hashlib,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
archive=Path(sys.argv[1]).resolve();number=sys.argv[2]
assert number.isdigit() and len(number)==2
prefix=Path('history')/('checkpoint_'+number)
ledger=[]
with zipfile.ZipFile(archive) as z:
    for info in z.infolist():
        if info.is_dir():continue
        rel=PurePosixPath(info.filename)
        assert not rel.is_absolute() and '..' not in rel.parts
        old=z.read(info)
        oldsha=hashlib.sha256(old).hexdigest()
        current=ROOT/Path(*rel.parts)
        # The ledger itself is rewritten below, even when it presently matches.
        same=(str(rel)!='checkpoint_history.csv' and current.is_file()
              and hashlib.sha256(current.read_bytes()).hexdigest()==oldsha)
        if same:
            location=Path(*rel.parts);treatment='retained at original path'
        else:
            location=prefix/Path(*rel.parts);dest=ROOT/location
            if dest.exists():
                assert dest.read_bytes()==old, str(dest)+' has conflicting history bytes'
            else:
                dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(old)
            treatment='prior bytes retained; current file extends or supersedes this version'
        ledger.append(dict(checkpoint=number,original_path=str(rel),sha256=oldsha,
                           retained_path=location.as_posix(),treatment=treatment))
path=ROOT/'checkpoint_history.csv'
earlier=[]
if path.exists():
    with path.open(newline='') as f:
        earlier=[r for r in csv.DictReader(f) if r['checkpoint']!=number]
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['checkpoint','original_path','sha256','retained_path','treatment'])
    w.writeheader();w.writerows(earlier+ledger)
print({'checkpoint':number,'members':len(ledger),
       'archived_changed_members':sum(r['treatment'].startswith('prior bytes') for r in ledger)})
