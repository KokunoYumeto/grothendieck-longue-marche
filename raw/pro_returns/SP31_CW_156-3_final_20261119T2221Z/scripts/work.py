from pathlib import Path
import re,json,csv,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'out'
W=ROOT/'source/SP31_CW_156-3_witnesses'
MAP={int(r['our_scan']):r for r in csv.DictReader((W/'page_map.tsv').open(),delimiter='\t')}
COLLATION_KINDS={
 'misread word','misread symbol or index','omission','text not on the page',
 'deletion state (struck given live or live given struck)','insertion or placement',
 'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}',
 'drawing or diagram','other',
}
def collation_kind(kind):
 aliases={
  'math glyph or index':'misread symbol or index',
  'deletion state':'deletion state (struck given live or live given struck)',
  r'readable ink left as \\ill{}':r'readable ink left as \ill{}',
 }
 normalized=aliases.get(kind,kind)
 if normalized not in COLLATION_KINDS:raise ValueError(f'Unknown collation kind: {kind!r}')
 return normalized
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def witnesses(n):
 r=MAP[n];c=(W/r['codex_file']).read_text();h=(W/r['hua_file']).read_text();p=int(r['their_page'])
 m=re.search(r'\\page\{'+str(p)+r'\}(.*?)(?=\\page\{|\\end\{document\})',h,re.S)
 return c,m.group(1) if m else ''
def arguments(tex,macro):
 pat='\\'+macro+'{';pos=0
 while True:
  i=tex.find(pat,pos)
  if i<0:return
  j=i+len(pat);start=j;d=1
  while j<len(tex) and d:
   if tex[j]=='{' and (j==0 or tex[j-1]!='\\'):d+=1
   if tex[j]=='}' and (j==0 or tex[j-1]!='\\'):d-=1
   j+=1
  yield i,tex[start:j-1]
  pos=j

def row(place,c,h,final,shows,crop,kind='other',confidence='high',C=True,H=True,marked=False):
 return dict(place=place,c=c,h=h,final=final,shows=shows,crop=crop,kind=kind,confidence=confidence,C=C,H=H,marked=marked)
def save(n,tex,rows,blocks,decisions=None,observations=''):
 r=MAP[n];p=OUT/'pages'/Path(r['codex_file']).name
 if not tex.endswith('\n'):tex+='\n'
 p.write_text(tex)
 rec=dict(scan=n,folder=r['folder'],their_page=r['their_page'],filename=p.name,rows=rows,blocks=blocks,decisions=decisions or [],observations=observations,done=utc())
 (OUT/'records'/f'{n:03}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
 rebuild()
 with (OUT/'progress.log').open('a') as f:f.write(f'scan {n:03} done {utc()}\n')
 print('saved',n,'rows',len(rows),'C',sum(x['C'] for x in rows),'H',sum(x['H'] for x in rows))
def cell(x):return str(x).replace('|','&#124;').replace('\n','<br>')
def inventory_projection(s):
 # Only transparent markup and spacing are removed; symbols/words are not
 # modernised, expanded, substituted, or inferred. Keep source offsets.
 skip=set()
 i=0
 while i<len(s):
  if s[i]=='\\' and i+1<len(s) and not s[i+1].isalpha():i+=2
  elif s[i]=='%':
   end=s.find('\n',i);end=len(s) if end<0 else end
   skip.update(range(i,end));i=end
  else:i+=1
 for m in re.finditer(r'\\(?:uline|uuline|text|textbf|emph|mathrm|mathit|mathsf|mathcal|mathscr|deleted|inserted|margin|unsure|handwritten)\b',s):skip.update(range(m.start(),m.end()))
 chars=[];offsets=[]
 for i,c in enumerate(s):
  if i in skip or c in '{}$':continue
  if c=='\\' and i+1<len(s) and s[i+1] in '{}$':continue
  if c.isspace() or c=='~':
   if chars and chars[-1]!=' ':chars.append(' ');offsets.append(i)
  else:chars.append(c);offsets.append(i)
 if chars and chars[-1]==' ':chars.pop();offsets.pop()
 return ''.join(chars),offsets
def inventory_math_projection(s):
 # Exact common TeX/Unicode encodings only. No spelling, index or prose
 # substitutions are made; this is used solely inside display delimiters.
 base,base_offsets=inventory_projection(s)
 symbols={'in':'∈','notin':'∉','subset':'⊂','subseteq':'⊆','supset':'⊃','supseteq':'⊇',
          'le':'≤','leq':'≤','ge':'≥','geq':'≥','ne':'≠','neq':'≠','cap':'∩','cup':'∪',
          'Rightarrow':'⇒','Leftrightarrow':'⇔','exists':'∃','forall':'∀','infty':'∞',
          'times':'×','cdot':'·','varnothing':'∅','emptyset':'∅','setminus':'∖'}
 subs=dict(zip('₀₁₂₃₄₅₆₇₈₉','0123456789'));chars=[];offsets=[];i=0
 while i<len(base):
  if base[i].isspace():i+=1;continue
  if base[i] in subs:
   chars.append('_');offsets.append(base_offsets[i])
   while i<len(base) and base[i] in subs:chars.append(subs[base[i]]);offsets.append(base_offsets[i]);i+=1
   continue
  command=re.match(r'\\([A-Za-z@]+)',base[i:]) if base[i]=='\\' else None
  if command and command.group(1) in symbols:
   value=symbols[command.group(1)];chars.extend(value);offsets.extend([base_offsets[i]]*len(value));i+=len(command.group(0));continue
  chars.append(base[i]);offsets.append(base_offsets[i]);i+=1
 return ''.join(chars),offsets
def inventory_anchor(tex,row,projected,offsets):
 explicit=re.search(r'\btex line (\d+)\b',row[5])
 if explicit and 'mechanical text match' not in row[5]:
  line=int(explicit.group(1));starts=[0]+[m.end() for m in re.finditer('\n',tex)]
  column=re.search(r'\bcolumn (\d+)\b',row[5]);column=int(column.group(1)) if column else 1
  if 1<=line<=len(starts):return starts[line-1]+column-1,'explicit TeX line/column'
 needle,_=inventory_projection(row[6]);candidates=[(needle,'unique normalized first_words')]
 lead=re.split(r'\.{3}|…',needle)[0].strip()
 if lead!=needle and len(lead)>=12:candidates.append((lead,'unique prefix before ellipsis'))
 for needle,method in candidates:
  if len(needle)<4:continue
  found=[];start=0
  while True:
   p=projected.find(needle,start)
   if p<0:break
   q=p+len(needle)
   if not (needle[0].isalnum() and p and projected[p-1].isalnum()) and not (needle[-1].isalnum() and q<len(projected) and projected[q].isalnum()):found.append(p)
   start=p+1
  if len(found)==1:return offsets[found[0]],method
 if row[4]=='display':
  needle,_=inventory_math_projection(row[6]);matches=[]
  if len(needle)>=3:
   for start,end,_ in display_spans(tex):
    body,body_offsets=inventory_math_projection(tex[start+2:end-2]);p=0
    while True:
     found=body.find(needle,p)
     if found<0:break
     matches.append(start+2+body_offsets[found]);p=found+1
   if len(matches)==1:return matches[0],'unique display token match using exact TeX/Unicode encodings'
 return None,'stored mechanical text anchor no longer matches uniquely' if explicit else 'no unique conservative text anchor'
def display_spans(tex):
 # Lex control symbols so a row break followed by [ is not a display opener.
 spans=[];i=0;start=None
 while i<len(tex):
  if tex[i]=='%':
   end=tex.find('\n',i);i=len(tex) if end<0 else end
  elif tex[i]=='\\':
   if i+1<len(tex) and tex[i+1]=='[':start=i;i+=2
   elif i+1<len(tex) and tex[i+1]==']':
    if start is not None:spans.append((start,i+2,tex[start+2:i]));start=None
    i+=2
   else:
    command=re.match(r'\\[A-Za-z@]+',tex[i:]);i+=len(command.group(0)) if command else 2
  else:i+=1
 return spans
def order_inventory_rows(tex,rows,macro_offsets):
 """Stable partial-order merge; unanchored positions remain unresolved.

 Existing manual-block order and all exact TeX anchors are constraints. No
 image position is inferred. Ambiguous blocks use stable existing order and
 are listed as unresolved in the separate report. Background is non-linear.
 """
 import heapq
 from collections import Counter
 projected,offsets=inventory_projection(tex)
 background=[i for i,r in enumerate(rows) if r[5]=='paper background']
 active=[i for i in range(len(rows)) if i not in background]
 manual=[i for i in active if rows[i][3] not in macro_offsets]
 anchors={};methods={}
 for i in active:
  if rows[i][3] in macro_offsets:anchors[i]=macro_offsets[rows[i][3]];methods[i]='exact macro offset'
  else:anchors[i],methods[i]=inventory_anchor(tex,rows[i],projected,offsets)
 edges={i:set() for i in active};degree={i:0 for i in active}
 def edge(a,b):
  if b not in edges[a]:edges[a].add(b);degree[b]+=1
 for a,b in zip(manual,manual[1:]):edge(a,b)
 anchored=sorted((i for i in active if anchors[i] is not None),key=lambda i:(anchors[i],i))
 for a,b in zip(anchored,anchored[1:]):edge(a,b)
 ready=[i for i in active if not degree[i]];heapq.heapify(ready);ordered=[]
 while ready:
  i=heapq.heappop(ready);ordered.append(i)
  for j in edges[i]:
   degree[j]-=1
   if not degree[j]:heapq.heappush(ready,j)
 conflict=len(ordered)!=len(active)
 if conflict:
  # Do not override a contradiction between declared block order and matched
  # text order. Only macro-to-macro order can safely improve in this case.
  ordered=manual+sorted((i for i in active if i not in manual),key=lambda i:(anchors[i],i))
 ordered+=background
 result=[rows[i] for i in ordered]
 assert Counter(map(tuple,result))==Counter(map(tuple,rows)), 'Inventory row preservation failure'
 report=[]
 for i,r in enumerate(rows):
  p=anchors.get(i)
  status=('non-linear paper background' if i in background else 'anchor/declaration conflict; interleaving withheld' if conflict else 'unresolved relative to macro rows; stable declared order' if p is None else 'TeX-anchored; physical layout not independently inferred')
  report.append([r[0],r[3],tex.count('\n',0,p)+1 if p is not None else '',p if p is not None else '',methods.get(i,'background position'),status])
 return result,report
def rebuild():
 recs=[json.loads(p.read_text()) for p in sorted((OUT/'records').glob('[0-9][0-9][0-9].json'))]
 head=['# SP31_CW_156-3 — changes and decisions','', 'Counts refer to localized reading/state differences, not macro substitutions. A row may differ from both witnesses. Rows retaining a C doubt or recording S are documented separately from differences. Scan coordinates refer to the supplied whole JPEG; enlarged crops are retained in crops/.','', '| Scan | Against C | Against H | C high | C medium | C low | H high | H medium | H low |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
 totals=[0]*8
 for r in recs:
  rs=r['rows'];cs=[sum(x['C'] for x in rs),sum(x['H'] for x in rs)]+[sum(x[w] and x['confidence']==c for x in rs) for w in ['C','H'] for c in ['high','medium','low']]
  head.append('| '+str(r['scan'])+' | '+' | '.join(map(str,cs))+' |');totals=[a+b for a,b in zip(totals,cs)]
 head.append('| **Total** | '+' | '.join(map(str,totals))+' |')
 head+=['','## Consequential corrections','']
 for r in recs:
  for j,x in enumerate(r['rows'],1):
   if x.get('consequential'):head.append(f"- Scan {r['scan']}, {x['place']}: {x['consequential']}")
 sweep_path=OUT/'records/sweep_decisions.md'
 if sweep_path.exists():head+=['',sweep_path.read_text()]
 head+=['','## Page decisions','']
 coll=[];inv=[];doubts=[];inventory_order_report=[];display_inventory_report=[]
 c_ledger={}
 ledger_path=OUT/'audit/source_C_unsure.tsv'
 if ledger_path.exists():
  with ledger_path.open(newline='') as f:
   for entry in csv.DictReader(f,delimiter='\t'):c_ledger.setdefault(int(entry['scan']),[]).append(entry)
 for r in recs:
  n=r['scan'];tex=(OUT/'pages'/r['filename']).read_text()
  head +=[f'### Scan {n:03} (H page {r["their_page"]})','',r['observations'],'','| ID / place | C | H | Consolidated | Ink evidence / crop | Confidence |','|---|---|---|---|---|---|']
  for j,x in enumerate(r['rows'],1):
   xid=f'{n:03}-{j:02}'
   head.append('| '+' | '.join(map(cell,[xid+' '+x['place'],x['c'],x['h'],x['final'],x['shows']+'; crop '+x['crop'],x['confidence']]))+' |')
   if x['H']:coll.append([r['folder'],r['their_page'],n,x['place'],x['h'],x['c'],x['final'],x['shows']+'; crop '+x['crop'],collation_kind(x['kind']),'yes' if x['marked'] else 'no',x['confidence']])
  if r['decisions']:
   head+=['','C doubt decisions (grouped by passage; occurrence ledger in `audit/source_C_unsure.tsv`; every retained ambiguity remains marked):','']
   for d in r['decisions']:head.append('- '+d)
  if c_ledger.get(n):
   head+=['','Source C doubt occurrence ledger (candidate alignment is mechanical; ink dispositions, crop references and reasons are the primary reader\'s entries). These supplementary rows are not added again to the difference counts above.','','| Occurrence / C line | C token | Final line / candidate span | Root ink disposition | Crop reference | Root reason |','|---|---|---|---|---|---|']
   for entry in c_ledger[n]:
    reason=entry.get('reason') or entry.get('review_note') or 'Pending root ink review'
    head.append('| '+' | '.join(map(cell,[entry['occurrence_id']+' / '+entry['source_line'],entry['source_token'],entry['final_line']+' / '+entry['final_aligned_text'],entry.get('ink_disposition') or 'Pending root ink review',entry.get('crop_links') or 'Pending root ink review',reason]))+' |')
  head+=['','Remaining unresolved readings:','']
  for j,(pos,a) in enumerate(arguments(tex,'unsure'),1):
   line=tex.count('\n',0,pos)+1
   local_line=tex.splitlines()[line-1]
   confidence='low' if 'rotatebox' in local_line or len(a)>=30 or ('deleted' in a and n==17) else 'medium'
   doubts.append([n,f'tex line {line}',a.split('|')[0],' | '.join(a.split('|')[1:]) or 'no alternative fixed',confidence])
   head.append(f'- TeX line {line}: `\\unsure{{{a}}}`.')
  for pos,a in arguments(tex,'illegible'):
   line=tex.count('\n',0,pos)+1;doubts.append([n,f'tex line {line}',r'\illegible{'+a+'}','physically unreadable ink; no letters supplied','low'])
   head.append(f'- TeX line {line}: physically unreadable group `\\illegible{{{a}}}`.')
  if not list(arguments(tex,'unsure')) and not list(arguments(tex,'illegible')):head.append('None.')
  page_inv=[];macro_offsets={};projected,projected_offsets=inventory_projection(tex)
  for j,b in enumerate(r['blocks'],1):
   kind,pos,words=b
   item=[n,'text','print' if pos=='paper background' else 'his hand',f'{n:03}-B{j:02}',kind,pos,words,'yes']
   if 'mechanical text match' in pos:
    anchor,_=inventory_anchor(tex,item,projected,projected_offsets)
    if anchor is not None:
     line=tex.count('\n',0,anchor)+1;column=anchor-tex.rfind('\n',0,anchor)
     item[5]=re.sub(r'tex line \d+, column \d+',f'tex line {line}, column {column}',pos)
   page_inv.append(item)
  kinds={'deleted':'deletion','inserted':'insertion','margin':'margin note','diagram':'diagram','figure':'drawing'}
  for m,k in kinds.items():
   for j,(pos,a) in enumerate(arguments(tex,m),1):
    element=f'{n:03}-{m}{j:02}';macro_offsets[element]=pos
    page_inv.append([n,'text','his hand',element,k,f'tex line {tex.count(chr(10),0,pos)+1}',a,'yes'])
  for j,(start,end,body) in enumerate(display_spans(tex),1):
   represented=[]
   for item in page_inv:
    if item[4]!='display':continue
    anchor,_=inventory_anchor(tex,item,projected,projected_offsets)
    if anchor is not None and start<=anchor<end:represented.append(item[3])
   first_line=tex.count('\n',0,start)+1;last_line=tex.count('\n',0,end)+1
   if not represented:
    element=f'{n:03}-display{j:02}';macro_offsets[element]=start
    page_inv.append([n,'text','his hand',element,'display',f'tex lines {first_line}-{last_line}; display delimiters',body.strip(),'yes'])
    represented=[element];status='added from exact TeX display delimiters'
   else:status='covered by existing anchored display block'
   display_inventory_report.append([n,j,first_line,last_line,'; '.join(represented),status])
  ordered,order_report=order_inventory_rows(tex,page_inv,macro_offsets)
  inv.extend(ordered);inventory_order_report.extend(order_report)
 (OUT/'SP31_CW_156-3_changes.md').write_text('\n'.join(head)+'\n')
 with (OUT/'SP31_CW_156-3_collation.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);w.writerows(coll)
 with (OUT/'SP31_CW_156-3_inventory.csv').open('w') as f:
  w=csv.writer(f,lineterminator='\n');w.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);w.writerows(inv)
 with (OUT/'SP31_CW_156-3_inventory_order.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['scan','element','anchor_tex_line','anchor_offset','method','order_status']);w.writerows(inventory_order_report)
 with (OUT/'SP31_CW_156-3_display_inventory.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['scan','display_number','start_tex_line','end_tex_line','inventory_elements','status']);w.writerows(display_inventory_report)
 notation=(OUT/'records/notation.md').read_text() if (OUT/'records/notation.md').exists() else '# Notation and remaining doubts\n\n## Notation table\n\nUnder construction from sequential image reading.\n'
 ds=[notation,'','## Remaining doubts','','| Scan | Place | Reading | Alternatives | Confidence |','|---|---|---|---|---|']
 ds+=['| '+' | '.join(map(cell,d))+' |' for d in doubts]
 ds+=['','## Abbreviations','', (OUT/'records/abbreviations.md').read_text() if (OUT/'records/abbreviations.md').exists() else 'Under construction.','','## Legibility and witnesses','',(OUT/'records/legibility.md').read_text() if (OUT/'records/legibility.md').exists() else 'Legibility assessment pending.']
 (OUT/'SP31_CW_156-3_doubts.md').write_text('\n'.join(ds)+'\n')
 (OUT/'SP31_CW_156-3_transcription.tex').write_bytes(b''.join((OUT/'pages'/r['filename']).read_bytes() for r in recs))
if __name__=='__main__':
 import sys
 if len(sys.argv)>1 and sys.argv[1].isdigit():
  c,h=witnesses(int(sys.argv[1]));print('WITNESS C\n'+c+'\nWITNESS H\n'+h)
 else:rebuild()
