"""Encode matrix separators robustly inside the required diagram macro."""
from pathlib import Path
from datetime import datetime, timezone
import re
ROOT=Path(__file__).resolve().parents[1]
count=0
for p in sorted((ROOT/'pages').glob('*.tex')):
    s=p.read_text()
    def fix(m):
        global count
        options=m[1] or ''
        if 'ampersand replacement' in options:return m[0]
        body=m[2]; stack=[];out=[];start=0
        for t in re.finditer(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|(?<!\\)&',body):
            out.append(body[start:t.start()])
            if t[1]:stack.append(t[1]);out.append(t[0])
            elif t[2]:
                if not stack or stack.pop()!=t[2]:raise ValueError((p.name,t[0]))
                out.append(t[0])
            else:out.append('&' if stack else r'\&')
            start=t.end()
        out.append(body[start:])
        opts='[ampersand replacement=\\&'+(','+options[1:-1] if options else '')+']'
        count+=1
        return r'\begin{tikzcd}'+opts+''.join(out)+r'\end{tikzcd}'
    s=re.sub(r'\\begin\{tikzcd\}(\[[^\]]*\])?([\s\S]*?)\\end\{tikzcd\}',fix,s)
    p.write_text(s)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:f.write(f'pre-freeze TeX encoding: {count} tikz-cd matrices given explicit ampersand replacement {stamp}\n')
print(count,'TikZ-CD environments encoded')
