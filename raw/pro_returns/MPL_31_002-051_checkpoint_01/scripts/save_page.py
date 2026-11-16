from pathlib import Path
from datetime import datetime, timezone
import csv, json, re
BASE=Path(__file__).resolve().parent.parent
PREFIX='MPL_31_002-051'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def extract_macros(s):
    pat=re.compile(r'\\(unsure|illegible)\{')
    for m in pat.finditer(s):
        start=m.end(); depth=1; i=start
        while i<len(s) and depth:
            if s[i] in '{}':
                j=i-1
                while j>=0 and s[j]=='\\': j-=1
                if (i-1-j)%2==0: depth += 1 if s[i]=='{' else -1
            i+=1
        yield m.group(1),s[start:i-1],s[:m.start()].count('\n')+1

def rebuild():
    # Optional per-occurrence ratings use the complete, unmodified macro argument.
    # Example key: "002:L12:<full argument of unsure or illegible>".
    confidence_path=BASE/'records/doubt_confidence.json'
    confidence_overrides=json.loads(confidence_path.read_text(encoding='utf-8')) if confidence_path.exists() else {}
    if not isinstance(confidence_overrides,dict) or any(
        not isinstance(key,str) or value not in ('high','medium','low')
        for key,value in confidence_overrides.items()
    ):
        raise ValueError('records/doubt_confidence.json must map occurrence keys to high, medium, or low')
    pages=sorted((BASE/'pages').glob(PREFIX+'_31_scan*.tex'))
    (BASE/(PREFIX+'_transcription.tex')).write_bytes(b''.join(p.read_bytes() for p in pages))
    notation=(BASE/'records/notation.md').read_text() if (BASE/'records/notation.md').exists() else ''
    abbreviations=(BASE/'records/abbreviations.md').read_text() if (BASE/'records/abbreviations.md').exists() else ''
    rows=[]
    for p in pages:
        scan=int(re.search(r'scan(\d+)',p.name).group(1))
        for macro,value,line in extract_macros(p.read_text()):
            a=value.split('|',1)
            escape=lambda x:x.replace('|','&#124;').replace('\n',' ')
            confidence=confidence_overrides.get(f'{scan:03d}:L{line}:{value}', 'low' if macro=='illegible' else 'medium')
            rows.append(f'| 31 | {scan:03d} | fragment L{line} | `{escape(a[0])}` | {"`"+escape(a[1])+"`" if len(a)>1 else ("unreadable word(s)" if macro=="illegible" else "—")} | {confidence} |')
    intro='# Notation table\n\n'+notation+'\n\n# Doubt register\n\nLocations use line numbers in the individual page fragment, in manuscript reading order; they are approximate locations on the scan. Each doubtful occurrence is listed separately. Confidence is in the proposed reading, not in the mathematical assertion. A medium rating identifies a visual reading that remains uncertain; physically unreadable words are low.\n\n| Cote | Scan | Approximate location | Reading | Alternative | Confidence |\n|---|---:|---|---|---|---|\n'
    default_legibility='The transcription is being read directly from the supplied images without OCR. Rapid connected handwriting, abbreviated words, overwritten passages, and small superscripts require particular caution. Doubt marks record visual uncertainty rather than a correction from mathematical context. This note will be updated after the complete second reading.'
    legibility_path=BASE/'records/legibility.md'
    legibility=(legibility_path.read_text(encoding='utf-8').strip() or default_legibility) if legibility_path.exists() else default_legibility
    ending='\n\n# Abbreviations\n\n'+abbreviations+'\n\n# Legibility and limits\n\n'+legibility+'\n'
    (BASE/(PREFIX+'_doubts.md')).write_text(intro+'\n'.join(rows)+ending,encoding='utf-8')

def save(scan,text,elements,sheet_kind='text',observations=''):
    p=BASE/'pages'/f'{PREFIX}_31_scan{scan:03d}.tex'
    if p.exists(): raise RuntimeError(f'Page already exists: {p}; revise explicitly')
    p.write_text(text.strip()+'\n\n',encoding='utf-8')
    inventory=BASE/(PREFIX+'_inventory.csv')
    exists=inventory.exists()
    with inventory.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if not exists:w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for n,(kind,pos,words) in enumerate(elements,1):w.writerow([31,f'{scan:03d}',sheet_kind,f'{scan:03d}-{n:02d}',kind,pos,words,'yes'])
    if observations:
        with (BASE/'records/reading_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## Scan {scan:03d}\n\n{observations}\n')
    rebuild()
    with (BASE/'progress.log').open('a',encoding='utf-8') as f:f.write(f'31 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(elements)} inventory elements, {len(text)} characters')
