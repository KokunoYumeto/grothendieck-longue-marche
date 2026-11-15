"""Render checkpoint07 proof pages and record the final build diagnostics.

The resulting PNGs are inspected separately; rendering is not visual review.
"""
from pathlib import Path
import json
import re
import fitz

root = Path(__file__).resolve().parents[1]
doc = fitz.open(root / 'LM8_PUSH_paper.pdf')
log = (root / 'build/LM8_PUSH_paper.log').read_text()
console = (root / 'build/build_console.out').read_text()
new_ids = [f'A.{i}' for i in range(41, 48)] + ['C.32'] + [f'D.{i}' for i in range(58, 62)]
headings = []
for i, page in enumerate(doc):
    page_text = page.get_text()
    for match in re.finditer(r'(?m)^([A-H]\.[0-9]+)\. ', page_text):
        # A sentence can begin with a cross-reference; a statement heading
        # also has its displayed status immediately after its title.
        after = page_text[match.end():match.end() + 200]
        if re.search(r'\b(?:Proved|Open|Known|Refuted)\.', after):
            headings.append((match.group(1), i + 1))
findings = {}
pages = {1, 25, 50, 75, 86, 91, 98, 120, 155, 180, 215,
         250, 273, 278, 300, 304, 310, len(doc)}
for key in new_ids:
    matches = [j for j, (sid, _) in enumerate(headings) if sid == key]
    if len(matches) != 1:
        raise RuntimeError(f'Expected one statement heading for {key}: {matches}')
    j = matches[0]
    first = headings[j][1]
    last = headings[j + 1][1] if j + 1 < len(headings) else first
    findings[key] = {'first_page': first, 'through_page': last}
    pages.update({first, min(first + 1, last), (first + last) // 2, last})
out = root / 'qa/checkpoint07'
out.mkdir(parents=True, exist_ok=True)
for pageno in sorted(pages):
    doc[pageno - 1].get_pixmap(matrix=fitz.Matrix(1.25, 1.25)).save(
        out / f'page_{pageno:03d}.png')
overfull = [float(v) for v in re.findall(r'Overfull \\hbox \((\d+(?:\.\d+)?)pt', log)]
all_overfull = [float(v) for v in re.findall(r'Overfull \\hbox \((\d+(?:\.\d+)?)pt', console)]
record = {
    'pdf_pages': len(doc),
    'rendered_pages': sorted(pages),
    'new_statement_pages': findings,
    'all_pass_overfull_boxes': len(all_overfull),
    'all_pass_overfull_boxes_above_2pt': sum(x > 2 for x in all_overfull),
    'final_overfull_boxes': len(overfull),
    'final_overfull_boxes_above_2pt': sum(x > 2 for x in overfull),
    'final_warning_count': len(re.findall('Warning', log)),
    'final_undefined_count': len(re.findall('undefined', log)),
    'visual_review': 'Recorded separately after viewing every rendered page.',
}
(out / 'rendered_pages.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
