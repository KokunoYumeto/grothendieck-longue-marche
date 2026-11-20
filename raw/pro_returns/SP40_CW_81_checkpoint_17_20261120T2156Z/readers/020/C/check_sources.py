from pathlib import Path
import json,re
from datetime import datetime,timezone

out=Path('/workspace/scratch/94548b74fbe0/out/readers/020/C')
raw=(out/'reading.tex').read_text()
tex='\n'.join(re.sub(r'(?<!\\)%.*','',line) for line in raw.splitlines())
report=json.loads((out/'report.json').read_text())
issues=[]
stack=[]
for n,ch in enumerate(tex):
    if ch in '{}':
        backslashes=0
        k=n-1
        while k>=0 and tex[k]=='\\':backslashes+=1;k-=1
        if backslashes%2:continue
        if ch=='{':stack.append(n)
        elif stack:stack.pop()
        else:issues.append(f'unmatched closing brace at character {n}')
if stack:issues.append(f'{len(stack)} unmatched opening braces')
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',tex):
    action,name=m.groups()
    if action=='begin':envs.append(name)
    elif not envs or envs.pop()!=name:issues.append(f'environment mismatch {name}')
if envs:issues.append(f'unclosed environments {envs}')
if tex.count(r'\[')!=tex.count(r'\]'):issues.append('display delimiter count mismatch')
for m in re.finditer(r'\\\[(.*?)\\\]',tex,re.S):
    if re.search(r'\n[ \t]*\n',m.group(1)):issues.append('empty line inside display')
dollars=len(re.findall(r'(?<!\\)\$',tex))
if dollars%2:issues.append('odd number of inline math dollar delimiters')
if r'\cotefile' in tex:issues.append('unexpected cotefile command')
if tex.count(r'\scanpage{20}')!=1:issues.append('scanpage count differs from one')
if '% archive sheet number: 19' not in raw:issues.append('archive-number comment missing')
known=set('scanpage Pi unsure circ deleted Sigma cap ne varnothing overline quad operatorname uline figure begin end path node setminus draw alpha in cup widehat inserted rlap phantom margin makebox linewidth rotatebox shortstack reversemarginpar normalmarginpar forall pi beta Longleftrightarrow Rightarrow rightarrow fontsize selectfont'.split())
macros=sorted(set(re.findall(r'(?<!\\)\\([A-Za-z]+)',tex)))
unknown=sorted(set(macros)-known)
if unknown:issues.append('unrecognized commands '+','.join(unknown))
valid_kinds={'misread word','misread symbol or index','omission','text not on the page',
 'deletion state (struck given live or live given struck)','insertion or placement',
 'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for d in report['differences']:
    if d['kind'] not in valid_kinds:issues.append('invalid kind '+d['id'])
    if d['readers_crop'] and not (out/d['readers_crop']).is_file():issues.append('missing difference crop '+d['id'])
for d in report['doubts']:
    if not (out/d['crop']).is_file():issues.append('missing doubt crop '+d['location'])
for c in report['crops']:
    if not (out/c['path']).is_file():issues.append('missing crop '+c['path'])
source_map=report['notes']['C_source_doubt_map']
if [s['id'] for s in source_map]!=[f'C-R{i:02}' for i in range(1,12)]:issues.append('original doubt-row identity mismatch')
if sum(len(s['local_decisions']) for s in source_map)!=13:issues.append('local doubt decision count mismatch')
checks={
 'opening_ring_qualification':r'\Pi_I^{\unsure{\circ|0}}' in tex,
 'recurring_unwrapped_rings':tex.count(r'\Pi_J^\circ')==1 and tex.count(r'\Pi_I^\circ')==1,
 'word_and_definite_point':r'\unsure{deux|clas}. parmi' in tex,
 'cancelled_sigma_j_i':r'\deleted{\Sigma_{\unsure{j|i}}}' in tex,
 'resolved_sait':r'On sait donc' in tex,
 'all_abbreviation_accent_alternatives':r'\unsure{dèm.|dém.|dem.}' in tex,
 'all_union_index_states':r'\unsure{\deleted{I}K|K}' in tex,
 'all_membership_states':r'\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}' in tex,
 'non_vide_visible_plus_phantom':r'\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}' in tex,
 'six_literal_paths':len(re.findall(r'\\draw\[',tex))==6,
 'two_graphic_rectangles':tex.count('use as bounding box')==2,
 'no_generic_visible_union_or_brace':r'\bigcup' not in tex and r'\overbrace' not in tex,
 'two_long_closure_rules':tex.count(r'\overline{')==2,
 'three_hat_occurrences':tex.count(r'\widehat{')==3,
 'no_mathematical_check_claim':report['check_events']==[],
 'all_image_views_single':all(x['inspections']==1 and x['delivery']=='successful' for x in report['image_audit']['image_views'])
}
for name,value in checks.items():
    if not value:issues.append('source consistency check failed: '+name)
actual_counts={
 'difference_rows':len(report['differences']),
 'diff_C_true':sum(x['diff_C'] for x in report['differences']),
 'diff_H_true':sum(x['diff_H'] for x in report['differences']),
 'remaining_local_doubts':len(report['doubts']),
 'inventory_items':len(report['inventory']),
 'literal_path_commands':len(re.findall(r'\\draw\[',tex))
}
for k,v in actual_counts.items():
    if report['counts'][k]!=v:issues.append('reported count mismatch: '+k)
audit={'scope':'Direct source structure, reference existence, row identities, declared counts and literal report/source choices only; no compilation, rendering, mathematical computation, image comparison or metric validation.',
 'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'issues':issues,'braces_balanced':not stack,'environment_stack_empty':not envs,
 'display_pairs':tex.count(r'\['),'inline_dollar_count':dollars,
 'macro_names':macros,'source_consistency':checks,'actual_counts':actual_counts,
 'view_history':'One whole, two halves and seventeen crops. No failed unseen delivery or repeated view.',
 'complete_tex_read_again_for_source_only_consistency':True}
(out/'source_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
report['structural_audit']={'status':'passed' if not issues else 'issues remain','file':'source_audit.json','issues':issues,'compilation_performed':False,'rendering_performed':False}
report['end_utc']=audit['checked_utc']
for d in report['differences']:
    if d['id']=='020C-D10':d['reading']='E_i, et'
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'issues':issues,'source_consistency':checks,'counts':actual_counts,'checked_utc':audit['checked_utc']},indent=2))
