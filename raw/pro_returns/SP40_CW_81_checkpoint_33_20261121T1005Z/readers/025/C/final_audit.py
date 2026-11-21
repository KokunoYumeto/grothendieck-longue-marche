from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
R=Path(__file__).parent
s=(R/'reading.tex').read_text();report=json.loads((R/'report.json').read_text());sm=json.loads((R/'source_map.json').read_text());va=json.loads((R/'view_audit.json').read_text())
# Source-only syntax checks. No compilation, rendering or mathematical checks.
clean='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())
stack=[];errors=[]
for m in re.finditer(r'(?<!\\)[{}]',clean):
 if m.group()=='{':stack.append(m.start())
 elif stack:stack.pop()
 else:errors.append('unmatched closing brace at '+str(m.start()))
if stack:errors.append('unmatched opening braces '+str(stack))
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 if m[1]=='begin':envs.append(m[2])
 elif not envs or envs.pop()!=m[2]:errors.append('environment mismatch '+m.group())
if envs:errors.append('open environments '+str(envs))
assert clean.count(r'\[')==clean.count(r'\]')==2
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert '\n\n' not in s
for g in sm['groups']:
 a,b=g['char_offsets'];assert s[a:b]==g['literal_source'],g['id']
 aa,bb=g['byte_offsets_utf8'];assert s.encode()[aa:bb].decode()==g['literal_source']
for d in report['differences']:
 if d.get('reader_source_excerpt'):
  a,b=d['reader_source_char_offsets'];assert s[a:b]==d['reader_source_excerpt'],d['id']
 if d.get('readers_crop'):assert (R/d['readers_crop']).exists()
assert len(report['C_doubt_rows'])==8
assert len({r['source_row_id'] for r in report['C_doubt_rows']})==8
assert len(va['events'])==19
assert len({e['path'] for e in va['events']})==19
assert all(e['success'] and e['view_count']==1 for e in va['events'])
assert all(c['successfully_viewed'] for c in report['crops'])
assert not errors,errors
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',clean)))
allowed={'scanpage','tikz','coordinate','useasboundingbox','node','rlap','phantom','deleted','draw','unsure','Sigma','prime','overline','subset','cap','fill','ne','varnothing','begin','end','setminus','mathop','raisebox','scriptstyle','bigcup','bigcap','limits','alpha','in','widehat','qquad','text','quad','forall','pi','textsuperscript','inserted','bigl','mid','figure'}
unknown=sorted(set(commands)-allowed)
assert not unknown,unknown
now=datetime.now(timezone.utc).isoformat()
checks={'time_utc':now,'method':'source-only structural and consistency review','braces':'balanced excluding escaped delimiters and comments','environments':'balanced aligned and tikzpicture','display_pairs':2,'dollar_count_even':True,'empty_physical_lines_inside_math':0,'macros':'all source commands in supplied macros or ordinary LaTeX/TikZ/amsmath vocabulary','source_group_count':len(sm['groups']),'source_offsets_exact':True,'report_reader_source_quotes_exact':True,'crop_files_exist':True,'image_audit_unique_successful_views':19,'original_C_doubt_rows':8,'math_checks_performed':False,'compiled':False,'rendered':False,'installed_packages':False,'image_matching_performed':False,'sha256_reading_tex':hashlib.sha256(s.encode()).hexdigest(),'limitations':['Literal path/font placements are manual approximations, not rendered or metric verified.','Disjoints reaches physical paper edge; no unseen punctuation is supplied.','Unresolved glyph/state/role/hand alternatives remain explicit.'],'errors':errors}
report['final_audit']=checks;report['end_utc']=now
report['provenance']['source_macro_occurrences']={k:len(re.findall(r'\\'+k+r'\b',clean)) for k in ['unsure','illegible','deleted','inserted']}
report['provenance']['source_macro_occurrence_note']='Counts include invisible annotations and therefore are not physical-locus counts.'
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(R/'final_audit.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
va['complete_visual_read']=True;va['end_utc']=now;va['final_counts']={'whole':1,'a':1,'b':1,'deep_crops':16,'successful_total':19,'failed_unseen_deliveries':0,'reopens':0,'recrops':0};va['stopped_after_assigned_page']=True
(R/'view_audit.json').write_text(json.dumps(va,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False,indent=2))
