from pathlib import Path
import re,json,hashlib,datetime
P=Path('out/readers/026/A');s=(P/'reading.tex').read_text()
clean='\n'.join(re.split(r'(?<!\\)%',ln,maxsplit=1)[0] for ln in s.splitlines())
stack=[];errs=[]
for m in re.finditer(r'(?<!\\)[{}]',clean):
 if m.group()=='{':stack.append(m.start())
 elif stack:stack.pop()
 else:errs.append({'extra_closing_brace':m.start()})
errs += [{'unclosed_brace':p} for p in stack]
env=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 typ,name=m.groups()
 if typ=='begin':env.append(name)
 elif not env or env[-1]!=name:errs.append({'environment_mismatch':[typ,name,list(env)]})
 else:env.pop()
if env:errs.append({'unclosed_environments':env})
displays=re.findall(r'\\\[([\s\S]*?)\\\]',s)
blank_math=[]
for i,d in enumerate(displays,1):
 for j,l in enumerate(d.splitlines(),1):
  if j>1 and not l.strip():blank_math.append({'display':i,'relative_line':j})
if blank_math:errs.append({'blank_physical_lines_in_display':blank_math})
if clean.count('\\[')!=clean.count('\\]'):errs.append({'display_delimiter_count':[clean.count('\\['),clean.count('\\]')]})
dollars=len(re.findall(r'(?<!\\)\$',clean))
if dollars%2:errs.append({'odd_dollar_count':dollars})
if '$$' in clean:errs.append({'double_dollars_present':True})
report=json.loads((P/'report.json').read_text());sm=json.loads((P/'source_map.json').read_text())
assert len(report['C_doubt_source_rows'])==15
assert [r['id'] for r in report['C_doubt_source_rows']]==[f'C026-R{i:02d}' for i in range(1,16)]
assert ''.join(x['text'] for x in sm['complete_source_partition'])==s
for g in sm['local_groups']:
 assert s[g['source_char_start']:g['source_char_end_exclusive']]==g['source_excerpt'],g['id']
 assert s.count('% BEGIN '+g['id']+'\n')==1,g['id']
 assert s.count('% END '+g['id']+'\n')==1,g['id']
 assert hashlib.sha256(g['source_excerpt'].encode()).hexdigest()==g['source_excerpt_sha256']
for d in report['differences']:
 if d.get('readers_crop'):assert (P/d['readers_crop']).is_file(),d['id']
for c in report['crops']:
 assert (P/c['path']).is_file()
 assert hashlib.sha256((P/c['path']).read_bytes()).hexdigest()==c['sha256']
for n in ['A026-S04','A026-S05','A026-S07']:
 g=next(g for g in sm['local_groups'] if g['id']==n)
 assert r'\phantom{$\Sigma_{\deleted{\unsure{\alpha}}}' in g['source_excerpt'],n
assert 'raisebox{-2mm}' in s
assert r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1171,1188)' in s
assert '% margin note written sideways' in s and '% archive sheet number: 25' in s
cmds=sorted(set(re.findall(r'\\([A-Za-z]+)',clean)))
result={'checked_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'source_only':True,'compilation_attempted':False,'rendering_attempted':False,'brace_balance':not any('brace' in str(e) for e in errs),'environment_balance':not env and not any('environment' in str(e) for e in errs),'display_count':len(displays),'dollar_tokens':dollars,'blank_physical_lines_inside_displays':blank_math,'group_count':len(sm['local_groups']),'every_group_occurs_once':True,'exact_source_partition_reconstruction':True,'crop_references_and_hashes_valid':True,'C_source_rows_in_exact_order':15,'qualified_index_annotations_present':True,'registered_M02_nested_once':True,'M03_downward_displacement_present':True,'macros_encountered':cmds,'errors':errs,'prior_source_repairs':['Removed one extra generated closing brace in invisible annotation nodes before this check.','Replaced empty hidden $$ annotations with an empty-height phantom expression.','Kept the two binary pairs, their correction and bent guide in one complete local group.'],'scope':'Structural source reconstruction and delimiters only. No mathematical or image-identity result follows.'}
(P/'source_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['macros_encountered','prior_source_repairs']},ensure_ascii=False,indent=2))
if errs:raise SystemExit(1)
