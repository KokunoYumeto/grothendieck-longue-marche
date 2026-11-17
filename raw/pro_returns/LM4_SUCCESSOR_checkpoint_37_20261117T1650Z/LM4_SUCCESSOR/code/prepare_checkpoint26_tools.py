"""Prepare size/restoration tools and retain the new authored initial PDF."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
p=root/'code/package_checkpoint.py'
original=p.read_bytes()
backup=root/'records/checkpoint26_before_authored_pdf_exception_package_checkpoint.py.retained.txt'
assert not backup.exists()
backup.write_bytes(original)
old="{'B118_initial_spacing.pdf','B122_initial_layout.pdf'}"
new="{'B118_initial_spacing.pdf','B122_initial_layout.pdf','B128_initial_comma.pdf'}"
assert original.decode().count(old)==1
p.write_text(original.decode().replace(old,new))

p=root/'code/estimate_checkpoint26_size.py'
assert not p.exists()
s=(root/'code/estimate_checkpoint25_size.py').read_text()
s=s.replace('checkpoint25','checkpoint26').replace('checkpoint_24','checkpoint_25').replace('checkpoint24','checkpoint25')
assert s.count(old)==1
p.write_text(s.replace(old,new))

p=root/'code/verify_checkpoint26_system_tars.py'
assert not p.exists()
s=(root/'code/verify_checkpoint25_system_tars.py').read_text()
s=s.replace('checkpoint25','checkpoint26').replace('checkpoint_25','checkpoint_26')
p.write_text(s)

record={
 'scope':'Retain all authored preview/initial PDFs at their original paths; no prior archive changed.',
 'prior_packager_sha256':hashlib.sha256(original).hexdigest(),
 'preserved_prior_packager':str(backup.relative_to(root)),
 'added_authored_exception':'work_DE/B128_initial_comma.pdf',
 'corresponding_preserved_source':'work_DE/B128_initial_comma_source.tex',
 'pdf_sha256':hashlib.sha256((root/'work_DE/B128_initial_comma.pdf').read_bytes()).hexdigest(),
 'reason':'The authored initial PDF has a differently named retained source and must not be classified as a third-party source copy.',
 'creates_zip':False,
}
(root/'records/checkpoint26_authored_pdf_retention.json').write_text(json.dumps(record,indent=2)+'\n')
print('Prepared checkpoint26 size/restoration tools; retained the new authored initial PDF.')
