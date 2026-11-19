import json,re
from pathlib import Path
out=Path('/workspace/scratch/17347c1714f0/out/readers/scan004/R1')
tex=(out/'reading.tex').read_text(encoding='utf-8')
report=json.loads((out/'report.json').read_text(encoding='utf-8'))
body=re.sub(r'(?<!\\)%[^\n]*','',tex)
brace_depth=0
for match in re.finditer(r'(?<!\\)[{}]',body):
    brace_depth += 1 if match.group()=='{' else -1
    assert brace_depth>=0, ('unmatched closing brace',match.start())
assert brace_depth==0, ('brace balance',brace_depth)
stack=[]
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}',body):
    if match[1]=='begin': stack.append(match[2])
    else:
        assert stack and stack[-1]==match[2], ('environment mismatch',match[2],stack)
        stack.pop()
assert not stack, stack
assert len(re.findall(r'(?<!\\)\$',body))%2==0
assert len(re.findall(r'(?<!\\)\\\[',body))==len(re.findall(r'(?<!\\)\\\]',body))
assert len(re.findall(r'(?<!\\)\\\(',body))==len(re.findall(r'(?<!\\)\\\)',body))
assert body.count(r'\begingroup')==body.count(r'\endgroup')
for finding in report['findings']:
    assert finding['reading'] in tex, finding['id']
    assert finding['h'] is None and finding['diff_h'] is False
assert r'\scanpage{4}' in tex
assert r'\cotefile' not in tex
assert r'\mspage' not in tex
assert '% archive sheet number: 3' in tex
print('PASS: UTF-8 JSON parses; TeX braces, environments, group markers and math delimiters balance; each final finding occurs exactly in reading.tex; H absent is represented without omission rows; scan and archive markers agree. No compilation performed.')
