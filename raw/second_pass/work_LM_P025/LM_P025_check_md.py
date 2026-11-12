"""LM_P025: report table rows whose unescaped pipe count differs from the header's."""
import re
import sys

PIPE = re.compile(r"(?<!\\)\|")
expected = None
for i, line in enumerate(open(sys.argv[1], encoding="utf-8"), 1):
    if not line.startswith("|"):
        expected = None
        continue
    n = len(PIPE.findall(line))
    if expected is None:
        expected = n
    elif n != expected:
        print(f"line {i}: {n} pipes, expected {expected}")
print("checked")
