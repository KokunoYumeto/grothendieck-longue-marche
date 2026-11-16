"""Literal/regex research searches after the transcription freeze; no OCR."""
from pathlib import Path
import argparse, datetime, json, re

ROOT=Path(__file__).resolve().parents[1]
CONTEXT=ROOT.parent/'context'

def search(pattern):
    rx=re.compile(pattern,re.I)
    hits=[]
    for path in sorted(CONTEXT.rglob('*')):
        if not path.is_file() or path.suffix not in ('.md','.tex','.txt'):
            continue
        cote=scan=None
        heading=''
        for lineno,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
            m=re.search(r'\\cotefile\{([^}]+)\}',line)
            if m:cote=m.group(1);scan=None
            m=re.search(r'\\scanpage\{([^}]+)\}',line)
            if m:scan=m.group(1)
            if line.startswith('#'):heading=line
            if rx.search(line):
                hits.append({'file':str(path.relative_to(CONTEXT)),'line':lineno,'cote':cote,'scan':scan,'heading':heading,'text':line})
    return hits

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('note')
    parser.add_argument('pattern')
    parser.add_argument('--limit',type=int,default=24)
    args=parser.parse_args()
    assert (ROOT/'records/frozen_hashes.json').exists()
    hits=search(args.pattern)
    record={'note':args.note,'utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'scope':'all supplied context .md/.tex/.txt files; PDF text when available separately','pattern':args.pattern,'count':len(hits),'hits':hits}
    with (ROOT/'records/research_root_searches.jsonl').open('a',encoding='utf-8') as out:
        out.write(json.dumps(record,ensure_ascii=False)+'\n')
    print(json.dumps({'note':args.note,'pattern':args.pattern,'count':len(hits),'hits':hits[:args.limit]},ensure_ascii=False,indent=2))
