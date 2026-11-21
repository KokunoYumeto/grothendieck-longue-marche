"""Coverage screens for the completed first readings, without image recognition.

These checks find documentary omissions; they do not establish that a box
geometrically covers its intended ink. The main reader separately checks that.
Run before prepare_second.py freezes the first readings and coordinates.
"""
from pathlib import Path
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
SCANS = list(range(108, 118)) + list(range(119, 132))
assert not (ROOT/'second/first_readings_frozen.json').exists()
records = []
def normalized(s): return re.sub(r'\s+', '', s)
for scan in SCANS:
    stem = f'147_scan{scan}'
    page = (ROOT/'pages'/f'{stem}.tex').read_text()
    report = json.loads((ROOT/'review'/f'{stem}_reviewed.json').read_text())
    first = list(csv.DictReader((ROOT/'second'/f'{stem}_first.tsv').open(), delimiter='\t'))
    boxes = list(csv.DictReader((ROOT/'second'/f'{stem}_boxes.tsv').open(), delimiter='\t'))
    assert [x['box'] for x in first] == [x['box'] for x in boxes]
    assert len({x['box'] for x in boxes}) == len(boxes)
    for box, reading, original in zip(boxes, first, report['second_boxes']):
        assert box['box'] == original['box'] == reading['box']
        assert [int(box[k]) for k in ('x0','y0','x1','y1')] == original['coords']
        assert reading['reading'] == original['reading']
    full_text = '\n'.join(x['reading'] for x in first)
    numbers = set(re.findall(r'\d+', re.sub(r'\\scanpage\{\d+\}', '', page)))
    missing_numbers = sorted(numbers - set(re.findall(r'\d+', full_text)))
    candidates = []
    for m in re.finditer(r'\\(deleted|inserted|margin|mspage)\{', page):
        start = m.end(); depth = 1; i = start
        while i < len(page) and depth:
            if page[i] == '{' and page[i-1] != '\\': depth += 1
            elif page[i] == '}' and page[i-1] != '\\': depth -= 1
            i += 1
        argument = page[start:i-1]
        if normalized(argument) and not any(normalized(argument) in normalized(x['reading']) for x in first):
            candidates.append({'macro': m[1], 'argument': argument})
    links = ' '.join(x['statement_id'] for x in report.get('check_events', []))
    unlinked = [f'N{scan}-{i:02d}' for i in range(1,len(report.get('notes',[]))+1)
                if f'N{scan}-{i:02d}' not in links]
    records.append({'page':stem, 'boxes':len(boxes),
                    'numeric_tokens_not_in_first_readings':missing_numbers,
                    'literal_argument_coverage_candidates':candidates,
                    'notes_without_check_event_link':unlinked})
out={'scope':'Literal/numeric documentary coverage only, not proof of geometric coverage. '
             'A passage split across boxes or alternative spacing syntax can appear as a candidate.',
     'pages':records}
(ROOT/'review/preblind_coverage_screen.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
