from pathlib import Path
import json,re,hashlib,collections

P=Path('/workspace/scratch/94548b74fbe0/out/readers/022/C')
s=(P/'reading.tex').read_text();report=json.loads((P/'report.json').read_text())
clean='\n'.join(re.split(r'(?<!\\)%',x)[0] for x in s.splitlines())
stack=[];brace_errors=[]
for n,line in enumerate(clean.splitlines(),1):
 for j,c in enumerate(line):
  if c=='{' and (j==0 or line[j-1]!='\\'):stack.append((n,j))
  elif c=='}' and (j==0 or line[j-1]!='\\'):
   if stack:stack.pop()
   else:brace_errors.append(['extra closing brace',n,j])
brace_errors += [['unclosed brace',*x] for x in stack]
env=[];env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 if m.group(1)=='begin':env.append(m.group(2))
 elif not env or env.pop()!=m.group(2):env_errors.append(m.group(0))
env_errors+=env
allowed={'scanpage','deleted','unsure','operatorname','inserted','mbox','begin','end','path','draw','node','fill','small','large','scriptsize','alpha','beta','Sigma','widehat','overline','cap','cup','bigcap','bigcup','setminus','in','subset','ne','varnothing','Rightarrow','phantom','rlap','figure','uline','par','rotatebox'}
commands=set(re.findall(r'\\([A-Za-z]+)',clean));unknown=sorted(commands-allowed)
g=json.loads((P/'source_groups.json').read_text());paths=json.loads((P/'path_components.json').read_text());im=json.loads((P/'image_audit.json').read_text())
excerpt_errors=[]
for v in g:
 t=s[v['start_char']:v['end_char_exclusive']]
 if t!=v['source'] or hashlib.sha256(t.encode()).hexdigest()!=v['sha256']:excerpt_errors.append(v['id'])
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
checks={
 'brace_errors':brace_errors,'environment_errors':env_errors,'unknown_commands':unknown,
 'display_open_count':clean.count('\\['),'display_close_count':clean.count('\\]'),
 'unescaped_dollar_count':len(re.findall(r'(?<!\\)\$',clean)),
 'unescaped_dollar_even':len(re.findall(r'(?<!\\)\$',clean))%2==0,
 'physical_empty_lines':sum(not x.strip() for x in s.splitlines()),
 'group_excerpt_errors':excerpt_errors,'source_group_count':len(g),'path_count':len(paths),
 'path_owner_missing':[x['id'] for x in paths if not x['owner']],
 'source_group_ids_unique':len({v['id'] for v in g})==len(g),
 'sigma_group_count':len([v for v in g if re.fullmatch(r'C022-S\d\d',v['id'])]),
 'required_page_marker':re.findall(r'\\scanpage\{([^}]+)\}',clean),
 'cotefile_count':clean.count('\\cotefile'),'mspage_count':clean.count('\\mspage'),
 'archive_21_comment_count':s.count('% archive sheet number: 21'),
 'invalid_difference_kinds':[d['id'] for d in report['differences'] if d['kind'] not in kinds],
 'missing_crop_files':[c['path'] for c in report['crops'] if not (P/c['path']).is_file()],
 'each_successful_image_seen_once':all(x['successful_view_count']==1 for x in im['events']),
 'image_event_count':len(im['events']),'failed_unseen_deliveries':len(im['failed_unseen_deliveries']),
 'C_source_doubt_identity_count':len(report['C_doubt_source_map']),
 'C_source_doubt_decision_coverage':all(all(any(d['id']==a for d in report['differences']) for a in r['decision_ids']) for r in report['C_doubt_source_map']),
 'H_actual_local_marker_ids':[d['id'] for d in report['differences'] if d['marked_in_H']],
 'all_differences_have_exact_H_excerpt':all(bool(d.get('H_exact_source')) for d in report['differences']),
 'all_differences_have_exact_C_excerpt':all(bool(d.get('C_exact_source')) for d in report['differences']),
 'all_inventory_entries_transcribed':all(v['transcribed']=='yes' for v in report['inventory']),
 'math_check_events_count':len(report['check_events']),
 'scope':'Source-only administrative/structural audit. No TeX compiler, rendering, OCR, image comparison or mathematical proof check was used.'
}
bad=brace_errors or env_errors or unknown or excerpt_errors or checks['invalid_difference_kinds'] or checks['missing_crop_files'] or checks['path_owner_missing']
checks['passed_bounded_source_checks']=not bool(bad) and checks['display_open_count']==checks['display_close_count'] and checks['unescaped_dollar_even'] and checks['physical_empty_lines']==0 and checks['all_differences_have_exact_C_excerpt'] and checks['all_differences_have_exact_H_excerpt']
(P/'source_audit.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False))
