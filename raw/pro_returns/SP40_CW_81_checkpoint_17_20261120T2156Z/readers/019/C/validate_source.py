from pathlib import Path
import json, re

ROOT=Path('/workspace/scratch/94548b74fbe0/out/readers/019/C')
tex=(ROOT/'reading.tex').read_text()
report=json.loads((ROOT/'report.json').read_text())
lines=[]
for line in tex.splitlines():
    line=re.split(r'(?<!\\)%',line,maxsplit=1)[0]
    lines.append(line)
body='\n'.join(lines)

stack=[]
errors=[]
for i,ch in enumerate(body):
    if ch in '{}':
        n=0
        j=i-1
        while j>=0 and body[j]=='\\':
            n+=1;j-=1
        if n%2: continue
        if ch=='{':stack.append(i)
        elif not stack:errors.append('Closing brace without opener at '+str(i))
        else:stack.pop()
if stack:errors.append('Unclosed brace positions '+str(stack))
env=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    if m[1]=='begin':env.append(m[2])
    elif not env or env[-1]!=m[2]:errors.append('Environment mismatch '+m[0])
    else:env.pop()
if env:errors.append('Unclosed environments '+str(env))
for op,cl in [(r'\[',r'\]'),(r'\(',r'\)')]:
    if body.count(op)!=body.count(cl):errors.append('Unbalanced delimiter '+op)
for m in re.finditer(r'\\\[(.*?)\\\]',tex,re.S):
    if re.search(r'\n[ \t]*\n',m[1]):errors.append('Blank physical line inside display')
if body.count('$')%2:errors.append('Odd dollar count')
if r'\cotefile' in body:errors.append('Unexpected cotefile command')
if r'\scanpage{19}' not in body:errors.append('Missing scanpage')
if '% archive sheet number: 18' not in tex:errors.append('Archive comment missing')

allowed={'scanpage','operatorname','unsure','deleted','geq','cap','Sigma','underset','hspace',
         'vcenter','hbox','begin','end','path','fill','draw','text','setminus','mathop','coprod',
         'bigsqcup','limits','alpha','in','overset','cdot','jmath','widehat','quad','left','right',
         'subset','pi','qquad','forall','cup','vphantom','bigcup','not'}
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',body)))
unknown=[x for x in commands if x not in allowed]
if unknown:errors.append('Macro names needing review: '+', '.join(unknown))
for d in report['differences']:
    if d['H'] is None:errors.append('Null H on full-text-witness page: '+d['id'])
    p=d['readers_crop']
    if p and not (ROOT/p).exists():errors.append('Missing crop '+p)
for c in report['crops']:
    if not (ROOT/c['path']).exists():errors.append('Missing manifest file '+c['path'])
    if c['successful_views']!=1:errors.append('Wrong view count '+c['path'])
if len(report['source_C_doubt_rows'])!=12:errors.append('Original C row count differs from 12')
if report['counts']['literal_tikz_components'] != len(re.findall(r'\\(?:draw|fill)\b',body)):
    errors.append('Literal graphical component count mismatch')
required=[r'ens.',r'\unsure{on a}',r'\unsure{avec}',r"\unsure{l'une|l'un}",
          r'\unsure{On a|\deleted{On}On a}',r'\unsure{deuxième|deuxieme|dernier}',
          r'\unsure{à|:} sommer',r'$K_1$ cet ens.',r'\overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0']
for s in required:
    if s not in tex:errors.append('Reading/report anchor absent: '+s)
result={'structural_source_only':True,'compilation':False,'rendering':False,
        'errors':errors,'commands_reviewed':commands,'balanced_braces':not stack,
        'display_pairs':body.count(r'\['),'inline_paren_pairs':body.count(r'\('),
        'literal_graphical_components':len(re.findall(r'\\(?:draw|fill)\b',body)),
        'crop_files_checked':len(report['crops']),'source_rows_checked':12}
(ROOT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
if errors:raise SystemExit(1)
