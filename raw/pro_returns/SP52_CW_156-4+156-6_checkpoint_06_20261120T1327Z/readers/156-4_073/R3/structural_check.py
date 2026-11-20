from pathlib import Path
import json,re
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R3')
pkt=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_073')
s=(root/'reading.tex').read_text()
r=json.loads((root/'report.json').read_text())
clean='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())
brace_stack=[]; errors=[]
for i,ch in enumerate(clean):
    if ch in '{}':
        n=0;j=i-1
        while j>=0 and clean[j]=='\\': n+=1;j-=1
        if n%2: continue
        if ch=='{': brace_stack.append(i)
        elif brace_stack: brace_stack.pop()
        else: errors.append('Unmatched closing brace')
if brace_stack: errors.append('Unclosed braces')
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    action,name=m.groups()
    if action=='begin': envs.append(name)
    elif not envs or envs.pop()!=name: errors.append('Environment mismatch: '+name)
if envs: errors.append('Unclosed environments: '+str(envs))
if len(re.findall(r'(?<!\\)\$',clean))%2: errors.append('Odd dollar count')
if clean.count(r'\[')!=2 or clean.count(r'\]')!=2: errors.append('Expected exactly two display pairs')
if r'\cotefile' in s: errors.append('Unexpected cote marker')
if re.search(r'\\(?:newcommand|renewcommand|def)\b',s): errors.append('Unexpected macro definition')
if r'\illegible' in s: errors.append('Unexpected illegible placeholder')
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for d in r['differences']:
    if d['kind'] not in allowed_kinds: errors.append('Bad kind '+d['id']+': '+repr(d['kind']))
    for field in ('change_c','change_h','math_consequential'):
        if type(d[field]) is not bool: errors.append('Nonboolean '+d['id']+' '+field)
    if d['marked_in_h'] not in ('yes','no'): errors.append('Bad marked_in_h '+d['id'])
    if d['crop'] and not Path(d['crop']).exists(): errors.append('Missing crop '+d['id'])
    if not Path(d['bbox_image']).exists(): errors.append('Missing bbox source '+d['id'])
for row in r['inventory']:
    if row['kind'] not in {'text','display','diagram','drawing','margin note','insertion','deletion'}: errors.append('Bad inventory kind')
    if row['sheet_kind']!='text': errors.append('Unexpected sheet kind')
    if row['transcribed']!='yes': errors.append('Untranscribed inventory row')
for x in r['literal_witness_snippet_checks']:
    if not x['literal_snippet_present']: errors.append('Bad literal witness scope '+x['id'])
for ref in r['figure_references']:
    if ref not in s: errors.append('Missing named figure '+ref)
# Count balanced C unsure occurrences, including nested wrappers.
c=(pkt/'C.tex').read_text()
count=len(re.findall(r'\\unsure\{',c))
if count!=len(r['c_doubts']): errors.append(f'C unsure count {count} differs from dispositions {len(r["c_doubts"])}')
result={'status':'pass' if not errors else 'fail','errors':errors,'C_unsure_count':count,'c_doubt_dispositions':len(r['c_doubts']),'differences':len(r['differences']),'remaining_doubts':len(r['remaining_doubts']),'crops':len(r['crops']),'checks':['Balanced braces','Nested environments','Paired math delimiters and two displays','No new macros/cote/illegible','Report field enums/booleans and existing source/crop paths','Literal C/H source snippets','Named final figures','One disposition per C unsure'],'not_performed':['LaTeX compilation','OCR','Mathematical validation']}
(root/'structural_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
