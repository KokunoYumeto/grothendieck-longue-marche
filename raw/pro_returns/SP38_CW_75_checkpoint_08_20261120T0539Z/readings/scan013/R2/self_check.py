from pathlib import Path
import re,json
base=Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R2')
r=json.loads((base/'report.json').read_text())
t=(base/'reading.tex').read_text()
m=json.loads((base/'crop_manifest.json').read_text())
# Remove comments while respecting escaped percent signs.
s='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in t.splitlines())
depth=0
for i,ch in enumerate(s):
    if ch not in '{}': continue
    j=i-1
    while j>=0 and s[j]=='\\': j-=1
    if (i-1-j)%2: continue
    depth += 1 if ch=='{' else -1
    assert depth>=0,('early closing brace',i)
assert depth==0,('brace depth',depth)
stack=[]
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
    action,env=match.groups()
    if action=='begin': stack.append(env)
    else:
        assert stack and stack[-1]==env,('environment mismatch',env,stack)
        stack.pop()
assert not stack,stack
assert len(re.findall(r'(?<!\\)\\\[',s))==len(re.findall(r'(?<!\\)\\\]',s))
assert s.startswith(r'\scanpage{13}')
assert r'\cotefile' not in s and r'\mspage' not in s
assert r'\newcommand' not in s and r'\documentclass' not in s
required={'id','place','c','h','final','evidence','confidence','kind','marked_in_H','diff_c','diff_h','bbox','crop','doubt_action','s_id','math_note'}
ids=[v['id'] for v in r['findings']]
assert len(ids)==len(set(ids))
assert all(f'C{i:02}' in ids for i in range(1,14))
assert set(r['c_doubt_map'])=={f'C{i:02}' for i in range(1,14)}
for f in r['findings']:
    assert required <= set(f),f['id']
    x0,y0,x1,y1=f['bbox']
    assert 0<=x0<x1<=1687 and 0<=y0<y1<=2362,f['id']
    if f['crop']: assert (base.parent.parent.parent/f['crop']).exists(),f['crop']
    if f['id'].startswith('C'): assert f['doubt_action'] in ('retain','resolve'),f['id']
    else: assert f['doubt_action']=='',f['id']
assert len(m['crops'])==r['crop_count']==16
assert all(v['visually_inspected'] for v in m['crops'])
assert all((base/v['path']).is_file() for v in m['crops'])
assert all(v['transcribed']=='yes' for v in r['inventory'])
for old in [r'\unsure{splitte}',r'\unsure{Rmq}',r'\unsure{\simeq|=}']:
    assert old not in t,old
assert r'\deleted{\mathbb{Z}}\mathbb{F}_3^{+}' in t
assert r'Z.\operatorname{Aut}(Z).' in t
assert t.count(r'\unsure{')==13,t.count(r'\unsure{')
assert t.count(r'\illegible{')==1
assert t.count(r'\deleted{')==5
assert len(r['unresolved'])==14
# Make the recurring A-alphabet difference explicit at both occurrences.
f=next(v for v in r['findings'] if v['id']=='C11')
f['place']='Rounded A in the parenthesis below the box, recurring in the last A3 identity'
f['c']=r'\unsure{\mathcal{A}|A}_2; \mathcal{A}_3'
f['h']=r'\mathfrak{A}_2; \mathfrak{A}_3'
f['final']=r'\unsure{\mathcal{A}|A}_2; \mathcal{A}_3'
r['s_decisions']=[]
r['self_check']['latex_balance']='Passed literal brace, display delimiter, and nested environment checks; no compilation.'
r['self_check']['report_reading_synchronization']='Checked: 13 C doubts mapped; 4 resolved and absent as doubts in reading; 9 retained (including illegible word); 5 new doubts; 14 unresolved entries total. All 5 deletions and 13 unsure calls accounted for.'
r['self_check']['workflow_compliance']='Only assigned packet, brief/conventions/preamble/notation snapshot, and three supplied scan images read. Each full image viewed once; 16 distinct crops viewed once. No OCR, recognition, external research, compilation, installation, or external saving.'
(base/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
summary={'brace_balance':'pass','environment_balance':'pass','original_C_doubts':13,'resolved_C_doubts':sum(v['doubt_action']=='resolve' for v in r['findings']),'retained_C_doubts':sum(v['doubt_action']=='retain' for v in r['findings']),'findings':len(r['findings']),'diff_C_rows':sum(v['diff_c'] for v in r['findings']),'diff_H_rows':sum(v['diff_h'] for v in r['findings']),'inventory':len(r['inventory']),'crop_count':len(m['crops']),'unresolved':len(r['unresolved']),'unsure_calls':t.count(r'\unsure{'),'deleted_calls':t.count(r'\deleted{')}
(base/'self_check.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
