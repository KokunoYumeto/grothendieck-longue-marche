#!/usr/bin/env python3
"""One-time Markdown delimiter repair; never accesses the transcription."""
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / 'records/research_albanese.md'
source = path.read_text()
parts = re.split(r'(`[^`]*`)', source)
count = 0

def repair(text):
    global count
    text = text.replace('\\(', '(').replace('\\)', ')')
    out = []
    i = 0
    while i < len(text):
        if text[i] != '(':
            out.append(text[i]); i += 1; continue
        j = i + 1
        level = 1
        while j < len(text) and level:
            if text[j] == '(': level += 1
            if text[j] == ')': level -= 1
            j += 1
        if level:
            out.append(text[i]); i += 1; continue
        content = text[i+1:j-1]
        math = ('\\' in content or re.fullmatch(r"[A-Za-z](?:['*]|\^\d+)?", content)
                or re.fullmatch(r'[A-Za-z0-9]+(?:[=+*/^_-][A-Za-z0-9,-]+)+', content))
        if math and '\n\n' not in content:
            out.append('$' + content + '$'); count += 1
        else:
            out.append(text[i:j])
        i = j
    return ''.join(out)

for i in range(0, len(parts), 2):
    parts[i] = repair(parts[i])
result = ''.join(parts)
path.write_text(result)
print(f'Restored {count} math delimiters in {path}.')
