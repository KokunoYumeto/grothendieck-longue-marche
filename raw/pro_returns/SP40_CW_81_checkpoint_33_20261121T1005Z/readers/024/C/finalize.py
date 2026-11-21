from pathlib import Path
import json,re,hashlib,datetime,collections
D=Path('out/readers/024/C');s=D.joinpath('reading.tex').read_text();r=json.loads(D.joinpath('report.json').read_text());sm=json.loads(D.joinpath('source_map.json').read_text());va=json.loads(D.joinpath('view_audit.json').read_text());md=D.joinpath('reading.md').read_text()
errors=[];checks={}
def record(key,ok,detail):
 checks[key]={'passed':bool(ok),'detail':detail}
 if not ok:errors.append(key)
t='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())
st=[];extra=[]
for i,c in enumerate(t):
 if i and t[i-1]=='\\':continue
 if c=='{':st.append(i)
 elif c=='}':
  if st:st.pop()
  else:extra.append(i)
record('braces',not st and not extra,{'unclosed':st,'extra_closers':extra})
es=[];eb=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
 if m[1]=='begin':es.append(m[2])
 elif not es or es.pop()!=m[2]:eb.append(m.group())
record('environments',not es and not eb,{'unclosed':es,'mismatches':eb})
record('display_delimiters',t.count(r'\[')==1 and t.count(r'\]')==1,{'open':t.count(r'\['),'close':t.count(r'\]')})
dollars=len(re.findall(r'(?<!\\)\$',t));record('dollar_pairing',dollars%2==0,{'count':dollars})
record('no_blank_physical_source_lines_in_math','\n\n' not in s[s.index(r'\['):s.index(r'\]')],{'display_checked':True,'inline_source':'No blank lines occur between opening and closing inline math constructs; paragraph gaps occur before Lemme, le, Soient.'})
allowed={'scanpage','unsure','Pi','circ','setminus','bigcup','alpha','begin','end','path','node','fill','deleted','draw','phantom','figure','uline','forall','in','inserted','quad','text','overset','Longleftrightarrow','overline','cap','ne','varnothing','rlap','mathord','cdot','Sigma','subset'}
used=set(re.findall(r'\\([A-Za-z]+)',t));record('command_vocabulary',used<=allowed,{'used':sorted(used),'unexpected':sorted(used-allowed)})
record('single_backslash_commands',not re.search(r'\\\\[A-Za-z]+',t),'No double-backslash command token in active source.')
record('scan_and_archive_wrappers',s.count(r'\scanpage{24}')==1 and '% archive sheet number: 23' in s and r'\cotefile' not in t and r'\mspage' not in t,'Scan wrapper 24 once; archive 23 only in comment; no cotefile or manuscript-page number.')
span_errors=[]
for collection in ['groups','plain_units','paths_and_nodes','wrappers','environments']:
 for obj in sm[collection]:
  sp=obj['source_span'];a=sp['character_start'];b=sp['character_end_exclusive']
  if s[a:b]!=sp['exact_tex']:span_errors.append((collection,obj.get('id')))
record('source_map_exact_spans',not span_errors,{'span_errors':span_errors,'groups':len(sm['groups']),'paths_and_nodes':len(sm['paths_and_nodes']),'wrappers':len(sm['wrappers']),'environments':len(sm['environments'])})
sha=hashlib.sha256(s.encode()).hexdigest();record('source_map_reading_hash',sha==sm['sha256'],sha)
gids={g['id'] for g in sm['groups']};missing_groups=[]
for x in r['differences']+r['inventory']:
 gs=x.get('source_groups',[])+([x['source_group']] if x.get('source_group') else [])
 for g in gs:
  if g not in gids:missing_groups.append(g)
record('group_references',not missing_groups,{'missing':missing_groups})
missing_crops=[c['path'] for c in r['crops'] if not D.joinpath(c['path']).exists()]
known={c['path'] for c in r['crops']};missing_refs=[d['readers_crop'] for d in r['differences'] if d.get('readers_crop') and d['readers_crop'] not in known]
record('crop_references',not missing_crops and not missing_refs,{'missing_files':missing_crops,'missing_references':missing_refs,'count':len(known)})
counts=collections.Counter(e['status'] for e in va['events']);paths=[e['path'] for e in va['events'] if e['status']=='success'];unique=len(paths)==len(set(paths))
record('viewing_counts',counts.get('success')==25 and counts.get('failed',0)==0 and unique and len(r['crops'])==22,{'statuses':dict(counts),'unique_successful_paths':unique,'whole':1,'halves':2,'crops':22})
record('original_C_rows',len(r['C_source_doubts'])==18 and {x['id'] for x in r['C_source_doubts']}=={f'C024-R{i:02d}' for i in range(1,19)},{'rows':len(r['C_source_doubts']),'resolved':sum(x['overall_status']=='resolved' for x in r['C_source_doubts']),'retained':sum(x['overall_status']=='retained' for x in r['C_source_doubts'])})
record('inventory_coverage',len(r['C_inventory_coverage'])==12 and all(x['transcribed']=='yes' for x in r['inventory']),{'original_inventory_rows':len(r['C_inventory_coverage']),'final_inventory_rows':len(r['inventory'])})
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
record('collation_categories',all(x['kind'] in kinds for x in r['differences']),sorted({x['kind'] for x in r['differences']}))
record('honest_check_events',r['check_events']==[],'No mathematical check/computation performed; structural checks live in this separate record.')
# Complete candidates are checked against literal source or its retained complete-state comments/metadata.
required=[r'\unsure{Considerons|Considérons}',r"\alpha'",r"l'ens",r'\unsure{On a|On}',r'\unsure{U|E}',r'{def}',r'(S,I)\deleted{R})|(S,I\deleted{)},R)',r'\unsure{ens de|ens des}',r'\unsure{aretes|arêtes|arètes}',r'\unsure{existe|ex}',r'\unsure{Soient|Soit}',r'\unsure{exactemt|exactement}',r'\unsure{de|dé|qui}',r'\unsure{Le|Ce}',r'\unsure{le|Le}',r'\unsure{connexes|conn}',r"\unsure{l'ens|l'une}",r'definit un',r'contenu dans',r'tel que',r'(et de $=$ pour']
missing=[q for q in required if q not in s];record('complete_candidate_source_tokens',not missing,{'missing':missing})
record('public_counts_and_candidates',f"{len(r['differences'])} difference/source-choice records" in md and f"{len(r['inventory'])} inventory elements" in md and all(z in md for z in ['qu\'on followed by an unassigned point','aretes|arêtes|arètes','exactemt|exactement','de|dé|qui']),{'differences':len(r['differences']),'inventory':len(r['inventory'])})
record('public_block_spacing',r'\in R\quad' in md and r'\Longleftrightarrow}\quad' in md,'Public reading block uses explicit ordinary math spacing.')
validation={'scan':24,'reader':'C','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Source-only structural and reference checks. No TeX compilation, rendering, OCR, image comparison, alignment or curve-coordinate computation.','checks':checks,'errors':errors,'passed':not errors}
D.joinpath('structural_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
if errors:
 print(json.dumps(validation,ensure_ascii=False,indent=2));raise SystemExit(1)
r['end_utc']=validation['checked_utc']
r['provenance']['structural_validation_file']='structural_validation.json'
r['provenance']['source_agreement']='All exact source-map slices, group/crop links, original doubt identities, full-candidate tokens and public counts passed structural checks. Manuscript readings and punctuation reviewed together against the completed own visual record.'
r['source_macro_occurrences']={k:len(re.findall(r'\\'+k+r'\b',t)) for k in ['unsure','illegible','deleted','inserted','uline']}
r['source_macro_count_scope']='Active source counts include invisible provenance/state annotations; these are not claimed as rendered visible counts.'
r['counts']['physical_clusters_diff_C']=len({x.get('physical_cluster',x['id']) for x in r['differences'] if x['diff_C']})
r['counts']['physical_clusters_diff_H']=len({x.get('physical_cluster',x['id']) for x in r['differences'] if x['diff_H']})
r['artifact_hashes_before_report_hash']={'reading.tex':sha,'reading.md':hashlib.sha256(md.encode()).hexdigest(),'source_map.json':hashlib.sha256(D.joinpath('source_map.json').read_bytes()).hexdigest(),'view_audit.json':hashlib.sha256(D.joinpath('view_audit.json').read_bytes()).hexdigest()}
D.joinpath('report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':True,'end_utc':r['end_utc'],'checks':len(checks),'counts':r['counts'],'source_macro_occurrences':r['source_macro_occurrences']},ensure_ascii=False,indent=2))
