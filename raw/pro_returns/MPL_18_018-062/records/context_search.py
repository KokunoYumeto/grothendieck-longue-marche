"""Record research-only regex searches in the supplied text context (no OCR)."""
from pathlib import Path
import re,json,sys
root=Path(__file__).resolve().parents[2]
paths=[p for p in (root/'context').rglob('*') if p.suffix in {'.md','.tex'}]
def search(item,pattern):
 out=[]
 for p in paths:
  cote=scan='';section=''
  for n,line in enumerate(p.read_text().splitlines(),1):
   m=re.search(r'\\cotefile\{(\d+)\}',line)
   if m:cote=m[1]
   m=re.search(r'\\scanpage\{(\d+)\}',line)
   if m:scan=m[1]
   if line.startswith('#'):section=line
   if re.search(pattern,line,re.I):out.append(dict(file=str(p.relative_to(root/'context')),line=n,cote=cote,scan=scan,section=section,text=line))
 data=dict(item=item,pattern=pattern,matches=out)
 dest=root/'MPL_18_018-062_work/records/context_searches.jsonl'
 with dest.open('a') as f:f.write(json.dumps(data,ensure_ascii=False)+'\n')
 return out
if __name__=='__main__':
 for x in search(sys.argv[1],sys.argv[2]): print(json.dumps(x,ensure_ascii=False))
