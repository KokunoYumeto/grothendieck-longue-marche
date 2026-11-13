#!/usr/bin/env python3
"""Recreate exact duplicate evidence PNGs listed in IMAGE_ALIASES.tsv."""
from pathlib import Path
import csv,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2]
def main():
    path=ROOT/'work/records/IMAGE_ALIASES.tsv'
    if not path.exists():print('No image alias inventory is present.');return
    with path.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    for row in rows:
        for key in ['alias_path','stored_path']:
            p=Path(row[key])
            if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe relative path')
        source=ROOT/row['stored_path'];target=ROOT/row['alias_path'];data=source.read_bytes()
        if len(data)!=int(row['bytes']) or hashlib.sha256(data).hexdigest()!=row['sha256']:raise ValueError('Stored image hash mismatch')
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and target.read_bytes()!=data:raise ValueError('Different file already occupies the alias path')
        if not target.exists():shutil.copyfile(source,target)
    print(f'Restored or verified {len(rows)} exact image aliases.')
if __name__=='__main__':main()
