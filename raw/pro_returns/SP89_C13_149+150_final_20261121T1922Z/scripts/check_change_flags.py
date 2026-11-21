"""Flag obvious record inconsistencies for manual review; never decide ink."""
from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[1]
def preferred(s):
 out='';i=0
 while i<len(s):
  if s.startswith('\\unsure{',i):
   j=i+8;depth=1;k=j
   while k<len(s) and depth:
    if s[k]=='{' and (k==0 or s[k-1]!='\\'):depth+=1
    elif s[k]=='}' and (k==0 or s[k-1]!='\\'):depth-=1
    k+=1
   body=s[j:k-1];d=0;cut=len(body)
   for z,ch in enumerate(body):
    if ch=='{':d+=1
    elif ch=='}':d-=1
    elif ch=='|' and d==0:cut=z;break
   head=body[:cut]
   out+=preferred(head) if head else '<PRESENT_UNREADABLE>'
   i=k
  else:out+=s[i];i+=1
 return out
flags=[]
for p in sorted((W/'reports').glob('*/report.json')):
 r=json.loads(p.read_text())
 for c in r['changes']:
  issues=[]
  if not c['against_c'] and not c['against_h']:issues.append('Neither witness differs')
  for witness,key in [('c','against_c'),('h','against_h')]:
   if c[key] and re.sub(r'\s+',' ',c[witness]).strip()==re.sub(r'\s+',' ',c['final']).strip():
    issues.append('Exact '+witness.upper()+' reading equals final')
  if c['against_c'] and '\\unsure' not in c['c'] and '\\unsure' in c['final'] and re.sub(r'\s+','',preferred(c['final']))==re.sub(r'\s+','',c['c']):
   issues.append('Only new uncertainty relative to C preferred reading')
  if issues:flags.append(dict(page=r['page'],id=c['id'],issues=issues))
print(json.dumps(flags,ensure_ascii=False,indent=2))
