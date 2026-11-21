"""Correct one joined TeX control word to encode the already audited bar and K.

The earlier transcription hash manifest is preserved byte-for-byte. The final
manifest is written separately after all descriptive reconciliation is complete.
No source reading, fixed blind input/return, or audit decision is revised here.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
from assemble import build
B=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
jp=B/'serialization_corrections.json';assert not jp.exists()
frozen=B/'transcription_sha256.json';frozen_bytes=frozen.read_bytes();manifest=json.loads(frozen_bytes)
p=B/'pages/149_scan075.tex';before=p.read_text();old=r'\midK';new=r'\mid K'
assert sha(p)==manifest['files']['pages/149_scan075.tex']
assert before.count(old)==1
rp=B/'reviews/149_scan075.json';r=json.loads(rp.read_text())
audit=next(x for x in r['audit_adjudications'] if x['box']=='B15')
assert new in audit['final']
assert old not in audit['final']
matches=[x for x in r['notation'] if old in x['form']];assert len(matches)==1
nr=matches[0];assert nr['form'].count(old)==1
old_note=nr['form'];nr['form']=nr['form'].replace(old,new)
before_hash=sha(p);combined_before=sha(B/'SP86_C13_149_transcription.tex')
p.write_text(before.replace(old,new))
r['notes'].append('Serialization record: the space separating the TeX control word \\mid from the following K was restored after the first hash recording. The vertical bar and K are exactly the reading already fixed in audit B15 and change P16b; no manuscript reading or material count changes. The earlier hash manifest is preserved, and the final hash manifest is recorded separately.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
build()
record=dict(utc=stamp,page='149_scan075',kind='TeX control-word delimiter only',before=old,after=new,source_reading=audit['final'],source_crop=audit['crop'],source_coords=audit['coords'],evidence=audit['evidence'],reason='A TeX alphabetic control word consumes the contiguous letters midK. The supplied preamble defines no midK command. Separating it as \\mid followed by the letter K gives the bar and K already recorded in B15; the added source-code space supplies no manuscript glyph.',page_before_sha256=before_hash,page_after_sha256=sha(p),combined_before_sha256=combined_before,combined_after_sha256=sha(B/'SP86_C13_149_transcription.tex'),notation_before=old_note,notation_after=nr['form'],preserved_earlier_manifest='transcription_sha256.json',earlier_manifest_sha256=hashlib.sha256(frozen_bytes).hexdigest(),final_manifest='transcription_sha256_final.json',material_counts_changed=False,fixed_audit_records_changed=False)
jp.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
assert frozen.read_bytes()==frozen_bytes
with (B/'progress.log').open('a') as f:
 f.write(f'transcription freeze superseded {stamp}: one TeX control-word separator restored at scan075 (mid followed by K), matching fixed audit B15; earlier transcription_sha256.json preserved; final freeze will use transcription_sha256_final.json\n')
print(json.dumps({'utc':stamp,'page':'149_scan075','source_reading_changed':False,'serialization_corrected':True,'earlier_manifest_preserved':True}))
