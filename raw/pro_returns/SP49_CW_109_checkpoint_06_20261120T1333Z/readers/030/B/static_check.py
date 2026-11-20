from pathlib import Path
import json,re,difflib
from PIL import Image
p=Path('work/readers/030/B')
reading=(p/'reading.tex').read_text()
report=json.loads((p/'report.json').read_text())
c=Path('work/inputs/030/C.tex').read_text()
body='\n'.join(line.split('%',1)[0] for line in reading.splitlines())
assert reading.startswith('\\cotefile{109}\n\\scanpage{30}\n')
assert reading.count('\\cotefile{')==1 and reading.count('\\scanpage{')==1
level=0
for i,ch in enumerate(body):
    if ch in '{}':
        n=0;k=i-1
        while k>=0 and body[k]=='\\': n+=1;k-=1
        if n%2: continue
        level += 1 if ch=='{' else -1
        assert level>=0,('unmatched close',i)
assert level==0
assert len(re.findall(r'(?<!\\)\$',body))%2==0
begins=re.findall(r'\\begin\{([^}]+)\}',body)
ends=re.findall(r'\\end\{([^}]+)\}',body)
assert begins==ends==[]
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',body)))
allowed={'cotefile','scanpage','quad','ldots','unsure','S','uuline','uline','deleted','tikz','node','fill','draw','cong','normalmarginpar','margin'}
assert set(commands)<=allowed,(set(commands)-allowed)
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
for row in report['changes']:
    assert row['kind'] in allowed_kinds,row['kind']
    assert row['c']=='' or row['c'] in c,row['id']
    assert row['reading'] in reading,row['id']
    assert row['h'] is None and row['diff_h'] is False
    assert row['diff_c'] is True and row['marked_in_H'] is False
    assert row['confidence'] in {'high','medium','low'}
for group in ['changes','c_doubts','remaining_doubts']:
    for row in report[group]:
        assert Path(row['source']).exists(),row['place']
        assert Path(row['source']).name in {'H109-03_109_scan030.jpg','H109-03_109_scan030_a.jpg','H109-03_109_scan030_b.jpg'}
        box=row['bbox']; assert len(box)==4
        width,height=Image.open(row['source']).size
        assert 0<=box[0]<box[2]<=width and 0<=box[1]<box[3]<=height,(row['place'],box)
        if row['crop']: assert Path(row['crop']).exists()
c_unsure=re.findall(r'\\unsure\{[^{}]*\}',c)
doubt_c='\n'.join(row['c'] for row in report['c_doubts'])
assert len(c_unsure)==6
assert all(mark in doubt_c for mark in c_unsure)
assert any('corner' in row['place'] for row in report['c_doubts'])
assert body.count('\\unsure{')==8
assert len(report['remaining_doubts'])==body.count('\\unsure{')+1
assert body.count('\\deleted{')==3
assert body.count('\\uline{')==1 and body.count('\\uuline{')==1
assert len(report['inventory'])==72
assert len({r['element'] for r in report['inventory']})==72
assert all(r['sheet_kind']=='list' for r in report['inventory'])
assert all(r['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for r in report['inventory'])
frozen=json.loads((p/'unresolved_frozen.json').read_text())
log=[json.loads(x) for x in (p/'crops/crops.jsonl').read_text().splitlines()]
assert len(log)==len(frozen['loci'])==25
assert len({r['output'] for r in log})==25
for planned,actual in zip(frozen['loci'],log):
    assert planned['output']==actual['output'] and planned['bbox']==actual['box']
    assert planned['source']==actual['source'] and actual['width']==2400
    assert Image.open(actual['output']).size[0]==2400
assert report['crop_workflow']['viewed_crops']==[r['output'] for r in frozen['loci']]
assert report['math_checks']==[]
assert report['coverage']['changes']==len(report['changes'])==15
assert report['coverage']['c_and_context_decisions']==len(report['c_doubts'])==28
static={'json_valid':True,'tex_braces_balanced':True,'math_delimiters_even':True,'environments_checked':'none present','macros_checked':commands,'literal_changes_checked_against_C':15,'change_readings_present_in_reading_tex':15,'original_C_uncertainty_macros_accounted_for':6,'archive_corner_doubt_accounted_for':True,'remaining_body_uncertainty_macros':8,'archive_remaining_doubt':1,'crop_log_entries':25,'all_crop_files_2400_pixels_wide':True,'viewed_crop_list_matches_frozen_list':True,'source_bboxes_within_assigned_images':True,'inventory_rows':72,'H_comparison_rows':0,'mathematical_check_events':0,'compilation_attempted':False,'verification_scope':'Static text/JSON/TeX and crop-manifest checks only; no image reopened during these checks.'}
report['static_checks']=static
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(p/'static_checks.json').write_text(json.dumps(static,ensure_ascii=False,indent=2)+'\n')
(p/'literal_diff.patch').write_text(''.join(difflib.unified_diff(c.splitlines(True),reading.splitlines(True),fromfile='work/inputs/030/C.tex',tofile='work/readers/030/B/reading.tex')))
print(json.dumps(static,indent=2))
