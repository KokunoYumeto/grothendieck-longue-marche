from pathlib import Path
import csv,re,collections
P=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','answers','notes']
rows=[]
for rel in ['work_A/A_results.csv','work_CE/results.csv','work_DE/results_DE.csv','work_DE/B_separability_results.csv']:
 if not (P/rel).exists():continue
 with (P/rel).open() as f:
  for r in csv.DictReader(f):
   r={k:r.get(k,'') for k in fields}; r['where_proved']=str(Path(rel).parent)+'/'+r['where_proved']; rows.append(r)
banswers={167:'B.4;B.4.a;B.4.b;B.4.c;B.4.h',168:'B.4;B.4.a;B.4.b;B.4.c;B.4.h',1:'B.1;R5',2:'B.1;B.6;Lead4',3:'B.1;B.4;R5',4:'B.2;R6',5:'B.2;R6',6:'B.2;R6',7:'B.2;B.4;R6',8:'B.3.P1',9:'B.3.P2',10:'B.3.P3',11:'B.3.P4',12:'B.3.P4;B.3.P5',13:'B.4.a;Lead5',14:'B.8',15:'B.8',16:'B.3.P7 graded',17:'B.3.P7 full',18:'B.4.b',19:'B.4.a;B.4.b',20:'B.3.P6;B.4.h',21:'B.4.d;B.4.e;Lead6;Lead7',22:'B.4.e;Lead7',23:'B.4.d;Lead6',24:'B.4.d',25:'B.4.d;B.5;B.6',26:'B.4.d',27:'B.4.e;Lead7',28:'B.2;R6;B.4.c',35:'B.4.c',36:'B.1;R5',37:'B.5',38:'B.5',39:'B.6;Lead4',40:'B.4.h',41:'B.7',53:'B.3.P4;B.4.g',55:'B.3.P5;B.4.h'}
for p in sorted([*(P/'sections').glob('a_*.tex'), *(P/'sections').glob('b_*.tex')]):
 s=p.read_text()
 matches=list(re.finditer(r'\\statement\{([AB]\.(\d+))\}\{([^}]+)\}\{',s))
 for index,m in enumerate(matches):
  start=m.end(); depth=1;j=start
  while j<len(s) and depth:
   depth+=(s[j]=='{')-(s[j]=='}');j+=1
  title=s[start:j-1]
  end=matches[index+1].start() if index+1<len(matches) else len(s)
  block=s[j:end]
  claim=block.split('\\begin{proof}',1)[0].strip()
  claim=re.split(r'\\subsection\*?\{',claim)[0].strip()
  full_statement=re.sub(r'\s+',' ',title+' '+claim)
  references=set(re.findall(r'\b(?:[A-E]\.\d+|R[1-9])\b',block))-{m[1]}
  citations=[]
  for cited in re.findall(r'\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]+)\}',block):
   citations.extend(cited.split(','))
  deps='; '.join(sorted(references)+sorted(set(citations)))
  rows.append(dict(id=m[1],statement=full_statement,status=m[3],where_proved=str(p.relative_to(P))+'; '+m[1],depends_on=deps,answers=(banswers.get(int(m[2]),'B.4') if m[1].startswith('B.') else ('A.6;A.7;A.8' if int(m[2]) in {105,109,110,111,112,113,117,119} else ('A.4;A.5;A.7;A.8' if int(m[2]) in {106,107,108,114,115,116,118} else 'A.7;A.8'))),notes='The complete scoped statement is included in this field; LaTeX formulas retain the paper notation.'))
# Normalize every register claim and proof location against the actual paper source.
# This also prevents component-relative prefixes from being duplicated on merge.
claim_sources={}
paper_sources=set()
def visit_source(path):
 path=path.resolve()
 if path in paper_sources:return
 assert path.exists(),('Missing paper source',path)
 paper_sources.add(path)
 for rel in re.findall(r'\\(?:input|InputIfFileExists)\{([^}]+)\}',path.read_text()):
  child=P/rel
  if not child.suffix:child=child.with_suffix('.tex')
  if child.exists():visit_source(child)
visit_source(P/'LM4_SUCCESSOR_paper.tex')
for path in sorted(paper_sources):
 content=path.read_text()
 ms=list(re.finditer(r'\\statement\{([A-E]\.\d+)\}\{(Proved|Refuted|Known|Open)\}\{',content))
 for ix,m in enumerate(ms):
  start=m.end();depth=1;j=start
  while j<len(content) and depth:
   depth+=(content[j]=='{')-(content[j]=='}');j+=1
  title=content[start:j-1]
  end=ms[ix+1].start() if ix+1<len(ms) else len(content)
  block=content[j:end]
  claim=block.split('\\begin{proof}',1)[0].strip()
  claim=re.split(r'\\(?:sub)*section\*?\{',claim)[0].strip()
  full=re.sub(r'\s+',' ',title+' '+claim)
  assert m[1] not in claim_sources,('Duplicate paper statement',m[1],path)
  claim_sources[m[1]]=(str(path.relative_to(P)),m[2],full)
for row in rows:
 source,status,full=claim_sources[row['id']]
 assert row['status']==status,('Status mismatch',row['id'])
 row['statement']=full
 row['where_proved']=source+'; '+row['id']
assert set(claim_sources)=={r['id'] for r in rows},('Paper/register IDs differ',set(claim_sources)^{r['id'] for r in rows})

ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids)),[k for k,v in collections.Counter(ids).items() if v>1]
rows.sort(key=lambda r:(r['id'][0],int(r['id'].split('.')[1])))
with (P/'LM4_SUCCESSOR_results.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
parts=['sections/b_sources.bib','sections/a_central_sources.bib','work_A/A_references.bib','work_CE/CE_references.bib','work_DE/references_DE.bib','work_DE/B_separability_references.bib']
entries=[]; seen={}
for rel in parts:
 if not (P/rel).exists():continue
 s=(P/rel).read_text()
 for m in re.finditer(r'(?m)^@\w+\s*\{\s*([^,]+),',s):
  j=m.end();depth=1
  while j<len(s) and depth:
   if s[j]=='{' and (j==0 or s[j-1]!='\\'):depth+=1
   if s[j]=='}' and (j==0 or s[j-1]!='\\'):depth-=1
   j+=1
  entry=s[m.start():j]
  if m[1] in seen:
   assert seen[m[1]]==entry,('Conflicting bibliography key',m[1])
  else: entries.append(entry);seen[m[1]]=entry
(P/'LM4_SUCCESSOR_references.bib').write_text('% Primary records opened and verified as stated in each note; see source logs.\n\n'+'\n\n'.join(entries)+'\n')
print('RESULT_ROWS',len(rows),dict(collections.Counter(r['status'] for r in rows)))
print('BIBLIOGRAPHY_ENTRIES',len(entries))
