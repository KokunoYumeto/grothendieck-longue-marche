"""Small structural scanner; no image recognition or transcription generation."""
import re

def escaped(text,i):
    j=i-1
    while j>=0 and text[j]=='\\':j-=1
    return (i-1-j)%2==1

def macro_arguments(text,name):
    out=[]
    for hit in re.finditer(r'\\'+name+r'\{',text):
        if escaped(text,hit.start()):continue
        i=hit.end();a=i;depth=1
        while i<len(text) and depth:
            if not escaped(text,i):
                if text[i]=='{':depth+=1
                elif text[i]=='}':depth-=1
            i+=1
        if depth:raise ValueError(f'Unclosed {name} at {hit.start()}')
        out.append((name,hit.start(),i,text[a:i-1]))
    return out

def split_alternative(s):
    depth=0
    for i,ch in enumerate(s):
        if escaped(s,i):continue
        if ch=='{':depth+=1
        elif ch=='}':depth-=1
        elif ch=='|' and depth==0:return s[:i],s[i+1:]
    return s,'—'
