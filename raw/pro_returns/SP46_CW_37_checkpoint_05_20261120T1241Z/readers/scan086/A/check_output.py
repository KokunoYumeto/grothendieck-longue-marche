from pathlib import Path
import json,re
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan086/A')
s=(root/'reading.tex').read_text()
r=json.loads((root/'report.json').read_text())
# Ignore comments while checking source balance; this is not a TeX run.
s_clean='\n'.join(line.split('%',1)[0] for line in s.splitlines())
level=0
for n,ch in enumerate(s_clean):
    if ch=='{' and (n==0 or s_clean[n-1]!='\\'):
        level+=1
    elif ch=='}' and (n==0 or s_clean[n-1]!='\\'):
        level-=1
        assert level>=0,('premature close',n)
assert level==0,('brace imbalance',level)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s_clean):
    operation,env=m.groups()
    if operation=='begin': stack.append(env)
    else:
        assert stack and stack.pop()==env,('environment mismatch',env)
assert not stack
assert s_clean.count('$')%2==0
assert s.startswith('\\scanpage{86}\n')
assert '\\cotefile' not in s
assert '\\n' not in s.replace('\\noindent','')
assert r['scan']==86 and r['reader']=='A'
assert len(r['image_views'])==3
assert len(r['crops'])==7
assert all(d['h_reading'] is None and d['diff_h'] is False for d in r['decisions'])
assert sum(d['c_doubt'] for d in r['decisions'])==5
assert all(len(d['bbox'])==4 for d in r['decisions'])
assert all(Path(c['file']).is_file() for c in r['crops'])
assert all(i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} and i['transcribed']=='yes' for i in r['inventory'])
assert r['check_events']==[]
assert s.count('\\begin{tikzpicture}')==2
assert s.count('\\deleted{')==6
result={
 'json_valid':True,'brace_balance':True,'environment_balance':True,'inline_math_balance':True,
 'source_images':3,'crop_views':7,'inventory_rows':len(r['inventory']),'decision_rows':len(r['decisions']),
 'explicit_C_doubts':sum(d['c_doubt'] for d in r['decisions']),
 'C_differences':sum(d['diff_c'] for d in r['decisions']),
 'H_available':False,'all_H_readings_null':True,'typed_corrections':6,'graphic_loci':2,
 'tex_compilation_attempted':False
}
(root/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
