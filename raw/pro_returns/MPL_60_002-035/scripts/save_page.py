import csv, json, re, sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_60_002-035'

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def extract_macro(text, macro):
    start = 0
    marker = '\\' + macro + '{'
    while True:
        i = text.find(marker, start)
        if i < 0: break
        a = i + len(marker)
        j, depth = a, 1
        while j < len(text) and depth:
            if text[j] == '{' and (j == 0 or text[j-1] != '\\'): depth += 1
            if text[j] == '}' and (j == 0 or text[j-1] != '\\'): depth -= 1
            j += 1
        yield text[a:j-1], text[:i].count('\n')+1
        start = j

def rebuild():
    records = [json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('page*.json'))]
    with (ROOT/(PREFIX+'_inventory.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for rec in records:
            for i,row in enumerate(rec['inventory'],1):
                w.writerow([60,rec['scan'],rec.get('sheet_kind','text'),i,*row,'yes'])
    notation=(ROOT/'records/notation.md').read_text() if (ROOT/'records/notation.md').exists() else '# Notation table\n\nTo be extended as signs occur.\n'
    lines=[notation.rstrip(),'','## Doubts','', 'Line numbers refer to the corresponding page LaTeX file; positions in the source are also recorded where necessary. Every `unsure` and `illegible` token is indexed. A doubt mark is a palaeographic reservation, not a mathematical correction. Macro-index rows use medium confidence by default; a more specific palaeographic row at the same location supplies the controlling confidence and explanation.','', '| File | Scan | Approximate line | Reading | Alternative / issue | Confidence |','|---|---:|---|---|---|---|']
    esc=lambda x:str(x).replace('|','\\|').replace('\n',' ')
    for rec in records:
        for macro in ['unsure','illegible']:
            for value,ln in extract_macro(rec['text'],macro):
                parts=value.split('|',1)
                read=parts[0] if macro=='unsure' else 'Unreadable: '+parts[0]+' word(s)'
                alt=parts[1] if len(parts)>1 else ('Incomplete or ambiguous ink' if macro=='unsure' else 'No secure reading')
                lines.append('| 60 | '+str(rec['scan'])+' | '+str(ln)+' | `'+esc(read)+'` | '+esc(alt)+' | '+('low' if macro=='illegible' else 'medium')+' |')
        for d in rec.get('doubts',[]):
            lines.append('| 60 | '+str(rec['scan'])+' | '+' | '.join(esc(v) for v in d)+' |')
    lines+=['','## Abbreviations','', (ROOT/'records/abbreviations.md').read_text().rstrip() if (ROOT/'records/abbreviations.md').exists() else 'None recorded yet.','','## Legibility and limits','',(ROOT/'records/legibility.md').read_text().rstrip() if (ROOT/'records/legibility.md').exists() else 'Provisional: assessed during the sequential visual reading.','']
    (ROOT/(PREFIX+'_doubts.md')).write_text('\n'.join(lines),encoding='utf-8')
    (ROOT/(PREFIX+'_transcription.tex')).write_text(''.join(rec['text'] for rec in records),encoding='utf-8')

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='rebuild':
        rebuild()
    else:
        p=json.load(sys.stdin)
        n=p['scan']
        page=ROOT/'pages'/f'{PREFIX}_60_scan{n:03d}.tex'
        if page.exists(): raise SystemExit('Page exists; edit explicitly and update record before rebuilding.')
        if not p['text'].endswith('\n'): p['text']+='\n'
        page.write_text(p['text'],encoding='utf-8')
        (ROOT/'records'/f'page{n:03d}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        rebuild()
        with (ROOT/'progress.log').open('a') as f: f.write(f'60 scan {n:03d} done {now()}\n')
        print(f'Saved scan {n:03d}: {len(p["inventory"])} inventory elements.')
