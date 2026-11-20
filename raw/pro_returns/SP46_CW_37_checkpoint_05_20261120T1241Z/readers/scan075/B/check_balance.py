from pathlib import Path
import json
import re

root=Path(__file__).parent
text=(root/'reading.tex').read_text()
clean='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in text.splitlines())
stack=[]
for n,ch in enumerate(clean):
    if ch not in '{}':
        continue
    slash=0
    p=n-1
    while p>=0 and clean[p]=='\\':
        slash+=1
        p-=1
    if slash%2:
        continue
    if ch=='{':
        stack.append(n)
    else:
        assert stack, f'Unmatched closing brace at {n}'
        stack.pop()
assert not stack, f'Unclosed braces: {stack}'
env=[]
for hit in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    kind,name=hit.groups()
    if kind=='begin':
        env.append(name)
    else:
        assert env and env.pop()==name, f'Environment mismatch: {name}'
assert not env, env
for opening,closing in [(r'\(',r'\)'),(r'\[',r'\]'),(r'\begingroup',r'\endgroup')]:
    assert clean.count(opening)==clean.count(closing),(opening,closing)
report=json.loads((root/'report.json').read_text())
assert report['scan']==75 and report['reader']=='B'
assert len(report['image_views'])==3
assert len(report['crops'])==7
assert len(report['decisions'])==7
assert sum(row['c_doubt'] for row in report['decisions'])==4
assert all(row['h_reading'] is None and row['diff_h'] is False for row in report['decisions'])
assert all(len(row['bbox'])==4 and 0<=row['bbox'][0]<row['bbox'][2]<=1680 and 0<=row['bbox'][1]<row['bbox'][3]<=2001 for row in report['decisions'])
assert all(Path(row['file']).exists() for row in report['crops'])
assert all(row['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion'] for row in report['inventory'])
assert clean.count(r'\arrow[')==9
assert clean.count(r'\deleted{')==2
assert clean.startswith(r'\scanpage{75}')
assert r'\cotefile{' not in clean and r'\mspage{' not in clean
summary={
    'brace_balance':'pass',
    'environment_balance':'pass',
    'math_delimiter_counts':'pass',
    'json_and_required_fields':'pass',
    'decision_count':len(report['decisions']),
    'c_doubt_count':sum(row['c_doubt'] for row in report['decisions']),
    'unresolved_decisions':sum(row['unresolved'] for row in report['decisions']),
    'diagram_arrows':clean.count(r'\arrow['),
    'deletions':clean.count(r'\deleted{'),
    'compilation':'not run',
}
(root/'balance_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
