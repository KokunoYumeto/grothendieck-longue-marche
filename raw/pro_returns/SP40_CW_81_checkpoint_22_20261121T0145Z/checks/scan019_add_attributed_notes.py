#!/usr/bin/env python3
"""Bounded post-QA repair: add the root-requested attributed content paragraph."""
from pathlib import Path
import copy
import hashlib
import json

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
path=OUT/'scan019_record_draft.json'
sha=lambda b:hashlib.sha256(b).hexdigest()
before_bytes=path.read_bytes()
before_sha=sha(before_bytes)
assert before_sha=='58e83613f93bfd9b727f5bef51f7e8a3bfda9c082b612db02245b428e6f21931'
record=json.loads(before_bytes)
original=copy.deepcopy(record)
paragraph=r"""The manuscript calls the cases $\operatorname{card} I=0,1$ trivial and says that $\operatorname{card} I=2$ has already been seen. It states that it remains to show that the two written intersections $U_{J,i}\cap\Sigma_i^+$ and $U_{J,i}\cap\Sigma_i^-$ have « la forme précédente ». Its brace records $\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha$. In the lower prose, it restricts the written union to $\alpha\in K_0$ satisfying the stated $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ relation; the sheet then writes « i.e. » followed by $\Sigma_\alpha^+\not\subset\Sigma_i^+$. It names that recorded set $K_1$ and ends with $U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)$. These are attributed manuscript assertions, including the « i.e. » relationship; no equivalence or proof check was performed."""
head,tail=record['notes'].split('\n\n',1)
insertion_char_start=len(head)+2
record['notes']=head+'\n\n'+paragraph+'\n\n'+tail
assert {k for k in record if record[k]!=original[k]}=={'notes'}
assert record['notes'].replace(paragraph+'\n\n','',1)==original['notes']
after_bytes=(json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode()
path.write_bytes(after_bytes)
mapping=json.loads((OUT/'scan019_final_source_map.json').read_text())
source_attachments=[]
for source_id in ['019.01','019.02','019.09','019.14','019.17']:
    source_attachments.append(dict(source_inventory_identity=source_id,
        exact_source_attachments=mapping['original_inventory_source_attachments'][source_id]))
provenance=dict(scan=19,scope='One root-requested notes paragraph after the completed frozen QA pass; no ink/count/TeX/map change.',
    changed_record_fields=['/notes'],prior_record_sha256=before_sha,new_record_sha256=sha(after_bytes),
    prior_notes_sha256_utf8=sha(original['notes'].encode()),new_notes_sha256_utf8=sha(record['notes'].encode()),
    inserted_paragraph=paragraph,inserted_paragraph_sha256_utf8=sha(paragraph.encode()),
    notes_char_start=insertion_char_start,notes_char_end=insertion_char_start+len(paragraph),
    placement='Inserted after the existing first notes paragraph; every pre-existing notes byte is retained in order.',
    exact_selected_source_attachments=source_attachments,
    root_instruction=dict(source='Root session message after frozen-pass completion',
        text='Please now apply the deferred attributed mathematical-content paragraph only, update its exact provenance and final record hash, and send changed field/text/hash to root and qa019_source for bounded follow-up. Keep every other selected field and TeX unchanged.'),
    content_order_instruction=dict(source='Root session message before pass completion',
        text="For the post-QA notes paragraph, ensure the recorded restriction is hatted Sigma_alpha^+ not-subset hatted Sigma_i^+, followed by the sheet's i.e. unhatted version, then named K1 and final complement. Attribute these assertions and state no equivalence/proof check was performed."),
    unchanged_draft_sha256=mapping['final_sha256'],unchanged_map_sha256=sha((OUT/'scan019_final_source_map.json').read_bytes()),
    unchanged_counts=record['counts'],main_adjudicated=False,follow_up_scope='Only inserted notes paragraph, exact source attribution and changed-field/hash correspondence.')
ppath=OUT/'scan019_notes_addition_provenance.json'
ppath.write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
fpath=OUT/'scan019_source_fingerprints.json'
f=json.loads(fpath.read_text())
f['prepared_files']['scan019_record_draft.json']={'sha256':sha(after_bytes)}
f['prepared_files']['scan019_notes_addition_provenance.json']={'sha256':sha(ppath.read_bytes())}
f['prior_frozen_record_sha256']=before_sha
f['record_stage']='Root-requested notes paragraph added after the completed frozen source pass; bounded notes-only follow-up and root approval pending.'
fpath.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changed_fields=['/notes'],record_sha256=sha(after_bytes),provenance_sha256=sha(ppath.read_bytes()),
    inserted_paragraph=paragraph,all_other_record_fields_unchanged=True),ensure_ascii=False))
