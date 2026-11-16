from pathlib import Path
import csv,re,collections
P=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','answers','notes']
rows=[]
for rel in ['work_A/A_results.csv','work_CE/results.csv','work_DE/results_DE.csv']:
 with (P/rel).open() as f:
  for r in csv.DictReader(f):
   r={k:r.get(k,'') for k in fields}; r['where_proved']=str(Path(rel).parent)+'/'+r['where_proved']; rows.append(r)
banswers={1:'B.1;R5',2:'B.1;B.6;Lead4',3:'B.1;B.4;R5',4:'B.2;R6',5:'B.2;R6',6:'B.2;R6',7:'B.2;B.4;R6',8:'B.3.P1',9:'B.3.P2',10:'B.3.P3',11:'B.3.P4',12:'B.3.P4;B.3.P5',13:'B.4.a;Lead5',14:'B.8',15:'B.8',16:'B.3.P7 graded',17:'B.3.P7 full',18:'B.4.b',19:'B.4.a;B.4.b',20:'B.3.P6;B.4.h',21:'B.4.d;B.4.e;Lead6;Lead7',22:'B.4.e;Lead7',23:'B.4.d;Lead6',24:'B.4.d',25:'B.4.d;B.5;B.6',26:'B.4.d',27:'B.4.e;Lead7'}
for p in sorted((P/'sections').glob('b_*.tex')):
 for m in re.finditer(r'\\statement\{(B\.(\d+))\}\{([^}]+)\}\{',p.read_text()):
  start=m.end(); depth=1;j=start
  s=p.read_text()
  while j<len(s) and depth:
   depth+=(s[j]=='{')-(s[j]=='}');j+=1
  title=s[start:j-1]
  rows.append(dict(id=m[1],statement=title,status=m[3],where_proved=str(p.relative_to(P))+'; '+m[1],depends_on='See complete proof and typed hypotheses in paper',answers=banswers.get(int(m[2]),'B.4'),notes='Exact scope is the complete statement, including conditional hypotheses; title is an index.'))
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids)),[k for k,v in collections.Counter(ids).items() if v>1]
rows.sort(key=lambda r:(r['id'][0],int(r['id'].split('.')[1])))
with (P/'LM4_SUCCESSOR_results.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
parts=['sections/b_sources.bib','work_A/A_references.bib','work_CE/CE_references.bib','work_DE/references_DE.bib']
entries=[]; seen={}
for rel in parts:
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
