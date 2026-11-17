from pathlib import Path
import csv, hashlib
base=Path(__file__).resolve().parents[2]/'background'
rows=list(csv.DictReader((base/'MANIFEST.tsv').open(),delimiter='\t'))
errors=[]
for row in rows:
 p=base/row['file']; data=p.read_bytes()
 if len(data)!=int(row['bytes']): errors.append((row['file'],'size'))
 if hashlib.sha256(data).hexdigest()!=row['sha256']: errors.append((row['file'],'hash'))
print('Manifest entries:',len(rows))
print('Verified size and SHA-256:',len(rows)-len(errors))
print('Errors:',errors)
assert not errors
