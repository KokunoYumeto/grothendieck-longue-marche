#!/usr/bin/env python3
"""Preserve the failed visual check and split long coverage rows verbatim."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent.parent
record = ROOT / 'research/checkpoint08_coverage_repair.json'
assert not record.exists()
assembler = ROOT / 'code/assemble_register.py'
before = assembler.read_text()
saved = ROOT / 'research/assemble_register_before_checkpoint08_coverage.py'
assert not saved.exists()
saved.write_text(before)
qa = json.loads((ROOT / 'research/visual_qa.json').read_text())
assert qa['page_count'] == 444
qa['visually_inspected'] = False
qa['inspected_contact_sheets'] = [r['file'] for r in qa['contact_sheets']]
qa['full_resolution_inspected_pages'] = [234, 237, 241, 242, 243, 244,
    245, 246, 248, 250, 251, 252, 386, 390, 391, 392, 393, 396,
    399, 401, 403, 405, 437, 438]
qa['inspection_notes'] = [
    'All twenty contact sheets were actually viewed by root.',
    'The twenty-four listed pages were actually viewed at full resolution.',
    'The proof displays are clear. Pages 437 and 438 have coverage rows extending into the footer and beyond the page, although the log reports no overfull box. This build is rejected for delivery.',
]
qa['image_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
    for p in (ROOT / 'build/renders').glob('*.png')}
(ROOT / 'research/checkpoint08_seventh_visual_qa_failed.json').write_text(
    json.dumps(qa, indent=2) + '\n')
failures = ROOT / 'research/checkpoint08_coverage_visual_failures'
failures.mkdir()
for name in ['page_437.png', 'page_438.png', 'contact_sheet_20.png']:
    shutil.copy2(ROOT / 'build/renders' / name, failures / name)
old = "for a,b,c,d in TASKS:\n    coverage+=tex_escape(a)+' & '+tex_escape(b)+' & '+tex_text(c+'. '+d)+r' \\\\'+'\\n'\n"
new = '''def coverage_chunks(text, limit=900):
    # Retain every character and only split at whitespace outside inline math.
    chunks = []
    start = 0
    while len(text) - start > limit:
        math = False
        candidates = []
        for pos in range(start, min(len(text), start + limit)):
            if text[pos] == '$' and (pos == 0 or text[pos-1] != '\\\\'):
                math = not math
            if text[pos].isspace() and not math:
                candidates.append(pos + 1)
        assert candidates, text[start:start+limit]
        end = candidates[-1]
        chunks.append(text[start:end])
        start = end
    chunks.append(text[start:])
    assert ''.join(chunks) == text
    assert all(chunk.count('$') % 2 == 0 for chunk in chunks)
    return chunks

for a,b,c,d in TASKS:
    for index, chunk in enumerate(coverage_chunks(c+'. '+d)):
        item = a if index == 0 else a + ' cont.'
        statements = b if index == 0 else ''
        coverage+=tex_escape(item)+' & '+tex_escape(statements)+' & '+tex_text(chunk)+r' \\\\'+'\\n'
'''
assert before.count(old) == 1
after = before.replace(old, new)
assembler.write_text(after)
record.write_text(json.dumps({
    'reason': 'Actual visual footer collision and clipped coverage text on pages 437 and 438.',
    'old_generator': old, 'new_generator': new,
    'complete_original_assembler': str(saved.relative_to(ROOT)),
    'assembler_before_sha256': hashlib.sha256(before.encode()).hexdigest(),
    'assembler_after_sha256': hashlib.sha256(after.encode()).hexdigest(),
    'mathematical_changes': False,
    'preservation_check': 'Each original task-state string equals the concatenation of its output chunks, character for character.',
}, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'preserved_failed_pages': [437, 438],
                  'row_chunk_limit_characters': 900}, indent=2))
