#!/usr/bin/env python3
"""Record a visually completed page; never reads source images or performs OCR."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_134-8_043-087'
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def arguments(text, macro):
    start = 0
    needle = '\\' + macro + '{'
    while True:
        pos = text.find(needle, start)
        if pos < 0:
            return
        i = pos + len(needle)
        j, depth = i, 1
        while j < len(text) and depth:
            if text[j] == '{' and (j == 0 or text[j-1] != '\\'):
                depth += 1
            elif text[j] == '}' and (j == 0 or text[j-1] != '\\'):
                depth -= 1
            j += 1
        yield text.count('\n', 0, pos)+1, text[i:j-1]
        start = j

def main():
    data = json.load(sys.stdin)
    scan = int(data['scan'])
    page = ROOT/'pages'/f'{PREFIX}_134-8_scan{scan:03d}.tex'
    content = page.read_text()
    assert f'\\scanpage{{{scan}}}' in content
    inventory = ROOT/f'{PREFIX}_inventory.csv'
    with inventory.open(newline='') as f:
        rows = list(csv.DictReader(f))
    assert not any(int(r['scan']) == scan for r in rows), 'already recorded'
    with inventory.open('a',newline='') as f:
        out=csv.writer(f)
        for i, element in enumerate(data['elements'], 1):
            kind, position, incipit = element
            out.writerow(['134-8',f'{scan:03d}',data.get('sheet_kind','text'),f'{scan:03d}.{i:02d}',kind,position,incipit,'yes'])
    with (ROOT/f'{PREFIX}_doubts.md').open('a') as f:
        for line, reading in arguments(content,'unsure'):
            readings = reading.split('|',1)
            main = readings[0].replace('|','&#124;').replace('\n',' ')
            alt = readings[1].replace('|','&#124;').replace('\n',' ') if len(readings)>1 else 'Ink does not decide a firmer reading'
            conf = 'low' if len(readings)>1 else 'medium'
            f.write(f'| 134-8 | {scan:03d} | TeX line {line} | `{main}` | {alt} | {conf} |\n')
        for line, n in arguments(content,'illegible'):
            f.write(f'| 134-8 | {scan:03d} | TeX line {line} | Unreadable ink, estimated {n} word(s) | No reliable reading after visual enlargement | low |\n')
    if data.get('observations'):
        with (ROOT/'records'/'reading_observations.md').open('a') as f:
            f.write(f'\n## Scan {scan:03d}\n\n'+data['observations']+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'134-8 scan {scan:03d} full image, half a, half b visually read; line and element inventory checked.\n')
        f.write(f'134-8 scan {scan:03d} done {utc()}\n')
    (ROOT/'records'/f'scan{scan:03d}_inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(f'Scan {scan:03d}: saved; {len(data["elements"])} inventory elements; {len(list(arguments(content,"unsure")))} doubt markers.')

if __name__ == '__main__':
    main()
