#!/usr/bin/env python3
"""Resume the standard source-row collection without altering its saved prefix."""
from pathlib import Path
import hashlib,json
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
data=CODE/'pbc_quotient86_standard_recollection.json'
raw=data.read_bytes();pause=json.loads((CODE/'pbc_quotient86_standard_recollection_checkpoint13_pause.json').read_text())
assert sha(data)==pause['raw_sha256'] and len(raw)==pause['raw_bytes']
done=json.loads(raw+b'\n]\n');assert len(done)==pause['complete_source_records']
old=CODE/'pbc_quotient86_standard_recollection.g';text=old.read_text()
prefix,rest=text.split('PBC_leaves:=',1);leaftext,post=rest.split(';;\nAssert',1)
leaves=json.loads(leaftext);assert len(leaves)==9083
for row,leaf in zip(done,leaves):assert row[:3]==[leaf[1],leaf[2],leaf[3]]
k=len(done);mismatch=sum(not r[4] for r in done)
prefix=prefix.replace('PBC_recollect_count:=0;; PBC_recollect_mismatches:=0;;',
                      f'PBC_recollect_count:={k};; PBC_recollect_mismatches:={mismatch};;')
opening='PrintTo(PBC_recollect_path,"[\\n");'
assert prefix.count(opening)==1;prefix=prefix.replace(opening,'# Existing complete record prefix is preserved byte-for-byte.')
new=CODE/'pbc_quotient86_standard_recollection_resume13.g'
new.write_text(prefix+'PBC_leaves:='+json.dumps(leaves[k:],separators=(',',':'))+';;\nAssert'+post)
out=dict(status='Prepared exact continuation from checkpoint13 prefix',
         generator_sha256=sha(__file__),original_program_sha256=sha(old),
         preserved_prefix_sha256=sha(data),preserved_prefix_bytes=len(raw),
         preserved_complete_records=k,remaining_templates=len(leaves)-k,
         continuation_program_sha256=sha(new),
         scope='Only fresh standard source recollection. No quotient Hopf identity is claimed.')
(CODE/'pbc_quotient86_standard_recollection_resume13.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
