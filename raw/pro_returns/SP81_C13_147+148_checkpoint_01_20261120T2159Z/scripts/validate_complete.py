"""Completeness and evidence gate. This does not compile or judge the transcription."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, sys

root = Path(__file__).resolve().parents[1]
source = root.parent / 'source'
manifest = json.loads((root / 'work/manifest.json').read_text())
pages = [m['page'] for m in manifest]
errors = []

def need(ok, message):
    if not ok:
        errors.append(message)

def tsv(path, supplied=False):
    with path.open(newline='') as f:
        options = {'delimiter': '\t'}
        if supplied:
            options['quoting'] = csv.QUOTE_NONE
        return list(csv.DictReader(f, **options))

marks = tsv(source / 'SP81_C13_147+148_texts/MARKS.tsv', True)
diffs = tsv(source / 'SP81_C13_147+148_C_H_differences.tsv', True)
views = (root / 'work/root_views.tsv').read_text()
reports = []
allowed_kinds = {'misread word', 'misread symbol or index', 'omission', 'text not on the page',
                 'deletion state', 'insertion or placement',
                 'abbreviation expanded or spelling modernised', 'readable ink left as \\ill{}',
                 'drawing or diagram', 'other'}
first_times = []
audit_times = []
for m in manifest:
    page = m['page']
    report_path = root / 'work' / (page + '_final.json')
    if not report_path.is_file():
        errors.append(page + ': missing approved report')
        continue
    r = json.loads(report_path.read_text())
    reports.append(r)
    need(r.get('root_approved'), page + ': not approved')
    need(r.get('audit'), page + ': missing blind audit')
    first_times.append(r.get('approved_at', ''))
    if r.get('audit'):
        need(r['audit']['reader'] != r['reader'], page + ': same first and second reader')
        audit_times.append(r['audit']['audited_at'])
    cote, scan = page.split('_scan')
    expected_marks = {v['id'] for v in marks if v['cote'] == cote and int(v['scan']) == int(scan)}
    need({v['id'] for v in r['decisions']} == expected_marks, page + ': mark coverage')
    expected_diffs = {i for i, v in enumerate(diffs, 1) if v['page'] == page}
    need({int(v['row']) for v in r.get('diff_coverage', [])} == expected_diffs, page + ': supplied difference coverage')
    for c in r['changes']:
        need(c['confidence'] in ('high', 'medium', 'low'), c['id'] + ': confidence')
        need(c['kind'] in allowed_kinds, c['id'] + ': collation kind')
        need(c.get('differs_C') or c.get('differs_H'), c['id'] + ': no witness difference')
        crop = c.get('crop', '')
        need(bool(crop) and (root / 'crops' / crop).is_file(), c['id'] + ': evidence crop missing')
        need(bool(crop) and crop in views, c['id'] + ': root crop view missing')
        if c.get('differs_H'):
            need((source / 'SP81_C13_147+148_texts/hua' / ('hua_' + page + '.tex')).is_file(), c['id'] + ': absent H')
    need(all(v['transcribed'] == 'yes' for v in r['inventory']), page + ': incomplete inventory')
    need(bool(r.get('deletion_insertion_check')), page + ': correction-state review missing')
    for d in r['decisions']:
        need(d['decision'] in ('first', 'alternative', 'other', 'undecided'), d['id'] + ': invalid decision')
        if d['decision'] != 'undecided':
            need(d['crop'] != 'page' and '.png' in d['crop'], d['id'] + ': resolved without crop')
    page_path = root / 'pages' / (page + '.tex')
    if not page_path.is_file():
        errors.append(page + ': missing text')
        continue
    text = page_path.read_text()
    need('\\cotefile{' + cote + '}' in text and '\\scanpage{' + str(int(scan)) + '}' in text, page + ': headers')
    need(not re.search(r'\\(?:ill|uncertain|struck|add|marginal)\{', text), page + ': foreign witness macro')
    depth = 0
    for line in text.splitlines():
        for token in re.findall(r'\\.|[{}]|[^{}\\]+', line.split('%')[0]):
            depth += (token == '{') - (token == '}')
            need(depth >= 0, page + ': brace underflow')
    need(depth == 0, page + ': brace imbalance')
    second_paths = {kind: root / 'second' / (page + '_' + kind + '.tsv')
                    for kind in ('boxes', 'first', 'second', 'adjudications')}
    for kind, path in second_paths.items():
        need(path.is_file(), page + ': missing ' + kind)
    if all(path.is_file() for path in second_paths.values()):
        rows = {kind: tsv(path) for kind, path in second_paths.items()}
        sets = [{v['box'] for v in rows[kind]} for kind in ('boxes', 'first', 'second')]
        need(sets[0] == sets[1] == sets[2], page + ': blind box coverage')
        for kind in ('boxes', 'first', 'second'):
            need(len(rows[kind]) == len(sets[0]), page + ': duplicated ' + kind + ' box')
        comparison_path = root / 'second' / (page + '_comparison.json')
        need(comparison_path.is_file(), page + ': comparison missing')
        if comparison_path.is_file():
            comp = json.loads(comparison_path.read_text())
            need({v['box'] for v in comp['differences']} == {v['box'] for v in rows['adjudications']}, page + ': adjudication coverage')
        for v in r.get('audit_changes', []):
            need(v['crop'] in views and (root / 'crops' / v['crop']).is_file(), page + ': blind difference crop unviewed')

need(len(reports) == 24, 'All 24 reports required')
if len(first_times) == 24 and len(audit_times) == 24:
    need(max(first_times) <= min(audit_times), 'Audit recorded before completion of all first readings')
decision_rows = tsv(root / 'decisions.tsv')
need([v['id'] for v in decision_rows] == [v['id'] for v in marks], 'Aggregate MARKS order/coverage')
collation = tsv(root / 'SP81_C13_147+148_collation.tsv')
need(len(collation) == sum(bool(c.get('differs_H')) for r in reports for c in r['changes']), 'Collation count')
for c in collation:
    need(int(c['their_page']) + 1 == int(c['our_scan']), 'H page/scan mapping')
joined = '\n'.join((root / 'pages' / (page + '.tex')).read_text().rstrip() + '\n'
                   for page in pages if (root / 'pages' / (page + '.tex')).is_file())
need((root / 'SP81_C13_147+148_transcription.tex').read_text() == joined, 'Combined text differs from ordered page fragments')
outcome = {'checked_at': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           'approved_pages': len(reports), 'audited_pages': len(audit_times),
           'mark_decisions': len(decision_rows), 'supplied_difference_rows': len(diffs),
           'errors': errors, 'method': 'Static completeness/evidence checks only; no TeX compilation or OCR.'}
(root / 'work/final_validation.json').write_text(json.dumps(outcome, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(outcome, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
