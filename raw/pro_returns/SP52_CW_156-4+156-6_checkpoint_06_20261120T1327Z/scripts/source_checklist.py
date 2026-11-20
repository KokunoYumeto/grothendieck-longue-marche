"""Index only the current packet's draft uncertainties; no image/OCR or reading decision."""
from pathlib import Path
import re,sys
O=Path(__file__).resolve().parents[1];K=sys.argv[1];P=O.parent/'page_packets'/K
C=(P/'C.tex').read_text();H=(P/'H.tex').read_text()
def esc(s):return s.replace('|','\\|').replace('\n','<br>')
def balanced(s,a):
 i=s.index('{',a)+1;d=1
 while d:
  if s[i] in '{}':
   j=i-1;n=0
   while j>=0 and s[j]=='\\':n+=1;j-=1
   if not n%2:d+=1 if s[i]=='{' else -1
  i+=1
 return i
out=[f'# Source checklist — {K}\n','This is an index of draft-witness uncertainty, not an ink decision. Every item awaits the independent readers and crop adjudication.\n','## C explicit unsure occurrences\n','| Number | Exact macro | Immediate source context |','| --- | --- | --- |']
for n,m in enumerate(re.finditer(r'\\unsure\{',C),1):
 e=balanced(C,m.start());out.append(f'| {n} | {esc(C[m.start():e])} | {esc(C[max(0,m.start()-65):min(len(C),e+65)])} |')
out+=['\n## H unreadable placeholders\n','| Number | Exact source context |','| --- | --- |']
for n,m in enumerate(re.finditer(r'\\ill\{\}',H),1):out.append(f'| {n} | {esc(H[max(0,m.start()-85):min(len(H),m.end()+85)])} |')
out+=['\nH editorial-note placeholders remain editorial observations; they must not be invented as manuscript words. Repeated placeholders require physical alignment. Read the exact packet for final quotation scope.\n']
(O/'decisions'/f'{K}_source_checklist.md').write_text('\n'.join(out))
print({'C_unsure':C.count('\\unsure{'),'H_ill':H.count('\\ill{'),'checklist':f'decisions/{K}_source_checklist.md'})
