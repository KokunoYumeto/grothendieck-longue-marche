#!/usr/bin/env python3
"""One root-requested prose enrichment; preserve all selected decision data."""
from pathlib import Path
import copy
import hashlib
import json
import sys
sys.dont_write_bytecode=True
from scan020_prepare_sources import span

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=OUT/'scan020_record_draft.json'
before_bytes=rp.read_bytes()
r=json.loads(before_bytes)
before=copy.deepcopy(r)
note_path='out/checks/scan020_root_note_selection.md'
note=(BASE/note_path).read_text()
start=note.index('Grothendieck continues')
end=note.index('\n\nUse the four frozen')
selected=note[start:end]
entries=r['attributed_content_note']['entries']
def label(a):return f"{a['path']} characters [{a['char_start']},{a['char_end']})"
old_paragraphs=[e['text']+' Exact selected source: '+ '; '.join(label(a) for a in e['source_attachments'])+'.' for e in entries]
old_prefix='\n\n'.join(old_paragraphs)+'\n\n'
assert r['notes'].startswith(old_prefix),'Expected unchanged assembler-note prefix before enrichment.'
tail=r['notes'][len(old_prefix):]
references='Exact frozen content entries retained: '+'; '.join(e['id']+': '+', '.join(label(a) for a in e['source_attachments']) for e in entries)+'.'
r['notes']=selected+'\n\n'+references+'\n\n'+tail
r['root_selected_content_note']=dict(
    root_source=span(note_path,note,source_sha256_utf8=sha(BASE/note_path)),
    selected_prose_source=span(note_path,note,start,end,source_sha256_utf8=sha(BASE/note_path)),
    source_sha256_utf8=sha(BASE/note_path),selected_prose=selected,
    retained_CONTENT020_source_entries=copy.deepcopy(entries),
    margin_archive_selected_sources={d['id']:copy.deepcopy(d['final_source_attachment']) for d in r['decisions'] if d['id'] in ['L020-38','L020-39']},
    scope='Root-selected attributed prose supplements the unchanged assembler source entries. No TeX, map, decision, count, doubt or inventory change.',
    main_approved=False)
r['processing_provenance'].setdefault('record_enrichment_history',[]).append(dict(
    original_record_sha256=hashlib.sha256(before_bytes).hexdigest(),
    original_notes_sha256_utf8=hashlib.sha256(before['notes'].encode()).hexdigest(),
    root_note_source=note_path,root_note_sha256=sha(BASE/note_path),
    scope='Single bounded pre-QA content-note enrichment; the four CONTENT020 entries and all selected data remain unchanged.'))
for k in ['decisions','counts','doubts','inventory','C_source_rows','attributed_content_note','selected_draft','selected_source_map']:
    assert r[k]==before[k],k
assert sha(OUT/'scan020_final_draft.tex')==r['selected_draft']['sha256']
assert sha(OUT/'scan020_final_source_map.json')==r['selected_source_map']['sha256']
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
fp=OUT/'scan020_source_fingerprints.json'
f=json.loads(fp.read_text())
f.setdefault('record_freeze_history',[]).append(dict(sha256=hashlib.sha256(before_bytes).hexdigest(),
    scope='Pre-enrichment selected record; superseded only by root-selected prose before record QA permission.'))
f['prepared_files']['scan020_record_draft.json']={'sha256':sha(rp)}
f['prepared_files']['scan020_root_note_selection.md']={'sha256':sha(BASE/note_path)}
f['root_selected_content_note']=dict(path=note_path,sha256=sha(BASE/note_path))
fp.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record_sha256=sha(rp),previous_record_sha256=hashlib.sha256(before_bytes).hexdigest(),
    root_note_sha256=sha(BASE/note_path),draft_sha256=r['selected_draft']['sha256'],map_sha256=r['selected_source_map']['sha256'],
    counts=r['counts'],selected_decisions_counts_doubts_inventory_unchanged=True),ensure_ascii=False))
