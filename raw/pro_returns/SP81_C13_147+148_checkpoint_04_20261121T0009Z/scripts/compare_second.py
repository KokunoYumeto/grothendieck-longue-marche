from pathlib import Path
import csv,json,re,difflib,sys,hashlib
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
page=sys.argv[1]
def read(suffix):
 p=root/'second'/f'{page}_{suffix}.tsv'
 return {r['box']:r['reading'] for r in csv.DictReader(p.open(),delimiter='\t')}
first=read('first');second=read('second')
first_path=root/'second'/f'{page}_first.tsv'
second_path=root/'second'/f'{page}_second.tsv'
assert first_path.stat().st_mtime_ns <= second_path.stat().st_mtime_ns, 'First reading must precede blind reading.'
assert first.keys()==second.keys(),(set(first)-set(second),set(second)-set(first))
def tokens(s):return re.findall(r'\\[a-zA-Z]+|\\.|[A-Za-zÀ-ž]+|[0-9]+|[^\s]',s)
rows=[]
for box,a in first.items():
 b=second[box];ta=tokens(a);tb=tokens(b)
 if ta!=tb:
  spans=[]
  for tag,i,j,k,l in difflib.SequenceMatcher(None,ta,tb,autojunk=False).get_opcodes():
   if tag!='equal':spans.append({'operation':tag,'first_tokens':ta[i:j],'second_tokens':tb[k:l]})
  rows.append({'box':box,'first':a,'second':b,'token_differences':spans})
(root/'second'/f'{page}_comparison.json').write_text(json.dumps({'page':page,'boxes':len(first),'different_boxes':len(rows),'differences':rows,
 'compared_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'first_sha256':hashlib.sha256(first_path.read_bytes()).hexdigest(),
 'second_sha256':hashlib.sha256(second_path.read_bytes()).hexdigest(),
 'first_written_at':datetime.fromtimestamp(first_path.stat().st_mtime,timezone.utc).isoformat(),
 'second_written_at':datetime.fromtimestamp(second_path.stat().st_mtime,timezone.utc).isoformat()},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':page,'boxes':len(first),'different_boxes':len(rows)}))
