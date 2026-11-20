"""Show compact textual differences between independent returns; no image reading."""
from pathlib import Path
import argparse,json,re,difflib
O=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('stem');p.add_argument('--reports',action='store_true');a=p.parse_args()
def tokens(text):
    text=re.sub(r'(?m)^%.*$','',text)
    return re.findall(r'\\[A-Za-z]+|[^\s{}]+|[{}]',text)
allr={}
for rid in ['r1','r2','r3']:
    q=O/'readers'/a.stem/rid
    if not (q/'report.json').exists():print(rid,'PENDING');continue
    r=json.loads((q/'report.json').read_text());allr[rid]=r
    t=(q/'reading.tex').read_text()
    print(rid,'differences',len(r.get('differences',[])),'C questions',len(r.get('c_doubts',[])),'unresolved',len(r.get('unresolved',[])),'inventory',len(r.get('inventory',[])),'crops',len(r.get('crops',[])))
    if rid=='r1':base=tokens(t)
    elif 'r1' in allr:
        current=tokens(t)
        for tag,i,j,k,l in difflib.SequenceMatcher(a=base,b=current,autojunk=False).get_opcodes():
            if tag!='equal':print('VS r1',tag,repr(' '.join(base[max(0,i-3):min(len(base),j+3)])),'=>',repr(' '.join(current[max(0,k-3):min(len(current),l+3)])))
    if a.reports:
        for d in r.get('differences',[]):
            print(json.dumps({k:d.get(k) for k in ['id','place','C','H','reading','source','bbox','diff_C','diff_H','confidence']},ensure_ascii=False))
        print('notes',json.dumps(r.get('notes',[]),ensure_ascii=False))
        print('checks',json.dumps(r.get('checks',[]),ensure_ascii=False))
print('All complete:',len(allr)==3)
