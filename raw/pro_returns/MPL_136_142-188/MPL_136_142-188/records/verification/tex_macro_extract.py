"""Lossless, non-expanding extraction of named one-argument TeX macros."""
from pathlib import Path
import re
from collections import Counter

TRACKED={'unsure','illegible','deleted','inserted','margin','diagram','figure','uline','uuline','mspage','scanpage','cotefile'}

def escaped(text,pos):
    j=pos-1
    while j>=0 and text[j]=='\\':j-=1
    return (pos-j-1)%2==1

def mask_comments(text):
    chars=list(text);i=0
    while i<len(text):
        if text[i]=='%' and not escaped(text,i):
            end=text.find('\n',i)
            if end<0:end=len(text)
            chars[i:end]=' '*(end-i);i=end
        else:i+=1
    return ''.join(chars)

def argument_span(masked,pos):
    while pos<len(masked) and masked[pos].isspace():pos+=1
    if pos>=len(masked) or masked[pos]!='{':return None
    depth=1;end=pos+1
    while end<len(masked):
        if not escaped(masked,end):
            if masked[end]=='{':depth+=1
            elif masked[end]=='}':
                depth-=1
                if depth==0:return pos,end
        end+=1
    return None

def top_level_pipes(argument):
    """Return split candidates, preserving every original character.

    No interpretation is assigned to a literal pipe; the caller retains the
    complete raw argument and may review mathematical vertical bars manually.
    Braced or escaped pipes are not split candidates.
    """
    masked=mask_comments(argument);depth=0;positions=[]
    for pos,char in enumerate(masked):
        if escaped(masked,pos):continue
        if char=='{':depth+=1
        elif char=='}':depth-=1
        elif char=='|' and depth==0:positions.append(pos)
    parts=[];start=0
    for pos in positions:
        parts.append(argument[start:pos]);start=pos+1
    parts.append(argument[start:])
    assert '|'.join(parts)==argument
    return positions,parts

def extract_file(path,names=TRACKED):
    path=Path(path);raw=path.read_text(encoding='utf-8');masked=mask_comments(raw)
    scan=int(re.search(r'scan(\d+)\.tex$',path.name)[1]);counts=Counter();records=[];errors=[]
    for token in re.finditer(r'\\([A-Za-z@]+|.)',masked):
        macro=token[1]
        if macro not in names:continue
        line=masked.count('\n',0,token.start())+1
        span=argument_span(masked,token.end())
        if span is None:
            errors.append({'scan':scan,'line':line,'macro':macro,'problem':'missing or unbalanced braced argument'})
            continue
        a,b=span;counts[macro]+=1
        records.append({'id':f'{scan}:{macro}:{counts[macro]}','cote':'136','scan':scan,'filename':path.name,'macro':macro,'occurrence':counts[macro],
                        'line':line,'end_line':masked.count('\n',0,b)+1,'start':token.start(),'arg_start':a,'end':b,
                        'argument':raw[a+1:b],'source':raw[token.start():b+1]})
    for record in records:
        record['container_ids']=[outer['id'] for outer in records if outer['start']<record['start']<outer['end']]
        record['container_macros']=[outer['macro'] for outer in records if outer['start']<record['start']<outer['end']]
    return records,errors
