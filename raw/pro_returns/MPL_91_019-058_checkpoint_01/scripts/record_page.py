from pathlib import Path
from datetime import datetime, timezone
import csv,json,re,sys
ROOT=Path(__file__).resolve().parent.parent

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def macros(text,name):
    out=[]
    for m in re.finditer(r'\\'+name+r'\{',text):
        start=m.end(); depth=1; k=start
        while k<len(text) and depth:
            if text[k]=='{' and (k==0 or text[k-1]!='\\'): depth+=1
            if text[k]=='}' and (k==0 or text[k-1]!='\\'): depth-=1
            k+=1
        out.append((text.count('\n',0,m.start())+1,text[start:k-1]))
    return out

def finish(scan,text,elements,observations='',sheet_kind='text'):
    text=text.strip()+'\n'
    p=ROOT/'pages'/f'MPL_91_019-058_91_scan{scan:03}.tex'
    if p.exists(): raise ValueError('Page already recorded: '+str(scan))
    assert f'\\scanpage{{{scan}}}' in text
    p.write_text(text,encoding='utf8')
    with (ROOT/'MPL_91_019-058_inventory.csv').open('a',newline='',encoding='utf8') as f:
        wr=csv.writer(f)
        for i,e in enumerate(elements,1):
            wr.writerow([91,scan,sheet_kind,f'{scan:03}-{i:02}',*e,'yes'])
    with (ROOT/'precontext_observations.md').open('a',encoding='utf8') as f:
        f.write(f'\n## Scan {scan:03}\n\n'+observations.strip()+'\n')
    with (ROOT/'progress.log').open('a') as f: f.write(f'91 scan {scan:03} done {now()}\n')
    refresh()
    print(f'Saved scan {scan:03}: {len(text)} characters; {len(elements)} inventory elements; {len(macros(text,"unsure"))} doubt marks.')

def refresh():
    ps=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/'MPL_91_019-058_transcription.tex').write_text('\n'.join(p.read_text() for p in ps),encoding='utf8')
    notation=(ROOT/'notation.md').read_text() if (ROOT/'notation.md').exists() else ''
    out=['# Notation table\n',notation,'\n# Doubt register\n','Line references below are approximate lines of the individual page fragment (including its page markers); the quoted reading is the primary locator. Every uncertainty macro is registered, including repeated signs. Confidence is medium unless a question mark or illegible span makes it low. No unmarked reading is guaranteed.\n','| File | Scan | Approx. line | Reading | Alternatives | Confidence |','|---|---:|---:|---|---|---|']
    for p in ps:
        s=int(re.search(r'scan(\d+)',p.name)[1]); txt=p.read_text()
        for line,val in macros(txt,'unsure'):
            a=val.split('|',1); reading=a[0]; alt=a[1] if len(a)>1 else 'Unresolved; no reliable alternative'
            reading=reading.replace('|','&#124;').replace('\n',' ');alt=alt.replace('|','&#124;').replace('\n',' ')
            out.append(f'| 91 | {s} | {line} | `{reading}` | `{alt}` | '+('low' if '?' in val else 'medium')+' |')
        for line,val in macros(txt,'illegible'):
            out.append(f'| 91 | {s} | {line} | Physically unreadable span ({val} estimated words) | — | low |')
    out += ['\n# Abbreviations\n', (ROOT/'abbreviations.md').read_text() if (ROOT/'abbreviations.md').exists() else '', '\n# Legibility and reliability\n','This is a visual diplomatic reading of the supplied enhanced scans, with no OCR. Rapidly drawn word endings, overwriting, minute indices and crossed-out additions are the least secure. The in-place uncertainty marks take precedence over contextual mathematical plausibility. The context archive is excluded from the reading process.\n']
    (ROOT/'MPL_91_019-058_doubts.md').write_text('\n'.join(out),encoding='utf8')
if __name__=='__main__': refresh()
