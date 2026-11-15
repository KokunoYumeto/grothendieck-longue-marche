"""Index every nested uncertainty without OCR or language-model reconstruction."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
def braces(s,start):
 assert s[start]=='{'
 depth=1;i=start+1
 while i<len(s):
  if s[i]=='\\':
   m=re.match(r'\\[A-Za-z]+|\\.',s[i:]);i+=len(m.group()) if m else 1;continue
  if s[i]=='{':depth+=1
  if s[i]=='}':
   depth-=1
   if depth==0:return s[start+1:i],i+1
  i+=1
 raise ValueError('Unbalanced brace at '+str(start))
def occurrences(s,names):
 out=[]
 for m in re.finditer(r'\\('+'|'.join(names)+r')\{',s):
  arg,end=braces(s,m.end()-1)
  out.append((m.start(),end,m.group(1),arg,s.count('\n',0,m.start())+1))
 return out
def split_alt(s):
 depth=0;i=0
 while i<len(s):
  if s[i]=='\\':
   m=re.match(r'\\[A-Za-z]+|\\.',s[i:]);i+=len(m.group()) if m else 1;continue
  if s[i]=='{':depth+=1
  elif s[i]=='}':depth-=1
  elif s[i]=='|' and depth==0:return s[:i],s[i+1:]
  i+=1
 return s,''
def cell(s):return '`'+s.replace('\n',' ').replace('|','&#124;').replace('`','&#96;')+'`'
rows=[]
for p in sorted((root/'pages').glob('*.tex')):
 n=int(p.stem[-3:]);s=p.read_text();deletions=occurrences(s,['deleted'])
 for start,end,macro,arg,line in occurrences(s,['unsure','illegible']):
  reading,alt=split_alt(arg)
  in_del=any(a<=start<b for a,b,*_ in deletions)
  conf='low' if in_del or macro=='illegible' else 'medium'
  if n in {60,62,64,66,68,72,86,87,90,94} and not re.search(r'\\|[\^_=]',arg):conf='low'
  if n in {75,77} and 'vartheta' in arg:conf='low'
  if n==50 and line>=32:conf='low'
  if n==80 and 'relative absolue' in arg:conf='low'
  if macro=='illegible':reading=f'physically unreadable: estimated {arg} word(s)';alt='no recoverable reading'
  location=f'TeX l. {line}'+('; deletion' if in_del else '')
  rows.append(f'| 33 | {n:03d} | {location} | {cell(reading)} | {cell(alt) if alt else "—"} | {conf} |')
head=(root/'records/doubts_preface.md').read_text()
tail=(root/'records/doubts_postscript.md').read_text()
(root/'MPL_33_050-097_doubts.md').write_text(head+'\n| File | Scan | Approximate location | Reading | Alternative(s) | Confidence |\n|---|---|---|---|---|---|\n'+'\n'.join(rows)+'\n\n'+tail)
print(len(rows),'uncertainty occurrences indexed')
