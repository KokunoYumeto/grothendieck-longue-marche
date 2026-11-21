from pathlib import Path
import json,re
r=Path(__file__).parent
s=(r/'reading.tex').read_text()
j=json.loads((r/'report.json').read_text())
t=re.sub(r'(?<!\\)%.*','',s)
balance=0
for i,ch in enumerate(t):
    if ch in '{}':
        n=0;k=i-1
        while k>=0 and t[k]=='\\':n+=1;k-=1
        if n%2:continue
        balance+=1 if ch=='{' else -1
        assert balance>=0,('early brace',i)
assert balance==0,balance
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
    op,env=m.groups()
    if op=='begin':stack.append(env)
    else:assert stack and stack.pop()==env,('environment',m.group())
assert not stack,stack
assert t.count(r'\[')==t.count(r'\]')
assert t.count('$')%2==0
assert r'\cotefile' not in t
assert r'\scanpage{11}' in t
assert '\\newcommand' not in t and '\\renewcommand' not in t
required={'id','location','C','H','reading','evidence','confidence','kind','diff_C','diff_H','C_doubt_status','readers_crop','bbox'}
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
ids=set(); rows=set()
for x in j['differences']:
    assert required<=x.keys(),x['id']
    assert x['id'] not in ids,x['id'];ids.add(x['id'])
    assert x['kind'] in kinds,(x['id'],x['kind'])
    assert x['confidence'] in {'high','medium','low'}
    assert x['C_doubt_status'] in {None,'resolved','retained'}
    if x['C_doubt_status']=='resolved':assert x['diff_C'],x['id']
    if x.get('C_source_doubt_row'):rows.add(x['C_source_doubt_row'])
    if x['readers_crop']:assert (r/x['readers_crop']).is_file(),x['readers_crop']
assert rows==set(range(1,16)),rows
for x in j['inventory']:
    assert x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
    assert x['transcribed']=='yes'
for x in j['crops']:assert (r/x['path']).is_file()
assert len(j['crops'])==16
for x in j['doubts']:assert (r/x['crop']).is_file()
checks=[
(r'\mathbb P(X)', 'resolved upper-left double P'),
(r'\deleted{\unsure{e|\mathcal E}}Z','top predecessor candidate order'),
(r'\operatorname{Hom}(X,\underline{\operatorname{Hom}}(\mathscr E,Z)','right arguments and single close'),
(r'P(\operatorname{Hom}(X,Z)','middle single close and plain Hom'),
(r'U\times_{\unsure{Y|V}}U','diagram subscript order'),
(r'\unsure{H|U}','arrow-side candidate order'),
(r'\unsure{V|W}','lower diagram retained doubt'),
(r'\draw (11,365) -- (9,565) (15,416) -- (25,551);','two unequal left rules'),
(r'\draw[line width=1.4pt] (85,159) -- (111,337);','upper drawing thick segment boundary'),
]
for needle,label in checks:assert needle in s,label
assert not re.search(r'\\rlap\{\\operatorname',s),'unboxed math operator in rlap'
print('PASS: braces, environment nesting, display pairs, even dollar count, no new macros/cote, report schema and kinds, unique IDs, all 15 source doubt rows, 16 crop paths, local reading/report assertions.')
print('Difference records:',len(j['differences']),'C flagged:',sum(x['diff_C'] for x in j['differences']),'H flagged:',sum(x['diff_H'] for x in j['differences']))
print('Original source doubt rows:',sorted(rows))
print('Current TeX macro names:',', '.join(sorted(set(re.findall(r'\\([A-Za-z]+)',t)))))
print('CURRENT READING.TEX\n'+s)
