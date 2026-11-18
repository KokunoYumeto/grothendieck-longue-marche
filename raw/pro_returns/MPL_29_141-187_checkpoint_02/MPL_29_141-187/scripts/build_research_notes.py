#!/usr/bin/env python3
"""Integrate reviewed research drafts; never read or write a transcription."""
from pathlib import Path
import re, csv, json

root=Path(__file__).resolve().parents[1]
draft=root/'research_drafts'
mapping={
'RF01':'N142.1','RF02':'N143.1','RF03':'N143.2','RF04':'N143.3',
'RF05':'N145.1','RF06':'N144.1','RF07a':'N149.1','RF07b':'N151.1',
'RF08':'N152.1','RF09':'N153.1','RF10':'N156.1','RF11':'N157.1',
'RF12':'N155.1','RF13':'N158.1','RF14':'N159.1','RF15':'N160.1',
'RF16':'N187.1','RF17':'N187.2','RF18':'N187.3',
'IC01':'N162.1','IC02':'N162.2','IC03':'N163.1','IC04':'N162.3',
'IC05':'N165.1','IC06':'N167.1','IC07':'N168.1','IC08':'N169.1',
'IC09':'N169.2','IC10':'N170.1','IC11':'N171.1','IC12':'N171.2',
'IC13':'N171.3','IC14':'N171.4','IC15':'N172.1','IC16':'N172.2','IC17':'N172.3'}
def remap(s):
    for a,b in sorted(mapping.items(),key=lambda x:-len(x[0])):
        s=re.sub(r'\b'+a+r'\b',b,s)
    return s
entries=[]
for filename,prefix in [('research_finite_notes.md','RF'),('infinite_coverings.md','IC')]:
    text=(draft/filename).read_text()
    for m in re.finditer(r'^### ('+prefix+r'\d+[a-z]?) — ([^\n]+)\n([\s\S]*?)(?=^### |^## |\Z)',text,re.M):
        nid=mapping[m[1]]
        body=remap(m[3].strip())
        body=re.sub(r' \*\*Search:\*\* Q\d+\.', '', body)
        body=body.replace('`context/','`')
        entries.append((nid,m[2],body))
text=(draft/'root_late_notes.md').read_text()
for m in re.finditer(r'^## (N\d+\.\d+) — ([^\n]+)\n([\s\S]*?)(?=^## |\Z)',text,re.M):
    entries.append((m[1],m[2],m[3].strip()))
header=(draft/'notes_frontmatter.md').read_text() if (draft/'notes_frontmatter.md').exists() else '# Research notes — cote 29, scans 141–187\n\nWORKING INTEGRATION: post-freeze research notes; final editorial review in progress. The source fragments are frozen and unchanged.\n\n'
parts=[header]
for nid,title,body in sorted(entries,key=lambda e:tuple(map(int,e[0][1:].split('.')))):
    parts.append(f'## {nid} — {title}\n\n{body}\n')
for n in ['additional_crosslinks.md','standing_questions.md','sources.md']:
    if (draft/n).exists():parts.append((draft/n).read_text())
(root/'MPL_29_141-187_notes.md').write_text('\n'.join(parts))

queries={}
with (draft/'research_finite_context_search.tsv').open(newline='') as f:
    for row in csv.DictReader(f,delimiter='\t'):
        ids=['N149.1','N151.1'] if row['candidate_id']=='RF07' else [mapping[row['candidate_id']]]
        for nid in ids:queries[nid]=row['actual_rg_pattern']
for row in json.loads((draft/'infinite_coverings_context_searches.json').read_text()):
    queries[mapping[row['note_id']]]=row['query']
for n in ['root_context_queries.tsv','additional_context_queries.tsv']:
    if (draft/n).exists():
        with (draft/n).open(newline='') as f:
            for row in csv.DictReader(f,delimiter='\t'):queries[row['note_id']]=row['query']
with (root/'records/CONTEXT_QUERIES.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['note_id','query']);w.writerows(queries.items())

types={'refuted with refined ID':"refuted, with the refined statement's id",'carried as background':'carried as background without fault found','used and rechecked':'used and rechecked in this run'}
events=[]
for name in ['root_check_events.tsv','research_finite_events.tsv','infinite_coverings_check_events.tsv','additional_check_events.tsv']:
    if not (draft/name).exists():continue
    with (draft/name).open(newline='') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            row={k:remap(v) for k,v in row.items()}
            row['type']=types.get(row['type'],row['type'])
            events.append(row)
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(events)
print(f'Integrated {len(entries)} main notes, {len(queries)} queries, {len(events)} actual check events')
