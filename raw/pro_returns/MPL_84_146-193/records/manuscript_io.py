from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def escaped(text, index):
    """Whether the character at index follows an odd run of backslashes."""
    backslashes, cursor = 0, index - 1
    while cursor >= 0 and text[cursor] == '\\':
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1

def macro_values(text, macro):
    needle = '\\' + macro + '{'
    pos = 0
    while True:
        start = text.find(needle, pos)
        if start < 0:
            return
        if escaped(text, start):
            pos = start + len(needle)
            continue
        left = start + len(needle)
        level, end = 1, left
        while end < len(text) and level:
            if text[end] == '{' and not escaped(text, end):
                level += 1
            elif text[end] == '}' and not escaped(text, end):
                level -= 1
            end += 1
        if level:
            raise ValueError(f'Unclosed \\{macro} argument at source offset {start}')
        yield start, text[left:end-1]
        # Continue inside this argument, so nested occurrences are indexed too.
        pos = left

def split_alternative(value):
    """Split at the first unescaped pipe outside all nested brace groups."""
    level = 0
    for index, char in enumerate(value):
        if escaped(value, index):
            continue
        if char == '{':
            level += 1
        elif char == '}':
            level -= 1
        elif char == '|' and level == 0:
            return value[:index], '|', value[index+1:]
    return value, '', ''

def rebuild():
    records = sorted((ROOT/'records').glob('scan*.json'))
    with (ROOT/'MPL_84_146-193_inventory.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for rp in records:
            rec = json.loads(rp.read_text())
            for i, e in enumerate(rec['elements'], 1):
                w.writerow([84, rec['scan'], rec.get('sheet_kind','text'), i, *e, 'yes'])
    notation = (ROOT/'records/notation.md').read_text(encoding='utf-8')
    lines = [notation, '\n# Doubt register\n',
        'Locations below give the approximate vertical block and the line in the page LaTeX file. Every `\\unsure` and `\\illegible` occurrence is indexed; the transcription is the authoritative location. Repeated entries represent repeated occurrences, not independent evidence.\n',
        '| Cote | Scan | Approximate position / source line | Reading | Alternatives | Confidence |',
        '|---|---|---|---|---|---|']
    for rp in records:
        rec = json.loads(rp.read_text())
        page = ROOT/'pages'/f'MPL_84_146-193_84_scan{rec["scan"]:03d}.tex'
        tex = page.read_text(encoding='utf-8')
        for start, val in sorted(list(macro_values(tex,'unsure')) + list(macro_values(tex,'illegible'))):
            line = tex.count('\n',0,start)+1
            prefix = tex[:start]
            block = re.findall(r'% position: ([^\n]+)',prefix)
            pos = block[-1] if block else 'top'
            reading, sep, alt = split_alternative(val)
            conf = 'low' if sep or '\\deleted{' in tex[max(0,start-12):start] else 'medium'
            if tex[start:start+10] == '\\illegible':
                reading, alt, conf = f'{val} unreadable word(s)', 'none defensible', 'low'
            reading = reading.replace('|','&#124;')
            alt = (alt or 'not securely resolved').replace('|','&#124;')
            lines.append(f'| 84 | {rec["scan"]} | {pos}; source line {line} | `{reading}` | `{alt}` | {conf} |')
    abbr = ROOT/'records/abbreviations.md'
    limits = ROOT/'records/legibility.md'
    lines += ['\n# Abbreviations\n',abbr.read_text() if abbr.exists() else 'Register in progress.\n',
        '\n# Legibility and limits\n',limits.read_text() if limits.exists() else 'Register in progress.\n']
    (ROOT/'MPL_84_146-193_doubts.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    pages = sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/'MPL_84_146-193_transcription.tex').write_text('\n'.join(p.read_text() for p in pages),encoding='utf-8')

if __name__ == '__main__':
    if sys.argv[1] == 'done':
        scan = int(sys.argv[2])
        rebuild()
        with (ROOT/'progress.log').open('a') as f:
            f.write(f'84 scan {scan:03d} done {utc()}\n')
        print(f'Saved scan {scan:03d}; inventory and doubts rebuilt.')
    elif sys.argv[1] == 'rebuild':
        rebuild()
