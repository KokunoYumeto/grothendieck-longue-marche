from pathlib import Path
import re,json
HERE=Path(__file__).resolve().parent
tex=(HERE/'reading.tex').read_text()
# Strip comments while retaining escaped percent.
s='\n'.join(re.split(r'(?<!\\)%',l,1)[0] for l in tex.splitlines())
errors=[]
stack=[]
for m in re.finditer(r'\\[{}]|[{}]',s):
 t=m.group()
 if t.startswith('\\'):continue
 if t=='{':stack.append(m.start())
 elif not stack:errors.append('Unmatched closing brace at '+str(m.start()))
 else:stack.pop()
if stack:errors.append('Unclosed braces: '+str(stack))
ens=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
 action,name=m.groups()
 if action=='begin':ens.append(name)
 elif not ens or ens.pop()!=name:errors.append('Environment mismatch: '+name)
if ens:errors.append('Unclosed environments: '+str(ens))
allowed={'scanpage','figure','begin','end','draw','fill','filldraw','node','diagram','bullet','circ','vphantom','arrow','unsure','deleted','hbox','hspace','rlap','phantom','scriptsize','small','bfseries','path'}
macros=set(re.findall(r'\\([A-Za-z]+)',s))
unknown=sorted(macros-allowed)
if unknown:errors.append('Review control sequences: '+str(unknown))
r=json.loads((HERE/'report.json').read_text())
for d in r['differences']:
 if d['readers_crop'] and not (HERE/d['readers_crop']).is_file():errors.append('Missing crop '+d['readers_crop'])
 if d['H'] is not None or d['diff_H'] is not False:errors.append('H desc violation '+d['id'])
for c in r['crops']:
 if not (HERE/c['path']).is_file():errors.append('Missing crop '+c['path'])
 if c['rotation']!=0:errors.append('Unexpected rotation')
source_rows={d['C_doubt_source']['row'] for d in r['differences'] if 'C_doubt_source' in d}
if source_rows!={1,2,3,4,5}:errors.append('C doubtful section coverage incomplete')
if r['check_events']!=[]:errors.append('Unexpected mathematical event')
if '% archive sheet number: 9' not in tex:errors.append('Missing archive comment')
if not any(x['element']=='010.59' and x['transcribed']=='yes' for x in r['inventory']):errors.append('Missing archive inventory')
checks={
 'lower_left_reversed_primary':r'\unsure{\circ|\bullet}\arrow' in tex,
 'lower_middle_local_doubt':r'\unsure{\circ|\bullet}' in tex[tex.index('at (563,1026)'):],
 'lower_right_local_doubt':r'\unsure{\bullet|\circ}' in tex[tex.index('at (1075,1032)'):],
 'overdrawn_disk_uncertainty':r'\unsure{\rlap{\hbox{\begin{tikzpicture}' in tex,
 'overdrawn_disk_invisible_annotation':r'\phantom{\deleted{\hbox{\begin{tikzpicture}' in tex,
 'upper_detached_arc':'(414,240)' in tex,
 'right_upper_slant':'(1567,351)' in tex,
 'lower_left_gap_trace':'(368,743)' in tex,
 'middle_small_spot':'(1314,544)' in tex,
 'lower_pendant_stroke':'(490,911)--(489,920)' in tex,
 'right_angular_inner_slant':'(1440,1036)' in tex,
 'faint_horizontal_continuation':'(250,826)--(276,828)' in tex,
 'right_pale_patch':'(1628,797)' in tex,
 'five_OK_labels':len(re.findall(r'\{OK\}',tex))==5,
 'single_ou_label':len(re.findall(r'\{ou\}',tex))==1,
 'single_question_mark_label':len(re.findall(r'\{\?\}',tex))==1,
 'balanced_math_dollars':s.count('$')%2==0,
 'exact_crop_count':len(r['crops'])==13,
 'no_macro_definition':not re.search(r'\\(?:newcommand|renewcommand|def)\b',s)
}
for k,v in checks.items():
 if not v:errors.append('Failed consistency check '+k)
out={'validation':'structural source checks only','compiler_invoked':False,'render_validation':False,'brace_balance':not stack,'environments_remaining':ens,'control_sequences':sorted(macros),'checks':checks,'C_doubt_source_rows':sorted(source_rows),'decision_rows':len(r['differences']),'C_difference_rows':sum(x['diff_C'] for x in r['differences']),'inventory_entries':len(r['inventory']),'crop_files':len(r['crops']),'errors':errors}
(HERE/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
