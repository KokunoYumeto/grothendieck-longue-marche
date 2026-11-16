from pathlib import Path
import csv, hashlib
base=Path(__file__).resolve().parents[2]/'background'
rows=list(csv.DictReader((base/'MANIFEST.tsv').open(),delimiter='\t'))
bad=[]
for r in rows:
    p=base/r['path_in_zip']
    b=p.read_bytes()
    if len(b)!=int(r['bytes']) or hashlib.sha256(b).hexdigest()!=r['sha256']:
        bad.append(r['path_in_zip'])
print('Manifest entries:',len(rows))
print('Size and SHA-256 mismatches:',len(bad))
for p in bad: print(p)
assert not bad
