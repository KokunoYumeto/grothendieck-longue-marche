"""Read-only verification of transcription; writes research/progress records only."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads((ROOT / p).read_text())

frozen = load('records/frozen_hashes.json')
expected = load('records/run_state.json')['expected_scans']
assert expected == list(range(3, 9)) + list(range(28, 53))
comparisons = {p: {'frozen': h, 'current': sha(ROOT / p)} for p, h in frozen['files'].items()}
assert len(comparisons) == 32
assert all(c['frozen'] == c['current'] for c in comparisons.values()), 'FROZEN TEXT CHANGED'

pages = [ROOT / 'pages' / f'MPL_36_002-052_36_scan{n:03}.tex' for n in expected]
assert set(pages) == set((ROOT / 'pages').glob('*.tex'))
combined = (ROOT / 'MPL_36_002-052_transcription.tex').read_text()
assert combined == '\n'.join(p.read_text().rstrip() + '\n' for p in pages)
assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}', combined)] == expected
assert combined.startswith('\\cotefile{36}\n\\scanpage{3}\n')
assert '\\documentclass' not in combined and '\\begin{document}' not in combined

images = sorted((ROOT.parent / 'scans').rglob('*.jpg'))
assert len(images) == 93
for n in expected:
    assert len([p for p in images if re.search(fr'_scan{n:03}(?:_[ab])?\.jpg$', p.name)]) == 3

with (ROOT / 'MPL_36_002-052_inventory.csv').open(newline='') as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
    rows = list(reader)
assert len(rows) == 787
assert all(row['transcribed'] == 'yes' and row['cote'] == '36' for row in rows)
assert {int(row['scan']) for row in rows} == set(expected)
assert {row['kind'] for row in rows} <= {'text','display','diagram','drawing','margin note','insertion','deletion'}
sheet_kinds = {}
for n in expected:
    kinds = {row['sheet_kind'] for row in rows if int(row['scan']) == n}
    assert len(kinds) == 1, (n, kinds)
    sheet_kinds[str(n)] = next(iter(kinds))
assert Counter(sheet_kinds.values()) == {'text':16,'reused_typed':12,'cover':2,'cancelled_draft':1}

unsure = len(re.findall(r'\\unsure\{', combined))
illegible = len(re.findall(r'\\illegible\{', combined))
doubts = (ROOT / 'MPL_36_002-052_doubts.md').read_text()
doubt_rows = len(re.findall(r'^\| 36\.pdf \| \d+ \|', doubts, re.M))
assert (unsure, illegible, doubt_rows) == (324,5,329)

progress = (ROOT / 'progress.log').read_text()
done = re.findall(r'^36 scan (\d{3}) done (.+)$', progress, re.M)
audits = re.findall(r'^scan (\d{3}) audited (.+)$', progress, re.M)
assert [int(n) for n, _ in done] == expected
assert [int(n) for n, _ in audits] == expected
assert all(t <= frozen['frozen_utc'] for _, t in done + audits)
opened = re.search(r'^context opened (.+)$', progress, re.M).group(1)
assert frozen['frozen_utc'] < opened

notes = load('records/notes_data.json')
searches = load('records/context_searches.json')
register = load('records/register_context_searches.json')
ids = [f'N{n:02}' for n in range(1,93)]
assert [n['id'] for n in notes] == ids
assert [n['id'] for n in searches] == ids
assert len(register) == 34 and len({n['id'] for n in register}) == 34
allowed = {'conjecture','unproved claim','unpursued implication','own idea','reading question','self-flagged','withdrawn in the same text'}
for note in notes:
    assert note['kind'] in allowed and note['body'] and note['context'] and note['location']
    assert set(note['scans']) <= set(expected)
    if note['kind'] == 'own idea': assert note['confidence'] in ('high','medium','low') and note['reason']
for row in searches + register:
    assert len(row['searched_files']) == 3 and row['utc'] > opened
    assert row['query'] and row['hit_count'] == len(row['matches'])
main_notes = (ROOT / 'MPL_36_002-052_notes.md').read_text()
assert re.findall(r'^### (N\d{2}) — ', main_notes, re.M) == ids
for title in ('Standing question 1', 'Standing question 2', 'Explicit comparison with every substantive results-register entry', 'Primary references and exact verification limits'):
    assert title in main_notes
assert all(f'**P{n}.**' in main_notes for n in range(1,10))

utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
result = {'verified_utc':utc, 'frozen_utc':frozen['frozen_utc'], 'context_opened_utc':opened,
    'all_frozen_hashes_unchanged':True, 'frozen_file_count':32, 'hash_comparisons':comparisons,
    'expected_scans':expected, 'source_image_count':len(images), 'page_count':len(pages),
    'combined_exactly_matches_ordered_pages':True, 'inventory_rows':len(rows), 'inventory_all_transcribed_yes':True,
    'sheet_kinds':sheet_kinds, 'sheet_kind_counts':dict(Counter(sheet_kinds.values())),
    'unsure_occurrences':unsure, 'illegible_occurrences':illegible, 'doubt_rows':doubt_rows,
    'page_done_records':len(done), 'separate_audit_records':len(audits),
    'research_note_count':len(notes), 'research_note_kind_counts':dict(Counter(n['kind'] for n in notes)),
    'individual_note_searches':len(searches), 'substantive_results_register_entries':len(register),
    'individual_register_searches':len(register), 'primary_reference_count':9,
    'limits':'Integrity and structural checks do not remove the recorded palaeographic doubts or certify conditional research leads.'}
(ROOT / 'records/final_verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'records/notes_final_verification.md').write_text(f'''\n## Final integrity and scope verification\n\nAt **{utc}**, all **32 frozen SHA-256 values**—the 31 page files and combined transcription—were unchanged from the pre-context freeze. The combined fragment matches the ordered page files exactly. All 31 actual supplied scan numbers occur once; their 93 source images, 31 completion entries and 31 separate audit entries are accounted for.\n\nThe inventory has **787 entries, all marked yes**. The doubts table indexes all **324 uncertainty macros and five illegible-prose macros**; these remain explicit limitations on the witness. The research record contains **92 numbered items, 15 labelled own ideas, 92 individual context searches and 34 separately searched register dispositions**, together with the two standing inventories and nine primary references. `records/final_verification.json` contains the machine-readable check, and `progress.log` records the chronology. These checks establish file integrity and documented coverage; they do not turn an uncertain reading, incomplete proof, or earlier-run claim into an established result.\n''')
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'final integrity verified {utc}; all 32 frozen SHA-256 hashes unchanged; 31 pages, 787 inventory rows, 329 doubts, 92 research notes, 34 substantive register comparisons\n')
print(json.dumps({k: result[k] for k in ('verified_utc','all_frozen_hashes_unchanged','page_count','inventory_rows','doubt_rows','research_note_count','substantive_results_register_entries')}, indent=2))
