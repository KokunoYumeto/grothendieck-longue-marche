from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_45_033-080'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def page(n, text, sheet_kind, elements, doubts=()):
    path = ROOT / 'pages' / f'{PREFIX}_45_scan{n:03d}.tex'
    if path.exists():
        raise RuntimeError(f'Page already exists: {n}')
    assert text.startswith(('\\cotefile{45}\n\\scanpage{33}', f'\\scanpage{{{n}}}'))
    path.write_text(text.strip()+'\n', encoding='utf-8')
    inventory = ROOT / f'{PREFIX}_inventory.csv'
    new = not inventory.exists()
    with inventory.open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if new:
            w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i, (kind, position, words) in enumerate(elements, 1):
            w.writerow(['45', f'{n:03d}', sheet_kind, f'{n:03d}.{i:02d}', kind, position, words, 'yes'])
    with (ROOT/f'{PREFIX}_doubts.md').open('a', encoding='utf-8') as f:
        for line, reading, alternative, confidence in doubts:
            def cell(s): return str(s).replace('|', '\\|').replace('\n',' ')
            f.write('| 45 | %03d | %s | %s | %s | %s |\n' % (n,cell(line),cell(reading),cell(alternative),confidence))
    with (ROOT/'progress.log').open('a', encoding='utf-8') as f:
        f.write(f'45 scan {n:03d} done {utc()}\n')
    print(f'45 scan {n:03d} saved; {len(elements)} inventory elements.')

