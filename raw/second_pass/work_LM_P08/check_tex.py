import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
BS = chr(92)
d = 0
neg = []
for i, ch in enumerate(s):
    prev = s[i-1] if i else ''
    if ch == '{' and prev != BS:
        d += 1
    elif ch == '}' and prev != BS:
        d -= 1
        if d < 0:
            neg.append(i)
            d = 0
print('brace depth at end', d, 'negative at', neg[:3])
print('display open/close', s.count(BS + '['), s.count(BS + ']'))
print('unescaped dollars even:', len(re.findall(r'(?<!\\)\$', s)) % 2 == 0)
print('scanpages', re.findall(r'scanpage\{(\d+)\}', s))
print('control chars', [hex(ord(c)) for c in set(s) if ord(c) < 32 and c != '\n'])
for line_no, line in enumerate(s.split('\n'), 1):
    if len(re.findall(r'(?<!\\)\$', line)) % 2:
        print('odd $ on line', line_no)
