#!/usr/bin/env python3
"""Record the final artifact gate; visual inspection is recorded separately."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

base = Path(__file__).resolve().parents[1]
pdf = base / 'FLAGGED_149_paper.pdf'
subprocess.run(['pdftotext', '-layout', str(pdf),
                str(base / 'audit' / 'paper_text.txt')], check=True)
content = (base / 'audit' / 'paper_text.txt').read_text()
pages = content.split('\f')
if not pages[-1].strip():
    pages.pop()
info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
fonts = subprocess.check_output(['pdffonts', str(pdf)], text=True)
pdf_sha256 = hashlib.sha256(pdf.read_bytes()).hexdigest()
visual_record = base / 'audit' / 'visual_review.json'
visual = (json.loads(visual_record.read_text()) if visual_record.exists()
          else {'status': 'Pending manual review of rendered pages'})
if visual.get('status') == 'Passed':
    assert visual['pdf_sha256'] == pdf_sha256, 'Visual review belongs to a different PDF'
results = list(csv.DictReader((base / 'FLAGGED_149_results.csv').open()))
missing = [r['id'] for r in results
           if not re.search(r'(?<![A-Za-z0-9])' + re.escape(r['id']) + r'\.', content)]
assert not missing, missing
report = (base / 'FLAGGED_149_report.md').read_text()
assert report.splitlines()[0] == 'INCOMPLETE'
credit = 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)'
assert credit in report
assert credit in re.sub(r'\s+', ' ', content)
log = (base / 'audit' / 'latex_final.txt').read_text()
problems = [line for line in log.splitlines()
            if re.search(r'Overfull|Underfull|Missing character|Warning|^!', line)]
assert not problems, problems
biblog = (base / 'audit' / 'bibtex_final.txt').read_text()
assert not re.search(r'Warning|error|I couldn.t', biblog, re.I), biblog
assert all(page.strip() for page in pages)
locations = {}
for ident in ['A1', 'B9', 'B14', 'B15', 'C6', 'D5', 'E5',
              'F17.6', 'F17.7', 'G6', 'ZCF12', 'Z142e']:
    locations[ident] = [i+1 for i, page in enumerate(pages)
                        if re.search(r'(?<![A-Za-z0-9])' + re.escape(ident) + r'\.', page)]
summary = {
    'credit_verified': True,
    'incomplete_status_verified': True,
    'pdf_pages': len(pages),
    'pdf_bytes': pdf.stat().st_size,
    'pdf_sha256': pdf_sha256,
    'all_result_identifiers_in_pdf': len(results),
    'missing_result_identifiers': missing,
    'final_lualatex_warnings_or_box_errors': problems,
    'bibtex_warnings_or_errors': [],
    'result_page_locations': locations,
    'pdf_info': info,
    'pdf_font_inventory': fonts,
    'visual_inspection': visual,
}
(base / 'audit' / 'final_validation.json').write_text(
    json.dumps(summary, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items()
                  if k not in ['pdf_info', 'pdf_font_inventory']}, indent=2))
