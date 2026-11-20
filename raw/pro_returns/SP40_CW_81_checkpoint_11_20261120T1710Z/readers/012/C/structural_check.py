from pathlib import Path
import re,json
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/readers/012/C'
s=(O/'reading.tex').read_text(); c=(B/'packets/012/C.tex').read_text()
r=json.loads((O/'report.json').read_text()); marks=json.loads((O/'marks_manifest.json').read_text())
body='\n'.join(line.split('%',1)[0] for line in s.splitlines())
results={}
for left,right,name in [('{','}','braces'),('[',']','brackets'),('(',')','parentheses')]:
 depth=0;low=0
 for ch in body:
  if ch==left:depth+=1
  elif ch==right:depth-=1;low=min(low,depth)
 results[name]={'final_depth':depth,'minimum_depth':low,'ok':depth==0 and low==0}
stack=[];env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 action,env=m.groups()
 if action=='begin':stack.append(env)
 elif not stack or stack.pop()!=env:env_errors.append(m.group(0))
results['environments']={'remaining_stack':stack,'errors':env_errors,'ok':not stack and not env_errors}
cmds=sorted(set(re.findall(r'\\([A-Za-z]+)',body)))
allowed={'scanpage','figure','begin','end','path','node','draw','unsure','scriptsize'}
results['macros']={'used':cmds,'unknown':sorted(set(cmds)-allowed),'ok':set(cmds)<=allowed}
ps=list(re.finditer(r'\\path\[fill=black,even odd rule\]\s*.*?;',c,re.S))
missing=[];repeated=[]
for i,p in enumerate(ps,1):
 n=s.count(p.group(0))
 if n==0:missing.append(i)
 if n>1:repeated.append(i)
results['source_paths']={'source_count':len(ps),'missing':missing,'repeated':repeated,'ok':len(ps)==68 and not missing and not repeated}
labels=re.findall(r'\\node\[inner sep=0pt[^\n]*;',c)
results['source_labels']={'source_count':len(labels),'all_present_once':all(s.count(x)==1 for x in labels),'ok':len(labels)==8 and all(s.count(x)==1 for x in labels)}
results['marks']={'count':len(marks),'missing':[m['id'] for m in marks if m['tex'] not in s or '% '+m['id']+':' not in s],'ok':all(m['tex'] in s and '% '+m['id']+':' in s for m in marks)}
required={'scan','reader','start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read','differences','doubts','inventory','notes','notation','check_events','crops','brief_feedback'}
results['report_keys']={'missing':sorted(required-set(r)),'ok':required<=set(r)}
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
results['difference_schema']={'invalid_kinds':[d['id'] for d in r['differences'] if d['kind'] not in kinds],'invalid_readings':[d['id'] for d in r['differences'] if 'reading' not in d],'ok':all(d['kind'] in kinds and 'reading' in d for d in r['differences'])}
results['doubts_schema']={'ok':all('reading' in d and 'alternatives' in d for d in r['doubts'])}
refs=set()
for key in ['differences','doubts']:
 for x in r[key]:
  ref=x.get('readers_crop') or x.get('crop')
  if ref:refs.add(ref)
refs.update(x['path'] for x in r['crops'])
results['crop_references']={'count':len(refs),'missing':[x for x in sorted(refs) if not (O/x).is_file()],'ok':all((O/x).is_file() for x in refs)}
source_rows=r['source_doubt_map'];diff_ids={d['id'] for d in r['differences']}
results['source_doubt_mapping']={'source_rows':len(source_rows),'source_ids':[x['source_row_id'] for x in source_rows],'statuses':[x['status'] for x in source_rows],'ok':len(source_rows)==3 and len({x['source_row_id'] for x in source_rows})==3 and all(all(i in diff_ids for i in x['difference_ids']) for x in source_rows)}
results['inventory']={'count':len(r['inventory']),'ok':all(i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} and i['transcribed']=='yes' for i in r['inventory']) and len({i['element'] for i in r['inventory']})==len(r['inventory'])}
results['source_path_inventory_coverage']={'missing':sorted(set(range(1,69))-{p for i in r['inventory'] for p in i.get('C_source_paths',[])}),'ok':set(range(1,69))<={p for i in r['inventory'] for p in i.get('C_source_paths',[])}}
results['scope']={'has_scan12':r'\scanpage{12}' in s,'has_archive11':'% archive sheet number: 11' in s,'offscan_heading_absent':'Décompositions' not in s,'no_author_page_macro':r'\mspage' not in s,'no_cotefile':r'\cotefile' not in s,'ok':r'\scanpage{12}' in s and '% archive sheet number: 11' in s and 'Décompositions' not in s and r'\mspage' not in s and r'\cotefile' not in s}
results['abbreviation_schema']={'ok':all('expansion' in x for x in r['abbreviations'])}
results['mathematical_checks']={'check_events':r['check_events'],'ok':r['check_events']==[]}
manifest=json.loads((O/'crops/manifest.json').read_text())
results['crop_manifest_sync']={'count':len(manifest),'unique_paths':len({x['path'] for x in manifest}),'ok':r['crops']==manifest and len(manifest)==17 and len({x['path'] for x in manifest})==17 and r['notes']['image_views']['crops_generated']==17 and r['notes']['image_views']['crops_visually_inspected']==17}
mark_errors=[]
for m in marks:
 ds=[x for x in r['differences'] if x.get('local_id')==m['id']]
 qs=[x for x in r['doubts'] if x.get('local_id')==m['id']]
 iv=[x for x in r['inventory'] if x['element']=='012.C.'+m['id']]
 if len(ds)!=1 or len(qs)!=1 or len(iv)!=1:
  mark_errors.append(m['id']+': record cardinality');continue
 d,q,i=ds[0],qs[0],iv[0]
 if not (d['reading']==q['reading']==i['first_words_or_objects']==m['reading'] and d['bbox']==q['bbox']==i['bbox']==m['bbox'] and d['readers_crop']==q['crop']==m['crop'] and q['hand']==i['hand']==m['hand']):
  mark_errors.append(m['id']+': record mismatch')
 if m['crop']:
  cr=next(x for x in manifest if x['path']==m['crop']);a,b,c,d=cr['bbox'];e,f,g,h=m['bbox']
  if not (a<=e<g<=c and b<=f<h<=d):mark_errors.append(m['id']+': bbox outside crop')
results['new_mark_synchronization']={'count':len(marks),'errors':mark_errors,'ok':not mark_errors}
results['overall_pass']=all(x['ok'] for x in results.values() if isinstance(x,dict) and 'ok' in x)
(O/'structural_checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
if not results['overall_pass']:raise SystemExit(1)
