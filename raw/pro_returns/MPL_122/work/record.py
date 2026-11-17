from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT=Path(__file__).resolve().parents[1]
SCANS=list(range(3,19))+list(range(20,36))
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f: f.write(s+'\n')

def _tex_structure(text):
    """Lex control sequences and balanced groups without treating escaped ink as syntax.

    This is a structural reader only: it neither interprets nor changes any
    manuscript reading. Comments, escaped braces, and inline verbatim spans
    do not contribute grouping braces.
    """
    commands, closes, stack = [], {}, []
    i = 0
    while i < len(text):
        char = text[i]
        if char == '%':
            newline = text.find('\n', i)
            i = len(text) if newline < 0 else newline + 1
        elif char == '\\':
            start = i
            i += 1
            if i < len(text) and (text[i].isalpha() or text[i] == '@'):
                first = i
                while i < len(text) and (text[i].isalpha() or text[i] == '@'):
                    i += 1
                name = text[first:i]
                commands.append((name, start, i))
                if name == 'verb':
                    if i < len(text) and text[i] == '*':
                        i += 1
                    if i < len(text):
                        delimiter = text[i]
                        end = text.find(delimiter, i + 1)
                        i = len(text) if end < 0 else end + 1
            else:
                # Includes control symbols \\{, \\}, \\%, and \\\\.
                i += 1
        elif char == '{':
            stack.append(i)
            i += 1
        elif char == '}':
            if stack:
                closes[stack.pop()] = i
            i += 1
        else:
            i += 1
    return commands, closes

def _next_group(text, position):
    while position < len(text):
        if text[position].isspace():
            position += 1
        elif text[position] == '%':
            newline = text.find('\n', position)
            position = len(text) if newline < 0 else newline + 1
        else:
            return position if text[position] == '{' else None
    return None

def _split_reading(argument):
    """Split only literal top-level pipes; nested/escaped pipes stay in place."""
    parts, depth, start, i = [], 0, 0, 0
    while i < len(argument):
        char = argument[i]
        if char == '%':
            newline = argument.find('\n', i)
            i = len(argument) if newline < 0 else newline + 1
        elif char == '\\':
            i += 1
            if i < len(argument) and (argument[i].isalpha() or argument[i] == '@'):
                while i < len(argument) and (argument[i].isalpha() or argument[i] == '@'):
                    i += 1
            else:
                i += 1
        else:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
            elif char == '|' and depth == 0:
                parts.append(argument[start:i].strip())
                start = i + 1
            i += 1
    parts.append(argument[start:].strip())
    return parts

def enumerate_unsure(text):
    """Return each balanced \\unsure argument, including nested occurrences."""
    commands, closes = _tex_structure(text)
    deletions = []
    for name, start, end in commands:
        if name == 'deleted':
            opening = _next_group(text, end)
            if opening is not None and opening in closes:
                deletions.append((opening, closes[opening]))
    entries = []
    for name, start, end in commands:
        if name != 'unsure':
            continue
        line = text.count('\n', 0, start) + 1
        opening = _next_group(text, end)
        if opening is None or opening not in closes:
            raise ValueError(f'Unbalanced or missing \\unsure argument at .tex line {line}')
        argument = text[opening + 1:closes[opening]]
        parts = _split_reading(argument)
        entries.append({
            'line': line,
            'argument': argument,
            'reading': parts[0],
            'alternatives': parts[1:],
            'deleted': any(left < start < right for left, right in deletions),
        })
    return entries

def _comparison_reading(text):
    # Exact textual matching after only presentation whitespace/math delimiters
    # are removed. No spelling, notation, or semantic normalization is done.
    text = str(text).strip().strip('`$ ')
    if text.startswith('\\(') and text.endswith('\\)'):
        text = text[2:-2]
    return re.sub(r'\s+', '', text)

def _manual_low_readings(meta):
    readings = set()
    for row in meta.get('doubts', []):
        if len(row) < 4 or str(row[-1]).strip().lower() != 'low':
            continue
        reading = str(row[1])
        readings.add(_comparison_reading(reading))
        try:
            for entry in enumerate_unsure(reading):
                readings.add(_comparison_reading(entry['argument']))
                readings.add(_comparison_reading(entry['reading']))
        except ValueError:
            pass
    return readings - {''}

def _md_cell(value):
    return str(value).replace('|', '&#124;').replace('\r', '').replace('\n', '<br>')

def supplementary_doubts(page_paths, metas):
    by_scan = {int(meta['scan']): meta for meta in metas}
    lines = [
        '', '## Supplementary enumeration of every `\\unsure` occurrence', '',
        'This table is extracted mechanically from the page fragments. The line number is the physical line in the named `.tex` page, not a manuscript line. Confidence defaults to medium; it is low for a reading inside `\\deleted`, or an exact textual match to a manually recorded low-confidence reading. These defaults do not replace the manual judgments above. Nested uncertainty marks each receive their own row.', '',
        '| Cote | Scan | Page `.tex` line | First reading | Alternatives | Confidence | Basis |',
        '|---|---:|---:|---|---|---|---|',
    ]
    for path in page_paths:
        scan = int(re.search(r'scan(\d{3})\.tex$', path.name).group(1))
        low_readings = _manual_low_readings(by_scan.get(scan, {}))
        for entry in enumerate_unsure(path.read_text(encoding='utf-8')):
            candidates = [_comparison_reading(entry['argument']), _comparison_reading(entry['reading'])]
            manual_low = any(candidate in low_readings for candidate in candidates)
            confidence = 'low' if entry['deleted'] or manual_low else 'medium'
            basis = []
            if entry['deleted']:
                basis.append('inside deletion')
            if manual_low:
                basis.append('manual low-confidence reading')
            if not basis:
                basis.append('default; see manual table where applicable')
            cells = [122, scan, entry['line'], entry['reading'], ' | '.join(entry['alternatives']) or '—', confidence, '; '.join(basis)]
            lines.append('| ' + ' | '.join(_md_cell(cell) for cell in cells) + ' |')
    return lines

def save(scan,tex,elements,doubts=(),observations=(),sheet_kind='text'):
    path=ROOT/'pages'/f'MPL_122_122_scan{scan:03}.tex'
    for earlier in SCANS[:SCANS.index(scan)]:
        assert (ROOT/'pages'/f'MPL_122_122_scan{earlier:03}.tex').exists(), earlier
    assert not path.exists(), 'Use an explicit audit edit for existing pages.'
    assert f'\\scanpage{{{scan}}}' in tex
    path.write_text(tex.strip()+'\n',encoding='utf-8')
    meta={'scan':scan,'sheet_kind':sheet_kind,'elements':elements,'doubts':doubts,'observations':observations}
    (ROOT/'work'/f'scan{scan:03}.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rebuild()
    log(f'122 scan {scan:03} done {now()}')
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements.')
def rebuild():
    metas=[json.loads(p.read_text()) for p in sorted((ROOT/'work').glob('scan[0-9][0-9][0-9].json'))]
    with (ROOT/'MPL_122_inventory.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f); w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for m in metas:
            for i,e in enumerate(m['elements'],1): w.writerow([122,m['scan'],m['sheet_kind'],f'{m["scan"]:03}-{i:02}',*e,'yes'])
    page_paths=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/'MPL_122_transcription.tex').write_text(''.join(p.read_text(encoding='utf-8') for p in page_paths),encoding='utf-8')
    notation=(ROOT/'work'/'notation.md').read_text() if (ROOT/'work'/'notation.md').exists() else ''
    lines=['# MPL_122 — Doubts and notation','',notation,'','## Reading doubts','', '| Cote | Scan | Approximate location | Reading | Alternatives / difficulty | Confidence |','|---|---:|---|---|---|---|']
    for m in metas:
        for d in m['doubts']:
            lines.append('| 122 | '+str(m['scan'])+' | '+' | '.join(str(s).replace('|','&#124;') for s in d)+' |')
    lines+=supplementary_doubts(page_paths,metas)
    lines+=['','## Abbreviations','', (ROOT/'work'/'abbreviations.md').read_text() if (ROOT/'work'/'abbreviations.md').exists() else 'In progress.','','## Legibility and limits','', (ROOT/'work'/'legibility.md').read_text() if (ROOT/'work'/'legibility.md').exists() else 'In progress; all doubt marks will be reviewed before the transcription is frozen.','']
    (ROOT/'MPL_122_doubts.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__': rebuild()
