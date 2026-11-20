from pathlib import Path
import re,json
out=Path(__file__).resolve().parent
tex=(out/'reading.tex').read_text()
r=json.loads((out/'report.json').read_text())
body='\n'.join(line.split('%',1)[0] for line in tex.splitlines())
stack=[]
braces=[]
for k,c in enumerate(body):
    if c in '{}' and (k==0 or body[k-1]!='\\'):
        if c=='{':stack.append(k)
        elif not stack:braces.append({'unexpected_close':k})
        else:stack.pop()
if stack:braces.append({'unclosed_openings':stack})
envs=[]; env_issues=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    action,name=m.groups()
    if action=='begin':envs.append(name)
    elif not envs or envs[-1]!=name:env_issues.append([action,name,list(envs)])
    else:envs.pop()
if envs:env_issues.append(['unclosed',envs])
allowed={'scanpage','Sigma','cup','deleted','unsure','begin','path','node','draw','end','setminus','inserted','subset','amalg','figure','fill','overline','overset','text','subsetneq','cap','margin','ne','varnothing','rlap','phantom','big','quad','scriptstyle'}
commands=set(re.findall(r'\\([A-Za-z]+)',body))
missing_crops=[c['path'] for c in r['crops'] if not (out/c['path']).is_file()]
missing_refs=[d['id'] for d in r['differences'] if d['readers_crop'] and not (out/d['readers_crop']).is_file()]
ids=[d['id'] for d in r['differences']]
dby={d['id']:d for d in r['differences']}
source_issues=[]
for sr in r['C_doubt_source_map']:
    for i in sr['local_ids']:
        if i not in dby or dby[i]['C_doubt_status'] not in ('resolved','retained'):source_issues.append([sr['row'],i])
        elif sr['statuses'][i]!=dby[i]['C_doubt_status']:source_issues.append(['status_mismatch',i])
markers=[f'G{i:02}' for i in range(1,11)]+['BR01','BR02']
marker_issues=[m for m in markers if m not in tex or m not in ids]
checks={
 'brace_issues':braces,
 'environment_issues':env_issues,
 'dollar_delimiter_count':body.count('$'),
 'dollar_delimiter_even':body.count('$')%2==0,
 'display_open_count':body.count('\\['),
 'display_close_count':body.count('\\]'),
 'unknown_commands':sorted(commands-allowed),
 'duplicate_difference_ids':len(ids)!=len(set(ids)),
 'missing_crops':missing_crops,
 'missing_crop_references':missing_refs,
 'source_doubt_row_count':len(r['C_doubt_source_map']),
 'source_doubt_local_count':sum(len(x['local_ids']) for x in r['C_doubt_source_map']),
 'source_doubt_coverage_issues':source_issues,
 'graphic_marker_issues':marker_issues,
 'H_null_rows':[d['id'] for d in r['differences'] if d['H'] is None],
 'all_inventory_transcribed_yes':all(i['transcribed']=='yes' for i in r['inventory']),
 'archive_comment_present':'% archive sheet number: 15' in tex,
 'no_authorial_page_macro':'\\mspage' not in body,
 'no_new_macros':not any(x in body for x in ('\\newcommand','\\renewcommand','\\def')),
 'resolved_doubts_counted_C':[d['id'] for d in r['differences'] if d['C_doubt_status']=='resolved' and not d['diff_C']],
 'explicit_final_readings':{
  'opening_index':r'\Sigma_{\deleted{\unsure{2}}1}^+' in tex,
  'old_verb':r'\deleted{\unsure{sera|sont}} est' in tex,
  'opening_word_and_colon':r"\unsure{é|ê}gal\unsure{e|} :" in tex,
  'right_insertion':r'\inserted{de $X/E_{\unsure{2}}$}' in tex,
  'lower_insertion':r'\inserted{\unsure{en|on} conclurait}' in tex,
  'qualified_join_count':tex.count(r'\deleted{\amalg}\unsure{\cup|\amalg}')==2,
  'definition_label':r'\overset{\text{def}}{=}' in tex,
  'footer':'ce qui n\'est pas.' in tex,
 },
 'compiled':False,'rendered':False,'mathematical_checks_performed':False
}
(out/'validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False,indent=2))
