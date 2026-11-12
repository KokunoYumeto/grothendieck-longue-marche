"""Validate and ZIP the finished deliverable, with a SHA-256 manifest.

Requires the final build, register assembly, all-page render, and explicit
visual review record to have completed. No upload or network operation occurs.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / 'code'
PREFIX = 'LM1_GROUP_SCHEMES'
ZIP = ROOT.parent / (PREFIX + '.zip')
audit = []


def require(condition, message):
    if not condition:
        raise AssertionError(message)
    audit.append('PASS ' + message)


required = [PREFIX + extension for extension in [
    '_paper.tex', '_paper.pdf', '_results.csv', '_readings.csv',
    '_references.bib', '_report.md',
]]
require(all((ROOT / name).is_file() for name in required),
        'All six requested primary files exist')
assembly = json.loads((CODE / 'assembly_audit.json').read_text())
with (ROOT / (PREFIX + '_results.csv')).open(newline='') as stream:
    results = list(csv.DictReader(stream))
require(len(results) == assembly['statements'], 'CSV statement count matches assembly')
require(dict(Counter(row['status'] for row in results)) == assembly['statuses'],
        'CSV status counts match assembly')
require(assembly['primary_requests'] == 40 and assembly['followups'] == 6,
        'All 40 primary requests and six followups have coverage rows')
require(not assembly['unfinished'], 'No task falls below its declared completion category')

log = (ROOT / (PREFIX + '_paper.log')).read_text(errors='replace')
bad = re.findall(r'^.*(?:Undefined control sequence|undefined citations|undefined references|'
                 r'Citation .* undefined|Reference .* undefined|Overfull \\[hv]box|'
                 r'Missing character:|Label\(s\) may have changed|Rerun to get).*$'
                 , log, re.M)
require(not bad, 'Final LuaLaTeX log has no undefined citations/references, missing characters, overfull boxes, or rerun request')
require('Output written on' in log, 'Final LuaLaTeX run wrote a PDF')
require('exit 0' in (CODE / 'build_pdf.out').read_text(), 'Build helper recorded successful tool exits')
info = subprocess.check_output(['pdfinfo', str(ROOT / (PREFIX + '_paper.pdf'))], text=True)
pages = int(re.search(r'^Pages:\s+(\d+)$', info, re.M).group(1))
require('GPT-6 Astra (OpenAI, ChatGPT Pro mode)' in info, 'PDF metadata carries the requested AI credit')
pdf_text = (CODE / 'paper_text.txt').read_text()
require('??' not in pdf_text, 'Extracted PDF text contains no unresolved reference marker')
missing_ids = [row['id'] for row in results if not re.search(
    r'(?<![A-Za-z0-9])' + re.escape(row['id']) + r'\.(?!\d)', pdf_text)]
require(not missing_ids, 'Every registered numbered statement appears in PDF text')
render = json.loads((CODE / 'render_audit.json').read_text())
review = json.loads((CODE / 'visual_review.json').read_text())
pdf_hash = hashlib.sha256((ROOT / (PREFIX + '_paper.pdf')).read_bytes()).hexdigest()
require(render['pdf_pages'] == pages and render['rendered_pages'] == pages,
        f'All {pages} PDF pages rendered')
require(render['pdf_sha256'] == pdf_hash, 'Rendering applies to this exact PDF')
require(review['pdf_sha256'] == pdf_hash, 'Visual review applies to this exact PDF')
require(review['all_contact_sheets_inspected'] and review['outcome'] == 'passed',
        'All contact sheets and specified full-size pages passed visual inspection')

expected_math = ['AB_identities', 'AB_enumerate', 'AB_general_finite',
                 'AB_signed_finite', 'C_presentations', 'D_finite',
                 'D_components', 'D_gt', 'D_number_fields', 'D_arithmetic',
                 'D_motives', 'E_integrality', 'E_envelope', 'E_automorphisms']
expected_math += [name for name in ['AB_functoriality', 'AB_modular_comparison',
                                   'B_late_sections'] if (CODE / (name + '.py')).exists()]
for stem in expected_math:
    require((CODE / (stem + '.py')).is_file() and
            (CODE / (stem + '.out')).is_file() and
            (CODE / (stem + '.out')).stat().st_size > 0,
            stem + ': source and actual nonempty output are included')
    require('Traceback (most recent call last)' not in (CODE / (stem + '.out')).read_text(),
            stem + ': recorded output has no Python traceback')

report = (ROOT / (PREFIX + '_report.md')).read_text()
require(report.startswith('| Request |'), 'Report opens with the requested coverage table')
require('GPT-6 Astra (OpenAI, ChatGPT Pro mode)' in report,
        'Report carries the requested AI credit')

audit += [f'PDF pages: {pages}', f'PDF SHA-256: {pdf_hash}',
          'Statement statuses: ' + json.dumps(assembly['statuses'], sort_keys=True),
          'Primary task outcomes: ' + json.dumps(assembly['primary_outcomes'], sort_keys=True),
          'Visual checks are recorded in code/visual_review.json.',
          'The ZIP is subsequently tested and every archived SHA-256 is checked.']
(CODE / 'package_audit.out').write_text('\n'.join(audit) + '\n')

excluded_suffixes = {'.aux', '.log', '.toc', '.bbl', '.blg', '.synctex', '.pyc'}


def include(path):
    rel = path.relative_to(ROOT)
    if '__pycache__' in rel.parts or any(part.startswith('.') for part in rel.parts):
        return False
    if path.suffix in excluded_suffixes:
        return False
    if rel.name == 'MANIFEST.sha256':
        return False
    if len(rel.parts) == 1 and path.suffix == '.out':
        return False
    return True


files = sorted(path for path in ROOT.rglob('*') if path.is_file() and include(path))
manifest = '\n'.join(hashlib.sha256(path.read_bytes()).hexdigest() + '  ' +
                     path.relative_to(ROOT).as_posix() for path in files) + '\n'
(ROOT / 'MANIFEST.sha256').write_text(manifest)
with zipfile.ZipFile(ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in files + [ROOT / 'MANIFEST.sha256']:
        archive.write(path, PREFIX + '/' + path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(ZIP) as archive:
    assert archive.testzip() is None
    for line in manifest.splitlines():
        expected, name = line.split('  ', 1)
        assert hashlib.sha256(archive.read(PREFIX + '/' + name)).hexdigest() == expected, name
print('\n'.join(audit))
print('PASS ZIP CRC test and every archived SHA-256')
print('ZIP:', ZIP.name, 'files:', len(files) + 1, 'bytes:', ZIP.stat().st_size)
