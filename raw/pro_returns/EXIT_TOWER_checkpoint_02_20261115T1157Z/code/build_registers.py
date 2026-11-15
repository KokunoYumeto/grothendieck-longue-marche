#!/usr/bin/env python3
"""Assemble the exact statement, reading and bibliography registers.

Metadata is kept beside each contributor's working record. The statement
column contains the complete TeX statement, preserving its quantifiers and
maps rather than replacing it by a title.
"""
from pathlib import Path
import csv,json,re

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','statement','status','where_proved','depends_on',
        'manuscript_passages','depends_on_doubtful_reading','notes']
def brace(s,i):
    assert s[i]=='{'
    depth=1;j=i+1
    while depth:
        if s[j]=='{' and s[j-1]!='\\':depth+=1
        if s[j]=='}' and s[j-1]!='\\':depth-=1
        j+=1
    return s[i+1:j-1],j
def statements():
    for p in sorted((ROOT/'sections').glob('*.tex')):
        s=p.read_text()
        for m in re.finditer(r'\\begin\{result\}',s):
            vals=[];i=m.end()
            for _ in range(3):
                while s[i].isspace():i+=1
                v,i=brace(s,i);vals.append(v)
            end=s.index('\\end{result}',i)
            yield vals[0],vals[1],vals[2],s[i:end].strip(),str(p.relative_to(ROOT))
def key(k):
    m=re.fullmatch(r'([A-Z]+)\.(\d+)(.*)',k)
    return (m[1],int(m[2]),m[3]) if m else (k,0,'')
def texescape(s):
    d={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$',
       '#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}',
       '^':r'\textasciicircum{}'}
    return ''.join(d.get(c,c) for c in str(s))
metadata={}
for p in sorted((ROOT/'agents').glob('*_results.json')):
    for row in json.loads(p.read_text()):
        if row['id'] in metadata:raise ValueError('Duplicate metadata '+row['id'])
        metadata[row['id']]=row
rows=[];seen=set();contexts=[];missing=[]
for ident,status,title,body,p in statements():
    if ident in seen:raise ValueError('Duplicate result '+ident)
    seen.add(ident)
    row={x:'' for x in FIELDS};row.update(metadata.get(ident,{}))
    row.update(id=ident,statement=title+'\n'+body,
               status=status.split(';')[0].split(',')[0],where_proved=p)
    if ident not in metadata:missing.append(ident)
    rows.append({x:row[x] for x in FIELDS})
    passage=row['manuscript_passages']
    if passage:
        contexts.append('\\expandafter\\def\\csname ResultContext@'+ident+
                        '\\endcsname{'+texescape(passage)+'}')
rows.sort(key=lambda r:key(r['id']))
with (ROOT/'EXIT_TOWER_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
(ROOT/'sections/result_contexts.tex').write_text('\n'.join(contexts)+'\n')
readings=[]
for p in sorted((ROOT/'agents').glob('*_readings.json')):
    readings.extend(json.loads(p.read_text()))
RFIELDS=['package','scan','the \\unsure or \\illegible place',
         'what the mathematics supports','how strongly']
aliases={'place':'the \\unsure or \\illegible place',
         'supports':'what the mathematics supports','strength':'how strongly',
         'doubtful_place':'the \\unsure or \\illegible place',
         'mathematical_support':'what the mathematics supports',
         'the_unsure_or_illegible_place':'the \\unsure or \\illegible place',
         'what_the_mathematics_supports':'what the mathematics supports',
         'how_strongly':'how strongly'}
with (ROOT/'EXIT_TOWER_readings.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=RFIELDS);w.writeheader()
    for row in readings:
        mapped={aliases.get(k,k):v for k,v in row.items()}
        if any(not mapped.get(k) for k in RFIELDS):
            raise ValueError('Incomplete reading row: '+str(row))
        w.writerow({k:mapped.get(k,'') for k in RFIELDS})
bib=[];bibkeys=set()
for p in sorted((ROOT/'agents').glob('*_references.bib')):
    s=p.read_text()
    for m in re.finditer(r'@\w+\s*\{\s*([^,]+),',s):
        if m[1] in bibkeys:raise ValueError('Duplicate bib key '+m[1])
        bibkeys.add(m[1])
    bib.append(s)
(ROOT/'EXIT_TOWER_references.bib').write_text('\n\n'.join(bib))
out={'statements':len(rows),'status_counts':{s:sum(r['status']==s for r in rows)
       for s in sorted({r['status'] for r in rows})},
     'readings':len(readings),'references':len(bibkeys),
     'missing_metadata':missing,'unused_metadata':sorted(set(metadata)-seen)}
(ROOT/'code/register_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
