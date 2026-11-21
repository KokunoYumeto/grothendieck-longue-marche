"""Token-by-token comparison, preserving all reading and uncertainty tokens.

Whitespace, line breaks, dollar delimiters, and TeX spacing/size commands are
layout only. Equivalent arrows and tilde macro spellings are canonicalized.
All other tokens, including cancellation/insertion wrappers, punctuation,
case, accents, indices and uncertainty alternatives, remain in comparison.
"""
from pathlib import Path
import argparse,csv,difflib,hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]

def tokens(s):
    s=re.sub(r'(?<!\\)%[^\n]*','',s)
    s=s.replace('\\widetilde','\\tilde').replace('\\longrightarrow','\\rightarrow').replace('\\longleftarrow','\\leftarrow').replace('\\longmapsto','\\mapsto')
    s=re.sub(r'\\(?:qquad|quad|left|right|bigl|bigr|Bigl|Bigr|big|Big|displaystyle|textstyle)\b','',s)
    s=re.sub(r'\\[,;!: ]','',s)
    s=s.replace('$','')
    for delimiter in [r'\(', r'\)', r'\[', r'\]']:
        s=s.replace(delimiter,'')
    return re.findall(r'\\[A-Za-z]+|\\.|[^\s]',s)

def load(path):
    return list(csv.DictReader(path.open(),delimiter='\t'))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('scan',type=int);args=ap.parse_args()
    stem=f'149_scan{args.scan:03d}';dest=ROOT/'second'
    sealed=json.loads((dest/'SECOND_READINGS_SHA256.json').read_text())[stem]
    for entry in sealed['files']:
        if hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()!=entry['sha256']:
            raise ValueError('A sealed independent reading was modified before comparison.')
    first=load(dest/f'{stem}_first.tsv');second=load(dest/f'{stem}_second.tsv');boxes=load(dest/f'{stem}_boxes.tsv')
    ids=[r['box'] for r in boxes]
    if [r['box'] for r in first]!=ids or [r['box'] for r in second]!=ids:
        raise ValueError('The first and second readings must match the box order exactly.')
    comparison=[]
    for a,b in zip(first,second):
        ta,tb=tokens(a['reading']),tokens(b['reading'])
        operations=[]
        for op,i,j,k,l in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes():
            if op!='equal':operations.append({'operation':op,'first_span':[i,j],'second_span':[k,l],'first_tokens':ta[i:j],'second_tokens':tb[k:l]})
        comparison.append({'box':a['box'],'first':a['reading'],'second':b['reading'],'different':ta!=tb,'raw_different':a['reading']!=b['reading'],'operations':operations})
    (dest/f'{stem}_comparison.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2)+'\n')
    with (dest/f'{stem}_differences.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['box','first','second','token_difference'])
        for r in comparison:
            if r['different']:w.writerow([r['box'],r['first'],r['second'],json.dumps(r['operations'],ensure_ascii=False)])
    print(json.dumps({'scan':args.scan,'boxes':len(ids),'differences':sum(r['different'] for r in comparison),'layout_only':sum(r['raw_different'] and not r['different'] for r in comparison)}))

if __name__=='__main__':main()
