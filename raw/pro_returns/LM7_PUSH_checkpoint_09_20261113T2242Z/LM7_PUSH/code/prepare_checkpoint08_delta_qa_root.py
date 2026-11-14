#!/usr/bin/env python3
"""Match previously viewed PNGs exactly and render the new synthesis pages."""
from pathlib import Path
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parent.parent
old = json.loads((ROOT / 'research/checkpoint08_seventh_visual_qa_failed.json').read_text())
new = json.loads((ROOT / 'research/visual_qa.json').read_text())
assert new['page_count'] == 448
unchanged, changed = [], []
for page in new['rendered_pages']:
    name = f'page_{page:03d}.png'
    digest = hashlib.sha256((ROOT / 'build/renders' / name).read_bytes()).hexdigest()
    (unchanged if old['image_sha256'].get(name) == digest else changed).append(page)
old_contacts, new_contacts = [], []
for row in new['contact_sheets']:
    name = row['file']
    digest = hashlib.sha256((ROOT / 'build/renders' / name).read_bytes()).hexdigest()
    (old_contacts if old['image_sha256'].get(name) == digest else new_contacts).append(name)
pdf = fitz.open(ROOT / 'LM7_PUSH_paper.pdf')
additional = [2, 3, 123, 124, 254, 255, 256]
assert not set(additional) & set(new['rendered_pages'])
for page in additional:
    pdf[page-1].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False).save(
        ROOT / 'build/renders' / f'page_{page:03d}.png')
record = {
    'current_pdf_sha256': new['pdf_sha256'],
    'previous_viewed_image_record': 'research/checkpoint08_seventh_visual_qa_failed.json',
    'byte_identical_previously_viewed_pages': unchanged,
    'changed_sample_pages_requiring_fresh_view': changed,
    'byte_identical_previously_viewed_contact_sheets': old_contacts,
    'changed_contact_sheets_requiring_fresh_view': new_contacts,
    'additional_full_resolution_pages_requiring_view': additional,
    'no_visual_approval_inferred_by_this_program': True,
}
(ROOT / 'research/checkpoint08_delta_qa.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'unchanged_sample_pages': len(unchanged),
    'changed_sample_pages': len(changed), 'unchanged_contacts': old_contacts,
    'changed_contacts': new_contacts, 'additional_pages': additional}, indent=2))
