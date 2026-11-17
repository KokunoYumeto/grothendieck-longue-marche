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

def split_reading(value):
    depth=0
    for i,c in enumerate(value):
        if c=='{' and (i==0 or value[i-1]!='\\'): depth+=1
        elif c=='}' and (i==0 or value[i-1]!='\\'): depth-=1
        elif c=='|' and depth==0: return [value[:i],value[i+1:]]
    return [value]

def reading_confidence(scan,line,value):
    if '?' in value or len(value)>65 or '\\illegible' in value: return 'low'
    difficult={19,27,37,39,41,44,45,52,55,56,57,58}
    if scan in difficult and len(value)>17 and ' ' in value: return 'low'
    if scan==55 and line>=12: return 'low'
    return 'medium'

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
    combined=ROOT/'MPL_91_019-058_transcription.tex'
    joined=b''.join(p.read_bytes() for p in ps)
    if 'transcription frozen' in (ROOT/'progress.log').read_text():
        assert combined.read_bytes()==joined, 'Frozen transcription must not change'
    else:
        combined.write_bytes(joined)
    notation=(ROOT/'notation.md').read_text() if (ROOT/'notation.md').exists() else ''
    out=['# Notation table\n',notation,'\n# Doubt register\n','Line references below are approximate lines of the individual page fragment (including its page markers); the quoted reading is the primary locator. Every uncertainty macro is registered, including repeated signs. Confidence rates the visual reading only. Long or especially difficult marginal/cancelled readings are low; other tentative readings are medium. No unmarked reading is guaranteed.\n','| File | Scan | Approx. line | Reading | Alternatives | Confidence |','|---|---:|---:|---|---|---|']
    for p in ps:
        s=int(re.search(r'scan(\d+)',p.name)[1]); txt=p.read_text()
        for line,val in macros(txt,'unsure'):
            a=split_reading(val); reading=a[0]; alt=a[1] if len(a)>1 else 'Unresolved; no reliable alternative'
            reading=reading.replace('|','&#124;').replace('\n',' ');alt=alt.replace('|','&#124;').replace('\n',' ')
            out.append(f'| 91 | {s} | {line} | `{reading}` | `{alt}` | '+reading_confidence(s,line,val)+' |')
        for line,val in macros(txt,'illegible'):
            out.append(f'| 91 | {s} | {line} | Physically unreadable span ({val} estimated words) | — | low |')
    out += ['\n# Abbreviations\n', (ROOT/'abbreviations.md').read_text() if (ROOT/'abbreviations.md').exists() else '', '\n# Legibility and reliability\n',(ROOT/'reliability.md').read_text()]
    (ROOT/'MPL_91_019-058_doubts.md').write_text('\n'.join(out),encoding='utf8')
if __name__=='__main__': refresh()
