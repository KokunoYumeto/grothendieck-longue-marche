from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_12_051-098'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def macros(text, name):
    needle = '\\' + name + '{'
    start = 0
    while True:
        at = text.find(needle, start)
        if at < 0:
            return
        left = at + len(needle)
        depth, right = 1, left
        while right < len(text) and depth:
            if text[right] == '{' and (right == 0 or text[right-1] != '\\'):
                depth += 1
            elif text[right] == '}' and (right == 0 or text[right-1] != '\\'):
                depth -= 1
            right += 1
        yield at, text[left:right-1]
        start = left

def save_page(scan, text, elements, sheet_kind='text', remarks=''):
    path = ROOT/'pages'/f'{PREFIX}_12_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError('Page already saved; audit edits must be explicit.')
    assert text.startswith('\\scanpage{'+str(scan)+'}') or (scan == 51 and text.startswith('\\cotefile{12}'))
    path.write_text(text.strip()+'\n', encoding='utf-8')
    rows=[]
    for pos, kind, first in elements:
        rows.append([12,scan,sheet_kind,len(rows)+1,kind,pos,first,'yes'])
    for name, kind in [('deleted','deletion'),('inserted','insertion'),('margin','margin note')]:
        for at, val in macros(text,name):
            rows.append([12,scan,sheet_kind,len(rows)+1,kind,f'within page; TeX line {text[:at].count(chr(10))+1}',val.replace('\n',' ')[:220],'yes'])
    with (ROOT/f'{PREFIX}_inventory.csv').open('a',encoding='utf-8',newline='') as f:
        csv.writer(f).writerows(rows)
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'12 scan {scan:03d} done {utc()}\n')
    with (ROOT/'records'/'page_records.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps({'scan':scan,'elements':elements,'sheet_kind':sheet_kind,'remarks':remarks},ensure_ascii=False)+'\n')
    rebuild_doubts()
    print(f'Saved scan {scan:03d}: {len(rows)} inventory rows.')

def rebuild_doubts():
    target = ROOT/f'{PREFIX}_doubts.md'
    original=target.read_text(encoding='utf-8')
    heading=original.split('# Doubts by page')[0]
    tail=original.split('# Abbreviations',1)[1]
    lines=['# Doubts by page','','Locations are TeX source lines within the named page fragment; repeated doubtful symbols are listed at each occurrence. Confidence concerns the offered reading, not the mathematical plausibility.','','| Cote | Scan | Approximate line / element | Reading | Alternative / issue | Confidence |','|---|---|---|---|---|---|']
    def clean(s):
        return s.replace('\n',' ').replace('|','\\|').replace('`','&#96;')
    for p in sorted((ROOT/'pages').glob('*.tex')):
        scan=int(re.search(r'scan(\d+)',p.name).group(1))
        tex=p.read_text(encoding='utf-8')
        for at, val in macros(tex,'unsure'):
            reading, sep, alt=val.partition('|')
            lines.append(f'| 12 | {scan:03d} | TeX line {tex[:at].count(chr(10))+1} | `{clean(reading)}` | {clean(alt) if sep else "Incomplete or ambiguous pen strokes"} | medium |')
        for at,val in macros(tex,'illegible'):
            lines.append(f'| 12 | {scan:03d} | TeX line {tex[:at].count(chr(10))+1} | `\\illegible{{{val}}}` | Ink cannot be resolved after enlargement | low |')
    target.write_text(heading+'\n'.join(lines)+'\n\n# Abbreviations'+tail,encoding='utf-8')

if __name__ == '__main__':
    rebuild_doubts()
