from pathlib import Path
from datetime import datetime, timezone
import json, re, subprocess
from register_data import ROWS

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT.parent / 'context'
rs = (CTX / 'notes/RESULTS_STATE.md').read_text()
expected = re.findall(r'^- \*\*(.+?)\*\* \[', rs, re.M)
expected += ['Hua, findings register, 36-griffiths-conditional-l-adic']
assert len(expected) == 34, expected
assert {r[0] for r in ROWS} == set(expected)
assert len(ROWS) == len({r[0] for r in ROWS}) == 34
files = sorted(CTX.rglob('*.md'))
searches = []
parts = ['\n## Explicit comparison with every substantive results-register entry\n\n',
    'The table accounts for all **34 substantive entries** supplied by `notes/RESULTS_STATE.md`: one open item, one settled-status claim, one intake entry, 28 returned-package leads, two planning items, and one Hua finding. The source files named in the register were not separately supplied, except for CT; their truncated summaries do not authorize reconstruction of missing statements or scan locators. Each row has a fresh context search recorded in `records/register_context_searches.json`.\n\n',
    'The introductory referee list certifies exactly LM4 D.32 and D.34, and LM7_PUSH D.44, D.50, E.58, E.61, E.62, E.64, E.65 and E.67 as reported in RS; neither LM7 E.23 nor LM7_PUSH C.6 is thereby certified. The run states “RETURNED” report workflow completion, not theorem status. Earlier register comparisons inside CT refer to a different supplied dossier; they are not silently added to the present register.\n\n',
    '| Exact register ID | Supplied status, with its limits | Source file and supplied locus | Relation of the current pages | Current note(s) |\n',
    '|---|---|---|---|---|\n']

def prose(s):
    s = re.sub(r'(?<=[a-z])(?=\d)', ' ', s)
    s = re.sub(r';(?=\S)', '; ', s)
    s = re.sub(r',(?=\d)', ', ', s)
    s = s.replace('SGA1', 'SGA 1').replace('SGA3', 'SGA 3')
    return s

def cell(s):
    return s.replace('|', '\\|').replace('\n', ' ')

for ident, status, source, relation, notes, query in ROWS:
    result = subprocess.run(['rg', '-n', '-i', '-e', query] + [str(f) for f in files], capture_output=True, text=True)
    assert result.returncode in (0, 1), result.stderr
    matches = []
    for line in result.stdout.splitlines():
        path, number, excerpt = line.split(':', 2)
        matches.append({'file': str(Path(path).relative_to(CTX)), 'line': int(number), 'excerpt': excerpt[:360]})
    raw_id = ident.split(', ')[-1] if ident.startswith('Hua,') else ident
    rs_lines = [i for i, line in enumerate(rs.splitlines(), 1) if line.startswith('- **' + raw_id + '**')]
    assert len(rs_lines) == 1, (ident, rs_lines)
    searches.append({'id': ident, 'query': query, 'utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), 'searched_files': [str(f.relative_to(CTX)) for f in files], 'register_line': rs_lines[0], 'hit_count': len(matches), 'matches': matches})
    parts.append('| ' + ' | '.join(cell(s) for s in ('`' + ident + '`', status, prose(source), prose(relation), prose(notes))) + ' |\n')

parts.append('\n**Planning disposition:** README S19 is confirmed by the SGA 7 editorial headings on scans 003–008 and the duality/biextension programmes on 028–052. N34 supplies the closest directly inspected published comparison, with Deligne’s two-term-complex formulation; N45, N52, N63, N76 and N85 add precise Stacks tests or comparators. The SGA 7 chapter bibliography is verified, while a complete original-print collation was not achieved; the preceding standing inventories answer the title and unverified-step requests without inferring content of omitted scans.\n')
(ROOT / 'records/notes_register.md').write_text(''.join(parts))
(ROOT / 'records/register_context_searches.json').write_text(json.dumps(searches, ensure_ascii=False, indent=2) + '\n')
index = ['# Results-register context searches\n\n']
for row in searches:
    index.append(f"## {row['id']}\n\nQuery: `{row['query']}`. Exact register entry: `notes/RESULTS_STATE.md:{row['register_line']}`. Matches: {row['hit_count']}.\n\n")
    for m in row['matches'][:10]:
        index.append(f"- `{m['file']}:{m['line']}` — {m['excerpt']}\n")
    index.append('\n')
(ROOT / 'records/register_context_searches.md').write_text(''.join(index))
print(f'All {len(ROWS)} substantive register entries represented; {sum(not r["hit_count"] for r in searches)} no-hit queries.')
