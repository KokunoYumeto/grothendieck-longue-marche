"""Compare independent box readings, preserving exact texts and token changes."""
from pathlib import Path
import csv,difflib,json,re,sys
csv.field_size_limit(16 * 1024 * 1024)
ROOT=Path(__file__).resolve().parents[1]
def tokens(s):return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]',s)
def read(p):return list(csv.DictReader(p.open(),delimiter='\t'))
page=sys.argv[1]
a=read(ROOT/'second'/f'{page}_first.tsv'); b=read(ROOT/'second'/f'{page}_second.tsv')
bb={x['box']:x['reading'] for x in b}
if len(bb)!=len(b):raise ValueError('Duplicate second-reading boxes')
if set(bb)!={x['box'] for x in a}:raise ValueError('First/second box sets differ')
rows=[]
for x in a:
    first=x['reading'];second=bb[x['box']];at=tokens(first);bt=tokens(second)
    diff=[]
    # Large literal TikZ outlines contain thousands of repeated punctuation tokens.
    # The matcher heuristic changes block selection only: every token, complete
    # reading and unequal interval is still retained in the comparison output.
    large = max(len(at), len(bt)) > 20000
    for tag,i,j,k,l in difflib.SequenceMatcher(None,at,bt,autojunk=large).get_opcodes():
        if tag!='equal':diff.append({'type':tag,'first_tokens':at[i:j],'second_tokens':bt[k:l]})
    rows.append({'box':x['box'],'same_tokens':not diff,'first':first,'second':second,'token_changes':diff})
(ROOT/'second'/f'{page}_comparison.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':page,'boxes':len(rows),'different':sum(not r['same_tokens'] for r in rows)},ensure_ascii=False))
for r in rows:
    if not r['same_tokens']:print(json.dumps(r,ensure_ascii=False))
