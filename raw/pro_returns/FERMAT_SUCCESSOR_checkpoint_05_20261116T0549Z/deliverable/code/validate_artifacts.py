"""Check the paper/register/report contract and the publication build inventory.

This is a consistency gate, not a mathematical proof checker.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def group(text, start):
    assert text[start] == '{'
    depth = 1
    end = start + 1
    while depth:
        if text[end] == '{':
            depth += 1
        elif text[end] == '}':
            depth -= 1
        end += 1
    return text[start + 1:end - 1], end


statements = {}
tex_files = [ROOT / 'FERMAT_SUCCESSOR_paper.tex']
tex_files += sorted((ROOT / 'sections').glob('*.tex'))
tex_files += sorted((ROOT / 'tables').glob('*.tex'))
reachable = set()
pending = [tex_files[0]]
while pending:
    source = pending.pop()
    if source in reachable:
        continue
    reachable.add(source)
    for target in re.findall(r'\\input\s*\{([^}]+)\}', source.read_text()):
        child = ROOT / target
        if child.suffix != '.tex':
            child = child.with_suffix('.tex')
        assert child.exists(), ('missing manuscript input', source, target)
        pending.append(child)
citations = set()
for path in tex_files:
    text = path.read_text()
    for match in re.finditer(re.escape(r'\begin{statement}'), text):
        pos = match.end()
        values = []
        for _ in range(3):
            while text[pos].isspace():
                pos += 1
            value, pos = group(text, pos)
            values.append(value)
        sid, title, status = values
        assert path in reachable, ('statement source omitted from the compiled paper', sid, path)
        assert sid not in statements, ('duplicate statement', sid, path)
        statements[sid] = {'source': str(path.relative_to(ROOT)), 'status': status.split(',')[0].split(';')[0].split(' ')[0]}
    for match in re.finditer(r'\\cite\w*\s*(?:\[[^\]]*\]\s*)*\{([^{}]+)\}', text):
        citations.update(k.strip() for k in match.group(1).split(','))

rows = list(csv.DictReader((ROOT / 'FERMAT_SUCCESSOR_results.csv').open()))
assert len(rows) == len({r['id'] for r in rows}), 'duplicate register IDs'
assert {r['id'] for r in rows} == set(statements), 'source/register IDs differ'
for row in rows:
    item = statements[row['id']]
    assert row['status'] == item['status'], (row['id'], 'status mismatch')
    assert item['source'] in row['where_proved'], (row['id'], 'source mismatch')
    assert row['answers (lead or task)'], (row['id'], 'no task mapping')
    assert row['status'] in {'Proved', 'Known', 'Refuted', 'Open'}

bib = (ROOT / 'FERMAT_SUCCESSOR_references.bib').read_text()
bib_entries = {}
for entry in re.split(r'(?m)(?=^@)', bib):
    if not entry.startswith('@'):
        continue
    key = entry.split('{', 1)[1].split(',', 1)[0]
    assert key not in bib_entries, ('duplicate bibliography key', key)
    assert re.search(r'\b(?:verified|unverified)\b', entry, re.I), ('no verification label', key)
    bib_entries[key] = entry
assert citations <= set(bib_entries), ('undefined bibliography keys', sorted(citations - set(bib_entries)))

report = (ROOT / 'FERMAT_SUCCESSOR_report.md').read_text()
assert report.startswith('INCOMPLETE\n'), 'unresolved return must be labelled INCOMPLETE'
task_rows = re.findall(r'^\| ((?:[ABCD]\.\d+)|(?:Lead \d+)) \|', report, re.M)
expected = {f'{part}.{i}' for part, maximum in [('A', 12), ('B', 13), ('C', 8), ('D', 2)] for i in range(1, maximum + 1)}
expected |= {f'Lead {i}' for i in range(1, 10)}
assert len(task_rows) == 44 and set(task_rows) == expected, 'task/lead report table differs'
credit = 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)'
assert credit in report and credit in tex_files[0].read_text()

concordance = list(csv.DictReader((ROOT / 'records/manuscript_concordance.csv').open()))
assert {r['id'] for r in concordance} == {s for s in statements if s[0] in 'AB'}

log = (ROOT / 'FERMAT_SUCCESSOR_paper.log').read_text()
overflows = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt', log)]
assert max(overflows, default=0) <= 2, ('overflow exceeds 2pt', overflows)
assert 'Missing character:' not in log
assert not re.search(r'(?:Citation|Reference).*undefined', log)

build_path = ROOT / 'records/build_inputs.json'
build = json.loads(build_path.read_text()) if build_path.exists() else {}
pdf_sha = hashlib.sha256((ROOT / 'FERMAT_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()
if '--publication' in sys.argv:
    assert build.get('sources_stable_during_build')
    assert build.get('pdf_sha256') == pdf_sha
    for name, digest in build['sources'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, ('source changed after build', name)
    qa = json.loads((ROOT / 'records/pdf_qa.json').read_text())
    assert qa['pdf_sha256'] == pdf_sha, 'page-image QA does not cover this PDF'
    assert qa['viewed_pages'], 'no visual page inspection recorded'

result = {
    'status': 'all requested consistency checks passed',
    'statements': len(statements),
    'task_and_lead_rows': len(task_rows),
    'bibliography_entries': len(bib_entries),
    'cited_keys': len(citations),
    'manuscript_links': len(concordance),
    'overfull_boxes': len(overflows),
    'largest_overflow_pt': max(overflows, default=0),
    'pdf_sha256': pdf_sha,
    'publication_inventory_and_visual_QA_checked': '--publication' in sys.argv,
}
print(json.dumps(result, indent=2))
