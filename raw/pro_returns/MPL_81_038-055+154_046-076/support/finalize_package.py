"""Verify immutable transcription and assemble the requested final archive."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, importlib.util, json, re, subprocess, zipfile

root=Path('/workspace/scratch/89f8415d3ab0')
deliver=root/'deliver'
prefix='MPL_81_038-055+154_046-076'
now=lambda:datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
frozen=json.loads((deliver/'records/frozen_sha256.json').read_text())
actual={name:hashlib.sha256((deliver/name).read_bytes()).hexdigest() for name in frozen['files']}
assert actual==frozen['files'], 'Frozen transcription hash mismatch; never repair from context.'
pages=sorted((deliver/'pages').glob('*.tex'))
combined=(deliver/f'{prefix}_transcription.tex').read_bytes()
assert combined==b''.join(p.read_bytes() for p in pages)
assert len(pages)==31

spec=importlib.util.spec_from_file_location('package_validator',root/'support/validate_package.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
structural=module.validate(deliver)
assert structural['ok'], structural
notes=(deliver/f'{prefix}_notes.md').read_text()
note_ids=re.findall(r'^### ([CABDOQT]\d{2}) —',notes,re.M)
assert len(note_ids)==110 and len(set(note_ids))==110
queries=json.loads((deliver/'records/context_queries.json').read_text())['items']
assert {x['id'] for x in queries}==set(note_ids)
assert all(x['total_matching_lines'] for x in queries)

for filename in [f'{prefix}_notes.md',f'{prefix}_doubts.md']:
    width=None
    for i,line in enumerate((deliver/filename).read_text().splitlines(),1):
        if line.startswith('|'):
            count=len(re.findall(r'(?<!\\)\|',line))
            if width is None:width=count
            assert count==width, (filename,i,'Markdown table width',count,width)
        else:width=None

doubts=json.loads((deliver/'records/doubt_occurrences.json').read_text())
# The supplied uncertainty record uses the extractor's keyed object.
if isinstance(doubts,dict):
    occurrences=doubts.get('occurrences',doubts.get('items',[]))
else:occurrences=doubts
assert len(occurrences)==507, ('doubt count',len(occurrences))
clean_source=module.tex_without_comments(combined.decode('utf-8'))
assert clean_source.count('\\unsure{')==507
assert combined.count(b'\\illegible{')==0
timestamp=now()
report={'utc':timestamp,'ok':True,'frozen_utc':frozen['frozen_utc'],
 'frozen_files_verified':len(actual),'all_frozen_hashes_unchanged':True,
 'combined_bytes':len(combined),'combined_sha256':hashlib.sha256(combined).hexdigest(),
 'page_count':len(pages),'doubt_occurrences':len(occurrences),'illegible_occurrences':0,
 'research_note_items':len(note_ids),'notes_words':len(notes.split()),
 'context_queries':len(queries),'markdown_table_widths_checked':True,
 'structural':structural,
 'compile_record':'support/validation/compile_07_final_prefreeze.json',
 'compile_scope':'31 sources;40 validation PDF pages;no source errors,overfull boxes,or missing glyphs;4 underfull warnings.',
 'limits':'Mechanical checks do not certify paleographic accuracy or mathematical proofs.'}
(deliver/'records/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(deliver/'records/current_state.md').write_text(
 '# Completed work state\n\n'
 f'Final verification: {timestamp}.\n\n'
 'All31 retained cote154 scans046–076 are transcribed and second-audited by the primary reader. '
 'No OCR; no parallel transcription or scan reading. '
 'All32 frozen hashes are unchanged after context research.\n\n'
 'Completed: combined fragment;31 page files;507-entry doubts register with notation table and abbreviation glossary;'
 '693-row all-yes inventory;110-item research notes with source comparisons and APA references;progress log;validation records.\n\n'
 'Context opened only after freezing. Research-only assistants compared context and literature; no frozen source edits occurred.\n\n'
 'The requested final ZIP is being assembled. Its save is the final delivery step. '
 'Checkpoint01 was saved at the first hourly boundary. If the final save crosses14:34:29UTC, '
 'checkpoint02 must be saved at that hourly boundary, never as a section checkpoint.\n')
with (deliver/'progress.log').open('a') as f:
    f.write(f'research notes completed {timestamp};110 items;110 recorded context searches;context/source locator audits incorporated\n')
    f.write(f'final structural validation passed {timestamp};31 pages;693 inventory rows all yes;507 unsure;0 illegible\n')
    f.write(f'frozen hashes verified unchanged {timestamp};31 page files and combined transcription;32 of32 match\n')
    f.write(f'final package assembled {timestamp}\n')

included=[]
for p in sorted(deliver.rglob('*')):
    if p.is_file():included.append((p,str(p.relative_to(deliver))))
# Preserve textual work records and scripts; generated render binaries are
# validation intermediates, while every manuscript graphic is native TikZ.
extensions={'.py','.md','.tex','.csv','.json','.log','.stdout','.txt'}
for p in sorted((root/'support').rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts and p.suffix in extensions:
        included.append((p,str(p.relative_to(root))))
manifest={'utc':timestamp,'members':[name for _,name in included],
          'original_input_archives_and_images_included':False,
          'generated_validation_binaries_included':False}
manifest_path=deliver/'records/package_manifest.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
included.append((manifest_path,'records/package_manifest.json'))
path=root/f'{prefix}.zip'
if path.exists():raise RuntimeError('Refusing to overwrite existing final ZIP.')
with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p,name in included:z.write(p,name)
with zipfile.ZipFile(path) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))
    for name,digest in frozen['files'].items():
        assert hashlib.sha256(z.read(name)).hexdigest()==digest
print(json.dumps({'zip':str(path),'bytes':path.stat().st_size,'members':len(included),
                  'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                  'validation':{k:report[k] for k in ['ok','frozen_files_verified','page_count','doubt_occurrences','research_note_items','notes_words']}},ensure_ascii=False))
