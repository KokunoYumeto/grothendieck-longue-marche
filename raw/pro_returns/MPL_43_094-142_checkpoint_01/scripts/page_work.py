from pathlib import Path
from datetime import datetime, timezone
import csv, re, json

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_43_094-142'
FIELDS = ['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def braced(text, macro):
    for match in re.finditer(r'\\'+re.escape(macro)+r'\{', text):
        start=match.end(); depth=1; end=start
        while end<len(text) and depth:
            if text[end]=='{' and (end==0 or text[end-1]!='\\'): depth+=1
            if text[end]=='}' and (end==0 or text[end-1]!='\\'): depth-=1
            end+=1
        yield text.count('\n',0,match.start())+1, text[start:end-1]

def save_page(scan, text, elements, sheet_kind='text', observations=''):
    path=ROOT/'pages'/f'{PREFIX}_43_scan{scan:03}.tex'
    if path.exists(): raise RuntimeError(f'Page already saved: {path}')
    assert text.startswith(('\\cotefile{43}\n' if scan==94 else '')+f'\\scanpage{{{scan}}}')
    assert '\\documentclass' not in text and '\\includegraphics' not in text
    path.write_text(text.rstrip()+'\n\n',encoding='utf-8')
    with (ROOT/f'{PREFIX}_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS)
        for n,(kind,pos,words) in enumerate(elements,1):
            w.writerow(dict(cote=43,scan=scan,sheet_kind=sheet_kind,element=f'{scan:03}-{n:02}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
    (ROOT/'records'/f'scan{scan:03}_reading.txt').write_text(
        f'Scan {scan:03}: whole image and both supplied halves visually read by the primary reader.\n'
        'No OCR used. First transcription checked against the images; inventory completed.\n'+observations+'\n',encoding='utf-8')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'43 scan {scan:03} done {utc()}\n')
    rebuild()
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements; {len(list(braced(text,"unsure")))} doubt marks.')

def rebuild():
    pages=sorted((ROOT/'pages').glob(f'{PREFIX}_43_scan*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_bytes(b''.join(p.read_bytes() for p in pages))
    pre=(ROOT/'records/notation_and_abbreviations.md').read_text(encoding='utf-8')
    lines=[pre,'\n## Individual doubtful readings\n',
           'Approximate line numbers refer to the physical line in the page fragment; the quoted reading also locates the passage. A mark applies only to the enclosed ink. Confidence defaults to medium for a proposed reading, low for an unresolved pair or physically unreadable deleted text.\n',
           '| File | Scan | Approx. fragment line | Reading | Alternatives | Confidence |',
           '|---|---:|---:|---|---|---|']
    for p in pages:
        scan=int(re.search(r'scan(\d+)',p.name).group(1))
        t=p.read_text(encoding='utf-8')
        for line,reading in braced(t,'unsure'):
            parts=reading.split('|',1)
            esc=lambda s:s.replace('|','&#124;').replace('\n',' ')
            lines.append(f'| 43 | {scan} | {line} | `{esc(parts[0])}` | {"`"+esc(parts[1])+"`" if len(parts)>1 else "—"} | {"low" if len(parts)>1 else "medium"} |')
        for line,count in braced(t,'illegible'):
            lines.append(f'| 43 | {scan} | {line} | `\\illegible{{{count}}}` | No defensible word reading at inspected enlargement | low |')
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

if __name__=='__main__': rebuild()
