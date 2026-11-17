"""Install reviewed37 codec branches, retaining the complete old packager.

This creates no archive and starts no compressor. Actual size and decoder
verification are separate required operations, not inferred here.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, shutil

r=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=r/'code/package_checkpoint.py'
new=r/'work_root/package_checkpoint37_proposed.py'
assert sha(old)=='7c753ea7355dcb2dc511ee31f6e3814121784835fe987fb0cd2df37cf3abb447'
assert sha(new)=='09388957e560ea6c3800d2b2f61febab64c12f89a307ceccfc12add31889cc64'
review_path=r/'work_CE/review_checkpoint37_codec_packager.json'
review=json.loads(review_path.read_text())
assert review['result']=='PASS_COMPLETE_SOURCE_ONLY_REVIEW'
for row in review['sources']:
    assert sha(r/row['path'])==row['sha256']
assert review['predecessor']['sha256']==sha(old)
ast.parse(new.read_text())
backup=r/'records/checkpoint37_before_codec_policy'
backup.mkdir(exist_ok=False)
shutil.copy2(old,backup/old.name)
old.write_bytes(new.read_bytes())
assert sha(old)==sha(new)
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
    source=str(new.relative_to(r)),installed=str(old.relative_to(r)),sha256=sha(old),
    retained_predecessor=str((backup/old.name).relative_to(r)),
    predecessor_sha256=sha(backup/old.name),
    independent_review=dict(path=str(review_path.relative_to(r)),sha256=sha(review_path)),
    image_dictionary_bytes=536870912,document_dictionary_bytes=268435456,
    data_dictionary_bytes=67108864,older_branches_preserved=True,
    creates_archive=False,starts_encoder=False,size_success_claimed=False)
target=r/'records/checkpoint37_codec_policy_install.json'
with target.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps(record,indent=2))
