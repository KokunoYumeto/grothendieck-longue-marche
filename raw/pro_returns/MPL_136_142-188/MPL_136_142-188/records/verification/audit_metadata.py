"""Mechanical macro extraction and inventory comparison; no image/context access."""
from pathlib import Path
import csv,re,json,collections
ROOT=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188')
OUT=Path('/workspace/scratch/fce80d805cc4/verification')
MACROS={'unsure','illegible','deleted','inserted','margin','diagram','figure','uline','uuline','mspage','scanpage','cotefile','begin','end'}
MAP={'deleted':'deletion','inserted':'insertion','margin':'margin note','diagram':'diagram','figure':'drawing'}
FOCUS={144,149,153,155,162}

def escaped(s,i):
 j=i-1
 while j>=0 and s[j]=='\\': j-=1
 return (i-j-1)%2==1

def mask_comments(s):
 chars=list(s)
 i=0
 while i<len(s):
  if s[i]=='%' and not escaped(s,i):
   j=s.find('\n',i)
   if j<0:j=len(s)
   chars[i:j]=' '*(j-i)
   i=j
  else:i+=1
 return ''.join(chars)

def argument(s,start):
 p=start
 while p<len(s) and s[p].isspace():p+=1
 if p==len(s) or s[p]!='{':return None
 depth=1;q=p+1
 while q<len(s):
  if not escaped(s,q):
   if s[q]=='{':depth+=1
   elif s[q]=='}':
    depth-=1
    if depth==0:return p,q
  q+=1
 return None

def write_csv(name,rows,fields):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

pages=sorted((ROOT/'pages').glob('*.tex'))
before={p.name:p.stat().st_mtime_ns for p in pages}
occ=[];doubts=[];malformed=[];unwrapped=[];display_counts={}
for p in pages:
 scan=int(re.search(r'scan(\d+)\.tex$',p.name)[1]);raw=p.read_text();s=mask_comments(raw)
 local=[];ordinal=collections.Counter()
 for m in re.finditer(r'\\([A-Za-z@]+|.)',s):
  name=m[1]
  if name not in MACROS:continue
  span=argument(s,m.end());line=s.count('\n',0,m.start())+1
  if span is None:
   malformed.append({'scan':scan,'line':line,'macro':name,'problem':'missing or unbalanced braced argument'})
   continue
  a,b=span;ordinal[name]+=1
  item={'scan':scan,'filename':p.name,'macro':name,'occurrence':ordinal[name],'line':line,
        'end_line':s.count('\n',0,b)+1,'start':m.start(),'arg_start':a,'end':b,
        'argument':raw[a+1:b]}
  local.append(item)
 for item in local:
  containers=[q['macro'] for q in local if q['start']<item['start']<q['end'] and q['macro'] not in {'begin','end'}]
  item['containers']=';'.join(containers)
  if item['macro'] in {'unsure','illegible'}:
   doubts.append({k:item[k] for k in ('scan','filename','macro','occurrence','line','end_line','containers','argument')})
   if item['macro']=='illegible' and not item['argument'].strip().isdigit():
    malformed.append({'scan':scan,'line':item['line'],'macro':'illegible','problem':'argument is not an integer'})
  if item['macro']=='begin':
   env=item['argument'].strip()
   if env=='tikzcd' and 'diagram' not in containers:
    unwrapped.append({'scan':scan,'line':item['line'],'environment':env,'expected_wrapper':'diagram'})
   if env=='tikzpicture' and 'figure' not in containers and 'diagram' not in containers:
    unwrapped.append({'scan':scan,'line':item['line'],'environment':env,'expected_wrapper':'figure'})
  if item['macro'] not in {'begin','end'}:
   occ.append({k:item[k] for k in ('scan','filename','macro','occurrence','line','end_line','containers')})
 display_counts[scan]=sum(1 for m in re.finditer(r'\\([A-Za-z@]+|.)',s) if m[1]=='[')+sum(1 for q in local if q['macro']=='begin' and q['argument'].strip() in {'equation','equation*','align','align*','gather','gather*','multline','multline*','eqnarray','eqnarray*'})

with (ROOT/'MPL_136_142-188_inventory.csv').open(newline='') as f:
 inventory=list(csv.DictReader(f))
inv_counts=collections.Counter((int(r['scan']),r['kind']) for r in inventory)
macro_counts=collections.Counter((r['scan'],r['macro']) for r in occ)
comparison=[]
for scan in sorted(int(re.search(r'scan(\d+)\.tex$',p.name)[1]) for p in pages):
 for macro,kind in MAP.items():
  a=macro_counts[scan,macro];b=inv_counts[scan,kind]
  comparison.append({'scan':scan,'macro':macro,'inventory_kind':kind,'macro_count':a,'inventory_rows':b,'macro_surplus':a-b,'macro_lines':';'.join(str(r['line']) for r in occ if r['scan']==scan and r['macro']==macro)})
comparison.extend({'scan':s,'macro':'display delimiters/environments','inventory_kind':'display','macro_count':n,'inventory_rows':inv_counts[s,'display'],'macro_surplus':n-inv_counts[s,'display'],'macro_lines':''} for s,n in display_counts.items())
write_csv('macro_occurrences.csv',occ,['scan','filename','macro','occurrence','line','end_line','containers'])
write_csv('doubt_macros.csv',doubts,['scan','filename','macro','occurrence','line','end_line','containers','argument'])
write_csv('inventory_macro_comparison.csv',comparison,['scan','macro','inventory_kind','macro_count','inventory_rows','macro_surplus','macro_lines'])
counts=[]
for p in pages:
 scan=int(re.search(r'scan(\d+)\.tex$',p.name)[1])
 counts.append({'scan':scan,'unsure':macro_counts[scan,'unsure'],'illegible':macro_counts[scan,'illegible']})
write_csv('doubt_macro_counts.csv',counts,['scan','unsure','illegible'])
write_csv('malformed_macros.csv',malformed,['scan','line','macro','problem'])
write_csv('unwrapped_diagrams_drawings.csv',unwrapped,['scan','line','environment','expected_wrapper'])
changed=[p.name for p in pages if p.stat().st_mtime_ns!=before[p.name]]
summary={'pages':len(pages),'inventory_rows':len(inventory),'unsure':sum(r['unsure'] for r in counts),'illegible':sum(r['illegible'] for r in counts),'malformed_macros':len(malformed),'unwrapped_environments':len(unwrapped),'changed_during_check':changed,'macro_surplus_items':[r for r in comparison if r['macro_surplus']>0 and r['macro']!='display delimiters/environments'],'macro_deficit_items':[r for r in comparison if r['macro_surplus']<0 and r['macro']!='display delimiters/environments']}
(OUT/'metadata_audit_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
report=['# Mechanical inventory and doubt-macro audit','',f"Pages: {len(pages)}. Inventory rows: {len(inventory)}.",'',f"Doubt occurrences: {summary['unsure']} `unsure`, {summary['illegible']} `illegible`.",'',f"Malformed tracked macros: {len(malformed)}. Unwrapped diagram/drawing environments: {len(unwrapped)}.",'','This report compares syntactic occurrences with inventory kind counts. Physical-element grouping is reserved for the sole visual reader. No images or research context were accessed, and no readings were interpreted.','', '## Positive macro-count differences','', '| Scan | Macro | Macro occurrences | Inventory rows | Difference | Source lines |','|---|---|---:|---:|---:|---|']
for r in summary['macro_surplus_items']:
 report.append(f"| {r['scan']} | `{r['macro']}` | {r['macro_count']} | {r['inventory_rows']} | {r['macro_surplus']} | {r['macro_lines']} |")
report.extend(['','## Focus scans','', '| Scan | Macro | Macro occurrences | Inventory rows | Difference |','|---|---|---:|---:|---:|'])
for r in comparison:
 if r['scan'] in FOCUS and r['macro']!='display delimiters/environments':
  report.append(f"| {r['scan']} | `{r['macro']}` | {r['macro_count']} | {r['inventory_rows']} | {r['macro_surplus']} |")
report.extend(['','## Outputs','','- `doubt_macros.csv`: every doubt occurrence, exact raw argument, source line, and containing wrappers; generated mechanically without printing the readings.','- `doubt_macro_counts.csv`: per-scan counts.','- `macro_occurrences.csv`: tracked editorial macro locations without their textual contents.','- `inventory_macro_comparison.csv`: all scan/kind count comparisons, including displayed-math syntax.','- `malformed_macros.csv` and `unwrapped_diagrams_drawings.csv`: structural exceptions.','',f"Files modified during check: {len(changed)}.",''])
(OUT/'mechanical_inventory_report.md').write_text('\n'.join(report))
print(json.dumps({k:v for k,v in summary.items() if k not in {'macro_surplus_items','macro_deficit_items'}},indent=2))
print('Positive macro-count differences:')
for r in summary['macro_surplus_items']:
 print(f"scan {r['scan']}: {r['macro']} macros={r['macro_count']}, inventory={r['inventory_rows']}, surplus={r['macro_surplus']}, source lines={r['macro_lines']}")
print('Focus scan differences (all directions):')
for r in comparison:
 if r['scan'] in FOCUS and r['macro_surplus'] and r['macro']!='display delimiters/environments':
  print(f"scan {r['scan']}: {r['macro']} macros={r['macro_count']}, inventory={r['inventory_rows']}, difference={r['macro_surplus']}")
