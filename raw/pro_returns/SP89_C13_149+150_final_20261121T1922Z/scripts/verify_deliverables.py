"""Structural completeness checks only; this is not OCR or TeX compilation."""
from pathlib import Path
import csv, json, re, sys, hashlib

W = Path(__file__).resolve().parents[1]
P = 'SP89_C13_149+150'
order = (W / 'scripts/page_order.txt').read_text().splitlines()
errors = []
def rows(p, delimiter='\t'):
    with p.open() as f:
        return list(csv.DictReader(f, delimiter=delimiter))
def require(ok, message):
    if not ok:
        errors.append(message)

actual_pages = sorted(p.stem for p in (W / 'pages').glob('*.tex'))
require(actual_pages == sorted(order), 'Page file coverage differs from the 25-page order')
marks = rows(W.parent / 'source/SP89_C13_149+150_texts/MARKS.tsv')
decisions = rows(W / 'decisions.tsv')
require([r['id'] for r in decisions] == [r['id'] for r in marks],
        'Original doubt decisions do not exactly preserve MARKS.tsv order')
required = ['changes.md', 'collation.tsv', 'doubts.md', 'inventory.csv',
            'notes.md', 'sheet_feedback.md', 'hand_log.md', 'transcription.tex']
for name in required:
    require((W / (P + '_' + name)).exists(), 'Missing deliverable ' + name)
for page in order:
    rp = W / 'reports' / page / 'report.json'
    if not rp.exists():
        errors.append('Missing report ' + page)
        continue
    r = json.loads(rp.read_text())
    require(r.get('main_reviewed'), 'First reading incomplete: ' + page)
    require(r.get('audited_utc'), 'Independent audit incomplete: ' + page)
    require(r.get('second_reader') and r['second_reader'] != r['reader'],
            'Independent reader missing or not different: ' + page)
    require(all(i['transcribed'] == 'yes' for i in r['inventory']),
            'Untranscribed inventory element: ' + page)
    for d in r['decisions']:
        if d['decision'] != 'undecided':
            require(d.get('crop') != 'page' and (W / d['crop']).exists(),
                    'Resolved doubt lacks crop: ' + d['id'])
    for c in r['changes']:
        require(c['confidence'] in ['high', 'medium', 'low'],
                'Bad confidence: ' + page + ' ' + c['id'])
        if c.get('crop') and c['crop'] != 'page':
            require((W / c['crop']).exists(), 'Missing evidence crop: ' + c['crop'])
    for suffix in ['boxes.tsv', 'first.tsv', 'second.tsv', 'comparison.json',
                   'adjudications.json', 'adjudicated.tsv', 'assignment.json']:
        require((W / 'second' / (page + '_' + suffix)).exists(),
                'Missing independent-reading record: ' + page + '_' + suffix)
    f = W / 'pages' / (page + '.tex')
    if not f.exists():
        continue
    tex = f.read_text()
    # Escaped braces, literal comments and structural commands only. No rendering.
    cleaned = re.sub(r'(?<!\\)%[^\n]*', '', tex)
    depth = 0
    for match in re.finditer(r'(?<!\\)[{}]', cleaned):
        depth += 1 if match.group() == '{' else -1
        require(depth >= 0, 'Premature closing brace: ' + page)
    require(depth == 0, 'Unbalanced braces: ' + page)
    envs = []
    for action, env in re.findall(r'\\(begin|end)\{([^{}]+)\}', cleaned):
        if action == 'begin':
            envs.append(env)
        else:
            require(bool(envs) and envs[-1] == env, 'Environment mismatch: ' + page)
            if envs:
                envs.pop()
    require(not envs, 'Unclosed environment: ' + page)
    require('\\scanpage{' + str(int(page.split('_scan')[1])) + '}' in tex,
            'Wrong or missing scanpage tag: ' + page)
    require(not re.search(r'\\(?:documentclass|usepackage|begin\{document\})', tex),
            'Page unexpectedly contains a preamble: ' + page)

inventory = rows(W / (P + '_inventory.csv'), ',')
require(set(r['scan'] for r in inventory) == set(order), 'Inventory page coverage incomplete')
summary = dict(pages=len(actual_pages), original_marks=len(marks),
               decisions=len(decisions), inventory_elements=len(inventory), errors=errors)
(W / 'reports/structural_verification.json').write_text(
    json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False))
sys.exit(bool(errors))
