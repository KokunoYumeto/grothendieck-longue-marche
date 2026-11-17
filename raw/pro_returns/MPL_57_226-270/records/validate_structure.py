from pathlib import Path
import sys,re,csv,json,collections
sys.path.insert(0,str(Path(__file__).parent))
from workflow import BASE,EXPECTED,now,log
pages=sorted((BASE/'pages').glob('*.tex'))
errors=[]
if [int(p.stem[-3:]) for p in pages]!=EXPECTED:errors.append('Page set/order mismatch')
pglog=(BASE/'progress.log').read_text()
for n in EXPECTED:
 if not re.search(rf'^57 scan {n} done ',pglog,re.M):errors.append(f'{n}: missing done timestamp')
 if not re.search(rf'^scan {n} audited ',pglog,re.M):errors.append(f'{n}: missing audit timestamp')
for p in pages:
 t=p.read_text();scan=int(p.stem[-3:]);stack=[];i=0;dollars=0
 while i<len(t):
  c=t[i]
  if c=='%':
   j=t.find('\n',i);i=len(t) if j<0 else j+1;continue
  if c=='\\':
   if i+1<len(t) and t[i+1] in '{}$%\\':i+=2;continue
  elif c=='{':stack.append(i)
  elif c=='}':
   if not stack:errors.append(f'{scan}: extra closing brace at {i}')
   else:stack.pop()
  elif c=='$':dollars+=1
  i+=1
 if stack:errors.append(f'{scan}: {len(stack)} unclosed braces')
 if dollars%2:errors.append(f'{scan}: odd math delimiters')
 a=collections.Counter(re.findall(r'\\begin\{([^}]+)\}',t));b=collections.Counter(re.findall(r'\\end\{([^}]+)\}',t))
 if a!=b:errors.append(f'{scan}: environment mismatch')
 if re.findall(r'\\scanpage\{(\d+)\}',t)!=[str(scan)]:errors.append(f'{scan}: scan marker mismatch')
 if any(x in t for x in [r'\documentclass',r'\usepackage',r'\includegraphics']):errors.append(f'{scan}: prohibited preamble/image')
combined=(BASE/'MPL_57_226-270_transcription.tex').read_text()
if combined!='\n'.join(p.read_text() for p in pages):errors.append('Combined fragment mismatch')
if not combined.startswith('\\cotefile{57}\n\\scanpage{226}'):errors.append('Opening markers mismatch')
rows=list(csv.DictReader((BASE/'MPL_57_226-270_inventory.csv').open()))
if sorted(set(int(r['scan']) for r in rows))!=EXPECTED:errors.append('Inventory scan set mismatch')
if len(set(r['element'] for r in rows))!=len(rows):errors.append('Duplicate inventory identifiers')
valid={'text','display','diagram','drawing','margin note','insertion','deletion'}
if any(r['kind'] not in valid or r['transcribed']!='yes' for r in rows):errors.append('Unfinished/invalid inventory rows')
summary={'validated_utc':now(),'scans':len(pages),'source_images':129,'inventory_elements':len(rows),'inventory_kind_counts':dict(collections.Counter(r['kind'] for r in rows)),'sheet_counts':dict(collections.Counter(next(r['sheet_kind'] for r in rows if r['scan']==str(n)) for n in EXPECTED)),'uncertainty_macro_occurrences':combined.count('\\unsure{'),'physically_obscured_word_estimates':[int(x) for x in re.findall(r'\\illegible\{(\d+)\}',combined)],'checks':['expected 43 scans in order; 232 and 247 excluded','done and second-audit timestamps for every scan','balanced braces, paired environments, even math delimiters','combined fragment identical to ordered page files','no preamble or included images','unique inventory rows, valid element types, all transcribed=yes'],'compile_status':'Not run successfully: xelatex.fmt and tikz-cd.sty unavailable. Structural validation is not a compilation claim.','errors':errors}
(BASE/'records/structural_validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
log(f'structural validation passed: 43 scans, {len(rows)} inventory elements, braces/environments/order complete; TeX build unavailable (missing format/package) {now()}')
