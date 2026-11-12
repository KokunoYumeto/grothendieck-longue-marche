import re
import sys

s = open(sys.argv[1], encoding="utf-8").read()
d, neg, i = 0, [], 0
while i < len(s):
    c = s[i]
    if c == "\\":
        i += 2
        continue
    if c == "%":
        j = s.find("\n", i)
        i = len(s) if j < 0 else j
        continue
    if c == "{":
        d += 1
    elif c == "}":
        d -= 1
        if d < 0:
            neg.append(i)
    i += 1
print("brace depth at end:", d, "negative at:", neg[:5])
print("\\[ :", s.count("\\["), " \\] :", s.count("\\]"))
n = len(re.findall(r"(?<!\\)\$", s))
print("unescaped $:", n, "even" if n % 2 == 0 else "ODD")
print("scanpages:", re.findall(r"\\scanpage\{(\d+)\}", s))
print("control chars:", [hex(ord(ch)) for ch in s if ord(ch) < 32 and ch not in "\n\r\t"][:5])
for k, line in enumerate(s.splitlines(), 1):
    if len(re.findall(r"(?<!\\)\$", line)) % 2:
        print("odd $ on line", k, ":", line[:90])
