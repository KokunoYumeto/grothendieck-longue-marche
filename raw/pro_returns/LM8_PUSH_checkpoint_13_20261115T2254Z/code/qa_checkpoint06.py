"""Record log checks and render the checkpoint06 paper for human visual QA.

Rendering is not a substitute for the separately recorded visual inspection.
"""
from pathlib import Path
import json
import re
import fitz

root = Path(__file__).resolve().parents[1]
doc = fitz.open(root / 'LM8_PUSH_paper.pdf')
log = (root / 'build/LM8_PUSH_paper.log').read_text()
findings = {}
for key in ['A.37.', 'A.38.', 'A.39.2', 'A.40.', 'C.30.',
            'D.53.', 'D.54.', 'D.55.', 'D.56.', 'D.57.']:
    findings[key] = [i + 1 for i, page in enumerate(doc)
                     if key in page.get_text()]
pages = {1, 25, 104, 132, 180, 215, 240, 242, 248, 250, 260, 275, len(doc)}
for key, matches in findings.items():
    if matches:
        pages.update([matches[0], matches[len(matches)//2], matches[-1]])
out = root / 'qa/checkpoint06'
out.mkdir(parents=True, exist_ok=True)
for pageno in sorted(pages):
    doc[pageno - 1].get_pixmap(matrix=fitz.Matrix(1.25, 1.25)).save(
        out / f'page_{pageno:03d}.png')
overfull = [float(v) for v in re.findall(r'Overfull \\hbox \((\d+(?:\.\d+)?)pt', log)]
record = {
    'pdf_pages': len(doc),
    'rendered_pages': sorted(pages),
    'new_statement_pages': findings,
    'final_overfull_boxes': len(overfull),
    'final_overfull_boxes_above_2pt': sum(x > 2 for x in overfull),
    'final_warning_count': len(re.findall('Warning', log)),
    'final_undefined_count': len(re.findall('undefined', log)),
    'visual_review': 'Recorded separately after viewing every rendered page.',
}
(out / 'rendered_pages.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
