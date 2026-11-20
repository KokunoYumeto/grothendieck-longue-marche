"""Syntax and deliverable integrity checks, never a substitute for visual reading."""
from pathlib import Path
import re,json,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
EXPECTED=[2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18]
EVENT_TYPES={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
KINDS={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
def strip_comments(s):return '\n'.join(re.split(r'(?<!\\)%',l)[0] for l in s.splitlines())
def check_tex(p):
    s=strip_comments(p.read_text());errors=[];stack=[]
    for m in re.finditer(r'\\[{}%$]|[{}]',s):
        v=m.group()
        if v=='{':stack.append(m.start())
        elif v=='}':
            if not stack:errors.append('extra closing brace')
            else:stack.pop()
    if stack:errors.append(f'{len(stack)} unclosed braces')
    if len(re.findall(r'(?<!\\)\$',s))%2:errors.append('odd dollar count')
    if len(re.findall(r'\\\[',s))!=len(re.findall(r'\\\]',s)):errors.append('unbalanced display delimiters')
    if len(re.findall(r'\\\(',s))!=len(re.findall(r'\\\)',s)):errors.append('unbalanced inline delimiters')
    env=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        action,name=m.groups()
        if action=='begin':env.append(name)
        elif not env or env.pop()!=name:errors.append(f'environment mismatch {name}')
    if env:errors.append('unclosed environments '+repr(env))
    return errors
def main():
    pages=sorted((ROOT/'pages').glob('*.tex'));errors=[]
    scans=[]
    for p in pages:
        scans.append(int(re.search(r'scan(\d+)',p.name).group(1)))
        errors.extend(p.name+': '+x for x in check_tex(p))
    combined=ROOT/'SP47_CW_103_transcription.tex'
    if combined.exists():
        errors.extend(combined.name+': '+x for x in check_tex(combined))
        expected='\n\n'.join(p.read_text().rstrip() for p in pages)+'\n'
        if combined.read_text()!=expected:errors.append('combined text differs from page concatenation')
        if combined.read_text().count('\\cotefile{103}')!=1:errors.append('cotefile count is not one')
    for dpath in sorted((ROOT/'decisions').glob('scan*.json')):
        d=json.loads(dpath.read_text());n=d['scan']
        for c in d['changes']:
            if c.get('confidence') not in {'high','medium','low'}:errors.append(f'{n}: invalid confidence at {c["place"]}')
            if c.get('kind') not in KINDS:errors.append(f'{n}: invalid collation kind at {c["place"]}')
            if c.get('marked_in_H') not in {'yes','no'}:errors.append(f'{n}: invalid H doubt flag at {c["place"]}')
            if c.get('consequential') and not isinstance(c['consequential'],str):errors.append(f'{n}: consequential explanation is not text')
            if c.get('readers') and set(c['readers'])!={'A','B','C'}:errors.append(f'{n}: disagreement lacks all three readings at {c["place"]}')
            if (c['against_c'] or c['against_h']) and not c.get('crops'):errors.append(f'{n}: no main adjudication crop for {c["place"]}')
            for cp in c.get('crops',[]):
                if not (ROOT/cp).exists():errors.append(f'{n}: missing crop {cp}')
        for i in d['inventory']:
            if i['transcribed']!='yes':errors.append(f'{n}: inventory not transcribed {i["element"]}')
        for e in d.get('check_events',[]):
            if e.get('type') not in EVENT_TYPES:errors.append(f'{n}: invalid check-event type')
            if not isinstance(e.get('outcome'),str):errors.append(f'{n}: check-event outcome is not text')
        for reader in 'ABC':
            rd=ROOT/'readers'/f'scan{n:03}'/reader
            if not (rd/'reading.tex').exists() or not (rd/'report.json').exists():errors.append(f'{n}: missing reader {reader}')
    result={'pages':scans,'missing_scans':[n for n in EXPECTED if n not in scans],'syntax_and_integrity_errors':errors,
        'marks':{m:combined.read_text().count('\\'+m+'{') if combined.exists() else 0 for m in ['unsure','illegible','deleted','inserted','diagram','figure']}}
    (ROOT/'records/validation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
    return len(errors)
if __name__=='__main__':raise SystemExit(bool(main()))
