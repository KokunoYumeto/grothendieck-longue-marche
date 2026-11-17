"""Verify deliverable completeness and the post-context transcription freeze.

This checker never edits a manuscript file. Run from any working directory.
It writes only its own JSON report. Archive assembly is a separate operation.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_138_046-089'
EXPECTED = [n for n in range(46, 90) if n not in (79, 88)]
pages = sorted((ROOT / 'pages').glob('*.tex'))
assert [int(re.search(r'scan(\d+)', p.name).group(1)) for p in pages] == EXPECTED
required = [PREFIX + ending for ending in (
    '_transcription.tex', '_doubts.md', '_inventory.csv', '_notes.md')]
required += ['progress.log', 'frozen_sha256.txt']
assert all((ROOT / name).is_file() for name in required)

frozen = {}
for line in (ROOT / 'frozen_sha256.txt').read_text().splitlines():
    digest, name = line.split(None, 1)
    assert name not in frozen
    frozen[name] = digest
expected_frozen = {str(p.relative_to(ROOT)) for p in pages}
expected_frozen.add(PREFIX + '_transcription.tex')
assert set(frozen) == expected_frozen
actual = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
          for name in frozen}
assert actual == frozen, 'A frozen transcription hash has changed'
combined = (ROOT / (PREFIX + '_transcription.tex')).read_bytes()
assert combined == b'\n'.join(p.read_bytes() for p in pages)
tex = combined.decode('utf-8')
assert tex.startswith('\\cotefile{138}')
assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}', tex)] == EXPECTED
assert '\\documentclass' not in tex and '\\begin{document}' not in tex

with (ROOT / (PREFIX + '_inventory.csv')).open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
assert fields == ['cote', 'scan', 'sheet_kind', 'element', 'kind',
                  'position', 'first_words_or_objects', 'transcribed']
assert len(rows) == 612
assert len({r['element'] for r in rows}) == len(rows)
assert {int(r['scan']) for r in rows} == set(EXPECTED)
assert all(r['cote'] == '138' and r['transcribed'] == 'yes' for r in rows)
assert {r['sheet_kind'] for r in rows} <= {
    'text', 'reused_typed', 'cancelled_draft', 'cover'}
assert {r['kind'] for r in rows} <= {
    'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
assert all(set(r) == set(fields) and all(v is not None for v in r.values())
           for r in rows)

doubts = (ROOT / (PREFIX + '_doubts.md')).read_text()
assert doubts.startswith('# Notation table')
assert '# Abbreviations' in doubts and '# Legibility' in doubts
doubt_section = doubts.split('# Doubts', 1)[1].split('# Abbreviations', 1)[0]
doubt_rows = re.findall(r'^\| 138 \|', doubt_section, re.M)
assert len(doubt_rows) == tex.count('\\unsure{') == 268

notes = (ROOT / (PREFIX + '_notes.md')).read_text()
items = re.findall(r'^### (N\d+)\s+—[^\n]*\n(.*?)(?=^### N\d+\s+—|^## |\Z)',
                   notes, re.M | re.S)
assert [n for n, _ in items] == [f'N{i:02}' for i in range(1, 47)]
for note_id, item in items:
    assert all(field in item for field in (
        '**Source:**', '**Kind:**', '**Context/relation:**', '**Register:**')), note_id
    kind = re.search(r'\*\*Kind:\*\* (.*?)(?= \*\*|\n)', item).group(1)
    if 'own idea' in kind:
        assert 'confidence' in item.lower(), note_id
assert '## V. Standing question: steps the manuscript itself marks as unverified' in notes
assert '## VI. Standing question: title sheets, headings, and counts' in notes
with (ROOT / 'research_records/context_searches.tsv').open(newline='') as f:
    searches = list(csv.DictReader(f, delimiter='\t'))
assert [r['note_id'] for r in searches] == [n for n, _ in items]
assert all(r['rg_query'] and r['selected_context_and_relation'] and r['register_connection']
           for r in searches)

log = (ROOT / 'progress.log').read_text()
assert re.match(r'\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC\n', log)
assert [int(n) for n in re.findall(r'^138 scan (\d+) done ', log, re.M)] == EXPECTED
assert [int(n) for n in re.findall(r'^scan (\d+) audited ', log, re.M)] == EXPECTED
assert log.index('transcription frozen ') < log.index('context opened ')
for name, digest in frozen.items():
    assert f'SHA-256 {digest}  {name}' in log

files = [p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
assert all(p.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.pdf', '.zip', '.pyc'}
           for p in files)
assert not (ROOT / 'scans').exists() and not (ROOT / 'context').exists()
report = {
    'checked_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'result': 'PASS',
    'page_count': len(pages),
    'scan_set': EXPECTED,
    'frozen_files_checked': len(frozen),
    'all_frozen_hashes_unchanged': actual == frozen,
    'combined_exact_ordered_page_bytes_with_LF_separators': True,
    'combined_sha256': actual[PREFIX + '_transcription.tex'],
    'inventory_rows': len(rows),
    'inventory_all_transcribed_yes': True,
    'marked_doubts_and_doubt_rows': len(doubt_rows),
    'numbered_research_notes': len(items),
    'context_search_records': len(searches),
    'required_standing_sections_present': True,
    'all_done_and_audit_log_entries_present': True,
    'attached_scans_and_context_excluded': True,
    'limitation': 'No successful LaTeX compilation or rendered validation is claimed.'
}
out = ROOT / 'technical_qa/final_package_check.json'
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
