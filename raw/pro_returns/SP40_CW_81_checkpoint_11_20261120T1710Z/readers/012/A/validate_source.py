from pathlib import Path
import re,json,datetime
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/012/A'
s=(out/'reading.tex').read_text()
c=(root/'packets/012/C.tex').read_text()
r=json.loads((out/'report.json').read_text())
clean='\n'.join(line.split('%',1)[0] for line in s.splitlines())
checks={}
level=0;minimum=0
for ch in clean:
 if ch=='{':level+=1
 elif ch=='}':level-=1;minimum=min(minimum,level)
checks['braces_balanced']=level==0 and minimum==0
stack=[];errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 what,env=m.groups()
 if what=='begin':stack.append(env)
 elif not stack or stack.pop()!=env:errors.append(m.group(0))
checks['environments_balanced']=not stack and not errors
macros=sorted(set(re.findall(r'\\([A-Za-z]+)',clean)))
allowed={'scanpage','figure','begin','end','path','node','unsure','draw','fill','scriptsize'}
checks['macros_allowed']=set(macros)<=allowed
checks['no_new_macro_or_package']=not re.search(r'\\(?:newcommand|renewcommand|def|usepackage|input|includegraphics)\b',clean)
checks['scan_macro']=s.count(r'\scanpage{12}')==1 and r'\cotefile' not in clean
checks['archive_comment']=s.count('% archive sheet number: 11')==1 and r'\mspage' not in clean
paths=re.findall(r'\\path\[fill=black,even odd rule\]\s*.*?;',c,re.S)
checks['all_original_68_paths_exactly_once']=len(paths)==68 and all(s.count(p)==1 for p in paths)
nodes=re.findall(r'\\node\[inner sep=0pt.*?;',c)
checks['all_original_8_label_nodes_retained']=len(nodes)==8 and all(s.count(n)==1 for n in nodes)
checks['all_difference_anchors_present']=all(d.get('tex_anchor') and d['tex_anchor'] in s for d in r['differences'])
checks['all_doubt_anchors_present']=all(d.get('tex_anchor') and d['tex_anchor'] in s for d in r['doubts'])
checks['all_doubts_use_reading']=all('reading' in d for d in r['doubts'])
checks['abbreviations_use_expansion']=all('expansion' in a for a in r['abbreviations'])
checks['all_C_rows_mapped_once']=[a['source_row_id'] for a in r['source_C_doubt_rows']]==['C-D1','C-D2','C-D3']
checks['C_row_map_references_exist']=all(any(d['id']==l['difference_id'] for d in r['differences']) and any(d['id']==l['doubt_id'] for d in r['doubts']) for a in r['source_C_doubt_rows'] for l in a['local_loci'])
checks['crop_manifest_unique_11']=len(r['crops'])==11 and len({p['path'] for p in r['crops']})==11
checks['crop_paths_exist']=all((out/p['path']).is_file() for p in r['crops'])
checks['all_crop_references_valid']=all(d['readers_crop'] is None or (out/d['readers_crop']).is_file() for d in r['differences']) and all(d['crop'] is None or (out/d['crop']).is_file() for d in r['doubts'])
checks['bboxes_full_scan_bounded']=all(0<=d['bbox'][0]<d['bbox'][2]<=1690 and 0<=d['bbox'][1]<d['bbox'][3]<=2361 for d in r['differences'])
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
checks['difference_kinds_valid']=all(d['kind'] in kinds for d in r['differences'])
ikinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
checks['inventory_kinds_valid']=all(a['kind'] in ikinds for a in r['inventory'])
checks['inventory_actual_representation']=all(a['transcribed']=='yes' for a in r['inventory'])
checks['all_original_paths_in_inventory']=set(p for a in r['inventory'] for p in a.get('source_paths',[]))==set(range(1,69))
checks['every_new_C_reading_in_inventory']=all(any(a.get('difference_id')==d['id'] for a in r['inventory']) for d in r['differences'] if d['diff_C'])
checks['mathematical_check_events_empty']=r['check_events']==[]
checks['all_sources_current']=r['scan']==12 and r['reader']=='A' and r['start_utc']=='2026-11-20T12:54:24Z'
result={'checks':checks,'all_passed':all(checks.values()),'macros':macros,'original_path_count':len(paths),'original_label_count':len(nodes),'environment_occurrences':dict((e,len(re.findall(r'\\begin\{'+re.escape(e)+r'\}',clean))) for e in set(re.findall(r'\\begin\{([^}]+)\}',clean))),'compiler_invoked':False,'rendering_invoked':False,'check_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')}
(out/'structural_checks.json').write_text(json.dumps(result,indent=2)+'\n')
if not result['all_passed']:
 print(json.dumps(result,indent=2));raise SystemExit(1)
r['end_utc']=result['check_utc']
r['structural_validation']=result
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
md=(out/'reading.md').read_text()
md+='\nCompletion UTC: '+r['end_utc']+'. All '+str(len(checks))+' structural source checks passed.\n'
(out/'reading.md').write_text(md)
print(json.dumps({'all_passed':result['all_passed'],'checks':len(checks),'end_utc':r['end_utc'],'difference_rows':len(r['differences']),'doubts':len(r['doubts']),'inventory':len(r['inventory']),'crops':len(r['crops']),'macros':macros},indent=2))
