#!/usr/bin/env python3
"""Prepare the next hourly capture tools without making an archive."""
from pathlib import Path
import ast
import json

root = Path(__file__).resolve().parents[1]
created = []

def save(name, source):
    path = root / 'code' / name
    assert not path.exists(), path
    ast.parse(source)
    path.write_text(source)
    created.append(name)

for name in ('record_checkpoint16_build.py', 'checkpoint16_integrity.py',
             'assemble_checkpoint16_visual_review.py'):
    source = (root / 'code' / name).read_text().replace('checkpoint16', 'checkpoint17')
    source = source.replace("'checkpoint': 16", "'checkpoint': 17")
    save(name.replace('16', '17'), source)

source = (root / 'code/freeze_checkpoint16.py').read_text()
source = source.replace('checkpoint16', 'checkpoint17').replace('checkpoint_15.zip', 'checkpoint_16.zip')
old = "assert new_ids == ['A.75', 'A.76', 'A.77', 'A.78', 'A.79', 'C.45', 'C.46', 'C.47', 'D.90', 'D.91', 'D.92']"
assert old in source
source = source.replace(old, "expected = json.loads((root / 'notes/checkpoint17_expected_new_ids.json').read_text())\nassert new_ids == expected, (new_ids, expected)")
source = source.replace('Further single-branch p-group geometry, larger section-image loci and later character research stay unregistered in notes; no subsequent candidate enters this frozen paper.',
                        'Further cover families, section-image loci and character research stay unregistered in notes after this freeze; no later candidate enters the frozen paper.')
save('freeze_checkpoint17.py', source)

source = (root / 'code/qa_checkpoint16.py').read_text().replace('checkpoint16', 'checkpoint17')
source = source.replace("changed_ids = ['A.45', 'C.1', 'C.6', 'C.9', 'D.5']", "changed_ids = ['A.45', 'C.6', 'C.9', 'D.5']")
save('qa_checkpoint17.py', source)

source = (root / 'code/prepare_checkpoint16_storage.py').read_text()
source = source.replace('checkpoint16', 'checkpoint17').replace('checkpoint15', 'checkpoint16')
source = source.replace('checkpoint17_pdf_delta_encoding.json', 'checkpoint16_pdf_delta_encoding.json')
source = source.replace("qa['encoded_images'] >= 485", "qa['encoded_images'] >= 544")
source = source.replace("state['paper_pages'] >= 566 and state['paper_statements'] >= 296", "state['paper_pages'] >= 600 and state['paper_statements'] >= 303")
source = source.replace("history['through_checkpoint'] == 15", "history['through_checkpoint'] == 16")
source = source.replace("history['historical_entries'] == 20267", "history['historical_entries'] == 24074")
source = source.replace('assert len(large) == 13', 'assert len(large) == 21')
source = source.replace("large = large + delta['transforms']", "assert [e for e in large if e.get('codec') == 'ZSTD_PDF_DICT01'] == delta['transforms']")
source = source.replace('# added in checkpoint14, remain unchanged. Append eight exact PDF restorations.', '# added in checkpoint14, and the eight prior PDF restorations remain unchanged.')
source = source.replace('2026-11-16T02:00:00Z', '2026-11-16T03:00:00Z')
source = source.replace("'history_through_checkpoint': 15", "'history_through_checkpoint': 16")
source = source.replace('all20267 historical entries', 'all24074 historical entries')
source = source.replace("'new_pdf_delta_transforms': 8", "'retained_pdf_delta_transforms': 8")
save('prepare_checkpoint17_storage.py', source)

source = (root / 'code/checkpoint16_size_delta.py').read_text()
source = source.replace('checkpoint16', 'checkpoint17').replace('checkpoint15', 'checkpoint16').replace('checkpoint_15.zip', 'checkpoint_16.zip')
source = source.replace('default=8', 'default=1')
source = source.replace('Read-only conservative forecast with exact savings from four PDF deltas.', 'Read-only conservative forecast from the previous saved archive; no ZIP is created.')
source = source.replace("delta=json.loads((ROOT/'notes/checkpoint17_pdf_delta_encoding.json').read_text())\n", '')
source = source.replace("    encoded_hashes={r['sha256'] for r in delta['rows']}\n    replaced=[{'path':e['path'],'compressed_bytes':z.getinfo(e['path']).compress_size}\n              for e in manifest['files'] if e['sha256'] in encoded_hashes]", '    replaced=[]')
source = source.replace("skipped.update(e['original_path'] for e in delta['transforms'])\n", '')
source = source.replace('Conservative read-only forecast, retaining prior archive plus new bytes and removing only four exactly verified original PDF encodings; no ZIP created.',
                        'Conservative read-only forecast, retaining the entire prior archive plus new unique bytes and the explicit reserve; no ZIP created.')
save('checkpoint17_size_delta.py', source)

source = (root / 'code/record_checkpoint16_save.py').read_text()
source = source.replace('checkpoint16', 'checkpoint17').replace('checkpoint_16.zip', 'checkpoint_17.zip')
source = source.replace("'checkpoint': 16", "'checkpoint': 17")
source = source.replace("'16' not in catalog", "'17' not in catalog").replace("catalog['16']", "catalog['17']").replace('Checkpoint16 already', 'Checkpoint17 already')
source = source.replace('2026-11-16T03:00:00Z', '2026-11-16T04:00:00Z').replace('2026-11-16T02:00:00Z', '2026-11-16T03:00:00Z')
save('record_checkpoint17_save.py', source)

print(json.dumps({'status': 'PASS', 'created': created, 'syntax_parsed': True,
                  'archive_created': False}, indent=2))
