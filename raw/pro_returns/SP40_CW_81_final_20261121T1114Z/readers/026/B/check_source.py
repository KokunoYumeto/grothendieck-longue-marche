from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parent
tex=(P/'reading.tex').read_text()
# Strip only unescaped TeX comments. All source checks below are syntactic/administrative.
clean='\n'.join(re.split(r'(?<!\\)%',l,maxsplit=1)[0] for l in tex.splitlines())
stack=[]; brace_errors=[]
for m in re.finditer(r'(?<!\\)[{}]',clean):
 if m.group()=='{':stack.append(m.start())
 elif stack:stack.pop()
 else:brace_errors.append(m.start())
env=[];env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 action,name=m.groups()
 if action=='begin':env.append(name)
 elif not env or env.pop()!=name:env_errors.append([action,name,m.start()])
opens=len(re.findall(r'\\\[',clean));closes=len(re.findall(r'\\\]',clean))
math_blank=[];inside=False
for no,line in enumerate(tex.splitlines(),1):
 if '\\[' in line:inside=True
 if inside and not line.strip():math_blank.append(no)
 if '\\]' in line:inside=False
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',clean)))
allowed={'scanpage','uline','deleted','inserted','unsure','begin','end','path','draw','fill','node','Sigma','alpha','circ','mathcal','mathscr','varepsilon','text','scriptstyle','in','phantom','rlap','setminus','ne','varnothing','cap','subset','supset','cup','overset','reversemarginpar','normalmarginpar','margin','diagram','rotatebox','bullet','quad','qquad'}
unknown=sorted(set(commands)-allowed)
report=json.loads((P/'report.json').read_text());sm=json.loads((P/'source_map.json').read_text())
recon=''.join(x['source'] for x in sm['ordered_source_partition'])
checks={'brace_balance':not stack and not brace_errors,'unclosed_braces':len(stack),'unmatched_closers':brace_errors,'environment_balance':not env and not env_errors,'unclosed_environments':env,'environment_errors':env_errors,'display_delimiters':{'open':opens,'close':closes,'balanced':opens==closes},'dollar_delimiters':{'count':len(re.findall(r'(?<!\\)\$',clean)),'even':len(re.findall(r'(?<!\\)\$',clean))%2==0},'blank_physical_lines_inside_displays':math_blank,'command_names':commands,'unapproved_or_unknown_command_names':unknown,'exact_source_partition_reconstruction':recon==tex,'exact_group_slices':all(tex[g['start_char']:g['end_char']]==g['literal_source'] for g in sm['source_groups']),'exact_group_sha256':all(hashlib.sha256(g['literal_source'].encode()).hexdigest()==g['source_sha256'] for g in sm['source_groups']),'reading_hash_agreement':hashlib.sha256(tex.encode()).hexdigest()==sm['reading_sha256']==report['provenance']['source_reconstruction']['reading_sha256'],'all_crops_exist':all((P/c['path']).is_file() for c in report['crops']),'actual_C_rows_exactly_15':len(report['C_uncertainty_source_rows'])==15,'C_source_order':[r['source_row_id'] for r in report['C_uncertainty_source_rows']],'view_counts':report['view_counts'],'all_inventory_transcribed':all(x['transcribed']=='yes' for x in report['inventory']),'macro_occurrence_counts_excluding_comments':{k:len(re.findall(r'\\'+k+r'\b',clean)) for k in ['unsure','illegible','deleted','inserted']},'scope':'Source-only checks. No compilation, rendering, pixel comparison, theorem, proof or mathematical correspondence check.'}
(P/'source_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False,indent=2))
