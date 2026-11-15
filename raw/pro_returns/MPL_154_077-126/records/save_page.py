from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys, re
ROOT=Path(__file__).resolve().parents[1]
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def macros(text, name):
    start=0
    key='\\'+name+'{'
    while (at:=text.find(key,start))>=0:
        pos=at+len(key); depth=1; end=pos
        while end<len(text) and depth:
            if text[end]=='{' and (end==0 or text[end-1]!='\\'): depth+=1
            if text[end]=='}' and (end==0 or text[end-1]!='\\'): depth-=1
            end+=1
        yield at,text[pos:end-1]
        start=end

def regenerate_doubts():
    notation=ROOT/'records/notation.md'
    intro=notation.read_text() if notation.exists() else '# Notation table\n\nTable in progress.\n'
    lines=[intro,'\n# Doubt register\n\nApproximate lines are numbered in the page fragment; wrapped manuscript lines are not normalized. Each entry is a visual uncertainty, not a proposed correction.\n\n| File | Scan | Approx. line in fragment | Reading | Alternative | Confidence |\n|---|---:|---:|---|---|---|']
    for path in sorted((ROOT/'pages').glob('*.tex')):
        t=path.read_text(); scan=int(re.search(r'scan(\d+)',path.name)[1])
        for at,body in macros(t,'unsure'):
            options=body.split('|',1); reading=options[0]; alt=options[1] if len(options)>1 else 'No independently secure alternative'
            safe=lambda s:s.replace('|','&#124;').replace('\n',' ').replace('`','&#96;')
            lines.append(f'| 154 | {scan} | {t[:at].count(chr(10))+1} | `{safe(reading)}` | {safe(alt)} | low |')
        for at,body in macros(t,'illegible'):
            lines.append(f'| 154 | {scan} | {t[:at].count(chr(10))+1} | Physically unreadable: {body} word(s) | — | low |')
    footer=ROOT/'records/doubts_footer.md'
    if footer.exists(): lines.append('\n'+footer.read_text())
    (ROOT/'MPL_154_077-126_doubts.md').write_text('\n'.join(lines)+'\n')

def save(data):
    n=int(data['scan']); p=ROOT/'pages'/f'MPL_154_077-126_154_scan{n:03}.tex'
    if p.exists() and not data.get('revise'): raise SystemExit(f'Page already exists: {p}')
    t=data['text'].rstrip()+'\n'
    if f'\\scanpage{{{n}}}' not in t: raise SystemExit('Missing scan marker')
    p.write_text(t)
    inv=ROOT/'MPL_154_077-126_inventory.csv'
    with inv.open(newline='') as f: rows=list(csv.reader(f))
    rows=[rows[0]]+[r for r in rows[1:] if r[1]!=str(n)]
    for i,e in enumerate(data['elements'],1):
        kind,pos,first=e
        rows.append(['154',str(n),data.get('sheet_kind','text'),str(i),kind,pos,first,'yes'])
    with inv.open('w',newline='') as f: csv.writer(f).writerows(rows)
    with (ROOT/'progress.log').open('a') as f: f.write(f'154 scan {n:03} '+('revised' if data.get('revise') else 'done')+' '+utc()+'\n')
    regenerate_doubts()
    print(f'Saved scan {n:03}: {len(t)} characters; {len(data["elements"])} inventory elements')
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='doubts': regenerate_doubts()
    else: save(json.load(sys.stdin))
