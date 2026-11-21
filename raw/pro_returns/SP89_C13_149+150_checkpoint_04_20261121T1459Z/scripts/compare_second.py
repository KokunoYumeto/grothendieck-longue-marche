from pathlib import Path
import csv,re,json,sys,difflib

W=Path(__file__).resolve().parents[1]

def rows(path):
    with path.open() as f:
        return list(csv.DictReader(f,delimiter='\t'))

def tokens(s):
    # Preserve every source-bearing TeX command, letter, digit and punctuation.
    # Only spacing is ignored. No semantic/lexical or editorial normalization.
    return re.findall(r'\\[A-Za-z]+|\\.|[^\W\d_]+|\d+|[^\s]',s,re.UNICODE)

def compare(page):
    a=rows(W/'second'/f'{page}_first.tsv')
    b=rows(W/'second'/f'{page}_second.tsv')
    expected=[x['box'] for x in rows(W/'second'/f'{page}_boxes.tsv')]
    if [x['box'] for x in a]!=expected or [x['box'] for x in b]!=expected:
        raise ValueError('Box coverage/order differs: '+page)
    out=[];identical=0
    for x,y in zip(a,b):
        at,bt=tokens(x['reading']),tokens(y['reading'])
        ops=[dict(operation=t,first_tokens=at[i:j],second_tokens=bt[k:l])
             for t,i,j,k,l in difflib.SequenceMatcher(a=at,b=bt,autojunk=False).get_opcodes()
             if t!='equal']
        if not ops:identical+=1
        out.append(dict(box=x['box'],first=x['reading'],second=y['reading'],
                        token_equal=not ops,differences=ops))
    dest=W/'second'/f'{page}_comparison.json'
    dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(page=page,boxes=len(out),equal=identical,different=len(out)-identical)))
    return out

if __name__=='__main__':
    for page in sys.argv[1:]:compare(page)
