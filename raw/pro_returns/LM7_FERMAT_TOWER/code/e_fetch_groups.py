"""Retrieve primary GroupNames permutation-generator data, orders <=24.

The retrieved executable-looking GAP strings are parsed as permutations only;
they are never executed. The computation program uses the resulting JSON.
"""
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import re,json,html,hashlib

BASE=Path(__file__).resolve().parents[1]
SRC=BASE/'sources'
URL='https://www.people.maths.bris.ac.uk/~matyd/GroupNames/'
index=(SRC/'groupnames_index.html').read_text()
groups=[]
for row in re.findall(r'<tr>(.*?)</tr>',index,re.S):
    cells=re.findall(r'<td[^>]*>(.*?)</td>',row,re.S)
    if len(cells)!=6:continue
    m=re.fullmatch(r'(\d+),(\d+)',cells[-1].strip())
    if not m or int(m[1])>24:continue
    href=re.search(r'href="([^"]+)"',cells[0])[1]
    label=html.unescape(re.sub(r'<[^>]+>','',cells[-2]))
    groups.append({'order':int(m[1]),'id':int(m[2]),'name':label,'url':URL+href})

def fetch(g):
    name=f"groupnames_{g['order']}_{g['id']}.html"
    p=SRC/name
    if not p.exists():
        with urlopen(g['url'],timeout=35) as r:p.write_bytes(r.read())
    text=p.read_text()
    clean=html.unescape(re.sub(r'<[^>]+>','',text))
    m=re.search(r'G\s*:=\s*Group\s*\((.*?)\)\s*;',clean,re.S)
    if not m:
        if g['order']==1:raw='()'
        else:raise RuntimeError('Missing GAP generator string: '+g['name'])
    else:raw=m[1].strip()
    # Each generator is a concatenation of cycles, separated by a comma
    # outside parentheses. Extract it with a parenthesis-level parser.
    gens=[];piece='';level=0
    for ch in raw+',':
        if ch=='(':level+=1
        if ch==')':level-=1
        if ch==',' and level==0:
            if piece.strip():gens.append(piece.strip())
            piece=''
        else:piece+=ch
    cycles=[]
    for gen in gens:
        if re.sub(r'[\d\s(),]','',gen):raise RuntimeError('Unexpected data syntax '+gen)
        cycles.append([[int(x) for x in c.split(',') if x.strip()] for c in re.findall(r'\(([^()]*)\)',gen)])
    return {**g,'cycles':cycles,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

with ThreadPoolExecutor(max_workers=8) as pool:
    data=list(pool.map(fetch,groups))
data.sort(key=lambda x:(x['order'],x['id']))
(BASE/'code/e_group_input.json').write_text(json.dumps(data,indent=2)+'\n')
for g in data:print(g['order'],g['id'],g['name'],g['cycles'])
print('Retrieved',len(data),'group models; generator strings parsed without execution.')
