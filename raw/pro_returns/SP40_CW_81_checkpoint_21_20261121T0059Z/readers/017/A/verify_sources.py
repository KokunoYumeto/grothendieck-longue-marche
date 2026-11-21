from pathlib import Path
import json,re
out=Path('/workspace/scratch/94548b74fbe0/out/readers/017/A')
tex=(out/'reading.tex').read_text()
report=json.loads((out/'report.json').read_text())
# Ignore unescaped source comments, then check structural delimiters only.
body='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in tex.splitlines())
stack=[];errors=[]
for i,c in enumerate(body):
 if c not in '{}':continue
 n=0;j=i-1
 while j>=0 and body[j]=='\\':n+=1;j-=1
 if n%2:continue
 if c=='{':stack.append(i)
 elif stack:stack.pop()
 else:errors.append('unmatched closing brace at '+str(i))
if stack:errors.append('unmatched opening braces at '+str(stack))
env=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 op,name=m.groups()
 if op=='begin':env.append(name)
 elif not env or env.pop()!=name:errors.append('environment mismatch '+name)
if env:errors.append('unclosed environments '+str(env))
for disp in re.findall(r'\\\[(.*?)\\\]',tex,re.S):
 if '\n\n' in disp:errors.append('empty line inside display')
if body.count(r'\[')!=body.count(r'\]'):errors.append('display delimiter count mismatch')
paths={x['path'] for x in report['crops']}
for p in paths:
 if not (out/p).is_file():errors.append('missing crop '+p)
for d in report['differences']:
 if d['readers_crop'] and d['readers_crop'] not in paths:errors.append('unknown difference crop '+d['id'])
ids={d['id'] for d in report['differences']}
for row in report['notes']['C_source_row_map']:
 for part,id in row['parts'].items():
  if id not in ids:errors.append('unmapped source part '+row['row']+':'+part)
allowed_custom={'scanpage','uline','deleted','inserted','unsure','figure','margin'}
# Inventory of macros for manual PREAMBLE/standard-command review, not a compiler.
macros=sorted(set(re.findall(r'\\([A-Za-z]+)',body)))
result={'inputs':['reading.tex','report.json','crop_manifest.json'],'checks':'comment-aware brace balance; begin/end nesting; display delimiter counts and empty physical lines; crop existence and references; source-row ID references; macro inventory for manual review','errors':errors,'source_rows':len(report['notes']['C_source_row_map']),'source_parts':sum(len(x['parts']) for x in report['notes']['C_source_row_map']),'differences':len(report['differences']),'draw_path_commands':len(re.findall(r'\\draw\[',body)),'crop_files':len(paths),'macros':macros,'compiler_or_renderer_used':False}
(out/'source_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
