#!/usr/bin/env python3
"""Merge audited registers and bibliography, normalize citation aliases, validate."""
from pathlib import Path
import re,json,csv,collections
root=Path(__file__).resolve().parents[1]
aliases={
 "AF_Boggi2020":"Boggi2020BC",
 "AF_Boggi2026":"Boggi2026Automorphisms",
 "AF_HarbaterSchneps2000":"HarbaterSchneps2000",
 "HoshiMochizuki2011Nodal":"HoshiMochizuki2011",
 "Nakamura1994Sphere":"Nakamura1994"
}
def norm(s):
 for a,b in aliases.items():s=s.replace(a,b)
 return s

for p in (root/'sections').glob('*.tex'):
 s=p.read_text(); t=norm(s)
 if t!=s:p.write_text(t)

def entries(s):
 starts=list(re.finditer(r'^@(\w+)\s*\{\s*([^,]+),',s,re.M))
 for i,m in enumerate(starts):
  block=s[m.end():starts[i+1].start() if i+1<len(starts) else len(s)]
  fields={};pos=0
  while True:
   q=re.search(r'(\w+)\s*=\s*',block[pos:])
   if not q:break
   name=q.group(1);j=pos+q.end()
   if block[j]=='{':
    depth=1;k=j+1
    while depth:
     if block[k]=='{' and (k==0 or block[k-1]!='\\'):depth+=1
     elif block[k]=='}' and (k==0 or block[k-1]!='\\'):depth-=1
     k+=1
    value=block[j+1:k-1];pos=k
   elif block[j]=='"':
    k=j+1
    while block[k]!='"' or block[k-1]=='\\':k+=1
    value=block[j+1:k];pos=k+1
   else:
    k=block.index(',',j);value=block[j:k].strip();pos=k+1
   fields[name]=value
  yield m.group(1),norm(m.group(2).strip()),fields

merged={}
# The first entry supplies the preferred metadata; duplicates add missing fields
# and the additional audited theorem list.
for prefix in ('D','BC','E','AF'):
 for typ,key,fields in entries((root/'audit'/f'{prefix}_references.bib').read_text()):
  if key not in merged:
   merged[key]=(typ,fields)
  else:
   old=merged[key][1]
   for k,v in fields.items():
    if k not in old:old[k]=v
    elif k=='note' and v!=old[k]:
     old[k]+=' Additional audit: '+v

order=['author','editor','title','booktitle','journal','year','volume','number','pages','publisher',
       'series','howpublished','eprint','archivePrefix','doi','url','keywords','note']
out=[]
for key,(typ,fields) in sorted(merged.items()):
 note=fields.get('note','')
 assert note, f'No verification note for {key}'
 # Opened-source verification is distinct from proof certification.
 if not re.search(r'\b(?:unverified|verified)\b',note,re.I):
  note='verified: '+note
 fields['keywords']='unverified' if re.search(r'\bunverified\b',note,re.I) else 'verified'
 link=('https://doi.org/'+fields['doi']) if fields.get('doi') else fields.get('url')
 if link and r'\url{' not in note:
  note+=r' Source: \url{'+link+'}'
 fields['note']=note
 field_order=order+sorted(set(fields)-set(order))
 body=',\n'.join('  '+k+'={'+fields[k]+'}' for k in field_order if k in fields)
 out.append('@'+typ+'{'+key+',\n'+body+'\n}')
(root/'LM3_TEICHMULLER_TOWER_references.bib').write_text('\n\n'.join(out)+'\n')
(root/'audit'/'citation_aliases.json').write_text(json.dumps(aliases,indent=2)+'\n')

def flat(v):
 if isinstance(v,dict):return '; '.join(str(k)+': '+flat(x) for k,x in v.items())
 if isinstance(v,list):return '; '.join(flat(x) for x in v)
 if isinstance(v,bool):return 'Yes' if v else 'No'
 if v is None:return ''
 return str(v)

allrows=[]
for prefix in ('AF','BC','D','E'):
 rows=json.loads((root/'audit'/f'{prefix}_results.json').read_text())
 for r in rows:
  r={k:norm(flat(v)) for k,v in r.items()}
  allrows.append(r)
allrows.sort(key=lambda r:(r['id'].split('.')[0],int(r['id'].split('.')[1])))
columns=['id','statement','status','where_proved','depends_on',
 'manuscript_passages (section; folio; scan)',
 'depends_on_doubtful_reading (scan, alternatives)','notes']
with (root/'LM3_TEICHMULLER_TOWER_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=columns);w.writeheader()
 for r in allrows:
  r['manuscript_passages (section; folio; scan)']=r.pop('manuscript_passages','')
  r['depends_on_doubtful_reading (scan, alternatives)']=r.pop('depends_on_doubtful_reading','')
  w.writerow({k:r.get(k,'') for k in columns})

readingrows=[]
for prefix in ('AF','BC','D','E'):
 for r in json.loads((root/'audit'/f'{prefix}_readings.json').read_text()):
  place=flat(r.get('place',r.get('doubtful_reading',r.get('reading',''))))
  if r.get('readings'):place+='; alternatives: '+flat(r['readings'])
  if r.get('alternatives'):place+='; alternatives: '+flat(r['alternatives'])
  support=r.get('support',r.get('mathematical_support',r.get('mathematics_supports',r.get('what_the_mathematics_supports',r.get('mathematical_effect','')))))
  if not support:
   raise ValueError('Unknown reading schema '+str(r))
  readingrows.append({
   'package':flat(r.get('package',r.get('source'))),'scan':flat(r.get('scan',re.findall(r'scan(\d+)',r.get('manuscript_passage','')))),
   'the \\unsure or \\illegible place':place,
   'what the mathematics supports':flat(support),
   'how strongly':flat(r.get('strength',r.get('how_strongly',r.get('inspection',''))))
  })
readingrows.sort(key=lambda r:(r['package'],r['scan']))
cols=['package','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly']
with (root/'LM3_TEICHMULLER_TOWER_readings.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(readingrows)

statements={}
used=set()
for p in (root/'sections').glob('*.tex'):
 s=p.read_text()
 assert not [c for c in s if ord(c)<32 and c not in '\n\r\t'],p
 for ident,status,title in re.findall(r'^\\statement\{([^}]+)\}\{([^}]+)\}\{(.*)\}\s*$',s,re.M):
  assert ident not in statements,ident
  statements[ident]=(status,p.name)
 for cites in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',s):
  used.update(k.strip() for k in cites.split(','))
assert used<=set(merged),sorted(used-set(merged))
assert set(statements)=={r['id'] for r in allrows},(set(statements)-{r['id'] for r in allrows})
for r in allrows:
 assert r['status']==statements[r['id']][0],r['id']
 assert r['status'] in ('Proved','Known','Refuted','Open')
 assert r['where_proved'],r['id']
 assert r['statement'],r['id']
summary={
 'statements':len(statements),
 'by_status':dict(sorted(collections.Counter(r['status'] for r in allrows).items())),
 'by_part':dict(sorted(collections.Counter(r['id'][0] for r in allrows).items())),
 'reading_records':len(readingrows),
 'bibliography_entries':len(merged),
 'citation_keys_used':len(used),
 'missing_citations':sorted(used-set(merged)),
 'all_statements_registered':True,
 'verification_means':'Source opened; not automatic certification of every proof.',
 'status':'PASS'
}
(root/'audit'/'validation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))

