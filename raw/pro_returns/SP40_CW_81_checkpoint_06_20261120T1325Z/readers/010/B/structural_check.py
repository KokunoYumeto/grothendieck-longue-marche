from pathlib import Path
import json
import re
from datetime import datetime,timezone
OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/010/B')
s=(OUT/'reading.tex').read_text()
r=json.loads((OUT/'report.json').read_text())
clean=re.sub(r'(?m)(?<!\\)%.*$','',s)
brace_stack=[]
for m in re.finditer(r'\\[{}]|[{}]',clean):
 t=m.group()
 if t.startswith('\\'): continue
 if t=='{': brace_stack.append(m.start())
 else:
  assert brace_stack, f'excess closing brace at {m.start()}'
  brace_stack.pop()
assert not brace_stack, f'unclosed braces: {brace_stack}'
for left,right in [('(',')'),('[',']')]:
 assert clean.count(left)==clean.count(right),(left,clean.count(left),clean.count(right))
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 action,name=m.groups()
 if action=='begin': envs.append(name)
 else:
  assert envs and envs[-1]==name, ('environment',name,envs)
  envs.pop()
assert not envs
allowed={'scanpage','figure','begin','end','draw','fill','node','path','scriptsize','small','bfseries','diagram','bullet','circ','vphantom','arrow','unsure','deleted','hbox','hspace','rlap','phantom'}
macros=set(re.findall(r'\\([A-Za-z]+)',clean))
assert macros<=allowed, sorted(macros-allowed)
assert s.count(r'\scanpage{10}')==1
assert '% archive sheet number: 9' in s
assert r'\mspage' not in s and r'\cotefile' not in s
assert s.count('{OK}')==5 and s.count('{ou}')==1 and s.count('{?}')==1
assert s.count(r'\unsure{')==5
assert r'\unsure{\circ|\bullet}' in s
assert s.count(r'\unsure{\bullet|\circ}')==3
assert r'\unsure{\rlap{' in s and r'\phantom{\deleted{' in s
assert not any(x in clean for x in [r'\newcommand',r'\renewcommand',r'\def',r'\includegraphics'])
assert all(d['H'] is None and d['diff_H'] is False for d in r['differences'])
source_doubts=[d for d in r['differences'] if d['C_doubt_status']]
assert len(source_doubts)==5
assert sorted(d['C_doubt_source_row'] for d in source_doubts)==[1,2,3,4,5]
assert all(d['C_doubt_status']=='retained' for d in source_doubts)
assert r['check_events']==[]
assert len(r['inventory'])==70
assert any(x['first_words_or_objects'].startswith('archive numeral 9') and x['transcribed']=='yes' for x in r['inventory'])
assert all(x['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion'] for x in r['inventory'])
assert all(x['transcribed']=='yes' for x in r['inventory'])
assert len(r['crops'])==13
for c in r['crops']:
 assert (OUT/c['path']).exists()
 x0,y0,x1,y1=c['bbox']['coordinates']
 assert 0<=x0<x1<=1680 and 0<=y0<y1<=1208
for d in r['differences']:
 if d['readers_crop']: assert (OUT/d['readers_crop']).exists()
 for p in d.get('additional_crops',[]): assert (OUT/p).exists()
for d in r['doubts']:
 assert (OUT/d['crop']).exists()
 for p in d.get('additional_crops',[]): assert (OUT/p).exists()
# Anchors for each additional local drawing agree with its report entry.
anchors={'B08':'(1153,251)','B09':'(1314,543)','B10':'(1340,332)', 'B11':'(491,912)--(490,920)', 'B12':'(490,861)', 'B13':'(1018,26)', 'B14':'(1037,29)', 'B15':'(1567,352)', 'B16':'(416,241)', 'B17':'(784,42)', 'B18':'(369,743)', 'B19':'(252,825)', 'B20':'(1436,1043)', 'B21':'(1568,908)', 'B22':'(1566,921)', 'B23':'(1550,893)', 'B24':'(1603,930)', 'B25':'(1435,1084)'}
assert all(a in s for a in anchors.values())
assert all(k in [d['id'] for d in r['differences']] for k in anchors)
end=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
checks={
 'checked_utc':end,'brace_balance':True,'environment_nesting':True,'bracket_and_parenthesis_counts':True,'allowed_macro_names':sorted(macros),'page_marker_and_archive_comment':True,'five_OK_one_ou_one_question_mark':True,'five_explicit_unsure_wrappers':True,'all_H_fields_null_and_false':True,'five_source_C_doubts_classified_once':True,'complete_inventory_items':70,'crop_files_verified':13,'reading_report_anchor_consistency':True,'compiler_invoked':False,'mathematical_checks_performed':False,
 'limits':'These are source checks only. They establish no compiled layout or rendering result.'}
(OUT/'structural_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
r['end_utc']=end
r['notes']['source_checks']='Direct structural checks passed: brace balance, environment nesting, bracket/parenthesis counts, allowed macro names, page marker/archive comment, five OK labels/one ou/one question mark, all five source C-doubt mappings, 13 crop references, and reading/report anchors. No compilation or rendering validation was attempted.'
(OUT/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
md=(OUT/'reading.md').read_text().replace('End UTC: to be filled after structural verification.','End UTC: '+end)
md+='\nStructural verification completed: braces, environments, delimiters, allowed macro names, page/archive markers, label counts, all five source C-doubt mappings, all thirteen crop references, and drawing/report anchors passed. No compilation or render validation is claimed.\n'
(OUT/'reading.md').write_text(md)
print(json.dumps({'end_utc':end,'difference_rows':len(r['differences']),'diff_C_true':sum(d['diff_C'] for d in r['differences']),'source_C_doubts':len(source_doubts),'inventory_items':len(r['inventory']),'crops':len(r['crops']),'structural_checks':'passed','compiler_invoked':False},ensure_ascii=False))
