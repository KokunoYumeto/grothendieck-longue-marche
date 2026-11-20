"""Literal token-by-token comparison of the written first and blind readings.
Only whitespace is ignored. No reading is chosen by this script.
"""
from pathlib import Path
import csv,re,difflib,json
root=Path(__file__).resolve().parents[1]
token=re.compile(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]')
def load(p):
 with p.open(newline='') as f:return {r['box']:r['reading'] for r in csv.DictReader(f,delimiter='\t')}
allout=[]
for f in sorted((root/'second').glob('*_first.tsv')):
 p=f.with_name(f.name.replace('_first.tsv','_second.tsv'))
 if not p.exists():continue
 a,b=load(f),load(p)
 if set(a)!=set(b):raise ValueError(f'Box mismatch {f.name}: missing={set(a)-set(b)}, extra={set(b)-set(a)}')
 out=[]
 for k in a:
  ta,tb=token.findall(a[k]),token.findall(b[k])
  ops=[]
  for op,i,j,u,v in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes():
   if op!='equal':ops.append({'operation':op,'first_range':[i,j],'second_range':[u,v],'first_tokens':ta[i:j],'second_tokens':tb[u:v]})
  out.append({'box':k,'different':bool(ops),'first':a[k],'second':b[k],'token_differences':ops})
 q=f.with_name(f.name.replace('_first.tsv','_comparison.json'))
 q.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 allout.append({'page':f.stem.replace('_first',''),'boxes':len(out),'different':sum(x['different'] for x in out),'comparison':str(q.relative_to(root))})
(root/'second/comparison_summary.json').write_text(json.dumps(allout,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(allout,ensure_ascii=False))
