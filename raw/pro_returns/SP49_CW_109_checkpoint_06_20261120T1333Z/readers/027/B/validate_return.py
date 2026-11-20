from pathlib import Path
import json,re,collections
base=Path('work/readers/027/B')
r=json.loads((base/'report.json').read_text())
s=(base/'reading.tex').read_text()
c=Path('work/inputs/027/C.tex').read_text()
# Static balance only; no compilation or image reinspection.
t=re.sub(r'(?<!\\)%.*','',s)
bal=0
for i,ch in enumerate(t):
    if ch in '{}':
        j=i-1
        while j>=0 and t[j]=='\\':j-=1
        if (i-1-j)%2:continue
        bal+=1 if ch=='{' else -1
        assert bal>=0,('premature closing brace',i)
assert bal==0,bal
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
    op,e=m.groups()
    if op=='begin':stack.append(e)
    else:
        assert stack and stack[-1]==e,(op,e,stack)
        stack.pop()
assert not stack,stack
assert len(re.findall(r'(?<!\\)\$',t))%2==0
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for x in r['changes']:
    assert x['kind'] in allowed,x['id']
    assert x['h'] is None and x['diff_h'] is False and x['marked_in_H'] is False,x['id']
    assert not x['c'] or x['c'] in c,('nonliteral C',x['id'],x['c'])
    if x.get('c_additional_literal'): assert x['c_additional_literal'] in c,x['id']
    assert x['crop'] or (x['source'] and len(x['bbox'])==4),x['id']
    if x['crop']:assert Path(x['crop']).is_file(),x['id']
    assert Path(x['source']).is_file(),x['id']
for x in r['c_doubts']:
    assert x['crop'] or (x['source'] and len(x['bbox'])==4),x['place']
    if x['crop']:assert Path(x['crop']).is_file(),x['place']
    assert Path(x['source']).is_file(),x['place']
assert len([x for x in r['c_doubts'] if x.get('decision_type')=='explicit C doubt'])==21
assert len({x['id'] for x in r['changes']})==len(r['changes'])
assert [x['element'] for x in r['inventory']]==[f'{i:02}' for i in range(1,len(r['inventory'])+1)]
assert all(x['sheet_kind']=='list' for x in r['inventory'])
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in r['inventory'])
assert all(x['transcribed']=='yes' for x in r['inventory'])
log=[json.loads(x) for x in (base/'crops/crops.jsonl').read_text().splitlines()]
assert len(log)==27 and len({x['output'] for x in log})==27
views=json.loads((base/'crop_views.json').read_text())
assert views['count']==27
assert set(views['displayed_once'])=={x['output'] for x in log}
assert "``s}''" in s
assert "}'' and" not in s
assert s.count("``commutes \\uline{with}''")==1
assert 'scxxviim' not in s and 'scxxviin' not in s
assert r"\deleted{would'nt}" in s
assert r"\unsure{''|'}" in s
assert 'developing' in s and 'enveloping' in s
assert r'\compile' not in s
out={'valid_json':True,'static_braces_balanced':True,'static_environments_balanced':True,'inline_math_delimiters_even':True,'all_C_comparison_fields_literal':True,'all_required_image_locators_present':True,'all_21_explicit_C_doubts_accounted_for':True,'changes':len(r['changes']),'context_and_notation_confirmations':sum(x.get('decision_type')!='explicit C doubt' for x in r['c_doubts']),'resolved_explicit_C_doubts':sum(x.get('decision_type')=='explicit C doubt' and x['resolved'] for x in r['c_doubts']),'remaining_doubt_loci':len(r['remaining_doubts']),'inventory_rows':len(r['inventory']),'inventory_kinds':dict(collections.Counter(x['kind'] for x in r['inventory'])),'enhanced_crops_generated_once_each':len(log),'enhanced_crops_displayed_once_each':views['count'],'H_comparisons':0,'mathematical_check_events':len(r['math_checks']),'no_compilation_attempted':True,'literal_diff_review':'Reviewed complete C-to-reading diff. Corrected an output-only missing p.304 closer and duplicate p.326 closer before final validation.'}
(base/'static_validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
