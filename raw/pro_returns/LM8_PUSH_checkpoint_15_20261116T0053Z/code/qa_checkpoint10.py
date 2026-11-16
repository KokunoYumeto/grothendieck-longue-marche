"""Render checkpoint10 proof pages and record final build diagnostics.

Rendering is not visual review. Every rendered page is inspected separately.
"""
from pathlib import Path
import json
import re
import fitz

root = Path(__file__).resolve().parents[1]
doc = fitz.open(root / 'LM8_PUSH_paper.pdf')
log = (root / 'build/LM8_PUSH_paper.log').read_text()
console = (root / 'build/build_console.out').read_text()
new_ids = ([f'A.{i}' for i in range(55, 59)]
           + ['C.40'] + [f'D.{i}' for i in range(70, 74)])
changed_ids = ['A.45', 'A.54', 'C.5', 'D.5', 'D.29', 'D.41']
headings = []
for i, page in enumerate(doc):
    page_text = page.get_text()
    for match in re.finditer(r'(?m)^([A-H]\.[0-9]+)\.\s+', page_text):
        after = page_text[match.end():match.end() + 220]
        if re.search(r'\b(?:Proved|Open|Known|Refuted)\.', after):
            headings.append((match.group(1), i + 1))
findings = {}
pages = {1, len(doc), *range(25, len(doc), 25)}
for key in new_ids:
    matches = [j for j, (sid, _) in enumerate(headings) if sid == key]
    if len(matches) != 1:
        raise RuntimeError(f'Expected one statement heading for {key}: {matches}')
    j = matches[0]
    first = headings[j][1]
    last = headings[j + 1][1] if j + 1 < len(headings) else first
    findings[key] = {'first_page': first, 'through_page': last}
    pages.update({first, min(first + 1, last), (first + last) // 2, last})
for key in changed_ids:
    first = next(page for sid, page in headings if sid == key)
    pages.update({first, min(first + 1, len(doc))})
out = root / 'qa/checkpoint10'
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
    'changed_existing_statement_ids': changed_ids,
    'all_pass_overfull_boxes': len(all_overfull),
    'all_pass_overfull_boxes_above_2pt': sum(x > 2 for x in all_overfull),
    'final_overfull_boxes': len(overfull),
    'final_overfull_boxes_above_2pt': sum(x > 2 for x in overfull),
    'final_warning_count': len(re.findall('Warning', log)),
    'final_undefined_count': len(re.findall('undefined', log)),
    'final_missing_character_count': log.count('Missing character'),
    'visual_review': 'Recorded separately after viewing every rendered page.',
}
(out / 'rendered_pages.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
