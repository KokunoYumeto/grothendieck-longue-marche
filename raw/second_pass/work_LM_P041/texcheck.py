import re
import sys

path = sys.argv[1]
s = open(path, encoding='utf-8').read()
# brace balance, ignoring escaped braces
t = s.replace('\\{', '').replace('\\}', '')
depth = 0
line = 1
problems = []
for ch in t:
    if ch == '\n':
        line += 1
    elif ch == '{':
        depth += 1
    elif ch == '}':
        depth -= 1
        if depth < 0:
            problems.append('negative depth at line %d' % line)
            depth = 0
print('final brace depth:', depth)
print('problems:', problems[:5])
print('display opens \\[ :', s.count('\\['), ' closes \\] :', s.count('\\]'))
print('scanpages:', re.findall(r'\\scanpage\{(\d+)\}', s))
print('mspages:', re.findall(r'\\mspage\{(\d+)\}', s))
for m in ['\\unsure{', '\\deleted{', '\\inserted{', '\\margin{', '\\uline{', '\\illegible{']:
    print(m, s.count(m))
# unsure arguments with an empty alternative
for m in re.finditer(r'\\unsure\{([^{}]*)\}', s):
    a = m.group(1)
    if '|' in a and any(x.strip() == '' for x in a.split('|')):
        print('empty alternative:', a)
