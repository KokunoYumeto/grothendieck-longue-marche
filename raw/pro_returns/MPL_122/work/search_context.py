from pathlib import Path
import re,json,subprocess,collections
p=Path(__file__).resolve().parents[1] / 'MPL_122_notes.md'
root=p.parent.parent
s=p.read_text()
files=['context/README.md','context/notes/RESULTS_STATE.md','context/hua_project/README.md','context/hua_project/122.modern.tex']
records=[]
for match in re.finditer(r'^### (RN\d{3}) — ([^\n]*)\n(.*?)(?=^### |^## |\Z)',s,re.M|re.S):
    note,title,body=match.groups()
    q=re.search(r'\*\*Context search:\*\* (.*?)\. \*\*Comparison:',body,re.S)
    if not q:
        raise ValueError(f'No context query for {note}')
    query=q.group(1).strip()
    result=subprocess.run(['rg','-n','-i','--no-heading','--color','never','--',query,*files],cwd=root,capture_output=True,text=True)
    if result.returncode not in [0,1]:
        raise ValueError((note,result.stderr))
    hits=[]
    for line in result.stdout.splitlines():
        path,num,_=line.split(':',2)
        hits.append({'file':path,'line':int(num)})
    records.append({'note':note,'title':title,'query':query,'hits':hits,'hit_count':len(hits),'counts_by_file':dict(collections.Counter(h['file'] for h in hits))})
assert [r['note'] for r in records]==[f'RN{i:03d}' for i in range(1,70)]
out=p.parent/'work'/'context_searches.json'
out.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Queries executed:',len(records))
for r in records:
    print(r['note'],r['hit_count'],'RS',r['counts_by_file'].get(files[1],0),'Hua',r['counts_by_file'].get(files[3],0))
print('Word count:',len(s.split()))

