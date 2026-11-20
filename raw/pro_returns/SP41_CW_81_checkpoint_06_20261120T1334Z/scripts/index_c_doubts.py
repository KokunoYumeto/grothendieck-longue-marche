from pathlib import Path
import re,csv,json
root=Path(__file__).resolve().parents[2];rows=[]
for p in sorted((root/'source/SP41_CW_81_witnesses/codex').glob('*/pages/*.tex')):
 s=p.read_text();n=int(re.search(r'scan(\d+)',p.name).group(1));k=0
 for m in re.finditer(r'\\(unsure|illegible)\{',s):
  i=m.end();j=i;depth=1
  while j<len(s) and depth:
   if s[j]=='{' and (j==0 or s[j-1]!='\\'):depth+=1
   elif s[j]=='}' and (j==0 or s[j-1]!='\\'):depth-=1
   j+=1
  k+=1;rows.append([n,f'C{n:03d}-D{k:03d}',s[:m.start()].count('\n')+1,m.group(1),s[i:j-1]])
p=root/'work/validation/C_doubt_index.tsv'
with p.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['scan','source_doubt_id','source_tex_line','macro','content']);w.writerows(rows)
print(json.dumps({'C_doubt_macros':len(rows),'by_scan':{n:sum(r[0]==n for r in rows) for n in sorted({r[0] for r in rows})}}))
