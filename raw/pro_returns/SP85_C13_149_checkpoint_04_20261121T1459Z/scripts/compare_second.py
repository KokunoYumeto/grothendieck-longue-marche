"""Token-by-token comparison of independent written readings; no OCR."""
from pathlib import Path
import csv,re,difflib,json,sys

ROOT=Path(__file__).resolve().parents[1]
def read(path):
    return list(csv.DictReader(path.open(),delimiter='\t'))
def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]',s)
def run(page):
    a=read(ROOT/'second'/f'{page}_first.tsv');b=read(ROOT/'second'/f'{page}_second.tsv')
    assert [x['box'] for x in a]==[x['box'] for x in b],f'Box ID/order mismatch {page}'
    results=[]
    for x,y in zip(a,b):
        at,bt=tokens(x['reading']),tokens(y['reading'])
        ops=[{'type':op,'first_tokens':at[i:j],'second_tokens':bt[k:l]} for op,i,j,k,l in difflib.SequenceMatcher(None,at,bt,autojunk=False).get_opcodes() if op!='equal']
        results.append({'box':x['box'],'first':x['reading'],'second':y['reading'],'different':bool(ops),'token_differences':ops})
    (ROOT/'second'/f'{page}_comparison.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
    with (ROOT/'second'/f'{page}_comparison.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['box','different','first','second','token_operations'])
        for r in results:w.writerow([r['box'],'yes' if r['different'] else 'no',r['first'],r['second'],json.dumps(r['token_differences'],ensure_ascii=False)])
    print(json.dumps({'page':page,'boxes':len(results),'different_boxes':sum(r['different'] for r in results),'token_operations':sum(len(r['token_differences']) for r in results)}))
if __name__=='__main__':
    for page in sys.argv[1:]:run(page)
