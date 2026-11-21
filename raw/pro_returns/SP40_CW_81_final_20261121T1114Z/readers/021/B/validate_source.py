from pathlib import Path
import re,json
base=Path('out/readers/021/B')
s=(base/'reading.tex').read_text()
body='\n'.join(line.split('%',1)[0] for line in s.splitlines())
stack=[];unmatched=[]
for m in re.finditer(r'(?<!\\)[{}]',body):
 if m.group()=='{':stack.append(m.start())
 elif stack:stack.pop()
 else:unmatched.append(m.start())
envstack=[];env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 op,name=m.groups()
 if op=='begin':envstack.append(name)
 elif not envstack or envstack[-1]!=name:env_errors.append([op,name])
 else:envstack.pop()
blank_display=[];inside=False
for i,line in enumerate(s.splitlines(),1):
 if r'\[' in line:inside=True
 elif r'\]' in line:inside=False
 elif inside and not line.strip():blank_display.append(i)
# Full group boundaries must agree with the current literal source.
a=json.loads((base/'source_audit.json').read_text())
source_groups_ok=all(s[g['source_start_char']:g['source_end_char_exclusive']]==g['exact_source'] for g in a['groups'])
r=json.loads((base/'report.json').read_text())
for d in r['differences']:
 if d['kind'].startswith('readable ink left as'):d['kind']=r'readable ink left as \ill{}'
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
files_ok=all((base/d['readers_crop']).is_file() for d in r['differences'] if d['readers_crop'])
required_outside={'on a':r' on a','live signifie':r' signifie aussi que','comma cqfd':r',\qquad\text{cqfd.}','margin closing':r'\end{tikzcd}}'}
outside_ok={k:v in body for k,v in required_outside.items()}
check={'type':'structural source-only validation','brace_unmatched_open':len(stack),'brace_unmatched_close':len(unmatched),'environment_stack_remaining':envstack,'environment_errors':env_errors,'display_open_count':body.count(r'\['),'display_close_count':body.count(r'\]'),'blank_lines_inside_display':blank_display,'dollar_delimiter_count':len(re.findall(r'(?<!\\)\$',body)),'source_group_boundaries_match':source_groups_ok,'referenced_crop_files_exist':files_ok,'allowed_difference_kinds':all(d['kind'] in allowed for d in r['differences']),'actual_C_source_rows':len(r['actual_C_outcome_map']),'H_null_rows':[d['id'] for d in r['differences'] if d['H'] is None],'outside_group_content_checks':outside_ok,'new_tex_macros_defined':bool(re.search(r'\\(?:newcommand|renewcommand|def)\b',body)),'compilation_performed':False,'rendering_performed':False,'mathematical_checks_performed':False}
assert not stack and not unmatched and not envstack and not env_errors
assert body.count(r'\[')==body.count(r'\]') and not blank_display
assert source_groups_ok and files_ok and check['allowed_difference_kinds'] and all(outside_ok.values())
a['structural_validation']=check
r['provenance']['structural_validation']=check
r['provenance']['source_only_events']+=['Administrative report counts and source-row mappings were generated from the current records.','An initial report-build assertion included3 slip-table context rows after the15 doubtful-reading rows; the parser was corrected to stop at the Slips kept as written heading.','An initial source-only brace check found one open margin brace: an end-group comment consumed same-line following tokens. A newline was added after every generated group marker; the live on a, signifie aussi que, formula comma/cqfd. and margin closure were then checked directly in uncommented source.','Difference-kind metadata was corrected from a two-backslash ill category spelling to the exact required one-backslash spelling; manuscript tokens were unchanged.','The next source-only validation found empty physical lines before several display closures after the end-group marker repair. Only empty lines inside display delimiters were removed, and the group offsets were regenerated from the repaired source.']
(base/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(base/'source_audit.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
(base/'source_validation.json').write_text(json.dumps(check,ensure_ascii=False,indent=2))
log=json.loads((base/'processing_log.json').read_text());log['source_only_events']=r['provenance']['source_only_events'];log['structural_validation']=check
(base/'processing_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
print(json.dumps(check,ensure_ascii=False))
