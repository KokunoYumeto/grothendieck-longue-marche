from pathlib import Path
import json,re,hashlib
OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/022/A')
tex=(OUT/'reading.tex').read_text()
r=json.loads((OUT/'report.json').read_text())
g=json.loads((OUT/'graphical_audit.json').read_text())
s=json.loads((OUT/'source_audit.json').read_text())
errors=[];checks=[]
# Remove only unescaped comments, preserving newlines.
def clean_line(line):
 for i,ch in enumerate(line):
  if ch=='%':
   n=0;j=i-1
   while j>=0 and line[j]=='\\':n+=1;j-=1
   if n%2==0:return line[:i]
 return line
clean='\n'.join(clean_line(x) for x in tex.splitlines())
# Explicit brace syntax, skipping escaped literal braces.
stack=[]
for i,ch in enumerate(clean):
 if ch not in '{}':continue
 n=0;j=i-1
 while j>=0 and clean[j]=='\\':n+=1;j-=1
 if n%2:continue
 if ch=='{':stack.append(i)
 elif not stack:errors.append('extra closing brace at '+str(i))
 else:stack.pop()
if stack:errors.append('unclosed braces '+str(stack))
checks.append({'check':'unescaped braces','result':'pass' if not stack and not any('brace' in x for x in errors) else 'fail'})
env=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 action,name=m.groups()
 if action=='begin':env.append(name)
 elif not env or env.pop()!=name:errors.append('environment mismatch '+name)
if env:errors.append('unclosed environments '+str(env))
checks.append({'check':'environment nesting','result':'pass' if not env and not any('environment' in x for x in errors) else 'fail'})
# Display delimiters and forbidden paragraph tokens.
display=False;display_count=0
for n,line in enumerate(clean.splitlines(),1):
 if r'\[' in line:
  if display:errors.append('nested display at '+str(n))
  display=True;display_count+=1
 if display and not line.strip():errors.append('blank physical line within display at '+str(n))
 if r'\]' in line:
  if not display:errors.append('unmatched closing display at '+str(n))
  display=False
if display:errors.append('unclosed display')
checks.append({'check':'display delimiters and no blank physical lines inside displays','display_count':display_count,'result':'pass' if not any('display' in x for x in errors) else 'fail'})
math_dollars=len(re.findall(r'(?<!\\)\$',clean))
if math_dollars%2:errors.append('odd inline dollar count')
checks.append({'check':'inline math dollar parity','count':math_dollars,'result':'pass' if math_dollars%2==0 else 'fail'})
allowed={'scanpage','figure','begin','end','path','node','resizebox','rlap','phantom','deleted','inserted','unsure','operatorname','alpha','beta','in','bigcap','bigcup','Sigma','widehat','overline','cap','cup','varnothing','ne','subset','setminus','Rightarrow','draw','fill'}
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',clean)))
unknown=sorted(set(commands)-allowed)
if unknown:errors.append('unreviewed commands '+str(unknown))
checks.append({'check':'command-name allowlist against standard LaTeX/TikZ/preamble use','commands':commands,'unknown':unknown,'result':'pass' if not unknown else 'fail'})
if re.search(r'(?<!\\)\b(?:overset|underset|widehat|overline)\{',clean):errors.append('bare command-name token')
checks.append({'check':'no bare overset/underset/widehat/overline token','result':'pass' if not any('bare' in x for x in errors) else 'fail'})
if re.search(r'\\(?:newcommand|renewcommand|def)\b',clean):errors.append('macro definition in reading')
checks.append({'check':'no macro definitions','result':'pass' if not any('definition' in x for x in errors) else 'fail'})
# Every report reference resolves to the chosen source body or named final prose/display.
valid={x['id'] for x in g['groups']}|{x['id'] for x in g['labels']}|{'final prose outside figure','final display outside figure','% archive sheet number: 21'}
for v in r['differences']:
 for ref in v['source_groups']:
  if ref not in valid:errors.append('bad difference reference '+v['id']+':'+ref)
 if v['readers_crop'] and not (OUT/v['readers_crop']).is_file():errors.append('missing crop '+v['readers_crop'])
for v in r['doubts']:
 if v['crop'] and not (OUT/v['crop']).is_file():errors.append('missing doubt crop '+v['crop'])
for v in g['groups']:
 a=v['source_start_byte_utf8'];b=v['source_end_byte_utf8']
 if tex.encode()[a:b].decode()!=v['complete_source_excerpt']:errors.append('source span mismatch '+v['id'])
checks.append({'check':'report/crop/source-group/source-byte-span references','result':'pass' if not any(('reference' in x or 'crop' in x or 'span' in x) for x in errors) else 'fail'})
for v in g['labels']:
 if v['visible_tex'] not in tex:errors.append('missing visible label '+v['id'])
checks.append({'check':'all 67 recorded visible labels occur in reading source','result':'pass' if not any('label' in x for x in errors) else 'fail'})
required={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for v in r['differences']:
 if v['kind'] not in required:errors.append('bad kind '+v['kind'])
checks.append({'check':'required collation-kind vocabulary','result':'pass' if not any('kind' in x for x in errors) else 'fail'})
if len(r['C_doubt_source_map'])!=7:errors.append('source doubt row count')
if sum(v['return_status']=='resolved' for v in r['C_doubt_source_map'])!=1:errors.append('doubt resolution count')
if sum(v['return_status']=='retained' for v in r['C_doubt_source_map'])!=6:errors.append('doubt retention count')
checks.append({'check':'seven actual C rows: one resolved, six retained','result':'pass' if not any('doubt' in x for x in errors) else 'fail'})
if [x['id'] for x in r['differences'] if x['marked_in_H']]!=['A022-D20','A022-D21']:errors.append('H marker scope')
checks.append({'check':'actual H doubt markers only at the two ill loci','result':'pass' if not any('marker' in x for x in errors) else 'fail'})
checks.append({'check':'drawing command ownership','draw':s['literal_draw_command_count'],'fill':s['literal_fill_command_count'],'result':'pass' if all(v['owner'] for v in s['all_literal_paths']) else 'fail'})
if not all(v['owner'] for v in s['all_literal_paths']):errors.append('unowned literal path')
# Reading/report agreements that are at risk after the local edits.
for fragment in [r'\unsure{On|Un}',r'proc\unsure{è|é|e}de',r'\unsure{etant|étant} \unsure{disjoints|disjointes}',r'\unsure{formule|relation}',r'\deleted{\unsure{Y|Z|X}}',r'ferm\unsure{é|è|e}es','alors que','peut','considérer','dans lequel','ce qui est immédiat']:
 if fragment not in tex:errors.append('missing selected reading '+fragment)
if 'ce qui est immédiat.' in tex:errors.append('unwanted terminal period')
if r'\scanpage{22}' not in tex or '% archive sheet number: 21' not in tex:errors.append('page/archive marker')
checks.append({'check':'selected wording, alternatives, punctuation and page/archive comments','result':'pass' if not any(('selected reading' in x or 'period' in x or 'page/archive' in x) for x in errors) else 'fail'})
result={'source_sha256':hashlib.sha256(tex.encode()).hexdigest(),'source_only':True,'compilation_or_render_performed':False,'mathematical_check':False,'checks':checks,'errors':errors,'passed':not errors}
(OUT/'structural_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':not errors,'checks':len(checks),'errors':errors,'source_sha256':result['source_sha256']},ensure_ascii=False))
