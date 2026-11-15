"""Final deliverable checks requested by the transcription task (read only)."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, hashlib, json, re

work=Path(__file__).resolve().parents[1]
page_paths=sorted((work/'pages').glob('MPL_18_018-062_18_scan*.tex'))
assert len(page_paths)==45
assert [int(re.search(r'scan(\d+)',p.name)[1]) for p in page_paths]==list(range(18,63))
combined=(work/'MPL_18_018-062_transcription.tex').read_text()
assert combined.startswith('\\cotefile{18}\n\\scanpage{18}')
assert '\\documentclass' not in combined
assert combined.count('\\scanpage{')==45
hashes=[]
for line in (work/'records/frozen.sha256').read_text().splitlines():
    expected,name=line.split(None,1)
    actual=hashlib.sha256((work/name.strip()).read_bytes()).hexdigest()
    assert actual==expected,name
    hashes.append(name.strip())
assert len(hashes)==46

inventory=list(csv.DictReader((work/'MPL_18_018-062_inventory.csv').open()))
assert list(inventory[0])==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
assert len(inventory)==624
assert {int(r['scan']) for r in inventory}==set(range(18,63))
assert all(r['cote']=='18' and r['transcribed']=='yes' for r in inventory)
assert combined.count('\\unsure{')==268
assert combined.count('\\illegible{')==0
log=(work/'progress.log').read_text()
assert len(re.findall(r'^18 scan \d{3} done ',log,re.M))==45
assert len(re.findall(r'^scan \d{3} audited ',log,re.M))==45
assert log.index('transcription frozen ')<log.index('context opened ')

notes=(work/'MPL_18_018-062_notes.md').read_text()
assert 'Compilation pending.' not in notes
assert (work/'records/research_self_flagged.md').is_file()
assert '## 6.' in notes and 'self-flagged' in notes.lower()
assert '## 7. Title sheets, headings and page counts' in notes
assert '### MB03b —' in notes and '### P26 —' in notes
sections=re.split(r'(?=^### (?:C|RH|P|MB|R|SF|T)\d)',notes,flags=re.M)[1:]
identifiers=[]; possible_long=[]; missing=[]
for section in sections:
    section=re.split(r'^## (?!#)',section,maxsplit=1,flags=re.M)[0]
    ident=re.match(r'### ([A-Z]+\d+[a-z]?)',section)[1]
    identifiers.append(ident)
    for field in ('**Kind:**','**Witness:**'):
        if field not in section: missing.append((ident,field))
    if '**Context search:**' not in section and '**Context:**' not in section:
        missing.append((ident,'context search/link'))
    metadata=section.split('\n\n')[1]
    if 'own idea' in metadata.lower() and '**Confidence' not in metadata:
        missing.append((ident,'confidence'))
    body='\n\n'.join(section.split('\n\n')[2:])
    body=re.sub(r'\|[^\n]*\|','',body)
    body=re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)|\$[^$]*\$', 'MATH',body,flags=re.S)
    body=re.sub(r'`[^`]*`','CODE',body)
    # A deliberately conservative flag, not an automatic sentence verdict.
    count=len(re.findall(r'[.!?](?=\s+[A-ZÀ-ÖØ-Þ]|\s*$)',body))
    if count>4: possible_long.append((ident,count,body[:180]))
assert len(identifiers)==len(set(identifiers)), 'duplicate research identifiers'
assert not missing,missing

without_code=re.sub(r'```.*?```|`[^`\n]*`','',notes,flags=re.S)
assert without_code.count('\\(')==without_code.count('\\)'), 'inline math delimiters'
assert without_code.count('\\[')==without_code.count('\\]'), 'display math delimiters'
assert len(re.findall(r'(?<!\\)\$',without_code))%2==0, 'dollar math delimiters'
exprs=re.findall(r'\\\((.*?)\\\)|\\\[(.*?)\\\]|(?<!\\)\$([^$]+)\$',without_code,re.S)
brace_errors=[]
for match in exprs:
    expression=next(x for x in match if x)
    clean=re.sub(r'\\[{}]','',expression)
    depth=0
    for char in clean:
        if char=='{':depth+=1
        elif char=='}':depth-=1
        if depth<0:break
    if depth:brace_errors.append(expression)
assert not brace_errors,brace_errors

result={
    'pages':len(page_paths),'inventory_elements':len(inventory),
    'uncertainty_occurrences':combined.count('\\unsure{'),
    'unchanged_frozen_files':len(hashes),
    'research_observations':len(identifiers),'research_words':len(notes.split()),
    'research_groups':dict(Counter(re.match(r'[A-Z]+',i)[0] for i in identifiers)),
    'math_expressions_checked':len(exprs),'possible_long_bodies_to_review':possible_long,
}
print(json.dumps(result,ensure_ascii=False,indent=2))
