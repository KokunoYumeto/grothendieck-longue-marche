"""Structural LaTeX checks and independent-reading token comparison; no OCR."""
from pathlib import Path
import json, re, csv, hashlib, argparse, difflib

ROOT=Path(__file__).resolve().parents[1]

def uncomment(s):
    return '\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())

def tokens(s):
    return re.findall(r'\\[A-Za-z]+\*?|\\.|[A-Za-zÀ-ÿ]+|[0-9]+|[^\s]',s)

def check(path):
    s=uncomment(path.read_text());errors=[];balance=0
    for m in re.finditer(r'(?<!\\)[{}]',s):
        balance+=1 if m.group()=='{' else -1
        if balance<0:errors.append('closing brace before opening');break
    if balance:errors.append(f'brace balance {balance}')
    ds=len(re.findall(r'(?<!\\)\$',s))
    if ds%2:errors.append(f'odd dollar count {ds}')
    if len(re.findall(r'(?<!\\)\\\[',s))!=len(re.findall(r'(?<!\\)\\\]',s)):errors.append('display delimiters differ')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
        typ,env=m.groups()
        if typ=='begin':stack.append(env)
        elif not stack or stack.pop()!=env:errors.append('environment mismatch '+env)
    if stack:errors.append('unclosed environments '+repr(stack))
    return errors

def compare_second():
    summary=[]
    for fp in sorted((ROOT/'second').glob('*_first.tsv')):
        base=fp.name.removesuffix('_first.tsv');sp=ROOT/'second'/f'{base}_second.tsv'
        if not sp.exists():continue
        def read(p):
            with p.open() as f:return {r['box']:r['reading'] for r in csv.DictReader(f,delimiter='\t')}
        a,b=read(fp),read(sp);rows=[]
        for box in a.keys()|b.keys():
            at,bt=tokens(a.get(box,'')),tokens(b.get(box,''))
            if at!=bt:
                ops=[{'tag':tag,'first':at[i:j],'second':bt[k:l]} for tag,i,j,k,l in difflib.SequenceMatcher(None,at,bt,autojunk=False).get_opcodes() if tag!='equal']
                rows.append(dict(box=box,first=a.get(box,''),second=b.get(box,''),token_differences=json.dumps(ops,ensure_ascii=False),decision='',evidence=''))
        op=ROOT/'second'/f'{base}_differences.tsv'
        # Preserve decisions on repeated comparison when both source readings match.
        old={}
        if op.exists():
            with op.open() as f:old={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
        for r in rows:
            o=old.get(r['box'],{})
            if o.get('first')==r['first'] and o.get('second')==r['second']:
                r['decision']=o.get('decision','');r['evidence']=o.get('evidence','')
        rows.sort(key=lambda x:x['box'])
        with op.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=['box','first','second','token_differences','decision','evidence'],delimiter='\t');w.writeheader();w.writerows(rows)
        summary.append({'page':base,'boxes':len(a),'second_boxes':len(b),'differences':len(rows),'undecided':sum(not r['decision'] for r in rows)})
    (ROOT/'records/second_comparison_summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary))

def validate():
    result={p.name:check(p) for p in sorted((ROOT/'pages').glob('*.tex'))}
    combined=ROOT/'SP116_CW_75_transcription.tex'
    if combined.exists():result[combined.name]=check(combined)
    (ROOT/'records/latex_balance.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['validate','compare']);a=p.parse_args()
    validate() if a.action=='validate' else compare_second()
