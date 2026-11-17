#!/usr/bin/env python3
"""Perform a distinct supplied-context search for every final individual note."""
import re, subprocess, json
from pathlib import Path
base=Path(__file__).resolve().parents[1]
context=base.parent/'context'
src=(base/'MPL_64_078-115_notes.md').read_text()
entries=[]
for match in re.finditer(r'^### ([^\n]+)\n(.*?)(?=^### |^## |\Z)',src,re.M|re.S):
    title,body=match.groups()
    search=re.search(r'\*\*Search:\*\*\s*([^;\n]+);',body)
    if not search:continue
    terms=re.findall(r'`([^`]+)`',search.group(1))
    if not terms:raise RuntimeError(f'No literal search terms for {title}')
    entries.append((title.split(' — ')[0],terms))
if not any(key=='P01' for key,_ in entries):
    entries.append(('P01',['Descriptions explicites','Weierstrass','pages 100']))
records=[]; report=[]
for ident,terms in entries:
    cmd=['rg','-n','-i','-F']
    for term in terms:cmd+=['-e',term]
    cmd+=[str(context)]
    p=subprocess.run(cmd,text=True,capture_output=True)
    if p.returncode not in (0,1):raise RuntimeError(p.stderr)
    lines=p.stdout.splitlines()
    relative=[x.replace(str(context)+'/', 'context/',1) for x in lines]
    records.append({'note_id':ident,'terms':terms,'matching_lines':len(lines),
                    'excerpt_limit':30,'first_matches':relative[:30]})
    report.append(f'## {ident}\nTerms: '+', '.join(terms)+f'\nMatching lines: {len(lines)}\nShowing at most30 matches; selected relevant passages are cited in the main note.\n'+'\n'.join(relative[:30])+'\n')
(base/'records'/'final_note_context_searches.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(base/'records'/'final_note_context_searches.txt').write_text('\n'.join(report))
print(json.dumps({'individual_notes_searched':len(entries),'zero_hit_notes':[r['note_id'] for r in records if r['matching_lines']==0]},indent=2))
