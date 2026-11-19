from pathlib import Path
import csv,json,re,html
from extract_uncertainties import extract,mask_noncode,closing_brace
OUT=Path(__file__).resolve().parents[1]
rows=[]
def spans(s,kind):
 m=mask_noncode(s);a=[]
 for t in re.finditer(r'\\'+kind+r'\s*\{',m):
  op=m.find('{',t.start());a.append((t.start(),closing_brace(m,op)+1))
 return a
def alternatives(arg):
 out=[];start=0;depth=0;i=0
 while i<len(arg):
  if arg[i]=='\\':
   i+=1
   if i<len(arg) and not arg[i].isalpha():i+=1;continue
   while i<len(arg) and (arg[i].isalpha() or arg[i]=='@'):i+=1
   continue
  if arg[i]=='{':depth+=1
  elif arg[i]=='}':depth-=1
  elif arg[i]=='|' and depth==0:out.append(arg[start:i]);start=i+1
  i+=1
 out.append(arg[start:]);return out
for p in sorted((OUT/'pages').glob('*.tex')):
 s=p.read_text();n=int(re.search(r'scan(\d+)',p.name)[1]);deleted=spans(s,'deleted');margins=spans(s,'margin')
 for o in extract(s,p.name,f'S{n:03}-U'):
  old=any(a<=o.start<b for a,b in deleted);margin=any(a<=o.start<b for a,b in margins)
  confidence='low' if o.macro==r'\illegible' or old or (margin and n in (5,16,17,18,24)) else 'medium'
  parts=alternatives(o.argument)
  rows.append([o.occurrence_id,n,f'{o.line}:{o.column}',parts[0],' | '.join(parts[1:]),confidence,('deleted; ' if old else '')+('margin' if margin else 'main text or display'),o.argument])
cols=['id','scan','tex_line_column','reading','alternatives','confidence','state','exact_argument']
with (OUT/'SP33_CW_156-5_uncertainty_review.tsv').open('w',newline='') as f:w=csv.writer(f,delimiter='\t');w.writerow(cols);w.writerows(rows)
def code(x):return '<code>'+html.escape(str(x)).replace('|','&#124;').replace('\n','</code><br><code>')+'</code>'
lines=['## Complete occurrence-by-occurrence doubt table','','The explanatory table above groups related difficult passages. This table additionally accounts for every uncertainty macro in the final pages, including old writing inside cancellations. Locations are one-based TeX source line:column, not invented manuscript line numbers. Confidence concerns the preferred decipherment: conservatively low for unreadable or cancelled ink and the especially difficult margins, medium for the other retained readings; the adjacent explanatory table gives the passage-specific reasons. A one-reading uncertainty remains uncertain even when no alternative is proposed.','','| ID | Scan | TeX line:column | Preferred reading / illegible count | Alternatives | Confidence | State |','|---|---:|---|---|---|---|---|']
for row in rows:lines.append('| '+' | '.join(code(v) if i in (2,3,4) else str(v) for i,v in enumerate(row[:7]))+' |')
lines+=['',f'Total: {len(rows)} uncertainty occurrences. The exact raw arguments, including all nested ordinary TeX, are also preserved in SP33_CW_156-5_uncertainties.tsv and its rendered appendix.','']
p=OUT/'SP33_CW_156-5_doubts.md';s=p.read_text().split('\n## Complete occurrence-by-occurrence doubt table')[0];p.write_text(s+'\n'+'\n'.join(lines))
print(f'Added {len(rows)} exhaustive doubt rows with location, alternatives, confidence and deletion/margin state.')
