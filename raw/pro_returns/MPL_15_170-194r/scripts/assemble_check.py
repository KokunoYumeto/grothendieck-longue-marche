from pathlib import Path
import csv, re

root = Path(__file__).resolve().parents[1]
order = [170,171,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194]
parts = []
for n in order:
    p = root/'pages'/f'MPL_15_170-194r_15_scan{n:03d}.tex'
    s = p.read_text()
    assert re.findall(r'\\scanpage\{(\d+)\}', s) == [str(n)], p
    assert '\\documentclass' not in s and '\\includegraphics' not in s, p
    depth = 0
    for match in re.finditer(r'(?<!\\)[{}]', s):
        depth += 1 if match.group() == '{' else -1
        assert depth >= 0, (p, match.start())
    assert depth == 0, (p, depth)
    stack = []
    for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', s):
        action, env = match.groups()
        if action == 'begin': stack.append(env)
        else: assert stack.pop() == env, (p, env)
    assert not stack, (p, stack)
    assert len(re.findall(r'(?<!\\)\$', s)) % 2 == 0, p
    parts.append(s.rstrip()+'\n')
combined = '\n'.join(parts)
assert combined.startswith('\\cotefile{15}\n\\scanpage{170}')
assert re.findall(r'\\cotefile\{([^}]+)\}', combined) == ['15']
(root/'MPL_15_170-194r_transcription.tex').write_text(combined)
rows = list(csv.DictReader((root/'MPL_15_170-194r_inventory.csv').open()))
assert set(rows[0]) == {'cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'}
assert set(int(r['scan']) for r in rows) == set(order)
assert all(r['transcribed'] == 'yes' for r in rows)
assert all(r['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for r in rows)
log=(root/'progress.log').read_text()
assert [int(x) for x in re.findall(r'^scan (\d+) audited',log,re.M)] == order
assert [int(x) for x in re.findall(r'^15 scan (\d+) done',log,re.M)] == order
print(f'18 page files; {len(rows)} inventory elements; all marked yes; complete done/audited order; balanced braces, math delimiters and environments.')
print('Explicit uncertainty occurrences:', combined.count('\\unsure{'))
