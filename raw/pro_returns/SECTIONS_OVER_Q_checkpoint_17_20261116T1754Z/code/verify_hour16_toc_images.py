#!/usr/bin/env python3
"""Verify exact pixel identity of reviewed body pages after two TOC-label edits."""
from pathlib import Path
import hashlib,json
import fitz
w=Path(__file__).resolve().parents[1];q=w/'qa/hour16'
old=json.loads((q/'pre_toc_render_record.json').read_text())
new=json.loads((q/'render_record.json').read_text())
before=json.loads((q/'pre_toc_image_hashes.json').read_text())
assert old['pdf_pages']==new['pdf_pages']==661
assert old['rendered_pages']==new['rendered_pages']
assert old['required_full_resolution_pages']==new['required_full_resolution_pages']
doc=fitz.open(w/'SECTIONS_OVER_Q_paper.pdf')
for n in [601,602]:
    doc[n-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(q/'full'/f'page_{n:03d}.png')
paths=[f'page_{n:03d}.png' for n in new['rendered_pages']]
paths += [f'full/page_{n:03d}.png' for n in new['required_full_resolution_pages']+[601,602]]
paths += [Path(p).name for p in new['contact_parts']]
current={p:hashlib.sha256((q/p).read_bytes()).hexdigest() for p in paths}
changed=[p for p in paths if current[p]!=before[p]]
assert set(changed)=={'page_001.png','page_003.png','full/page_001.png','full/page_003.png','contact_part_1.png'},changed
record=dict(previous_pdf_sha256=old['pdf_sha256'],final_pdf_sha256=new['pdf_sha256'],
            pdf_pages=661,compared_images=len(paths),changed_images=changed,
            identical_images=[p for p in paths if p not in changed],
            final_image_hashes=current,
            result='PASS: every reviewed body image and every unchanged contact sheet is byte-identical. Only the two repaired TOC pages and their first contact sheet changed.')
(q/'toc_image_equivalence.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['identical_images','final_image_hashes']},indent=2))
