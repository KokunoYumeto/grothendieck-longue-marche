from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def record_page(scan, text, elements, sheet_kind='text', notes=''):
    path = ROOT / 'pages' / f'MPL_105_105_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError(f'Already recorded: {scan}')
    text = text.strip() + '\n\n'
    if f'\\scanpage{{{scan}}}' not in text:
        raise ValueError('Missing scan marker')
    path.write_text(text, encoding='utf-8')
    with (ROOT / 'MPL_105_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i, (kind, position, opening) in enumerate(elements, 1):
            writer.writerow(['105', scan, sheet_kind, f'{scan:03d}-{i:02d}', kind, position, opening, 'yes'])
    if notes:
        with (ROOT / 'records' / 'precontext_observations.md').open('a', encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03d}\n\n{notes}\n')
    with (ROOT / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(f'105 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}; {len(elements)} inventory elements.')

def build_doubts():
    intro=(ROOT/'records'/'notation_and_legibility.md').read_text(encoding='utf-8')
    rows=[]
    for path in sorted((ROOT/'pages').glob('*.tex')):
        text=path.read_text(encoding='utf-8')
        scan=int(re.search(r'scan(\d+)',path.name).group(1))
        for m in re.finditer(r'\\(unsure|illegible)\{',text):
            start=m.end(); level=1; end=start
            while end<len(text) and level:
                if text[end]=='{' and (end==0 or text[end-1]!='\\'): level+=1
                elif text[end]=='}' and (end==0 or text[end-1]!='\\'): level-=1
                end+=1
            val=text[start:end-1]
            reading,sep,alternative=val.partition('|')
            if m.group(1)=='illegible':
                reading=f'Physically obscured: approximately {val} word(s)'; alternative='No reliable recovery'; confidence='low'
            else:
                alternative=alternative if sep else 'Unresolved; no secure alternative'; confidence='medium'
            line=text.count('\n',0,m.start())+1
            vals=['105',f'{scan:03d}',f'TeX line {line}',reading,alternative,confidence]
            rows.append('| '+' | '.join(v.replace('|','\\|').replace('\n',' ') for v in vals)+' |')
    header='\n## Reading doubts\n\nLocations give the approximate line in the page fragment; the page fragment and inventory supply the spatial context. Medium means a tentative ink-based reading, not confirmation from mathematics. Unrecoverable cancellations are low confidence.\n\n| File | Scan | Approximate line | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n'
    (ROOT/'MPL_105_doubts.md').write_text(intro+header+'\n'.join(rows)+'\n',encoding='utf-8')

if __name__=='__main__':
    build_doubts()
